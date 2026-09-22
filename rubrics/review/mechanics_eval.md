# Rubric review

75 rubrics. SA = caption adherence (core/minor); PC = physics (fatal/core/major/minor, each tagged with a violation type). Expectation is the hidden field from data/, shown for the reviewer only.

# Mechanics

## MECH-0251 · inertia · eval

**Caption.** A cyclist riding along a flat street stops pedalling and rests both feet on the pedals, and the bicycle coasts on down the street, gradually slowing.

**Expectation (hidden).** The bicycle keeps rolling forward after the legs stop, with no pause or jolt at the moment pedalling ends; the path stays straight and the wheels keep turning; it slows only gently, never speeding up, stopping dead, or rolling backward while the feet stay still.

**Declared violation types.** causeless_motion, trajectory_momentum

**SA**
- S1 [core] A cyclist rides along a flat street.
- S2 [core] The cyclist stops pedalling and rests both feet on the pedals.
- S3 [core] The bicycle coasts on down the street.
- S4 [core] It gradually slows.
- S5 [minor] The street is flat.
- S6 [minor] The pedalling stops first and the coasting follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The bicycle keeps rolling after the legs stop, with no pause or jolt at that moment, and slows only gently.
  - fail: It stops dead when the pedalling stops; or it speeds up with the feet still; or it rolls backward.
- P2 [core · trajectory_momentum]
  - expect: The path stays straight and the wheels keep turning.
  - fail: It swerves on the open street with no steering; or the wheels stop turning while it moves; or it jumps position between frames.
- P3 [major · gravity_direction]
  - expect: The bicycle stays upright on its wheels with the rider seated.
  - fail: It tips over while coasting at speed; or floats; or sinks into the road.
- P4 [major · shape_identity]
  - expect: The rider's legs stay still on the pedals and the pedals stop turning.
  - fail: The pedals keep turning with the feet still; or a leg bends mid-shin; or the rider detaches from the bike.
- P5 [fatal · shape_identity]
  - expect: One rider and one bicycle keep their number and shape.
  - fail: A limb detaches; or the bicycle duplicates; or the rider merges with the bike.
- P6 [minor · attribute_drift]
  - expect: The rider's clothing, the bike and the street stay the same.
  - fail: The clothing changes colour; or the bike changes; or the street rearranges.

**Note.** Inertia scene: the cyclist is kept because stopping the legs is the cause. Riding form is not judged.

## MECH-0252 · inertia · eval

**Caption.** A girl spinning on an office chair grabs the edge of the desk to stop, and her ponytail swings on around her head after the chair has stopped.

**Expectation (hidden).** The hair continues in the direction of the spin for a moment after the chair halts and then falls; it does not stop with the chair or swing the other way first.

**Declared violation types.** causeless_motion, trajectory_momentum

**SA**
- S1 [core] A girl spins on an office chair.
- S2 [core] She grabs the edge of the desk.
- S3 [core] The chair stops.
- S4 [core] Her ponytail swings on around her head after the chair has stopped.
- S5 [minor] The grab comes first, then the chair stops, then the hair swings on.

**PC**
- P1 [core · causeless_motion]
  - expect: The hair continues in the direction of the spin for a moment after the chair halts and then falls.
  - fail: The hair stops with the chair; or it keeps swinging long after; or it swings before the spin.
- P2 [core · trajectory_momentum]
  - expect: The ponytail carries on the same way the chair was turning.
  - fail: It swings the other way first; or flies straight up; or wraps the wrong way round her head.
- P3 [major · missing_consequence]
  - expect: The grab is what stops the chair: the hand closes on the desk and the chair halts.
  - fail: The chair stops before the hand reaches the desk; or the hand grabs and the chair keeps spinning; or the desk moves instead.
- P4 [major · gravity_direction]
  - expect: The hair falls back down after swinging.
  - fail: It hangs out sideways; or rises; or stays horizontal.
- P5 [fatal · shape_identity]
  - expect: One girl and one chair keep their number and shape.
  - fail: The hair detaches; or a second girl appears; or she merges with the chair.
- P6 [minor · attribute_drift]
  - expect: Her clothing, the chair and the desk stay the same.
  - fail: Her clothing changes colour; or the chair changes; or the desk rearranges.

**Note.** Inertia scene: the girl is kept because her hair is what carries the momentum. Her expression is not judged.

## MECH-0253 · inertia · eval

**Caption.** A stack of newspapers rides a conveyor belt in a printing plant, and when the belt is stopped the stack slides on a little before halting.

**Expectation (hidden).** The slide is in the belt's former direction and starts as the belt stops; the stack stops within a short distance and does not slide backward.

**Declared violation types.** causeless_motion, trajectory_momentum

**SA**
- S1 [core] A stack of newspapers rides a conveyor belt.
- S2 [core] The belt is stopped.
- S3 [core] The stack slides on a little.
- S4 [core] It halts.
- S5 [minor] The setting is a printing plant.
- S6 [minor] The belt stops first and the slide follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The slide starts as the belt stops and not before, and the stack stops within a short distance.
  - fail: It slides while the belt is running steadily; or slides with no stop; or keeps sliding to the end of the belt.
- P2 [core · trajectory_momentum]
  - expect: The slide is in the belt's former direction.
  - fail: It slides backward; or sideways; or the stack lifts off.
- P3 [major · shape_identity]
  - expect: The stack stays a stack, shearing a little at most.
  - fail: The papers fly everywhere; or the stack merges with the belt; or the stack grows.
- P4 [major · gravity_direction]
  - expect: It stays down on the belt.
  - fail: It floats; or sinks into the belt; or hangs over the edge unsupported.
- P5 [fatal · permanence_count]
  - expect: One stack and one belt keep their number.
  - fail: The stack duplicates; or vanishes; or the belt turns into another object.
- P6 [minor · attribute_drift]
  - expect: The newspapers and the plant stay the same.
  - fail: The papers change; or the belt changes colour; or the plant rearranges.

## MECH-0254 · gravity_fall · eval

**Caption.** The cord holding a hanging flowerpot on a porch snaps, and the pot falls and breaks on the boards below.

**Expectation (hidden).** The pot drops straight down the moment the cord parts, speeding up, and breaks on impact with soil spilling; it does not hover or fall sideways.

**Declared violation types.** gravity_direction, material_response

**SA**
- S1 [core] A flowerpot hangs from a cord on a porch.
- S2 [core] The cord snaps.
- S3 [core] The pot falls.
- S4 [core] It breaks on the boards below.
- S5 [minor] The snap comes first, then the fall, then the break.

**PC**
- P1 [core · gravity_direction]
  - expect: The pot drops straight down the moment the cord parts, speeding up.
  - fail: It hovers; or falls sideways; or slows as it falls.
- P2 [core · material_response]
  - expect: It breaks on impact with soil spilling, not before, and does not bounce whole.
  - fail: It breaks in mid-air; or bounces whole; or squashes like dough.
- P3 [major · missing_consequence]
  - expect: The cord is what held it, and the cord end swings free afterward.
  - fail: The pot falls with the cord intact; or the cord snaps and the pot hangs; or the cord vanishes.
- P4 [major · permanence_count]
  - expect: One pot, its soil and its pieces.
  - fail: The pot vanishes; or two pots fall; or soil appears from nowhere.
- P5 [fatal · solidity]
  - expect: The pot does not pass through the boards.
  - fail: It passes through the boards; or the boards pass through it; or it merges with the porch.
- P6 [minor · attribute_drift]
  - expect: The pot's colour and the porch stay the same.
  - fail: The pot changes colour; or the plant changes; or the porch rearranges.

## MECH-0255 · gravity_fall · eval

**Caption.** A sandbag hanging from a hook in a gym is unhooked and drops onto the mat below.

**Expectation (hidden).** The bag starts falling the instant it leaves the hook, drops straight down with increasing speed, lands on the mat and slumps; the empty hook swings; the bag does not drift sideways or pause.

**Declared violation types.** gravity_direction, trajectory_momentum

**SA**
- S1 [core] A sandbag hangs from a hook in a gym.
- S2 [core] It is unhooked.
- S3 [core] It drops onto the mat below.
- S4 [minor] The unhooking comes first and the drop follows.

**PC**
- P1 [core · gravity_direction]
  - expect: It falls the instant it leaves the hook, straight down and faster as it goes, and lands on the mat.
  - fail: It hangs after unhooking; or drifts sideways; or pauses in the air.
- P2 [core · trajectory_momentum]
  - expect: It lands below where it hung and slumps without bouncing high.
  - fail: It lands far to one side; or bounces higher than it fell; or slides away.
- P3 [major · causeless_motion]
  - expect: The empty hook swings after the release.
  - fail: The hook stays rigidly still; or swings before; or falls too.
- P4 [major · material_response]
  - expect: The bag is heavy and floppy and slumps on landing.
  - fail: It is a rigid block; or bounces like rubber; or bursts into sand.
- P5 [fatal · permanence_count]
  - expect: One bag and one hook keep their number.
  - fail: The bag duplicates; or vanishes; or the hook turns into another object.
- P6 [minor · attribute_drift]
  - expect: The bag and the gym stay the same.
  - fail: The bag changes colour; or the mat changes; or the gym rearranges.

## MECH-0256 · gravity_fall · eval

**Caption.** A phone balanced on a balcony rail slips off and falls into the swimming pool below with a splash.

**Expectation (hidden).** The phone falls straight down, faster as it goes, and enters the water with a splash then sinks; it does not drift outward or float.

**Declared violation types.** gravity_direction, trajectory_momentum

**SA**
- S1 [core] A phone is balanced on a balcony rail.
- S2 [core] It slips off.
- S3 [core] It falls into the swimming pool below.
- S4 [core] It makes a splash.
- S5 [minor] The slip comes first, then the fall, then the splash.

**PC**
- P1 [core · gravity_direction]
  - expect: It falls straight down, faster as it goes, and enters the water.
  - fail: It drifts outward; or floats; or slows.
- P2 [core · trajectory_momentum]
  - expect: It lands below the rail, not far out.
  - fail: It lands far from the rail; or curves; or hangs.
- P3 [major · missing_consequence]
  - expect: There is a splash at entry and the phone sinks.
  - fail: No splash; or it floats on top; or the splash is elsewhere.
- P4 [major · material_response]
  - expect: The phone is rigid and the water splashes and closes over it.
  - fail: The phone bends; or the water is rigid; or the phone bounces off the water.
- P5 [fatal · permanence_count]
  - expect: One phone keeps its number.
  - fail: It duplicates; or vanishes in the air; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The rail, the pool and the surroundings stay the same.
  - fail: The rail changes; or the pool changes colour; or the surroundings rearrange.

## MECH-0257 · collision · eval

**Caption.** A pigeon flies straight at a closed window, hits the glass with a thump, bounces off and drops to the ground below.

**Expectation (hidden).** The pigeon stops at the pane and is thrown back at the instant of impact; the glass stays whole and nothing passes through it; the bird falls after the bounce and does not fly on through the window.

**Declared violation types.** solidity, trajectory_momentum

**SA**
- S1 [core] A pigeon flies straight at a closed window.
- S2 [core] It hits the glass.
- S3 [core] It bounces off.
- S4 [core] It drops to the ground below.
- S5 [minor] The hit comes first, then the bounce, then the drop.

**PC**
- P1 [core · solidity]
  - expect: The pigeon stops at the pane, the glass stays whole, and nothing passes through.
  - fail: It passes through the glass; or the glass shatters and lets it through; or the bird sinks into the glass.
- P2 [core · trajectory_momentum]
  - expect: It is thrown back at the instant of impact, slower than it came.
  - fail: It is thrown back before contact; or keeps going forward; or leaves faster.
- P3 [major · gravity_direction]
  - expect: It falls after the bounce and lands.
  - fail: It hovers; or rises after the bounce; or floats.
- P4 [major · shape_identity]
  - expect: Its wings and body stay attached.
  - fail: A wing detaches; or the body morphs; or two birds appear.
- P5 [fatal · shape_identity]
  - expect: One pigeon and one window keep their number.
  - fail: The bird splits; or the window duplicates; or the bird merges with the glass.
- P6 [minor · attribute_drift]
  - expect: The plumage and the window frame stay the same.
  - fail: The plumage changes; or the frame changes; or the wall rearranges.

**Note.** The pigeon is self-driven: its flight is its own. Only the impact and what follows are judged.

## MECH-0258 · collision · eval

**Caption.** A football kicked at goal hits the crossbar and drops down onto the goal line.

**Expectation (hidden).** The ball rebounds off the bar at the moment of contact and falls under gravity; the bar does not bend and the ball does not pass through it.

**Declared violation types.** trajectory_momentum, gravity_direction

**SA**
- S1 [core] A football is kicked at a goal.
- S2 [core] It hits the crossbar.
- S3 [core] It drops down onto the goal line.
- S4 [minor] The hit comes first and the drop follows.

**PC**
- P1 [core · trajectory_momentum]
  - expect: It rebounds off the bar at the moment of contact.
  - fail: It changes course before the bar; or passes through; or leaves faster than it arrived.
- P2 [core · gravity_direction]
  - expect: It falls under gravity to the line.
  - fail: It hangs; or rises; or floats.
- P3 [major · material_response]
  - expect: The bar stays rigid and the ball squashes briefly.
  - fail: The bar bends; or the ball stays flat; or the ball sticks.
- P4 [major · solidity]
  - expect: The ball does not pass through the bar or the net.
  - fail: It passes through the bar; or through the net; or the net passes through the ball.
- P5 [fatal · permanence_count]
  - expect: One ball and one goal keep their number.
  - fail: The ball duplicates; or vanishes; or the goal changes shape.
- P6 [minor · attribute_drift]
  - expect: The ball and the goal stay the same.
  - fail: The ball changes colour; or the goal changes; or the pitch rearranges.

## MECH-0259 · collision · eval

**Caption.** A cue ball is struck into a tight triangle of balls on a pool table, and the balls scatter across the table in all directions.

**Expectation (hidden).** The balls move only after being struck, spread outward from the impact, and none overlaps another; the cue ball slows sharply.

**Declared violation types.** trajectory_momentum, missing_consequence, solidity

**SA**
- S1 [core] A tight triangle of balls sits on a pool table.
- S2 [core] A cue ball is struck into it.
- S3 [core] The balls scatter across the table in all directions.
- S4 [minor] The strike comes first and the scatter follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The balls move only after being struck, spreading outward from the impact.
  - fail: They move before; or are struck and stay; or scatter from a different point.
- P2 [core · trajectory_momentum]
  - expect: The cue ball slows sharply and the struck balls spread outward.
  - fail: The cue ball keeps its speed; or the balls move as a block; or balls fly back through the cue ball.
