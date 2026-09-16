#!/usr/bin/env python3
"""Build data/drafts/heat_draft.json: proposed rewrites of the Heat train captions.

Rules applied
  person     - a human who is only narrator/actor is removed (state description or passive voice);
               where the body IS the physics (hand as heat source, breath) only a minimal
               "a hand" / "breath" stays.  keep_person = the person is the phenomenon (steaming runners).
  timescale  - minute/hour-scale processes written as a completed action are rephrased as an
               in-progress state or a result state that a 5 s clip can show.
  expectation- expectations that demanded completion or a long-run outcome now require only the
               direction of change (process_direction), never the amount.
Every record keeps id / category / subcategory / violation_types; old_caption / old_expectation
are kept for side-by-side review; `change` lists which rules touched the record.
"""
import json
from pathlib import Path

SRC = Path("/u/hchen56/phyRubric/data/train/heat.json")
DST = Path("/u/hchen56/phyRubric/data/drafts/heat_draft.json")

# ids the user decided to drop (no seconds-scale phenomenon); kept in the draft with change=["delete"] so ids stay
# stable during review, removed (and Heat renumbered) only when the reviewed draft is accepted into heat.json.
DELETE = {"HEAT-0013": "snow on a warm hood melts over minutes", "HEAT-0015": "ice cream on a warm brownie: minutes",
          "HEAT-0022": "carton gone soft: result of a long wait, nothing happens on screen",
          "HEAT-0023": "sorbet slumping off a spoon: minutes, and duplicates the ice-cream melts",
          "HEAT-0024": "butter on a baked potato: slow and duplicates the butter melts",
          "HEAT-0036": "frozen soap bubble: needs -10 C or colder and a counter-intuitive outcome; not everyday commonsense"}

# id -> (caption or None, expectation or None, [changes], note)
O: dict[str, tuple] = {}
def o(i, c=None, e=None, ch=(), note=""):
    O[f"HEAT-{i:04d}"] = (c, e, list(ch), note)

# ---------------------------------------------------------------- melt_freeze
o(1, "An ice cream cone stands in a holder on a sunny picnic table, and the ice cream is melting and dripping down the side of the cone.",
     "The ice cream sags and drips run downward and pool at the base; the visible change may be small, but it never firms back up or drips upward.",
     ["person", "timescale", "expectation"], "child was narrative only; melting is minutes-scale so shown in progress")
o(2, "Hot water is poured from a kettle over a large block of ice on the ground, and the ice melts where the water hits it.",
     "The surface turns wet and glossy and hollows where the hot water lands, meltwater runs down the block and pools on the ground, and faint steam may rise; the block may crack from the heat but does not grow, vanish all at once, or refreeze.",
     ["person", "timescale", "expectation"], "user's variant: hot water on ice is a fast, visible process; pouring is the only human action and stays passive")
o(3, "A pat of cold butter is dropped into a hot frying pan, and it melts into a spreading pool of liquid.", None, ["person"])
o(4, "A pat of butter on a small plate is heated in a microwave and slowly melts.",
     "The pat softens from the edges and bottom, slumps lower, and a glossy pool spreads outward on the plate as the pat shrinks; the butter does not stay a sharp-edged block, grow, vanish, or re-solidify while the microwave runs.",
     ["person", "timescale", "expectation"], "user's variant: butter melting in a microwave; no human, melting shown in progress")
o(5, "A bowl full of chocolate pieces sits in a pan of steaming hot water and is stirred with a spatula, and the chocolate slowly melts.",
     "The pieces soften and lose their sharp edges from the outside in, move only where the spatula pushes them, and merge into a smooth glossy liquid as the stirring smears melted streaks together; the chocolate does not stay snap-hard, break back into separate pieces, or re-harden while the water steams.",
     ["person", "timescale", "expectation"], "user's variant, written as a bain-marie (bowl in hot water) rather than water poured onto the chocolate, which would make it seize into a grainy paste; stirring with a spatula added at the user's request, in passive voice")
