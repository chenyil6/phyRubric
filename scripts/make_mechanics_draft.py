#!/usr/bin/env python3
"""Build data/drafts/mechanics_draft.json: proposed rewrites of the Mechanics train captions
that minimise human presence without changing the physics each caption tests.

Rule (Proposal.md 4.1, "people are a noise source"):
  person      - a whole person who is only the actor is removed: passive voice, a device or the
                environment as the cause, or the smallest body part that must apply the force
                ("a hand", "a foot", "an arm", "breath").  The human action stays in the opening
                clause so the judged physics happens after the person has exited.
                Where the body was a load / target / catcher / occluded object it is replaced by an
                object or an animal (noted per record).
  expectation - the expectation is re-worded to match (pronouns and roles), never loosened.
  keep_person - the body IS the physics (inertia on a body, falls, jumps, biomechanics, mouth as
                pump or cutter); the caption is left as is.
  scene       - the user found the original scene odd; a different everyday scene testing the same
                physics (same subcategory and violation types) replaces it.
Every record keeps id / category / subcategory / violation_types; old_caption / old_expectation
are kept for side-by-side review; `change` lists which rules touched the record.
"""
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data/train/mechanics.json"
DST = ROOT / "data/drafts/mechanics_draft.json"
REVIEW = ROOT / "data/drafts/mechanics_draft_review.md"

# id -> (caption or None, expectation or None, [changes], note)
O: dict[str, tuple] = {}


def o(i, c=None, e=None, ch=(), note=""):
    O[f"MECH-{i:04d}"] = (c, e, list(ch), note)


def keep(i, note):
    o(i, None, None, ["keep_person"], note)


# ---------------------------------------------------------------- inertia
o(1, "Two passengers sit in the back seat of a car when it brakes hard, and both are thrown forward against their seat belts.",
  None, ["person"], "bodies are the inertia demo and stay; 'friends, chatting' was decorative (faces, mouths) and is dropped")
keep(2, "the swaying body is the phenomenon")
o(4, "A shopping cart is given a push across an empty parking lot and let go, and it rolls on by itself until it slows to a stop.",
  None, ["person"], "pusher reduced to an implied push in the opening clause; hands may show at the start")
o(5, "An empty playground swing is given one push and left alone, and it keeps going back and forth on its own before gradually dying down.",
  None, ["person"], "the child was only the load and the parent only the trigger; an empty swing shows the same decay")
keep(6, "the lurching body is the phenomenon")
o(7, "A phone lying flat on the dashboard of a car slides forward toward the windshield when the car brakes suddenly at a red light.",
  None, ["person"], "'the driver brakes' -> 'the car brakes'; nothing else changes")
keep(8, "the leaping, stumbling body is the phenomenon")
o(9, "A serving cart carrying a tray of full water glasses is pushed forward and stopped short, and the water sloshes forward and spills.",
  "The water surges in the direction the cart was moving, at the moment it stops; the glasses may slide forward on the tray; the water settles afterwards.",
  ["person", "expectation"], "waiter and running child replaced by a pushed cart; same sudden-stop slosh")
o(11, "A wagon loaded with pumpkins is pulled along a path by its handle and the pull stops suddenly; the wagon rolls on a little and the pumpkins tip forward.",
  "The wagon does not stop the instant the pull does; it rolls until the handle checks it; the pumpkins tip forward, not backward.",
  ["person", "expectation"], "adult and toddler replaced by a hand-pulled wagon and a loose load that tips the same way")
o(12, "A bowling ball is released at the top of the lane and rolls the full length of the lane to the pins at the far end.",
  None, ["person"], "bowler removed; the release is the opening clause")
keep(13, "the rider thrown off the board is the phenomenon")
o(14, "A car driving along an icy street brakes hard, its wheels lock, and it slides on past the stop line before it comes to a halt.",
  "The car keeps moving in its original direction after the wheels lock and slows only gradually while the wheels are not turning; it comes to rest beyond the line, not on the spot, and does not swerve or stop instantly.",
  ["scene"], "user found the skidding dog odd; replaced by a car braking on ice, the same overshoot of the intended stop with no person or animal")
o(16, "A wet umbrella is flicked sharply and stopped short, and the water drops fly off the tip and keep going in the direction of the flick.",
  None, ["person"], "man removed; passive flick")
keep(17, "the leaning bodies are the phenomenon")

# ---------------------------------------------------------------- gravity_fall
o(18, "A bag of oranges tips over at the top of a staircase, and the oranges spill out and tumble down the stairs to the bottom.",
  None, ["person"], "user's variant: the bag tipping over is the trigger, no person or hand")
o(19, "A hammer resting on the top of a ladder is knocked off and falls to the ground.",
  "The hammer drops straight down, speeding up as it falls, and hits the ground; it does not pause or drift sideways.",
  ["person", "expectation"], "two people removed; the knock is the opening clause and the helper who missed the catch is gone")
o(21, "The string of a helium balloon tied to a park bench comes loose, and the balloon floats up into the sky.",
  "The balloon rises steadily with the string trailing below it; it does not fall, hover at bench height, or rise faster than a gentle drift.",
  ["person", "expectation"], "child replaced by a string coming loose from a bench: no person at all")