- P3 [major · solidity]
  - expect: No ball overlaps another.
  - fail: Balls overlap; or pass through each other; or sink into the cloth.
- P4 [major · causeless_motion]
  - expect: Each ball rolls straight and slows.
  - fail: A ball curves; or speeds up; or restarts.
- P5 [fatal · permanence_count]
  - expect: The balls keep their number.
  - fail: A ball vanishes; or a new one appears; or balls merge.
- P6 [minor · attribute_drift]
  - expect: The balls' colours and the table stay the same.
  - fail: Colours swap; or the cloth changes; or the table rearranges.

## MECH-0260 · collision · eval

**Caption.** A marble rolls across a table and hits a heavy steel ball at rest; the marble bounces back the way it came while the steel ball barely moves.

**Expectation (hidden).** At contact the marble reverses and rolls back slower than it arrived; the steel ball shifts at most slightly; neither passes through the other and the steel ball does not shoot off.

**Declared violation types.** trajectory_momentum, solidity

**SA**
- S1 [core] A marble rolls across a table toward a heavy steel ball at rest.
- S2 [core] The marble hits the steel ball.
- S3 [core] The marble bounces back the way it came.
- S4 [core] The steel ball barely moves.
- S5 [minor] The approach comes first and the rebound follows.

**PC**
- P1 [core · trajectory_momentum]
  - expect: At contact the marble reverses and rolls back slower, and the steel ball shifts at most slightly.
  - fail: The steel ball shoots off; or the marble keeps going; or the marble leaves faster.
- P2 [core · solidity]
  - expect: Neither passes through the other.
  - fail: They pass through each other; or overlap; or sink into the table.
- P3 [major · causeless_motion]
  - expect: Motion changes only at the contact.
  - fail: The marble reverses before contact; or the steel ball moves before; or the marble restarts.
- P4 [major · material_response]
  - expect: Both are hard and the contact is a brief click.
  - fail: A ball dents; or they stick; or a ball wobbles like jelly.
- P5 [fatal · permanence_count]
  - expect: Two balls stay two.
  - fail: A ball vanishes; or a third appears; or they merge.
- P6 [minor · attribute_drift]
  - expect: The balls and the table stay the same.
  - fail: The marble changes colour; or the steel ball changes size; or the table rearranges.

## MECH-0261 · friction_rolling · eval

**Caption.** A bottle cap spun on a kitchen counter spins in place, slows, and rattles to a stop.

**Expectation (hidden).** The spin slows steadily and the cap wobbles more as it slows; it does not speed up or stop instantly.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A bottle cap is spun on a kitchen counter.
- S2 [core] It spins in place.
- S3 [core] It slows.
- S4 [core] It rattles to a stop.
- S5 [minor] The spin comes first, then the slowing, then the stop.

**PC**
- P1 [core · process_direction]
  - expect: It slows steadily and wobbles more as it slows.
  - fail: It speeds up; or the wobble shrinks; or it stops instantly.
- P2 [core · causeless_motion]
  - expect: Nothing touches it after the spin.
  - fail: It is driven along; or reverses; or restarts.
- P3 [major · gravity_direction]
  - expect: It stays on the counter and settles flat.
  - fail: It lifts; or hangs on its edge; or floats.
- P4 [major · material_response]
  - expect: The cap is rigid and rattles.
  - fail: It bends; or melts; or splits.
- P5 [fatal · permanence_count]
  - expect: One cap keeps its number.
  - fail: It duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The cap and the counter stay the same.
  - fail: The cap changes colour; or the counter changes; or the kitchen rearranges.

## MECH-0262 · friction_rolling · eval

**Caption.** A wet bar of soap is squeezed in a hand in the bath, slips out of the grip and skids across the bottom of the tub.

**Expectation (hidden).** The soap leaves the hand as the fingers close and shoots out in one direction; it skids across the wet surface in a straight line and slows to a stop or stops against the side of the tub; it does not hover, change direction on its own, or stay stuck to the hand.

**Declared violation types.** trajectory_momentum, causeless_motion, gravity_direction

**SA**
- S1 [core] A wet bar of soap is squeezed in a hand in a bath.
- S2 [core] It slips out of the grip.
- S3 [core] It skids across the bottom of the tub.
- S4 [minor] The squeeze comes first, then the slip, then the skid.

**PC**
- P1 [core · causeless_motion]
  - expect: It leaves the hand as the fingers close and not before, then skids and slows or stops against the side.
  - fail: It hovers; or changes direction on its own; or stays stuck to the hand.
- P2 [core · trajectory_momentum]
  - expect: It shoots out in one direction and skids in a straight line.
  - fail: It curves; or reverses; or goes straight up.
- P3 [major · gravity_direction]
  - expect: It drops to the tub bottom and stays on it.
  - fail: It floats; or rises; or hangs.
- P4 [major · material_response]
  - expect: The slippery soap slides on the wet surface.
  - fail: It sticks dead on landing; or bounces like rubber; or dissolves instantly.
- P5 [fatal · permanence_count]
  - expect: One bar of soap keeps its number.
  - fail: It duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The soap and the tub stay the same.
  - fail: The soap changes colour; or the tub changes; or the bathroom rearranges.

**Note.** The hand is kept as the minimal trigger; the person is not judged.

## MECH-0263 · friction_rolling · eval

**Caption.** A tin can lying on its side and a wooden block are given the same shove across a floor; the can rolls far while the block stops within a short distance.

**Expectation (hidden).** Both start moving together; the block slows quickly and stops while the can rolls on much farther before stopping; neither speeds up or changes direction on its own.

**Declared violation types.** trajectory_momentum, causeless_motion

**SA**
- S1 [core] A tin can lying on its side and a wooden block are on a floor.
- S2 [core] Both are given a shove.
- S3 [core] The can rolls far.
- S4 [core] The block stops within a short distance.
- S5 [minor] The shove is the same for both.
- S6 [minor] The shove comes first and the two outcomes follow.

**PC**
- P1 [core · trajectory_momentum]
  - expect: Both start together, the block slows quickly and stops, and the can rolls on much further.
  - fail: The block goes further than the can; or both stop together; or the can stops dead.
- P2 [core · causeless_motion]
  - expect: Neither speeds up or changes direction on its own.
  - fail: One speeds up; or curves; or restarts.
- P3 [major · gravity_direction]
  - expect: Both stay on the floor.
  - fail: One floats; or sinks; or lifts.
- P4 [major · material_response]
  - expect: The can rolls, turning, and the block slides without turning.
  - fail: The block rolls like a can; or the can slides without turning; or the can squashes.
- P5 [fatal · permanence_count]
  - expect: One can and one block keep their number.
  - fail: One duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The can, the block and the floor stay the same.
  - fail: The can changes label; or the block changes; or the floor rearranges.

## MECH-0264 · projectile · eval

**Caption.** A water balloon is lobbed over a garden fence and arcs over into a paddling pool on the other side.

**Expectation (hidden).** The balloon rises, clears the fence near the top of its arc, wobbles in flight, and falls into the pool with a splash; it does not travel flat or hang above the fence.

**Declared violation types.** trajectory_momentum, gravity_direction

**SA**
- S1 [core] A water balloon is lobbed over a garden fence.
- S2 [core] It arcs over the fence.
- S3 [core] It lands in a paddling pool on the other side.
- S4 [minor] The lob comes first, then the arc, then the landing.

**PC**
- P1 [core · trajectory_momentum]
  - expect: It follows one smooth arc, clearing the fence near the top.
  - fail: It flies flat; or hangs above the fence; or changes direction.
- P2 [core · gravity_direction]
  - expect: It falls after the peak and lands in the pool with a splash.
  - fail: It rises again; or hovers; or floats down.
- P3 [major · material_response]
  - expect: It wobbles in flight as a bag of liquid and splashes or bursts on landing.
  - fail: It is a rigid ball; or deflates in the air; or bounces out whole and high.
- P4 [major · solidity]
  - expect: It clears the fence and does not pass through it.
  - fail: It passes through the fence; or sinks into the pool bottom; or the pool passes through it.
- P5 [fatal · permanence_count]
  - expect: One balloon keeps its number.
  - fail: It duplicates; or vanishes in flight; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The balloon, the fence and the pool stay the same.
  - fail: The balloon changes colour; or the fence changes; or the pool rearranges.

## MECH-0265 · projectile · eval

**Caption.** A weighted fishing line is cast far out over a lake from the bank, and the weight splashes into the water.

**Expectation (hidden).** The weight flies in an arc, pulling line behind it, and drops into the water; it does not stop in the air or fly straight.

**Declared violation types.** trajectory_momentum, gravity_direction

**SA**
- S1 [core] A weighted fishing line is cast from a bank over a lake.
- S2 [core] The weight flies out.
- S3 [core] It splashes into the water.
- S4 [minor] The line trails behind the weight.
- S5 [minor] The cast comes first and the splash follows.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The weight flies in an arc pulling the line behind it.
  - fail: It flies flat; or stops in the air; or changes direction.
- P2 [core · gravity_direction]
  - expect: It falls after the peak into the water.
  - fail: It rises; or hovers; or floats on top.
- P3 [major · missing_consequence]
  - expect: A splash and rings appear where it enters.
  - fail: No splash; or the splash is elsewhere; or the splash comes before it lands.
- P4 [major · material_response]
  - expect: The line is a limp thread trailing behind.
  - fail: It is a rigid rod; or stretches; or leads the weight.
- P5 [fatal · permanence_count]
  - expect: One weight and one line keep their number.
  - fail: The weight duplicates; or vanishes; or the line splits.
- P6 [minor · attribute_drift]
  - expect: The rod and the lake stay the same.
  - fail: The rod changes; or the lake changes colour; or the bank rearranges.

## MECH-0266 · projectile · eval

**Caption.** A tennis ball rolls off the end of a table and curves down to the floor, landing a short distance out from the table's edge, and bounces on.

**Expectation (hidden).** The ball keeps moving forward as it leaves the edge and drops in a curve that steepens; it lands beyond the edge, not straight below it, and does not stop in the air or fall straight down.

**Declared violation types.** trajectory_momentum, gravity_direction

**SA**
- S1 [core] A tennis ball rolls off the end of a table.
- S2 [core] It curves down to the floor.
- S3 [core] It lands a short distance out from the edge.
- S4 [core] It bounces on.
- S5 [minor] The roll off comes first, then the curve down, then the bounce.

**PC**
- P1 [core · trajectory_momentum]
  - expect: It keeps moving forward as it leaves the edge and lands beyond it, not straight below.
  - fail: It drops straight down at the edge; or stops in the air; or reverses.
- P2 [core · gravity_direction]
  - expect: The curve steepens as it falls and it falls faster.
  - fail: It flies flat; or hangs; or slows.
- P3 [major · process_direction]
  - expect: It bounces lower than it dropped.
  - fail: It bounces higher; or the same height; or stops dead.
- P4 [major · material_response]
  - expect: It squashes briefly and springs back round.
  - fail: It stays flat; or sinks into the floor; or splashes.
- P5 [fatal · permanence_count]
  - expect: One ball keeps its number.
  - fail: It duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The ball and the table stay the same.
  - fail: The ball changes colour; or the table changes; or the room rearranges.

## MECH-0267 · balance_topple · eval

**Caption.** A house of playing cards stands on a table; the table is bumped and the house collapses into a heap.

**Expectation (hidden).** The collapse begins at the bump and runs through the structure in under a second; every card ends flat or leaning on the table; none stays balanced in the air.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] A house of playing cards stands on a table.
- S2 [core] The table is bumped.
- S3 [core] The house collapses into a heap.
- S4 [minor] The bump comes first and the collapse follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The collapse begins at the bump and runs through the structure quickly.
  - fail: It collapses before the bump; or the table is bumped and it stands; or only part falls and the rest hangs in place.
- P2 [core · gravity_direction]
  - expect: Every card ends flat or leaning on the table, and none stays in the air.
  - fail: A card hangs in the air; or rises; or stays balanced on nothing.
- P3 [major · material_response]
  - expect: The cards flex slightly, slide and flutter.
  - fail: They bounce like rigid blocks; or fold like cloth; or shatter.
- P4 [major · permanence_count]
  - expect: The cards keep their number.
  - fail: Cards vanish; or multiply; or restack themselves.
- P5 [fatal · shape_identity]
  - expect: The cards and the table keep their shape.
  - fail: A card turns into another object; or the table changes; or cards merge.
- P6 [minor · attribute_drift]
  - expect: The cards' faces and the table stay the same.
  - fail: The faces change; or the table changes colour; or the room rearranges.

## MECH-0268 · balance_topple · eval

**Caption.** A ladder leaning at too shallow an angle against a garden wall slides out at its feet and falls flat to the ground.

**Expectation (hidden).** The feet slip away from the wall first, the top slides down the wall as the angle flattens, and the ladder lands flat; it does not stay propped once the feet move or fall toward the wall.

**Declared violation types.** gravity_direction, causeless_motion

**SA**
- S1 [core] A ladder leans against a garden wall at a shallow angle.
- S2 [core] Its feet slide out.
- S3 [core] It falls flat to the ground.
- S4 [minor] The angle is shallow.
- S5 [minor] The feet slide first and the fall follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The feet slip away from the wall first and the top slides down as the angle flattens, with nothing else touching it.
  - fail: The top moves first with the feet fixed; or the ladder is pushed; or the feet slide toward the wall.
- P2 [core · gravity_direction]
  - expect: It does not stay propped once the feet move, and it lands flat.
  - fail: It stays propped after the feet slide; or falls toward or over the wall; or hangs mid-fall.
- P3 [major · trajectory_momentum]
  - expect: It falls away from the wall along its own line.
  - fail: It falls sideways; or upward; or rotates about its middle.
- P4 [major · material_response]
  - expect: The ladder is rigid and clatters.
  - fail: It bends; or bounces high; or breaks into pieces.
- P5 [fatal · permanence_count]
  - expect: One ladder keeps its number.
  - fail: It duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The ladder and the wall stay the same.
  - fail: The ladder changes; or the wall changes; or the garden rearranges.

## MECH-0269 · balance_topple · eval

**Caption.** A bin standing in a yard is knocked by the swinging end of a long ladder and tips over.

**Expectation (hidden).** The bin tips at the moment the ladder end hits it and falls in the direction of the swing, spilling; it does not move before contact.

**Declared violation types.** trajectory_momentum, gravity_direction

**SA**
- S1 [core] A bin stands in a yard.
- S2 [core] The swinging end of a long ladder knocks it.
- S3 [core] The bin tips over.
- S4 [minor] The knock comes first and the tip follows.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The bin tips at the moment the ladder end hits it and falls in the direction of the swing.
  - fail: It tips toward the ladder; or before contact; or the ladder passes without touching and the bin falls anyway.