o(6, "A glowing red-hot metal ball is set on top of a large block of ice, and the ice melts around it.",
     "The ice hisses and steams where the ball touches it, meltwater collects at the contact and the ball settles into a growing hollow; the ball's glow dims as it cools and the ice may crack; the ice does not stay untouched, the ball does not glow brighter or float free of the surface, and nothing refreezes while the ball is hot.",
     ["person", "timescale", "expectation"], "user's variant (viral red-hot-ball-on-ice clip); temperature written as 'glowing red-hot', not a number, per the no-numerals caption rule")
o(7, "A glass of lemonade with ice cubes sits on a table in the sun, and the ice is melting.",
     "The cubes are smaller and rounder than fresh ice and keep shrinking while floating; they do not grow, multiply, or sink, and the lemonade does not overflow.",
     ["timescale", "expectation"], "'until they are gone' needs 30+ min")
o(8, "A fruit popsicle is held upright on its stick in the summer heat, and it drips down the stick onto the hand.",
     "Drips run downward along the stick; the popsicle gets thinner and softer and may slide on the stick; it does not refreeze or drip upward.",
     ["person"], "hand kept as drip target")
o(9, None, "Water gathers at each tip and drops fall straight down; the icicles do not grow while dripping, and any change in length is a shortening.",
     ["expectation"], "shortening is not visible in 5 s")
o(10, "An ice cube is dropped into a mug of hot tea, and it melts quickly.",
      "The cube floats, its edges round off and it shrinks steadily while faint steam rises from the tea; the tea level may rise slightly as it goes in; the cube does not grow, sink like a stone, vanish in a single frame, or stay sharp-cornered in hot liquid.",
      ["person", "timescale", "expectation"], "user's choice from candidates: replaces a near-duplicate of HEAT-0018/0047 (cheese on hot food) with a liquid heat source and a seconds-scale melt")
o(11, "A candle burns on a dinner table, and melted wax spills over the rim and runs down one side.",
      "The pool sits at the top near the flame; the overflow runs downward and slows as it cools; the candle does not get taller and wax does not flow upward.",
      ["timescale", "expectation"], "pool forming is minutes-scale; the overflow itself is seconds")
o(12, "A marshmallow on a stick is held over a campfire, and it softens and sags.",
      "The side facing the fire puffs and goes glossy first, then the marshmallow slumps and droops under its own weight, more on the fire side; the surface may brown, blacken in spots, or even catch if close to the flame, and any such darkening deepens and never fades back to white; it does not firm up again while over the heat.",
      ["person", "expectation"], "stick-holder minimised; browning/charring allowed as an irreversible side effect on the fire side but not required")
o(14, None,
      "Each stone is smaller and wetter than when it fell and has a dark wet ring around it that spreads; stones do not grow, reappear, or stay bone-dry.",
      ["expectation"], "user kept the original caption; only the expectation no longer requires the stones to finish melting")
o(16, "Snowflakes land on the dark sleeve of a warm coat during a snowfall and melt into tiny drops.",
      "Each flake turns into a small water bead within moments of landing and the beads merge or soak into the fabric; flakes do not accumulate as dry snow on the warm sleeve.",
      ["person"])
o(17, "An ice cube is flicked onto a hot skillet, and it skitters around and shrinks as it melts.",
      "The cube glides and spins on the hot surface with hissing steam, shrinking all the while; it does not sit still, grow, or stay the same size.",
      ["person", "timescale"], "'until it is gone' dropped")
o(19, "A cube of cold butter is dropped into a bowl of hot soup, and the butter melts and spreads across the surface.", None, ["person"])
o(20, "A chocolate-coated ice cream bar is held in the sun, and the chocolate coating softens and smears on the fingers.",
      "The coating loses its stiffness and streaks where touched; it does not stay brittle in the sun or re-harden on warm fingers.",
      ["person"], "fingers kept: they are the warm contact")
o(21, "A dog has just come in from the snow with clumps of snow on its fur, and the snow is melting and dripping onto the floor.",
      "The clumps look wet and shrink or slide off, drops fall downward, and a wet patch forms on the floor; the snow does not stay white and fluffy indoors or grow.",
      ["timescale", "expectation"])
