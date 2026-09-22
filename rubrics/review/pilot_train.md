# Rubric review

50 rubrics. SA = caption adherence (core/minor); PC = physics (fatal/core/major/minor, each tagged with a violation type). Expectation is the hidden field from data/, shown for the reviewer only.

# Mechanics

## MECH-0001 · inertia · train

**Caption.** Two passengers sit in the back seat of a car when it brakes hard, and both are thrown forward against their seat belts.

**Expectation (hidden).** The lurch happens at the moment of braking, not before or after; it is forward, not backward or sideways; they settle back once the car has stopped.

**Declared violation types.** causeless_motion, trajectory_momentum

**SA**
- S1 [core] Two passengers sit in the back seat of a car.
- S2 [core] The car brakes hard: the view outside slows sharply or the car pitches, and the passengers react.
- S3 [core] Both passengers pitch forward against their seat belts.
- S4 [minor] Seat belts are visible across the passengers.
- S5 [minor] The lurch follows the braking rather than preceding it.

**PC**
- P1 [core · causeless_motion]
  - expect: The passengers' forward lurch begins with the braking and only then; before it they sit at rest relative to the seat.
  - fail: The passengers pitch forward while the car is still cruising steadily; or they lurch with no braking visible at all; or one lurches long after the other under the same braking.
- P2 [core · trajectory_momentum]
  - expect: The lurch is toward the front of the car, the belts arrest it, and afterwards the passengers settle back into the seat.
  - fail: The passengers are thrown backward into the seat or sideways; or they keep travelling forward past where the belt holds them; or they are flung out of the seat entirely.
- P3 [major · material_response]
  - expect: The belts behave as inextensible straps: they go taut across the body, hold, and go slack again only as the passenger settles back.
  - fail: A belt stretches far out like a rubber band; or hangs slack while the passenger is plainly pressing into it; or the belt goes rigid and stands away from the body.
- P4 [major · trajectory_momentum] (if: Loose objects or hanging items are visible inside the car.)
  - expect: Loose objects and hanging items in the cabin swing or slide forward at the same moment as the passengers.
  - fail: Loose objects stay put or slide backward while the passengers pitch forward; or they move before the passengers do.
- P5 [fatal · shape_identity]
  - expect: Passengers, belts and seats keep their number and shape and nothing passes through anything.
  - fail: A passenger merges with the seat or with the other passenger; or a belt passes through a body; or a limb appears, vanishes or detaches; or a head passes through the headrest.
- P6 [minor · attribute_drift]
  - expect: Clothing colours, the car interior and the view through the windows stay consistent apart from the braking.
  - fail: A passenger's clothing changes colour; or the seat pattern changes; or the outside scene jumps to a different place.

**Note.** Inertia scene: the people are kept because their bodies are what shows the lurch. Facial expressions, seating posture and how hard the brake is applied are not judged; only when and which way the bodies move.

## MECH-0018 · gravity_fall · train

**Caption.** A bag of oranges tips over at the top of a staircase, and the oranges spill out and tumble down the stairs to the bottom.

**Expectation (hidden).** The oranges bounce from step to step and gather at the bottom; none stay in the air, roll upward, or stop on a step without reason.

**Declared violation types.** gravity_direction, trajectory_momentum

**SA**
- S1 [core] A bag containing oranges is present at the top of a staircase.
- S2 [core] The bag tips over and oranges spill out of it.
- S3 [core] The oranges travel down the stairs toward the bottom.
- S4 [minor] Several oranges are involved rather than a single one.
- S5 [minor] The tipping comes first, then the spill, then the tumble down the stairs.

**PC**
- P1 [core · gravity_direction]
  - expect: Every orange that leaves the bag moves downward from step to step; only the steps, the walls or another orange stop or redirect it.
  - fail: An orange rolls up a step or climbs the stairs; or hovers above a step; or stops in mid-air.
- P2 [major · trajectory_momentum]
  - expect: Each orange bounces off the step it hits and leaves it downward and away, no higher than where it came from; the oranges spread apart as they tumble.
  - fail: An orange rebounds higher than the step it fell from; or reverses back up the staircase after a bounce; or all the oranges move as one rigid formation.
- P3 [major · causeless_motion]
  - expect: Oranges start moving only after the bag tips, and an orange that has come to rest stays at rest.
  - fail: Oranges are rolling out before the bag tips; or an orange that has stopped on a step or the floor sets off again with nothing touching it.
- P4 [major · material_response]
  - expect: The oranges stay round and firm through their impacts; they may bruise or split but do not flow or stretch.
  - fail: An orange flattens like dough on landing and stays flat; or splashes like a liquid; or stretches as it falls.
- P5 [fatal · permanence_count]
  - expect: The oranges keep their number and shape and the bag stays one bag; nothing passes through a step or through the bag.
  - fail: Oranges appear from nowhere, vanish or merge; or an orange passes through a step or the bag's cloth; or an orange turns into a different object.
- P6 [minor · attribute_drift]
  - expect: The staircase, walls and bag keep their colour and layout while the oranges tumble.
  - fail: Steps change count or shape between frames; or the bag changes colour or size; or an orange changes colour mid-tumble.

## MECH-0032 · collision · train

**Caption.** A white cue ball rolls straight into a red ball sitting still on a pool table; the red ball rolls away and the cue ball stops.

**Expectation (hidden).** The red ball sets off in the direction the cue ball was travelling at the instant of contact; the cue ball loses almost all its speed; the balls do not overlap.

**Declared violation types.** trajectory_momentum, missing_consequence

**SA**
- S1 [core] A white cue ball and a red ball are on a pool table.
- S2 [core] The cue ball rolls into the red ball, which is still before contact.
- S3 [core] After contact the red ball rolls away and the cue ball is stopped or nearly stopped.
- S4 [minor] The cue ball approaches on a straight path.
- S5 [minor] The moving ball is white and the struck ball is red.

**PC**
- P1 [core · missing_consequence]
  - expect: The red ball is set in motion by the contact: it starts moving at the moment the cue ball reaches it, not before and not without it.
  - fail: The cue ball touches the red ball and the red ball does not move; or the red ball starts rolling before the cue ball arrives; or the cue ball stops short of the red ball and the red ball rolls away anyway.
- P2 [core · trajectory_momentum]
  - expect: After a head-on hit the red ball leaves along the cue ball's line of approach and the cue ball's speed drops sharply, so the red ball is the faster of the two afterwards.
  - fail: The red ball leaves at a sharp angle or back toward the cue ball after a square hit; or the cue ball keeps rolling at its previous speed after the hit; or both balls move off together at the same speed in the same direction.
- P3 [major · causeless_motion]
  - expect: Once moving, each ball rolls straight and slows gradually; a ball at rest stays at rest until struck.
  - fail: A ball curves or changes direction on the open cloth with nothing touching it; or speeds up on its own; or a stopped ball starts rolling again untouched.
- P4 [major · material_response]
  - expect: The balls are hard and round: the contact is a brief click and each ball keeps its shape.
  - fail: A ball dents or flattens at the contact; or the balls stick together and travel as a pair; or a ball wobbles like jelly.
- P5 [fatal · permanence_count]
  - expect: Two balls remain two balls; neither passes into the other or through the table.
  - fail: The balls overlap or pass through each other; or a ball vanishes, splits or a third ball appears; or a ball sinks into the cloth.
- P6 [minor · attribute_drift]
  - expect: The balls keep their colours and the table markings stay put.
  - fail: The cue ball turns red or the red ball turns white; or the balls swap colours after contact; or table spots and lines shift between frames.

## MECH-0048 · friction_rolling · train

**Caption.** A loaded sled slides down a snowy slope, runs out onto a flat patch of bare grass, and stops within a short distance.

**Expectation (hidden).** The slowing begins where the snow ends and is much sharper on grass than it was on snow; the sled does not keep gliding or stop while still on snow.

**Declared violation types.** causeless_motion, trajectory_momentum

**SA**
- S1 [core] A sled carrying a load is present on a snowy slope.
- S2 [core] The sled slides down the slope.
- S3 [core] The sled runs onto a patch of bare grass at the bottom and comes to a stop there.
- S4 [minor] The slope shows snow and the flat run-out shows grass: a visible change of surface.
- S5 [minor] The order is descent on snow, then grass, then stop.

**PC**
- P1 [core · trajectory_momentum]
  - expect: On snow the sled keeps gliding; the sharp slowing begins where the runners reach the grass, and the sled stops within a short run on the grass.
  - fail: The sled stops dead while still on the snow slope with nothing in its way; or glides across the grass without slowing, as if still on snow; or slows and then speeds up again on the flat.
- P2 [major · causeless_motion]
  - expect: The sled moves only downhill under gravity and stays stopped once it has stopped; it does not start, turn or restart untouched.
  - fail: The sled sets off uphill; or turns sharply on open ground with nothing deflecting it; or moves again after having come to rest.
- P3 [major · gravity_direction]
  - expect: The sled keeps contact with the surface and its load rides on it; a hard stop may pitch the load forward but not upward or backward.
  - fail: The sled floats above the snow or grass; or the load rises off the sled with nothing lifting it; or the load is thrown backward, uphill, when the sled stops.
- P4 [major · material_response] (if: Snow or grass is visibly disturbed by the runners.)
  - expect: Snow thrown up by the runners falls back to the ground; grass under the sled is flattened, not sprayed.
  - fail: Snow spray hangs in the air or rises away; or the sled ploughs through the grass as if it were loose powder.
- P5 [fatal · permanence_count]
  - expect: One sled and its load keep their shape and number and stay above the ground.
  - fail: The sled or its load vanishes, duplicates or changes into another object; or the sled passes through the ground or a fence.
- P6 [minor · attribute_drift]
  - expect: The load's contents, the sled's colour and the boundary between snow and grass stay consistent throughout.
  - fail: The load changes contents or colour; or the snow-grass boundary shifts between frames; or the slope changes shape.

## MECH-0062 · projectile · train

**Caption.** A soft ball is tossed in a gentle arc across a lawn and lands in a laundry basket standing on the grass.

**Expectation (hidden).** The ball follows a smooth arc, rising then falling; it does not fly straight, hang in the air, or change direction midway.

**Declared violation types.** trajectory_momentum, gravity_direction

**SA**
- S1 [core] A soft ball is present.
- S2 [core] A laundry basket stands on grass.
- S3 [core] The ball is tossed and travels through the air toward the basket.
- S4 [core] The ball lands in the basket.
- S5 [minor] The toss is a gentle lob in an arc, not a hard throw.
- S6 [minor] The setting is a lawn.

**PC**
- P1 [core · trajectory_momentum]
  - expect: In flight the ball follows one smooth curve that rises, peaks and falls; its sideways motion keeps going in the same direction until it lands.
  - fail: The ball flies in a straight line at constant height; or hangs at the top of its arc; or changes direction midway with nothing touching it; or stops and then continues.