- P2 [core · gravity_direction]
  - expect: It falls to the ground and stays, and any contents spill downward.
  - fail: It hovers; or rights itself; or the contents rise.
- P3 [major · causeless_motion]
  - expect: The bin does not move before the contact.
  - fail: It moves before; or slides with nothing touching it; or jumps.
- P4 [major · material_response]
  - expect: The bin is rigid and may dent.
  - fail: It folds; or bounces high; or melts.
- P5 [fatal · permanence_count]
  - expect: One bin and one ladder keep their number.
  - fail: The bin duplicates; or vanishes; or the ladder passes through it.
- P6 [minor · attribute_drift]
  - expect: The bin and the yard stay the same.
  - fail: The bin changes colour; or the yard rearranges; or the ladder changes.

## MECH-0270 · tension · eval

**Caption.** The cord of a window blind is pulled, and the blind gathers upward as the cord runs down.

**Expectation (hidden).** The blind rises only as fast as the cord is pulled and stops when the pulling stops; the cord stays taut on the pulled side and does not stretch.

**Declared violation types.** material_response, missing_consequence

**SA**
- S1 [core] A window blind hangs with its cord.
- S2 [core] The cord is pulled.
- S3 [core] The blind gathers upward.
- S4 [core] The cord runs down.
- S5 [minor] The pull comes first and the rise follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The blind rises only as fast as the cord is pulled and stops when the pulling stops.
  - fail: It rises with no pull; or keeps rising after the pull stops; or the cord is pulled and the blind stays.
- P2 [core · material_response]
  - expect: The cord stays taut on the pulled side and does not stretch.
  - fail: It is slack while lifting; or stretches; or bunches.
- P3 [major · gravity_direction]
  - expect: The blind hangs from the head rail and the slats gather at the top.
  - fail: They gather at the bottom; or the blind rises above the rail; or it floats.
- P4 [major · trajectory_momentum]
  - expect: The cord goes down as the blind goes up.
  - fail: Both go up; or the cord is still while the blind moves; or the blind goes down as the cord is pulled.
- P5 [fatal · permanence_count]
  - expect: One blind and one cord keep their number.
  - fail: The blind duplicates; or the cord vanishes; or the blind turns into another object.
- P6 [minor · attribute_drift]
  - expect: The blind and the window stay the same.
  - fail: The blind changes colour; or the window changes; or the room rearranges.

## MECH-0271 · tension · eval

**Caption.** A marionette is lifted off the stage by its control bar, and the strings go taut and the puppet's limbs hang from them.

**Expectation (hidden).** The strings straighten as the bar lifts, the limbs rise only when their strings tighten, and the strings go slack when the puppet is set down.

**Declared violation types.** material_response, gravity_direction

**SA**
- S1 [core] A marionette lies on a stage with its control bar.
- S2 [core] The bar is lifted.
- S3 [core] The strings go taut.
- S4 [core] The puppet's limbs hang from the strings.
- S5 [minor] The lift comes first, then the taut strings, then the hanging limbs.

**PC**
- P1 [core · material_response]
  - expect: The strings straighten as the bar lifts, the limbs rise only when their strings tighten, and the strings go slack when the puppet is set down.
  - fail: Limbs rise with slack strings; or the strings stretch; or they stay taut with the puppet on the stage and the bar low.
- P2 [core · gravity_direction]
  - expect: The limbs hang down from the strings, dangling.
  - fail: They stand out sideways; or the puppet rises above the bar; or the limbs float.
- P3 [major · causeless_motion]
  - expect: The puppet moves only as the bar moves.
  - fail: It moves by itself; or jumps; or the bar moves and the puppet does not.
- P4 [major · shape_identity]
  - expect: The limbs stay attached at their joints.
  - fail: A limb detaches; or a string passes through the puppet; or the puppet duplicates.
- P5 [fatal · permanence_count]
  - expect: One puppet and one bar keep their number.
  - fail: The puppet duplicates; or vanishes; or the bar turns into another object.
- P6 [minor · attribute_drift]
  - expect: The puppet's costume and the stage stay the same.
  - fail: The costume changes; or the stage changes; or the strings change colour.

## MECH-0272 · tension · eval

**Caption.** The anchor rope of a small boat is hauled in, and the rope comes up taut and dripping until the anchor breaks the surface.

**Expectation (hidden).** The rope runs straight down into the water under load and stays taut while pulled; water drips from it; the anchor appears only when enough rope is in.

**Declared violation types.** material_response, gravity_direction

**SA**
- S1 [core] An anchor rope runs from a small boat into the water.
- S2 [core] It is hauled in.
- S3 [core] The rope comes up taut and dripping.
- S4 [core] The anchor breaks the surface.
- S5 [minor] The hauling comes first and the anchor appears last.

**PC**
- P1 [core · material_response]
  - expect: The rope runs straight down under load and stays taut while pulled.
  - fail: It is slack while hauling; or stretches; or hangs in a loose curve.
- P2 [core · gravity_direction]
  - expect: Water drips downward from the rope and the anchor hangs below it.
  - fail: Drips rise; or the anchor is above the rope; or the rope rises on its own.
- P3 [major · missing_consequence]
  - expect: The anchor appears only when enough rope is in.
  - fail: It appears immediately; or the rope is hauled and no anchor comes; or it appears elsewhere.
- P4 [major · causeless_motion]
  - expect: The rope moves only as it is hauled.
  - fail: It climbs by itself; or the anchor rises alone; or the boat shoots away.
- P5 [fatal · permanence_count]
  - expect: One rope and one anchor keep their number.
  - fail: The rope splits; or the anchor duplicates; or the anchor vanishes.
- P6 [minor · attribute_drift]
  - expect: The boat and the water stay the same.
  - fail: The boat changes colour; or the water changes; or the shore rearranges.

## MECH-0273 · deformation · eval

**Caption.** A vacuum-packed foam mattress is cut open, and the flat compressed slab swells and puffs up toward its full thickness.

**Expectation (hidden).** The foam expands as soon as the bag is opened, thickening evenly and slowing as it nears full size; it does not stay flat, shrink, or grow beyond a mattress shape.

**Declared violation types.** material_response, shape_identity

**SA**
- S1 [core] A vacuum-packed foam mattress lies as a flat slab.
- S2 [core] The bag is cut open.
- S3 [core] The slab swells and puffs up.
- S4 [minor] It grows toward its full thickness.
- S5 [minor] The cut comes first and the swelling follows.

**PC**
- P1 [core · material_response]
  - expect: The foam expands as soon as the bag opens, thickening and slowing as it nears full size.
  - fail: It stays flat; or expands before the cut; or springs up instantly like a spring.
- P2 [core · shape_identity]
  - expect: It stays a mattress shape and does not shrink or grow beyond it.
  - fail: It shrinks; or balloons round; or splits.
- P3 [major · process_direction]
  - expect: It only expands and then holds.
  - fail: It deflates again; or pulses; or grows then shrinks.
- P4 [major · causeless_motion]
  - expect: It stays put while expanding.
  - fail: It slides; or jumps; or lifts off.
- P5 [fatal · permanence_count]
  - expect: One mattress keeps its number.
  - fail: It duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The foam's colour and the room stay the same.
  - fail: The foam changes colour; or the bag changes; or the room rearranges.

## MECH-0274 · deformation · eval

**Caption.** A rubber duck is squeezed under the bathwater and released, and it squirts water and puffs back to shape.

**Expectation (hidden).** The duck flattens while squeezed, a jet of water comes out of its hole, and it refills and rounds out when released.

**Declared violation types.** material_response, process_direction

**SA**
- S1 [core] A rubber duck is squeezed under bathwater.
- S2 [core] It is released.
- S3 [core] It squirts water.
- S4 [core] It puffs back to shape.
- S5 [minor] The squeeze comes first, then the release, then the squirt and the puff back.

**PC**
- P1 [core · material_response]
  - expect: It flattens while squeezed and rounds out when released.
  - fail: It stays flat; or does not deform; or shatters.
- P2 [core · process_direction]
  - expect: The jet comes out on the squeeze, and the refill and rounding come on the release.
  - fail: It squirts while unsqueezed; or squirts only on release; or puffs back while still squeezed.
- P3 [major · gravity_direction]
  - expect: The jet arcs and falls back to the water, and the duck floats up.
  - fail: The jet rises indefinitely; or the duck sinks; or the water is rigid.
- P4 [major · missing_consequence]
  - expect: The water comes from the duck's hole.
  - fail: It comes from elsewhere; or there is no jet; or the jet comes before the squeeze.
- P5 [fatal · permanence_count]
  - expect: One duck keeps its number.
  - fail: It duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The duck's colour and the bath stay the same.
  - fail: The duck changes colour; or the bath changes; or the bathroom rearranges.

## MECH-0275 · deformation · eval

**Caption.** A sheet of aluminium foil is pressed down over an upturned bowl and lifted off, and the foil keeps the bowl's rounded shape.

**Expectation (hidden).** The foil wrinkles and moulds to the bowl while pressed and holds that dome shape after it is lifted away; it does not spring back flat or tear.

**Declared violation types.** material_response, shape_identity

**SA**
- S1 [core] A sheet of aluminium foil is pressed down over an upturned bowl.
- S2 [core] It is lifted off.
- S3 [core] The foil keeps the bowl's rounded shape.
- S4 [minor] The press comes first, then the lift, then the shape holds.

**PC**
- P1 [core · material_response]
  - expect: It wrinkles and moulds to the bowl while pressed and holds that dome after it is lifted away.
  - fail: It springs back flat; or tears; or does not mould.
- P2 [core · shape_identity]
  - expect: The dome matches the bowl.
  - fail: It is a different shape; or grows; or shrinks.
- P3 [major · causeless_motion]
  - expect: It moves only with the hands.
  - fail: It lifts itself; or slides; or jumps.
- P4 [major · solidity]
  - expect: The foil lies on the bowl, not through it.
  - fail: It passes through the bowl; or the bowl passes through the foil; or the hands pass through.
- P5 [fatal · permanence_count]
  - expect: One sheet and one bowl keep their number.
  - fail: The foil duplicates; or the bowl vanishes; or the foil turns into another object.
- P6 [minor · attribute_drift]
  - expect: The foil's shine and the bowl stay the same.
  - fail: The foil changes colour; or the bowl changes; or the background rearranges.

## MECH-0276 · cut_tear · eval

**Caption.** A cable tie holding a bundle of cables is snipped with cutters, and the bundle springs apart into loose cables.

**Expectation (hidden).** The tie parts where the blades close and the cables spread out at that instant; the tie does not rejoin and the bundle does not stay tight without it.

**Declared violation types.** permanence_count, missing_consequence

**SA**
- S1 [core] A cable tie holds a bundle of cables.
- S2 [core] It is snipped with cutters.
- S3 [core] The bundle springs apart into loose cables.
- S4 [minor] The snip comes first and the spring apart follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The tie parts where the blades close and the cables spread at that instant.
  - fail: The cables spread before the cut; or the tie is cut and they stay tight; or the tie parts elsewhere.
- P2 [core · permanence_count]
  - expect: The tie does not rejoin and the cables keep their number.
  - fail: It rejoins; or cables vanish; or the tie vanishes.
- P3 [major · material_response]
  - expect: The cables spring apart as stiff but flexible things.
  - fail: They are rigid rods; or flow like liquid; or the tie stretches.
- P4 [major · gravity_direction]
  - expect: The loose cables sag and droop.
  - fail: They float; or rise; or stand out rigidly.
- P5 [fatal · shape_identity]
  - expect: The cutters and the cables keep their shape.
  - fail: The cutters pass through a cable without cutting; or a cable turns into another object; or cables merge.
- P6 [minor · attribute_drift]
  - expect: The cables' colours and the background stay the same.
  - fail: The colours change; or the cutters change; or the background rearranges.

## MECH-0277 · cut_tear · eval

**Caption.** A plank on a sawhorse is sawn through, and the cut end drops to the ground as the saw comes through.

**Expectation (hidden).** The kerf deepens with each stroke, sawdust falls, and the piece parts only when the saw is through; the two pieces do not rejoin.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A plank rests on a sawhorse.
- S2 [core] It is sawn through.
- S3 [core] The cut end drops to the ground as the saw comes through.
- S4 [minor] The sawing comes first and the drop follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The kerf deepens with each stroke, sawdust falls, and the piece parts only when the saw is through.
  - fail: It parts before the saw is through; or the saw passes with no cut; or the cut appears elsewhere.
- P2 [core · permanence_count]
  - expect: The two pieces stay two.
  - fail: They rejoin; or a third piece appears; or the plank is whole again.
- P3 [major · gravity_direction]
  - expect: The cut end falls and the sawdust falls.
  - fail: They float; or rise; or hang.
- P4 [major · material_response]
  - expect: The wood is rigid and splinters.
  - fail: It bends; or melts; or shatters like glass.
- P5 [fatal · shape_identity]
  - expect: One saw and one plank keep their number.
  - fail: The saw passes through the hand; or the plank duplicates; or the saw vanishes.
- P6 [minor · attribute_drift]
  - expect: The plank and the sawhorse stay the same.
  - fail: The wood changes colour; or the sawhorse changes; or the background rearranges.

## MECH-0278 · cut_tear · eval

**Caption.** A sheet of paper is fed into a shredder, and it comes out the bottom as a bundle of thin strips.

**Expectation (hidden).** The sheet is drawn in at the top and strips emerge below as it passes; the sheet does not reappear whole.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A sheet of paper is fed into the top of a shredder.
- S2 [core] It is drawn in.
- S3 [core] Strips come out of the bottom.
- S4 [minor] The sheet goes in first and the strips come out after.

**PC**
- P1 [core · missing_consequence]
  - expect: The sheet is drawn in at the top and strips emerge below as it passes.
  - fail: Strips emerge before the sheet enters; or the sheet goes in and nothing comes out; or strips come out the top.
- P2 [core · permanence_count]
  - expect: The sheet does not reappear whole and the strips are from that sheet.
  - fail: The sheet is whole again; or strips appear from nowhere; or the sheet vanishes with no strips.
- P3 [major · gravity_direction]
  - expect: The strips hang and fall.
  - fail: They rise; or float; or stand out rigidly.
- P4 [major · material_response]
  - expect: The strips are flexible paper.
  - fail: They are rigid; or melt; or tear randomly.
- P5 [fatal · shape_identity]
  - expect: One shredder keeps its shape.
  - fail: It duplicates; or turns into another object; or the paper merges with it.
- P6 [minor · attribute_drift]
  - expect: The shredder and the paper stay the same.
  - fail: The shredder changes; or the paper changes colour; or the room rearranges.