o(23, "A spoonful of frozen sorbet is held over a bowl, and it slumps and drips off the spoon.", None, ["person"])
o(25, "A small snowball sits on a plate indoors and is melting into a puddle.",
      "The snowball sags and shrinks as the puddle grows; the snow does not re-form or stay dry, and the puddle does not shrink.",
      ["person", "timescale", "expectation"], "collapse to a puddle takes many minutes")
o(27, "Warm chocolate sauce is poured over a scoop of ice cream, and the sauce firms into a crackly shell on the cold surface.", None, ["person"])
o(28, "A bead of hot glue is squeezed from a glue gun onto a piece of wood, a button is pressed into it, and the glue sets hard around the button.", None, ["person"])
o(29, "Boiling sugar syrup is drizzled from a spoon into a bowl of ice water, and the syrup hardens instantly into brittle golden threads.", None, ["person"])
o(30, "Melted sealing wax is dripped onto the flap of an envelope and a stamp is pressed into it, and the wax hardens with the stamp's design.", None, ["person"])
o(32, "A hairdryer is aimed at crayons taped to the top of a canvas, and the crayons melt and run down the canvas in coloured streaks that harden lower down.", None, ["person"])
o(33, "Hot caramel is poured onto a cold marble slab, and the caramel spreads, then stiffens into a glassy sheet.", None, ["person"])
o(34, "Melted butter is poured onto a plate that has just come out of the freezer, and the butter turns cloudy and firm on the plate.", None, ["person"])
o(35, "On a bitterly cold winter morning a cup of water is splashed onto a frozen car windshield, and the water freezes into a film of ice on the glass.", None, ["person"])
o(36, "On a bitterly cold winter day a soap bubble is blown outdoors and caught on the wand, and the bubble turns frosty and stiff.", None, ["person"])
o(37, "Melted chocolate is piped in lines onto a sheet of parchment on a chilled tray, and the lines set firm and matte.", None, ["person"])
o(38, "A fingertip is dipped into the warm wax pool of a candle and pulled out, and the wax on the finger cools into a thin hard cap.", None, ["person"], "finger is the cold surface")
o(39, "Hot bacon fat is poured into a glass jar straight from the fridge, and the fat begins to set where it touches the cold glass.",
      "Solid white forms first at the cold glass walls and creeps inward; the fat stops sloshing as it sets; it does not turn clear again.",
      ["person", "timescale"], "room-temperature setting takes minutes; a cold jar makes it seconds")
o(42, "A bag of frozen peas is emptied into a pot of hot water, and the frost on them vanishes and the clumps break apart.", None, ["person"])
o(43, "A crayon lying on the dashboard of a car parked in the sun has softened and slumped over.",
      "The crayon is bent toward the dashboard where it softened and may sag a little further; it does not straighten while still warm.",
      ["timescale", "expectation"], "softening takes tens of minutes; shown as result state")
o(44, "A block of frozen orange juice is dropped into a jug of water and stirred, and it starts to melt into the water.",
      "The block rounds off, gets smaller, and sheds pieces while the water turns orange; it does not stay the same size, grow, or clear the water.",
      ["timescale", "expectation"], "'until it is gone' dropped")
o(46, "Chocolate coins left in a jacket pocket on a warm day have softened, and when unwrapped the foil comes away smeared and the coin bends.", None, ["person"])
o(47, "A block of hard cheese is held near a hot grill, and the near face softens and begins to sag and drip.", None, ["person"])
o(48, "An ice cube sits on a sun-warmed metal plate on a balcony and is melting.",
      "The puddle grows as the cube shrinks and rounds off; nothing refreezes on the warm plate and the cube does not grow.",
      ["timescale", "expectation"], "full melt takes minutes")
o(49, "Frost is scraped off a car windshield with a card while the heater runs inside, and the remaining frost turns to water and runs down the glass.", None, ["person"])
o(50, "Hot melted chocolate is spooned onto a cold metal bowl turned upside down, and it stiffens where it lands, leaving a fixed drip pattern.", None, ["person"])