- P2 [major · gravity_direction]
  - expect: After the peak the ball descends, and once in the basket it stays down.
  - fail: The ball rises again after starting to fall; or bobs up out of the basket with nothing pushing it; or drifts sideways over the basket without descending.
- P3 [major · material_response]
  - expect: The soft ball rebounds little: it may flex on impact and settle; the basket stays rigid and at most rocks.
  - fail: The ball bounces back out as high as it came in; or the ball flattens and stays flat; or the basket crumples or ripples like cloth under the ball.
- P4 [major · causeless_motion]
  - expect: The basket stays still until the ball arrives.
  - fail: The basket slides or rocks before the ball reaches it; or moves toward the ball as if to catch it.
- P5 [fatal · permanence_count]
  - expect: One ball, one basket; both keep their shape and identity, and the ball passes through neither the basket wall nor the ground.
  - fail: The ball vanishes in flight or a second ball appears; or the ball turns into another object; or it passes through the basket wall or the ground.
- P6 [minor · attribute_drift]
  - expect: The ball keeps its colour and size in flight; the basket and lawn stay unchanged.
  - fail: The ball changes colour or size while in the air; or the basket changes pattern; or the lawn changes texture.

## MECH-0078 · balance_topple · train

**Caption.** A tall stack of cardboard boxes in a hallway is pushed from one side and topples, boxes tumbling to the floor.

**Expectation (hidden).** The stack leans away from the push before falling; the upper boxes go first and fall on the side away from the push; they do not float or fall toward it.

**Declared violation types.** gravity_direction, trajectory_momentum

**SA**
- S1 [core] A tall stack of cardboard boxes stands in a hallway.
- S2 [core] The stack is pushed from one side.
- S3 [core] The stack topples and boxes fall to the floor.
- S4 [minor] Several boxes are stacked vertically.
- S5 [minor] The push comes first, then the lean, then the fall.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The stack leans away from the side it is pushed from, the top moving furthest first, and falls on that far side.
  - fail: The stack leans or falls toward the pusher; or the bottom box moves first while the top stays put; or the boxes drop straight down in place without leaning.
- P2 [major · gravity_direction]
  - expect: Every box that leaves the stack moves downward until it meets the floor or another box, and comes to rest on the floor.
  - fail: A box floats or hangs in the air; or moves upward after leaving the stack; or drifts along the hallway with nothing pushing it.
- P3 [major · causeless_motion]
  - expect: Nothing moves until the push arrives; boxes that have landed stay where they land.
  - fail: The stack begins leaning before anything touches it; or a landed box slides, rights itself or restacks by itself.
- P4 [major · material_response]
  - expect: Boxes stay boxy: corners may dent or crush on impact, but they do not bounce high, wobble like jelly or fold like cloth.
  - fail: A box bounces back up as high as it fell; or ripples like fabric; or flattens completely and re-inflates.
- P5 [fatal · permanence_count]
  - expect: The boxes keep their number and identity and pass through nothing.
  - fail: Boxes vanish, multiply or merge as they fall; or a box passes through another box, the wall or the floor; or a box changes into a different object.
- P6 [minor · attribute_drift]
  - expect: Box labels, tape and colours, and the hallway itself, stay the same through the fall.
  - fail: A box's colour or printing changes between frames; or the hallway walls shift; or a box changes size mid-fall.

## MECH-0094 · tension · train

**Caption.** Two large dogs each grab an end of a slack rope toy lying on the grass and pull; the rope goes taut and the middle knot moves toward the stronger dog.

**Expectation (hidden).** The rope straightens between the dogs before the knot moves, bows only where the jaws grip it, and stays taut while they pull.

**Declared violation types.** material_response, missing_consequence

**SA**
- S1 [core] Two large dogs are present.
- S2 [core] A rope toy with a knot in the middle lies slack on the grass at the start.
- S3 [core] Each dog takes hold of one end of the rope.
- S4 [core] The dogs pull and the rope goes taut.
- S5 [core] The knot moves toward one of the dogs.
- S6 [minor] The setting is grass outdoors.

**PC**
- P1 [core · material_response]
  - expect: The rope transmits pull only when taut: it straightens between the two mouths first, and only then does the knot travel, toward the dog that is gaining ground.
  - fail: The knot slides along a rope that is still slack; or the rope lengthens like elastic as the dogs back away; or the taut rope sags in the middle while both dogs are plainly pulling.
- P2 [core · missing_consequence]
  - expect: Each dog's pull has a visible effect: the rope is drawn straight between them, and a dog that backs away drags the rope and the other dog's head with it.
  - fail: Both dogs pull and the rope stays slack on the grass; or a dog backs away and its rope end stays where it was; or the knot moves toward the dog that is being dragged.
- P3 [major · trajectory_momentum]
  - expect: Once taut the rope moves as one piece: the knot and both ends move the same way when the winning dog backs up.
  - fail: The knot moves one way while the rope ends move the other; or one end moves while the rope between stays fixed; or the rope moves before either dog does.
- P4 [major · gravity_direction]
  - expect: Slack parts of the rope hang or lie on the grass; the taut rope runs straight between the mouths and sags only when the pull eases.
  - fail: A slack loop of rope hangs in the air with nothing holding it; or the rope floats up off the grass before the dogs pull.
- P5 [fatal · permanence_count]
  - expect: One rope with one knot and two dogs; the rope stays a single continuous piece and passes through nothing.
  - fail: The rope splits into two ropes or gains a second knot; or an end passes through a dog's head or the rope through itself; or a dog vanishes or duplicates; or the knot disappears.
- P6 [minor · attribute_drift]
  - expect: The rope's colours and the dogs' coats stay the same.
  - fail: The rope changes colour or texture; or the knot changes size; or a dog's coat changes pattern between frames.

**Note.** The dogs are self-driven: how hard they pull, which one wins and their footing are not judged. Only the rope's response to the pull is.

## MECH-0110 · deformation · train

**Caption.** A hand squeezes a wet kitchen sponge over a sink, water streams out, and the sponge springs back to shape when the hand opens.

**Expectation (hidden).** The sponge compresses only while squeezed and the water runs out during the squeeze; the recovery is quick and nearly complete.

**Declared violation types.** material_response, process_direction

**SA**
- S1 [core] A wet kitchen sponge is held in a hand over a sink.
- S2 [core] The hand squeezes and the sponge compresses.
- S3 [core] Water comes out of the sponge.
- S4 [core] The hand opens and the sponge returns toward its shape.
- S5 [minor] A sink is below the sponge.
- S6 [minor] The order is squeeze, water out, release, spring back.

**PC**
- P1 [core · material_response]
  - expect: The sponge compresses only where and while it is squeezed and expands again when the grip opens, recovering most of its shape.
  - fail: The sponge stays crushed after the hand opens; or it expands while the hand is still closed on it; or it compresses before the fingers close; or it behaves as a rigid block that does not compress.
- P2 [core · process_direction]
  - expect: Water leaves the sponge during the squeeze and runs down into the sink; the sponge does not take water back in from the air.
  - fail: Water streams out while the sponge is unsqueezed; or water rises from the sink back into the sponge; or the sponge grows wetter as it is squeezed.
- P3 [major · gravity_direction]
  - expect: The released water falls straight down into the sink.
  - fail: Water floats away from the sponge; or flows sideways or upward; or hangs beneath the sponge without falling.
- P4 [major · material_response]
  - expect: The expelled water behaves as a liquid: a stream or drips that splash and spread in the sink.
  - fail: The water comes out as solid lumps; or as balls that bounce off the sink like rubber; or it keeps a fixed shape after leaving the sponge.
- P5 [fatal · shape_identity]
  - expect: One hand with its fingers and one sponge keep their number and identity; the hand does not pass through the sponge.
  - fail: Fingers multiply, vanish or pass through the sponge; or the sponge splits in two or merges with the hand; or water appears away from the sponge or vanishes in mid-air.
- P6 [minor · attribute_drift]
  - expect: The sponge keeps its colours and the sink stays the same.
  - fail: The sponge changes colour or its scouring side swaps; or the sink's contents change between frames.

## MECH-0127 · cut_tear · train

**Caption.** A sheet of coloured paper is cut in half with scissors, and the two halves fall apart on the table.

**Expectation (hidden).** The paper parts exactly where and when the blades close, leaving straight edges; it is not cut ahead of the blades and the halves do not rejoin.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A sheet of coloured paper and a pair of scissors are present.
- S2 [core] The scissors cut across the sheet.
- S3 [core] The sheet ends up as two separate pieces.
- S4 [minor] The pieces lie apart on a table.
- S5 [minor] The cut runs through the sheet roughly in half rather than snipping a corner.
- S6 [minor] The cut comes first and the halves separate after it.

**PC**
- P1 [core · missing_consequence]
  - expect: The paper parts exactly where the blades close and only as far as they have closed; the cut edge advances with the blades.
  - fail: The blades close through the paper and it stays whole; or the sheet splits ahead of the blades or along a line the blades never touched; or the paper is already in two before the scissors reach it.
- P2 [major · process_direction]
  - expect: Once cut, the edges stay cut; the two pieces separate and do not rejoin.
  - fail: A cut heals or the halves fuse back into one sheet; or the cut line shifts position after it is made.
- P3 [major · gravity_direction]
  - expect: Freed parts of the paper drop or slide down onto the table and stay there.
  - fail: A half hangs in the air unsupported; or drifts upward; or slides across the table on its own after settling.
- P4 [major · material_response]
  - expect: The paper behaves as a thin sheet: it flexes, its cut edge is a clean line, and the scissors stay rigid.
  - fail: The paper stretches like rubber before parting; or shatters like glass; or the scissor blades bend or pass through each other.
- P5 [fatal · permanence_count]
  - expect: One sheet becomes exactly two pieces that together make up the original; the scissors stay one pair.
  - fail: A third piece appears or a half vanishes; or the pieces change size after the cut; or the scissors duplicate or merge with the paper; or the blades pass through the hand.
- P6 [minor · attribute_drift]
  - expect: The paper's colour and the table stay the same on both pieces.
  - fail: One half changes colour; or the paper's printed side changes; or the table surface shifts.

## MECH-0143 · fluid · train

**Caption.** Water is poured from a jug into an empty drinking glass on a table until the glass is nearly full.

**Expectation (hidden).** A continuous stream falls from the jug into the glass and the level rises steadily while the jug empties; the water does not vanish, flow upward, or appear in the glass before the stream reaches it.

**Declared violation types.** material_response, process_direction

**SA**
- S1 [core] A jug and a drinking glass are present, the glass empty at the start.
- S2 [core] Water is poured from the jug into the glass.
- S3 [core] The glass fills toward nearly full.
- S4 [minor] The pour stops before the glass overflows.
- S5 [minor] The glass stands on a table.