## MECH-0279 · fluid · eval

**Caption.** Thick paint is poured from a tin onto a flat canvas, and it spreads slowly into a rounded pool and stops.

**Expectation (hidden).** The paint flows outward from where it lands, slower and thicker than water would, and settles into a rounded shape with a raised edge; it does not keep spreading thin or climb back into the tin.

**Declared violation types.** process_direction, material_response

**SA**
- S1 [core] Thick paint is poured from a tin onto a flat canvas.
- S2 [core] It spreads slowly.
- S3 [core] It forms a rounded pool.
- S4 [core] It stops spreading.
- S5 [minor] The pour comes first, then the spread, then the stop.

**PC**
- P1 [core · material_response]
  - expect: It flows outward slower and thicker than water, with a rounded raised edge.
  - fail: It spreads thin and fast; or is a rigid lump; or beads into balls.
- P2 [core · process_direction]
  - expect: It spreads and then settles, and does not keep spreading thin or climb back.
  - fail: It climbs back into the tin; or shrinks; or jumps.
- P3 [major · gravity_direction]
  - expect: The stream falls down onto the canvas.
  - fail: It curves; or hangs; or rises.
- P4 [major · missing_consequence] (if: The tin's tilt is visible in the clip.)
  - expect: The tin's tilt produces the flow.
  - fail: Paint pours from an upright tin; or the tin is tipped and nothing comes; or it continues after the tin is righted.
- P5 [fatal · permanence_count]
  - expect: One tin and one canvas, and paint comes only from the tin.
  - fail: Paint appears with no stream; or the tin duplicates; or paint passes through the canvas.
- P6 [minor · attribute_drift]
  - expect: The paint's colour and the canvas stay the same.
  - fail: The paint changes colour; or the canvas changes; or the room rearranges.

## MECH-0280 · fluid · eval

**Caption.** A large stone is dropped into a bucket full of water, and water spills over the rim onto the ground.

**Expectation (hidden).** The splash and overflow happen as the stone enters, the level stays at the rim afterward, and the stone sinks to the bottom; the stone does not pass through the bucket.

**Declared violation types.** material_response, missing_consequence, solidity

**SA**
- S1 [core] A bucket is full of water.
- S2 [core] A large stone is dropped into it.
- S3 [core] Water spills over the rim onto the ground.
- S4 [minor] The drop comes first and the spill follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The splash and overflow happen as the stone enters, and the level stays at the rim afterward.
  - fail: It overflows before; or the stone goes in and nothing overflows; or the level drops far below the rim.
- P2 [core · solidity]
  - expect: The stone sinks to the bottom and does not pass through the bucket.
  - fail: It passes through; or floats; or hangs.
- P3 [major · material_response]
  - expect: The water splashes and runs down the outside.
  - fail: It is rigid; or beads; or the stone splashes like liquid.
- P4 [major · gravity_direction]
  - expect: Spilled water runs downward.
  - fail: It runs up; or floats; or hangs.
- P5 [fatal · permanence_count]
  - expect: One bucket and one stone keep their number.
  - fail: The bucket duplicates; or the stone vanishes; or water appears elsewhere.
- P6 [minor · attribute_drift]
  - expect: The bucket and the ground stay the same.
  - fail: The bucket changes colour; or the ground changes; or the background rearranges.

## MECH-0281 · fluid · eval

**Caption.** The plug of a full bathtub is pulled, and as the water drains a swirling whirlpool forms over the drain.

**Expectation (hidden).** The level falls steadily and a dimple over the drain deepens into a spinning funnel that grows as the water gets shallower; the water does not rise or spin without draining.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A full bathtub has its plug pulled.
- S2 [core] The water drains.
- S3 [core] A swirling whirlpool forms over the drain.
- S4 [minor] The plug comes out first and the whirlpool forms after.

**PC**
- P1 [core · process_direction]
  - expect: The level falls steadily and a dimple over the drain deepens into a funnel that grows as the water gets shallower.
  - fail: The level rises; or the funnel shrinks as the water gets lower; or it drains and then refills.
- P2 [core · causeless_motion]
  - expect: The spin is at the drain, and the water does not spin without draining.
  - fail: It spins with the plug in; or spins away from the drain; or the whole tub churns.
- P3 [major · gravity_direction]
  - expect: The water goes down the drain.
  - fail: It goes up; or out over the rim; or floats.
- P4 [major · material_response]
  - expect: The surface is liquid, dimpling into a funnel.
  - fail: It is rigid; or beads; or is solid.
- P5 [fatal · permanence_count]
  - expect: One tub keeps its shape and the drain stays where it is.
  - fail: The drain moves; or the tub duplicates; or water appears from nowhere.
- P6 [minor · attribute_drift]
  - expect: The tub and the bathroom stay the same.
  - fail: The tub changes colour; or the tiles change; or the room rearranges.

## MECH-0282 · fluid · eval

**Caption.** A bucket with a hole near its bottom is filled from a tap, and a thin stream squirts out of the hole and arcs onto the ground.

**Expectation (hidden).** The stream comes only from the hole, arcs outward and down, and gets weaker as the level in the bucket falls; it does not squirt upward.

**Declared violation types.** material_response, gravity_direction

**SA**
- S1 [core] A bucket with a hole near its bottom is filled from a tap.
- S2 [core] A thin stream squirts out of the hole.
- S3 [core] It arcs onto the ground.
- S4 [minor] The filling comes first and the squirt follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The stream arcs outward and down.
  - fail: It squirts upward; or goes straight out level; or hangs.
- P2 [core · material_response]
  - expect: The stream is thin liquid that breaks into drops.
  - fail: It is a rigid rod; or beads; or is solid.
- P3 [major · missing_consequence]
  - expect: The stream comes only from the hole.
  - fail: It comes from elsewhere; or there is no stream with water above the hole; or a stream comes from an empty bucket.
- P4 [major · process_direction]
  - expect: The stream is stronger with more water above the hole.
  - fail: It is unchanged when the bucket empties; or stops while the bucket is full; or reverses.
- P5 [fatal · permanence_count]
  - expect: One bucket keeps its number.
  - fail: It duplicates; or vanishes; or the hole moves.
- P6 [minor · attribute_drift]
  - expect: The bucket and the tap stay the same.
  - fail: The bucket changes colour; or the tap changes; or the ground rearranges.

## MECH-0283 · granular · eval

**Caption.** A tray of dry rice is tilted to one side, and the rice slides to the low edge and piles up there while the high side clears.

**Expectation (hidden).** The grains flow downhill as a sheet once the tilt is steep enough, collect against the low rim, and the pile's surface settles at a slope; they do not move uphill or stay spread evenly on a tilted tray.

**Declared violation types.** gravity_direction, causeless_motion

**SA**
- S1 [core] A tray of dry rice is tilted to one side.
- S2 [core] The rice slides to the low edge.
- S3 [core] It piles up there.
- S4 [core] The high side clears.
- S5 [minor] The tilt comes first and the slide follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The grains flow downhill as a sheet and collect against the low rim.
  - fail: They move uphill; or stay spread evenly on the tilted tray; or float.
- P2 [core · causeless_motion]
  - expect: The flow starts once the tilt is steep enough and not before.
  - fail: It slides on a level tray; or slides before the tilt; or keeps flowing with the tray level again.
- P3 [major · material_response]
  - expect: The grains flow and pile at a slope.
  - fail: They flow flat like liquid; or move as a solid block; or bounce like balls.
- P4 [major · process_direction]
  - expect: The pile only grows on the low side while tilted.
  - fail: It shrinks; or redistributes; or appears before the tilt.
- P5 [fatal · permanence_count]
  - expect: One tray keeps its number and the rice its total.
  - fail: Rice appears from nowhere; or vanishes; or the tray duplicates.
- P6 [minor · attribute_drift]
  - expect: The tray and the rice stay the same.
  - fail: The tray changes colour; or the rice changes colour; or the background rearranges.

## MECH-0284 · granular · eval

**Caption.** A sandbag on a low wall is punctured near its bottom, and a thin stream of sand runs out onto the ground while the bag slowly slumps.

**Expectation (hidden).** The stream comes only from the hole and falls straight down, building a small cone below; the bag sags and wrinkles as it empties; the sand does not flow back in or stop while the bag is still full.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] A sandbag sits on a low wall.
- S2 [core] It is punctured near its bottom.
- S3 [core] A thin stream of sand runs out onto the ground.
- S4 [core] The bag slowly slumps.
- S5 [minor] The puncture comes first, then the stream, then the slump.

**PC**
- P1 [core · missing_consequence]
  - expect: The stream comes only from the hole and starts at the puncture.
  - fail: It starts before the puncture; or comes from elsewhere; or the bag is punctured and nothing comes out.
- P2 [core · gravity_direction]
  - expect: The sand falls straight down and builds a small cone below.
  - fail: It goes up; or sideways; or hangs.
- P3 [major · material_response]
  - expect: The bag sags and wrinkles as it empties, and the sand runs as grains.
  - fail: The bag is rigid; or the sand is liquid; or the bag inflates.
- P4 [major · process_direction]
  - expect: The stream continues and does not flow back.
  - fail: Sand flows back in; or stops while the bag is still full; or the cone shrinks.
- P5 [fatal · permanence_count]
  - expect: One bag keeps its number.
  - fail: It duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The bag and the wall stay the same.
  - fail: The bag changes colour; or the wall changes; or the background rearranges.

## MECH-0285 · granular · eval

**Caption.** A sack of potatoes is tipped out onto a barn floor, and the potatoes tumble out and roll apart into a loose spread.

**Expectation (hidden).** The potatoes fall and roll away from the pile, coming to rest scattered; they do not stack or stay in the sack's shape.

**Declared violation types.** material_response, trajectory_momentum

**SA**
- S1 [core] A sack of potatoes is tipped out onto a barn floor.
- S2 [core] The potatoes tumble out.
- S3 [core] They roll apart into a loose spread.
- S4 [minor] The tip comes first and the spread follows.

**PC**
- P1 [core · trajectory_momentum]
  - expect: They fall and roll away from the pile and come to rest scattered.
  - fail: They roll back in; or move as a block; or roll uphill.
- P2 [core · material_response]
  - expect: The potatoes are firm and roll and bump, not stacking or holding the sack's shape.
  - fail: They hold the sack's shape; or stack; or squash.
- P3 [major · gravity_direction]
  - expect: They fall to the floor.
  - fail: They float; or rise; or hang.
- P4 [major · causeless_motion]
  - expect: They come to rest and stay.
  - fail: They restart; or speed up; or jump.
- P5 [fatal · permanence_count]
  - expect: The potatoes keep their number.
  - fail: Potatoes multiply; or vanish; or turn into other objects.
- P6 [minor · attribute_drift]
  - expect: The sack and the barn stay the same.
  - fail: The sack changes colour; or the barn rearranges; or the potatoes change colour.

## MECH-0286 · gas_wind · eval

**Caption.** A model rocket reaches the top of its flight, its nose pops off and a parachute unfolds, and the rocket drifts slowly down under the canopy.

**Expectation (hidden).** The canopy fills and rounds out above the rocket, whose fall slows sharply the moment it opens; the rocket hangs below the canopy and drifts with the wind; it does not keep falling fast or rise.

**Declared violation types.** missing_consequence, gravity_direction

**SA**
- S1 [core] A model rocket reaches the top of its flight.
- S2 [core] Its nose pops off.
- S3 [core] A parachute unfolds.
- S4 [core] The rocket drifts slowly down under the canopy.
- S5 [minor] The nose comes off first, then the canopy opens, then the drift down.

**PC**
- P1 [core · missing_consequence]
  - expect: The canopy fills above the rocket and the fall slows sharply the moment it opens.
  - fail: The rocket keeps falling fast with the canopy open; or slows before the canopy; or the canopy opens below the rocket.
- P2 [core · gravity_direction]
  - expect: The rocket hangs below the canopy and descends, not rising.
  - fail: It rises; or hovers indefinitely; or the rocket is above the canopy.
- P3 [major · trajectory_momentum]
  - expect: It drifts with the wind.
  - fail: It drifts against visible wind; or straight down with visible wind; or jinks.
- P4 [major · material_response]
  - expect: The canopy is cloth that fills and billows, and the cords are taut.
  - fail: It is a rigid dome; or the cords are slack while hanging; or the canopy shreds.
- P5 [fatal · permanence_count]
  - expect: One rocket and one parachute keep their number.
  - fail: The rocket duplicates; or vanishes; or the parachute turns into another object.
- P6 [minor · attribute_drift]
  - expect: The rocket's colours and the sky stay the same.
  - fail: The rocket changes colour; or the canopy changes; or the field rearranges.

## MECH-0287 · gas_wind · eval

**Caption.** The sail of a small boat is let loose in a breeze, and it fills and bellies out to one side.

**Expectation (hidden).** The sail bulges away from the wind and flaps when the wind drops; it does not belly toward the wind.

**Declared violation types.** causeless_motion, material_response

**SA**
- S1 [core] The sail of a small boat is let loose.
- S2 [core] It fills.
- S3 [core] It bellies out to one side.
- S4 [minor] A breeze is visible in other signs.
- S5 [minor] The release comes first and the filling follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The sail bulges away from the wind and flaps when the wind drops.
  - fail: It bellies toward the wind; or fills in still air; or stays limp in wind.
- P2 [core · material_response]
  - expect: The cloth fills smoothly and flaps at the edges.
  - fail: It is rigid; or stretches; or tears.
- P3 [major · trajectory_momentum]
  - expect: It bellies to the same side as other wind signs.
  - fail: It bellies opposite; or flips randomly; or spins.
- P4 [major · gravity_direction]
  - expect: The sail hangs from the mast when slack.
  - fail: It floats; or rises; or hangs sideways with no wind.
- P5 [fatal · permanence_count]
  - expect: One sail and one boat keep their number.
  - fail: The sail duplicates; or vanishes; or the boat turns into another object.
- P6 [minor · attribute_drift]
  - expect: The sail's colour and the water stay the same.
  - fail: The sail changes colour; or the boat changes; or the water changes.

## MECH-0288 · gas_wind · eval

**Caption.** A gust of wind reaches a row of wind turbines on a hill, and the blades start turning and speed up.

**Expectation (hidden).** The blades begin turning only when the wind arrives and slow when it drops; all turbines turn the same way.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A row of wind turbines stands on a hill.
- S2 [core] A gust of wind reaches them.
- S3 [core] The blades start turning.
- S4 [core] They speed up.
- S5 [minor] The gust comes first and the turning follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The blades begin turning only when the wind arrives and slow when it drops.
  - fail: They turn in still air; or the wind arrives and they stay still; or they keep speeding up after the wind drops.