# ---------------------------------------------------------------- boil_steam
o(51, "A kettle on a stove is at the boil, steam pours from the spout, and the lid rattles.", None, ["timescale"], "'comes to the boil' takes minutes")
o(54, "The lid is lifted off a rice cooker, and a cloud of steam billows up out of it.", None, ["person"])
o(55, "A steam wand is pushed into a jug of milk, and the milk hisses, swirls, and rises in the jug as foam.", None, ["person"])
o(61, "A hot shower has just been turned off, and the bathroom is filled with steam drifting up toward the ceiling.", None, ["person"])
o(62, "A steam iron is pressed onto a shirt on an ironing board, and puffs of steam rise from around the iron.", None, ["person"])
o(64, "Boiling water is poured from a kettle into a mug, and steam rises from the mug as it fills.", None, ["person"])
o(67, "A pot of water hangs over a campfire on a tripod, boiling, with steam rising into the evening air.", None, ["timescale"])
o(69, "Water is ladled onto the hot stones of a sauna, and a burst of steam rises off the stones with a hiss.", None, ["person"])
o(70, "The lid of a large pot of dumplings is lifted at a street stall, and steam rolls up out of the pot into the cold air.", None, ["person"])
o(74, "A pan of water on a stove is at a boil, and the burner is turned off; the bubbling dies down and only faint steam remains.", None, ["person"])
o(77, "Steam rises from the surface of a hot spring on a cold morning.", None, ["person"], "bathers were scenery")
o(78, "A wet towel is laid over a hot radiator, and steam rises from the towel where it touches the hot metal.",
      "Wisps rise from the towel, strongest where it touches the radiator; the towel does not get wetter; steam does not flow downward.",
      ["timescale", "expectation"], "drying is not visible in 5 s")
o(79, "Wet spinach is tossed into a very hot pan, and a burst of steam rises with a loud hiss as the leaves wilt.", None, ["person"])
o(81, "Water is poured onto the hot coals of a barbecue after cooking, and a hissing cloud of steam rises from the grill.", None, ["person"])
o(82, "The door of a hot oven is opened, and a wave of hot air and steam rushes up and out of the opening.",
      "The visible steam and shimmer go upward out of the opening; nothing pours down onto the floor.", ["person"])
o(83, "A live lobster is dropped into a pot of boiling water, and the water surges and steam rises as the level jumps.", None, ["person"])
o(85, "Hot tar is spread from a bucket across a roof, and steam and fumes rise off the fresh tar.", None, ["person"])
o(88, None, None, ["keep_person"], "the runners' bodies are the steam source")
o(91, "A glowing piece of metal is plunged into a bucket of water, and a cloud of steam bursts up from the bucket.", None, ["person"])
o(92, "A ladle of hot broth is poured over cold noodles in a bowl, and a puff of steam rises from the bowl.", None, ["person"])
o(94, "Boiling water is poured over a tea bag in a glass, and steam rises while the colour spreads from the bag.", None, ["person"])
o(97, "A lid is lifted from a pan of steamed vegetables, and steam rises to fog the range hood above.", None, ["person"])
o(100, "Frozen french fries are dropped into a pot of hot oil, and the oil erupts in bubbles and steam.", None, ["person"])

# ---------------------------------------------------------------- condensation
o(101, "A cold bottle of soda has just been taken out of the fridge on a hot day, and beads of water form on the outside of the bottle.", None, ["person"])
o(102, "Breath is blown onto a cold window pane, and a patch of fog appears on the glass and then fades.", None, ["person"], "breath is the moisture source; minimal")
o(103, "A hot shower has just run in a closed bathroom, and the mirror is fogged over so that reflections are a blur.",
       "The fog is even across the glass and clears slowly, or clears in a streak if wiped; it does not vanish all at once.", ["person"])
o(104, "A pair of glasses is brought in from the cold street into a warm café, and the lenses fog over.",
       "The fog appears on the lenses within a moment of entering and does not appear while they are still outside; any later change is toward clearing.", ["person", "expectation"])
o(105, "A glass of ice water sits on a wooden table in a warm room, and condensation runs down the outside of the glass onto the table.",
       "Droplets on the outside run down and feed the ring; the ring does not shrink while the glass stays cold; the water does not come from inside the glass.",
       ["timescale", "expectation"], "a ring takes minutes to form; shown as in progress")