o(23, "A ceramic plate slides off the edge of a restaurant counter, drops onto the tiled floor, and shatters.",
  None, ["person"], "waiter's hand replaced by the plate sliding off a counter")
o(24, "A tennis ball is tossed straight up in a backyard and comes back down to the same spot.",
  None, ["person"], "boy removed; the catch is dropped, the up-and-down is unchanged")
o(25, "A watering can is turned upside down over a flower bed and the water pours out onto the soil.",
  None, ["person"], "gardener removed; passive")
o(26, "A stack of coins on the corner of a kitchen counter is knocked off by an elbow and the coins scatter on the floor.",
  None, ["person"], "'someone's elbow' -> 'an elbow'")
o(27, "An egg is cracked on the rim of a bowl and the shell pulled apart above it, and the yolk and white drop into the bowl.",
  None, ["person"], "cook removed; passive, hands implied")
keep(28, "the skydiver is the falling body")
keep(29, "the diver is the falling body")
o(30, "A water balloon is dropped from a second-floor balcony, and it falls straight down and bursts on the pavement.",
  "The balloon starts falling the moment it is released, drops straight down and gets faster as it goes, and does not drift sideways, slow, or hover; it bursts only when it hits the pavement, and the water spreads out on the ground and stays there.",
  ["person", "expectation"], "boy removed; 'his hand opens' -> 'it is released'")
o(31, "A button on a vending machine is pressed, and a can drops inside the machine and lands in the tray at the bottom.",
  None, ["person"], "man reduced to the button press")
o(32, "A handful of dry sand is picked up on a beach and let trickle out between the fingers onto the sand below.",
  "The sand runs straight down between the fingers and piles up below the hand; it does not hang in the air or blow away on a still day.",
  ["person", "expectation"], "toddler removed; fingers are the container here and stay")

# ---------------------------------------------------------------- collision
o(36, "Two bumper cars at a fairground drive straight at each other, meet head-on, and both cars bounce back a little.",
  "Both cars stop or rebound at the moment of contact; neither car passes through the other.",
  ["person", "expectation"], "children no longer named; drivers, if rendered, are not judged")
o(37, "A tennis ball is thrown hard against a brick wall and bounces back the way it came.",
  None, ["person"], "'toward the thrower' dropped")
o(42, "A dodgeball thrown hard hits a heavy punching bag hanging in a gym, bounces off it, and drops to the floor.",
  "The bag swings back at the moment of impact; the ball rebounds and falls nearby, not passing through the bag or sticking to it.",
  ["person", "expectation"], "boy as soft target replaced by a hanging punching bag: same soft, yielding target that is pushed back")
o(44, "A toy train runs along a track, hits a wooden block lying across the rails, and stops.",
  None, ["person"], "'someone has placed' dropped")
o(45, "A putted golf ball rolls across the green, hits the back of the cup's rim, pops up, and drops into the hole.",
  None, ["person"], "golfer removed; the putt is the opening clause")
keep(47, "two colliding bodies are the phenomenon")
o(48, "A soccer ball rolled at a slant into a low garden wall bounces off at a slant the other way and rolls on across the lawn.",
  "The change of direction happens at the wall and mirrors the angle the ball came in at; the ball keeps rolling after contact, a little slower; it does not stop dead at the wall, pass into it, or come straight back.",
  ["scene"], "user found the ping-pong clip too hard: tiny fast ball, sub-frame glancing contact, needs a player. Same oblique deflection with a large slow ball and no person")
o(50, "A soccer ball rolled across a paved yard hits an empty plastic bucket standing in its path; the bucket is knocked over and the ball rolls on more slowly.",
  "The bucket moves only when the ball reaches it and topples away from the ball; the ball slows at the contact and carries on in roughly the same direction or stops; it does not pass through the bucket, and the bucket does not move before contact.",
  ["scene"], "user found the beach ball on sand uncertain: a light ball may not tip the bucket and beach balls barely roll on sand. Heavier ball on pavement makes the knock-over certain")

# ---------------------------------------------------------------- friction_rolling
o(51, "A loaded sled slides down a snowy slope, runs out onto a flat patch of bare grass, and stops within a short distance.",
  None, ["person"], "child was only the load; a loaded sled keeps the momentum")
o(53, "A car tries to pull away from a snow-covered kerb, its rear wheels spin in place and throw up snow, and the car stays almost where it is.",
  None, ["person"], "'a driver tries' -> 'a car tries'")
keep(54, "the slipping body is the phenomenon")
o(56, "A hula hoop is rolled along a sidewalk and let go; it rolls on by itself, wobbles, and falls over.",
  None, ["person"], "boy removed; passive")
o(59, "A piece of chalk is drawn in a large circle across a blackboard, and a white line appears where it has passed.",
  None, ["person"], "teacher removed; passive")
o(60, "A heavy wooden barrel being rolled up a plank onto a truck bed is let go halfway up, and it rolls back down to the ground.",
  "The roll back begins as soon as the barrel is released and speeds up down the plank; the barrel does not stay put on the slope or continue upward.",
  ["person", "expectation"], "man removed; passive")