- P2 [core · process_direction]
  - expect: The speed builds steadily.
  - fail: They reach full speed instantly; or reverse; or jerk.
- P3 [major · trajectory_momentum]
  - expect: All the turbines turn the same way.
  - fail: They turn in opposite directions; or one stays still while the others spin in the same wind; or they turn erratically.
- P4 [major · material_response]
  - expect: The blades are rigid.
  - fail: They bend like cloth; or detach; or stretch.
- P5 [fatal · permanence_count]
  - expect: The turbines keep their number.
  - fail: A turbine vanishes; or appears; or a blade vanishes.
- P6 [minor · attribute_drift]
  - expect: The turbines and the hill stay the same.
  - fail: The turbines change colour; or the hill rearranges; or the sky changes.

## MECH-0289 · biomechanics · eval

**Caption.** A gymnast performs a cartwheel across a mat, hands then feet touching the ground in turn.

**Expectation (hidden).** Her hands and feet touch the mat one after another in sequence, her body stays whole and bends only at the joints, and she lands upright.

**Declared violation types.** shape_identity, gravity_direction

**SA**
- S1 [core] A gymnast performs a cartwheel across a mat.
- S2 [core] Hands then feet touch the ground in turn.
- S3 [core] She lands upright.
- S4 [minor] The hands touch first, then the feet.

**PC**
- P1 [core · shape_identity]
  - expect: Her hands and feet touch the mat one after another in sequence, her body stays whole, and she bends only at the joints.
  - fail: A limb detaches; or a limb bends mid-bone; or hands and feet are all down at once mid-wheel.
- P2 [core · gravity_direction]
  - expect: She stays in contact through hands or feet and lands upright.
  - fail: She floats; or hovers upside down; or sinks.
- P3 [major · solidity]
  - expect: Her hands and feet land on the mat, not in it.
  - fail: They sink; or pass through; or the mat passes through her.
- P4 [major · trajectory_momentum]
  - expect: She travels sideways across the mat.
  - fail: She jumps position; or ends where she started; or reverses mid-wheel.
- P5 [fatal · shape_identity]
  - expect: Her limbs keep their number and stay attached.
  - fail: A limb vanishes; or a second figure appears; or she merges with the mat.
- P6 [minor · attribute_drift]
  - expect: Her leotard and the mat stay the same.
  - fail: The leotard changes colour; or the mat changes; or the gym rearranges.

**Note.** Biomechanics scene: the body is the physics. Form, posture and skill are not judged; only that limbs stay attached, bend at joints, keep ground contact and pass through nothing.

## MECH-0290 · biomechanics · eval

**Caption.** A person walking along a pavement catches a foot on a raised kerb, stumbles forward with arms flung out, and recovers balance after two quick steps.

**Expectation (hidden).** The stumble begins at the trip, the body pitches forward and the arms come up; the recovery steps are quick and in the direction of travel; the person does not fall backward or freeze mid-fall.

**Declared violation types.** trajectory_momentum, causeless_motion

**SA**
- S1 [core] A person walks along a pavement.
- S2 [core] A foot catches on a raised kerb.
- S3 [core] They stumble forward with arms flung out.
- S4 [core] They recover balance after quick steps.
- S5 [minor] The trip comes first, then the stumble, then the recovery.

**PC**
- P1 [core · causeless_motion]
  - expect: The stumble begins at the trip.
  - fail: It begins before; or with no kerb contact; or on flat pavement away from the kerb.
- P2 [core · trajectory_momentum]
  - expect: The body pitches forward and the recovery steps are in the direction of travel.
  - fail: They fall backward; or freeze mid-fall; or step sideways.
- P3 [major · gravity_direction]
  - expect: They stay on their feet and end upright.
  - fail: They float; or hover leaning; or sink.
- P4 [major · shape_identity]
  - expect: The arms come up at the joints.
  - fail: They detach; or bend mid-bone; or the body folds mid-torso.
- P5 [fatal · shape_identity]
  - expect: Their limbs keep their number and stay attached.
  - fail: A limb vanishes; or a second figure appears; or they merge with the kerb.
- P6 [minor · attribute_drift]
  - expect: Their clothing and the pavement stay the same.
  - fail: The clothing changes colour; or the kerb moves; or the street rearranges.

**Note.** Biomechanics scene: the body is the physics. Form, posture and skill are not judged; only that limbs stay attached, bend at joints, keep ground contact and pass through nothing.

## MECH-0291 · biomechanics · eval

**Caption.** A person carries a full bucket of water in one hand and leans the body to the other side to balance the load.

**Expectation (hidden).** The lean is away from the bucket and appears as soon as the bucket is lifted; the free arm may swing out; the person does not lean toward the bucket or walk upright as if it weighed nothing.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] A person carries a full bucket of water in one hand.
- S2 [core] They lean their body to the other side.
- S3 [minor] The bucket is full.

**PC**
- P1 [core · gravity_direction]
  - expect: The lean is away from the bucket and appears as soon as it is lifted.
  - fail: They lean toward the bucket; or walk upright as if it weighed nothing; or lean before lifting it.
- P2 [core · missing_consequence]
  - expect: The bucket's weight shows: the arm is straight and the shoulder drops.
  - fail: The arm is bent casually; or the bucket floats; or the bucket swings up.
- P3 [major · material_response]
  - expect: The water level in the bucket stays flat, sloshing a little.
  - fail: It is rigid; or spills upward; or tilts steeply.
- P4 [major · shape_identity]
  - expect: The body bends at the joints.
  - fail: It folds mid-torso; or a limb detaches; or the arm stretches.
- P5 [fatal · shape_identity]
  - expect: Their limbs keep their number, and one bucket stays one bucket.
  - fail: A limb vanishes; or the bucket duplicates; or they merge with the bucket.
- P6 [minor · attribute_drift]
  - expect: Their clothing and the bucket stay the same.
  - fail: The clothing changes colour; or the bucket changes; or the background rearranges.

**Note.** Biomechanics scene: the body is the physics. Form, posture and skill are not judged; only that limbs stay attached, bend at joints, keep ground contact and pass through nothing.

## MECH-0292 · biomechanics · eval

**Caption.** A person standing on one leg wobbles, sways further, and puts the other foot down to stay upright.

**Expectation (hidden).** The sway grows before the foot comes down and stops after it lands; the foot lands on the side the body was leaning toward; the person does not stay perfectly still or fall over.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A person stands on one leg.
- S2 [core] They wobble and sway further.
- S3 [core] They put the other foot down.
- S4 [minor] The sway comes first and the foot comes down after.

**PC**
- P1 [core · gravity_direction]
  - expect: The sway grows before the foot comes down, and the foot lands on the side the body was leaning toward.
  - fail: The foot lands on the other side; or they fall over; or they stay perfectly still.
- P2 [core · causeless_motion]
  - expect: The sway stops after the foot lands.
  - fail: They keep swaying after; or the sway stops before the foot is down; or they jump.
- P3 [major · solidity]
  - expect: The foot lands on the ground.
  - fail: It sinks; or hovers above the ground while they steady; or passes through.
- P4 [major · shape_identity]
  - expect: The body bends at the joints.
  - fail: It folds mid-bone; or a limb detaches; or a leg stretches.
- P5 [fatal · shape_identity]
  - expect: Their limbs keep their number and stay attached.
  - fail: A limb vanishes; or a third leg appears; or a second figure appears.
- P6 [minor · attribute_drift]
  - expect: Their clothing and the floor stay the same.
  - fail: The clothing changes colour; or the floor changes; or the room rearranges.

**Note.** Biomechanics scene: the body is the physics. Form, posture and skill are not judged; only that limbs stay attached, bend at joints, keep ground contact and pass through nothing.

## MECH-0293 · soft_material · eval

**Caption.** A silk scarf draped over the back of a chair slides off and pools in soft folds on the floor.

**Expectation (hidden).** The scarf slips down following the chair's shape, falls as a limp sheet, and lands in loose folds; it does not stay rigid, float, or land flat as a square.

**Declared violation types.** material_response, gravity_direction

**SA**
- S1 [core] A silk scarf is draped over the back of a chair.
- S2 [core] It slides off.
- S3 [core] It pools in soft folds on the floor.
- S4 [minor] The slide comes first and the pooling follows.

**PC**
- P1 [core · gravity_direction]
  - expect: It slips down following the chair's shape, falls, and lands.
  - fail: It floats; or rises; or stays in the air.
- P2 [core · material_response]
  - expect: It falls as a limp sheet and lands in loose folds.
  - fail: It is rigid; or lands flat as a square; or tears.
- P3 [major · process_direction]
  - expect: It settles and stays.
  - fail: It rises again; or slides on; or re-drapes itself.
- P4 [major · solidity]
  - expect: It lies on the floor, not through it.
  - fail: It passes through the floor; or through the chair; or the chair passes through it.
- P5 [fatal · permanence_count]
  - expect: One scarf keeps its number.
  - fail: It duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The scarf's colour and the chair stay the same.
  - fail: The scarf changes colour; or the chair changes; or the room rearranges.

## MECH-0294 · soft_material · eval

**Caption.** A sock is pulled over a foot, the opening stretching as the fabric is drawn up over the heel and ankle.

**Expectation (hidden).** The sock stretches around the foot and follows its shape; the foot goes into the opening, not through the fabric.

**Declared violation types.** shape_identity, solidity

**SA**
- S1 [core] A sock is pulled over a foot.
- S2 [core] The opening stretches.
- S3 [core] The fabric is drawn up over the heel and ankle.
- S4 [minor] The opening stretches first and the fabric is drawn up after.

**PC**
- P1 [core · solidity]
  - expect: The foot goes into the opening, not through the fabric.
  - fail: It goes through the fabric; or the sock passes through the foot; or the hands pass through.
- P2 [core · shape_identity]
  - expect: The sock stretches around the foot and follows its shape.
  - fail: It does not stretch; or grows huge; or the foot changes shape.
- P3 [major · material_response]
  - expect: The knit stretches and recovers.
  - fail: It is rigid; or tears; or melts.
- P4 [major · causeless_motion]
  - expect: It moves only as it is pulled.
  - fail: It climbs by itself; or slides off; or jumps.
- P5 [fatal · shape_identity]
  - expect: One sock and one foot keep their number.
  - fail: The sock duplicates; or the foot detaches; or they merge.
- P6 [minor · attribute_drift]
  - expect: The sock's colour and the background stay the same.
  - fail: The sock changes colour; or the foot changes; or the background rearranges.

## MECH-0295 · soft_material · eval

**Caption.** A wet paper towel is laid over the top of an upright bottle, and it drapes and clings to the bottle's shape.

**Expectation (hidden).** The towel folds down over the bottle's shoulders and hangs along its sides, showing the shape beneath; it does not stay flat like a lid or slide off.

**Declared violation types.** material_response, shape_identity

**SA**
- S1 [core] A wet paper towel is laid over the top of an upright bottle.
- S2 [core] It drapes down.
- S3 [core] It clings to the bottle's shape.
- S4 [minor] The towel is wet.

**PC**
- P1 [core · material_response]
  - expect: It folds over the shoulders and hangs along the sides, clinging.
  - fail: It stays flat like a lid; or slides off; or is rigid.
- P2 [core · shape_identity]
  - expect: It shows the shape beneath and keeps its own size.
  - fail: The bottle's shape changes; or the towel grows; or it shrinks.
- P3 [major · gravity_direction]
  - expect: It hangs down.
  - fail: It rises; or floats; or stands out sideways.
- P4 [major · solidity]
  - expect: It lies on the bottle, not through it.
  - fail: It passes through; or the bottle passes through it; or the hands pass through.
- P5 [fatal · permanence_count]
  - expect: One towel and one bottle keep their number.
  - fail: The towel duplicates; or the bottle vanishes; or the towel turns into another object.
- P6 [minor · attribute_drift]
  - expect: The towel and the bottle stay the same.
  - fail: The towel changes colour; or the bottle changes; or the background rearranges.

## MECH-0296 · soft_material · eval

**Caption.** A coil of rope is thrown onto a dock, and it lands in a loose tangle of loops.

**Expectation (hidden).** The rope bends into loops that lie on top of one another; it does not pass through itself or land in a straight line.

**Declared violation types.** shape_identity, solidity

**SA**
- S1 [core] A coil of rope is thrown onto a dock.
- S2 [core] It lands.
- S3 [core] It lies in a loose tangle of loops.
- S4 [minor] The throw comes first and the landing follows.

**PC**
- P1 [core · solidity]
  - expect: The loops lie on top of one another and the rope does not pass through itself.
  - fail: It passes through itself; or through the dock; or the loops run into one another.
- P2 [core · shape_identity]
  - expect: It bends into loops and keeps its length.
  - fail: It lands in a straight line; or stretches; or splits.
- P3 [major · gravity_direction]
  - expect: It falls and lies on the dock.
  - fail: It floats; or rises; or hangs.
- P4 [major · material_response]
  - expect: The flexible rope flops.
  - fail: It is rigid; or bounces high; or melts.
- P5 [fatal · permanence_count]
  - expect: One rope keeps its number and its two ends.
  - fail: It duplicates; or vanishes; or the ends multiply.
- P6 [minor · attribute_drift]
  - expect: The rope's colour and the dock stay the same.
  - fail: The rope changes colour; or the dock changes; or the water rearranges.

## MECH-0297 · occlusion_containment · eval

**Caption.** A coin is pushed under the edge of a rug, and when the rug is lifted the coin lies where it was pushed.

**Expectation (hidden).** A small bump shows in the rug where the coin is; the coin is hidden while covered and is the same coin, in that spot, when the rug is lifted.

**Declared violation types.** permanence_count, solidity

**SA**
- S1 [core] A coin is pushed under the edge of a rug.
- S2 [core] The rug is lifted.
- S3 [core] The coin lies where it was pushed.
- S4 [minor] The push comes first, then the lift, then the coin is seen.

**PC**
- P1 [core · permanence_count]
  - expect: The coin is hidden while covered and is the same coin, in that spot, when the rug is lifted.
  - fail: It is gone; or a different coin; or it is elsewhere.
- P2 [core · solidity]
  - expect: The coin is not visible through the rug.
  - fail: It shows through the rug; or passes through the rug; or the rug passes through the coin.
- P3 [major · causeless_motion]
  - expect: The coin moves only when pushed.
  - fail: It slides alone; or jumps; or moves under the rug by itself.
- P4 [major · gravity_direction]
  - expect: The coin lies flat on the floor.
  - fail: It floats; or stands on edge; or rises into the rug.