o(106, "Breath is blown onto the shiny back of a cold metal spoon, and the spoon fogs and then clears.", None, ["person"])
o(107, "A hot shower runs with the bathroom door closed, and the bathroom window is misting over from the bottom up.",
       "The mist thickens while the shower runs and heavier drops run downward in streaks; the glass does not clear while the shower runs.", ["person", "timescale"])
o(108, None, None, ["keep_person"], "the passengers' breath is the moisture source")
o(109, "A chest freezer is opened, and a low mist rolls out over the rim and sinks toward the floor.", None, ["person"])
o(110, "The lid of a pot that has been simmering is lifted and turned over, and its underside is covered in drops that run and drip off.", None, ["person"])
o(111, None, None, ["keep_person"], "breath cloud needs a breather")
o(117, "A camera is carried from an air-conditioned lobby out into humid summer heat, and its lens fogs up.", None, ["person"])
o(118, None, None, ["keep_person"], "breath inside the visor")
o(121, "A cold bottle of white wine stands in a bucket of ice on a restaurant table, and the bottle neck above the ice is beaded with water.", None, ["timescale"])
o(123, "A pair of sunglasses left in a cold car is carried into a warm shop, and the lenses cloud over.",
       "The clouding appears within moments indoors and does not appear while still in the cold car; any later change is toward clearing.", ["person", "expectation"])
o(126, "A hot dishwasher is opened and the steam that escapes fogs the cool kitchen window above the sink.", None, ["person"])
o(127, "A pair of glasses is brought in from a cold morning ride, and the lenses fog over in the warm office.",
       "The lenses cloud over shortly after coming indoors; any change afterwards is toward clearing, never thicker fog on warming lenses.",
       ["person", "timescale", "expectation"], "fog-then-clear cycle takes minutes")
o(130, "A cold hand presses against a warm window from inside, and when it lifts away a foggy handprint is left on the glass.", None, ["person"], "hand is the cold object")
o(131, None, None, ["keep_person"], "breath in the scarf")
o(136, "A hot mug of cocoa steams on a windowsill on a cold day, and the steam fogs the window beside it.",
       "The window fogs where the rising steam meets it and the patch grows while the mug steams; it does not fog away from the steam.", ["person", "expectation"])
o(137, None, None, ["keep_person"], "goggles fog from the swimmer's face")
o(138, "A frozen chocolate bar is taken out of the freezer, and a white frost forms on the wrapper within moments.", None, ["person"])
o(140, "A warm oven door is opened to check bread, and the glasses of the cook leaning in fog over from the escaping steam.",
       "The lenses fog as the steam hits them and start to clear once away from the steam.", ["person"], "person minimised; glasses need a wearer to be in the steam")
o(143, "A pair of glasses is carried into a steam room, and the lenses cloud over completely within seconds.",
       "The lenses go white and opaque almost at once and stay fogged while in the steam.", ["person"])
o(144, "A cold glass of iced coffee stands on a humid balcony railing, and water drips from its base onto the railing.", None, ["person"])
o(145, "A proofing cabinet full of warm moist air is opened, and the cool glass of the door immediately fogs on the inside.", None, ["person"])
o(148, "Breath is blown onto a cold hand mirror, and the fog on the glass hides the reflection for a moment before it clears.",
       "The fog appears with the breath, blurs the reflection, and clears from the edges within seconds; the reflection returns unchanged.", ["person"])
o(149, "A cold metal railing on a humid summer morning is covered in fine droplets, and a finger drags through them leaving a clear line.",
       "The line stays clear where the finger passed while the surrounding droplets remain; the droplets do not vanish from the untouched area.",
       ["person", "expectation"], "re-fogging takes minutes")
o(150, "A tray of ice cubes is taken from the freezer, and the cubes and tray frost over white.",
       "The white frost appears first on the coldest surfaces; any later change is toward wetness as the tray warms, and the frost does not vanish and return.",
       ["timescale", "expectation"])

# ---------------------------------------------------------------- burn_smoke
o(151, "A sheet of newspaper is held to a campfire flame, and the paper catches, curls, blackens, and falls apart into ash.", None, ["person"])
o(152, "A candle on a table is blown out, and a thin trail of smoke rises from the wick.",
       "The flame leans away from the puff of breath and goes out during it; the smoke rises straight up and drifts; the candle does not relight on its own.", ["person"])