**PC**
- P1 [core · process_direction]
  - expect: The water level in the glass rises steadily while the stream is flowing, stays flat, and does not drop or reset while the pour continues.
  - fail: The level goes down while water is still entering; or jumps up or down between frames; or the glass is full before the stream reaches it.
- P2 [core · material_response]
  - expect: Water leaves the jug as a continuous stream that falls into the glass, splashing or swirling on arrival, and settles to a flat surface.
  - fail: The stream hangs as a rigid, glassy rod that does not move; or the water in the glass keeps a tilted or humped surface once the pour stops; or the water behaves as a solid block.
- P3 [major · gravity_direction]
  - expect: The stream falls straight down from the jug's lip to the glass.
  - fail: The stream curves upward or sideways with no wind; or water flows from the glass up into the jug; or the stream bends around the glass.
- P4 [major · missing_consequence] (if: The jug's tilt is visible.)
  - expect: The jug's tilt produces the stream: water flows only while the jug is tipped and stops when it is righted.
  - fail: Water pours from a level jug; or the jug is tipped and no water comes out; or the stream continues after the jug is upright.
- P5 [fatal · permanence_count]
  - expect: One jug, one glass; water appears only from the jug and ends up only in the glass, on the table or in the air between.
  - fail: Water appears in the glass with no stream connecting it; or the stream passes through the glass wall; or the glass or jug duplicates, vanishes or changes shape.
- P6 [minor · attribute_drift]
  - expect: The glass, jug and table keep their appearance; the water stays clear.
  - fail: The water changes colour; or the glass changes shape or size; or the table pattern shifts.

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

# Optics

## OPT-0001 · shadow · train

**Caption.** A wooden puppet hanging in a sunny window lifts one arm as its string is pulled, and its shadow on the wall lifts its arm too.

**Expectation (hidden).** The shadow's arm moves at the same instant and in the same direction as the puppet's; the shadow stays joined at the feet and falls on the side away from the sun.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A wooden puppet on strings hangs in a window with sunlight coming through.
- S2 [core] The puppet's arm lifts as a string is pulled.
- S3 [core] The puppet's shadow is visible on a wall.
- S4 [core] The shadow's arm lifts too.
- S5 [minor] The strings and their movement are visible.
- S6 [minor] The shadow shows a recognisable puppet outline with head, body and arms.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow's arm moves when the puppet's arm moves, at the same time and in the corresponding direction.
  - fail: The puppet's arm lifts and the shadow is unchanged; or the shadow's arm moves first or noticeably after; or the shadow's arm goes down as the puppet's goes up; or the shadow moves an arm while the puppet is still.
- P2 [core · shape_identity]
  - expect: The shadow keeps the puppet's silhouette: the same number of limbs and the same proportions; only the parts that move on the puppet change on the shadow.
  - fail: The shadow shows a different figure or extra limbs; or the shadow's shape changes with the puppet unchanged; or it splits into two shadows.
- P3 [major · missing_consequence]
  - expect: The shadow lies on the side of the puppet away from the window; light and shadow are on opposite sides.
  - fail: The shadow falls on the window side, between the puppet and the sun; or the shadow appears on two opposite walls at once.
- P4 [major · causeless_motion]
  - expect: The shadow does not move on its own: when the puppet hangs still the shadow is still, apart from any sway the puppet shows.
  - fail: The shadow drifts across the wall while the puppet hangs still; or the shadow swings with no matching sway of the puppet.
- P5 [fatal · permanence_count]
  - expect: One puppet and one shadow of it; the puppet keeps its parts and does not pass through the window or wall.
  - fail: The puppet gains or loses a limb; or a second puppet appears; or the puppet passes through the glass; or the shadow becomes a solid object.
- P6 [minor · attribute_drift]
  - expect: The puppet's paint, the wall colour and the window frame stay the same; the shadow stays dark rather than turning coloured.
  - fail: The puppet changes colour; or the shadow turns bright or coloured; or the wall texture changes.

## OPT-0002 · shadow · train

**Caption.** A riderless skateboard rolls past a streetlamp at night, and its shadow swings around it as it passes under the light.

**Expectation (hidden).** The shadow points away from the lamp: it trails behind the board as it approaches, shortens under the lamp, and stretches out ahead once it has passed; it never points toward the lamp.

**Declared violation types.** missing_consequence, trajectory_momentum

**SA**
- S1 [core] A skateboard with no rider is present.
- S2 [core] It rolls along the ground.
- S3 [core] A lit streetlamp stands nearby and it is night.
- S4 [core] The skateboard's shadow is visible and changes as the board passes the lamp.
- S5 [minor] The board passes close to or under the lamp.
- S6 [minor] The scene is dark apart from the lamp light.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow lies on the side of the board away from the lamp: behind it while approaching, short beneath it under the lamp, stretching ahead once past.
  - fail: The shadow points toward the lamp; or stays fixed on one side of the board as it passes; or the shadow does not move with the board; or no shadow is cast under a lit lamp.
- P2 [major · trajectory_momentum]
  - expect: The board rolls in a straight line at a steady, gently slowing pace.
  - fail: The board speeds up on the flat with nothing pushing it; or turns or reverses by itself; or hops.
- P3 [major · shape_identity]
  - expect: The shadow keeps the board's outline, deck and wheels, and stays attached at the wheels.
  - fail: The shadow detaches from the wheels; or has a different shape from the board; or splits into two shadows under one lamp.
- P4 [major · causeless_motion]
  - expect: The shadow moves only as the board moves; the lamp stays lit and steady.
  - fail: The shadow swings while the board is stationary; or the lamp goes out or moves; or the shadow changes length with the board standing still.
- P5 [fatal · permanence_count]
  - expect: One board with its wheels and one shadow; nothing appears, vanishes or passes through the pavement.
  - fail: The board vanishes or duplicates; or a rider appears from nowhere; or wheels vanish; or the board passes through the lamp post.
- P6 [minor · attribute_drift]
  - expect: The deck's colour and graphics, the lamp and the street stay the same.
  - fail: The deck changes colour; or the lamp changes colour; or the street markings shift.

## OPT-0049 · reflection · train

**Caption.** A toy robot in front of a mirror raises its right arm, and its reflection raises the arm on the opposite side.

**Expectation (hidden).** The reflected arm rises at the same instant and mirrored left-right; the reflection faces the robot and matches its colours; it does not lag or move differently.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A toy robot stands in front of a mirror.
- S2 [core] The robot raises one arm.
- S3 [core] The robot's reflection is visible in the mirror.
- S4 [core] The reflection raises an arm.
- S5 [minor] The reflection raises the arm that corresponds to the robot's raised arm: the one directly across the mirror from it.
- S6 [minor] The robot reads as a toy robot: blocky and mechanical.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflection moves exactly when the robot moves: its arm rises together with the robot's arm and stops when it stops.
  - fail: The robot's arm rises and the reflection's arms stay down; or the reflection moves first or later; or the reflection raises an arm while the robot is still; or the reflected arm goes down as the real one goes up.
- P2 [core · shape_identity]
  - expect: The reflection is a mirror image: the same robot in the same colours, facing the real one, with every part directly across the mirror surface from the real part, so the raised arm appears on the same side of the frame as the real raised arm.
  - fail: The reflected raised arm is on the other side of the frame from the real one, as in a rotated copy rather than a mirror image; or the reflection shows the robot's back; or it is a different robot or colour; or it is upside down.
- P3 [major · causeless_motion]
  - expect: The reflection does not move on its own.
  - fail: The reflection turns, shifts or waves while the robot is stationary; or the reflection slides across the mirror with neither robot nor camera moving.
- P4 [major · material_response]
  - expect: The mirror is a flat rigid surface: the reflection is undistorted and keeps the robot's proportions.
  - fail: The mirror surface ripples like water; or the reflection stretches or warps while the robot is unchanged; or the mirror bends.
- P5 [fatal · permanence_count]
  - expect: One robot and one reflection; the reflection stays inside the mirror and the robot keeps all its parts.
  - fail: The reflection steps out of the mirror or appears outside its frame; or a second robot appears; or the robot loses or gains an arm; or the robot passes into the mirror.
- P6 [minor · attribute_drift]
  - expect: Robot colours and the mirror frame stay the same; the reflection's colours match the robot's throughout.
  - fail: The robot or its reflection changes colour; or the frame changes; or the reflection's colours drift away from the robot's.

**Note.** Mirror geometry: each point of the image lies directly across the mirror from the real point, so the reflected raised arm is on the SAME side of the frame as the real raised arm. The caption's 'opposite side' refers to the reflected robot's own left and right, which are swapped because it faces the viewer. A reflection whose raised arm is on the other side of the frame is a rotated copy and fails P2.

## OPT-0050 · reflection · train

**Caption.** A bus drives slowly past a row of shop windows, and its reflection moves along in the glass beside it.

**Expectation (hidden).** The reflection keeps pace and disappears where the glass ends; it is mirrored and shows the same movement at the same time.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A bus moves along a street.
- S2 [core] A row of shop windows runs beside the street.
- S3 [core] The bus's reflection is visible in the windows.
- S4 [core] The reflection moves along with the bus.
- S5 [minor] The bus moves slowly.
- S6 [minor] The reflection shows the bus's shape and colour.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflection travels with the bus, in step with it, and appears only in the glass: it stops where a pane ends and shows again in the next pane.
  - fail: The reflection stays still while the bus moves; or moves in the opposite direction; or continues across the wall between windows; or the bus has no reflection in a plainly reflective window.
- P2 [major · causeless_motion]
  - expect: Nothing in the reflection moves that is not moving in reality; a stationary bus has a stationary reflection.
  - fail: The reflection moves while the bus has stopped; or shows the bus in a different pose or heading; or people in the reflection move differently from those on the street.
- P3 [major · shape_identity]
  - expect: The reflection is a mirror image of the bus: same colours and size, alongside the real bus, with any lettering reversed.
  - fail: The reflection is a different vehicle or colour; or upside down; or far larger or smaller than the bus; or its lettering reads the right way round.
- P4 [major · material_response]
  - expect: The windows are flat rigid panes: the reflection is undistorted and the shop interior is seen through it.
  - fail: The glass ripples like water; or the reflection warps as it slides; or the window frames bend.
- P5 [fatal · permanence_count]
  - expect: One bus and one reflection per pane; the bus does not pass through the windows and nothing appears or vanishes.
  - fail: A second bus appears; or the bus drives into the glass; or the reflection steps out into the street; or the bus vanishes mid-pass.
- P6 [minor · attribute_drift]
  - expect: The shop fronts, the bus livery and the street stay the same.
  - fail: The bus's livery changes; or shop signs change; or the number of windows changes.

## OPT-0097 · refraction_transparency · train

**Caption.** A drinking straw is placed into a glass of water, and it looks bent where it enters the water.

**Expectation (hidden).** The part of the straw under water appears shifted relative to the part above, with the break exactly at the waterline; the straw itself stays straight when lifted out.

**Declared violation types.** shape_identity, missing_consequence

**SA**
- S1 [core] A glass of water is present.
- S2 [core] A drinking straw is placed into it.
- S3 [core] The straw appears bent or broken at the waterline.
- S4 [minor] The glass is clear enough to see the straw below the surface.
- S5 [minor] The bend appears once the straw is in the water, not before.

**PC**
- P1 [core · missing_consequence]
  - expect: The apparent break in the straw sits exactly at the water surface: above it the straw is seen directly, below it the submerged part appears shifted or magnified through the water.
  - fail: The straw looks perfectly continuous with no offset at the waterline; or the kink sits above or below the water surface rather than at it; or the straw bends where it passes through air only.
- P2 [core · shape_identity]
  - expect: The straw itself stays straight and rigid: the bend is an appearance that stays at the waterline as the straw or water moves, and is absent out of the water.
  - fail: The straw is physically kinked or curved when lifted out; or the kink stays at a fixed point on the straw as the straw is raised or lowered; or the straw flexes like rubber.
- P3 [major · material_response]
  - expect: The water surface is level and settles; the glass is rigid and transparent; the submerged straw is seen through the water.
  - fail: The water surface stays tilted or humped; or the glass warps; or the water turns opaque and hides the straw.
- P4 [major · causeless_motion]
  - expect: The straw stays where it is placed, resting against the rim or the bottom; the glass stays put.
  - fail: The straw slides or rotates by itself; or hovers without touching glass or water; or the glass moves on its own.
- P5 [fatal · permanence_count]
  - expect: One straw, one glass; the straw does not pass through the glass wall and neither duplicates or vanishes.
  - fail: The straw passes through the glass wall; or a second straw appears; or the straw vanishes below the surface; or the glass changes shape.
- P6 [minor · attribute_drift]
  - expect: The straw's stripes and colour and the glass's shape stay the same above and below the waterline, apart from the optical shift.
  - fail: The straw changes colour underwater; or its stripe pattern changes; or the table or background shifts.

## OPT-0098 · refraction_transparency · train

**Caption.** Goldfish swim in an aquarium and are clearly visible through the glass.

**Expectation (hidden).** The fish are visible through the glass and water at all times and stay inside the tank; the glass does not hide them or let them pass through.

**Declared violation types.** missing_consequence, solidity

**SA**
- S1 [core] An aquarium filled with water is present.
- S2 [core] Goldfish are inside it.
- S3 [core] The fish are visible through the glass.
- S4 [core] The fish swim: they move through the water.
- S5 [minor] There are several goldfish, orange in colour.
- S6 [minor] The tank is transparent on the side facing the viewer.

**PC**
- P1 [core · solidity]
  - expect: The fish stay inside the water; the glass is a barrier they never cross, and tank decorations are solid to them.
  - fail: A fish passes through the glass or swims out into the room; or a fish appears outside the tank; or fish swim through decorations as if they were not there.
- P2 [core · missing_consequence]
  - expect: The glass and water are transparent: fish are seen through them wherever the tank is in view.
  - fail: The glass turns opaque and hides the fish; or the water blocks the view of fish at the back while the front is clear.
- P3 [major · gravity_direction]
  - expect: The fish stay submerged; the water surface stays level at the top of the tank.
  - fail: A fish hovers above the water surface; or the water surface tilts and holds; or the water level changes with no cause.
- P4 [major · trajectory_momentum]
  - expect: The fish move as fish: smooth swimming with tail motion and turning without jumps in position.
  - fail: A fish slides with a rigid body and no tail motion; or moves backwards at speed tail-first; or spins in place like a propeller.
- P5 [fatal · permanence_count]
  - expect: The number of fish is constant; each keeps its shape and identity with no merging or splitting.
  - fail: Fish appear or vanish; or two fish merge; or a fish splits; or a fish changes into something else; or a fish jumps from one place to another between frames.
- P6 [minor · attribute_drift]
  - expect: Fish colours, decorations and the tank frame stay the same; refraction may shift things slightly but the layout is constant.
  - fail: A fish changes colour; or decorations move on their own; or the tank frame changes shape.

**Note.** Fish are self-driven: where they go, when they start and stop is not judged. This caption has no triggered event; the physics is transparency and containment.

## OPT-0142 · illumination · train

**Caption.** A flashlight is swept across a dark wall, and the bright spot slides along the wall.

**Expectation (hidden).** The spot moves in the direction the flashlight turns and stays lit only where the beam points; it does not remain on the wall after the beam moves.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A lit flashlight is present.
- S2 [core] A dark wall is present.
- S3 [core] The beam's bright spot is on the wall and slides along it.
- S4 [minor] The flashlight turns or moves during the sweep.
- S5 [minor] The spot is a bright patch with a soft edge, brighter at its centre.

**PC**
- P1 [core · missing_consequence]
  - expect: The spot follows the flashlight: it moves in the direction the flashlight turns, at the same time, and sits where the beam points.
  - fail: The flashlight turns and the spot stays put; or the spot moves opposite to the flashlight's turn; or the spot moves while the flashlight is held still; or the spot lags behind and then jumps.
- P2 [major · causeless_motion]
  - expect: Light on the wall exists only where the beam is: no glow lingers behind the spot and none appears ahead of it.
  - fail: A lit trail remains on the wall behind the spot; or a patch lights up before the beam arrives; or a second spot appears with only one flashlight.
- P3 [major · missing_consequence] (if: The beam is visible in the air (dust, haze or smoke).)
  - expect: A beam visible in the air runs straight from the flashlight's head to the spot.
  - fail: The visible beam points elsewhere than the spot; or the beam is bent; or the beam is visible but the flashlight's head is dark.
- P4 [major · shape_identity]
  - expect: The spot is one patch that stretches into an oval as the beam strikes the wall more obliquely and rounds up when it strikes squarely.
  - fail: The spot splits into several pieces; or takes a sharp geometric shape like a square; or keeps a fixed shape while the beam angle plainly changes.
- P5 [fatal · permanence_count]
  - expect: One flashlight and one spot; the flashlight keeps its shape and does not pass through the wall.
  - fail: The flashlight duplicates or vanishes; or passes through the wall; or the spot becomes a solid object; or the wall changes shape.
- P6 [minor · attribute_drift]
  - expect: The wall's colour and texture stay the same; the parts of the room outside the beam stay as dark as they were.
  - fail: The wall's texture changes between frames; or the room's overall brightness changes with the flashlight steady; or objects on the wall move.

## OPT-0143 · illumination · train

**Caption.** A single candle burns in a dark room, and it lights the objects nearest to it while the far wall stays dark.

**Expectation (hidden).** The objects closest to the flame are brightest, brightness falls off with distance, and the light flickers with the flame.

**Declared violation types.** missing_consequence, attribute_drift

**SA**
- S1 [core] A single lit candle is present.
- S2 [core] The room is dark and the candle is the only light.
- S3 [core] Objects near the candle are lit by it.
- S4 [core] The far wall stays dark.
- S5 [minor] The light flickers gently with the flame.
- S6 [minor] There are objects near the candle for it to light.

**PC**
- P1 [core · missing_consequence]
  - expect: Light comes from the flame: surfaces facing the candle are lit, farther ones are dimmer, and the far wall stays dark.
  - fail: The far wall is as bright as the nearby objects; or the brightest surfaces are far from the candle; or nearby objects are dark while the room is lit; or the light comes from somewhere other than the flame.
- P2 [major · causeless_motion]
  - expect: Brightness changes only with the flame: a steady flame gives steady light and a flicker gives a flicker.
  - fail: The room brightens or darkens while the flame is unchanged; or the light pulses with no flicker; or the lit area moves while the candle stays.
- P3 [major · missing_consequence] (if: Shadows of the nearby objects are visible.)
  - expect: Objects near the candle cast shadows pointing away from it.
  - fail: Shadows point toward the candle; or shadows fall in different directions from a single flame; or an object between the candle and the wall casts no shadow.
- P4 [major · gravity_direction]
  - expect: The flame points upward from the wick.
  - fail: The flame points down or sideways in still air; or floats above the wick; or is detached from the candle.
- P5 [fatal · permanence_count]
  - expect: One candle and one flame; objects in the room keep their number and do not pass through each other.
  - fail: A second flame or candle appears; or objects appear or vanish as the light flickers; or the candle passes through the table.
- P6 [minor · attribute_drift]
  - expect: The objects keep their colours and positions; only their brightness varies with the flame.
  - fail: An object changes colour rather than brightness; or an object shifts position; or the wall's texture changes.

## OPT-0178 · color_mixing · train

**Caption.** Yellow and blue paint squeezed side by side on a palette are stirred together with a brush, and the mixture turns green.

**Expectation (hidden).** Green appears where the two colours meet and spreads as the stirring continues until no pure yellow or blue is left; the mixture does not separate back.

**Declared violation types.** attribute_drift, process_direction

**SA**
- S1 [core] Yellow paint and blue paint sit side by side on a palette.
- S2 [core] A brush stirs them together.
- S3 [core] The mixture becomes green.
- S4 [minor] Green appears where the two colours meet, streaky at first.
- S5 [minor] The colours are separate first, then stirred, then green.

**PC**
- P1 [core · process_direction]
  - expect: Green appears only where yellow and blue are stirred together and spreads as stirring continues; mixed areas stay mixed.
  - fail: Green appears before the brush touches the paints; or a mixed area separates back into yellow and blue; or the green fades and returns; or green shows up in a spot the brush never reached.
- P2 [core · attribute_drift]
  - expect: The mixture is green, between the two parents; unstirred yellow stays yellow and unstirred blue stays blue.
  - fail: The mixture comes out red, purple, brown or white; or the unstirred yellow turns another colour; or the parents swap colours.
- P3 [major · material_response]
  - expect: The paints behave as thick liquids: they streak and smear under the brush, mounds flatten, and the brush leaves marks.
  - fail: The paint stays as rigid blobs the brush passes through unchanged; or it flows like water and floods the palette; or it bounces like rubber.
- P4 [major · causeless_motion]
  - expect: Paint moves only where the brush pushes it.
  - fail: Paint slides or swirls by itself; or the blobs move toward each other before the brush arrives; or the brush marks move after the brush has gone.
- P5 [fatal · permanence_count]
  - expect: Paint is conserved: the amount does not grow or vanish, and the brush and palette keep their shape.
  - fail: Paint appears from nowhere or the palette empties; or a second brush appears; or the brush passes through the palette; or the palette changes shape.
- P6 [minor · attribute_drift]
  - expect: The palette, the brush handle and the background stay the same.
  - fail: The palette changes colour or shape; or the brush handle changes; or background objects shift.

## OPT-0179 · color_mixing · train

**Caption.** A drop of red food colouring is added to a glass of white icing and stirred, and the icing turns pink.

**Expectation (hidden).** Streaks of red spread through the white and blend to an even pink; the colour does not come out again.

**Declared violation types.** attribute_drift, process_direction

**SA**
- S1 [core] A container of white icing is present.
- S2 [core] A drop of red food colouring is added to it.
- S3 [core] The icing is stirred.
- S4 [core] The icing turns pink.
- S5 [minor] Red streaks appear first and blend toward an even pink.
- S6 [minor] The order is drop, stir, pink.

**PC**
- P1 [core · process_direction]
  - expect: Colour spreads from the drop through the icing as it is stirred; coloured areas stay coloured, and the pink deepens or evens out but never returns to white.
  - fail: The icing turns white again where it was pink; or the red gathers back into a drop; or the pink appears before the drop lands; or the colour flickers.
- P2 [core · attribute_drift]
  - expect: The result is pink, a lighter tint of the red, with red streaks where unmixed; the white stays white until the colour reaches it.
  - fail: The icing turns a colour other than pink or red; or the red streaks turn white instead of blending; or the icing becomes darker red than the drop itself.
- P3 [major · material_response]
  - expect: The icing behaves as a thick paste: the spoon leaves furrows, streaks stay where drawn until stirred, and the drop sits on it rather than dispersing like ink in water.
  - fail: The icing flows like water and the colour disperses in swirls on its own; or the icing is rigid and the spoon passes through it without marking; or it bounces like rubber.
- P4 [major · causeless_motion]
  - expect: The icing moves only where stirred; the colouring does not spread faster than stirring carries it.
  - fail: Colour spreads through unstirred icing on its own; or the icing swirls with no spoon; or the bowl turns by itself.
- P5 [fatal · permanence_count]
  - expect: One container and one spoon; the amount of icing stays the same and nothing passes through the container.
  - fail: The container fills or empties on its own; or a second spoon appears; or the spoon passes through the container; or the container changes shape.
- P6 [minor · attribute_drift]
  - expect: The container, the spoon and the table keep their appearance.
  - fail: The container changes colour; or the spoon changes; or the table pattern shifts.

# Electricity

## ELEC-0001 · switch_light · train

**Caption.** The wall switch in a dark hallway is flipped up, and the ceiling light comes on.

**Expectation (hidden).** The light comes on at the instant the switch moves, not before or after, and stays on; nothing else in the room changes.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A wall switch in a hallway; the hallway is dark at the start.
- S2 [core] The switch is flipped: it moves to its other position.
- S3 [core] The ceiling light comes on.
- S4 [minor] The light is a ceiling fixture.
- S5 [minor] The order is dark, flip, lit.

**PC**
- P1 [core · missing_consequence]
  - expect: The light comes on at the moment the switch moves, and only then.
  - fail: The switch flips and the light stays off; or the light comes on before the switch is touched; or it comes on well after the flip with nothing else happening; or it comes on while the switch is untouched.
- P2 [core · process_direction]
  - expect: Once on, the light stays on steadily and the hallway stays lit for the rest of the clip.
  - fail: The light goes off again by itself; or flickers on and off after the flip; or dims back to dark; or the switch moves back by itself.
- P3 [major · missing_consequence]
  - expect: When the light is on, the hallway is lit from the ceiling fixture: walls and floor below it are brighter than before, with shadows pointing away from it.
  - fail: The fixture glows but the hallway stays dark; or the hallway brightens while the fixture stays dark; or the light comes from a place other than the fixture.
- P4 [major · causeless_motion]
  - expect: Nothing else in the hallway moves or changes when the switch is flipped.
  - fail: Doors open, objects move or the hallway layout changes at the flip; or the switch plate moves along the wall.
- P5 [fatal · permanence_count]
  - expect: One switch and one ceiling light; the switch stays on the wall and the fixture on the ceiling.
  - fail: A second switch or light appears; or the fixture vanishes or moves across the ceiling; or the switch sinks into the wall; or the hand passes through the switch.
- P6 [minor · attribute_drift]
  - expect: The wall colour, fixture design and hallway contents stay the same apart from the lighting.
  - fail: The wall changes colour rather than brightness; or the fixture changes shape; or pictures on the wall change.

## ELEC-0002 · switch_light · train

**Caption.** The wall switch in a lit hallway is flipped down, and the ceiling light goes off.

**Expectation (hidden).** The light goes out the instant the switch moves and the room falls dark; the light does not fade slowly or flicker back on.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A wall switch in a hallway; the hallway is lit at the start.
- S2 [core] The switch is flipped.
- S3 [core] The ceiling light goes off.
- S4 [minor] The hallway goes dark.
- S5 [minor] The order is lit, flip, off.

**PC**
- P1 [core · missing_consequence]
  - expect: The light goes off at the moment the switch moves, and only then.
  - fail: The switch moves and the light stays on; or the light goes off before the switch is touched; or it goes off long after with nothing else happening.
- P2 [core · process_direction]
  - expect: Once off, the light stays off for the rest of the clip; the hallway stays as dark as the loss of that light makes it.
  - fail: The light comes back on by itself; or flickers between on and off; or the hallway brightens again with no other source.
- P3 [major · missing_consequence]
  - expect: The illumination disappears with the fixture: the walls and floor under it go dimmer and its shadows vanish.
  - fail: The fixture goes dark while the hallway stays as bright; or the hallway darkens while the fixture still glows; or light remains pooled on the floor under a dark fixture.
- P4 [major · causeless_motion]
  - expect: Nothing else changes at the flip.
  - fail: Objects move or doors open when the switch is flipped; or the switch moves back by itself; or the fixture swings.
- P5 [fatal · permanence_count]
  - expect: One switch and one light, both staying in place; the hand does not pass through the wall.
  - fail: A second switch appears; or the fixture vanishes rather than going dark; or the hand passes into the wall; or doors appear or vanish in the dark.
- P6 [minor · attribute_drift]
  - expect: The hallway keeps its colours and contents apart from brightness.
  - fail: Walls change colour; or pictures change; or the fixture changes shape.

## ELEC-0043 · plug_power · train

**Caption.** The plug of a lit table lamp is pulled out of the wall socket, and the lamp goes out.

**Expectation (hidden).** The lamp goes dark the instant the plug leaves the socket and stays dark; the switch on the lamp is still on.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A table lamp is lit.
- S2 [core] Its plug is in a wall socket.
- S3 [core] The plug is pulled out of the socket.
- S4 [core] The lamp goes out.
- S5 [minor] A cord connects the lamp to the plug.
- S6 [minor] The order is lit, plug pulled, out.

**PC**
- P1 [core · missing_consequence]
  - expect: The lamp goes dark at the moment the plug leaves the socket, and only then.
  - fail: The plug is out and the lamp still shines; or the lamp goes out before the plug moves; or the lamp goes out with the plug still seated.
- P2 [core · process_direction]
  - expect: Once unplugged the lamp stays dark; it does not relight while the plug is out.
  - fail: The lamp comes back on while the plug is out; or flickers between lit and dark; or keeps glowing for the rest of the clip after being unplugged.
- P3 [major · missing_consequence]
  - expect: The light the lamp cast disappears with it: the shade darkens and the surfaces it lit go dimmer.
  - fail: The bulb goes dark while its light on the table and wall stays; or the room brightens as the lamp goes out; or the shade keeps glowing with the bulb dark.
- P4 [major · material_response]
  - expect: The cord follows the plug: it slackens and drops when pulled free and stays attached at both ends.
  - fail: The cord stretches like elastic; or stands rigid in the air after the plug is out; or floats.
- P5 [fatal · permanence_count]
  - expect: One lamp, one cord, one plug and one socket; the plug leaves the socket whole and nothing passes through the wall or table.
  - fail: The plug vanishes or a second plug appears; or the plug passes through the wall; or the socket moves; or the cord splits or detaches; or the lamp changes shape.
- P6 [minor · attribute_drift]
  - expect: The lamp's shade colour and the room stay the same apart from the light.
  - fail: The shade changes colour rather than brightness; or the wall changes; or the socket's design changes.

## ELEC-0044 · plug_power · train

**Caption.** A desk fan with its switch already on is plugged into a socket, and the blades start turning.

**Expectation (hidden).** The blades begin to spin when the plug goes in and speed up to a steady rate; they do not spin before the plug is inserted.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A desk fan is present.
- S2 [core] Its plug is inserted into a socket.
- S3 [core] The blades start turning after the plug goes in.
- S4 [minor] The fan is still before it is plugged in.
- S5 [minor] Plugging in comes first, spinning after.

**PC**
- P1 [core · missing_consequence]
  - expect: The blades begin to turn when the plug seats in the socket, and only then.
  - fail: The plug is in and the blades stay still; or the blades start before the plug reaches the socket; or they start with the plug lying loose.
- P2 [core · causeless_motion]
  - expect: Before the plug is in the blades are still; after, they speed up and settle to a steady spin; they do not stop or reverse on their own.
  - fail: The blades spin while unplugged; or turn slowly by themselves before plugging; or stop and restart with the plug in; or reverse direction.
- P3 [major · trajectory_momentum]
  - expect: The blades spin about the hub as one piece with a smooth speed-up; the head may oscillate if built to.
  - fail: The blades wobble off the hub; or the spin jumps abruptly between fast and still; or blades move independently of each other.
- P4 [major · missing_consequence] (if: Light items such as paper, ribbons or hair are in front of the fan.)
  - expect: Light items in front of the fan flutter in the airflow once the blades spin and are still before.
  - fail: Ribbons or paper flutter before the blades turn; or nothing in front moves while the fan blows; or the flutter blows toward the fan.
- P5 [fatal · permanence_count]
  - expect: One fan with a fixed number of blades, one plug and cord; the plug enters the socket rather than passing into the wall.
  - fail: Blades appear or vanish; or the fan duplicates; or the plug passes through the wall beside the socket; or the cord detaches or splits.
- P6 [minor · attribute_drift]
  - expect: The fan's colour, the desk and the socket stay the same.
  - fail: The fan changes colour; or the cage changes pattern; or the socket moves along the wall.

## ELEC-0081 · lightning · train

**Caption.** A storm rolls over a farm at night, and a bolt of lightning flashes from the clouds to the ground, lighting up the fields for an instant.

**Expectation (hidden).** The bolt is a jagged bright line from cloud to ground that appears and vanishes within a fraction of a second; the fields are lit only during the flash and are dark again afterwards.

**Declared violation types.** process_direction, gravity_direction, permanence_count

**SA**
- S1 [core] A farm landscape at night under storm clouds.
- S2 [core] A lightning bolt spans from the clouds to the ground.
- S3 [core] The fields are lit briefly by the flash.
- S4 [minor] The bolt is jagged or branched.
- S5 [minor] The fields go dark again afterwards.

**PC**
- P1 [core · process_direction]
  - expect: The bolt and the flash are brief: they appear, may flicker, and are gone; the landscape is lit only during the flash and returns to dark.
  - fail: The bolt stands as a steady lit line for the whole clip; or the fields stay lit after the bolt has gone; or the sky brightens without a bolt and stays bright.
- P2 [core · missing_consequence]
  - expect: The flash lights the scene: fields, farm buildings and cloud undersides brighten during the bolt, lit from the bolt's direction.
  - fail: The bolt is visible but the ground and clouds stay as dark as before; or the lit area is far from the bolt; or the fields are lit while no bolt is present.
- P3 [major · shape_identity]
  - expect: The bolt is a jagged, branching bright line with a main channel.
  - fail: The bolt is a perfectly straight beam; or a smooth wave; or a solid glowing tube that persists; or a shape with no connection between cloud and ground while the ground lights up.
- P4 [major · gravity_direction] (if: Rain or wind-blown items are visible.)
  - expect: Rain falls downward and wind-blown items move with the storm.
  - fail: Rain rises or hangs still; or leaves blow upward steadily; or rain falls sideways while the trees stand still.
- P5 [fatal · permanence_count]
  - expect: The farm's buildings, trees and fences are the same before and after the flash; the flash reveals what was there, it does not create or remove anything.
  - fail: Buildings or trees appear or vanish between dark and lit frames; or the landscape changes layout after the flash; or a bolt passes through a building leaving it lit like a lamp.
- P6 [minor · attribute_drift]
  - expect: The scene's colours are consistent: the flash whitens or blues the scene briefly and it returns to the same night colours.
  - fail: The sky changes to daylight after the flash; or the fields change colour permanently; or clouds change shape abruptly between frames.

**Note.** The caption's violation_types include gravity_direction; nothing about a bolt itself has a gravity direction, so it is covered only by the rain item P4, which is gated. Consider replacing gravity_direction with shape_identity on the data record.

## ELEC-0082 · lightning · train

**Caption.** Lightning flashes inside a bank of dark clouds over a city, and the clouds glow for a moment and then go dark.

**Expectation (hidden).** The glow is brief and comes from within the clouds; the sky returns to dark right after; the city lights are unaffected.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A city skyline under a dark sky.
- S2 [core] A bank of dark clouds above it.
- S3 [core] A flash lights the clouds from within.
- S4 [core] The clouds go dark again.
- S5 [minor] The glow is inside or among the clouds, not a bolt to the ground.
- S6 [minor] The city lights stay as they were.

**PC**
- P1 [core · process_direction]
  - expect: The glow is brief: the clouds light up and then return to dark; flashes may repeat but each ends.
  - fail: The clouds stay lit for the rest of the clip; or the glow brightens steadily without ending; or the sky turns to daylight.
- P2 [major · missing_consequence]
  - expect: The glow comes from within or behind the clouds: their undersides and edges brighten with their texture revealed.
  - fail: The flash lights the city streets while the clouds stay dark; or the glow is a flat wash over the whole frame with no cloud structure.
- P3 [major · permanence_count]
  - expect: The cloud bank and skyline are unchanged by the flash: the same clouds and the same buildings, revealed and then hidden.
  - fail: Buildings appear or vanish between dark and lit frames; or the cloud shapes differ between the lit frame and the dark ones; or the skyline moves.
- P4 [major · causeless_motion]
  - expect: City lights stay steady through the flash; clouds drift only slowly.
  - fail: City lights blink out at the flash or all change at once; or the clouds jump or swirl at the flash; or the buildings sway.
- P5 [fatal · shape_identity]
  - expect: The skyline and clouds keep their shape; nothing passes through a building.
  - fail: A building changes shape; or the clouds turn into solid objects; or lightning passes through a building and lights its interior like a lamp; or the city duplicates.
- P6 [minor · attribute_drift]
  - expect: The colour of the night sky and the city lights is consistent before and after.
  - fail: The sky changes colour permanently after the flash; or windows change lit pattern all at once; or the clouds change colour when not lit.

## ELEC-0107 · spark · train

**Caption.** A robotic welding arm touches down on a steel car body on an assembly line, and a shower of bright sparks bursts from the joint and falls to the floor.

**Expectation (hidden).** Sparks appear only while the arm's tip touches the metal, fly outward and downward, and go dark within a short distance; they do not rise or linger on the floor as lights.

**Declared violation types.** gravity_direction, permanence_count, process_direction

**SA**
- S1 [core] A robotic welding arm is present.
- S2 [core] A steel car body sits on an assembly line.
- S3 [core] The arm's tip touches down on the body.
- S4 [core] A shower of sparks bursts from the contact point.
- S5 [minor] The sparks fall toward the floor.
- S6 [minor] Contact comes first and the sparks follow.

**PC**
- P1 [core · process_direction]
  - expect: Sparks appear only while the tip is in contact and issue from the contact point; when the tip lifts they stop.
  - fail: Sparks appear before the tip touches; or continue streaming after the tip has lifted; or come from a point other than the joint; or sparks flow back into the joint.
- P2 [major · gravity_direction]
  - expect: Sparks fly out from the joint along arcs that bend downward and go dark before or when they reach the floor.
  - fail: Sparks rise steadily and collect above the joint; or hang in the air; or lie on the floor still glowing like lamps for the rest of the clip; or curve upward after leaving the joint.
- P3 [major · permanence_count]
  - expect: Sparks are short-lived: each fades within a short flight, and the number in the air rises with the burst and falls when it ends.
  - fail: Sparks persist as permanent bright dots; or a pile of glowing sparks builds on the floor; or sparks appear in mid-air far from the joint.
- P4 [major · causeless_motion]
  - expect: The car body sits still on the line, or moves steadily with it; only the arm moves.
  - fail: The body jumps or shifts at the touch; or the line surges; or the body slides away from the arm.
- P5 [fatal · solidity]
  - expect: The arm's tip touches the surface and stays outside the metal; arm and body keep their shape and number.
  - fail: The tip sinks into or passes through the car body; or a second arm appears; or the body changes shape; or a car part vanishes.
- P6 [minor · attribute_drift]
  - expect: The car body's colour, the arm's markings and the factory background stay the same.
  - fail: The body panel changes colour; or the arm changes colour; or the background machines rearrange.

## ELEC-0108 · spark · train

**Caption.** A spinning angle grinder is pressed against a metal pipe clamped in a vise, and a fan of orange sparks streams off the wheel.

**Expectation (hidden).** The sparks leave the wheel in the direction it is spinning, curve downward under gravity, and fade; they stop the instant the wheel leaves the metal.

**Declared violation types.** trajectory_momentum, gravity_direction, permanence_count

**SA**
- S1 [core] An angle grinder with a spinning wheel.
- S2 [core] A metal pipe is clamped in a vise.
- S3 [core] The wheel is pressed against the pipe.
- S4 [core] A fan of orange sparks streams off the wheel.
- S5 [minor] The sparks are orange to yellow.
- S6 [minor] Contact comes first and the sparks follow.

**PC**
- P1 [core · trajectory_momentum]
  - expect: Sparks leave the contact point along the direction the wheel's rim is moving, in one fan, and curve downward as they fly.
  - fail: Sparks radiate equally in all directions from the contact; or the fan points opposite to the rim's motion; or the fan direction jumps around while the grinder is steady.
- P2 [major · gravity_direction]
  - expect: Sparks that fly far arc downward and go out; they do not rise or hover.
  - fail: Sparks rise steadily and gather above the grinder; or hang in the air; or lie on the bench glowing like lamps.
- P3 [major · process_direction]
  - expect: Sparks appear only while the wheel is on the metal and stop when it lifts.
  - fail: Sparks stream while the wheel is off the pipe; or continue after the grinder is withdrawn; or sparks flow back to the wheel.
- P4 [major · permanence_count]
  - expect: Sparks are transient: each fades in flight and none accumulate.
  - fail: Sparks persist as fixed dots; or a glowing pile builds on the floor; or sparks appear from a point away from the contact.
- P5 [fatal · solidity]
  - expect: The wheel touches the pipe's surface and grinds it; it does not pass through the pipe, and grinder, pipe and vise keep their shape and number.
  - fail: The wheel sinks through the pipe; or the pipe passes through the vise; or the grinder duplicates; or the pipe changes shape without being cut.
- P6 [minor · attribute_drift]
  - expect: The grinder's colour, the pipe and the vise stay the same apart from a grinding mark.
  - fail: The grinder changes colour; or the pipe changes diameter; or the vise moves along the bench.

## ELEC-0140 · magnet · train

**Caption.** A small magnet is pressed against a refrigerator door and released, and it stays stuck on the door.

**Expectation (hidden).** The magnet holds on the vertical door with nothing else supporting it and does not slide down or fall; a photo tucked under it stays too.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] A refrigerator door is present.
- S2 [core] A small magnet is pressed against it.
- S3 [core] The magnet is released: the hand or tool withdraws.
- S4 [core] The magnet stays on the door.
- S5 [minor] The magnet is small, fridge-magnet sized.
- S6 [minor] The order is press, release, stays.