- P5 [fatal · permanence_count]
  - expect: One coin and one rug keep their number.
  - fail: The coin duplicates; or the rug vanishes; or the coin turns into another object.
- P6 [minor · attribute_drift]
  - expect: The rug's pattern and the floor stay the same.
  - fail: The pattern changes; or the floor changes; or the room rearranges.

## MECH-0298 · occlusion_containment · eval

**Caption.** A bus drives behind a tall building and emerges from the other side a moment later.

**Expectation (hidden).** The bus is hidden for a time matching its speed and the building's width, and reappears at the same speed and heading; it does not show through the building.

**Declared violation types.** permanence_count, trajectory_momentum

**SA**
- S1 [core] A bus drives along a street.
- S2 [core] It passes behind a tall building.
- S3 [core] It emerges from the other side.
- S4 [minor] The disappearance comes first and the emergence follows.

**PC**
- P1 [core · permanence_count]
  - expect: It is the same bus, and it does not show through the building.
  - fail: A different bus emerges; or two buses; or the bus appears elsewhere.
- P2 [core · trajectory_momentum]
  - expect: It is hidden for a time matching its speed and the building's width and reappears at the same speed and heading.
  - fail: It emerges instantly; or after far too long; or emerges going back.
- P3 [major · solidity]
  - expect: The bus is not visible through the building.
  - fail: It shows through; or passes through the building; or the building passes through the bus.
- P4 [major · causeless_motion]
  - expect: The building stays still.
  - fail: It moves; or vanishes; or the street changes.
- P5 [fatal · shape_identity]
  - expect: One bus and one building keep their shape.
  - fail: The bus turns into another vehicle; or the building changes shape; or the bus merges with it.
- P6 [minor · attribute_drift]
  - expect: The bus's colours and the street stay the same.
  - fail: The bus changes colour; or the building changes; or the street rearranges.

## MECH-0299 · occlusion_containment · eval

**Caption.** A marble is dropped into the top of a long cardboard tube standing upright, and it comes out of the bottom and rolls away.

**Expectation (hidden).** The marble is hidden inside the tube and exits at the bottom after a short delay; the same marble comes out, and nothing exits before it enters.

**Declared violation types.** permanence_count, gravity_direction

**SA**
- S1 [core] A long cardboard tube stands upright.
- S2 [core] A marble is dropped into the top.
- S3 [core] It comes out of the bottom.
- S4 [core] It rolls away.
- S5 [minor] The drop comes first, then the exit, then the roll.

**PC**
- P1 [core · permanence_count]
  - expect: The same marble comes out, and nothing exits before it enters.
  - fail: A different marble exits; or two marbles; or one exits before one has entered.
- P2 [core · gravity_direction]
  - expect: It falls through and exits the bottom after a short delay.
  - fail: It exits the top; or hangs inside; or rises.
- P3 [major · solidity]
  - expect: It is hidden inside and does not show through the wall.
  - fail: It shows through; or passes through the wall; or the tube passes through it.
- P4 [major · causeless_motion]
  - expect: It rolls away and slows.
  - fail: It curves; or speeds up; or restarts.
- P5 [fatal · shape_identity]
  - expect: One marble and one tube keep their shape.
  - fail: The marble turns into another object; or the tube changes shape; or they merge.
- P6 [minor · attribute_drift]
  - expect: The marble's colour and the tube stay the same.
  - fail: The marble changes colour; or the tube changes; or the background rearranges.

## MECH-0300 · occlusion_containment · eval

**Caption.** A cat crawls under a blanket on a bed, and a moving lump travels across the blanket to the far edge, where the cat comes out.

**Expectation (hidden).** The lump is the cat's size and moves continuously; the cat is not visible through the blanket and emerges only at the edge.

**Declared violation types.** permanence_count, solidity

**SA**
- S1 [core] A cat crawls under a blanket on a bed.
- S2 [core] A moving lump travels across the blanket.
- S3 [core] The cat comes out at the far edge.
- S4 [minor] The crawl in comes first, then the lump, then the emergence.

**PC**
- P1 [core · permanence_count]
  - expect: The cat emerges only at the edge, and it is the same cat.
  - fail: It appears elsewhere; or two cats; or it vanishes for good.
- P2 [core · solidity]
  - expect: The cat is not visible through the blanket and the lump is its size.
  - fail: It shows through; or passes through the top of the blanket; or the lump is the wrong size.
- P3 [major · trajectory_momentum]
  - expect: The lump moves continuously.
  - fail: It jumps; or splits; or the lump keeps moving while the cat is out.
- P4 [major · material_response]
  - expect: The blanket drapes over the lump.
  - fail: It is rigid; or stretches; or tears.
- P5 [fatal · shape_identity]
  - expect: One cat stays one cat.
  - fail: It splits; or merges with the blanket; or turns into another animal.
- P6 [minor · attribute_drift]
  - expect: The blanket's pattern and the bed stay the same.
  - fail: The pattern changes; or the bed changes; or the room rearranges.

**Note.** The cat is self-driven: its path under the blanket is its own. Only containment and the lump are judged.

## MECH-0301 · inertia · eval

**Caption.** A train pulls out of a station, and a suitcase standing loose in the aisle tips over toward the rear of the carriage.

**Expectation (hidden).** The suitcase begins to tip as the train starts moving, falls toward the back of the carriage, and lies still once down; it does not tip before the train moves or fall toward the front.

**Declared violation types.** trajectory_momentum, causeless_motion

**SA**
- S1 [core] A suitcase stands loose in the aisle of a train carriage.
- S2 [core] The train pulls out of the station.
- S3 [core] The suitcase tips over toward the rear of the carriage.
- S4 [minor] The train moves first and the tip follows.

**PC**
- P1 [core · causeless_motion]
  - expect: It begins to tip as the train starts, not before, and lies still once down.
  - fail: It tips before the train moves; or tips with no motion; or rights itself and tips again.
- P2 [core · trajectory_momentum]
  - expect: It falls toward the back of the carriage.
  - fail: It falls toward the front; or sideways; or up.
- P3 [major · gravity_direction]
  - expect: It falls to the floor and stays.
  - fail: It hangs; or rights itself; or floats.
- P4 [major · material_response]
  - expect: The case is rigid and thuds.
  - fail: It folds; or bounces high; or melts.
- P5 [fatal · permanence_count]
  - expect: One suitcase keeps its number.
  - fail: It duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The suitcase and the carriage stay the same.
  - fail: The case changes colour; or the seats change; or the view outside jumps.

## MECH-0302 · inertia · eval

**Caption.** A tablecloth is pulled sharply out from under a set of plates and glasses, and the dishes stay almost where they were on the bare table.

**Expectation (hidden).** The cloth leaves the table in one quick motion while the dishes shift only slightly and settle; they do not fly off with the cloth, rise, or move before the cloth is pulled.

**Declared violation types.** trajectory_momentum, permanence_count

**SA**
- S1 [core] Plates and glasses stand on a tablecloth.
- S2 [core] The cloth is pulled sharply out from under them.
- S3 [core] The dishes stay almost where they were on the bare table.
- S4 [minor] The pull comes first and the dishes settle after.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The cloth leaves in one quick motion while the dishes shift only slightly and settle.
  - fail: The dishes fly off with the cloth; or rise; or slide far across the table.
- P2 [core · permanence_count]
  - expect: All the dishes remain on the table with the same count.
  - fail: A dish vanishes; or appears; or a dish is found under the cloth.
- P3 [major · causeless_motion]
  - expect: The dishes do not move before the pull.
  - fail: They move before; or move after settling; or jump.
- P4 [major · material_response]
  - expect: The cloth flows out flat and the dishes are rigid.
  - fail: The cloth is rigid; or the dishes bend; or the cloth tears.
- P5 [fatal · shape_identity]
  - expect: The dishes keep their shape and the table stays one table.
  - fail: A dish turns into another object; or the table duplicates; or dishes merge.
- P6 [minor · attribute_drift]
  - expect: The dishes and the room stay the same.
  - fail: The dishes change pattern; or the table changes; or the room rearranges.

**Note.** The hands pulling are kept as the minimal trigger; the person is not judged.

## MECH-0303 · gravity_fall · eval

**Caption.** A ripe apple comes loose from a branch and drops through the leaves to the grass beneath the tree.

**Expectation (hidden).** The apple falls straight down, speeding up as it goes, brushes through leaves without stopping, and comes to rest on the grass below the branch; it does not drift sideways, pause, or rise.

**Declared violation types.** gravity_direction, trajectory_momentum

**SA**
- S1 [core] An apple hangs from a branch.
- S2 [core] It comes loose.
- S3 [core] It drops through the leaves.
- S4 [core] It lands on the grass beneath.
- S5 [minor] The loosening comes first, then the drop, then the landing.

**PC**
- P1 [core · gravity_direction]
  - expect: It falls straight down, speeding up, and comes to rest below the branch.
  - fail: It drifts sideways; or pauses; or rises.
- P2 [core · trajectory_momentum]
  - expect: It brushes through the leaves without stopping.
  - fail: It stops in the leaves; or bounces up high; or reverses.
- P3 [major · missing_consequence]
  - expect: The leaves stir as it passes.
  - fail: They stay rigid; or stir before; or the apple passes through them untouched.
- P4 [major · material_response]
  - expect: The apple is firm and may bounce low.
  - fail: It splashes; or bounces high; or floats.
- P5 [fatal · permanence_count]
  - expect: One apple keeps its number.
  - fail: It duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The apple's colour and the tree stay the same.
  - fail: The apple changes colour; or the tree rearranges; or the grass changes.

## MECH-0304 · gravity_fall · eval

**Caption.** A drone hovering over a field loses power, and it drops straight down into the grass.

**Expectation (hidden).** The drone starts falling the moment its rotors stop, accelerates downward, and lands below where it hovered; it does not glide away, slow before landing, or stay in the air with the rotors still.

**Declared violation types.** gravity_direction, causeless_motion

**SA**
- S1 [core] A drone hovers over a field.
- S2 [core] It loses power and its rotors stop.
- S3 [core] It drops straight down into the grass.
- S4 [minor] The rotors stop first and the drop follows.

**PC**
- P1 [core · causeless_motion]
  - expect: It falls the moment the rotors stop and not before.
  - fail: It falls with the rotors spinning; or stays up with the rotors still; or rises.
- P2 [core · gravity_direction]
  - expect: It accelerates downward and lands below where it hovered.
  - fail: It glides away; or slows before landing; or hovers.
- P3 [major · trajectory_momentum]
  - expect: It goes straight down with no gliding.
  - fail: It goes sideways; or curves; or spins away.
- P4 [major · material_response]
  - expect: It is rigid and may break on landing.
  - fail: It bounces high; or melts; or floats.
- P5 [fatal · permanence_count]
  - expect: One drone keeps its number.
  - fail: It duplicates; or vanishes in the air; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The drone and the field stay the same.
  - fail: The drone changes colour; or the field rearranges; or the sky changes.

## MECH-0305 · collision · eval

**Caption.** A wrecking ball swings into a brick wall, and bricks burst out of the far side as the ball is stopped and swings back.

**Expectation (hidden).** The bricks move only at the moment of impact and fly away from the ball; the ball loses most of its speed at the wall and swings back less far than it came; the ball does not pass through the wall or stop before touching it.

**Declared violation types.** solidity, trajectory_momentum

**SA**
- S1 [core] A wrecking ball swings into a brick wall.
- S2 [core] Bricks burst out of the far side.
- S3 [core] The ball is stopped.
- S4 [core] It swings back.
- S5 [minor] The impact comes first, then the bricks fly, then the swing back.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The bricks move only at impact and fly away from the ball, and the ball loses most of its speed and swings back less far than it came.
  - fail: Bricks move before the impact; or the ball keeps its speed; or it swings back further than it came.
- P2 [core · solidity]
  - expect: The ball does not pass through the wall and stops at contact.
  - fail: It passes through; or stops before touching; or the wall passes through the ball.
- P3 [major · gravity_direction]
  - expect: The bricks fall to the ground.
  - fail: They hang; or rise; or float.
- P4 [major · material_response]
  - expect: The bricks break and scatter and the ball stays rigid.
  - fail: The wall bends like rubber; or the ball squashes; or the bricks melt.
- P5 [fatal · permanence_count]
  - expect: One ball keeps its number, and the bricks are the wall's.
  - fail: The ball duplicates; or bricks appear from nowhere; or the wall is whole again.
- P6 [minor · attribute_drift]
  - expect: The ball and the site stay the same.
  - fail: The ball changes colour; or the wall's bricks change colour; or the site rearranges.

## MECH-0306 · friction_rolling · eval

**Caption.** A car brakes hard on a dry road, its tyres screech and leave dark skid marks, and it stops within a short distance.

**Expectation (hidden).** The marks appear behind the tyres only while the car is braking and stay on the road after it stops; the car slows quickly and comes to rest, not sliding on as it would on ice.

**Declared violation types.** trajectory_momentum, missing_consequence

**SA**
- S1 [core] A car brakes hard on a dry road.
- S2 [core] Dark skid marks appear behind the tyres.
- S3 [core] It stops within a short distance.
- S4 [minor] The road is dry.
- S5 [minor] The braking comes first and the marks and stop follow.

**PC**
- P1 [core · missing_consequence]
  - expect: The marks appear behind the tyres only while braking and stay after.
  - fail: Marks appear ahead of the tyres; or before braking; or they vanish.
- P2 [core · trajectory_momentum]
  - expect: The car slows quickly and comes to rest on a straight line.
  - fail: It slides on as if on ice; or swerves; or speeds up.
- P3 [major · causeless_motion]
  - expect: It stays stopped.
  - fail: It restarts; or rolls back; or jumps.
- P4 [major · material_response]
  - expect: The tyres may smoke and the car's nose dips.
  - fail: The tyres deform hugely; or the car flips; or the body bends.
- P5 [fatal · permanence_count]
  - expect: One car keeps its number.
  - fail: It duplicates; or vanishes; or turns into another vehicle.
- P6 [minor · attribute_drift]
  - expect: The car's colour and the road stay the same.
  - fail: The car changes colour; or the road markings shift; or the surroundings rearrange.

## MECH-0307 · friction_rolling · eval

**Caption.** A wooden crate rests on a board that is slowly tilted up at one end; the crate stays put as the slope grows, then suddenly slides down to the bottom.

**Expectation (hidden).** The crate does not move at shallow angles, starts sliding all at once when the slope is steep, and speeds up on the way down; it does not creep at every angle or slide uphill.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A wooden crate rests on a board.
- S2 [core] The board is slowly tilted up at one end.
- S3 [core] The crate stays put as the slope grows.
- S4 [core] It suddenly slides down to the bottom.
- S5 [minor] The tilt comes first, then the wait, then the slide.