o(61, "A bicycle is turned upside down, its front wheel is given a spin, and the wheel keeps spinning for a while before stopping.",
  None, ["person"], "'someone spins ... and steps back' -> 'is given a spin'")
o(62, "A ball is rolled up a gentle grassy slope; it slows, stops, and rolls back down.",
  None, ["person"], "child removed; passive")
keep(65, "the rider's dragging foot is the brake; could be framed from the knees down")
o(66, "A car drives onto a frozen pond, its front wheels are turned sharply, and the car keeps sliding straight ahead instead of turning.",
  None, ["person"], "'the driver turns the steering wheel' -> 'the wheels are turned'")

# ---------------------------------------------------------------- projectile
o(67, "A soft ball is tossed in a gentle arc across a lawn and lands in a laundry basket standing on the grass.",
  None, ["person"], "father and daughter replaced by a toss into a basket; the arc is unchanged")
o(68, "A running garden hose propped at an upward angle beside a vegetable bed sends its stream over the bed, and the water comes down on the far side.",
  None, ["person"], "gardener replaced by a propped hose: no person at all")
o(69, "A basketball shot from the three-point line drops through the hoop.",
  None, ["person"], "teenager removed; passive")
keep(70, "the child is the projectile")
o(71, "A flat stone is thrown sideways low over a calm lake, and it skips across the surface several times before sinking.",
  None, ["person"], "boy removed; passive")
o(73, "A baseball is struck high into the outfield and comes down onto the grass far from where it was hit.",
  None, ["person"], "batter and fielder removed; the catch is dropped, the arc is unchanged")
o(74, "A snowball thrown across a snowy yard hits a wooden fence post and bursts into loose snow.",
  None, ["person"], "friend as target replaced by a fence post")
keep(76, "the jumping body is the projectile")
o(77, "A coin is flipped into the air and caught as it comes down.",
  None, ["person"], "referee removed; passive")
o(78, "A dart is thrown at a dartboard on a pub wall and sticks in the board.",
  None, ["person"], "man removed; passive")
o(79, "A horse gallops toward a low fence, jumps over it, and lands on the far side.",
  None, ["person"], "rider removed; the horse alone is the projectile")
o(80, "A soccer ball is punted far down the field, and it lands and bounces near the far end.",
  None, ["person"], "goalkeeper removed; passive")
o(82, "A rubber ball is dropped from shoulder height onto a concrete driveway and bounces several times before rolling away.",
  None, ["person"], "kid removed; passive")

# ---------------------------------------------------------------- balance_topple
o(83, "A tall stack of cardboard boxes in a hallway is pushed from one side and topples, boxes tumbling to the floor.",
  "The stack leans away from the push before falling; the upper boxes go first and fall on the side away from the push; they do not float or fall toward it.",
  ["person", "expectation"], "mover removed; passive")
o(84, "A block is pulled out of the bottom row of a tall wooden block tower and the tower collapses.",
  None, ["person"], "girl removed; passive")
o(85, "A bicycle resting on its kickstand is hit by a stray soccer ball and falls over onto its side.",
  None, ["person"], "passing pedestrian replaced by a stray ball: no person at all")
keep(86, "the tipping body is the phenomenon")
o(87, "The top cup of a tower of stacked plastic cups on a carpet is swiped sideways, and the top of the tower falls.",
  None, ["person"], "toddler removed; passive, the stacking is dropped")
o(88, "An elbow knocks a full wine glass on a table; it tips over and the wine spills across the tablecloth.",
  None, ["person"], "'waiter's elbow' -> 'an elbow'")
o(89, "A stepladder standing on a lawn is pushed sideways past its balance point and falls over onto the grass.",
  None, ["person"], "man removed; passive")
o(90, "The tall thin tower on top of a sandcastle is tapped with a plastic shovel, and the tower crumbles and slides down the side of the castle.",
  None, ["person"], "child removed; passive")
o(93, "Two heavy sacks sit on opposite ends of a level seesaw; one sack is dragged off its end, and the other end drops to the ground.",
  "The drop happens as soon as the sack's weight leaves the seat; the emptied end rises at the same time; the beam does not stay level.",
  ["person", "expectation"], "two children replaced by two sacks; removing one load is the same event")
o(94, "A hardback book is pushed slowly toward the edge of a table until it tips over the edge and falls to the floor.",
  None, ["person"], "boy removed; passive")
o(95, "A stack of textbooks is balanced on the palm of a hand; the hand tilts to one side, and the books slide off and fall to the floor.",
  None, ["person"], "student reduced to a hand")
keep(96, "cyclist and bike fall together; the body is part of the toppling object")
o(97, "A wooden spoon is balanced across the rim of a pot and a heavy ladle set on one end, and the spoon tips and the ladle falls into the pot.",
  None, ["person"], "cook removed; passive")
keep(98, "the stumbling body is what launches the plates")
o(99, "The top of a tall unanchored bookshelf is pulled forward; the shelf tips forward and falls, spilling books.",
  "The shelf leans toward the pull, the books slide off the shelves as it tilts, and it falls to the floor; it does not fall backward or stop mid-tilt.",
  ["person", "expectation"], "climbing child removed; a pull on the top gives the same tip-forward")