**PC**
- P1 [core · missing_consequence]
  - expect: After release the magnet holds where it was placed on the vertical door, with nothing supporting it.
  - fail: The magnet drops when the hand lets go; or slides slowly down the door; or floats away from the door; or hangs a gap away from the surface without touching.
- P2 [major · causeless_motion]
  - expect: Once released the magnet stays put: it does not slide, rotate or creep.
  - fail: The magnet moves across the door after release with nothing touching it; or rotates; or jumps to a new spot.
- P3 [major · gravity_direction] (if: A photo, note or other item is tucked under the magnet.)
  - expect: An item tucked under the magnet stays too, held against the door.
  - fail: The item falls while the magnet stays; or the item floats up; or the item is held while the magnet is off the door.
- P4 [major · material_response]
  - expect: The magnet stays a rigid solid and the door does not dent.
  - fail: The magnet squashes like putty against the door; or the door surface deforms around it; or the magnet bounces off and then sticks.
- P5 [fatal · permanence_count]
  - expect: One magnet on the outside of the door; the door and hand keep their shape.
  - fail: The magnet sinks into the door; or a second magnet appears; or the magnet vanishes; or fingers pass through the magnet.
- P6 [minor · attribute_drift]
  - expect: The magnet's colour and design and the other items on the door stay the same.
  - fail: The magnet changes colour or shape; or other magnets or notes on the door move or vanish; or the door changes colour.