**PC**
- P1 [core · causeless_motion]
  - expect: It does not move at shallow angles and starts sliding all at once when the slope is steep.
  - fail: It creeps at every angle; or slides on a level board; or slides uphill.
- P2 [core · gravity_direction]
  - expect: It speeds up on the way down and stops at the bottom.
  - fail: It slows on the way down; or stops mid-slope; or floats.
- P3 [major · trajectory_momentum]
  - expect: It slides straight down the board.
  - fail: It goes sideways; or spins; or goes off the side.
- P4 [major · material_response]
  - expect: The crate and the board stay rigid.
  - fail: The crate bends; or the board sags; or the crate squashes.
- P5 [fatal · permanence_count]
  - expect: One crate and one board keep their number.
  - fail: The crate duplicates; or vanishes; or the board turns into another object.
- P6 [minor · attribute_drift]
  - expect: The crate and the board stay the same.
  - fail: The crate changes colour; or the board changes; or the background rearranges.

## MECH-0308 · projectile · eval

**Caption.** A pumpkin is launched from a catapult on a field, arcs high over the grass, and smashes on the ground far away.

**Expectation (hidden).** The pumpkin rises, slows near the top of its arc, and falls faster toward the ground; it breaks apart only when it lands and does not hover, change direction in the air, or bounce whole.

**Declared violation types.** trajectory_momentum, material_response

**SA**
- S1 [core] A pumpkin is launched from a catapult.
- S2 [core] It arcs high over the grass.
- S3 [core] It smashes on the ground far away.
- S4 [minor] The launch comes first, then the arc, then the smash.

**PC**
- P1 [core · trajectory_momentum]
  - expect: It rises, slows near the top of its arc, and falls faster toward the ground.
  - fail: It flies flat; or hovers; or changes direction in the air.
- P2 [core · material_response]
  - expect: It breaks apart only when it lands, not in the air, and does not bounce whole.
  - fail: It breaks in the air; or bounces whole; or squashes and stays.
- P3 [major · gravity_direction]
  - expect: The pieces fall and scatter low.
  - fail: They rise; or hang; or float.
- P4 [major · causeless_motion]
  - expect: The catapult arm swings and then stops.
  - fail: The pumpkin leaves before the arm moves; or the arm passes through the pumpkin; or the arm keeps swinging round.
- P5 [fatal · permanence_count]
  - expect: One pumpkin becomes its pieces.
  - fail: It duplicates in flight; or vanishes; or is whole again.
- P6 [minor · attribute_drift]
  - expect: The catapult and the field stay the same.
  - fail: The catapult changes; or the field rearranges; or the pumpkin changes colour in flight.

## MECH-0309 · projectile · eval

**Caption.** A ping-pong ball is served, arcs over the net, bounces once on the far side of the table, and drops off the end.

**Expectation (hidden).** The ball follows a smooth arc, bounces lower than its flight height, and falls off the table edge under gravity; it does not pass through the net, hover, or bounce higher than it came.

**Declared violation types.** trajectory_momentum, solidity

**SA**
- S1 [core] A ping-pong ball is served.
- S2 [core] It arcs over the net.
- S3 [core] It bounces once on the far side of the table.
- S4 [core] It drops off the end of the table.
- S5 [minor] The serve comes first, then the net, then the bounce, then the drop.

**PC**
- P1 [core · trajectory_momentum]
  - expect: It follows a smooth arc, bounces lower than its flight, and falls off the edge.
  - fail: It bounces higher than it came; or hovers; or changes direction in the air.
- P2 [core · solidity]
  - expect: It goes over the net, not through it.
  - fail: It passes through the net; or through the table; or the table passes through it.
- P3 [major · gravity_direction]
  - expect: It falls after the peak and off the edge.
  - fail: It rises; or hangs; or floats.
- P4 [major · material_response]
  - expect: The light ball bounces crisply.
  - fail: It stays flat; or sticks; or melts.
- P5 [fatal · permanence_count]
  - expect: One ball keeps its number.
  - fail: It duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The ball and the table stay the same.
  - fail: The ball changes colour; or the net changes; or the table rearranges.

## MECH-0310 · balance_topple · eval

**Caption.** A broom is stood upright on the end of its handle in the middle of a kitchen floor and let go; it stays for a moment, leans more and more, and falls to the floor.

**Expectation (hidden).** The lean grows steadily faster once it starts and the broom falls in the direction it leaned; it does not stand indefinitely, right itself, or fall before it begins to lean.

**Declared violation types.** gravity_direction, causeless_motion

**SA**
- S1 [core] A broom is stood upright on the end of its handle on a kitchen floor.
- S2 [core] It is let go.
- S3 [core] It stays for a moment.
- S4 [core] It leans more and more.
- S5 [core] It falls to the floor.
- S6 [minor] The release comes first, then the lean, then the fall.

**PC**
- P1 [core · gravity_direction]
  - expect: The lean grows faster once it starts and the broom falls in the direction it leaned.
  - fail: It stands indefinitely; or rights itself; or falls opposite to its lean.
- P2 [core · causeless_motion]
  - expect: Nothing pushes it, and it falls only after leaning.
  - fail: It falls before leaning; or is pushed; or slides across the floor.
- P3 [major · trajectory_momentum]
  - expect: It pivots about the end of the handle.
  - fail: The handle end slides far; or it floats up; or it spins.
- P4 [major · material_response]
  - expect: It is rigid and clatters.
  - fail: It bends; or bounces; or melts.
- P5 [fatal · permanence_count]
  - expect: One broom keeps its number.
  - fail: It duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The broom and the kitchen stay the same.
  - fail: The broom changes colour; or the floor changes; or the kitchen rearranges.

## MECH-0311 · balance_topple · eval

**Caption.** A round-bottomed roly-poly toy on a table is pushed over onto its side and let go, and it rocks back upright and settles.

**Expectation (hidden).** The toy swings back toward upright as soon as it is released, rocks a few times with shrinking swings, and ends up standing; it does not stay on its side or tip over the other way.

**Declared violation types.** causeless_motion, trajectory_momentum

**SA**
- S1 [core] A round-bottomed roly-poly toy is on a table.
- S2 [core] It is pushed over onto its side and let go.
- S3 [core] It rocks back upright.
- S4 [core] It settles standing.
- S5 [minor] The release comes first, then the rocking, then the settling.

**PC**
- P1 [core · trajectory_momentum]
  - expect: It swings back toward upright as soon as it is released, rocks with shrinking swings, and ends standing.
  - fail: It stays on its side; or tips over the other way; or the swings grow.
- P2 [core · causeless_motion]
  - expect: Nothing touches it after the release.
  - fail: It is pushed again; or slides; or restarts after settling.
- P3 [major · gravity_direction]
  - expect: It stays on the table.
  - fail: It floats; or lifts; or sinks.
- P4 [major · material_response]
  - expect: It is rigid.
  - fail: It squashes; or melts; or splits.
- P5 [fatal · permanence_count]
  - expect: One toy keeps its number.
  - fail: It duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The toy's colours and the table stay the same.
  - fail: The toy changes colour; or the table changes; or the background rearranges.

**Note.** The hand is kept as the minimal trigger; the person is not judged.

## MECH-0312 · tension · eval

**Caption.** A backpack is hooked to a bungee cord hanging from a beam and let go; the cord stretches, the pack bounces back up, and it bobs up and down before settling.

**Expectation (hidden).** The cord lengthens as the pack drops and shortens as it rises, each bounce smaller than the last; the pack never rises above the point where it was released and the cord does not go slack while the pack hangs.

**Declared violation types.** material_response, trajectory_momentum

**SA**
- S1 [core] A backpack is hooked to a bungee cord hanging from a beam.
- S2 [core] It is let go.
- S3 [core] The cord stretches.
- S4 [core] The pack bounces back up.
- S5 [core] It bobs up and down before settling.
- S6 [minor] The release comes first, then the stretch, then the bounces.

**PC**
- P1 [core · material_response]
  - expect: The cord lengthens as the pack drops and shortens as it rises, and it does not go slack while the pack hangs.
  - fail: The cord is rigid; or slack while the pack hangs; or it snaps.
- P2 [core · trajectory_momentum]
  - expect: Each bounce is smaller than the last and the pack never rises above the point where it was released.
  - fail: It rises above the release point; or the bounces grow; or it swings far sideways.
- P3 [major · causeless_motion]
  - expect: Nothing touches it after the release.
  - fail: It is pushed; or restarts after settling; or jumps.
- P4 [major · gravity_direction]
  - expect: The pack hangs below the beam.
  - fail: It rises above the beam; or floats; or hangs sideways.
- P5 [fatal · permanence_count]
  - expect: One pack and one cord keep their number.
  - fail: The pack duplicates; or the cord vanishes; or the pack turns into another object.
- P6 [minor · attribute_drift]
  - expect: The pack and the beam stay the same.
  - fail: The pack changes colour; or the beam changes; or the room rearranges.

## MECH-0313 · tension · eval

**Caption.** A wet blanket is thrown over a thin washing line, the line sags deeply, then snaps, and the blanket falls to the grass.

**Expectation (hidden).** The sag deepens under the weight before the break; at the snap the two ends of the line spring apart and the blanket drops straight down; the line does not hold the load after breaking or rejoin.

**Declared violation types.** material_response, gravity_direction

**SA**
- S1 [core] A wet blanket is thrown over a thin washing line.
- S2 [core] The line sags deeply.
- S3 [core] The line snaps.
- S4 [core] The blanket falls to the grass.
- S5 [minor] The sag comes first, then the snap, then the fall.

**PC**
- P1 [core · material_response]
  - expect: The sag deepens under the weight before the break, and at the snap the ends spring apart.
  - fail: The line holds unchanged; or stretches like elastic; or rejoins.
- P2 [core · gravity_direction]
  - expect: The blanket drops straight down after the snap.
  - fail: It floats; or rises; or hangs on nothing.
- P3 [major · missing_consequence]
  - expect: The line no longer holds anything after breaking.
  - fail: It holds the load after breaking; or the blanket falls with the line intact; or the line vanishes.
- P4 [major · material_response]
  - expect: The wet blanket is heavy and limp.
  - fail: It is rigid; or floats like dry cloth; or tears.
- P5 [fatal · permanence_count]
  - expect: One blanket keeps its number and one line becomes two ends.
  - fail: The blanket duplicates; or the line is whole again; or the blanket turns into another object.
- P6 [minor · attribute_drift]
  - expect: The blanket's colour and the yard stay the same.
  - fail: The blanket changes colour; or the posts change; or the yard rearranges.

## MECH-0314 · deformation · eval

**Caption.** A brick is set on top of a coil spring standing on a table, the spring compresses under it, and when the brick is lifted off the spring extends again.

**Expectation (hidden).** The spring shortens only while the brick is on it and returns to its full height after the brick is removed; it does not stay compressed or stretch longer than it started.

**Declared violation types.** material_response, shape_identity

**SA**
- S1 [core] A coil spring stands on a table.
- S2 [core] A brick is set on top of it.
- S3 [core] The spring compresses.
- S4 [core] The brick is lifted off.
- S5 [core] The spring extends again.
- S6 [minor] The brick is set on first, then lifted, then the spring recovers.

**PC**
- P1 [core · material_response]
  - expect: The spring shortens only while the brick is on it and returns to its full height after the brick is removed.
  - fail: It stays compressed; or does not compress; or stretches longer than it started.
- P2 [core · shape_identity]
  - expect: The spring keeps its coil shape.
  - fail: It bends sideways and stays; or splits; or melts.
- P3 [major · gravity_direction]
  - expect: The brick sits on top of the spring.
  - fail: It floats; or passes through the spring; or hangs beside it.
- P4 [major · causeless_motion]
  - expect: The spring moves only with the brick.
  - fail: It bounces by itself; or slides; or jumps.
- P5 [fatal · permanence_count]
  - expect: One spring and one brick keep their number.
  - fail: The spring duplicates; or the brick vanishes; or the spring turns into another object.
- P6 [minor · attribute_drift]
  - expect: The spring and the table stay the same.
  - fail: The spring changes colour; or the brick changes; or the table rearranges.

## MECH-0315 · deformation · eval

**Caption.** A car reverses slowly into a lamp post, and its rear bumper dents inward and stays dented after it pulls forward.

**Expectation (hidden).** The dent forms at the point of contact at the moment of impact and remains when the car moves away; the bumper does not spring back to shape and the post does not bend.

**Declared violation types.** material_response, permanence_count

**SA**
- S1 [core] A car reverses slowly toward a lamp post.
- S2 [core] The rear bumper hits the post.
- S3 [core] The bumper dents inward.
- S4 [core] It stays dented after the car pulls forward.
- S5 [minor] The impact comes first, then the dent, then the car pulls away.

**PC**
- P1 [core · material_response]
  - expect: The dent forms at the point of contact at the moment of impact, and the post does not bend.
  - fail: No dent forms; or the post bends; or the bumper shatters.
- P2 [core · permanence_count]
  - expect: The dent remains when the car moves away.
  - fail: It springs back; or the dent vanishes; or the dent is there before contact.
- P3 [major · solidity]
  - expect: The car stops at the post and does not pass into it.
  - fail: It passes through the post; or the post passes through the car; or the car sinks into the road.
- P4 [major · causeless_motion]
  - expect: The post stays put.
  - fail: It moves; or vanishes; or leans and stays leaning.
- P5 [fatal · permanence_count]
  - expect: One car and one post keep their number.
  - fail: The car duplicates; or the post vanishes; or the car turns into another vehicle.
- P6 [minor · attribute_drift]
  - expect: The car's colour and the street stay the same.
  - fail: The car changes colour; or the post changes; or the street rearranges.

## MECH-0316 · cut_tear · eval

**Caption.** A lawnmower runs across an overgrown lawn, and the grass behind it is cut short with clippings scattered.

**Expectation (hidden).** The grass is shorter only where the mower has passed, the cut edge follows the mower's path, and clippings appear behind it; the grass ahead stays tall and does not grow back behind.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A lawnmower runs across an overgrown lawn.
- S2 [core] The grass behind it is cut short.
- S3 [core] Clippings are scattered behind it.
- S4 [minor] The lawn is overgrown ahead of the mower.
- S5 [minor] The mower passes first and the cut grass follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The grass is shorter only where the mower has passed, and the cut edge follows the mower's path.
  - fail: Grass is cut ahead of the mower; or the mower passes and the grass stays tall; or the cut appears elsewhere.
- P2 [core · permanence_count]
  - expect: The grass ahead stays tall and does not grow back behind.
  - fail: It grows back behind; or the tall grass ahead becomes short; or the cut strip vanishes.