# ---------------------------------------------------------------- tension
o(100, "Two large dogs each grab an end of a slack rope toy lying on the grass and pull; the rope goes taut and the middle knot moves toward the stronger dog.",
  "The rope straightens between the dogs before the knot moves, bows only where the jaws grip it, and stays taut while they pull.",
  ["person", "expectation"], "two teams of people replaced by two dogs playing tug; same slack-to-taut and drift toward the stronger side")
o(101, "A large dog on a leash tied to a post spots a squirrel and lunges after it; the leash snaps taut and the dog is stopped short.",
  "The leash goes from slack to straight at the instant the dog reaches its end; the dog stops at that same instant, not before, and the post does not move.",
  ["person", "expectation"], "owner replaced by a post; the jerk on the owner is dropped")
o(102, "A basket of wet laundry is hung from the middle of a clothesline strung between two posts, and the line sags under the weight.",
  None, ["person"], "woman removed; passive")
o(103, "A kite tied by its string to a fence post is lifted by a steady wind, and the string pulls taut from the post up to the kite.",
  "The string runs in a shallow taut curve and tugs at the post; it does not hang slack while the kite is flying.",
  ["person", "expectation"], "child replaced by a fence post: no person at all")
o(104, "A bucket is lowered into a well on a rope and hauled back up full of water.",
  "The rope hangs straight down under the bucket's weight and stays taut as it is pulled; the bucket rises only as fast as rope is pulled in.",
  ["person", "expectation"], "man removed; passive")
o(105, "A heavy sack is dropped into an empty hammock strung between two trees, and the hammock sags deeply under it.",
  "The sag forms as the weight lands, the ropes pull straight to the trees, and the hammock swings gently before settling.",
  ["person", "expectation"], "man as load replaced by a sack")
o(107, "A fishing line goes tight as a fish takes the bait, and the rod, resting in a holder on the bank, bends toward the water.",
  None, ["person"], "angler replaced by a rod holder: no person at all")
o(108, "An empty tire swing hanging from a branch is given a push and swings back and forth beneath the branch.",
  "The rope stays straight and taut throughout and the tire follows an arc under the branch; the rope does not go slack or bend.",
  ["person", "expectation"], "child and friend replaced by a pushed tire swing; the tire is the visible mass")
o(109, "A sled loaded with firewood is pulled across a snowy field by a rope, then the pull stops, and the rope goes slack.",
  "The rope is taut while the sled is being pulled and droops only after the pull stops; the sled slides on a little before stopping.",
  ["person", "expectation"], "parent and child replaced by a loaded sled and a passive pull")
o(112, "A crane cable is hooked to a steel beam lying on the ground; the crane lifts, the cable tightens, and the beam rises off the ground.",
  None, ["person"], "'the operator lifts' -> 'the crane lifts'")
o(113, "A soaked towel is wrung out over a sink, and water streams out of it.",
  "The towel twists thinner where wrung and the water falls straight down into the sink while it is twisted; the flow stops when the twisting stops.",
  ["person", "expectation"], "woman removed; passive")
keep(114, "the jerked head is the phenomenon")
o(115, "The rope on a flagpole is pulled steadily, and the flag rises up the pole as the rope runs through the pulley at the top.",
  "The rope stays taut on the pulled side, the flag moves only as fast as rope is pulled in, and it stops rising when the pulling stops; the rope does not stretch or go slack while lifting.",
  ["person", "expectation"], "man removed; passive")
o(116, "A heavy bucket hung from the handle of a backyard zip line is released and rides it down to the far end, the cable sagging under it.",
  "The cable dips most under the handle and the dip travels with the bucket; the cable stays straight on either side and does not go slack or stretch like elastic.",
  ["person", "expectation"], "child as load replaced by a bucket")

# ---------------------------------------------------------------- deformation
o(118, "An empty aluminum soda can lying on a driveway is stepped on, and it crumples flat and stays flat.",
  "The crushing happens under the foot, not before; the can keeps its crushed shape after the foot lifts and does not spring back.",
  ["person", "expectation"], "man removed; passive, the foot stays in the expectation")
o(119, "Two thumbs press into a ball of modelling clay on a table, and the clay keeps the thumbprints after the hands lift away.",
  None, ["person"], "child reduced to thumbs")
o(120, "A foam pillow is pressed down and released, and it puffs back to its shape.",
  "The pillow sinks only where pressed and recovers gradually after release; it does not stay dented or spring back instantly like rubber.",
  ["person", "expectation"], "woman removed; passive")
keep(121, "the jumping body is the load")
o(122, "A metal paper clip is bent open and let go, and it stays in its new shape.",
  "The bending happens only where the clip is worked, and it does not spring closed after release.",
  ["person", "expectation"], "man removed; passive")
o(123, "A hand is pressed into a slab of memory foam and lifted away, and the hand-shaped dent slowly fills back in.",
  None, ["person"], "child removed; the hand stays because the dent is hand-shaped")
o(124, "An inflated balloon is squeezed between two palms; it flattens between the hands and bulges out at the sides, then rounds out again when the hands let go.",
  "The balloon keeps roughly the same overall size while squeezed, bulging where it is not pressed; it does not shrink, pass through the hands, or stay flat.",
  ["person", "expectation"], "man reduced to palms")