o(153, "A match is struck against the side of its box, and it flares into a flame that settles to a steady burn.", None, ["person"])
o(154, "A lit match is touched to a candle wick, and the wick catches and holds a small flame.", None, ["person"])
o(155, "A dry log is tossed onto a campfire, and a burst of sparks flies up into the night.", None, ["person"])
o(157, None, "The smoke rises in a thin steady stream that wavers and spreads higher up; the tip glows red; the stick does not lengthen and the smoke does not sink.",
       ["expectation"], "shortening not visible in 5 s")
o(158, "The candles on a birthday cake are blown out, and all the little flames go out and leave rising wisps of smoke.",
       "The flames lean away from the puff of breath before they die; each wick sends up a wisp of smoke; no candle relights on its own.", ["person"])
o(159, "A long barbecue lighter is clicked, and a small flame appears at its tip and burns steadily.", None, ["person"])
o(160, "The glowing embers in a fireplace are poked with a poker, and they brighten and send up a swirl of sparks.", None, ["person"])
o(161, "The knob on a gas stove is turned, and a ring of blue flames lights around the burner.", None, ["person"])
o(162, "A metal snuffer is lowered over a candle flame, and the flame dies and smoke curls out from under the snuffer.", None, ["person"])
o(163, "A bucket of water is poured over a dying campfire, and the fire goes out with a hiss in a cloud of steam and smoke.", None, ["person"])
o(164, "A lit sparkler is held at arm's length, and it throws off a spray of bright sparks that fade as they fall.",
       "Sparks fly outward and downward from the burning point, going dark within a hand's length; the burning point moves down the wire, never back up.", ["person", "expectation"])
o(165, "A marshmallow on a stick catches fire over a campfire and is blown out, leaving it blackened.", None, ["person"])
o(166, "A kerosene lamp is lit with a match, and the wick catches and the flame steadies inside the glass chimney.", None, ["person"])
o(167, "A match is set to a pile of dry leaves, and the fire spreads across the pile with smoke rising from it.", None, ["person"])
o(168, "A charcoal chimney starter is lit, and flames and smoke rise up through the coals from the paper burning below.",
       "The fire climbs upward through the chimney and smoke pours out of the top; the flames do not start at the top.", ["person", "expectation"], "coals glowing takes minutes")
o(169, "The last embers of a campfire are dying down under grey ash.",
       "The glow stays dim or fades and only faint smoke rises; the embers do not brighten or flame up without being disturbed or fed.",
       ["timescale", "expectation"], "orange-to-grey fade takes many minutes")
o(170, "A hand waves over a candle that has just been blown out, and the rising smoke swirls and scatters.", None, ["person"], "hand is the air source")
o(171, "A fatty burger is flipped on a grill, and fat drips onto the coals and a flame flares up under the patty.", None, ["person"])
o(172, "Air is blown gently onto the embers of a fire, and they glow brighter and a small flame springs up.",
       "The embers brighten while the air blows and the flame appears at the brightest spot; the glow eases when the blowing stops.", ["person"])
o(173, "A lid is slid over a small grease fire in a pan, and the flames go out.", None, ["person"])
o(175, "A candle flame flickers as a draft passes the table, then steadies again.", None, ["person"])
o(177, "A blowtorch heats a copper pipe, and the flame roars out of the nozzle in a blue cone.", None, ["person"])
o(178, "A stove-top burner is lit under a wok, and the flames spread around the burner ring and lick up its sides.", None, ["person"])
o(179, "A hose sprays water onto a burning shed, and the flames shrink and the smoke turns from black to white steam.", None, ["person"])
o(180, "A cigarette lighter is snapped shut, and its flame vanishes at once.", None, ["person"])
o(181, "A lit sparkler is dropped into a bucket of water, and it goes out with a hiss and a puff of steam.", None, ["person"])
o(183, "A burning twig is held upright, and the flame climbs along it toward the hand until it is dropped.", None, ["person"], "hand is the flame's target")
o(184, "A row of tea-light candles is lit one after another with a long match, and each flame stands upright after it catches.", None, ["person"])
o(185, "Dry grass beside a footpath catches from a dropped cigarette, and the small fire is stamped out with a boot.", None, ["person"])
o(186, "Brandy is ignited in a pan, and a sheet of flame rises above the pan and then dies down.", None, ["person"])
o(187, "A magnifying glass focuses sunlight onto a dry leaf until a wisp of smoke appears and a small glowing spot begins to spread.", None, ["person"])
o(189, "A wooden match burns down toward the fingers holding it and is dropped into an ashtray just before it reaches them.", None, ["person"], "fingers are what the flame approaches")
o(190, "A wooden skewer is dropped into the grill's coals and catches fire.",
       "The skewer lights where it touches the coals, the flame runs along it, and it blackens and shrinks behind the flame; it does not return to pale wood.",
       ["person", "timescale"], "'burns to a black stick' takes longer than 5 s")