## ELEC-0177 · static · train

**Caption.** A balloon is rubbed on a wool sweater and pressed against a wall, and it stays stuck to the wall when released.

**Expectation (hidden).** The balloon holds on the vertical wall with nothing supporting it for a while, then may drift down slowly; it does not fall at once.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] A balloon is present.
- S2 [core] It is rubbed against a wool sweater.
- S3 [core] It is pressed against a wall.
- S4 [core] It stays on the wall after being released.
- S5 [minor] The sweater is woolly or knitted.
- S6 [minor] The order is rub, press, release, stays.

**PC**
- P1 [core · missing_consequence]
  - expect: After release the balloon stays against the wall unsupported; if it lets go it slides or peels down, it does not launch off.
  - fail: The balloon falls the instant it is released; or drifts away from the wall or up to the ceiling with nothing lifting it; or hangs a gap away from the wall.
- P2 [major · gravity_direction]
  - expect: If the balloon comes off it moves downward, sliding along or falling from the wall; the sweater and hands obey gravity.
  - fail: The balloon comes off and moves upward or sideways along the wall; or hangs in mid-air away from the wall; or the sweater floats.
- P3 [major · material_response]
  - expect: The balloon is a light elastic shell: it dents slightly where pressed and springs back.
  - fail: The balloon keeps a deep dent after the hand leaves; or stretches out like taffy; or the wall surface dents under it.