o(125, "Loose snow is packed between mittened hands into a firm snowball that holds its shape when the hands open.",
  None, ["person"], "child reduced to mittened hands")
keep(126, "the gymnast is the load and the projectile")
o(128, "The heel of a hand presses into a ball of bread dough on a floured counter and the dough flattens and spreads.",
  None, ["person"], "baker reduced to a hand")
o(129, "A loaded toolbox is set down on top of a large cardboard box in a garage, the box caves in under it, and it stays crumpled when the toolbox is lifted away.",
  None, ["person"], "sitting person replaced by a heavy toolbox; the expectation already speaks of 'the weight'")
o(130, "A fresh green twig is bent into a curve and one end let go, and the twig springs back to nearly straight.",
  None, ["person"], "child removed; passive")
o(131, "A ripe avocado is pressed firmly between finger and thumb and the skin dents inward and stays dented.",
  None, ["person"], "cook removed; finger and thumb stay")
o(132, "A bowstring is drawn back and released, and the arrow flies off toward the target.",
  "The bow limbs flex as the string is drawn and spring back on release; the arrow leaves at the instant of release, not before.",
  ["person", "expectation"], "archer removed; 'to her cheek' dropped so no face is required")
o(133, "A rubber band stretched between two fingers is let slip at one end; the band snaps back and drops.",
  None, ["person"], "child reduced to fingers")

# ---------------------------------------------------------------- cut_tear
o(134, "A sheet of coloured paper is cut in half with scissors, and the two halves fall apart on the table.",
  None, ["person"], "child removed; passive")
o(135, "A loaf of crusty bread is torn in two at a dinner table.",
  "The crust cracks and the loaf pulls apart with a ragged tear where it is pulled, crumbs falling; the two pieces stay separate.",
  ["person", "expectation"], "man removed; passive")
o(136, "A ripe tomato is sliced into rounds on a cutting board with a sharp knife.",
  None, ["person"], "cook removed; passive")
o(137, "A strip of packing tape is ripped off a cardboard box and the box flaps come free.",
  "The tape peels up along its length as it is pulled, sometimes taking the top layer of cardboard with it; the flaps open only after the tape is off.",
  ["person", "expectation"], "woman removed; passive")
keep(138, "the mouth is the cutter")
o(139, "A carrot is chopped into rounds with quick knife strokes, and the pieces pile up beside the blade.",
  None, ["person"], "chef removed; passive")
o(140, "A length of cotton fabric is torn along a snipped edge, and it rips into two pieces.",
  "The rip runs in a straight line following the weave as it is pulled, loose threads fraying at the edges; the tear does not run ahead of the pull.",
  ["person", "expectation"], "tailor removed; passive")
o(141, "A tuft of cotton candy is pulled off the top of a cone and comes away as a separate wisp.",
  None, ["person"], "child removed; passive")
o(142, "A dry twig is snapped in half with a crack.",
  None, ["person"], "hiker removed; passive")
o(143, "A bar of chocolate is broken along its grooves into separate pieces.",
  "The bar snaps cleanly along the grooves where it is bent; the pieces do not stick back together or bend without breaking.",
  ["person", "expectation"], "woman removed; passive")
o(144, "The two sides of a bag of chips are pulled apart at the top seam and the bag pops open.",
  "The seal gives way suddenly as the sides are pulled, sometimes tearing down one side, and the chips inside are visible; the bag does not open before the pull.",
  ["person", "expectation"], "teenager removed; passive")
o(145, "A slice is cut out of a round birthday cake and lifted onto a plate, leaving a wedge-shaped gap in the cake.",
  None, ["person"], "host removed; passive")
o(146, "An orange is peeled starting from a slit at the top, and the pieces of peel pile up beside the bare fruit.",
  "The peel comes away only where it is worked loose, exposing the segments underneath; the fruit does not regrow its skin.",
  ["person", "expectation"], "man removed; passive")
o(147, "An axe swung down onto a log standing on end on a chopping block splits it into two pieces that fall apart to the sides.",
  None, ["person"], "man removed; passive. A hydraulic log splitter would remove the arms too but changes the look of the event")
o(148, "A page is torn out of a spiral notebook, leaving a fringe of paper on the coil.",
  None, ["person"], "student removed; passive")
o(149, "A thick garden hose is cut through with a pair of shears, leaving two open ends.",
  None, ["person"], "gardener removed; passive")
o(150, "A stubborn weed is pulled out of the soil by its leaves, and the whole plant comes up with its roots and clinging soil.",
  None, ["person"], "boy removed; passive")

# ---------------------------------------------------------------- fluid
o(151, "Water is poured from a jug into an empty drinking glass on a table until the glass is nearly full.",
  None, ["person"], "woman removed; passive")
o(152, "A full glass of milk on a kitchen table is knocked over, and the milk spreads across the table and drips off the edge.",
  None, ["person"], "child removed; passive")
o(153, "A stone is dropped into a still garden pond; it splashes, sinks, and ripples spread out across the water.",
  None, ["person"], "boy removed; passive")