o(191, "A paper lantern's candle is lit, and the lantern glows from inside as the flame steadies.", None, ["person"])
o(193, "A handful of dry pine needles is fed to a small fire, and they crackle and flare up brightly before the flames settle.", None, ["person"])
o(194, "The pilot on a water heater is lit with a long lighter, and a small steady blue flame appears and stays lit.", None, ["person"])
o(195, "A candle inside a glass jar has burned down to its last pool of wax, and the flame goes out.",
       "The flame is small, dies, and smoke rises from the wick; the wax does not refill and the flame does not return.", ["timescale", "expectation"])
o(197, "A lit match is dropped into a fire pit filled with kindling, and the fire catches and grows from the bottom up.", None, ["person"])
o(199, "A fire steel is scraped with a knife, and sparks shower onto a nest of dry tinder that begins to smoke and then flame.", None, ["person"])
o(200, "A candle is snuffed by pinching the wick between wet fingers, and the flame goes out with a faint hiss and a wisp of smoke.", None, ["person"], "fingers do the snuffing")

# ---------------------------------------------------------------- heat_response
o(201, "Frozen dumplings are dropped into a pot of boiling water; they sink at first, and the ones that have cooked bob back up to the surface.",
       "The dumplings sink on entry; any that rise do so one by one and stay bobbing at the surface; none floats the instant it enters or sinks again once up.",
       ["person", "timescale"], "cooking takes minutes; the rise of already-cooked ones is what the clip shows")
o(206, "A tall candle standing on the dashboard of a car parked in the sun has softened and bent over.",
       "The candle is bent toward the dashboard where it softened and may sag further; it does not stand back up in the heat.", ["timescale", "expectation"])
o(208, "A hot oven door is opened, and the air above the opening shimmers and wavers.", None, ["person"])
o(209, "A bag of frozen vegetables is tipped into a hot wok, and the frost on them disappears with a hiss as they hit the pan.", None, ["person"])
o(210, "A gel ice pack left in the sun on a picnic blanket has gone soft and floppy.",
       "The pack bends and sags as it is lifted and its surface sweats; it does not stiffen again in the sun.", ["timescale", "expectation"])
o(211, "Wet chicken pieces are dropped into a pan of hot oil, and the oil spits and crackles violently for a moment.", None, ["person"])
o(213, "A vinyl record left on the back seat of a car in the sun has warped into a wavy shape.",
       "The disc is bent into gentle waves and stays warped; it does not flatten again while warm.", ["timescale"])
o(215, "A heat gun is aimed at the loose plastic wrap around a gift basket, and the wrap tightens and shrinks snugly around the basket.", None, ["person"])
o(216, "A spoonful of gnocchi is dropped into boiling water, and the cooked ones rise to the surface one by one.",
       "The gnocchi sink on entry and any that rise bob up one by one and float; none floats the instant it enters.", ["person", "timescale"])
o(221, None, "Vapour rises from the side nearest the heat; the umbrella does not become wetter and the vapour does not sink.", ["expectation"], "drying not visible in 5 s")
o(223, "A few drops of water are flicked onto a hot griddle, and the drops skitter around and vanish.", None, ["person"])
o(227, "Cooking oil is poured into a pan over high heat, and the oil begins to shimmer and ripple across its surface.", None, ["person"])
o(228, "A chocolate bar left on a sunny windowsill has gone soft and bends over the edge of the sill.",
       "The bar droops over the sill edge and would take a fingerprint if touched; it does not stiffen while still in the sun.", ["person", "timescale"])