- P3 [major · material_response]
  - expect: The clippings are small and scatter.
  - fail: The grass is rigid; or the clippings rise indefinitely; or they form a solid block.
- P4 [major · gravity_direction]
  - expect: The clippings fall.
  - fail: They hang; or rise; or float away.
- P5 [fatal · permanence_count]
  - expect: One mower keeps its number.
  - fail: It duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The mower and the garden stay the same.
  - fail: The mower changes colour; or the garden rearranges; or the grass changes colour.

## MECH-0317 · cut_tear · eval

**Caption.** A dog bites into a stuffed cushion on a sofa and tears it open, and white stuffing spills out through the rip.

**Expectation (hidden).** The fabric parts where the teeth pull, the rip widens as the dog tugs, and stuffing comes out only through the rip; the cushion does not seal itself or shrink back to shape.

**Declared violation types.** material_response, permanence_count

**SA**
- S1 [core] A dog bites into a stuffed cushion on a sofa.
- S2 [core] It tears the cushion open.
- S3 [core] White stuffing spills out through the rip.
- S4 [minor] The bite comes first, then the rip, then the stuffing.

**PC**
- P1 [core · material_response]
  - expect: The fabric parts where the teeth pull and the rip widens as the dog tugs.
  - fail: The fabric stretches like rubber; or shatters; or tears elsewhere.
- P2 [core · permanence_count]
  - expect: Stuffing comes out only through the rip and the cushion does not reseal.
  - fail: It reseals; or stuffing comes from elsewhere; or the stuffing returns.
- P3 [major · gravity_direction]
  - expect: The stuffing falls or drifts down.
  - fail: It rises indefinitely; or hangs; or floats up.
- P4 [major · shape_identity]
  - expect: The cushion deflates as stuffing leaves.
  - fail: It stays plump; or grows; or turns into another object.
- P5 [fatal · shape_identity]
  - expect: One dog and one cushion keep their number.
  - fail: The dog splits; or the cushion duplicates; or the dog merges with the cushion.
- P6 [minor · attribute_drift]
  - expect: The cushion's colour and the sofa stay the same.
  - fail: The cushion changes colour; or the sofa changes; or the room rearranges.

**Note.** The dog is self-driven: its tugging is its own. Only the fabric's response is judged.

## MECH-0318 · fluid · eval

**Caption.** An empty glass bottle is pushed neck-first under the water in a sink, and water flows in while a stream of bubbles escapes from the neck.

**Expectation (hidden).** Water rises inside the bottle while air leaves as bubbles that climb to the surface; the bottle fills only as fast as the air escapes and does not fill instantly or stay empty under water.

**Declared violation types.** process_direction, gravity_direction

**SA**
- S1 [core] An empty glass bottle is pushed neck-first under the water in a sink.
- S2 [core] Water flows in.
- S3 [core] A stream of bubbles escapes from the neck.
- S4 [minor] The push under comes first and the filling follows.

**PC**
- P1 [core · process_direction]
  - expect: Water rises inside the bottle while air leaves, and it fills only as fast as the air escapes.
  - fail: It fills instantly; or stays empty under water; or empties again.
- P2 [core · gravity_direction]
  - expect: The bubbles climb to the surface.
  - fail: They sink; or hang; or go sideways.
- P3 [major · material_response]
  - expect: The water is liquid and the bubbles wobble.
  - fail: It is rigid; or the bubbles are solid; or the water beads.
- P4 [major · causeless_motion]
  - expect: The bottle stays where it is held.
  - fail: It floats away; or jumps; or spins.
- P5 [fatal · permanence_count]
  - expect: One bottle keeps its number.
  - fail: It duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The bottle and the sink stay the same.
  - fail: The bottle changes colour; or the sink changes; or the kitchen rearranges.

**Note.** The hand is kept as the minimal trigger; the person is not judged.

## MECH-0319 · granular · eval

**Caption.** A snow plough drives down a street, and the snow rolls up along its blade and is left in a ridge at the roadside.

**Expectation (hidden).** Snow piles against the blade and spills off its end as the plough moves, leaving a continuous ridge behind and a cleared strip in its path; snow does not pass through the blade or return to the cleared strip.

**Declared violation types.** missing_consequence, solidity

**SA**
- S1 [core] A snow plough drives down a street.
- S2 [core] Snow rolls up along its blade.
- S3 [core] It is left in a ridge at the roadside.
- S4 [minor] The plough passes first and the ridge is left after.

**PC**
- P1 [core · missing_consequence]
  - expect: Snow piles against the blade and spills off its end, leaving a continuous ridge behind and a cleared strip in its path.
  - fail: No ridge forms; or snow returns to the cleared strip; or the ridge appears ahead of the plough.
- P2 [core · solidity]
  - expect: Snow does not pass through the blade.
  - fail: It passes through the blade; or the blade passes through the snow; or the plough sinks into the road.
- P3 [major · material_response]
  - expect: The snow rolls, breaks and piles.
  - fail: It moves as a rigid block; or flows like liquid; or bounces.
- P4 [major · trajectory_momentum]
  - expect: It is pushed to the side the blade is angled toward.
  - fail: It goes to the opposite side; or straight up; or ahead of the plough.
- P5 [fatal · permanence_count]
  - expect: One plough keeps its number.
  - fail: It duplicates; or vanishes; or turns into another vehicle.
- P6 [minor · attribute_drift]
  - expect: The plough and the street stay the same.
  - fail: The plough changes colour; or the buildings rearrange; or the street changes.

## MECH-0320 · granular · eval

**Caption.** The base of a steep pile of dry sand in a sandbox is scraped away, and a section of the slope above slides down as a sheet and comes to rest at a gentler angle.

**Expectation (hidden).** The slide starts where the support was removed and moves downhill, grains flowing rather than tumbling as a block; the pile ends flatter than it began and does not steepen or rebuild itself.

**Declared violation types.** gravity_direction, causeless_motion

**SA**
- S1 [core] A steep pile of dry sand is in a sandbox.
- S2 [core] Its base is scraped away.
- S3 [core] A section of the slope above slides down as a sheet.
- S4 [core] It comes to rest at a gentler angle.
- S5 [minor] The scrape comes first and the slide follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The slide starts where the support was removed.
  - fail: It starts before the scrape; or elsewhere; or the base is scraped and nothing moves.
- P2 [core · gravity_direction]
  - expect: It moves downhill with the grains flowing, and the pile ends flatter than it began.
  - fail: It steepens; or rebuilds itself; or slides uphill.
- P3 [major · material_response]
  - expect: It flows as grains, not as a block.
  - fail: It moves as a block; or flows like liquid; or bounces.
- P4 [major · process_direction]
  - expect: It slides and then settles.
  - fail: It keeps flowing indefinitely; or reverses; or jumps.
- P5 [fatal · permanence_count]
  - expect: One pile keeps its total of sand.
  - fail: Sand appears from nowhere; or vanishes; or the pile duplicates.
- P6 [minor · attribute_drift]
  - expect: The sand's colour and the sandbox stay the same.
  - fail: The sand changes colour; or the box changes; or the background rearranges.

## MECH-0321 · gas_wind · eval

**Caption.** A car speeds past a pile of dry leaves at the roadside, and the leaves are whirled up in its wake and settle again behind it.

**Expectation (hidden).** The leaves lift only as the car passes, swirl in the direction of travel, and drift back down after it has gone; they do not move before the car arrives or rise indefinitely.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A pile of dry leaves lies at a roadside.
- S2 [core] A car speeds past.
- S3 [core] The leaves are whirled up in its wake.
- S4 [core] They settle again behind it.
- S5 [minor] The car passes first, then the leaves lift, then they settle.

**PC**
- P1 [core · causeless_motion]
  - expect: The leaves lift only as the car passes.
  - fail: They lift before the car arrives; or with no car; or keep swirling long after it has gone.
- P2 [core · gravity_direction]
  - expect: They drift back down after the car has passed.
  - fail: They rise indefinitely; or hang; or float away.
- P3 [major · trajectory_momentum]
  - expect: They swirl in the direction the car travelled.
  - fail: They fly against it; or only straight up; or crosswise.
- P4 [major · material_response]
  - expect: They flutter and tumble.
  - fail: They are rigid; or move as balls; or as one sheet.
- P5 [fatal · permanence_count]
  - expect: One car keeps its number and the leaves are the pile's.
  - fail: The car duplicates; or leaves appear from nowhere; or the car passes through the pile.
- P6 [minor · attribute_drift]
  - expect: The car's colour and the roadside stay the same.
  - fail: The car changes colour; or the roadside rearranges; or the leaves change colour.

## MECH-0322 · gas_wind · eval

**Caption.** A gust through an open window blows the bedroom door shut with a bang.

**Expectation (hidden).** The door swings closed in the direction the curtains blow and stops at the frame; it does not close in still air or swing against the wind.

**Declared violation types.** causeless_motion, solidity

**SA**
- S1 [core] A bedroom window is open and a door stands ajar.
- S2 [core] A gust comes through the window.
- S3 [core] The door swings shut.
- S4 [minor] Other signs of wind, such as curtains, are visible.
- S5 [minor] The gust comes first and the door shuts after.

**PC**
- P1 [core · causeless_motion]
  - expect: The door swings closed in the direction the curtains blow and not in still air.
  - fail: It closes in still air; or swings against the wind; or closes before the gust.
- P2 [core · solidity]
  - expect: It stops at the frame.
  - fail: It passes through the frame; or through the wall; or the frame passes through the door.
- P3 [major · trajectory_momentum]
  - expect: It swings on its hinges in an arc.
  - fail: It slides; or lifts; or spins.
- P4 [major · material_response]
  - expect: The door is rigid and may rebound slightly.
  - fail: It bends; or bounces fully open again; or shatters.
- P5 [fatal · permanence_count]
  - expect: One door keeps its number.
  - fail: It duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The door and the room stay the same.
  - fail: The door changes colour; or the room rearranges; or the window changes.

## MECH-0323 · biomechanics · eval

**Caption.** A person jumps down from a low garden wall, lands on both feet and bends deeply at the knees, then straightens up and walks on.

**Expectation (hidden).** The knees bend on landing and the body sinks before rising again; the landing is heavier than the take-off; the person does not land stiff-legged, float down, or bounce back up onto the wall.

**Declared violation types.** trajectory_momentum, gravity_direction

**SA**
- S1 [core] A person jumps down from a low garden wall.
- S2 [core] They land on both feet.
- S3 [core] They bend deeply at the knees.
- S4 [core] They straighten up and walk on.
- S5 [minor] The jump comes first, then the landing, then the bend, then walking on.

**PC**
- P1 [core · gravity_direction]
  - expect: They fall faster to the ground, the knees bend on landing, and the body sinks before rising again.
  - fail: They float down; or land stiff-legged; or bounce back up onto the wall.
- P2 [core · trajectory_momentum]
  - expect: They go forward off the wall, land ahead of it, and walk on.
  - fail: They go backward; or land back on the wall; or freeze.
- P3 [major · shape_identity]
  - expect: The body bends at the joints.
  - fail: It folds mid-bone; or a limb detaches; or a leg stretches.
- P4 [major · solidity]
  - expect: The feet land on the ground.
  - fail: They sink; or pass through the wall; or the ground passes through them.
- P5 [fatal · shape_identity]
  - expect: Their limbs keep their number and stay attached.
  - fail: A limb vanishes; or a second figure appears; or they merge with the wall.
- P6 [minor · attribute_drift]
  - expect: Their clothing and the garden stay the same.
  - fail: The clothing changes colour; or the wall changes; or the garden rearranges.

**Note.** Biomechanics scene: the body is the physics. Form, posture and skill are not judged; only that limbs stay attached, bend at joints, keep ground contact and pass through nothing.

## MECH-0324 · soft_material · eval

**Caption.** A curtain is drawn along its rail to one side, and the fabric gathers into deep folds as it bunches at the end.

**Expectation (hidden).** The folds grow deeper and closer together as more curtain arrives, the hem stays hanging under gravity, and the cloth does not stiffen, stretch, or pass through itself.

**Declared violation types.** shape_identity, material_response

**SA**
- S1 [core] A curtain hangs on a rail.
- S2 [core] It is drawn along the rail to one side.
- S3 [core] The fabric gathers into deep folds at the end.
- S4 [minor] The drawing comes first and the folds deepen after.

**PC**
- P1 [core · shape_identity]
  - expect: The folds grow deeper and closer as more curtain arrives, the fabric keeps its length, and it does not pass through itself.
  - fail: It passes through itself; or grows; or the folds do not deepen.
- P2 [core · material_response]
  - expect: The soft cloth folds and the hem hangs.
  - fail: It is rigid; or stretches; or tears.
- P3 [major · gravity_direction]
  - expect: The hem hangs under gravity.
  - fail: It rises; or floats; or stands out sideways.
- P4 [major · causeless_motion]
  - expect: It moves only as it is drawn.
  - fail: It moves by itself; or slides back; or jumps.
- P5 [fatal · permanence_count]
  - expect: One curtain keeps its number.
  - fail: It duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The curtain's colour and the window stay the same.
  - fail: The curtain changes colour; or the rail changes; or the room rearranges.

**Note.** The hand is kept as the minimal trigger; the person is not judged.

## MECH-0325 · occlusion_containment · eval

**Caption.** A red sock is tossed into a front-loading washing machine with other clothes and the door shut; through the glass window the sock is seen tumbling past among the clothes.

**Expectation (hidden).** The sock appears at the window now and then as the drum turns, always the same sock, and never outside the machine while the door is shut; it does not vanish for good or multiply.

**Declared violation types.** permanence_count, solidity

**SA**
- S1 [core] A red sock is tossed into a front-loading washing machine with other clothes.
- S2 [core] The door is shut.
- S3 [core] The sock is seen through the glass tumbling past among the clothes.
- S4 [minor] The toss and the door shutting come first, then the tumbling.

**PC**
- P1 [core · permanence_count]
  - expect: The same sock appears at the window now and then, and never outside while the door is shut.
  - fail: Two red socks appear; or the sock is outside; or it vanishes for good.
- P2 [core · solidity]
  - expect: The clothes stay inside the drum behind the glass.
  - fail: They pass through the glass; or through the door; or the drum passes through them.
- P3 [major · trajectory_momentum]
  - expect: The clothes tumble with the drum's turn.
  - fail: They stay still while the drum turns; or move against it; or float.
- P4 [major · shape_identity]
  - expect: The sock keeps its colour and shape.
  - fail: It changes colour; or grows; or turns into another garment.
- P5 [fatal · permanence_count]
  - expect: One machine keeps its number.
  - fail: It duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The machine and the room stay the same.
  - fail: The machine changes colour; or the room rearranges; or the door changes.