o(154, "Olive oil is poured into a glass of water, and the oil gathers in a layer floating on top of the water.",
  None, ["person"], "cook removed; passive")
o(156, "A jar of honey is tipped over a slice of toast, and the honey flows out in a slow thick ribbon onto the toast.",
  None, ["person"], "woman removed; passive")
o(157, "A half-full fish tank resting on a table is tilted to one side, and the water climbs the low side and spills over the rim.",
  None, ["person"], "carrying man removed; the tank is tilted on a table, passive")
o(158, "A small air pump runs with its tube in a glass of soapy water, and bubbles rise and pile up in a foam at the top of the glass.",
  "Bubbles form at the tube tip and rise; the foam builds while the pump runs and spills over the rim if it gets tall enough; bubbles do not sink.",
  ["person", "expectation"], "child blowing through a straw replaced by an air pump: no face")
o(159, "Several ice cubes are dropped into a glass of soda, and the cubes bob up and float near the surface.",
  None, ["person"], "bartender removed; passive")
o(160, "A dry sponge is dropped into a basin of water; it floats, darkens as it soaks up water, and settles lower.",
  None, ["person"], "woman removed; passive")
o(162, "A saucepan is tipped and soup poured into a bowl until it is full and begins to spill over the sides.",
  None, ["person"], "cook removed; passive")
keep(164, "the paddler is the engine; arms and torso are needed for the stroke")
keep(165, "the mouth is the pump")
o(166, "A plastic ketchup bottle is squeezed over a plate of fries, and ketchup comes out of the nozzle onto the fries.",
  None, ["person"], "cook removed; passive")
o(167, "An inflated beach ball is pushed under the water in a swimming pool and let go, and it pops back up to the surface.",
  None, ["person"], "boy removed; passive")

# ---------------------------------------------------------------- granular
o(168, "A bag of sugar is poured into a large mixing bowl, and the sugar builds up into a mound in the bowl.",
  None, ["person"], "baker removed; passive")
o(169, "A bucket packed with damp sand is turned upside down on the beach and lifted off, leaving a bucket-shaped sand tower standing.",
  None, ["person"], "child removed; passive")
o(171, "A salt shaker is shaken over a plate of fries and salt grains fall onto the fries.",
  None, ["person"], "diner removed; passive")
o(174, "A bag of soil is emptied into a flower pot, filling it with a loose heap.",
  None, ["person"], "gardener removed; passive")
o(175, "Bare feet walk across a stretch of dry beach sand, leaving a trail of footprints behind.",
  "Each foot sinks a little and pushes sand up around the print; the prints appear only where a foot has stepped and stay behind.",
  ["person", "expectation"], "man reduced to feet")
o(176, "Snow is shovelled off a driveway onto the lawn, building a ragged pile there.",
  "Each shovelful flies in a loose clump that breaks apart in the air and lands scattered; the driveway clears where it has been shovelled.",
  ["person", "expectation"], "man removed; passive, arms and shovel remain")
o(177, "Dried beans are poured from a bag into a glass jar until it is full and beans spill over onto the counter.",
  None, ["person"], "cook removed; passive")
o(178, "A handful of seed is scattered across bare soil with a sweeping throw, and the seeds land spread over a wide patch.",
  None, ["person"], "farmer removed; passive")
o(179, "A used coffee filter is knocked against the rim of a bin, and the puck of wet grounds drops out and breaks apart in the bin.",
  None, ["person"], "barista removed; passive")
o(180, "The top of a small pile of dry sand in a sandbox is kicked, and sand sprays forward and leaves a gouge in the pile.",
  None, ["person"], "child removed; passive")
o(181, "A bucket of gravel is poured slowly onto one spot on a flat concrete floor, and the gravel piles up into a cone.",
  None, ["person"], "worker removed; passive")
o(182, "A box of dry pasta is tipped into a pot of boiling water, and the pasta sinks and settles at the bottom.",
  None, ["person"], "woman removed; passive")
o(184, "A stick is dragged through a patch of loose gravel on a path, leaving a furrow behind it.",
  None, ["person"], "child removed; passive")

# ---------------------------------------------------------------- gas_wind
o(185, "An inflated balloon held shut at the neck is let go without being tied, and it shoots off around the room until it drops limp to the floor.",
  None, ["person"], "the blowing-up (a face) is dropped; only the releasing hand remains")
o(186, "A gust of wind lifts a wide-brimmed hat off a bench on a seafront and carries it away along the ground.",
  None, ["person"], "head replaced by a bench: no person at all")
o(187, "A gust of wind hits a dandelion clock standing in a meadow, and the seeds detach and drift away.",
  "The seeds leave in the direction of the wind and float slowly downward as they drift; the stalk is left bare and the seeds do not return.",
  ["person", "expectation"], "girl's breath replaced by wind: no face")
o(189, "An umbrella is opened on a windy street corner, and the wind tugs it sideways and flips the canopy inside out.",
  "The umbrella leans downwind and pulls at the hand holding it; the flip happens when a gust catches the underside; the canopy does not return to shape on its own.",
  ["person", "expectation"], "woman reduced to the holding hand")
o(191, "A bubble machine in a park sends out a stream of soap bubbles; the bubbles float away on the breeze and pop one by one.",
  None, ["person"], "child blowing bubbles replaced by a bubble machine: no face")