- P4 [major · causeless_motion]
  - expect: The balloon moves only when handled: it is still on the wall after release, small drifts aside, and does not slide around or spin.
  - fail: The balloon travels across the wall by itself; or spins in place while stuck; or jumps to a different spot on the wall.
- P5 [fatal · permanence_count]
  - expect: One balloon; it passes through nothing and does not duplicate or vanish; the hand keeps its fingers.
  - fail: The balloon passes into the wall; or a second balloon appears; or it vanishes or turns into another object; or fingers pass through the balloon.
- P6 [minor · attribute_drift]
  - expect: The balloon's colour and the wall stay the same; the sweater keeps its colour and pattern.
  - fail: The balloon changes colour or size, slight dents aside; or the wall changes; or the sweater changes pattern.

**Note.** An air-filled balloon is implied: a helium balloon would float without being rubbed and pressed, so a balloon that rises away from the wall fails P1.

# Acoustics

## ACOU-0001 · struck_vibration · train

**Caption.** Grains of rice lie on the head of a snare drum; the drum is struck once with a stick and the grains jump.

**Expectation (hidden).** The grains are still until the strike, leap up together at the strike and settle back within a second or two as the head goes quiet; they do not move before the stick lands.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A snare drum with grains of rice lying on its head.
- S2 [core] A stick strikes the drum once.
- S3 [core] The grains jump.
- S4 [minor] The strike is a single hit.
- S5 [minor] The strike comes first and the jump follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The grains lie still until the stick hits, jump at the strike, then settle; they do not move before the strike.
  - fail: Grains bounce or shift before the stick reaches the head; or jump with the stick nowhere near; or stay still as the stick hits.
