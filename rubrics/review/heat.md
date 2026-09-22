# Rubric review

250 rubrics. SA = caption adherence (core/minor); PC = physics (fatal/core/major/minor, each tagged with a violation type). Expectation is the hidden field from data/, shown for the reviewer only.

# Heat

## HEAT-0001 · melt_freeze · train

**Caption.** An ice cream cone stands in a holder on a sunny picnic table, and the ice cream is melting and dripping down the side of the cone.

**Expectation (hidden).** The ice cream sags and drips run downward and pool at the base; it never firms back up or drips upward.

**Declared violation types.** process_direction, material_response, gravity_direction

**SA**
- S1 [core] An ice cream cone stands in a holder.
- S2 [core] The ice cream is visibly melting: it sags and softens.
- S3 [core] Drips run down the side of the cone.
- S4 [minor] The setting is a sunny outdoor picnic table.
- S5 [minor] No hand holds the cone; it stays upright in the holder.

**PC**
- P1 [core · process_direction]
  - expect: The ice cream softens and sags progressively: it slumps and loses its peaks, and each change persists; it never firms up or regains a shape it has lost.
  - fail: The ice cream regains a firm shape or ridges it had lost; or a drip retreats back into the scoop; or the melt alternates between more and less melted.
- P2 [major · gravity_direction]
  - expect: Melted ice cream runs downward along the cone; drips fall or pool at the base.
  - fail: A drip climbs upward or moves sideways around the cone against gravity; or melt collects on top of the scoop; or a drop leaves the cone and floats.
- P3 [major · material_response]
  - expect: The melting ice cream turns glossy and flows as a thick liquid; the cone stays a crisp solid, softening only where soaked.
  - fail: The cone melts or sags like the ice cream; or the melt runs as thin water rather than a thick coating; or a drip hardens into a spike standing out sideways.
- P4 [major · missing_consequence]
  - expect: The melt has a source: drips originate from the softening scoop and the cone gets wetter where they pass.
  - fail: Drips run down a cone whose ice cream stays fully firm and unchanged; or the cone's surface stays dry where drips have passed.
- P5 [fatal · permanence_count]
  - expect: One cone, one scoop; matter only moves from scoop to cone to table.
  - fail: The scoop grows larger while dripping; or a second scoop appears; or the cone vanishes or changes into another object; or ice cream appears on the table with no drip reaching it.
- P6 [minor · attribute_drift]
  - expect: The ice cream's colour, the cone's pattern and the holder stay the same.
  - fail: The ice cream changes colour or flavour; or the cone's waffle pattern changes; or the holder moves or vanishes.

## HEAT-0002 · melt_freeze · train

**Caption.** Hot water is poured from a kettle over a large block of ice on the ground, and the ice melts where the water hits it.

**Expectation (hidden).** The surface turns wet and glossy and hollows where the hot water lands, meltwater runs down the block and pools on the ground, and faint steam may rise; the block may crack from the heat but does not grow, vanish all at once, or refreeze.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A large block of ice sits on the ground.
- S2 [core] Hot, steaming water is poured onto the block from a kettle.
- S3 [core] The ice melts visibly where the water lands: wet, hollowed, running.
- S4 [minor] The kettle is visible as the source of the water.
- S5 [minor] Meltwater runs off the block.
- S6 [minor] The pour comes first and the melting follows it.

**PC**
- P1 [core · process_direction]
  - expect: Where the hot water lands the ice turns glossy, hollows and shrinks; the change is cumulative and grows only while water keeps coming.
  - fail: The hollow fills back in or the surface refreezes matt; or the block grows; or the melt spot moves to where no water fell.
- P2 [major · missing_consequence]
  - expect: The stream leaves a visible effect: wetting, a pit, run-off and possibly steam; the ice under the stream does not stay dry and sharp.
  - fail: Water runs over the ice and it stays dry, frosted and unchanged; or the block melts evenly everywhere at once including where no water touched.
- P3 [major · gravity_direction]
  - expect: The poured water and the meltwater run down the block and pool on the ground.
  - fail: Water climbs the block or flows uphill; or pools on top of the block's sloping face; or steam sinks and hugs the ground.
- P4 [major · material_response]
  - expect: Ice stays a hard solid where the water has not reached; it may crack sharply from the heat but does not bend, sag or flow.
  - fail: The block sags or bends like wax; or ice flows as a viscous lump; or the ice turns into snow or slush all over at once.
- P5 [fatal · permanence_count]
  - expect: One block, one kettle; the block only loses matter and water comes only from the kettle.
  - fail: The block vanishes at a stroke or a second block appears; or water appears on the ice with no stream; or the kettle vanishes; or the stream passes through the block.
- P6 [minor · attribute_drift]
  - expect: The ground, the kettle and the ice's colour stay consistent.
  - fail: The kettle changes colour or shape; or the ice turns coloured; or the ground changes texture away from the water.

## HEAT-0003 · melt_freeze · train

**Caption.** A pat of cold butter is dropped into a hot frying pan, and it melts into a spreading pool of liquid.

**Expectation (hidden).** The pat softens at the bottom first, slides and shrinks as it melts, and the liquid spreads outward; it does not stay a rigid block or re-solidify while the pan is hot.

**Declared violation types.** process_direction, material_response

**SA**
- S1 [core] A pat of butter is dropped into a frying pan.
- S2 [core] The butter melts: it loses its block shape and turns to liquid.
- S3 [core] A pool of liquid butter spreads across the pan.
- S4 [minor] The butter starts as a solid pat with square edges.
- S5 [minor] The drop comes first and the melting follows.

**PC**
- P1 [core · process_direction]
  - expect: The melting runs one way: the pat softens, slumps and shrinks while the pool around it grows, and each change persists.
  - fail: The pat regains its square edges or its height; or the pool shrinks back into the pat; or the butter firms into a solid block again in the pan; or the pat alternates between softer and firmer.
- P2 [core · material_response]
  - expect: The melted butter flows as a thin liquid that runs to the pan's low places and wets its surface; the unmelted pat is a soft solid that slides on the film.
  - fail: The pool stands as a dome or holds a fixed shape as the pan is tilted; or the melt moves as a solid slab across the pan; or the pat shatters into dry pieces; or the liquid stands in a heap above the pan's surface.
- P3 [major · gravity_direction]
  - expect: The pool spreads outward and downhill across the pan's floor and runs to its lowest side.
  - fail: The pool climbs the pan's sloping wall and stays there; or a run of butter travels uphill; or liquid butter lifts off the pan and floats.
- P4 [major · missing_consequence]
  - expect: The melt starts where the butter meets the pan: the pat's underside goes glossy and the film spreads out from beneath it.
  - fail: A pool spreads on the pan while the pat is still sharp-edged and dry underneath; or the pat melts from its top face while its underside stays solid and matt; or the pool appears on a part of the pan the butter never touched.
- P5 [fatal · permanence_count]
  - expect: One pat of butter; matter moves only from the pat into the pool, and the pan keeps its shape.
  - fail: The pat grows; or a second pat appears; or the pool vanishes at a stroke; or butter appears outside the pan with none crossing the rim; or the pat passes through the pan's base.
- P6 [minor · attribute_drift]
  - expect: The pan's finish, the hob and the things around it stay the same.
  - fail: The pan's finish changes pattern; or the hob's knobs move; or items around the pan rearrange.

**Note.** Browning of the butter is chemistry and is outside the branch; a deepening golden colour is not judged.

## HEAT-0004 · melt_freeze · train

**Caption.** A pat of butter on a small plate is heated in a microwave and slowly melts.

**Expectation (hidden).** The pat softens from the edges and bottom, slumps lower, and a glossy pool spreads outward on the plate as the pat shrinks; the butter does not stay a sharp-edged block, grow, vanish, or re-solidify while the microwave runs.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A pat of butter sits on a small plate.
- S2 [core] The plate is inside a microwave.
- S3 [core] The butter melts: it slumps and turns to liquid.
- S4 [core] A pool of butter spreads on the plate.
- S5 [minor] The pat starts with sharp edges.
- S6 [minor] The order is solid pat, slumping, pool.

**PC**
- P1 [core · process_direction]
  - expect: The melting runs one way: the pat shrinks while the pool grows, and each change persists.
  - fail: The pat regains its sharp edges or its height; or the pool shrinks back into the pat; or the butter sets solid again while the microwave runs; or the pat alternates between softer and firmer.
- P2 [core · permanence_count]
  - expect: The butter that leaves the pat is the butter in the pool: one pat on one plate, and nothing appears or vanishes.
  - fail: The pat grows while the pool spreads; or a second pat appears; or butter appears past the plate's rim with none crossing it; or butter appears on the plate away from both the pat and the pool.
- P3 [major · gravity_direction]
  - expect: The pool spreads outward and settles level in the plate's well.
  - fail: The pool climbs the plate's rim and stays above it; or a run of butter travels up the rim; or liquid butter lifts off the plate and hangs above it.
- P4 [major · material_response]
  - expect: The liquid butter is thin and glossy and finds its own level; the pat is a soft solid that slumps.
  - fail: The pool holds a dome or a fixed ridge; or the melt moves as a solid slab; or the pat shatters into dry pieces; or the pool keeps its shape when the plate is moved.
- P5 [fatal · shape_identity]
  - expect: The plate keeps its shape and the butter stays on it; nothing passes through the plate.
  - fail: Butter passes through the plate; or the plate changes shape or vanishes; or a second plate appears; or the plate merges with the surface under it.
- P6 [minor · attribute_drift]
  - expect: The plate's pattern and the microwave's interior stay the same.
  - fail: The plate's pattern changes; or the microwave's interior changes; or the walls inside change colour.

**Note.** Spitting or popping of the butter is expected and is not judged.

## HEAT-0005 · melt_freeze · train

**Caption.** A bowl of half-melted chocolate sits in a pan of steaming water and is stirred with a spatula, and the remaining pieces melt into the liquid.

**Expectation (hidden).** The remaining pieces soften and lose their edges from the outside in and are smeared into the glossy liquid by the spatula; the melted part does not re-harden or break back into separate pieces while the water steams.

**Declared violation types.** process_direction, material_response

**SA**
- S1 [core] A bowl of chocolate sits in a pan of steaming water.
- S2 [core] Some of the chocolate is already liquid and some is still in pieces.
- S3 [core] A spatula stirs the chocolate.
- S4 [core] The remaining pieces melt into the liquid.
- S5 [minor] Steam rises from the water around the bowl.
- S6 [minor] The stirring comes first and the pieces disappear into the liquid after.

**PC**
- P1 [core · process_direction]
  - expect: The pieces only lose their edges and shrink and the liquid share only grows; nothing hardens again while the water steams.
  - fail: A piece grows back; or the liquid turns grainy and separates into pieces again; or the mixture sets firm in the bowl; or pieces reappear where the spatula has smoothed the liquid.
- P2 [core · material_response]
  - expect: The melted chocolate is a thick glossy liquid that flows slowly, holds the spatula's trail for a moment and then levels; the pieces are soft solids that smear.
  - fail: The melted chocolate runs as thin as water; or the surface keeps a sharp ridge where the spatula passed; or a piece shatters into dry shards; or the liquid climbs the spatula and stands up on it.
- P3 [major · gravity_direction]
  - expect: The chocolate settles into the bottom of the bowl and levels; the steam around the bowl rises.
  - fail: Chocolate climbs the bowl's wall and stays above its level; or the steam sinks and pools around the pan; or liquid chocolate lifts off the surface and hangs.
- P4 [major · missing_consequence]
  - expect: The spatula's passage shows: it leaves a trail that fills in behind it and the pieces it meets are pushed along.
  - fail: The spatula passes through the chocolate leaving the surface undisturbed; or the pieces stay put as the spatula sweeps through them; or the surface moves where the spatula never went.
- P5 [fatal · permanence_count]
  - expect: One bowl and one spatula; the chocolate stays in the bowl and pieces become liquid rather than disappearing.
  - fail: A piece vanishes with none of it joining the liquid; or the chocolate's level drops with nothing taken out; or the spatula passes through the bowl; or a second bowl appears.
- P6 [minor · attribute_drift]
  - expect: The bowl's colour, the pan and the spatula stay the same.
  - fail: The bowl changes colour; or the spatula changes shape; or the pan moves on the hob by itself.

## HEAT-0006 · melt_freeze · train

**Caption.** A glowing red-hot metal ball is set on top of a large block of ice, and the ice melts around it.

**Expectation (hidden).** The ice hisses and steams where the ball touches it, meltwater collects at the contact and the ball settles into a growing hollow; the ball's glow dims as it cools and the ice may crack; the ice does not stay untouched, the ball does not glow brighter or float free of the surface, and nothing refreezes while the ball is hot.

**Declared violation types.** process_direction, material_response

**SA**
- S1 [core] A block of ice.
- S2 [core] A glowing metal ball is set on top of the block.
- S3 [core] The ice melts around the ball.
- S4 [minor] The ball glows red at the start.
- S5 [minor] Steam or mist shows at the contact.
- S6 [minor] The ball is placed first and the melting follows.

**PC**
- P1 [core · process_direction]
  - expect: The hollow under the ball only deepens and the ball settles into it; meltwater gathers there and the ice does not close back over.
  - fail: The hollow fills back in; or the ball rises out of it with nothing lifting it; or the meltwater freezes around the glowing ball; or the ice surface returns to smooth and dry.
- P2 [core · material_response]
  - expect: Away from the contact the ice stays a hard solid and may crack sharply; at the contact it turns to water; the ball keeps its round rigid shape.
  - fail: The block sags or bends like wax; or the ice flows as a soft lump; or the ball squashes or spreads; or the whole block turns to slush at once while the ball touches one spot.
- P3 [major · process_direction]
  - expect: The ball's glow only fades while it sits in the ice.
  - fail: The ball's glow brightens as it melts in; or it goes dark and glows again; or the glow spreads out into the ice around it.
- P4 [major · gravity_direction]
  - expect: The ball settles downward into the ice, meltwater runs down the block's sides and pools below, and any steam rises.
  - fail: The ball climbs the block or hangs above its hollow; or meltwater runs up the block's side; or the steam sinks and pools on the ground.
- P5 [fatal · permanence_count]
  - expect: One ball and one block; the block only loses matter and the ball stays whole.
  - fail: The ball vanishes; or a second ball appears; or the block grows; or the ball passes out through the block's base leaving it whole above; or water appears on the block far from the ball with no melt running there.
- P6 [minor · attribute_drift]
  - expect: The ice's look away from the contact and the surface under the block stay the same.
  - fail: The ice turns a colour; or the ground under the block changes texture away from the water; or the block's frosted look changes all over at once.

**Note.** The ball may sink out of sight into the block; it is then judged by the hollow and the meltwater.

## HEAT-0007 · melt_freeze · train

**Caption.** A fruit popsicle stands upright on its stick in a cup on a sunny table, and it drips down the stick.

**Expectation (hidden).** Drips run downward along the stick and collect in the cup; the popsicle looks glossy and soft and may slide on the stick; it does not refreeze, grow, or drip upward.

**Declared violation types.** process_direction, gravity_direction

**SA**
- S1 [core] A popsicle stands upright on its stick in a cup.
- S2 [core] The popsicle is melting: it goes glossy and loses its sharp shape.
- S3 [core] Drips run down the stick.
- S4 [minor] The setting is a sunlit table.
- S5 [minor] Drips collect in the cup below.
- S6 [minor] No hand holds the popsicle.

**PC**
- P1 [core · process_direction]
  - expect: The popsicle only softens and shrinks, and each drip that leaves it does not come back.
  - fail: The popsicle regains a corner or an edge it had lost; or a drip climbs back into it; or the melt alternates between softer and firmer; or the popsicle freezes hard again in the sun.
- P2 [core · gravity_direction]
  - expect: The melt runs downward along the stick and falls or pools in the cup.
  - fail: A drip climbs the stick; or runs up the popsicle's side; or a drop leaves the stick and floats; or melt gathers on top of the popsicle and stays there.
- P3 [major · material_response]
  - expect: The melting popsicle is a soft wet solid that sags and sheds thin coloured liquid, and the stick stays a rigid flat stick.
  - fail: The stick sags or melts with the popsicle; or the melt sets into a spike standing out from the stick; or the popsicle crumbles into dry powder; or a drip stands in a heap on the stick without running.
- P4 [major · missing_consequence]
  - expect: The drips come from the softening popsicle and wet what they pass: the stick darkens where they run.
  - fail: Drips run down the stick while the popsicle above stays hard-edged and dry; or the stick stays dry where drips have passed; or drips start part-way down the stick with nothing above them.
- P5 [fatal · permanence_count]
  - expect: One popsicle on one stick in one cup; matter moves only from popsicle to stick to cup.
  - fail: The popsicle grows; or a second popsicle appears; or the popsicle vanishes while still whole; or liquid appears in the cup with no drip reaching it; or the stick passes through the cup.
- P6 [minor · attribute_drift]
  - expect: The popsicle's colour, the cup and the table stay the same.
  - fail: The popsicle changes colour; or the cup changes shape; or the table's surface changes pattern.

## HEAT-0008 · melt_freeze · train

**Caption.** Icicles hanging from a roof gutter drip steadily in the afternoon sun.

**Expectation (hidden).** Water gathers at each tip and drops fall straight down; the icicles do not grow while dripping, and any change in length is a shortening.

**Declared violation types.** process_direction, gravity_direction

**SA**
- S1 [core] Icicles hang from a roof gutter.
- S2 [core] The icicles drip: drops form and leave their tips.
- S3 [core] The dripping is steady: more than one drop falls.
- S4 [minor] The setting is sunlit.
- S5 [minor] Drops gather at the tips rather than along the shafts.

**PC**
- P1 [core · gravity_direction]
  - expect: Each drop gathers at an icicle's tip, hangs, and then falls straight down away from it.
  - fail: A drop climbs the icicle; or leaves the tip sideways with nothing blowing it; or hangs at the tip and draws back into the ice; or a drop travels upward toward the gutter.
- P2 [core · process_direction]
  - expect: The icicles only shorten or thin; they do not build up while they drip.
  - fail: An icicle lengthens while drops fall from it; or a fallen drop returns and freezes onto the tip; or an icicle thickens; or a drip retreats into the ice.
- P3 [major · material_response]
  - expect: The icicles are hard ice that stays rigid; they glisten as they melt and may snap off.
  - fail: An icicle sags or bends like a rope; or flows as a soft lump; or the ice turns to snow all over at once; or an icicle stretches longer as a drop pulls on its tip.
- P4 [major · missing_consequence]
  - expect: The melt has an effect below: drops land on whatever lies beneath and wet it.
  - fail: Drops land and leave the ground below dry; or drops vanish in mid-air before landing; or the ground is wet in a place no drop reaches.
- P5 [fatal · permanence_count]
  - expect: The icicles keep their number and stay attached to the gutter until they break away.
  - fail: An icicle vanishes while still hanging; or a new icicle appears fully formed; or an icicle passes through the gutter; or the gutter changes shape.
- P6 [minor · attribute_drift]
  - expect: The roof, the gutter and the look of the ice stay the same.
  - fail: The gutter changes colour; or the roof tiles change pattern; or the ice turns a colour.

## HEAT-0009 · melt_freeze · train

**Caption.** An ice cube is dropped into a mug of hot tea, and it melts quickly.

**Expectation (hidden).** The cube floats, its edges round off and it shrinks steadily while faint steam rises from the tea; the tea level may rise slightly as it goes in; the cube does not grow, sink like a stone, vanish in a single frame, or stay sharp-cornered in hot liquid.

**Declared violation types.** process_direction, material_response

**SA**
- S1 [core] A mug of hot tea.
- S2 [core] An ice cube is dropped into the tea.
- S3 [core] The cube melts: its corners round off and it gets smaller.
- S4 [minor] Steam rises from the tea.
- S5 [minor] The cube floats at the surface.
- S6 [minor] The drop comes first and the melting follows.

**PC**
- P1 [core · process_direction]
  - expect: The cube only shrinks and rounds off, and each corner it loses stays lost.
  - fail: The cube regains a sharp corner; or grows; or alternates between smaller and larger; or freezes into a clear block again in the hot tea.
- P2 [core · material_response]
  - expect: The cube is a hard solid that floats mostly submerged and bobs, and the tea is a thin liquid that closes round it.
  - fail: The cube sinks to the bottom like a stone and stays there; or sits wholly on top of the tea like a ball on a sheet; or the cube bends or sags; or the tea holds a dent around the cube like a solid.
- P3 [major · gravity_direction]
  - expect: The cube's melt joins the tea and the tea's surface stays level in the mug.
  - fail: The tea's surface tilts and stays tilted with the mug upright; or water rises out of the mug and hangs above it; or the cube lifts out of the tea into the air.
- P4 [major · missing_consequence]
  - expect: The drop has an effect: the tea splashes or ripples as the cube enters.
  - fail: The cube enters and the surface stays glassy; or the tea ripples before the cube reaches it; or the level drops as the cube goes in.
- P5 [fatal · permanence_count]
  - expect: One cube and one mug; the cube passes into the tea and nowhere else.
  - fail: The cube vanishes in a single frame while still large; or a second cube appears; or the cube passes through the mug's wall; or the mug changes shape.
- P6 [minor · attribute_drift]
  - expect: The mug's pattern, the tea's colour and the table stay the same.
  - fail: The mug changes pattern; or the tea changes colour other than paling where the melt mixes in; or items on the table rearrange.

## HEAT-0010 · melt_freeze · train

**Caption.** A candle burns on a dinner table, and melted wax spills over the rim and runs down one side.

**Expectation (hidden).** The pool sits at the top near the flame; the overflow runs downward and slows as it cools; the candle does not get taller and wax does not flow upward.

**Declared violation types.** process_direction, gravity_direction

**SA**
- S1 [core] A lit candle stands on a table.
- S2 [core] A pool of melted wax sits at the candle's top.
- S3 [core] Wax spills over the rim.
- S4 [core] The wax runs down one side of the candle.
- S5 [minor] The pool lies around the flame at the candle's top.
- S6 [minor] The order is pool, spill over the rim, run down.

**PC**
- P1 [core · gravity_direction]
  - expect: The overflow runs downward along the candle's side from the rim where it spilled.
  - fail: Wax runs up the candle's side; or climbs back over the rim into the pool; or a run travels sideways round the candle and stays level; or a drop leaves the candle and floats.
- P2 [core · process_direction]
  - expect: The run only advances down the side and stops where it has cooled, and what has set stays set.
  - fail: A set run high on the candle turns liquid again with no fresh wax reaching it; or the run retreats up the candle; or the candle grows taller as the wax runs; or the run advances and withdraws in turn.
- P3 [major · material_response]
  - expect: The wax is a thin liquid in the pool near the flame and a dull raised ridge where it has run and cooled.
  - fail: A run stays glossy and runny far below wax that has already set dull above it; or a run sets as a spike standing out sideways from the candle; or the candle's body sags or bends as a whole; or the pool sets into a hard skin while the flame burns in it.
- P4 [major · missing_consequence]
  - expect: The pool sits at the top around the flame and the spill starts at its rim.
  - fail: Wax spills over the rim while the candle's top is dry and solid; or the pool lies away from the flame while the wax beside the flame stays solid; or a run appears part-way down the candle with no wax coming over the rim above it.
- P5 [fatal · permanence_count]
  - expect: One candle with one wick and one flame; wax moves from pool to side to table.
  - fail: The candle grows taller; or a second candle or flame appears; or the flame detaches from the wick and floats; or wax appears on the table with no run reaching it.
- P6 [minor · attribute_drift]
  - expect: The candle's colour, the holder and the table stay the same.
  - fail: The candle changes colour; or the table's pattern changes; or the holder moves or vanishes.

## HEAT-0011 · melt_freeze · train

**Caption.** A marshmallow on a stick is propped over a campfire, and it puffs, softens and sags.

**Expectation (hidden).** The side facing the fire puffs and goes glossy first, then the marshmallow slumps and droops under its own weight, more on the fire side; the surface may brown, blacken in spots, or even catch if close to the flame, and any such darkening deepens and never fades back to white; it does not firm up again while over the heat.

**Declared violation types.** process_direction, material_response, gravity_direction

**SA**
- S1 [core] A marshmallow on a stick is propped over a campfire.
- S2 [core] The marshmallow puffs up: it swells.
- S3 [core] The marshmallow softens and sags.
- S4 [minor] The stick is propped rather than held.
- S5 [minor] The side facing the fire changes first.
- S6 [minor] The puffing comes first and the sagging follows.

**PC**
- P1 [core · process_direction]
  - expect: The change runs one way while the marshmallow is over the fire: it swells, goes glossy and slumps, and any darkening of the surface deepens.
  - fail: The marshmallow firms up and regains its straight sides over the heat; or a darkened patch turns pale again; or it draws back to the shape it started with; or it alternates between puffed and flat.
- P2 [core · material_response]
  - expect: The marshmallow behaves as a softening foam: it swells, its skin goes glossy and slack, and it stretches and droops around the stick.
  - fail: The marshmallow keeps sharp square edges while glossy and sagging; or it runs off the stick as a thin liquid; or it crumbles dry; or it bounces on the stick like rubber.
- P3 [core · gravity_direction]
  - expect: The sag is downward: the soft marshmallow droops below the stick and any drip runs down.
  - fail: The marshmallow droops upward or out sideways with nothing pushing it; or a drip climbs the stick; or the marshmallow lifts off the stick and hangs above it.
- P4 [major · missing_consequence]
  - expect: The change is strongest on the side toward the fire and the far side changes less.
  - fail: The side away from the fire puffs and slumps while the side toward it stays firm; or the marshmallow changes evenly all round while the fire is plainly on one side; or a flame appears on the marshmallow while its surface stays white and unmarked.
- P5 [fatal · permanence_count]
  - expect: One marshmallow on one stick; it stays on the stick and loses matter only by dripping or burning.
  - fail: The marshmallow vanishes while still whole; or a second marshmallow appears; or the marshmallow splits into two whole marshmallows; or the stick passes through the marshmallow and it drops off.
- P6 [minor · attribute_drift]
  - expect: The stick, the fire's logs and the surroundings stay the same.
  - fail: The stick changes colour or length; or the logs rearrange; or the background changes between frames.

**Note.** Browning or blackening of the marshmallow is chemistry and is not judged in itself; what is judged is that any darkening deepens and does not fade.

## HEAT-0012 · melt_freeze · train

**Caption.** An ice cube is flicked onto a hot skillet, and it skitters around and shrinks as it melts.

**Expectation (hidden).** The cube glides and spins on the hot surface with hissing steam, shrinking all the while; it does not sit still, grow, or stay the same size.

**Declared violation types.** process_direction, permanence_count, causeless_motion

**SA**
- S1 [core] A skillet.
- S2 [core] An ice cube is flicked onto the skillet.
- S3 [core] The cube slides about on the surface.
- S4 [core] The cube shrinks.
- S5 [minor] Steam or a wet film shows at the cube's edge.
- S6 [minor] The flick comes first and the sliding and shrinking follow.

**PC**
- P1 [core · process_direction]
  - expect: The cube only shrinks and rounds off while it is on the hot pan.
  - fail: The cube grows; or regains a sharp corner; or freezes into a clear block again; or alternates between smaller and larger.
- P2 [core · causeless_motion]
  - expect: The cube glides and spins because it was flicked and because it rides on its own steam; its path bends only where it meets the pan's slope or wall.
  - fail: The cube darts off at a new angle with nothing touching it and no wall met; or stops dead and sets off again from rest; or climbs the pan's wall and hangs there; or moves against the flick before touching anything.
- P3 [core · permanence_count]
  - expect: The cube turns only into water and steam, and the shrinking cube is the cube that was flicked.
  - fail: The cube vanishes in a single frame while still large; or a second cube appears; or the cube splits into pieces that are each as big as the cube was; or water appears far across the pan with no cube reaching there.
- P4 [major · material_response]
  - expect: The cube stays a hard solid that skids without deforming, and the melt it leaves is a thin film lying on the pan's surface.
  - fail: The cube smears like butter as it slides; or flattens into a pancake; or the melt stands as a dome on the pan; or the cube bounces off the pan like a ball.
- P5 [fatal · solidity]
  - expect: The cube stays on top of the pan's surface and nothing passes through the pan.
  - fail: The cube sinks into the pan's metal; or passes through the pan's wall; or the pan changes shape; or the cube passes through the pan's handle.
- P6 [minor · attribute_drift]
  - expect: The skillet's finish and the hob around it stay the same.
  - fail: The skillet changes colour; or its handle changes shape; or items around the hob rearrange.

## HEAT-0013 · melt_freeze · train

**Caption.** A handful of shredded cheese is scattered onto a hot skillet, and the shreds melt and flow together into a bubbling layer.

**Expectation (hidden).** The shreds slump and go glossy where they touch the pan first, then merge into one layer that bubbles at the edges; they do not stay as separate dry strands or pull back apart.

**Declared violation types.** process_direction, material_response

**SA**
- S1 [core] A skillet.
- S2 [core] Shredded cheese is scattered onto the skillet.
- S3 [core] The shreds melt: they lose their strand shape.
- S4 [core] The melted cheese flows together into one layer.
- S5 [minor] The layer bubbles at its edges.
- S6 [minor] The scattering comes first, then the melting, then the merging.

**PC**
- P1 [core · process_direction]
  - expect: The shreds only soften, slump and join, and the layer's reach only grows; separate strands do not come back.
  - fail: A melted patch separates into dry strands again; or the layer sets firm and matt in the hot pan; or the strands stiffen and stand up again; or the layer alternates between joined and separate.
- P2 [core · material_response]
  - expect: Melting cheese slumps, goes glossy, stretches and pools as a thick liquid that bubbles, and the shreds soften before they join.
  - fail: The shreds run as thin as water; or they shatter dry; or the layer stands as a rigid sheet that keeps its shape when the pan is tilted; or the shreds keep hard square edges while glossy and flowing.
- P3 [major · gravity_direction]
  - expect: The melted cheese runs into the pan's low places and spreads across its floor.
  - fail: The cheese climbs the pan's wall and stays above the floor; or a run travels uphill; or melted cheese lifts off the pan and hangs.
- P4 [major · missing_consequence]
  - expect: The shreds melt where they touch the pan: they go glossy from underneath and the layer forms on the pan's floor.
  - fail: Shreds high on a heap melt while those on the pan stay dry and separate; or a pool spreads on a part of the pan no cheese touched; or bubbles rise through the layer while the cheese is still dry strands.
- P5 [fatal · permanence_count]
  - expect: The cheese in the layer is the cheese that was scattered, and it stays in the pan.
  - fail: The layer grows with no cheese added; or shreds vanish with none joining the layer; or cheese appears outside the pan with none crossing the rim; or the pan changes shape.
- P6 [minor · attribute_drift]
  - expect: The pan's surface and the hob around it stay the same.
  - fail: The pan changes colour; or its handle changes shape; or items around the hob rearrange.

**Note.** Browning of the cheese is chemistry and is not judged.

## HEAT-0014 · melt_freeze · train

**Caption.** A cube of cold butter is dropped into a bowl of hot soup, and the butter melts and spreads across the surface.

**Expectation (hidden).** The cube floats and shrinks while a shiny film spreads out from it over the soup; it does not sink whole or stay solid.

**Declared violation types.** process_direction, gravity_direction

**SA**
- S1 [core] A bowl of hot soup.
- S2 [core] A cube of butter is dropped into the soup.
- S3 [core] The butter melts: the cube shrinks and loses its edges.
- S4 [core] A film of melted butter spreads across the soup's surface.
- S5 [minor] Steam rises from the soup.
- S6 [minor] The drop comes first and the spreading follows.

**PC**
- P1 [core · process_direction]
  - expect: The cube only shrinks while the film at the surface grows, and the film does not gather back into a cube.
  - fail: The cube regains its square edges; or grows; or the film draws back together into a solid lump; or the butter sets into a firm pat on the hot soup.
- P2 [core · gravity_direction]
  - expect: The cube floats at the surface and the film stays at the surface, spreading outward across it.
  - fail: The cube sinks whole to the bottom and stays there; or the film climbs the bowl's wall and stays above the soup; or butter lifts off the surface and hangs above it.
- P3 [major · material_response]
  - expect: The melted butter is a thin glossy film that spreads and breaks into drifting patches, and the cube is a soft solid that floats mostly submerged.
  - fail: The melted butter stands as a dome on the soup; or the film keeps a fixed shape while the soup swirls beneath it; or the cube shatters dry; or the cube sits wholly on top of the soup like a ball on a sheet.
- P4 [major · missing_consequence]
  - expect: The film spreads out from the melting cube and drifts with the soup's movement.
  - fail: A film covers the soup while the cube is still sharp-edged and matt; or the film appears on the far side of the bowl with none spreading from the cube; or the cube shrinks while the surface stays clear of any film.
- P5 [fatal · permanence_count]
  - expect: One cube and one bowl; the butter goes only into the film.
  - fail: The cube vanishes in a single frame while still large; or a second cube appears; or the cube passes through the bowl's wall; or the soup's level drops with nothing taken out.
- P6 [minor · attribute_drift]
  - expect: The bowl's pattern, the soup's colour and the table stay the same.
  - fail: The bowl changes pattern; or the soup changes colour away from where the butter's sheen lies; or items on the table rearrange.

## HEAT-0015 · melt_freeze · train

**Caption.** A small snowball is set on a hot griddle, and it hisses and collapses into water and steam.

**Expectation (hidden).** The snow darkens and slumps from the bottom where it touches the metal, meltwater spreads and sizzles around it and steam rises; the ball does not stay white and firm, grow, or refreeze.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A griddle.
- S2 [core] A snowball is set on the griddle.
- S3 [core] The snowball collapses: it loses its round shape and slumps.
- S4 [core] Water spreads around it and steam rises.
- S5 [minor] The snowball is white and firm at the start.
- S6 [minor] The setting down comes first and the collapse follows.

**PC**
- P1 [core · process_direction]
  - expect: The snowball only darkens, slumps and shrinks, and the wet patch around it only grows.
  - fail: The snowball regains its round shape; or turns white and firm again on the griddle; or the wet patch draws back into the ball; or the ball alternates between firmer and softer.
- P2 [core · permanence_count]
  - expect: The water and steam come from the snowball, which loses matter and gains none.
  - fail: The snowball grows; or a second snowball appears; or the ball vanishes in a single frame while still round; or water appears across the griddle with none running there from the ball.
- P3 [major · gravity_direction]
  - expect: The ball settles downward as it slumps, the meltwater spreads outward across the griddle, and the steam rises.
  - fail: The ball lifts off the griddle; or the meltwater climbs the griddle's edge and stays; or the steam sinks and pools around the griddle.
- P4 [major · material_response]
  - expect: The snow collapses as a wet crumbling solid that slumps from the bottom where it meets the metal, and the melt is a thin film that sizzles.
  - fail: The ball melts from its top while its underside stays white and dry; or the ball bends and flows as one soft lump; or the melt stands as a dome on the griddle; or the ball bounces on the metal.
- P5 [fatal · solidity]
  - expect: The snowball sits on top of the griddle's surface and nothing passes through the metal.
  - fail: The ball sinks into the griddle's metal; or the melt passes through the griddle; or the griddle changes shape; or a second griddle appears.
- P6 [minor · attribute_drift]
  - expect: The griddle's finish and the surroundings stay the same.
  - fail: The griddle changes colour; or its surface pattern changes; or items around it rearrange.

## HEAT-0016 · melt_freeze · train

**Caption.** A candle tips and a drop of liquid wax falls onto a wooden table, where it hardens into a small white disc.

**Expectation (hidden).** The drop spreads slightly on landing, then stops moving and turns from clear to opaque as it sets; it does not keep flowing or become liquid again.

**Declared violation types.** process_direction, material_response, attribute_drift

**SA**
- S1 [core] A candle is tipped to one side.
- S2 [core] A drop of liquid wax falls from it onto a wooden table.
- S3 [core] The drop spreads on landing.
- S4 [core] The wax hardens into a small disc.
- S5 [minor] The set wax is white and dull.
- S6 [minor] The order is fall, spread, set.

**PC**
- P1 [core · process_direction]
  - expect: The drop spreads once as it lands, then stops moving and stays where it set for the rest of the clip.
  - fail: The set disc turns liquid again and flows on with nothing heating it; or the disc draws back into a bead and lifts off the table; or the wax spreads, stops and spreads again with none added.
- P2 [core · material_response]
  - expect: The wax lands as a thin liquid that flows briefly, then sets as a rigid solid: it goes from glossy and see-through to dull and opaque and sits on the wood as one piece.
  - fail: The wax stays a glossy liquid bead for the rest of the clip; or it soaks into the wood and disappears; or the set disc bends or flows when the table is knocked.
- P3 [major · gravity_direction]
  - expect: The drop falls downward from the candle's rim to the table.
  - fail: The drop travels upward from the candle; or hangs in the air part-way down; or moves sideways across the room with nothing blowing it.
- P4 [major · causeless_motion]
  - expect: The candle moves only as it is tipped, and the table and the set disc stay put.
  - fail: The candle rights itself with nothing touching it; or the disc slides across the table; or the table shifts as the drop lands.
- P5 [fatal · permanence_count]
  - expect: One drop leaves the candle and one disc lies on the table; wax neither appears nor vanishes.
  - fail: A second disc appears where no drop landed; or the disc vanishes; or the drop passes through the table; or the candle's wax grows back as the drop leaves.
- P6 [minor · attribute_drift]
  - expect: The candle's colour, the table's grain away from the disc and the room stay the same.
  - fail: The candle changes colour; or the table's grain changes pattern; or objects on the table rearrange.

## HEAT-0017 · melt_freeze · train

**Caption.** Warm chocolate sauce is poured over a scoop of ice cream, and the sauce firms into a crackly shell on the cold surface.

**Expectation (hidden).** The sauce flows down the scoop, slows, and stiffens where it touches the ice cream, turning dull; it does not keep running off the cold scoop.

**Declared violation types.** process_direction, material_response

**SA**
- S1 [core] A scoop of ice cream.
- S2 [core] Chocolate sauce is poured over the scoop.
- S3 [core] The sauce flows down the scoop.
- S4 [core] The sauce firms into a shell on the ice cream.
- S5 [minor] The set shell looks dull rather than glossy.
- S6 [minor] The order is pour, flow, set.

**PC**
- P1 [core · process_direction]
  - expect: The sauce's change runs one way where it lies on the cold scoop: it slows, stops and stays set.
  - fail: A set patch of shell turns runny again and flows on with no fresh sauce over it; or the shell draws back up the scoop; or the shell alternates between glossy and runny and dull and set.
- P2 [core · material_response]
  - expect: The sauce arrives as a thin liquid that flows and coats, and where it sets it is a rigid shell that cracks rather than flows.
  - fail: The set shell sags or drips as the scoop is moved; or the sauce sets as a soft skin that stretches; or the shell crumbles to dust; or the sauce stands as a rigid ridge before it has stopped flowing.
- P3 [major · gravity_direction]
  - expect: The sauce runs downward over the scoop's sides and any excess falls to the dish.
  - fail: The sauce climbs the scoop; or a run travels up over the scoop's top; or a drip leaves the scoop and floats; or sauce gathers under the scoop and rises around it.
- P4 [major · missing_consequence]
  - expect: The ice cream shows the sauce arriving: the surface it covers goes dark, and the scoop goes wet and glossy where the warm sauce lies.
  - fail: Sauce runs over the scoop and the surface under it stays pale and untouched; or the shell forms on a part of the scoop no sauce reached; or the scoop stays sharp-edged and dry where sauce has pooled on it.
- P5 [fatal · permanence_count]
  - expect: One scoop and one stream of sauce; the sauce goes from the jug to the scoop to the dish and nowhere else.
  - fail: Sauce appears on the dish with none running off the scoop; or the scoop grows; or a second scoop appears; or the sauce passes through the scoop and out below it.
- P6 [minor · attribute_drift]
  - expect: The bare ice cream's colour, the dish and the table stay the same.
  - fail: The bare ice cream changes colour; or the dish changes pattern; or items on the table rearrange.

## HEAT-0018 · melt_freeze · train

**Caption.** A bead of hot glue is squeezed from a glue gun onto a piece of wood, a button is pressed into it, and the glue sets hard around the button.

**Expectation (hidden).** The glue comes out clear and runny, pulls a thin string as the gun lifts, and turns firm and cloudy within seconds; it does not stay runny.

**Declared violation types.** process_direction, material_response

**SA**
- S1 [core] A glue gun squeezes a bead of glue onto a piece of wood.
- S2 [core] A button is pressed into the glue.
- S3 [core] The glue sets: it stops moving and holds the button.
- S4 [minor] The glue comes out clear and runny.
- S5 [minor] A thin string of glue trails as the gun lifts.
- S6 [minor] The order is bead, button pressed in, glue set.

**PC**
- P1 [core · process_direction]
  - expect: The glue flows while it leaves the nozzle, then stops spreading and stays put with the button in it.
  - fail: The set glue turns runny again and flows on with nothing heating it; or the bead draws back into the nozzle; or the glue sets and then spreads again with none added; or the button rises back out of the set glue.
- P2 [core · material_response]
  - expect: The glue leaves the nozzle as a thick liquid that mounds and strings, and where it sets it is a firm cloudy solid that holds the button and does not flow.
  - fail: The glue runs off the wood as thin as water; or the set glue stretches like elastic as the button is pushed; or the bead keeps a rigid shape as it leaves the nozzle; or the glue soaks into the wood and disappears.
- P3 [major · gravity_direction]
  - expect: The bead falls from the nozzle down onto the wood and the string of glue hangs and sags from the nozzle.
  - fail: The bead travels upward from the nozzle; or the string stands straight up from the wood; or the bead hangs in the air between nozzle and wood; or glue runs up the gun's nozzle.
- P4 [major · missing_consequence]
  - expect: Pressing the button spreads the glue: it squeezes out around the button's edge and the button sits down into the bead.
  - fail: The button presses in and the glue stays a smooth untouched mound; or glue squeezes out on a part of the wood away from the button; or the button rests on top of the bead with no glue rising around it.
- P5 [fatal · solidity]
  - expect: One button on one bead on the wood; the button sits in the glue and the gun stays outside it; nothing passes through the wood.
  - fail: The button sinks through the wood; or the nozzle passes into the wood; or a second button appears; or the button vanishes into the glue leaving no bulge.
- P6 [minor · attribute_drift]
  - expect: The wood's grain away from the bead, the button's face and the gun stay the same.
  - fail: The wood's grain changes pattern; or the button's face changes design; or the gun changes colour.

## HEAT-0019 · melt_freeze · train

**Caption.** Boiling sugar syrup is drizzled from a spoon into a bowl of ice water, and the syrup hardens instantly into brittle golden threads.

**Expectation (hidden).** The threads set the moment they hit the water and keep the shape they fell in; they do not dissolve, spread, or stay soft.

**Declared violation types.** process_direction, material_response

**SA**
- S1 [core] A bowl of ice water.
- S2 [core] Syrup is drizzled from a spoon into the water.
- S3 [core] The syrup hardens in the water.
- S4 [core] The hardened syrup forms threads.
- S5 [minor] The threads look brittle and golden.
- S6 [minor] The drizzle comes first and the hardening follows.

**PC**
- P1 [core · process_direction]
  - expect: Each thread sets as it enters the water and keeps the shape it fell in; set threads stay set.
  - fail: A set thread softens and runs again in the cold water; or a thread dissolves away into the water; or a thread flattens and spreads on the bowl's floor after setting; or threads join back into a running stream.
- P2 [core · material_response]
  - expect: The syrup is a thick liquid falling from the spoon and a rigid brittle solid in the water: the threads hold their curls and snap rather than bend.
  - fail: The threads bend and sway like string in the water; or stretch when lifted; or the syrup spreads as a cloud through the water; or the threads stay soft and squash together into a lump.
- P3 [major · gravity_direction]
  - expect: The syrup falls downward from the spoon into the water and the threads then sink or hang below the surface.
  - fail: The stream travels upward from the spoon; or a thread rises out of the water; or a thread hangs in the air between spoon and water; or the syrup climbs the spoon.
- P4 [major · missing_consequence]
  - expect: The water shows the syrup arriving: the surface dimples and ripples where the stream lands and the ice shifts.
  - fail: The stream enters and the surface stays glassy; or the water ripples before the stream reaches it; or the ice at the surface stays fixed as the stream pours through it.
- P5 [fatal · permanence_count]
  - expect: The threads in the water are the syrup that fell; the bowl and spoon keep their shape.
  - fail: Threads appear in the water with none falling there; or a thread vanishes; or the syrup passes through the bowl's wall; or a second spoon appears.
- P6 [minor · attribute_drift]
  - expect: The bowl, the spoon and the ice stay the same.
  - fail: The bowl changes colour; or the spoon changes shape; or a thread changes colour after setting.

## HEAT-0020 · melt_freeze · train

**Caption.** A hairdryer is aimed at crayons taped to the top of a canvas, and the crayons melt and run down the canvas in coloured streaks that harden lower down.

**Expectation (hidden).** The wax flows downward only while heated, slows as it cools away from the dryer, and stops as a raised hardened streak; it does not run upward or stay liquid at the bottom.

**Declared violation types.** process_direction, gravity_direction, material_response

**SA**
- S1 [core] Crayons are taped to the top of a canvas.
- S2 [core] A hairdryer is aimed at the crayons.
- S3 [core] The crayons melt.
- S4 [core] Coloured wax runs down the canvas.
- S5 [minor] The streaks harden lower down the canvas.
- S6 [minor] The order is heat, melt, run down, harden.

**PC**
- P1 [core · gravity_direction]
  - expect: The melted wax runs downward from each crayon's tip, straight down the canvas.
  - fail: A streak runs upward from a crayon; or travels sideways across the canvas and stays level; or a drop of wax leaves the canvas and floats; or wax gathers above the crayons.
- P2 [core · process_direction]
  - expect: Each streak only grows downward while heat is on it, and where it has stopped and set it stays set.
  - fail: A streak retreats back up toward its crayon; or a set streak low on the canvas runs again with no fresh wax reaching it; or a streak's colour drains away leaving the canvas bare; or the crayons grow back as the streaks lengthen.
- P3 [core · material_response]
  - expect: The wax is a thin liquid where the dryer plays on it and a raised dull ridge where it has cooled; the crayon bodies soften and slump at the tip.
  - fail: A streak stays glossy and runny far from the dryer while wax nearer the heat has already set dull; or a streak sets as a spike standing out from the canvas; or the canvas sags or melts with the wax; or the crayons shatter dry.
- P4 [major · missing_consequence] (if: The hairdryer's nozzle and the direction it points are in view.)
  - expect: The melting follows the dryer: crayons in its stream melt and run while ones away from it stay solid.
  - fail: Crayons the dryer is not aimed at run while the ones in its stream stay solid; or every crayon runs at once while the dryer is plainly aimed at one; or a streak appears below a crayon that is still whole and dry.
- P5 [major · causeless_motion]
  - expect: The canvas and the crayons stay put; the crayons change only by softening at the tip.
  - fail: A crayon slides across the canvas with nothing pushing it; or the canvas swings or tips with nothing touching it; or a crayon leaves the canvas while its tape still holds it.
- P6 [fatal · permanence_count]
  - expect: The crayons stay taped where they are and the wax on the canvas came down from them.
  - fail: A streak appears with no crayon above it; or a crayon vanishes while still whole; or a new crayon appears on the canvas; or wax passes through the canvas and shows on its back.
- P7 [minor · attribute_drift]
  - expect: Each streak keeps its crayon's colour, and the bare canvas and the wall behind stay the same.
  - fail: A streak is a colour no crayon has; or the bare canvas changes shade; or the wall behind changes.

## HEAT-0021 · melt_freeze · train

**Caption.** Hot caramel is poured onto a cold marble slab, and the caramel spreads, then stiffens into a glassy sheet.

**Expectation (hidden).** The caramel spreads while hot, slows, and stops moving as it sets; the sheet is rigid and can be cracked; it does not keep flowing off the slab.

**Declared violation types.** process_direction, material_response

**SA**
- S1 [core] A marble slab.
- S2 [core] Hot caramel is poured onto the slab.
- S3 [core] The caramel spreads across the slab.
- S4 [core] The caramel stiffens into a sheet.
- S5 [minor] The set sheet looks glassy.
- S6 [minor] The order is pour, spread, stiffen.

**PC**
- P1 [core · process_direction]
  - expect: The caramel spreads while it is hot, then slows and stops and stays where it has set.
  - fail: A set part of the sheet flows again with nothing heating it; or the sheet draws back toward the point where it was poured; or the caramel spreads, stops and spreads again with none added; or the sheet alternates between runny and set.
- P2 [core · material_response]
  - expect: The caramel arrives as a thick liquid that flows and levels and sets as a rigid brittle sheet that cracks rather than bends.
  - fail: The set sheet bends or sags when lifted; or stretches like toffee when pulled; or the caramel runs as thin as water over the slab; or the sheet crumbles to powder as it sets.
- P3 [major · gravity_direction]
  - expect: The caramel runs downhill across the slab and over its edge where the slab slopes, and the pour falls downward from the pan.
  - fail: The caramel climbs the slab's raised edge and stays; or flows uphill across the slab; or the stream travels upward from the pan; or the sheet lifts off the slab and hangs.
- P4 [major · missing_consequence]
  - expect: The slab shows the caramel arriving: the sheet is thickest where the pour landed and thins outward, and it fills the slab's hollows.
  - fail: The sheet is thickest far from where the pour landed with nothing moving it there; or caramel appears on a part of the slab the flow never reached; or the sheet bridges over a hollow in the slab without touching it.
- P5 [fatal · permanence_count]
  - expect: One pour and one sheet; the caramel goes from the pan onto the slab and nowhere else.
  - fail: Caramel appears on the slab with none pouring there; or the sheet vanishes; or the caramel passes through the slab; or a second sheet appears.
- P6 [minor · attribute_drift]
  - expect: The slab's veining away from the caramel and the surroundings stay the same.
  - fail: The slab's veining changes pattern; or the pan changes shape; or items around the slab rearrange.

**Note.** The caramel's colour is the product of cooking done before the clip; further darkening is chemistry and is not judged.

## HEAT-0022 · melt_freeze · train

**Caption.** Melted butter is poured onto a plate that has just come out of the freezer, and the butter turns cloudy and firm on the plate.

**Expectation (hidden).** The clear yellow liquid goes opaque pale and stops flowing within seconds of touching the cold plate; it does not stay glossy and runny.

**Declared violation types.** process_direction, attribute_drift

**SA**
- S1 [core] A plate that reads as very cold: frost or chill haze on it.
- S2 [core] Melted butter is poured onto the plate.
- S3 [core] The butter turns cloudy.
- S4 [core] The butter stops flowing and becomes firm.
- S5 [minor] The butter is clear and runny as it is poured.
- S6 [minor] The order is pour, cloud over, firm up.

**PC**
- P1 [core · process_direction]
  - expect: The change runs one way on the cold plate: the butter slows, clouds and stops, and where it has set it stays set.
  - fail: A clouded patch turns clear and runny again with nothing heating it; or the butter clouds and clears in turn; or the set butter flows on across the plate with none added; or the pool draws back toward the point where it was poured.
- P2 [core · attribute_drift]
  - expect: The change from clear to cloudy happens in the butter where it lies on the cold plate and spreads through it.
  - fail: The plate's pattern changes rather than the butter; or the butter clouds in the jug before it is poured; or a clouded area returns to clear while still on the plate; or the cloudiness appears on a part of the plate with no butter on it.
- P3 [major · gravity_direction]
  - expect: The poured butter falls downward into the plate and spreads out level in its well.
  - fail: The butter climbs the plate's rim and stays above it; or the stream travels upward from the jug; or the pool stands as a dome above the plate's rim; or butter lifts off the plate and hangs.
- P4 [major · material_response]
  - expect: The butter flows as a thin liquid while it is warm and becomes a soft opaque solid that keeps its shape when the plate is tilted.
  - fail: The set butter runs off a tilted plate as a liquid; or the butter sets into a glassy sheet that shatters; or the pool stretches like elastic; or the butter soaks into the plate.
- P5 [fatal · permanence_count]
  - expect: One plate and one pour; the butter that lands stays on the plate.
  - fail: Butter appears on the plate with none pouring there; or the pool vanishes; or the butter passes through the plate; or a second plate appears.
- P6 [minor · attribute_drift]
  - expect: The plate's pattern away from the butter, the jug and the surroundings stay the same.
  - fail: The plate's pattern changes; or the jug changes shape; or items around the plate rearrange.

## HEAT-0023 · melt_freeze · train

**Caption.** On a bitterly cold winter morning a cup of water is splashed onto a frozen car windshield, and the water freezes into a film of ice on the glass.

**Expectation (hidden).** The water runs briefly and then stops, turning white and opaque where it freezes; the ice does not run off afterwards or clear the glass.

**Declared violation types.** process_direction, material_response

**SA**
- S1 [core] A car windshield covered in frost or ice.
- S2 [core] Water is splashed onto the glass from a cup.
- S3 [core] The water runs briefly on the glass.
- S4 [core] The water freezes into a film of ice on the glass.
- S5 [minor] The setting reads as bitterly cold: frost, snow or ice around.
- S6 [minor] The order is splash, run, freeze.

**PC**
- P1 [core · process_direction]
  - expect: The water runs, slows and stops where it freezes, and the frozen film then stays.
  - fail: A frozen patch turns back to running water with nothing warming it; or the film goes and leaves the glass bare; or the water runs, freezes and runs again in steps; or the film retreats up the glass.
- P2 [core · attribute_drift]
  - expect: Where the water freezes the glass turns white and opaque and stays so; the change is in the film, not in the clear glass elsewhere.
  - fail: The frozen film turns clear so the glass ends cleaner than before; or the whole windshield turns white at once including where no water landed; or the film's white fades back to clear while the cold holds; or the car's paint changes rather than the glass.
- P3 [major · gravity_direction]
  - expect: The splashed water runs downward over the glass before it sets, and the film is thickest along its downward path.
  - fail: The water runs up the windshield; or the film builds above where the water landed; or water splashes upward off the glass and stays in the air.
- P4 [major · material_response]
  - expect: The water flows as a thin liquid and becomes a hard film stuck to the glass that could be scraped; it does not stay a mobile liquid.
  - fail: The film ripples or flows when the glass is touched; or the water sets as a soft jelly that dents; or the film peels off as a rubbery sheet; or the water beads up and rolls off the glass without wetting it.
- P5 [fatal · permanence_count]
  - expect: One cup of water lands on one windshield; the ice on the glass is the water that was splashed.
  - fail: Ice appears on the glass where no water landed; or the film vanishes at a stroke; or the water passes through the glass into the car; or a second cup appears.
- P6 [minor · attribute_drift]
  - expect: The car's paint, the wipers and the surroundings stay the same.
  - fail: The car changes colour; or the wipers jump to a new position with nothing touching them; or the background changes between frames.

## HEAT-0024 · melt_freeze · train

**Caption.** Hot bacon fat is poured into a glass jar straight from the fridge, and the fat begins to set where it touches the cold glass.

**Expectation (hidden).** Solid white forms first at the cold glass walls and creeps inward; the fat stops sloshing as it sets; it does not turn clear again.

**Declared violation types.** process_direction, attribute_drift

**SA**
- S1 [core] A glass jar that reads as cold: frost or condensation on it.
- S2 [core] Hot fat is poured into the jar.
- S3 [core] The fat begins to set where it touches the glass.
- S4 [core] Solid white fat forms at the jar's walls.
- S5 [minor] The poured fat is clear and runny.
- S6 [minor] The order is pour, set at the walls, spread inward.

**PC**
- P1 [core · process_direction]
  - expect: The setting runs one way: the white grows from the cold glass inward and the fat's surface stops sloshing.
  - fail: The white creeps back to the glass leaving the fat clear again; or the set fat turns runny with nothing heating it; or the white appears in the middle first and works out to the glass; or the fat sets and melts in turn.
- P2 [core · attribute_drift]
  - expect: The change from clear to white happens in the fat itself, at the cold glass, and spreads through it.
  - fail: The jar's glass turns white rather than the fat; or the white appears in the pan before the fat is poured; or the white fades back to clear while the jar is still cold; or the label on the jar changes rather than the fat.
- P3 [major · gravity_direction]
  - expect: The fat falls downward into the jar and lies level in it, its surface flat while the jar stands upright.
  - fail: The fat climbs the jar's wall above its level and stays; or the stream travels upward from the pan; or the fat's surface tilts and stays tilted with the jar upright; or fat lifts out of the jar's mouth.
- P4 [major · material_response]
  - expect: The hot fat is a thin liquid that pours and sloshes and the set fat is a soft opaque solid that keeps its shape when the jar is moved.
  - fail: The set fat sloshes when the jar is tilted; or the fat sets into a glassy solid that cracks; or the fat stretches like dough as it is poured; or the liquid fat stands in a heap above its level.
- P5 [fatal · permanence_count]
  - expect: One jar and one pour; the fat that goes in stays in.
  - fail: The fat's level drops with none poured out; or fat appears in the jar with none pouring in; or the fat passes through the jar's wall; or a second jar appears.
- P6 [minor · attribute_drift]
  - expect: The jar's label, the pan and the counter stay the same.
  - fail: The label changes; or the pan changes shape; or items on the counter rearrange.

## HEAT-0025 · melt_freeze · train

**Caption.** A frozen fish fillet is laid in a hot pan, and the white frost on its surface disappears as the fillet thaws.

**Expectation (hidden).** The frost vanishes from the pan side first with a hiss and the fillet turns from stiff to limp; the frost does not return.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A frying pan.
- S2 [core] A frozen fish fillet is laid in the pan.
- S3 [core] The white frost on the fillet disappears.
- S4 [core] The fillet goes from stiff to limp.
- S5 [minor] Water or steam shows at the fillet's edge.
- S6 [minor] The frost goes from the pan side first.

**PC**
- P1 [core · process_direction]
  - expect: The frost only disappears, starting where the fillet meets the pan, and bare areas stay bare.
  - fail: The frost grows back on a bare part of the fillet; or the frost spreads over the fillet in the hot pan; or the frost comes and goes in patches; or the fillet stiffens again after going limp.
- P2 [core · permanence_count]
  - expect: The frost turns to water and steam at the fillet's surface, and the fillet stays one piece.
  - fail: The frost goes with nothing wet or steaming at the fillet; or frost appears on the pan away from the fillet; or the fillet splits into two whole fillets; or the fillet vanishes.
- P3 [major · material_response]
  - expect: The fillet begins as a stiff board that lies rigid and becomes a limp slab that settles into the pan's shape.
  - fail: The fillet stays rigid and stands proud of the pan while its frost has gone and it looks wet; or the fillet flows like a liquid; or the fillet shatters like glass; or the fillet stiffens into a curl and stays rigid.
- P4 [major · gravity_direction]
  - expect: Melted frost runs to the pan's low places and pools around the fillet, and any steam rises.
  - fail: The water climbs the pan's wall and stays; or a run of water travels uphill; or the steam sinks and pools around the pan; or the fillet lifts off the pan.
- P5 [fatal · solidity]
  - expect: The fillet lies on top of the pan's surface and nothing passes through the pan.
  - fail: The fillet sinks into the pan's metal; or the water passes through the pan; or the pan changes shape; or a second pan appears.
- P6 [minor · attribute_drift]
  - expect: The pan's finish and the hob around it stay the same.
  - fail: The pan changes colour; or its handle changes shape; or items around the hob rearrange.

**Note.** The fish's colour change as it cooks is chemistry and is not judged.

## HEAT-0026 · melt_freeze · train

**Caption.** A bag of frozen peas is emptied into a pot of hot water, and the frost on them vanishes and the clumps break apart.

**Expectation (hidden).** The frozen clumps separate as they thaw and the peas sink or bob individually; the frost does not reappear.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A pot of hot water.
- S2 [core] Frozen peas are emptied into the pot from a bag.
- S3 [core] The frost on the peas disappears.
- S4 [core] The frozen clumps break apart into separate peas.
- S5 [minor] Steam rises from the water.
- S6 [minor] The order is emptied in, frost gone, clumps apart.

**PC**
- P1 [core · process_direction]
  - expect: The frost only disappears and the clumps only break apart; loose peas do not join back up.
  - fail: Loose peas gather back into a frozen clump; or frost grows back on the peas in the hot water; or a clump breaks apart and forms again; or the frost comes and goes.
- P2 [core · permanence_count]
  - expect: The peas that fall in are the peas in the pot; none appears or vanishes.
  - fail: Peas vanish from the pot; or peas appear in the water with none falling there; or two peas merge into one; or the pot's contents rise with nothing added.
- P3 [major · gravity_direction]
  - expect: The peas fall downward from the bag into the water and sink or ride at the surface, and the clumps drop to the pot's floor.
  - fail: Peas travel upward out of the bag; or hang in the air between bag and pot; or a pea rises out of the water and stays above it; or the peas gather on the pot's rim.
- P4 [major · material_response]
  - expect: The clumps are frozen lumps that hold together until they loosen and then let go pea by pea, and the peas stay firm round grains.
  - fail: A clump melts into a smooth paste; or the peas squash flat in the water; or a clump stays a single rigid lump while frost-free and tumbling in the boil; or the peas dissolve away.
- P5 [fatal · shape_identity]
  - expect: The pot keeps its shape, the bag stays a bag and nothing passes through the pot's wall.
  - fail: The peas pass through the pot's wall; or the pot changes shape; or the bag turns into another object; or a second pot appears.
- P6 [minor · attribute_drift]
  - expect: The pot, the bag's printing and the hob stay the same.
  - fail: The pot changes colour; or the bag's printing changes; or items around the hob rearrange.

**Note.** The peas' colour brightening as they cook is not judged.

## HEAT-0027 · melt_freeze · train

**Caption.** A wax crayon lies on a hot skillet, and it softens, slumps, and melts into a coloured pool.

**Expectation (hidden).** The crayon sags and loses its shape from the side touching the pan, and a pool of the same colour spreads out from it; it does not stay stiff, straighten, or change colour.

**Declared violation types.** process_direction, material_response, gravity_direction

**SA**
- S1 [core] A skillet.
- S2 [core] A wax crayon lies on the skillet.
- S3 [core] The crayon softens and slumps.
- S4 [core] The crayon melts into a pool.
- S5 [minor] The pool is the same colour as the crayon.
- S6 [minor] The softening comes first and the pool follows.

**PC**
- P1 [core · process_direction]
  - expect: The crayon only softens, slumps and shrinks while the pool grows; it does not firm up again on the pan.
  - fail: The crayon straightens or regains its round shape; or the pool draws back into the crayon; or the wax sets into a solid stick again in the pan; or the crayon alternates between stiff and slumped.
- P2 [core · material_response]
  - expect: The crayon is a soft solid that bends and sags from the side touching the metal and the melt is a thin liquid that spreads.
  - fail: The crayon shatters into dry pieces; or the pool stands as a rigid dome; or the crayon stretches like elastic; or the melt moves as a solid slab across the pan.
- P3 [core · gravity_direction]
  - expect: The crayon sags downward onto the pan and the pool spreads outward and downhill across it.
  - fail: The crayon bends upward with nothing lifting it; or the pool climbs the pan's wall and stays; or melted wax lifts off the pan; or the pool gathers uphill of the crayon on a tilted pan.
- P4 [major · missing_consequence]
  - expect: The crayon melts where it touches the metal: it goes glossy underneath first and the pool spreads from beneath it.
  - fail: The crayon melts from its top face while its underside stays matt and sharp; or a pool spreads on a part of the pan the crayon never touched; or the crayon slumps while the pan around it stays dry.
- P5 [fatal · permanence_count]
  - expect: One crayon; the wax goes only into the pool.
  - fail: The crayon grows; or a second crayon appears; or the crayon vanishes while still whole; or wax appears across the pan with none flowing there.
- P6 [minor · attribute_drift]
  - expect: The pool keeps the crayon's colour, and the pan's finish and the surroundings stay the same.
  - fail: The pool is a different colour from the crayon; or the pan changes colour; or items around the pan rearrange.

## HEAT-0028 · melt_freeze · train

**Caption.** A block of frozen orange juice is dropped into a jug of hot water, and it melts, the orange colour spreading into the water.

**Expectation (hidden).** The block rounds off and shrinks while orange streaks sink and spread from it and the water turns steadily more orange; the block does not grow and the water does not clear again.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A jug of hot water.
- S2 [core] A block of frozen orange juice is dropped into the jug.
- S3 [core] The block melts: it rounds off and shrinks.
- S4 [core] Orange colour spreads through the water.
- S5 [minor] Streaks of orange run from the block.
- S6 [minor] The drop comes first and the colouring follows.

**PC**
- P1 [core · process_direction]
  - expect: The block only shrinks while the water grows more orange, and the colour does not gather back.
  - fail: The block grows; or the water clears again while the block is still shrinking; or the colour draws back into the block; or the block regains a sharp corner.
- P2 [core · permanence_count]
  - expect: The colour in the water came out of the block, which loses matter and gains none.
  - fail: A second block appears; or the block vanishes in a single frame while still large; or the water turns orange with no streaks leaving the block; or orange appears in the jug before the block is in.
- P3 [major · gravity_direction]
  - expect: The block floats or rests in the water and the orange streaks sink and spread from it; the surface stays level in the jug.
  - fail: The streaks climb out of the water; or the block rises out of the water and hangs above it; or the surface tilts and stays tilted with the jug upright; or streaks rise from the jug's floor with no block there.
- P4 [major · material_response]
  - expect: The block is a hard solid that rounds off as it melts and the juice mixes as a liquid that streaks and blends; the water closes around the block.
  - fail: The block bends or sags as one lump; or the juice moves as a solid mass through the water; or the block crumbles to dry powder; or the water holds a dent around the block like a solid.
- P5 [fatal · solidity]
  - expect: One jug and one block; the block stays in the water and passes through nothing.
  - fail: The block passes through the jug's wall; or the jug changes shape; or the block passes out through the jug's base; or the block merges with the jug's handle.
- P6 [minor · attribute_drift]
  - expect: The jug's shape and markings and the surroundings stay the same.
  - fail: The jug changes colour; or its markings change; or items around the jug rearrange.

## HEAT-0029 · melt_freeze · train

**Caption.** A spoonful of solid white coconut oil is dropped into a hot frying pan, and it melts into clear liquid.

**Expectation (hidden).** The white lump turns glossy and clear from the bottom where it touches the pan and shrinks as a colourless pool spreads out around it; the pool stays clear with no foam or browning, and the oil does not stay white and solid or turn white again in the hot pan.

**Declared violation types.** process_direction, attribute_drift

**SA**
- S1 [core] A frying pan.
- S2 [core] A spoonful of white solid coconut oil is dropped into the pan.
- S3 [core] The oil melts.
- S4 [core] The melted oil is clear liquid.
- S5 [minor] A clear pool spreads out around the shrinking lump.
- S6 [minor] The order is white lump, melting, clear pool.

**PC**
- P1 [core · process_direction]
  - expect: The lump only shrinks while the clear pool grows; it does not firm up again in the pan.
  - fail: The lump regains the shape it was spooned in; or the pool draws back into the lump; or the oil sets white and solid again in the pan; or the lump alternates between larger and smaller.
- P2 [core · attribute_drift]
  - expect: The change from white to clear happens in the oil where it melts, starting at the pan, and the clear pool stays clear.
  - fail: The clear pool turns white again while the pan is hot; or the lump melts into a liquid that stays milky; or the pan's surface changes colour rather than the oil; or the lump turns clear before it has begun to melt.
- P3 [major · gravity_direction]
  - expect: The pool spreads outward and downhill over the pan's floor and runs to its low side.
  - fail: The pool climbs the pan's wall and stays; or a run of oil travels uphill; or oil lifts off the pan and floats; or the pool gathers above the lump.
- P4 [major · missing_consequence]
  - expect: The lump melts where it touches the metal: it goes clear and glossy underneath and the pool spreads from beneath it.
  - fail: The lump melts from its top while its underside stays white and matt; or a pool spreads on a part of the pan the lump never touched; or the lump shrinks while the pan around it stays dry.
- P5 [fatal · permanence_count]
  - expect: One spoonful of oil; the oil goes only from the lump into the pool.
  - fail: The lump grows; or a second lump appears; or the lump vanishes while still large; or oil appears across the pan with none flowing there.
- P6 [minor · attribute_drift]
  - expect: The pan's finish, the spoon and the hob stay the same.
  - fail: The pan changes colour; or the spoon changes shape; or items around the hob rearrange.

**Note.** Browning or foaming of the oil is chemistry and is not judged; the caption's point is that the melt is clear rather than white.

## HEAT-0030 · melt_freeze · train

**Caption.** A wedge of cheese sits under the heating element of a raclette grill, and the face nearest the element softens, sags and drips.

**Expectation (hidden).** Only the face toward the heat softens and goes glossy; drips run downward off the lowest point onto the plate below; the far side stays firm and the cheese does not stiffen again under the heat.

**Declared violation types.** process_direction, gravity_direction

**SA**
- S1 [core] A wedge of cheese sits under a grill's heating element.
- S2 [core] The face nearest the element softens and goes glossy.
- S3 [core] That face sags.
- S4 [core] Cheese drips from the wedge.
- S5 [minor] The far side of the wedge stays firm.
- S6 [minor] The softening comes first and the dripping follows.

**PC**
- P1 [core · process_direction]
  - expect: The softening only advances on the face toward the element and the sag only deepens; the cheese does not stiffen again under the heat.
  - fail: The sagging face pulls back up into a flat firm face; or a drip retreats into the wedge; or the softened face turns matt and firm again under the element; or the wedge alternates between sagging and firm.
- P2 [core · gravity_direction]
  - expect: The softened cheese sags downward and drips fall from the wedge's lowest point onto what is below.
  - fail: The cheese sags upward toward the element; or a drip climbs the wedge; or a drop leaves the wedge and hangs in the air; or melted cheese gathers on the wedge's top face and stays there.
- P3 [major · missing_consequence]
  - expect: The change is strongest on the face toward the element and least on the side away from it.
  - fail: The face away from the element sags while the face toward it stays firm; or the whole wedge softens evenly while the element is plainly on one side; or the wedge drips while its surface stays matt and dry.
- P4 [major · material_response]
  - expect: The softening cheese is a thick liquid that stretches and drips slowly and the rest of the wedge stays a firm solid with a cut edge.
  - fail: The melted cheese runs as thin as water; or the whole wedge slumps as one soft lump; or the softened face stretches into a strand that snaps back like elastic; or the cheese shatters dry.
- P5 [fatal · permanence_count]
  - expect: One wedge; the cheese goes only from the wedge to what lies below.
  - fail: The wedge grows; or a second wedge appears; or the wedge vanishes while still whole; or cheese appears on the plate with no drip reaching it.
- P6 [minor · attribute_drift]
  - expect: The grill's frame, the plate and the surroundings stay the same.
  - fail: The grill changes shape; or the plate changes pattern; or items around the grill rearrange.

**Note.** Browning of the cheese's surface is chemistry and is not judged.

## HEAT-0031 · melt_freeze · train

**Caption.** Warm water is poured over a frosted car windshield on a cold morning, and the frost clears where the water runs.

**Expectation (hidden).** The frost turns clear along the path of the water and the water runs downward off the glass; frost does not re-form on the wetted glass while the water is warm, and untouched areas stay frosted.

**Declared violation types.** process_direction, gravity_direction

**SA**
- S1 [core] A frosted car windshield.
- S2 [core] Water is poured over the glass.
- S3 [core] The frost clears where the water runs.
- S4 [core] The water runs down off the glass.
- S5 [minor] Parts of the glass the water misses stay frosted.
- S6 [minor] The pour comes first and the clearing follows.

**PC**
- P1 [core · process_direction]
  - expect: The frost only clears along the water's path, and cleared glass stays clear while the water keeps coming.
  - fail: Frost grows back on glass the water has just cleared; or the frost clears on a part of the glass the water never reached; or the clearing spreads and shrinks in turn; or the whole windshield clears at once while the water runs down one strip.
- P2 [core · gravity_direction]
  - expect: The water runs downward over the glass and off its lower edge or onto the bonnet.
  - fail: The water runs up the windshield; or a run travels sideways and stays level with nothing tilting the car; or water leaves the glass and rises; or the water stands on the sloping glass without running down.
- P3 [major · missing_consequence]
  - expect: The glass shows the water arriving: it goes clear and wet where the water runs and the frost's edge is pushed back along that path.
  - fail: Water runs over frosted glass and it stays white and dry; or the clear path lies away from where the water runs; or the frost's edge stays fixed while water pours across it.
- P4 [major · material_response]
  - expect: The frost is a thin white crust that wets and goes as the water passes, and the water is a thin liquid that sheets and streaks.
  - fail: The frost lifts off as a rigid sheet and slides away; or the water beads up and rolls off without wetting the glass; or the water runs as a thick syrup.
- P5 [fatal · permanence_count]
  - expect: One windshield; the water runs over the glass and off it and nothing passes through.
  - fail: The water passes through the glass into the car; or the windshield changes shape; or a second windshield appears; or the frost returns all over at a stroke with the car untouched.
- P6 [minor · attribute_drift]
  - expect: The car's paint, the wipers and the surroundings stay the same.
  - fail: The car changes colour; or the wipers jump to a new position with nothing touching them; or the background changes between frames.

## HEAT-0032 · melt_freeze · train

**Caption.** A handful of chocolate chips is dropped into a saucepan of hot cream, and the chips melt into the cream.

**Expectation (hidden).** The chips soften, lose their sharp edges and go glossy, sinking or smearing into the cream while dark streaks spread through the pale cream; the chips do not stay hard-edged, float unchanged, or re-harden in the hot cream.

**Declared violation types.** process_direction, material_response

**SA**
- S1 [core] A saucepan of cream.
- S2 [core] Chocolate chips are dropped into the cream.
- S3 [core] The chips melt: they lose their shape.
- S4 [core] Dark streaks spread through the pale cream.
- S5 [minor] Steam rises from the cream.
- S6 [minor] The drop comes first and the melting follows.

**PC**
- P1 [core · process_direction]
  - expect: The chips only soften, lose their edges and shrink while the cream grows darker; chips do not form again.
  - fail: A chip regains its pointed shape; or dark streaks gather back into a chip; or the mixture separates into pale cream and hard chips again; or the chips alternate between hard and soft.
- P2 [core · material_response]
  - expect: The melting chocolate is a thick liquid that smears and blends into the cream and the chips are soft solids that squash rather than shatter.
  - fail: A chip shatters into dry shards; or the melted chocolate runs as thin as water and sits apart on top; or a chip stays hard-edged while glossy and smearing; or the mixture sets into a rigid block in the hot pan.
- P3 [major · gravity_direction]
  - expect: The chips sink into the cream or sit in it and the dark streaks sink and spread; the cream's surface stays level.
  - fail: A chip rises out of the cream and hangs above it; or the streaks climb the pan's wall and stay; or the surface tilts and stays tilted with the pan level; or chocolate gathers on the pan's rim.
- P4 [major · missing_consequence]
  - expect: The chips show the hot cream around them: they go glossy where they are wetted and the cream darkens where they lie.
  - fail: The chips sit in the cream sharp-edged and matt while the cream darkens; or the cream darkens on the far side of the pan from the chips with nothing stirring it there; or the chips soften while the cream stays pale everywhere.
- P5 [fatal · permanence_count]
  - expect: The chips that go in are the chips in the pan and the pan's contents gain nothing.
  - fail: Chips appear in the pan with none falling in; or a chip vanishes with none of it joining the cream; or the pan's level rises with nothing added; or a chip passes through the pan's wall.
- P6 [minor · attribute_drift]
  - expect: The pan, the hob and the surroundings stay the same.
  - fail: The pan changes colour; or its handle changes shape; or items around the hob rearrange.

## HEAT-0033 · melt_freeze · train

**Caption.** A square of chocolate lies in a skillet over low heat, and it melts into a spreading pool.

**Expectation (hidden).** The square goes glossy and sags from the bottom, its edges round off and a pool spreads out around it; it does not keep sharp edges, re-harden in the warm pan, or turn pale.

**Declared violation types.** process_direction, material_response

**SA**
- S1 [core] A skillet.
- S2 [core] A square of chocolate lies in the skillet.
- S3 [core] The square melts: it goes glossy and loses its edges.
- S4 [core] A pool of chocolate spreads around it.
- S5 [minor] The square starts with straight sharp edges.
- S6 [minor] The melting comes first and the pool follows.

**PC**
- P1 [core · process_direction]
  - expect: The square only softens and shrinks while the pool grows; nothing hardens again in the warm pan.
  - fail: The square regains its sharp edges; or the pool draws back into the square; or the chocolate sets firm and matt again in the pan; or the square alternates between firmer and softer.
- P2 [core · material_response]
  - expect: The melted chocolate is a thick glossy liquid that flows slowly and levels, and the square is a soft solid that slumps and smears.
  - fail: The melted chocolate runs as thin as water; or the square shatters into dry shards; or the pool stands as a rigid dome; or the square keeps sharp edges while glossy and flowing.
- P3 [major · gravity_direction]
  - expect: The pool spreads outward and downhill across the pan's floor and runs to its low side.
  - fail: The pool climbs the pan's wall and stays; or a run travels uphill; or melted chocolate lifts off the pan and floats.
- P4 [major · missing_consequence]
  - expect: The square melts where it touches the pan: it goes glossy underneath first and the pool spreads from beneath it.
  - fail: The square melts from its top face while its underside stays matt and sharp; or a pool spreads on a part of the pan the square never touched; or the square slumps while the pan around it stays dry.
- P5 [fatal · permanence_count]
  - expect: One square; the chocolate goes only into the pool.
  - fail: The square grows; or a second square appears; or the square vanishes while still whole; or chocolate appears across the pan with none flowing there.
- P6 [minor · attribute_drift]
  - expect: The pool keeps the square's dark colour, and the pan's finish and the hob stay the same.
  - fail: The chocolate turns pale; or the pan changes colour; or items around the hob rearrange.

## HEAT-0034 · melt_freeze · train

**Caption.** Hot espresso is poured over a scoop of vanilla ice cream in a glass, and the ice cream melts.

**Expectation (hidden).** The scoop softens and shrinks where the hot coffee runs over it, and pale melted cream runs down and streaks into the dark coffee at the bottom of the glass; the scoop does not stay a firm ball, grow, or refreeze in the hot liquid.

**Declared violation types.** process_direction, material_response

**SA**
- S1 [core] A scoop of ice cream sits in a glass.
- S2 [core] Hot espresso is poured over the scoop.
- S3 [core] The ice cream melts where the coffee runs over it.
- S4 [core] Pale melted cream runs down and streaks into the dark coffee.
- S5 [minor] Steam rises from the coffee.
- S6 [minor] The pour comes first and the melting follows.

**PC**
- P1 [core · process_direction]
  - expect: The scoop only softens and shrinks where the coffee runs, and melt that has left it does not return.
  - fail: The scoop regains a firm round shape; or melted cream draws back into the scoop; or the scoop freezes hard again in the hot coffee; or the melt alternates between more and less melted.
- P2 [core · material_response]
  - expect: The softening ice cream is a thick pale liquid that streaks and blends slowly into the thin dark coffee, and the scoop is a soft solid that slumps.
  - fail: The melted cream stands as a rigid cap on the coffee; or the scoop shatters dry; or the scoop bounces on the coffee like a ball; or the scoop keeps sharp edges while glossy and running.
- P3 [major · gravity_direction]
  - expect: The coffee falls downward onto the scoop and runs down it, and the pale melt sinks and streaks down into the coffee below.
  - fail: The coffee's stream travels upward; or the melt climbs the glass's wall and stays; or pale streaks rise from the coffee onto the scoop's top; or the scoop rises out of the glass.
- P4 [major · missing_consequence]
  - expect: The scoop shows the hot coffee arriving: it goes wet and glossy and hollows where the stream lands.
  - fail: The coffee runs over the scoop and it stays dry, matt and sharp-edged; or a hollow forms on a part of the scoop the stream never reached; or the coffee darkens the glass while the scoop stays untouched.
- P5 [fatal · permanence_count]
  - expect: One scoop in one glass; matter goes from the scoop into the liquid.
  - fail: The scoop grows; or a second scoop appears; or the scoop vanishes while still large; or the glass's level drops with nothing taken out.
- P6 [minor · attribute_drift]
  - expect: The glass's shape, the coffee's colour where it is unmixed and the surroundings stay the same.
  - fail: The glass changes shape; or the coffee changes colour away from where the cream mixes in; or items around the glass rearrange.

## HEAT-0035 · melt_freeze · train

**Caption.** A soap bubble rests on a snow-covered railing in bitter cold, and feathery ice crystals spread across its surface until the whole bubble has frozen white.

**Expectation (hidden).** The crystals start at a few points and spread across the film within seconds, turning it from clear to frosted; the bubble keeps its shape while it freezes; the frost does not retreat and the bubble does not clear again.

**Declared violation types.** process_direction, material_response

**SA**
- S1 [core] A soap bubble rests on a snow-covered railing.
- S2 [core] Ice crystals appear on the bubble's surface.
- S3 [core] The crystals spread across the bubble.
- S4 [core] The bubble ends frosted white.
- S5 [minor] The crystals are feathery or branching.
- S6 [minor] The crystals start at a few points and spread from them.

**PC**
- P1 [core · process_direction]
  - expect: The frosting only spreads: crystals grow outward from where they started and frosted film stays frosted.
  - fail: A frosted area turns clear again; or the crystals retreat toward the points they started from; or the bubble clears and frosts in turn; or the frost appears everywhere at once with no spreading front.
- P2 [core · material_response]
  - expect: The bubble stays a thin film holding its round shape while the frost grows across it: the crystals lie in the film rather than standing off it as a crust.
  - fail: The bubble sags or collapses while staying whole as it freezes; or the frost stands off the film as a thick shell; or the bubble turns into a solid ball of ice with no film; or the film ripples like open water.
- P3 [major · gravity_direction]
  - expect: The bubble rests on the railing under its own weight and stays there; anything that breaks off falls.
  - fail: The bubble rises off the railing and hangs in the air; or the bubble rolls uphill along the railing; or a broken piece of the frozen film floats upward.
- P4 [major · missing_consequence]
  - expect: The frost grows on the bubble's own surface, spreading from where the film meets the cold railing or from a few points on it.
  - fail: The frost appears on the railing rather than on the bubble; or the bubble frosts from its top down while its base on the cold railing stays clear; or the snow around the bubble changes while the bubble stays clear.
- P5 [fatal · shape_identity]
  - expect: One bubble keeps its round shape and stays on the railing; nothing passes through it.
  - fail: The bubble turns into a different shape such as a cube; or a second bubble appears; or the bubble passes through the railing; or the railing changes shape.
- P6 [minor · attribute_drift]
  - expect: The railing, the snow on it and the background stay the same.
  - fail: The railing changes colour; or the snow on the railing changes texture away from the bubble; or the background changes between frames.

## HEAT-0036 · melt_freeze · train

**Caption.** A bottle of water taken from a very cold freezer while still liquid is tapped against a table, and the water inside turns to slush from the top down within seconds.

**Expectation (hidden).** The ice starts at one spot and spreads through the liquid as a cloudy front; the bottle keeps its shape and the slush does not turn back into clear water.

**Declared violation types.** process_direction, material_response

**SA**
- S1 [core] A bottle of clear liquid water.
- S2 [core] The bottle is tapped against a table.
- S3 [core] The water turns to slush.
- S4 [core] The slush spreads through the bottle.
- S5 [minor] The water is clear before the tap.
- S6 [minor] The tap comes first and the freezing follows.

**PC**
- P1 [core · process_direction]
  - expect: The freezing only spreads: the cloudy front advances through the liquid and the frozen part stays frozen.
  - fail: A cloudy area turns clear again; or the front retreats to where it started; or the water clears and clouds in turn; or the whole bottle clouds at once before the tap.
- P2 [core · material_response]
  - expect: The water goes from a liquid that sloshes to a slush that holds its shape and no longer sloshes; the bottle stays a rigid bottle.
  - fail: The frozen water sloshes freely when the bottle is tilted; or the slush pours out as a thin liquid; or the bottle collapses inward as the water freezes; or the slush turns into a clear hard block with no cloudiness.
- P3 [major · missing_consequence]
  - expect: The water is clear and still until the bottle is struck, and the change begins at that moment.
  - fail: The water clouds before the bottle is struck; or the bottle is struck and the liquid stays clear and sloshing to the end of the clip; or the clouding begins and stops before the tap lands.
- P4 [major · gravity_direction]
  - expect: The bottle stays where it is put and the slush stays inside it; the liquid's surface stays level while the bottle is upright.
  - fail: The bottle lifts off the table; or the water's surface tilts and stays tilted with the bottle upright; or slush rises out of the bottle's neck with the cap on.
- P5 [fatal · permanence_count]
  - expect: One bottle; the water inside stays the same water and neither appears nor vanishes.
  - fail: The water's level jumps; or a second bottle appears; or the slush passes through the bottle's wall; or the bottle vanishes.
- P6 [minor · attribute_drift]
  - expect: The bottle's label and cap and the table stay the same.
  - fail: The label changes; or the cap changes colour; or the table's surface changes pattern.

## HEAT-0037 · melt_freeze · train

**Caption.** Two identical ice cubes sit side by side, one on a thick metal block and one on a plastic block, and the cube on the metal is melting faster in a spreading pool.

**Expectation (hidden).** The cube on the metal shrinks and rounds off sooner and its puddle grows larger than the one on the plastic; neither cube grows, and the difference does not reverse.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] Two ice cubes sit side by side, one on a metal block and one on a plastic block.
- S2 [core] The cube on the metal is melting: it is rounder and lower.
- S3 [core] A pool spreads under the cube on the metal.
- S4 [minor] The two cubes start alike.
- S5 [minor] The pool on the metal block is the larger of the two.

**PC**
- P1 [core · missing_consequence]
  - expect: The difference shows on the metal side: the cube on the metal rounds off and its pool grows more than the cube on the plastic.
  - fail: The cube on the plastic rounds off and pools while the cube on the metal stays sharp; or both cubes melt alike with one plainly on metal and one on plastic; or the pool under the plastic block grows while the metal stays dry.
- P2 [core · process_direction]
  - expect: Both cubes only shrink and round off, neither grows back, and the difference between them does not reverse.
  - fail: A cube regains a sharp corner; or a pool draws back into its cube; or the cube on the metal ends sharper than the cube on the plastic after being rounder; or a cube freezes solid again on its block.
- P3 [major · gravity_direction]
  - expect: Each pool spreads outward on its block's flat top and runs off the edges.
  - fail: A pool climbs its block's side and stays above the top; or meltwater travels uphill; or a drop leaves a block and rises.
- P4 [major · material_response]
  - expect: The cubes stay hard solids that keep their corners until those corners melt away, and the melt is a thin film on each block.
  - fail: A cube sags or bends as a soft lump; or a cube crumbles to dry powder; or a pool stands as a dome on its block; or a cube smears across its block as it shrinks.
- P5 [fatal · permanence_count]
  - expect: Two cubes and two blocks; water comes only from the cubes.
  - fail: A third cube appears; or a cube vanishes in a single frame while still large; or water appears on a block with no cube on it; or a cube passes into its block.
- P6 [minor · attribute_drift]
  - expect: The blocks' surfaces away from the water and the surroundings stay the same.
  - fail: A block changes colour; or the metal block's finish changes pattern; or items around the blocks rearrange.

## HEAT-0038 · melt_freeze · train

**Caption.** Molten candle wax is dripped from a spoon into a bowl of cold water, and each drop hardens into a pale bead that floats.

**Expectation (hidden).** Each drop goes from clear and runny to opaque and solid within a moment of touching the water, keeps the shape it landed in, and floats; the beads do not dissolve, spread out, or melt back together.

**Declared violation types.** material_response, process_direction

**SA**
- S1 [core] A bowl of cold water.
- S2 [core] Molten wax is dripped from a spoon into the water.
- S3 [core] Each drop hardens in the water.
- S4 [core] The hardened beads float.
- S5 [minor] The beads are pale and dull.
- S6 [minor] The drip comes first and the hardening follows.

**PC**
- P1 [core · material_response]
  - expect: The wax falls as a clear runny drop and becomes a pale solid bead in the water that keeps the shape it landed in and can be lifted out.
  - fail: A bead spreads into a flat film on the water; or a bead dissolves into the water; or a bead stays a clear glossy liquid drop floating; or a bead stretches when lifted.
- P2 [core · process_direction]
  - expect: Each bead sets once and stays set; beads do not soften back or join into a stream.
  - fail: A set bead turns runny again in the cold water; or beads merge into one running stream of liquid wax; or a bead sets, softens and sets again; or the beads alternate between pale and clear.
- P3 [major · gravity_direction]
  - expect: The drops fall downward from the spoon into the water, and the beads then sit at the surface.
  - fail: A drop travels upward from the spoon; or a bead sinks to the bowl's floor and stays there; or a drop hangs in the air between spoon and water; or a bead rises out of the water and hangs above it.
- P4 [major · missing_consequence]
  - expect: The water shows each drop arriving: the surface dimples and ripples where it lands.
  - fail: A drop enters and the surface stays glassy; or the water ripples before a drop reaches it; or the ripples appear far from where the drop lands.
- P5 [fatal · permanence_count]
  - expect: The beads in the water are the drops that fell; the bowl and spoon keep their shape.
  - fail: A bead appears in the water with no drop falling there; or a bead vanishes; or the wax passes through the bowl's wall; or a second spoon appears.
- P6 [minor · attribute_drift]
  - expect: The bowl, the spoon and the water stay the same.
  - fail: The bowl changes colour; or the spoon changes shape; or the water turns a colour.

## HEAT-0039 · melt_freeze · train

**Caption.** Ice cubes are dropped into a glass of warm cola, and they crack with a snap as they hit the liquid, splitting and fizzing.

**Expectation (hidden).** Cracks appear on the cubes within a moment of entering the warm liquid and some cubes split; the pieces float and begin to shrink; the cubes do not stay glassy and whole or fuse back together.

**Declared violation types.** material_response, permanence_count

**SA**
- S1 [core] A glass of cola.
- S2 [core] Ice cubes are dropped into the glass.
- S3 [core] Cracks appear in the cubes.
- S4 [core] Some of the cubes split.
- S5 [minor] The cola fizzes around the cubes.
- S6 [minor] The drop comes first and the cracking follows.

**PC**
- P1 [core · material_response]
  - expect: The cubes are brittle solids: cracks run through them in lines and pieces come apart along those cracks, each piece staying hard.
  - fail: A cube bends or squashes instead of cracking; or a cube crumbles to slush all over; or a cube stretches as it splits; or the pieces stay joined by a soft thread.
- P2 [core · permanence_count]
  - expect: The pieces in the glass came from the cubes that were dropped, and no new ice appears.
  - fail: Pieces fuse back into a whole cube; or new cubes appear in the glass with none dropped; or a cube vanishes in a single frame while still large; or the ice in the glass grows.
- P3 [major · gravity_direction]
  - expect: The cubes fall downward into the cola, sink and rise to ride at the surface, and the bubbles rise.
  - fail: A cube sits wholly on top of the cola like a ball on a sheet; or a cube sinks and stays on the glass's floor while others float; or bubbles sink to the bottom; or a cube rises out of the glass.
- P4 [major · missing_consequence]
  - expect: The drop has an effect: the cola splashes and foams where the cubes land and the level rises.
  - fail: The cubes enter and the surface stays glassy with no bubbles; or the cola foams before the cubes reach it; or the foam appears on the far side of the glass from the cubes.
- P5 [fatal · solidity]
  - expect: The cubes stay in the cola inside the glass and nothing passes through the glass.
  - fail: A cube passes through the glass's wall; or the glass changes shape; or a cube passes through another cube; or the glass vanishes.
- P6 [minor · attribute_drift]
  - expect: The glass's shape, the cola's colour and the table stay the same.
  - fail: The glass changes shape or pattern; or the cola changes colour; or items on the table rearrange.

**Note.** The snap is sound and is not judged; the cracking is read from the cracks appearing in the ice.

## HEAT-0040 · melt_freeze · train

**Caption.** Coarse salt is scattered over an icy doorstep, and the ice pits and turns to slush where the grains land.

**Expectation (hidden).** Small hollows form around each grain and spread, the surface goes wet and grey, and the untouched ice stays hard and clear; the pits do not heal over.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] An icy doorstep.
- S2 [core] Coarse salt is scattered over the ice.
- S3 [core] The ice pits where the grains land.
- S4 [core] The surface turns to slush around the grains.
- S5 [minor] Ice the grains miss stays hard and clear.
- S6 [minor] The scattering comes first and the pitting follows.

**PC**
- P1 [core · missing_consequence]
  - expect: Hollows form around the grains and spread from them, and ice with no grain on it stays hard and clear.
  - fail: Hollows form on parts of the step where no grain landed; or the whole step turns to slush at once while the grains lie in one patch; or grains land and the ice around them stays dry and unmarked to the end of the clip; or the slush appears before the salt is scattered.
- P2 [core · process_direction]
  - expect: The pits only deepen and widen and the wet grey area only grows; nothing heals over.
  - fail: A pit fills back in and the ice returns to smooth; or the slush turns back to clear hard ice while the grains lie in it; or the wet area shrinks; or the surface goes from slush to clear and back.
- P3 [major · gravity_direction]
  - expect: The grains fall downward onto the step and stay where they land or settle into their pits, and meltwater runs downhill across the step.
  - fail: A grain travels upward off the step; or a grain hangs above the ice without touching it; or meltwater climbs the step's riser; or the slush flows uphill.
- P4 [major · material_response]
  - expect: The grains stay hard grains sitting in the ice, and the ice goes from hard and clear to wet and grey where they lie.
  - fail: A grain melts away like a drop of water and leaves no pit; or the ice turns rubbery and dents under the grains; or the slush sets into a smooth glaze while the grains lie in it.
- P5 [fatal · permanence_count]
  - expect: The grains on the step are the grains that were scattered, and the step keeps its shape.
  - fail: Grains appear on the step with none scattered there; or a grain passes into the step's stone; or the step changes shape; or a second step appears.
- P6 [minor · attribute_drift]
  - expect: The doorstep's stone away from the ice, the door and the surroundings stay the same.
  - fail: The step's stone changes colour; or the door changes colour; or items around the step rearrange.

## HEAT-0041 · melt_freeze · train

**Caption.** Molten sealing wax is dripped onto the flap of an envelope and a metal stamp is pressed into the pool, and the wax sets hard with the stamped pattern within seconds.

**Expectation (hidden).** The wax spreads while liquid, takes the stamp's pattern, and stops moving as it hardens and dulls; the pattern stays sharp and the wax does not flow again after the stamp lifts.

**Declared violation types.** material_response, shape_identity

**SA**
- S1 [core] Molten wax is dripped onto the flap of an envelope.
- S2 [core] A metal stamp is pressed into the pool of wax.
- S3 [core] The stamp is lifted.
- S4 [core] The wax holds the stamp's pattern.
- S5 [minor] The set wax looks dull rather than glossy.
- S6 [minor] The order is drip, press, lift, set pattern.

**PC**
- P1 [core · material_response]
  - expect: The wax is a thick liquid that mounds and spreads as it lands, takes the stamp's shape under pressure and sets as a firm solid that keeps it.
  - fail: The wax runs off the envelope as thin as water; or the pool springs back to a dome as the stamp lifts; or the wax shatters under the stamp; or the set wax bends as the envelope is moved.
- P2 [core · shape_identity]
  - expect: The stamp's pattern appears in the wax as a sunken print of the stamp's face and stays sharp after the stamp lifts.
  - fail: The print sinks back and the wax ends smooth; or the print keeps changing shape after the stamp is away; or a pattern appears that the stamp's face does not carry; or the print appears before the stamp touches the wax.
- P3 [major · gravity_direction]
  - expect: The wax falls downward onto the flap and spreads out level in a pool, and the stamp comes down onto it.
  - fail: The wax travels upward from the spoon; or the pool climbs the envelope's edge and stays; or the pool stands as a tall column above the flap; or wax lifts off the envelope and hangs.
- P4 [major · missing_consequence]
  - expect: Pressing shows: the wax spreads wider under the stamp and rises around its edge.
  - fail: The stamp presses in and the pool's width does not change; or wax rises on a part of the envelope away from the stamp; or the stamp presses down to the paper with no wax squeezing out.
- P5 [fatal · permanence_count]
  - expect: One pool of wax, one stamp and one envelope; the stamp stays outside the paper and the wax stays on the flap.
  - fail: The stamp passes through the envelope; or a second seal appears; or the wax vanishes; or the envelope changes shape.
- P6 [minor · attribute_drift]
  - expect: The envelope's paper, the stamp's handle and the table stay the same.
  - fail: The envelope's paper changes colour; or the stamp's handle changes shape; or items on the table rearrange.

## HEAT-0042 · melt_freeze · train

**Caption.** A cube of jelly sits on a plate resting over a pan of steaming water, and it slumps and melts into a puddle.

**Expectation (hidden).** The cube softens and sags from the bottom and edges, its corners round off and a clear puddle of the same colour spreads out; it does not firm up again while the plate is hot.

**Declared violation types.** process_direction, shape_identity

**SA**
- S1 [core] A cube of jelly sits on a plate.
- S2 [core] The plate rests over a pan of steaming water.
- S3 [core] The cube slumps: its corners round off and it sinks lower.
- S4 [core] A puddle spreads out from the cube.
- S5 [minor] Steam rises from the pan.
- S6 [minor] The slumping comes first and the puddle follows.

**PC**
- P1 [core · process_direction]
  - expect: The cube only slumps and shrinks while the puddle grows, and nothing firms up again over the steam.
  - fail: The cube regains a sharp corner or its height; or the puddle draws back into the cube; or the jelly sets firm again on the hot plate; or the cube alternates between firmer and softer.
- P2 [core · shape_identity]
  - expect: The cube loses its flat faces and straight edges from the bottom and edges first and becomes a low glossy mound and then a puddle.
  - fail: The cube keeps its sharp corners while glossy and flowing; or the cube shrinks evenly and stays a smaller cube throughout; or the cube's top rounds off while its base keeps sharp corners; or the cube turns into another shape such as a ball with its corners intact.
- P3 [major · gravity_direction]
  - expect: The cube sinks downward onto the plate and the puddle spreads outward and settles level in the plate's well.
  - fail: The cube rises off the plate; or the puddle climbs the plate's rim and stays above it; or jelly lifts off the plate and hangs; or the puddle gathers on the cube's top.
- P4 [major · material_response]
  - expect: The jelly is a wobbling soft solid that slumps and stretches and the melt is a thin liquid of the same colour that levels.
  - fail: The jelly shatters into dry pieces; or the melt runs as a thick paste that keeps its ridges; or the cube bounces on the plate like rubber and keeps its shape; or the melt sets a skin that holds its shape when the plate is tilted.
- P5 [fatal · permanence_count]
  - expect: One cube on one plate; the jelly goes only into the puddle.
  - fail: The cube grows; or a second cube appears; or the cube vanishes while still whole; or jelly appears past the plate's rim with none crossing it.
- P6 [minor · attribute_drift]
  - expect: The jelly's colour, the plate's pattern and the pan stay the same.
  - fail: The jelly changes colour; or the plate's pattern changes; or the pan moves on the hob by itself.

## HEAT-0043 · melt_freeze · train

**Caption.** Thick white icing is piped onto cinnamon rolls fresh from the oven, and it softens and runs down into the gaps between them.

**Expectation (hidden).** The icing loses its piped ridges, goes glossy and thin, and flows downward off the high points; it does not hold its shape or run uphill.

**Declared violation types.** process_direction, gravity_direction

**SA**
- S1 [core] Cinnamon rolls fresh from the oven.
- S2 [core] Thick white icing is piped onto the rolls.
- S3 [core] The icing softens: it loses its piped ridges and goes glossy.
- S4 [core] The icing runs down into the gaps between the rolls.
- S5 [minor] The icing is thick and holds its ridges when first piped.
- S6 [minor] The piping comes first and the running follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The icing runs downward off the rolls' high points and gathers in the gaps and hollows between them.
  - fail: The icing climbs a roll's side and stays; or a run travels uphill onto a roll's top; or icing lifts off a roll and hangs; or icing gathers in a gap and then rises back onto the roll above.
- P2 [core · process_direction]
  - expect: The icing only softens, flattens and flows, and the ridges it loses do not come back.
  - fail: A flattened ridge stands up sharply again; or a run draws back up onto a roll's top; or the icing sets stiff again on the hot rolls; or the icing alternates between ridged and flat.
- P3 [major · material_response]
  - expect: The icing is a thick liquid that slumps, glosses over and flows slowly with a rounded edge, and the rolls stay soft bread.
  - fail: The icing runs as thin as water; or the icing stays a rigid white cap with sharp ridges while glossy and flowing; or the icing shatters or crumbles; or the rolls squash flat under the icing's weight.
- P4 [major · missing_consequence]
  - expect: The rolls show the icing arriving: their surface goes wet and glossy where it lies and the gaps fill from the icing above.
  - fail: The icing runs over a roll and the surface under it stays dry and matt; or a gap fills with icing while none runs into it from above; or the icing softens while no roll's surface changes.
- P5 [fatal · permanence_count]
  - expect: The icing on the rolls is the icing that was piped, and the rolls keep their number and shape.
  - fail: Icing appears in a gap with none coming from above; or a roll vanishes or a new roll appears; or the icing grows in amount with none piped; or a roll passes through the tray.
- P6 [minor · attribute_drift]
  - expect: The icing's white, the rolls' colour and the tray stay the same.
  - fail: The icing changes colour; or the rolls change colour; or the tray changes shape.

## HEAT-0044 · melt_freeze · train

**Caption.** A car's frosted side mirror is switched to heat on a cold morning, and the frost turns to droplets in a patch that spreads across the glass.

**Expectation (hidden).** The clearing starts in one area and spreads outward, the white frost turning wet and then clear; frost does not re-form on the cleared glass while the heater runs.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] A car's side mirror covered in frost.
- S2 [core] A clear patch appears on the glass.
- S3 [core] The frost turns to droplets in that patch.
- S4 [core] The patch spreads across the glass.
- S5 [minor] No hand or scraper touches the glass.
- S6 [minor] The patch starts in one area and grows from there.

**PC**
- P1 [core · process_direction]
  - expect: The clearing only spreads: the clear area grows outward from where it started and cleared glass stays clear.
  - fail: Frost grows back over glass that had cleared; or the clear patch shrinks; or the glass clears and frosts in turn; or the frost thickens while the patch spreads.
- P2 [core · missing_consequence]
  - expect: The frost goes by turning wet: the white crust darkens to droplets at the patch's edge before the glass is clear behind it.
  - fail: The frost goes and leaves the glass dry; or the whole mirror clears at once with no spreading edge; or the patch clears while the frost's edge stays a sharp white line with no wet band.
- P3 [major · gravity_direction]
  - expect: Droplets that grow large enough run downward over the glass and gather at its lower edge.
  - fail: A droplet runs up the mirror; or a droplet leaves the glass and rises; or water gathers along the mirror's top edge and stays; or a run travels sideways and stays level with the car still.
- P4 [major · causeless_motion]
  - expect: The mirror stays where it is set and the car stays still; only the frost changes.
  - fail: The mirror swings or folds with nothing touching it; or the car rocks; or the mirror's glass turns in its housing by itself.
- P5 [fatal · permanence_count]
  - expect: One mirror in one housing; the frost turns to water on the glass and nothing passes through it.
  - fail: The mirror's glass vanishes; or a second mirror appears; or water appears inside the housing with none running there; or the mirror changes shape.
- P6 [minor · attribute_drift]
  - expect: The car's paint, the mirror's housing and the surroundings stay the same.
  - fail: The car changes colour; or the housing changes shape or colour; or the background behind the car changes between frames.

## HEAT-0045 · melt_freeze · train

**Caption.** Two wet ice cubes straight from the freezer are pressed together for a moment and let go, and they stay stuck as one piece.

**Expectation (hidden).** After release the cubes hold together and can be lifted as one; they do not fall apart, slide off each other, or melt open at the join while they stay cold.

**Declared violation types.** material_response, permanence_count

**SA**
- S1 [core] Two ice cubes are held, wet from the freezer.
- S2 [core] The cubes are pressed together.
- S3 [core] The hands let go.
- S4 [core] The cubes stay stuck together.
- S5 [minor] The cubes look wet at the start.
- S6 [minor] The order is press, release, stay stuck.

**PC**
- P1 [core · material_response]
  - expect: The cubes are hard solids that meet face to face and join at the film of water between them, and the join holds when the pair is lifted or tilted.
  - fail: The cubes squash or deform where they are pressed; or the pair bends at the join like a hinge; or the cubes merge into one smooth block with no seam; or the join stretches as the pair is lifted.
- P2 [core · permanence_count]
  - expect: Two cubes throughout: they stay two pieces stuck together and neither appears, vanishes nor grows.
  - fail: The two cubes merge into a single larger cube with no seam; or a third cube appears; or a cube vanishes; or the pair ends larger than the two cubes were.
- P3 [major · missing_consequence]
  - expect: After the hands let go the cubes stay in contact along the pressed faces with nothing else holding them.
  - fail: The cubes fall apart as the hands open; or the cubes slide off each other and drop; or the pair holds together with a gap between the faces; or one cube hangs from the other without touching it.
- P4 [major · gravity_direction]
  - expect: The stuck pair rests or hangs under its own weight and falls if let go entirely, and meltwater runs downward off it.
  - fail: The pair floats when released; or a cube rises away from the other; or meltwater runs up a cube's face; or the pair hangs in the air with the hands gone.
- P5 [fatal · solidity]
  - expect: The cubes stay outside each other, touching at their faces, and nothing passes through either cube or through the hands.
  - fail: One cube passes into the other; or a finger passes through a cube; or a cube passes through the surface it rests on; or a cube passes through the other and out the far side.
- P6 [minor · attribute_drift]
  - expect: The cubes' clear look, the hands and the surroundings stay the same.
  - fail: A cube turns a colour; or the surface under them changes pattern; or the background changes between frames.

**Note.** The hands are kept because pressing is the caption's action; they are otherwise not judged.

## HEAT-0046 · boil_steam · train

**Caption.** A kettle on a stove is at the boil, steam pours from the spout, and the lid rattles.

**Expectation (hidden).** Steam rises and spreads upward from the spout, thinning as it goes; the rattle coincides with the steam; steam does not sink or flow downward.

**Declared violation types.** process_direction, gravity_direction, missing_consequence

**SA**
- S1 [core] A kettle sits on a stove.
- S2 [core] Steam comes out of the spout.
- S3 [core] The lid rattles: a small repeated movement on its seat.
- S4 [minor] The kettle is a stovetop kettle with a spout and a lid.
- S5 [minor] The burner or stove is visible under the kettle.

**PC**
- P1 [core · gravity_direction]
  - expect: Steam leaves the spout and rises, spreading and thinning as it goes up.
  - fail: Steam sinks toward the stove or pools on the counter; or stays as a dense cloud that does not thin; or streams straight sideways with no draught visible.
- P2 [core · process_direction]
  - expect: The steam keeps coming and the plume moves outward from the spout; puffs that have left keep moving away.
  - fail: The plume runs back into the spout; or a puff retreats toward the kettle; or steam appears in the air far from the spout and drifts toward it.
- P3 [major · missing_consequence]
  - expect: The lid's rattle goes with the boil: it lifts and drops on its seat while steam issues, and steam may puff from under it.
  - fail: The lid moves with no steam anywhere; or the lid lifts and stays up; or the lid rattles while the kettle is off the stove.
- P4 [major · causeless_motion]
  - expect: The kettle itself stays put on the burner; only the lid and the steam move.
  - fail: The kettle slides, rocks or turns on the burner with nothing touching it; or the spout swings.
- P5 [fatal · permanence_count]
  - expect: One kettle with one lid and one spout; the lid stays attached and nothing passes through the kettle body.
  - fail: A second spout or lid appears; or the lid passes through the kettle wall; or the kettle changes shape or vanishes; or steam comes through the closed lid's body rather than round its edge.
- P6 [minor · attribute_drift]
  - expect: The kettle's colour and the stove's knobs stay the same.
  - fail: The kettle changes colour or material; or the stove's burners change position; or the wall behind changes.

## HEAT-0047 · boil_steam · train

**Caption.** A pot of pasta water boils over on a stove, and foamy water spills down the outside of the pot onto the burner.

**Expectation (hidden).** Foam rises inside the pot, climbs over the rim, and runs down the outside, hissing on the burner; the level inside drops as it spills; foam does not fall back into the pot from above.

**Declared violation types.** process_direction, gravity_direction, material_response

**SA**
- S1 [core] A pot sits on a stove.
- S2 [core] Foam rises inside the pot and over the rim.
- S3 [core] Foamy water runs down the outside of the pot to the burner.
- S4 [minor] The water is pasta water: cloudy, starchy foam, pasta may be visible.
- S5 [minor] The order is foam rises, spills over, runs down.

**PC**
- P1 [core · process_direction]
  - expect: The foam climbs from inside the pot up and over the rim, and spilled foam is on its way down the outside: inside to out, up then over then down.
  - fail: Foam climbs back up the outside into the pot; or the spill retreats over the rim; or the outside is wet before any foam reaches the rim.
- P2 [major · gravity_direction]
  - expect: Once over the rim the foam and water run downward on the pot wall and onto the burner.
  - fail: Foam runs sideways round the pot or upward; or falls up; or hangs off the rim as a static curtain without descending.
- P3 [major · material_response]
  - expect: The overflow is a frothy liquid: bubbles collapse, the liquid streaks, and it steams or spits on the hot burner.
  - fail: The foam sits as a rigid dome that does not deform; or the spill behaves as a solid sheet peeling off; or the liquid on the hot burner lies still with no steam or reaction.
- P4 [major · missing_consequence]
  - expect: Foam over the rim means the level inside has reached the rim; the spill wets the pot wall and leaves it wet.
  - fail: Foam pours over while the visible inside is calm and far from full; or the wall is dry again right after foam ran down it.
- P5 [fatal · permanence_count]
  - expect: One pot that keeps its shape; foam passes only over the rim, not through the wall.
  - fail: Foam appears on the outside with none crossing the rim; or the pot changes shape or size; or a second pot appears; or foam passes through the pot wall.
- P6 [minor · attribute_drift]
  - expect: Pot colour, stove knobs and burner layout stay the same.
  - fail: The pot changes colour; or the burner moves; or the stovetop pattern changes.

## HEAT-0048 · boil_steam · train

**Caption.** A saucepan of water on high heat is at a rolling boil, with large bubbles bursting at the surface.

**Expectation (hidden).** Bubbles form at the bottom and rise to burst at the top, the surface churns, and wisps of steam rise; bubbles do not sink or form at the surface and travel down.

**Declared violation types.** process_direction, gravity_direction

**SA**
- S1 [core] A saucepan of water sits on a hob.
- S2 [core] Bubbles rise through the water.
- S3 [core] Bubbles burst at the surface.
- S4 [minor] The surface churns.
- S5 [minor] The bubbles are large.

**PC**
- P1 [core · gravity_direction]
  - expect: The bubbles form at the pan's bottom and rise to the surface, growing as they go, and burst there.
  - fail: Bubbles sink from the surface to the bottom; or form at the surface and travel down; or hang still in mid-water; or rise part-way and then fall back.
- P2 [core · process_direction]
  - expect: The boil keeps up: bubbles keep arriving from below and the churn goes on, and bubbles that have left the floor keep rising.
  - fail: The surface goes glassy still while bubbles keep streaming below it; or the bubbling stops and then starts again by itself; or bubbles run back into the pan's floor; or bubbles shrink as they rise and vanish before the surface while the surface still churns.
- P3 [major · missing_consequence]
  - expect: Each burst shows at the surface: it breaks through, throws a small splash and leaves a ring that spreads.
  - fail: A bubble reaches the surface and the surface stays glassy; or rings spread from spots where no bubble arrived; or the surface churns while nothing rises below it.
- P4 [major · material_response]
  - expect: The water behaves as a liquid: it churns, splashes and finds its level, and wisps of steam rise from it.
  - fail: The surface holds a fixed shape while bubbles burst through it; or the water stands in a heap above the pan's rim; or the churning water moves as a solid mass; or the steam sinks and pools around the pan.
- P5 [fatal · permanence_count]
  - expect: One pan of water; the water stays in the pan and its level changes only by boiling away or spilling.
  - fail: Water passes through the pan's wall; or the level jumps up with nothing added; or a second pan appears; or the pan changes shape.
- P6 [minor · attribute_drift]
  - expect: The pan, the hob and the surroundings stay the same.
  - fail: The pan changes colour; or its handle changes shape; or the hob's knobs move by themselves.

## HEAT-0049 · boil_steam · train

**Caption.** The lid is lifted off a rice cooker, and a cloud of steam billows up out of it.

**Expectation (hidden).** The steam escapes upward the moment the lid comes off, spreads, and thins; it does not pour down the sides or stay in the cooker.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] A rice cooker with its lid on.
- S2 [core] The lid is lifted off.
- S3 [core] A cloud of steam comes out of the cooker.
- S4 [minor] The steam billows up and spreads.
- S5 [minor] The lift comes first and the steam follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The steam rises out of the cooker, spreading and thinning as it climbs.
  - fail: The steam pours down the cooker's sides and pools on the counter; or sinks to the floor; or stays inside the cooker with the lid off; or streams straight sideways with nothing blowing it.
- P2 [core · process_direction]
  - expect: The steam escapes when the lid comes off and the plume moves outward and away; puffs that have left keep going.
  - fail: The plume runs back into the cooker; or a puff retreats toward the pot; or steam appears above the closed lid and drifts down into it; or steam billows before the lid has moved.
- P3 [major · material_response]
  - expect: The steam is a soft cloud that spreads, waves and fades; the lid is a rigid piece and the rice below stays a bed of grains.
  - fail: The steam holds a fixed rigid shape; or pours like a liquid over the rim; or the lid bends like cloth as it lifts; or the steam lifts the rice out of the pot.
- P4 [major · missing_consequence]
  - expect: The steam comes from the hot food: the plume issues from the pot's mouth where the lid was and the rice below looks wet.
  - fail: The plume comes from the cooker's base or side rather than its mouth; or steam pours from the closed part of the cooker while its mouth is clear; or the pot below holds no food and no water while a thick plume pours from it.
- P5 [fatal · permanence_count]
  - expect: One cooker and one lid; the lid stays a lid and nothing passes through the cooker.
  - fail: The lid passes through the cooker's rim; or a second lid appears; or the cooker vanishes; or a hand passes through the lid.
- P6 [minor · attribute_drift]
  - expect: The cooker's casing, its controls and the counter stay the same.
  - fail: The casing changes colour; or the controls rearrange; or items on the counter change.

## HEAT-0050 · boil_steam · train

**Caption.** A steam wand is pushed into a jug of milk, and the milk hisses, swirls, and rises in the jug as foam.

**Expectation (hidden).** The foam builds from the top of the milk while the wand runs and stops rising when the wand is switched off; the milk level does not drop.

**Declared violation types.** process_direction, material_response

**SA**
- S1 [core] A jug of milk.
- S2 [core] A steam wand is pushed into the milk.
- S3 [core] The milk swirls.
- S4 [core] The milk rises in the jug as foam.
- S5 [minor] Vapour shows at the jug's mouth.
- S6 [minor] The wand goes in first and the foam rises after.

**PC**
- P1 [core · process_direction]
  - expect: The foam builds from the milk's surface while the wand runs and stays up when the wand stops; the level only rises.
  - fail: The foam sinks back while the wand still runs; or the level drops as the foam builds; or the foam builds and collapses in turn; or the foam rises before the wand is in the milk.
- P2 [core · material_response]
  - expect: The milk is a liquid that swirls and takes on a thick bubbly head holding soft peaks.
  - fail: The milk stays a flat mirror while the wand runs in it; or the foam stands as rigid spikes that keep their shape when the jug is shaken; or the milk sets solid; or the foam pours off the top like water.
- P3 [major · gravity_direction]
  - expect: The foam sits on top of the milk, the milk stays in the jug, and the vapour rises from the mouth.
  - fail: The foam gathers under the milk at the jug's floor; or milk climbs out of the jug and hangs above it; or the vapour sinks and pools around the jug; or the foam lifts off the milk as a separate cloud.
- P4 [major · causeless_motion]
  - expect: The milk swirls only while the wand runs and settles when it stops; the jug stays where it is held.
  - fail: The milk swirls with the wand out of it and still; or the swirl speeds up after the wand stops; or the jug spins with nothing turning it; or the milk churns before the wand enters.
- P5 [fatal · permanence_count]
  - expect: One jug and one wand; the milk stays in the jug and nothing appears or vanishes.
  - fail: Milk passes through the jug's wall; or the jug's contents jump in level with nothing added; or a second wand appears; or the jug changes shape.
- P6 [minor · attribute_drift]
  - expect: The jug's metal, the wand and the surroundings stay the same.
  - fail: The jug changes colour; or the wand changes shape; or the machine behind changes.

## HEAT-0051 · boil_steam · train

**Caption.** A pressure cooker on a stove starts hissing, and a jet of steam shoots up from the valve on its lid.

**Expectation (hidden).** The jet goes straight up from the valve, spreading as it rises, and the hissing lasts as long as the jet; steam does not come from the sealed rim.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] A pressure cooker stands on a hob.
- S2 [core] A jet of steam comes from the valve on its lid.
- S3 [core] The jet goes upward.
- S4 [minor] The jet spreads as it rises.
- S5 [minor] The steam comes from the valve rather than the lid's rim.

**PC**
- P1 [core · gravity_direction]
  - expect: The jet leaves the valve going up and spreads and thins as it climbs.
  - fail: The jet shoots downward onto the hob; or the steam pours down the cooker's sides and pools; or the jet hangs as a fixed shape without rising; or the steam sinks to the floor.
- P2 [core · missing_consequence]
  - expect: The steam issues from the valve alone and lasts as long as the jet does, and the lid's rim stays sealed.
  - fail: Steam escapes all round the lid's rim while the valve is clear; or the jet comes from the cooker's body or base; or the valve is clear and steam appears above the cooker with nothing leaving it; or the jet appears while the valve is shut flat.
- P3 [major · material_response]
  - expect: The jet is a narrow fast plume at the valve that softens into a spreading cloud above it.
  - fail: The jet stays a hard-edged column all the way up; or the steam pours like a liquid; or the valve bends or droops; or the plume breaks into solid lumps.
- P4 [major · causeless_motion]
  - expect: The cooker stays put on the hob; only the valve and the steam move.
  - fail: The cooker slides, rocks or turns with nothing touching it; or the lid lifts and stays up; or the cooker's handles swing.
- P5 [fatal · permanence_count]
  - expect: One cooker with one lid and one valve; the lid stays on and nothing passes through the body.
  - fail: The lid passes through the cooker's rim; or a second valve appears; or the cooker changes shape; or steam passes out through the body's wall.
- P6 [minor · attribute_drift]
  - expect: The cooker's finish, its handles and the hob stay the same.
  - fail: The cooker changes colour; or a handle changes shape; or the hob's knobs move by themselves.

**Note.** The hiss is sound and is not judged.

## HEAT-0052 · boil_steam · train

**Caption.** A pot of soup simmers on a stove, with small bubbles breaking the surface and steam rising.

**Expectation (hidden).** Bubbles appear from below and pop at the surface, the surface shifts gently, and steam rises; the soup does not go still while the heat stays on.

**Declared violation types.** process_direction, gravity_direction

**SA**
- S1 [core] A pot of soup sits on a hob.
- S2 [core] Small bubbles break the soup's surface.
- S3 [core] Steam rises from the pot.
- S4 [minor] The surface shifts gently rather than churning hard.
- S5 [minor] The bubbles come up from below.

**PC**
- P1 [core · gravity_direction]
  - expect: The bubbles rise from below to the surface and burst there, and the steam rises from the surface upward.
  - fail: Bubbles sink from the surface downward; or hang still in the soup; or the steam sinks over the pot's rim and pools on the hob; or the steam streams straight down.
- P2 [core · process_direction]
  - expect: The simmer keeps up: bubbles keep arriving and steam keeps leaving, and puffs that have left keep going.
  - fail: The steam runs back into the pot; or a puff retreats toward the surface; or the surface goes glassy still while bubbles keep streaming below it; or the bubbling stops and then starts again by itself.
- P3 [major · missing_consequence]
  - expect: Each bubble shows at the surface: it breaks through and leaves a spreading ring.
  - fail: A bubble reaches the surface and the surface stays glassy; or rings spread from spots where no bubble arrived; or the surface shifts while nothing rises below it.
- P4 [major · material_response]
  - expect: The soup behaves as a liquid: it shifts, ripples and finds its level, with any solid pieces bobbing in it.
  - fail: The surface holds a fixed shape while bubbles burst through it; or the soup stands in a heap above the rim; or the soup moves as a solid mass; or pieces in the soup stay fixed in place while the liquid moves around them.
- P5 [fatal · permanence_count]
  - expect: One pot of soup; the soup stays in the pot.
  - fail: Soup passes through the pot's wall; or the level jumps up with nothing added; or a second pot appears; or the pot changes shape.
- P6 [minor · attribute_drift]
  - expect: The pot, the hob and the soup's colour stay the same.
  - fail: The pot changes colour; or the soup changes colour; or the hob's knobs move by themselves.

## HEAT-0053 · boil_steam · train

**Caption.** Eggs boil in a pot on a stove, rattling against each other as the water bubbles around them.

**Expectation (hidden).** The eggs jostle only because of the bubbling water, staying at the bottom; steam rises above the pot; the eggs do not float up or stay perfectly still in a boiling pot.

**Declared violation types.** process_direction, causeless_motion

**SA**
- S1 [core] A pot of water sits on a hob.
- S2 [core] Eggs sit in the water.
- S3 [core] Bubbles rise around the eggs.
- S4 [core] The eggs jostle against each other.
- S5 [minor] The eggs stay at the pot's bottom.
- S6 [minor] Steam rises above the pot.

**PC**
- P1 [core · causeless_motion]
  - expect: The eggs move only as the bubbling water pushes them: they knock and shift while the water churns and settle when it calms.
  - fail: An egg darts across the pot with the water still; or an egg spins fast on the spot with nothing turning it; or the eggs jostle in water with no bubbles rising; or an egg jumps out of the water.
- P2 [core · process_direction]
  - expect: The boil keeps up while the eggs knock: bubbles keep arriving from below and steam keeps leaving.
  - fail: The bubbling stops and then starts again by itself; or the steam runs back into the pot; or bubbles sink from the surface to the eggs; or the surface goes glassy still while bubbles stream below it.
- P3 [major · gravity_direction]
  - expect: The eggs rest low in the pot and the bubbles and steam rise.
  - fail: An egg rises out of the water and hangs above it; or an egg hangs motionless in mid-water; or bubbles sink toward the pot's floor; or the steam sinks and pools around the pot.
- P4 [major · material_response]
  - expect: The eggs are hard-shelled solids that knock and rebound off each other and the pot, and the water closes round them.
  - fail: An egg squashes where it strikes another; or an egg's shell bends; or the eggs merge into one lump; or the water holds a dent around an egg like a solid.
- P5 [fatal · permanence_count]
  - expect: The eggs keep their number and stay in the pot; nothing appears or vanishes.
  - fail: An egg vanishes; or a new egg appears; or an egg passes through the pot's wall; or two eggs merge into one.
- P6 [minor · attribute_drift]
  - expect: The pot, the hob and the eggs' shells stay the same.
  - fail: The pot changes colour; or an egg's shell changes colour; or the hob's knobs move by themselves.

**Note.** The rattle is sound and is not judged; the jostling is read from the eggs' visible knocking.

## HEAT-0054 · boil_steam · train

**Caption.** A steam iron is pressed onto a shirt on an ironing board, and puffs of steam rise from around the iron.

**Expectation (hidden).** Steam comes out only while the iron is on the fabric and rises from its edges; the fabric under the iron flattens; steam does not pour downward.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] A shirt lies on an ironing board.
- S2 [core] An iron is pressed onto the shirt.
- S3 [core] Puffs of steam rise from around the iron.
- S4 [minor] The fabric under the iron flattens.
- S5 [minor] The steam comes while the iron is on the fabric.

**PC**
- P1 [core · gravity_direction]
  - expect: The steam rises from the iron's edges, spreading and thinning as it climbs.
  - fail: The steam pours downward through the board; or sinks and pools on the floor; or hangs as a fixed shape without rising; or streams straight sideways with nothing blowing it.
- P2 [core · missing_consequence]
  - expect: The steam comes out while the iron is on the fabric and from around its plate, and the fabric flattens where the iron has passed.
  - fail: Steam puffs while the iron stands well clear of the shirt; or the iron passes over a crease and the fabric behind it is unchanged; or the steam comes from the board rather than the iron; or a crease flattens where the iron has not been.
- P3 [major · process_direction]
  - expect: The creases only drop out along the iron's path, and flattened fabric stays flat.
  - fail: A crease comes back on fabric the iron has just passed over; or the fabric wrinkles more where the iron has been; or the creases drop out all over the shirt while the iron sits in one place.
- P4 [major · material_response]
  - expect: The shirt is cloth that presses flat under the plate and darkens where it is damp; the iron is a rigid solid.
  - fail: The shirt stays board-stiff and keeps its creases under the plate; or the fabric stretches like elastic under the iron; or the iron's plate bends; or the shirt sticks to the plate and lifts with it.
- P5 [fatal · solidity]
  - expect: The iron rests on top of the shirt and the shirt on the board; nothing passes through anything.
  - fail: The iron sinks into the board; or the iron passes through the shirt; or a second iron appears; or the board changes shape.
- P6 [minor · attribute_drift]
  - expect: The shirt's colour and pattern away from the press, the board's cover and the room stay the same.
  - fail: The shirt changes colour; or the board's cover changes pattern; or items in the room rearrange.

## HEAT-0055 · boil_steam · train

**Caption.** Steam rises from a manhole cover on a city street on a cold morning.

**Expectation (hidden).** The steam comes up through the holes and drifts upward, thinning and bending with the breeze; it does not flow along the ground like water.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] A manhole cover sits in a street.
- S2 [core] Steam comes up through the cover.
- S3 [core] The steam rises.
- S4 [minor] The setting reads as cold: bare trees, frost or winter clothing.
- S5 [minor] The steam drifts and thins as it rises.

**PC**
- P1 [core · gravity_direction]
  - expect: The steam leaves the cover going up, spreading and thinning; it may lean with a breeze but it does not sink.
  - fail: The steam flows along the street like water; or pools in the gutter; or sinks back into the cover's holes; or hangs as a fixed shape without rising or drifting.
- P2 [core · process_direction]
  - expect: The plume moves outward and away from the cover, and puffs that have left keep going.
  - fail: The plume runs back into the cover; or a puff retreats toward the holes; or steam appears high above the street and drifts down into the cover; or steam appears in the air away from the cover and drifts toward it.
- P3 [major · missing_consequence]
  - expect: The steam comes up through the cover's holes or its rim rather than out of the road's solid surface.
  - fail: The steam rises from solid asphalt away from the cover; or the cover is clear and steam appears above it with nothing leaving it; or the steam rises from a wall or a parked car instead.
- P4 [major · material_response]
  - expect: The steam is a soft cloud that spreads, waves and fades; the cover stays a rigid iron plate.
  - fail: The steam holds a fixed rigid shape; or pours like a liquid; or the cover lifts and hangs in the air; or the steam turns into solid lumps.
- P5 [fatal · permanence_count]
  - expect: One cover in one road; the cover stays in its seat and nothing passes through the road.
  - fail: The cover vanishes; or a second cover appears; or the cover passes down through the road; or the road's surface opens up.
- P6 [minor · attribute_drift]
  - expect: The road markings, the kerb and the buildings stay the same.
  - fail: The road markings change; or the kerb changes shape; or the buildings behind change between frames.

**Note.** The wind is often invisible; the plume leaning as it rises is not a violation.

## HEAT-0056 · boil_steam · train

**Caption.** Boiling water is poured from a kettle into a mug, and steam rises from the mug as it fills.

**Expectation (hidden).** Steam rises from the falling stream and from the mug's surface, growing as the mug fills; the water itself falls downward and the steam goes up.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] A kettle pours water into a mug.
- S2 [core] The mug fills.
- S3 [core] Steam rises from the mug.
- S4 [minor] Steam also rises from the falling stream.
- S5 [minor] The steam grows as the mug fills.
- S6 [minor] The pour comes first and the mug's steam follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The water falls downward from the spout into the mug while the steam rises upward from both the stream and the mug.
  - fail: The water travels upward from the spout; or the stream bends up into the air; or the steam sinks over the mug's rim and pools on the table; or the steam pours downward from the spout.
- P2 [core · process_direction]
  - expect: The mug's level only rises while the pour lasts and the steam keeps leaving upward; puffs that have left keep going.
  - fail: The mug's level drops while water still pours in; or the steam runs back into the mug; or a puff retreats to the surface; or water climbs back up the stream into the kettle.
- P3 [major · missing_consequence]
  - expect: The pour has an effect in the mug: the surface churns and rises where the stream lands and the mug's inside wall wets.
  - fail: The stream enters and the surface stays glassy with the level unchanged; or the level rises with no stream reaching the mug; or the mug's inside stays dry above the water.
- P4 [major · material_response]
  - expect: The water is a thin liquid that falls as a continuous stream, splashes and finds its level; the steam is a soft cloud that spreads and fades.
  - fail: The stream falls as a rigid rod; or the water stands in a heap above the mug's rim; or the steam holds a fixed rigid shape; or the stream breaks into solid lumps.
- P5 [fatal · permanence_count]
  - expect: One kettle and one mug; the water goes from kettle to mug and nowhere else.
  - fail: Water appears in the mug with no stream reaching it; or the stream passes through the mug's wall; or the mug's level jumps; or a second mug appears.
- P6 [minor · attribute_drift]
  - expect: The kettle, the mug's pattern and the counter stay the same.
  - fail: The kettle changes colour; or the mug's pattern changes; or items on the counter rearrange.

## HEAT-0057 · boil_steam · train

**Caption.** Noodles cook in a pot of boiling water, bobbing and swirling with the bubbles.

**Expectation (hidden).** The noodles move with the churning water and settle when the heat is turned down; they do not move on their own in still water.

**Declared violation types.** process_direction, causeless_motion

**SA**
- S1 [core] A pot of boiling water sits on a hob.
- S2 [core] Noodles are in the water.
- S3 [core] The noodles bob and swirl.
- S4 [minor] Bubbles rise around the noodles.
- S5 [minor] Steam rises above the pot.

**PC**
- P1 [core · causeless_motion]
  - expect: The noodles move only as the churning water carries them, and they settle when the churn eases.
  - fail: A noodle darts across the pot with the water still; or a noodle travels against the swirl; or the noodles swirl in water with no bubbles rising; or a noodle leaves the water and hangs above it.
- P2 [core · process_direction]
  - expect: The boil keeps up while the noodles turn: bubbles keep coming from below and steam keeps rising.
  - fail: The bubbling stops and then starts again by itself; or the steam runs back into the pot; or bubbles sink from the surface downward; or the surface goes glassy still while bubbles stream below it.
- P3 [major · material_response]
  - expect: The noodles are limp strands that bend and coil in the water and drape over each other, and the water closes round them.
  - fail: The noodles stay straight and rigid like sticks while tumbling in the boil; or a noodle snaps into pieces that stay stiff; or the noodles fuse into one solid mass; or the water holds a dent around a noodle.
- P4 [major · gravity_direction]
  - expect: The noodles ride in the water, sinking or rising with the churn, and the bubbles and steam rise.
  - fail: A noodle hangs motionless in mid-water while the rest churn; or a noodle rises out of the water and stays above it; or bubbles sink toward the pot's floor; or the steam sinks and pools around the pot.
- P5 [fatal · permanence_count]
  - expect: The noodles keep their number and stay in the pot; nothing appears or vanishes.
  - fail: A noodle vanishes; or new noodles appear with none added; or a noodle passes through the pot's wall; or two noodles merge into one thicker strand.
- P6 [minor · attribute_drift]
  - expect: The pot, the hob and the water stay the same.
  - fail: The pot changes colour; or the water turns a colour; or the hob's knobs move by themselves.

**Note.** The noodles softening as they cook is expected; how soft they get is not judged.

## HEAT-0058 · boil_steam · train

**Caption.** Water boils in a glass electric kettle, with streams of bubbles rising from the bottom to the surface.

**Expectation (hidden).** Bubbles start at the heated base and travel upward, growing as they rise, and steam leaves the top; bubbles do not travel downward.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] A glass electric kettle holds water.
- S2 [core] Bubbles form at the kettle's base.
- S3 [core] The bubbles rise to the surface.
- S4 [minor] Streams of bubbles run up through the water.
- S5 [minor] The bubbles grow as they rise.

**PC**
- P1 [core · gravity_direction]
  - expect: The bubbles start at the base and travel upward to the surface, growing as they rise, and burst there.
  - fail: Bubbles travel downward from the surface to the base; or form at the surface and sink; or hang still in mid-water; or rise part-way and then fall back.
- P2 [core · process_direction]
  - expect: The streams keep coming from the base while the water boils and the surface churns; bubbles that have left the base keep rising.
  - fail: A bubble retreats into the base; or the streams stop and then start again by themselves; or the surface goes glassy still while streams run below it; or bubbles shrink as they rise and vanish before reaching the surface.
- P3 [major · missing_consequence]
  - expect: Each stream shows at the surface: bubbles break through and the surface above a stream churns most.
  - fail: The streams reach the surface and it stays glassy; or the surface churns above a part of the base with no stream under it; or the water churns while no bubble rises anywhere.
- P4 [major · material_response]
  - expect: The water is a liquid that churns and finds its level, and the glass stays a rigid clear wall.
  - fail: The water stands in a heap above its level; or the churn moves as a solid mass; or the glass flexes or bulges; or the water sticks to the glass in a fixed shape.
- P5 [fatal · permanence_count]
  - expect: One kettle; the water stays inside and its level changes only by boiling away.
  - fail: Water passes through the glass; or the level jumps up with nothing added; or a second kettle appears; or the kettle changes shape.
- P6 [minor · attribute_drift]
  - expect: The kettle's base, its handle and the counter stay the same.
  - fail: The handle changes shape; or the base changes colour; or items on the counter rearrange.

## HEAT-0059 · boil_steam · train

**Caption.** A divided hot pot with spicy red oil broth on one side and clear broth on the other heats over a burner, and the red side comes to the boil while the clear side stays calm.

**Expectation (hidden).** Large bubbles rise and burst through the red oil layer and its surface churns, while the clear side stays nearly flat with at most a few tiny bubbles and faint steam; the two broths stay on their own sides of the divider and keep their colours; the red side does not fall quiet while the burner is on, and the clear side does not boil harder than the red side.

**Declared violation types.** material_response, process_direction, attribute_drift

**SA**
- S1 [core] A divided hot pot sits over a burner, with red oil broth on one side and clear broth on the other.
- S2 [core] The red side comes to the boil: bubbles rise and burst through it.
- S3 [core] The red side's surface churns.
- S4 [core] The clear side stays nearly flat.
- S5 [minor] The divider keeps the two broths apart.
- S6 [minor] Each broth keeps to its own colour.

**PC**
- P1 [core · process_direction]
  - expect: The red side's boil keeps up while the burner is under it and the clear side stays calmer throughout; the difference does not reverse.
  - fail: The red side falls quiet and stays flat while the clear side churns; or the clear side boils harder than the red side; or the red side's boil stops and then starts again by itself; or the two sides swap which one is boiling.
- P2 [core · material_response]
  - expect: The red side is a liquid with an oil layer on top through which large bubbles rise and burst; the clear side is a liquid showing at most small bubbles and faint steam.
  - fail: The red layer holds a fixed shape while bubbles burst through it; or the oil layer stands in a heap above the broth; or the clear broth sets solid; or the red broth moves as one solid mass.
- P3 [core · attribute_drift]
  - expect: Each broth keeps to its own side and its own colour: red on one side and clear on the other.
  - fail: Red broth appears on the clear side with none crossing the divider; or the clear broth turns red all over; or the two broths swap sides; or the red broth's colour drains away and leaves it clear.
- P4 [major · gravity_direction]
  - expect: The bubbles rise through each broth to its surface and any steam rises above the pot.
  - fail: Bubbles sink from a surface toward the pot's floor; or hang still in the broth; or the steam sinks and pools around the burner; or broth climbs the divider and stays above it.
- P5 [fatal · permanence_count]
  - expect: One pot with one divider and two broths; the broths stay on their own sides and nothing passes through the divider or the pot.
  - fail: Broth passes through the divider; or the divider vanishes; or a third compartment appears; or broth passes through the pot's wall.
- P6 [minor · attribute_drift]
  - expect: The pot's rim, the burner and the table stay the same.
  - fail: The pot changes shape; or the burner moves by itself; or items on the table rearrange.

## HEAT-0060 · boil_steam · train

**Caption.** Water is ladled onto the hot stones of a sauna, and a burst of steam rises off the stones with a hiss.

**Expectation (hidden).** The water hisses and vanishes into steam almost at once, the steam rises and fills the upper room; water does not remain pooled on the hot stones.

**Declared violation types.** gravity_direction, process_direction, permanence_count

**SA**
- S1 [core] Hot stones sit in a sauna.
- S2 [core] Water is ladled onto the stones.
- S3 [core] A burst of steam rises off the stones.
- S4 [minor] A ladle is the water's source.
- S5 [minor] The steam fills the space above the stones.
- S6 [minor] The pour comes first and the steam follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The steam leaves the stones going up and fills the space above them, spreading and thinning.
  - fail: The steam pours down off the stones and pools on the floor; or sinks below the stones; or hangs as a fixed shape without rising; or streams straight down from the ladle.
- P2 [core · process_direction]
  - expect: The burst comes when the water lands and then eases, and the plume moves outward and away.
  - fail: The steam bursts before the water reaches the stones; or the plume runs back into the stones; or a puff retreats toward the stones; or the burst grows steadily with no more water poured.
- P3 [core · permanence_count]
  - expect: The water that lands turns to steam rather than staying pooled on the hot stones.
  - fail: The poured water lies in a pool on the stones and stays; or water runs off the stones as a stream and gathers below; or the water goes with no steam appearing; or steam appears above the stones with no water poured.
- P4 [major · material_response]
  - expect: The water falls as a thin liquid and the steam is a soft cloud that spreads and fades; the stones stay hard where no water fell.
  - fail: The water bounces off the stones as a solid lump; or the steam holds a fixed rigid shape; or the stones sag or crumble as the water lands; or the steam pours like a liquid.
- P5 [fatal · shape_identity]
  - expect: The stones keep their number and shapes in their basket and the ladle stays a ladle.
  - fail: A stone vanishes; or a stone changes into another object; or the stones merge into one lump; or the ladle passes through the stones.
- P6 [minor · attribute_drift]
  - expect: The stones' colour away from the water, the basket and the room's wood stay the same.
  - fail: The stones change colour where no water fell; or the basket changes shape; or the wood panelling changes pattern.

**Note.** The hiss is sound and is not judged. Who ladles the water is not judged.

## HEAT-0061 · boil_steam · train

**Caption.** The lid of a large pot of dumplings is lifted at a street stall, and steam rolls up out of the pot into the cold air.

**Expectation (hidden).** Steam rises and hangs visibly in the cold air before fading; the dumplings sit in bubbling water below; steam does not sink.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] A large pot of dumplings with a lid stands at a stall.
- S2 [core] The lid is lifted.
- S3 [core] Steam rolls up out of the pot.
- S4 [core] The dumplings sit in bubbling water below.
- S5 [minor] The steam hangs visibly in the cold air before it fades.
- S6 [minor] The lift comes first and the steam follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The steam rises out of the pot, spreading and thinning as it climbs.
  - fail: The steam pours down the pot's sides and pools; or sinks to the ground; or stays in the pot with the lid off; or streams straight down from the rim.
- P2 [core · process_direction]
  - expect: The steam escapes as the lid comes off and the plume moves outward and away; puffs that have left keep going.
  - fail: The plume runs back into the pot; or a puff retreats to the water; or steam billows before the lid has moved; or steam appears above the closed lid and sinks into it.
- P3 [major · missing_consequence]
  - expect: The pot shows the boil: bubbles break the water's surface around the dumplings and the dumplings are wet.
  - fail: The water is glassy still while a thick plume pours from it; or the dumplings sit dry in the water; or steam rises from a pot with no water in it.
- P4 [major · material_response]
  - expect: The steam is a soft cloud that spreads, waves and fades; the dumplings are soft parcels that jostle; the lid is a rigid piece.
  - fail: The steam holds a fixed rigid shape; or pours like a liquid over the rim; or a dumpling shatters; or the lid bends like cloth as it lifts.
- P5 [fatal · permanence_count]
  - expect: One pot with one lid; the dumplings keep their number and stay in the pot.
  - fail: A dumpling vanishes; or new dumplings appear with none added; or the lid passes through the pot's rim; or a dumpling passes through the pot's wall.
- P6 [minor · attribute_drift]
  - expect: The pot, the stall and the surroundings stay the same.
  - fail: The pot changes colour; or the stall's signs change; or items around the stall rearrange.

## HEAT-0062 · boil_steam · train

**Caption.** A dishwasher door is opened at the end of its cycle, and a wave of steam rolls up and out of the machine.

**Expectation (hidden).** The steam escapes upward past the door and thins; the dishes inside are wet and hot; steam does not flow down onto the floor.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] A dishwasher.
- S2 [core] Its door is opened.
- S3 [core] Steam rolls up and out of the machine.
- S4 [core] The dishes inside are wet.
- S5 [minor] The steam spreads above the open door.
- S6 [minor] The opening comes first and the steam follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The steam rises past the door and spreads above it, thinning as it climbs.
  - fail: The steam flows down over the door and pools on the floor; or sinks below the machine; or hangs as a fixed shape without rising; or pours downward out of the machine.
- P2 [core · process_direction]
  - expect: The steam escapes as the door opens and the plume moves outward and away; puffs that have left keep going.
  - fail: The plume runs back into the machine; or a puff retreats to the racks; or steam rolls out before the door has moved; or steam appears above the closed door and sinks into it.
- P3 [major · missing_consequence]
  - expect: The inside shows the hot wash: the dishes and racks are wet and the steam comes from them.
  - fail: The dishes are dry while a thick plume pours out; or the steam comes from the door's outside face; or steam pours from an empty machine with dry racks.
- P4 [major · material_response]
  - expect: The steam is a soft cloud that spreads and fades; the door is a rigid panel on its hinge and the dishes stay rigid in their racks.
  - fail: The steam holds a fixed rigid shape; or pours like a liquid over the door's edge; or the door bends as it opens; or the dishes sag in the racks.
- P5 [fatal · permanence_count]
  - expect: One machine with one door; the dishes keep their number and stay in the racks.
  - fail: A dish vanishes; or new dishes appear; or the door passes through the machine's frame; or a dish passes through a rack.
- P6 [minor · attribute_drift]
  - expect: The machine's front, the kitchen units and the floor stay the same.
  - fail: The machine changes colour; or the units change; or the floor's pattern changes.

## HEAT-0063 · boil_steam · train

**Caption.** A coffee pot on a warming plate is nearly empty, and the last of the coffee bubbles and steams in the bottom.

**Expectation (hidden).** Small bubbles form and burst in the shallow liquid, steam rises, and the level drops further; the coffee does not increase in volume.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A coffee pot stands on a warming plate.
- S2 [core] A shallow layer of coffee lies in its bottom.
- S3 [core] Bubbles form and burst in the coffee.
- S4 [core] Steam rises from the pot.
- S5 [minor] The pot is nearly empty.
- S6 [minor] The level drops further.

**PC**
- P1 [core · process_direction]
  - expect: The level only drops while the pot sits on the plate, and bubbles keep forming while steam keeps rising.
  - fail: The level rises with nothing poured in; or the bubbling stops and then starts again by itself; or the steam runs back into the pot; or the level rises and falls in turn.
- P2 [core · permanence_count]
  - expect: The coffee leaves only as steam and no coffee appears in the pot.
  - fail: Coffee appears in the pot with none poured in; or the layer vanishes in a single frame; or a second pot appears; or coffee passes through the pot's glass.
- P3 [major · gravity_direction]
  - expect: The bubbles rise through the shallow layer and burst at its surface, and the steam rises out of the pot.
  - fail: Bubbles sink through the layer; or hang still in the coffee; or the steam sinks over the rim and pools on the plate; or the steam pours downward from the spout.
- P4 [major · material_response]
  - expect: The coffee is a thin liquid that lies level in the pot's bottom and shifts as bubbles burst; the pot stays rigid glass.
  - fail: The shallow layer stands as a dome; or the coffee moves as a solid mass; or the pot's glass flexes; or the layer climbs the pot's wall and stays.
- P5 [fatal · shape_identity]
  - expect: One pot with one handle and one spout on one plate; the pot keeps its shape.
  - fail: The pot changes shape; or a second spout appears; or the pot merges with the plate; or the handle detaches and floats.
- P6 [minor · attribute_drift]
  - expect: The pot's markings, the plate and the counter stay the same.
  - fail: The pot's markings change; or the plate changes colour; or items on the counter rearrange.

**Note.** Darkening or burning of the coffee is chemistry and is not judged.

## HEAT-0064 · boil_steam · train

**Caption.** A pan of water on a stove is at a boil, and the burner is turned off; the bubbling dies down and only faint steam remains.

**Expectation (hidden).** The churning stops within seconds of the heat going off and steam fades gradually; the water does not keep boiling with no heat or stop instantly.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] A pan of boiling water sits on a hob.
- S2 [core] The burner is turned off.
- S3 [core] The bubbling dies down.
- S4 [core] Faint steam still rises afterwards.
- S5 [minor] The bubbling is vigorous before the knob is turned.
- S6 [minor] The order is boiling, knob turned, bubbling eased.

**PC**
- P1 [core · missing_consequence]
  - expect: The bubbling begins to ease after the knob is turned, and not before.
  - fail: The bubbling eases before the knob is touched; or the knob is turned and the water churns as hard as before to the end of the clip; or the boil grows after the knob is turned off; or the churn stops before the hand reaches the knob.
- P2 [core · process_direction]
  - expect: The easing runs one way: the churn dies down and the water does not come back to a rolling boil with the burner off.
  - fail: The water returns to a rolling boil with the burner off; or the bubbling eases and surges in turn; or the churn stops in a single frame with the surface instantly flat; or the steam thickens after the burner is off.
- P3 [major · gravity_direction]
  - expect: The remaining bubbles rise to the surface and the faint steam rises above the pan.
  - fail: Bubbles sink from the surface downward; or the steam sinks over the rim and pools on the hob; or the steam pours downward from the pan; or bubbles hang still in the water.
- P4 [major · material_response]
  - expect: The water settles as a liquid: the surface goes from churning to shifting to nearly flat and finds its level.
  - fail: The surface holds its churned shape frozen in place; or the water stands in a heap above its level; or the water sets solid; or the surface keeps a fixed pattern of peaks after the churn has stopped.
- P5 [fatal · permanence_count]
  - expect: One pan of water on one hob; the water stays in the pan.
  - fail: Water passes through the pan's wall; or the level jumps up with nothing added; or a second pan appears; or the pan changes shape.
- P6 [minor · attribute_drift]
  - expect: The pan, the burner and the surroundings stay the same.
  - fail: The pan changes colour; or the burner's knob moves by itself; or items around the hob rearrange.

**Note.** How quickly the boil dies down is not judged, only that it eases after the knob is turned and does not return.

## HEAT-0065 · boil_steam · train

**Caption.** A geyser in a national park erupts, sending a column of boiling water and steam high into the air before it falls back.

**Expectation (hidden).** The water rises as a column, slows at the top, and falls back down around the vent while the steam keeps drifting upward and away.

**Declared violation types.** gravity_direction, trajectory_momentum, process_direction

**SA**
- S1 [core] A geyser vent in the ground.
- S2 [core] A column of water and steam rises from the vent.
- S3 [core] The column reaches high into the air.
- S4 [core] The water falls back around the vent.
- S5 [minor] Steam drifts away above the column.
- S6 [minor] The rise comes first and the fall follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The water rises from the vent, slows as it climbs and falls back down around the vent, while the steam keeps rising and drifting.
  - fail: The water keeps climbing out of view without slowing or falling; or the fallen water travels upward from the ground; or the steam sinks and pools around the vent; or the column hangs at a fixed height without rising or falling.
- P2 [core · trajectory_momentum]
  - expect: The drops leave the vent going up and follow arcs that bend over and come down, spreading as they go.
  - fail: The drops climb in straight lines and stop dead at the top; or the column bends sideways and stays level with nothing blowing it; or the drops return along the line they rose on and re-enter the vent; or the spray gathers into a rising ball.
- P3 [core · process_direction]
  - expect: The eruption builds and then eases, and water that has fallen back stays down.
  - fail: Fallen water rises back into the column with no fresh eruption; or the column's height jumps up and down in steps; or the eruption stops and restarts in the same instant.
- P4 [major · material_response]
  - expect: The water breaks into spray and drops as it rises and splashes where it lands; the steam is a soft cloud that spreads.
  - fail: The column stays a rigid rod of water; or the spray holds a fixed shape in the air; or the steam turns into solid lumps; or the fallen water lies as a heap above the ground.
- P5 [fatal · permanence_count]
  - expect: One vent; the water comes out of it and falls back to the ground around it.
  - fail: Water appears in the air away from the column; or a second column rises from bare ground; or the column vanishes at a stroke while still high; or the vent moves across the ground.
- P6 [minor · attribute_drift]
  - expect: The ground around the vent, its mineral crust and the background stay the same.
  - fail: The crust changes colour; or the ground's shape changes between frames; or the hills behind change.

## HEAT-0066 · boil_steam · train

**Caption.** Wet spinach is tossed into a very hot pan, and a burst of steam rises with a loud hiss as the leaves wilt.

**Expectation (hidden).** The steam rises the moment the wet leaves touch the pan; the leaves shrink and go limp within seconds and do not spring back.

**Declared violation types.** gravity_direction, process_direction, material_response

**SA**
- S1 [core] A hot pan.
- S2 [core] Wet spinach is tossed into the pan.
- S3 [core] A burst of steam rises.
- S4 [core] The leaves wilt: they go limp and shrink.
- S5 [minor] The leaves look wet as they go in.
- S6 [minor] The toss comes first, then the steam, then the wilting.

**PC**
- P1 [core · gravity_direction]
  - expect: The steam rises from the pan, spreading and thinning, while the leaves stay down in the pan.
  - fail: The steam pours down the pan's sides and pools on the hob; or sinks below the pan; or a leaf rises out of the pan and hangs above it; or the steam hangs as a fixed shape without rising.
- P2 [core · process_direction]
  - expect: The burst comes when the wet leaves meet the pan and then eases; the wilting only advances and the leaves do not stiffen again.
  - fail: The steam bursts before the leaves reach the pan; or a wilted leaf springs back crisp and upright; or the burst grows stronger with nothing added; or the leaves wilt and then swell back.
- P3 [core · material_response]
  - expect: The leaves go from stiff wet sheets to limp glossy folds that collapse into the pan and shrink, and the water on them turns to steam.
  - fail: The leaves stay stiff and flat while glossy and shrinking; or a leaf shatters dry; or the leaves melt into a liquid; or the leaves swell up and stiffen.
- P4 [major · missing_consequence]
  - expect: The burst comes from the wet leaves meeting the hot metal: it is fiercest as they land and the pan goes wet where they lie.
  - fail: The steam pours from a part of the pan no leaf touched; or the leaves land and the pan stays dry with no steam at all; or the burst is fiercest long after the leaves have settled and gone limp.
- P5 [fatal · permanence_count]
  - expect: The leaves in the pan are the leaves that were tossed in; they shrink rather than vanishing.
  - fail: A leaf vanishes in a single frame while still whole; or new leaves appear with none added; or a leaf passes through the pan's wall; or the leaves merge into one smooth sheet.
- P6 [minor · attribute_drift]
  - expect: The pan's finish and the hob stay the same.
  - fail: The pan changes colour; or its handle changes shape; or items around the hob rearrange.

**Note.** The hiss is sound and is not judged. The leaves darkening as they cook is chemistry and is not judged.

## HEAT-0067 · boil_steam · train

**Caption.** A locomotive at a heritage railway lets off steam, and a great white cloud rolls up from beside the wheels.

**Expectation (hidden).** The cloud bursts out and rises, thinning as it spreads; it does not sink and lie along the track.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] A steam locomotive.
- S2 [core] A white cloud of steam bursts out from beside its wheels.
- S3 [core] The cloud rolls upward.
- S4 [minor] The cloud is large and white.
- S5 [minor] The cloud thins as it spreads.

**PC**
- P1 [core · gravity_direction]
  - expect: The cloud leaves the locomotive's side low down and rises, spreading and thinning.
  - fail: The cloud sinks and lies along the track; or flows away down the ballast like water; or hangs as a fixed shape without rising; or pours downward under the locomotive and stays there.
- P2 [core · process_direction]
  - expect: The burst comes out and moves away from the locomotive; puffs that have left keep going.
  - fail: The cloud runs back into the locomotive; or a puff retreats toward the cylinder; or steam appears in the air away from the locomotive and drifts into it; or the cloud grows with no steam leaving the engine.
- P3 [major · missing_consequence]
  - expect: The steam issues from an opening on the locomotive low beside the wheels and is thickest there.
  - fail: The cloud is thickest far from the locomotive with nothing carrying it there; or the cloud appears above the boiler while nothing leaves the engine's side; or the locomotive stands clear of any cloud while a cloud rolls along the platform.
- P4 [major · material_response]
  - expect: The steam is a soft cloud that billows, spreads and fades; the locomotive stays a rigid machine.
  - fail: The steam holds a fixed rigid shape; or pours like a liquid; or the cloud lifts the locomotive; or the steam breaks into solid lumps.
- P5 [fatal · permanence_count]
  - expect: One locomotive on the track; it keeps its wheels and fittings and passes through nothing.
  - fail: A wheel vanishes; or a second locomotive appears; or the locomotive passes through the platform; or the locomotive changes shape.
- P6 [minor · attribute_drift]
  - expect: The locomotive's livery, its number and the platform stay the same.
  - fail: The livery changes colour; or the number changes; or the platform's signs change.

**Note.** The locomotive is a driven machine; whether it moves and how fast are not judged.

## HEAT-0068 · boil_steam · train

**Caption.** Water is poured onto the hot coals of a barbecue after cooking, and a hissing cloud of steam rises from the grill.

**Expectation (hidden).** Steam rises in a burst where the water hits and the coals darken and stop glowing there; the water does not stay pooled on hot coals.

**Declared violation types.** gravity_direction, process_direction, permanence_count

**SA**
- S1 [core] A barbecue holds hot coals.
- S2 [core] Water is poured onto the coals.
- S3 [core] A cloud of steam rises from the grill.
- S4 [core] The coals darken where the water lands.
- S5 [minor] The coals glow before the water is poured.
- S6 [minor] The pour comes first and the steam follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The water falls downward onto the coals while the steam rises from them, spreading and thinning.
  - fail: The water travels upward from the jug; or the steam pours down over the barbecue's sides and pools; or the steam sinks below the grill; or the cloud hangs as a fixed shape without rising.
- P2 [core · process_direction]
  - expect: The coals' glow only fades where the water lands and does not return there; the burst of steam comes at the pour and then eases.
  - fail: A doused coal glows brightly again with no more fuel; or the glow spreads to coals the water has already darkened; or steam bursts before the water reaches the coals; or the burst grows stronger with no more water poured.
- P3 [core · permanence_count]
  - expect: The water that lands turns to steam or soaks the ash rather than lying in a pool on the glowing coals.
  - fail: The poured water stands in a clear pool on the glowing coals and stays; or the water goes with no steam appearing; or steam appears above the grill with no water poured; or the coals vanish where the water lands.
- P4 [major · material_response]
  - expect: The water falls as a thin liquid, the steam is a soft cloud that spreads, and the coals stay hard lumps that may crack and darken.
  - fail: The water bounces off the coals as a solid lump; or the steam holds a fixed rigid shape; or the coals sag or flow like wax; or the steam pours like a liquid.
- P5 [fatal · shape_identity]
  - expect: The coals keep their number and lumpy shapes in the grill, and the barbecue keeps its shape.
  - fail: A coal changes into another object; or the coals merge into one smooth mass; or a coal vanishes leaving no ash; or the barbecue's bowl changes shape.
- P6 [minor · attribute_drift]
  - expect: The barbecue's body, the grill bars and the surroundings stay the same.
  - fail: The barbecue changes colour; or the grill bars change spacing; or items around the barbecue rearrange.

## HEAT-0069 · boil_steam · train

**Caption.** A hot pot bubbles in the centre of a dinner table, and thin slices of meat dropped into the broth curl up and rise to the surface.

**Expectation (hidden).** Steam rises from the broth, the slices curl and float up within seconds, and the broth keeps bubbling; the slices do not sink and lie flat.

**Declared violation types.** process_direction, causeless_motion

**SA**
- S1 [core] A hot pot bubbles in the centre of a table.
- S2 [core] Thin slices of meat are dropped into the broth.
- S3 [core] The slices curl up.
- S4 [core] The slices rise to the surface.
- S5 [minor] Steam rises from the broth.
- S6 [minor] The drop comes first, then the curling, then the rise.

**PC**
- P1 [core · process_direction]
  - expect: Each slice only curls further and, once it is at the surface, stays up, while the broth keeps bubbling.
  - fail: A curled slice flattens out again in the broth; or a slice that has surfaced sinks back to the bottom and stays there; or the slices curl and uncurl in turn; or the bubbling stops and then starts again by itself.
- P2 [core · causeless_motion]
  - expect: The slices move as the churning broth carries them and as they curl, and they jostle at the surface.
  - fail: A slice darts across the pot with the broth still; or a slice travels against the churn; or a slice leaps out of the broth with nothing lifting it; or a slice spins fast on the spot with nothing turning it.
- P3 [major · gravity_direction]
  - expect: The slices sink as they go in, then rise to the surface and ride there partly submerged, while the bubbles and steam rise.
  - fail: A slice sits wholly on top of the broth like a leaf on a sheet; or a slice hangs motionless in mid-broth; or bubbles sink toward the pot's floor; or the steam sinks and pools on the table.
- P4 [major · material_response]
  - expect: The slices are limp sheets that curl and fold and hold together, and the broth closes round them.
  - fail: A slice stays a flat rigid plate while rising; or a slice breaks into crumbs; or the slices fuse into one lump; or the broth holds a dent around a slice.
- P5 [fatal · permanence_count]
  - expect: The slices in the pot are the slices that were dropped in and they keep their number.
  - fail: A slice vanishes; or new slices appear with none added; or a slice passes through the pot's wall; or two slices merge into one thicker piece.
- P6 [minor · attribute_drift]
  - expect: The pot, the table and the broth's colour stay the same.
  - fail: The pot changes colour; or the table's setting rearranges; or the broth changes colour.

**Note.** The meat's colour change as it cooks is chemistry and is not judged.

## HEAT-0070 · boil_steam · train

**Caption.** A jet of steam from a wallpaper steamer plate softens old wallpaper, and the paper peels away in wet strips.

**Expectation (hidden).** Steam escapes upward around the plate's edges; the paper darkens and loosens only where steamed; the strips hang and fall downward.

**Declared violation types.** gravity_direction, material_response, process_direction

**SA**
- S1 [core] A steamer plate is held against a papered wall.
- S2 [core] Steam escapes from around the plate.
- S3 [core] The wallpaper loosens where the plate has been.
- S4 [core] The paper peels away in strips.
- S5 [minor] The strips look wet and darkened.
- S6 [minor] The steaming comes first and the peeling follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The steam escapes upward around the plate's edges and the loosened strips hang and fall downward.
  - fail: The steam pours downward through the wall; or sinks and pools on the floor; or a loosened strip hangs upward from its top edge with nothing holding it; or a fallen strip rises toward the ceiling.
- P2 [core · material_response]
  - expect: The paper goes from dry and stuck to wet, dark and limp where the steam reaches it, and comes away in soft floppy strips.
  - fail: The paper stays dry and pale while peeling; or a strip snaps off as a rigid board; or the paper turns to liquid and runs down the wall; or a strip stretches like rubber as it is pulled.
- P3 [core · process_direction]
  - expect: The paper only loosens where the steam has been and loosened paper stays loose.
  - fail: A loosened strip presses itself back onto the wall and sticks; or the paper loosens on a part of the wall the plate has not reached; or the paper dries pale again while the steamer works on it; or the paper loosens and re-sticks in turn.
- P4 [major · missing_consequence]
  - expect: The plate's path shows: the wall behind the peeled strips is bare and damp while paper away from the plate stays stuck.
  - fail: The wall behind a peeled strip is dry and dusty; or paper comes away from a part of the wall the plate never touched; or the plate is held on the wall and the paper there stays dry and tight to the end of the clip.
- P5 [fatal · permanence_count]
  - expect: One plate on one wall; strips come off the wall and neither appear nor vanish.
  - fail: A strip vanishes in mid-air; or new paper appears on the bare wall; or the plate passes into the wall; or a second plate appears.
- P6 [minor · attribute_drift]
  - expect: The wallpaper's pattern away from the peeled area and the room stay the same.
  - fail: The wallpaper's pattern changes; or the bare wall changes colour; or items in the room rearrange.

## HEAT-0071 · boil_steam · train

**Caption.** Rain falls on a sun-baked road, and steam rises from the hot asphalt as the drops hit.

**Expectation (hidden).** The rain falls downward and the steam rises upward off the surface; wet patches spread and the steaming fades as the road cools.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] Rain falls on a road.
- S2 [core] Steam rises from the road's surface.
- S3 [core] The road reads as sun-baked: bright and dry away from the wet patches.
- S4 [minor] Wet patches spread on the road.
- S5 [minor] The rain falls first and the steam follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The rain falls downward onto the road and the steam rises upward off the surface.
  - fail: The rain rises from the road; or the steam sinks and flows along the road like water; or the steam pours downward into the asphalt; or the raindrops hang still in the air.
- P2 [core · process_direction]
  - expect: The wet patches only spread while the rain falls and the steaming only eases as the road cools; steam that has left keeps rising.
  - fail: The steam runs back into the road; or a puff retreats to the surface; or a wet patch dries back to bright dry asphalt while the rain still falls on it; or the steaming grows stronger the longer the rain falls.
- P3 [major · missing_consequence]
  - expect: The steam rises where drops land on hot asphalt and not from surfaces the rain misses.
  - fail: Steam rises from a dry patch no rain has reached; or drops land and the road stays dry with no steam and no wet mark; or the steam pours from the grass verge rather than the road.
- P4 [major · material_response]
  - expect: The drops splash and spread on the asphalt, the steam is a soft cloud that waves and fades, and the road stays a hard surface.
  - fail: The drops bounce off the road as solid beads and stay round; or the steam holds a fixed rigid shape; or the asphalt ripples like water; or the drops stand as domes on the road.
- P5 [fatal · permanence_count]
  - expect: One road; the rain falls onto it and the wet marks come from the drops.
  - fail: A wet patch appears where no rain fell; or the road's surface opens up; or a puddle vanishes at a stroke; or the road changes shape.
- P6 [minor · attribute_drift]
  - expect: The road markings, the kerb and the surroundings stay the same.
  - fail: The road markings change; or the kerb changes shape; or the buildings or trees behind change between frames.

## HEAT-0072 · boil_steam · train

**Caption.** A glowing piece of metal is plunged into a bucket of water, and a cloud of steam bursts up from the bucket.

**Expectation (hidden).** The steam erupts the instant the metal enters, rises, and fades; the metal loses its glow in the water and does not glow again.

**Declared violation types.** gravity_direction, process_direction, attribute_drift

**SA**
- S1 [core] A glowing piece of metal.
- S2 [core] The metal is plunged into a bucket of water.
- S3 [core] A cloud of steam bursts up from the bucket.
- S4 [core] The metal loses its glow in the water.
- S5 [minor] The metal glows before it enters the water.
- S6 [minor] The plunge comes first and the steam follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The metal goes downward into the water while the steam bursts upward out of the bucket, spreading and thinning.
  - fail: The metal rises out of the water with nothing lifting it; or the steam pours down the bucket's sides and pools; or the steam sinks below the bucket; or the cloud hangs as a fixed shape without rising.
- P2 [core · process_direction]
  - expect: The burst comes as the metal enters and then eases, and the metal's glow only fades while it is in the water.
  - fail: The steam bursts before the metal reaches the water; or the metal glows brighter in the water; or the glow goes and comes back while the metal stays submerged; or the burst grows stronger the longer the metal sits in the water.
- P3 [core · attribute_drift]
  - expect: The change is in the metal: it goes from glowing to dark and stays dark in the water.
  - fail: The water glows rather than the metal; or the metal's glow moves onto the bucket; or the metal's glow spreads through the water as a glowing cloud.
- P4 [major · material_response]
  - expect: The water boils hard around the metal and closes over it, the metal stays a rigid piece, and the steam is a soft cloud that spreads.
  - fail: The water stays glassy still as the glowing metal enters; or the metal bends or melts in the water; or the steam holds a fixed rigid shape; or the water stands in a heap above the bucket's rim.
- P5 [fatal · permanence_count]
  - expect: One piece of metal and one bucket; the metal goes into the water and stays there.
  - fail: The metal vanishes in the water; or a second piece appears; or the metal passes through the bucket's wall; or the water's level jumps with nothing added.
- P6 [minor · attribute_drift]
  - expect: The bucket, the tongs and the surroundings stay the same.
  - fail: The bucket changes colour; or the tongs change shape; or items around the bucket rearrange.

## HEAT-0073 · boil_steam · train

**Caption.** A ladle of hot broth is poured over cold noodles in a bowl, and a puff of steam rises from the bowl.

**Expectation (hidden).** Steam rises where the hot broth lands; the broth flows down around the noodles; the puff thins as the bowl cools.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] A bowl of noodles.
- S2 [core] Hot broth is poured over them from a ladle.
- S3 [core] A puff of steam rises from the bowl.
- S4 [minor] The broth flows down around the noodles.
- S5 [minor] The puff thins after the pour.
- S6 [minor] The pour comes first and the steam follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The broth falls downward from the ladle into the bowl and spreads around the noodles while the steam rises.
  - fail: The broth travels upward from the ladle; or the steam sinks over the bowl's rim and pools on the table; or the broth climbs the bowl's wall and stays above its level; or the steam pours downward from the ladle.
- P2 [core · process_direction]
  - expect: The steam appears where the hot broth lands and the puff thins after the pour, while the bowl's level only rises during it.
  - fail: Steam rises from the bowl before the broth reaches it; or the puff grows steadily after the pour has stopped; or the steam runs back into the bowl; or the level drops while broth still pours in.
- P3 [major · missing_consequence]
  - expect: The pour has an effect: the noodles are pushed and wetted where the stream lands and the bowl fills.
  - fail: The stream enters and the noodles stay dry and unmoved; or the level rises with no stream reaching the bowl; or the noodles float dry on top of the broth.
- P4 [major · material_response]
  - expect: The broth is a thin liquid that falls as a stream and finds its level, the noodles are limp strands that shift and soak, and the steam is a soft cloud.
  - fail: The stream falls as a rigid rod; or the broth stands in a heap above the rim; or the noodles stay stiff and rigid in the hot broth; or the steam holds a fixed rigid shape.
- P5 [fatal · permanence_count]
  - expect: One ladle and one bowl; the broth goes from ladle to bowl and nowhere else.
  - fail: Broth appears in the bowl with no stream reaching it; or the stream passes through the bowl's wall; or noodles appear or vanish; or a second bowl appears.
- P6 [minor · attribute_drift]
  - expect: The bowl's pattern, the table and the noodles' colour stay the same.
  - fail: The bowl's pattern changes; or the table's setting rearranges; or the noodles change colour.

## HEAT-0074 · boil_steam · train

**Caption.** Boiling water is poured over a tea bag in a glass, and steam rises while the colour spreads from the bag.

**Expectation (hidden).** Steam rises from the glass; the colour drifts out of the bag into the water and does not gather back into the bag.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] A tea bag sits in a glass.
- S2 [core] Boiling water is poured over the bag.
- S3 [core] Steam rises from the glass.
- S4 [core] Colour spreads from the bag into the water.
- S5 [minor] The bag stays in the glass.
- S6 [minor] The pour comes first and the colouring follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The water falls downward into the glass and the steam rises from it, while the colour sinks and spreads through the water.
  - fail: The water travels upward from the kettle; or the steam sinks over the glass's rim and pools; or the colour climbs out of the water; or the steam pours downward from the spout.
- P2 [core · process_direction]
  - expect: The water only grows more coloured while the bag sits in it and the colour does not gather back into the bag.
  - fail: The water clears again while the bag stays in it; or the colour draws back into the bag; or the water darkens and lightens in turn; or the water is dark before the bag is in it.
- P3 [major · missing_consequence]
  - expect: The colour comes out of the bag: it streams from where the bag sits and the water near it darkens first.
  - fail: The water darkens evenly all over before any colour leaves the bag; or colour appears at the far side of the glass with none spreading from the bag; or the bag sits in hot water and the water stays clear to the end of the clip.
- P4 [major · material_response]
  - expect: The bag is a limp paper pouch that swells and sinks and sheds colour, and the water is a thin liquid that swirls and finds its level.
  - fail: The bag stays a rigid flat packet in the water; or the bag dissolves away into the water; or the water stands in a heap above the rim; or the colour moves as a solid mass through the water.
- P5 [fatal · permanence_count]
  - expect: One bag in one glass; the bag stays whole and the water comes only from the pour.
  - fail: The bag vanishes; or a second bag appears; or the bag passes through the glass's wall; or the water's level jumps with nothing poured.
- P6 [minor · attribute_drift]
  - expect: The glass, the bag's tag and the counter stay the same.
  - fail: The glass changes shape; or the tag changes; or items on the counter rearrange.

## HEAT-0075 · boil_steam · train

**Caption.** A car with an overheated engine sits at the roadside with steam pouring out from under the hood.

**Expectation (hidden).** The steam escapes upward from the edges of the hood and grille and drifts away; it does not run down the front of the car.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] A car stands at a roadside.
- S2 [core] Steam pours out from under its hood.
- S3 [core] The steam rises.
- S4 [minor] The steam escapes at the hood's edges or the grille.
- S5 [minor] The steam drifts away and thins.

**PC**
- P1 [core · gravity_direction]
  - expect: The steam leaves the hood's gaps going up and spreads and thins as it climbs.
  - fail: The steam runs down the front of the car and pools on the road; or sinks under the car and stays; or hangs as a fixed shape without rising; or pours downward from the grille onto the road.
- P2 [core · process_direction]
  - expect: The plume moves outward and away from the car; puffs that have left keep going.
  - fail: The plume runs back under the hood; or a puff retreats toward the grille; or steam appears in the air away from the car and drifts into it; or the plume grows with nothing leaving the car.
- P3 [major · missing_consequence]
  - expect: The steam comes out of the engine bay at the hood's edges, the grille or the wheel arch and is thickest there.
  - fail: The steam comes out of the car's boot or its windows; or the plume is thickest far from the car with nothing carrying it there; or the hood's gaps are clear while steam appears above the roof with nothing leaving the bay.
- P4 [major · material_response]
  - expect: The steam is a soft cloud that billows and fades and the car stays a rigid body with its hood shut or propped.
  - fail: The steam holds a fixed rigid shape; or pours like a liquid over the bumper; or the hood bends like cloth; or the steam lifts the car.
- P5 [fatal · permanence_count]
  - expect: One car with one hood; the car keeps its panels and wheels and passes through nothing.
  - fail: A wheel vanishes; or a second car appears; or the hood passes through the windscreen; or the car changes shape.
- P6 [minor · attribute_drift]
  - expect: The car's paint, its number plate and the roadside stay the same.
  - fail: The car changes colour; or the plate's characters change; or the roadside changes between frames.

**Note.** Whether the engine is running is not judged and no driver need be shown.

## HEAT-0076 · boil_steam · train

**Caption.** A lid is lifted from a pan of steamed vegetables, and steam rises to fog the range hood above.

**Expectation (hidden).** The steam rises straight to the hood and spreads under it; the hood's metal fogs where the steam touches; steam does not sink toward the counter.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] A pan of vegetables with a lid stands under a range hood.
- S2 [core] The lid is lifted.
- S3 [core] Steam rises from the pan.
- S4 [core] The hood above fogs where the steam reaches it.
- S5 [minor] The steam spreads under the hood.
- S6 [minor] The order is lift, rise, fogging.

**PC**
- P1 [core · gravity_direction]
  - expect: The steam rises straight from the pan to the hood and spreads under it.
  - fail: The steam sinks toward the counter and pools; or pours down the pan's sides; or hangs as a fixed shape without rising; or travels down from the hood into the pan.
- P2 [core · process_direction]
  - expect: The steam keeps leaving the pan and the fogging on the hood only builds while the steam reaches it.
  - fail: The plume runs back into the pan; or the fog on the hood clears while steam still hits it; or the hood fogs before the lid is off; or a puff retreats toward the pan.
- P3 [major · missing_consequence]
  - expect: The hood fogs where the steam meets it and stays clearer away from the plume.
  - fail: The hood fogs evenly all over while the plume hits one spot; or the hood fogs in a place the steam never reaches; or the steam hits the hood and its metal stays dry and bright.
- P4 [major · material_response]
  - expect: The steam is a soft cloud that spreads and fades, the fog on the hood is a fine haze that may bead, and the lid is a rigid piece.
  - fail: The steam holds a fixed rigid shape; or the fog on the hood stands out as a thick crust; or the lid bends like cloth as it lifts; or the steam pours like a liquid over the hood's lip.
- P5 [fatal · permanence_count]
  - expect: One pan with one lid under one hood; the vegetables keep their number and stay in the pan.
  - fail: A vegetable vanishes; or new vegetables appear; or the lid passes through the pan's rim; or the hood changes shape.
- P6 [minor · attribute_drift]
  - expect: The hood's metal away from the fog, the pan and the hob stay the same.
  - fail: The hood changes colour; or the pan changes shape; or the hob's knobs move by themselves.

## HEAT-0077 · boil_steam · train

**Caption.** A saucepan of milk on a stove begins to boil, and the milk foams up rapidly toward the rim.

**Expectation (hidden).** The foam rises quickly and climbs the sides, threatening to spill; if the pan is lifted off the heat the foam sinks back; it does not stay as a static layer.

**Declared violation types.** process_direction, material_response

**SA**
- S1 [core] A saucepan of milk sits on a hob.
- S2 [core] The milk foams up.
- S3 [core] The foam climbs toward the rim.
- S4 [minor] The foam rises fast enough to threaten a spill.
- S5 [minor] The milk lies flat before the foam rises.

**PC**
- P1 [core · process_direction]
  - expect: The foam only rises while the pan stays on the heat; it falls back only if the pan is lifted off.
  - fail: The foam sinks back while the pan sits on the burner with nothing changed; or the foam rises and falls in turn on the heat; or the foam rises before the milk has begun to bubble; or the foam collapses and swells again with nothing touched.
- P2 [core · material_response]
  - expect: The milk is a liquid that throws up a thick bubbly foam which climbs the pan's wall and collapses when it spills or cools.
  - fail: The milk stays a flat mirror while foam stands above it; or the foam stands as rigid spikes that keep their shape when the pan is moved; or the milk sets solid; or the foam pours off as a thin clear liquid.
- P3 [major · gravity_direction]
  - expect: The foam climbs the inside of the pan and, if it goes over, runs down the outside, while the milk otherwise stays in the pan.
  - fail: The foam climbs the outside of the pan and goes in over the rim; or foam lifts off the pan and hangs above it; or foam runs upward on the pan's outside; or the milk runs up the pan's wall and out with no foam at the rim.
- P4 [major · missing_consequence]
  - expect: Foam near the rim means the milk below has risen: the level and the foam go up together.
  - fail: The foam reaches the rim while the visible milk below is calm and far from full; or the milk's level drops while the foam climbs; or the foam climbs while the surface below shows no bubbles.
- P5 [fatal · permanence_count]
  - expect: One pan of milk; the milk stays in the pan except where it spills over the rim.
  - fail: Milk passes through the pan's wall; or the level jumps up with nothing added; or a second pan appears; or the pan changes shape.
- P6 [minor · attribute_drift]
  - expect: The pan, the hob and the milk's colour stay the same.
  - fail: The pan changes colour; or the milk changes colour; or the hob's knobs move by themselves.

## HEAT-0078 · boil_steam · train

**Caption.** A vent pipe on a factory roof releases a steady plume of white steam into the winter sky.

**Expectation (hidden).** The plume rises from the pipe, bends with the wind, and thins with distance; it does not fall back onto the roof.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] A vent pipe stands on a factory roof.
- S2 [core] A plume of white steam leaves the pipe.
- S3 [core] The plume rises.
- S4 [minor] The plume bends as it climbs.
- S5 [minor] The plume thins with distance.

**PC**
- P1 [core · gravity_direction]
  - expect: The plume leaves the pipe's mouth going up, bends as it climbs and thins; it does not sink.
  - fail: The plume falls back onto the roof and pools; or flows down the pipe's side; or hangs as a fixed shape without rising or drifting; or pours downward out of the pipe.
- P2 [core · process_direction]
  - expect: The plume moves outward and away from the pipe; puffs that have left keep going.
  - fail: The plume runs back into the pipe; or a puff retreats toward the mouth; or steam appears in the sky away from the pipe and drifts into it; or the plume grows with nothing leaving the pipe.
- P3 [major · missing_consequence]
  - expect: The plume issues from the pipe's mouth and is densest there.
  - fail: The plume is densest far from the pipe with nothing carrying it there; or the pipe's mouth is clear and the plume starts in the air above it; or the steam rises from the roof's surface rather than the pipe.
- P4 [major · causeless_motion] (if: Flags, trees or other smoke in the scene show which way the wind blows.)
  - expect: The plume leans the same way as the other signs of wind in the scene.
  - fail: The plume leans against the direction the flags or trees show; or the plume stands straight up while nearby flags are stretched out; or the plume's lean changes while the flags hold steady.
- P5 [major · material_response]
  - expect: The steam is a soft cloud that spreads, waves and fades, and the pipe stays a rigid stack.
  - fail: The plume holds a fixed rigid shape; or pours like a liquid; or the pipe bends or sways with the plume; or the plume breaks into solid lumps.
- P6 [fatal · permanence_count]
  - expect: One pipe on one roof; the pipe stays in place and nothing passes through the roof.
  - fail: The pipe vanishes; or a second pipe appears; or the pipe sinks into the roof; or the roof changes shape.
- P7 [minor · attribute_drift]
  - expect: The roof, the pipe's paint and the buildings around stay the same.
  - fail: The pipe changes colour; or the roof's fittings rearrange; or the buildings behind change between frames.

**Note.** The wind itself is invisible; a plume that leans while rising is not a violation.

## HEAT-0079 · boil_steam · train

**Caption.** Frozen french fries are dropped into a pot of hot oil, and the oil erupts in bubbles and steam.

**Expectation (hidden).** The bubbling starts the moment the fries go in and is fiercest at first, easing as the frost is gone; steam rises; the oil level rises with the fries.

**Declared violation types.** process_direction, material_response, gravity_direction

**SA**
- S1 [core] A pot of hot oil.
- S2 [core] Frozen fries are dropped into the oil.
- S3 [core] The oil erupts in bubbles.
- S4 [core] Steam rises from the pot.
- S5 [minor] The bubbling is fiercest right after the fries go in.
- S6 [minor] The drop comes first and the eruption follows.

**PC**
- P1 [core · process_direction]
  - expect: The bubbling starts as the fries enter, is fiercest at first and then eases; it does not build up long after.
  - fail: The oil bubbles hard before the fries reach it; or the bubbling grows steadily with nothing added; or the bubbling stops and then starts again by itself; or the steam runs back into the oil.
- P2 [core · material_response]
  - expect: The oil is a thin liquid that throws up a mass of fine bubbles and foam and closes round the fries, and the fries stay firm sticks.
  - fail: The oil stays a flat mirror as the frozen fries enter; or the oil sets solid; or a fry melts away into the oil; or the foam stands as a rigid dome above the pot.
- P3 [core · gravity_direction]
  - expect: The fries fall downward into the oil and sink or ride at the surface while the bubbles and steam rise.
  - fail: A fry rises out of the oil and hangs above it; or bubbles sink toward the pot's floor; or the steam sinks over the rim and pools on the hob; or the oil climbs the pot's wall and stays above its level.
- P4 [major · missing_consequence]
  - expect: The fries show the oil: the frost on them goes and the oil's level rises as they go in.
  - fail: The fries sit in the bubbling oil with frost still on them to the end of the clip; or the oil's level drops as the fries go in; or the oil erupts in a part of the pot no fry reached.
- P5 [fatal · permanence_count]
  - expect: The fries in the pot are the fries that were dropped, and the oil stays in the pot.
  - fail: A fry vanishes; or new fries appear with none added; or oil passes through the pot's wall; or the oil's level jumps with nothing added.
- P6 [minor · attribute_drift]
  - expect: The pot, the hob and the oil's colour stay the same.
  - fail: The pot changes colour; or the oil changes colour; or items around the hob rearrange.

**Note.** The fries browning as they cook is chemistry and is not judged.

## HEAT-0080 · boil_steam · train

**Caption.** A glass electric kettle at a rolling boil clicks off, and the churning bubbles die down and the steam thins.

**Expectation (hidden).** The streams of bubbles from the base stop within moments of the click and the surface settles, while the steam from the spout weakens gradually; the water does not keep boiling hard with the element off or fall still in a single frame.

**Declared violation types.** process_direction, causeless_motion

**SA**
- S1 [core] A glass kettle is at a rolling boil.
- S2 [core] The kettle's switch clicks off.
- S3 [core] The streams of bubbles from the base stop.
- S4 [core] The surface settles.
- S5 [minor] Steam from the spout weakens after the click.
- S6 [minor] The order is boiling, switch off, settling.

**PC**
- P1 [core · process_direction]
  - expect: After the switch goes off the bubbling only eases and the water does not come back to a rolling boil, while the steam only thins.
  - fail: The water returns to a rolling boil with the switch off; or the bubbling eases and surges in turn; or the steam thickens after the switch is off; or the streams stop and then start again by themselves.
- P2 [core · causeless_motion]
  - expect: The water moves only as the dying boil carries it and then settles, and the kettle stays on its base.
  - fail: The water swirls or churns after the surface has settled with nothing stirring it; or the kettle rocks or slides with nothing touching it; or the switch moves back to on by itself; or the water churns while the switch is off and the base is quiet.
- P3 [major · missing_consequence]
  - expect: The switch acts on the boil: the streams of bubbles from the base stop and the surface settles after it, not before.
  - fail: The streams stop before the switch has moved; or the switch goes off and the streams run as hard as before to the end of the clip; or the surface settles while streams still run from the base.
- P4 [major · gravity_direction]
  - expect: The remaining bubbles rise to the surface and the steam leaves the spout upward.
  - fail: Bubbles sink from the surface to the base; or hang still in the water; or the steam sinks over the spout and pools on the counter; or the steam pours downward from the spout.
- P5 [fatal · permanence_count]
  - expect: One kettle on one base; the water stays inside and its level changes only by boiling away.
  - fail: Water passes through the glass; or the level jumps up with nothing added; or a second kettle appears; or the kettle changes shape.
- P6 [minor · attribute_drift]
  - expect: The kettle's handle, its base and the counter stay the same.
  - fail: The handle changes shape; or the base changes colour; or items on the counter rearrange.

**Note.** The click is sound; it is read from the switch moving. How quickly the boil dies down is not judged.

## HEAT-0081 · boil_steam · train

**Caption.** A garment steamer is run slowly down a wrinkled shirt hanging on a rail, and the creases relax and drop out where the steam passes.

**Expectation (hidden).** Steam rises from the steamer head, the fabric darkens slightly with moisture and smooths only along the path the head has taken; creases do not come back once steamed and untreated areas stay wrinkled.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] A wrinkled shirt hangs on a rail.
- S2 [core] A steamer head is moved down the shirt.
- S3 [core] Steam rises from the steamer head.
- S4 [core] The creases drop out where the head has passed.
- S5 [minor] The fabric darkens where it is damp.
- S6 [minor] The steaming comes first and the smoothing follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The fabric smooths only along the path the head has taken, and wrinkles away from that path stay.
  - fail: The whole shirt smooths at once while the head is at one spot; or creases drop out on a part of the shirt the head never reached; or the head passes over a crease and the fabric behind it is unchanged; or the shirt smooths before any steam appears.
- P2 [core · process_direction]
  - expect: Creases only drop out and smoothed fabric stays smooth.
  - fail: A crease comes back on fabric the head has just passed over; or the fabric wrinkles more where the head has been; or the fabric dries and creases again while the steamer works on it; or the shirt smooths and wrinkles in turn.
- P3 [major · gravity_direction]
  - expect: The steam rises from the head and the shirt hangs downward from the rail, its hem swinging and settling.
  - fail: The steam pours downward through the shirt; or sinks and pools on the floor; or the shirt's hem rises and stays up with nothing lifting it; or the shirt lifts off the rail.
- P4 [major · material_response]
  - expect: The shirt is cloth that hangs, sways and relaxes as it dampens, and the steamer head is a rigid tool.
  - fail: The shirt stays board-stiff and keeps its shape as the head passes; or the fabric stretches like elastic under the head; or the head bends or droops; or the shirt sticks to the head and lifts with it.
- P5 [fatal · permanence_count]
  - expect: One shirt on one rail and one steamer head; the shirt stays on its hanger and nothing passes through it.
  - fail: The head passes through the shirt; or a second shirt appears; or the shirt vanishes; or the shirt's collar or sleeve detaches.
- P6 [minor · attribute_drift]
  - expect: The shirt's colour and pattern, the rail and the room stay the same.
  - fail: The shirt changes colour or pattern; or the rail changes shape; or items in the room rearrange.

## HEAT-0082 · boil_steam · train

**Caption.** A basket of laundry fresh from a hot dryer is set outside on a freezing morning, and vapour rises off the warm clothes.

**Expectation (hidden).** The vapour rises from the clothes and thins as it drifts; it is thickest at first and fades as the clothes cool; it does not sink or gather on the ground.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] A basket of laundry stands outside.
- S2 [core] Vapour rises off the clothes.
- S3 [core] The setting reads as freezing: frost, snow or bare winter ground.
- S4 [minor] The vapour is thickest at first.
- S5 [minor] The vapour thins as it drifts.

**PC**
- P1 [core · gravity_direction]
  - expect: The vapour leaves the clothes going up, spreading and thinning as it rises.
  - fail: The vapour sinks over the basket's rim and pools on the ground; or flows away across the ground like water; or hangs as a fixed shape without rising; or pours downward through the basket.
- P2 [core · process_direction]
  - expect: The vapour only eases as the clothes cool; it does not build up again with nothing added.
  - fail: The vapour thickens steadily the longer the basket stands; or the vapour stops and then starts again with nothing touching the clothes; or the plume runs back into the clothes; or a puff retreats to the laundry.
- P3 [major · missing_consequence]
  - expect: The vapour comes off the clothes themselves and is thickest just above them.
  - fail: The vapour rises from the ground beside the basket while the clothes are clear; or the vapour is thickest high above the basket with nothing carrying it there; or the vapour rises from the empty part of the basket.
- P4 [major · material_response]
  - expect: The vapour is a soft cloud that spreads and fades and the clothes are limp folded cloth in the basket.
  - fail: The vapour holds a fixed rigid shape; or pours like a liquid over the rim; or the clothes stand stiff like boards; or the vapour lifts a garment out of the basket.
- P5 [fatal · permanence_count]
  - expect: One basket of laundry; the garments keep their number and stay in the basket.
  - fail: A garment vanishes; or new garments appear; or a garment passes through the basket's wall; or the basket changes shape.
- P6 [minor · attribute_drift]
  - expect: The clothes' colours, the basket and the surroundings stay the same.
  - fail: A garment changes colour; or the basket changes colour; or the frost or snow around changes between frames.

## HEAT-0083 · boil_steam · train

**Caption.** A spoonful of salt is tipped into a pot of boiling water, and the water froths up sharply for a moment before settling back to a rolling boil.

**Expectation (hidden).** The surge of foam comes at the moment the salt goes in and climbs the sides, then dies back within seconds; the water does not froth before the salt goes in or stay frothed.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A pot of boiling water sits on a hob.
- S2 [core] A spoonful of salt is tipped in.
- S3 [core] The water froths up sharply.
- S4 [core] The froth dies back to a rolling boil.
- S5 [minor] The froth climbs the pot's sides at its peak.
- S6 [minor] The order is boiling, salt in, surge, settle.

**PC**
- P1 [core · missing_consequence]
  - expect: The surge comes at the moment the salt goes in and rises from where it lands.
  - fail: The water froths up before the salt reaches it; or the salt goes in and the surface does not change at all; or the surge rises on the far side of the pot from where the salt landed; or the surge appears with the spoon still held clear of the pot.
- P2 [core · process_direction]
  - expect: The surge rises and then dies back to the boil it came from, and it does not surge again with no more salt.
  - fail: The froth stays up for the rest of the clip; or the froth surges again with nothing added; or the froth dies back to a still glassy surface; or the surge builds steadily higher after the salt is in.
- P3 [major · gravity_direction]
  - expect: The froth climbs the pot's inside wall and falls back into the water, and anything that goes over the rim runs down the outside.
  - fail: The froth climbs the pot's outside and goes in over the rim; or froth lifts off the pot and hangs above it; or froth runs upward on the outside; or the froth stands above the rim without falling back or spilling.
- P4 [major · material_response]
  - expect: The froth is a mass of fine bubbles that swells and collapses, and the salt falls as loose grains that sink and disappear into the water.
  - fail: The froth stands as a rigid dome; or the salt grains float on top and stay; or the salt clumps into a solid lump that sits on the surface; or the water sets solid.
- P5 [fatal · permanence_count]
  - expect: One pot of water; the salt goes in and the water stays in the pot.
  - fail: The water's level jumps up with nothing added; or water passes through the pot's wall; or a second pot appears; or the salt appears in the pot before the spoon tips.
- P6 [minor · attribute_drift]
  - expect: The pot, the spoon and the hob stay the same.
  - fail: The pot changes colour; or the spoon changes shape; or the hob's knobs move by themselves.

## HEAT-0084 · boil_steam · train

**Caption.** A baked potato fresh from the oven is split open with a fork, and steam rises from the white flesh inside.

**Expectation (hidden).** The steam appears the moment the potato is opened, rises from the cut faces and thins; it does not come from the unbroken skin or sink onto the plate.

**Declared violation types.** missing_consequence, gravity_direction

**SA**
- S1 [core] A baked potato.
- S2 [core] The potato is split open with a fork.
- S3 [core] Steam rises from the flesh inside.
- S4 [minor] The flesh inside is white and fluffy.
- S5 [minor] The split comes first and the steam follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The steam appears from the cut faces at the moment the potato opens and not from the unbroken skin.
  - fail: Steam rises from the whole potato before it is opened; or the potato is opened and no steam appears from the cut to the end of the clip; or steam pours from the unbroken skin while the cut faces are clear; or steam appears above the potato with nothing leaving the cut.
- P2 [core · gravity_direction]
  - expect: The steam rises from the cut faces, spreading and thinning as it climbs.
  - fail: The steam sinks onto the plate and pools; or pours downward out of the cut; or hangs as a fixed shape without rising; or flows sideways with nothing blowing it.
- P3 [major · material_response]
  - expect: The skin is a tough shell that tears along the fork's line and the flesh inside is soft and crumbly, while the fork stays rigid.
  - fail: The skin stretches like rubber as the fork goes in; or the flesh runs out as a liquid; or the potato splits as a brittle shell into sharp shards; or the fork bends.
- P4 [major · process_direction]
  - expect: The split only opens wider and the steam only leaves; the potato does not close up again.
  - fail: The split closes and the potato is whole again; or the cut faces knit back together; or the steam runs back into the potato; or the flesh draws back inside the skin.
- P5 [fatal · permanence_count]
  - expect: One potato and one fork; the potato stays one potato in two halves and nothing passes through the plate.
  - fail: A second potato appears; or the potato vanishes; or the fork passes through the plate; or the halves merge into a whole potato with no seam.
- P6 [minor · attribute_drift]
  - expect: The plate, the potato's skin away from the cut and the table stay the same.
  - fail: The plate changes pattern; or the skin changes colour away from the cut; or items on the table rearrange.

## HEAT-0085 · condensation · train

**Caption.** A cold bottle of soda has just been taken out of the fridge on a hot day, and beads of water form on the outside of the bottle.

**Expectation (hidden).** A haze appears first, then droplets grow and some run downward, leaving trails; the beads do not appear on the inside of the bottle or vanish while it stays cold.

**Declared violation types.** process_direction, permanence_count, gravity_direction

**SA**
- S1 [core] A bottle of soda is present.
- S2 [core] Beads of water form on the outside of the bottle.
- S3 [core] The bottle reads as cold and just out of the fridge: an open fridge, chill haze or frost on the glass.
- S4 [minor] The setting is a hot day: sun, outdoors or a warm room.
- S5 [minor] The bottle is a soda bottle with a label and cap.

**PC**
- P1 [core · process_direction]
  - expect: The condensation builds: a haze, then droplets that grow and multiply; the bottle's surface gets wetter, never drier, while it is out.
  - fail: The droplets shrink or vanish while the bottle sits; or the surface fogs and clears repeatedly; or the beading reduces over the clip.
- P2 [major · gravity_direction]
  - expect: Droplets that grow large enough run downward, leaving trails; water gathers at the bottom of the bottle or on the surface beneath.
  - fail: A drop runs upward or sideways along the bottle; or water collects on top of the cap; or a drop leaves the bottle and floats.
- P3 [major · permanence_count]
  - expect: The water appears only on the outside of the cold bottle, as beads on the surface.
  - fail: Beads form on the inside of the bottle or on the table away from the bottle; or drops detach and drift off into the air.
- P4 [major · material_response]
  - expect: The beads behave as water on glass or plastic: they stay round, merge when they touch, and run as streaks.
  - fail: Touching drops overlap without merging; or drops jump about on the surface; or the beads turn to hard frost while the bottle sweats.
- P5 [fatal · shape_identity]
  - expect: One bottle keeps its shape and cap; nothing passes through it.
  - fail: The bottle changes shape; or a second bottle appears or the bottle vanishes; or the cap comes off by itself; or the liquid inside passes through the wall.
- P6 [minor · attribute_drift]
  - expect: The label, cap colour and soda colour stay the same; the background stays put.
  - fail: The label text or colour changes; or the soda changes colour; or background objects shift.

## HEAT-0086 · condensation · train

**Caption.** Breath is blown onto a cold window pane, and a patch of fog appears on the glass and then fades.

**Expectation (hidden).** The fog appears where the breath hits, exactly during the exhale, and clears from the edges inward over a few seconds; it does not appear before the breath.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A window pane is present.
- S2 [core] Breath is blown onto it: a face or mouth near the glass, or visible breath.
- S3 [core] A patch of fog appears on the glass.
- S4 [core] The fog fades again.
- S5 [minor] The fog is a rounded patch localised where the breath lands.
- S6 [minor] Appearing comes first, fading after.

**PC**
- P1 [core · process_direction]
  - expect: The fog appears during the exhale, then thins and shrinks until gone; once clear it stays clear without another breath.
  - fail: The patch grows after the breath has stopped; or comes back without another breath; or flickers on and off; or moves across the glass.
- P2 [major · permanence_count]
  - expect: The fog is a haze on the glass surface: it hides what is behind it only where it lies, and the same view returns as it clears.
  - fail: The fogged patch hides objects that are missing when it clears, or new objects appear behind it; or the fog detaches from the glass and drifts as a cloud.
- P3 [major · missing_consequence]
  - expect: The breath produces the fog: the patch appears in front of the mouth during the exhale.
  - fail: Breath is blown at the glass and it stays clear; or the fog appears far from where the breath lands.
- P4 [major · material_response]
  - expect: The fog is fine condensation: a matte haze that thins evenly.
  - fail: The patch hardens into frost; or peels off as a film; or turns opaque white like paint.
- P5 [fatal · shape_identity]
  - expect: The window, its frame and whoever breathes keep their shape and number; nothing passes through the glass.
  - fail: The face or a hand passes through the glass; or the pane changes size; or a second pane appears; or the face deforms.
- P6 [minor · attribute_drift]
  - expect: The frame, the view outside and the glass's colour stay the same throughout.
  - fail: The frame changes colour; or the view outside jumps; or the glass tints.

**Note.** The breath is kept because it is the moisture source. The person is judged only as the origin of the breath; face and expression are not judged.

## HEAT-0087 · condensation · train

**Caption.** A pair of glasses is brought in from the cold street into a warm café, and the lenses fog over.

**Expectation (hidden).** The fog appears on the lenses within a moment of entering and does not appear while they are still outside; any later change is toward clearing.

**Declared violation types.** process_direction, attribute_drift

**SA**
- S1 [core] A pair of glasses.
- S2 [core] The glasses are brought in from outside into a warm room.
- S3 [core] The lenses fog over.
- S4 [minor] The lenses are clear while still outside.
- S5 [minor] The fogging comes after the glasses are inside.

**PC**
- P1 [core · process_direction]
  - expect: The fog appears once the glasses are inside and then holds or clears; it does not appear while they are still out in the cold.
  - fail: The lenses are fogged while still outside in the cold; or the fog appears, clears and appears again with the glasses held still indoors; or the fog thickens after the lenses have cleared; or the fog appears before the glasses have moved.
- P2 [core · attribute_drift]
  - expect: The change is a haze on the lenses themselves: what lies behind them blurs where the haze is and comes back as it clears.
  - fail: The frames change colour rather than the lenses; or the haze lies on the frame and not on the glass; or the view behind the lenses changes to a different scene as the fog clears; or the lenses turn a colour instead of hazing.
- P3 [major · gravity_direction]
  - expect: Droplets that gather run downward on the lens and any drip falls away.
  - fail: A droplet runs up the lens; or a drip leaves the lens and rises; or water gathers along the lens's top edge and stays.
- P4 [major · permanence_count]
  - expect: The fog lies on the glass surface and nothing else appears or vanishes behind it.
  - fail: Objects seen through the fogged lens are missing when it clears; or new objects appear behind the fog; or the fog detaches from the lens and drifts as a cloud; or the lens vanishes behind the fog.
- P5 [fatal · shape_identity]
  - expect: One pair of glasses with two lenses in one frame; the frame keeps its shape and nothing passes through the lenses.
  - fail: A lens vanishes; or a third lens appears; or a hand passes through a lens; or the frame bends into another shape.
- P6 [minor · attribute_drift]
  - expect: The frames, the room behind and the clothing stay the same.
  - fail: The frames change colour; or the room's furniture rearranges; or the clothing changes.

**Note.** The glasses may be on a face or in a hand; the person is not judged.

## HEAT-0088 · condensation · train

**Caption.** A glass of ice water sits on a wooden table in a warm room, and condensation runs down the outside of the glass onto the table.

**Expectation (hidden).** Droplets on the outside run down and feed the ring; the ring does not shrink while the glass stays cold; the water does not come from inside the glass.

**Declared violation types.** process_direction, gravity_direction, permanence_count

**SA**
- S1 [core] A glass of ice water stands on a wooden table.
- S2 [core] Droplets cover the outside of the glass.
- S3 [core] Water runs down the glass.
- S4 [core] A wet ring forms on the table.
- S5 [minor] Ice is visible in the glass.
- S6 [minor] The droplets grow before they run.

**PC**
- P1 [core · process_direction]
  - expect: The beading only builds while the glass stays cold: droplets grow, join and run, and the ring on the table only grows.
  - fail: The droplets shrink or go while the glass stays cold with ice in it; or the ring on the table shrinks; or the glass beads and dries in turn; or the beading eases while the ice is still there.
- P2 [core · gravity_direction]
  - expect: Droplets that grow large enough run downward on the glass, leaving trails, and gather at its foot.
  - fail: A droplet runs up the glass; or water gathers on the rim's top and stays; or a drop leaves the glass and rises; or a run travels sideways round the glass and stays level.
- P3 [core · permanence_count]
  - expect: The water on the outside comes out of the air onto the cold glass, and the ring is fed by runs off the glass.
  - fail: The glass's own level drops as the ring grows; or beads form on the inside of the glass; or the ring appears on the table with no water running down to it; or drops detach and drift off into the air.
- P4 [major · material_response]
  - expect: The beads behave as water on glass: they stay rounded, merge when they touch and run as streaks, and the wood darkens where it is wet.
  - fail: Touching drops overlap without merging; or drops jump about on the glass; or the beads turn to hard frost while the glass runs with water; or the table stays dry-looking under a spreading ring.
- P5 [fatal · shape_identity]
  - expect: One glass on one table; the glass keeps its shape and nothing passes through it.
  - fail: The glass changes shape; or a second glass appears; or the ice passes through the glass's wall; or the glass sinks into the table.
- P6 [minor · attribute_drift]
  - expect: The table's grain away from the ring, the room and the glass's pattern stay the same.
  - fail: The table's grain changes pattern; or the room's contents rearrange; or the glass changes pattern.

## HEAT-0089 · condensation · train

**Caption.** A hot shower runs with the bathroom door closed, and the bathroom window is misting over from the bottom up.

**Expectation (hidden).** The mist thickens while the shower runs and heavier drops run downward in streaks; the glass does not clear while the shower runs.

**Declared violation types.** process_direction, gravity_direction

**SA**
- S1 [core] A shower runs in a bathroom with the door closed.
- S2 [core] The window mists over.
- S3 [core] The mist thickens from the bottom upward.
- S4 [minor] Steam shows in the room.
- S5 [minor] The window is clear at the start.

**PC**
- P1 [core · process_direction]
  - expect: The mist only thickens while the shower runs and misted glass does not clear.
  - fail: The glass clears while the shower still runs; or the mist thins and thickens in turn; or the window is fully misted before the shower starts; or the mist retreats down the glass while steam still fills the room.
- P2 [core · gravity_direction]
  - expect: Heavier drops that gather in the mist run downward in streaks, and the mist builds up the glass from its lower part.
  - fail: A streak runs up the window; or the mist builds from the top down while steam fills the room from below; or drops gather along the window's top edge and stay; or a drop leaves the glass and rises.
- P3 [major · missing_consequence]
  - expect: The mist lies on the room side of the glass, thickest where the steam reaches, and the room shows the steam.
  - fail: The mist forms on the outside face of the glass; or the window mists while the room shows no steam at all; or the mist is thickest in a corner the steam never reaches; or the mirror and tiles stay bone dry while the window runs with water.
- P4 [major · material_response]
  - expect: The mist is a fine haze that beads and streaks, and the glass stays a rigid clear pane.
  - fail: The mist stands off the glass as a thick crust; or the mist peels away as a film; or the glass flexes; or the haze turns opaque white like paint.
- P5 [fatal · permanence_count]
  - expect: One window in one frame; what is seen through the clear glass is the same before and after the misting.
  - fail: The window changes size; or a second window appears; or objects seen through the glass are missing once it clears; or the frame vanishes.
- P6 [minor · attribute_drift]
  - expect: The frame, the tiles and the fittings stay the same.
  - fail: The frame changes colour; or the tiles change pattern; or the fittings move.

**Note.** Whoever is in the shower is not judged.

## HEAT-0090 · condensation · train

**Caption.** A chest freezer is opened, and a low mist rolls out over the rim and sinks toward the floor.

**Expectation (hidden).** The mist spills over the edge and downward, hugging the freezer's sides and thinning as it falls; it does not rise like steam.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] A chest freezer is opened.
- S2 [core] Mist rolls out over its rim.
- S3 [core] The mist sinks toward the floor.
- S4 [minor] The mist hugs the freezer's sides as it falls.
- S5 [minor] The opening comes first and the mist follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The mist spills over the rim and falls, hugging the freezer's sides and spreading along the floor, thinning as it goes.
  - fail: The mist rises off the freezer like steam and climbs to the ceiling; or hangs above the open lid without falling; or shoots upward in a plume; or sinks and then rises back into the freezer.
- P2 [core · process_direction]
  - expect: The mist keeps spilling while the lid is open and what has left keeps moving away and fading.
  - fail: The mist runs back into the freezer; or a puff retreats over the rim; or the mist rolls out before the lid has moved; or the mist thickens steadily after the lid has been shut.
- P3 [major · missing_consequence]
  - expect: The mist comes out of the cold cabinet at its open mouth and is thickest at the rim.
  - fail: The mist pours from the freezer's closed side; or the mist is thickest far across the floor with nothing carrying it there; or the mist appears above the lid with none crossing the rim.
- P4 [major · material_response]
  - expect: The mist is a soft low cloud that spreads, waves and fades, and the lid is a rigid panel on its hinge.
  - fail: The mist holds a fixed rigid shape; or pools as a liquid with a flat surface; or the lid bends as it opens; or the mist breaks into solid lumps.
- P5 [fatal · permanence_count]
  - expect: One freezer with one lid; the contents keep their number and stay inside.
  - fail: A packet in the freezer vanishes; or new packets appear; or the lid passes through the cabinet's wall; or the freezer changes shape.
- P6 [minor · attribute_drift]
  - expect: The freezer's casing, the floor and the room stay the same.
  - fail: The casing changes colour; or the floor's pattern changes; or items in the room rearrange.

**Note.** Cold mist that sinks is what this caption asks for; it is not steam and it does not rise.

## HEAT-0091 · condensation · train

**Caption.** The lid of a pot that has been simmering is lifted and turned over, and its underside is covered in drops that run and drip off.

**Expectation (hidden).** Drops cover the inner face of the lid and fall from the lowest edge as it tilts; the drops do not stay put on a tilted lid.

**Declared violation types.** gravity_direction, permanence_count

**SA**
- S1 [core] A lid is lifted off a pot.
- S2 [core] The lid is turned over.
- S3 [core] Its underside is covered in drops.
- S4 [core] Drops run and drip off the lid.
- S5 [minor] The pot below is simmering or steaming.
- S6 [minor] The order is lift, turn, drip.

**PC**
- P1 [core · gravity_direction]
  - expect: The drops run to the lid's lowest point as it tilts and fall from there straight down.
  - fail: Drops stay fixed in place on a steeply tilted lid; or run up toward the lid's raised side; or a drop leaves the lid and rises; or drops run along the lid's rim and stay level as it tilts.
- P2 [core · permanence_count]
  - expect: The drops are on the lid's inner face and come from the pot's steam; they leave only by running off or falling.
  - fail: Drops appear on the lid's outer face while its inner face is dry; or a drop vanishes in mid-air; or new drops appear on a part of the lid the steam never reached; or the lid's inner face is dry when it comes off a steaming pot.
- P3 [major · process_direction]
  - expect: Once the lid is off, the drops only gather, run and fall; the film on it does not grow back.
  - fail: The lid's inner face beads up again while it is held clear of the pot's steam; or drops that have fallen come back onto the lid; or the drops grow and shrink in turn; or the lid dries and beads again with nothing touching it.
- P4 [major · material_response]
  - expect: The drops behave as water on metal or glass: rounded, merging when they touch and running as streaks.
  - fail: Touching drops overlap without merging; or drops jump about on the lid; or the drops set as hard frost on the warm lid; or the drops stand as tall columns on the lid.
- P5 [fatal · shape_identity]
  - expect: One lid with one handle; the lid keeps its shape and nothing passes through it.
  - fail: The lid changes shape; or a second lid appears; or the handle detaches and floats; or a hand passes through the lid.
- P6 [minor · attribute_drift]
  - expect: The lid's finish, the pot and the hob stay the same.
  - fail: The lid changes colour; or the pot changes shape; or the hob's knobs move by themselves.

## HEAT-0092 · condensation · train

**Caption.** A man exhales on a frosty morning, and his breath appears as a white cloud that drifts away and fades.

**Expectation (hidden).** The cloud appears just in front of his mouth on each exhale, spreads, and disappears within a second or two; it is not visible when he inhales.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A person stands outdoors on a cold morning.
- S2 [core] A white cloud of breath appears in front of the mouth.
- S3 [core] The cloud drifts away.
- S4 [core] The cloud fades.
- S5 [minor] The setting reads as frosty: frost, bare trees or winter clothing.
- S6 [minor] The cloud appears with the exhale, not between breaths.

**PC**
- P1 [core · process_direction]
  - expect: Each cloud appears at the exhale, spreads and fades and does not come back, and nothing shows between breaths.
  - fail: A cloud appears while the chest is drawing in and no breath is going out; or a faded cloud thickens again with no new breath; or a cloud hangs unchanged for the rest of the clip; or the cloud runs back into the mouth.
- P2 [core · permanence_count]
  - expect: The cloud starts just in front of the mouth and goes by thinning away.
  - fail: A cloud appears in the air away from the face with nothing coming from the mouth; or the cloud vanishes in a single frame while still thick; or two clouds appear from one exhale in different places; or the cloud splits into solid pieces.
- P3 [major · gravity_direction]
  - expect: The cloud drifts and spreads as it thins; it does not fall as a liquid.
  - fail: The cloud sinks to the ground and pools; or falls in a stream from the mouth; or hangs as a fixed shape without drifting; or pours downward over the chest.
- P4 [major · material_response]
  - expect: The cloud is a soft haze that spreads, waves and fades; it holds no edges and does not turn solid.
  - fail: The cloud holds a fixed rigid shape; or turns into solid lumps; or pours like a liquid; or keeps a sharp outline as it drifts.
- P5 [fatal · shape_identity]
  - expect: One person with the same face and clothing; the cloud stays outside the body.
  - fail: The face changes shape; or a second head appears; or the cloud passes into the chest and out the back; or the clothing turns into another garment.
- P6 [minor · attribute_drift]
  - expect: The clothing, the background and the light stay the same.
  - fail: The clothing changes colour; or the background changes between frames; or the scene changes from frosty to green.

**Note.** The person is kept because the breath is the caption's subject; the face and expression are not judged.

## HEAT-0093 · condensation · train

**Caption.** A tub of ice cream is taken from the freezer, and a white frost forms on its lid as it sits on the counter.

**Expectation (hidden).** The frost appears as a growing white haze on the cold surfaces, then turns to water droplets as the tub warms; it does not appear on the warm counter.

**Declared violation types.** process_direction, attribute_drift

**SA**
- S1 [core] A tub of ice cream is taken from a freezer.
- S2 [core] The tub sits on a counter.
- S3 [core] A white frost forms on its lid.
- S4 [minor] The frost grows as a haze on the cold surfaces.
- S5 [minor] The counter around the tub stays clear of frost.

**PC**
- P1 [core · process_direction]
  - expect: The frost builds first on the cold surfaces and any later change is toward wetness as the tub warms; it does not come and go.
  - fail: The frost thickens, goes and thickens again; or the frost turns back to bare dry plastic and then frosts again; or wet drops on the lid turn back into dry white frost while the tub sits in the warm room; or the frost thins and thickens in turn.
- P2 [core · attribute_drift]
  - expect: The white appears on the tub's own cold surfaces and spreads across them, not on the warm counter or wall.
  - fail: The frost appears on the counter around the tub while the lid stays bare; or the tub's label changes colour rather than frosting over; or the frost appears on the warm wall behind; or the frost covers the whole scene.
- P3 [major · gravity_direction]
  - expect: Once the frost turns to drops they run downward on the tub's sides and gather at its base.
  - fail: A drop runs up the tub's side; or water gathers on top of the lid and stays as a dome; or a drop leaves the tub and rises; or a run travels sideways round the tub and stays level.
- P4 [major · material_response]
  - expect: The frost is a fine white bloom on the surface that softens into beads as the tub warms, and the tub stays a rigid tub.
  - fail: The frost stands off as thick spikes of ice; or the frost peels away as a sheet; or the tub's wall flexes as the frost grows; or the frost turns to a hard glaze that stays dry as the tub warms.
- P5 [fatal · permanence_count]
  - expect: One tub with one lid on one counter; the tub keeps its shape and nothing passes through it.
  - fail: The tub changes shape; or a second tub appears; or the lid passes into the tub; or the tub vanishes.
- P6 [minor · attribute_drift]
  - expect: The tub's label, the counter and the kitchen stay the same.
  - fail: The label's printing changes; or the counter changes pattern; or items in the kitchen rearrange.

## HEAT-0094 · condensation · train

**Caption.** A frosted beer mug is filled from a tap on a warm terrace, and the outside of the mug beads with water.

**Expectation (hidden).** The frost turns to droplets that run down the glass and wet the table; the beads grow while the mug is cold.

**Declared violation types.** process_direction, gravity_direction

**SA**
- S1 [core] A frosted beer mug.
- S2 [core] The mug is filled from a tap.
- S3 [core] The outside of the mug beads with water.
- S4 [minor] The frost on the glass turns to droplets.
- S5 [minor] The setting is a warm terrace.
- S6 [minor] The filling comes first and the beading follows.

**PC**
- P1 [core · process_direction]
  - expect: The beading only builds while the mug stays cold: the frost turns to droplets that grow and join.
  - fail: The droplets shrink or go while the mug stays cold and full; or the glass beads and dries in turn; or the droplets turn back into dry white frost in the warm air; or the beading eases while the glass is still frosted.
- P2 [core · gravity_direction]
  - expect: Droplets that grow large enough run downward on the outside of the mug and wet the table beneath.
  - fail: A droplet runs up the mug; or water gathers on the rim's top and stays; or a drop leaves the mug and rises; or a run travels sideways round the mug and stays level.
- P3 [major · missing_consequence]
  - expect: The water forms on the outside of the cold glass, up to the level of the cold drink, and the table wets where runs reach it.
  - fail: Beads form on the inside of the mug above the drink; or the beading is heaviest above the drink's level and absent below it; or the table stays dry under a mug streaming with runs; or drops appear on the table with none running down to it.
- P4 [major · material_response]
  - expect: The beads behave as water on glass: rounded, merging when they touch and running as streaks, with the frost softening into them.
  - fail: Touching drops overlap without merging; or drops jump about on the glass; or the frost stays hard and dry while runs stream over it; or the beads stand as tall columns on the glass.
- P5 [fatal · shape_identity]
  - expect: One mug; it keeps its shape and handle and nothing passes through it.
  - fail: The mug changes shape; or a second mug appears; or the handle detaches; or the drink passes through the glass's wall.
- P6 [minor · attribute_drift]
  - expect: The terrace's table, the tap and the drink's colour stay the same.
  - fail: The table changes pattern; or the tap changes shape; or the drink changes colour.

## HEAT-0095 · condensation · train

**Caption.** Steam from a kettle rises against a kitchen cabinet door, and the door beads with water that runs down.

**Expectation (hidden).** Water forms on the door where the steam hits and runs downward in drips; the water does not form on the hot kettle.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] A kettle gives off steam.
- S2 [core] The steam rises against a cabinet door.
- S3 [core] The door beads with water.
- S4 [core] The water runs down the door.
- S5 [minor] The beads form where the steam meets the door.
- S6 [minor] The steaming comes first and the beading follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The steam rises to the door and the water on it runs downward in drips toward the counter.
  - fail: A run travels up the door; or the steam sinks from the kettle to the counter; or water gathers along the door's top edge and stays; or a drip leaves the door and rises.
- P2 [core · process_direction]
  - expect: The beading only builds while the steam keeps arriving, and runs only advance downward.
  - fail: The door dries while steam still plays on it; or the beads grow and shrink in turn; or the door is wet before any steam reaches it; or a run retreats up the door.
- P3 [major · missing_consequence]
  - expect: The water forms on the door where the steam reaches it and not on the hot kettle itself.
  - fail: Beads form on the kettle's hot body while the door stays dry; or the door beads in a place the steam never reaches; or the steam plays on the door and it stays dry to the end of the clip; or the door beads evenly all over while the plume hits one spot.
- P4 [major · material_response]
  - expect: The beads behave as water on a painted surface: rounded, merging when they touch and running as streaks, and the door stays a rigid panel.
  - fail: Touching drops overlap without merging; or drops jump about on the door; or the door's paint bubbles and peels as the water runs; or the beads turn to frost on the warm door.
- P5 [fatal · shape_identity]
  - expect: The door keeps its flat panel shape on its hinges and the kettle keeps its shape; nothing passes through either.
  - fail: The door bends or bows; or a second door appears; or water passes through the door into the cabinet; or the kettle changes shape.
- P6 [minor · attribute_drift]
  - expect: The door's colour and handle, the kettle and the counter stay the same.
  - fail: The door changes colour; or the handle changes shape; or items on the counter rearrange.

## HEAT-0096 · condensation · train

**Caption.** A lid is snapped onto a container of hot food, and the inside of the clear lid fogs over.

**Expectation (hidden).** The fog forms on the inner surface of the lid within moments and thickens into drops; the outside stays clear.

**Declared violation types.** process_direction, attribute_drift

**SA**
- S1 [core] A container of hot food.
- S2 [core] A clear lid is snapped onto the container.
- S3 [core] The inside of the lid fogs over.
- S4 [minor] Drops gather on the fogged surface.
- S5 [minor] The outside of the lid stays clear.
- S6 [minor] The lid goes on first and the fogging follows.

**PC**
- P1 [core · process_direction]
  - expect: The fog only thickens on the inner face while the food is hot and the lid is on; it does not clear on its own.
  - fail: The fog clears while the lid stays on the hot food; or the fog thins and thickens in turn; or the lid is fogged before it is put on; or the fog moves to the outer face as it thickens.
- P2 [core · attribute_drift]
  - expect: The change is a haze on the lid's inner surface, and the outer surface stays clear.
  - fail: The outer face fogs while the inner face stays clear; or both faces fog equally; or the lid's plastic turns milky right through rather than hazing on one face; or the container's wall changes colour rather than the lid.
- P3 [major · gravity_direction]
  - expect: Drops that gather on the underside of the lid hang there and run to its lowest point, and fall back into the food if the lid is tilted.
  - fail: Drops run upward on the lid's underside; or drops fall upward off the lid; or drops stay fixed on a steeply tilted lid; or drops rise from the food to the lid as visible streams.
- P4 [major · missing_consequence]
  - expect: The fog is heaviest over the hot food and thinner over the lid's cooler rim.
  - fail: The lid fogs in a place with no food beneath; or the fog is heaviest at the rim and absent over the food; or the fog appears on the lid before it is lowered onto the container.
- P5 [fatal · permanence_count]
  - expect: One container and one lid; the lid stays on and nothing passes through it.
  - fail: The lid passes into the container's wall; or a second lid appears; or food passes through the lid; or the container changes shape.
- P6 [minor · attribute_drift]
  - expect: The container's colour, the food's look and the counter stay the same.
  - fail: The container changes colour; or the food changes into something else; or items on the counter rearrange.

## HEAT-0097 · condensation · train

**Caption.** A camera is carried from an air-conditioned lobby out into humid summer heat, and its lens fogs up.

**Expectation (hidden).** The fog appears on the cold lens shortly after stepping outside and clears as the camera warms; it does not appear while still indoors.

**Declared violation types.** process_direction, attribute_drift

**SA**
- S1 [core] A camera is carried from indoors out into the open air.
- S2 [core] The camera's lens fogs up.
- S3 [minor] The lens is clear while still indoors.
- S4 [minor] The air outside reads as hot and humid.
- S5 [minor] The fogging comes after stepping outside.

**PC**
- P1 [core · process_direction]
  - expect: The fog appears once the camera is outside and then clears as it warms; it does not appear while the camera is still indoors.
  - fail: The lens is fogged while still inside; or the fog appears, clears and appears again with the camera held still outside; or the fog thickens after the lens has cleared; or the fog appears before the camera has moved.
- P2 [core · attribute_drift]
  - expect: The change is a haze on the lens glass: the view through it blurs where the haze lies and comes back as it clears.
  - fail: The camera's body changes colour rather than the lens; or the haze lies on the lens barrel and not on the glass; or the view through the lens changes to a different scene as the fog clears; or the lens turns a colour instead of hazing.
- P3 [major · gravity_direction]
  - expect: Any drops that gather on the lens run downward on the glass.
  - fail: A drop runs up the lens; or a drop leaves the lens and rises; or water gathers along the lens's top edge and stays.
- P4 [major · permanence_count]
  - expect: The fog lies on the glass and nothing else appears or vanishes behind it.
  - fail: Objects seen through the fogged lens are missing when it clears; or new objects appear behind the fog; or the fog detaches from the lens and drifts as a cloud; or the lens vanishes behind the fog.
- P5 [fatal · shape_identity]
  - expect: One camera with one lens; the camera keeps its shape and nothing passes through the glass.
  - fail: The lens vanishes; or a second lens appears on the body; or a hand passes through the lens; or the camera changes shape.
- P6 [minor · attribute_drift]
  - expect: The camera's body, its markings and the surroundings stay the same.
  - fail: The body changes colour; or the markings change; or the surroundings change between frames.

## HEAT-0098 · condensation · train

**Caption.** A motorcyclist stops at a light on a cold day, and the inside of the helmet visor fogs with each breath.

**Expectation (hidden).** The fog thickens with each exhale and thins between breaths; when the visor is lifted it clears.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A motorcyclist in a helmet has stopped at a light.
- S2 [core] The inside of the visor fogs.
- S3 [core] The fog thickens with each breath.
- S4 [core] The fog thins between breaths.
- S5 [minor] The setting reads as cold.
- S6 [minor] The fog is on the visor's inner face.

**PC**
- P1 [core · process_direction]
  - expect: Each breath thickens the fog and it thins between breaths; if the visor is lifted it clears.
  - fail: The fog thickens while the rider is drawing breath in; or the fog thickens steadily with no breathing at all; or the fog clears while breath still reaches it with the visor down; or the fog stays unchanged through every breath.
- P2 [core · permanence_count]
  - expect: The fog lies on the visor's inner face and what is behind it is unchanged when it thins.
  - fail: The fog forms on the visor's outer face; or objects seen through the fogged visor are missing when it thins; or the fog detaches from the visor and drifts as a cloud; or the fog appears on the helmet's shell rather than the visor.
- P3 [major · gravity_direction]
  - expect: Drops that gather on the visor run downward on its inner face.
  - fail: A drop runs up the visor; or a drop leaves the visor and rises; or water gathers along the visor's top edge and stays.
- P4 [major · material_response]
  - expect: The fog is a fine haze that beads and streaks, and the visor stays a rigid clear shield on its pivot.
  - fail: The fog stands off the visor as a thick crust; or the fog peels away as a film; or the visor flexes or ripples; or the haze turns opaque white like paint.
- P5 [fatal · shape_identity]
  - expect: One helmet with one visor; the helmet keeps its shape and nothing passes through the visor.
  - fail: The visor vanishes; or a second visor appears; or a hand passes through the visor; or the helmet changes shape.
- P6 [minor · attribute_drift]
  - expect: The helmet's paint, the bike and the street stay the same.
  - fail: The helmet changes colour; or the bike changes colour; or the street's traffic lights change layout.

**Note.** The rider is kept because the breath is the moisture's source; the rider is otherwise not judged.

## HEAT-0099 · condensation · train

**Caption.** Sunlight warms a greenhouse in the morning, and the inside of its glass panes is covered in drops that begin to run down.

**Expectation (hidden).** The drops merge and streak downward on the inner surface; the glass gradually clears from the top as the day warms.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] A greenhouse with glass panes.
- S2 [core] The inside of the panes is covered in drops.
- S3 [core] The drops begin to run down.
- S4 [minor] The drops merge into streaks as they run.
- S5 [minor] The setting is a sunlit morning.

**PC**
- P1 [core · gravity_direction]
  - expect: The drops merge and run downward on the inner face of the glass and gather along the lower rails.
  - fail: A drop runs up a pane; or a streak travels sideways and stays level; or water gathers along a pane's top rail and stays; or a drop leaves the glass and rises.
- P2 [core · process_direction]
  - expect: The drops only merge, run and clear from the glass; the panes do not bead up again while the house warms.
  - fail: A pane that has cleared beads up again with nothing cooling it; or the drops grow and shrink in turn; or the streaks retreat up the glass; or the panes fog harder as the sun rises on them.
- P3 [major · missing_consequence]
  - expect: The water lies on the inside of the panes and the plants and soil below are damp.
  - fail: The drops lie on the outer face while the inner face is dry; or the panes run with water while the soil and plants inside are bone dry and dusty; or the drops appear on the frame and not on the glass.
- P4 [major · material_response]
  - expect: The drops behave as water on glass: rounded, merging when they touch and running as streaks, and the glass stays rigid and clear.
  - fail: Touching drops overlap without merging; or drops jump about on the pane; or the water sets as frost in the warming house; or the glass flexes as the water runs.
- P5 [fatal · permanence_count]
  - expect: The greenhouse keeps its panes and frame and nothing passes through the glass.
  - fail: A pane vanishes; or a new pane appears; or water passes through the glass to the outside; or the frame changes shape.
- P6 [minor · attribute_drift]
  - expect: The frame, the plants and the paths stay the same.
  - fail: The frame changes colour; or the plants change into different plants; or the paths change pattern.

## HEAT-0100 · condensation · train

**Caption.** A car's air conditioning is turned to full blast on a humid day, and faint mist drifts out of the dashboard vents.

**Expectation (hidden).** The mist appears at the vents and disappears within a short distance into the cabin air; it does not pool or pour like liquid.

**Declared violation types.** process_direction, gravity_direction

**SA**
- S1 [core] A car's dashboard vents.
- S2 [core] Faint mist drifts out of the vents.
- S3 [minor] The mist disappears a short way into the cabin.
- S4 [minor] The mist comes from the vents rather than elsewhere.
- S5 [minor] The mist is faint rather than a thick cloud.

**PC**
- P1 [core · process_direction]
  - expect: The mist keeps coming from the vents while the fan runs and fades a short way out; puffs that have left keep moving away.
  - fail: The mist runs back into the vents; or a puff retreats to a vent's grille; or the mist thickens the further it gets from the vents; or mist appears deep in the cabin with none leaving the vents.
- P2 [core · gravity_direction]
  - expect: The mist drifts out along the vents' direction and fades; it does not pour down and pool.
  - fail: The mist pours down the dashboard and pools on the floor like a liquid; or sinks in a stream from the vents onto the seats; or hangs as a fixed shape without drifting; or gathers at the roof as a thick standing layer.
- P3 [major · missing_consequence]
  - expect: The mist comes out of the vents' openings and is thickest at their mouths.
  - fail: The mist comes out of the dashboard's solid face away from the vents; or the mist is thickest far from the vents with nothing carrying it there; or the vents are clear while mist appears in front of them with nothing leaving them.
- P4 [major · material_response]
  - expect: The mist is a soft faint haze that spreads and fades, and the vents and dashboard stay rigid.
  - fail: The mist holds a fixed rigid shape; or pours as a liquid with a flat surface; or the vents' louvres bend as the mist leaves; or the mist turns into solid lumps.
- P5 [fatal · permanence_count]
  - expect: One dashboard with its vents in fixed places; the cabin's contents stay the same.
  - fail: A vent vanishes; or new vents appear; or the dashboard changes shape; or items in the cabin appear or vanish.
- P6 [minor · attribute_drift]
  - expect: The dashboard's colour, its dials and the cabin stay the same.
  - fail: The dashboard changes colour; or the dials change layout; or the seats change colour.

## HEAT-0101 · condensation · train

**Caption.** A cold metal water pipe runs along a basement wall on a humid day, and it sweats droplets that drip onto the floor.

**Expectation (hidden).** Drops form along the underside of the pipe and fall straight down, leaving a wet line on the floor; water does not appear on the warm wall.

**Declared violation types.** gravity_direction, permanence_count

**SA**
- S1 [core] A metal pipe runs along a basement wall.
- S2 [core] Droplets form on the pipe.
- S3 [core] Droplets fall from the pipe onto the floor.
- S4 [core] A wet line builds on the floor below the pipe.
- S5 [minor] The droplets gather on the pipe's underside.
- S6 [minor] The forming comes first and the dripping follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The drops gather on the pipe's underside, hang and fall straight down to the floor below.
  - fail: A drop runs up the pipe; or a drop leaves the pipe and rises; or drops gather on the pipe's top and stay as a dome; or a drop falls sideways and lands far from the pipe with nothing blowing it.
- P2 [core · permanence_count]
  - expect: The water comes out of the air onto the cold pipe and leaves only by falling, and the wet line lies under the pipe.
  - fail: Drops appear on the warm wall away from the pipe; or the wet line lies away from the pipe with no drop falling there; or a drop vanishes in mid-air; or water appears inside the pipe and passes out through its wall.
- P3 [major · process_direction]
  - expect: The beading only builds while the pipe stays cold and the wet line on the floor only grows.
  - fail: The drops shrink or go while the pipe stays cold; or the wet line shrinks; or the pipe beads and dries in turn; or the drops turn to dry frost on the sweating pipe.
- P4 [major · material_response]
  - expect: The drops behave as water on metal: rounded, merging when they touch, and running along the pipe to its lowest point before falling.
  - fail: Touching drops overlap without merging; or drops jump about on the pipe; or the drops stand as tall columns under the pipe; or the pipe's metal sags where it is wet.
- P5 [fatal · shape_identity]
  - expect: One pipe on its brackets; the pipe keeps its shape and stays on the wall.
  - fail: The pipe bends or sags; or a second pipe appears; or the pipe sinks into the wall; or a bracket vanishes and the pipe hangs in the air.
- P6 [minor · attribute_drift]
  - expect: The wall away from the wet line, the brackets and the basement stay the same.
  - fail: The wall changes colour away from the wet patch; or a bracket changes shape; or items in the basement rearrange.

## HEAT-0102 · condensation · train

**Caption.** Steam from a hot shower drifts against the cool tiled wall, and the tiles bead with water that runs in streaks.

**Expectation (hidden).** Drops form on the tiles, join, and run downward; the tiles look wet only where the steam reaches.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] Steam drifts against a tiled wall.
- S2 [core] The tiles bead with water.
- S3 [core] The water runs down in streaks.
- S4 [minor] The tiles look wet where the steam reaches them.
- S5 [minor] The drops join before they run.

**PC**
- P1 [core · gravity_direction]
  - expect: The drops join and run downward over the tiles and gather at the grout lines and the wall's foot.
  - fail: A streak runs up the tiles; or water gathers along the wall's top and stays; or a drop leaves the tiles and rises; or a streak travels sideways and stays level.
- P2 [core · process_direction]
  - expect: The beading only builds while steam keeps arriving, and runs only advance downward.
  - fail: The tiles dry while steam still drifts against them; or the beads grow and shrink in turn; or the tiles are wet before any steam reaches them; or a streak retreats up the wall.
- P3 [major · missing_consequence]
  - expect: The tiles are wet where the steam reaches them and drier where it does not.
  - fail: The wall beads evenly all over while the steam drifts against one part; or the tiles bead in a corner the steam never reaches; or the steam drifts against the tiles and they stay dry to the end of the clip.
- P4 [major · material_response]
  - expect: The drops behave as water on glazed tile: rounded, merging when they touch and running as streaks, and the grout darkens as it wets.
  - fail: Touching drops overlap without merging; or drops jump about on the tile; or the water sets as frost on the warm wall; or the tiles' glaze bubbles as the water runs.
- P5 [fatal · permanence_count]
  - expect: The wall keeps its tiles in their courses and nothing passes through it.
  - fail: A tile vanishes; or a new tile appears; or water passes through the wall; or the wall changes shape.
- P6 [minor · attribute_drift]
  - expect: The tiles' colour and pattern away from the wet area and the fittings stay the same.
  - fail: The tiles change colour; or the pattern changes; or the fittings move.

## HEAT-0103 · condensation · train

**Caption.** A hot dishwasher is opened and the steam that escapes fogs the cool kitchen window above the sink.

**Expectation (hidden).** The fog forms on the window where the rising steam reaches it and clears over time; it does not form on the warm dishwasher.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] A dishwasher is opened.
- S2 [core] Steam escapes from the machine.
- S3 [core] The steam reaches a window above the sink.
- S4 [core] The window fogs.
- S5 [minor] The fog forms where the rising steam meets the glass.
- S6 [minor] The order is opening, steam, fog.

**PC**
- P1 [core · gravity_direction]
  - expect: The steam rises from the open machine toward the window and the fog's drops run downward on the glass.
  - fail: The steam sinks to the floor while the window fogs anyway; or a drop runs up the window; or the steam pours downward out of the machine; or water gathers along the window's top and stays.
- P2 [core · process_direction]
  - expect: The fog builds while the steam keeps reaching the glass and then clears; it does not form before the door opens.
  - fail: The window is fogged before the door has moved; or the fog clears while steam still reaches the glass; or the fog thins and thickens in turn; or the fog thickens after the machine has been shut and the steam has gone.
- P3 [major · missing_consequence]
  - expect: The fog forms on the cool window where the steam reaches it and not on the warm dishwasher.
  - fail: The dishwasher's own door fogs while the window stays clear; or the fog forms in a part of the window the steam never reaches; or the steam reaches the glass and it stays clear and bright to the end of the clip.
- P4 [major · material_response]
  - expect: The steam is a soft cloud that spreads and fades and the fog on the glass is a fine haze that beads.
  - fail: The steam holds a fixed rigid shape; or the fog stands off the glass as a thick crust; or the steam pours like a liquid into the sink; or the haze turns opaque white like paint.
- P5 [fatal · permanence_count]
  - expect: One window in one frame; what is seen through the clear glass is the same before and after.
  - fail: The window changes size; or a second window appears; or objects seen through the glass are missing once it clears; or the frame vanishes.
- P6 [minor · attribute_drift]
  - expect: The window frame, the sink and the units stay the same.
  - fail: The frame changes colour; or the sink's taps change shape; or the units change.

## HEAT-0104 · condensation · train

**Caption.** A cold bottle of milk is poured into a glass on a hot patio, and the outside of the glass mists over.

**Expectation (hidden).** The mist appears on the glass up to the level of the cold milk and beads into drops that run down; above the milk line it stays clearer.

**Declared violation types.** process_direction, gravity_direction

**SA**
- S1 [core] Milk is poured from a bottle into a glass.
- S2 [core] The outside of the glass mists over.
- S3 [core] The mist beads into drops.
- S4 [core] The drops run down.
- S5 [minor] The mist reaches up to the level of the milk in the glass.
- S6 [minor] The setting is a hot patio.

**PC**
- P1 [core · process_direction]
  - expect: The misting only builds while the glass holds the cold milk, and the beads grow and join rather than clearing.
  - fail: The mist clears while the cold milk stays in the glass; or the glass mists and dries in turn; or the glass is misted before the milk is poured; or the beads shrink while the glass is still cold.
- P2 [core · gravity_direction]
  - expect: The drops run downward on the outside of the glass and gather at its foot or wet the table.
  - fail: A drop runs up the glass; or water gathers on the rim's top and stays; or a drop leaves the glass and rises; or a run travels sideways round the glass and stays level.
- P3 [major · missing_consequence]
  - expect: The mist reaches up the glass to the milk's level and the glass above that line stays clearer.
  - fail: The misting is heaviest above the milk's level and absent below it; or the whole glass including the empty part mists equally from the first frame; or mist forms on the inside of the glass; or the glass mists before any milk is in it.
- P4 [major · material_response]
  - expect: The beads behave as water on glass: rounded, merging when they touch and running as streaks, and the milk is a thin liquid that finds its level.
  - fail: Touching drops overlap without merging; or drops jump about on the glass; or the milk stands in a heap above the rim; or the beads turn to frost on the glass in the heat.
- P5 [fatal · permanence_count]
  - expect: One bottle and one glass; the milk goes from bottle to glass and nowhere else.
  - fail: Milk appears in the glass with no stream reaching it; or the glass's level jumps; or the milk passes through the glass's wall; or a second glass appears.
- P6 [minor · attribute_drift]
  - expect: The bottle's label, the glass's shape and the patio table stay the same.
  - fail: The label changes; or the glass changes shape; or the table's setting rearranges.

## HEAT-0105 · condensation · train

**Caption.** A pair of glasses is carried into a steam room, and the lenses cloud over completely within seconds.

**Expectation (hidden).** The lenses go white and opaque almost at once and stay fogged while in the steam.

**Declared violation types.** process_direction, attribute_drift

**SA**
- S1 [core] A pair of glasses is carried into a steam room.
- S2 [core] The lenses cloud over.
- S3 [core] The lenses end fully clouded.
- S4 [minor] The lenses are clear as they go in.
- S5 [minor] The room is full of steam.

**PC**
- P1 [core · process_direction]
  - expect: The clouding only builds while the glasses stay in the steam and the lenses stay fogged there.
  - fail: The lenses clear while still in the steam; or the clouding thins and thickens in turn; or the lenses are clouded before they enter; or the clouding retreats to the lens edges while the steam holds.
- P2 [core · attribute_drift]
  - expect: The change is a haze on the lens glass that hides what lies behind it.
  - fail: The frames change colour rather than the lenses; or the haze lies on the frame and not on the glass; or the lenses turn a colour instead of hazing; or the view behind the lenses changes to a different scene as they cloud.
- P3 [major · gravity_direction]
  - expect: Drops that gather on the lenses run downward and any drip falls away.
  - fail: A drop runs up a lens; or a drop leaves a lens and rises; or water gathers along a lens's top edge and stays.
- P4 [major · material_response]
  - expect: The haze is a fine film on the glass that beads; the lenses stay rigid and the frames keep their shape.
  - fail: The haze stands off the glass as a thick crust; or the haze peels away as a film; or a lens flexes or bulges; or the haze turns to hard frost in the steam.
- P5 [fatal · shape_identity]
  - expect: One pair of glasses with two lenses in one frame; nothing passes through the lenses.
  - fail: A lens vanishes; or a third lens appears; or a hand passes through a lens; or the frame bends into another shape.
- P6 [minor · attribute_drift]
  - expect: The frames, the room's tiles and the benches stay the same.
  - fail: The frames change colour; or the tiles change pattern; or the benches move.

**Note.** The glasses may be on a face or in a hand; the person is not judged.

## HEAT-0106 · condensation · train

**Caption.** A cold pane of glass is held over a steaming kettle, and it fogs and then drips from its lower edge.

**Expectation (hidden).** Fog forms on the underside facing the steam, gathers into drops, and drips from the lowest edge; the top face stays dry.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] A pane of glass is held over a steaming kettle.
- S2 [core] The pane's underside fogs.
- S3 [core] Drops gather on the pane.
- S4 [core] Drops drip from its lower edge.
- S5 [minor] The top face of the pane stays dry.
- S6 [minor] The fogging comes first and the dripping follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The drops on the underside run to the pane's lowest edge and fall from there straight down.
  - fail: Drops run up the pane's underside; or drops fall upward off the pane; or drops stay fixed on a steeply tilted pane; or drops gather along the pane's highest edge and drip from there.
- P2 [core · process_direction]
  - expect: The fogging and the beading only build while the steam keeps reaching the pane, and the drops only gather and fall.
  - fail: The pane's underside dries while steam still reaches it; or the drops shrink and grow in turn; or the pane is wet before any steam reaches it; or a drop that has fallen returns to the pane.
- P3 [major · missing_consequence]
  - expect: The fog and the drops are on the face toward the steam and the top face stays dry.
  - fail: The top face fogs while the underside stays dry; or both faces fog equally; or the pane fogs in a part the steam never reaches; or the steam plays on the pane and it stays clear and dry to the end of the clip.
- P4 [major · material_response]
  - expect: The drops behave as water on glass: rounded, merging when they touch and running as streaks, and the pane stays rigid and clear.
  - fail: Touching drops overlap without merging; or drops jump about on the pane; or the water sets as frost over a steaming kettle; or the pane flexes as the water runs.
- P5 [fatal · permanence_count]
  - expect: One pane and one kettle; the drops come from the steam and leave only by falling.
  - fail: A drop vanishes in mid-air; or drops appear on the top face with none crossing the edge; or the pane passes through the kettle; or a second pane appears.
- P6 [minor · attribute_drift]
  - expect: The kettle, the pane's edges and the surroundings stay the same.
  - fail: The kettle changes colour; or the pane changes size; or items around the kettle rearrange.

**Note.** Whoever holds the pane is not judged.

## HEAT-0107 · condensation · train

**Caption.** Breath is blown onto a cold hand mirror, and the fog on the glass hides the reflection for a moment before it clears.

**Expectation (hidden).** The fog appears with the breath, blurs the reflection, and clears from the edges within seconds; the reflection returns unchanged.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A hand mirror.
- S2 [core] Breath is blown onto the mirror.
- S3 [core] Fog appears on the glass.
- S4 [core] The fog hides the reflection.
- S5 [core] The fog clears.
- S6 [minor] The order is breath, fog, clear.

**PC**
- P1 [core · process_direction]
  - expect: The fog appears during the exhale, then thins and shrinks until gone, and once clear it stays clear without another breath.
  - fail: The patch grows after the breath has stopped; or the fog comes back with no second breath; or the fog flickers on and off; or the patch moves across the glass with nothing blowing it.
- P2 [core · permanence_count]
  - expect: The fog is a haze on the glass: it hides the reflection only where it lies and the same reflection returns as it clears.
  - fail: The reflection that returns shows something the fog did not hide before; or the fog detaches from the glass and drifts as a cloud; or the mirror shows no reflection at all once the fog clears; or the fog appears behind the glass rather than on it.
- P3 [major · missing_consequence]
  - expect: The breath makes the fog: the patch appears on the glass in front of the mouth during the exhale.
  - fail: Breath is blown at the mirror and the glass stays clear; or the fog appears on the mirror's back; or the fog appears far from where the breath lands; or the fog appears before any breath reaches the glass.
- P4 [major · material_response]
  - expect: The fog is fine condensation: a matte haze that thins evenly and may bead.
  - fail: The patch hardens into frost; or the patch peels off as a film; or the haze turns opaque white like paint; or the glass flexes where the fog lies.
- P5 [fatal · shape_identity]
  - expect: One mirror in one frame; the mirror keeps its shape and nothing passes through the glass.
  - fail: The mirror changes shape; or a second mirror appears; or a hand passes through the glass; or the frame vanishes.
- P6 [minor · attribute_drift]
  - expect: The mirror's frame, the hand holding it and the background stay the same.
  - fail: The frame changes colour; or the background changes between frames; or the mirror's handle changes shape.

**Note.** The breath is the moisture's source; the person is judged only as its origin.

## HEAT-0108 · condensation · train

**Caption.** A cold metal railing on a humid summer morning is covered in fine droplets, and a finger drags through them leaving a clear line.

**Expectation (hidden).** The line stays clear where the finger passed while the surrounding droplets remain; the droplets do not vanish from the untouched area.

**Declared violation types.** permanence_count, process_direction

**SA**
- S1 [core] A metal railing is covered in fine droplets.
- S2 [core] A finger drags through the droplets.
- S3 [core] A clear line is left where the finger passed.
- S4 [minor] The droplets around the line stay in place.
- S5 [minor] The drag comes first and the line follows.

**PC**
- P1 [core · permanence_count]
  - expect: The line is clear where the finger wiped and the droplets away from it stay in place.
  - fail: The droplets vanish from the untouched parts of the railing as the line is drawn; or droplets appear on a part of the railing the finger has just wiped; or the whole railing clears at the drag; or droplets appear where the finger has not been.
- P2 [core · process_direction]
  - expect: The cleared line stays clear while the railing stays cold, or beads slowly back in; it does not fill in at a stroke.
  - fail: The line fills back in at once behind the finger; or the line clears and beads and clears again with nothing touching it; or the line widens on its own after the finger has gone; or the droplets march back into the line as a front.
- P3 [major · gravity_direction]
  - expect: The water the finger pushes runs downward or gathers as drops that hang under the rail.
  - fail: The pushed water runs up the railing; or a drop leaves the railing and rises; or the water gathers along the railing's top and stands as a dome; or the pushed water hangs in the air beside the rail.
- P4 [major · material_response]
  - expect: The droplets behave as water on metal: they merge where the finger sweeps them together and then hang or run, and the railing stays rigid.
  - fail: The droplets overlap without merging where the finger sweeps them; or the droplets jump about on the railing; or the railing's metal dents where the finger drags; or the water sets as frost on a summer morning.
- P5 [fatal · shape_identity]
  - expect: One railing; it keeps its shape and the finger passes along its surface, not through it.
  - fail: The finger passes into the railing; or the railing bends; or a second railing appears; or the railing vanishes.
- P6 [minor · attribute_drift]
  - expect: The railing's paint away from the line and the surroundings stay the same.
  - fail: The railing changes colour; or its paint's pattern changes; or the background changes between frames.

## HEAT-0109 · condensation · train

**Caption.** A tray of ice cubes is taken from the freezer, and the cubes and tray frost over white.

**Expectation (hidden).** The white frost appears first on the coldest surfaces; any later change is toward wetness as the tray warms, and the frost does not vanish and return.

**Declared violation types.** process_direction, attribute_drift

**SA**
- S1 [core] A tray of ice cubes is taken from a freezer.
- S2 [core] A white frost forms on the tray and the cubes.
- S3 [minor] The frost appears first on the coldest surfaces.
- S4 [minor] The frost spreads as a haze.
- S5 [minor] The tray is taken out first and the frost follows.

**PC**
- P1 [core · process_direction]
  - expect: The frost builds on the cold surfaces and any later change is toward wetness as the tray warms; it does not come and go.
  - fail: The frost thickens, goes and thickens again; or the frost turns back to bare dry plastic and then frosts again; or wet drops turn back into dry white frost in the warm room; or the frost thins and thickens in turn.
- P2 [core · attribute_drift]
  - expect: The white appears on the tray and the cubes themselves and spreads across them, not on the warm counter around.
  - fail: The frost appears on the counter while the tray stays bare; or the tray's plastic changes colour rather than frosting; or the frost appears on the wall behind; or the frost covers the whole scene.
- P3 [major · gravity_direction]
  - expect: Once the frost turns to drops they run downward on the tray's sides and gather below it.
  - fail: A drop runs up the tray's side; or water gathers on the tray's top edge and stays as a dome; or a drop leaves the tray and rises; or a run travels sideways and stays level.
- P4 [major · material_response]
  - expect: The frost is a fine white bloom on the surface that softens into beads as the tray warms, and the cubes stay hard solids in their wells.
  - fail: The frost stands off as thick spikes of ice; or the frost peels away as a sheet; or the tray's plastic flexes as the frost grows; or a cube slumps while the frost is still growing.
- P5 [fatal · permanence_count]
  - expect: One tray with its cubes; the cubes keep their number and stay in their wells.
  - fail: A cube vanishes; or a new cube appears in an empty well; or a cube passes through the tray's floor; or the tray changes shape.
- P6 [minor · attribute_drift]
  - expect: The tray's colour, the counter and the kitchen stay the same.
  - fail: The tray changes colour; or the counter changes pattern; or items in the kitchen rearrange.

## HEAT-0110 · condensation · train

**Caption.** A dog waits alone in a parked car on a cold evening, and the windows fog up from the inside as it pants.

**Expectation (hidden).** The fog forms on the inside face of the glass, thickest near the dog and toward the top, and grows while the dog pants; it does not form on the outside of the windows or clear while the car stays shut.

**Declared violation types.** process_direction, attribute_drift

**SA**
- S1 [core] A dog sits alone in a parked car.
- S2 [core] The car's windows fog up.
- S3 [core] The fog is on the inside of the glass.
- S4 [core] The fog grows while the dog pants.
- S5 [minor] The fog is thickest near the dog and toward the top of the glass.
- S6 [minor] The setting reads as a cold evening.

**PC**
- P1 [core · process_direction]
  - expect: The fog only thickens while the dog breathes in the shut car and does not clear on its own.
  - fail: The fog clears while the car stays shut and the dog keeps panting; or the fog thins and thickens in turn; or the windows are fogged before the dog has breathed; or the fog retreats to the window edges while the car stays shut.
- P2 [core · attribute_drift]
  - expect: The haze lies on the inner face of the glass, thickest nearest the dog, and the outer face stays clear.
  - fail: The fog forms on the outside of the windows; or both faces fog equally; or the fog is thickest on the window furthest from the dog; or the car's paint changes rather than the glass.
- P3 [major · gravity_direction]
  - expect: Drops that gather in the fog run downward on the inner face of the glass.
  - fail: A drop runs up the glass; or a drop leaves the glass and rises; or water gathers along a window's top edge and stays.
- P4 [major · material_response]
  - expect: The fog is a fine haze that beads and streaks, and the glass stays rigid and clear.
  - fail: The fog stands off the glass as a thick crust; or the fog peels away as a film; or the glass flexes; or the haze turns opaque white like paint.
- P5 [fatal · shape_identity]
  - expect: One dog in one car; the dog keeps its body and the car its windows, and nothing passes through the glass.
  - fail: The dog gains or loses a limb; or a second dog appears; or the dog passes through a window; or a window vanishes.
- P6 [minor · attribute_drift]
  - expect: The dog's coat, the car's interior and the street outside stay the same.
  - fail: The coat changes colour or pattern; or the seats change colour; or the street outside changes between frames.

**Note.** The dog is an animal and its movements are not judged; it is kept because its breath is the moisture's source.

## HEAT-0111 · condensation · train

**Caption.** A car's defroster is switched on against a windshield fogged from the inside, and a clear patch spreads upward from the vents.

**Expectation (hidden).** The glass clears first just above the dashboard vents and the clear area grows upward and outward; the fog does not thicken while the defroster runs and does not clear from the top down.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] A windshield is fogged on the inside.
- S2 [core] The defroster is switched on.
- S3 [core] A clear patch appears just above the dashboard vents.
- S4 [core] The clear patch grows upward and outward.
- S5 [minor] The fog is thick before the switch.
- S6 [minor] The clearing comes after the switch.

**PC**
- P1 [core · process_direction]
  - expect: The clear area only grows outward from the vents and glass that has cleared stays clear while the defroster runs.
  - fail: Fog grows back on glass that had cleared while the defroster runs; or the clear patch shrinks; or the glass clears and fogs in turn; or the fog thickens while the defroster runs.
- P2 [core · missing_consequence]
  - expect: The clearing starts just above the vents and spreads from there, and it starts after the switch.
  - fail: The clearing starts at the windshield's top and works down; or the whole windshield clears at once with no spreading edge; or the glass clears before the defroster is switched on; or the clearing starts in a corner far from any vent.
- P3 [major · gravity_direction]
  - expect: Drops in the fog that grow large enough run downward on the inner face of the glass.
  - fail: A drop runs up the windshield; or a drop leaves the glass and rises; or water gathers along the glass's top edge and stays.
- P4 [major · material_response]
  - expect: The fog is a fine haze that thins evenly at the clearing edge, and the glass stays a rigid clear pane.
  - fail: The fog peels away as a film; or the fog slides down the glass as a sheet; or the haze turns opaque white like paint; or the glass flexes as it clears.
- P5 [fatal · permanence_count]
  - expect: One windshield; what is seen through the cleared glass is the scene outside the car.
  - fail: Objects outside appear or vanish as the glass clears; or a second windshield appears; or the windshield changes shape; or the dashboard vents vanish.
- P6 [minor · attribute_drift]
  - expect: The dashboard, the vents and the view outside stay the same apart from the clearing.
  - fail: The dashboard changes colour; or the vents change layout; or the scene outside jumps to a different place.

## HEAT-0112 · condensation · train

**Caption.** Chunks of dry ice are dropped into a punch bowl of water, and thick white fog boils up, spills over the rim and sinks toward the table.

**Expectation (hidden).** The fog rises out of the bowl, pours over the rim, flows down the outside and spreads along the table, thinning as it goes, while the water bubbles; it does not drift up to the ceiling like steam.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] Chunks of dry ice are dropped into a bowl of water.
- S2 [core] Thick white fog boils up out of the bowl.
- S3 [core] The fog spills over the rim.
- S4 [core] The fog sinks toward the table.
- S5 [minor] The water in the bowl bubbles.
- S6 [minor] The order is drop, fog, spill.

**PC**
- P1 [core · gravity_direction]
  - expect: The fog rises out of the bowl, pours over the rim, falls down the outside and spreads along the table, thinning as it goes.
  - fail: The fog drifts up to the ceiling like steam and does not fall; or hangs above the bowl without spilling; or shoots upward in a plume and stays high; or rises from the table back into the bowl.
- P2 [core · process_direction]
  - expect: The fog keeps coming while the dry ice is in the water and what has left keeps moving away and fading.
  - fail: The fog runs back into the bowl; or a puff retreats over the rim; or the fog boils up before the dry ice reaches the water; or the fog thickens steadily after the chunks have gone.
- P3 [major · missing_consequence]
  - expect: The water shows the dry ice working: it bubbles and churns around the chunks and the fog rises from there.
  - fail: The water is glassy still while thick fog pours off it; or the fog rises from a part of the bowl with no chunk in it; or the chunks sit in the water with no bubbles and no fog at all.
- P4 [major · material_response]
  - expect: The fog is a dense low cloud that pours, spreads and fades, and the chunks stay hard lumps that shrink.
  - fail: The fog holds a fixed rigid shape; or pools as a liquid with a flat surface; or a chunk melts into a clear liquid on the surface; or the fog breaks into solid lumps.
- P5 [fatal · permanence_count]
  - expect: One bowl; the chunks that go in are the chunks in the water and they shrink rather than vanishing at a stroke.
  - fail: A chunk vanishes in a single frame while still large; or new chunks appear with none dropped; or a chunk passes through the bowl's wall; or the water's level jumps with nothing added.
- P6 [minor · attribute_drift]
  - expect: The bowl's pattern, the table and the punch's colour stay the same.
  - fail: The bowl changes pattern; or the table's setting rearranges; or the punch changes colour.

**Note.** Dry ice fog sinks; that is what this caption asks for and it is not a violation.

## HEAT-0113 · condensation · train

**Caption.** Liquid nitrogen is poured into a metal bowl, and a cloud of white fog rolls over the rim and cascades down the sides.

**Expectation (hidden).** The liquid boils violently in the bowl and the fog spills downward over the edge, hugging the surface it falls onto and thinning as it spreads; the fog does not drift upward like steam.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] Liquid nitrogen is poured into a metal bowl.
- S2 [core] The liquid boils in the bowl.
- S3 [core] White fog rolls over the bowl's rim.
- S4 [core] The fog cascades down the bowl's sides.
- S5 [minor] The fog spreads along the surface it falls onto.
- S6 [minor] The pour comes first and the fog follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The fog spills over the rim and falls down the outside, hugging the surface it lands on and spreading as it thins.
  - fail: The fog rises off the bowl like steam and climbs; or hangs above the rim without falling; or shoots upward in a plume; or rises from the table back into the bowl.
- P2 [core · process_direction]
  - expect: The fog keeps coming while the liquid boils and what has left keeps moving away and fading.
  - fail: The fog runs back into the bowl; or a puff retreats over the rim; or the fog rolls out before the liquid is poured; or the fog thickens steadily after the boiling has stopped.
- P3 [major · missing_consequence]
  - expect: The bowl shows the liquid boiling: it churns hard in the bowl and the fog comes from there.
  - fail: The liquid lies glassy still while thick fog pours off it; or the fog pours from the bowl's outside while the inside is calm and clear; or the liquid is poured in and no fog appears at all.
- P4 [major · material_response]
  - expect: The liquid is a thin clear liquid that boils and skitters, the fog is a dense low cloud that pours and fades, and the bowl stays a rigid metal bowl.
  - fail: The liquid sits as a still clear pool with no movement; or the fog holds a fixed rigid shape; or the fog pools as a liquid with a flat surface; or the bowl's metal sags or melts.
- P5 [fatal · permanence_count]
  - expect: One bowl and one pour; the liquid goes from the flask into the bowl and boils away.
  - fail: Liquid appears in the bowl with none poured; or the liquid's level jumps up with nothing added; or the liquid passes through the bowl's wall; or a second bowl appears.
- P6 [minor · attribute_drift]
  - expect: The bowl's metal, the flask and the table stay the same.
  - fail: The bowl changes colour; or the flask changes shape; or items on the table rearrange.

**Note.** Fog from liquid nitrogen sinks; that is what this caption asks for and it is not a violation.

## HEAT-0114 · condensation · train

**Caption.** The glass door of a supermarket freezer is closed after being held open, and the inside of the glass fogs over, then slowly clears as the cold air circulates.

**Expectation (hidden).** The fog forms on the inner face of the door within moments of closing and fades gradually from the edges or the vents; it does not form on the outside or vanish all at once.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] A supermarket freezer with a glass door.
- S2 [core] The door is closed.
- S3 [core] The inside of the glass fogs over.
- S4 [core] The fog clears again.
- S5 [minor] The fog is on the inner face of the door.
- S6 [minor] The order is closed, fogged, cleared.

**PC**
- P1 [core · process_direction]
  - expect: The fog forms after the door shuts and then only clears; once clear it stays clear with the door shut.
  - fail: The fog forms before the door has closed; or the fog clears and forms again with the door shut; or the fog thickens after it has begun to clear; or the glass is fogged while the door stands open.
- P2 [core · missing_consequence]
  - expect: The clearing spreads from one part of the glass, such as its edges or a vent, with a visible edge.
  - fail: The whole pane goes from fogged to clear at a stroke with no edge at all; or the fog lifts off the glass as a sheet; or the clearing starts and then reverses; or the fog clears while the door is being opened again.
- P3 [major · attribute_drift]
  - expect: The haze lies on the inner face and the outer face stays clear.
  - fail: The fog forms on the outer face; or both faces fog equally; or the door's frame changes colour rather than the glass; or the goods behind the glass change colour as it fogs.
- P4 [major · gravity_direction]
  - expect: Drops that gather in the fog run downward on the inner face.
  - fail: A drop runs up the glass; or a drop leaves the glass and rises; or water gathers along the glass's top edge and stays.
- P5 [fatal · permanence_count]
  - expect: One door on its hinge; the goods behind the glass are the same before and after the fogging.
  - fail: Packets behind the glass appear or vanish while it is fogged; or a second door appears; or the door passes through the cabinet's frame; or the door vanishes.
- P6 [minor · attribute_drift]
  - expect: The cabinet's frame, its labels and the aisle stay the same.
  - fail: The frame changes colour; or the labels change; or the aisle behind changes between frames.

## HEAT-0115 · condensation · train

**Caption.** A steel cocktail shaker filled with ice is shaken, and its outside turns white with frost within seconds.

**Expectation (hidden).** The frost appears as a white haze that spreads over the metal while it is cold, thickest where the ice is inside; it turns to wet droplets as the shaker warms and does not appear on the warm parts.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A steel cocktail shaker is filled with ice.
- S2 [core] The shaker is shaken.
- S3 [core] Its outside turns white with frost.
- S4 [minor] The frost is thickest over the part the ice fills.
- S5 [minor] The shaking comes first and the frost follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The frost appears on the shaker's outside while it is shaken with ice inside, thickest over the part the ice fills.
  - fail: The frost appears before the shaking starts; or the shaker is shaken with ice in it and its outside stays bright and dry to the end of the clip; or the frost appears on the cap while the body over the ice stays bright; or the frost appears on the hands rather than the metal.
- P2 [core · process_direction]
  - expect: The frost only builds while the shaker stays cold and any later change is toward wetness as it warms.
  - fail: The frost thickens, goes and thickens again while the shaking goes on; or wet drops turn back into dry white frost as the shaker warms; or the frost retreats while the ice is still inside; or the frost thins and thickens in turn.
- P3 [major · gravity_direction]
  - expect: Once the frost turns to drops they run downward on the shaker's sides and drip from its base.
  - fail: A drop runs up the shaker; or water gathers on the cap's top and stays as a dome; or a drop leaves the shaker and rises; or a run travels sideways round the shaker and stays level.
- P4 [major · material_response]
  - expect: The frost is a fine white bloom on the metal that softens into beads, and the shaker stays a rigid steel vessel.
  - fail: The frost stands off as thick spikes of ice; or the frost peels away as a sheet; or the shaker's metal flexes as it is shaken; or the frost sets as a hard glaze that stays dry as the shaker warms.
- P5 [fatal · shape_identity]
  - expect: One shaker with its cap on; the shaker keeps its shape and nothing passes through it.
  - fail: The shaker changes shape; or a second shaker appears; or the cap passes into the body; or ice passes out through the steel.
- P6 [minor · attribute_drift]
  - expect: The shaker's finish away from the frost, the hands and the bar stay the same.
  - fail: The shaker changes colour; or the bar's bottles rearrange; or the background changes between frames.

**Note.** The hands are kept because the shaking is the caption's action; they are otherwise not judged.

## HEAT-0116 · condensation · train

**Caption.** A chilled bottle of sparkling water is uncapped, and a small puff of white mist rises from its neck and vanishes.

**Expectation (hidden).** The mist appears at the instant the cap comes off, rises a little above the neck and fades within a second; it does not appear before the cap is off or keep pouring out.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A chilled bottle of sparkling water.
- S2 [core] The cap is taken off.
- S3 [core] A small puff of white mist rises from the neck.
- S4 [core] The puff vanishes.
- S5 [minor] The bottle reads as chilled: frost or condensation on it.
- S6 [minor] The order is uncap, puff, gone.

**PC**
- P1 [core · missing_consequence]
  - expect: The puff appears at the bottle's neck at the instant the cap comes off and not before.
  - fail: The mist appears while the cap is still on tight; or the cap comes off and no mist appears at all to the end of the clip; or the mist appears at the bottle's base rather than its neck; or the mist appears in the air above the bottle with nothing leaving the neck.
- P2 [core · causeless_motion]
  - expect: The puff rises a little from the neck and fades; it does not pour on and on or move about on its own.
  - fail: The mist keeps pouring from the neck for the rest of the clip; or the puff darts sideways with nothing blowing it; or the puff sinks and pools on the table; or the puff shrinks and grows again with the bottle untouched.
- P3 [major · gravity_direction]
  - expect: The puff rises from the neck and spreads as it thins.
  - fail: The puff pours down the bottle's sides and pools; or hangs as a fixed shape without rising; or falls in a stream from the neck; or climbs the bottle from its base up to the neck.
- P4 [major · material_response]
  - expect: The mist is a soft faint haze that spreads and fades, and the water inside fizzes and may rise a little in the neck.
  - fail: The mist holds a fixed rigid shape; or pours as a liquid; or the water inside stays glassy still with no bubbles as the cap comes off; or the mist turns into solid lumps.
- P5 [fatal · permanence_count]
  - expect: One bottle and one cap; the cap comes off whole and the water stays in the bottle.
  - fail: The cap vanishes; or a second cap appears; or the cap passes through the bottle's neck; or the water's level jumps with nothing poured.
- P6 [minor · attribute_drift]
  - expect: The bottle's label, the cap and the surroundings stay the same.
  - fail: The label changes; or the cap changes colour; or items around the bottle rearrange.

**Note.** Who opens the bottle is not judged.

## HEAT-0117 · burn_smoke · train

**Caption.** A sheet of newspaper is laid over a campfire, and the paper catches, curls, blackens, and falls apart into ash.

**Expectation (hidden).** The flame spreads across the paper from where it touched the fire, the paper curls and shrinks as it burns, and grey flakes drift down; the paper does not return or burn from a spot the flame never reached.

**Declared violation types.** process_direction, permanence_count, gravity_direction

**SA**
- S1 [core] A campfire with flames is present.
- S2 [core] A sheet of newspaper is laid over it.
- S3 [core] The paper catches fire.
- S4 [core] The paper curls and blackens.
- S5 [minor] The paper falls apart into ash or flakes.
- S6 [minor] The order is laid, catches, curls and blackens, breaks apart.

**PC**
- P1 [core · process_direction]
  - expect: The burn advances outward from where flame first touches the paper; burnt areas stay black and the paper only shrinks and darkens.
  - fail: Blackened paper turns white again; or the paper grows back or uncurls to flat; or the flame front retreats leaving unburnt paper behind; or the fire starts from a spot no flame reached.
- P2 [major · gravity_direction]
  - expect: Flames on the paper point upward; light flakes may lift in the hot air, but heavier pieces and ash settle down into the fire.
  - fail: Flames point downward; or the whole sheet lifts off the fire and hangs above it; or pieces of paper fall upward away from the fire in still air.
- P3 [major · material_response]
  - expect: Burning paper curls, blackens and thins; it does not melt into liquid or drip.
  - fail: The paper melts and runs like plastic; or stays flat and white while flames sit on it; or turns to ash without ever blackening or curling.
- P4 [major · missing_consequence]
  - expect: Where the paper covers the fire the flames respond: they lick around and through it, and smoke rises from it.
  - fail: The paper sits on the flames with no darkening, smoke or flame reaching it; or flames pass through the sheet leaving it untouched.
- P5 [fatal · permanence_count]
  - expect: The sheet and the fire keep their identity: the paper only shrinks, the logs stay the logs; nothing appears or vanishes abruptly.
  - fail: The paper vanishes in a single step while still whole; or a second sheet appears; or ash appears far from the paper; or logs appear, vanish or pass through each other.
- P6 [minor · attribute_drift]
  - expect: The newsprint pattern, the logs and the surroundings stay consistent apart from the burning.
  - fail: The print on the unburnt part changes; or the logs rearrange; or the ground changes between frames.

## HEAT-0118 · burn_smoke · train

**Caption.** A candle on a table is blown out, and a thin trail of smoke rises from the wick.

**Expectation (hidden).** The flame leans away from the puff of breath and goes out during it; the smoke rises straight up and drifts; the candle does not relight on its own.

**Declared violation types.** missing_consequence, gravity_direction, process_direction

**SA**
- S1 [core] A lit candle stands on a table.
- S2 [core] The flame is blown at: a puff of breath, a face or a visible lean of the flame.
- S3 [core] The flame goes out.
- S4 [core] A thin trail of smoke rises from the wick afterwards.
- S5 [minor] The order is lit, blown, out, smoke.

**PC**
- P1 [core · missing_consequence]
  - expect: The blow acts on the flame: it leans away from the puff, flickers, and goes out during it.
  - fail: The flame keeps burning steadily as the candle is blown; or it leans toward the source of the blow rather than away.
- P2 [core · process_direction]
  - expect: Once out the flame stays out; the wick may glow briefly then darkens; the smoke follows the extinction rather than preceding it.
  - fail: The flame relights by itself; or flickers back and forth between lit and out; or smoke rises from the wick while the flame is still fully burning.
- P3 [major · gravity_direction]
  - expect: The smoke trail rises from the wick, thinning and wavering as it climbs.
  - fail: Smoke sinks down the candle or pools on the table; or runs horizontally along the table with no draught; or flows back into the wick.
- P4 [major · causeless_motion]
  - expect: The candle stays where it is; only the flame and the smoke move.
  - fail: The candle slides or topples while being blown; or rotates; or the smoke stands as a fixed, unmoving shape.
- P5 [fatal · permanence_count]
  - expect: One candle with one wick and one flame; the flame does not detach or split, and the candle keeps its shape.
  - fail: The flame separates from the wick and floats; or a second flame or candle appears; or the candle shortens or grows abruptly; or the wick vanishes.
- P6 [minor · attribute_drift]
  - expect: The candle's colour, the holder and the table stay the same; the room dims only by the loss of the flame.
  - fail: The candle changes colour; or the room gets brighter after the flame is out; or the table pattern shifts.

**Note.** The puff of breath is invisible. Its effect (the lean and the extinction) is what is judged; a flame that simply goes out with no visible puff is not a violation.

## HEAT-0119 · burn_smoke · train

**Caption.** A match is struck against the side of its box, and it flares into a flame that settles to a steady burn.

**Expectation (hidden).** The flame appears at the head at the moment of the strike, flares, then burns steadily pointing upward while the matchstick blackens behind it.

**Declared violation types.** process_direction, gravity_direction, missing_consequence

**SA**
- S1 [core] A match is struck against the side of its box.
- S2 [core] A flame appears at the match head.
- S3 [core] The flame flares up.
- S4 [core] The flame settles to a steady burn.
- S5 [minor] The matchstick blackens behind the flame.
- S6 [minor] The order is strike, flare, steady burn.

**PC**
- P1 [core · missing_consequence]
  - expect: The flame appears at the head at the moment it scrapes the box and not before.
  - fail: The flame appears before the head touches the box; or the head scrapes across the box and no flame appears at all; or the flame appears at the stick's far end; or the flame appears with the match held clear of the box.
- P2 [core · process_direction]
  - expect: The flame flares and then settles to a steady burn, and the blackening behind it only spreads.
  - fail: The flame settles and then flares up again with nothing added; or a blackened part of the stick turns back to pale wood; or the flame goes out and relights by itself; or the blackening retreats along the stick.
- P3 [core · gravity_direction]
  - expect: The flame points upward whatever way the match is held.
  - fail: The flame points downward; or leans with the match rather than standing upright; or hangs below the head; or points along the stick toward the fingers whatever way is up.
- P4 [major · material_response]
  - expect: The matchstick stays a stiff stick that blackens and curls where it has burnt, and the box stays a rigid box.
  - fail: The stick melts and drips; or stays pale and straight where the flame has passed; or the box catches and vanishes at once; or the stick stretches as it burns.
- P5 [fatal · permanence_count]
  - expect: One match and one box; the match shortens only by burning and the box keeps its shape.
  - fail: A second flame appears on the stick; or the match vanishes while still long; or the flame detaches from the match and floats; or the box changes into another object.
- P6 [minor · attribute_drift]
  - expect: The box's label, the hand and the background stay the same.
  - fail: The box's label changes; or the background changes between frames; or the unburnt part of the stick changes colour.

**Note.** The hand is kept because striking is the caption's action; it is otherwise not judged.

## HEAT-0120 · burn_smoke · train

**Caption.** A dry log is tossed onto a campfire, and a burst of sparks flies up into the night.

**Expectation (hidden).** Sparks rise with the hot air, drift, and go out within seconds; the flames climb around the new log; sparks do not fall as bright points to the ground.

**Declared violation types.** gravity_direction, trajectory_momentum, process_direction

**SA**
- S1 [core] A campfire burns.
- S2 [core] A log is tossed onto the fire.
- S3 [core] A burst of sparks flies up.
- S4 [minor] The flames climb around the new log.
- S5 [minor] The sparks go dark as they rise.
- S6 [minor] The toss comes first and the sparks follow.

**PC**
- P1 [core · gravity_direction]
  - expect: The sparks rise with the hot air above the fire, drift and go dark.
  - fail: The sparks fall straight to the ground and lie there glowing; or sink below the fire; or hang still in the air; or travel downward from the fire into the ground.
- P2 [core · trajectory_momentum]
  - expect: The sparks leave the fire where the log lands, spread outward as they rise and their paths curve with the rising air.
  - fail: The sparks rise in straight parallel lines with no spread; or fly out from a point away from where the log landed; or all turn together at the same instant as if steered; or race ahead of the rising smoke and stop dead.
- P3 [core · process_direction]
  - expect: The burst comes at the moment the log lands and then eases, and each spark only fades.
  - fail: The sparks burst before the log lands; or a spark brightens again after fading; or the burst grows steadily with nothing added; or the burst stops and starts again with the fire untouched.
- P4 [major · missing_consequence]
  - expect: The log's landing shows: the fire's logs shift, the flames are pushed aside and then climb around the new log.
  - fail: The log lands and the fire is unchanged, with the flames steady and the logs unmoved; or the flames are pushed aside before the log arrives; or the log rests on the flames without touching the wood beneath.
- P5 [fatal · permanence_count]
  - expect: One log is added and the fire's logs keep their number; sparks come from the fire and go dark rather than vanishing at a stroke while bright.
  - fail: The log vanishes on landing; or a second log appears in the air; or a log passes through another log; or sparks appear in the sky far from the fire with none rising there.
- P6 [minor · attribute_drift]
  - expect: The fire's stones, the ground and the surroundings stay the same.
  - fail: The stones around the fire rearrange; or the ground changes texture; or the background changes between frames.

## HEAT-0121 · burn_smoke · train

**Caption.** Wind gusts across a campfire, and the flames lean over and stretch out sideways before standing up again.

**Expectation (hidden).** The flames bend in the direction the wind blows and return to pointing upward when the gust passes; they do not lean into the wind.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A campfire burns.
- S2 [core] The flames lean over to one side.
- S3 [core] The flames stretch out sideways.
- S4 [core] The flames stand up again afterwards.
- S5 [minor] Other signs of wind show: smoke, grass or clothing move the same way.
- S6 [minor] The order is upright, leaning, upright again.

**PC**
- P1 [core · causeless_motion]
  - expect: The flames lean the way the wind blows, as the smoke and anything loose in the scene show, and stand up again when the gust passes.
  - fail: The flames lean against the way the smoke and grass are blown; or the flames lean while the smoke rises straight up and nothing else moves; or the flames stay leaning after everything else has settled; or each flame leans a different way at the same moment.
- P2 [core · gravity_direction]
  - expect: Between gusts the flames point upward from the wood.
  - fail: The flames point downward between gusts; or hang below the logs; or lie flat along the ground with no sign of wind; or point upward while the smoke above them sinks.
- P3 [major · process_direction]
  - expect: The leaning follows the gust and eases as it passes; the flames do not go out and relight on their own.
  - fail: A flame goes out and relights with nothing touching it; or the lean grows steadily with no gust; or the flames flatten and stand in a rhythm unrelated to any visible sign of wind; or the flames stay flat while the smoke rises straight.
- P4 [major · missing_consequence]
  - expect: The smoke leans with the flames and streams downwind.
  - fail: The smoke rises straight while the flames are flattened; or the smoke leans one way and the flames the other; or the smoke stops while the flames lean hard.
- P5 [fatal · permanence_count]
  - expect: One fire with its logs; the flames stay on the wood and the logs keep their number.
  - fail: A flame detaches from the wood and floats; or a second fire appears beside the first; or a log vanishes; or the flames pass through a log and out below it.
- P6 [minor · attribute_drift]
  - expect: The logs, the stones and the surroundings stay the same.
  - fail: The logs rearrange; or the stones change shape; or the background changes between frames.

## HEAT-0122 · burn_smoke · train

**Caption.** A stick of incense is lit in a quiet room, and a thin ribbon of smoke rises from its tip and curls in the still air.

**Expectation (hidden).** The smoke rises in a thin steady stream that wavers and spreads higher up; the tip glows red; the stick does not lengthen and the smoke does not sink.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] A stick of incense stands in a holder.
- S2 [core] Its tip glows.
- S3 [core] A thin ribbon of smoke rises from the tip.
- S4 [core] The ribbon curls and waves as it rises.
- S5 [minor] The room is still: nothing else moves.
- S6 [minor] The smoke comes from the tip rather than along the stick.

**PC**
- P1 [core · gravity_direction]
  - expect: The smoke leaves the tip going up in a thin stream that waves and spreads higher up.
  - fail: The smoke sinks from the tip to the table and pools; or the ribbon runs straight down the stick; or the smoke hangs as a fixed shape without rising; or the smoke streams sideways and stays level with nothing blowing it.
- P2 [core · process_direction]
  - expect: The smoke keeps leaving the tip and what has left keeps rising and spreading, while the glowing point creeps down the stick.
  - fail: The ribbon runs back into the tip; or a puff retreats to the stick; or the burnt part of the stick returns to unburnt incense; or the stick grows longer as it burns.
- P3 [major · missing_consequence]
  - expect: The smoke comes from the glowing point: the ribbon starts there and the stick behind it is ash.
  - fail: The ribbon starts in the air above the stick with a gap below it; or the smoke comes from the stick's base or holder; or the tip glows while no smoke leaves it at all; or the smoke leaves a part of the stick that has not burnt.
- P4 [major · material_response]
  - expect: The smoke is a fine thread that waves and spreads and the ash is a fragile grey column that bends and may drop.
  - fail: The ribbon holds a fixed rigid shape like a wire; or the smoke pours like a liquid; or the ash stays straight and bright like fresh incense; or the ash falls upward.
- P5 [fatal · permanence_count]
  - expect: One stick in one holder; the stick shortens only by burning and the holder stays put.
  - fail: The stick lengthens; or a second stick appears already lit; or the stick vanishes while still long; or the glowing point jumps to a new place on the stick.
- P6 [minor · attribute_drift]
  - expect: The holder, the table and the room stay the same.
  - fail: The holder changes shape; or the table's pattern changes; or items in the room rearrange.

## HEAT-0123 · burn_smoke · train

**Caption.** A long barbecue lighter is clicked, and a small flame appears at its tip and burns steadily.

**Expectation (hidden).** The flame appears at the click, points upward regardless of how the lighter is tilted, and disappears when the trigger is released.

**Declared violation types.** missing_consequence, gravity_direction

**SA**
- S1 [core] A long barbecue lighter.
- S2 [core] The lighter's trigger is pressed.
- S3 [core] A flame appears at its tip.
- S4 [core] The flame burns steadily.
- S5 [minor] The flame is at the tip rather than the handle.
- S6 [minor] The press comes first and the flame follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The flame appears at the tip at the moment the trigger is pressed and goes out when it is released.
  - fail: The flame is alight before the trigger is pressed; or the trigger is pressed and no flame appears at all; or the flame stays alight after the trigger is released; or the flame appears at the handle rather than the tip.
- P2 [core · gravity_direction]
  - expect: The flame points upward however the lighter is tilted.
  - fail: The flame points downward; or leans along the lighter's barrel as it is tilted; or hangs below the tip; or points at the hand whatever way the lighter is held.
- P3 [major · process_direction]
  - expect: Once lit the flame burns steadily while the trigger is held and does not go out and relight by itself.
  - fail: The flame goes out and relights with the trigger still held; or grows and shrinks in turn with the trigger held steady; or drifts away from the tip and burns in the air; or splits into two flames.
- P4 [major · material_response]
  - expect: The lighter stays a rigid wand and the flame is a soft tongue of light at its tip.
  - fail: The lighter's barrel bends or droops near the flame; or the flame holds a fixed rigid shape like a blade; or the lighter melts; or the flame casts solid pieces.
- P5 [fatal · permanence_count]
  - expect: One lighter with one tip; the lighter keeps its shape and the hand passes through nothing.
  - fail: A second tip or flame appears; or the lighter vanishes; or the hand passes through the lighter; or the lighter changes into another object.
- P6 [minor · attribute_drift]
  - expect: The lighter's body, its trigger and the surroundings stay the same.
  - fail: The lighter changes colour; or the trigger moves to a different place; or the background changes between frames.

## HEAT-0124 · burn_smoke · train

**Caption.** The glowing embers in a fireplace are poked with a poker, and they brighten and send up a swirl of sparks.

**Expectation (hidden).** The embers glow brighter where disturbed, sparks rise and fade, and the glow settles again afterwards; the embers do not turn back into unburnt wood.

**Declared violation types.** missing_consequence, gravity_direction, process_direction

**SA**
- S1 [core] Glowing embers lie in a fireplace.
- S2 [core] A poker pokes the embers.
- S3 [core] The embers brighten where they are disturbed.
- S4 [core] A swirl of sparks rises.
- S5 [minor] The glow settles again afterwards.
- S6 [minor] The poke comes first and the brightening follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The embers brighten where the poker disturbs them and sparks rise from that spot.
  - fail: The embers brighten before the poker reaches them; or the poker stirs the embers and nothing brightens or lifts; or the embers brighten at the far side of the grate from the poker; or sparks rise from a part of the grate the poker never touched.
- P2 [core · gravity_direction]
  - expect: The sparks rise with the hot air, drift and go dark, while the embers stay down in the grate.
  - fail: The sparks fall to the hearth and lie there glowing; or sink below the grate; or an ember lifts and hangs in the air; or the sparks travel downward into the ash.
- P3 [core · process_direction]
  - expect: The brightening eases after the poking stops and the embers do not turn back into unburnt wood.
  - fail: A glowing ember turns back into pale unburnt wood; or the glow keeps brightening after the poker is withdrawn; or the embers go dark and glow again with nothing touching them; or the ash gathers back into a whole log.
- P4 [major · material_response]
  - expect: The embers are crumbling glowing lumps that break and shift under the poker and the ash is loose, while the poker stays rigid.
  - fail: An ember bounces off the poker like a rubber ball; or the embers flow like a liquid; or the poker bends where it touches the embers; or the ash holds a rigid shape when pushed.
- P5 [fatal · permanence_count]
  - expect: The embers in the grate are the embers that were there, breaking up rather than appearing or vanishing, and the poker stays outside them.
  - fail: A glowing ember appears in the grate from nowhere; or an ember vanishes at a stroke while still bright; or the poker passes through the grate's floor; or a second poker appears.
- P6 [minor · attribute_drift]
  - expect: The fireplace's surround, the grate and the hearth stay the same.
  - fail: The surround changes colour; or the grate changes shape; or items on the hearth rearrange.

**Note.** Who holds the poker is not judged.

## HEAT-0125 · burn_smoke · train

**Caption.** The knob on a gas stove is turned, and a ring of blue flames lights around the burner.

**Expectation (hidden).** The flames appear all around the ring within a moment of the click, stand upright, and grow or shrink as the knob is turned; they vanish when it is turned off.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A gas stove with a burner and a knob.
- S2 [core] The knob is turned.
- S3 [core] A ring of flames lights around the burner.
- S4 [core] The flames stand around the whole ring.
- S5 [minor] The flames are blue.
- S6 [minor] The turn comes first and the flames follow.

**PC**
- P1 [core · missing_consequence]
  - expect: The flames appear all around the ring shortly after the knob turns and go out when it is turned off.
  - fail: The flames are alight before the knob is touched; or the knob is turned and no flame appears at all; or the flames light on one side while the rest of the ring stays dark to the end of the clip; or the flames stay alight after the knob is turned back to off.
- P2 [core · process_direction]
  - expect: Once lit the flames hold steady and grow or shrink only as the knob is turned.
  - fail: The flames grow and shrink with the knob untouched; or go out and relight by themselves; or creep off the burner onto the stove top; or the knob turns back by itself.
- P3 [major · gravity_direction]
  - expect: The flames stand upward from the burner's ports.
  - fail: The flames point downward under the burner; or lie flat along the stove top with nothing blowing them; or hang below the burner; or meet in a ball above the centre while the ports are clear.
- P4 [major · material_response]
  - expect: The flames are soft tongues at the ports that flicker, and the burner and grate stay rigid metal.
  - fail: The flames hold fixed rigid shapes like blades; or the burner's metal sags as it lights; or the grate bends; or the flames leave solid pieces behind.
- P5 [fatal · permanence_count]
  - expect: One burner with its ring of ports and one knob; the burner keeps its shape and place.
  - fail: A second burner lights with its own knob untouched; or the burner vanishes; or the burner moves across the stove top; or the knob vanishes.
- P6 [minor · attribute_drift]
  - expect: The stove top, the grate and the other knobs stay the same.
  - fail: The stove top changes colour; or the grate changes pattern; or another knob moves by itself.

## HEAT-0126 · burn_smoke · train

**Caption.** A metal snuffer is lowered over a candle flame, and the flame dies and smoke curls out from under the snuffer.

**Expectation (hidden).** The flame goes out within a moment of being covered, and smoke leaks out and rises when the snuffer is lifted; the flame does not keep burning under the cap.

**Declared violation types.** missing_consequence, gravity_direction

**SA**
- S1 [core] A lit candle.
- S2 [core] A metal snuffer is lowered over the flame.
- S3 [core] The flame goes out.
- S4 [core] Smoke curls out from under the snuffer.
- S5 [minor] The snuffer covers the flame.
- S6 [minor] The order is lowered, out, smoke.

**PC**
- P1 [core · missing_consequence]
  - expect: The flame goes out once the snuffer covers it and does not keep burning under the cap.
  - fail: The flame burns on under the closed snuffer; or the flame goes out before the snuffer reaches it; or the flame goes out with the snuffer still held well clear; or the flame relights while the snuffer is still over it.
- P2 [core · gravity_direction]
  - expect: The smoke escapes under the snuffer's rim and rises, and it rises from the wick when the snuffer is lifted.
  - fail: The smoke sinks down the candle and pools on the table; or pours downward through the candle; or hangs as a fixed shape without rising; or runs back into the wick.
- P3 [major · process_direction]
  - expect: Once out the flame stays out; the wick may glow briefly and then darkens.
  - fail: The flame relights by itself after the snuffer is lifted; or flickers back and forth between lit and out; or the wick's glow brightens after the flame has gone; or smoke rises from the wick while the flame still burns at full size.
- P4 [major · material_response]
  - expect: The snuffer stays a rigid metal cap on its handle, the candle keeps its shape, and the smoke is a fine thread that waves.
  - fail: The snuffer bends or melts over the flame; or the candle's body sags as the snuffer comes down; or the smoke holds a fixed rigid shape; or the snuffer sticks to the candle and lifts it.
- P5 [fatal · permanence_count]
  - expect: One candle with one wick and one snuffer; the flame does not detach or split.
  - fail: The flame separates from the wick and floats; or a second flame or candle appears; or the snuffer passes through the candle; or the wick vanishes.
- P6 [minor · attribute_drift]
  - expect: The candle's colour, the holder and the table stay the same.
  - fail: The candle changes colour; or the holder moves or vanishes; or the table's pattern changes.

## HEAT-0127 · burn_smoke · train

**Caption.** A bucket of water is poured over a dying campfire, and the fire goes out with a hiss in a cloud of steam and smoke.

**Expectation (hidden).** The flames vanish where the water lands, a thick cloud rises and thins, and the wet ash stays dark; the fire does not flare back up.

**Declared violation types.** missing_consequence, gravity_direction, process_direction

**SA**
- S1 [core] A campfire burns with small flames.
- S2 [core] Water is poured over the fire from a bucket.
- S3 [core] The flames go out where the water lands.
- S4 [core] A cloud of steam and smoke rises.
- S5 [minor] The wet ash stays dark.
- S6 [minor] The pour comes first and the cloud follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The flames go out where the water lands and the ash there goes dark and wet.
  - fail: The water lands and the flames burn on unchanged; or the flames go out before the water reaches them; or the flames go out in a part of the fire the water never reached while the wetted part burns on; or the ash stays dry and pale where the water has soaked it.
- P2 [core · gravity_direction]
  - expect: The water falls downward onto the fire while the steam and smoke rise, spreading and thinning.
  - fail: The water travels upward from the bucket; or the cloud sinks and pools around the fire; or the cloud hangs as a fixed shape without rising; or the water runs uphill out of the fire pit.
- P3 [core · process_direction]
  - expect: The fire only dies: doused flames do not flare back up and the wetted ash stays dark.
  - fail: A doused part of the fire flares up again with nothing added; or the wet ash dries and glows again; or the flames shrink and grow in turn while water keeps pouring; or the ash gathers back into unburnt wood.
- P4 [major · material_response]
  - expect: The water falls as a thin liquid and soaks the ash, the cloud is soft and spreading, and the logs stay charred solids.
  - fail: The water bounces off the fire as a solid lump; or the cloud holds a fixed rigid shape; or the logs melt or flow; or the water sits on the ash as beads that do not soak in.
- P5 [fatal · permanence_count]
  - expect: One bucket and one fire; the logs keep their number and the water goes only from the bucket to the fire.
  - fail: A log vanishes at a stroke; or a new log appears; or water appears in the fire pit with none poured there; or the bucket passes through a log.
- P6 [minor · attribute_drift]
  - expect: The fire's stones, the ground and the surroundings stay the same.
  - fail: The stones rearrange; or the ground changes texture away from the water; or the background changes between frames.

**Note.** The hiss is sound and is not judged.

## HEAT-0128 · burn_smoke · train

**Caption.** A lit sparkler stands upright in a cake, throwing off a spray of bright sparks that fade as they fall.

**Expectation (hidden).** Sparks fly outward and downward from the burning point and go dark within a short distance; the burning point moves down the wire, never back up, and the spent wire above it is dark.

**Declared violation types.** gravity_direction, permanence_count, process_direction

**SA**
- S1 [core] A lit sparkler stands upright in a cake.
- S2 [core] Sparks spray out from the sparkler's burning point.
- S3 [core] The sparks fade as they travel.
- S4 [minor] The burning point is part-way down the wire.
- S5 [minor] The wire above the burning point is dark.
- S6 [minor] The sparks travel away from the sparkler.

**PC**
- P1 [core · gravity_direction]
  - expect: The sparks fly outward from the burning point and their paths bend downward, going dark before or as they land.
  - fail: The sparks rise steadily and gather above the sparkler; or hang in the air; or lie on the cake glowing like lamps for the rest of the clip; or curve upward after leaving the wire.
- P2 [core · permanence_count]
  - expect: Each spark fades within a short flight and none accumulate, and the sparkler is one wire.
  - fail: Sparks persist as fixed bright dots; or a glowing pile builds on the cake; or sparks appear in the air far from the sparkler; or a second sparkler appears already lit.
- P3 [core · process_direction]
  - expect: The burning point only travels down the wire and the spent wire above it stays dark.
  - fail: The burning point climbs back up the wire; or a dark part of the wire lights up again; or the burning point jumps to a new place on the wire; or the spent wire turns back to fresh coating.
- P4 [major · missing_consequence]
  - expect: The sparks come from the burning point and the wire behind it is spent.
  - fail: The sparks come from a part of the wire that is still coated and unburnt; or the sparks come from the wire's tip while the burning point is elsewhere; or the sparkler burns with no sparks leaving it at all.
- P5 [fatal · shape_identity]
  - expect: One sparkler in one cake; the wire stays a straight wire and the cake keeps its shape.
  - fail: The wire bends into another shape; or the sparkler passes through the cake and out below; or a second wire appears; or the cake changes shape.
- P6 [minor · attribute_drift]
  - expect: The cake's icing away from the sparkler, the plate and the table stay the same.
  - fail: The icing changes colour; or the plate changes pattern; or items on the table rearrange.

## HEAT-0129 · burn_smoke · train

**Caption.** A kerosene lamp is lit with a match, and the wick catches and the flame steadies inside the glass chimney.

**Expectation (hidden).** The flame starts at the wick where the match touches, stands upright inside the glass, and keeps burning after the match is withdrawn.

**Declared violation types.** missing_consequence, gravity_direction

**SA**
- S1 [core] A kerosene lamp with a wick and a glass chimney.
- S2 [core] A match is held to the wick.
- S3 [core] The wick catches: a flame appears at it.
- S4 [core] The flame steadies inside the chimney.
- S5 [minor] The match is withdrawn and the flame keeps burning.
- S6 [minor] The order is match to wick, catch, steady.

**PC**
- P1 [core · missing_consequence]
  - expect: The flame starts at the wick where the match touches it and keeps burning after the match is taken away.
  - fail: The wick is alight before the match reaches it; or the match touches the wick and no flame appears at all; or the flame goes out as soon as the match is withdrawn; or the flame appears above the chimney rather than at the wick.
- P2 [core · gravity_direction]
  - expect: The flame stands upward from the wick inside the chimney.
  - fail: The flame points downward from the wick; or lies flat inside the chimney with nothing blowing it; or hangs below the wick; or rises out through the chimney's top and burns in the air above it.
- P3 [major · process_direction]
  - expect: Once steady the flame holds and does not go out and relight by itself.
  - fail: The flame goes out and relights with nothing touching the lamp; or grows and shrinks in turn with the wick untouched; or splits into two flames; or drifts off the wick and burns in the chimney's middle.
- P4 [major · material_response]
  - expect: The wick stays a soft charring cord, the chimney a rigid clear glass, and the lamp's body solid.
  - fail: The chimney melts or bends over the flame; or the wick stretches upward as the flame burns; or the glass ripples as the flame steadies; or the lamp's base sags.
- P5 [fatal · permanence_count]
  - expect: One lamp with one wick, one chimney and one flame, and the match is a separate stick.
  - fail: A second flame appears on the wick; or the chimney vanishes; or the match passes through the glass; or the flame detaches and floats out of the lamp.
- P6 [minor · attribute_drift]
  - expect: The lamp's metal, the glass's shape and the room stay the same.
  - fail: The lamp changes colour; or the chimney changes shape; or items in the room rearrange.

**Note.** Whoever holds the match is not judged.

## HEAT-0130 · burn_smoke · train

**Caption.** A match is set to a pile of dry leaves, and the fire spreads across the pile with smoke rising from it.

**Expectation (hidden).** The flames spread outward from the lit spot, leaves blacken and shrink into ash, and smoke rises; burnt leaves do not become whole again.

**Declared violation types.** process_direction, gravity_direction, permanence_count

**SA**
- S1 [core] A pile of dry leaves.
- S2 [core] A match is set to the pile.
- S3 [core] Flames spread across the pile.
- S4 [core] Leaves blacken and shrink.
- S5 [minor] Smoke rises from the pile.
- S6 [minor] The flames spread outward from where the match touched.

**PC**
- P1 [core · process_direction]
  - expect: The burn advances outward from the lit spot and burnt leaves stay black and shrunken.
  - fail: Blackened leaves turn green or pale again; or the flame front retreats leaving unburnt leaves behind it; or the fire starts at a spot no flame reached; or ash gathers back into whole leaves.
- P2 [core · gravity_direction]
  - expect: The flames point upward from the pile and the smoke rises, while ash and burnt fragments settle down.
  - fail: The flames point downward into the ground; or the smoke sinks and pools around the pile; or burnt fragments rise steadily and stay aloft; or the flames hang below the pile.
- P3 [core · permanence_count]
  - expect: The leaves in the pile are the leaves that burn: they shrink to ash rather than vanishing at a stroke, and none appear.
  - fail: The pile vanishes in a single frame while still whole; or new leaves appear on the burning pile; or a leaf vanishes leaving no ash; or the pile grows as it burns.
- P4 [major · missing_consequence]
  - expect: Where the flames reach, the leaves darken, curl and smoke, and leaves the flames have not reached stay dry and pale.
  - fail: Leaves far from the flames blacken while those in the flames stay pale; or the flames pass over leaves and leave them green and flat; or smoke rises from a part of the pile with no flame or char.
- P5 [fatal · shape_identity]
  - expect: The pile stays a pile of leaves that burns down and the ground below stays ground.
  - fail: The leaves turn into another material as they burn; or the ground opens up under the pile; or a second pile appears already burning; or the flames pass through the ground.
- P6 [minor · attribute_drift]
  - expect: The ground around the pile and the surroundings stay the same.
  - fail: The ground changes texture away from the fire; or the background changes between frames; or the unburnt leaves change colour.

**Note.** Who strikes the match is not judged.

## HEAT-0131 · burn_smoke · train

**Caption.** A charcoal chimney starter is lit, and flames and smoke rise up through the coals from the paper burning below.

**Expectation (hidden).** The fire climbs upward through the chimney and smoke pours out of the top; the flames do not start at the top.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] A charcoal chimney starter is filled with coals.
- S2 [core] Paper burns below the coals.
- S3 [core] Flames rise up through the coals.
- S4 [core] Smoke pours out of the top.
- S5 [minor] The fire starts at the bottom.
- S6 [minor] The order is paper lit below, flames climb, smoke at the top.

**PC**
- P1 [core · gravity_direction]
  - expect: The flames and smoke travel upward through the coals and out of the chimney's top.
  - fail: The flames start at the top and travel down; or the smoke pours out of the bottom and sinks to the ground; or the flames point downward out of the base; or the smoke hangs as a fixed shape without rising.
- P2 [core · process_direction]
  - expect: The fire only climbs: the coals catch from the bottom upward and lit coals stay lit.
  - fail: A lit coal turns back to cold black charcoal; or the fire starts at the top of the chimney; or the flames climb and then fall back to the paper leaving the coals cold; or the paper below turns back into unburnt paper.
- P3 [major · missing_consequence]
  - expect: The paper burning below feeds the flames and the coals above it begin to glow.
  - fail: The paper burns and the coals above stay untouched and cold to the end of the clip; or the coals glow while the paper below is unlit; or the flames appear in the middle of the chimney with the paper below unlit.
- P4 [major · material_response]
  - expect: The coals stay hard lumps that glow and shift as they settle and the paper chars and crumbles, while the chimney stays a rigid metal can.
  - fail: A coal melts or flows; or the coals swell up and fill the chimney; or the paper melts and drips; or the chimney's metal sags or bulges.
- P5 [fatal · permanence_count]
  - expect: One chimney with its coals; the coals keep their number and stay inside until the chimney is tipped.
  - fail: A coal vanishes; or new coals appear with none added; or a coal passes through the chimney's wall; or the chimney changes shape.
- P6 [minor · attribute_drift]
  - expect: The chimney's handle, the ground and the surroundings stay the same.
  - fail: The handle changes shape; or the ground changes texture; or items around the chimney rearrange.

## HEAT-0132 · burn_smoke · train

**Caption.** A fatty burger is flipped on a grill, and fat drips onto the coals and a flame flares up under the patty.

**Expectation (hidden).** The flare appears where the fat lands and dies back after a moment; the flames go upward around the patty.

**Declared violation types.** missing_consequence, gravity_direction, process_direction

**SA**
- S1 [core] A burger patty lies on a grill.
- S2 [core] The patty is flipped.
- S3 [core] Fat drips from the patty onto the coals.
- S4 [core] A flame flares up under the patty.
- S5 [minor] The flare dies back after a moment.
- S6 [minor] The order is flip, drip, flare.

**PC**
- P1 [core · missing_consequence]
  - expect: The flare appears where the fat lands on the coals and dies back after a moment.
  - fail: The flare appears before any fat has dripped; or fat drips onto the coals and nothing flares at all; or the flare appears at a part of the grill no fat reached; or the flare keeps growing with no more fat dripping.
- P2 [core · gravity_direction]
  - expect: The fat drips downward from the patty to the coals and the flames climb upward around the patty.
  - fail: Fat drips upward from the patty; or a drip hangs in the air between patty and coals; or the flames point downward away from the patty; or the flames hang below the coals.
- P3 [core · process_direction]
  - expect: The flare only rises and then dies back and does not return with no more fat, and the patty's seared face does not return to raw.
  - fail: The flare dies back and rises again with no fresh drip; or the patty's seared face turns back to raw pink where the flame licked it; or the flare shrinks and grows in turn with the patty still; or a burnt mark on the patty fades.
- P4 [major · material_response]
  - expect: The fat leaves as thin drops that fall and sizzle, the patty stays a soft solid that dents under the tongs, and the bars stay rigid.
  - fail: The fat leaves as a solid lump; or the patty flows off the bars as a liquid; or the patty shatters when flipped; or the grill bars bend under the patty.
- P5 [fatal · permanence_count]
  - expect: One patty on one grill; the patty keeps its shape apart from the flip and the coals keep their number.
  - fail: The patty vanishes; or a second patty appears; or the patty passes through the bars and out below; or a coal vanishes leaving no ash.
- P6 [minor · attribute_drift]
  - expect: The grill's bars, the coals' bed and the surroundings stay the same.
  - fail: The bars change spacing; or the coals rearrange where no fat fell; or the background changes between frames.

**Note.** The patty browning as it cooks is chemistry and is not judged. Who flips the burger is not judged.

## HEAT-0133 · burn_smoke · train

**Caption.** Air is blown gently onto the embers of a fire, and they glow brighter and a small flame springs up.

**Expectation (hidden).** The embers brighten while the air blows and the flame appears at the brightest spot; the glow eases when the blowing stops.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] Embers of a fire.
- S2 [core] Air is blown onto the embers.
- S3 [core] The embers glow brighter.
- S4 [core] A small flame springs up.
- S5 [minor] The flame appears at the brightest spot.
- S6 [minor] The glow eases when the blowing stops.

**PC**
- P1 [core · missing_consequence]
  - expect: The embers brighten where the air reaches them while the blowing lasts, and the flame appears at the brightest spot.
  - fail: The embers brighten before any air reaches them; or the air is blown onto the embers and nothing brightens; or the embers brighten on the far side from the blowing; or the flame appears away from the brightened embers.
- P2 [core · process_direction]
  - expect: The brightening follows the blowing and eases when it stops, and the embers do not turn back into unburnt wood.
  - fail: The glow keeps brightening after the blowing has stopped; or a glowing ember turns back into pale unburnt wood; or the glow eases while the blowing goes on; or the flame appears before the embers brighten.
- P3 [major · gravity_direction]
  - expect: The flame points upward from the embers and any ash or sparks lifted by the air rise and then settle.
  - fail: The flame points downward into the ash; or ash blown up keeps rising and stays aloft; or sparks fall through the grate and lie glowing below; or the flame hangs below the embers.
- P4 [major · material_response]
  - expect: The embers are crumbling glowing lumps and the ash is loose dust that lifts in the moving air.
  - fail: An ember bounces like a rubber ball as the air hits it; or the ash stays a rigid crust as the air blows over it; or the embers flow like a liquid; or the ash lifts as one solid sheet.
- P5 [fatal · permanence_count]
  - expect: The embers are the embers that were there; none appears from nowhere or vanishes at a stroke while bright.
  - fail: A glowing ember appears from nowhere; or an ember vanishes at a stroke while still bright; or the flame detaches and floats away from the wood; or a second fire appears.
- P6 [minor · attribute_drift]
  - expect: The grate, the surround and the surroundings stay the same.
  - fail: The grate changes shape; or the surround changes colour; or the background changes between frames.

**Note.** The breath is invisible; the embers brightening is what shows it. Who blows is not judged.

## HEAT-0134 · burn_smoke · train

**Caption.** A lid is slid over a small grease fire in a pan, and the flames go out.

**Expectation (hidden).** The flames die within moments of the lid covering the pan and smoke seeps from the edges; the fire does not keep burning under the lid.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A pan with flames on its contents.
- S2 [core] A lid is slid over the pan.
- S3 [core] The flames go out.
- S4 [minor] Smoke seeps from the lid's edges.
- S5 [minor] The lid covers the pan fully.
- S6 [minor] The order is flames, lid on, out.

**PC**
- P1 [core · missing_consequence]
  - expect: The flames go out once the lid covers the pan and do not keep burning under it.
  - fail: The flames burn on under the closed lid; or the flames go out before the lid reaches the pan; or the flames go out with the lid still held clear; or the flames relight while the lid is still on.
- P2 [core · process_direction]
  - expect: Once out the fire stays out while the lid is on, and any smoke only thins.
  - fail: The flames relight under the closed lid; or the flames go out and come back with the lid on; or the smoke thickens steadily under the closed lid; or the fire grows as the lid comes down.
- P3 [major · gravity_direction]
  - expect: The smoke seeps out at the lid's rim and rises.
  - fail: The smoke pours downward from under the lid onto the hob; or sinks and pools around the pan; or hangs as a fixed shape without rising; or runs back under the lid.
- P4 [major · material_response]
  - expect: The lid stays a rigid disc that sits on the pan's rim and the pan keeps its shape.
  - fail: The lid bends or melts over the flames; or the pan's wall sags; or the lid sticks to the flames and lifts with them; or the lid sinks into the pan's contents.
- P5 [fatal · permanence_count]
  - expect: One pan with one lid; the pan stays on the hob and nothing passes through it.
  - fail: The lid passes through the pan's rim; or a second lid appears; or the flames pass through the lid and burn above it; or the pan vanishes.
- P6 [minor · attribute_drift]
  - expect: The pan's handle, the hob and the surroundings stay the same.
  - fail: The handle changes shape; or the hob's knobs move by themselves; or items around the hob rearrange.

**Note.** Who slides the lid is not judged.

## HEAT-0135 · burn_smoke · train

**Caption.** Smoke drifts from a chimney on a windy day and is blown sideways as it leaves the stack.

**Expectation (hidden).** The smoke rises a little then streams downwind, in the same direction as trees and flags bend; it does not go against the wind.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] Smoke leaves a chimney.
- S2 [core] The smoke is blown sideways.
- S3 [minor] The smoke rises a little before it streams away.
- S4 [minor] Trees or flags nearby bend the same way.
- S5 [minor] The smoke thins with distance.

**PC**
- P1 [core · causeless_motion]
  - expect: The smoke streams the same way the trees and flags in the scene are bent and keeps that direction while they hold theirs.
  - fail: The smoke streams against the way the trees and flags bend; or the smoke stands straight up while the trees are bent hard; or the smoke's direction swings about while the trees hold steady; or the smoke streams one way while other smoke in the scene streams the other.
- P2 [core · gravity_direction]
  - expect: The smoke leaves the stack going up before it is carried sideways and thins as it goes; it does not sink down the roof.
  - fail: The smoke pours down the chimney's side and along the roof; or sinks to the ground and pools; or goes straight down from the stack's mouth; or hangs as a fixed shape without rising or drifting.
- P3 [major · process_direction]
  - expect: The plume keeps leaving the stack and what has left keeps moving away and fading.
  - fail: The plume runs back into the chimney; or a puff retreats toward the mouth; or smoke appears downwind with none leaving the stack; or the plume grows with nothing leaving the chimney.
- P4 [major · material_response]
  - expect: The smoke is a soft cloud that spreads, waves and fades, and the chimney stays a rigid stack.
  - fail: The plume holds a fixed rigid shape; or pours like a liquid; or the chimney bends with the plume; or the plume breaks into solid lumps.
- P5 [fatal · permanence_count]
  - expect: One chimney on one roof; the chimney stays in place and the roof keeps its shape.
  - fail: The chimney vanishes; or a second chimney appears; or the chimney sinks into the roof; or the roof changes shape.
- P6 [minor · attribute_drift]
  - expect: The roof's tiles, the chimney's brick and the house stay the same.
  - fail: The tiles change pattern; or the brickwork changes colour; or the house's windows change layout.

## HEAT-0136 · burn_smoke · train

**Caption.** A bonfire on a beach burns high, and sparks and embers rise into the dark sky and wink out.

**Expectation (hidden).** The sparks climb with the hot air, drift, and go dark high above the fire; the flames point upward and lean with the sea breeze.

**Declared violation types.** gravity_direction, permanence_count, process_direction

**SA**
- S1 [core] A bonfire burns on a beach.
- S2 [core] Sparks and embers rise from the fire.
- S3 [core] The sparks go dark high above the fire.
- S4 [minor] The flames point upward.
- S5 [minor] The flames lean with the breeze.
- S6 [minor] The sky is dark.

**PC**
- P1 [core · gravity_direction]
  - expect: The sparks rise with the hot air above the flames, drift and go dark, and the flames point upward from the wood.
  - fail: The sparks fall to the sand and lie there glowing; or sink below the fire; or the flames point downward into the sand; or the sparks travel downward into the ground.
- P2 [core · permanence_count]
  - expect: Each spark fades in flight and none accumulate, and the fire's wood keeps its number.
  - fail: Sparks persist as fixed bright dots in the sky; or a glowing pile builds on the sand; or sparks appear in the sky far from the fire with none rising there; or a log vanishes at a stroke.
- P3 [core · process_direction]
  - expect: Each spark only fades as it rises and the fire's wood only chars.
  - fail: A spark brightens again after fading; or a charred log turns back to pale unburnt wood; or the sparks stream out and then stream back into the fire; or the ash gathers back into whole logs.
- P4 [major · missing_consequence]
  - expect: The flames lean the same way as the smoke and anything loose in the scene.
  - fail: The flames lean against the way the smoke streams; or the flames stand straight while the smoke is flattened; or the flames lean while the smoke rises straight and nothing else moves.
- P5 [fatal · shape_identity]
  - expect: The fire's logs keep their shapes as they char and the beach stays sand.
  - fail: A log turns into another object; or the logs merge into one smooth mass; or the sand opens up under the fire; or the flames pass through a log and out below it.
- P6 [minor · attribute_drift]
  - expect: The sand, the sea behind and the surroundings stay the same.
  - fail: The sand changes colour; or the sea's edge jumps to a new place; or the background changes between frames.

## HEAT-0137 · burn_smoke · train

**Caption.** A blowtorch heats a copper pipe, and the flame roars out of the nozzle in a blue cone.

**Expectation (hidden).** The flame points in the direction the torch is aimed, appears and disappears with the valve, and the pipe darkens where it is heated.

**Declared violation types.** missing_consequence, trajectory_momentum

**SA**
- S1 [core] A blowtorch is aimed at a copper pipe.
- S2 [core] A flame comes out of the torch's nozzle.
- S3 [core] The flame is a blue cone.
- S4 [core] The pipe darkens where the flame plays on it.
- S5 [minor] The flame comes and goes with the torch's valve.
- S6 [minor] The flame points where the torch is aimed.

**PC**
- P1 [core · missing_consequence]
  - expect: The flame points where the torch points, comes and goes with the valve, and the pipe changes only where it plays.
  - fail: The flame is alight before the valve is opened; or the valve is opened and no flame appears; or the pipe darkens on a side the flame never reaches; or the flame plays on the pipe and the pipe stays bright and unchanged to the end of the clip.
- P2 [core · trajectory_momentum]
  - expect: The flame leaves the nozzle along its axis as a cone that holds its direction as the torch moves and bends only where it meets the pipe.
  - fail: The flame streams out at right angles to the nozzle; or lags behind as the torch swings and catches up later; or curls back onto the torch's body; or the cone points at the pipe while the nozzle points away.
- P3 [major · gravity_direction]
  - expect: The flame keeps its direction whatever way the torch is tilted and does not fall.
  - fail: The flame droops downward as the torch is tilted up; or falls off the nozzle and lands; or hangs below the nozzle in still air; or rises straight up while the nozzle points sideways.
- P4 [major · material_response]
  - expect: The pipe stays a rigid tube that darkens and may glow where it is heated, and the torch stays a rigid tool.
  - fail: The pipe sags or bends where the flame plays with nothing bending it; or the pipe itself drips away as a liquid; or the torch's nozzle melts; or the pipe swells up.
- P5 [fatal · permanence_count]
  - expect: One torch and one pipe; the flame stays at the nozzle and the pipe stays one piece.
  - fail: A second flame appears away from the nozzle; or the flame detaches and floats; or the pipe splits in two with nothing cutting it; or the torch vanishes.
- P6 [minor · attribute_drift]
  - expect: The torch's body, the bench and the pipe away from the heated patch stay the same.
  - fail: The torch changes colour; or the bench's contents rearrange; or the pipe changes colour away from where the flame plays.

## HEAT-0138 · burn_smoke · train

**Caption.** A hose sprays water onto a burning shed, and the flames shrink and the smoke turns from black to white steam.

**Expectation (hidden).** The flames die where the water lands and rising steam replaces the dark smoke; the fire does not grow while being doused.

**Declared violation types.** missing_consequence, process_direction, attribute_drift

**SA**
- S1 [core] A shed is burning.
- S2 [core] A hose sprays water onto it.
- S3 [core] The flames shrink where the water lands.
- S4 [core] The dark smoke gives way to white steam.
- S5 [minor] The steam rises from the wetted parts.
- S6 [minor] The spraying comes first and the shrinking follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The flames shrink where the water lands and the wetted parts stop burning.
  - fail: The water lands and the flames burn on unchanged there; or the flames shrink on a part of the shed the water never reached; or the flames shrink before the water arrives; or the fire grows where the water lands.
- P2 [core · process_direction]
  - expect: The fire only shrinks while the water keeps coming and doused parts do not flare back up.
  - fail: A doused part flares up again while the water still plays on it; or the flames shrink and grow in turn with the spray steady; or the charred wood turns back to unburnt timber; or the fire spreads to parts already soaked.
- P3 [core · attribute_drift]
  - expect: The smoke above the wetted parts changes from dark to white and stays white while the water plays there.
  - fail: The white steam turns back to black smoke where the water still lands; or the smoke stays black over a part that is steaming wet; or the whole plume turns white before any water arrives; or the shed's paint changes colour rather than the smoke.
- P4 [major · gravity_direction]
  - expect: The water arcs from the hose down onto the shed while the smoke and steam rise.
  - fail: The water arcs upward and keeps climbing out of view; or the plume sinks and pools around the shed; or the water runs up the shed's wall; or the plume hangs as a fixed shape without rising.
- P5 [fatal · permanence_count]
  - expect: One shed and one stream; the shed's walls and roof stay in place as they char and the water comes only from the hose.
  - fail: The shed vanishes at a stroke; or a second shed appears; or water appears on the shed with no stream reaching it; or the stream passes through a wall and out the far side unchanged.
- P6 [minor · attribute_drift]
  - expect: The ground around the shed, the hose and the surroundings stay the same.
  - fail: The ground changes texture away from the water; or the background changes between frames; or the hose changes colour.

**Note.** Who holds the hose is not judged.

## HEAT-0139 · burn_smoke · train

**Caption.** A lit sparkler is dropped into a bucket of water, and it goes out with a hiss and a puff of steam.

**Expectation (hidden).** The sparks stop as the sparkler enters the water, a small cloud rises, and the wire sinks dark; it does not keep sparking under water.

**Declared violation types.** missing_consequence, gravity_direction, process_direction

**SA**
- S1 [core] A lit sparkler throws sparks.
- S2 [core] The sparkler is dropped into a bucket of water.
- S3 [core] The sparks stop.
- S4 [core] A puff of steam rises from the bucket.
- S5 [minor] The wire sinks dark in the water.
- S6 [minor] The drop comes first and the stopping follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The sparks stop as the sparkler enters the water and it does not keep sparking under the surface.
  - fail: The sparkler keeps throwing sparks under the water; or the sparks stop before the sparkler reaches the water; or the sparks stop with the sparkler still held clear of the bucket; or the sparks start again while the sparkler is submerged.
- P2 [core · gravity_direction]
  - expect: The sparkler falls downward into the water and sinks or rests in it while the steam rises.
  - fail: The sparkler rises out of the water with nothing lifting it; or the steam pours down the bucket's sides and pools; or the sparkler hangs in the air above the water; or the steam sinks below the bucket.
- P3 [core · process_direction]
  - expect: The burning only ends: the spent wire stays dark and the puff comes at the moment of entry and then eases.
  - fail: The wire lights again under the water; or the dark wire turns back to fresh coating; or the steam bursts before the sparkler enters; or the puff grows steadily after the sparkler is in.
- P4 [major · missing_consequence]
  - expect: The water shows the sparkler arriving: it splashes and ripples where it lands and the steam rises from there.
  - fail: The sparkler enters and the surface stays glassy; or the water ripples before the sparkler reaches it; or the steam rises from a part of the bucket the sparkler never entered.
- P5 [fatal · permanence_count]
  - expect: One sparkler and one bucket; the wire goes into the water and stays there.
  - fail: The sparkler vanishes in the water; or a second sparkler appears; or the wire passes through the bucket's wall; or the water's level jumps with nothing added.
- P6 [minor · attribute_drift]
  - expect: The bucket, the water and the surroundings stay the same.
  - fail: The bucket changes colour; or the water turns a colour; or items around the bucket rearrange.

**Note.** The hiss is sound and is not judged.

## HEAT-0140 · burn_smoke · train

**Caption.** A campfire is fed with damp wood, and thick white smoke pours off the logs while the flames struggle.

**Expectation (hidden).** The smoke rises thickly and drifts with the wind; the flames stay small and flicker; the smoke does not settle to the ground.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] A campfire burns with damp-looking wood.
- S2 [core] Thick white smoke pours off the logs.
- S3 [core] The flames stay small and flicker.
- S4 [minor] The smoke drifts with the wind.
- S5 [minor] The smoke is thicker than the flames are tall.

**PC**
- P1 [core · gravity_direction]
  - expect: The smoke leaves the logs going up, spreading and thinning; it may lean with the wind but does not settle to the ground.
  - fail: The smoke sinks and lies on the ground around the fire; or pours downward through the logs; or hangs as a fixed shape without rising; or the flames point downward.
- P2 [core · process_direction]
  - expect: The smoke keeps leaving the wood and what has left keeps moving away and fading, while the wood only chars.
  - fail: The plume runs back into the logs; or a puff retreats to the wood; or a charred log turns back to pale unburnt wood; or smoke appears downwind with none leaving the fire.
- P3 [major · missing_consequence]
  - expect: The smoke comes off the wood where it is heated and the logs darken and steam there.
  - fail: The smoke pours from a log that stays bright and unmarked to the end of the clip; or the smoke rises from the ground beside the fire while the logs are clear; or the logs char while no smoke leaves them at all.
- P4 [major · material_response]
  - expect: The smoke is a thick soft cloud that billows and fades, the flames are small soft tongues, and the wood stays solid and charring.
  - fail: The plume holds a fixed rigid shape; or the smoke pours like a liquid; or a log melts or flows; or the flames hold fixed rigid shapes like blades.
- P5 [fatal · permanence_count]
  - expect: The fire's logs keep their number and char rather than vanishing.
  - fail: A log vanishes at a stroke; or a new log appears; or a log passes through another log; or the flames detach and float away.
- P6 [minor · attribute_drift]
  - expect: The stones, the ground and the surroundings stay the same.
  - fail: The stones rearrange; or the ground changes texture; or the background changes between frames.

## HEAT-0141 · burn_smoke · train

**Caption.** A row of tea-light candles is lit one after another with a long match, and each flame stands upright after it catches.

**Expectation (hidden).** Each candle lights only when the match touches it and stays lit afterwards; none lights before being touched or goes out on its own.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A row of tea-light candles.
- S2 [core] A long match is held to the candles one after another.
- S3 [core] Each candle lights when the match touches it.
- S4 [core] Each flame stands upright once lit.
- S5 [minor] The candles light in order along the row.
- S6 [minor] The candles not yet touched stay dark.

**PC**
- P1 [core · missing_consequence]
  - expect: Each candle lights only when the match touches its wick, and candles the match has not reached stay dark.
  - fail: A candle lights before the match reaches it; or the match touches a wick and it stays dark to the end of the clip; or every candle lights at once when the first is touched; or a candle at the far end lights while the match works at the near end.
- P2 [core · permanence_count]
  - expect: The candles keep their number and their places, and each keeps one wick and one flame.
  - fail: A second flame appears on one wick; or a candle vanishes; or a new candle appears in the row; or two candles merge into one.
- P3 [major · gravity_direction]
  - expect: Each flame stands upward from its wick and the wax pools at the candle's top.
  - fail: A flame points downward; or hangs below its wick; or melted wax climbs a candle's side; or a flame lies flat along the row with nothing blowing it.
- P4 [major · process_direction]
  - expect: Once lit a candle stays lit and the flames do not go out on their own.
  - fail: A lit candle goes out with nothing touching it; or a flame flickers between lit and out; or a lit flame jumps to an unlit candle; or a lit candle's wax level rises.
- P5 [fatal · shape_identity]
  - expect: The candles keep their cups and shapes and the match stays a stick; nothing passes through anything.
  - fail: A candle's cup changes shape; or the match passes through a candle; or a flame detaches from its wick and floats; or a candle turns into another object.
- P6 [minor · attribute_drift]
  - expect: The candles' colour, the surface they stand on and the surroundings stay the same.
  - fail: A candle changes colour; or the surface changes pattern; or the background changes between frames.

**Note.** Who holds the match is not judged.

## HEAT-0142 · burn_smoke · train

**Caption.** Brandy is ignited in a pan, and a sheet of flame rises above the pan and then dies down.

**Expectation (hidden).** The flame rises upward from the surface, burns for a few seconds, and shrinks away; it does not sink into the pan or come back once gone.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] A pan with brandy in it.
- S2 [core] The brandy catches fire.
- S3 [core] A sheet of flame rises above the pan.
- S4 [core] The flame dies down.
- S5 [minor] The flame covers the liquid's surface.
- S6 [minor] The order is lit, rise, die down.

**PC**
- P1 [core · gravity_direction]
  - expect: The flame stands upward from the liquid's surface and the liquid stays in the pan.
  - fail: The flame points downward into the pan's base; or hangs below the pan; or the burning liquid climbs the pan's wall and over the rim with nothing tipping it; or the flame lies flat along the hob with nothing blowing it.
- P2 [core · process_direction]
  - expect: The flame rises, burns and then shrinks away, and it does not come back once gone.
  - fail: The flame dies down and flares up again with nothing added; or sinks into the liquid and reappears; or grows steadily for the rest of the clip; or the liquid's level rises as it burns.
- P3 [major · missing_consequence]
  - expect: The flame sits on the liquid: it covers the surface and shrinks as the liquid does.
  - fail: The flame burns in the air above the pan with a gap to the liquid; or the flame burns over a dry empty pan; or the flame covers only one spot while the whole surface is alight.
- P4 [major · material_response]
  - expect: The flame is a soft low sheet that waves over the liquid and the liquid stays a thin liquid that shifts as the pan moves.
  - fail: The flame holds a fixed rigid shape; or the liquid sets solid as it burns; or the liquid stands in a heap above the rim; or the flame leaves solid pieces behind.
- P5 [fatal · permanence_count]
  - expect: One pan with its contents; the flame stays over the pan and the contents stay in it.
  - fail: The flame detaches and floats away from the pan; or a second flame appears beside the pan; or the contents pass through the pan's wall; or the pan vanishes.
- P6 [minor · attribute_drift]
  - expect: The pan, the hob and the surroundings stay the same.
  - fail: The pan changes colour; or the hob's knobs move by themselves; or items around the hob rearrange.

**Note.** How high the flame rises is not judged. Who lights the brandy is not judged.

## HEAT-0143 · burn_smoke · train

**Caption.** A magnifying glass focuses sunlight onto a dry leaf until a wisp of smoke appears and a small glowing spot begins to spread.

**Expectation (hidden).** The smoke rises from the bright spot; the dark scorched patch grows outward from that spot and does not shrink.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A magnifying glass is held over a dry leaf.
- S2 [core] A bright spot of light lies on the leaf.
- S3 [core] A wisp of smoke rises from the bright spot.
- S4 [core] A dark scorched patch appears and spreads.
- S5 [minor] The patch has a glowing edge.
- S6 [minor] The bright spot comes first, then the smoke, then the patch.

**PC**
- P1 [core · process_direction]
  - expect: The scorched patch only grows outward from the bright spot and does not shrink or lighten.
  - fail: The scorched patch shrinks; or the dark patch turns back to pale leaf; or the patch appears away from the bright spot; or the patch grows and shrinks in turn.
- P2 [core · permanence_count]
  - expect: The leaf chars where the light is focused and shrinks rather than vanishing, and the glass stays outside it.
  - fail: The leaf vanishes at a stroke while still whole; or a second leaf appears; or the glass passes into the leaf; or a hole appears in the leaf where the spot never lay.
- P3 [major · missing_consequence]
  - expect: The smoke rises from the bright spot, and the patch appears where the spot lies and follows it if it moves.
  - fail: Smoke rises from a part of the leaf the spot never reached; or the spot lies on the leaf and nothing darkens or smokes at all to the end of the clip; or the patch stays where it was while the spot moves on and the new place stays pale; or the smoke rises before any bright spot appears.
- P4 [major · gravity_direction]
  - expect: The smoke rises from the leaf and any ash falls.
  - fail: The smoke sinks and pools on the ground; or pours downward through the leaf; or ash lifts and stays aloft; or the smoke hangs as a fixed shape without rising.
- P5 [fatal · shape_identity]
  - expect: One leaf and one glass; the leaf keeps its outline apart from the burnt hole and the glass keeps its shape.
  - fail: The leaf turns into another object; or the glass bends or melts; or a second glass appears; or the leaf's stem detaches and floats.
- P6 [minor · attribute_drift]
  - expect: The leaf's colour away from the patch, the ground and the surroundings stay the same.
  - fail: The leaf changes colour away from the burn; or the ground changes texture; or the background changes between frames.

**Note.** Whoever holds the glass is not judged; the sunlight is invisible except as the bright spot.

## HEAT-0144 · burn_smoke · train

**Caption.** A wooden skewer is dropped into the grill's coals and catches fire.

**Expectation (hidden).** The skewer lights where it touches the coals, the flame runs along it, and it blackens and shrinks behind the flame; it does not return to pale wood.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A wooden skewer is dropped into a grill's coals.
- S2 [core] The skewer catches fire where it touches the coals.
- S3 [core] The flame runs along the skewer.
- S4 [core] The skewer blackens and shrinks behind the flame.
- S5 [minor] The skewer is pale wood before it catches.
- S6 [minor] The drop comes first and the catching follows.

**PC**
- P1 [core · process_direction]
  - expect: The flame only advances along the skewer from where it caught, and the blackened part stays black.
  - fail: A blackened part of the skewer turns back to pale wood; or the flame front retreats leaving unburnt wood behind it; or the skewer catches at a point no coal touched; or the skewer grows longer as it burns.
- P2 [core · permanence_count]
  - expect: The skewer shrinks to ash rather than vanishing at a stroke, and the coals keep their number.
  - fail: The skewer vanishes in a single frame while still long; or a second skewer appears; or a coal vanishes leaving no ash; or the skewer passes through the grate and out below whole.
- P3 [major · gravity_direction]
  - expect: The flame points upward from the skewer, the skewer rests on the coals, and ash settles down.
  - fail: The flame points downward under the skewer; or the skewer lifts off the coals and hangs in the air; or the ash rises and stays aloft; or the flame hangs below the coals.
- P4 [major · missing_consequence]
  - expect: The skewer catches where it touches the coals and the wood there chars first.
  - fail: The skewer catches at its far end away from the coals; or the skewer lies on glowing coals and stays pale and unmarked to the end of the clip; or the flame appears in the air beside the skewer with a gap to the wood.
- P5 [fatal · shape_identity]
  - expect: The skewer stays a straight stick as it chars and the coals stay lumps; nothing turns into anything else.
  - fail: The skewer melts and drips; or the skewer turns into another object; or the coals merge into one smooth mass; or the skewer bends into a ring.
- P6 [minor · attribute_drift]
  - expect: The grate, the coals' bed and the surroundings stay the same.
  - fail: The grate changes spacing; or the coals rearrange away from the skewer; or the background changes between frames.

## HEAT-0145 · burn_smoke · train

**Caption.** A gust blows across a row of candles on a windowsill, and the flames bend sideways and two of them go out, leaving smoke trails.

**Expectation (hidden).** All the flames lean the same way with the gust; the ones that go out smoke upward; the survivors straighten after the gust.

**Declared violation types.** causeless_motion, missing_consequence, gravity_direction

**SA**
- S1 [core] A row of candles stands on a windowsill.
- S2 [core] The flames bend sideways.
- S3 [core] Two of the flames go out.
- S4 [core] Smoke trails rise from the ones that went out.
- S5 [minor] The surviving flames straighten afterwards.
- S6 [minor] All the flames lean the same way.

**PC**
- P1 [core · causeless_motion]
  - expect: All the flames lean the same way at the same moment as the gust reaches them, and the survivors straighten when it passes.
  - fail: The flames lean in different directions at the same moment; or a flame leans against the way the others lean; or the flames stay leaning after the curtains and everything else have settled; or a flame leans while nothing else in the scene moves at all.
- P2 [core · missing_consequence]
  - expect: The flames that go out are the ones the gust flattened, and they go out during the gust.
  - fail: A flame goes out before the gust reaches it; or a flame goes out while it stands straight and untouched; or the flames go out one after another over the clip with no gust; or a flame that went out relights during the same gust.
- P3 [core · gravity_direction]
  - expect: The smoke trails rise from the wicks that went out and the surviving flames point upward between gusts.
  - fail: A smoke trail sinks down the candle and pools on the sill; or a trail pours downward off the sill; or a surviving flame points downward; or a trail hangs as a fixed shape without rising.
- P4 [major · process_direction]
  - expect: Once out a candle stays out and its smoke trail only rises and thins.
  - fail: A candle relights by itself; or a trail runs back into its wick; or a flame flickers between lit and out after the gust has passed; or a wick's glow brightens into a flame with nothing touching it.
- P5 [fatal · permanence_count]
  - expect: The candles keep their number and places and each keeps one wick; no flame detaches.
  - fail: A flame separates from its wick and floats; or a second flame appears on one wick; or a candle vanishes; or a new candle appears on the sill.
- P6 [minor · attribute_drift]
  - expect: The candles' colour, the sill and the window stay the same.
  - fail: A candle changes colour; or the sill's surface changes; or the view through the window jumps to a different place.

## HEAT-0146 · burn_smoke · train

**Caption.** A handful of dry pine needles is fed to a small fire, and they crackle and flare up brightly before the flames settle.

**Expectation (hidden).** The flare comes as the needles land and rises upward, then dies back to the size before; the needles become ash and do not reappear.

**Declared violation types.** process_direction, gravity_direction

**SA**
- S1 [core] A small fire burns.
- S2 [core] A handful of dry pine needles is dropped onto it.
- S3 [core] The flames flare up brightly.
- S4 [core] The flames settle back down.
- S5 [minor] The needles turn to ash.
- S6 [minor] The drop comes first and the flare follows.

**PC**
- P1 [core · process_direction]
  - expect: The flare comes as the needles land and dies back to the size the fire was, and the needles only char to ash.
  - fail: The flare comes before the needles land; or ash gathers back into whole needles; or the flare dies back and rises again with nothing added; or the flare keeps growing for the rest of the clip.
- P2 [core · gravity_direction]
  - expect: The flare rises upward from the fire and the ash and fragments settle down.
  - fail: The flare points downward into the fire pit; or the needles are blown upward and stay aloft as they burn; or the ash rises and stays in the air; or the flames hang below the wood.
- P3 [major · missing_consequence]
  - expect: The needles catch where they land on the flames and the flare comes from that spot.
  - fail: The needles land and nothing flares at all; or the flare rises from a part of the fire where no needles landed; or the needles sit in the flames and stay pale and whole to the end of the clip.
- P4 [major · material_response]
  - expect: The needles are fine dry stalks that curl, blacken and crumble, and the fire's logs stay solid.
  - fail: A needle melts and drips; or the needles stay straight and pale while glowing; or the needles fuse into one lump; or a log flows like a liquid.
- P5 [fatal · permanence_count]
  - expect: The needles that were dropped are the needles that burn, and the fire's logs keep their number.
  - fail: The needles vanish in mid-air before landing; or new needles appear on the fire with none dropped; or a log vanishes; or a needle passes through a log and out below.
- P6 [minor · attribute_drift]
  - expect: The fire's stones, the ground and the surroundings stay the same.
  - fail: The stones rearrange; or the ground changes texture; or the background changes between frames.

**Note.** The crackle is sound and is not judged. Who feeds the fire is not judged.

## HEAT-0147 · burn_smoke · train

**Caption.** A candle inside a glass jar has burned down to its last pool of wax, and the flame goes out.

**Expectation (hidden).** The flame is small, dies, and smoke rises from the wick; the wax does not refill and the flame does not return.

**Declared violation types.** process_direction, gravity_direction, permanence_count

**SA**
- S1 [core] A candle burns in a glass jar, down to a shallow pool of wax.
- S2 [core] The flame is small.
- S3 [core] The flame goes out.
- S4 [core] Smoke rises from the wick.
- S5 [minor] The wax does not refill.
- S6 [minor] The order is small flame, out, smoke.

**PC**
- P1 [core · process_direction]
  - expect: The flame only shrinks and goes out and does not return, and the wax's level does not rise.
  - fail: The flame relights by itself; or the flame grows large again with no more wax; or the wax pool deepens with nothing added; or the flame flickers between lit and out after it has gone.
- P2 [core · gravity_direction]
  - expect: The flame stands upward from the wick and the smoke rises after it, while the wax lies level in the jar's bottom.
  - fail: The flame points downward; or the smoke sinks inside the jar and pools; or the wax climbs the jar's wall and stays; or the smoke pours downward out of the jar.
- P3 [core · permanence_count]
  - expect: One candle in one jar; the wax only goes and the wick stays in its pool.
  - fail: A second wick appears; or the wax pool vanishes at a stroke; or a new candle appears in the jar; or the wick detaches and floats in the wax.
- P4 [major · missing_consequence]
  - expect: The light the flame cast goes with it: the jar's glass and the surface around it go dimmer as the flame dies.
  - fail: The flame goes out while its glow still lies on the table; or the room brightens as the flame dies; or the jar keeps glowing with the flame out; or a glow remains on the jar's rim.
- P5 [fatal · shape_identity]
  - expect: The jar keeps its shape and the wick stays a wick; nothing passes through the glass.
  - fail: The jar changes shape; or the glass melts or sags; or the flame passes through the glass and burns outside; or the jar turns into another object.
- P6 [minor · attribute_drift]
  - expect: The jar's label, the table and the room stay the same apart from the light.
  - fail: The label changes; or the table's pattern changes; or the wax changes colour.

## HEAT-0148 · burn_smoke · train

**Caption.** A lit match is dropped into a fire pit filled with kindling, and the fire catches and grows from the bottom up.

**Expectation (hidden).** The flames start where the match lands and spread upward through the kindling; smoke rises; the fire does not start at the top or everywhere at once.

**Declared violation types.** process_direction, gravity_direction, missing_consequence

**SA**
- S1 [core] A fire pit is filled with kindling.
- S2 [core] A lit match is dropped into it.
- S3 [core] The kindling catches where the match lands.
- S4 [core] The flames spread upward through the kindling.
- S5 [minor] Smoke rises from the pit.
- S6 [minor] The fire grows from the bottom up rather than starting at the top.

**PC**
- P1 [core · missing_consequence]
  - expect: The kindling catches at the spot the match lands and the fire spreads from there.
  - fail: The kindling catches before the match lands; or the match lands among the kindling and nothing catches at all; or the fire starts at the top of the pile while the match lies at the bottom; or the fire starts at a corner of the pit the match never reached.
- P2 [core · process_direction]
  - expect: The fire only spreads and the charred kindling stays charred.
  - fail: Charred kindling turns back to pale wood; or the flame front retreats leaving unburnt kindling behind it; or the fire catches, goes out and catches again with nothing added; or the pile grows as it burns.
- P3 [core · gravity_direction]
  - expect: The flames climb upward through the pile and the smoke rises, while embers and ash settle down.
  - fail: The flames travel downward from the top of the pile; or the smoke sinks and pools around the pit; or the flames hang below the pit's floor; or ash rises and stays aloft.
- P4 [major · material_response]
  - expect: The kindling sticks char, curl and crumble and the pile settles as they burn, while the pit stays a rigid ring.
  - fail: A stick melts and drips; or the sticks stay pale and straight while flames cover them; or the pile lifts as one solid block; or the pit's stones sag.
- P5 [fatal · permanence_count]
  - expect: The kindling in the pit is the kindling that burns and the match is one stick; nothing appears from nowhere.
  - fail: New kindling appears in the pit; or a stick vanishes leaving no ash; or a second lit match appears; or the match passes through the pit's floor.
- P6 [minor · attribute_drift]
  - expect: The pit's stones, the ground and the surroundings stay the same.
  - fail: The stones rearrange; or the ground changes texture; or the background changes between frames.

**Note.** Who drops the match is not judged.

## HEAT-0149 · burn_smoke · train

**Caption.** A candle is set beside an open window on a windy night, and its flame streams sideways and flickers wildly.

**Expectation (hidden).** The flame leans away from the window in the direction the curtain blows and dances with each gust; it never leans toward the wind.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A candle stands beside an open window.
- S2 [core] The flame streams sideways.
- S3 [core] The flame flickers.
- S4 [minor] The curtain moves the same way.
- S5 [minor] The flame leans away from the window.
- S6 [minor] The night is dark outside.

**PC**
- P1 [core · causeless_motion]
  - expect: The flame leans away from the window the same way the curtain blows, and it dances as the gusts come and go.
  - fail: The flame leans toward the window against the way the curtain blows; or the flame streams hard while the curtain hangs dead still; or the flame's direction swings about while the curtain holds steady; or the flame stays flat after the curtain has settled.
- P2 [core · gravity_direction]
  - expect: Between gusts the flame stands upward from the wick and the melted wax runs down the candle.
  - fail: The flame points downward between gusts; or hangs below the wick; or melted wax climbs the candle's side; or the flame lies flat while the curtain hangs still and nothing moves.
- P3 [major · process_direction]
  - expect: The flame stays alight through the gusts unless it is blown out, and once out it stays out.
  - fail: The flame goes out and relights by itself; or shrinks to nothing and returns with each gust; or the wick's glow brightens into a flame with no gust passing; or the flame splits into two flames.
- P4 [major · material_response]
  - expect: The flame is a soft tongue that stretches and waves and the candle's body stays solid with a wax pool at its top.
  - fail: The flame holds a fixed rigid shape as it leans; or the candle's body bends with the wind; or the flame breaks into solid pieces; or the wax pool sets hard while the flame burns in it.
- P5 [fatal · permanence_count]
  - expect: One candle with one wick and one flame; the flame stays on the wick.
  - fail: The flame separates from the wick and floats; or a second flame or candle appears; or the candle vanishes; or the wick vanishes while the flame burns on.
- P6 [minor · attribute_drift]
  - expect: The candle's colour, the curtain's pattern and the room stay the same.
  - fail: The candle changes colour; or the curtain changes pattern; or items in the room rearrange.

## HEAT-0150 · burn_smoke · train

**Caption.** A fire steel is scraped with a knife, and sparks shower onto a nest of dry tinder that begins to smoke and then flame.

**Expectation (hidden).** The sparks fall downward onto the tinder, smoke rises from where they land, and a small flame follows the smoke; nothing burns before the sparks land.

**Declared violation types.** gravity_direction, process_direction, missing_consequence

**SA**
- S1 [core] A fire steel is scraped with a knife over a nest of tinder.
- S2 [core] Sparks shower from the steel.
- S3 [core] The sparks land on the tinder.
- S4 [core] Smoke rises from where they land.
- S5 [core] A small flame follows the smoke.
- S6 [minor] Nothing burns before the sparks land.

**PC**
- P1 [core · gravity_direction]
  - expect: The sparks fly downward from the steel onto the tinder below and go dark on the way or as they land, while the smoke and flame rise from the tinder.
  - fail: The sparks rise from the steel and gather above it; or sparks hang in the air; or the smoke sinks and pools around the nest; or the flame points downward into the ground.
- P2 [core · process_direction]
  - expect: The sparks come only during the scrape, then smoke appears where they landed and a flame follows; the order does not reverse.
  - fail: The smoke appears before any spark lands; or the flame appears before any smoke; or the sparks keep flying after the knife has stopped; or the charred tinder turns back to pale dry fibre.
- P3 [core · missing_consequence]
  - expect: The smoke and flame appear at the spot the sparks landed and not elsewhere.
  - fail: The smoke rises from a part of the nest no spark reached; or the sparks land on the tinder and nothing smokes or catches at all to the end of the clip; or the flame appears in the air above the nest with a gap to the tinder; or the nest smokes while the sparks fly wide of it.
- P4 [major · material_response]
  - expect: The tinder is a nest of fine dry fibres that glows, curls and blackens, and the steel and knife stay rigid.
  - fail: The tinder melts and drips; or the fibres stay pale and straight while glowing; or the nest lifts as one solid block; or the knife bends as it scrapes.
- P5 [fatal · permanence_count]
  - expect: One steel, one knife and one nest; the sparks come from the steel and the tinder chars rather than vanishing.
  - fail: Sparks appear in the air far from the steel; or the nest vanishes at a stroke while still whole; or a second steel appears; or the knife passes through the steel.
- P6 [minor · attribute_drift]
  - expect: The ground, the steel's handle and the surroundings stay the same.
  - fail: The steel's handle changes colour; or the ground changes texture; or the background changes between frames.

**Note.** Whoever scrapes the steel is not judged.

## HEAT-0151 · burn_smoke · train

**Caption.** A glass jar is lowered over a burning tea light on a plate, and the flame shrinks and goes out within seconds, leaving a wisp of smoke inside the jar.

**Expectation (hidden).** The flame gets smaller and dimmer after the jar comes down and then dies; the smoke rises and hangs inside the jar; the flame does not keep burning at full size or relight.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A tea light burns on a plate.
- S2 [core] A glass jar is lowered over it.
- S3 [core] The flame shrinks and dims.
- S4 [core] The flame goes out.
- S5 [minor] A wisp of smoke hangs inside the jar.
- S6 [minor] The jar's rim rests on the plate.

**PC**
- P1 [core · missing_consequence]
  - expect: The flame shrinks after the jar comes down over it and then goes out.
  - fail: The flame burns at full size under the closed jar to the end of the clip; or the flame shrinks before the jar reaches it; or the flame goes out with the jar still held well clear; or the flame grows as the jar comes down.
- P2 [core · process_direction]
  - expect: The flame only shrinks and goes out under the jar and does not relight while the jar stays down; the smoke inside only thins or hangs.
  - fail: The flame relights under the closed jar; or the flame shrinks and grows in turn under the jar; or the smoke inside clears and the flame returns; or the wick's glow brightens into a flame with the jar down.
- P3 [major · gravity_direction]
  - expect: The smoke rises from the wick inside the jar and gathers at its top, and the candle stays on the plate.
  - fail: The smoke sinks to the plate and pools under the wick; or pours downward out through the plate; or the candle lifts inside the jar and hangs; or the smoke hangs as a fixed shape without rising.
- P4 [major · material_response]
  - expect: The jar stays a rigid clear glass over the candle and the candle keeps its shape with a wax pool at its top.
  - fail: The jar melts or sags over the flame; or the glass ripples as the flame dies; or the candle's body slumps as the jar comes down; or the jar sticks to the flame and lifts with it.
- P5 [fatal · solidity]
  - expect: The jar's rim sits on the plate and the candle stays inside it; nothing passes through the glass.
  - fail: The smoke passes out through the glass and rises outside the jar; or the jar passes through the plate; or the candle passes through the jar's wall; or a second jar appears.
- P6 [minor · attribute_drift]
  - expect: The plate, the candle's cup and the surroundings stay the same.
  - fail: The plate changes pattern; or the candle's cup changes colour; or items around the plate rearrange.

**Note.** Who lowers the jar is not judged.

## HEAT-0152 · burn_smoke · train

**Caption.** A slice of bread sits in a running toaster, and its top edge darkens and thin smoke begins to rise from the slots.

**Expectation (hidden).** The darkening deepens over time and never lightens; smoke rises from the slots only after the bread has darkened; the bread does not turn pale again.

**Declared violation types.** process_direction, attribute_drift

**SA**
- S1 [core] A slice of bread sits in a toaster.
- S2 [core] The bread's top edge darkens.
- S3 [core] Thin smoke rises from the toaster's slots.
- S4 [minor] The darkening deepens over time.
- S5 [minor] The smoke comes after the bread has darkened.

**PC**
- P1 [core · process_direction]
  - expect: The darkening only deepens and the bread does not turn pale again, and the smoke only rises once the bread has begun to darken.
  - fail: A darkened part of the bread turns pale again; or the darkening spreads and then shrinks; or the smoke rises while the bread is still pale all over; or the darkening jumps from one edge of the bread to the other.
- P2 [core · attribute_drift]
  - expect: The change is in the bread where the heat reaches it, deepest at the edge nearest the element, and the toaster's shell stays as it was.
  - fail: The toaster's shell darkens rather than the bread; or the bread darkens evenly right through including the part standing clear of the slot; or the bread lightens at the edge nearest the element; or the crumbs in the tray change colour rather than the bread.
- P3 [major · gravity_direction]
  - expect: The smoke rises out of the slots, spreading and thinning.
  - fail: The smoke pours down the toaster's sides and pools on the counter; or sinks below the toaster; or hangs as a fixed shape without rising; or pours downward through the slots.
- P4 [major · missing_consequence]
  - expect: The smoke comes out of the slot where the bread sits and not from the toaster's base or sides.
  - fail: The smoke comes from the toaster's base; or the bread chars black while no smoke leaves the slots at all; or the smoke leaves an empty slot while the bread is in the other.
- P5 [fatal · permanence_count]
  - expect: One slice in one toaster; the slice stays one slice and the toaster keeps its shape.
  - fail: A second slice appears; or the slice vanishes; or the slice passes through the toaster's shell; or the toaster changes shape.
- P6 [minor · attribute_drift]
  - expect: The toaster's finish, its controls and the counter stay the same.
  - fail: The toaster changes colour; or its lever moves to a different place; or items on the counter rearrange.

**Note.** The browning of the bread is chemistry; what is judged is that the darkening runs one way and starts where the heat reaches it.

## HEAT-0153 · burn_smoke · train

**Caption.** The vents on a charcoal grill's bowl are slid shut, and the bright orange coals dim to a dull glow.

**Expectation (hidden).** The glow fades gradually after the vents close and does not flare back up while they stay shut; the coals do not brighten or go dark in a single frame.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] A charcoal grill with glowing coals and vents on its bowl.
- S2 [core] The vents are slid shut.
- S3 [core] The coals' glow fades.
- S4 [core] The coals end at a dull glow.
- S5 [minor] The coals are bright orange before the vents close.
- S6 [minor] The order is bright, vents shut, dimmer.

**PC**
- P1 [core · missing_consequence]
  - expect: The glow begins to fade after the vents are slid shut and not before.
  - fail: The glow fades before the vents are touched; or the vents are shut and the coals stay bright orange to the end of the clip; or the coals brighten after the vents are shut; or the glow fades while the vents are being opened.
- P2 [core · process_direction]
  - expect: The fade runs one way while the vents stay shut and the coals do not flare back up.
  - fail: The coals flare up again with the vents still shut; or the glow fades and brightens in turn; or the coals go dark in a single frame; or the ash gathers back into unburnt charcoal.
- P3 [major · gravity_direction]
  - expect: Any smoke from the coals rises and escapes where it can, and ash settles down in the bowl.
  - fail: The smoke sinks into the bowl and pools; or pours downward out of the grill's base; or ash rises and stays aloft; or the smoke hangs as a fixed shape without rising.
- P4 [major · material_response]
  - expect: The coals stay hard lumps that dull and crust with ash, and the vents stay rigid sliding plates.
  - fail: A coal melts or flows; or the coals swell as they dim; or a vent bends as it is slid; or the ash holds a rigid shape when the grill is knocked.
- P5 [fatal · permanence_count]
  - expect: The coals keep their number in the bowl, dulling rather than vanishing, and the vents stay on the grill.
  - fail: A coal vanishes leaving no ash; or new coals appear with none added; or a vent vanishes; or the bowl changes shape.
- P6 [minor · attribute_drift]
  - expect: The grill's body, its legs and the surroundings stay the same.
  - fail: The grill changes colour; or a leg changes shape; or items around the grill rearrange.

**Note.** How far the glow has faded by the end of the clip is not judged, only that it fades one way after the vents shut.

## HEAT-0154 · burn_smoke · train

**Caption.** A sheet of paper rests on a wire rack above a burning candle, and a brown spot forms over the flame, then a hole burns through with a glowing edge spreading outward.

**Expectation (hidden).** The brown patch appears first and darkens, the hole opens at its centre and grows outward with a glowing rim and thin smoke; the hole does not shrink and the paper does not turn white again.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A sheet of paper rests on a wire rack above a burning candle.
- S2 [core] A brown spot forms on the paper over the flame.
- S3 [core] The spot darkens.
- S4 [core] A hole opens at its centre.
- S5 [minor] The hole grows with a glowing rim.
- S6 [minor] Thin smoke rises from the spot.

**PC**
- P1 [core · process_direction]
  - expect: The brown spot only darkens, the hole only grows and the paper does not turn white again.
  - fail: The brown spot fades back to white paper; or the hole closes up; or the hole grows and shrinks in turn; or the glowing rim travels inward and the hole fills in behind it.
- P2 [core · permanence_count]
  - expect: The paper chars and burns away at the hole rather than vanishing all at once, and no new paper appears.
  - fail: The whole sheet vanishes in a single frame; or a second sheet appears; or a hole appears in a part of the paper away from the flame; or the sheet grows larger as it burns.
- P3 [major · missing_consequence]
  - expect: The spot and the hole form directly over the flame and the paper away from the flame stays white.
  - fail: The spot forms at a corner of the sheet away from the flame; or the flame plays under the paper and it stays white and unmarked to the end of the clip; or the paper browns evenly all over while the flame sits under one spot.
- P4 [major · gravity_direction]
  - expect: The smoke rises from the spot, any charred flakes fall, and the flame points upward at the paper.
  - fail: The smoke sinks through the rack and pools; or charred flakes rise and stay aloft; or the flame points downward away from the paper; or the smoke pours downward out of the hole.
- P5 [fatal · shape_identity]
  - expect: One sheet on one rack over one candle; the paper stays paper as it chars and the rack stays rigid.
  - fail: The paper melts and drips; or the paper turns into another material as it burns; or the rack's wires bend or melt; or the candle passes through the rack.
- P6 [minor · attribute_drift]
  - expect: The rack, the candle's holder and the surroundings stay the same.
  - fail: The rack changes spacing; or the holder changes colour; or items around the rack rearrange.

## HEAT-0155 · burn_smoke · train

**Caption.** A struck match stands upright in a holder and burns down, the flame creeping down the stick as the burnt part above it blackens and curls.

**Expectation (hidden).** The flame moves downward along the stick, the wood behind it turns black and bends, and the flame shrinks as it nears the base; the burnt part does not turn pale again and the flame does not climb back up.

**Declared violation types.** process_direction, shape_identity

**SA**
- S1 [core] A struck match stands upright in a holder.
- S2 [core] The flame moves down the stick.
- S3 [core] The part of the stick above the flame is blackened.
- S4 [core] The blackened part curls.
- S5 [minor] The flame shrinks as it nears the base.
- S6 [minor] The burnt part stays black.

**PC**
- P1 [core · process_direction]
  - expect: The flame only travels downward along the stick and the wood it has passed stays black.
  - fail: The flame climbs back up the stick; or a blackened part turns back to pale wood; or the flame jumps to a new place on the stick; or the burnt part straightens and lightens.
- P2 [core · shape_identity]
  - expect: The burnt stick stays a thin stick that blackens and bends and does not turn into another material.
  - fail: The burnt stick melts and drips; or the stick turns into another object; or the burnt part swells into a lump; or the stick stretches longer as it burns.
- P3 [major · gravity_direction]
  - expect: The flame points upward from the burning point whatever the stick's angle, and ash falls.
  - fail: The flame points downward from the burning point; or hangs below the stick; or ash rises and stays aloft; or the flame lies flat against the stick with nothing blowing it.
- P4 [major · missing_consequence]
  - expect: The flame is at the boundary between the black part and the pale part and moves with it.
  - fail: The flame burns in the middle of the pale part with black wood beyond it; or the flame burns above the blackened part on fresh wood; or the black part grows while the flame stays fixed at the head; or the flame burns with no blackening behind it at all.
- P5 [fatal · permanence_count]
  - expect: One match in one holder; the match shortens only by burning and stays in the holder.
  - fail: A second flame appears on the stick; or a new match appears in the holder; or the flame detaches and floats; or the match passes through the holder.
- P6 [minor · attribute_drift]
  - expect: The holder, the surface it stands on and the surroundings stay the same.
  - fail: The holder changes shape; or the surface changes pattern; or the background changes between frames.

## HEAT-0156 · burn_smoke · train

**Caption.** A metal spoon rests across a stand with its bowl just above a candle flame, and black soot builds up on the underside where the flame touches.

**Expectation (hidden).** The black patch appears only where the flame licks the metal and grows darker and wider over time; it does not appear elsewhere on the spoon or fade while the flame is there.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A metal spoon rests across a stand with its bowl above a candle flame.
- S2 [core] A black patch appears on the spoon's underside.
- S3 [core] The patch grows darker and wider.
- S4 [minor] The patch is where the flame licks the metal.
- S5 [minor] The rest of the spoon stays bright.

**PC**
- P1 [core · missing_consequence]
  - expect: The black patch appears only where the flame touches the metal and grows from there.
  - fail: The patch appears on the spoon's handle away from the flame; or the flame licks the spoon and its underside stays bright to the end of the clip; or the patch appears on the spoon's upper face while its underside stays clean; or the whole spoon blackens evenly while the flame licks one spot.
- P2 [core · process_direction]
  - expect: The patch only darkens and widens and does not fade while the flame plays on it.
  - fail: The black patch fades back to bright metal with the flame still under it; or the patch shrinks; or the patch darkens and lightens in turn; or the soot lifts off by itself and leaves the metal clean.
- P3 [major · gravity_direction]
  - expect: The flame points upward at the spoon's bowl and any smoke rises past it.
  - fail: The flame points downward away from the spoon; or hangs below the candle; or the smoke sinks and pools under the spoon; or the smoke pours downward from the spoon's underside.
- P4 [major · material_response]
  - expect: The spoon stays rigid metal that takes the soot as a loose black film, and the candle keeps its shape with a wax pool.
  - fail: The spoon sags or melts over the flame; or the spoon's metal bubbles; or the soot sets as a hard shell that keeps the spoon's shape once the spoon moves away; or the candle's body slumps as a whole.
- P5 [fatal · permanence_count]
  - expect: One spoon on one stand over one candle; the spoon stays in place and the candle stays below it.
  - fail: A second spoon appears; or the spoon vanishes; or the spoon passes through the stand; or the flame detaches from the wick and floats up to the spoon.
- P6 [minor · attribute_drift]
  - expect: The stand, the candle's holder and the surroundings stay the same.
  - fail: The stand changes shape; or the holder changes colour; or items around the stand rearrange.

## HEAT-0157 · burn_smoke · train

**Caption.** A burning log in a fireplace cracks with a pop, and a few sparks jump out onto the hearth and go dark.

**Expectation (hidden).** The sparks leave the log at the pop, fly outward and downward, and fade within a second or two of landing; they do not rise to the ceiling or keep glowing on the stone.

**Declared violation types.** trajectory_momentum, process_direction

**SA**
- S1 [core] A log burns in a fireplace.
- S2 [core] The log cracks.
- S3 [core] A few sparks jump out of the fire onto the hearth.
- S4 [core] The sparks go dark.
- S5 [minor] The sparks leave the log at the crack.
- S6 [minor] The crack comes first and the sparks follow.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The sparks leave the log at the crack, fly outward and downward along arcs and land on the hearth.
  - fail: The sparks rise straight up and stay aloft; or fly out from a point away from the crack; or curve back into the fire after leaving it; or travel in straight lines and stop dead in mid-air.
- P2 [core · process_direction]
  - expect: The sparks fade within a moment of landing and do not brighten again, and the crack in the log stays open.
  - fail: A landed spark brightens again and burns on the stone; or the crack closes and the log is whole again; or the sparks keep glowing on the hearth for the rest of the clip; or sparks keep jumping out with no further crack.
- P3 [major · gravity_direction]
  - expect: The sparks arc downward after leaving the log and settle on the hearth, and the flames point upward.
  - fail: The sparks rise and gather at the chimney's mouth; or hang in the air above the hearth; or the flames point downward; or a landed spark lifts off the stone by itself.
- P4 [major · material_response]
  - expect: The log is charred wood that splits along a crack and the sparks are small hot fragments that dull, while the hearth stays hard stone.
  - fail: The log bends instead of cracking; or the log melts and drips; or a spark bounces high off the stone like a rubber ball; or the hearth's stone dents where sparks land.
- P5 [fatal · permanence_count]
  - expect: The sparks come from the log and go dark rather than vanishing while bright, and the logs keep their number.
  - fail: Sparks appear on the hearth with none leaving the fire; or a spark vanishes at a stroke while still bright; or a log vanishes; or a second log appears already burning.
- P6 [minor · attribute_drift]
  - expect: The hearth's stone, the fireplace's surround and the room stay the same.
  - fail: The hearth changes colour; or the surround changes shape; or items in the room rearrange.

**Note.** The pop is sound and is not judged; the crack is read from the log splitting.

## HEAT-0158 · burn_smoke · train

**Caption.** A lit candle in a holder is tilted to one side, and the flame keeps pointing straight up while melted wax runs down the low side.

**Expectation (hidden).** The flame stays vertical whatever the candle's angle and the wax runs down the lower edge and drips off it; the flame does not lean with the candle and the wax does not run uphill.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] A lit candle in a holder is tilted to one side.
- S2 [core] The flame keeps pointing straight up.
- S3 [core] Melted wax runs down the candle's low side.
- S4 [minor] The wax drips off the low edge.
- S5 [minor] The flame does not lean with the candle.
- S6 [minor] The tilt comes first and the running follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The flame stays upright whatever the candle's angle and the melted wax runs down the low side and drips from its lowest point.
  - fail: The flame leans with the candle and stays in line with the wick; or the wax runs up toward the candle's high side; or a drip leaves the candle and rises; or the wax gathers on the high side and stays there.
- P2 [core · missing_consequence]
  - expect: The tilt shows in the wax: the pool at the top runs toward the low side and spills there.
  - fail: The candle tilts and the wax pool stays square with the candle's top instead of level with the ground; or the wax pool spills over the high side; or the candle tilts and no wax moves at all; or wax runs down a side the candle is not tilted toward.
- P3 [major · process_direction]
  - expect: The run only advances down the low side and stops where it sets, and set wax stays set.
  - fail: A set run turns liquid again with no fresh wax reaching it; or the run retreats up the candle; or the candle grows taller as the wax runs; or the run advances and withdraws in turn.
- P4 [major · material_response]
  - expect: The wax is a thin liquid near the flame that stiffens into a dull ridge lower down, and the candle's body stays a solid column.
  - fail: The candle's body bends with the tilt; or the wax runs off as thin as water and leaves no ridge; or the run sets as a spike standing out sideways; or the candle melts through at its middle.
- P5 [fatal · permanence_count]
  - expect: One candle with one wick and one flame in one holder; the flame stays on the wick.
  - fail: The flame separates from the wick and floats; or a second flame appears; or the candle vanishes; or wax appears below with no run reaching it.
- P6 [minor · attribute_drift]
  - expect: The candle's colour, the holder and the surface below stay the same.
  - fail: The candle changes colour; or the holder changes shape; or the surface below changes pattern.

## HEAT-0159 · heat_response · train

**Caption.** Dumplings that have cooked in a pot of boiling water bob up to the surface one by one.

**Expectation (hidden).** The dumplings rise one by one from the bottom and stay bobbing at the surface; none sinks again once up.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] A pot of boiling water: bubbles or steam are visible.
- S2 [core] Dumplings are in the water.
- S3 [core] At least one dumpling rises from below to the surface during the clip.
- S4 [minor] Dumplings that have risen float and bob at the surface.
- S5 [minor] They surface one by one, at different moments, not all together.

**PC**
- P1 [core · gravity_direction]
  - expect: A dumpling that rises comes up from below, reaches the surface and stays there, partly submerged and bobbing; dumplings still cooking stay down.
  - fail: A dumpling that has surfaced goes back down to the bottom; or hangs motionless in mid-water; or rises out of the water into the air; or sits wholly on top of the water like a ball on a sheet.
- P2 [core · process_direction]
  - expect: The change is one way and staggered: the number of dumplings at the surface only grows, and they arrive at different moments. Bobbing at the surface is small up-and-down motion, not sinking.
  - fail: The same dumpling alternates between the bottom and the surface; or the count at the surface drops with none removed; or all rise at exactly the same instant like a block.
- P3 [major · material_response]
  - expect: The dumplings stay whole, soft-edged parcels that jostle in the boiling water; bubbles rise around them.
  - fail: A dumpling dissolves or bursts into liquid; or dumplings bounce off the water surface like balls; or the water surface holds them up like a solid sheet.
- P4 [major · causeless_motion]
  - expect: Dumplings move only by rising or drifting with the rolling water; they do not dart or swap places.
  - fail: A dumpling shoots across the pot; or spins fast; or jumps out of the water with nothing lifting it.
- P5 [fatal · permanence_count]
  - expect: The dumplings visible at the end are the ones that were in the pot; none appears from nothing, merges or passes through the pot.
  - fail: A dumpling pops into existence in open water or in the air; or two dumplings merge into one; or a dumpling vanishes mid-frame; or a dumpling passes through the pot wall.
- P6 [minor · attribute_drift]
  - expect: The pot, stove and dumpling colours stay the same apart from gradual cooking changes.
  - fail: The pot changes size or colour; or the dumplings change colour instantly; or the stove knobs change.

**Note.** The caption does not say the dumplings are dropped in; the clip may open with them already submerged, and a clip with no drop and no sinking phase passes SA. Bobbing (small up-and-down while staying at the top) is not sinking.

## HEAT-0160 · heat_response · train

**Caption.** Popcorn kernels in a covered pot with hot oil begin to pop, jumping and turning into fluffy white pieces that fill the pot.

**Expectation (hidden).** Each kernel bursts suddenly into a much larger piece and jumps; the pot fills from the bottom up; popped pieces do not shrink back into kernels.

**Declared violation types.** process_direction, permanence_count, shape_identity

**SA**
- S1 [core] A pot with kernels in oil is shown, seen through a clear lid or from inside.
- S2 [core] Kernels pop: they change into fluffy white pieces.
- S3 [core] Popping pieces jump.
- S4 [core] The pot fills with popcorn as popping continues.
- S5 [minor] The pot is covered with a lid.
- S6 [minor] Kernels come first and the popped pieces accumulate afterwards.

**PC**
- P1 [core · process_direction]
  - expect: The transformation is one way: kernel to popped piece, popped pieces stay popped, and the amount of popcorn only increases.
  - fail: A popped piece shrinks back into a kernel; or pieces vanish so the pot empties again; or popping stops and starts with the pot emptying in between.
- P2 [core · shape_identity]
  - expect: Each pop is an abrupt change at the kernel from a small hard grain to a much larger irregular white puff; unpopped kernels stay small and dark until they pop.
  - fail: Kernels swell gradually and smoothly like balloons; or popped pieces turn back yellow and smooth; or the popcorn forms one continuous mass rather than separate pieces.
- P3 [major · gravity_direction]
  - expect: Pieces that jump come down again onto the pile or the pot floor; the pot fills from the bottom up.
  - fail: Pieces hang in the air; or gather at the lid while the bottom is empty; or rise steadily and stay up.
- P4 [major · material_response]
  - expect: The kernels are solid grains and the oil a thin liquid; the lid stays rigid and at most rattles.
  - fail: Kernels melt or dissolve into the oil; or the popped mass flows and settles level like a liquid; or the lid bends like cloth.
- P5 [fatal · permanence_count]
  - expect: Popcorn appears only from kernels in the pot; the pot and lid keep their shape and nothing passes through them.
  - fail: Popped pieces appear outside the pot with the lid on; or the pot changes shape or size; or pieces pass through the lid or wall; or the kernel count grows with none added.
- P6 [minor · attribute_drift]
  - expect: The pot, the lid handle and the stove stay the same; popcorn stays white to pale yellow.
  - fail: The pot changes colour; or the popcorn turns a different colour; or the stove background changes.

## HEAT-0161 · heat_response · train

**Caption.** Chestnuts roast in a pan over a fire, and their shells split open with a crack.

**Expectation (hidden).** Each shell cracks along a line and gapes open, the nut inside showing; the split does not close again.

**Declared violation types.** process_direction, shape_identity

**SA**
- S1 [core] Chestnuts sit in a pan over a fire.
- S2 [core] A shell splits open.
- S3 [core] The split gapes open.
- S4 [minor] The nut inside shows through the split.
- S5 [minor] The split does not close again.

**PC**
- P1 [core · process_direction]
  - expect: Each split only opens wider and stays open.
  - fail: A split closes and the shell is whole again; or a split narrows; or the shell splits and forms again; or a split opens and shuts in turn.
- P2 [core · shape_identity]
  - expect: The shell stays a hard shell that cracks along a line and gapes, and the nut inside stays a nut.
  - fail: The shell melts and drips; or the shell squashes flat instead of cracking; or the whole chestnut turns into another object; or the shell stretches as it splits.
- P3 [major · gravity_direction]
  - expect: The chestnuts rest in the pan and any that jump come back down into it, and the flames point upward.
  - fail: A chestnut leaps out of the pan and hangs in the air; or a chestnut rises and stays above the pan; or the flames point downward under the pan; or a chestnut falls upward out of the pan.
- P4 [major · causeless_motion]
  - expect: The chestnuts shift only as they are shaken, as they split or as the pan is moved.
  - fail: A chestnut slides across the pan with the pan still and no split; or a chestnut spins fast on the spot; or the chestnuts arrange themselves into a pattern; or the pan slides on the fire with nothing touching it.
- P5 [fatal · permanence_count]
  - expect: The chestnuts keep their number in the pan and a split shell stays with its nut.
  - fail: A chestnut vanishes; or a new chestnut appears in the pan; or a nut leaves its shell and the shell vanishes; or a chestnut passes through the pan's floor.
- P6 [minor · attribute_drift]
  - expect: The pan, the fire's wood and the surroundings stay the same.
  - fail: The pan changes colour; or the pan's holes change pattern; or items around the fire rearrange.

**Note.** The crack is sound and is not judged; the split is read from the shell opening. The shells darkening as they roast is chemistry and is not judged.

## HEAT-0162 · heat_response · train

**Caption.** A plastic spoon left resting on the rim of a hot frying pan droops and bends over the edge.

**Expectation (hidden).** The spoon softens only where it touches the hot rim and sags downward under its own weight; it does not straighten while still hot.

**Declared violation types.** material_response, gravity_direction, process_direction

**SA**
- S1 [core] A plastic spoon rests on the rim of a frying pan.
- S2 [core] The spoon softens where it touches the rim.
- S3 [core] The spoon droops over the edge.
- S4 [minor] The spoon is straight at the start.
- S5 [minor] The spoon bends at the point of contact rather than along its whole length.
- S6 [minor] The softening comes first and the drooping follows.

**PC**
- P1 [core · material_response]
  - expect: The spoon goes from a stiff stick to a soft one that bends at the heated spot and hangs, keeping its plastic look.
  - fail: The spoon shatters into pieces; or runs off the pan as a liquid; or stays perfectly rigid while bent at a sharp angle with nothing holding it; or stretches like elastic along its whole length.
- P2 [core · gravity_direction]
  - expect: The softened part bends downward under the spoon's own weight, its free end hanging lower.
  - fail: The spoon bends upward away from the pan; or the free end rises; or the spoon bends sideways with nothing pushing it; or the spoon lifts off the rim and hangs in the air.
- P3 [core · process_direction]
  - expect: The droop only deepens while the spoon rests on the hot rim and the spoon does not straighten again.
  - fail: The spoon straightens while still on the hot rim; or the droop deepens and eases in turn; or the spoon droops before it touches the pan; or the bend moves along the spoon to a part away from the rim.
- P4 [major · missing_consequence]
  - expect: The bend forms where the spoon touches the hot rim and the part away from the pan stays stiff.
  - fail: The spoon bends at a point well away from the pan; or the spoon droops from the end resting on the cool counter; or the whole spoon softens evenly while only its middle touches the rim.
- P5 [fatal · permanence_count]
  - expect: One spoon on one pan; the spoon stays one piece and does not pass through the pan.
  - fail: The spoon breaks into two pieces that both stay whole; or a second spoon appears; or the spoon sinks into the pan's metal; or the spoon vanishes.
- P6 [minor · attribute_drift]
  - expect: The spoon's colour, the pan and the hob stay the same.
  - fail: The spoon changes colour; or the pan changes colour; or items around the hob rearrange.

## HEAT-0163 · heat_response · train

**Caption.** A strip of tissue paper is held above a hot radiator, and it lifts and flutters upward in the warm air.

**Expectation (hidden).** The strip rises and dances only above the radiator and hangs still when moved away; it does not fall straight down over the heat.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A strip of tissue paper is held above a radiator.
- S2 [core] The strip lifts.
- S3 [core] The strip flutters.
- S4 [minor] The strip hangs still when it is held away from the radiator.
- S5 [minor] The strip rises rather than hanging straight down.

**PC**
- P1 [core · causeless_motion]
  - expect: The strip lifts and dances only while it is over the radiator and hangs still when held away from it.
  - fail: The strip flutters while held well away from the radiator with nothing else moving; or the strip hangs dead still directly over the radiator; or the strip flutters before it is brought over the radiator; or the strip keeps dancing after it has been taken away and held elsewhere.
- P2 [core · gravity_direction]
  - expect: Over the radiator the strip is carried upward and its free end rises; away from it the strip hangs downward.
  - fail: The strip hangs straight down while directly over the radiator; or the strip is pushed downward toward the radiator; or the strip lifts while held below the radiator; or the strip stands out stiffly sideways with nothing blowing it.
- P3 [major · material_response]
  - expect: The strip is a limp light sheet that ripples along its length and folds over.
  - fail: The strip stays a rigid flat board as it rises; or stretches as it lifts; or holds a fixed wave shape frozen in place; or stands stiff like a wire.
- P4 [major · missing_consequence] (if: Other light items such as dust, a curtain or a second strip are in the rising air.)
  - expect: Other light things in the rising air over the radiator stir too, and the strip's flutter is strongest where the air leaves the radiator.
  - fail: The strip flutters hard while dust or a curtain right beside it hangs dead still; or the flutter is strongest far out to the side of the radiator; or the strip stirs while nothing else in the rising air does.
- P5 [fatal · permanence_count]
  - expect: One strip; it stays one piece and does not pass through the radiator.
  - fail: The strip vanishes; or a second strip appears; or the strip passes through the radiator's fins; or the strip merges with the curtain.
- P6 [minor · attribute_drift]
  - expect: The radiator's paint, the wall and the room stay the same.
  - fail: The radiator changes colour; or the wall changes colour; or items in the room rearrange.

**Note.** Whoever holds the strip is not judged.

## HEAT-0164 · heat_response · train

**Caption.** A hot oven door is opened, and the air above the opening shimmers and wavers.

**Expectation (hidden).** The shimmer rises out of the oven and is strongest directly above the opening, fading with height; it does not flow down toward the floor.

**Declared violation types.** process_direction, gravity_direction

**SA**
- S1 [core] An oven door is opened.
- S2 [core] The air above the opening shimmers.
- S3 [core] The shimmer wavers.
- S4 [minor] The shimmer is strongest just above the opening.
- S5 [minor] The shimmer fades with height.
- S6 [minor] The opening comes first and the shimmer follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The shimmer rises out of the oven's mouth and fades with height; it does not flow down toward the floor.
  - fail: The shimmer flows down the oven door and pools on the floor; or sinks below the opening; or pours downward out of the oven; or hangs as a fixed band without rising.
- P2 [core · process_direction]
  - expect: The shimmer appears as the door opens and eases as the oven cools, and the wavering keeps moving upward and outward.
  - fail: The shimmer appears before the door has moved; or runs back into the oven; or thickens steadily after the door has been shut; or the wavering freezes into a fixed pattern.
- P3 [major · missing_consequence]
  - expect: The shimmer sits above the open mouth and things seen through it waver, while the view away from the mouth stays steady.
  - fail: The shimmer appears above a closed part of the oven; or the view through the shimmer stays perfectly steady; or the whole room wavers while the shimmer sits over the mouth; or the shimmer appears with the door still shut.
- P4 [major · causeless_motion]
  - expect: The oven and the things around it stay put; only the air above the mouth moves.
  - fail: The door swings further open or shuts by itself; or items on the hob jump as the door opens; or the oven shifts; or the racks inside slide out by themselves.
- P5 [fatal · permanence_count]
  - expect: One oven with one door; the contents of the oven are the same as the door opens.
  - fail: Food in the oven appears or vanishes; or a rack vanishes; or the door passes through the oven's frame; or the oven changes shape.
- P6 [minor · attribute_drift]
  - expect: The oven's front, its controls and the kitchen stay the same.
  - fail: The oven changes colour; or the controls rearrange; or items in the kitchen rearrange.

## HEAT-0165 · heat_response · train

**Caption.** Wet chicken pieces are dropped into a pan of hot oil, and the oil spits and crackles violently for a moment.

**Expectation (hidden).** The spitting starts the instant the wet food touches the oil, throws droplets upward and outward, and eases as the surface water is gone.

**Declared violation types.** process_direction, trajectory_momentum

**SA**
- S1 [core] A pan of hot oil.
- S2 [core] Wet chicken pieces are dropped into the oil.
- S3 [core] The oil spits: droplets fly up and out.
- S4 [core] The spitting eases.
- S5 [minor] The pieces look wet as they go in.
- S6 [minor] The drop comes first and the spitting follows.

**PC**
- P1 [core · process_direction]
  - expect: The spitting starts as the wet pieces touch the oil, is fiercest at first and then eases.
  - fail: The oil spits before the pieces reach it; or the spitting grows steadily for the rest of the clip; or the spitting stops and then starts again with nothing added; or the oil lies glassy still as the wet pieces enter.
- P2 [core · trajectory_momentum]
  - expect: The droplets leave the oil's surface where the pieces landed, fly up and out along arcs and fall back onto the pan or the hob.
  - fail: The droplets rise and hang in the air; or fly out in straight lines and stop dead; or leave the pan from a spot no piece landed in; or curve back into the oil along the line they left on.
- P3 [major · gravity_direction]
  - expect: The pieces sink or ride in the oil, the thrown droplets arc down again and any steam rises.
  - fail: A piece rises out of the oil and hangs above it; or the droplets keep climbing out of view; or the steam sinks over the rim and pools on the hob; or the oil climbs the pan's wall and stays above its level.
- P4 [major · material_response]
  - expect: The oil is a thin liquid that bursts into fine droplets and foam and closes round the pieces, and the pieces stay firm.
  - fail: The oil sets solid as the pieces enter; or a piece melts away into the oil; or the droplets hold their shape as solid beads on the hob; or the foam stands as a rigid dome above the pan.
- P5 [fatal · permanence_count]
  - expect: The pieces in the pan are the pieces that were dropped and the oil stays in the pan.
  - fail: A piece vanishes; or new pieces appear with none added; or oil passes through the pan's wall; or the oil's level jumps with nothing added.
- P6 [minor · attribute_drift]
  - expect: The pan, the hob and the oil's colour stay the same.
  - fail: The pan changes colour; or the oil changes colour; or items around the hob rearrange.

**Note.** The chicken browning as it cooks is chemistry and is not judged.

## HEAT-0166 · heat_response · train

**Caption.** A marshmallow in a microwave swells to several times its size and then collapses when the door opens.

**Expectation (hidden).** It puffs up gradually while heating and sinks back into a sticky blob once the heat stops; it does not stay puffed.

**Declared violation types.** process_direction, shape_identity

**SA**
- S1 [core] A marshmallow sits in a microwave.
- S2 [core] The marshmallow swells.
- S3 [core] The marshmallow grows to several times its size.
- S4 [core] The door is opened.
- S5 [core] The marshmallow collapses into a sticky blob.
- S6 [minor] The swelling comes first and the collapse follows.

**PC**
- P1 [core · process_direction]
  - expect: The marshmallow only swells while the microwave runs and only collapses after the heat stops; it does not swell again with the door open.
  - fail: The marshmallow shrinks while the microwave still runs; or it swells again after the door is open with nothing running; or the swelling and collapsing repeat with the door open; or it collapses before the door has moved.
- P2 [core · shape_identity]
  - expect: The marshmallow stays one mass of foam as it swells, its surface stretching, and it slumps into a lower wider blob when it collapses.
  - fail: The marshmallow keeps its sharp cylinder edges while several times its size; or it swells into a smooth sphere with a hard shell; or it splits into separate marshmallows as it swells; or it turns into another object.
- P3 [major · gravity_direction]
  - expect: The swollen marshmallow slumps downward when it collapses and stays on the plate.
  - fail: The marshmallow lifts off the plate as it swells and hangs in the air; or it collapses upward into a tall spike; or it rises when the door opens; or it slumps sideways off the plate with nothing pushing it.
- P4 [major · material_response]
  - expect: The marshmallow behaves as a softening foam: it stretches, goes glossy and stays sticky and slack after collapsing.
  - fail: The marshmallow shatters when it collapses; or snaps back to its first firm shape; or runs off the plate as a thin liquid; or bounces on the plate like rubber.
- P5 [fatal · permanence_count]
  - expect: One marshmallow on one plate in one microwave; it swells and slumps rather than appearing or vanishing.
  - fail: A second marshmallow appears; or the marshmallow vanishes; or it passes through the plate; or it passes through the microwave's door.
- P6 [minor · attribute_drift]
  - expect: The plate, the microwave's interior and the marshmallow's colour stay the same.
  - fail: The plate's pattern changes; or the interior changes; or the marshmallow changes colour.

**Note.** Browning of the marshmallow is chemistry and is not judged.

## HEAT-0167 · heat_response · train

**Caption.** A paper pinwheel is held above a lit candle, and it begins to spin in the rising warm air.

**Expectation (hidden).** The spinning begins when the pinwheel is over the flame and stops when it is moved away; it does not spin over an unlit candle.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A paper pinwheel is held above a lit candle.
- S2 [core] The pinwheel begins to spin.
- S3 [core] The pinwheel stops when it is moved away from the candle.
- S4 [minor] The candle is lit.
- S5 [minor] The pinwheel is still before it is brought over the flame.
- S6 [minor] The bringing over comes first and the spinning follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The pinwheel spins only while it is over the flame and slows and stops when it is moved away.
  - fail: The pinwheel spins while held well away from the candle; or it spins over an unlit candle; or it stays still directly over the flame; or it keeps spinning at the same rate after being taken away.
- P2 [core · missing_consequence]
  - expect: The flame's rising air turns the wheel: the spin starts once the wheel is over the flame and not before.
  - fail: The wheel spins before it is brought over the flame; or the wheel is held over the flame and stays still to the end of the clip; or the wheel spins while the candle is out; or the flame is blown out and the wheel spins faster.
- P3 [major · trajectory_momentum]
  - expect: The wheel turns about its pin in one direction and slows gradually rather than stopping dead.
  - fail: The wheel reverses direction with nothing changing; or stops dead in a single frame while still over the flame; or wobbles off its pin; or its vanes move at different rates.
- P4 [major · gravity_direction]
  - expect: The flame points upward and leans only as the wheel or a draught disturbs it, and the wheel is held above it.
  - fail: The flame points downward; or the flame is drawn up into the wheel and burns above it; or the flame hangs below the candle; or the wheel is pushed downward toward the flame.
- P5 [fatal · permanence_count]
  - expect: One pinwheel with its vanes on one pin and one candle with one flame.
  - fail: A vane vanishes; or a second pinwheel appears; or the flame detaches and floats up to the wheel; or the wheel comes off its pin and hangs in the air.
- P6 [minor · attribute_drift]
  - expect: The pinwheel's colours, the candle and the surroundings stay the same.
  - fail: A vane changes colour; or the candle changes colour; or items around the candle rearrange.

**Note.** Whoever holds the pinwheel is not judged. Whether the paper scorches is not judged.

## HEAT-0168 · heat_response · train

**Caption.** A heat gun is aimed at the loose plastic wrap around a gift basket, and the wrap tightens and shrinks snugly around the basket.

**Expectation (hidden).** The film pulls tight and smooth where the heat is applied and stays tight afterwards; it does not loosen again.

**Declared violation types.** material_response, process_direction

**SA**
- S1 [core] Loose plastic wrap surrounds a gift basket.
- S2 [core] A heat gun is aimed at the wrap.
- S3 [core] The wrap tightens.
- S4 [core] The wrap shrinks snugly around the basket.
- S5 [minor] The wrap is loose and wrinkled at the start.
- S6 [minor] The heating comes first and the tightening follows.

**PC**
- P1 [core · material_response]
  - expect: The wrap is a thin film that pulls smooth and taut where the heat plays and holds that shape, and the basket keeps its shape under it.
  - fail: The wrap stays loose and wrinkled while glossy and pulling; or the wrap melts into holes and runs; or the wrap stretches looser as it is heated; or the basket collapses as the wrap tightens.
- P2 [core · process_direction]
  - expect: The tightening only advances where the heat has played and tightened wrap stays tight.
  - fail: A tightened area goes slack again with nothing cooling it; or the wrap tightens and loosens in turn; or the wrap tightens on a part the gun has not reached; or the wrinkles come back where the gun has passed.
- P3 [major · missing_consequence]
  - expect: The wrap tightens where the gun is aimed and stays loose where it is not.
  - fail: The whole wrap tightens at once while the gun plays on one spot; or the wrap tightens on the far side from the gun while the near side stays loose; or the gun plays on the wrap and it stays loose and wrinkled to the end of the clip.
- P4 [major · causeless_motion]
  - expect: The basket and its contents stay put and the wrap moves only as it shrinks or as the gun's air pushes it.
  - fail: The basket slides or tips with nothing touching it; or the contents rearrange inside the basket; or the wrap billows away from the basket and stays out; or the basket lifts off the table.
- P5 [fatal · permanence_count]
  - expect: One basket in one wrap; the wrap stays one sheet and the contents keep their number.
  - fail: The wrap splits into separate sheets; or a second basket appears; or an item in the basket vanishes; or the wrap passes through the basket's side.
- P6 [minor · attribute_drift]
  - expect: The basket's weave, its contents and the surroundings stay the same.
  - fail: The basket's weave changes pattern; or an item in the basket changes colour; or the background changes between frames.

## HEAT-0169 · heat_response · train

**Caption.** Sausages sizzle in a hot pan, and one of them splits open along its side with a pop.

**Expectation (hidden).** The skin bursts along a line and the split gapes open, juices escaping; the skin does not close again.

**Declared violation types.** process_direction, shape_identity

**SA**
- S1 [core] Sausages lie in a hot pan.
- S2 [core] One sausage splits along its side.
- S3 [core] The split gapes open.
- S4 [core] Juices escape from the split.
- S5 [minor] The other sausages stay whole.
- S6 [minor] The split does not close again.

**PC**
- P1 [core · process_direction]
  - expect: The split only opens wider and stays open, and the juices only leave.
  - fail: The split closes and the skin is whole again; or the split narrows; or the juices draw back into the sausage; or the split opens and shuts in turn.
- P2 [core · shape_identity]
  - expect: The skin stays a casing that bursts along a line and gapes, and the sausage keeps being one sausage.
  - fail: The sausage melts and drips; or the skin stretches like rubber and stays whole while gaping; or the sausage splits into two whole sausages; or the sausage turns into another object.
- P3 [major · gravity_direction]
  - expect: The juices run down the sausage into the pan and gather at its low places, and the sausages rest in the pan.
  - fail: The juices climb up the sausage; or a drop leaves the sausage and rises; or a sausage lifts off the pan and hangs; or the juices gather on the sausage's top and stay.
- P4 [major · causeless_motion]
  - expect: The sausages shift only as the pan is moved, as they split or as the fat spits.
  - fail: A sausage slides across the pan with the pan still and no split; or a sausage rolls uphill; or the sausages line themselves up in a row; or a sausage spins fast on the spot.
- P5 [fatal · permanence_count]
  - expect: The sausages keep their number in the pan and none appears or vanishes.
  - fail: A sausage vanishes; or a new sausage appears in the pan; or two sausages merge into one; or a sausage passes through the pan's floor.
- P6 [minor · attribute_drift]
  - expect: The pan, the hob and the surroundings stay the same.
  - fail: The pan changes colour; or its handle changes shape; or items around the hob rearrange.

**Note.** The pop is sound and is not judged. The sausages browning as they cook is chemistry and is not judged.

## HEAT-0170 · heat_response · train

**Caption.** A dented ping-pong ball is dropped into a bowl of very hot water, and the dent pops back out.

**Expectation (hidden).** The dent pushes out within seconds of the ball entering the hot water and the ball floats round; the dent does not return in the hot water.

**Declared violation types.** shape_identity, process_direction

**SA**
- S1 [core] A ping-pong ball with a dent in it.
- S2 [core] The ball is dropped into a bowl of hot water.
- S3 [core] The dent pops out.
- S4 [core] The ball ends round.
- S5 [minor] The ball floats.
- S6 [minor] The drop comes first and the dent's popping out follows.

**PC**
- P1 [core · shape_identity]
  - expect: The dent moves outward until the ball's surface is round again, and the ball stays one hollow sphere of the same size.
  - fail: The dent deepens instead of popping out; or a new dent appears elsewhere on the ball; or the ball swells much larger than it was; or the ball turns into another shape such as an egg.
- P2 [core · process_direction]
  - expect: The change runs one way in the hot water: the dent only comes out and does not return.
  - fail: The dent pops out and then presses back in while the ball stays in the hot water; or the dent comes and goes in turn; or the dent pops out before the ball reaches the water; or the ball's surface ripples back and forth.
- P3 [major · gravity_direction]
  - expect: The ball floats at the surface, bobbing, and the water stays level in the bowl.
  - fail: The ball sinks to the bowl's floor and stays; or hangs motionless in mid-water; or rises out of the water and hangs above it; or the water's surface tilts and stays tilted with the bowl level.
- P4 [major · missing_consequence]
  - expect: The drop has an effect: the water splashes and ripples where the ball lands and the ball is wetted.
  - fail: The ball enters and the surface stays glassy; or the water ripples before the ball reaches it; or the ball stays dry while floating; or the dent pops out while the ball is still in the air above the water.
- P5 [fatal · permanence_count]
  - expect: One ball and one bowl; the ball stays in the water and nothing passes through the bowl.
  - fail: The ball vanishes; or a second ball appears; or the ball passes through the bowl's wall; or the bowl changes shape.
- P6 [minor · attribute_drift]
  - expect: The ball's colour and markings, the bowl and the surroundings stay the same.
  - fail: The ball changes colour; or its printed markings change; or the bowl changes pattern.

## HEAT-0171 · heat_response · train

**Caption.** A hot air balloon's burner is fired, and the balloon lifts off the field.

**Expectation (hidden).** The balloon rises while the burner fires and drifts slowly; it does not lift before the burner runs or drop as soon as it stops.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] A hot air balloon stands on a field with its envelope up.
- S2 [core] The burner is fired: a flame roars into the envelope's mouth.
- S3 [core] The balloon lifts off the field.
- S4 [minor] The balloon rises slowly.
- S5 [minor] The firing comes first and the lift follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The balloon rises after the burner fires and not before; it does not lift with the burner dark.
  - fail: The balloon lifts off before the burner is fired; or the burner fires and the basket stays settled on the ground to the end of the clip; or the balloon rises while the burner is plainly off; or the balloon drops at the moment the burner fires.
- P2 [core · gravity_direction]
  - expect: The balloon rises upward with the basket hanging below the envelope, and it drifts sideways only with the wind.
  - fail: The balloon rises basket first with the envelope below; or the balloon shoots sideways across the field with no sign of wind; or the envelope hangs below the basket; or the balloon sinks while the burner roars on.
- P3 [major · trajectory_momentum]
  - expect: The lift builds from rest without jumps and the balloon keeps rising or levels off.
  - fail: The balloon jumps up in steps between frames; or stops dead in mid-air and starts again from rest; or rises and falls in turn with the burner steady; or spins fast about its own axis.
- P4 [major · material_response]
  - expect: The envelope stays a taut fabric bag that rounds out and ripples, and the ropes stay taut between envelope and basket.
  - fail: The envelope stays a rigid shell; or the ropes go slack while the basket hangs from them; or the envelope collapses as the balloon rises; or the ropes stretch like elastic.
- P5 [fatal · permanence_count]
  - expect: One balloon with one envelope and one basket; the balloon keeps its parts and passes through nothing.
  - fail: The basket detaches and the balloon rises alone; or a second balloon appears; or the envelope vanishes; or the balloon passes through a tree or a mast.
- P6 [minor · attribute_drift]
  - expect: The envelope's panels, the basket and the field stay the same.
  - fail: The envelope's panel colours change; or the basket changes shape; or the field's markings change.

**Note.** The burner's roar is sound and is not judged; the firing is read from the flame. The crew are not judged.

## HEAT-0172 · heat_response · train

**Caption.** A plastic soda bottle is left too close to a campfire, and the near side shrivels and caves in.

**Expectation (hidden).** The plastic facing the fire wrinkles and pulls inward; the far side keeps its shape; the caved side does not pop back out.

**Declared violation types.** material_response, process_direction

**SA**
- S1 [core] A plastic bottle stands near a campfire.
- S2 [core] The side facing the fire shrivels.
- S3 [core] That side caves inward.
- S4 [core] The far side keeps its shape.
- S5 [minor] The bottle is smooth at the start.
- S6 [minor] The shrivelling comes first and the caving follows.

**PC**
- P1 [core · material_response]
  - expect: The plastic on the fire side goes soft, wrinkles and pulls inward, keeping its plastic look, while the rest stays a rigid bottle.
  - fail: The bottle shatters into pieces; or the whole bottle runs into a puddle at once; or the fire side stays perfectly smooth while caving deeply; or the bottle stretches upward like taffy.
- P2 [core · process_direction]
  - expect: The caving only deepens on the fire side and the caved side does not pop back out.
  - fail: The caved side pops back out to smooth while the bottle stays by the fire; or the caving deepens and eases in turn; or the far side caves while the fire side stays smooth; or the shrivelling appears before the bottle is near the fire.
- P3 [major · missing_consequence]
  - expect: The change is strongest on the side toward the fire and least on the far side.
  - fail: The far side shrivels while the fire side stays smooth; or the bottle shrivels evenly all round while the fire is plainly on one side; or the bottle caves in at its base while its fire-facing wall stays smooth.
- P4 [major · gravity_direction]
  - expect: The bottle stays standing or topples downward as it softens, and its contents stay in it and lie level.
  - fail: The bottle rises off the ground; or the bottle leans further and further over without falling; or the contents climb the bottle's wall and stay; or the bottle floats toward the fire.
- P5 [fatal · permanence_count]
  - expect: One bottle; it keeps its cap and label and does not pass through the ground.
  - fail: The bottle vanishes; or a second bottle appears; or the cap passes into the bottle; or the bottle sinks into the ground.
- P6 [minor · attribute_drift]
  - expect: The bottle's label, the fire's stones and the surroundings stay the same.
  - fail: The label's printing changes; or the stones rearrange; or the background changes between frames.

**Note.** Smoke or discolouring from the melting plastic is chemistry and is not judged.

## HEAT-0173 · heat_response · train

**Caption.** A few drops of water are flicked onto a hot griddle, and the drops skitter around and vanish.

**Expectation (hidden).** The drops dance across the surface and disappear within seconds; they do not sit still or grow.

**Declared violation types.** permanence_count, causeless_motion

**SA**
- S1 [core] A hot griddle.
- S2 [core] A few drops of water are flicked onto the griddle.
- S3 [core] The drops skitter across the surface.
- S4 [core] The drops disappear.
- S5 [minor] The drops stay whole beads while they skitter.
- S6 [minor] The flick comes first and the skittering follows.

**PC**
- P1 [core · permanence_count]
  - expect: Each drop shrinks as it skitters and goes by shrinking away, and the drops that skitter are the drops that were flicked.
  - fail: A drop vanishes in a single frame while still large; or new drops appear on the griddle with none flicked; or a drop grows as it skitters; or drops merge into a puddle that stays.
- P2 [core · causeless_motion]
  - expect: The drops glide and swerve because they were flicked and because they ride on their own steam; their paths bend only at the griddle's slope or edge.
  - fail: A drop darts off at a new angle with nothing met and no slope; or a drop stops dead and sets off again from rest; or a drop climbs the griddle's raised edge and hangs there; or a drop travels against the flick before touching anything.
- P3 [major · material_response]
  - expect: The drops stay rounded beads that skitter without wetting the metal, and any steam they give off is a fine wisp.
  - fail: A drop spreads into a flat wet film that stays; or a drop bounces high off the griddle like a ball; or a drop sets solid on the metal; or a drop stands as a tall column.
- P4 [major · gravity_direction]
  - expect: The drops stay on the griddle's surface and any steam rises.
  - fail: A drop lifts off the griddle and hangs in the air; or a drop rises and stays above the metal; or the steam sinks and pools around the griddle; or a drop falls upward off the griddle.
- P5 [fatal · solidity]
  - expect: The drops stay on top of the griddle's surface and nothing passes through the metal.
  - fail: A drop sinks into the griddle's metal; or a drop passes through the griddle; or the griddle changes shape; or a second griddle appears.
- P6 [minor · attribute_drift]
  - expect: The griddle's finish and the surroundings stay the same.
  - fail: The griddle changes colour; or its surface pattern changes; or items around it rearrange.

## HEAT-0174 · heat_response · train

**Caption.** A lidded plastic container of leftovers is heated in a microwave, and the lid domes upward and pops loose.

**Expectation (hidden).** The lid bulges more and more as the food heats, then lifts at one corner with a puff of steam; it does not sink inward.

**Declared violation types.** process_direction, shape_identity

**SA**
- S1 [core] A plastic container with its lid on sits in a microwave.
- S2 [core] The lid domes upward.
- S3 [core] The dome grows.
- S4 [core] The lid lifts at one corner.
- S5 [minor] A puff of steam escapes as the lid lifts.
- S6 [minor] The doming comes first and the popping loose follows.

**PC**
- P1 [core · process_direction]
  - expect: The dome only grows while the food heats and the lid does not sink back before it lifts.
  - fail: The dome sinks inward while the microwave runs; or the dome grows and shrinks in turn; or the lid domes before the microwave has started; or the lid lifts, re-seats itself and domes again.
- P2 [core · shape_identity]
  - expect: The lid stays one lid whose flat top bows upward and springs back or hangs loose once it lifts.
  - fail: The lid keeps a perfectly flat top while plainly lifting at its rim; or the lid swells into a balloon much larger than the container; or the lid splits into pieces; or the lid turns into another object.
- P3 [major · gravity_direction]
  - expect: The dome bulges upward rather than downward, and the lid falls back onto the container or lies on it once loose.
  - fail: The lid bows downward into the food; or the loose lid rises and hangs above the container; or the lid flies up and sticks to the microwave's roof; or the food climbs the container's wall and stays.
- P4 [major · missing_consequence]
  - expect: The food shows the heating: it steams or bubbles, and the steam escapes where the lid lifts.
  - fail: The lid domes while the food below is still with no steam at all; or the steam escapes from the container's base; or the lid lifts and no steam or movement shows in the food to the end of the clip.
- P5 [fatal · permanence_count]
  - expect: One container with one lid; the lid stays a separate piece and the food stays inside.
  - fail: The lid merges into the container's rim; or a second lid appears; or food passes through the container's wall; or the container vanishes.
- P6 [minor · attribute_drift]
  - expect: The container's colour, the food's look and the microwave's interior stay the same.
  - fail: The container changes colour; or the food changes into something else; or the interior changes.

## HEAT-0175 · heat_response · train

**Caption.** Heat rises from a barbecue grill on a summer afternoon, and the view of the fence behind it wavers in the shimmering air.

**Expectation (hidden).** The shimmer sits above the grill and rises, fading with height; the fence is distorted only through the hot air above the grill.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] A barbecue grill.
- S2 [core] The air above the grill shimmers.
- S3 [core] The fence behind wavers where it is seen through the shimmer.
- S4 [minor] The shimmer is strongest just above the grill.
- S5 [minor] The shimmer fades with height.
- S6 [minor] The fence stands steady where it is not seen through the shimmer.

**PC**
- P1 [core · gravity_direction]
  - expect: The shimmer rises from the grill and fades with height; it does not flow downward.
  - fail: The shimmer flows down the grill's sides and pools on the ground; or sinks below the grill; or pours downward through the grill's bars; or hangs as a fixed band without rising.
- P2 [core · process_direction]
  - expect: The shimmer keeps rising while the grill is hot and the wavering keeps moving upward, easing as the grill cools.
  - fail: The shimmer runs back down into the grill; or the wavering freezes into a fixed pattern; or the shimmer thickens steadily long after the fire is out; or a waver retreats toward the grill.
- P3 [major · missing_consequence]
  - expect: Only the part of the fence seen through the rising air wavers and the rest stands steady.
  - fail: The whole fence wavers including parts seen well away from the shimmer; or the fence stands perfectly steady behind a strong shimmer; or the shimmer sits over a cold part of the yard while the air above the grill is still.
- P4 [major · causeless_motion]
  - expect: The grill and the fence stay put; only the air above the grill moves.
  - fail: The fence's boards shift or lean; or the grill slides with nothing touching it; or the grill's lid swings by itself; or objects beside the grill jump.
- P5 [fatal · permanence_count]
  - expect: One grill and one fence; the fence keeps its boards and the grill its parts.
  - fail: A fence board vanishes; or a new board appears; or the grill's lid vanishes; or the fence changes into a wall.
- P6 [minor · attribute_drift]
  - expect: The fence's colour, the grill's body and the yard stay the same.
  - fail: The fence changes colour; or the grill changes colour; or items in the yard rearrange.

## HEAT-0176 · heat_response · train

**Caption.** Cooking oil is poured into a pan over high heat, and the oil begins to shimmer and ripple across its surface.

**Expectation (hidden).** The surface goes from still to moving in fine ripples as the pan heats and thin wisps of smoke may rise; the ripples do not appear in a cold pan.

**Declared violation types.** process_direction, causeless_motion

**SA**
- S1 [core] Oil is poured into a pan on a hob.
- S2 [core] The oil's surface goes from still to moving.
- S3 [core] Fine ripples run across the surface.
- S4 [minor] Thin wisps may rise from the oil.
- S5 [minor] The oil is still just after it is poured.
- S6 [minor] The pour comes first and the rippling follows.

**PC**
- P1 [core · process_direction]
  - expect: The surface goes from still to rippling as the pan heats and the rippling keeps up.
  - fail: The oil ripples while it is still falling from the bottle; or the surface goes glassy still and stays so while wisps rise from it; or the rippling stops and then starts again by itself; or the ripples appear before any oil is in the pan.
- P2 [core · causeless_motion]
  - expect: The ripples run across the oil's own surface and the oil stays in the pan; nothing else moves it.
  - fail: The oil swirls as though stirred with nothing in the pan; or the whole body of oil slides from side to side in a still pan; or the pan shakes with nothing touching it; or the ripples hold one fixed pattern that never changes.
- P3 [major · gravity_direction]
  - expect: The oil lies level in the pan and finds its level as it is poured, and any wisps rise.
  - fail: The oil's surface tilts and stays tilted with the pan level; or the oil climbs the pan's wall and stays above its level; or the wisps sink over the rim and pool on the hob; or the oil stands in a heap in the pan's middle.
- P4 [major · material_response]
  - expect: The oil is a thin liquid that pours in a stream, spreads over the pan's floor and shows fine surface movement.
  - fail: The oil pours as a solid rod; or the oil sets solid in the pan; or the oil moves as a single rigid sheet; or the oil beads up and rolls about without wetting the pan.
- P5 [fatal · permanence_count]
  - expect: One pan and one pour; the oil stays in the pan and its level changes only by pouring.
  - fail: The oil's level jumps up with nothing poured; or oil passes through the pan's wall; or a second pan appears; or the pan changes shape.
- P6 [minor · attribute_drift]
  - expect: The pan, the hob and the oil's colour stay the same.
  - fail: The pan changes colour; or the oil changes colour; or items around the hob rearrange.

**Note.** Smoking of the oil is chemistry and is not judged.

## HEAT-0177 · heat_response · train

**Caption.** A handful of dry rice noodles is dropped into hot water, and they go from stiff and brittle to limp and floppy.

**Expectation (hidden).** The noodles soften from the ends touching the water and sink into loose coils; they do not stiffen again in the hot water.

**Declared violation types.** material_response, process_direction

**SA**
- S1 [core] A pot of hot water.
- S2 [core] Dry rice noodles are dropped into the water.
- S3 [core] The noodles go limp.
- S4 [core] The noodles sink into loose coils.
- S5 [minor] The noodles are stiff and straight at the start.
- S6 [minor] The softening starts at the ends in the water.

**PC**
- P1 [core · material_response]
  - expect: The noodles go from stiff straight sticks to limp strands that bend, coil and drape over each other.
  - fail: The noodles stay straight and rigid while fully under the water and glossy; or a noodle snaps into stiff pieces and stays stiff; or the noodles fuse into one solid block; or the noodles stretch like elastic.
- P2 [core · process_direction]
  - expect: The softening only advances and softened noodles do not stiffen again in the hot water.
  - fail: A limp noodle stiffens and straightens again in the water; or the noodles soften and stiffen in turn; or the noodles are limp before they reach the water; or a coiled noodle springs back straight.
- P3 [major · missing_consequence]
  - expect: The softening starts where the noodles meet the water and spreads along them, while parts still out of the water stay stiff.
  - fail: The part standing out of the water goes limp while the submerged part stays stiff; or the whole bundle goes limp at once while only its tips are wetted; or the noodles sit in hot water and stay stiff and straight to the end of the clip.
- P4 [major · gravity_direction]
  - expect: The softened noodles sink or settle into the water and the bundle sags downward as it gives way.
  - fail: A noodle rises out of the water and hangs above it; or a noodle hangs motionless in mid-water; or the bundle stands upright in the water with nothing holding it; or the noodles float on top like a raft and stay dry.
- P5 [fatal · permanence_count]
  - expect: The noodles that go in are the noodles in the water and none appears or vanishes.
  - fail: A noodle vanishes; or new noodles appear with none added; or two noodles merge into one thicker strand; or a noodle passes through the pot's wall.
- P6 [minor · attribute_drift]
  - expect: The pot, the water and the surroundings stay the same.
  - fail: The pot changes colour; or the water turns a colour; or items around the pot rearrange.

## HEAT-0178 · heat_response · train

**Caption.** Hot water is poured over a pot of dried seaweed, and the crisp sheets swell and soften into flowing strands.

**Expectation (hidden).** The sheets expand and become slippery and limp within moments; they do not return to crisp flat sheets in the water.

**Declared violation types.** material_response, process_direction, shape_identity

**SA**
- S1 [core] A pot of dried seaweed sheets.
- S2 [core] Hot water is poured over the seaweed.
- S3 [core] The sheets swell.
- S4 [core] The sheets soften into limp strands.
- S5 [minor] The sheets are crisp and flat at the start.
- S6 [minor] The pour comes first and the swelling follows.

**PC**
- P1 [core · material_response]
  - expect: The seaweed goes from crisp flat sheets to slippery limp strands that move with the water.
  - fail: The sheets stay crisp and flat while fully wetted and moving; or a sheet shatters into dry shards under the water; or the seaweed melts into a liquid; or the strands stiffen into wire.
- P2 [core · process_direction]
  - expect: The swelling and softening only advance and the seaweed does not go crisp again in the water.
  - fail: A softened strand goes crisp and flat again in the water; or the seaweed swells and shrinks in turn; or the seaweed is limp before the water reaches it; or the strands draw back into flat dry sheets.
- P3 [core · shape_identity]
  - expect: Each sheet keeps being one piece of seaweed as it opens out and unfurls into strands.
  - fail: A sheet splits into many separate whole sheets; or the seaweed turns into another material; or the sheets fuse into one smooth mass; or a sheet grows into a shape it never had, such as a ball.
- P4 [major · gravity_direction]
  - expect: The poured water falls downward into the pot, the seaweed sinks or drifts in it, and the water lies level.
  - fail: The water travels upward from the jug; or a strand rises out of the water and hangs above it; or the water's surface tilts and stays tilted with the pot level; or the seaweed climbs the pot's wall and stays.
- P5 [fatal · permanence_count]
  - expect: The seaweed in the pot is the seaweed that was there and the water comes only from the pour.
  - fail: Seaweed appears in the pot with none added; or a sheet vanishes; or the water's level jumps with nothing poured; or seaweed passes through the pot's wall.
- P6 [minor · attribute_drift]
  - expect: The pot, the jug and the surroundings stay the same.
  - fail: The pot changes colour; or the jug changes shape; or items around the pot rearrange.

**Note.** The seaweed darkening as it soaks is expected; its colour is not judged.

## HEAT-0179 · heat_response · train

**Caption.** A flour tortilla lies on a wire rack over a gas flame, and pockets of the tortilla puff up into bubbles.

**Expectation (hidden).** The bubbles rise on the upper side while the tortilla is over the flame and the underside browns in spots; the puffed pockets do not appear before heating and the browning does not fade.

**Declared violation types.** shape_identity, process_direction

**SA**
- S1 [core] A tortilla lies on a wire rack over a gas flame.
- S2 [core] Pockets of the tortilla puff up.
- S3 [core] The puffed pockets stand as bubbles on its upper side.
- S4 [minor] The underside darkens in spots.
- S5 [minor] The tortilla is flat before it is over the flame.
- S6 [minor] The heating comes first and the puffing follows.

**PC**
- P1 [core · shape_identity]
  - expect: The tortilla stays one flat round that raises separate domed pockets on its upper face, each still joined to the sheet.
  - fail: A pocket detaches and floats free of the tortilla; or the whole tortilla swells into a ball; or the tortilla splits into separate pieces as it puffs; or the tortilla turns into another object.
- P2 [core · process_direction]
  - expect: The pockets only rise while the tortilla is over the flame and the darkening on the underside only deepens.
  - fail: A pocket sinks flat and rises again with the tortilla still over the flame; or a darkened spot fades back to pale dough; or the pockets appear before the tortilla is over the flame; or the darkening spreads and then shrinks.
- P3 [major · gravity_direction]
  - expect: The pockets rise upward on the upper face, the tortilla rests on the rack, and the flame points upward at it.
  - fail: The pockets bulge downward through the rack; or the tortilla lifts off the rack and hangs in the air; or the flame points downward away from the tortilla; or a pocket rises and carries the tortilla up with it.
- P4 [major · missing_consequence]
  - expect: The pockets and the dark spots appear where the flame reaches the tortilla from below.
  - fail: The pockets rise on a part of the tortilla the flame never reaches; or the underside stays pale and unmarked while pockets rise all over; or the tortilla sits over the flame and stays flat and unmarked to the end of the clip.
- P5 [fatal · permanence_count]
  - expect: One tortilla on one rack; the tortilla stays one piece and the rack keeps its wires.
  - fail: A second tortilla appears; or the tortilla vanishes; or the tortilla passes through the rack's wires; or a wire vanishes.
- P6 [minor · attribute_drift]
  - expect: The rack, the hob and the surroundings stay the same.
  - fail: The rack changes spacing; or the hob's knobs move by themselves; or items around the hob rearrange.

**Note.** The browning of the tortilla is chemistry; what is judged is that the darkening runs one way and appears where the flame reaches it.

## HEAT-0180 · heat_response · train

**Caption.** A damp sock hangs from a stick propped beside a campfire, and steam rises from it.

**Expectation (hidden).** Steam rises from the side of the sock facing the fire and drifts upward with the heat; the sock does not become wetter and the vapour does not sink.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] A damp sock hangs from a stick beside a campfire.
- S2 [core] Steam rises from the sock.
- S3 [minor] The steam comes from the side facing the fire.
- S4 [minor] The steam drifts upward and away.
- S5 [minor] The sock hangs rather than being held.

**PC**
- P1 [core · gravity_direction]
  - expect: The steam leaves the sock going up, spreading and thinning, while the sock hangs downward from the stick.
  - fail: The steam sinks and pools below the sock; or pours downward through the sock; or the sock's toe rises and stays up with nothing lifting it; or the steam hangs as a fixed shape without rising.
- P2 [core · process_direction]
  - expect: The steam only leaves the sock and the sock only dries; it does not get wetter while it hangs by the fire.
  - fail: The steam runs back into the sock; or a puff retreats to the fabric; or a dried patch goes dark and wet again with nothing wetting it; or the steaming grows steadily thicker the longer the sock hangs.
- P3 [major · missing_consequence]
  - expect: The steam comes from the sock's own damp fabric and is thickest on the side toward the fire.
  - fail: The steam rises from the stick rather than the sock; or the steam is thickest on the side away from the fire; or the sock hangs by the fire soaking wet and no steam leaves it at all; or the steam rises from the ground beside the fire while the sock is clear.
- P4 [major · material_response]
  - expect: The sock is limp damp cloth that hangs in folds and sways, and the steam is a soft cloud that spreads.
  - fail: The sock stands stiff like a board; or stretches downward like elastic; or the steam holds a fixed rigid shape; or the sock sets hard as it dries.
- P5 [fatal · permanence_count]
  - expect: One sock on one stick; the sock stays on the stick and the fire's wood keeps its number.
  - fail: The sock vanishes; or a second sock appears; or the sock passes through the stick; or a log vanishes.
- P6 [minor · attribute_drift]
  - expect: The sock's colour and pattern, the stick and the surroundings stay the same.
  - fail: The sock changes colour or pattern; or the stick changes shape; or the background changes between frames.

**Note.** Scorching of the sock is not judged; the caption's event is the steam.

## HEAT-0181 · heat_response · train

**Caption.** Bacon strips laid in a hot pan begin to sizzle, and the strips shrink and curl at the edges.

**Expectation (hidden).** The strips get shorter and their edges lift and buckle as they cook; fat pools around them; the strips do not flatten or grow.

**Declared violation types.** material_response, process_direction, shape_identity

**SA**
- S1 [core] Bacon strips lie in a hot pan.
- S2 [core] The strips shrink.
- S3 [core] Their edges lift and buckle.
- S4 [core] Fat pools around them.
- S5 [minor] The strips are flat and straight at the start.
- S6 [minor] The shrinking and curling come after the strips are in the pan.

**PC**
- P1 [core · material_response]
  - expect: The strips go from limp flat slices to stiffer buckled ones that hold their curl, and the fat that leaves them is a thin liquid.
  - fail: A strip stays perfectly flat and limp while shrunken and glossy; or a strip melts away entirely into the fat; or the fat stands as a dome beside the strips; or a strip stretches longer as it cooks.
- P2 [core · process_direction]
  - expect: The shrinking and curling only advance and the strips do not flatten out or grow again.
  - fail: A curled strip flattens out and lengthens again in the hot pan; or the strips shrink and grow in turn; or a strip's curl eases while the pan stays hot; or the fat draws back into the strips.
- P3 [core · shape_identity]
  - expect: Each strip stays one strip that buckles and ripples along its length, keeping its two ends.
  - fail: A strip splits into separate pieces with nothing cutting it; or the strips fuse into one sheet; or a strip rolls into a solid tube with no seam; or a strip turns into another object.
- P4 [major · gravity_direction]
  - expect: The fat runs to the pan's low places and pools there, and the strips stay in the pan.
  - fail: The fat climbs the pan's wall and stays; or a strip lifts off the pan and hangs; or the fat gathers on top of a strip and stays; or the fat runs uphill.
- P5 [fatal · permanence_count]
  - expect: The strips keep their number in the pan and none appears or vanishes.
  - fail: A strip vanishes; or a new strip appears in the pan; or two strips merge into one; or a strip passes through the pan's floor.
- P6 [minor · attribute_drift]
  - expect: The pan, the hob and the surroundings stay the same.
  - fail: The pan changes colour; or its handle changes shape; or items around the hob rearrange.

**Note.** The bacon browning as it cooks is chemistry and is not judged.

## HEAT-0182 · heat_response · train

**Caption.** A hairdryer is aimed at a bent plastic pipe, and the pipe softens enough to be straightened by hand and holds its new shape when cool.

**Expectation (hidden).** The pipe bends only where heated, moves under the hands while warm, and stays put after cooling; it does not spring back to its old bend.

**Declared violation types.** material_response, process_direction

**SA**
- S1 [core] A bent plastic pipe.
- S2 [core] A hairdryer is aimed at the bend.
- S3 [core] The pipe softens at the heated spot.
- S4 [core] The pipe is straightened by hand.
- S5 [minor] The pipe holds its new shape.
- S6 [minor] The heating comes first, then the bending, then the holding.

**PC**
- P1 [core · material_response]
  - expect: The pipe goes from stiff to bendable at the heated spot and back to stiff as it cools, keeping its round section.
  - fail: The pipe stays stiff and springs back as soon as the hands let go; or the pipe runs off as a liquid; or the pipe stretches like elastic while being straightened; or the pipe shatters at the bend.
- P2 [core · process_direction]
  - expect: The pipe holds the new shape once it has cooled and does not return to its old bend.
  - fail: The pipe springs back to its old bend after the hands let go and it has cooled; or the pipe bends further on its own; or the new shape and the old bend alternate; or the pipe softens again with the dryer off and away.
- P3 [major · missing_consequence]
  - expect: The pipe bends only where the dryer has played and stays stiff elsewhere.
  - fail: The pipe bends at a point the dryer never reached; or the pipe bends along its whole length while the dryer plays on one spot; or the dryer plays on the pipe and it stays as stiff as before to the end of the clip.
- P4 [major · gravity_direction]
  - expect: The pipe rests on its support and its free end hangs or is held; it does not rise.
  - fail: The pipe lifts off the bench and hangs in the air; or the softened part bends upward with nothing lifting it; or the pipe floats toward the dryer; or the free end rises with the hands gone.
- P5 [fatal · permanence_count]
  - expect: One pipe; it stays one piece and keeps its length apart from the bending.
  - fail: The pipe breaks into two pieces; or a second pipe appears; or the pipe vanishes; or the pipe passes through the bench.
- P6 [minor · attribute_drift]
  - expect: The pipe's colour, the dryer and the bench stay the same.
  - fail: The pipe changes colour; or the dryer changes shape; or items on the bench rearrange.

**Note.** The hands are kept because the straightening is the caption's action; they are otherwise not judged.

## HEAT-0183 · heat_response · train

**Caption.** A frozen block of soup sits in a pan over heat, sliding around on a thin layer of melt and shrinking as the liquid pools around it.

**Expectation (hidden).** The block loosens from the pan, glides slightly when the pan is tilted, and gets smaller as the pool grows; the pool does not refreeze.

**Declared violation types.** process_direction, causeless_motion

**SA**
- S1 [core] A frozen block of soup sits in a pan on a hob.
- S2 [core] The block slides on a thin layer of melt.
- S3 [core] The block shrinks.
- S4 [core] A pool of liquid grows around it.
- S5 [minor] The block loosens from the pan's floor.
- S6 [minor] The melting comes first and the sliding follows.

**PC**
- P1 [core · process_direction]
  - expect: The block only shrinks while the pool grows, and the pool does not freeze again on the hot pan.
  - fail: The block grows; or the pool draws back into the block; or the pool freezes solid around the block on the hot pan; or the block alternates between larger and smaller.
- P2 [core · causeless_motion]
  - expect: The block glides only as the pan is tilted or moved and as it rides on the melt, and it slows and stops when the pan is still.
  - fail: The block darts across a level pan with nothing touching it; or spins fast on the spot; or climbs the pan's wall and hangs there; or slides uphill in a tilted pan.
- P3 [major · gravity_direction]
  - expect: The block settles downward as it melts and the pool spreads outward and downhill across the pan.
  - fail: The block lifts off the pan and hangs; or the pool climbs the pan's wall and stays; or the pool gathers uphill of the block in a tilted pan; or melted soup lifts off the pan.
- P4 [major · missing_consequence]
  - expect: The block melts where it touches the hot pan: its underside wets first and the pool spreads from beneath it.
  - fail: The block melts from its top while its underside stays frosted and dry; or a pool spreads on a part of the pan the block never touched; or the block slides about on a dry pan with no melt under it.
- P5 [fatal · permanence_count]
  - expect: One block in one pan; the soup goes only from the block into the pool.
  - fail: The block vanishes while still large; or a second block appears; or the pool's level jumps with nothing added; or soup passes through the pan's wall.
- P6 [minor · attribute_drift]
  - expect: The pan, the hob and the soup's colour stay the same.
  - fail: The pan changes colour; or the soup changes colour; or items around the hob rearrange.

## HEAT-0184 · heat_response · train

**Caption.** A lava lamp that has warmed up glows on a table, and the blobs of wax inside rise and sink.

**Expectation (hidden).** Blobs rise from the bottom, slow near the top, and fall again in a slow cycle; they do not jump or move in a way unrelated to the warm base.

**Declared violation types.** gravity_direction, process_direction, causeless_motion

**SA**
- S1 [core] A lava lamp glows on a table.
- S2 [core] Blobs of wax rise inside it.
- S3 [core] Blobs sink again.
- S4 [minor] The blobs rise from the lamp's base.
- S5 [minor] The blobs slow near the top.
- S6 [minor] The rising and sinking repeat.

**PC**
- P1 [core · gravity_direction]
  - expect: The blobs rise from the warm base, slow near the top and fall again, moving up and down through the liquid.
  - fail: The blobs all sink to the base and stay there while the lamp glows; or the blobs gather at the top and stay; or a blob hangs motionless in mid-liquid for the rest of the clip; or the blobs rise from the top and sink to the base.
- P2 [core · causeless_motion]
  - expect: The blobs move only with the slow currents in the lamp and their paths are gentle.
  - fail: A blob shoots across the lamp sideways; or a blob spins fast on the spot; or the blobs arrange themselves into a pattern; or the blobs move in a rhythm unrelated to the base, jumping while the base is dark.
- P3 [core · process_direction]
  - expect: The rising and sinking runs as a slow cycle: a blob that has risen comes down and one that has fallen goes up, and the wax stays wax.
  - fail: A blob vanishes at the top and reappears at the base; or the wax sets into a solid lump while the lamp glows; or every blob freezes in place while the lamp still glows; or the blobs freeze and melt in turn.
- P4 [major · material_response]
  - expect: The blobs are soft rounded lumps that stretch, pinch off and merge, and the liquid around them is clear and thin.
  - fail: A blob keeps a sharp-cornered shape as it rises; or two blobs touch and pass through each other without merging or parting; or the blobs shatter; or the liquid moves as a solid mass with the blobs fixed in it.
- P5 [fatal · permanence_count]
  - expect: One lamp; the wax stays inside the glass and the blobs merge or split rather than appearing or vanishing.
  - fail: A blob appears from nowhere in the middle of the liquid; or a blob vanishes in mid-liquid; or wax passes through the glass; or a second lamp appears.
- P6 [minor · attribute_drift]
  - expect: The lamp's base, its cap and the table stay the same.
  - fail: The lamp's base changes colour; or the wax changes colour; or items on the table rearrange.

## HEAT-0185 · heat_response · train

**Caption.** A pat of cold butter is placed in the centre of a hot pancake on the griddle, and it slides and glides across the surface as it melts.

**Expectation (hidden).** The pat moves on a film of melted butter, slowing as it shrinks, and leaves a glossy trail; it does not stay put or refreeze.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A pancake cooks on a griddle.
- S2 [core] A pat of butter is placed in its centre.
- S3 [core] The pat slides across the pancake.
- S4 [core] The pat shrinks as it melts.
- S5 [minor] The pat leaves a glossy trail.
- S6 [minor] The placing comes first and the sliding follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The pat glides on the film of melted butter under it and slows as it shrinks, moving only where the surface slopes or the griddle is tilted.
  - fail: The pat darts across a level pancake with nothing touching it; or it climbs back to the centre by itself; or it stops dead and sets off again from rest; or it spins fast on the spot.
- P2 [core · process_direction]
  - expect: The pat only shrinks while it slides and the melt only spreads; it does not firm up again on the hot pancake.
  - fail: The pat regains its square edges; or the trail draws back into the pat; or the butter sets solid again on the pancake; or the pat alternates between larger and smaller.
- P3 [major · gravity_direction]
  - expect: The pat and the melt run downhill across the pancake and off its edge onto the griddle where it slopes.
  - fail: The melt climbs uphill across the pancake; or the pat slides up a slope with nothing pushing it; or melted butter lifts off the pancake; or the melt gathers above the pat on a sloping surface.
- P4 [major · missing_consequence]
  - expect: The pat leaves a wet glossy trail where it has passed and the pancake's surface there looks soaked.
  - fail: The pat slides across and the pancake behind it stays dry and matt; or a glossy trail appears on a part of the pancake the pat never crossed; or the pat shrinks while no film shows under or behind it.
- P5 [fatal · permanence_count]
  - expect: One pat on one pancake; the butter goes only from the pat into the trail.
  - fail: The pat grows; or a second pat appears; or the pat vanishes while still large; or butter appears on the griddle with none running there.
- P6 [minor · attribute_drift]
  - expect: The griddle, the pancake's edge and the surroundings stay the same.
  - fail: The griddle changes colour; or the pancake changes shape apart from cooking; or items around the griddle rearrange.

**Note.** The pancake browning as it cooks is chemistry and is not judged.

## HEAT-0186 · heat_response · train

**Caption.** Boiling water is poured into a collapsed vacuum-packed camping meal pouch, and the pouch swells and stands up.

**Expectation (hidden).** The pouch fills out as the water goes in and steam rises from its opening; it does not stay flat.

**Declared violation types.** shape_identity, process_direction

**SA**
- S1 [core] A collapsed camping meal pouch.
- S2 [core] Boiling water is poured into the pouch.
- S3 [core] The pouch fills out.
- S4 [core] The pouch stands up.
- S5 [minor] Steam rises from its opening.
- S6 [minor] The pour comes first and the swelling follows.

**PC**
- P1 [core · shape_identity]
  - expect: The pouch stays one bag whose flat sides bow out as it fills and which stands on its base once full.
  - fail: The pouch keeps its flat collapsed shape while plainly full and standing; or the pouch swells into a ball far larger than its seams allow; or the pouch splits into separate bags; or the pouch turns into another object.
- P2 [core · process_direction]
  - expect: The pouch only fills and rises while the water goes in and does not collapse again with the water in it.
  - fail: The pouch collapses flat again while still full; or the pouch fills and flattens in turn; or the pouch stands up before any water is poured; or the water's level drops while pouring goes on.
- P3 [major · gravity_direction]
  - expect: The water falls downward from the kettle into the pouch, lies in its base and the steam rises from the opening.
  - fail: The water travels upward from the kettle; or the water gathers at the pouch's top and stays; or the steam pours downward out of the opening; or the pouch rises off the ground as it fills.
- P4 [major · material_response]
  - expect: The pouch is a limp foil bag that creases and bulges and holds the water, and the water is a thin liquid that finds its level.
  - fail: The pouch stays a rigid box as it fills; or the pouch stretches like elastic; or the water stands in a heap above the pouch's opening; or the pouch sets hard once full.
- P5 [fatal · permanence_count]
  - expect: One pouch and one pour; the water goes from the kettle into the pouch and nowhere else.
  - fail: Water appears in the pouch with no stream reaching it; or the water passes through the pouch's wall; or a second pouch appears; or the pouch vanishes.
- P6 [minor · attribute_drift]
  - expect: The pouch's printing, the kettle and the surroundings stay the same.
  - fail: The pouch's printing changes; or the kettle changes shape; or items around the pouch rearrange.

## HEAT-0187 · heat_response · train

**Caption.** A hairdryer is aimed at a wet patch on a bathroom mirror, and the patch shrinks from its edges.

**Expectation (hidden).** The dry area spreads from where the warm air hits and the border of the wet patch retreats inward; the patch does not grow or reappear where it has dried.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A wet patch lies on a bathroom mirror.
- S2 [core] A hairdryer is aimed at the patch.
- S3 [core] The patch shrinks.
- S4 [core] The patch's border moves inward.
- S5 [minor] The dry area spreads from where the warm air hits.
- S6 [minor] The drying comes first at the patch's edges.

**PC**
- P1 [core · process_direction]
  - expect: The patch only shrinks while the dryer plays on it and dried glass stays dry.
  - fail: The patch grows while the dryer plays on it; or a dried part of the glass goes wet again with nothing wetting it; or the patch shrinks and grows in turn; or the patch shrinks before the dryer is aimed at it.
- P2 [core · permanence_count]
  - expect: The water goes by drying from the patch's edge inward and does not appear elsewhere on the glass.
  - fail: A new wet patch appears on dry glass; or the patch jumps to a new place on the mirror; or the patch vanishes at a stroke while still large; or the patch shrinks while a matching patch grows beside it.
- P3 [major · missing_consequence]
  - expect: The drying starts where the warm air hits and spreads from there, while glass the dryer does not reach stays wet.
  - fail: The patch dries from its far side while the dryer plays on its near side; or the whole mirror dries at once while the dryer plays on one spot; or the dryer plays on the patch and it stays as wet as before to the end of the clip.
- P4 [major · gravity_direction]
  - expect: Any water the air pushes runs downward on the glass and gathers at the mirror's lower edge.
  - fail: A run travels up the mirror; or a drop leaves the glass and rises; or water gathers along the mirror's top edge and stays; or the pushed water hangs in the air beside the glass.
- P5 [fatal · shape_identity]
  - expect: One mirror in its frame; the mirror keeps its shape and the dryer stays outside the glass.
  - fail: The mirror changes shape; or the dryer passes into the glass; or a second mirror appears; or the frame vanishes.
- P6 [minor · attribute_drift]
  - expect: The frame, the bathroom fittings and the room behind stay the same.
  - fail: The frame changes colour; or the fittings move; or the room behind changes between frames.

## HEAT-0188 · heat_response · train

**Caption.** Wet footprints on a sun-baked pool deck dry in the heat, shrinking and fading from their edges.

**Expectation (hidden).** Each print fades from its thin edges inward, the dark wet area getting smaller and lighter; prints do not darken, spread, or reappear once gone.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] Wet footprints lie on a pool deck.
- S2 [core] The prints shrink.
- S3 [core] The prints fade from their edges inward.
- S4 [minor] The deck reads as sun-baked: bright and dry around the prints.
- S5 [minor] The dark wet area gets smaller and lighter.

**PC**
- P1 [core · process_direction]
  - expect: Each print only shrinks and lightens from its thin edges inward and does not darken or spread again.
  - fail: A print darkens again with nothing wetting it; or a print spreads outward; or a print fades and then returns; or the prints go from pale to dark.
- P2 [core · permanence_count]
  - expect: The prints go by drying, in place, and no new prints appear on the dry deck.
  - fail: A new print appears on dry deck with nobody walking there; or a print jumps to a new place on the deck; or a print vanishes at a stroke while still dark and wet; or the prints multiply.
- P3 [major · missing_consequence]
  - expect: The deck under each print is a shade darker while it is wet and matches the dry deck once the print is gone.
  - fail: A print's area stays dark after the print has plainly dried; or the deck around an untouched print goes as dark as the print; or the prints show no difference from the dry deck at all.
- P4 [major · gravity_direction]
  - expect: The prints lie flat on the deck and any water in them soaks in or runs downhill on a slope.
  - fail: The water in a print rises off the deck as beads that hang; or a print's water runs uphill across the deck; or a print lifts off the deck as a film; or the water in a print stands as a dome.
- P5 [fatal · shape_identity]
  - expect: One deck; the prints stay flat marks on it and the deck keeps its surface.
  - fail: A print becomes a hole in the deck; or the deck's surface opens up; or a print turns into another shape such as a hand print; or the deck changes into water.
- P6 [minor · attribute_drift]
  - expect: The deck's colour and texture away from the prints and the surroundings stay the same.
  - fail: The deck changes colour; or its texture changes pattern; or items around the deck rearrange.

## HEAT-0189 · heat_response · train

**Caption.** An egg is cracked into a hot frying pan, and the clear white turns opaque white from the edges inward.

**Expectation (hidden).** The white sets and whitens first where it touches the hot pan and the change spreads inward while the yolk stays yellow and domed; the set white does not turn clear again and the egg does not slide around as one piece before it sets.

**Declared violation types.** process_direction, attribute_drift

**SA**
- S1 [core] An egg is cracked into a hot frying pan.
- S2 [core] The white spreads in the pan.
- S3 [core] The white turns from clear to opaque.
- S4 [core] The change spreads from the edges inward.
- S5 [minor] The yolk stays yellow and domed.
- S6 [minor] The cracking comes first and the whitening follows.

**PC**
- P1 [core · process_direction]
  - expect: The whitening only advances inward and the set white does not turn clear again.
  - fail: A set white part turns clear again in the hot pan; or the whitening spreads and then retreats; or the whole raw egg slides about the pan as one piece before any of it has set; or the change starts at the yolk and works outward to the pan's edge.
- P2 [core · attribute_drift]
  - expect: The change from clear to opaque happens in the white where it touches the hot pan, and the yolk stays yellow and domed.
  - fail: The yolk turns white while the white stays clear; or the pan's surface changes colour rather than the egg; or the white is opaque before the egg is cracked; or the white goes opaque all at once with no spreading edge.
- P3 [major · gravity_direction]
  - expect: The white spreads outward and downhill over the pan's floor and the yolk sits on it.
  - fail: The white climbs the pan's wall and stays; or the yolk rises off the white and hangs; or the white runs uphill; or the yolk sinks through the white and out below the pan.
- P4 [major · material_response]
  - expect: The raw white is a thin runny liquid that spreads, the set white is a soft solid that holds its shape, and the yolk stays a soft dome.
  - fail: The raw white stands as a rigid dome as it is poured; or the set white runs off a tilted pan as a liquid; or the yolk shatters; or the set white stretches like elastic.
- P5 [fatal · permanence_count]
  - expect: One egg in one pan; the white and yolk stay one each and the shell stays outside.
  - fail: A second yolk appears; or the yolk vanishes; or the white passes through the pan's floor; or a shell piece falls into the pan and vanishes.
- P6 [minor · attribute_drift]
  - expect: The pan, the hob and the shell stay the same.
  - fail: The pan changes colour; or its handle changes shape; or items around the hob rearrange.

**Note.** The white turning opaque is the caption's asserted outcome; the chemistry of it is not judged, only that the change runs one way and starts where the egg meets the pan.

## HEAT-0190 · heat_response · train

**Caption.** A drop of food colouring falls into each of two glasses side by side, one of hot water and one of cold, and the colour spreads through the hot water while it sinks in a thin thread in the cold.

**Expectation (hidden).** In the hot glass the colour billows and spreads through the whole glass within seconds; in the cold glass it sinks as a thread and lingers near the bottom; the cold glass does not colour faster than the hot one.

**Declared violation types.** process_direction, causeless_motion

**SA**
- S1 [core] Two glasses of water stand side by side.
- S2 [core] One glass reads as hot and the other as cold: steam, ice or condensation shows which.
- S3 [core] A drop of colouring falls into each glass.
- S4 [core] The colour spreads through the hot glass.
- S5 [core] In the cold glass the colour sinks as a thin thread.
- S6 [minor] The two drops fall at about the same moment.

**PC**
- P1 [core · process_direction]
  - expect: The colour in each glass only spreads further and the water does not clear again; the difference between the two does not reverse.
  - fail: A glass's water clears again while the colour stays in it; or the colour gathers back into a drop; or the cold glass colours through more fully than the hot one; or the colour spreads and shrinks in turn.
- P2 [core · causeless_motion]
  - expect: The colour moves with the water's own currents: it billows in the hot glass and sinks in a slow thread in the cold one, and it does not dart about.
  - fail: The colour darts across a glass in a straight line and stops dead; or the colour swirls hard in the still cold glass while the hot glass's colour hangs at the top; or the colour climbs out of the water; or the colour moves in a fixed pattern that repeats exactly in both glasses.
- P3 [major · gravity_direction]
  - expect: Each drop falls downward into its glass and the thread in the cold glass sinks toward the bottom.
  - fail: A drop travels upward from the dropper; or the thread in the cold glass rises to the surface and stays; or a drop hangs in the air above a glass; or the colour in the cold glass gathers at the top and stays.
- P4 [major · missing_consequence]
  - expect: The drops show their arrival: each surface dimples and ripples where its drop lands.
  - fail: A drop enters and its surface stays glassy; or a surface ripples before its drop reaches it; or the ripples appear in the glass the drop did not enter.
- P5 [fatal · permanence_count]
  - expect: Two glasses and two drops; the colour in each glass came from its own drop and neither level jumps.
  - fail: Colour appears in a glass with no drop falling into it; or a glass's level jumps with nothing added; or a third glass appears; or colour passes through a glass's wall.
- P6 [minor · attribute_drift]
  - expect: The glasses' shapes, the table and the dropper stay the same.
  - fail: A glass changes shape; or the table's setting rearranges; or the dropper changes colour.

## HEAT-0191 · heat_response · train

**Caption.** A glass thermometer is lowered into a mug of hot water, and its red column climbs.

**Expectation (hidden).** The column starts rising as soon as the bulb is in the water, climbs steadily and slows as it settles; it does not fall, jump, or move before the bulb is wet.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] A glass thermometer.
- S2 [core] The thermometer is lowered into a mug of hot water.
- S3 [core] Its red column climbs.
- S4 [minor] The column slows as it settles.
- S5 [minor] The bulb is in the water.
- S6 [minor] The lowering comes first and the climbing follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The column starts to rise once the bulb is in the water and not before.
  - fail: The column rises before the bulb reaches the water; or the bulb sits in the hot water and the column stays where it was to the end of the clip; or the column rises while the thermometer is held in the air; or the column falls as the bulb enters the hot water.
- P2 [core · process_direction]
  - expect: The column only rises while the bulb stays in the hot water and then holds; it does not fall back while the water stays hot.
  - fail: The column falls back while the bulb stays in the hot water; or the column rises and falls in turn; or the column jumps up and down between frames; or the column rises past the tube's top and out of it.
- P3 [major · material_response]
  - expect: The column is a continuous thread of liquid in the tube that moves along it, and the glass stays rigid.
  - fail: The column breaks into separate beads that move apart; or the column moves as a solid rod that sticks out of the tube; or the glass bends in the hot water; or the column spreads sideways to fill the tube unevenly.
- P4 [major · gravity_direction]
  - expect: The thermometer hangs or stands in the mug with its bulb down and the water lies level around it.
  - fail: The thermometer floats out of the water and hangs above it; or the water climbs the thermometer's tube and stays; or the water's surface tilts and stays tilted with the mug level; or the thermometer rises bulb first out of the mug.
- P5 [fatal · permanence_count]
  - expect: One thermometer in one mug; the glass stays whole and the column stays inside it.
  - fail: The thermometer breaks and the liquid spills; or a second thermometer appears; or the column's liquid passes out through the glass; or the thermometer passes through the mug's wall.
- P6 [minor · attribute_drift]
  - expect: The thermometer's scale, the mug and the surroundings stay the same.
  - fail: The scale's markings change; or the mug changes pattern; or items around the mug rearrange.

**Note.** How far the column climbs is not judged, only that it rises after the bulb is wetted and does not fall back.

## HEAT-0192 · heat_response · train

**Caption.** A limp balloon is stretched over the neck of an empty glass bottle, and the bottle is set in a bowl of hot water; the balloon begins to stand up and inflate.

**Expectation (hidden).** The balloon lifts and swells slowly once the bottle is in the hot water and not before; it does not shrink or fill instantly.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A limp balloon is stretched over the neck of a bottle.
- S2 [core] The bottle is set in a bowl of hot water.
- S3 [core] The balloon lifts and stands up.
- S4 [core] The balloon swells.
- S5 [minor] The balloon is limp before the bottle goes into the water.
- S6 [minor] The setting in comes first and the swelling follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The balloon lifts and swells once the bottle stands in the hot water and not before.
  - fail: The balloon is standing and swollen before the bottle is in the water; or the bottle sits in the hot water and the balloon stays flat against the neck to the end of the clip; or the balloon swells while the bottle stands on the dry counter; or the balloon sags as the bottle enters the hot water.
- P2 [core · process_direction]
  - expect: The swelling only advances while the bottle stays in the hot water and the balloon does not sag back.
  - fail: The balloon sags back flat while the bottle stays in the hot water; or the balloon swells and shrinks in turn; or the balloon swells all at once in a single frame; or the balloon stays fully swollen after the bottle is lifted into cold air and left.
- P3 [major · gravity_direction]
  - expect: The balloon rises above the neck and the bottle stands in the water with the water level around it.
  - fail: The balloon hangs downward from the neck while swollen; or the bottle floats up out of the bowl; or the water climbs the bottle's outside and stays; or the balloon lifts the bottle out of the water.
- P4 [major · material_response]
  - expect: The balloon is a thin elastic skin that stretches smooth as it fills and stays gripped on the neck, and the bottle stays rigid glass.
  - fail: The balloon stays limp and wrinkled while plainly full; or the balloon stays rigid as it rises; or the bottle's glass bulges as the balloon fills; or the balloon slides off the neck and stays inflated in the air.
- P5 [fatal · permanence_count]
  - expect: One balloon on one bottle in one bowl; the balloon stays on the neck and the bottle stays whole.
  - fail: A second balloon appears; or the balloon vanishes; or the balloon passes into the bottle; or the bottle passes through the bowl's wall.
- P6 [minor · attribute_drift]
  - expect: The balloon's colour, the bottle's label and the bowl stay the same.
  - fail: The balloon changes colour; or the label changes; or the bowl changes pattern.

## HEAT-0193 · heat_response · train

**Caption.** Boiling water is poured into a thick glass tumbler taken straight from the fridge, and the glass cracks with a sharp snap.

**Expectation (hidden).** The crack appears within moments of the hot water going in and runs through the glass, which may split and leak; the glass does not stay whole or heal.

**Declared violation types.** material_response, permanence_count

**SA**
- S1 [core] A glass tumbler that reads as cold: frost or condensation on it.
- S2 [core] Boiling water is poured into the tumbler.
- S3 [core] A crack appears in the glass.
- S4 [core] The crack runs through the glass.
- S5 [minor] The glass may split and leak.
- S6 [minor] The pour comes first and the crack follows.

**PC**
- P1 [core · material_response]
  - expect: The glass is a brittle solid: a crack runs through it as a sharp line and the glass stays rigid, splitting rather than bending.
  - fail: The glass bends or sags instead of cracking; or the glass stretches as the water goes in; or the glass crumbles to powder; or the crack closes and the glass flexes back.
- P2 [core · permanence_count]
  - expect: The crack stays in the glass and any pieces stay as pieces; the glass does not heal.
  - fail: The crack closes and the glass is whole again; or a piece that fell away reappears joined to the glass; or a second tumbler appears; or the glass vanishes.
- P3 [major · missing_consequence]
  - expect: The crack appears after the hot water goes in and any water leaks out through the split.
  - fail: The crack appears before the water reaches the glass; or the water goes in and the glass stays whole and unmarked to the end of the clip; or the glass splits open and the water stays in it with no leak.
- P4 [major · gravity_direction]
  - expect: The water falls downward into the tumbler and any leak runs down its outside and pools below.
  - fail: The water travels upward from the kettle; or a leak runs up the glass; or the water climbs the glass's wall and stays above its level; or the leak hangs in the air beside the glass.
- P5 [fatal · shape_identity]
  - expect: One tumbler; it stays a tumbler as it cracks and does not turn into another material.
  - fail: The glass melts and drips; or the glass turns into another object; or the glass's shape changes without breaking; or the glass becomes a fabric that folds.
- P6 [minor · attribute_drift]
  - expect: The counter, the kettle and the surroundings stay the same.
  - fail: The counter changes pattern; or the kettle changes shape; or items around the glass rearrange.

## HEAT-0194 · heat_response · train

**Caption.** Pancake batter is poured onto a hot griddle, and the pale liquid sets from the edge inward while small bubbles rise through its top.

**Expectation (hidden).** The batter stops spreading and turns matte from the outside in, bubbles form and burst on the upper side, and the underside browns; the set part does not turn back to liquid.

**Declared violation types.** process_direction, material_response

**SA**
- S1 [core] Pancake batter is poured onto a hot griddle.
- S2 [core] The batter spreads into a round.
- S3 [core] The batter sets from its edge inward.
- S4 [core] Small bubbles rise and burst on its upper side.
- S5 [minor] The set part turns matte.
- S6 [minor] The pour comes first and the setting follows.

**PC**
- P1 [core · process_direction]
  - expect: The setting only advances inward from the edge and the set part does not turn back to liquid.
  - fail: A set part turns back to glossy liquid on the hot griddle; or the setting spreads and then retreats; or the batter sets from its centre outward to the edge; or the batter sets and softens in turn.
- P2 [core · material_response]
  - expect: The batter arrives as a thick liquid that spreads and levels and becomes a soft solid that holds its shape and can be lifted.
  - fail: The batter runs as thin as water over the griddle; or the batter stays a glossy liquid while being lifted whole; or the set pancake shatters; or the batter stands as a rigid dome as it is poured.
- P3 [major · gravity_direction]
  - expect: The batter spreads outward and downhill over the griddle and the bubbles rise to its upper surface and burst there.
  - fail: The batter climbs the griddle's raised edge and stays; or the bubbles sink through the batter to the griddle; or a bubble rises off the pancake and floats; or the batter runs uphill.
- P4 [major · missing_consequence]
  - expect: The batter sets where it touches the hot metal first: its underside and rim firm up while the middle is still wet.
  - fail: The middle of the top sets while the rim is still liquid; or the pancake's underside stays wet and glossy while its top has set; or the batter sits on the griddle and stays fully liquid to the end of the clip.
- P5 [fatal · permanence_count]
  - expect: One pour makes one pancake; the batter stays on the griddle and nothing appears or vanishes.
  - fail: A second pancake appears with nothing poured; or the pancake vanishes; or batter passes through the griddle; or the pancake grows with no batter added.
- P6 [minor · attribute_drift]
  - expect: The griddle, the jug and the surroundings stay the same.
  - fail: The griddle changes colour; or the jug changes shape; or items around the griddle rearrange.

**Note.** The underside browning as it cooks is chemistry and is not judged.

## HEAT-0195 · heat_response · train

**Caption.** Grey raw shrimp are dropped into a hot pan, and they curl and turn pink.

**Expectation (hidden).** Each shrimp tightens into a curve and its colour changes from translucent grey to opaque pink within seconds; the change starts on the side touching the pan and does not reverse.

**Declared violation types.** attribute_drift, process_direction

**SA**
- S1 [core] Grey raw shrimp are dropped into a hot pan.
- S2 [core] Each shrimp tightens into a curve.
- S3 [core] The shrimp turn from grey to pink.
- S4 [minor] The change starts on the side touching the pan.
- S5 [minor] The shrimp look translucent at the start.
- S6 [minor] The drop comes first and the curling follows.

**PC**
- P1 [core · process_direction]
  - expect: The curling and the colour change only advance and do not reverse.
  - fail: A curled shrimp straightens out again in the hot pan; or a pink shrimp turns grey again; or the shrimp curl and uncurl in turn; or the colour change spreads and then retreats.
- P2 [core · attribute_drift]
  - expect: The change is in the shrimp themselves, starting on the side touching the pan and spreading through each one.
  - fail: The pan's surface changes colour rather than the shrimp; or a shrimp turns pink on its upper side while the side on the metal stays grey; or the shrimp are pink before they reach the pan; or the shrimp all change colour in a single frame with no spreading.
- P3 [major · shape_identity]
  - expect: Each shrimp stays one shrimp that draws into a tighter curve, keeping its tail and body.
  - fail: A shrimp splits into pieces with nothing cutting it; or the shrimp fuse into one mass; or a shrimp curls into a closed ring with no seam; or a shrimp turns into another object.
- P4 [major · gravity_direction]
  - expect: The shrimp rest in the pan and any juices run to its low places.
  - fail: A shrimp lifts off the pan and hangs; or the juices climb the pan's wall and stay; or a shrimp rolls uphill in a tilted pan; or the juices gather on top of a shrimp and stay.
- P5 [fatal · permanence_count]
  - expect: The shrimp keep their number in the pan and none appears or vanishes.
  - fail: A shrimp vanishes; or a new shrimp appears in the pan; or two shrimp merge into one; or a shrimp passes through the pan's floor.
- P6 [minor · attribute_drift]
  - expect: The pan, the hob and the surroundings stay the same.
  - fail: The pan changes colour; or its handle changes shape; or items around the hob rearrange.

**Note.** The shrimp's colour change is the caption's asserted outcome; the chemistry of it is not judged, only that it runs one way and starts where the shrimp meet the pan.

## HEAT-0196 · heat_response · train

**Caption.** An iron rod rests with one end buried in the glowing coals of a forge, and the buried end begins to glow dull red and brightens toward orange.

**Expectation (hidden).** The glow appears only on the part in the coals and spreads a short way along the rod; it grows brighter over time; the far end stays dark and the rod does not glow before it is heated.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] An iron rod rests with one end in the glowing coals of a forge.
- S2 [core] The buried end begins to glow.
- S3 [core] The glow brightens.
- S4 [core] The glow spreads a short way along the rod.
- S5 [minor] The far end of the rod stays dark.
- S6 [minor] The rod is dark before it is in the coals.

**PC**
- P1 [core · process_direction]
  - expect: The glow only brightens and spreads a little while the end stays in the coals; it does not fade or retreat.
  - fail: The glow fades while the end stays buried in the coals; or the glow brightens and dims in turn; or the glowing part goes dark and glows again; or the glow spreads to the far end and then retreats.
- P2 [core · missing_consequence]
  - expect: The glow appears only on the part in the coals and spreads a short way out of them, while the rest of the rod stays dark.
  - fail: The glow appears at the rod's far end away from the coals; or the whole rod glows evenly including the end held clear; or the rod's buried end stays dark while the coals glow around it to the end of the clip; or the glow appears before the rod is in the coals.
- P3 [major · material_response]
  - expect: The rod stays a rigid bar that keeps its shape while glowing and can be moved as one piece.
  - fail: The glowing end sags or droops with nothing bending it; or the rod drips as a liquid; or the rod bends into a curve by itself; or the rod swells where it glows.
- P4 [major · gravity_direction]
  - expect: The rod rests on the coals or the forge's edge and any sparks or smoke from the coals rise.
  - fail: The rod lifts off the coals and hangs in the air; or sparks fall through the forge and lie glowing below; or the smoke sinks and pools around the forge; or the rod floats above the fire.
- P5 [fatal · permanence_count]
  - expect: One rod and one bed of coals; the rod stays one bar and the coals keep their number.
  - fail: The rod vanishes; or a second rod appears; or the rod passes through the forge's floor; or a coal vanishes leaving no ash.
- P6 [minor · attribute_drift]
  - expect: The forge's body, the coals' bed and the surroundings stay the same.
  - fail: The forge changes colour; or the coals rearrange away from the rod; or items around the forge rearrange.

**Note.** How bright the glow gets is not judged, only that it brightens one way and appears where the rod is in the coals.

## HEAT-0197 · heat_response · train

**Caption.** A layer of white sugar in a dry pan over heat melts from the edges into a clear liquid that turns amber and then deep brown.

**Expectation (hidden).** The melting starts at the edges and works inward, the liquid darkens steadily from clear to amber to brown with thin smoke at the end; the colour never lightens and the liquid does not turn back into grains.

**Declared violation types.** process_direction, attribute_drift

**SA**
- S1 [core] A layer of white sugar lies in a dry pan over heat.
- S2 [core] The sugar melts from the edges inward.
- S3 [core] The melt is a clear liquid.
- S4 [core] The liquid darkens to amber and then deep brown.
- S5 [minor] Thin smoke may rise at the end.
- S6 [minor] The melting comes first and the darkening follows.

**PC**
- P1 [core · process_direction]
  - expect: The melting only advances inward from the edges and the darkening only deepens; neither reverses.
  - fail: A melted part turns back into white grains; or the melting spreads and then retreats; or the dark liquid lightens back to amber or clear; or the sugar melts at the centre first and works out to the edges.
- P2 [core · attribute_drift]
  - expect: The colour change happens in the liquid itself and runs one way from clear to amber to brown.
  - fail: The pan's surface changes colour rather than the sugar; or the liquid is brown before any sugar has melted; or the liquid's colour goes back and forth between amber and brown; or the dry grains turn brown while still unmelted.
- P3 [major · gravity_direction]
  - expect: The melted sugar runs to the pan's low places and spreads across its floor, and any smoke rises.
  - fail: The melt climbs the pan's wall and stays; or a run travels uphill; or melted sugar lifts off the pan; or the smoke sinks over the rim and pools on the hob.
- P4 [major · material_response]
  - expect: The sugar goes from loose dry grains to a thick glossy liquid that flows slowly and levels.
  - fail: The melt runs as thin as water; or the grains stay dry and separate while the layer flows; or the melt sets solid in the hot pan; or the liquid stands as a rigid dome.
- P5 [fatal · permanence_count]
  - expect: The sugar in the pan is the sugar that was there; it melts rather than appearing or vanishing.
  - fail: Sugar appears in the pan with none added; or the layer vanishes at a stroke; or a second pan appears; or the melt passes through the pan's floor.
- P6 [minor · attribute_drift]
  - expect: The pan's finish, the hob and the surroundings stay the same.
  - fail: The pan changes colour; or its handle changes shape; or items around the hob rearrange.

**Note.** The sugar's browning is the caption's asserted outcome; the chemistry of it is not judged, only that the colour runs one way and the melting starts at the edges.

## HEAT-0198 · heat_response · train

**Caption.** A flat bag of microwave popcorn lies in a running microwave, and the bag swells and puffs up as popping begins inside.

**Expectation (hidden).** The bag stays flat at first, then rises and rounds out while the pops come faster; it does not inflate before the popping starts or flatten while the popping goes on.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A flat bag of popcorn lies in a running microwave.
- S2 [core] The bag stays flat at first.
- S3 [core] The bag rises and rounds out.
- S4 [core] Popping happens inside as it swells.
- S5 [minor] The pops come faster as the bag fills.
- S6 [minor] The bag stays flat before the popping starts.

**PC**
- P1 [core · missing_consequence]
  - expect: The bag stays flat until popping starts inside it and then rises with it; it does not inflate before any pop.
  - fail: The bag is fully puffed before any popping shows; or the bag stays flat while pops plainly shake it to the end of the clip; or the bag flattens while the popping goes on; or the bag swells with the microwave off and still.
- P2 [core · shape_identity]
  - expect: The bag stays one bag whose flat sides bow out and whose folds open as it fills, keeping its printed faces.
  - fail: The bag swells into a smooth sphere with no folds or seams; or the bag splits into separate bags; or the bag turns into another object; or the bag keeps its sharp flat creases while plainly full and round.
- P3 [major · gravity_direction]
  - expect: The bag rises upward off the turntable's floor as it fills and stays on the turntable.
  - fail: The bag swells downward into the turntable; or the bag lifts off the turntable and hangs in the air; or the bag sinks as it fills; or the bag rises and sticks to the microwave's roof.
- P4 [major · process_direction]
  - expect: The bag only fills while the popping goes on and the pops grow more frequent and then ease; the bag does not deflate mid-way.
  - fail: The bag deflates and inflates again while the popping goes on; or the popping stops and starts again with the microwave running steadily; or the bag's size jumps between frames; or the popped bag flattens to its first shape with the microwave still running.
- P5 [fatal · permanence_count]
  - expect: One bag in one microwave; the bag stays inside and nothing passes through it.
  - fail: Popcorn appears outside the sealed bag; or a second bag appears; or the bag passes through the microwave's door; or the bag vanishes.
- P6 [minor · attribute_drift]
  - expect: The bag's printing, the turntable and the microwave's interior stay the same.
  - fail: The bag's printing changes; or the turntable changes shape; or the interior changes.

**Note.** The pops are sound; they are read from the bag jumping and from its filling.

## HEAT-0199 · heat_response · train

**Caption.** A cold egg is lowered into a pot of boiling water, and its shell cracks and a thread of white leaks out and sets into a pale wisp.

**Expectation (hidden).** The crack appears after the egg is in the water, the white streams out through it and turns opaque and solid in the hot water; the wisp does not dissolve or go back into the shell.

**Declared violation types.** material_response, permanence_count

**SA**
- S1 [core] An egg is lowered into a pot of boiling water.
- S2 [core] The shell cracks.
- S3 [core] A thread of white leaks out through the crack.
- S4 [core] The white sets into a pale wisp in the water.
- S5 [minor] The crack appears after the egg is in the water.
- S6 [minor] The wisp trails from the crack.

**PC**
- P1 [core · material_response]
  - expect: The leaking white is a runny liquid that streams out and becomes an opaque soft solid trailing in the water.
  - fail: The leaking white stays clear and runny in the boiling water to the end of the clip; or the white sets into a hard brittle shard; or the white dissolves away into the water; or the white stretches like elastic.
- P2 [core · permanence_count]
  - expect: The white in the water came out through the crack and stays as a wisp; it does not return to the shell or appear elsewhere.
  - fail: The wisp draws back into the shell; or a wisp appears in the water away from the egg with none leaking there; or the wisp vanishes; or a second egg appears.
- P3 [major · process_direction]
  - expect: The crack only opens and the white only leaves; the shell does not heal.
  - fail: The crack closes and the shell is whole again; or the white leaks and is drawn back in turn; or the crack appears before the egg reaches the water; or the set wisp turns clear again.
- P4 [major · gravity_direction]
  - expect: The egg sinks in the water, the wisp trails and drifts with the boil, and bubbles rise.
  - fail: The egg rises out of the water and hangs above it; or the wisp rises out of the water and stays above the surface; or bubbles sink toward the pot's floor; or the egg hangs motionless in mid-water while the boil churns around it.
- P5 [fatal · shape_identity]
  - expect: One egg with one shell; the shell stays a shell that cracks and the pot keeps its shape.
  - fail: The shell melts; or the egg turns into another object; or the shell peels away entirely leaving a bare egg; or the egg passes through the pot's wall.
- P6 [minor · attribute_drift]
  - expect: The pot, the hob and the water stay the same.
  - fail: The pot changes colour; or the water turns a colour; or items around the hob rearrange.

## HEAT-0200 · heat_response · train

**Caption.** An inflated balloon drifts down onto a burning candle, and it bursts the instant the flame touches it.

**Expectation (hidden).** The balloon is whole until it meets the flame and disappears into shreds at that instant; the candle keeps burning; the balloon does not float through the flame or deflate slowly.

**Declared violation types.** material_response, missing_consequence

**SA**
- S1 [core] An inflated balloon drifts down toward a burning candle.
- S2 [core] The balloon meets the flame.
- S3 [core] The balloon bursts.
- S4 [core] The candle keeps burning afterwards.
- S5 [minor] Shreds or fragments show where the balloon was.
- S6 [minor] The contact comes first and the burst follows.

**PC**
- P1 [core · material_response]
  - expect: The balloon is a stretched elastic skin that bursts at once rather than deflating or melting slowly.
  - fail: The balloon deflates slowly through a hole and sags; or the balloon melts and drips onto the candle; or the balloon bounces off the flame and stays whole; or the balloon shrinks away to nothing without bursting.
- P2 [core · missing_consequence]
  - expect: The balloon is whole until it meets the flame and bursts at that moment.
  - fail: The balloon bursts before it reaches the flame; or the balloon rests on the flame and stays whole to the end of the clip; or the balloon passes through the flame and drifts on unchanged; or the balloon bursts while the candle is out.
- P3 [major · gravity_direction]
  - expect: The balloon drifts downward onto the candle, any shreds fall afterwards, and the flame points upward.
  - fail: The balloon rises away from the candle with nothing lifting it; or shreds rise and stay aloft; or the flame points downward; or shreds hang in the air where the balloon was.
- P4 [major · process_direction]
  - expect: Once burst the balloon stays burst and the candle keeps burning.
  - fail: Shreds gather back into a whole balloon; or the balloon fills out again; or the candle's flame goes out and relights by itself; or the burst repeats with nothing new arriving.
- P5 [fatal · permanence_count]
  - expect: One balloon and one candle; the candle keeps its wick and flame and nothing passes through the table.
  - fail: A second balloon appears; or the candle vanishes; or the flame detaches from the wick and floats; or a shred passes through the table.
- P6 [minor · attribute_drift]
  - expect: The candle's colour, the holder and the surroundings stay the same.
  - fail: The candle changes colour; or the holder changes shape; or a shred is a different colour from the balloon.

**Note.** The bang is sound and is not judged. Whether the shreds stay in view is not required; what is judged is that the balloon goes at the moment of contact.

## HEAT-0251 · melt_freeze · eval

**Caption.** A slice of cheese is laid on a hot dog straight off the grill, and the cheese softens and slumps over the sides.

**Expectation (hidden).** The slice loses its stiff edges and drapes down over the sausage; it does not stay square or re-harden on the hot surface.

**Declared violation types.** process_direction, material_response

**SA**
- S1 [core] A slice of cheese lies on a hot dog.
- S2 [core] The cheese softens: it goes glossy and loses its stiff edges.
- S3 [core] The cheese drapes down over the sausage's sides.
- S4 [minor] The slice is square-edged at the start.
- S5 [minor] The softening comes first and the draping follows.

**PC**
- P1 [core · process_direction]
  - expect: The cheese only softens and drapes further and does not stiffen again on the hot sausage.
  - fail: The slice regains its square edges; or the drape pulls back up onto the sausage's top; or the cheese sets firm and matt again on the hot sausage; or the cheese alternates between stiff and slack.
- P2 [core · material_response]
  - expect: The cheese is a thin sheet that softens, stretches and hangs over the sausage's curve while staying one piece.
  - fail: The slice keeps its flat stiff shape while draped over the curve; or the cheese runs off as thin as water; or the slice shatters dry; or the cheese stretches into a thread that snaps back like elastic.
- P3 [major · gravity_direction]
  - expect: The softened cheese hangs downward over the sides and any drip runs down to the bun or the plate.
  - fail: The cheese drapes upward away from the sausage; or a drip climbs the sausage; or melted cheese gathers on the slice's top and stays; or a drip leaves the cheese and floats.
- P4 [major · missing_consequence]
  - expect: The cheese softens where it touches the hot sausage: it goes glossy from underneath and moulds to the sausage's shape.
  - fail: The cheese softens on its upper face while its underside stays stiff and matt; or the slice drapes without touching the sausage anywhere; or the slice lies on the hot sausage and stays stiff and square to the end of the clip.
- P5 [fatal · permanence_count]
  - expect: One slice on one sausage; the cheese goes only from the slice onto the sausage and the bun.
  - fail: A second slice appears; or the slice vanishes; or the slice grows; or cheese appears on the plate with none running there.
- P6 [minor · attribute_drift]
  - expect: The bun, the sausage's surface and the plate stay the same.
  - fail: The bun changes shape; or the plate changes pattern; or the sausage changes colour.

**Note.** Browning of the cheese is chemistry and is not judged.

## HEAT-0252 · melt_freeze · eval

**Caption.** A handful of gummy bears is scattered on a hot baking tray, and they soften, slump and spread into flat glossy blobs.

**Expectation (hidden).** Each bear loses its shape from the bottom up, going shiny and flattening into a wider, lower blob; the blobs do not keep sharp features, shrink upward, or firm up again on the hot tray.

**Declared violation types.** shape_identity, process_direction

**SA**
- S1 [core] Gummy bears are scattered on a baking tray.
- S2 [core] The bears soften and slump.
- S3 [core] The bears spread into flat glossy blobs.
- S4 [minor] Each bear loses its shape from the bottom up.
- S5 [minor] The bears keep their own colours.
- S6 [minor] The softening comes first and the spreading follows.

**PC**
- P1 [core · shape_identity]
  - expect: Each bear loses its ears, arms and face from the bottom upward and becomes a wider, lower blob.
  - fail: A bear keeps its sharp ears and face while flat and glossy; or a bear shrinks upward into a taller narrower shape; or a bear's features sharpen as it melts; or a bear turns into another figure.
- P2 [core · process_direction]
  - expect: The slumping only advances and the blobs do not firm up again on the hot tray.
  - fail: A blob draws back up into a standing bear; or a blob's edges pull inward and it stands taller; or the bears set firm and matt again on the hot tray; or a bear alternates between standing and slumped.
- P3 [major · gravity_direction]
  - expect: Each bear sinks downward onto the tray and its blob spreads outward and downhill.
  - fail: A bear rises off the tray; or a blob climbs the tray's rim and stays; or a blob spreads uphill on a tilted tray; or melted gummy lifts off the tray.
- P4 [major · material_response]
  - expect: The gummy softens into a thick glossy liquid that flows slowly and keeps a rounded edge.
  - fail: A blob runs as thin as water; or a bear shatters dry; or a blob stands as a rigid dome with sharp edges; or a bear stretches into a thread that snaps back like elastic.
- P5 [fatal · permanence_count]
  - expect: The bears on the tray are the bears that were scattered; none appears or vanishes.
  - fail: A bear vanishes; or a new bear appears on the tray; or a blob grows with nothing added; or a blob passes through the tray.
- P6 [minor · attribute_drift]
  - expect: Each blob keeps its bear's colour, and the tray and the surroundings stay the same.
  - fail: A blob is a different colour from its bear; or the tray changes colour; or items around the tray rearrange.

## HEAT-0253 · melt_freeze · eval

**Caption.** Snow scraped off a windshield lands on the warm bonnet of a car whose engine has just been running, and it melts into rivulets that run off the edge.

**Expectation (hidden).** The snow darkens and slumps where it touches the metal, water runs downhill off the bonnet and drips from the edge; the snow does not stay white and dry on the warm metal or refreeze there.

**Declared violation types.** process_direction, gravity_direction

**SA**
- S1 [core] Snow lands on a car's bonnet.
- S2 [core] The snow darkens and slumps where it touches the metal.
- S3 [core] Water runs across the bonnet.
- S4 [core] Water drips from the bonnet's edge.
- S5 [minor] The bonnet reads as warm: bare or wet where snow has melted.
- S6 [minor] The landing comes first and the melting follows.

**PC**
- P1 [core · process_direction]
  - expect: The snow only darkens, slumps and shrinks while the wet area grows; it does not freeze again on the warm metal.
  - fail: The snow turns white and firm again on the bonnet; or a rivulet freezes into ice on the warm metal; or the wet area shrinks while snow still sits on it; or the snow alternates between firmer and softer.
- P2 [core · gravity_direction]
  - expect: The meltwater runs downhill across the bonnet and drips from its lowest edge.
  - fail: A rivulet runs up the bonnet toward the windscreen; or water gathers at the bonnet's high edge and stays; or a drip leaves the edge and rises; or the rivulets run sideways and stay level on a sloping bonnet.
- P3 [major · missing_consequence]
  - expect: The snow melts where it touches the warm metal: it wets from underneath and the rivulets come from the slumping heap.
  - fail: The snow melts from its top while its underside stays white and dry; or rivulets run on a part of the bonnet no snow reached; or the snow slumps while the metal around it stays dry.
- P4 [major · material_response]
  - expect: The snow is a wet crumbling solid that slumps and the melt is a thin liquid that runs in streaks.
  - fail: The heap melts into a thick syrup that stands in a dome; or the snow lifts as one solid slab; or the snow bends and flows as one soft lump; or the melt beads up and rolls off without wetting the paint.
- P5 [fatal · permanence_count]
  - expect: The water on the bonnet came from the snow; the snow loses matter and gains none.
  - fail: The heap grows; or new snow appears on the bonnet with none landing; or water appears at the bonnet's edge with none running there; or the snow vanishes at a stroke while still white and deep.
- P6 [minor · attribute_drift]
  - expect: The car's paint, its badge and the surroundings stay the same.
  - fail: The car changes colour; or the badge changes; or the background changes between frames.

## HEAT-0254 · melt_freeze · eval

**Caption.** A snowball thrown against a warm sunlit window sticks for a moment, then slides down the glass as it melts, leaving a wet streak.

**Expectation (hidden).** The snow softens, slides downward, and leaves water behind; it does not climb or refreeze on the warm glass.

**Declared violation types.** process_direction, gravity_direction

**SA**
- S1 [core] A snowball hits a window.
- S2 [core] The snowball sticks to the glass for a moment.
- S3 [core] The snowball slides down the glass.
- S4 [core] A wet streak is left behind it.
- S5 [minor] The window is sunlit.
- S6 [minor] The order is hit, stick, slide, streak.

**PC**
- P1 [core · process_direction]
  - expect: The snowball only softens and shrinks and the streak only grows; nothing freezes again on the warm glass.
  - fail: The snowball regains its round firm shape; or the streak draws back into the snowball; or the wet streak freezes to frost on the sunlit glass; or the snowball alternates between firmer and softer.
- P2 [core · gravity_direction]
  - expect: The snowball slides downward on the glass, the streak runs down behind it and water gathers at the sill.
  - fail: The snowball slides up the window; or the streak runs upward above where the ball struck; or the snowball leaves the glass and rises; or water gathers along the window's top and stays.
- P3 [major · missing_consequence]
  - expect: The streak lies along the path the ball took and the glass there is wet, while glass the ball missed stays dry.
  - fail: The streak lies away from the ball's path; or the glass stays dry behind a sliding snowball; or a streak appears on a pane the ball never touched; or the streak runs ahead of the sliding ball.
- P4 [major · material_response]
  - expect: The snowball is a wet crumbling solid that flattens where it struck, sheds crumbs and shrinks, and the glass stays rigid.
  - fail: The snowball bounces off the glass like a rubber ball and stays round; or the snowball shatters into dry powder that stays on the glass; or the glass flexes where the ball struck; or the ball smears into a paste that keeps its shape.
- P5 [fatal · permanence_count]
  - expect: One snowball on one window; the snow leaves only as water and crumbs.
  - fail: The snowball vanishes at a stroke while still large; or a second snowball appears on the glass; or the snowball passes through the glass; or the streak appears with no ball sliding down it.
- P6 [minor · attribute_drift]
  - expect: The window's frame, the view through the glass and the surroundings stay the same.
  - fail: The frame changes colour; or the view through the glass jumps to a different place; or the sill changes shape.

**Note.** Who throws the snowball is not judged.

## HEAT-0255 · melt_freeze · eval

**Caption.** Morning sun falls on half of a frosted car windshield, and the frost on the sunlit half turns to droplets while the shaded half stays white.

**Expectation (hidden).** The clearing spreads only within the sunlit area, frost turning wet and then clear with drops running down; the shaded half stays frosted; frost does not re-form on the sunlit glass.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] A frosted car windshield with sunlight on part of it.
- S2 [core] The frost on the sunlit part turns to droplets.
- S3 [core] The clearing spreads within the sunlit area.
- S4 [core] The shaded part stays white with frost.
- S5 [minor] Drops run down the cleared glass.
- S6 [minor] The sunlit and shaded parts are plainly divided.

**PC**
- P1 [core · missing_consequence]
  - expect: The clearing keeps to the sunlit area and the shaded frost stays white.
  - fail: The frost clears on the shaded half while the sunlit half stays white; or the whole windshield clears at once including the shaded part; or the sunlit frost stays white and dry while the shaded part beads; or the clearing's edge lies away from the line between sun and shade.
- P2 [core · process_direction]
  - expect: The clearing only spreads within the sunlit area and cleared glass stays clear.
  - fail: Frost grows back on glass the sun has cleared; or the clear area shrinks; or the glass clears and frosts in turn; or the frost thickens on the sunlit part as the sun rises on it.
- P3 [major · gravity_direction]
  - expect: Drops that grow large enough run downward on the glass and gather at its lower edge.
  - fail: A drop runs up the windshield; or a drop leaves the glass and rises; or water gathers along the glass's top edge and stays; or a run travels sideways and stays level with the car still.
- P4 [major · material_response]
  - expect: The frost is a white crust that wets and beads before the glass is clear, and the water runs as streaks.
  - fail: The frost vanishes leaving the glass dry; or the frost lifts off as a rigid sheet and slides away; or the water beads up and rolls off without wetting the glass; or the frost turns to a hard glaze that stays dry.
- P5 [fatal · permanence_count]
  - expect: One windshield; the frost turns to water on the glass and nothing passes through it.
  - fail: The windshield changes shape; or a second windshield appears; or water passes through the glass into the car; or the frost returns all over at a stroke with the car untouched.
- P6 [minor · attribute_drift]
  - expect: The car's paint, the wipers and the surroundings stay the same.
  - fail: The car changes colour; or the wipers jump to a new position with nothing touching them; or the background changes between frames.

## HEAT-0256 · melt_freeze · eval

**Caption.** Chocolate sprinkles are scattered over hot buttered toast, and they soften and smear into dark streaks.

**Expectation (hidden).** The sprinkles lose their hard edges and go glossy where they touch the hot toast, merging into streaks; they do not stay as separate hard grains or harden again while the toast is hot.

**Declared violation types.** shape_identity, process_direction

**SA**
- S1 [core] Chocolate sprinkles are scattered over hot buttered toast.
- S2 [core] The sprinkles soften and lose their hard edges.
- S3 [core] The sprinkles smear into dark streaks.
- S4 [minor] The sprinkles go glossy where they touch the toast.
- S5 [minor] The sprinkles are separate hard grains at the start.
- S6 [minor] The softening comes first and the smearing follows.

**PC**
- P1 [core · shape_identity]
  - expect: Each sprinkle loses its stick shape from the bottom up and spreads into a low streak, and neighbouring streaks may join.
  - fail: A sprinkle keeps its sharp stick shape while glossy and spread; or a sprinkle's edges sharpen as it melts; or a sprinkle turns into a hard bead that stays whole; or the sprinkles rise into standing spikes.
- P2 [core · process_direction]
  - expect: The softening only advances and the streaks do not harden into grains again on the hot toast.
  - fail: A streak draws back into a hard sprinkle; or the sprinkles set firm and matt again on the hot toast; or the sprinkles alternate between hard and soft; or a streak's edges pull inward and it stands taller.
- P3 [major · gravity_direction]
  - expect: The melted chocolate spreads into the toast's surface and runs to its low places and off its edge.
  - fail: A streak climbs the toast's crust and stays; or melted chocolate lifts off the toast; or a streak runs uphill on a tilted slice; or the chocolate gathers on the crust's high rim and stays.
- P4 [major · missing_consequence]
  - expect: The sprinkles soften where they touch the hot toast, going glossy from underneath, and the toast's surface darkens where they lie.
  - fail: A sprinkle softens on its upper side while its underside stays matt and hard; or a streak appears on a part of the toast no sprinkle touched; or the sprinkles soften while the toast stays pale and dry under them.
- P5 [fatal · permanence_count]
  - expect: The sprinkles on the toast are the sprinkles that were scattered; none appears or vanishes.
  - fail: A sprinkle vanishes; or new sprinkles appear on the toast; or a streak grows with nothing added; or a sprinkle passes through the toast.
- P6 [minor · attribute_drift]
  - expect: The toast's crust, the plate and the surroundings stay the same.
  - fail: The toast's crust changes shape; or the plate changes pattern; or items around the plate rearrange.

## HEAT-0257 · melt_freeze · eval

**Caption.** A pot of boiling water is flung into the air on a day far below freezing, and the spray turns into a cloud of ice crystals and vapour that drifts away instead of falling as water.

**Expectation (hidden).** The arc of water breaks into a white cloud almost at once and the cloud hangs and drifts with the air; little or no liquid water reaches the ground; the cloud does not gather back into a stream.

**Declared violation types.** material_response, gravity_direction

**SA**
- S1 [core] A pot of boiling water is flung into the air.
- S2 [core] The arc of water breaks into a white cloud.
- S3 [core] The cloud hangs and drifts.
- S4 [core] Little or no liquid water reaches the ground.
- S5 [minor] The setting reads as far below freezing: snow, ice or heavy winter clothing.
- S6 [minor] The fling comes first and the cloud follows.

**PC**
- P1 [core · material_response]
  - expect: The water leaves the pot as an arc and breaks into a cloud of fine crystals and vapour rather than staying a stream of drops.
  - fail: The arc stays a solid sheet of water all the way to the ground; or the water lands as a puddle and stays liquid; or the cloud sets into a single sheet of ice in the air; or the water freezes into one solid lump in flight.
- P2 [core · gravity_direction]
  - expect: The cloud drifts and spreads with the air rather than falling as water, and what does fall settles as frost or snow.
  - fail: The cloud falls straight down as a stream of water and splashes; or the cloud rises steadily and keeps climbing out of view; or the cloud hangs as a fixed shape without drifting; or water rises from the ground back into the cloud.
- P3 [major · process_direction]
  - expect: The cloud only spreads and thins and does not gather back into a stream.
  - fail: The cloud gathers back into a stream and returns to the pot; or the cloud thickens steadily after the fling; or the crystals melt into liquid in the freezing air and pool; or the cloud spreads and then draws in again.
- P4 [major · trajectory_momentum]
  - expect: The water leaves the pot along the arm's swing, follows an arc, and the cloud carries on in that direction as it spreads.
  - fail: The water leaves the pot against the swing; or the cloud stops dead at the top of the arc; or the cloud reverses and returns along the arc; or the arc bends sideways with no sign of wind.
- P5 [fatal · permanence_count]
  - expect: One pot of water; the cloud is the water that was flung and none appears from nowhere.
  - fail: A second cloud appears away from the arc; or the cloud vanishes at a stroke while still thick; or the pot refills itself; or water appears in the air far from the arc.
- P6 [minor · attribute_drift]
  - expect: The pot, the clothing and the snowy surroundings stay the same.
  - fail: The pot changes colour; or the clothing changes colour; or the ground's snow changes texture between frames.

**Note.** Whoever flings the pot is kept because the throw is the caption's action; their form is not judged.

## HEAT-0258 · melt_freeze · eval

**Caption.** A garden sprayer mists water onto a bare branch in deep winter cold, and the mist freezes into a white glaze on the twigs within seconds.

**Expectation (hidden).** The wet twigs turn white and glassy shortly after the mist lands and the glaze thickens with more spraying; drops that formed stop running and hang as ice; the glaze does not melt off while the cold holds.

**Declared violation types.** material_response, process_direction

**SA**
- S1 [core] A sprayer mists water onto a bare branch.
- S2 [core] The wet twigs turn white and glassy.
- S3 [core] The glaze thickens with more spraying.
- S4 [minor] Drops on the twigs stop running and hang as ice.
- S5 [minor] The setting reads as deep winter cold.
- S6 [minor] The spraying comes first and the glaze follows.

**PC**
- P1 [core · material_response]
  - expect: The mist lands as fine drops that stop moving and become a hard glassy coat on the twigs, and the twigs stay rigid.
  - fail: The drops stay runny and keep dripping off in the cold; or the glaze stays a soft slush that smears; or the twigs droop and swing like rope under a thin glaze; or the glaze sets as a dry white powder that blows away.
- P2 [core · process_direction]
  - expect: The glaze only thickens with more spraying and does not melt off while the cold holds.
  - fail: The glaze melts off the twigs while the cold holds and nothing warms them; or the glaze thins between sprays; or the glaze forms and clears in turn; or the twigs are glazed before any mist reaches them.
- P3 [major · gravity_direction]
  - expect: The mist falls and drifts downward onto the twigs, drops hang from their undersides and any that fall go down.
  - fail: The mist rises from the sprayer and gathers above the branch; or the drops on the twigs hang upward from their tops; or a drop leaves a twig and rises; or a fallen drop returns to a twig.
- P4 [major · missing_consequence]
  - expect: The glaze forms where the mist lands and twigs the mist misses stay bare.
  - fail: A twig the mist never reached is glazed; or the mist lands on a twig and it stays bare and dry to the end of the clip; or the whole branch glazes at once while the mist plays on one part.
- P5 [fatal · permanence_count]
  - expect: One branch and one sprayer; the ice on the twigs is the water that was sprayed.
  - fail: Ice appears on a twig with no mist reaching it; or the glaze vanishes at a stroke; or a twig vanishes; or a second branch appears.
- P6 [minor · attribute_drift]
  - expect: The branch's bark away from the glaze, the sprayer and the surroundings stay the same.
  - fail: The bark changes colour; or the sprayer changes shape; or the background changes between frames.

## HEAT-0259 · melt_freeze · eval

**Caption.** A scoop of sorbet is set on a waffle fresh off the iron, and it slumps and runs into the squares.

**Expectation (hidden).** The scoop softens from the bottom, sinks and spreads, and coloured liquid fills the waffle's grid and runs off the edge; the scoop does not stay a firm ball or refreeze on the hot waffle.

**Declared violation types.** process_direction, gravity_direction

**SA**
- S1 [core] A scoop of sorbet sits on a waffle.
- S2 [core] The scoop softens and sinks.
- S3 [core] Coloured liquid fills the waffle's squares.
- S4 [core] Liquid runs off the waffle's edge.
- S5 [minor] The waffle is fresh off the iron.
- S6 [minor] The softening comes first and the running follows.

**PC**
- P1 [core · process_direction]
  - expect: The scoop only softens, sinks and shrinks while the liquid spreads; it does not firm up again on the hot waffle.
  - fail: The scoop regains a firm round shape; or the liquid draws back into the scoop; or the sorbet freezes hard again on the hot waffle; or the scoop alternates between firmer and softer.
- P2 [core · gravity_direction]
  - expect: The melt runs downward into the waffle's squares, fills them and runs off its lowest edge.
  - fail: The melt climbs out of a square and over a ridge uphill; or the liquid gathers on the waffle's ridges and stays; or a drip leaves the waffle and rises; or the melt runs up the scoop's side.
- P3 [major · material_response]
  - expect: The sorbet is a soft wet solid that slumps and sheds a thin coloured liquid, and the waffle stays a crisp grid that softens only where soaked.
  - fail: The waffle melts or sags with the sorbet; or the melt runs as a thick paste that keeps ridges; or the scoop shatters into dry crumbs; or the melt sets into a spike standing out from the waffle.
- P4 [major · missing_consequence]
  - expect: The melt comes from the softening scoop and wets what it passes: the waffle darkens where the liquid runs.
  - fail: Liquid fills the squares while the scoop above stays hard-edged and dry; or the waffle stays dry where liquid has run; or liquid appears in a square with none running into it.
- P5 [fatal · permanence_count]
  - expect: One scoop on one waffle; the sorbet goes only from the scoop into the squares and off the edge.
  - fail: The scoop grows; or a second scoop appears; or the scoop vanishes while still whole; or liquid appears on the plate with none running off the waffle.
- P6 [minor · attribute_drift]
  - expect: The sorbet's colour, the waffle's pattern and the plate stay the same.
  - fail: The sorbet changes colour; or the waffle's grid changes pattern; or the plate changes shape.

## HEAT-0260 · melt_freeze · eval

**Caption.** A chocolate bunny stands on a plate under a bright heat lamp, and its ears soften, droop and bend over.

**Expectation (hidden).** The parts nearest the lamp go glossy and sag first, bending downward under their own weight; the bunny does not stand back up or firm up while the lamp is on.

**Declared violation types.** process_direction, shape_identity

**SA**
- S1 [core] A chocolate bunny stands on a plate under a heat lamp.
- S2 [core] The parts nearest the lamp go glossy and soften.
- S3 [core] The ears droop.
- S4 [core] The ears bend over.
- S5 [minor] The bunny is upright with straight ears at the start.
- S6 [minor] The softening comes first and the drooping follows.

**PC**
- P1 [core · process_direction]
  - expect: The softening and drooping only advance while the lamp is on; the bunny does not stand back up or firm up again.
  - fail: A drooped ear stands back up while the lamp is on; or the ears droop and straighten in turn; or the chocolate sets firm and matt again under the lamp; or the bunny regains a shape it had lost.
- P2 [core · shape_identity]
  - expect: The bunny stays one chocolate figure whose ears bend and sag while the rest of it keeps its shape longer.
  - fail: The bunny keeps sharp straight ears while glossy and plainly bent over; or the whole bunny collapses into a puddle in a single frame; or the bunny turns into another figure; or an ear detaches and stays a whole ear.
- P3 [major · gravity_direction]
  - expect: The ears bend downward under their own weight and any drip runs down the bunny to the plate.
  - fail: An ear bends upward toward the lamp; or a drip climbs the bunny; or melted chocolate gathers on the bunny's head and stays; or an ear lifts away and hangs in the air.
- P4 [major · missing_consequence]
  - expect: The change is strongest on the parts nearest the lamp and least on the side away from it.
  - fail: The side away from the lamp softens while the near side stays firm; or the bunny softens evenly all over while the lamp is plainly on one side; or the ears droop while their surface stays matt and dry.
- P5 [fatal · permanence_count]
  - expect: One bunny on one plate; the chocolate goes only from the bunny onto the plate.
  - fail: The bunny grows; or a second bunny appears; or the bunny vanishes while still whole; or chocolate appears on the plate with no run reaching it.
- P6 [minor · attribute_drift]
  - expect: The bunny's colour, the plate and the surroundings stay the same.
  - fail: The bunny changes colour; or the plate changes shape; or items around the plate rearrange.

## HEAT-0261 · boil_steam · eval

**Caption.** Vegetables are tossed in a wok over a high flame, and a cloud of steam rises with each toss.

**Expectation (hidden).** Steam rises from the hot food and thins above the wok; each toss releases a fresh burst; it does not sink.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] Vegetables are tossed in a wok over a flame.
- S2 [core] Steam rises from the wok.
- S3 [core] Each toss releases a fresh burst of steam.
- S4 [minor] The steam thins above the wok.
- S5 [minor] The tossing comes first and each burst follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The steam leaves the wok going up and spreads and thins, and the vegetables fall back into the wok.
  - fail: The steam pours down the wok's sides and pools on the hob; or sinks below the wok; or a vegetable rises out of the wok and hangs above it; or the steam hangs as a fixed shape without rising.
- P2 [core · process_direction]
  - expect: Each burst comes with a toss and then eases, and the steam that has left keeps moving away.
  - fail: A burst comes before the toss; or the plume runs back into the wok; or a puff retreats to the food; or the bursts keep growing with no further toss.
- P3 [major · trajectory_momentum]
  - expect: The tossed vegetables leave the wok along its swing, arc up and fall back into it.
  - fail: The vegetables leave the wok against the swing; or they stop dead at the top of the arc; or they rise and keep climbing out of view; or they land outside the wok with the wok held under them.
- P4 [major · missing_consequence]
  - expect: The burst comes from the hot food and pan where the vegetables land back, and the vegetables look wet or glossy.
  - fail: The steam pours from a part of the hob away from the wok; or the vegetables are tossed and no steam appears at all; or the steam bursts from an empty part of the wok while the food sits at its other side.
- P5 [fatal · permanence_count]
  - expect: The vegetables in the wok are the vegetables that were tossed and they keep their number.
  - fail: A vegetable vanishes in mid-air; or new vegetables appear with none added; or a vegetable passes through the wok's wall; or two pieces merge into one.
- P6 [minor · attribute_drift]
  - expect: The wok, the hob and the surroundings stay the same.
  - fail: The wok changes colour; or its handle changes shape; or items around the hob rearrange.

**Note.** Who tosses the wok is not judged. The vegetables browning as they cook is chemistry and is not judged.

## HEAT-0262 · boil_steam · eval

**Caption.** A toy steam engine's boiler is heated by a small burner, and once the water boils, steam puffs from the cylinder and the flywheel begins to turn.

**Expectation (hidden).** Nothing moves until steam appears; the flywheel starts turning as the puffs begin and speeds up as the steam grows; it does not turn before the boiler is hot or keep turning after the steam stops.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A toy steam engine has a burner under its boiler.
- S2 [core] Steam puffs from the cylinder.
- S3 [core] The flywheel begins to turn.
- S4 [core] The flywheel speeds up as the puffs grow.
- S5 [minor] Nothing on the engine moves before the steam appears.
- S6 [minor] The steam comes first and the turning follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The flywheel stays still until steam puffs from the cylinder, turns while the puffs come and slows when they stop.
  - fail: The flywheel turns before any steam appears; or it keeps turning at the same rate after the steam has stopped; or it turns while the burner is out and the boiler dry; or it stops and starts again while the puffs come steadily.
- P2 [core · missing_consequence]
  - expect: The puffs and the wheel's turning go together: each puff comes as the piston moves and the wheel turns with them.
  - fail: The wheel turns while the cylinder is dry with no puff at all; or the puffs come while the wheel stands still to the end of the clip; or the puffs come from the boiler's filler cap rather than the cylinder; or the wheel turns faster as the puffs die away.
- P3 [major · gravity_direction]
  - expect: The steam leaves the cylinder going up and spreads and thins.
  - fail: The steam pours down the engine's base and pools; or sinks below the engine; or hangs as a fixed shape without rising; or pours downward out of the cylinder onto the table.
- P4 [major · trajectory_momentum]
  - expect: The flywheel turns about its own axle in one direction and the piston moves back and forth in line with the cylinder.
  - fail: The wheel reverses direction with nothing changing; or wobbles off its axle; or the piston moves across the cylinder rather than along it; or the wheel turns while the connecting rod stays still.
- P5 [fatal · permanence_count]
  - expect: One engine with one flywheel and one cylinder; the engine stays on the table and its parts stay attached.
  - fail: The flywheel detaches and rolls away; or a second flywheel appears; or the piston passes out through the cylinder's wall; or the engine vanishes.
- P6 [minor · attribute_drift]
  - expect: The engine's paint, the burner and the table stay the same.
  - fail: The engine changes colour; or the burner changes shape; or items on the table rearrange.

## HEAT-0263 · boil_steam · eval

**Caption.** A hot bath is being run, and steam rises from the falling water and fills the bathroom.

**Expectation (hidden).** The steam rises from the tap stream and the bath surface and collects near the ceiling; the mirror may fog.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] Water runs from a tap into a bath.
- S2 [core] Steam rises from the falling water.
- S3 [core] Steam rises from the bath's surface.
- S4 [core] The steam collects near the ceiling.
- S5 [minor] The bath's level rises.
- S6 [minor] The water falls while the steam rises.

**PC**
- P1 [core · gravity_direction]
  - expect: The water falls downward from the tap into the bath while the steam rises from both the stream and the surface and gathers high in the room.
  - fail: The water travels upward from the tap; or the steam sinks to the floor and pools; or the steam pours downward from the tap; or the steam gathers under the bath.
- P2 [core · process_direction]
  - expect: The bath's level only rises while the tap runs and the steam keeps leaving upward.
  - fail: The level drops while the tap still runs; or the steam runs back into the bath; or a puff retreats to the surface; or water climbs back up the stream into the tap.
- P3 [major · missing_consequence]
  - expect: The pour has an effect in the bath: the surface churns where the stream lands and the level rises, and the mirror or tiles may fog.
  - fail: The stream enters and the surface stays glassy with the level unchanged; or the level rises with no stream reaching the bath; or the surface churns in a corner the stream never reaches.
- P4 [major · material_response]
  - expect: The water is a thin liquid that falls as a continuous stream, splashes and finds its level, and the steam is a soft cloud that spreads and fades.
  - fail: The stream falls as a rigid rod; or the water stands in a heap above the bath's rim; or the steam holds a fixed rigid shape; or the stream breaks into solid lumps.
- P5 [fatal · permanence_count]
  - expect: One bath and one tap; the water goes from the tap into the bath and nowhere else.
  - fail: Water appears in the bath with no stream reaching it; or the level jumps; or the water passes through the bath's wall; or a second tap appears.
- P6 [minor · attribute_drift]
  - expect: The bath's enamel, the taps and the bathroom stay the same.
  - fail: The bath changes colour; or the taps change shape; or the tiles change pattern.

## HEAT-0264 · boil_steam · eval

**Caption.** A frying pan straight off a high flame is put under a running tap, and the water hisses into a burst of steam and spits.

**Expectation (hidden).** The steam erupts the instant the water meets the pan and rises, fading as the pan cools and the hissing dies down; the water does not sit quietly in the hot pan.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A frying pan is held under a running tap.
- S2 [core] A burst of steam rises as the water meets the pan.
- S3 [core] The water spits from the pan.
- S4 [core] The steam fades as the pan cools.
- S5 [minor] The pan comes off the flame first and goes under the tap after.
- S6 [minor] The burst is fiercest at first.

**PC**
- P1 [core · missing_consequence]
  - expect: The steam bursts at the instant the water meets the pan and not before.
  - fail: The steam bursts before the water reaches the pan; or the water runs onto the pan and no steam appears at all; or the steam bursts from the pan's handle rather than its face; or the steam appears with the pan held clear of the stream.
- P2 [core · process_direction]
  - expect: The burst is fiercest at first and then eases as the pan cools; it does not build up again with the tap running steadily.
  - fail: The burst grows steadily stronger the longer the tap runs; or the burst stops and then starts again with nothing changed; or the steam runs back into the pan; or the pan's steam thickens after it has been taken out of the stream.
- P3 [major · gravity_direction]
  - expect: The water falls downward from the tap onto the pan while the steam rises and the spat droplets arc down again.
  - fail: The water travels upward from the tap; or the steam sinks into the sink and pools; or the spat droplets rise and hang in the air; or the steam pours downward out of the pan.
- P4 [major · material_response]
  - expect: The water is a thin liquid that bursts into fine droplets on the hot metal and runs off into the sink, and the pan stays a rigid pan.
  - fail: The water beads up and rolls off the pan without wetting it or steaming; or the pan's metal visibly sags as the water hits; or the steam holds a fixed rigid shape; or the water sets solid in the pan.
- P5 [fatal · permanence_count]
  - expect: One pan under one stream; the water goes from the tap onto the pan and into the sink.
  - fail: Water appears in the pan with no stream reaching it; or the pan vanishes; or a second pan appears; or the water passes through the pan's base.
- P6 [minor · attribute_drift]
  - expect: The pan's finish, the sink and the tap stay the same.
  - fail: The pan changes colour; or the sink changes shape; or the tap changes design.

**Note.** The hiss is sound and is not judged. Who holds the pan is not judged.

## HEAT-0265 · boil_steam · eval

**Caption.** The bleed valve on an old radiator is opened, and a hiss of steam escapes until water spurts out and the valve is shut.

**Expectation (hidden).** The steam jet rises from the valve while it is open and stops when the water arrives and the valve is closed.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] A bleed valve on a radiator is opened.
- S2 [core] Steam escapes from the valve.
- S3 [core] Water spurts from the valve.
- S4 [core] The valve is shut and the escape stops.
- S5 [minor] The steam comes from the valve rather than elsewhere.
- S6 [minor] The order is open, steam, water, shut.

**PC**
- P1 [core · missing_consequence]
  - expect: The steam and then the water come out of the valve while it is open and stop when it is shut.
  - fail: Steam escapes from the valve while it is still shut tight; or the valve is opened and nothing comes out at all; or the escape carries on after the valve has been shut; or the water spurts before the valve is opened.
- P2 [core · gravity_direction]
  - expect: The steam rises from the valve and the spurted water arcs out and falls downward.
  - fail: The steam sinks down the radiator and pools on the floor; or the water spurts upward and keeps climbing; or the steam pours downward through the radiator; or the water hangs in the air after leaving the valve.
- P3 [major · process_direction]
  - expect: The escape runs one way: steam first and then water, and it does not go back to steam once water is coming.
  - fail: The water spurts first and steam follows; or the escape turns back from water to steam with the valve held open; or the escape stops and starts again with the valve untouched; or the water is drawn back into the valve.
- P4 [major · material_response]
  - expect: The steam is a soft plume at the valve and the water is a thin liquid that spurts, runs down the radiator and wets what is below.
  - fail: The steam holds a fixed rigid shape; or the water leaves as a solid lump; or the water beads up and rolls off the radiator without wetting it; or the radiator's metal bulges as the valve opens.
- P5 [fatal · permanence_count]
  - expect: One radiator with one valve; the valve stays in the radiator and nothing passes through its body.
  - fail: The valve falls out while the radiator keeps its shape; or a second valve appears; or water passes out through the radiator's panel; or the radiator vanishes.
- P6 [minor · attribute_drift]
  - expect: The radiator's paint, the wall and the floor stay the same.
  - fail: The radiator changes colour; or the wall changes colour; or the floor's covering changes.

**Note.** The hiss is sound and is not judged. Who opens the valve is not judged.

## HEAT-0266 · boil_steam · eval

**Caption.** A saucer that has been covering a steaming mug of tea is lifted off, and a puff of steam escapes while the saucer's underside is beaded with drops.

**Expectation (hidden).** The puff rises the moment the cover lifts and thins; the drops on the underside run to the lowest point and fall or hang there; the saucer's underside is not dry and the steam does not appear before the saucer moves.

**Declared violation types.** missing_consequence, gravity_direction

**SA**
- S1 [core] A saucer covers a mug of tea.
- S2 [core] The saucer is lifted off.
- S3 [core] A puff of steam escapes from the mug.
- S4 [core] The saucer's underside is beaded with drops.
- S5 [minor] The drops run to the saucer's lowest point as it tilts.
- S6 [minor] The lift comes first and the puff follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The puff escapes as the saucer lifts and not before, and the saucer's underside is wet where the steam met it.
  - fail: The puff escapes while the saucer still sits flat on the mug; or the saucer lifts and no steam leaves the mug at all; or the saucer's underside is dry after covering a steaming mug; or the drops lie on the saucer's upper face while its underside is dry.
- P2 [core · gravity_direction]
  - expect: The puff rises from the mug while the drops on the saucer run to its lowest point and hang or fall from there.
  - fail: The puff sinks over the mug's rim and pools on the table; or the drops run up toward the saucer's raised side; or a drop leaves the saucer and rises; or drops stay fixed in place on a steeply tilted saucer.
- P3 [major · process_direction]
  - expect: The steam keeps leaving the mug and the drops on the saucer only gather, run and fall.
  - fail: The puff runs back into the mug; or a puff retreats to the tea; or the saucer's underside beads up again while held clear of the steam; or a fallen drop returns to the saucer.
- P4 [major · material_response]
  - expect: The drops behave as water on china: rounded, merging when they touch and running as streaks, and the saucer stays a rigid disc.
  - fail: Touching drops overlap without merging; or drops jump about on the saucer; or the drops set as frost on the warm china; or the saucer bends as it lifts.
- P5 [fatal · permanence_count]
  - expect: One mug and one saucer; the drops come from the tea's steam and the tea stays in the mug.
  - fail: The tea's level jumps; or a second saucer appears; or the saucer passes through the mug's rim; or tea passes through the mug's wall.
- P6 [minor · attribute_drift]
  - expect: The mug's pattern, the saucer and the table stay the same.
  - fail: The mug's pattern changes; or the saucer changes colour; or items on the table rearrange.

## HEAT-0267 · boil_steam · eval

**Caption.** A pot of jam boils on a stove, and the surface foams up and bubbles thickly.

**Expectation (hidden).** The foam rises while the heat is on and sinks back when the pot is pulled off; the bubbles burst slowly on the thick surface.

**Declared violation types.** process_direction, material_response

**SA**
- S1 [core] A pot of jam boils on a stove.
- S2 [core] The surface foams up.
- S3 [core] Thick bubbles rise and burst slowly.
- S4 [minor] The foam climbs while the heat is on.
- S5 [minor] The foam sinks back when the pot is pulled off the heat.

**PC**
- P1 [core · process_direction]
  - expect: The foam only rises while the pot stays on the heat and sinks back only when it is pulled off.
  - fail: The foam sinks back while the pot sits on the burner with nothing changed; or the foam rises and falls in turn on the heat; or the foam stays up after the pot has been pulled off and left standing; or the foam rises before any bubble appears.
- P2 [core · material_response]
  - expect: The jam is a thick liquid whose bubbles push up slowly, hold their domes for a moment and burst heavily, leaving the surface mounded.
  - fail: The jam bubbles as thin and fast as water; or the surface holds a fixed shape while bubbles burst through it; or the jam sets solid in the pot; or the foam stands as rigid spikes that keep their shape when the pot is moved.
- P3 [major · gravity_direction]
  - expect: The bubbles rise from below to the surface and burst there, and the jam stays in the pot unless it climbs over the rim.
  - fail: Bubbles sink from the surface toward the pot's floor; or hang still in the jam; or the jam climbs the pot's outside and goes in over the rim; or jam lifts off the surface and hangs above it.
- P4 [major · missing_consequence]
  - expect: Foam high in the pot means the jam below has risen: the level and the foam go up together.
  - fail: The foam reaches the rim while the jam below is calm and far from full; or the jam's level drops while the foam climbs; or the foam climbs while the surface below shows no bubbles at all.
- P5 [fatal · permanence_count]
  - expect: One pot of jam; the jam stays in the pot except where it spills over the rim.
  - fail: Jam passes through the pot's wall; or the level jumps up with nothing added; or a second pot appears; or the pot changes shape.
- P6 [minor · attribute_drift]
  - expect: The pot, the hob and the jam's colour stay the same.
  - fail: The pot changes colour; or the jam changes colour; or the hob's knobs move by themselves.

## HEAT-0268 · boil_steam · eval

**Caption.** A pot of potatoes boils with its lid on, and the lid rattles and lifts as steam escapes around its edge.

**Expectation (hidden).** The lid jumps in time with the puffs of steam and steam rises from the gap; the rattling stops when the heat is turned down.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A pot of potatoes boils with its lid on.
- S2 [core] The lid rattles: it lifts and drops on its seat.
- S3 [core] Steam escapes around the lid's edge.
- S4 [minor] The lid's jumps come with the puffs of steam.
- S5 [minor] The rattling stops when the heat is turned down.

**PC**
- P1 [core · causeless_motion]
  - expect: The lid lifts and drops as the puffs of steam push it and settles when the boil eases, and the pot itself stays put.
  - fail: The lid jumps with no steam escaping anywhere; or the lid lifts and stays up; or the pot slides or turns on the burner with nothing touching it; or the lid rattles while the water below is glassy still.
- P2 [core · gravity_direction]
  - expect: The steam escapes at the lid's rim and rises, and the lid falls back onto its seat after each lift.
  - fail: The steam pours down the pot's sides and pools on the hob; or the lid rises and hangs above the pot; or the steam sinks below the pot; or the lid falls upward off the pot.
- P3 [major · missing_consequence]
  - expect: The rattle goes with the boil: the water churns, bubbles break the surface and steam puffs out as the lid lifts.
  - fail: The lid rattles while nothing rises below it; or the water churns hard while the lid sits dead still and no steam escapes; or the steam puffs out while the lid is plainly clamped down tight.
- P4 [major · material_response]
  - expect: The lid stays a rigid disc that knocks on the rim and the potatoes stay firm lumps that jostle in the water.
  - fail: The lid bends or ripples as it lifts; or a potato dissolves into the water; or the lid sticks to the pot and the pot lifts with it; or the potatoes merge into one lump.
- P5 [fatal · permanence_count]
  - expect: One pot with one lid; the potatoes keep their number and stay in the pot.
  - fail: A potato vanishes; or a new potato appears; or the lid passes through the pot's rim; or a second lid appears.
- P6 [minor · attribute_drift]
  - expect: The pot, the lid's handle and the hob stay the same.
  - fail: The pot changes colour; or the lid's handle changes shape; or the hob's knobs move by themselves.

**Note.** The rattle is sound and is not judged; it is read from the lid's visible lifting and dropping.

## HEAT-0269 · boil_steam · eval

**Caption.** A moka pot on a stove starts to gurgle, and coffee sputters up into the top chamber with puffs of steam.

**Expectation (hidden).** The coffee appears in the upper chamber only after the gurgling starts and rises in spurts, steam puffing from the spout; the flow does not run back down or begin before the pot is hot.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A moka pot stands on a stove.
- S2 [core] Coffee appears in the top chamber.
- S3 [core] The coffee rises in spurts.
- S4 [core] Puffs of steam come from the spout.
- S5 [minor] The top chamber is empty at the start.
- S6 [minor] The gurgling comes first and the coffee follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The coffee rises only after the pot has been on the heat and the gurgling has begun, in spurts that come and go with it.
  - fail: Coffee appears in the top chamber before the pot has been on the heat; or the coffee rises in a smooth stream with no spurts while the pot gurgles; or the coffee keeps rising after the pot has been taken off and set aside; or the coffee rises with the pot cold and dry.
- P2 [core · gravity_direction]
  - expect: The coffee comes up the central spout into the top chamber and gathers in its base, and the steam rises from the spout.
  - fail: The coffee runs back down into the lower chamber and stays; or the coffee gathers at the top chamber's lid and stays; or the steam pours downward into the pot; or the coffee climbs the outside of the pot.
- P3 [major · process_direction]
  - expect: The level in the top chamber only rises while the pot works and does not fall back.
  - fail: The top chamber's level drops with the pot still on the heat; or the coffee rises and falls in turn; or the coffee in the top chamber clears back to nothing; or the lower chamber fills as the top empties.
- P4 [major · material_response]
  - expect: The coffee is a thin dark liquid that sputters and streams, and the pot stays a rigid metal body.
  - fail: The coffee leaves as solid lumps; or the pot's metal bulges as the coffee rises; or the coffee stands as a rigid column in the chamber; or the coffee sets solid in the pot.
- P5 [fatal · permanence_count]
  - expect: One pot in two chambers; the coffee that appears above came up from below and the pot stays whole.
  - fail: Coffee appears in the top chamber with the lower chamber still full and the spout dry; or the pot's lid vanishes; or a second pot appears; or coffee passes through the pot's wall.
- P6 [minor · attribute_drift]
  - expect: The pot's finish, the hob and the surroundings stay the same.
  - fail: The pot changes colour; or its handle changes shape; or items around the hob rearrange.

**Note.** The gurgle is sound and is not judged; it is read from the coffee's spurting.

## HEAT-0270 · boil_steam · eval

**Caption.** A hot towel is unrolled on a counter, and steam rises from the cloth as it opens.

**Expectation (hidden).** Steam rises from the whole unfolded towel, thickest as it is first opened, and fades as the towel cools.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] A rolled hot towel lies on a counter.
- S2 [core] The towel is unrolled.
- S3 [core] Steam rises from the cloth.
- S4 [core] The steam is thickest as the towel first opens.
- S5 [minor] The steam fades as the towel cools.
- S6 [minor] The unrolling comes first and the steam follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The steam leaves the towel going up, spreading and thinning as it rises.
  - fail: The steam sinks over the counter's edge and pools on the floor; or pours downward through the towel; or hangs as a fixed shape without rising; or flows sideways with nothing blowing it.
- P2 [core · process_direction]
  - expect: The steam is thickest as the towel opens and then only eases; it does not build up again with nothing added.
  - fail: The steam thickens steadily the longer the towel lies open; or the steam stops and then starts again with nothing touching the towel; or the plume runs back into the cloth; or a puff retreats to the towel.
- P3 [major · missing_consequence]
  - expect: The steam comes off the towel's own damp cloth and is thickest over the newly opened folds.
  - fail: The steam rises from the counter beside the towel while the cloth is clear; or the steam is thickest over a part of the towel still rolled tight; or the towel lies open and steaming wet with no steam leaving it at all.
- P4 [major · material_response]
  - expect: The towel is limp damp cloth that unrolls, drapes and settles, and the steam is a soft cloud that spreads.
  - fail: The towel stays a rigid roll as it opens; or stands stiff like a board once open; or the steam holds a fixed rigid shape; or the towel sets hard as it cools.
- P5 [fatal · permanence_count]
  - expect: One towel on one counter; the towel stays one piece and nothing passes through the counter.
  - fail: The towel splits into two towels; or a second towel appears; or the towel vanishes; or the towel passes through the counter.
- P6 [minor · attribute_drift]
  - expect: The towel's colour, the counter and the surroundings stay the same.
  - fail: The towel changes colour; or the counter changes pattern; or items around the towel rearrange.

**Note.** Who unrolls the towel is not judged.

## HEAT-0271 · condensation · eval

**Caption.** A bottle from the fridge and an identical bottle from a cupboard stand side by side on a warm counter, and only the cold one beads with water.

**Expectation (hidden).** Mist and then drops form on the cold bottle and run down, wetting the counter beneath it; the room-temperature bottle stays dry throughout; the cold one does not dry off while it is still cold.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] Two identical bottles stand side by side on a counter.
- S2 [core] One bottle has come from a fridge and reads as cold.
- S3 [core] Mist and then drops form on the cold bottle.
- S4 [core] The room-temperature bottle stays dry.
- S5 [minor] Drops run down the cold bottle.
- S6 [minor] The counter wets beneath the cold bottle.

**PC**
- P1 [core · missing_consequence]
  - expect: The beading appears only on the cold bottle and the other stays dry throughout.
  - fail: The room-temperature bottle beads while the cold one stays dry; or both bottles bead equally; or neither bottle beads at all while one is plainly frosted from the fridge; or the dry bottle's label wets while its glass stays dry.
- P2 [core · process_direction]
  - expect: The beading on the cold bottle only builds while it stays cold: drops grow, join and run.
  - fail: The drops shrink or go while the bottle stays cold and frosted; or the cold bottle beads and dries in turn; or the beading eases while the frost is still on it; or the drops turn back into dry white frost on the warm counter.
- P3 [major · gravity_direction]
  - expect: Drops that grow large enough run downward on the cold bottle and wet the counter beneath it.
  - fail: A drop runs up the bottle; or water gathers on the cap's top and stays; or a drop leaves the bottle and rises; or a run travels sideways round the bottle and stays level.
- P4 [major · material_response]
  - expect: The beads behave as water on glass: rounded, merging when they touch and running as streaks, and the counter darkens where it wets.
  - fail: Touching drops overlap without merging; or drops jump about on the glass; or the counter stays dry-looking under a spreading pool; or the beads stand as tall columns on the glass.
- P5 [fatal · permanence_count]
  - expect: Two bottles on one counter; the water on the cold bottle comes out of the air and its contents stay inside.
  - fail: The cold bottle's level drops as the pool grows; or beads form on the inside of a bottle; or a third bottle appears; or a bottle passes through the counter.
- P6 [minor · attribute_drift]
  - expect: The bottles' labels, their caps and the counter stay the same.
  - fail: A label changes; or a cap changes colour; or items on the counter rearrange.

## HEAT-0272 · condensation · eval

**Caption.** A snorkelling mask worn in warm water fogs on the inside with each breath.

**Expectation (hidden).** The fog forms on the inner surface and thickens with each exhale; the outside of the glass stays clear.

**Declared violation types.** process_direction, attribute_drift

**SA**
- S1 [core] A snorkelling mask is worn.
- S2 [core] The inside of the mask's glass fogs.
- S3 [core] The fog thickens with each breath.
- S4 [minor] The outside of the glass stays clear.
- S5 [minor] The mask is clear at the start.
- S6 [minor] The breathing comes first and the fogging follows.

**PC**
- P1 [core · process_direction]
  - expect: The fog only thickens with each breath while the mask stays on; it does not clear on its own.
  - fail: The fog clears while the mask stays on and breathing goes on; or the fog thins and thickens with no breath; or the mask is fogged before any breath; or the fog retreats to the glass's edges while breathing continues.
- P2 [core · attribute_drift]
  - expect: The haze lies on the inner face of the glass and the outer face stays clear.
  - fail: The fog forms on the outside of the glass; or both faces fog equally; or the mask's skirt changes colour rather than the glass; or the water outside the mask clouds rather than the glass.
- P3 [major · gravity_direction]
  - expect: Drops that gather in the fog run downward on the inner face and pool at the mask's lower rim.
  - fail: A drop runs up the glass; or a drop leaves the glass and rises; or water gathers along the glass's top edge and stays; or the drops inside the mask float free of the glass.
- P4 [major · material_response]
  - expect: The fog is a fine haze that beads and streaks, and the glass stays rigid and clear.
  - fail: The fog stands off the glass as a thick crust; or peels away as a film; or the glass flexes or ripples; or the haze turns opaque white like paint.
- P5 [fatal · shape_identity]
  - expect: One mask with one lens; the mask keeps its shape on the face and nothing passes through the glass.
  - fail: The lens vanishes; or a second lens appears; or a hand passes through the lens; or the mask changes shape.
- P6 [minor · attribute_drift]
  - expect: The mask's skirt and strap and the water around stay the same.
  - fail: The skirt changes colour; or the strap changes shape; or the water's colour changes between frames.

**Note.** The diver is kept because the breath is the moisture's source; the person is otherwise not judged.

## HEAT-0273 · condensation · eval

**Caption.** The inside of a tent wall is covered in dew at dawn; the wall is tapped and drops rain down inside the tent.

**Expectation (hidden).** Before the tap the drops cling in place; at the tap they run together and fall straight down onto the groundsheet; the wall is drier where they fell from and the drops do not return.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] The inside of a tent wall is covered in dew.
- S2 [core] The wall is tapped.
- S3 [core] Drops rain down inside the tent.
- S4 [core] The drops land on the groundsheet.
- S5 [minor] The drops cling in place before the tap.
- S6 [minor] The wall is drier where the drops fell from.

**PC**
- P1 [core · gravity_direction]
  - expect: The drops hang on the wall until the tap, then run together and fall straight down onto the groundsheet.
  - fail: The drops fall upward off the wall; or the drops run up the wall as it is tapped; or the drops fly out sideways and stay in the air; or the drops fall and then rise back to the wall.
- P2 [core · missing_consequence]
  - expect: The drops fall where the wall was tapped and the wall there is left drier, while drops on untapped parts stay.
  - fail: The drops fall from a part of the wall the tap never reached; or the wall is tapped and no drop moves at all; or the whole wall sheds its dew at one tap on one spot; or the wall is just as wet after the drops have fallen from it.
- P3 [major · process_direction]
  - expect: The drops only gather and fall; the wall does not bead up again where they left with nothing wetting it.
  - fail: The wall beads up again where the drops fell with nothing wetting it; or drops that have fallen come back onto the wall; or the drops grow and shrink in turn; or the dew spreads over the dry patch as a front.
- P4 [major · material_response]
  - expect: The drops behave as water on fabric: rounded, merging when they touch and soaking the groundsheet where they land, and the wall is limp cloth that gives under the tap.
  - fail: Touching drops overlap without merging; or drops bounce off the groundsheet like beads and stay round; or the tent wall stays rigid like a board under the tap; or the drops set as frost on the fabric.
- P5 [fatal · permanence_count]
  - expect: One tent; the drops come off its wall and land inside, and nothing passes through the fabric.
  - fail: Drops pass through the tent wall from outside; or a drop vanishes in mid-air; or the groundsheet stays bone dry where drops landed; or the tent changes shape.
- P6 [minor · attribute_drift]
  - expect: The tent's fabric colour, the groundsheet and the gear inside stay the same.
  - fail: The fabric changes colour; or the groundsheet changes pattern; or the gear inside rearranges.

**Note.** Who taps the wall is not judged.

## HEAT-0274 · condensation · eval

**Caption.** A chilled cocktail glass is set on a bar in a warm room, and a film of mist forms on it and turns into running drops.

**Expectation (hidden).** The mist appears evenly on the cold glass and beads run down to wet the bar mat; the glass does not dry while cold.

**Declared violation types.** process_direction, gravity_direction

**SA**
- S1 [core] A chilled cocktail glass is set on a bar.
- S2 [core] A film of mist forms on the glass.
- S3 [core] The mist turns into drops.
- S4 [core] The drops run down.
- S5 [minor] The bar mat wets beneath the glass.
- S6 [minor] The setting down comes first and the misting follows.

**PC**
- P1 [core · process_direction]
  - expect: The misting and beading only build while the glass stays cold: the drops grow, join and run.
  - fail: The glass dries while it is still cold and frosted; or the glass mists and dries in turn; or the glass is misted before it is taken out of the chiller; or the beads shrink while the glass is still cold.
- P2 [core · gravity_direction]
  - expect: The drops run downward over the glass to its stem and foot and wet the bar mat.
  - fail: A drop runs up the glass; or water gathers on the rim and stays as a dome; or a drop leaves the glass and rises; or a run travels sideways round the bowl and stays level.
- P3 [major · missing_consequence]
  - expect: The mist lies on the outside of the cold glass and the mat wets where runs reach it.
  - fail: The mist forms on the inside of the glass; or the bar mat stays dry under a glass streaming with runs; or the mist forms on the bar beside the glass while the glass stays clear; or the glass mists before it is chilled.
- P4 [major · material_response]
  - expect: The mist is a fine even film that beads into rounded drops which merge and streak, and the glass stays rigid.
  - fail: Touching drops overlap without merging; or drops jump about on the glass; or the film peels away as a sheet; or the beads turn to hard frost while the glass runs with water.
- P5 [fatal · shape_identity]
  - expect: One glass on one bar; the glass keeps its bowl and stem and nothing passes through it.
  - fail: The glass changes shape; or a second glass appears; or the stem detaches; or the drink passes through the glass's wall.
- P6 [minor · attribute_drift]
  - expect: The glass's shape, the drink's colour and the bar stay the same.
  - fail: The glass changes pattern; or the drink changes colour; or items on the bar rearrange.

## HEAT-0275 · condensation · eval

**Caption.** A metal water bottle packed with ice sits on a gym bench, and a wet patch spreads on the bench beneath it.

**Expectation (hidden).** Droplets form on the cold metal and run down to the base, and the patch grows while the bottle stays cold.

**Declared violation types.** process_direction, gravity_direction

**SA**
- S1 [core] A metal water bottle stands on a gym bench.
- S2 [core] Droplets form on the bottle.
- S3 [core] The droplets run down to its base.
- S4 [core] A wet patch spreads on the bench beneath it.
- S5 [minor] The bottle reads as packed with ice: frost or chill on its surface.
- S6 [minor] The beading comes first and the patch follows.

**PC**
- P1 [core · process_direction]
  - expect: The beading and the patch only grow while the bottle stays cold.
  - fail: The droplets shrink or go while the bottle stays cold and frosted; or the wet patch shrinks; or the bottle beads and dries in turn; or the droplets turn back into dry frost in the warm room.
- P2 [core · gravity_direction]
  - expect: The droplets run downward on the bottle to its base and the patch grows out from under it.
  - fail: A droplet runs up the bottle; or water gathers on the cap and stays as a dome; or a drop leaves the bottle and rises; or the patch grows away from the bottle with no water running to it.
- P3 [major · missing_consequence]
  - expect: The water forms on the outside of the cold metal and the patch lies under the bottle where the runs reach the bench.
  - fail: The water appears on the bench away from the bottle with none running there; or the bottle's own level drops as the patch grows; or beads form inside the bottle's mouth while its outside stays dry; or the bench stays dry under a bottle streaming with runs.
- P4 [major · material_response]
  - expect: The beads behave as water on metal: rounded, merging when they touch and running as streaks, and the bench darkens where it wets.
  - fail: Touching drops overlap without merging; or drops jump about on the metal; or the bench stays dry-looking under a spreading patch; or the beads stand as tall columns on the metal.
- P5 [fatal · shape_identity]
  - expect: One bottle on one bench; the bottle keeps its shape and nothing passes through it.
  - fail: The bottle changes shape; or a second bottle appears; or the cap passes into the bottle; or water passes out through the metal wall.
- P6 [minor · attribute_drift]
  - expect: The bottle's finish, the bench and the gym behind stay the same.
  - fail: The bottle changes colour; or the bench changes pattern; or the gym's equipment rearranges.

## HEAT-0276 · condensation · eval

**Caption.** Rain begins on a warm, humid day while a car sits with its windows shut, and the inside of the windshield fogs over while the wipers sweep the outside without clearing it.

**Expectation (hidden).** The fog forms on the inner face and thickens; each wiper pass clears rain from the outside but leaves the haze unchanged; the fog does not vanish with the wipers.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A car sits with its windows shut in the rain.
- S2 [core] The inside of the windshield fogs.
- S3 [core] The wipers sweep the outside.
- S4 [core] Each wiper pass leaves the haze unchanged.
- S5 [minor] The wipers clear rain from the outside.
- S6 [minor] The fog thickens as the rain goes on.

**PC**
- P1 [core · missing_consequence]
  - expect: Each wiper pass clears the rain from the outer face and leaves the inner haze as it was.
  - fail: A wiper pass clears the fog from the inside of the glass; or the haze thins in a band following the wiper; or the wipers sweep and the outside stays as streaked with rain as before; or the fog clears where the wiper has passed and returns between passes.
- P2 [core · process_direction]
  - expect: The fog on the inside only thickens while the car stays shut and the rain goes on.
  - fail: The fog clears while the car stays shut; or the fog thins and thickens with the wipers' rhythm; or the windshield is fogged before the rain begins; or the fog retreats to the glass's edges while the rain goes on.
- P3 [major · gravity_direction]
  - expect: Rain runs downward on the outer face and drops in the inner fog run downward too.
  - fail: Rain runs up the windshield; or a drop on the inner face runs upward; or water gathers along the glass's top edge and stays; or a drop leaves the glass and rises.
- P4 [major · trajectory_momentum]
  - expect: Each wiper sweeps across the glass in an arc about its pivot and returns, and the blade stays on the glass.
  - fail: A wiper lifts off the glass and sweeps through the air; or a wiper moves in a straight line across the glass; or a wiper sweeps about a pivot that moves along the glass; or a blade passes through the glass.
- P5 [fatal · permanence_count]
  - expect: One windshield with its wipers; the wipers stay attached and the glass stays whole.
  - fail: A wiper vanishes; or a third wiper appears; or a wiper passes through the glass; or the windshield changes shape.
- P6 [minor · attribute_drift]
  - expect: The dashboard, the wipers' arms and the view outside stay the same.
  - fail: The dashboard changes colour; or a wiper arm changes shape; or the scene outside jumps to a different place.

## HEAT-0277 · condensation · eval

**Caption.** A fridge door is opened in a steamy kitchen, and the cold glass shelves inside fog over.

**Expectation (hidden).** The haze appears on the cold shelves and inner walls within moments of the door opening and thickens while it stays open; it does not appear on the warm outside of the door and does not form before the door opens.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A fridge door is opened in a steamy kitchen.
- S2 [core] The glass shelves inside fog over.
- S3 [core] The fog thickens while the door stays open.
- S4 [minor] The fog is on the cold surfaces inside.
- S5 [minor] The outside of the door stays clear.
- S6 [minor] The opening comes first and the fogging follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The fog appears on the cold shelves and inner walls once the door is open and not before.
  - fail: The shelves are fogged before the door opens; or the door opens and the cold shelves stay clear and bright to the end of the clip; or the fog appears on the warm outside of the door while the shelves stay clear; or the fog appears on the kitchen's walls rather than inside the fridge.
- P2 [core · process_direction]
  - expect: The fog only thickens while the door stays open and the warm air keeps reaching the shelves.
  - fail: The fog clears while the door stays open in the steamy kitchen; or the fog thins and thickens in turn; or the fog thickens after the door has been shut and the cold has returned; or the fog retreats to the shelves' edges while the door stays open.
- P3 [major · gravity_direction]
  - expect: Drops that gather on the shelves run downward and drip to the shelf below.
  - fail: A drop runs up a shelf's face; or a drop leaves a shelf and rises; or water gathers along a shelf's top edge and stays; or drops hang in the air between shelves.
- P4 [major · material_response]
  - expect: The fog is a fine haze that beads on the glass, and the shelves stay rigid clear plates.
  - fail: The fog stands off the glass as a thick crust; or peels away as a film; or a shelf flexes as it fogs; or the haze turns opaque white like paint.
- P5 [fatal · permanence_count]
  - expect: One fridge with its shelves and contents; the contents keep their number while the door is open.
  - fail: An item on a shelf vanishes; or new items appear; or a shelf vanishes; or the door passes through the cabinet's frame.
- P6 [minor · attribute_drift]
  - expect: The fridge's interior, its door seal and the kitchen stay the same.
  - fail: The interior changes colour; or the seal changes shape; or items in the kitchen rearrange.

## HEAT-0278 · condensation · eval

**Caption.** A warm loaf fresh from the oven is slid into a clear plastic bag, and the inside of the bag fogs over.

**Expectation (hidden).** The fog forms on the inner face of the bag within moments, thickest above the loaf, and gathers into drops; the outside of the bag stays dry and the fog does not appear before the loaf is inside.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A warm loaf is slid into a clear plastic bag.
- S2 [core] The inside of the bag fogs over.
- S3 [core] The fog is thickest above the loaf.
- S4 [core] The fog gathers into drops.
- S5 [minor] The outside of the bag stays dry.
- S6 [minor] The loaf goes in first and the fogging follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The fog appears on the bag's inner face once the warm loaf is inside and is thickest above it.
  - fail: The bag is fogged before the loaf is in it; or the loaf sits in the bag and the plastic stays clear and dry to the end of the clip; or the fog appears on the outside of the bag; or the fog is thickest at a corner far from the loaf.
- P2 [core · process_direction]
  - expect: The fog only thickens while the warm loaf stays in the bag and gathers into drops; it does not clear on its own.
  - fail: The fog clears while the warm loaf stays in the closed bag; or the fog thins and thickens in turn; or the drops draw back into a clear film and the bag dries; or the fog moves to the outer face as it thickens.
- P3 [major · gravity_direction]
  - expect: Drops on the bag's inner face run downward and pool at its bottom, and drops on the upper face hang and fall.
  - fail: A drop runs up the bag's inner face; or drops fall upward off the upper face; or water gathers along the bag's top and stays as a dome; or drops hang in the air inside the bag away from the plastic.
- P4 [major · material_response]
  - expect: The bag is a limp clear film that creases and clings and the fog beads on it, and the loaf stays a soft solid.
  - fail: The bag stays a rigid box as the loaf goes in; or the bag's film sets hard as it fogs; or the loaf flows as a liquid in the bag; or the fog stands off the film as a thick crust.
- P5 [fatal · permanence_count]
  - expect: One loaf in one bag; the loaf stays whole inside and nothing passes through the plastic.
  - fail: The loaf passes out through the bag's wall; or a second loaf appears; or the loaf vanishes; or the bag splits into two bags.
- P6 [minor · attribute_drift]
  - expect: The bag's printing, the loaf's crust and the counter stay the same.
  - fail: The bag's printing changes; or the crust changes pattern; or items on the counter rearrange.

**Note.** Who bags the loaf is not judged.

## HEAT-0279 · condensation · eval

**Caption.** A cup of hot coffee stands on the dashboard of a cold car, and a patch of fog spreads on the windshield above it.

**Expectation (hidden).** The patch appears directly above the cup and grows outward while the coffee steams; the rest of the glass stays clear; the patch does not form below the cup or on the outside of the glass.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A cup of hot coffee stands on a car's dashboard.
- S2 [core] Steam rises from the cup.
- S3 [core] A patch of fog forms on the windshield above the cup.
- S4 [core] The patch grows outward.
- S5 [minor] The rest of the glass stays clear.
- S6 [minor] The steaming comes first and the patch follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The patch forms on the glass directly above the cup, where the steam reaches it, and the glass away from it stays clear.
  - fail: The patch forms below the cup on the glass; or the patch forms on a part of the windshield the steam never reaches; or the whole windshield fogs evenly while the steam rises from one cup; or the patch forms on the outside of the glass.
- P2 [core · process_direction]
  - expect: The patch only grows while the coffee steams and does not clear on its own.
  - fail: The patch clears while the coffee still steams; or the patch grows and shrinks in turn; or the glass is fogged before the cup is on the dashboard; or the patch jumps to a new place on the glass.
- P3 [major · gravity_direction]
  - expect: The steam rises from the cup to the glass and drops in the patch run downward on the inner face.
  - fail: The steam sinks onto the dashboard and pools; or a drop in the patch runs up the glass; or the steam pours downward from the cup; or drops gather along the patch's top edge and stay.
- P4 [major · material_response]
  - expect: The fog is a fine haze that beads and streaks, and the glass stays rigid and clear.
  - fail: The fog stands off the glass as a thick crust; or peels away as a film; or the glass flexes where the patch lies; or the haze turns opaque white like paint.
- P5 [fatal · permanence_count]
  - expect: One cup on one dashboard; the cup stays upright and nothing passes through the glass.
  - fail: The cup vanishes; or a second cup appears; or the cup passes into the dashboard; or the coffee passes through the windshield.
- P6 [minor · attribute_drift]
  - expect: The dashboard, the cup's markings and the view outside stay the same.
  - fail: The dashboard changes colour; or the cup's markings change; or the scene outside jumps to a different place.

## HEAT-0280 · condensation · eval

**Caption.** A horse snorts in a cold stable, and clouds of breath puff from its nostrils and fade.

**Expectation (hidden).** A cloud appears at each snort just in front of the nostrils, spreads and vanishes within a second or two; nothing is visible between breaths; the clouds do not sink to the floor.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A horse stands in a stable.
- S2 [core] A cloud of breath appears at its nostrils.
- S3 [core] The cloud spreads and fades.
- S4 [core] A cloud appears at each snort.
- S5 [minor] Nothing is visible between breaths.
- S6 [minor] The setting reads as cold.

**PC**
- P1 [core · causeless_motion]
  - expect: Each cloud appears at the nostrils as the horse breathes out and moves away from them; nothing appears between breaths.
  - fail: A cloud appears in the air away from the horse's head with nothing leaving its nostrils; or a cloud appears while the horse is drawing breath in; or a cloud hangs unchanged for the rest of the clip; or the cloud moves toward the nostrils and is drawn in.
- P2 [core · process_direction]
  - expect: Each cloud only spreads and fades and does not come back once gone.
  - fail: A faded cloud thickens again with no new breath; or the clouds appear and disappear in a rhythm unrelated to the horse's breathing; or a cloud runs back into the nostrils; or the cloud thickens the further it gets from the head.
- P3 [major · gravity_direction]
  - expect: The clouds drift and spread as they thin and do not sink to the floor as a liquid.
  - fail: The clouds sink to the stable floor and pool; or a cloud falls in a stream from the nostrils; or a cloud hangs as a fixed shape without drifting; or the clouds pour downward over the horse's chest.
- P4 [major · material_response]
  - expect: Each cloud is a soft haze that spreads, waves and fades and holds no edges.
  - fail: A cloud holds a fixed rigid shape; or turns into solid lumps; or pours like a liquid; or keeps a sharp outline as it drifts.
- P5 [fatal · shape_identity]
  - expect: One horse with the same head, body and legs; the clouds stay outside its body.
  - fail: The horse gains or loses a limb; or a second horse appears; or a cloud passes into the horse's chest and out the back; or the horse's head changes shape.
- P6 [minor · attribute_drift]
  - expect: The horse's coat, the stable's walls and the straw stay the same.
  - fail: The coat changes colour or pattern; or the stable's walls change; or the straw rearranges.

**Note.** The horse is an animal and its movements are not judged; it is kept because its breath is the caption's subject.

## HEAT-0281 · burn_smoke · eval

**Caption.** The door of a wood stove is opened, and the flames inside lean out toward the opening and flare up.

**Expectation (hidden).** The flames grow and lean as the door opens and settle back when it shuts; they always point upward from the logs.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A wood stove with flames inside.
- S2 [core] The stove's door is opened.
- S3 [core] The flames lean out toward the opening.
- S4 [core] The flames flare up.
- S5 [minor] The flames settle back when the door is shut.
- S6 [minor] The opening comes first and the leaning follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The flames lean toward the opening as the door swings wide and settle back when it closes.
  - fail: The flames lean away from the opening deeper into the stove as the door opens; or the flames lean out while the door is still shut; or the flames stay leaning out after the door has been shut; or the flames lean out before the door has moved.
- P2 [core · gravity_direction]
  - expect: The flames point upward from the logs, leaning only toward the draught, and the smoke rises to the flue.
  - fail: The flames point downward into the ash; or the flames lie flat along the stove's floor with the door shut and no draught; or the smoke sinks out of the open door and pools on the hearth; or the flames hang below the logs.
- P3 [major · process_direction]
  - expect: The flare follows the door's opening and eases as the air settles, and the logs only char.
  - fail: The flare comes before the door moves; or the flare keeps growing after the door has been shut; or a charred log turns back to pale wood; or the flames go out and relight by themselves as the door opens.
- P4 [major · material_response]
  - expect: The flames are soft tongues that stretch toward the opening and the logs stay solid charring wood, while the door is a rigid panel on its hinge.
  - fail: The flames hold fixed rigid shapes as they lean; or a log melts or flows; or the door bends as it opens; or the flames leave solid pieces behind.
- P5 [fatal · permanence_count]
  - expect: One stove with one door; the logs keep their number and stay inside the firebox.
  - fail: A log vanishes; or a new log appears; or a log passes through the stove's wall; or the door passes through its frame.
- P6 [minor · attribute_drift]
  - expect: The stove's body, its glass and the hearth stay the same.
  - fail: The stove changes colour; or the door's glass changes shape; or items on the hearth rearrange.

**Note.** Who opens the door is not judged.

## HEAT-0282 · burn_smoke · eval

**Caption.** A birthday cake with lit candles is carried across a room, and the flames lean backward as it moves and stand up when it is set down.

**Expectation (hidden).** The flames trail opposite to the direction of motion, flicker, and return to pointing upward when the cake stops; none goes out unless blown.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A cake with lit candles is carried across a room.
- S2 [core] The flames lean backward as the cake moves.
- S3 [core] The cake is set down.
- S4 [core] The flames stand up again.
- S5 [minor] All the flames lean the same way.
- S6 [minor] The flames flicker as the cake moves.

**PC**
- P1 [core · causeless_motion]
  - expect: The flames trail opposite to the cake's direction of travel while it moves and return to upright once it stops.
  - fail: The flames lean forward in the direction the cake is travelling; or the flames stay leaning after the cake is set down; or the flames lean while the cake stands still; or each flame leans a different way at the same moment.
- P2 [core · gravity_direction]
  - expect: With the cake still the flames point upward from their wicks and the wax pools at each candle's top.
  - fail: A flame points downward with the cake still; or a flame hangs below its wick; or melted wax climbs a candle's side; or the flames lie flat while the cake stands still and nothing moves.
- P3 [major · process_direction]
  - expect: The flames stay alight through the carrying unless blown out, and once out a candle stays out.
  - fail: A candle goes out and relights by itself; or a flame shrinks to nothing and returns with each step; or every flame goes out as the cake is set down gently; or a wick's glow brightens into a flame with nothing touching it.
- P4 [major · material_response]
  - expect: The flames are soft tongues that stretch and waver and the candles stay upright in the cake's icing.
  - fail: A flame holds a fixed rigid shape as it leans; or a candle bends with the movement; or a candle sinks into the icing and stays sunk; or a flame breaks into solid pieces.
- P5 [fatal · permanence_count]
  - expect: The candles keep their number and places in the cake and each keeps one wick and one flame.
  - fail: A flame separates from its wick and floats; or a second flame appears on one wick; or a candle vanishes; or a new candle appears in the cake.
- P6 [minor · attribute_drift]
  - expect: The cake's icing, the candles' colours and the room stay the same.
  - fail: The icing changes colour or pattern; or a candle changes colour; or items in the room rearrange.

**Note.** Whoever carries the cake is not judged.

## HEAT-0283 · burn_smoke · eval

**Caption.** A line of flame advances across a stubble field with the wind, smoke drifting ahead of it.

**Expectation (hidden).** The fire line moves downwind, blackened ground is left behind it, and the smoke leans the same way as the flames.

**Declared violation types.** process_direction, causeless_motion

**SA**
- S1 [core] A line of flame crosses a stubble field.
- S2 [core] The line advances across the field.
- S3 [core] Blackened ground is left behind the line.
- S4 [core] Smoke drifts ahead of the flames.
- S5 [minor] The smoke leans the same way as the flames.
- S6 [minor] The line moves downwind.

**PC**
- P1 [core · process_direction]
  - expect: The line only advances into unburnt stubble and the blackened ground behind it stays black.
  - fail: The fire line retreats back over ground it has burnt; or blackened ground turns back to pale stubble; or the fire starts ahead of the line in stubble no flame has reached; or the burnt strip narrows behind the line.
- P2 [core · causeless_motion]
  - expect: The line advances the same way the smoke drifts and the stubble leans, and keeps that direction while they hold theirs.
  - fail: The line advances against the way the smoke drifts; or the smoke drifts one way while the flames lean the other; or the line's direction swings about while the smoke holds steady; or the line advances while the smoke stands straight up and the stubble is dead still.
- P3 [major · gravity_direction]
  - expect: The flames point upward from the stubble, leaning with the wind, and the smoke rises as it drifts.
  - fail: The flames point downward into the soil; or the smoke sinks and lies on the field ahead of the line; or the flames hang above the stubble with a gap below them; or the smoke pours downward into the burnt ground.
- P4 [major · missing_consequence]
  - expect: The stubble ahead of the line catches as the flames reach it and burns down to black ground behind.
  - fail: The stubble ahead catches before any flame reaches it; or the flames pass over stubble and leave it standing pale and unburnt; or the ground behind the line stays pale with the stubble gone; or the smoke rises from ground the line has not reached.
- P5 [fatal · shape_identity]
  - expect: The field stays a field of stubble that burns to black ground; nothing turns into anything else.
  - fail: The stubble turns into another material as it burns; or the ground opens up behind the line; or a second fire line appears from bare burnt ground; or the flames pass through a hedge and leave it whole.
- P6 [minor · attribute_drift]
  - expect: The field's edges, the trees around and the sky stay the same.
  - fail: The hedges change shape; or the trees change into different trees; or the sky changes colour permanently.

## HEAT-0284 · burn_smoke · eval

**Caption.** A small blowtorch is played over charcoal in a barbecue, and the coals begin to glow where the flame touches them.

**Expectation (hidden).** The glow appears only where the torch is aimed and spreads slowly to neighbouring coals; the flame points where the torch points.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] A blowtorch is played over charcoal in a barbecue.
- S2 [core] The coals begin to glow where the flame touches them.
- S3 [core] The glow spreads to neighbouring coals.
- S4 [minor] The flame points where the torch points.
- S5 [minor] The coals are black before the torch reaches them.
- S6 [minor] The torch comes first and the glow follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The glow appears only where the torch is aimed and spreads from there to the coals beside it.
  - fail: The coals glow before the torch reaches them; or the torch plays on a coal and it stays black to the end of the clip; or the glow appears on the far side of the bed from the torch; or the whole bed glows at once while the torch plays on one spot.
- P2 [core · process_direction]
  - expect: The glow only spreads and brightens and does not go out where it has caught.
  - fail: A glowing coal goes black again while the torch plays nearby; or the glow spreads and then retreats; or the glow brightens and dims in turn; or the ash gathers back into black charcoal.
- P3 [major · gravity_direction]
  - expect: The torch's flame points where it is aimed and any smoke or sparks from the coals rise.
  - fail: The flame droops downward as the torch is tilted up; or the smoke sinks into the barbecue and pools; or sparks fall through the grate and lie glowing below; or the flame hangs below the nozzle.
- P4 [major · material_response]
  - expect: The coals stay hard lumps that glow and crust with ash, and the torch stays a rigid tool.
  - fail: A coal melts or flows under the flame; or the coals swell as they glow; or the torch's nozzle melts; or the ash holds a rigid shape when the coals shift.
- P5 [fatal · permanence_count]
  - expect: One torch and one bed of coals; the coals keep their number and stay in the barbecue.
  - fail: A coal vanishes leaving no ash; or new coals appear with none added; or a coal passes through the grate and out below; or a second torch appears.
- P6 [minor · attribute_drift]
  - expect: The barbecue's body, the grate and the surroundings stay the same.
  - fail: The barbecue changes colour; or the grate changes spacing; or items around the barbecue rearrange.

## HEAT-0285 · burn_smoke · eval

**Caption.** A dry pine cone is tossed into a fireplace, and it catches, glows, and crumbles into embers.

**Expectation (hidden).** The cone lights where it touches the flames, burns from that side, and shrinks into glowing pieces that fade; it does not return whole.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A pine cone is tossed into a fireplace.
- S2 [core] The cone catches fire where it meets the flames.
- S3 [core] The cone glows.
- S4 [core] The cone crumbles into embers.
- S5 [minor] The embers fade.
- S6 [minor] The toss comes first and the catching follows.

**PC**
- P1 [core · process_direction]
  - expect: The cone only chars, glows and crumbles and does not return to whole pale wood.
  - fail: The cone turns back to pale unburnt wood; or the embers gather back into a whole cone; or the cone's scales close and lift again; or the burn front retreats leaving unburnt scales behind it.
- P2 [core · permanence_count]
  - expect: The cone shrinks to embers and ash rather than vanishing at a stroke, and the fire's wood keeps its number.
  - fail: The cone vanishes in a single frame while still whole; or a second cone appears in the air; or a log vanishes; or ash appears far from the cone with none falling there.
- P3 [major · gravity_direction]
  - expect: The cone falls downward into the fire, the flames climb upward around it and the embers settle in the grate.
  - fail: The cone rises out of the fire and hangs; or the flames point downward into the ash; or embers lift and stay aloft; or the cone falls upward out of the grate.
- P4 [major · missing_consequence]
  - expect: The cone catches where it meets the flames and its scales darken and open there first.
  - fail: The cone catches at a point no flame reached; or the cone rests in the flames and stays pale and closed to the end of the clip; or the flames pass through the cone and leave it untouched; or the cone glows while the flames are elsewhere in the grate.
- P5 [fatal · shape_identity]
  - expect: The cone stays a pine cone as it chars and crumbles into pieces; it does not turn into another material.
  - fail: The cone melts and drips; or the cone turns into another object; or the cone swells into a smooth ball; or the cone's scales fuse into one solid lump.
- P6 [minor · attribute_drift]
  - expect: The fireplace's surround, the grate and the hearth stay the same.
  - fail: The surround changes colour; or the grate changes shape; or items on the hearth rearrange.

**Note.** Who tosses the cone is not judged.

## HEAT-0286 · burn_smoke · eval

**Caption.** A candle burns inside a glass lantern hung outdoors, and its flame flickers as gusts pass but stays lit.

**Expectation (hidden).** The flame leans and dances with each gust and stands upright between gusts; the glass protects it from going out.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A candle burns inside a glass lantern hung outdoors.
- S2 [core] The flame flickers as gusts pass.
- S3 [core] The flame stays lit.
- S4 [minor] The flame stands upright between gusts.
- S5 [minor] Other signs of wind show: leaves, foliage or the lantern swinging.
- S6 [minor] The glass surrounds the flame.

**PC**
- P1 [core · causeless_motion]
  - expect: The flame dances when the gusts come, as the leaves and the swinging lantern show, and stands upright between them.
  - fail: The flame flickers hard while the leaves and the lantern hang dead still; or the flame stands dead steady while the lantern swings hard in a gust; or the flame's dancing follows a rhythm unrelated to any sign of wind; or the flame leans against the way the leaves are blown.
- P2 [core · gravity_direction]
  - expect: The flame points upward from the wick between gusts and the wax pools at the candle's top.
  - fail: The flame points downward between gusts; or hangs below the wick; or melted wax climbs the candle's side; or the flame lies flat inside still glass with nothing moving.
- P3 [major · process_direction]
  - expect: The flame stays alight through the gusts; if it goes out it stays out.
  - fail: The flame goes out and relights by itself; or shrinks to nothing and returns with each gust; or the wick's glow brightens into a flame with nothing touching it; or the flame splits into two flames.
- P4 [major · missing_consequence]
  - expect: The glass shields the flame: the flame moves less than the leaves and foliage outside the lantern do.
  - fail: The flame is flattened as hard as the leaves outside while the glass stands whole around it; or the flame is snuffed while the lantern's glass is whole and closed; or the flame is blown out by a gust that barely stirs the leaves.
- P5 [fatal · solidity]
  - expect: One candle inside one lantern; the glass stays whole and the flame stays inside it.
  - fail: The flame passes out through the glass and burns outside; or the candle passes through the lantern's base; or a second candle appears inside; or the lantern's glass vanishes.
- P6 [minor · attribute_drift]
  - expect: The lantern's frame, the candle's colour and the surroundings stay the same.
  - fail: The lantern's frame changes shape; or the candle changes colour; or the background changes between frames.

## HEAT-0287 · burn_smoke · eval

**Caption.** A floating candle in a bowl of water burns down until the flame reaches the water and goes out with a hiss.

**Expectation (hidden).** The flame shrinks as the wax runs out, dies the moment the water reaches the wick, and a wisp of smoke rises; the flame does not burn on at the waterline or relight.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] A candle floats in a bowl of water.
- S2 [core] The flame shrinks as the wax runs out.
- S3 [core] The water reaches the wick.
- S4 [core] The flame goes out.
- S5 [minor] A wisp of smoke rises.
- S6 [minor] The order is burning, shrinking, out.

**PC**
- P1 [core · process_direction]
  - expect: The flame only shrinks and then goes out and does not return; the wax level only drops.
  - fail: The flame relights by itself after going out; or the flame grows large again with no more wax; or the wax deepens with nothing added; or the flame flickers between lit and out after it has gone.
- P2 [core · missing_consequence]
  - expect: The flame goes out when the water reaches the wick and not before.
  - fail: The flame goes out while there is still a clear rim of wax above the water; or the water reaches the wick and the flame burns on at the waterline to the end of the clip; or the flame goes out while the wick is still dry; or the flame goes out while the candle is lifted clear of the water.
- P3 [major · gravity_direction]
  - expect: The candle floats at the surface, the flame stands upward from the wick and the smoke rises after it goes out.
  - fail: The candle sinks to the bowl's floor and the flame burns under water; or the flame points downward; or the smoke sinks over the bowl's rim and pools; or the candle rises out of the water and hangs.
- P4 [major · material_response]
  - expect: The candle floats as a soft wax disc with a pool of melt at its top, and the water stays a thin liquid that closes round it.
  - fail: The candle sits wholly on top of the water like a coin on a sheet; or the candle shatters; or the wax pool sets hard while the flame burns in it; or the water holds a dent around the candle like a solid.
- P5 [fatal · permanence_count]
  - expect: One candle in one bowl; the flame stays on the wick and the wax only goes.
  - fail: The flame separates from the wick and floats on the water; or a second candle appears; or the candle vanishes; or the water's level jumps with nothing added.
- P6 [minor · attribute_drift]
  - expect: The bowl, the water and the surroundings stay the same.
  - fail: The bowl changes pattern; or the water turns a colour; or items around the bowl rearrange.

**Note.** The hiss is sound and is not judged.

## HEAT-0288 · burn_smoke · eval

**Caption.** A pan of rice left on the stove boils dry, and smoke begins to rise as the grains on the bottom scorch black.

**Expectation (hidden).** Steam gives way to thin smoke as the last water goes, the smoke thickens and rises from the pan, and the blackening spreads from the bottom; the rice does not turn white again.

**Declared violation types.** process_direction, attribute_drift

**SA**
- S1 [core] A pan of rice sits on a stove.
- S2 [core] The steam gives way to thin smoke.
- S3 [core] The smoke rises from the pan.
- S4 [core] The grains on the bottom blacken.
- S5 [minor] The blackening spreads from the bottom.
- S6 [minor] The steam comes first and the smoke follows.

**PC**
- P1 [core · process_direction]
  - expect: The change runs one way: steam gives way to smoke as the last water goes, the smoke thickens and the blackening only spreads.
  - fail: The smoke gives way back to steam with the pan still on the heat; or a blackened grain turns white again; or the blackening spreads and then shrinks; or the water returns to the pan and the rice steams again.
- P2 [core · attribute_drift]
  - expect: The blackening happens in the rice at the pan's bottom and spreads from there, while the rice above stays paler.
  - fail: The rice at the top blackens while the grains on the pan's bottom stay white; or the pan's outside changes colour rather than the rice; or the whole panful blackens at once with no spreading; or the rice blackens before any steam has gone.
- P3 [major · gravity_direction]
  - expect: The smoke rises out of the pan, spreading and thinning.
  - fail: The smoke pours down the pan's sides and pools on the hob; or sinks below the pan; or hangs as a fixed shape without rising; or pours downward through the pan's base.
- P4 [major · missing_consequence]
  - expect: The smoke comes from the scorching rice at the pan's bottom and appears only once the water has gone.
  - fail: Thick smoke pours from the pan while water still stands in it and steam is rising; or the smoke comes from the hob beside the pan; or the rice blackens while no smoke leaves the pan at all.
- P5 [fatal · permanence_count]
  - expect: One pan of rice; the rice stays in the pan and its level only drops as the water goes.
  - fail: The rice's level rises with nothing added; or rice appears outside the pan with none leaving it; or a second pan appears; or rice passes through the pan's base.
- P6 [minor · attribute_drift]
  - expect: The pan's outside, the hob and the surroundings stay the same.
  - fail: The pan changes colour; or its handle changes shape; or items around the hob rearrange.

**Note.** The scorching of the rice is the caption's asserted outcome; the chemistry of it is not judged, only that the darkening runs one way and starts at the pan's bottom.

## HEAT-0289 · burn_smoke · eval

**Caption.** A stick of incense burns in a holder, and the grey ash column lengthens, curls, and finally drops into the tray.

**Expectation (hidden).** The glowing tip creeps down the stick as the ash above it grows and bends; the ash falls under gravity when it breaks and lands in the tray; the stick does not get longer and the ash does not reattach.

**Declared violation types.** process_direction, gravity_direction

**SA**
- S1 [core] A stick of incense burns in a holder.
- S2 [core] The glowing point creeps down the stick.
- S3 [core] The grey ash above the glowing point lengthens and curls.
- S4 [core] The ash breaks and drops into the tray.
- S5 [minor] Smoke rises from the glowing point.
- S6 [minor] The lengthening comes first and the dropping follows.

**PC**
- P1 [core · process_direction]
  - expect: The glowing point only creeps along the stick and the ash behind it only grows; burnt stick does not become fresh incense.
  - fail: The glowing point moves back the way it came; or the ash turns back into unburnt incense; or the stick grows longer as it burns; or the ash column shortens with nothing breaking off.
- P2 [core · gravity_direction]
  - expect: The ash column bends downward under its own weight and, when it breaks, falls straight down into the tray, while the smoke rises.
  - fail: The ash column bends upward; or a broken piece of ash rises or hangs in the air; or the ash falls upward out of the tray; or the smoke sinks and pools around the holder.
- P3 [major · missing_consequence]
  - expect: The ash builds behind the glowing point and the tray catches what falls from it.
  - fail: Ash appears in the tray with none falling from the stick; or the stick burns with no ash forming behind the glowing point at all; or the ash grows on the unburnt part ahead of the glowing point; or the smoke leaves a part of the stick that has not burnt.
- P4 [major · material_response]
  - expect: The ash is a fragile grey column that bends and crumbles, the unburnt stick stays rigid, and the smoke is a fine thread.
  - fail: The ash stays straight and bright like fresh incense; or the ash bends like rubber and springs back; or the unburnt stick sags; or the smoke holds a fixed rigid shape like a wire.
- P5 [fatal · permanence_count]
  - expect: One stick in one holder; the stick shortens only by burning and the ash goes only into the tray.
  - fail: A second stick appears already lit; or the stick vanishes while still long; or the glowing point jumps to a new place on the stick; or the ash reattaches to the stick after falling.
- P6 [minor · attribute_drift]
  - expect: The holder, the tray and the surroundings stay the same.
  - fail: The holder changes shape; or the tray changes colour; or items around the holder rearrange.

## HEAT-0290 · burn_smoke · eval

**Caption.** A burning sheet of newspaper is held up inside a fireplace opening, and its flames are pulled upward into the chimney.

**Expectation (hidden).** The flames and smoke bend up toward the flue rather than out into the room, and the paper is consumed from the burning edge inward; the flames do not lean out into the room or point downward.

**Declared violation types.** gravity_direction, causeless_motion

**SA**
- S1 [core] A burning sheet of newspaper is held inside a fireplace opening.
- S2 [core] The flames bend upward toward the flue.
- S3 [core] The smoke goes up the chimney.
- S4 [core] The paper is consumed from its burning edge inward.
- S5 [minor] The flames do not lean out into the room.
- S6 [minor] The paper blackens behind the flame front.

**PC**
- P1 [core · gravity_direction]
  - expect: The flames and smoke go upward into the flue rather than out into the room or downward.
  - fail: The flames lean out into the room away from the flue; or the smoke pours into the room and sinks to the hearth; or the flames point downward at the hearth; or the smoke hangs as a fixed shape without rising.
- P2 [core · causeless_motion]
  - expect: The flames lean toward the flue where the draught pulls them and keep that lean while the sheet is held in the opening.
  - fail: The flames lean toward the room's open side against the draught; or the flames' lean swings about while the sheet is held still and nothing else moves; or the flames stand dead straight while the smoke is drawn hard up the flue; or the flames lean out before the sheet is in the opening.
- P3 [major · process_direction]
  - expect: The burn advances from the burning edge into unburnt paper and the blackened paper stays black.
  - fail: Blackened paper turns white again; or the flame front retreats leaving unburnt paper behind it; or the sheet grows as it burns; or the paper catches at a spot no flame reached.
- P4 [major · material_response]
  - expect: The burning paper curls, blackens and thins and its ash flakes away; it does not melt or drip.
  - fail: The paper melts and runs like plastic; or stays flat and white while flames sit on it; or turns to ash without ever blackening or curling; or the sheet stiffens into a board as it burns.
- P5 [fatal · permanence_count]
  - expect: One sheet held in one fireplace; the paper shrinks to ash rather than vanishing while whole.
  - fail: The sheet vanishes in a single frame while still large; or a second sheet appears already burning; or ash appears on the hearth with none falling there; or the sheet passes through the fireplace's back wall.
- P6 [minor · attribute_drift]
  - expect: The fireplace's surround, the hearth and the room stay the same.
  - fail: The surround changes colour; or the hearth changes pattern; or items in the room rearrange.

**Note.** Whoever holds the sheet is not judged.

## HEAT-0291 · heat_response · eval

**Caption.** A sugar cube is dropped into a glass of hot water and another into a glass of cold water at the same moment, and the cube in hot water crumbles and vanishes first.

**Expectation (hidden).** Both cubes sink; the one in hot water darkens, slumps and disappears while the one in cold water is still a visible lump; the cold cube does not dissolve faster than the hot one.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] Two glasses of water stand side by side, one hot and one cold.
- S2 [core] A sugar cube is dropped into each at the same moment.
- S3 [core] Both cubes sink.
- S4 [core] The cube in the hot water darkens, slumps and disappears.
- S5 [core] The cube in the cold water is still a visible lump at that point.
- S6 [minor] Steam or ice shows which glass is which.

**PC**
- P1 [core · process_direction]
  - expect: Each cube only shrinks and crumbles and neither grows back; the difference between them does not reverse.
  - fail: A cube grows; or a crumbled cube gathers back into a whole cube; or the cube in the cold water disappears while the hot one is still a lump; or a cube alternates between larger and smaller.
- P2 [core · permanence_count]
  - expect: Each cube goes by dissolving into its own glass; the sugar does not appear elsewhere or vanish at a stroke while whole.
  - fail: A cube vanishes in a single frame while still square; or a third cube appears; or a cube passes through a glass's wall; or a cube moves from one glass to the other.
- P3 [major · gravity_direction]
  - expect: Both cubes fall downward into their glasses and sink to the bottom, and the sweet streams sink and spread.
  - fail: A cube floats at the surface and stays; or a cube hangs motionless in mid-water; or a cube rises out of the water; or the streams climb out of the water.
- P4 [major · material_response]
  - expect: Each cube is a pressed block of grains that wets, darkens and crumbles at its edges, and the water closes round it.
  - fail: A cube stays dry and sharp-edged under the water; or a cube melts into a glossy liquid lump; or a cube bounces off the glass's floor like a ball; or the water holds a dent around a cube like a solid.
- P5 [fatal · shape_identity]
  - expect: Two glasses and two cubes; the glasses keep their shapes and the cubes stay sugar as they crumble.
  - fail: A glass changes shape; or a cube turns into another object; or a cube fuses with the glass's floor; or a glass vanishes.
- P6 [minor · attribute_drift]
  - expect: The glasses' shapes, the table and the water's clarity stay the same.
  - fail: A glass changes pattern; or the table's setting rearranges; or a glass's water turns a colour.

## HEAT-0292 · heat_response · eval

**Caption.** A hot-air popcorn machine is switched on, and popped kernels burst out of the chute into a bowl.

**Expectation (hidden).** Kernels pop into much larger pieces and are blown out only after the machine has heated; the flow stops when it is switched off.

**Declared violation types.** process_direction, permanence_count, shape_identity

**SA**
- S1 [core] A hot-air popcorn machine stands with its chute over a bowl.
- S2 [core] The machine is switched on.
- S3 [core] Popped kernels come out of the chute.
- S4 [core] The popped pieces fall into the bowl.
- S5 [minor] The flow stops when the machine is switched off.
- S6 [minor] Nothing comes out before the machine is switched on.

**PC**
- P1 [core · process_direction]
  - expect: The pieces only come out while the machine runs and the bowl only fills; the flow stops when it is switched off.
  - fail: Pieces come out before the machine is switched on; or the bowl empties while the machine still runs; or the flow stops and starts again with the switch untouched; or pieces travel back up the chute into the machine.
- P2 [core · shape_identity]
  - expect: Each piece that leaves the chute is a large irregular white puff rather than a small hard grain, and unpopped kernels stay small and dark.
  - fail: Small hard kernels are blown out as if popped; or a popped piece turns back into a smooth yellow kernel; or a piece swells gradually like a balloon rather than bursting; or the pieces come out as one continuous mass.
- P3 [core · permanence_count]
  - expect: The popcorn in the bowl came out of the chute and none appears from nowhere.
  - fail: Pieces appear in the bowl with none leaving the chute; or the pile in the bowl shrinks while pieces keep arriving; or a piece vanishes in mid-air; or a second chute appears.
- P4 [major · gravity_direction]
  - expect: The pieces leave the chute, arc downward and land in the bowl or around it; they do not rise.
  - fail: The pieces rise from the chute and stay aloft; or hang in the air between chute and bowl; or fall upward out of the bowl; or the pile gathers on the machine's top.
- P5 [fatal · solidity]
  - expect: One machine with one chute and one bowl; the pieces pass through the chute's mouth and nothing passes through the machine's shell or the bowl.
  - fail: A piece passes out through the machine's shell; or a piece passes through the bowl's wall; or the chute passes into the bowl; or the machine changes shape.
- P6 [minor · attribute_drift]
  - expect: The machine's body, the bowl and the counter stay the same.
  - fail: The machine changes colour; or the bowl changes pattern; or items on the counter rearrange.

## HEAT-0293 · heat_response · eval

**Caption.** Two jars of honey are tipped side by side, one straight from the fridge and one that sat in the sun; the warm honey pours out in a quick stream while the cold honey barely moves.

**Expectation (hidden).** The warm honey flows out and down at once in a thinner stream; the cold honey creeps or stays put in the same time; neither flows upward and the cold jar does not empty faster.

**Declared violation types.** material_response, process_direction

**SA**
- S1 [core] Two jars of honey are tipped side by side.
- S2 [core] One jar has been in the sun and one in the fridge.
- S3 [core] The warm honey pours out in a stream.
- S4 [core] The cold honey creeps or stays put.
- S5 [minor] Both jars are tipped at about the same moment.
- S6 [minor] The difference between the two is plain.

**PC**
- P1 [core · material_response]
  - expect: Both are thick liquids, the warm one running in a thinner faster stream and the cold one creeping as a stiff mass that holds its shape.
  - fail: The cold honey pours out as freely as the warm one; or the warm honey stands as a rigid column as it leaves the jar; or the cold honey shatters as a solid; or the warm honey runs as thin as water and splashes.
- P2 [core · process_direction]
  - expect: Each honey only advances down and out and neither runs back up into its jar; the difference does not reverse.
  - fail: The cold jar empties faster than the warm one; or a stream runs back up into its jar; or the warm honey stops and the cold one speeds up with nothing changed; or the honey climbs the jar's inner wall and stays.
- P3 [major · gravity_direction]
  - expect: Both honeys move downward out of the tipped jars and fall or pile below.
  - fail: A honey runs upward out of a tipped jar; or a stream hangs in the air without falling; or the honey climbs the jar's outside; or a pile below rises back into a jar.
- P4 [major · missing_consequence]
  - expect: The jars show their contents moving: the warm jar's level drops while the cold jar's stays nearly still.
  - fail: The warm jar's level stays unchanged while a stream pours from it; or the cold jar's level drops as fast as the warm one's; or honey pours from a jar that is plainly still upright and untipped.
- P5 [fatal · permanence_count]
  - expect: Two jars of honey; the honey goes only from jar to the surface below and none appears from nowhere.
  - fail: Honey appears below a jar with none leaving it; or a jar refills itself; or a third jar appears; or honey passes through a jar's wall.
- P6 [minor · attribute_drift]
  - expect: The jars' labels, the honey's colour and the surface below stay the same.
  - fail: A label changes; or the honey changes colour; or the surface below changes pattern.

## HEAT-0294 · heat_response · eval

**Caption.** Candles are lit beneath a wooden Christmas pyramid, and its fan blades start turning and the figures rotate.

**Expectation (hidden).** The blades turn only after the candles are lit and slow to a stop when they are blown out.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A wooden Christmas pyramid stands with candles beneath its fan blades.
- S2 [core] The candles are lit.
- S3 [core] The fan blades start turning.
- S4 [core] The figures on the pyramid rotate.
- S5 [minor] The blades and figures are still before the candles are lit.
- S6 [minor] The lighting comes first and the turning follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The blades and figures stay still until the candles are lit, turn while they burn and slow to a stop when they are put out.
  - fail: The blades turn before the candles are lit; or they keep turning at the same rate after the candles are out; or they turn while the candles stand unlit; or they stop and start again while the candles burn steadily.
- P2 [core · missing_consequence]
  - expect: The rising air from the flames turns the blades and the figures turn with them, on the same shaft.
  - fail: The figures turn while the blades stand still; or the blades turn while the figures stay fixed; or the blades turn while the candles are plainly out; or the blades turn faster as the candles are blown out.
- P3 [major · trajectory_momentum]
  - expect: The blades turn about the pyramid's upright shaft in one direction and the tiers turn with them.
  - fail: The blades reverse direction with nothing changing; or the blades wobble off the shaft; or a tier turns the opposite way to the blades on the same shaft; or the whole pyramid slides across the table as it turns.
- P4 [major · gravity_direction]
  - expect: The flames point upward at the blades and the melted wax runs down the candles.
  - fail: A flame points downward; or a flame is drawn up into the blades and burns above them; or wax climbs a candle's side; or a flame hangs below its candle.
- P5 [fatal · permanence_count]
  - expect: One pyramid with its blades, tiers and figures; the figures keep their number and stay on their tiers.
  - fail: A figure vanishes; or a new figure appears on a tier; or a blade vanishes; or the pyramid's shaft passes through the table.
- P6 [minor · attribute_drift]
  - expect: The pyramid's wood, the figures' paint and the room stay the same.
  - fail: The wood changes colour; or a figure's paint changes; or items in the room rearrange.

## HEAT-0295 · heat_response · eval

**Caption.** A raw red steak is laid in a hot pan, and its surface turns from red to grey-brown from the edges inward while it sizzles.

**Expectation (hidden).** The colour change starts at the edges and where the meat touches the pan and spreads inward; it never reverses; the steak shrinks slightly and does not stay red on the hot surface.

**Declared violation types.** attribute_drift, process_direction

**SA**
- S1 [core] A raw red steak is laid in a hot pan.
- S2 [core] The steak's surface turns from red to grey-brown.
- S3 [core] The change spreads from the edges inward.
- S4 [core] The steak shrinks slightly.
- S5 [minor] The change starts where the meat touches the pan.
- S6 [minor] The laying down comes first and the colour change follows.

**PC**
- P1 [core · process_direction]
  - expect: The colour change only advances inward and the changed surface does not turn red again; the steak only shrinks.
  - fail: A greyed part turns red again in the hot pan; or the change spreads and then retreats; or the steak grows in the pan; or the change starts in the middle of the top face and works outward to the edges.
- P2 [core · attribute_drift]
  - expect: The change happens in the meat where it touches the hot pan and at its edges, and the pan's surface stays as it was.
  - fail: The pan's surface changes colour rather than the steak; or the steak's upper face greys while the side on the metal stays red; or the steak is grey-brown before it reaches the pan; or the whole steak changes colour in a single frame with no spreading.
- P3 [major · gravity_direction]
  - expect: The steak lies in the pan and any juices run to its low places and pool.
  - fail: The steak lifts off the pan and hangs; or the juices climb the pan's wall and stay; or the juices gather on top of the steak and stay; or the steak slides uphill in a tilted pan.
- P4 [major · material_response]
  - expect: The steak is a soft solid that stiffens and shrinks a little, staying one slab, and the juices are a thin liquid.
  - fail: The steak melts into a liquid; or the steak shatters; or the steak stretches longer as it cooks; or the juices set into a rigid crust that stands off the pan.
- P5 [fatal · permanence_count]
  - expect: One steak in one pan; the steak stays one piece and none appears or vanishes.
  - fail: A second steak appears; or the steak vanishes; or the steak splits into two whole steaks; or the steak passes through the pan's floor.
- P6 [minor · attribute_drift]
  - expect: The pan, the hob and the surroundings stay the same.
  - fail: The pan changes colour; or its handle changes shape; or items around the hob rearrange.

**Note.** The steak's colour change is the caption's asserted outcome; the chemistry of it is not judged, only that it runs one way and starts where the meat meets the pan.

## HEAT-0296 · heat_response · eval

**Caption.** A whole green pepper rests on a wire rack over a gas flame, and its skin blisters, puffs up and blackens where the flame touches it.

**Expectation (hidden).** Blisters rise and the skin darkens only on the side facing the flame, the black patches spreading and never fading; the skin does not smooth out again or blacken on the side away from the flame.

**Declared violation types.** material_response, attribute_drift

**SA**
- S1 [core] A whole green pepper rests on a wire rack over a gas flame.
- S2 [core] Blisters rise on the skin.
- S3 [core] The skin puffs up.
- S4 [core] The skin blackens where the flame touches it.
- S5 [minor] The side away from the flame stays green and smooth.
- S6 [minor] The blistering comes first and the blackening follows.

**PC**
- P1 [core · material_response]
  - expect: The skin lifts away from the flesh in blisters that stay raised and char, while the pepper keeps its body.
  - fail: The blisters sink back and the skin ends smooth; or the pepper's whole body collapses in a single frame; or the skin peels off as a rigid shell that keeps the pepper's shape; or the pepper melts and runs.
- P2 [core · attribute_drift]
  - expect: The blackening happens on the skin where the flame licks it and spreads from there; it never fades.
  - fail: A blackened patch fades back to green; or the side away from the flame blackens while the flame's side stays green; or the rack changes colour rather than the pepper; or the whole pepper blackens at once while the flame licks one spot.
- P3 [major · gravity_direction]
  - expect: The pepper rests on the rack, the flame points upward at it and any juices run down to the rack or the hob.
  - fail: The pepper lifts off the rack and hangs; or the flame points downward away from the pepper; or juices climb the pepper's side; or the flame hangs below the hob.
- P4 [major · process_direction]
  - expect: The blistering and the blackening only advance while the pepper is over the flame.
  - fail: A blister flattens and rises again with the pepper still over the flame; or the blackening spreads and shrinks in turn; or the skin blisters before the pepper is over the flame; or the blisters move to the side away from the flame.
- P5 [fatal · permanence_count]
  - expect: One pepper on one rack; the pepper stays one piece and the rack keeps its wires.
  - fail: A second pepper appears; or the pepper vanishes; or the pepper passes through the rack's wires; or a wire vanishes.
- P6 [minor · attribute_drift]
  - expect: The rack, the hob and the surroundings stay the same.
  - fail: The rack changes spacing; or the hob's knobs move by themselves; or items around the hob rearrange.

**Note.** The charring of the skin is the caption's asserted outcome; the chemistry of it is not judged, only that the darkening runs one way and appears where the flame touches.

## HEAT-0297 · heat_response · eval

**Caption.** A papadum is dropped into hot oil, and it puffs up and doubles in size within seconds.

**Expectation (hidden).** The flat disc blisters and expands as soon as it hits the oil and keeps its puffed shape when lifted out; it does not shrink back.

**Declared violation types.** shape_identity, process_direction

**SA**
- S1 [core] A flat papadum is dropped into hot oil.
- S2 [core] The papadum blisters.
- S3 [core] The papadum expands.
- S4 [core] The papadum keeps its puffed shape when lifted out.
- S5 [minor] The oil bubbles around it.
- S6 [minor] The drop comes first and the puffing follows.

**PC**
- P1 [core · shape_identity]
  - expect: The flat disc raises blisters and swells into a thicker bubbled round, staying one piece that keeps its outline.
  - fail: The papadum stays perfectly flat and smooth while plainly larger; or it swells into a smooth ball with no blisters; or it splits into separate pieces as it puffs; or it turns into another shape such as a tube.
- P2 [core · process_direction]
  - expect: The swelling only advances in the oil and the papadum does not shrink back once puffed.
  - fail: The papadum shrinks back flat in the oil; or it puffs and flattens in turn; or it is puffed before it reaches the oil; or it collapses as it is lifted out and stays flat.
- P3 [major · gravity_direction]
  - expect: The papadum rides at the oil's surface or is held under it, the bubbles rise, and any oil runs off it when lifted.
  - fail: The papadum sinks to the pot's floor and stays; or hangs motionless in mid-oil; or bubbles sink toward the pot's floor; or oil climbs the papadum as it is lifted out.
- P4 [major · missing_consequence]
  - expect: The oil shows the papadum arriving: it bubbles hard around it and the papadum goes glossy.
  - fail: The papadum enters and the oil stays glassy still; or the oil bubbles before the papadum reaches it; or the papadum puffs while the oil around it stays flat and clear; or the papadum stays dry and matt in the oil.
- P5 [fatal · permanence_count]
  - expect: One papadum in one pot; it stays one piece and the oil stays in the pot.
  - fail: A second papadum appears; or the papadum vanishes; or oil passes through the pot's wall; or the papadum passes through the pot's floor.
- P6 [minor · attribute_drift]
  - expect: The pot, the oil's colour and the surroundings stay the same.
  - fail: The pot changes colour; or the oil changes colour; or items around the pot rearrange.

**Note.** The papadum browning as it fries is chemistry and is not judged.

## HEAT-0298 · heat_response · eval

**Caption.** A pan straight from the stove is set down on a thin plastic cutting board, and the board warps and its edges lift.

**Expectation (hidden).** The board bends under and around the hot pan and keeps some of the warp after the pan is removed; it does not stay perfectly flat.

**Declared violation types.** material_response, process_direction

**SA**
- S1 [core] A pan is set down on a thin plastic cutting board.
- S2 [core] The board warps under the pan.
- S3 [core] The board's edges lift.
- S4 [core] Some of the warp stays after the pan is removed.
- S5 [minor] The board is flat at the start.
- S6 [minor] The setting down comes first and the warping follows.

**PC**
- P1 [core · material_response]
  - expect: The board is a thin plastic sheet that softens where the pan sits, bends around it and keeps its plastic look.
  - fail: The board shatters into pieces; or the board runs into a puddle; or the board stays perfectly flat while its edges are plainly lifted; or the board stretches like elastic.
- P2 [core · process_direction]
  - expect: The warp only deepens while the pan sits there and some of it remains after the pan is lifted.
  - fail: The board springs perfectly flat again the moment the pan is lifted; or the warp deepens and eases in turn; or the board warps before the pan is set down; or the board's edges lift and settle repeatedly with the pan still on it.
- P3 [major · gravity_direction]
  - expect: The board sags downward where the pan's weight presses and its free edges lift upward off the counter.
  - fail: The board bulges upward under the pan; or the board's edges curl downward through the counter; or the board lifts off the counter as a whole and hangs; or the pan rises off the board.
- P4 [major · missing_consequence]
  - expect: The warp forms where the hot pan rests and the board away from it stays flat.
  - fail: The board warps at a corner the pan never touched; or the pan sits on the board and it stays dead flat to the end of the clip; or the whole board warps evenly while the pan covers one part; or the counter warps rather than the board.
- P5 [fatal · permanence_count]
  - expect: One pan on one board; the board stays one sheet and the pan keeps its shape.
  - fail: The board splits into separate pieces; or a second board appears; or the pan sinks through the board; or the pan vanishes.
- P6 [minor · attribute_drift]
  - expect: The board's colour, the pan's finish and the counter stay the same.
  - fail: The board changes colour; or the pan changes colour; or items on the counter rearrange.

**Note.** Smoke or smell from the hot plastic is chemistry and is not judged.

## HEAT-0299 · heat_response · eval

**Caption.** A sealed, half-crushed plastic water bottle is dropped into a bowl of hot water, and its crushed sides push back out until the bottle is round.

**Expectation (hidden).** The dents move outward within seconds of the bottle entering the hot water and the bottle ends up round and taut; the sides do not cave in further or change before the bottle is in the water.

**Declared violation types.** shape_identity, process_direction

**SA**
- S1 [core] A sealed half-crushed plastic bottle.
- S2 [core] The bottle is dropped into a bowl of hot water.
- S3 [core] The crushed sides push outward.
- S4 [core] The bottle ends round and taut.
- S5 [minor] The bottle floats.
- S6 [minor] The drop comes first and the pushing out follows.

**PC**
- P1 [core · shape_identity]
  - expect: The dents move outward until the bottle's walls are round and taut, and the bottle stays one bottle of the same size.
  - fail: The dents press in further instead of pushing out; or new dents appear elsewhere on the bottle; or the bottle swells far beyond its original size; or the bottle turns into another shape such as a cube.
- P2 [core · process_direction]
  - expect: The change runs one way in the hot water: the dents only come out and do not press back in.
  - fail: A dent pushes out and then presses back in while the bottle stays in the hot water; or the dents come and go in turn; or the dents push out before the bottle reaches the water; or the walls ripple back and forth.
- P3 [major · gravity_direction]
  - expect: The bottle floats at the surface, bobbing, and the water stays level in the bowl.
  - fail: The bottle sinks to the bowl's floor and stays; or hangs motionless in mid-water; or rises out of the water and hangs above it; or the water's surface tilts and stays tilted with the bowl level.
- P4 [major · missing_consequence]
  - expect: The drop has an effect: the water splashes and ripples where the bottle lands and the bottle is wetted.
  - fail: The bottle enters and the surface stays glassy; or the water ripples before the bottle reaches it; or the bottle stays dry while floating; or the dents push out while the bottle is still in the air above the water.
- P5 [fatal · permanence_count]
  - expect: One bottle and one bowl; the bottle stays sealed in the water and nothing passes through the bowl.
  - fail: The bottle vanishes; or a second bottle appears; or water passes into the sealed bottle through its wall; or the bottle passes through the bowl's wall.
- P6 [minor · attribute_drift]
  - expect: The bottle's label, its cap and the bowl stay the same.
  - fail: The label changes; or the cap changes colour; or the bowl changes pattern.

## HEAT-0300 · heat_response · eval

**Caption.** Slices of cheese on toast sit under a hot grill, and the cheese bubbles and browns in dark spots.

**Expectation (hidden).** The cheese first goes glossy and soft, then bubbles rise and burst on its surface and brown patches appear and darken; the browning never lightens and the cheese does not firm back up under the grill.

**Declared violation types.** process_direction, attribute_drift

**SA**
- S1 [core] Slices of cheese sit on toast under a grill.
- S2 [core] The cheese goes glossy and soft.
- S3 [core] Bubbles rise and burst on the cheese's surface.
- S4 [core] Brown patches appear and darken.
- S5 [minor] The browning starts where the cheese is nearest the element.
- S6 [minor] The softening comes first and the browning follows.

**PC**
- P1 [core · process_direction]
  - expect: The cheese only softens, bubbles and browns further and does not firm back up or lighten under the grill.
  - fail: The cheese sets firm and matt again under the grill; or a brown patch fades back to pale cheese; or the browning spreads and then shrinks; or the cheese bubbles and goes flat and smooth in turn with the grill on.
- P2 [core · attribute_drift]
  - expect: The browning appears in the cheese itself, in patches nearest the element, and deepens from there.
  - fail: The toast's crust browns rather than the cheese; or the cheese browns evenly all over while the element is plainly on one side; or the cheese is brown before it goes under the grill; or the browning appears on the tray rather than the cheese.
- P3 [major · gravity_direction]
  - expect: The melted cheese slumps downward, spreads over the toast and runs off its edge, and the bubbles rise to its upper surface.
  - fail: The cheese climbs the toast's crust and stays; or the bubbles sink through the cheese into the toast; or melted cheese lifts off the toast; or the cheese runs uphill on a tilted tray.
- P4 [major · material_response]
  - expect: The cheese is a thick liquid that bubbles slowly and holds a rounded edge, and the toast stays firm bread beneath it.
  - fail: The cheese runs as thin as water; or the bubbles hold their domes as rigid shells; or the cheese shatters dry; or the toast flows like batter under the cheese.
- P5 [fatal · permanence_count]
  - expect: The slices on the toast are the slices that were laid there; the cheese goes only onto the toast and the tray.
  - fail: A slice vanishes; or a new slice appears on the toast; or the cheese grows in amount with none added; or cheese appears on the tray with none running off.
- P6 [minor · attribute_drift]
  - expect: The toast's crust, the tray and the surroundings stay the same.
  - fail: The crust changes shape; or the tray changes colour; or items around the tray rearrange.

**Note.** The browning of the cheese is the caption's asserted outcome; the chemistry of it is not judged, only that it runs one way and appears nearest the element.