o(193, "A hairdryer is aimed at a long-haired wig on a stand, and the hair streams away from the nozzle.",
  None, ["person"], "woman replaced by a wig on a stand; the hair is still the subject")
o(194, "A leaf blower is pointed at a pile of dry leaves on a path, and the leaves scatter and tumble away from the nozzle.",
  None, ["person"], "groundskeeper removed; passive")
o(197, "A puff of breath blows out the candles on a birthday cake, and thin wisps of smoke rise from the wicks.",
  "The flames lean away from the breath and go out during it; the smoke rises upward; the candles do not relight on their own.",
  ["person", "expectation"], "man reduced to breath, as in the Heat draft")
o(198, "The valve of an inflated air mattress is opened and the mattress pressed down, and it hisses and sags flat.",
  None, ["person"], "camper removed; passive")
o(199, "A hand pump attached to a flat bicycle tyre is worked up and down, and the tyre fills out until it is firm and round.",
  "The tyre swells a little with each stroke and not between strokes; it does not inflate instantly or shrink while the pumping goes on.",
  ["person", "expectation"], "man removed; passive")
o(201, "A vacuum cleaner nozzle is run over crumbs scattered on a carpet, and the crumbs disappear into the nozzle.",
  None, ["person"], "woman removed; passive")

# ---------------------------------------------------------------- biomechanics
for i in (202, 203, 204, 205, 209, 210, 211, 212, 213, 214, 217):
    keep(i, "biomechanics: the body is the phenomenon")
o(215, "Two hands struggle to twist the lid off a tight jar and finally get it open, lid in hand.",
  "The hands grip jar and lid and the forearms twist in opposite directions; the lid turns and comes off only after the twist, not before.",
  ["person", "expectation"], "man reduced to hands and forearms, which are the mechanism here")
o(218, "A man pushes a broken-down car along a flat empty street, and the car slowly starts to roll.",
  None, ["person"], "the pusher is the phenomenon and stays; the friend steering is removed")

# ---------------------------------------------------------------- soft_material
o(219, "The laces of a sneaker are tied into a bow and the loops pulled tight.",
  "The laces cross, loop, and pull through each other only where the fingers guide them; the knot tightens as the loops are pulled and stays tied; the laces never pass through themselves or change length.",
  ["person", "expectation"], "boy removed; passive")
o(220, "A bath towel is folded in half and then in half again, and the folded square is set on a shelf.",
  None, ["person"], "woman removed; passive")
o(221, "A sheet of paper is crumpled into a tight ball and dropped on the desk.",
  "The sheet wrinkles and folds in on itself as it is crushed; the ball keeps its crumpled shape and creases after release and does not unfold flat again.",
  ["person", "expectation"], "man removed; passive")
o(222, "A paper map is unfolded on the hood of a car and smoothed flat.",
  None, ["person"], "hiker removed; passive")
o(223, "A yoga mat is rolled up from one end into a tight cylinder and stood against the wall.",
  None, ["person"], "woman removed; passive")
o(224, "A long garden hose is coiled into loops on the lawn.",
  None, ["person"], "gardener removed; passive")
o(225, "A tablecloth is shaken out and let settle over a dining table, and the edges hang down over the sides.",
  None, ["person"], "man removed; passive")
o(226, "A sheet of paper is folded step by step into a paper airplane.",
  None, ["person"], "child removed; passive")
o(227, "The drawstring of a cloth bag is pulled, and the bag's opening gathers shut.",
  None, ["person"], "camper removed; passive")
o(228, "A wet shirt is hung on a clothesline by its shoulders, and the shirt hangs down and drips.",
  None, ["person"], "woman removed; passive")
o(229, "A long scarf is wrapped twice around a wooden post and its end tucked in.",
  "The scarf bends around the post in layers that lie on top of each other, and the free end gets shorter as it is wrapped; the scarf does not pass through itself or the post.",
  ["person", "expectation"], "neck replaced by a post; layering and shortening free end are unchanged")
o(230, "A knot is tied in a thick rope and both ends pulled hard so the knot tightens.",
  "The rope loops through itself only where the hands pass it, the knot shrinks and hardens as the ends are pulled, and it holds; the rope does not stretch like elastic or merge with itself.",
  ["person", "expectation"], "sailor removed; passive")
o(231, "A rolled-up rug is given a push and unrolls across a wooden floor, and the rug lies flat.",
  None, ["person"], "mover removed; passive")
o(232, "A letter is folded into thirds and slid into an envelope.",
  None, ["person"], "woman removed; passive")
o(233, "A blanket is pulled off a bed by one corner and dragged across the floor.",
  "The blanket slides off the bed and trails on the floor in soft folds, following the pull and bunching where it catches; it does not stay stiff or move ahead of the pull.",
  ["person", "expectation"], "child removed; passive")
o(234, "A sheet of wrapping paper is torn from a roll and folded around a shoebox, creasing the corners.",
  None, ["person"], "cashier removed; passive")

# ---------------------------------------------------------------- occlusion_containment
o(236, "A set of keys is put into a small wooden box and the lid closed, then the lid is opened again and the keys taken out.",
  None, ["person"], "woman removed; passive")