- P2 [core · process_direction]
  - expect: The hop is largest right after the strike and dies down: later bounces are smaller until the grains lie still.
  - fail: The grains keep bouncing at the same height for the whole clip; or bounce higher and higher after the strike; or start moving again after settling with no second strike.
- P3 [major · gravity_direction]
  - expect: Grains that jump come back down onto the head or fall off its edge.
  - fail: Grains hang in the air; or float away upward; or leave the head and come back up onto it.
- P4 [major · material_response]
  - expect: The head flexes as a skin at the strike, the stick rebounds, and the grains stay separate grains.
  - fail: The stick sinks into the head and stays; or the head shatters like glass; or the grains merge into a lump or flow like liquid.
- P5 [fatal · permanence_count]
  - expect: The grains keep their number, allowing for some falling off; the drum and stick keep their shape and the stick does not pass through the head.
  - fail: Grains appear from nowhere in the air; or the drum changes shape; or the stick passes through the head; or the grains vanish all at once.
- P6 [minor · attribute_drift]
  - expect: The drum's shell, the head's colour and the stick stay the same.
  - fail: The drum changes colour; or the head changes texture; or the stick changes length.

## ACOU-0002 · struck_vibration · train

**Caption.** The low string of an acoustic guitar is plucked, and the string blurs into a wide band before slowly sharpening to a line again.

**Expectation (hidden).** Only the plucked string blurs, the blur is widest right after the pluck and narrows steadily; the other strings stay sharp.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] An acoustic guitar is present.
- S2 [core] The low, thickest string is plucked.
- S3 [core] The plucked string blurs: it vibrates visibly.
- S4 [core] The blur narrows back to a sharp line.
- S5 [minor] Only that string is plucked; the others are not.
- S6 [minor] The order is pluck, wide blur, narrowing.

**PC**
- P1 [core · causeless_motion]
  - expect: The string is a sharp line until plucked, blurs at the pluck, and only then; the other strings stay sharp.
  - fail: The string blurs before it is touched; or a different string blurs; or all strings blur together; or the string blurs with no pluck.
- P2 [core · process_direction]
  - expect: The blur is widest right after the pluck and only narrows; it does not widen again without another pluck.
  - fail: The blur widens again after narrowing; or stays the same width for the whole clip; or the string goes sharp and then blurs again with no second pluck.
- P3 [major · material_response]
  - expect: The string stays anchored at the nut and the bridge: the blur is a band between the two fixed ends, widest near the middle.
  - fail: The string's ends move along the neck; or the blur is widest at the bridge; or the string sags or swings like a slack rope.
- P4 [major · causeless_motion]
  - expect: The guitar body, neck and other strings stay still; only the plucked string vibrates.
  - fail: The neck bends with the pluck; or the guitar body wobbles; or the other strings swing.
- P5 [fatal · permanence_count]
  - expect: The guitar's set of strings stays the same count; the plucked string stays one string and does not pass through the fretboard.
  - fail: Strings appear or vanish; or the string splits into two; or the string passes through the frets or body; or the guitar changes shape.
- P6 [minor · attribute_drift]
  - expect: The guitar's finish, the fret markers and the strings' spacing stay the same.
  - fail: The guitar changes colour; or frets move; or the strings change spacing.

## ACOU-0003 · struck_vibration · train

**Caption.** A gong is struck once with a padded mallet, and a ping-pong ball hanging on a thread against its face is knocked away and swings.

**Expectation (hidden).** The ball rests against the gong until the strike, is thrown outward the instant the gong sounds and swings back and forth, tapping the gong again as it returns while it rings; the ball does not move before the strike.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A gong is present.
- S2 [core] A ping-pong ball hangs on a thread, touching the gong's face.
- S3 [core] A mallet strikes the gong once.
- S4 [core] The ball is knocked away and swings.
- S5 [minor] The ball swings back toward the gong.
- S6 [minor] The strike comes first and the ball moves after it.

**PC**
- P1 [core · causeless_motion]
  - expect: The ball rests against the gong until the strike, is thrown outward at the strike, then swings on its thread.
  - fail: The ball moves before the mallet lands; or stays against the gong through the strike; or jumps away with the mallet nowhere near.
- P2 [core · process_direction]
  - expect: The swing decays: each return is smaller; the ball may tap the gong again as it returns and be knocked off again while the gong rings, but it does not gain height.
  - fail: The ball swings higher and higher; or keeps the same swing for the whole clip; or stops dead in mid-swing; or returns and sticks to the gong.
- P3 [major · material_response]
  - expect: The thread stays taut as the ball swings, hanging from its fixed point, and the ball moves on an arc.
  - fail: The thread stretches like elastic; or the ball swings in a straight horizontal line rather than an arc; or the thread goes slack while the ball is plainly at the end of it.
- P4 [major · trajectory_momentum]
  - expect: The ball swings as a pendulum: outward from the gong, back down through the bottom of its arc, up on the other side.
  - fail: The ball floats away and stays up; or drops straight down as if the thread were cut while it remains attached; or swings sideways along the gong's face.
- P5 [fatal · permanence_count]
  - expect: One gong, one ball and one thread; the ball stays attached and nothing passes through anything.
  - fail: The ball detaches and vanishes; or a second ball appears; or the mallet passes through the gong; or the gong changes shape.
- P6 [minor · attribute_drift]
  - expect: The gong's colour and the ball's appearance stay the same.
  - fail: The gong changes colour; or the ball changes colour or size; or the stand moves.

## ACOU-0004 · struck_vibration · train

**Caption.** A steel ruler is held flat on a desk with part sticking over the edge; the free end is flicked and it waggles up and down before coming to rest.

**Expectation (hidden).** The free end vibrates fast right after the flick with the tip blurring, the swings get smaller, and it stops within seconds; the part held on the desk stays still.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A steel ruler lies on a desk with part sticking out over the edge.
- S2 [core] The ruler is held down on the desk.
- S3 [core] The free end is flicked.
- S4 [core] The free end waggles up and down and comes to rest.
- S5 [minor] The held part stays still.
- S6 [minor] The flick comes first and the waggle follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The ruler is still until the flick, waggles from the flick, and does not start again by itself.
  - fail: The end moves before the flick; or waggles with no flick; or starts again after resting.
- P2 [core · process_direction]
  - expect: The waggle shrinks: the tip's excursions get smaller until it is still.
  - fail: The swings grow; or stay constant for the whole clip; or the tip stops dead at the top of a swing.
- P3 [major · material_response]
  - expect: The ruler bends elastically at the desk edge: the overhang flexes and returns straight, and the held part stays flat.
  - fail: The ruler kinks and stays bent; or bends like rubber into a large curve; or the held part lifts and waggles too.
- P4 [major · trajectory_momentum]
  - expect: The tip moves up and down about the straight position.
  - fail: The tip swings side to side; or rotates; or the ruler slides off the desk.
- P5 [fatal · permanence_count]
  - expect: One ruler; it passes through nothing, and the hand and desk keep their shape.
  - fail: The ruler duplicates; or passes through the desk; or vanishes; or the fingers pass through the ruler.
- P6 [minor · attribute_drift]
  - expect: The ruler's markings and the desk stay the same.
  - fail: The markings change; or the ruler changes length; or desk items move.

## ACOU-0027 · sound_driven_vibration · train

**Caption.** A glass of water sits on top of a large subwoofer, and when the music starts the water's surface breaks into fine ripples.

**Expectation (hidden).** The ripples appear only when the music plays, pulse with the bass, and the surface goes flat when the music stops; the glass does not slide off.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A glass of water is present.
- S2 [core] It sits on top of a large speaker or subwoofer.
- S3 [core] The water's surface ripples.
- S4 [minor] The surface is flat first and breaks into ripples at a moment, when the music starts.
- S5 [minor] The ripples are fine and small, not a big slosh.

**PC**
- P1 [core · missing_consequence]
  - expect: The rippling is driven by the speaker: the surface goes from flat to rippled when the music starts, and stays rippled while it plays.
  - fail: The speaker's cone plainly pumps and the water stays mirror-flat; or the surface is rippled from the start and goes flat while the cone is pumping; or the ripples appear and vanish at random with the cone unchanged.
- P2 [core · causeless_motion]
  - expect: The glass itself stays put or creeps only slightly; the water's ripples are fine and stay within the glass; nothing else moves without cause.
  - fail: The glass slides off or jumps; or the water sloshes in one big wave with the glass still; or ripples appear on other surfaces in the room.