o(229, "A handful of dry rice noodles is dropped into hot water, and they go from stiff and brittle to limp and floppy.", None, ["person"])
o(230, "A plastic rain poncho hanging close to a patio heater crinkles and shrinks where the heat hits it.",
       "The plastic wrinkles and pulls tight on the side toward the heater; the effect stays after the heat is removed.", ["person"])
o(231, "Hot water is poured over a pot of dried seaweed, and the crisp sheets swell and soften into flowing strands.", None, ["person"])
o(232, "A flour tortilla is held over a gas flame with tongs, and pockets of the tortilla puff up into bubbles.", None, ["person"])
o(233, "A frozen burger patty is dropped into a hot pan, and the ice on its surface crackles away in a burst of steam.", None, ["person"])
o(235, "A damp sock is held over a campfire on a stick, and steam rises from it as it dries.",
       "Steam rises from the sock; the sock does not get wetter and the vapour does not sink.", ["person", "expectation"])
o(236, "A basket of frozen spring rolls is lowered into hot oil, and the oil boils up around them in a rush of bubbles.", None, ["person"])
o(237, "A plastic ruler is held over a candle flame, and the ruler softens and sags in the middle.", None, ["person"])
o(239, "A jar of thick cloudy honey stands in a bowl of hot water, and the honey is turning clear and runny.",
       "The clearing starts at the outside of the jar nearest the hot water and spreads inward; the honey does not turn cloudier while warm.",
       ["timescale", "expectation"], "full clearing takes 10+ min")
o(240, "An ice cream truck's freezer door has been left open in the sun, and the ice cream sandwiches inside have sagged and softened in their wrappers.",
       None, ["timescale"])
o(241, "A wet pasta strainer is dropped onto a hot burner, and water sizzles off the metal in a burst of steam.", None, ["person"])
o(242, "A birthday balloon left in a car parked in the sun has swelled up.",
       "The balloon is larger and rounder than a freshly inflated one and stays that way in the heat; it does not shrink in the hot car.", ["timescale", "expectation"])
o(243, "A hairdryer is aimed at a bent plastic pipe, and the pipe softens enough to be straightened by hand and holds its new shape when cool.", None, ["person"])
o(244, "A frozen block of soup sits in a pan over heat, sliding around on a thin layer of melt and shrinking as the liquid pools around it.", None, ["person"])
o(245, "A lava lamp that has warmed up glows on a table, and the blobs of wax inside rise and sink.",
       "Blobs rise from the bottom, slow near the top, and fall again in a slow cycle; they do not jump or move in a way unrelated to the warm base.",
       ["timescale", "expectation"], "warm-up takes 30+ min")
o(246, "A pat of cold butter is placed in the centre of a hot pancake on the griddle, and it slides and glides across the surface as it melts.", None, ["person"])
o(247, "Boiling water is poured into a collapsed vacuum-packed camping meal pouch, and the pouch swells and stands up.", None, ["person"])
o(248, "A cold egg is dropped into a pot of boiling water, and the water briefly stops boiling around it before the bubbling returns.", None, ["person"])

recs = json.loads(SRC.read_text())
out = []
stats = {"person": 0, "timescale": 0, "expectation": 0, "keep_person": 0, "delete": 0, "unchanged": 0}
for r in recs:
    c, e, ch, note = O.get(r["id"], (None, None, [], ""))
    if r["id"] in DELETE:
        c, e, ch, note = None, None, ["delete"], DELETE[r["id"]]
    new = {
        "id": r["id"], "category": r["category"], "subcategory": r["subcategory"],
        "violation_types": r["violation_types"],
        "caption": c if c else r["caption"],
        "expectation": e if e else r["expectation"],
        "old_caption": r["caption"], "old_expectation": r["expectation"],
        "change": ch, "note": note,
    }
    assert (c is None) == ("person" not in ch and "timescale" not in ch) or c is not None
    for k in ch: stats[k] += 1
    if not ch: stats["unchanged"] += 1
    out.append(new)
DST.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
print(f"wrote {DST} with {len(out)} records; {stats}")