o(237, "An upturned cup is placed over a coin on a table, slid to the side, and lifted to reveal the coin.",
  None, ["person"], "man removed; passive")
o(238, "A dog trots along a street and passes behind a wide pillar, disappearing and then emerging on the far side.",
  "The dog is hidden for a moment consistent with its pace and reappears at the same size and gait; its body does not show through the pillar or change while hidden.",
  ["person", "expectation"], "walking woman replaced by a dog as the occluded mover")
o(240, "Three apples are dropped one by one into an empty cloth bag, and the bag sags and bulges.",
  None, ["person"], "shopper removed; passive")
o(241, "A glass of water is poured into an opaque metal jug, then the jug is tipped and the water poured back out into the glass.",
  None, ["person"], "man removed; passive")
o(243, "A coat lies on a table; an arm slides into one sleeve and the hand emerges from the cuff.",
  None, ["person"], "man reduced to the arm, which is the occluded object")
o(244, "A large dog stands behind a floor-length curtain, and the curtain bulges where it stands with its paws showing beneath the hem.",
  "The bulge matches the dog's body and moves when it moves; only its paws are visible below; it does not show through the fabric or appear elsewhere.",
  ["person", "expectation"], "hiding child replaced by a dog")
o(246, "A large hardcover book is pushed into a shoebox that is too small for it, and the book will not go in.",
  None, ["person"], "man removed; passive")
o(247, "A tennis ball is dropped into a bucket, then the bucket is tipped over and the ball rolls out onto the floor.",
  None, ["person"], "child removed; passive")
o(248, "A blanket is thrown over a wooden chair, and the shape of the chair shows through the blanket.",
  None, ["person"], "woman removed; passive")
o(250, "A coin is pushed into the slot of a piggy bank and the bank is then shaken, and the coin rattles inside.",
  None, ["person"], "child removed; passive")

# ---------------------------------------------------------------- build
recs = json.loads(SRC.read_text())
# Records already accepted into SRC (scripts/apply_draft.py) carry the new text there; keep the original
# old_caption / old_expectation from the previous draft so the review history survives a re-run.
prev = {r["id"]: r for r in json.loads(DST.read_text())} if DST.exists() else {}
out = []
stats = Counter()
for r in recs:
    c, e, ch, note = O.get(r["id"], (None, None, [], ""))
    old_c, old_e = r["caption"], r["expectation"]
    accepted = bool(ch) and (c is None or c == r["caption"]) and (e is None or e == r["expectation"]) and r["id"] in prev
    if accepted and prev[r["id"]]["old_caption"] != r["caption"]:
        old_c, old_e = prev[r["id"]]["old_caption"], prev[r["id"]]["old_expectation"]
    new = {
        "id": r["id"], "category": r["category"], "subcategory": r["subcategory"],
        "violation_types": r["violation_types"],
        "caption": c if c else r["caption"],
        "expectation": e if e else r["expectation"],
        "old_caption": old_c, "old_expectation": old_e,
        "change": ch, "note": note,
    }
    assert accepted or not (c and c == r["caption"]), r["id"]
    assert accepted or not (e and e == r["expectation"]), r["id"]
    assert not re.search(r"\d", new["caption"]), r["id"]  # no numerals in captions
    for k in ch:
        stats[k] += 1
    if not ch:
        stats["unchanged"] += 1
    out.append(new)
DST.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
print(f"wrote {DST} with {len(out)} records; {dict(stats)}")

# ---------------------------------------------------------------- review markdown
by_sub = defaultdict(list)
for n in out:
    by_sub[n["subcategory"]].append(n)
lines = ["# Mechanics caption rewrite draft — changed records only", "",
         "Rules: **person** = whole person removed or shrunk to the body part that must apply the force "
         "(passive voice, a device or the environment as cause; a load / target / occluded body swapped for an object or animal) · "
         "**expectation** = expectation re-worded to match, not loosened · **keep_person** = the body is the phenomenon, left as is · "
         "**scene** = scene swapped at the user's request for one that tests the same physics. "
         "The human action, where it survives, sits in the opening clause so the judged physics happens after the person has exited. "
         "Unchanged records (no person to begin with) are omitted here but present in the JSON.", ""]
for sub, items in by_sub.items():
    changed = [n for n in items if n["change"]]
    lines += [f"\n## {sub} ({len(changed)} of {len(items)} touched)", ""]
    for n in changed:
        tag = " + ".join(n["change"])
        head = f"### {n['id']}  `{tag}`"
        if n["note"]:
            head += f"  — {n['note']}"
        lines.append(head)
        if n["caption"] == n["old_caption"]:
            lines.append(f"- caption unchanged: {n['caption']}")
        else:
            lines.append(f"- old caption: {n['old_caption']}")
            lines.append(f"- **new caption:** {n['caption']}")
        if n["expectation"] != n["old_expectation"]:
            lines.append(f"- old expectation: {n['old_expectation']}")
            lines.append(f"- **new expectation:** {n['expectation']}")
        lines.append("")
REVIEW.write_text("\n".join(lines) + "\n")
print(f"wrote {REVIEW}")