- P3 [major · material_response]
  - expect: The ripples are a pattern on the water's surface: fine concentric or crossing waves, droplets at most; the water stays in the glass.
  - fail: The water jumps out in large spouts; or stays as a rigid textured surface that does not move; or the glass ripples along with the water.
- P4 [major · gravity_direction]
  - expect: Any droplets thrown up fall back and the water surface stays level overall.
  - fail: Droplets hover above the surface; or the water surface tilts and holds; or water climbs the glass walls.
- P5 [fatal · permanence_count]
  - expect: One glass and one speaker; the glass keeps its shape and the water its amount.
  - fail: A second glass appears; or the water level jumps; or the glass sinks into the speaker; or the glass vanishes.
- P6 [minor · attribute_drift]
  - expect: The speaker's grille, the glass and the background stay the same.
  - fail: The speaker changes design; or the glass changes shape; or the background shifts.

**Note.** Sound is inaudible in the frames. The timing anchor for P1 is a visible cone, indicator light or the caption's implied start; ripples with no visible driver are not a violation on their own.

## ACOU-0028 · sound_driven_vibration · train

**Caption.** A heavy truck rumbles past a house, and a teaspoon resting on a stack of plates by the window jiggles and chatters against the top plate.

**Expectation (hidden).** The spoon starts to jiggle as the truck approaches, moves most as it passes and lies still after it has gone; it does not move in a quiet street.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A teaspoon rests on a stack of plates near a window.
- S2 [core] A truck passes outside: seen through the window, or by its shadow or lights.
- S3 [core] The spoon jiggles and chatters on the top plate.
- S4 [minor] The jiggle is small; the spoon does not slide off.
- S5 [minor] The truck approaches, the spoon moves, the truck is gone, the spoon is still.

**PC**
- P1 [core · missing_consequence] (if: The truck or its passage is visible through the window.)
  - expect: The spoon's shaking follows the truck: it begins as the truck comes near, is strongest as it passes and dies away after it has gone.
  - fail: The truck passes and the spoon lies dead still; or the spoon shakes hardest after the truck has left; or the spoon shakes while the street is empty and stays unchanged as the truck passes.
- P2 [core · causeless_motion]
  - expect: The spoon's motion is a small tremble in place on the plate: it does not walk far or leap, and it stops when the shaking stops.
  - fail: The spoon leaps into the air; or slides across the plate and off the stack by itself; or spins; or keeps trembling unchanged for the whole clip.
- P3 [major · material_response]
  - expect: The plates stay a stack of rigid plates that may chatter slightly but stay stacked; the spoon stays rigid.
  - fail: Plates wobble like rubber; or the stack slides apart; or the spoon bends.
- P4 [major · gravity_direction]
  - expect: The spoon stays on the plate under gravity; if it hops it comes back down.
  - fail: The spoon hovers above the plate; or rises; or the plates lift.
- P5 [fatal · permanence_count]
  - expect: One spoon and the same plates; nothing passes through anything.
  - fail: A second spoon appears; or the plates change count; or the spoon sinks into the plate; or the spoon vanishes.
- P6 [minor · attribute_drift]
  - expect: The plates' pattern, the spoon and the window scene stay consistent apart from the truck.
  - fail: Plate patterns change; or the spoon changes colour; or the window view jumps.

## ACOU-0029 · sound_driven_vibration · train

**Caption.** A heavy door is slammed shut, and a picture frame on the nearby wall swings from side to side before hanging still.

**Expectation (hidden).** The frame starts swinging at the slam, the swings grow smaller, and it stops within a few seconds; it does not move before the slam.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A door and a picture frame on a nearby wall are present.
- S2 [core] The door slams shut.
- S3 [core] The frame swings from side to side afterwards.
- S4 [core] The frame comes to rest.
- S5 [minor] The frame hangs on the wall rather than standing on a surface.
- S6 [minor] The order is slam, swing, still.

**PC**
- P1 [core · causeless_motion]
  - expect: The frame hangs still until the slam, starts swinging at the slam, and does not start again by itself.
  - fail: The frame swings before the door moves; or starts long after the door has shut with nothing else happening; or starts again after coming to rest.
- P2 [core · process_direction]
  - expect: The swings shrink: each is smaller than the one before, until the frame hangs still.
  - fail: The swings grow; or stay the same size for the whole clip; or the frame stops dead at the end of a large swing.
- P3 [major · trajectory_momentum]
  - expect: The frame swings about its hanging point, staying on the wall, moving side to side in an arc.
  - fail: The frame slides along the wall; or rotates fully; or jumps between positions.
- P4 [major · material_response]
  - expect: The frame stays rigid, the wall does not deform, and the door stays a rigid slab as it slams.
  - fail: The frame bends; or the wall ripples at the slam; or the door flexes like rubber.
- P5 [fatal · permanence_count]
  - expect: One frame and one door; the frame stays on the wall and does not pass into it; nothing appears or vanishes.
  - fail: The frame passes into the wall; or falls off and is then back on the wall; or a second frame appears; or the picture inside the frame vanishes.
- P6 [minor · attribute_drift]
  - expect: The picture inside the frame, the wall and the door stay the same.
  - fail: The picture changes; or the wall colour changes; or the door changes design.

## ACOU-0053 · source_motion · train

**Caption.** A large speaker's cone pumps in and out as a bass-heavy track plays, and it stops moving when the music is paused.

**Expectation (hidden).** The cone moves in time with the beats, more on the low notes, and is still the instant the music pauses; it does not move in silence.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A large speaker with its cone visible.
- S2 [core] The cone moves in and out.
- S3 [core] The movement stops at some point, as the music is paused.
- S4 [minor] The stop is clean rather than a slow petering out.
- S5 [minor] The speaker is a large woofer.

**PC**
- P1 [core · causeless_motion]
  - expect: The cone moves as a piston along its axis, in and out about its rest position.
  - fail: The cone drifts sideways or rotates; or moves in only one direction and stays displaced; or keeps twitching irregularly after stopping.
- P2 [core · missing_consequence]
  - expect: When the music stops the cone stops: it returns to its rest position and stays there.
  - fail: The cone keeps pumping after the pause; or stops frozen away from its rest position; or alternates between moving and still several times.
- P3 [major · shape_identity]
  - expect: The cone keeps its round shape and its dust cap; it flexes as one piece with the surround stretching.
  - fail: The cone ripples like water; or changes size; or the dust cap detaches; or the cone splits.
- P4 [major · causeless_motion]
  - expect: The cabinet stays still; only the cone and its surround move.
  - fail: The cabinet rocks, walks or jumps with each beat; or the grille moves independently of the cone.
- P5 [fatal · permanence_count]
  - expect: One cone in one speaker; nothing passes through the cabinet.
  - fail: A second cone appears; or the cone vanishes; or the cone passes through the cabinet; or the speaker changes into another object.
- P6 [minor · attribute_drift]
  - expect: The speaker's colour, logo and the room stay the same.
  - fail: The cone changes colour; or the logo moves; or the background changes.

## ACOU-0054 · source_motion · train

**Caption.** A phone set to vibrate buzzes on a wooden table and creeps slowly across the surface.

**Expectation (hidden).** The phone shivers and moves only while it buzzes, in small jerks along the table.

**Declared violation types.** causeless_motion, trajectory_momentum

**SA**
- S1 [core] A phone lies on a wooden table.
- S2 [core] The phone visibly buzzes: it shivers in place.
- S3 [core] It moves across the table surface.
- S4 [minor] The motion is slow creeping in small jerks, not one glide.
- S5 [minor] The shivering is under way when the creeping starts; the phone does not move first and buzz later.

**PC**
- P1 [core · causeless_motion]
  - expect: The phone moves only while it visibly shivers; if the shiver stops, the phone stops at once and stays where it is.
  - fail: The phone slides while lying perfectly still; or keeps gliding after the shiver has visibly stopped; or starts moving again with no buzz.
- P2 [core · trajectory_momentum]
  - expect: The creep is a series of small jerks in a roughly consistent direction, possibly with slow rotation; the phone stays flat on the table.
  - fail: The phone shoots across the table in one smooth glide; or zigzags with large reversals; or stands up on an edge; or flips over.
- P3 [major · gravity_direction]
  - expect: The phone stays on the table surface throughout; if it reaches the edge it tips and falls.
  - fail: The phone hovers above the table; or hangs over the edge unsupported well past its middle; or climbs onto an object.
- P4 [major · material_response]
  - expect: The table is rigid and the phone a rigid slab.
  - fail: The table surface ripples like water; or the phone flexes like rubber; or the phone leaves a trail carved in the wood.
- P5 [fatal · permanence_count]
  - expect: One phone; it does not pass through the table, duplicate or vanish.
  - fail: The phone duplicates or vanishes; or passes into the table; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The phone's case, screen state and the table grain stay the same.
  - fail: The phone changes colour; or the screen content changes at random; or the table grain shifts.

**Note.** The caption does not require the buzzing to stop. A clip in which it never stops passes every SA item; if it does stop, the last two fail clauses of P1 apply to what follows.

## ACOU-0055 · source_motion · train

**Caption.** An electric toothbrush is switched on and left lying on a bathroom counter, and it buzzes and slowly turns in circles.

**Expectation (hidden).** The brush moves only while switched on and stops as soon as it is turned off.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] An electric toothbrush lies on a bathroom counter.
- S2 [core] It is switched on: a button is pressed or it starts buzzing.
- S3 [core] It visibly buzzes and moves.
- S4 [core] It turns in circles on the counter.
- S5 [minor] The motion is slow.
- S6 [minor] It is switched on first and moves after.

**PC**
- P1 [core · causeless_motion]
  - expect: The toothbrush moves only while it is on and buzzing: still before the switch, moving after, and if switched off it stops.
  - fail: It moves before being switched on; or moves while showing no vibration at all; or keeps moving after being switched off.
- P2 [core · missing_consequence]
  - expect: The visible vibration has its effect on the counter: the head blurs or shivers and the body creeps in small jerks, turning as it goes.
  - fail: The brush is plainly buzzing and the body glides smoothly as if pushed; or spins like a top; or the head does not shiver at all while the body moves.
- P3 [major · gravity_direction]
  - expect: It stays flat on the counter; if it reaches the edge it falls.
  - fail: It hovers; or stands up on end; or climbs a wall.
- P4 [major · material_response]
  - expect: The counter and the toothbrush stay rigid.
  - fail: The counter ripples; or the toothbrush bends; or the bristles stretch.
- P5 [fatal · permanence_count]
  - expect: One toothbrush; it does not pass into the counter, duplicate or vanish.
  - fail: A second toothbrush appears; or it vanishes; or it sinks into the counter; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: Its colour and the bathroom items stay the same.
  - fail: It changes colour; or the counter items move by themselves; or the counter changes pattern.

