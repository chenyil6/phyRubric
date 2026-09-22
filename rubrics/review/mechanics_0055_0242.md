# Rubric review

183 rubrics. SA = caption adherence (core/minor); PC = physics (fatal/core/major/minor, each tagged with a violation type). Expectation is the hidden field from data/, shown for the reviewer only.

# Mechanics

## MECH-0055 · friction_rolling · train

**Caption.** A heavy wooden barrel being rolled up a plank onto a truck bed is let go halfway up, and it rolls back down to the ground.

**Expectation (hidden).** The roll back begins as soon as the barrel is released and speeds up down the plank; the barrel does not stay put on the slope or continue upward.

**Declared violation types.** gravity_direction, causeless_motion

**SA**
- S1 [core] A heavy wooden barrel is being rolled up a plank toward a truck bed.
- S2 [core] It is let go part way up the plank.
- S3 [core] It rolls back down to the ground.
- S4 [minor] The plank leads up onto a truck bed.
- S5 [minor] The release comes first and the roll back follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The barrel goes up only while it is pushed; the roll back begins at the release and not before, and once on the ground it stays there.
  - fail: The barrel rolls back while it is still being pushed up; or it stays put on the slope after being released; or it sets off again after coming to rest on the ground.
- P2 [core · gravity_direction]
  - expect: After the release it goes downhill along the plank, quicker the further it rolls.
  - fail: The barrel carries on up the plank after being let go; or it slows as it rolls down; or it leaves the plank and floats.
- P3 [major · trajectory_momentum]
  - expect: The barrel turns as it rolls, keeps to the plank's line, and runs out onto the ground at the bottom.
  - fail: The barrel slides down without turning; or it turns sharply off the side of the plank with nothing touching it; or it stops dead at the foot of the plank as though it had hit a wall.
- P4 [major · material_response]
  - expect: The barrel stays a rigid drum and the plank stays a rigid board under it.
  - fail: The barrel squashes or wobbles like rubber; or the plank sags and springs like a trampoline; or the barrel's staves come apart as it rolls.
- P5 [fatal · permanence_count]
  - expect: One barrel, one plank and one truck keep their number and shape.
  - fail: The barrel vanishes or a second one appears; or it passes through the plank or the truck bed; or it turns into another object.
- P6 [minor · attribute_drift]
  - expect: The barrel's wood and hoops, the plank and the truck stay the same.
  - fail: The barrel changes colour or size; or the plank changes length between frames; or the truck changes shape.

## MECH-0056 · friction_rolling · train

**Caption.** A bicycle is turned upside down, its front wheel is given a spin, and the wheel keeps spinning for a while before stopping.

**Expectation (hidden).** The spin slows gradually and evenly; the wheel does not stop at once, speed up, or reverse.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A bicycle stands upside down on its saddle and handlebars.
- S2 [core] Its front wheel is given a spin.
- S3 [core] The wheel keeps spinning after the hand leaves it.
- S4 [core] The wheel comes to a stop.
- S5 [minor] It is the front wheel that is spun.
- S6 [minor] The spin comes first, then the wheel runs on, then it stops.

**PC**
- P1 [core · process_direction]
  - expect: After the spin the wheel slows steadily, turning the same way throughout, until it stops.
  - fail: The wheel speeds up on its own; or it reverses direction as it slows; or it slows and then picks up again.
- P2 [core · causeless_motion]
  - expect: The wheel turns because of the one spin and comes to rest only by slowing down.
  - fail: The wheel stops the instant the hand leaves it; or it starts turning again after stopping; or it is already turning before anything touches it.
- P3 [major · material_response]
  - expect: The wheel stays a rigid round rim turning about its hub.
  - fail: The rim wobbles out of round as it turns; or the spokes bend; or the tyre stretches.
- P4 [major · gravity_direction]
  - expect: The bicycle stays resting upside down on its saddle and handlebars.
  - fail: The bicycle rights itself with nothing touching it; or it lifts off the ground; or it slides across the floor while the wheel spins.
- P5 [fatal · permanence_count]
  - expect: One bicycle with its two wheels keeps its number and shape.
  - fail: A wheel vanishes or a third one appears; or the wheel passes through the fork; or the bicycle turns into another object.
- P6 [minor · attribute_drift]
  - expect: The bicycle's frame colour, the wheel and the surroundings stay the same.
  - fail: The frame changes colour; or the spinning wheel changes size; or the floor beneath rearranges between frames.

## MECH-0057 · friction_rolling · train

**Caption.** A ball is rolled up a gentle grassy slope; it slows, stops, and rolls back down.

**Expectation (hidden).** The ball slows steadily on the way up, pauses for an instant, and comes back along roughly the same line, speeding up on the way down.

**Declared violation types.** gravity_direction, trajectory_momentum

**SA**
- S1 [core] A ball is rolled up a grassy slope.
- S2 [core] It slows.
- S3 [core] It stops.
- S4 [core] It rolls back down.
- S5 [minor] The slope is gentle rather than steep.
- S6 [minor] The roll up comes first, then the stop, then the roll back.

**PC**
- P1 [core · gravity_direction]
  - expect: On the way up the ball slows, pauses for an instant, then comes back down, quicker the further it rolls.
  - fail: The ball keeps its speed all the way up the slope; or it stays put where it stopped; or it slows on the way down.
- P2 [core · trajectory_momentum]
  - expect: It comes back along roughly the line it went up.
  - fail: The ball turns sideways on the open slope with nothing touching it; or it rolls back down a part of the slope far from its track up; or it reverses again and rolls uphill.
- P3 [major · causeless_motion]
  - expect: Nothing touches the ball after the roll; its motion changes only with the slope.
  - fail: The ball speeds up while going uphill; or it stops and starts more than once on the slope; or it sets off again after coming to rest at the bottom.
- P4 [major · material_response]
  - expect: The ball stays round and rolls on the grass, which flattens under it.
  - fail: The ball squashes flat and stays flat; or it slides without turning; or the grass ripples like water as the ball passes.
- P5 [fatal · permanence_count]
  - expect: One ball is on the slope throughout and stays above the ground.
  - fail: The ball vanishes or a second one appears; or it passes through the ground; or it turns into another object.
- P6 [minor · attribute_drift]
  - expect: The ball's colour, the slope and the background stay the same.
  - fail: The ball changes colour; or the slope changes gradient between frames; or the background rearranges.

## MECH-0058 · friction_rolling · train

**Caption.** A wheelbarrow full of soil is pushed from a paved patio onto a soft lawn, and its wheel sinks into the turf and drags.

**Expectation (hidden).** The wheel rolls without sinking on the paving and sinks and leaves a track once it is on the lawn; the change happens at the edge of the paving.

**Declared violation types.** material_response, trajectory_momentum

**SA**
- S1 [core] A wheelbarrow full of soil is pushed along a paved patio.
- S2 [core] It is pushed onto a lawn.
- S3 [core] Its wheel sinks into the turf.
- S4 [core] The wheel drags.
- S5 [minor] The barrow is full of soil.
- S6 [minor] The paving comes first, then the lawn, then the sinking.

**PC**
- P1 [core · material_response]
  - expect: On the paving the wheel rolls without sinking; on the lawn it sinks and leaves a track, and the change happens at the edge of the paving.
  - fail: The wheel sinks into the paving; or it rolls over the lawn leaving no track as if on stone; or it sinks well before or well after the edge of the paving.
- P2 [core · trajectory_momentum]
  - expect: The barrow slows as the wheel sinks and drags.
  - fail: The barrow speeds up on the soft lawn; or it glides across the lawn as freely as it did on the paving; or it stops dead at the edge of the paving as though against a wall.
- P3 [major · gravity_direction]
  - expect: The barrow stays down on its wheel and legs, and the load rides in the tray.
  - fail: The barrow lifts off the ground; or soil rises out of the tray; or the wheel floats above the turf.
- P4 [major · material_response]
  - expect: The soil in the tray shifts and settles as the barrow jolts, and turf disturbed by the wheel stays on the ground.
  - fail: The load stays a rigid block while the barrow jolts; or soil rises away from the tray and hangs; or the turf flows like liquid around the wheel.
- P5 [fatal · permanence_count]
  - expect: One barrow with its load keeps its number and shape.
  - fail: The barrow vanishes or a second one appears; or the wheel passes through the ground; or the barrow turns into another object.
- P6 [minor · attribute_drift]
  - expect: The barrow's colour, the paving and the lawn stay the same.
  - fail: The barrow changes colour; or the edge between paving and lawn moves between frames; or the garden behind rearranges.

## MECH-0059 · friction_rolling · train

**Caption.** A log is rolled off the back of a trailer onto a slight downhill slope and rolls down to the bottom.

**Expectation (hidden).** The log turns about its length as it rolls, speeds up on the slope, and comes to rest at the bottom or against an obstacle; it does not stop on the slope or roll uphill.

**Declared violation types.** gravity_direction, trajectory_momentum

**SA**
- S1 [core] A log is rolled off the back of a trailer.
- S2 [core] It lands on a downhill slope.
- S3 [core] It rolls down to the bottom.
- S4 [minor] The slope is slight rather than steep.
- S5 [minor] The log leaves the trailer first and the roll down follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The log drops from the trailer to the ground and then goes downhill, quicker as it goes, coming to rest at the bottom or against something.
  - fail: The log rolls uphill; or it stops on the open slope with nothing in its way; or it hangs in the air after leaving the trailer.
- P2 [core · trajectory_momentum]
  - expect: It turns about its length as it rolls and keeps roughly a straight line down the slope.
  - fail: The log slides down end-on without turning; or it turns sharply on the open slope with nothing touching it; or it bounces higher than the trailer bed.
- P3 [major · causeless_motion]
  - expect: Once on the ground nothing but the slope moves the log, and at the bottom it stays.
  - fail: The log speeds up after reaching the flat; or it sets off again after coming to rest; or it changes direction with nothing touching it.
- P4 [major · material_response]
  - expect: The log stays a rigid cylinder and the ground takes the impact.
  - fail: The log bends as it rolls; or it splashes where it lands; or the ground ripples under it.
- P5 [fatal · permanence_count]
  - expect: One log and one trailer keep their number and shape.
  - fail: The log vanishes or a second one appears; or it passes through the trailer or the ground; or it turns into another object.
- P6 [minor · attribute_drift]
  - expect: The log's bark, the trailer and the slope stay the same.
  - fail: The log changes colour or length; or the trailer changes shape between frames; or the slope rearranges.

## MECH-0060 · friction_rolling · train

**Caption.** A skateboarder rolling along a flat path lowers his back foot and drags it on the ground, and the board slows and comes to a stop.

**Expectation (hidden).** The slowing starts the moment the foot touches the ground, not before and not long after; the board keeps a straight line as it slows and stops without a jolt, with the rider still standing on it; it does not keep rolling at full speed while the foot drags, and does not speed up or roll backward.

**Declared violation types.** causeless_motion, missing_consequence, trajectory_momentum

**SA**
- S1 [core] A skateboarder rolls along a flat path.
- S2 [core] He lowers his back foot to the ground.
- S3 [core] He drags the foot along the ground.
- S4 [core] The board slows and comes to a stop.
- S5 [minor] It is the back foot that is lowered.
- S6 [minor] The foot touches down first and the slowing follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The slowing begins when the foot touches the ground and goes on while it drags.
  - fail: The board keeps its speed while the foot plainly drags; or the board slows before the foot reaches the ground; or the foot drags and the board speeds up.
- P2 [core · trajectory_momentum]
  - expect: The board keeps a straight line as it slows and stops smoothly with the rider still on it.
  - fail: The board veers sharply while the foot drags; or it stops dead with a jolt and throws the rider; or it rolls backward after stopping.
- P3 [major · causeless_motion]
  - expect: Nothing else acts on the board, and once stopped it stays stopped.
  - fail: The board slows with the foot never touching the ground; or it sets off again after stopping; or it speeds up on the flat with no push.
- P4 [major · gravity_direction]
  - expect: The dragging foot stays on the ground and the board stays on its wheels.
  - fail: The foot hovers above the ground while the board slows; or the board lifts off the path; or the rider floats above the board.
- P5 [fatal · shape_identity]
  - expect: The rider and the board keep their number and shape, and nothing passes through anything.
  - fail: The foot passes through the deck or the ground; or a limb detaches or vanishes; or the board passes through the path.
- P6 [minor · attribute_drift]
  - expect: The rider's clothing, the board and the path stay the same.
  - fail: The rider's clothing changes colour; or the board's deck changes graphic; or the path's surface changes between frames.

**Note.** Friction scene: the rider is kept because his foot is the brake. Stance, style and how he balances are not judged; only when the foot touches down and how the board's speed responds.

## MECH-0061 · friction_rolling · train

**Caption.** A car drives onto a frozen pond, its front wheels are turned sharply, and the car keeps sliding straight ahead instead of turning.

**Expectation (hidden).** The car's path barely changes even though the wheels point sideways; the rear may swing out; the car does not turn crisply as on dry road.

**Declared violation types.** trajectory_momentum, causeless_motion

**SA**
- S1 [core] A car drives onto a frozen pond.
- S2 [core] Its front wheels are turned sharply.
- S3 [core] The car keeps sliding straight ahead instead of turning.
- S4 [minor] The wheels are turned first and the straight slide continues afterwards.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The car's path barely changes while the wheels point sideways; it carries on along its old line.
  - fail: The car turns crisply to follow the wheels as it would on dry road; or it turns the opposite way to the wheels; or it stops dead when the wheels are turned.
- P2 [core · causeless_motion]
  - expect: The car slides under its own momentum; any swing of the rear is gradual, and nothing changes its motion without acting on it.
  - fail: The car jinks sideways with the wheels straight; or it speeds up while sliding; or it reverses.
- P3 [major · material_response]
  - expect: On the ice the tyres skid rather than grip; the car may drift and the rear may swing out slowly.
  - fail: The tyres bite and the car pivots sharply; or the car tilts up onto two wheels; or the ice cracks open and swallows a wheel.
- P4 [major · gravity_direction]
  - expect: The car stays flat on the ice throughout.
  - fail: The car lifts off the surface; or it sinks through the ice; or it tilts and stays tilted with nothing holding it.
- P5 [fatal · permanence_count]
  - expect: One car keeps its shape on the pond.
  - fail: The car vanishes or a second one appears; or it passes through the bank or a tree; or it turns into another vehicle.
- P6 [minor · attribute_drift]
  - expect: The car's colour, the ice and the shore stay the same.
  - fail: The car changes colour; or the pond's edge moves between frames; or the trees on the shore rearrange.

## MECH-0063 · projectile · train

**Caption.** A running garden hose propped at an upward angle beside a vegetable bed sends its stream over the bed, and the water comes down on the far side.

**Expectation (hidden).** The stream leaves the nozzle and curves over in an arc before reaching the ground; it does not travel in a straight line or stop in the air.

**Declared violation types.** trajectory_momentum, gravity_direction

**SA**
- S1 [core] A running garden hose is propped at an upward angle beside a vegetable bed.
- S2 [core] Its stream arcs over the bed.
- S3 [core] The water comes down on the far side of the bed.
- S4 [minor] The hose is propped in place rather than held.
- S5 [minor] The bed lies between the hose and the spot where the water lands.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The stream leaves the nozzle along the hose's angle and curves over in one smooth arc.
  - fail: The stream travels in a straight line to the far side; or it bends upward after leaving the nozzle; or it kinks or changes direction in mid-air.
- P2 [core · gravity_direction]
  - expect: The arc peaks and comes down, and the water lands on the far side and stays on the ground.
  - fail: The water hangs in the air at the top of the arc; or it rises again after starting to fall; or it lands and rises back up.
- P3 [major · material_response]
  - expect: The stream is a continuous jet that breaks into drops and spray as it falls, and the soil darkens and puddles where it lands.
  - fail: The stream is a rigid rod that stays whole all the way to the ground; or it lands and the ground stays dry; or the water gathers into balls.
- P4 [major · causeless_motion]
  - expect: The hose stays propped and still and the arc of the stream stays steady.
  - fail: The hose whips about with nothing touching it; or the stream jumps to a new arc; or the hose rises off its prop.
- P5 [fatal · permanence_count]
  - expect: One hose and one stream: water appears only from the nozzle.
  - fail: A second stream appears from nowhere; or the stream vanishes in mid-air; or the hose turns into another object.
- P6 [minor · attribute_drift]
  - expect: The hose's colour, the bed's plants and the garden stay the same.
  - fail: The hose changes colour; or the plants in the bed rearrange between frames; or the garden behind changes.

## MECH-0064 · projectile · train

**Caption.** A basketball shot from the three-point line drops through the hoop.

**Expectation (hidden).** The ball rises in an arc, peaks, and descends into the hoop; it does not travel flat or hover above the rim.

**Declared violation types.** trajectory_momentum, gravity_direction

**SA**
- S1 [core] A basketball is shot from behind the three-point line.
- S2 [core] It flies toward the hoop.
- S3 [core] It drops through the hoop.
- S4 [minor] It goes cleanly through rather than bouncing on the rim first.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The ball follows one smooth arc that rises, peaks and descends into the hoop.
  - fail: The ball flies flat at a constant height; or it hangs above the rim; or it changes direction in mid-flight with nothing touching it.
- P2 [core · gravity_direction]
  - expect: After the peak the ball comes down, passes through the hoop, and continues down toward the floor.
  - fail: The ball rises again after starting to fall; or it stops in the net and stays there; or it floats back up out of the hoop.
- P3 [major · material_response]
  - expect: The net swings and flares as the ball passes through, and the ball keeps its shape.
  - fail: The net stays rigid and still as the ball passes through it; or the ball squashes to fit and stays squashed; or the net closes and holds the ball like a bag.
- P4 [major · solidity]
  - expect: The ball passes through the open ring and the net, not through the rim's metal or the backboard.
  - fail: The ball passes through the metal of the rim; or it passes through the backboard; or the net passes through the ball.
- P5 [fatal · permanence_count]
  - expect: One ball and one hoop are there throughout.
  - fail: The ball vanishes in flight or a second one appears; or the ball turns into another object; or the hoop disappears from the backboard.
- P6 [minor · attribute_drift]
  - expect: The ball's colour and seams, the court markings and the backboard stay the same.
  - fail: The ball changes colour in flight; or the three-point line shifts between frames; or the backboard changes shape.

## MECH-0065 · projectile · train

**Caption.** A child on a moving swing lets go at the front of the arc, flies forward, and lands on the ground ahead of the swing.

**Expectation (hidden).** The child leaves the seat with the swing's forward motion and follows a curve down to the ground; the empty swing keeps swinging.

**Declared violation types.** trajectory_momentum, gravity_direction

**SA**
- S1 [core] A child is on a moving swing.
- S2 [core] The child lets go at the front of the arc.
- S3 [core] The child flies forward through the air.
- S4 [core] The child lands on the ground ahead of the swing.
- S5 [minor] The release is at the front of the arc, not the back.
- S6 [minor] The release comes first, then the flight, then the landing.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The child leaves the seat carrying the swing's forward motion and follows one curve forward and down.
  - fail: The child drops straight down below the seat; or flies backward; or changes direction in mid-air.
- P2 [core · gravity_direction]
  - expect: After leaving the seat the child comes down and lands.
  - fail: The child hangs in the air after letting go; or rises after leaving the seat and keeps rising; or lands and bounces higher than the seat.
- P3 [major · causeless_motion]
  - expect: The empty swing keeps swinging after the release and dies down on its own.
  - fail: The seat stops dead the instant the child leaves it; or it swings harder after the release; or it follows the child forward off its chains.
- P4 [major · material_response]
  - expect: The child lands with knees bending or a stumble, and the ground takes the landing.
  - fail: The child lands rigid as a statue; or sinks into the ground; or bounces off the ground like a ball.
- P5 [fatal · shape_identity]
  - expect: The child, the seat and the chains keep their number and shape, and the hands let go of the chains rather than passing through them.
  - fail: A hand passes through a chain; or a limb detaches or vanishes; or the child passes through the seat.
- P6 [minor · attribute_drift]
  - expect: The child's clothing, the swing and the playground stay the same.
  - fail: The child's clothing changes colour; or the swing frame changes shape between frames; or the playground behind rearranges.

**Note.** Projectile scene: the child is kept because the body is the projectile. Posture and how the landing looks are not judged; only the direction and order of the motion.

## MECH-0066 · projectile · train

**Caption.** A flat stone is thrown sideways low over a calm lake, and it skips across the surface several times before sinking.

**Expectation (hidden).** Each hop is shorter and lower than the last and leaves a ring of ripples; the stone finally sinks and does not float or skip forever.

**Declared violation types.** trajectory_momentum, gravity_direction

**SA**
- S1 [core] A flat stone is thrown low over a lake.
- S2 [core] It skips across the surface.
- S3 [core] It sinks.
- S4 [minor] It skips several times rather than once.
- S5 [minor] The lake is calm before the stone arrives.
- S6 [minor] The skipping comes first and the sinking follows.

**PC**
- P1 [core · trajectory_momentum]
  - expect: Each hop is shorter and lower than the one before, all along one line.
  - fail: A hop is higher or longer than the one before it; or the stone turns sharply between hops; or it comes back toward the thrower.
- P2 [core · gravity_direction]
  - expect: Between hops the stone comes down to the water, and at the end it goes under and stays under.
  - fail: The stone floats on the surface; or it rises after a hop and keeps rising; or it comes back up after sinking.
- P3 [major · missing_consequence]
  - expect: Each touch leaves a splash and a ring of ripples spreading outward.
  - fail: The stone touches the water and leaves no mark; or ripples appear where the stone never touched; or the ripples run inward.
- P4 [major · material_response]
  - expect: The splashes fall back and settle, and the stone stays a rigid flat stone.
  - fail: A splash hangs in the air; or the water surface stays rigid like glass under the stone; or the stone bends.
- P5 [fatal · permanence_count]
  - expect: One stone is thrown and nothing else appears on the water.
  - fail: The stone vanishes in mid-air or a second one appears; or it turns into another object; or it passes through the water without a splash and reappears.
- P6 [minor · attribute_drift]
  - expect: The stone, the lake's colour and the far shore stay the same.
  - fail: The stone changes colour or size in flight; or the lake changes colour between frames; or the far shore rearranges.

## MECH-0067 · projectile · train

**Caption.** A lawn sprinkler sends jets of water up and out over a garden, and the water falls onto the grass some distance away.

**Expectation (hidden).** Each jet rises, curves over, and descends; the water lands at a distance that matches how high it was thrown and does not stay up.

**Declared violation types.** trajectory_momentum, gravity_direction

**SA**
- S1 [core] A lawn sprinkler is running in a garden.
- S2 [core] It sends jets of water up and outward.
- S3 [core] The water comes down on the grass some distance from the sprinkler.
- S4 [minor] There are several jets rather than one.

**PC**
- P1 [core · trajectory_momentum]
  - expect: Each jet leaves the sprinkler along one direction and curves over in an arc.
  - fail: A jet travels in a straight line to the ground; or it bends upward in mid-air; or it kinks.
- P2 [core · gravity_direction]
  - expect: The water comes down after the peak and lands, and the higher jets land further out.
  - fail: Water hangs at the top of an arc; or it rises again after starting to fall; or it lands and lifts off the grass.
- P3 [major · material_response]
  - expect: The jets break into drops and spray as they fall, and the grass darkens and glistens where they land.
  - fail: The jets are rigid rods; or the grass stays dry where the water lands; or the water gathers into balls.
- P4 [major · causeless_motion]
  - expect: The sprinkler head turns or oscillates steadily and the pattern moves with it, while the sprinkler itself stays put.
  - fail: The sprinkler slides across the lawn; or the jets jump between directions unrelated to the head; or the head stops and the jets keep sweeping.
- P5 [fatal · permanence_count]
  - expect: One sprinkler is the only source of water.
  - fail: A second sprinkler appears; or water appears from nowhere away from the head; or the sprinkler turns into another object.
- P6 [minor · attribute_drift]
  - expect: The sprinkler, the lawn and the garden stay the same.
  - fail: The sprinkler changes colour or shape; or the lawn changes texture between frames; or the garden behind rearranges.

## MECH-0068 · projectile · train

**Caption.** A baseball is struck high into the outfield and comes down onto the grass far from where it was hit.

**Expectation (hidden).** The ball climbs in a long arc, slows near the top, and falls steadily; it does not level off or drop straight down.

**Declared violation types.** trajectory_momentum, gravity_direction

**SA**
- S1 [core] A baseball is struck.
- S2 [core] It goes high into the outfield.
- S3 [core] It comes down onto the grass.
- S4 [minor] It lands far from where it was hit.
- S5 [minor] The hit comes first, then the flight, then the landing.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The ball follows one long smooth arc, its forward motion continuing until it lands.
  - fail: The ball flies flat at a constant height; or it hangs at the top; or it changes direction in mid-air with nothing touching it.
- P2 [core · gravity_direction]
  - expect: It slows near the top and then falls steadily to the grass.
  - fail: The ball rises again after starting to fall; or it levels off and glides; or it drops straight down from the peak with no forward travel.
- P3 [major · causeless_motion]
  - expect: Nothing touches the ball in flight.
  - fail: The ball speeds up in mid-air; or it jinks sideways; or it stops and restarts.
- P4 [major · material_response]
  - expect: The ball hits the grass and bounces or rolls low, flattening the grass.
  - fail: The ball bounces higher than its flight; or it sinks into the ground; or it splashes.
- P5 [fatal · permanence_count]
  - expect: One ball is in play throughout.
  - fail: The ball vanishes in flight or a second one appears; or it turns into another object; or it passes through the ground.
- P6 [minor · attribute_drift]
  - expect: The ball, the field markings and the outfield stay the same.
  - fail: The ball changes colour in flight; or the field lines shift between frames; or the outfield wall rearranges.

## MECH-0069 · projectile · train

**Caption.** A snowball thrown across a snowy yard hits a wooden fence post and bursts into loose snow.

**Expectation (hidden).** The snowball arcs through the air, breaks apart on impact rather than bouncing off whole, and snow scatters and falls.

**Declared violation types.** trajectory_momentum, material_response

**SA**
- S1 [core] A snowball is thrown across a yard.
- S2 [core] It hits a wooden fence post.
- S3 [core] It bursts into loose snow.
- S4 [minor] The yard is snowy.
- S5 [minor] The throw comes first, then the hit, then the burst.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The snowball follows one arc to the post.
  - fail: The snowball flies flat; or it hangs in mid-air; or it changes direction with nothing touching it.
- P2 [core · material_response]
  - expect: It breaks apart on impact and the snow scatters and falls; it does not bounce off whole.
  - fail: The snowball bounces off whole like rubber; or it sticks to the post as one lump and stays; or it passes the post unchanged.
- P3 [major · gravity_direction]
  - expect: The loose snow falls to the ground after the burst.
  - fail: Snow hangs in the air after the burst; or it rises; or it stays stuck in a cloud.
- P4 [major · missing_consequence]
  - expect: The post shows the hit: a patch of snow on it or snow at its base.
  - fail: The post is pristine and the ground bare after the burst; or snow appears at the post before the ball arrives; or the post is knocked over by the snowball.
- P5 [fatal · solidity]
  - expect: The post stays solid and the snowball does not pass through it.
  - fail: The snowball passes through the post; or the post vanishes; or a second snowball appears in flight.
- P6 [minor · attribute_drift]
  - expect: The post, the fence and the yard stay the same.
  - fail: The post changes colour or height; or the fence rearranges between frames; or the yard changes.

## MECH-0070 · projectile · train

**Caption.** A frog on a lily pad leaps toward the bank of a pond and lands on it.

**Expectation (hidden).** The frog rises and comes down in an arc; the lily pad dips and bobs as it pushes off; the frog does not hover or change direction mid-air.

**Declared violation types.** trajectory_momentum, gravity_direction

**SA**
- S1 [core] A frog sits on a lily pad on a pond.
- S2 [core] It leaps toward the bank.
- S3 [core] It lands on the bank.
- S4 [minor] The leap comes first and the landing follows.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The frog rises and comes down in one arc toward the bank.
  - fail: The frog flies flat; or it hangs in mid-air; or it changes direction with nothing touching it.
- P2 [core · gravity_direction]
  - expect: After the peak it descends, lands on the bank and stays down.
  - fail: The frog hovers above the water; or it rises again after starting to fall; or it lands and bounces up high.
- P3 [major · missing_consequence]
  - expect: The lily pad dips and bobs as the frog pushes off, and ripples spread from it.
  - fail: The pad stays still and the water flat as the frog leaves; or the pad sinks entirely and stays under; or the pad moves before the frog moves.
- P4 [major · material_response]
  - expect: The frog lands with its legs folding, and the bank takes the landing.
  - fail: The frog lands rigid; or it sinks into the bank; or it splashes into the bank as if it were water.
- P5 [fatal · shape_identity]
  - expect: One frog keeps its limbs and shape, and it does not pass through the pad or the bank.
  - fail: A leg detaches or vanishes; or a second frog appears; or the frog passes through the lily pad.
- P6 [minor · attribute_drift]
  - expect: The frog's colour, the pad and the pond stay the same.
  - fail: The frog changes colour in flight; or the lily pad changes size between frames; or the pond's edge moves.

**Note.** The frog is kept because its body is the projectile. Its posture and how it looks in the air are not judged.

## MECH-0071 · projectile · train

**Caption.** A jogger comes to a wide puddle on a path, jumps over it, and lands on the far side.

**Expectation (hidden).** The jogger follows a shallow arc from take-off to landing with no hang time; the legs come forward for the landing.

**Declared violation types.** trajectory_momentum, gravity_direction

**SA**
- S1 [core] A jogger runs along a path toward a wide puddle.
- S2 [core] The jogger jumps over the puddle.
- S3 [core] The jogger lands on the far side.
- S4 [minor] The puddle is wide enough to need a jump rather than a step.
- S5 [minor] The run-up comes first, then the jump, then the landing.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The jogger follows one shallow arc from take-off to landing, the running speed carrying across the puddle.
  - fail: The jogger rises straight up and comes down on the near side; or hangs in the air; or changes direction in mid-air.
- P2 [core · gravity_direction]
  - expect: After the peak the jogger comes down and lands on the far side.
  - fail: The jogger hovers over the puddle; or rises again after starting down; or lands and bounces up high.
- P3 [major · causeless_motion]
  - expect: The run carries into the jump, and after landing the jogger runs on or stops by taking steps.
  - fail: The jogger slides forward on landing with feet planted; or is carried backward after landing; or speeds up in mid-air.
- P4 [major · material_response]
  - expect: The legs swing forward for the landing and bend as the feet take the weight, and the path takes the landing.
  - fail: The jogger lands stiff as a board; or sinks into the path on landing; or the path ripples under the landing.
- P5 [fatal · shape_identity]
  - expect: One jogger keeps limbs, number and shape, and does not pass through the ground.
  - fail: A limb stretches, detaches or vanishes; or the jogger passes through the path; or a second figure appears.
- P6 [minor · attribute_drift]
  - expect: The jogger's clothing, the puddle and the path stay the same.
  - fail: The clothing changes colour; or the puddle moves along the path between frames; or the surroundings rearrange.

**Note.** Biomechanics scene: the jogger is kept because the body is the projectile. Running form is not judged; only the arc and the order of take-off, flight and landing.

## MECH-0072 · projectile · train

**Caption.** A coin is flipped into the air and caught as it comes down.

**Expectation (hidden).** The coin spins as it rises, slows to a peak, and falls back to the hand; it does not hover at the top.

**Declared violation types.** trajectory_momentum, gravity_direction

**SA**
- S1 [core] A coin is flipped into the air.
- S2 [core] It rises and comes back down.
- S3 [core] It is caught as it comes down.
- S4 [minor] The coin tumbles as it flies rather than travelling flat.
- S5 [minor] The flip comes first and the catch follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The coin slows as it rises, peaks, and falls quicker on the way down.
  - fail: The coin hangs at the top; or it rises at an unchanging speed; or it falls at one slow unchanging drift.
- P2 [core · trajectory_momentum]
  - expect: It goes up and comes back along nearly the same line to the hand.
  - fail: The coin drifts far to one side with nothing touching it; or it jinks in mid-air; or it keeps rising out of the frame.
- P3 [major · causeless_motion]
  - expect: The coin tumbles end over end in the air and stops only in the hand.
  - fail: The coin stops spinning in mid-air and hangs; or it reverses its spin; or it sets off again after being caught.
- P4 [major · missing_consequence]
  - expect: The hand closes on the coin and the coin stops there.
  - fail: The coin passes through the hand; or the hand closes and the coin keeps falling; or the coin stops above the open hand.
- P5 [fatal · permanence_count]
  - expect: One coin is in the air throughout.
  - fail: The coin vanishes at the top or a second one appears; or it turns into another object; or it merges with the hand.
- P6 [minor · attribute_drift]
  - expect: The coin's colour and size and the background stay the same.
  - fail: The coin changes colour or size in flight; or the background rearranges between frames; or the hand changes.

**Note.** The hand is kept as the minimal trigger and catcher; the person behind it is not judged.

## MECH-0073 · projectile · train

**Caption.** A dart is thrown at a dartboard on a pub wall and sticks in the board.

**Expectation (hidden).** The dart flies point-first in a slight arc and stops dead on impact with its tip in the board; it does not pass through the board or float.

**Declared violation types.** trajectory_momentum, missing_consequence

**SA**
- S1 [core] A dart is thrown at a dartboard hanging on a wall.
- S2 [core] It flies to the board.
- S3 [core] It sticks in the board.
- S4 [minor] The dart stays in the board rather than dropping out.
- S5 [minor] The throw comes first and the dart sticking follows.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The dart flies point-first along one line with at most a slight dip.
  - fail: The dart flies tail-first; or it turns over in mid-air; or it changes direction with nothing touching it.
- P2 [core · missing_consequence]
  - expect: On reaching the board the dart stops with its tip in the board and its flight standing out.
  - fail: The dart passes through the board; or it stops in mid-air short of the board; or it hangs on the board by its flight.
- P3 [major · gravity_direction]
  - expect: In flight the dart's path dips slightly rather than climbing, and anything that falls goes down.
  - fail: The dart curves upward in flight; or it rises after sticking; or it hangs in the air.
- P4 [major · material_response]
  - expect: The board takes the point, the dart quivers briefly and holds, and the board stays on the wall.
  - fail: The board swings or falls off the wall at the hit; or the dart bends; or the board ripples like cloth.
- P5 [fatal · solidity]
  - expect: One dart and one board stay solid and separate from the wall.
  - fail: The dart passes through the board and the wall; or the dart vanishes; or a second dart appears.
- P6 [minor · attribute_drift]
  - expect: The dart's flight colour, the board's rings and the wall stay the same.
  - fail: The dart changes colour; or the board's numbers rearrange between frames; or the wall changes.

## MECH-0074 · projectile · train

**Caption.** A horse gallops toward a low fence, jumps over it, and lands on the far side.

**Expectation (hidden).** The horse leaves the ground before the fence, arcs over it, lands front legs first, and continues forward; it does not hover above the fence.

**Declared violation types.** trajectory_momentum, gravity_direction

**SA**
- S1 [core] A horse gallops toward a fence.
- S2 [core] It jumps over the fence.
- S3 [core] It lands on the far side.
- S4 [minor] The fence is low.
- S5 [minor] The gallop comes first, then the jump, then the landing.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The horse leaves the ground before the fence, arcs over it, lands beyond it and carries on forward.
  - fail: The horse takes off after passing the fence; or it changes direction in mid-air; or it lands behind where it took off.
- P2 [core · gravity_direction]
  - expect: After the peak the horse comes down, front legs first, without hovering.
  - fail: The horse hovers above the fence; or it rises again after starting down; or it lands and bounces high.
- P3 [major · causeless_motion]
  - expect: The gallop carries into the jump, and after landing the horse runs on.
  - fail: The horse stops dead on landing; or slides forward on planted legs; or speeds up in mid-air.
- P4 [major · material_response]
  - expect: The legs fold and extend through the jump, and the turf takes the landing.
  - fail: The horse lands rigid; or it sinks into the ground; or the turf ripples like water.
- P5 [fatal · shape_identity]
  - expect: One horse keeps its legs and shape, and it does not pass through the fence.
  - fail: A leg detaches or vanishes; or the horse passes through a rail; or a second horse appears.
- P6 [minor · attribute_drift]
  - expect: The horse's coat, the fence and the field stay the same.
  - fail: The coat changes colour; or the fence changes height between frames; or the field rearranges.

**Note.** The horse is the projectile; its body is the physics. Jumping form is not judged.

## MECH-0075 · projectile · train

**Caption.** A soccer ball is punted far down the field, and it lands and bounces near the far end.

**Expectation (hidden).** The ball soars in a high arc and descends steadily; on landing it bounces lower than its flight height and rolls.

**Declared violation types.** trajectory_momentum, gravity_direction

**SA**
- S1 [core] A soccer ball is punted.
- S2 [core] It travels far down the field.
- S3 [core] It lands and bounces near the far end.
- S4 [minor] The flight is long, reaching the far end of the field.
- S5 [minor] The punt comes first, then the flight, then the bounce.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The ball follows one high arc, its forward motion carrying it toward the far end.
  - fail: The ball flies flat; or it hangs at the top; or it changes direction in mid-air with nothing touching it.
- P2 [core · gravity_direction]
  - expect: It descends steadily after the peak, and on landing it bounces lower than its flight and rolls.
  - fail: The ball rises again after starting to fall; or it bounces higher than it flew; or it hovers above the grass.
- P3 [major · process_direction]
  - expect: Each bounce is lower than the one before.
  - fail: A later bounce is higher than the one before it; or the ball stops dead on first contact with no bounce or roll; or it bounces back toward the kicker.
- P4 [major · material_response]
  - expect: The ball squashes briefly on landing and springs back round, and the grass flattens under it.
  - fail: The ball stays flat after landing; or it sinks into the ground; or the ground ripples.
- P5 [fatal · permanence_count]
  - expect: One ball is in play throughout.
  - fail: The ball vanishes in flight or a second one appears; or it turns into another object; or it passes through the ground.
- P6 [minor · attribute_drift]
  - expect: The ball's panels, the field lines and the goal stay the same.
  - fail: The ball changes colour in flight; or the field markings shift between frames; or the goal changes shape.

## MECH-0076 · projectile · train

**Caption.** A dolphin swimming fast bursts out of the sea, arcs through the air, and splashes back in.

**Expectation (hidden).** The dolphin rises, slows at the top, and falls back into the water; it does not stay suspended above the surface or change direction mid-air.

**Declared violation types.** trajectory_momentum, gravity_direction

**SA**
- S1 [core] A dolphin swims fast near the surface.
- S2 [core] It bursts out of the sea.
- S3 [core] It arcs through the air.
- S4 [core] It splashes back in.
- S5 [minor] It is moving fast before the leap.
- S6 [minor] The burst comes first, then the arc, then the splash.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The dolphin follows one arc, its forward motion carrying through the leap.
  - fail: The dolphin goes straight up and comes straight down; or it changes direction in mid-air; or it stops in the air.
- P2 [core · gravity_direction]
  - expect: It rises, slows at the top, and falls back to the water.
  - fail: The dolphin hovers above the surface; or it rises again after starting to fall; or it lands and rests on top of the water.
- P3 [major · missing_consequence]
  - expect: The water breaks and sprays where the dolphin leaves, and there is a splash where it enters.
  - fail: The dolphin exits leaving the surface flat; or it enters with no splash; or the splash appears where it did not enter.
- P4 [major · material_response]
  - expect: Water streams off the body in the air and the splash falls back to the sea.
  - fail: The splash hangs in the air; or the water stands rigid like glass; or the body squashes.
- P5 [fatal · shape_identity]
  - expect: One dolphin keeps its fins and shape.
  - fail: A fin detaches or vanishes; or a second dolphin appears from nowhere; or the dolphin turns into another creature.
- P6 [minor · attribute_drift]
  - expect: The dolphin's colour, the sea and the horizon stay the same.
  - fail: The dolphin changes colour; or the horizon shifts between frames; or the sea changes colour.

## MECH-0077 · projectile · train

**Caption.** A rubber ball is dropped from shoulder height onto a concrete driveway and bounces several times before rolling away.

**Expectation (hidden).** Each bounce is lower than the one before and none is higher than the drop height; the bounces get quicker as they get smaller.

**Declared violation types.** trajectory_momentum, process_direction

**SA**
- S1 [core] A rubber ball is dropped from about shoulder height.
- S2 [core] It lands on a concrete driveway.
- S3 [core] It bounces several times.
- S4 [core] It rolls away.
- S5 [minor] The ball is dropped rather than thrown.
- S6 [minor] The drop comes first, then the bounces, then the roll.

**PC**
- P1 [core · process_direction]
  - expect: Each bounce is lower than the one before, none higher than the drop, and the bounces get quicker as they shrink.
  - fail: A bounce is higher than the one before it; or the bounces stay the same height; or the ball stops dead on first contact with no bounce.
- P2 [core · trajectory_momentum]
  - expect: The ball comes down straight from the hand and bounces close to vertical, drifting only a little before rolling.
  - fail: The ball shoots off sideways at the first bounce on the flat concrete; or it reverses direction between bounces; or it jinks in mid-air.
- P3 [major · gravity_direction]
  - expect: It falls quicker as it drops, and after each bounce it comes down again.
  - fail: The ball hangs at the top of a bounce; or it rises after the last bounce; or it floats.
- P4 [major · material_response]
  - expect: The ball squashes briefly at each contact and springs back round, and the concrete stays unmarked.
  - fail: The ball stays flat after a bounce; or it sinks into the concrete; or it splashes.
- P5 [fatal · permanence_count]
  - expect: One ball is there throughout.
  - fail: The ball vanishes or a second one appears; or it turns into another object; or it passes through the driveway.
- P6 [minor · attribute_drift]
  - expect: The ball's colour and the driveway stay the same.
  - fail: The ball changes colour or size; or the driveway's cracks shift between frames; or the surroundings rearrange.

## MECH-0079 · balance_topple · train

**Caption.** A block is pulled out of the bottom row of a tall wooden block tower and the tower collapses.

**Expectation (hidden).** The collapse starts as the support is removed, the tower sways then falls, and the blocks scatter on the table; it does not stand for long on nothing.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] A tall tower of wooden blocks stands on a table.
- S2 [core] A block is pulled out of the bottom row.
- S3 [core] The tower collapses.
- S4 [minor] It is the bottom row the block comes from.
- S5 [minor] The pull comes first and the collapse follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The collapse starts as the support is removed: the tower sways or leans, then falls; it does not stand for long on nothing.
  - fail: The tower stands unmoved on the gap for the rest of the clip; or it collapses before the block is pulled; or the tower collapses from the top while the bottom row with its gap stays intact.
- P2 [core · gravity_direction]
  - expect: Blocks fall downward, land on the table, and stay there.
  - fail: A block rises; or hangs in the air; or slides along the table with nothing pushing it after landing.
- P3 [major · trajectory_momentum]
  - expect: The tower comes apart as it falls and the blocks scatter outward from where it lands.
  - fail: The tower topples as one rigid piece and lands whole; or blocks fly upward and outward as if exploding; or the blocks fall and re-stack themselves.
- P4 [major · material_response]
  - expect: The blocks stay rigid, clatter, and bounce low at most.
  - fail: A block bends; or bounces higher than the tower stood; or splashes.
- P5 [fatal · permanence_count]
  - expect: The blocks keep their number, and the pulled block stays out of the tower.
  - fail: Blocks vanish or multiply; or a block passes through the table or another block; or the pulled block reappears in its place.
- P6 [minor · attribute_drift]
  - expect: The blocks' colours, the table and the room stay the same.
  - fail: A block changes colour or size; or the table changes between frames; or the room behind rearranges.

## MECH-0080 · balance_topple · train

**Caption.** A bicycle resting on its kickstand is hit by a stray soccer ball and falls over onto its side.

**Expectation (hidden).** The bike rocks, leans further, and hits the ground; it falls on the side away from the kickstand's support and does not right itself.

**Declared violation types.** gravity_direction, trajectory_momentum

**SA**
- S1 [core] A bicycle rests on its kickstand.
- S2 [core] A soccer ball hits the bicycle.
- S3 [core] The bicycle falls over onto its side.
- S4 [minor] The hit comes first and the fall follows.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The bike rocks at the hit, leans further, and falls on the side away from the kickstand's support.
  - fail: The bike falls toward the kickstand side, over the stand; or it rights itself after leaning; or it falls before the ball arrives.
- P2 [core · gravity_direction]
  - expect: Once past its balance the bike goes down until it hits the ground and stays there.
  - fail: The bike hangs leaning in mid-fall; or it rises; or it bounces back upright.
- P3 [major · missing_consequence]
  - expect: The ball's arrival is what moves the bike, and the ball rebounds or drops after hitting.
  - fail: The ball passes the bike without touching it and the bike falls anyway; or the ball hits and stops dead in the air; or the ball sticks to the bike.
- P4 [major · material_response]
  - expect: The frame stays rigid, the wheels may spin, the kickstand may fold.
  - fail: The frame bends; or the bike bounces high off the ground; or a wheel squashes.
- P5 [fatal · permanence_count]
  - expect: One bicycle and one ball keep their number and shape.
  - fail: The bike vanishes or a second one appears; or the ball passes through the frame; or the bike turns into another object.
- P6 [minor · attribute_drift]
  - expect: The bike's colour, the ball and the surroundings stay the same.
  - fail: The bike changes colour; or the ball changes size; or the background rearranges.

## MECH-0081 · balance_topple · train

**Caption.** A man sitting in a dining chair leans back until only the two rear legs are on the floor, leans a little further, and tips over backward with the chair.

**Expectation (hidden).** The fall begins once he leans past the balance point and speeds up; he and the chair land on the floor behind him; the chair does not hang balanced.

**Declared violation types.** gravity_direction, trajectory_momentum

**SA**
- S1 [core] A man sits in a dining chair.
- S2 [core] He leans back until only the rear legs are on the floor.
- S3 [core] He leans a little further.
- S4 [core] He and the chair tip over backward.
- S5 [minor] The front legs are off the floor before the tip.
- S6 [minor] The lean comes first, then the balance on two legs, then the fall.

**PC**
- P1 [core · gravity_direction]
  - expect: The chair balances on its rear legs while he is near the tipping point; once past it the fall begins and speeds up.
  - fail: The chair hangs balanced far past upright for the rest of the clip; or the fall slows as it goes; or he rises off the chair.
- P2 [core · trajectory_momentum]
  - expect: They fall backward together and land behind where the chair stood.
  - fail: They fall forward; or the man falls and the chair stays upright; or they fall sideways.
- P3 [major · causeless_motion]
  - expect: Nothing pushes him; the tip comes from his own lean.
  - fail: The chair tips before he leans; or it slides across the floor; or it rights itself after starting to fall.
- P4 [major · material_response]
  - expect: The chair stays rigid in legs and back, and the floor takes the impact.
  - fail: The chair legs bend; or the chair bounces high; or the man's body folds like cloth.
- P5 [fatal · shape_identity]
  - expect: The man and the chair keep their number and shape, and neither passes into the other or the floor.
  - fail: He merges with the chair; or a limb detaches; or the chair passes through the floor.
- P6 [minor · attribute_drift]
  - expect: His clothing, the chair and the room stay the same.
  - fail: His clothing changes colour; or the chair changes design between frames; or the room rearranges.

**Note.** Balance scene: the man is kept because his body is the load that moves the balance point. His expression and how gracefully he falls are not judged.

## MECH-0082 · balance_topple · train

**Caption.** The top cup of a tower of stacked plastic cups on a carpet is swiped sideways, and the top of the tower falls.

**Expectation (hidden).** The struck cup flies off in the direction of the swipe, the cups below wobble and some fall; cups do not float or fall before being disturbed.

**Declared violation types.** gravity_direction, trajectory_momentum

**SA**
- S1 [core] A tower of stacked plastic cups stands on a carpet.
- S2 [core] The top cup is swiped sideways.
- S3 [core] The top of the tower falls.
- S4 [minor] Only the top cup is swiped.
- S5 [minor] The swipe comes first and the fall follows.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The struck cup flies off in the direction of the swipe, and the cups below wobble and some fall.
  - fail: The struck cup flies against the swipe; or the whole tower drops straight down as one piece; or the bottom cups fall while the top stays.
- P2 [core · gravity_direction]
  - expect: Cups that leave the tower fall to the carpet and stay there.
  - fail: A cup hangs in the air; or rises; or lands and bounces back onto the tower.
- P3 [major · causeless_motion]
  - expect: Cups move only after being struck or losing their support.
  - fail: Cups fall before the swipe; or a landed cup slides with nothing touching it; or a lower cup jumps off untouched while the tower above it stays.
- P4 [major · material_response]
  - expect: The plastic cups are light and stiff: they bounce and roll on the carpet without breaking.
  - fail: A cup shatters; or squashes flat and stays flat; or the carpet ripples like water.
- P5 [fatal · permanence_count]
  - expect: The cups keep their number and pass through nothing.
  - fail: Cups vanish or multiply; or a cup passes through another; or a cup turns into another object.
- P6 [minor · attribute_drift]
  - expect: The cups' colours, the carpet and the room stay the same.
  - fail: A cup changes colour or size; or the carpet changes pattern between frames; or the room rearranges.

## MECH-0083 · balance_topple · train

**Caption.** An elbow knocks a full wine glass on a table; it tips over and the wine spills across the tablecloth.

**Expectation (hidden).** The glass falls in the direction it was knocked, the wine pours out as it goes over and spreads on the cloth; the glass does not swing back upright.

**Declared violation types.** gravity_direction, material_response

**SA**
- S1 [core] A full wine glass stands on a table.
- S2 [core] An elbow knocks the glass.
- S3 [core] The glass tips over.
- S4 [core] The wine spills across the tablecloth.
- S5 [minor] The glass is full before the knock.
- S6 [minor] The knock comes first, then the tip, then the spill.

**PC**
- P1 [core · gravity_direction]
  - expect: The glass falls the way it was knocked and does not swing back upright.
  - fail: The glass rights itself; or it tips toward the elbow; or it hangs leaning without falling.
- P2 [core · material_response]
  - expect: The wine pours out as the glass goes over and spreads across the cloth as a liquid, soaking in.
  - fail: The wine stays in the glass on its side; or it leaves as a solid lump; or it beads up and rolls off the cloth without soaking in.
- P3 [major · gravity_direction]
  - expect: Spilled wine runs down onto the cloth and spreads outward, not back up the glass.
  - fail: Wine climbs the glass; or the puddle shrinks back into the glass; or wine floats.
- P4 [major · missing_consequence]
  - expect: The cloth darkens where the wine reaches it.
  - fail: Wine pours and the cloth stays dry; or a stain appears where no wine went; or the stain appears before the glass tips.
- P5 [fatal · permanence_count]
  - expect: One glass, and wine leaves it only over the rim.
  - fail: The glass vanishes or a second one appears; or wine passes through the wall of the glass; or the wine level rises while spilling.
- P6 [minor · attribute_drift]
  - expect: The wine's colour, the glass and the table setting stay the same.
  - fail: The wine changes colour; or the glass changes shape; or the table setting rearranges between frames.

**Note.** The elbow is kept as the minimal trigger; the person behind it is not judged.

## MECH-0084 · balance_topple · train

**Caption.** The tall thin tower on top of a sandcastle is tapped with a plastic shovel, and the tower crumbles and slides down the side of the castle.

**Expectation (hidden).** The sand breaks into loose grains and clumps that fall downward; the tower does not tip over as a rigid piece or stay standing.

**Declared violation types.** material_response, gravity_direction

**SA**
- S1 [core] A sandcastle has a tall thin tower on top.
- S2 [core] The tower is tapped with a plastic shovel.
- S3 [core] The tower crumbles.
- S4 [core] The sand slides down the side of the castle.
- S5 [minor] The shovel is plastic.
- S6 [minor] The tap comes first, then the crumble, then the slide.

**PC**
- P1 [core · material_response]
  - expect: The sand breaks into loose grains and clumps rather than tipping over as a rigid piece.
  - fail: The tower tips over whole and lands intact; or it bends; or it stays standing after the tap with only a dent.
- P2 [core · gravity_direction]
  - expect: Loose sand falls and slides downward over the castle's side and piles at the base.
  - fail: Sand rises; or hangs in the air; or slides up the side.
- P3 [major · missing_consequence]
  - expect: The crumbling begins at the tap, where the shovel lands.
  - fail: The tower crumbles before the shovel touches it; or the shovel taps and nothing happens for the rest of the clip; or the base crumbles while the tapped top stays.
- P4 [major · material_response]
  - expect: The rest of the castle stays put apart from where the sliding sand runs over it.
  - fail: The whole castle collapses from one tap on the tower; or the castle ripples like liquid; or the sliding sand bounces like balls.
- P5 [fatal · permanence_count]
  - expect: One castle and one shovel, and sand comes only from the tower.
  - fail: The tower reappears; or a second tower appears; or the shovel passes through the castle; or the sand vanishes mid-slide.
- P6 [minor · attribute_drift]
  - expect: The sand's colour, the castle and the beach stay the same.
  - fail: The sand changes colour; or the castle's other parts change shape between frames; or the beach rearranges.

## MECH-0085 · balance_topple · train

**Caption.** A snowman's head is knocked sideways by a thrown snowball, rolls off the body, and drops to the snow.

**Expectation (hidden).** The head moves at the moment of impact in the direction of the throw, falls to the ground, and may break apart; it does not hover above the shoulders.

**Declared violation types.** gravity_direction, material_response

**SA**
- S1 [core] A snowman stands with its head in place.
- S2 [core] A thrown snowball hits the head.
- S3 [core] The head is knocked sideways and rolls off the body.
- S4 [core] The head drops to the snow.
- S5 [minor] The snowball comes in through the air.
- S6 [minor] The hit comes first, then the roll off, then the drop.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The head moves at the moment of impact, in the direction of the throw, and rolls off that side.
  - fail: The head moves toward the thrower; or it moves before the snowball arrives; or it lifts straight up.
- P2 [core · gravity_direction]
  - expect: Once off the shoulders the head falls to the snow and stays there.
  - fail: The head hovers above the shoulders; or rises; or bounces back onto the body.
- P3 [major · material_response]
  - expect: The head is packed snow: it may dent, crack or break apart when it lands, and the snowball bursts or sticks.
  - fail: The head bounces like rubber; or shatters like glass into shards; or the snowball passes through it.
- P4 [major · causeless_motion]
  - expect: The body stays standing and nothing else moves.
  - fail: The body topples too with nothing hitting it; or the arms fly off; or the head rolls back up onto the body.
- P5 [fatal · permanence_count]
  - expect: One snowman and one snowball keep their number.
  - fail: The head vanishes or a second head appears; or the snowman turns into another object; or the snowball vanishes in flight.
- P6 [minor · attribute_drift]
  - expect: The snowman's features, the scarf and the yard stay the same.
  - fail: The face changes; or the scarf changes colour; or the yard rearranges.

## MECH-0086 · balance_topple · train

**Caption.** A pyramid of empty soda cans at a carnival booth is hit by a tennis ball, and the cans fly off and fall to the counter.

**Expectation (hidden).** The struck cans fly backward first, the cans above them lose support and fall; cans move only after being hit or losing support.

**Declared violation types.** trajectory_momentum, gravity_direction

**SA**
- S1 [core] A pyramid of empty soda cans stands on a booth counter.
- S2 [core] A tennis ball hits the pyramid.
- S3 [core] Cans fly off.
- S4 [core] Cans fall to the counter.
- S5 [minor] The cans are stacked as a pyramid.
- S6 [minor] The hit comes first, then the flying cans, then the fall.

**PC**
- P1 [core · trajectory_momentum]
  - expect: Struck cans fly away from the ball, and cans above them lose their support and drop.
  - fail: Cans fly toward the thrower; or all the cans move as one block; or cans on the far side move while the struck ones stay.
- P2 [core · gravity_direction]
  - expect: Cans come down to the counter or the floor and stay there.
  - fail: A can hangs in the air; or rises; or lands and re-stacks.
- P3 [major · causeless_motion]
  - expect: Cans move only after being hit or losing support.
  - fail: Cans topple before the ball arrives; or a landed can slides off untouched; or a can jumps from the base while the top stays.
- P4 [major · material_response]
  - expect: Empty cans are light and dent easily; they clatter and roll rather than shatter.
  - fail: A can shatters; or squashes flat and re-inflates; or the ball dents deeply and stays dented.
- P5 [fatal · permanence_count]
  - expect: The cans keep their number and the ball stays one ball.
  - fail: Cans vanish or multiply; or a can passes through another; or the ball vanishes at the hit.
- P6 [minor · attribute_drift]
  - expect: The cans' labels, the counter and the booth stay the same.
  - fail: A can changes label or colour; or the counter changes between frames; or the booth rearranges.

## MECH-0087 · balance_topple · train

**Caption.** Two heavy sacks sit on opposite ends of a level seesaw; one sack is dragged off its end, and the other end drops to the ground.

**Expectation (hidden).** The drop happens as soon as the sack's weight leaves the seat; the emptied end rises at the same time; the beam does not stay level.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] Two sacks sit on opposite ends of a seesaw.
- S2 [core] The seesaw is level at the start.
- S3 [core] One sack is dragged off its end.
- S4 [core] The other end drops to the ground.
- S5 [minor] The sack is dragged off first and the drop follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The drop happens as soon as the sack's weight leaves the seat, not before and not long after.
  - fail: The beam stays level after one sack is gone; or the end drops before the sack has left it; or the still-loaded end rises.
- P2 [core · gravity_direction]
  - expect: The loaded end goes down to the ground and the emptied end rises at the same time.
  - fail: Both ends go down; or the loaded end rises; or the beam floats level with only one sack on it.
- P3 [major · trajectory_momentum]
  - expect: The beam pivots about its centre, and the remaining sack rides down with its end and may slide toward the low end.
  - fail: The beam slides off its pivot; or the sack slides uphill; or the sack lifts off the seat.
- P4 [major · material_response]
  - expect: The beam stays rigid, and the sacks are heavy and floppy, sagging where they sit.
  - fail: The beam bends like rubber; or a sack bounces high; or a sack stays rigid as a box.
- P5 [fatal · permanence_count]
  - expect: Two sacks and one seesaw keep their number and shape.
  - fail: A sack vanishes or a third appears; or a sack passes through the beam; or the seesaw turns into another object.
- P6 [minor · attribute_drift]
  - expect: The sacks' colour, the seesaw and the ground stay the same.
  - fail: A sack changes colour or size; or the seesaw changes length between frames; or the ground rearranges.

## MECH-0088 · balance_topple · train

**Caption.** A hardback book is pushed slowly toward the edge of a table until it tips over the edge and falls to the floor.

**Expectation (hidden).** The book stays flat and still on the table while most of it is still supported; it tips only once most of its length is past the edge, turning over the edge as it goes and landing below it; it does not fall while barely overhanging, hang far out over the edge without tipping, drift off flat without turning, or float.

**Declared violation types.** gravity_direction, causeless_motion, trajectory_momentum

**SA**
- S1 [core] A hardback book lies on a table.
- S2 [core] It is pushed slowly toward the edge.
- S3 [core] It tips over the edge.
- S4 [core] It falls to the floor.
- S5 [minor] The push is slow rather than a shove.
- S6 [minor] The push comes first, then the tip, then the fall.

**PC**
- P1 [core · gravity_direction]
  - expect: The book stays flat and still while most of it is supported, and tips only once most of its length is past the edge.
  - fail: The book falls while barely overhanging; or it hangs far out over the edge without tipping; or it lifts off the table.
- P2 [core · trajectory_momentum]
  - expect: It turns over the edge as it goes and lands below it.
  - fail: It drifts off flat without turning; or it flies outward from the table; or it lands back on the table.
- P3 [major · causeless_motion]
  - expect: The book moves only while pushed and stays where it lands.
  - fail: It slides on its own before or after the push; or it sets off again on the floor; or it moves back from the edge untouched.
- P4 [major · material_response]
  - expect: The hard cover stays rigid and the pages may fan, and the floor takes the impact.
  - fail: The book bends like rubber; or it bounces high; or it passes into the floor.
- P5 [fatal · permanence_count]
  - expect: One book is there throughout.
  - fail: The book vanishes or a second one appears; or it turns into another object; or it passes through the table.
- P6 [minor · attribute_drift]
  - expect: The book's cover, the table and the floor stay the same.
  - fail: The cover changes colour or design; or the table changes between frames; or the floor rearranges.

## MECH-0089 · balance_topple · train

**Caption.** A stack of textbooks is balanced on the palm of a hand; the hand tilts to one side, and the books slide off and fall to the floor.

**Expectation (hidden).** The books slide toward the low side of the hand and fall from there; they do not stay on the tilted palm or fall toward the high side.

**Declared violation types.** gravity_direction, trajectory_momentum

**SA**
- S1 [core] A stack of textbooks is balanced on the palm of a hand.
- S2 [core] The hand tilts to one side.
- S3 [core] The books slide off.
- S4 [core] They fall to the floor.
- S5 [minor] Several books are stacked rather than one.
- S6 [minor] The tilt comes first, then the slide, then the fall.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The books slide toward the low side of the hand and fall from there.
  - fail: They slide toward the high side; or they stay on the tilted palm; or they lift off the hand.
- P2 [core · gravity_direction]
  - expect: Once off the hand they drop to the floor and stay there.
  - fail: They hang in the air; or rise; or land and re-stack.
- P3 [major · causeless_motion]
  - expect: The books stay put on the level palm and move only as the tilt grows.
  - fail: They slide before the hand tilts; or they move again after landing; or they jump off as a block while the hand is level.
- P4 [major · material_response]
  - expect: The books stay rigid, may fan open, and clatter on the floor.
  - fail: They bend like rubber; or bounce high; or splash.
- P5 [fatal · permanence_count]
  - expect: The books keep their number and pass through nothing.
  - fail: Books vanish or multiply; or a book passes through the hand; or a book turns into another object.
- P6 [minor · attribute_drift]
  - expect: The books' covers, the hand and the room stay the same.
  - fail: A cover changes colour; or the hand changes; or the room rearranges between frames.

**Note.** The hand is kept as the balancing surface; the person behind it is not judged.

## MECH-0090 · balance_topple · train

**Caption.** A cyclist comes to a stop at a light with both feet still on the pedals, the bicycle leans to one side, and cyclist and bike fall over together.

**Expectation (hidden).** The lean grows steadily into a fall toward the low side; the bike does not stay upright unsupported or fall toward the high side.

**Declared violation types.** gravity_direction, causeless_motion

**SA**
- S1 [core] A cyclist comes to a stop at a light.
- S2 [core] Both feet stay on the pedals.
- S3 [core] The bicycle leans to one side.
- S4 [core] Cyclist and bike fall over together.
- S5 [minor] A traffic light is visible.
- S6 [minor] The stop comes first, then the lean, then the fall.

**PC**
- P1 [core · gravity_direction]
  - expect: The lean grows steadily into a fall toward the low side, and nothing holds them up.
  - fail: The bike stays upright unsupported with the feet on the pedals; or it falls toward the high side; or it rights itself.
- P2 [core · causeless_motion]
  - expect: The lean starts once the bike has stopped, and nothing pushes it.
  - fail: The bike topples while still rolling forward; or it slides sideways; or it falls before stopping.
- P3 [major · trajectory_momentum]
  - expect: Cyclist and bike go down together as one and land beside where they stopped.
  - fail: The bike falls and the cyclist stays upright in the air; or they separate and fly apart; or they fall forward over the handlebars.
- P4 [major · material_response]
  - expect: The frame stays rigid, and the rider's body folds on landing.
  - fail: The frame bends; or the rider lands rigid as a statue; or the bike bounces high.
- P5 [fatal · shape_identity]
  - expect: The cyclist and the bike keep their number and shape, and neither passes into the other or the road.
  - fail: The cyclist merges with the bike; or a limb detaches; or the bike passes through the road.
- P6 [minor · attribute_drift]
  - expect: The cyclist's clothing, the bike and the street stay the same.
  - fail: The clothing changes colour; or the bike changes design; or the street rearranges.

**Note.** Balance scene: the cyclist is kept because the body is the load. Riding skill and how the fall looks are not judged.

## MECH-0091 · balance_topple · train

**Caption.** A wooden spoon is balanced across the rim of a pot and a heavy ladle set on one end, and the spoon tips and the ladle falls into the pot.

**Expectation (hidden).** The weighted end goes down as soon as the ladle is set on it; the spoon tips off the rim; nothing stays balanced on nothing.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] A wooden spoon is balanced across the rim of a pot.
- S2 [core] A ladle is set on one end of the spoon.
- S3 [core] The spoon tips.
- S4 [core] The ladle falls into the pot.
- S5 [minor] The ladle is set on first and the tip follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The weighted end goes down as soon as the ladle is set on it.
  - fail: The spoon stays level with the ladle on one end; or it tips before the ladle touches it; or the empty end goes down.
- P2 [core · gravity_direction]
  - expect: The spoon tips off the rim and the ladle drops into the pot and stays there.
  - fail: The ladle hangs in the air; or rises; or lands and balances on the rim.
- P3 [major · trajectory_momentum]
  - expect: The spoon pivots on the rim, the ladle slides toward the low end and falls in, and the spoon may follow.
  - fail: The spoon slides off along the rim without tipping; or the ladle slides uphill; or the spoon flips over and lands back balanced.
- P4 [major · material_response]
  - expect: The spoon, the ladle and the pot stay rigid and clatter.
  - fail: The spoon bends like rubber; or the pot's rim dents; or the ladle bounces high out of the pot.
- P5 [fatal · permanence_count]
  - expect: One spoon, one ladle and one pot keep their number.
  - fail: The ladle vanishes or a second appears; or the spoon passes through the pot; or the pot turns into another object.
- P6 [minor · attribute_drift]
  - expect: The spoon, the ladle and the pot stay the same.
  - fail: The spoon changes colour; or the ladle changes size; or the pot changes between frames.

## MECH-0092 · balance_topple · train

**Caption.** A person carrying a stack of dinner plates in one hand trips on a rug, and the plates slide off and shatter on the floor.

**Expectation (hidden).** The plates leave the hand as the person stumbles, fall to the floor, and break on impact; they do not break in the air or float.

**Declared violation types.** gravity_direction, material_response

**SA**
- S1 [core] A person carries a stack of dinner plates in one hand.
- S2 [core] The person trips on a rug.
- S3 [core] The plates slide off the hand.
- S4 [core] They shatter on the floor.
- S5 [minor] The rug is where the trip happens.
- S6 [minor] The trip comes first, then the slide, then the shattering.

**PC**
- P1 [core · gravity_direction]
  - expect: The plates leave the hand as the person stumbles and fall to the floor.
  - fail: The plates hang in the air; or they rise; or they stay on the hand while the person falls.
- P2 [core · material_response]
  - expect: The plates break on impact and the pieces scatter; they do not break in the air or bounce whole.
  - fail: They break in mid-air; or bounce off the floor whole; or flatten like dough.
- P3 [major · causeless_motion]
  - expect: The foot catches on the rug and the body pitches forward, and the plates go with it.
  - fail: The person trips on bare floor away from the rug; or the plates fly before the trip; or they fly backward.
- P4 [major · trajectory_momentum]
  - expect: The plates are thrown forward, the way the person was going.
  - fail: They go backward; or straight up; or scatter from a point on the floor before landing.
- P5 [fatal · shape_identity]
  - expect: The person keeps their limbs and shape, and the plates keep their number until they break.
  - fail: A limb detaches; or plates multiply in the air; or the person passes through the floor.
- P6 [minor · attribute_drift]
  - expect: The plates' pattern, the rug and the room stay the same.
  - fail: The plates change pattern; or the rug changes colour; or the room rearranges.

**Note.** The person is kept because their stumble is what launches the plates. Their balance and how they fall are not judged.

## MECH-0093 · balance_topple · train

**Caption.** The top of a tall unanchored bookshelf is pulled forward; the shelf tips forward and falls, spilling books.

**Expectation (hidden).** The shelf leans toward the pull, the books slide off the shelves as it tilts, and it falls to the floor; it does not fall backward or stop mid-tilt.

**Declared violation types.** gravity_direction, trajectory_momentum

**SA**
- S1 [core] A tall bookshelf stands with books on its shelves.
- S2 [core] The top of the shelf is pulled forward.
- S3 [core] The shelf tips forward and falls.
- S4 [core] Books spill out.
- S5 [minor] The pull is at the top of the shelf.
- S6 [minor] The pull comes first, then the tip, then the spill.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The shelf leans toward the pull, the top moving first, and falls to that side.
  - fail: The shelf falls backward; or the bottom moves first; or it stops mid-tilt and hangs.
- P2 [core · gravity_direction]
  - expect: The books slide off the shelves as it tilts and fall to the floor, and the shelf comes down.
  - fail: Books stay on the shelves through the fall; or rise; or hang in the air.
- P3 [major · causeless_motion]
  - expect: Nothing moves until the pull.
  - fail: The shelf leans before it is pulled; or books slide off while it stands upright; or it rights itself.
- P4 [major · material_response]
  - expect: The shelf stays a rigid case, and the books thud and fan.
  - fail: The shelf folds like cardboard; or books bounce high; or the shelf passes into the floor.
- P5 [fatal · permanence_count]
  - expect: One shelf and its books keep their number.
  - fail: The shelf vanishes or a second appears; or books multiply; or the shelf turns into another object.
- P6 [minor · attribute_drift]
  - expect: The shelf's wood, the books and the room stay the same.
  - fail: The shelf changes colour; or the books change covers; or the room rearranges.

## MECH-0095 · tension · train

**Caption.** A large dog on a leash tied to a post spots a squirrel and lunges after it; the leash snaps taut and the dog is stopped short.

**Expectation (hidden).** The leash goes from slack to straight at the instant the dog reaches its end; the dog stops at that same instant, not before, and the post does not move.

**Declared violation types.** material_response, causeless_motion

**SA**
- S1 [core] A dog is on a leash tied to a post.
- S2 [core] The dog lunges forward.
- S3 [core] The leash snaps taut.
- S4 [core] The dog is stopped short.
- S5 [minor] A squirrel is what the dog goes for.
- S6 [minor] The lunge comes first, then the taut leash, then the stop.

**PC**
- P1 [core · material_response]
  - expect: The leash goes from slack to straight at the instant the dog reaches its end; it does not stretch like elastic.
  - fail: The leash stretches on and on as the dog keeps going; or it stays curved while the dog is plainly held; or it goes taut while the dog is still standing.
- P2 [core · causeless_motion]
  - expect: The dog stops at the instant the leash goes tight and not before.
  - fail: The dog stops before the leash straightens; or it keeps running past the leash's length; or it is thrown back before the leash is taut.
- P3 [major · missing_consequence]
  - expect: The post holds and does not move, and the dog is jerked back or pulled up.
  - fail: The post bends or comes out of the ground; or the dog keeps going with the leash trailing; or the leash detaches without breaking.
- P4 [major · gravity_direction]
  - expect: The taut leash runs straight from collar to post, and a slack leash droops.
  - fail: A slack leash floats in a curve above the ground; or the taut leash sags; or the dog is lifted off the ground.
- P5 [fatal · shape_identity]
  - expect: One dog, one leash and one post keep their number and shape.
  - fail: The leash passes through the dog or the post; or the dog duplicates; or the leash vanishes.
- P6 [minor · attribute_drift]
  - expect: The dog's coat, the leash and the post stay the same.
  - fail: The coat changes pattern; or the leash changes colour; or the post changes between frames.

**Note.** The dog is self-driven: its speed, reaction and where it looks are not judged. Only the leash's response and the timing of the stop are.

## MECH-0096 · tension · train

**Caption.** A basket of wet laundry is hung from the middle of a clothesline strung between two posts, and the line sags under the weight.

**Expectation (hidden).** The sag forms as the basket is hung, is deepest at the basket, and the line stays straight between basket and posts; it does not stay level.

**Declared violation types.** material_response, gravity_direction

**SA**
- S1 [core] A clothesline is strung between two posts.
- S2 [core] A basket of laundry is hung from the middle of the line.
- S3 [core] The line sags under the weight.
- S4 [minor] The laundry is wet.
- S5 [minor] The basket is hung first and the sag follows.

**PC**
- P1 [core · material_response]
  - expect: The sag forms as the basket is hung, deepest at the basket, with the line running straight from basket to each post.
  - fail: The line stays level with the basket hanging; or it sags in a rounded droop away from the basket; or it stretches longer and longer.
- P2 [core · gravity_direction]
  - expect: The sag is downward and the basket hangs below the line's ends.
  - fail: The line bows upward; or the basket rises; or the basket hangs out sideways.
- P3 [major · missing_consequence]
  - expect: The posts lean inward or the line tugs at them as the weight comes on.
  - fail: The posts lean outward; or the line goes slack while the basket hangs; or the basket falls with the line intact and unbroken.
- P4 [major · causeless_motion]
  - expect: The basket swings a little and settles, and nothing else moves.
  - fail: The basket swings harder and harder; or it slides along the line untouched; or the line moves before the basket is hung.
- P5 [fatal · permanence_count]
  - expect: One line, one basket and two posts keep their number.
  - fail: The basket vanishes or a second appears; or the line passes through the basket; or a post disappears.
- P6 [minor · attribute_drift]
  - expect: The basket, the laundry and the yard stay the same.
  - fail: The basket changes colour; or the laundry changes; or the yard rearranges.

## MECH-0097 · tension · train

**Caption.** A kite tied by its string to a fence post is lifted by a steady wind, and the string pulls taut from the post up to the kite.

**Expectation (hidden).** The string runs in a shallow taut curve and tugs at the post; it does not hang slack while the kite is flying.

**Declared violation types.** material_response, gravity_direction

**SA**
- S1 [core] A kite is tied by a string to a fence post.
- S2 [core] The kite is lifted into the air by the wind.
- S3 [core] The string is taut from the post up to the kite.
- S4 [minor] The wind is steady and the kite holds rather than diving.
- S5 [minor] The lift comes first and the taut string follows.

**PC**
- P1 [core · material_response]
  - expect: The string runs in a shallow taut curve from post to kite and does not hang slack while the kite flies.
  - fail: The string droops in loose loops while the kite is up; or it stretches; or it runs straight down from the kite to the ground with the kite still flying.
- P2 [core · gravity_direction]
  - expect: The kite is above the post with the string climbing from post to kite, and a slack string falls.
  - fail: The kite is below the post with the string taut; or the string curves upward away from the kite; or the kite rises straight up and stays overhead with no lean downwind.
- P3 [major · missing_consequence]
  - expect: The string tugs at the post, and the post or the knot shows the pull.
  - fail: The kite flies with the string not attached to anything; or the string is attached but the kite drifts away with it trailing; or the post pulls out of the ground.
- P4 [major · causeless_motion]
  - expect: The kite bobs and shifts with the wind but stays at the string's end and does not dart against the wind.
  - fail: The kite flies upwind of the post; or it swoops in circles unrelated to the string; or it hovers with the string slack.
- P5 [fatal · permanence_count]
  - expect: One kite, one string and one post keep their number.
  - fail: The kite vanishes or a second appears; or the string passes through the post; or the kite turns into another object.
- P6 [minor · attribute_drift]
  - expect: The kite's colours, the string and the fence stay the same.
  - fail: The kite changes colour or shape; or the string changes; or the fence rearranges.

## MECH-0098 · tension · train

**Caption.** A bucket full of water is hauled up out of a well on a rope.

**Expectation (hidden).** The rope hangs straight down to the bucket and stays taut while it is pulled; the bucket rises only as fast as rope is pulled in and swings gently, and water may slop over its rim; it does not rise on its own or while the rope is slack.

**Declared violation types.** material_response, gravity_direction

**SA**
- S1 [core] A bucket hangs in a well on a rope.
- S2 [core] The rope is pulled.
- S3 [core] The bucket rises up out of the well.
- S4 [minor] The bucket is full of water.

**PC**
- P1 [core · material_response]
  - expect: The rope hangs straight down to the bucket and stays taut while pulled, and the bucket rises only as fast as rope is taken in.
  - fail: The rope goes slack while the bucket rises; or the rope stretches; or the bucket rises faster than the rope is taken in.
- P2 [core · gravity_direction]
  - expect: The bucket hangs below the rope, swinging gently, with the water level in it and any slop running down.
  - fail: The bucket rises on its own with the rope slack; or it hangs sideways; or water rises out of the bucket.
- P3 [major · causeless_motion]
  - expect: The bucket rises only while the rope is pulled and stops when the pull stops.
  - fail: The bucket rises with no pull; or it keeps rising after the pull stops; or it descends while being pulled.
- P4 [major · material_response]
  - expect: The water slops and settles, and the bucket stays rigid.
  - fail: The water stays a rigid block; or the bucket bends; or water floats.
- P5 [fatal · permanence_count]
  - expect: One bucket and one rope keep their number.
  - fail: The bucket vanishes or a second appears; or the rope passes through the bucket's handle; or the bucket turns into another object.
- P6 [minor · attribute_drift]
  - expect: The bucket, the rope and the well stay the same.
  - fail: The bucket changes colour; or the rope changes; or the well's stonework rearranges.

## MECH-0099 · tension · train

**Caption.** A heavy sack is dropped into an empty hammock strung between two trees, and the hammock sags deeply under it.

**Expectation (hidden).** The sag forms as the weight lands, the ropes pull straight to the trees, and the hammock swings gently before settling.

**Declared violation types.** material_response, gravity_direction

**SA**
- S1 [core] An empty hammock hangs between two trees.
- S2 [core] A sack is dropped into it.
- S3 [core] The hammock sags deeply under the sack.
- S4 [minor] The hammock is empty before the drop.
- S5 [minor] The drop comes first and the sag follows.

**PC**
- P1 [core · material_response]
  - expect: The sag forms as the weight lands, deepest under the sack, with the ropes pulling straight to the trees.
  - fail: The hammock stays flat with the sack in it; or the ropes go slack while it sags; or the cloth stretches down and down.
- P2 [core · gravity_direction]
  - expect: The sack falls into the hammock and rests at the low point, and the sag is downward.
  - fail: The sack bounces out; or hangs above the cloth; or the hammock bows upward.
- P3 [major · trajectory_momentum]
  - expect: The hammock swings gently after the drop and settles.
  - fail: It swings harder and harder; or stays rigid and still; or spins.
- P4 [major · missing_consequence]
  - expect: The trees or knots show the pull: branches dip or the ropes pull tight.
  - fail: The ropes float slack while the hammock sags; or the tree leans away; or the hammock sags with no ropes attached.
- P5 [fatal · permanence_count]
  - expect: One hammock and one sack keep their number.
  - fail: The sack vanishes or a second appears; or the sack passes through the cloth; or the hammock turns into another object.
- P6 [minor · attribute_drift]
  - expect: The hammock, the sack and the trees stay the same.
  - fail: The hammock changes colour; or the sack changes size; or the trees rearrange.

## MECH-0100 · tension · train

**Caption.** A tow rope lies slack on the ground between a truck and a stuck car; the truck drives forward, the rope goes taut, and the car jerks into motion behind it.

**Expectation (hidden).** The car does not move until the rope has straightened; the jerk happens at the instant the rope goes tight.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A rope lies slack between a truck and a car.
- S2 [core] The truck drives forward.
- S3 [core] The rope goes taut.
- S4 [core] The car jerks into motion behind the truck.
- S5 [minor] The rope lies on the ground and slack at the start.
- S6 [minor] The truck moves first, then the rope tightens, then the car moves.

**PC**
- P1 [core · causeless_motion]
  - expect: The car does not move until the rope has straightened.
  - fail: The car moves while the rope is still slack; or it moves before the truck does; or it moves on its own without the truck.
- P2 [core · missing_consequence]
  - expect: The jerk happens at the instant the rope goes tight, and the car then follows the truck.
  - fail: The rope goes taut and the car stays put; or the rope snaps taut and the truck is jerked back; or the car moves with a slack rope trailing.
- P3 [major · material_response]
  - expect: The rope lifts off the ground and straightens as it tightens, and it does not stretch like elastic.
  - fail: The rope stretches on and on; or it stays lying on the ground while taut; or it floats.
- P4 [major · trajectory_momentum]
  - expect: The car follows the line of the rope.
  - fail: The car moves sideways; or backward; or faster than the truck and overtakes it.
- P5 [fatal · permanence_count]
  - expect: One truck, one car and one rope keep their number.
  - fail: A vehicle vanishes or a third appears; or the rope passes through a bumper; or the rope vanishes.
- P6 [minor · attribute_drift]
  - expect: The vehicles' colours, the rope and the road stay the same.
  - fail: A vehicle changes colour; or the rope changes; or the road rearranges.

## MECH-0101 · tension · train

**Caption.** A fishing line goes tight as a fish takes the bait, and the rod, resting in a holder on the bank, bends toward the water.

**Expectation (hidden).** The bend appears as the line tightens and points toward where the line enters the water; the rod straightens if the line goes slack.

**Declared violation types.** material_response, missing_consequence

**SA**
- S1 [core] A fishing rod rests in a holder on a bank with its line in the water.
- S2 [core] The line goes tight.
- S3 [core] The rod bends toward the water.
- S4 [minor] The rod is in a holder rather than held.
- S5 [minor] The line tightens first and the bend follows.

**PC**
- P1 [core · material_response]
  - expect: The bend appears as the line tightens, curving toward where the line enters the water, and straightens if the line goes slack.
  - fail: The rod bends away from the water; or it bends while the line hangs slack; or it stays straight with the line plainly taut.
- P2 [core · missing_consequence]
  - expect: The tight line runs straight from the tip to the water and the rod tip dips.
  - fail: The line hangs in a loose curve while the rod is bent; or the line is taut and the rod tip does not move; or the rod bends before the line moves.
- P3 [major · causeless_motion]
  - expect: The rod stays in its holder and the holder stays put.
  - fail: The rod leaps out of the holder with nothing pulling; or the holder slides; or the rod bends and unbends in a steady rhythm with no change in the line.
- P4 [major · gravity_direction]
  - expect: A slack line droops, and the rod's bend is downward toward the water.
  - fail: The line rises up from the tip; or slack line floats; or the rod bends upward.
- P5 [fatal · permanence_count]
  - expect: One rod, one line and one holder keep their number.
  - fail: The rod vanishes or a second appears; or the line passes through the rod; or the holder disappears.
- P6 [minor · attribute_drift]
  - expect: The rod, the holder and the bank stay the same.
  - fail: The rod changes colour; or the holder changes; or the bank rearranges.

## MECH-0102 · tension · train

**Caption.** An empty tire swing hanging from a branch is given a push and swings back and forth beneath the branch.

**Expectation (hidden).** The rope stays straight and taut throughout and the tire follows an arc under the branch; the rope does not go slack or bend.

**Declared violation types.** material_response, trajectory_momentum

**SA**
- S1 [core] An empty tire swing hangs from a branch.
- S2 [core] It is given a push.
- S3 [core] It swings back and forth beneath the branch.
- S4 [minor] The tire is empty.
- S5 [minor] The push comes first and the swinging follows.

**PC**
- P1 [core · material_response]
  - expect: The rope stays straight and taut throughout and does not go slack or bend.
  - fail: The rope goes slack at the ends of the swing; or it bends mid-length; or it stretches.
- P2 [core · trajectory_momentum]
  - expect: The tire follows an arc under the branch at the rope's length.
  - fail: The tire rises above the branch; or it moves in a straight line; or it swings at a changing radius.
- P3 [major · causeless_motion]
  - expect: It swings from the one push, dies down, and nothing else touches it.
  - fail: It swings harder and harder; or stops dead; or starts again after stopping.
- P4 [major · gravity_direction]
  - expect: The tire hangs below the branch and the rope's fixed point is the branch.
  - fail: The tire floats up; or the branch bends down to the tire; or the rope's top slides along the branch.
- P5 [fatal · permanence_count]
  - expect: One tire, one rope and one branch keep their number.
  - fail: The tire vanishes or a second appears; or the rope passes through the branch; or the tire turns into another object.
- P6 [minor · attribute_drift]
  - expect: The tire, the rope and the tree stay the same.
  - fail: The tire changes colour; or the rope changes; or the tree rearranges.

## MECH-0103 · tension · train

**Caption.** A sled loaded with firewood is pulled across a snowy field by a rope, then the pull stops, and the rope goes slack.

**Expectation (hidden).** The rope is taut while the sled is being pulled and droops only after the pull stops; the sled slides on a little before stopping.

**Declared violation types.** material_response, causeless_motion

**SA**
- S1 [core] A sled loaded with firewood is pulled across a snowy field by a rope.
- S2 [core] The pull stops.
- S3 [core] The rope goes slack.
- S4 [minor] The load is firewood.
- S5 [minor] The pull stops first and the slack follows.

**PC**
- P1 [core · material_response]
  - expect: The rope is taut while the sled is being pulled and droops only after the pull stops.
  - fail: The rope is slack while the sled is plainly being pulled along; or it stays taut after the pull stops with the sled at rest; or it stretches.
- P2 [core · causeless_motion]
  - expect: The sled slides on a little after the pull stops, then stops and stays.
  - fail: The sled stops dead the instant the pull stops; or it keeps going at full speed; or it sets off again after stopping.
- P3 [major · gravity_direction]
  - expect: The slack rope drops onto the snow.
  - fail: The slack rope floats; or it rises; or it hangs in a curve in the air.
- P4 [major · trajectory_momentum]
  - expect: The sled follows the rope's line with the load riding on it.
  - fail: The sled swerves; or the load slides off backward; or the sled overtakes the rope.
- P5 [fatal · permanence_count]
  - expect: One sled, one rope and the load keep their number.
  - fail: The sled vanishes or a second appears; or the rope passes through the sled; or logs vanish from the load.
- P6 [minor · attribute_drift]
  - expect: The sled, the firewood and the field stay the same.
  - fail: The sled changes colour; or the load changes; or the field rearranges.

## MECH-0104 · tension · train

**Caption.** A cat pounces onto a spider web strung between two garden plants and the web tears apart under it.

**Expectation (hidden).** The strands stretch and break at the moment the cat lands, clinging to its fur; the web does not hold the cat up.

**Declared violation types.** material_response, permanence_count

**SA**
- S1 [core] A spider web is strung between two garden plants.
- S2 [core] A cat pounces onto the web.
- S3 [core] The web tears apart under the cat.
- S4 [minor] The pounce comes first and the tear follows.

**PC**
- P1 [core · material_response]
  - expect: The strands stretch and break at the moment the cat lands, clinging to its fur; the web does not hold the cat up.
  - fail: The web holds the cat like a net; or the strands snap back whole; or the web tears before the cat touches it.
- P2 [core · permanence_count]
  - expect: The torn strands stay torn and the web does not reform.
  - fail: The web is whole again later; or torn strands vanish; or a new web appears.
- P3 [major · gravity_direction]
  - expect: The cat comes down through the web to the ground.
  - fail: The cat hangs in the web above the ground; or rises; or bounces off the web.
- P4 [major · missing_consequence]
  - expect: The plants the web was anchored to shake as it tears.
  - fail: The plants stay rigid; or they shake before the cat arrives; or the web's anchor points float free.
- P5 [fatal · shape_identity]
  - expect: One cat keeps its limbs and shape.
  - fail: A limb detaches; or a second cat appears; or the cat passes through a plant.
- P6 [minor · attribute_drift]
  - expect: The cat's markings, the plants and the garden stay the same.
  - fail: The markings change; or the plants rearrange; or the garden changes between frames.

**Note.** The cat is self-driven: its leap and landing are not judged. Only the web's response is.

## MECH-0105 · tension · train

**Caption.** A boat tied to a dock by a long line drifts away on the tide until the line goes taut and stops it.

**Expectation (hidden).** The boat moves freely while the line is slack and stops the instant the line straightens, then swings on the end of the line.

**Declared violation types.** missing_consequence, material_response

**SA**
- S1 [core] A boat is tied to a dock by a line.
- S2 [core] The boat drifts away from the dock.
- S3 [core] The line goes taut.
- S4 [core] The boat is stopped by the line.
- S5 [minor] The line is long, so the boat drifts some distance before it tightens.
- S6 [minor] The drift comes first, then the taut line, then the stop.

**PC**
- P1 [core · material_response]
  - expect: The line goes from slack, drooping or in the water, to straight at the moment the boat reaches its length; it does not stretch.
  - fail: The line stretches; or it stays curved while the boat is held; or it is taut while the boat is still beside the dock.
- P2 [core · missing_consequence]
  - expect: The boat stops the instant the line straightens and then swings at the end of the line.
  - fail: The boat keeps drifting with the line taut; or it stops before the line is straight; or the line goes taut and the dock post comes away.
- P3 [major · causeless_motion]
  - expect: While the line is slack the boat drifts freely and slowly, and once held it swings.
  - fail: The boat speeds up as it drifts; or reverses on its own; or stops in open water with the line slack.
- P4 [major · gravity_direction]
  - expect: A slack line droops into the water, and a taut line runs straight above it.
  - fail: Slack line floats in the air; or the taut line sags into the water; or the boat lifts.
- P5 [fatal · permanence_count]
  - expect: One boat, one line and one dock keep their number.
  - fail: The boat vanishes or a second appears; or the line passes through the dock; or the boat turns into another object.
- P6 [minor · attribute_drift]
  - expect: The boat, the line and the dock stay the same.
  - fail: The boat changes colour; or the line changes; or the dock rearranges.

## MECH-0106 · tension · train

**Caption.** A crane cable is hooked to a steel beam lying on the ground; the crane lifts, the cable tightens, and the beam rises off the ground.

**Expectation (hidden).** The cable straightens first and the beam leaves the ground only after that, hanging straight below the hook; it does not rise before the cable is tight.

**Declared violation types.** missing_consequence, gravity_direction

**SA**
- S1 [core] A crane cable is hooked to a steel beam lying on the ground.
- S2 [core] The crane lifts.
- S3 [core] The cable tightens.
- S4 [core] The beam rises off the ground.
- S5 [minor] The lift comes first, then the tight cable, then the rising beam.

**PC**
- P1 [core · missing_consequence]
  - expect: The cable straightens first and the beam leaves the ground only after that.
  - fail: The beam rises before the cable is tight; or the cable is tight and the beam stays down while the hook rises; or the beam rises with the cable slack.
- P2 [core · gravity_direction]
  - expect: The beam hangs straight below the hook, level or tilting toward its heavier end, and does not swing far.
  - fail: The beam hangs off to one side of the hook; or it rises above the hook; or it floats up ahead of the cable.
- P3 [major · material_response]
  - expect: The cable stays straight and taut while the beam hangs and does not stretch.
  - fail: The cable sags with the beam hanging; or it stretches; or it bends sharply.
- P4 [major · causeless_motion]
  - expect: The beam moves only as the crane lifts and stops when the lift stops.
  - fail: The beam rises on its own; or keeps rising after the crane stops; or swings wildly with nothing touching it.
- P5 [fatal · permanence_count]
  - expect: One beam, one cable and one crane keep their number.
  - fail: The beam vanishes or a second appears; or the cable passes through the beam; or the beam turns into another object.
- P6 [minor · attribute_drift]
  - expect: The beam, the cable and the site stay the same.
  - fail: The beam changes colour or length; or the cable changes; or the site rearranges.

## MECH-0107 · tension · train

**Caption.** A necklace catches on a door handle as a woman walks past; the chain goes tight and jerks her head back.

**Expectation (hidden).** The jerk happens at the instant the chain goes taut; the chain does not stretch like elastic; it either holds or snaps.

**Declared violation types.** material_response, causeless_motion

**SA**
- S1 [core] A woman walks past a door handle.
- S2 [core] Her necklace catches on the handle.
- S3 [core] The chain goes tight.
- S4 [core] Her head is jerked back.
- S5 [minor] The catch comes first, then the tight chain, then the jerk.

**PC**
- P1 [core · material_response]
  - expect: The chain goes from loose to straight at the moment it catches, and it either holds or snaps; it does not stretch like elastic.
  - fail: The chain stretches longer and longer; or it goes tight while still hanging in a curve; or it passes through the handle.
- P2 [core · causeless_motion]
  - expect: The jerk happens at the instant the chain goes taut, not before.
  - fail: Her head jerks before the chain is tight; or the chain is tight and she walks on unaffected; or her head is jerked forward.
- P3 [major · trajectory_momentum]
  - expect: Her body carries on for a step while her head is checked, and she stops or turns back.
  - fail: Her whole body stops dead as one; or she is thrown forward; or she keeps walking with the chain stretched.
- P4 [major · missing_consequence]
  - expect: The door handle holds, and the door may rattle.
  - fail: The handle comes off; or the door swings open with her; or the chain detaches from her neck without breaking.
- P5 [fatal · shape_identity]
  - expect: The woman, the chain and the door keep their number and shape.
  - fail: A limb detaches; or the chain passes through her neck; or a second figure appears.
- P6 [minor · attribute_drift]
  - expect: Her clothing, the necklace and the door stay the same.
  - fail: Her clothing changes colour; or the necklace changes; or the door rearranges.

**Note.** The woman is kept because her neck is what the chain acts on. Her expression and stride are not judged; only the timing of the jerk and the chain's behaviour.

## MECH-0108 · tension · train

**Caption.** The rope on a flagpole is pulled steadily, and the flag rises up the pole as the rope runs through the pulley at the top.

**Expectation (hidden).** The rope stays taut on the pulled side, the flag moves only as fast as rope is pulled in, and it stops rising when the pulling stops; the rope does not stretch or go slack while lifting.

**Declared violation types.** material_response, missing_consequence

**SA**
- S1 [core] A flag hangs on a flagpole with a rope.
- S2 [core] The rope is pulled.
- S3 [core] The flag rises up the pole.
- S4 [minor] The pulley at the top of the pole is visible.
- S5 [minor] The pull is steady rather than in jerks.

**PC**
- P1 [core · material_response]
  - expect: The rope stays taut on the pulled side and does not stretch or go slack while lifting.
  - fail: The pulled side hangs slack while the flag rises; or the rope stretches; or it bunches.
- P2 [core · missing_consequence]
  - expect: The flag moves only as fast as rope is pulled in and stops when the pulling stops.
  - fail: The flag rises with no pull; or keeps rising after the pull stops; or the rope is pulled and the flag stays put.
- P3 [major · gravity_direction]
  - expect: The flag hangs or flutters from its clips, and the rope runs straight down from the pulley.
  - fail: The flag rises above the pulley; or the rope rises away from the pole; or the flag floats up ahead of the rope.
- P4 [major · trajectory_momentum]
  - expect: One side of the rope goes up as the other comes down.
  - fail: Both sides go up; or the rope does not move while the flag rises; or the flag goes down as the rope is pulled.
- P5 [fatal · permanence_count]
  - expect: One flag, one rope and one pole keep their number.
  - fail: The flag vanishes or a second appears; or the rope passes through the pole; or the flag turns into another object.
- P6 [minor · attribute_drift]
  - expect: The flag's colours, the pole and the sky stay the same.
  - fail: The flag changes colours; or the pole changes; or the background rearranges.

## MECH-0109 · tension · train

**Caption.** A heavy bucket hung from the handle of a backyard zip line is released and rides it down to the far end, the cable sagging under it.

**Expectation (hidden).** The cable dips most under the handle and the dip travels with the bucket; the cable stays straight on either side and does not go slack or stretch like elastic.

**Declared violation types.** material_response, gravity_direction

**SA**
- S1 [core] A bucket hangs from the handle of a zip line.
- S2 [core] It is released.
- S3 [core] It rides down the cable to the far end.
- S4 [core] The cable sags under it.
- S5 [minor] The release comes first and the ride follows.

**PC**
- P1 [core · material_response]
  - expect: The cable dips most under the handle and the dip travels with the bucket; it stays straight on either side and does not stretch.
  - fail: The cable stays level under the bucket; or it sags everywhere at once; or it stretches longer; or it bends upward.
- P2 [core · gravity_direction]
  - expect: The bucket runs downhill along the cable, speeding up, and slows at the far end; it hangs below the cable.
  - fail: The bucket climbs; or it stops mid-run with nothing in its way; or it rises above the cable.
- P3 [major · causeless_motion]
  - expect: The bucket moves only after release and stops at the end.
  - fail: It moves before release; or sets off again after reaching the end; or changes speed with nothing acting on it.
- P4 [major · trajectory_momentum]
  - expect: The bucket follows the cable's line, swinging a little, and the handle stays on the cable.
  - fail: The bucket swings off to the side of the cable's line; or it spins; or the handle leaves the cable and the bucket keeps going.
- P5 [fatal · permanence_count]
  - expect: One bucket, one handle and one cable keep their number.
  - fail: The bucket vanishes or a second appears; or the handle passes through the cable; or the bucket turns into another object.
- P6 [minor · attribute_drift]
  - expect: The bucket, the cable and the yard stay the same.
  - fail: The bucket changes colour; or the cable changes; or the yard rearranges.

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

## MECH-0111 · deformation · train

**Caption.** An empty aluminum soda can lying on a driveway is stepped on, and it crumples flat and stays flat.

**Expectation (hidden).** The crushing happens under the foot, not before; the can keeps its crushed shape after the foot lifts and does not spring back.

**Declared violation types.** material_response, process_direction

**SA**
- S1 [core] An empty soda can lies on a driveway.
- S2 [core] A foot steps on it.
- S3 [core] The can crumples flat.
- S4 [core] It stays flat after the foot lifts.
- S5 [minor] The can is empty before it is stepped on.
- S6 [minor] The step comes first, then the crumple, then the foot lifts.

**PC**
- P1 [core · material_response]
  - expect: The can crushes under the foot where the foot presses, the thin metal folding and creasing.
  - fail: The can holds the foot up like a block; or it shatters into pieces; or it squashes like a soft sponge with no creases.
- P2 [core · process_direction]
  - expect: The crush happens under the foot, not before, and the can keeps its crushed shape after the foot lifts.
  - fail: The can is flat before the foot reaches it; or it springs back to round after the foot lifts; or it goes on crumpling after the foot is gone.
- P3 [major · causeless_motion]
  - expect: The can stays where it lies apart from the foot's contact.
  - fail: The can rolls off before the foot arrives; or it jumps away after being crushed; or it slides across the driveway with nothing touching it.
- P4 [major · gravity_direction]
  - expect: The foot comes down onto the can and the can stays on the ground.
  - fail: The can lifts off the ground; or the foot passes below the driveway surface; or the can floats up after crushing.
- P5 [fatal · shape_identity]
  - expect: One can keeps its number, and the foot does not pass through it.
  - fail: The can vanishes or a second one appears; or the foot passes through the can; or the can turns into another object.
- P6 [minor · attribute_drift]
  - expect: The can's label, the shoe and the driveway stay the same.
  - fail: The label changes; or the shoe changes; or the driveway rearranges between frames.

**Note.** The foot is kept as the minimal trigger; the person is not judged.

## MECH-0112 · deformation · train

**Caption.** Two thumbs press into a ball of modelling clay on a table, and the clay keeps the thumbprints after the hands lift away.

**Expectation (hidden).** The clay dents where pressed and bulges beside the thumbs; the prints stay and the ball does not pop back into a sphere.

**Declared violation types.** material_response, process_direction

**SA**
- S1 [core] A ball of modelling clay sits on a table.
- S2 [core] Two thumbs press into it.
- S3 [core] The hands lift away.
- S4 [core] The thumbprints remain in the clay.
- S5 [minor] Two thumbs make two dents.
- S6 [minor] The press comes first, then the lift, then the prints remain.

**PC**
- P1 [core · material_response]
  - expect: The clay dents where pressed and bulges beside the thumbs, deforming smoothly without cracking or crumbling.
  - fail: The clay cracks like a dry shell; or it does not dent under the thumbs; or it flows like a liquid.
- P2 [core · process_direction]
  - expect: The prints stay after the thumbs lift, and the ball does not pop back into a sphere.
  - fail: The dents fill back in after the hands lift; or the prints are there before the thumbs touch; or the dents deepen after the thumbs have gone.
- P3 [major · causeless_motion]
  - expect: The ball stays put on the table apart from being pressed.
  - fail: The ball rolls away before the thumbs reach it; or it slides while pressed; or it moves after the hands leave.
- P4 [major · missing_consequence]
  - expect: The dents match where the thumbs pressed: two thumb-sized hollows.
  - fail: Dents appear where no thumb touched; or a thumb presses and no dent forms; or the whole ball flattens from two thumb presses.
- P5 [fatal · shape_identity]
  - expect: One ball of clay keeps its number, and the thumbs do not pass through it.
  - fail: The ball splits in two; or the thumbs pass through the clay; or the clay merges with the table.
- P6 [minor · attribute_drift]
  - expect: The clay's colour, the hands and the table stay the same.
  - fail: The clay changes colour; or the hands change; or the table rearranges between frames.

**Note.** The hands are kept as the minimal trigger; the person is not judged.

## MECH-0113 · deformation · train

**Caption.** A foam pillow is pressed down and released, and it puffs back to its shape.

**Expectation (hidden).** The pillow sinks only where pressed and recovers gradually after release; it does not stay dented or spring back instantly like rubber.

**Declared violation types.** material_response, process_direction

**SA**
- S1 [core] A foam pillow is present.
- S2 [core] It is pressed down.
- S3 [core] The press is released.
- S4 [core] The pillow puffs back to its shape.
- S5 [minor] The press comes first, then the release, then the recovery.

**PC**
- P1 [core · material_response]
  - expect: The pillow sinks only where pressed and recovers after the release.
  - fail: The pillow stays dented after the release; or it does not compress under the press; or it compresses everywhere at once.
- P2 [core · process_direction]
  - expect: The recovery follows the release and is gradual, not an instant snap like rubber.
  - fail: It snaps back the instant the hand lifts; or it starts expanding while still pressed; or it keeps sinking after the release.
- P3 [major · causeless_motion]
  - expect: The pillow stays where it is apart from being pressed.
  - fail: It slides away; or it jumps up off the surface; or it moves before being pressed.
- P4 [major · gravity_direction]
  - expect: The pillow lies on its surface and the press comes from above.
  - fail: The pillow lifts off the surface; or the dent forms on the underside; or it floats.
- P5 [fatal · shape_identity]
  - expect: One pillow keeps its number, and the hand does not pass through it.
  - fail: The pillow splits; or the hand passes through it; or a second pillow appears.
- P6 [minor · attribute_drift]
  - expect: The pillow's cover and the surroundings stay the same.
  - fail: The cover changes colour or pattern; or the bed or sofa changes; or the room rearranges.

## MECH-0114 · deformation · train

**Caption.** A heavy bowling ball is dropped onto the middle of a bed, the mattress dips under it, and it bounces slightly before settling.

**Expectation (hidden).** The dip appears as the ball lands and the rebound is smaller than the drop; the bed does not stay rigid like a floor or throw the ball higher than it fell from.

**Declared violation types.** material_response, trajectory_momentum

**SA**
- S1 [core] A bowling ball is dropped onto the middle of a bed.
- S2 [core] The mattress dips under it.
- S3 [core] The ball bounces slightly.
- S4 [core] The ball settles.
- S5 [minor] The bounce is slight rather than high.
- S6 [minor] The drop comes first, then the dip, then the bounce, then the settling.

**PC**
- P1 [core · material_response]
  - expect: The dip appears as the ball lands and the mattress springs back as the ball rises; the bed does not stay rigid like a floor.
  - fail: The mattress does not dip at all under the heavy ball; or it stays deeply dented with the ball off it; or it ripples like water.
- P2 [core · trajectory_momentum]
  - expect: The rebound is smaller than the drop, and the ball comes back down and settles in the dip.
  - fail: The ball bounces higher than it fell from; or it bounces the same height again and again; or it flies off sideways.
- P3 [major · gravity_direction]
  - expect: The ball falls straight down and after bouncing comes down again.
  - fail: It hangs in the air; or rises; or drifts sideways in the air.
- P4 [major · material_response]
  - expect: The ball stays a hard sphere.
  - fail: It squashes; or bends; or splits.
- P5 [fatal · permanence_count]
  - expect: One ball and one bed keep their number.
  - fail: The ball vanishes or a second appears; or it passes through the mattress; or it turns into another object.
- P6 [minor · attribute_drift]
  - expect: The ball, the bedding and the room stay the same.
  - fail: The ball changes colour; or the bedding changes pattern; or the room rearranges.

## MECH-0115 · deformation · train

**Caption.** A metal paper clip is bent open and let go, and it stays in its new shape.

**Expectation (hidden).** The bending happens only where the clip is worked, and it does not spring closed after release.

**Declared violation types.** material_response, process_direction

**SA**
- S1 [core] A metal paper clip is held.
- S2 [core] It is bent open.
- S3 [core] It is let go.
- S4 [core] It stays in its new shape.
- S5 [minor] The bend comes first, then the release, then the shape holds.

**PC**
- P1 [core · material_response]
  - expect: The wire bends smoothly only where it is worked, without snapping.
  - fail: The clip snaps in two; or it bends everywhere at once; or it stretches longer.
- P2 [core · process_direction]
  - expect: After release it keeps the bent shape and does not spring closed.
  - fail: It springs back to its original shape; or it goes on bending after release; or it is already open before the fingers work it.
- P3 [major · causeless_motion]
  - expect: The clip moves only in the fingers.
  - fail: It bends with no fingers on it; or it flies off; or it twists on its own after release.
- P4 [major · gravity_direction]
  - expect: Released, it lies or hangs where it is put.
  - fail: It floats; or rises; or drifts.
- P5 [fatal · permanence_count]
  - expect: One clip keeps its number.
  - fail: The clip vanishes or a second appears; or it turns into another object; or it merges with the fingers.
- P6 [minor · attribute_drift]
  - expect: The clip's colour and the background stay the same.
  - fail: The clip changes colour; or the hands change; or the background rearranges.

## MECH-0116 · deformation · train

**Caption.** A hand is pressed into a slab of memory foam and lifted away, and the hand-shaped dent slowly fills back in.

**Expectation (hidden).** The dent matches the hand and persists for a few seconds before disappearing gradually; it does not vanish instantly or stay permanently.

**Declared violation types.** material_response, process_direction

**SA**
- S1 [core] A hand is pressed into a slab of memory foam.
- S2 [core] The hand is lifted away.
- S3 [core] A hand-shaped dent remains.
- S4 [core] The dent slowly fills back in.
- S5 [minor] The press comes first, then the lift, then the dent fades.

**PC**
- P1 [core · material_response]
  - expect: The dent matches the hand, palm and fingers, and persists for a few seconds before disappearing gradually.
  - fail: No dent forms under the hand; or the dent is a shapeless hollow unlike a hand; or the foam cracks.
- P2 [core · process_direction]
  - expect: The dent fills in slowly and steadily, neither instantly nor never.
  - fail: The dent vanishes the instant the hand lifts; or it stays for the rest of the clip; or it deepens after the hand has gone.
- P3 [major · causeless_motion]
  - expect: The foam stays put.
  - fail: The slab slides; or lifts; or jumps.
- P4 [major · missing_consequence]
  - expect: The dent is where the hand pressed.
  - fail: A dent appears elsewhere; or the hand presses and leaves no mark; or the dent appears before the hand touches.
- P5 [fatal · shape_identity]
  - expect: One slab keeps its number, and the hand does not pass through it.
  - fail: The slab splits; or the hand passes through it; or a second slab appears.
- P6 [minor · attribute_drift]
  - expect: The foam's colour and the surroundings stay the same.
  - fail: The foam changes colour; or the hand changes; or the background rearranges.

## MECH-0117 · deformation · train

**Caption.** An inflated balloon is squeezed between two palms; it flattens between the hands and bulges out at the sides, then rounds out again when the hands let go.

**Expectation (hidden).** The balloon keeps roughly the same overall size while squeezed, bulging where it is not pressed; it does not shrink, pass through the hands, or stay flat.

**Declared violation types.** material_response, shape_identity

**SA**
- S1 [core] An inflated balloon is held between two palms.
- S2 [core] The palms squeeze it.
- S3 [core] It flattens between the hands.
- S4 [core] It bulges out at the sides.
- S5 [core] It rounds out again when the hands let go.
- S6 [minor] The squeeze comes first, then the flatten and bulge, then the release.

**PC**
- P1 [core · material_response]
  - expect: The balloon flattens where pressed and bulges where not, keeping roughly the same overall size, and rounds out on release.
  - fail: It stays flat after the hands open; or it shrinks as if deflating while squeezed; or it does not deform at all.
- P2 [core · shape_identity]
  - expect: It stays one balloon and does not pass through the hands or burst.
  - fail: The hands pass through the balloon; or it bursts and reforms; or it splits into two balloons.
- P3 [major · causeless_motion]
  - expect: The balloon changes only while the hands act and is still afterward.
  - fail: It pulsates on its own; or flies off; or deforms before the hands close.
- P4 [major · gravity_direction]
  - expect: Released, it stays in the hands or drops slowly.
  - fail: It shoots away like a jet; or rises steadily to the ceiling with nothing holding it; or hangs in mid-air away from the hands.
- P5 [fatal · permanence_count]
  - expect: One balloon keeps its number.
  - fail: The balloon vanishes or a second appears; or it turns into another object; or it merges with a hand.
- P6 [minor · attribute_drift]
  - expect: The balloon's colour and the background stay the same.
  - fail: The balloon changes colour; or the hands change; or the background rearranges.

## MECH-0118 · deformation · train

**Caption.** Loose snow is packed between mittened hands into a firm snowball that holds its shape when the hands open.

**Expectation (hidden).** The snow compresses and sticks together under pressure; the ball stays a ball after release and does not fall apart into loose snow or spring back.

**Declared violation types.** material_response, shape_identity

**SA**
- S1 [core] Loose snow is gathered in mittened hands.
- S2 [core] The hands pack it.
- S3 [core] A firm snowball forms.
- S4 [core] The hands open and the ball holds its shape.
- S5 [minor] The hands are mittened.
- S6 [minor] The packing comes first, then the ball forms, then the hands open.

**PC**
- P1 [core · material_response]
  - expect: The snow compresses and sticks together under pressure, going from loose to a firm ball.
  - fail: The snow stays powdery and falls through the fingers when packed; or it turns to liquid; or it hardens into a glassy ball.
- P2 [core · shape_identity]
  - expect: The ball stays a ball after release and does not fall apart or spring back to loose snow.
  - fail: It crumbles the instant the hands open; or it puffs back up into loose snow; or it splits into two balls.
- P3 [major · process_direction]
  - expect: The ball gets smaller and denser as it is packed, not larger.
  - fail: It grows while being packed with no snow added; or it shrinks after the hands open; or it swells.
- P4 [major · gravity_direction]
  - expect: Loose snow that falls goes down.
  - fail: Snow rises from the hands; or hangs in the air; or the ball floats between the hands.
- P5 [fatal · permanence_count]
  - expect: One snowball forms and keeps its number.
  - fail: The ball vanishes or a second appears; or it turns into another object; or it merges with a mitten.
- P6 [minor · attribute_drift]
  - expect: The mittens and the background stay the same.
  - fail: The mittens change colour; or the snow changes colour; or the background rearranges.

## MECH-0119 · deformation · train

**Caption.** A gymnast lands feet-first in the centre of a trampoline, the mat stretches deep under her, and it throws her back up into the air.

**Expectation (hidden).** The mat dips as she lands and springs back as she rises; the rebound follows the dip, and she leaves the mat as it returns to flat.

**Declared violation types.** material_response, trajectory_momentum

**SA**
- S1 [core] A gymnast comes down onto a trampoline.
- S2 [core] She lands feet-first in the centre.
- S3 [core] The mat stretches deep under her.
- S4 [core] She is thrown back up into the air.
- S5 [minor] The landing is feet-first.
- S6 [minor] The landing comes first, then the dip, then the rebound.

**PC**
- P1 [core · material_response]
  - expect: The mat dips as she lands and springs back as she rises, and she leaves it as it returns to flat.
  - fail: The mat stays rigid like a floor; or it stays stretched after she leaves; or it ripples like water.
- P2 [core · trajectory_momentum]
  - expect: The rebound follows the dip, upward, roughly along the line she came down.
  - fail: She is thrown sideways off the trampoline; or she rises before the mat has dipped; or she stops dead on the mat with no rebound.
- P3 [major · gravity_direction]
  - expect: She comes down, then goes up, slowing as she rises.
  - fail: She hangs at the bottom of the dip; or hangs at the top; or speeds up after leaving the mat.
- P4 [major · causeless_motion]
  - expect: The springs and frame hold and the trampoline stays put.
  - fail: The frame lifts off the ground; or it slides; or the mat moves before she lands.
- P5 [fatal · shape_identity]
  - expect: One gymnast keeps her limbs and shape, and she does not pass through the mat.
  - fail: A limb detaches; or she passes through the mat; or a second figure appears.
- P6 [minor · attribute_drift]
  - expect: Her leotard, the trampoline and the gym stay the same.
  - fail: The leotard changes colour; or the trampoline changes; or the gym rearranges.

**Note.** Biomechanics scene: the gymnast is kept because her body is the load. Form and technique are not judged.

## MECH-0120 · deformation · train

**Caption.** A tennis racket strikes a ball hard during a serve and the ball flies off toward the far court.

**Expectation (hidden).** The ball flattens against the strings for an instant and leaves round again; it does not pass through the strings or stick to them.

**Declared violation types.** material_response, trajectory_momentum

**SA**
- S1 [core] A tennis racket strikes a ball.
- S2 [core] The strike is hard.
- S3 [core] The ball flies off toward the far court.
- S4 [minor] The stroke is a serve.
- S5 [minor] The strike comes first and the flight follows.

**PC**
- P1 [core · material_response]
  - expect: The ball flattens against the strings for an instant and leaves round again; it does not pass through or stick.
  - fail: It passes through the strings; or it sticks to the racket; or it stays flattened in flight.
- P2 [core · trajectory_momentum]
  - expect: The ball leaves at the instant of contact, faster than it arrived, along the racket's swing.
  - fail: The ball moves off before the racket reaches it; or it leaves slower than it came; or it flies backward past the server.
- P3 [major · causeless_motion]
  - expect: The ball flies in one line after the hit.
  - fail: It jinks; or stops in the air; or speeds up in mid-air.
- P4 [major · material_response]
  - expect: The racket frame stays rigid, and the strings may flex.
  - fail: The frame bends; or the strings tear; or the racket passes through the ball.
- P5 [fatal · permanence_count]
  - expect: One ball and one racket keep their number.
  - fail: The ball vanishes or a second appears; or the racket vanishes; or the ball turns into another object.
- P6 [minor · attribute_drift]
  - expect: The ball, the racket and the court stay the same.
  - fail: The ball changes colour; or the racket changes; or the court lines shift.

**Note.** The server is kept because the swing is the physics. Serving form is not judged.

## MECH-0121 · deformation · train

**Caption.** The heel of a hand presses into a ball of bread dough on a floured counter and the dough flattens and spreads.

**Expectation (hidden).** The dough deforms only where pressed and slowly keeps the pressed shape; it does not spring back like rubber or crack like clay.

**Declared violation types.** material_response, process_direction

**SA**
- S1 [core] A ball of bread dough sits on a floured counter.
- S2 [core] The heel of a hand presses into it.
- S3 [core] The dough flattens.
- S4 [core] The dough spreads outward.
- S5 [minor] The counter is floured.
- S6 [minor] The press comes first, then the flatten and spread.

**PC**
- P1 [core · material_response]
  - expect: The dough deforms only where pressed, spreading outward, without cracking or springing back like rubber.
  - fail: The dough cracks like clay; or it springs back to a ball when the hand lifts; or it holds the hand up without flattening.
- P2 [core · process_direction]
  - expect: The flattening progresses with the press and holds; it does not reverse.
  - fail: The dough rises back into a ball; or it flattens before the hand touches; or it keeps spreading after the hand lifts.
- P3 [major · causeless_motion]
  - expect: The dough stays put on the counter.
  - fail: It slides; or lifts; or rolls.
- P4 [major · missing_consequence]
  - expect: Flour marks the dough and the counter where it is pressed.
  - fail: The dough passes over the flour leaving no mark; or flour appears where nothing touched; or flour rises in a cloud with no press.
- P5 [fatal · shape_identity]
  - expect: One ball of dough keeps its number, and the hand does not pass through it.
  - fail: The dough splits; or the hand passes through it; or a second ball appears.
- P6 [minor · attribute_drift]
  - expect: The dough's colour and the counter stay the same.
  - fail: The dough changes colour; or the counter changes; or the kitchen rearranges.

## MECH-0122 · deformation · train

**Caption.** A loaded toolbox is set down on top of a large cardboard box in a garage, and the box caves in under it.

**Expectation (hidden).** The top folds in and the sides buckle as the weight lands; the box does not hold like a stool.

**Declared violation types.** material_response, process_direction

**SA**
- S1 [core] A large cardboard box stands in a garage.
- S2 [core] A toolbox is set down on top of it.
- S3 [core] The box caves in under the toolbox.
- S4 [minor] The toolbox is loaded and heavy.
- S5 [minor] The toolbox is set down first and the caving follows.

**PC**
- P1 [core · material_response]
  - expect: The top folds in and the sides buckle as the weight lands; the box does not hold like a stool.
  - fail: The box holds the toolbox up unchanged; or it flattens completely in an instant like paper; or it shatters like glass.
- P2 [core · process_direction]
  - expect: The caving progresses as the weight settles and stays caved.
  - fail: The box caves before the toolbox touches it; or it springs back up while the toolbox is on it; or it caves and uncaves.
- P3 [major · gravity_direction]
  - expect: The toolbox sinks down with the collapsing top and stays there.
  - fail: The toolbox floats above; or it rises; or it tips off and hangs.
- P4 [major · causeless_motion]
  - expect: The box stays where it is.
  - fail: It slides; or jumps; or moves before the toolbox arrives.
- P5 [fatal · permanence_count]
  - expect: One box and one toolbox keep their number.
  - fail: The box vanishes or a second appears; or the toolbox passes through the box; or the box turns into another object.
- P6 [minor · attribute_drift]
  - expect: The box's printing, the toolbox and the garage stay the same.
  - fail: The printing changes; or the toolbox changes colour; or the garage rearranges.

## MECH-0123 · deformation · train

**Caption.** A fresh green twig is bent into a curve and one end let go, and the twig springs back to nearly straight.

**Expectation (hidden).** The twig bends smoothly without snapping and straightens on release; it does not stay curved or break.

**Declared violation types.** material_response, process_direction

**SA**
- S1 [core] A green twig is held.
- S2 [core] It is bent into a curve.
- S3 [core] One end is let go.
- S4 [core] The twig springs back to nearly straight.
- S5 [minor] The twig is fresh and green.
- S6 [minor] The bend comes first, then the release, then the spring back.

**PC**
- P1 [core · material_response]
  - expect: The twig bends smoothly without snapping and straightens on release.
  - fail: It snaps; or it stays curved; or it kinks like a wire.
- P2 [core · process_direction]
  - expect: The spring back follows the release and happens quickly.
  - fail: It straightens before the end is released; or it stays bent for the rest of the clip; or it bends further after release.
- P3 [major · causeless_motion]
  - expect: The twig moves only as it is bent and released.
  - fail: It whips about on its own; or flies off; or bends with no hands on it.
- P4 [major · trajectory_momentum]
  - expect: The released end swings back toward straight and may overshoot slightly.
  - fail: The released end swings further into the curve; or the held end moves while the released end stays; or the twig spins.
- P5 [fatal · permanence_count]
  - expect: One twig keeps its number.
  - fail: The twig vanishes or a second appears; or it turns into another object; or it merges with the hand.
- P6 [minor · attribute_drift]
  - expect: The twig's colour and the background stay the same.
  - fail: The twig changes colour; or the hands change; or the background rearranges.

## MECH-0124 · deformation · train

**Caption.** A ripe avocado is pressed firmly between finger and thumb and the skin dents inward and stays dented.

**Expectation (hidden).** The dent forms under the fingers and remains after they lift; the avocado does not spring back like a ball or crack like a shell.

**Declared violation types.** material_response, process_direction

**SA**
- S1 [core] An avocado is held between finger and thumb.
- S2 [core] It is pressed firmly.
- S3 [core] The skin dents inward.
- S4 [core] The dent stays after the fingers lift.
- S5 [minor] The press comes first, then the dent, then the fingers lift.

**PC**
- P1 [core · material_response]
  - expect: The dent forms under the fingers; the avocado does not spring back like a ball or crack like a shell.
  - fail: It springs back; or the skin cracks open; or it does not dent.
- P2 [core · process_direction]
  - expect: The dent remains after the fingers lift.
  - fail: It fills back in; or it is present before the press; or it deepens after the fingers have gone.
- P3 [major · causeless_motion]
  - expect: The fruit stays in the hand.
  - fail: It drops; or jumps; or moves before the press.
- P4 [major · missing_consequence]
  - expect: The dents are where the finger and thumb pressed.
  - fail: Dents appear elsewhere; or the press leaves no dent; or the whole fruit collapses.
- P5 [fatal · shape_identity]
  - expect: One avocado keeps its number, and the fingers do not pass through it.
  - fail: The fruit splits; or the fingers pass through it; or a second avocado appears.
- P6 [minor · attribute_drift]
  - expect: The avocado's colour and the background stay the same.
  - fail: The skin changes colour; or the hand changes; or the background rearranges.

## MECH-0125 · deformation · train

**Caption.** A bowstring is drawn back and released, and the arrow flies off toward the target.

**Expectation (hidden).** The bow limbs flex as the string is drawn and spring back on release; the arrow leaves at the instant of release, not before.

**Declared violation types.** material_response, trajectory_momentum

**SA**
- S1 [core] An arrow is on a bow with the string drawn back.
- S2 [core] The string is released.
- S3 [core] The arrow flies off toward the target.
- S4 [minor] A target is visible ahead.
- S5 [minor] The release comes first and the flight follows.

**PC**
- P1 [core · material_response]
  - expect: The bow limbs flex as the string is drawn and spring back on release, the string going from a V to straight.
  - fail: The limbs stay rigid; or they stay bent after release; or the string stretches like elastic.
- P2 [core · trajectory_momentum]
  - expect: The arrow leaves at the instant of release, not before, point-first along the line of aim.
  - fail: The arrow leaves before the string is released; or it stays on the string after release; or it flies tail-first or sideways.
- P3 [major · causeless_motion]
  - expect: The arrow flies in one line after release.
  - fail: It jinks; or stops in the air; or curves back.
- P4 [major · gravity_direction]
  - expect: The arrow's path dips slightly over distance, and anything dropped falls.
  - fail: The arrow curves upward; or hangs in the air; or rises.
- P5 [fatal · permanence_count]
  - expect: One arrow and one bow keep their number.
  - fail: The arrow vanishes or a second appears; or the bow vanishes; or the arrow turns into another object.
- P6 [minor · attribute_drift]
  - expect: The bow, the arrow and the range stay the same.
  - fail: The bow changes colour; or the arrow changes; or the target moves.

## MECH-0126 · deformation · train

**Caption.** A rubber band stretched between two fingers is let slip at one end; the band snaps back and drops.

**Expectation (hidden).** The band flies toward the finger still holding it at the instant of release and returns to its unstretched size.

**Declared violation types.** material_response, trajectory_momentum

**SA**
- S1 [core] A rubber band is stretched between two fingers.
- S2 [core] It is let slip at one end.
- S3 [core] The band snaps back.
- S4 [core] It drops.
- S5 [minor] The release comes first, then the snap back, then the drop.

**PC**
- P1 [core · material_response]
  - expect: The band shrinks back to its unstretched size at release.
  - fail: It stays stretched; or it snaps in two; or it stretches further.
- P2 [core · trajectory_momentum]
  - expect: The band flies toward the finger still holding it at the instant of release.
  - fail: It flies away from the holding finger; or it moves before release; or it hangs in the air stretched.
- P3 [major · gravity_direction]
  - expect: After snapping back it drops.
  - fail: It floats; or rises; or hangs.
- P4 [major · causeless_motion]
  - expect: The band moves only at release.
  - fail: It moves before release; or sets off again after landing; or jinks.
- P5 [fatal · permanence_count]
  - expect: One band keeps its number.
  - fail: The band vanishes or a second appears; or it turns into another object; or it merges with a finger.
- P6 [minor · attribute_drift]
  - expect: The band's colour and the background stay the same.
  - fail: The band changes colour; or the hands change; or the background rearranges.

## MECH-0128 · cut_tear · train

**Caption.** A loaf of crusty bread is torn in two at a dinner table.

**Expectation (hidden).** The crust cracks and the loaf pulls apart with a ragged tear where it is pulled, crumbs falling; the two pieces stay separate.

**Declared violation types.** material_response, permanence_count

**SA**
- S1 [core] A loaf of crusty bread is at a dinner table.
- S2 [core] It is torn.
- S3 [core] It ends up as two pieces.
- S4 [minor] The setting is a dinner table.
- S5 [minor] The tear comes first and the two pieces follow.

**PC**
- P1 [core · material_response]
  - expect: The crust cracks and the loaf pulls apart with a ragged tear where it is pulled, crumbs falling.
  - fail: The loaf stretches like rubber; or it parts along a clean straight line like a cut; or it shatters like glass.
- P2 [core · permanence_count]
  - expect: The two pieces stay separate and together make up the loaf.
  - fail: They rejoin; or a third piece appears; or the loaf is whole again.
- P3 [major · missing_consequence]
  - expect: The tear runs where the hands pull.
  - fail: The loaf splits before the hands pull; or it splits elsewhere; or the hands pull and it stays whole.
- P4 [major · gravity_direction]
  - expect: Crumbs fall down onto the table.
  - fail: Crumbs rise; or hang in the air; or return to the loaf.
- P5 [fatal · shape_identity]
  - expect: One loaf becomes two pieces, and the hands do not pass through it.
  - fail: The hands pass through the loaf; or the loaf turns into another object; or a second loaf appears.
- P6 [minor · attribute_drift]
  - expect: The bread's crust and the table setting stay the same.
  - fail: The crust changes colour; or the table setting rearranges; or the hands change.

## MECH-0129 · cut_tear · train

**Caption.** A ripe tomato is sliced into rounds on a cutting board with a sharp knife.

**Expectation (hidden).** Each stroke separates one slice that falls or is pushed aside, juice and seeds leak onto the board, and the tomato gets shorter; it is not cut ahead of the blade.

**Declared violation types.** missing_consequence, material_response

**SA**
- S1 [core] A tomato is on a cutting board.
- S2 [core] A knife slices it.
- S3 [core] The tomato is cut into rounds.
- S4 [minor] Several slices are made rather than one.
- S5 [minor] The slices are rounds cut across the tomato.

**PC**
- P1 [core · missing_consequence]
  - expect: Each stroke separates one slice where the blade passes, and the tomato gets shorter.
  - fail: The tomato is cut ahead of the blade; or the blade passes and the tomato stays whole; or slices appear with no stroke.
- P2 [core · material_response]
  - expect: Juice and seeds leak onto the board, the flesh is soft, and each slice falls or is pushed aside.
  - fail: The tomato is dry and rigid like wood; or the slice stays fused in place; or the tomato splashes like water.
- P3 [major · permanence_count]
  - expect: The slices stay separate and the tomato does not regrow.
  - fail: Slices rejoin; or a slice vanishes; or the tomato grows back.
- P4 [major · gravity_direction]
  - expect: Cut slices topple onto the board.
  - fail: They rise; or hang; or float.
- P5 [fatal · shape_identity]
  - expect: One tomato and one knife keep their number, and the blade passes through nothing but the tomato.
  - fail: The knife passes through the board; or a second tomato appears; or the knife vanishes.
- P6 [minor · attribute_drift]
  - expect: The tomato's colour, the knife and the board stay the same.
  - fail: The tomato changes colour; or the knife changes; or the board rearranges.

**Note.** The hand on the knife is kept as the minimal trigger; the person is not judged.

## MECH-0130 · cut_tear · train

**Caption.** A strip of packing tape is ripped off a cardboard box and the box flaps come free.

**Expectation (hidden).** The tape peels up along its length as it is pulled, sometimes taking the top layer of cardboard with it; the flaps open only after the tape is off.

**Declared violation types.** material_response, missing_consequence

**SA**
- S1 [core] A cardboard box is sealed with a strip of packing tape.
- S2 [core] The tape is ripped off.
- S3 [core] The box flaps come free.
- S4 [minor] The rip comes first and the flaps follow.

**PC**
- P1 [core · material_response]
  - expect: The tape peels up along its length as it is pulled, sometimes taking the top layer of cardboard with it.
  - fail: The tape shatters; or it stretches long like rubber; or it lifts off all at once with no pull.
- P2 [core · missing_consequence]
  - expect: The flaps open only after the tape is off.
  - fail: The flaps open with the tape still on; or the tape is off and the flaps stay sealed; or the flaps open before the pull.
- P3 [major · causeless_motion]
  - expect: The box stays put.
  - fail: It slides; or lifts; or jumps.
- P4 [major · permanence_count]
  - expect: The tape stays one strip and the box stays one box.
  - fail: The tape vanishes; or it regrows on the box; or the box splits.
- P5 [fatal · shape_identity]
  - expect: One box keeps its number, and the hands do not pass through it.
  - fail: The hands pass through the box; or a second box appears; or the box turns into another object.
- P6 [minor · attribute_drift]
  - expect: The box's printing and the tape's colour stay the same.
  - fail: The printing changes; or the tape changes colour; or the room rearranges.

## MECH-0131 · cut_tear · train

**Caption.** A boy bites into a whole apple and takes a bite-shaped piece out of it.

**Expectation (hidden).** The hollow appears exactly where he bit and stays there; the apple does not grow back or show the bite before his teeth reach it.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A boy holds a whole apple.
- S2 [core] He bites into it.
- S3 [core] A bite-shaped piece is missing afterward.
- S4 [minor] The apple is whole before the bite.
- S5 [minor] The bite comes first and the hollow follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The hollow appears exactly where he bit and nowhere else.
  - fail: The bite mark is elsewhere; or he bites and the apple stays whole; or the mark appears before his teeth reach it.
- P2 [core · permanence_count]
  - expect: The hollow stays and the apple does not grow back.
  - fail: The apple is whole again; or a second bite appears untouched; or the piece reappears.
- P3 [major · material_response]
  - expect: The flesh is crisp: it breaks off with juice, and the skin tears at the edge of the bite.
  - fail: The apple squashes like dough; or it shatters; or the bite is a clean straight cut.
- P4 [major · shape_identity]
  - expect: The boy's face and the apple stay separate.
  - fail: The teeth pass through the apple; or the apple passes into his face; or the apple splits in two.
- P5 [fatal · permanence_count]
  - expect: One apple and one boy keep their number.
  - fail: The apple vanishes; or duplicates; or turns into another fruit.
- P6 [minor · attribute_drift]
  - expect: The apple's colour and the boy's clothing stay the same.
  - fail: The apple changes colour; or the clothing changes; or the background rearranges.

**Note.** The boy is kept because the bite is the physics. His expression is not judged.

## MECH-0132 · cut_tear · train

**Caption.** A length of cotton fabric is torn along a snipped edge, and it rips into two pieces.

**Expectation (hidden).** The rip runs in a straight line following the weave as it is pulled, loose threads fraying at the edges; the tear does not run ahead of the pull.

**Declared violation types.** material_response, missing_consequence

**SA**
- S1 [core] A length of fabric has a snip at its edge.
- S2 [core] It is torn from the snip.
- S3 [core] It rips into two pieces.
- S4 [minor] The fabric is cotton.
- S5 [minor] The tear comes first and the two pieces follow.

**PC**
- P1 [core · material_response]
  - expect: The rip runs in a line following the weave as it is pulled, with threads fraying at the edges.
  - fail: The fabric stretches like rubber without tearing; or it shatters; or it tears in a jagged curve unlike a weave.
- P2 [core · missing_consequence]
  - expect: The tear advances with the pull and does not run ahead of it.
  - fail: The tear runs ahead of the pull; or the fabric is pulled and does not tear; or it is in two before the pull.
- P3 [major · permanence_count]
  - expect: The two pieces stay separate.
  - fail: They rejoin; or a third piece appears; or the fabric is whole again.
- P4 [major · gravity_direction]
  - expect: Loose ends of fabric hang down.
  - fail: They float; or rise; or hang out sideways unsupported.
- P5 [fatal · shape_identity]
  - expect: One length of fabric becomes two pieces, and the hands do not pass through it.
  - fail: The hands pass through the fabric; or a second length appears; or the fabric turns into another material.
- P6 [minor · attribute_drift]
  - expect: The fabric's colour and pattern stay the same on both pieces.
  - fail: One piece changes colour; or the pattern changes; or the background rearranges.

## MECH-0133 · cut_tear · train

**Caption.** A tuft of cotton candy is pulled off the top of a cone and comes away as a separate wisp.

**Expectation (hidden).** The floss stretches into strands before parting and leaves a ragged surface on the cone; the tuft does not rejoin the cone.

**Declared violation types.** material_response, permanence_count

**SA**
- S1 [core] Cotton candy sits on a cone.
- S2 [core] A tuft is pulled off the top.
- S3 [core] It comes away as a separate wisp.
- S4 [minor] The pull comes first and the separate wisp follows.

**PC**
- P1 [core · material_response]
  - expect: The floss stretches into strands before parting and leaves a ragged surface on the cone.
  - fail: It snaps like a solid; or it flows like a liquid; or the strands do not stretch.
- P2 [core · permanence_count]
  - expect: The tuft stays separate and the cone does not regrow.
  - fail: The tuft rejoins the cone; or it vanishes; or the cone grows back.
- P3 [major · missing_consequence]
  - expect: The cone shows where the tuft came from.
  - fail: The cone is unchanged after the pull; or a gap appears elsewhere; or the gap is there before the pull.
- P4 [major · gravity_direction]
  - expect: Loose strands droop.
  - fail: They rise; or hang unsupported; or float.
- P5 [fatal · shape_identity]
  - expect: One cone of candy keeps its number, and the hand does not pass through it.
  - fail: The hand passes through the floss; or a second cone appears; or the candy turns into another object.
- P6 [minor · attribute_drift]
  - expect: The candy's colour and the background stay the same.
  - fail: The candy changes colour; or the cone changes; or the background rearranges.

## MECH-0134 · cut_tear · train

**Caption.** A dry twig is snapped in half with a crack.

**Expectation (hidden).** The twig bends only slightly before breaking into two pieces with splintered ends; it does not bend like rubber or rejoin.

**Declared violation types.** material_response, permanence_count

**SA**
- S1 [core] A dry twig is held.
- S2 [core] It is snapped.
- S3 [core] It breaks into two pieces.
- S4 [minor] The break is near the middle.

**PC**
- P1 [core · material_response]
  - expect: The twig bends only slightly before breaking, with splintered ends.
  - fail: It bends like rubber without breaking; or it crumbles to powder; or the break is a clean cut.
- P2 [core · permanence_count]
  - expect: The two pieces stay two.
  - fail: They rejoin; or a third piece appears; or the twig is whole again.
- P3 [major · missing_consequence]
  - expect: The break is where the hands bend it.
  - fail: It breaks elsewhere; or it does not break under bending; or it breaks before bending.
- P4 [major · gravity_direction]
  - expect: Dropped pieces fall.
  - fail: They float; or rise; or hang.
- P5 [fatal · shape_identity]
  - expect: One twig becomes two pieces, and the hands do not pass through it.
  - fail: The hands pass through the twig; or a second twig appears; or the twig turns into another object.
- P6 [minor · attribute_drift]
  - expect: The twig's bark and the background stay the same.
  - fail: The bark changes colour; or the hands change; or the background rearranges.

## MECH-0135 · cut_tear · train

**Caption.** A bar of chocolate is broken along its grooves into separate pieces.

**Expectation (hidden).** The bar snaps cleanly along the grooves where it is bent; the pieces do not stick back together or bend without breaking.

**Declared violation types.** material_response, permanence_count

**SA**
- S1 [core] A bar of chocolate with grooves is held.
- S2 [core] It is broken.
- S3 [core] It breaks into separate pieces.
- S4 [minor] The break runs along the grooves.
- S5 [minor] The bending comes first and the break follows.

**PC**
- P1 [core · material_response]
  - expect: The bar snaps cleanly along a groove where it is bent; it does not bend without breaking.
  - fail: It bends like rubber; or it crumbles; or it melts.
- P2 [core · permanence_count]
  - expect: The pieces stay separate and together make up the bar.
  - fail: They stick back together; or a piece appears from nothing; or the bar is whole again.
- P3 [major · missing_consequence]
  - expect: The break follows the groove where the bar is bent.
  - fail: It breaks across a square; or it is bent with no break; or it breaks before bending.
- P4 [major · gravity_direction]
  - expect: Dropped pieces fall.
  - fail: They float; or rise; or hang.
- P5 [fatal · shape_identity]
  - expect: One bar becomes its pieces, and the hands do not pass through it.
  - fail: The hands pass through the bar; or a second bar appears; or the chocolate turns into another object.
- P6 [minor · attribute_drift]
  - expect: The chocolate's colour and wrapper stay the same.
  - fail: The chocolate changes colour; or the wrapper changes; or the background rearranges.

## MECH-0136 · cut_tear · train

**Caption.** The two sides of a bag of chips are pulled apart at the top seam and the bag pops open.

**Expectation (hidden).** The seal gives way suddenly as the sides are pulled, sometimes tearing down one side, and the chips inside are visible; the bag does not open before the pull.

**Declared violation types.** material_response, missing_consequence

**SA**
- S1 [core] A sealed bag of chips is held.
- S2 [core] The two sides are pulled apart at the top seam.
- S3 [core] The bag pops open.
- S4 [minor] The pull comes first and the pop follows.

**PC**
- P1 [core · material_response]
  - expect: The seal gives suddenly as the sides are pulled, sometimes tearing down one side, and the foil crinkles.
  - fail: The bag stretches like rubber; or it shatters; or it opens by itself with no pull.
- P2 [core · missing_consequence]
  - expect: The bag opens where it is pulled, after the pull, and the chips inside are visible.
  - fail: It opens before the pull; or the pull leaves it sealed; or it opens at the bottom.
- P3 [major · permanence_count]
  - expect: One bag stays one bag and the chips keep their number.
  - fail: The bag duplicates; or chips appear from nowhere; or the bag reseals.
- P4 [major · gravity_direction]
  - expect: Chips that spill fall.
  - fail: They float; or rise; or hang.
- P5 [fatal · shape_identity]
  - expect: One bag keeps its number, and the hands do not pass through it.
  - fail: The hands pass through the bag; or a second bag appears; or the bag turns into another object.
- P6 [minor · attribute_drift]
  - expect: The bag's printing and the background stay the same.
  - fail: The printing changes; or the hands change; or the background rearranges.

## MECH-0137 · cut_tear · train

**Caption.** A slice is cut out of a round birthday cake and lifted onto a plate, leaving a wedge-shaped gap in the cake.

**Expectation (hidden).** The gap matches the slice that was removed and stays open; the cake does not close up after the slice is lifted away.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A round birthday cake is present.
- S2 [core] A slice is cut out of it.
- S3 [core] The slice is lifted onto a plate.
- S4 [core] A wedge-shaped gap is left in the cake.
- S5 [minor] The gap is wedge-shaped.
- S6 [minor] The cut comes first, then the lift, then the gap remains.

**PC**
- P1 [core · missing_consequence]
  - expect: The gap matches the slice removed and appears as the slice lifts.
  - fail: The gap is there before the cut; or the slice lifts and the cake is whole; or the gap does not match the slice.
- P2 [core · permanence_count]
  - expect: The gap stays open and the cake does not close up.
  - fail: The gap closes; or a second slice appears from nothing; or the slice vanishes.
- P3 [major · material_response]
  - expect: The cake is soft: crumbs fall and frosting smears, and the slice holds its shape on the plate.
  - fail: The cake shatters; or it flows like liquid; or the slice bends like rubber.
- P4 [major · gravity_direction]
  - expect: The slice rests on the plate and crumbs fall.
  - fail: The slice floats; or crumbs rise; or the slice hangs in the air.
- P5 [fatal · shape_identity]
  - expect: One cake and one slice keep their number, and the knife passes through nothing but the cake.
  - fail: The knife passes through the plate; or a second cake appears; or the slice turns into another object.
- P6 [minor · attribute_drift]
  - expect: The cake's frosting and the candles stay the same.
  - fail: The frosting changes colour; or the candles rearrange; or the table changes.

## MECH-0138 · cut_tear · train

**Caption.** A strip of peel is torn off an orange starting from a slit in the top, exposing the segments underneath.

**Expectation (hidden).** The peel lifts only where it is being worked loose and comes away as one piece; the bare patch shows the segments and stays bare; the fruit does not regrow its skin.

**Declared violation types.** material_response, permanence_count

**SA**
- S1 [core] An orange has a slit in its top.
- S2 [core] A strip of peel is torn off from the slit.
- S3 [core] The segments underneath are exposed.
- S4 [minor] The peel comes away as a strip.
- S5 [minor] The tear comes first and the bare patch follows.

**PC**
- P1 [core · material_response]
  - expect: The peel lifts only where it is worked loose and comes away as one piece, with pith fibres.
  - fail: The peel shatters; or it flows; or it comes off all around in an instant.
- P2 [core · permanence_count]
  - expect: The bare patch stays bare and the skin does not regrow.
  - fail: The skin regrows; or the strip rejoins; or a second orange appears.
- P3 [major · missing_consequence]
  - expect: The bare patch is where the strip came off.
  - fail: It is elsewhere; or the strip comes off and the orange is unchanged; or the patch is there before the peel comes off.
- P4 [major · gravity_direction]
  - expect: The torn peel hangs or drops.
  - fail: It floats; or rises; or hangs unsupported.
- P5 [fatal · shape_identity]
  - expect: One orange keeps its number, and the fingers do not pass through it.
  - fail: The fingers pass through the orange; or the orange splits; or it turns into another fruit.
- P6 [minor · attribute_drift]
  - expect: The orange's colour and the background stay the same.
  - fail: The orange changes colour; or the hands change; or the background rearranges.

## MECH-0139 · cut_tear · train

**Caption.** An axe swung down onto a log standing on end on a chopping block splits it into two pieces that fall apart to the sides.

**Expectation (hidden).** The split starts where the blade bites and runs down the log; the halves fall away only after the blow lands; the axe does not pass through without effect.

**Declared violation types.** material_response, trajectory_momentum

**SA**
- S1 [core] A log stands on end on a chopping block.
- S2 [core] An axe is swung down onto it.
- S3 [core] The log splits into two pieces.
- S4 [core] The pieces fall apart to the sides.
- S5 [minor] The log stands on end before the blow.
- S6 [minor] The blow comes first, then the split, then the halves fall.

**PC**
- P1 [core · material_response]
  - expect: The split starts where the blade bites and runs down the log with a rough grain face.
  - fail: The axe passes through with no effect; or the log squashes; or the split is a clean smooth cut.
- P2 [core · trajectory_momentum]
  - expect: The halves fall away only after the blow lands, outward to the sides.
  - fail: The halves fall before the blow; or both fall to the same side; or they fly upward.
- P3 [major · gravity_direction]
  - expect: The halves fall to the ground, and the axe stays in the block or is lifted.
  - fail: The halves hang in the air; or rise; or the axe floats.
- P4 [major · causeless_motion]
  - expect: The chopping block stays put.
  - fail: It slides; or jumps; or the log moves before the blow.
- P5 [fatal · permanence_count]
  - expect: One log becomes two pieces and one axe keeps its number.
  - fail: A third piece appears; or a half vanishes; or the axe vanishes.
- P6 [minor · attribute_drift]
  - expect: The log's bark, the axe and the yard stay the same.
  - fail: The bark changes; or the axe changes; or the yard rearranges.

**Note.** The person swinging is kept because the swing is the physics. Technique is not judged.

## MECH-0140 · cut_tear · train

**Caption.** A page is torn out of a spiral notebook, leaving a fringe of paper on the coil.

**Expectation (hidden).** The page rips along the perforated edge as it is pulled and becomes a separate sheet; the notebook does not regain the page.

**Declared violation types.** material_response, permanence_count

**SA**
- S1 [core] A spiral notebook is open.
- S2 [core] A page is torn out.
- S3 [core] A fringe of paper is left on the coil.
- S4 [minor] The tear comes first and the fringe remains.

**PC**
- P1 [core · material_response]
  - expect: The page rips along the perforated edge as it is pulled, leaving a ragged fringe.
  - fail: It stretches like rubber; or the coil unwinds instead; or the page passes through the coil.
- P2 [core · permanence_count]
  - expect: The page is a separate sheet and the notebook does not regain it.
  - fail: It rejoins; or the page vanishes; or a second page appears.
- P3 [major · missing_consequence]
  - expect: The fringe stays on the coil where the page was torn.
  - fail: There is no fringe; or the fringe is there before the tear; or the page tears elsewhere.
- P4 [major · gravity_direction]
  - expect: The loose page droops or lies flat.
  - fail: It floats; or rises; or hangs unsupported.
- P5 [fatal · shape_identity]
  - expect: One notebook keeps its number, and the hand does not pass through it.
  - fail: The hand passes through the notebook; or a second notebook appears; or the page turns into another object.
- P6 [minor · attribute_drift]
  - expect: The notebook's cover and the writing stay the same.
  - fail: The cover changes; or the writing changes; or the desk rearranges.

## MECH-0141 · cut_tear · train

**Caption.** A thick garden hose is cut through with a pair of shears, leaving two open ends.

**Expectation (hidden).** The hose is pinched and then severed where the blades close; the cut does not appear elsewhere on the hose or before the blades meet.

**Declared violation types.** missing_consequence, material_response

**SA**
- S1 [core] A garden hose and a pair of shears are present.
- S2 [core] The shears cut through the hose.
- S3 [core] Two open ends are left.
- S4 [minor] The hose is thick.
- S5 [minor] The cut comes first and the two ends follow.

**PC**
- P1 [core · missing_consequence]
  - expect: The hose is severed where the blades close and only there, after they meet.
  - fail: It is cut elsewhere; or it is cut before the blades meet; or the blades close and the hose stays whole.
- P2 [core · material_response]
  - expect: The hose pinches under the blades before severing, leaving rubber ends.
  - fail: It shatters; or the blades bend; or the hose stretches.
- P3 [major · permanence_count]
  - expect: The two pieces stay two.
  - fail: They rejoin; or a third piece appears; or the hose is whole again.
- P4 [major · gravity_direction]
  - expect: The cut ends drop.
  - fail: They float; or rise; or hang.
- P5 [fatal · shape_identity]
  - expect: One hose becomes two, and one pair of shears keeps its number.
  - fail: The shears pass through the hand; or a second hose appears; or the shears vanish.
- P6 [minor · attribute_drift]
  - expect: The hose's colour and the shears stay the same.
  - fail: The hose changes colour; or the shears change; or the garden rearranges.

## MECH-0142 · cut_tear · train

**Caption.** A stubborn weed is pulled out of the soil by its leaves, and the whole plant comes up with its roots and clinging soil.

**Expectation (hidden).** The soil around the stem lifts and breaks as the roots come free; the plant does not float out untouched or leave the ground undisturbed.

**Declared violation types.** material_response, missing_consequence

**SA**
- S1 [core] A weed grows in soil.
- S2 [core] It is pulled by its leaves.
- S3 [core] The whole plant comes up.
- S4 [core] Roots and clinging soil come up with it.
- S5 [minor] The pull is by the leaves.
- S6 [minor] The pull comes first and the plant comes up after.

**PC**
- P1 [core · material_response]
  - expect: The soil around the stem lifts and breaks as the roots come free, and soil clings to the roots.
  - fail: The soil stays smooth and unbroken where the roots came out; or the roots slide out clean as from water; or the soil flows like liquid.
- P2 [core · missing_consequence]
  - expect: A hole is left where the plant was.
  - fail: There is no hole; or the hole is there before the pull; or the hole is elsewhere.
- P3 [major · gravity_direction]
  - expect: Loose soil falls back to the ground.
  - fail: It rises; or hangs in the air; or floats.
- P4 [major · causeless_motion]
  - expect: The plant moves only as it is pulled.
  - fail: It rises on its own; or jumps; or moves before the pull.
- P5 [fatal · shape_identity]
  - expect: One weed keeps its number, and the hand does not pass through it.
  - fail: The hand passes through the plant; or a second weed appears; or the weed turns into another object.
- P6 [minor · attribute_drift]
  - expect: The weed's leaves and the surrounding garden stay the same.
  - fail: The leaves change colour; or the garden rearranges; or the hand changes.

## MECH-0144 · fluid · train

**Caption.** A full glass of milk on a kitchen table is knocked over, and the milk spreads across the table and drips off the edge.

**Expectation (hidden).** The milk flows out as the glass goes over, spreads in a widening puddle, and runs off the low edge in drips; it does not hold a glass shape or flow uphill.

**Declared violation types.** material_response, gravity_direction

**SA**
- S1 [core] A full glass of milk stands on a kitchen table.
- S2 [core] It is knocked over.
- S3 [core] The milk spreads across the table.
- S4 [core] Milk drips off the edge of the table.
- S5 [minor] The glass is full before the knock.
- S6 [minor] The knock comes first, then the spread, then the drips.

**PC**
- P1 [core · material_response]
  - expect: The milk flows out as the glass goes over and spreads in a widening puddle; it does not hold the glass's shape.
  - fail: The milk stays in a glass shape after the glass falls; or it leaves as a solid lump; or it beads into balls that roll.
- P2 [core · gravity_direction]
  - expect: The puddle runs toward the low edge and drips downward from it.
  - fail: Milk flows uphill or back into the glass; or drips rise from the edge; or drips hang below the edge without falling.
- P3 [major · process_direction]
  - expect: The puddle only widens and the glass only empties.
  - fail: The puddle shrinks back; or the glass refills; or the puddle jumps between shapes.
- P4 [major · missing_consequence]
  - expect: The table is wet where milk has passed, and drips land on the floor.
  - fail: The table stays dry under the puddle; or a wet patch appears where no milk went; or drips vanish before reaching the floor.
- P5 [fatal · permanence_count]
  - expect: One glass, and milk comes only from it.
  - fail: The glass vanishes or duplicates; or milk appears away from the glass; or milk passes through the glass wall.
- P6 [minor · attribute_drift]
  - expect: The glass, the tablecloth and the kitchen stay the same.
  - fail: The milk changes colour; or the glass changes shape; or the table pattern shifts.

## MECH-0145 · fluid · train

**Caption.** A stone is dropped into a still garden pond; it splashes, sinks, and ripples spread out across the water.

**Expectation (hidden).** The splash rises at the moment of entry, the rings spread outward from that spot and fade as they widen; the stone does not float.

**Declared violation types.** material_response, process_direction

**SA**
- S1 [core] A stone is dropped into a still pond.
- S2 [core] It splashes.
- S3 [core] It sinks.
- S4 [core] Ripples spread out across the water.
- S5 [minor] The pond is still before the drop.
- S6 [minor] The splash comes first, then the sinking, then the ripples spread.

**PC**
- P1 [core · material_response]
  - expect: The splash rises at the moment of entry and falls back, and the water closes over the stone.
  - fail: There is no splash when the stone enters; or the splash hangs in the air; or the water stays rigid like glass.
- P2 [core · process_direction]
  - expect: Rings spread outward from the entry point and fade as they widen.
  - fail: Rings run inward; or they appear before the stone lands; or they stop dead and hold their shape.
- P3 [major · gravity_direction]
  - expect: The stone goes under and stays under.
  - fail: The stone floats; or it comes back up; or it hangs at the surface.
- P4 [major · causeless_motion]
  - expect: Away from the ripples the water stays still.
  - fail: Waves appear elsewhere with no cause; or the surface churns before the stone lands; or the centre of the rings moves.
- P5 [fatal · permanence_count]
  - expect: One stone enters and nothing else appears in the water.
  - fail: The stone vanishes in mid-air or a second appears; or it turns into another object; or a splash appears where nothing landed.
- P6 [minor · attribute_drift]
  - expect: The pond's colour and the garden around it stay the same.
  - fail: The water changes colour; or the plants rearrange; or the pond's edge moves.

## MECH-0146 · fluid · train

**Caption.** Olive oil is poured into a glass of water, and the oil gathers in a layer floating on top of the water.

**Expectation (hidden).** The oil sinks briefly in blobs and then rises to the surface; it does not mix in or settle at the bottom.

**Declared violation types.** material_response, gravity_direction

**SA**
- S1 [core] A glass of water is present.
- S2 [core] Olive oil is poured into it.
- S3 [core] The oil gathers into a layer floating on top of the water.
- S4 [minor] The pour comes first and the layer forms after.

**PC**
- P1 [core · gravity_direction]
  - expect: The oil sinks briefly in blobs as it lands and then rises to the surface, ending on top.
  - fail: The oil settles at the bottom; or it sinks and stays under; or the water rises above the oil.
- P2 [core · material_response]
  - expect: Oil and water stay separate, with blobs and a clear boundary and no mixing.
  - fail: The oil dissolves into the water; or it turns into a solid; or it foams up like soap.
- P3 [major · process_direction]
  - expect: The oil layer thickens while pouring and holds.
  - fail: The layer shrinks with oil still pouring; or the oil goes back into the bottle; or the layer is there before the pour.
- P4 [major · material_response]
  - expect: The stream falls as a thin liquid thread.
  - fail: The oil pours as a rigid rod; or as beads that bounce; or as a powder.
- P5 [fatal · permanence_count]
  - expect: One glass, and oil comes only from the pour.
  - fail: Oil appears in the glass with no stream; or the glass duplicates; or oil passes through the glass wall.
- P6 [minor · attribute_drift]
  - expect: The glass, the bottle and the background stay the same.
  - fail: The oil changes colour; or the glass changes shape; or the background rearranges.

## MECH-0147 · fluid · train

**Caption.** A motorboat speeds across a calm lake, leaving a spreading wake behind it.

**Expectation (hidden).** The wake is a V opening behind the boat with foam at the stern; the water ahead of the boat stays calm and the wake does not run ahead of the boat.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A motorboat moves fast across a lake.
- S2 [core] A wake spreads behind it.
- S3 [minor] The lake is calm apart from the wake.
- S4 [minor] The wake is behind the boat, not ahead of it.

**PC**
- P1 [core · missing_consequence]
  - expect: The wake is a V opening behind the boat with foam at the stern, and the water ahead stays calm.
  - fail: The boat moves and leaves no wake; or the wake runs ahead of the boat; or the water ahead churns as if already crossed.
- P2 [core · process_direction]
  - expect: The wake widens and fades with distance behind the boat.
  - fail: The wake narrows behind the boat; or it stays sharp all the way back; or it appears in pieces unconnected to the boat's path.
- P3 [major · trajectory_momentum]
  - expect: The boat travels in a line and the wake follows its path.
  - fail: The wake curves where the boat went straight; or the boat jinks; or the wake detaches and drifts.
- P4 [major · gravity_direction]
  - expect: Spray and the bow wave fall back to the surface.
  - fail: Spray hangs in the air; or rises; or the boat floats above the water.
- P5 [fatal · permanence_count]
  - expect: One boat keeps its number and shape.
  - fail: The boat vanishes or a second appears; or it turns into another vessel; or the wake appears with no boat.
- P6 [minor · attribute_drift]
  - expect: The boat's colour and the shoreline stay the same.
  - fail: The boat changes colour; or the shore rearranges; or the lake changes colour.

## MECH-0148 · fluid · train

**Caption.** A jar of honey is tipped over a slice of toast, and the honey flows out in a slow thick ribbon onto the toast.

**Expectation (hidden).** The ribbon is unbroken and falls straight down, piling up and spreading slowly on the toast; it does not pour thin and fast like water.

**Declared violation types.** material_response, gravity_direction

**SA**
- S1 [core] A jar of honey is tipped over a slice of toast.
- S2 [core] Honey flows out of the jar.
- S3 [core] It lands on the toast.
- S4 [minor] The flow is a slow thick ribbon.
- S5 [minor] The tip comes first and the flow follows.

**PC**
- P1 [core · material_response]
  - expect: The ribbon is unbroken and thick, piling up and spreading slowly on the toast; it does not pour thin and fast like water.
  - fail: It pours thin and fast like water; or it comes out as beads that bounce; or it comes out as a solid stick.
- P2 [core · gravity_direction]
  - expect: The ribbon falls straight down from the jar's lip to the toast.
  - fail: It curves upward or sideways; or it flows back into the jar; or it hangs without reaching the toast.
- P3 [major · process_direction]
  - expect: The pile on the toast grows while pouring and only spreads.
  - fail: The pile shrinks with honey still pouring; or it is there before the jar tips; or it jumps.
- P4 [major · missing_consequence] (if: The jar's tilt is visible in the clip.)
  - expect: The jar's tilt produces the flow: honey comes out only while the jar is tipped.
  - fail: Honey pours from an upright jar; or the jar is tipped and nothing comes out; or the ribbon continues after the jar is righted.
- P5 [fatal · permanence_count]
  - expect: One jar, and honey comes only from it.
  - fail: Honey appears on the toast with no ribbon; or the jar duplicates; or honey passes through the jar wall.
- P6 [minor · attribute_drift]
  - expect: The honey's colour, the jar and the plate stay the same.
  - fail: The honey changes colour; or the jar changes shape; or the plate rearranges.

## MECH-0149 · fluid · train

**Caption.** A half-full fish tank resting on a table is tilted to one side, and the water climbs the low side and spills over the rim.

**Expectation (hidden).** The water surface stays level while the tank tilts; the spill comes from the low side only and starts when the rim reaches the surface.

**Declared violation types.** material_response, gravity_direction

**SA**
- S1 [core] A half-full fish tank rests on a table.
- S2 [core] It is tilted to one side.
- S3 [core] The water rises on the low side.
- S4 [core] Water spills over the rim.
- S5 [minor] The tank is half-full before the tilt.
- S6 [minor] The tilt comes first, then the climb, then the spill.

**PC**
- P1 [core · gravity_direction]
  - expect: The water surface stays level while the tank tilts, so the water piles up at the low side.
  - fail: The water tilts with the tank keeping a fixed shape; or it climbs the high side; or it rises evenly all round.
- P2 [core · material_response]
  - expect: The spill comes from the low side only and starts when the rim reaches the surface.
  - fail: It spills from the high side; or it spills before the rim reaches the water; or it spills while the tank is level.
- P3 [major · missing_consequence]
  - expect: Spilled water runs down the outside of the tank and onto the table.
  - fail: The outside stays dry; or water appears on the table with none spilling; or drips rise.
- P4 [major · material_response]
  - expect: The water sloshes and settles as a liquid, and the tank stays rigid.
  - fail: The water stays a rigid block; or the glass bends; or the water beads into balls.
- P5 [fatal · permanence_count]
  - expect: One tank, and water leaves it only over the rim.
  - fail: Water passes through the glass; or the tank duplicates; or the water level rises while spilling.
- P6 [minor · attribute_drift]
  - expect: The tank, its contents and the table stay the same.
  - fail: The water changes colour; or the gravel inside rearranges; or the table changes.

## MECH-0150 · fluid · train

**Caption.** A small air pump runs with its tube in a glass of soapy water, and bubbles rise and pile up in a foam at the top of the glass.

**Expectation (hidden).** Bubbles form at the tube tip and rise; the foam builds while the pump runs and spills over the rim if it gets tall enough; bubbles do not sink.

**Declared violation types.** gravity_direction, material_response

**SA**
- S1 [core] An air pump's tube sits in a glass of soapy water.
- S2 [core] Bubbles come from the tube.
- S3 [core] The bubbles rise.
- S4 [core] Foam piles up at the top of the glass.
- S5 [minor] The water is soapy.
- S6 [minor] The bubbles come first and the foam builds after.

**PC**
- P1 [core · gravity_direction]
  - expect: Bubbles form at the tube tip and rise to the surface, and none sink.
  - fail: Bubbles sink; or hang mid-water; or form at the surface and go down.
- P2 [core · material_response]
  - expect: The foam builds while the pump runs as a mass of small bubbles and spills over the rim if it gets tall.
  - fail: Bubbles pop instantly leaving no foam; or the foam is a rigid dome; or the foam grows while the pump is off.
- P3 [major · process_direction]
  - expect: The foam only grows while pumping.
  - fail: It shrinks while pumping; or it is there before pumping; or it jumps.
- P4 [major · causeless_motion]
  - expect: The tube and the glass stay put.
  - fail: The glass slides; or the tube whips about; or the water churns away from the tube.
- P5 [fatal · permanence_count]
  - expect: One glass and one tube keep their number.
  - fail: The glass duplicates; or the tube vanishes; or foam appears away from the glass.
- P6 [minor · attribute_drift]
  - expect: The glass, the pump and the background stay the same.
  - fail: The water changes colour; or the glass changes shape; or the background rearranges.

## MECH-0151 · fluid · train

**Caption.** Several ice cubes are dropped into a glass of soda, and the cubes bob up and float near the surface.

**Expectation (hidden).** The cubes splash, dip below, and come back up to float with their tops just above the surface; the soda level rises as they go in.

**Declared violation types.** gravity_direction, material_response

**SA**
- S1 [core] A glass of soda is present.
- S2 [core] Several ice cubes are dropped in.
- S3 [core] The cubes bob up and float near the surface.
- S4 [minor] Several cubes rather than one.
- S5 [minor] The drop comes first and the floating follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The cubes splash, dip below, and come back up to float with their tops just above the surface.
  - fail: The cubes sink to the bottom and stay; or they hang mid-glass; or they float entirely above the soda.
- P2 [core · material_response]
  - expect: The soda level rises as the cubes go in, and fizz bubbles rise.
  - fail: The level drops; or stays unchanged; or the soda is rigid.
- P3 [major · process_direction]
  - expect: The bobbing dies down and the cubes settle.
  - fail: They bob harder; or they jump out; or they spin.
- P4 [major · shape_identity]
  - expect: The cubes stay cubes.
  - fail: Cubes merge; or dissolve instantly; or turn into another object.
- P5 [fatal · permanence_count]
  - expect: The cubes keep their number and the glass stays one glass.
  - fail: A cube vanishes or a new one appears; or the glass duplicates; or a cube passes through the glass wall.
- P6 [minor · attribute_drift]
  - expect: The soda's colour and the glass stay the same.
  - fail: The soda changes colour; or the glass changes shape; or the background rearranges.

## MECH-0152 · fluid · train

**Caption.** A dry sponge is dropped into a basin of water; it floats, darkens as it soaks up water, and settles lower.

**Expectation (hidden).** The darkening spreads from the wet side and the sponge sinks gradually as it fills; it does not sink instantly like a stone or stay dry.

**Declared violation types.** material_response, process_direction

**SA**
- S1 [core] A dry sponge is dropped into a basin of water.
- S2 [core] It floats.
- S3 [core] It darkens as it soaks up water.
- S4 [core] It settles lower.
- S5 [minor] The sponge is dry and light-coloured before the drop.
- S6 [minor] The drop comes first, then the float, then the darkening and settling.

**PC**
- P1 [core · process_direction]
  - expect: The darkening spreads from the wet side and only spreads, and the sponge sinks gradually as it fills.
  - fail: It sinks instantly like a stone; or it stays dry and high; or it lightens again.
- P2 [core · material_response]
  - expect: The sponge is soft and porous: it soaks and sags.
  - fail: Water beads off it like wax; or it dissolves; or it stays rigid.
- P3 [major · gravity_direction]
  - expect: It floats at the surface, part above water, and sits lower as it fills.
  - fail: It floats above the surface; or hovers mid-water; or rises as it soaks.
- P4 [major · missing_consequence]
  - expect: Ripples spread at the drop.
  - fail: There is no disturbance on entry; or ripples appear before it lands; or the water stays glassy.
- P5 [fatal · permanence_count]
  - expect: One sponge keeps its number.
  - fail: The sponge vanishes or a second appears; or it turns into another object; or it passes through the basin.
- P6 [minor · attribute_drift]
  - expect: The basin and the background stay the same.
  - fail: The basin changes colour; or the water changes colour; or the background rearranges.

## MECH-0153 · fluid · train

**Caption.** A bucket of water is emptied over a concrete sidewalk, and the water spreads out in a thin sheet and runs toward the lower side.

**Expectation (hidden).** The sheet spreads outward from where the water lands and flows downhill, leaving the concrete wet and dark; it does not stay in a heap or run uphill.

**Declared violation types.** material_response, gravity_direction

**SA**
- S1 [core] A bucket of water is emptied over a concrete sidewalk.
- S2 [core] The water spreads out in a thin sheet.
- S3 [core] It runs toward the lower side.
- S4 [minor] The emptying comes first and the spread and run follow.

**PC**
- P1 [core · material_response]
  - expect: The sheet spreads outward from where it lands, thin, leaving the concrete wet and dark.
  - fail: The water stays in a heap; or it holds the bucket's shape; or it beads into balls.
- P2 [core · gravity_direction]
  - expect: It flows downhill toward the lower side and pools there.
  - fail: It runs uphill; or spreads evenly on a plainly sloped surface; or rises.
- P3 [major · process_direction]
  - expect: The wet patch only grows and darkens.
  - fail: It shrinks back; or the concrete dries instantly; or the wet patch appears before the water.
- P4 [major · causeless_motion]
  - expect: The bucket empties by being tipped, and the water moves only by flowing.
  - fail: Water leaps from an upright bucket; or the sheet stops dead mid-slope; or water moves back into the bucket.
- P5 [fatal · permanence_count]
  - expect: One bucket, and water comes only from it.
  - fail: Water appears where none was poured; or the bucket duplicates; or water passes through the bucket.
- P6 [minor · attribute_drift]
  - expect: The bucket and the sidewalk stay the same.
  - fail: The bucket changes colour; or the sidewalk's slabs shift; or the surroundings rearrange.

## MECH-0154 · fluid · train

**Caption.** A saucepan is tipped and soup poured into a bowl until it is full and begins to spill over the sides.

**Expectation (hidden).** The level rises steadily and the overflow begins exactly when it reaches the rim, running down the outside onto the counter.

**Declared violation types.** material_response, missing_consequence

**SA**
- S1 [core] A saucepan is tipped over a bowl.
- S2 [core] Soup pours into the bowl.
- S3 [core] The bowl fills.
- S4 [core] Soup spills over the sides.
- S5 [minor] The pour comes first, then the fill, then the spill.

**PC**
- P1 [core · process_direction]
  - expect: The level rises steadily while pouring.
  - fail: The level drops while pouring; or it jumps; or the bowl is full before the pour.
- P2 [core · missing_consequence]
  - expect: The overflow begins exactly when the soup reaches the rim and runs down the outside onto the counter.
  - fail: It overflows before reaching the rim; or the bowl is over-full with a domed surface and nothing spills; or the outside stays dry.
- P3 [major · gravity_direction]
  - expect: The stream falls straight down and the overflow runs down.
  - fail: The stream curves up; or the overflow climbs; or soup hangs in the air.
- P4 [major · material_response]
  - expect: The soup is a liquid: it splashes and settles flat.
  - fail: It pours as a rigid rod; or as a solid lump; or as beads.
- P5 [fatal · permanence_count]
  - expect: One saucepan and one bowl, and soup comes only from the pan.
  - fail: Soup appears in the bowl with no stream; or the bowl duplicates; or soup passes through the bowl.
- P6 [minor · attribute_drift]
  - expect: The soup's colour, the bowl and the counter stay the same.
  - fail: The soup changes colour; or the bowl changes shape; or the counter rearranges.

## MECH-0155 · fluid · train

**Caption.** A dog climbs out of a lake and shakes itself, sending a spray of water droplets flying off its fur.

**Expectation (hidden).** Droplets leave the fur in all directions during the shake and fall to the ground around the dog; they do not hang in the air or return to the fur.

**Declared violation types.** trajectory_momentum, material_response

**SA**
- S1 [core] A dog climbs out of a lake.
- S2 [core] It shakes itself.
- S3 [core] Droplets fly off its fur.
- S4 [minor] The dog is wet as it comes out.
- S5 [minor] The climb out comes first, then the shake, then the spray.

**PC**
- P1 [core · trajectory_momentum]
  - expect: Droplets leave the fur in all directions during the shake, flung outward.
  - fail: Droplets hang beside the dog; or return to the fur; or fly only before the shake.
- P2 [core · material_response]
  - expect: The fur is wet and clumped and fluffs as water leaves, and the droplets are small rounded drops.
  - fail: The fur looks dry throughout; or the water leaves as a sheet; or as solid shards.
- P3 [major · gravity_direction]
  - expect: Droplets fall to the ground around the dog.
  - fail: They hang; or rise; or travel level to the edge of the frame.
- P4 [major · causeless_motion]
  - expect: The spray happens only while the dog shakes.
  - fail: Spray flies with the dog still; or continues long after the shake; or the dog is thrown by its own shake.
- P5 [fatal · shape_identity]
  - expect: One dog keeps its limbs and shape.
  - fail: A limb detaches; or a second dog appears; or the dog turns into another animal.
- P6 [minor · attribute_drift]
  - expect: The dog's coat and the lakeshore stay the same.
  - fail: The coat changes pattern; or the shore rearranges; or the water changes colour.

**Note.** The dog is self-driven: its shake is its own. Only the water's behaviour is judged.

## MECH-0156 · fluid · train

**Caption.** A woman paddles a kayak across a calm lake, pulling the blade back through the water, and the kayak moves forward.

**Expectation (hidden).** The kayak moves the opposite way to the blade's pull and starts moving with the stroke, not before it; each stroke leaves a swirl in the water behind the blade; between strokes the kayak glides on and slows only gently; it never moves backward or sideways while she pulls, and from rest it does not move before the first stroke.

**Declared violation types.** causeless_motion, trajectory_momentum, missing_consequence

**SA**
- S1 [core] A woman sits in a kayak on a lake.
- S2 [core] She pulls the paddle blade back through the water.
- S3 [core] The kayak moves forward.
- S4 [minor] The lake is calm.
- S5 [minor] The stroke comes first and the movement follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The kayak starts moving with the stroke, not before, and from rest it does not move before the first stroke.
  - fail: The kayak moves before the blade enters the water; or it moves with the paddle held clear; or it stops dead between strokes.
- P2 [core · trajectory_momentum]
  - expect: The kayak moves opposite to the blade's pull, forward as the blade goes back, and between strokes it glides and slows gently.
  - fail: The kayak moves backward while she pulls back; or sideways; or it speeds up between strokes.
- P3 [major · missing_consequence]
  - expect: Each stroke leaves a swirl behind the blade and a ripple at the hull.
  - fail: The blade passes through the water leaving no swirl; or swirls appear where no blade went; or the surface stays glassy around a moving hull.
- P4 [major · gravity_direction]
  - expect: The kayak floats level and drips from the paddle fall.
  - fail: The kayak lifts out of the water; or tilts and stays tilted; or drips rise.
- P5 [fatal · shape_identity]
  - expect: One kayak, one paddler and one paddle keep their number and shape.
  - fail: The paddle passes through the hull; or a second kayak appears; or a limb detaches.
- P6 [minor · attribute_drift]
  - expect: The kayak's colour, her clothing and the shore stay the same.
  - fail: The kayak changes colour; or her clothing changes; or the shore rearranges.

**Note.** The paddler is self-driven: her form is not judged. Only the timing and direction of the kayak's response to the stroke are.

## MECH-0157 · fluid · train

**Caption.** A girl sucks on a straw standing in a glass of juice, and the juice climbs the straw into her mouth while the level in the glass goes down.

**Expectation (hidden).** The juice rises inside the straw only while she sucks and drops back when she stops; the glass level falls as she drinks; juice does not leave the glass any other way.

**Declared violation types.** missing_consequence, gravity_direction, permanence_count

**SA**
- S1 [core] A straw stands in a glass of juice and a girl sucks on it.
- S2 [core] Juice climbs the straw.
- S3 [core] Juice reaches her mouth.
- S4 [core] The level in the glass goes down.
- S5 [minor] The suck comes first and the climb follows.

**PC**
- P1 [core · missing_consequence]
  - expect: Juice rises in the straw only while she sucks and drops back when she stops.
  - fail: The straw is full with no sucking; or she sucks and the straw stays empty; or the juice keeps rising after she stops.
- P2 [core · permanence_count]
  - expect: The glass level falls as she drinks, and juice leaves only via the straw.
  - fail: The level stays put while she drinks; or it rises; or juice vanishes from the glass with the straw empty.
- P3 [major · gravity_direction]
  - expect: The level in the glass stays flat and horizontal.
  - fail: It tilts; or domes up; or the juice climbs the glass wall.
- P4 [major · material_response]
  - expect: The juice is a liquid: it moves as a column in the straw and sloshes slightly.
  - fail: It moves as a rigid rod; or as beads; or as a solid.
- P5 [fatal · shape_identity]
  - expect: One glass, one straw and one girl keep their number.
  - fail: The straw passes through the glass; or a second straw appears; or the girl merges with the glass.
- P6 [minor · attribute_drift]
  - expect: The juice's colour, the glass and her clothing stay the same.
  - fail: The juice changes colour; or the glass changes; or her clothing changes.

**Note.** The girl is kept because her mouth is the pump. Her expression is not judged.

## MECH-0158 · fluid · train

**Caption.** A plastic ketchup bottle is squeezed over a plate of fries, and ketchup comes out of the nozzle onto the fries.

**Expectation (hidden).** Ketchup flows only while the bottle is squeezed, in a thick stream that falls onto the plate; the bottle dents where pressed and refills its shape when released.

**Declared violation types.** missing_consequence, material_response

**SA**
- S1 [core] A plastic ketchup bottle is held over a plate of fries.
- S2 [core] It is squeezed.
- S3 [core] Ketchup comes out of the nozzle.
- S4 [core] It lands on the fries.
- S5 [minor] The squeeze comes first and the flow follows.

**PC**
- P1 [core · missing_consequence]
  - expect: Ketchup flows only while the bottle is squeezed.
  - fail: It flows from an unsqueezed bottle; or the bottle is squeezed and nothing comes out; or it keeps flowing after the squeeze is released.
- P2 [core · material_response]
  - expect: The bottle dents where pressed and refills its shape when released, and the ketchup comes out as a thick stream.
  - fail: The bottle stays dented; or it does not dent; or the ketchup pours thin like water.
- P3 [major · gravity_direction]
  - expect: The stream falls straight down onto the fries.
  - fail: It curves upward; or hangs; or flows back into the nozzle.
- P4 [major · process_direction]
  - expect: The ketchup on the plate only accumulates.
  - fail: It shrinks back; or it is there before the squeeze; or it jumps.
- P5 [fatal · permanence_count]
  - expect: One bottle, and ketchup comes only from the nozzle.
  - fail: Ketchup appears with no stream; or the bottle duplicates; or ketchup passes through the bottle wall.
- P6 [minor · attribute_drift]
  - expect: The bottle's label, the plate and the fries stay the same.
  - fail: The label changes; or the plate changes; or the fries rearrange.

## MECH-0159 · fluid · train

**Caption.** An inflated beach ball is pushed under the water in a swimming pool and let go, and it pops back up to the surface.

**Expectation (hidden).** The ball rises as soon as it is released, breaks the surface with a splash, bobs, and settles floating mostly above the water; it does not stay under or sink.

**Declared violation types.** gravity_direction, trajectory_momentum

**SA**
- S1 [core] An inflated beach ball is pushed under the water in a pool.
- S2 [core] It is let go.
- S3 [core] It pops back up to the surface.
- S4 [minor] The release comes first and the rise follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The ball rises as soon as it is released, breaks the surface, bobs, and settles floating mostly above the water.
  - fail: It stays under; or sinks; or hovers mid-water.
- P2 [core · trajectory_momentum]
  - expect: It rises roughly straight up, may leap above the surface, and then settles.
  - fail: It shoots off sideways underwater; or leaps and stays airborne; or comes up far from where it was released with nothing moving it.
- P3 [major · missing_consequence]
  - expect: A splash and ripples spread where it breaks the surface.
  - fail: The surface stays glassy; or ripples appear before it arrives; or the splash is elsewhere.
- P4 [major · material_response]
  - expect: The ball stays round and taut.
  - fail: It squashes flat and stays flat; or deflates; or splits.
- P5 [fatal · permanence_count]
  - expect: One ball keeps its number.
  - fail: The ball vanishes or a second appears; or it turns into another object; or it passes through the pool wall.
- P6 [minor · attribute_drift]
  - expect: The ball's colours and the pool stay the same.
  - fail: The ball changes colours; or the pool's tiles shift; or the surroundings rearrange.

## MECH-0160 · granular · train

**Caption.** A bag of sugar is poured into a large mixing bowl, and the sugar builds up into a mound in the bowl.

**Expectation (hidden).** The sugar streams down in a steady flow and the mound grows as a cone that slumps at the sides; it does not pour as one solid lump or stack into a column.

**Declared violation types.** material_response, gravity_direction

**SA**
- S1 [core] Sugar is poured from a bag into a mixing bowl.
- S2 [core] The sugar builds up into a mound in the bowl.
- S3 [minor] The bowl is large.
- S4 [minor] The pour comes first and the mound builds after.

**PC**
- P1 [core · material_response]
  - expect: The sugar streams down as loose grains and the mound grows as a cone that slumps at the sides.
  - fail: It pours as one solid lump; or it stacks into a column; or it flows like a liquid with a flat surface.
- P2 [core · gravity_direction]
  - expect: The stream falls straight down and the mound builds from the bottom up.
  - fail: The stream curves upward; or grains rise; or the mound forms hanging from the bag.
- P3 [major · process_direction]
  - expect: The mound only grows while pouring.
  - fail: It shrinks; or it is there before the pour; or it jumps.
- P4 [major · missing_consequence] (if: The bag's tilt is visible in the clip.)
  - expect: The bag's tilt produces the stream.
  - fail: Sugar pours from an upright bag; or the bag is tipped and nothing comes out; or the stream continues after the bag is righted.
- P5 [fatal · permanence_count]
  - expect: One bag and one bowl, and sugar comes only from the bag.
  - fail: Sugar appears in the bowl with no stream; or the bowl duplicates; or sugar passes through the bowl.
- P6 [minor · attribute_drift]
  - expect: The bag, the bowl and the kitchen stay the same.
  - fail: The sugar changes colour; or the bowl changes shape; or the kitchen rearranges.

## MECH-0161 · granular · train

**Caption.** A bucket packed with damp sand is turned upside down on the beach and lifted off, leaving a bucket-shaped sand tower standing.

**Expectation (hidden).** The tower keeps the bucket's shape with edges crumbling slightly as the bucket comes away; it does not slump into a heap or stay stuck in the bucket.

**Declared violation types.** material_response, shape_identity

**SA**
- S1 [core] A bucket packed with damp sand is turned upside down on the beach.
- S2 [core] The bucket is lifted off.
- S3 [core] A bucket-shaped sand tower stands.
- S4 [minor] The sand is damp.
- S5 [minor] The lift comes first and the tower stands after.

**PC**
- P1 [core · material_response]
  - expect: The tower keeps the bucket's shape with edges crumbling slightly as the bucket comes away.
  - fail: It slumps into a heap; or it flows like liquid; or it stays stuck in the bucket.
- P2 [core · shape_identity]
  - expect: The tower is one solid shape that mirrors the bucket.
  - fail: It splits into pieces as the bucket lifts; or it changes shape after the bucket is gone; or it grows.
- P3 [major · gravity_direction]
  - expect: Loose sand falls down around the base.
  - fail: Sand rises; or hangs; or the tower lifts with the bucket and hangs.
- P4 [major · causeless_motion]
  - expect: The tower stays where it was formed.
  - fail: It slides; or tips over with nothing touching it; or jumps.
- P5 [fatal · permanence_count]
  - expect: One bucket and one tower keep their number.
  - fail: The tower vanishes or a second appears; or the bucket passes through the tower; or the tower turns into another object.
- P6 [minor · attribute_drift]
  - expect: The bucket's colour and the beach stay the same.
  - fail: The bucket changes colour; or the sand changes colour; or the beach rearranges.

## MECH-0162 · granular · train

**Caption.** A bag of rice slips off a kitchen counter, splits open on the floor, and rice grains scatter across the floor.

**Expectation (hidden).** The grains spray outward from the split as the bag hits and spread into a wide scatter; they do not stay in a bag shape or bounce back into the bag.

**Declared violation types.** material_response, permanence_count

**SA**
- S1 [core] A bag of rice slips off a kitchen counter.
- S2 [core] It splits open on the floor.
- S3 [core] Rice grains scatter across the floor.
- S4 [minor] The fall comes first, then the split, then the scatter.

**PC**
- P1 [core · material_response]
  - expect: The grains spray outward from the split as the bag hits and spread into a wide scatter.
  - fail: They stay in a bag shape; or bounce back into the bag; or flow like liquid.
- P2 [core · permanence_count]
  - expect: The rice on the floor is the rice from the bag, and the bag stays split.
  - fail: The bag reseals; or rice appears from nowhere; or the bag stays full while rice covers the floor.
- P3 [major · gravity_direction]
  - expect: The bag falls and the grains fall and settle.
  - fail: Grains rise; or hang; or the bag floats.
- P4 [major · trajectory_momentum]
  - expect: Grains skitter along the floor away from the impact and stop.
  - fail: They gather themselves into a pile; or move as one block; or set off again after stopping.
- P5 [fatal · shape_identity]
  - expect: One bag keeps its number, and it does not pass through the floor.
  - fail: The bag duplicates; or it passes through the floor; or it turns into another object.
- P6 [minor · attribute_drift]
  - expect: The bag's printing and the kitchen floor stay the same.
  - fail: The printing changes; or the floor pattern shifts; or the kitchen rearranges.

## MECH-0163 · granular · train

**Caption.** A salt shaker is shaken over a plate of fries and salt grains fall onto the fries.

**Expectation (hidden).** Grains fall from the holes only during each shake and land on the fries and plate below; they do not hang in the air or fall upward.

**Declared violation types.** gravity_direction, material_response

**SA**
- S1 [core] A salt shaker is held over a plate of fries.
- S2 [core] It is shaken.
- S3 [core] Salt grains fall onto the fries.
- S4 [minor] The shake comes first and the fall follows.

**PC**
- P1 [core · gravity_direction]
  - expect: Grains fall from the holes straight down onto the fries and plate.
  - fail: They hang in the air; or fall upward; or drift sideways.
- P2 [core · material_response]
  - expect: Grains fall as separate specks during each shake, not as a stream or lump.
  - fail: Salt pours as a solid rod; or as liquid; or as one lump.
- P3 [major · missing_consequence]
  - expect: Grains fall only during each shake.
  - fail: Grains fall with the shaker still; or the shake produces nothing; or grains keep falling after the shake stops.
- P4 [major · process_direction]
  - expect: Salt on the fries only accumulates.
  - fail: It vanishes; or it is there before the shake; or it jumps.
- P5 [fatal · permanence_count]
  - expect: One shaker, and salt comes only from it.
  - fail: Salt appears with no shaker above; or the shaker duplicates; or salt passes through the shaker.
- P6 [minor · attribute_drift]
  - expect: The shaker, the plate and the fries stay the same.
  - fail: The shaker changes; or the plate changes; or the fries rearrange.

## MECH-0164 · granular · train

**Caption.** A dump truck tips its bed and unloads a pile of gravel onto a construction site, where it settles into a heap.

**Expectation (hidden).** The gravel slides out in a rush as the bed tilts, spreads at the bottom, and forms a broad cone with sloping sides; it does not hold the bed's shape.

**Declared violation types.** material_response, gravity_direction

**SA**
- S1 [core] A dump truck tips its bed.
- S2 [core] Gravel slides out.
- S3 [core] The gravel settles into a heap on the ground.
- S4 [minor] The setting is a construction site.
- S5 [minor] The tip comes first and the heap forms after.

**PC**
- P1 [core · material_response]
  - expect: The gravel slides out in a rush as the bed tilts, spreads at the bottom, and forms a broad cone with sloping sides.
  - fail: It holds the bed's shape on the ground; or flows flat like liquid; or stays in the bed with the bed tipped.
- P2 [core · gravity_direction]
  - expect: Gravel falls downward from the bed and piles from the ground up.
  - fail: It rises; or hangs; or the heap forms in the air.
- P3 [major · process_direction]
  - expect: The heap only grows and the bed only empties.
  - fail: The heap shrinks; or the bed refills; or it jumps.
- P4 [major · causeless_motion]
  - expect: The truck stays put.
  - fail: It slides; or lifts; or the heap moves after settling.
- P5 [fatal · permanence_count]
  - expect: One truck, and gravel comes only from the bed.
  - fail: Gravel appears with no truck; or the truck duplicates; or gravel passes through the bed.
- P6 [minor · attribute_drift]
  - expect: The truck's colour and the site stay the same.
  - fail: The truck changes colour; or the site rearranges; or the gravel changes colour.

## MECH-0165 · granular · train

**Caption.** An hourglass is turned over on a desk, and sand runs from the top chamber into the bottom one.

**Expectation (hidden).** The sand runs in a thin steady stream through the neck, a cone building in the bottom while the top empties; the flow does not reverse or stop midway.

**Declared violation types.** process_direction, gravity_direction

**SA**
- S1 [core] An hourglass stands on a desk.
- S2 [core] It is turned over.
- S3 [core] Sand runs from the top chamber into the bottom one.
- S4 [minor] The turn comes first and the flow follows.

**PC**
- P1 [core · process_direction]
  - expect: The top empties and the bottom fills steadily, and the flow never reverses or stops midway.
  - fail: The flow reverses; or it stops with sand left above; or the bottom fills before the flip.
- P2 [core · gravity_direction]
  - expect: The sand runs down through the neck in a thin stream and builds a cone below.
  - fail: Sand rises; or hangs in the neck; or the cone builds on the ceiling of the chamber.
- P3 [major · material_response]
  - expect: The stream is thin and steady and the cone slumps at the sides.
  - fail: Sand pours as a lump; or as liquid with a flat surface; or the cone is a column.
- P4 [major · causeless_motion]
  - expect: The hourglass stays put after the flip.
  - fail: It slides; or tips; or sand flows with the hourglass still upright and full below.
- P5 [fatal · permanence_count]
  - expect: One hourglass, and the sand keeps its total.
  - fail: Sand appears from nowhere; or vanishes; or the hourglass duplicates.
- P6 [minor · attribute_drift]
  - expect: The hourglass's frame, the sand's colour and the desk stay the same.
  - fail: The frame changes; or the sand changes colour; or the desk rearranges.

## MECH-0166 · granular · train

**Caption.** A bag of soil is emptied into a flower pot, filling it with a loose heap.

**Expectation (hidden).** The soil falls in clumps and crumbs and settles when the pot is tapped; it does not pour like liquid or hold the bag's shape.

**Declared violation types.** material_response, gravity_direction

**SA**
- S1 [core] A bag of soil is emptied into a flower pot.
- S2 [core] The pot fills with a heap of soil.
- S3 [minor] The heap is loose rather than packed.
- S4 [minor] The emptying comes first and the heap forms after.

**PC**
- P1 [core · material_response]
  - expect: The soil falls in clumps and crumbs and settles as a loose heap.
  - fail: It pours like liquid with a flat surface; or it holds the bag's shape; or it comes out as one block.
- P2 [core · gravity_direction]
  - expect: It falls down into the pot and piles from the bottom.
  - fail: Soil rises; or hangs; or the heap floats above the rim.
- P3 [major · process_direction]
  - expect: The heap only grows and the bag only empties.
  - fail: The heap shrinks; or the bag refills; or it jumps.
- P4 [major · missing_consequence] (if: The bag's tilt is visible in the clip.)
  - expect: The bag's tilt produces the flow.
  - fail: Soil pours from an upright bag; or the bag is tipped and nothing comes out; or the flow continues after the bag is righted.
- P5 [fatal · permanence_count]
  - expect: One bag and one pot, and soil comes only from the bag.
  - fail: Soil appears in the pot with no flow; or the pot duplicates; or soil passes through the pot.
- P6 [minor · attribute_drift]
  - expect: The bag, the pot and the surroundings stay the same.
  - fail: The soil changes colour; or the pot changes shape; or the surroundings rearrange.

## MECH-0167 · granular · train

**Caption.** Bare feet walk across a stretch of dry beach sand, leaving a trail of footprints behind.

**Expectation (hidden).** Each foot sinks a little and pushes sand up around the print; the prints appear only where a foot has stepped and stay behind.

**Declared violation types.** material_response, missing_consequence

**SA**
- S1 [core] Bare feet walk across dry beach sand.
- S2 [core] Footprints are left behind.
- S3 [minor] The feet are bare.
- S4 [minor] The prints trail behind, in the direction walked from.

**PC**
- P1 [core · material_response]
  - expect: Each foot sinks a little and pushes sand up around the print.
  - fail: The sand stays flat under the foot; or the foot sinks to the ankle; or the sand flows like liquid.
- P2 [core · missing_consequence]
  - expect: Prints appear only where a foot has stepped and stay behind.
  - fail: Prints appear ahead of the walker; or where no foot went; or prints vanish or fill in behind.
- P3 [major · permanence_count]
  - expect: The number of prints matches the steps taken.
  - fail: Prints multiply; or a print disappears; or prints appear in a line with no walker.
- P4 [major · gravity_direction]
  - expect: Displaced sand falls back to the ground.
  - fail: It rises; or hangs in the air; or floats.
- P5 [fatal · shape_identity]
  - expect: The feet keep their number and shape, and they do not pass through the sand.
  - fail: A foot detaches; or extra feet appear; or a foot passes below the sand's surface entirely.
- P6 [minor · attribute_drift]
  - expect: The sand's colour and the beach stay the same.
  - fail: The sand changes colour; or the beach rearranges; or the feet change.

**Note.** The walker is kept because the feet are the physics. Gait is not judged.

## MECH-0168 · granular · train

**Caption.** Snow is shovelled off a driveway onto the lawn, building a ragged pile there.

**Expectation (hidden).** Each shovelful flies in a loose clump that breaks apart in the air and lands scattered; the driveway clears where it has been shovelled.

**Declared violation types.** material_response, trajectory_momentum

**SA**
- S1 [core] Snow is shovelled off a driveway.
- S2 [core] Each shovelful is thrown onto the lawn.
- S3 [core] A pile builds on the lawn.
- S4 [minor] The pile is ragged.
- S5 [minor] The driveway clears where it has been shovelled.

**PC**
- P1 [core · trajectory_momentum]
  - expect: Each shovelful flies in a loose clump along the swing's direction and lands on the lawn.
  - fail: It flies backward; or hangs; or lands back on the driveway from a swing toward the lawn.
- P2 [core · material_response]
  - expect: The clump breaks apart in the air and lands scattered, and the pile is loose and ragged.
  - fail: It stays a rigid block; or flows like liquid; or the pile is a smooth dome.
- P3 [major · missing_consequence]
  - expect: The driveway clears where it has been shovelled.
  - fail: The driveway stays covered after shovelling; or it clears ahead of the shovel; or snow reappears.
- P4 [major · gravity_direction]
  - expect: Thrown snow falls.
  - fail: It rises; or hangs; or floats.
- P5 [fatal · shape_identity]
  - expect: One shovel keeps its shape, and snow passes through nothing.
  - fail: The shovel passes through the snow; or a second shovel appears; or snow passes through the lawn.
- P6 [minor · attribute_drift]
  - expect: The driveway, the lawn and the house stay the same.
  - fail: The driveway changes; or the lawn changes; or the house rearranges.

**Note.** The shoveller is kept because the swing is the physics. Technique is not judged.

## MECH-0169 · granular · train

**Caption.** Dried beans are poured from a bag into a glass jar until it is full and beans spill over onto the counter.

**Expectation (hidden).** The beans fill the jar from the bottom up; the overflow begins when the jar is full and the extra beans bounce and roll on the counter.

**Declared violation types.** material_response, missing_consequence

**SA**
- S1 [core] Dried beans are poured from a bag into a glass jar.
- S2 [core] The jar fills.
- S3 [core] Beans spill over onto the counter.
- S4 [minor] The pour comes first, then the fill, then the spill.

**PC**
- P1 [core · material_response]
  - expect: The beans fill the jar from the bottom up as loose grains, and overflow beans bounce and roll on the counter.
  - fail: Beans pour as a lump; or flow like liquid; or the overflow sticks in a heap on the rim.
- P2 [core · missing_consequence]
  - expect: The overflow begins when the jar is full and not before.
  - fail: Beans spill with the jar half-full; or the jar overfills into a dome with none spilling; or beans spill before pouring.
- P3 [major · gravity_direction]
  - expect: The stream falls and spilled beans fall to the counter.
  - fail: Beans rise; or hang; or float.
- P4 [major · process_direction]
  - expect: The jar only fills.
  - fail: It empties; or jumps; or is full before the pour.
- P5 [fatal · permanence_count]
  - expect: One bag and one jar, and beans come only from the bag.
  - fail: Beans appear with no stream; or the jar duplicates; or beans pass through the glass.
- P6 [minor · attribute_drift]
  - expect: The jar, the bag and the counter stay the same.
  - fail: The jar changes shape; or the beans change colour; or the counter rearranges.

## MECH-0170 · granular · train

**Caption.** A handful of seed is scattered across bare soil with a sweeping throw, and the seeds land spread over a wide patch.

**Expectation (hidden).** The seeds fan out through the air in an arc during the sweep and drop onto the soil; they do not hang in the air or land in a single spot.

**Declared violation types.** trajectory_momentum, gravity_direction

**SA**
- S1 [core] A handful of seed is thrown with a sweeping motion over bare soil.
- S2 [core] The seeds land spread over a wide patch.
- S3 [minor] The throw is a sweep rather than a drop.
- S4 [minor] The throw comes first and the landing follows.

**PC**
- P1 [core · trajectory_momentum]
  - expect: Seeds fan out through the air in an arc during the sweep.
  - fail: They fly back at the thrower; or all go to a single spot; or hang in the air.
- P2 [core · gravity_direction]
  - expect: The seeds drop onto the soil and stay.
  - fail: They hang; or rise; or bounce high.
- P3 [major · material_response]
  - expect: Seeds are tiny separate grains that scatter, not a stream or a clump.
  - fail: They fly as one lump; or as a rope; or as liquid.
- P4 [major · causeless_motion]
  - expect: Seeds move only from the throw, and once landed they stay.
  - fail: They move before the throw; or hop after landing; or drift.
- P5 [fatal · permanence_count]
  - expect: Seeds come only from the hand.
  - fail: Seeds appear with no throw; or vanish in mid-air; or multiply.
- P6 [minor · attribute_drift]
  - expect: The soil and the surroundings stay the same.
  - fail: The soil changes colour; or the field rearranges; or the hand changes.

**Note.** The hand is kept as the minimal trigger; the person is not judged.

## MECH-0171 · granular · train

**Caption.** A used coffee filter is knocked against the rim of a bin, and the puck of wet grounds drops out and breaks apart in the bin.

**Expectation (hidden).** The puck comes loose on the knock and falls straight down, breaking into clumps and crumbs as it lands; it does not float or stay in the filter.

**Declared violation types.** material_response, gravity_direction

**SA**
- S1 [core] A used coffee filter is knocked against the rim of a bin.
- S2 [core] The puck of grounds drops out.
- S3 [core] It breaks apart in the bin.
- S4 [minor] The grounds are wet.
- S5 [minor] The knock comes first, then the drop, then the break-up.

**PC**
- P1 [core · material_response]
  - expect: The puck comes loose on the knock as one damp mass and breaks into clumps and crumbs as it lands.
  - fail: It stays in the filter; or pours like liquid; or bounces like rubber.
- P2 [core · gravity_direction]
  - expect: It falls straight down into the bin.
  - fail: It floats; or rises; or drifts sideways.
- P3 [major · missing_consequence]
  - expect: The knock frees the puck, and the filter is emptier afterward.
  - fail: The puck falls before the knock; or the knock frees nothing; or the filter is still full after the puck lands.
- P4 [major · causeless_motion]
  - expect: The bin stays put.
  - fail: It slides; or tips; or the puck moves after landing.
- P5 [fatal · permanence_count]
  - expect: One filter and one bin keep their number.
  - fail: The filter duplicates; or the puck vanishes in mid-air; or the bin turns into another object.
- P6 [minor · attribute_drift]
  - expect: The filter, the bin and the kitchen stay the same.
  - fail: The filter changes colour; or the bin changes; or the kitchen rearranges.

## MECH-0172 · granular · train

**Caption.** The top of a small pile of dry sand in a sandbox is kicked, and sand sprays forward and leaves a gouge in the pile.

**Expectation (hidden).** The spray goes in the direction of the kick and falls back to the ground a short way off; the pile does not move as one block.

**Declared violation types.** material_response, trajectory_momentum

**SA**
- S1 [core] A small pile of dry sand is in a sandbox.
- S2 [core] The top of it is kicked.
- S3 [core] Sand sprays forward.
- S4 [core] A gouge is left in the pile.
- S5 [minor] The sand is dry.
- S6 [minor] The kick comes first, then the spray and the gouge.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The spray goes in the direction of the kick.
  - fail: It sprays back at the kicker; or straight up; or the pile moves as one block.
- P2 [core · material_response]
  - expect: Dry sand flies as grains and falls back a short way off, and the gouge has loose sloping sides.
  - fail: It clumps like wet sand; or flows like water; or the pile stays intact.
- P3 [major · gravity_direction]
  - expect: Sprayed sand falls to the ground.
  - fail: It hangs; or rises; or floats.
- P4 [major · missing_consequence]
  - expect: The gouge is where the foot struck.
  - fail: The gouge is elsewhere; or there is no gouge; or the gouge is there before the kick.
- P5 [fatal · shape_identity]
  - expect: The foot keeps its shape and does not pass through the sandbox.
  - fail: The foot passes through the sandbox floor; or a second foot appears; or the pile turns into another object.
- P6 [minor · attribute_drift]
  - expect: The sandbox and the surroundings stay the same.
  - fail: The sandbox changes; or the sand changes colour; or the surroundings rearrange.

**Note.** The foot is kept as the minimal trigger; the person is not judged.

## MECH-0173 · granular · train

**Caption.** A box of dry pasta is tipped into a pot of boiling water, and the pasta sinks and settles at the bottom.

**Expectation (hidden).** The pieces slide out and splash into the water, then sink; they do not float on the surface or hang in the water.

**Declared violation types.** material_response, gravity_direction

**SA**
- S1 [core] A box of dry pasta is tipped into a pot of boiling water.
- S2 [core] The pasta sinks.
- S3 [core] It settles at the bottom.
- S4 [minor] The water is boiling.
- S5 [minor] The tip comes first, then the sinking, then the settling.

**PC**
- P1 [core · gravity_direction]
  - expect: The pieces slide out, splash in, and sink to the bottom.
  - fail: They float on the surface; or hang mid-water; or rise.
- P2 [core · material_response]
  - expect: The pieces are rigid dry pasta that clatter and pile loosely.
  - fail: They bend like cooked pasta at once; or dissolve; or land as one block.
- P3 [major · missing_consequence]
  - expect: A splash and a disturbed surface appear where the pasta lands.
  - fail: The surface is undisturbed; or the splash is elsewhere; or the splash comes before the pasta.
- P4 [major · causeless_motion]
  - expect: The pot stays put.
  - fail: It slides; or tips; or the pasta moves after settling.
- P5 [fatal · permanence_count]
  - expect: One box and one pot, and pasta comes only from the box.
  - fail: Pasta appears with no tip; or the pot duplicates; or pasta passes through the pot.
- P6 [minor · attribute_drift]
  - expect: The pot, the box and the stove stay the same.
  - fail: The pot changes; or the box changes; or the stove rearranges.

## MECH-0174 · granular · train

**Caption.** A cat digs in a litter box with its front paws, flinging litter backward and leaving a hollow.

**Expectation (hidden).** Litter is flung in small showers in the direction of the paw strokes and lands nearby; the hollow forms where the paws dig.

**Declared violation types.** material_response, trajectory_momentum

**SA**
- S1 [core] A cat digs in a litter box with its front paws.
- S2 [core] Litter is flung backward.
- S3 [core] A hollow is left where it digs.
- S4 [minor] The digging is with the front paws.
- S5 [minor] The digging comes first and the hollow forms after.

**PC**
- P1 [core · trajectory_momentum]
  - expect: Litter is flung in small showers in the direction of the paw strokes, backward.
  - fail: It is flung forward; or up and out of the box in a fountain; or no litter moves.
- P2 [core · material_response]
  - expect: Litter is loose grains that scatter and fall, and the hollow has sloping sides.
  - fail: It clumps into one mass; or flows like liquid; or the hollow has vertical walls.
- P3 [major · gravity_direction]
  - expect: Flung litter falls back.
  - fail: It hangs; or rises; or floats.
- P4 [major · missing_consequence]
  - expect: The hollow forms where the paws dig.
  - fail: It forms elsewhere; or there is no hollow; or the hollow is there before the digging.
- P5 [fatal · shape_identity]
  - expect: One cat keeps its limbs and shape.
  - fail: A paw detaches; or a second cat appears; or the cat passes through the box.
- P6 [minor · attribute_drift]
  - expect: The cat's markings and the box stay the same.
  - fail: The markings change; or the box changes; or the room rearranges.

**Note.** The cat is self-driven: its digging is its own. Only the litter's behaviour is judged.

## MECH-0175 · granular · train

**Caption.** A stick is dragged through a patch of loose gravel on a path, leaving a furrow behind it.

**Expectation (hidden).** Small ridges of pushed-aside stones form on each side of the furrow as the stick moves; the furrow does not appear ahead of the stick or close up behind it.

**Declared violation types.** material_response, missing_consequence

**SA**
- S1 [core] A stick is dragged through a patch of loose gravel on a path.
- S2 [core] A furrow is left behind it.
- S3 [minor] The gravel is loose.
- S4 [minor] The furrow trails behind the stick, not ahead of it.

**PC**
- P1 [core · material_response]
  - expect: Small ridges of pushed-aside stones form on each side of the furrow as the stick moves.
  - fail: The gravel closes behind like liquid; or the stick leaves no mark; or the stones fly up in a spray.
- P2 [core · missing_consequence]
  - expect: The furrow appears only where the stick has passed and stays.
  - fail: It appears ahead of the stick; or closes up behind; or appears elsewhere.
- P3 [major · causeless_motion]
  - expect: The stick moves only as dragged and stones move only as pushed.
  - fail: Stones move ahead of the stick; or the stick moves by itself; or stones rearrange after the stick has passed.
- P4 [major · gravity_direction]
  - expect: Displaced stones settle down.
  - fail: They hang; or rise; or float.
- P5 [fatal · permanence_count]
  - expect: One stick keeps its number, and the stones keep theirs.
  - fail: The stick duplicates; or stones vanish; or the stick passes through the path.
- P6 [minor · attribute_drift]
  - expect: The path and the surroundings stay the same.
  - fail: The gravel changes colour; or the path rearranges; or the stick changes.

**Note.** The hand on the stick is kept as the minimal trigger; the person is not judged.

## MECH-0176 · gas_wind · train

**Caption.** An inflated balloon held shut at the neck is let go without being tied, and it shoots off around the room until it drops limp to the floor.

**Expectation (hidden).** The balloon flies erratically while air escapes and shrinks as it goes; it falls only once empty and does not reinflate.

**Declared violation types.** trajectory_momentum, shape_identity

**SA**
- S1 [core] An inflated balloon is held shut at the neck.
- S2 [core] It is let go.
- S3 [core] It shoots off around the room.
- S4 [core] It drops limp to the floor.
- S5 [minor] The neck is not tied.
- S6 [minor] The release comes first, then the flight, then the drop.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The balloon flies erratically while air escapes, changing direction as the neck whips.
  - fail: It flies in a straight steady line like a thrown ball; or it hangs in the air; or it flies while still held shut.
- P2 [core · shape_identity]
  - expect: It shrinks as it goes and ends limp, and it does not reinflate.
  - fail: It stays fully round while flying; or it reinflates on the floor; or it grows.
- P3 [major · gravity_direction]
  - expect: It falls to the floor once empty and stays there.
  - fail: It stays aloft after going limp; or rises steadily to the ceiling; or bounces back up on its own.
- P4 [major · causeless_motion]
  - expect: It moves only while air escapes and nothing else pushes it.
  - fail: It moves before release; or keeps zipping about after going limp; or is pushed along the floor by nothing.
- P5 [fatal · permanence_count]
  - expect: One balloon keeps its number and passes through nothing.
  - fail: It duplicates; or passes through a wall; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The balloon's colour and the room stay the same.
  - fail: The balloon changes colour; or the room rearranges; or the furniture changes.

## MECH-0177 · gas_wind · train

**Caption.** A gust of wind lifts a wide-brimmed hat off a bench on a seafront and carries it away along the ground.

**Expectation (hidden).** The hat moves in the same direction as other things blown by the wind, tumbling and skipping along; it does not move against the wind.

**Declared violation types.** trajectory_momentum, causeless_motion

**SA**
- S1 [core] A wide-brimmed hat rests on a bench on a seafront.
- S2 [core] The hat lifts off the bench.
- S3 [core] It is carried away along the ground.
- S4 [minor] Other signs of wind are visible.
- S5 [minor] The lift comes first and the tumble along the ground follows.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The hat moves the same way as other things blown by the wind, tumbling and skipping along.
  - fail: It moves against the direction other things are blown; or it glides smoothly in a straight line as if pushed; or it moves crosswise to the visible wind signs.
- P2 [core · causeless_motion]
  - expect: The hat moves when the gust arrives and eases when the wind eases.
  - fail: It lifts with nothing else stirring; or it keeps travelling steadily while everything else is still; or it moves before any other sign of wind.
- P3 [major · gravity_direction]
  - expect: It lifts a little and comes down, tumbling along the ground rather than soaring.
  - fail: It soars high and keeps rising; or hangs in the air; or rolls along without touching the ground.
- P4 [major · material_response]
  - expect: The brim flexes and flaps in the wind.
  - fail: It is rigid as a plate; or folds like cloth; or turns inside out and stays so.
- P5 [fatal · permanence_count]
  - expect: One hat keeps its number and passes through nothing.
  - fail: It duplicates; or passes through the bench; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The hat's colour and the seafront stay the same.
  - fail: The hat changes colour; or the bench changes; or the seafront rearranges.

## MECH-0178 · gas_wind · train

**Caption.** A gust of wind hits a dandelion clock standing in a meadow, and the seeds detach and drift away.

**Expectation (hidden).** The seeds leave in the direction of the wind and float slowly downward as they drift; the stalk is left bare and the seeds do not return.

**Declared violation types.** trajectory_momentum, permanence_count

**SA**
- S1 [core] A dandelion clock stands in a meadow.
- S2 [core] A gust of wind hits it.
- S3 [core] The seeds detach.
- S4 [core] The seeds drift away.
- S5 [minor] The gust comes first, then the seeds detach, then they drift.

**PC**
- P1 [core · trajectory_momentum]
  - expect: Seeds leave in the direction of the wind and drift slowly, sinking gradually.
  - fail: They fly against the wind; or shoot off fast like grains; or drift in different directions from one another on one gust.
- P2 [core · permanence_count]
  - expect: The stalk is left bare where seeds left, and the seeds do not return or regrow.
  - fail: Seeds return to the head; or the head refills; or the head stays full while seeds fly.
- P3 [major · causeless_motion]
  - expect: Seeds leave when the gust arrives.
  - fail: They leave with the grass still; or the head stays intact through a gust that bends the grass; or they leave before the gust.
- P4 [major · gravity_direction]
  - expect: The seeds float slowly downward as they drift.
  - fail: They rise steadily; or hang still; or drop like stones.
- P5 [fatal · shape_identity]
  - expect: One dandelion keeps its stalk, and the seeds are its own.
  - fail: The stalk vanishes; or a second head appears; or the seeds turn into other objects.
- P6 [minor · attribute_drift]
  - expect: The meadow and the surroundings stay the same.
  - fail: The grass changes colour; or the meadow rearranges; or the stalk changes.

## MECH-0179 · gas_wind · train

**Caption.** A desk fan is switched on next to a loose stack of papers, and the top sheets lift and scatter across the desk and floor.

**Expectation (hidden).** The sheets move only after the fan starts and fly away from it; the bottom sheets stay longer than the top ones.

**Declared violation types.** causeless_motion, trajectory_momentum

**SA**
- S1 [core] A desk fan stands next to a loose stack of papers.
- S2 [core] The fan is switched on.
- S3 [core] The top sheets lift.
- S4 [core] Sheets scatter across the desk and floor.
- S5 [minor] The stack is loose.
- S6 [minor] The switch comes first, then the lift, then the scatter.

**PC**
- P1 [core · causeless_motion]
  - expect: Sheets move only after the fan starts.
  - fail: Sheets fly before the fan is on; or the fan runs and nothing moves; or sheets keep flying after the fan is off.
- P2 [core · trajectory_momentum]
  - expect: Sheets fly away from the fan.
  - fail: They fly toward the fan; or sideways across the airflow; or straight up and hover.
- P3 [major · process_direction]
  - expect: The top sheets go first and the bottom sheets stay longer.
  - fail: Bottom sheets fly first; or the whole stack lifts as one; or sheets restack themselves.
- P4 [major · gravity_direction]
  - expect: Sheets fall to the desk or floor and settle.
  - fail: They hang; or rise to the ceiling; or float.
- P5 [fatal · permanence_count]
  - expect: The sheets keep their number and the fan stays one fan.
  - fail: Sheets multiply; or vanish; or the fan duplicates.
- P6 [minor · attribute_drift]
  - expect: The fan, the desk and the room stay the same.
  - fail: The fan changes colour; or the desk rearranges; or the papers change printing.

## MECH-0180 · gas_wind · train

**Caption.** An umbrella is opened on a windy street corner, and the wind tugs it sideways and flips the canopy inside out.

**Expectation (hidden).** The umbrella leans downwind and pulls at the hand holding it; the flip happens when a gust catches the underside; the canopy does not return to shape on its own.

**Declared violation types.** material_response, causeless_motion

**SA**
- S1 [core] An umbrella is opened on a street corner.
- S2 [core] It is tugged sideways by the wind.
- S3 [core] The canopy flips inside out.
- S4 [minor] The street is windy, with other signs of wind.
- S5 [minor] The opening comes first, then the tug, then the flip.

**PC**
- P1 [core · material_response]
  - expect: The canopy strains, then inverts with a snap as the ribs bend, and it does not return on its own.
  - fail: The canopy returns to shape on its own; or it is rigid like a plate; or it tears into strips.
- P2 [core · causeless_motion]
  - expect: The umbrella leans downwind and the flip happens when a gust catches the underside.
  - fail: It leans upwind; or flips with no sign of wind; or flips before it is opened.
- P3 [major · trajectory_momentum]
  - expect: The pull is in the direction the wind blows other things.
  - fail: It pulls opposite to other wind signs; or spins in place; or flies straight up out of the hand.
- P4 [major · missing_consequence]
  - expect: The hand holding it is pulled and the arm strains.
  - fail: The hand is unmoved while the umbrella strains; or the umbrella flips with the handle not moving at all; or the arm moves before the wind.
- P5 [fatal · shape_identity]
  - expect: One umbrella keeps its number, and no rib passes through the fabric.
  - fail: Ribs pass through the canopy; or the umbrella duplicates; or it turns into another object.
- P6 [minor · attribute_drift]
  - expect: The umbrella's colour and the street stay the same.
  - fail: The umbrella changes colour; or the street rearranges; or the hand changes.

**Note.** The hand is kept as the anchor the wind pulls against; the person is not judged.

## MECH-0181 · gas_wind · train

**Caption.** Smoke rises from a house chimney on a calm winter evening and thins out as it climbs.

**Expectation (hidden).** The column drifts upward and widens; it does not sink to the ground or gather back into the chimney.

**Declared violation types.** gravity_direction, process_direction

**SA**
- S1 [core] Smoke comes out of a house chimney.
- S2 [core] It rises.
- S3 [core] It thins out as it climbs.
- S4 [minor] The evening is calm, so the column stays near vertical.

**PC**
- P1 [core · gravity_direction]
  - expect: The column drifts upward.
  - fail: It sinks to the ground; or hangs at chimney height; or flows down the roof.
- P2 [core · process_direction]
  - expect: It widens and thins with height and does not gather back.
  - fail: It gathers back into the chimney; or gets denser higher up; or forms a solid shape.
- P3 [major · causeless_motion]
  - expect: On a calm evening the column drifts gently with no sharp turns.
  - fail: It whips sideways; or jumps; or a piece detaches and drifts as a block.
- P4 [major · material_response]
  - expect: The smoke is diffuse, translucent and swirling.
  - fail: It is a solid shape; or a liquid; or a rigid stick.
- P5 [fatal · permanence_count]
  - expect: One chimney is the source.
  - fail: Smoke appears elsewhere; or the chimney duplicates; or the smoke vanishes all at once.
- P6 [minor · attribute_drift]
  - expect: The house, the roof and the sky stay the same.
  - fail: The house changes; or the roof rearranges; or the sky changes colour.

## MECH-0182 · gas_wind · train

**Caption.** A bubble machine in a park sends out a stream of soap bubbles; the bubbles float away on the breeze and pop one by one.

**Expectation (hidden).** The bubbles drift with the wind and sink slowly; each pops when it touches something or after a few seconds and does not re-form.

**Declared violation types.** trajectory_momentum, permanence_count

**SA**
- S1 [core] A bubble machine in a park sends out bubbles.
- S2 [core] The bubbles float away on the breeze.
- S3 [core] They pop one by one.
- S4 [minor] There is a stream of many bubbles.
- S5 [minor] The float comes first and the pops follow.

**PC**
- P1 [core · trajectory_momentum]
  - expect: Bubbles drift with the wind, all the same way, and sink slowly.
  - fail: They fly in different directions on one breeze; or against the wind; or shoot off fast.
- P2 [core · permanence_count]
  - expect: Each pops when it touches something or after a few seconds and does not re-form.
  - fail: A popped bubble reappears; or bubbles merge and split; or bubbles appear from nowhere away from the machine.
- P3 [major · gravity_direction]
  - expect: They sink slowly as they drift.
  - fail: They rise steadily; or hang still; or drop like stones.
- P4 [major · material_response]
  - expect: Bubbles are thin and iridescent, wobble, and vanish when they pop.
  - fail: They bounce off the ground like rubber balls; or hold a rigid shape when they hit something; or shatter into shards.
- P5 [fatal · shape_identity]
  - expect: One machine keeps its shape and is the only source.
  - fail: The machine duplicates; or it turns into another object; or bubbles pass through a person.
- P6 [minor · attribute_drift]
  - expect: The machine and the park stay the same.
  - fail: The machine changes colour; or the park rearranges; or the trees change.

## MECH-0183 · gas_wind · train

**Caption.** A light curtain hanging in front of an open window billows into the room with each gust of wind and falls back between gusts.

**Expectation (hidden).** The curtain moves in step with the wind, inward with a gust and back when it drops; it does not move on its own or against the wind.

**Declared violation types.** causeless_motion, material_response

**SA**
- S1 [core] A light curtain hangs in front of an open window.
- S2 [core] It billows into the room.
- S3 [core] It falls back.
- S4 [minor] The billowing repeats with each gust.
- S5 [minor] Each billow comes first and the fall back follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The curtain moves in step with the wind, inward with a gust and back when it drops.
  - fail: It moves with the window shut and no wind signs; or it billows outward through the window against the gust; or it stays rigidly still while other things blow.
- P2 [core · material_response]
  - expect: The light fabric flows and ripples and hangs in folds when slack.
  - fail: It is rigid like a board; or stretches like elastic; or stays inflated after the gust.
- P3 [major · gravity_direction]
  - expect: Between gusts it hangs down from the rail.
  - fail: It hangs sideways with no wind; or rises to the ceiling; or floats.
- P4 [major · trajectory_momentum]
  - expect: The billow is into the room, downwind of the window.
  - fail: It billows outward with the same wind; or alternates directions with no cause; or swings crosswise.
- P5 [fatal · permanence_count]
  - expect: One curtain on one rail keeps its number.
  - fail: The curtain duplicates; or passes through the wall; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The curtain's colour and the room stay the same.
  - fail: The curtain changes colour; or the window changes; or the room rearranges.

## MECH-0184 · gas_wind · train

**Caption.** A hairdryer is aimed at a long-haired wig on a stand, and the hair streams away from the nozzle.

**Expectation (hidden).** The hair blows in the direction the dryer points and falls back when the dryer is moved away.

**Declared violation types.** causeless_motion, trajectory_momentum

**SA**
- S1 [core] A long-haired wig sits on a stand.
- S2 [core] A hairdryer is aimed at it.
- S3 [core] The hair streams away from the nozzle.
- S4 [minor] The dryer is aimed first and the hair moves after.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The hair blows in the direction the dryer points.
  - fail: It blows toward the nozzle; or sideways; or straight up when the dryer points across.
- P2 [core · causeless_motion]
  - expect: The hair moves only while the dryer is running and aimed, and falls back when the dryer moves away.
  - fail: The hair streams with the dryer off; or stays streaming after the dryer moves away; or moves before the dryer is aimed.
- P3 [major · material_response]
  - expect: The hair flows in strands and flutters.
  - fail: It moves as a rigid block; or stretches; or detaches all at once.
- P4 [major · gravity_direction]
  - expect: When the airflow stops the hair falls back down.
  - fail: It stays up; or rises; or hangs out sideways.
- P5 [fatal · shape_identity]
  - expect: One wig on one stand keeps its number.
  - fail: The wig merges with the dryer; or the stand duplicates; or hair passes through the stand.
- P6 [minor · attribute_drift]
  - expect: The wig's colour and the surroundings stay the same.
  - fail: The hair changes colour; or the stand changes; or the background rearranges.

## MECH-0185 · gas_wind · train

**Caption.** A leaf blower is pointed at a pile of dry leaves on a path, and the leaves scatter and tumble away from the nozzle.

**Expectation (hidden).** The leaves move away from the blower in the direction of the blast, some lifting into the air, and settle further along; they do not move toward it.

**Declared violation types.** trajectory_momentum, causeless_motion

**SA**
- S1 [core] A leaf blower is pointed at a pile of dry leaves on a path.
- S2 [core] The leaves scatter.
- S3 [core] They tumble away from the nozzle.
- S4 [minor] The leaves are dry.
- S5 [minor] The blast comes first and the scatter follows.

**PC**
- P1 [core · trajectory_momentum]
  - expect: Leaves move away from the blower in the direction of the blast, some lifting into the air.
  - fail: They move toward the blower; or sideways across the blast; or straight up and hover.
- P2 [core · causeless_motion]
  - expect: Leaves move only while the blast is on them.
  - fail: They scatter with the blower off; or keep tumbling after it is switched off and the air is still; or move before it is aimed.
- P3 [major · gravity_direction]
  - expect: Lifted leaves come down and settle further along.
  - fail: They hang; or rise indefinitely; or float.
- P4 [major · material_response]
  - expect: The leaves flutter and tumble as thin dry things.
  - fail: They move as rigid discs; or as rolling balls; or as one solid sheet.
- P5 [fatal · permanence_count]
  - expect: One blower keeps its number, and the leaves are the pile's.
  - fail: The blower duplicates; or leaves appear from nowhere; or leaves pass through the path.
- P6 [minor · attribute_drift]
  - expect: The blower, the path and the surroundings stay the same.
  - fail: The blower changes colour; or the path rearranges; or the leaves change colour.

## MECH-0186 · gas_wind · train

**Caption.** A flag hanging limp from a pole outside a school lifts and streams out as a strong wind picks up.

**Expectation (hidden).** The flag stretches out downwind and ripples along its length; it points the same way as other things blown by the wind.

**Declared violation types.** causeless_motion, material_response

**SA**
- S1 [core] A flag hangs limp from a pole outside a school.
- S2 [core] The wind picks up.
- S3 [core] The flag lifts and streams out.
- S4 [minor] The wind comes first and the flag responds after.

**PC**
- P1 [core · causeless_motion]
  - expect: The flag lifts as the wind picks up and points the same way as other things blown.
  - fail: It streams while trees and grass are still; or points opposite to other wind signs; or lifts before any sign of wind.
- P2 [core · material_response]
  - expect: It stretches out downwind and ripples along its length.
  - fail: It is rigid like a board; or stays limp while strong wind signs are visible; or stretches longer.
- P3 [major · gravity_direction]
  - expect: It hangs below its clips when limp and lifts along the wind when blown.
  - fail: It rises above the pole top; or floats off; or hangs out sideways with no wind.
- P4 [major · trajectory_momentum]
  - expect: It streams out on the downwind side.
  - fail: It flips between sides randomly; or wraps around the pole and stays; or streams into the wind.
- P5 [fatal · permanence_count]
  - expect: One flag on one pole keeps its number.
  - fail: The flag duplicates; or passes through the pole; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The flag's colours, the pole and the school stay the same.
  - fail: The flag changes colours; or the pole changes; or the school rearranges.

## MECH-0187 · gas_wind · train

**Caption.** A plastic shopping bag lying on an empty parking lot inflates and tumbles away across the lot as the wind rises.

**Expectation (hidden).** The bag moves downwind, rising and dipping with the gusts; it does not travel against the wind or move before the wind picks up.

**Declared violation types.** causeless_motion, trajectory_momentum

**SA**
- S1 [core] A plastic shopping bag lies on an empty parking lot.
- S2 [core] It inflates.
- S3 [core] It tumbles away across the lot.
- S4 [minor] The lot is empty.
- S5 [minor] The bag inflates first and then tumbles.

**PC**
- P1 [core · causeless_motion]
  - expect: The bag moves as the wind picks up and not before.
  - fail: It moves before any sign of wind; or keeps moving steadily after the wind drops; or jumps.
- P2 [core · trajectory_momentum]
  - expect: It moves downwind, rising and dipping with the gusts.
  - fail: It moves against the wind; or in a straight line at constant height; or crosswise to other wind signs.
- P3 [major · gravity_direction]
  - expect: It dips back to the ground between gusts.
  - fail: It rises indefinitely; or hangs; or rolls along without lifting.
- P4 [major · material_response]
  - expect: It fills with air, flaps and crumples.
  - fail: It is rigid; or tears into strips; or stays flat while moving.
- P5 [fatal · permanence_count]
  - expect: One bag keeps its number and passes through nothing.
  - fail: It duplicates; or passes through a kerb; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The bag's colour and the lot stay the same.
  - fail: The bag changes colour; or the lot markings shift; or the surroundings rearrange.

## MECH-0188 · gas_wind · train

**Caption.** A puff of breath blows out the candles on a birthday cake, and thin wisps of smoke rise from the wicks.

**Expectation (hidden).** The flames lean away from the breath and go out during it; the smoke rises upward; the candles do not relight on their own.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] Lit candles stand on a birthday cake.
- S2 [core] A puff of breath is blown at them.
- S3 [core] The candles go out.
- S4 [core] Wisps of smoke rise from the wicks.
- S5 [minor] The puff comes first, then the flames go out, then the smoke.

**PC**
- P1 [core · missing_consequence]
  - expect: The flames lean away from the breath and go out during it.
  - fail: The flames stay upright during the puff; or go out before the puff; or lean toward the breath.
- P2 [core · process_direction]
  - expect: Once out the candles stay out, and the smoke follows the flame.
  - fail: The candles relight on their own; or smoke rises before a flame is out; or a flame comes back from the smoke.
- P3 [major · gravity_direction]
  - expect: The smoke rises upward.
  - fail: It sinks; or hangs; or flows sideways with no draught.
- P4 [major · material_response]
  - expect: The smoke is thin wisps that thin out.
  - fail: It is a solid rope; or a liquid; or a dense blob that holds its shape.
- P5 [fatal · permanence_count]
  - expect: The candles keep their number and the cake stays one cake.
  - fail: A candle vanishes; or a new one appears; or the cake changes into another object.
- P6 [minor · attribute_drift]
  - expect: The cake's frosting and the candles stay the same.
  - fail: The frosting changes colour; or the candles rearrange; or the table changes.

**Note.** The breath is kept as the trigger; the person blowing is not judged.

## MECH-0189 · gas_wind · train

**Caption.** The valve of an inflated air mattress is opened and the mattress pressed down, and it hisses and sags flat.

**Expectation (hidden).** The mattress collapses most where it is pressed and stays flat; it does not reinflate on its own.

**Declared violation types.** shape_identity, process_direction

**SA**
- S1 [core] An inflated air mattress is present.
- S2 [core] Its valve is opened.
- S3 [core] The mattress is pressed down.
- S4 [core] It sags flat.
- S5 [minor] The valve opens first, then the press, then the sag.

**PC**
- P1 [core · process_direction]
  - expect: The mattress deflates and stays flat, and it does not reinflate.
  - fail: It reinflates on its own; or goes flat and puffs back; or is flat before the valve opens.
- P2 [core · shape_identity]
  - expect: It collapses most where it is pressed, sagging as fabric over the remaining air.
  - fail: It stays a rigid block under the press; or shrinks to a tiny size; or splits into two mattresses.
- P3 [major · causeless_motion]
  - expect: The mattress stays put.
  - fail: It slides; or lifts; or jumps.
- P4 [major · gravity_direction]
  - expect: The pressed surface goes down and the fabric lies on the floor.
  - fail: It rises; or floats; or hangs.
- P5 [fatal · permanence_count]
  - expect: One mattress keeps its number.
  - fail: It duplicates; or passes through the floor; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The mattress's colour and the room stay the same.
  - fail: The mattress changes colour; or the room rearranges; or the hands change.

## MECH-0190 · gas_wind · train

**Caption.** A balloon pump is worked up and down with a limp balloon fitted over its nozzle, and the balloon swells until it is round and taut.

**Expectation (hidden).** The balloon grows a little with each stroke and not between strokes; it does not inflate instantly, shrink while the pumping goes on, or slip off the nozzle.

**Declared violation types.** shape_identity, process_direction

**SA**
- S1 [core] A limp balloon is fitted over the nozzle of a balloon pump.
- S2 [core] The pump is worked up and down.
- S3 [core] The balloon swells.
- S4 [core] It becomes round and taut.
- S5 [minor] The balloon is limp at the start.
- S6 [minor] The pumping comes first and the swelling follows.

**PC**
- P1 [core · process_direction]
  - expect: The balloon grows a little with each stroke and not between strokes, and it does not shrink while pumping.
  - fail: It inflates instantly; or shrinks while pumping continues; or grows between strokes with the pump still.
- P2 [core · shape_identity]
  - expect: It stays one balloon on the nozzle and gets rounder.
  - fail: It slips off the nozzle and keeps inflating; or splits into two; or turns into another shape.
- P3 [major · causeless_motion]
  - expect: Growth happens only with pumping.
  - fail: It grows with no hands on the pump; or keeps growing after pumping stops; or deflates and reinflates on its own.
- P4 [major · material_response]
  - expect: The rubber stretches smoothly and thins, and the pump body stays rigid.
  - fail: The balloon stays wrinkled while large; or the pump bends; or the balloon is rigid.
- P5 [fatal · permanence_count]
  - expect: One balloon and one pump keep their number.
  - fail: The balloon duplicates; or the pump vanishes; or the balloon passes through the nozzle.
- P6 [minor · attribute_drift]
  - expect: The balloon's colour and the pump stay the same.
  - fail: The balloon changes colour; or the pump changes; or the background rearranges.

## MECH-0191 · gas_wind · train

**Caption.** A feather is dropped in front of a running box fan and is carried away by the airflow before drifting to the floor.

**Expectation (hidden).** The feather moves away from the fan, tumbling, and lands some distance off rather than falling straight down; it does not rise indefinitely.

**Declared violation types.** trajectory_momentum, gravity_direction

**SA**
- S1 [core] A box fan is running.
- S2 [core] A feather is dropped in front of it.
- S3 [core] The feather is carried away by the airflow.
- S4 [core] It drifts to the floor.
- S5 [minor] The drop comes first, then the carry, then the landing.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The feather moves away from the fan, tumbling, and lands some distance off.
  - fail: It falls straight down in front of the fan; or moves toward the fan; or shoots off fast like a dart.
- P2 [core · gravity_direction]
  - expect: It sinks as it drifts and reaches the floor.
  - fail: It rises indefinitely; or hangs still; or drops like a stone.
- P3 [major · causeless_motion]
  - expect: The feather moves with the airflow only.
  - fail: It changes direction sharply with the fan steady; or moves before it is released; or hangs motionless in the airflow.
- P4 [major · material_response]
  - expect: The feather is light and flutters and spins.
  - fail: It is rigid; or folds like cloth; or splits.
- P5 [fatal · permanence_count]
  - expect: One feather and one fan keep their number.
  - fail: The feather duplicates; or vanishes in the air; or the fan turns into another object.
- P6 [minor · attribute_drift]
  - expect: The feather's colour and the room stay the same.
  - fail: The feather changes colour; or the fan changes; or the room rearranges.

## MECH-0192 · gas_wind · train

**Caption.** A vacuum cleaner nozzle is run over crumbs scattered on a carpet, and the crumbs disappear into the nozzle.

**Expectation (hidden).** Crumbs jump toward the nozzle only when it comes close and vanish into it; the carpet is clean behind the nozzle's path; crumbs do not fly away from it.

**Declared violation types.** missing_consequence, permanence_count, trajectory_momentum

**SA**
- S1 [core] Crumbs are scattered on a carpet.
- S2 [core] A vacuum cleaner nozzle is run over them.
- S3 [core] The crumbs disappear into the nozzle.
- S4 [minor] The nozzle passes first and the crumbs go after.

**PC**
- P1 [core · missing_consequence]
  - expect: Crumbs jump toward the nozzle only when it comes close and vanish into it.
  - fail: Crumbs vanish before the nozzle nears; or the nozzle passes and the crumbs stay; or crumbs vanish elsewhere on the carpet.
- P2 [core · permanence_count]
  - expect: The carpet is clean behind the nozzle's path and crumbs do not reappear.
  - fail: Crumbs reappear behind the nozzle; or new crumbs appear; or the carpet stays covered after the pass.
- P3 [major · trajectory_momentum]
  - expect: Crumbs move toward the nozzle mouth, not away.
  - fail: They fly away from the nozzle; or sideways; or straight up.
- P4 [major · causeless_motion]
  - expect: Crumbs stay still until the nozzle nears.
  - fail: Crumbs move about before the nozzle comes; or the carpet ripples; or crumbs hop with the nozzle far away.
- P5 [fatal · shape_identity]
  - expect: One nozzle keeps its number and does not pass through the carpet.
  - fail: It passes through the carpet; or duplicates; or the carpet tears open.
- P6 [minor · attribute_drift]
  - expect: The carpet's pattern and the nozzle stay the same.
  - fail: The carpet changes pattern; or the nozzle changes; or the room rearranges.

## MECH-0193 · biomechanics · train

**Caption.** A woman walks along a city sidewalk carrying a handbag, one foot after the other.

**Expectation (hidden).** One foot is on the ground at all times, the arms swing opposite to the legs, and the limbs bend only at hips, knees, elbows and shoulders.

**Declared violation types.** shape_identity, solidity

**SA**
- S1 [core] A woman walks along a city sidewalk.
- S2 [core] She carries a handbag.
- S3 [core] Her feet move one after the other.
- S4 [minor] The setting is a city sidewalk.

**PC**
- P1 [core · shape_identity]
  - expect: Her legs alternate, her arms swing opposite to her legs, and her limbs bend only at hips, knees, elbows and shoulders.
  - fail: Both legs move forward together; or a limb bends mid-bone; or her legs cross through each other.
- P2 [core · solidity]
  - expect: One foot is on the ground at all times and her feet land on the pavement, not in it.
  - fail: Both feet are off the ground at once during the walk; or a foot sinks into the pavement; or she slides forward with her feet still.
- P3 [major · gravity_direction]
  - expect: She stays upright with her weight over her feet.
  - fail: She leans far over and does not fall; or she floats; or her body rises and drops far more than a step would.
- P4 [major · permanence_count]
  - expect: The handbag stays in her hand or on her shoulder and swings with her.
  - fail: The bag vanishes; or floats beside her; or passes through her body.
- P5 [fatal · shape_identity]
  - expect: Her limbs keep their number and stay attached, and she passes through nothing.
  - fail: A limb detaches, vanishes or a third arm appears; or she merges with a passer-by; or her head passes through a sign.
- P6 [minor · attribute_drift]
  - expect: Her clothing, the bag and the street stay the same.
  - fail: Her clothing changes colour; or the bag changes; or the buildings rearrange.

**Note.** Biomechanics scene: the body is the physics. Gait, posture, style and skill are not judged; only that limbs stay attached, bend at joints, keep ground contact and pass through nothing.

## MECH-0194 · biomechanics · train

**Caption.** A man jogs across a park lawn from one side to the other.

**Expectation (hidden).** Both feet leave the ground briefly between strides, the arms swing in rhythm, and the body bobs slightly with each step; legs alternate.

**Declared violation types.** shape_identity, gravity_direction

**SA**
- S1 [core] A man jogs across a park lawn.
- S2 [core] He goes from one side to the other.
- S3 [minor] The pace is a jog rather than a walk.
- S4 [minor] The setting is a park lawn.

**PC**
- P1 [core · shape_identity]
  - expect: His legs alternate, his arms swing in rhythm, and his limbs bend at the joints.
  - fail: Both legs swing together; or a leg bends mid-bone; or his legs pass through each other.
- P2 [core · gravity_direction]
  - expect: Both feet leave the ground briefly between strides and come back, and the body bobs with each step.
  - fail: He glides with his feet never lifting; or he floats up and stays; or he sinks into the grass.
- P3 [major · solidity]
  - expect: His feet land on the grass, not in it.
  - fail: His feet sink to the ankle in the turf; or he passes through a bench; or the grass passes through his feet.
- P4 [major · trajectory_momentum]
  - expect: He travels steadily across the lawn.
  - fail: He jumps position between frames; or moves backward while running forward; or stops dead mid-stride hanging in the air.
- P5 [fatal · shape_identity]
  - expect: His limbs keep their number and stay attached.
  - fail: A limb detaches or vanishes; or a second figure appears from him; or he merges with a tree.
- P6 [minor · attribute_drift]
  - expect: His clothing and the park stay the same.
  - fail: His clothing changes colour; or the park rearranges; or the lawn changes.

**Note.** Biomechanics scene: the body is the physics. Gait, posture, style and skill are not judged; only that limbs stay attached, bend at joints, keep ground contact and pass through nothing.

## MECH-0195 · biomechanics · train

**Caption.** A boy climbs a flight of stairs two at a time and reaches the top.

**Expectation (hidden).** Each knee lifts high and the foot lands on top of a step, not inside it; the body rises with each push.

**Declared violation types.** shape_identity, solidity

**SA**
- S1 [core] A boy climbs a flight of stairs.
- S2 [core] He takes the steps two at a time.
- S3 [core] He reaches the top.
- S4 [minor] The climb comes first and the top is reached after.

**PC**
- P1 [core · solidity]
  - expect: Each foot lands on top of a step, not inside it.
  - fail: A foot sinks into a step; or a foot passes through a riser; or he slides up the stairs with his feet planted.
- P2 [core · shape_identity]
  - expect: Each knee lifts high and the legs alternate, and the limbs bend only at the joints.
  - fail: Both legs lift together; or a leg bends mid-shin; or a leg stretches to reach a step.
- P3 [major · gravity_direction]
  - expect: His body rises with each push, his weight over the supporting foot.
  - fail: He rises without a push; or floats up the stairs; or rises and sinks between steps.
- P4 [major · permanence_count]
  - expect: The staircase keeps its number of steps.
  - fail: Steps appear or vanish; or the staircase changes length; or the top moves away as he climbs.
- P5 [fatal · shape_identity]
  - expect: His limbs keep their number and stay attached.
  - fail: A limb detaches or vanishes; or a second boy appears; or he merges with the handrail.
- P6 [minor · attribute_drift]
  - expect: His clothing and the stairwell stay the same.
  - fail: His clothing changes colour; or the stairwell rearranges; or the steps change material.

**Note.** Biomechanics scene: the body is the physics. Gait, posture, style and skill are not judged; only that limbs stay attached, bend at joints, keep ground contact and pass through nothing.

## MECH-0196 · biomechanics · train

**Caption.** An elderly man lowers himself into an armchair and sits down.

**Expectation (hidden).** He bends at hips and knees and leans forward slightly as he sinks; his body does not fold anywhere other than at the joints.

**Declared violation types.** shape_identity, gravity_direction

**SA**
- S1 [core] A man stands in front of an armchair.
- S2 [core] He lowers himself into it.
- S3 [core] He sits down.
- S4 [minor] The lowering comes first and the sitting follows.

**PC**
- P1 [core · shape_identity]
  - expect: He bends at the hips and knees, and his body folds only at the joints.
  - fail: He folds mid-torso like cloth; or his legs bend mid-shin; or an arm detaches.
- P2 [core · gravity_direction]
  - expect: He sinks down under his own weight in a controlled way and settles onto the seat.
  - fail: He floats down slower than a feather; or he rises; or he sinks through the seat.
- P3 [major · solidity]
  - expect: He sits on the cushion, which compresses under him.
  - fail: He passes into the chair; or the chair passes through him; or the cushion stays rigid.
- P4 [major · trajectory_momentum]
  - expect: He leans forward slightly as he sinks and settles back.
  - fail: He falls backward over the chair; or tips sideways and hangs; or the chair moves toward him.
- P5 [fatal · shape_identity]
  - expect: His limbs keep their number and stay attached.
  - fail: A limb detaches or vanishes; or a second figure appears; or he merges with the chair.
- P6 [minor · attribute_drift]
  - expect: His clothing, the chair and the room stay the same.
  - fail: His clothing changes colour; or the chair changes; or the room rearranges.

**Note.** Biomechanics scene: the body is the physics. Gait, posture, style and skill are not judged; only that limbs stay attached, bend at joints, keep ground contact and pass through nothing.

## MECH-0197 · biomechanics · train

**Caption.** A dog runs across a yard to a ball lying on the grass and picks it up in its mouth.

**Expectation (hidden).** Its four legs move in a galloping rhythm and the body stretches and bunches with each bound; it slows and lowers its head to take the ball; it keeps four legs and one tail throughout.

**Declared violation types.** shape_identity, permanence_count

**SA**
- S1 [core] A dog runs across a yard.
- S2 [core] A ball lies on the grass.
- S3 [core] The dog picks up the ball in its mouth.
- S4 [minor] The run comes first and the pick-up follows.

**PC**
- P1 [core · shape_identity]
  - expect: Its four legs move in a galloping rhythm, the body stretches and bunches with each bound, and the legs bend at the joints.
  - fail: The legs move together like a rocking horse; or a leg bends mid-bone; or the legs pass through each other.
- P2 [core · permanence_count]
  - expect: It keeps four legs and one tail, and there is one ball.
  - fail: A leg or the tail vanishes or a fifth leg appears; or the ball duplicates; or the ball vanishes before the dog reaches it.
- P3 [major · missing_consequence]
  - expect: It slows and lowers its head to take the ball, and the ball leaves the grass in its mouth.
  - fail: The ball rises to the mouth by itself; or the dog runs past and the ball is in its mouth anyway; or the mouth closes and the ball stays on the grass.
- P4 [major · solidity]
  - expect: Its paws land on the grass and the ball is held in the mouth, not passing through it.
  - fail: Paws sink into the ground; or the ball passes through the jaw; or the dog passes through a fence.
- P5 [fatal · shape_identity]
  - expect: One dog keeps its shape and stays one dog.
  - fail: The dog splits into two; or merges with the ball; or turns into another animal.
- P6 [minor · attribute_drift]
  - expect: The dog's coat, the ball and the yard stay the same.
  - fail: The coat changes pattern; or the ball changes colour; or the yard rearranges.

**Note.** The dog is self-driven: its speed, path and how neatly it picks up the ball are not judged.

## MECH-0198 · biomechanics · train

**Caption.** A horse gallops across an open field from one end to the other.

**Expectation (hidden).** The legs move in a galloping sequence with moments when all four hooves are off the ground, the mane and tail stream back, and the legs bend only at their joints.

**Declared violation types.** shape_identity, gravity_direction

**SA**
- S1 [core] A horse gallops across an open field.
- S2 [core] It goes from one end to the other.
- S3 [minor] The gait is a gallop.

**PC**
- P1 [core · shape_identity]
  - expect: The legs move in a galloping sequence and bend at the joints, and the mane and tail stream back.
  - fail: The legs move in pairs like a rocking horse; or a leg bends mid-bone; or the legs pass through each other.
- P2 [core · gravity_direction]
  - expect: There are moments when all four hooves are off the ground and then they come back down, the body rising and falling with the strides.
  - fail: It glides with hooves never lifting; or floats up and stays; or sinks into the ground.
- P3 [major · solidity]
  - expect: The hooves land on the turf.
  - fail: They sink deep into the turf; or pass through a fence; or the turf passes through the hooves.
- P4 [major · trajectory_momentum]
  - expect: It travels steadily across the field.
  - fail: It jumps position between frames; or runs backward; or freezes mid-stride in the air.
- P5 [fatal · shape_identity]
  - expect: One horse keeps its legs and shape.
  - fail: A leg detaches or vanishes; or a second horse appears from it; or it turns into another animal.
- P6 [minor · attribute_drift]
  - expect: The horse's coat and the field stay the same.
  - fail: The coat changes colour; or the field rearranges; or the fence changes.

**Note.** The horse is self-driven: its speed and path are not judged.

## MECH-0199 · biomechanics · train

**Caption.** A cat crouches on a kitchen floor, jumps up onto the counter, and lands on it.

**Expectation (hidden).** The cat pushes off with its hind legs, arcs upward, and lands front paws first; it does not float up or land before it has jumped.

**Declared violation types.** trajectory_momentum, shape_identity

**SA**
- S1 [core] A cat crouches on a kitchen floor.
- S2 [core] It jumps up.
- S3 [core] It lands on the counter.
- S4 [minor] The crouch comes first, then the jump, then the landing.

**PC**
- P1 [core · trajectory_momentum]
  - expect: It pushes off with its hind legs, arcs upward, and lands front paws first.
  - fail: It floats up; or lands before it has jumped; or rises straight up and hangs.
- P2 [core · shape_identity]
  - expect: Its legs fold and extend at the joints and the body stretches in the air.
  - fail: A leg detaches; or the body stretches like rubber; or the legs bend mid-bone.
- P3 [major · gravity_direction]
  - expect: After the peak it comes down onto the counter and stays.
  - fail: It hovers; or rises through the ceiling; or bounces high off the counter.
- P4 [major · solidity]
  - expect: Its paws land on the counter top.
  - fail: It passes through the counter; or sinks into it; or the counter passes through the cat.
- P5 [fatal · shape_identity]
  - expect: One cat keeps its shape and stays one cat.
  - fail: It splits; or merges with the counter; or turns into another animal.
- P6 [minor · attribute_drift]
  - expect: The cat's markings and the kitchen stay the same.
  - fail: The markings change; or the kitchen rearranges; or the counter changes.

**Note.** The cat is self-driven: the timing of its jump is its own. Only the arc and the body's integrity are judged.

## MECH-0200 · biomechanics · train

**Caption.** A woman bends down, picks up a heavy box from the floor, and straightens up holding it.

**Expectation (hidden).** She bends her knees and back to reach the box, lifts with visible effort, and leans back slightly to balance the weight once standing.

**Declared violation types.** shape_identity, gravity_direction

**SA**
- S1 [core] A woman bends down toward a box on the floor.
- S2 [core] She picks up the box.
- S3 [core] She straightens up holding it.
- S4 [minor] The box is heavy, and the effort shows.
- S5 [minor] The bend comes first, then the lift, then the straightening.

**PC**
- P1 [core · shape_identity]
  - expect: She bends her knees and back at the joints to reach and straightens at them.
  - fail: She folds mid-torso; or her arms stretch to reach; or her legs bend mid-shin.
- P2 [core · gravity_direction]
  - expect: The box rises only as she lifts it, held in her hands, and she leans back slightly to balance once standing.
  - fail: The box floats up ahead of her hands; or rises with her hands not under it; or she leans far forward with a heavy box and does not fall.
- P3 [major · solidity]
  - expect: Her hands grip the box and do not pass through it.
  - fail: Her hands pass through the box; or the box passes into her body; or the box hangs in the air.
- P4 [major · material_response]
  - expect: The box stays rigid and her arms strain.
  - fail: The box folds like cloth; or it stretches; or her arms bend mid-forearm.
- P5 [fatal · shape_identity]
  - expect: Her limbs keep their number and stay attached.
  - fail: A limb detaches or vanishes; or a second figure appears; or she merges with the box.
- P6 [minor · attribute_drift]
  - expect: Her clothing, the box and the room stay the same.
  - fail: Her clothing changes colour; or the box changes; or the room rearranges.

**Note.** Biomechanics scene: the body is the physics. Gait, posture, style and skill are not judged; only that limbs stay attached, bend at joints, keep ground contact and pass through nothing.

## MECH-0201 · biomechanics · train

**Caption.** A boy catches a ball thrown to him with both hands and holds on to it.

**Expectation (hidden).** His arms reach toward the ball, his hands close around it, and his arms give slightly as it arrives; the ball does not pass through his hands.

**Declared violation types.** shape_identity, solidity

**SA**
- S1 [core] A ball is thrown to a boy.
- S2 [core] He catches it with both hands.
- S3 [core] He holds on to it.
- S4 [minor] Both hands are used.
- S5 [minor] The throw comes first and the catch follows.

**PC**
- P1 [core · solidity]
  - expect: The ball stops in his hands and does not pass through them.
  - fail: It passes through his hands; or passes into his chest; or his hands close on nothing while the ball goes on.
- P2 [core · shape_identity]
  - expect: His arms reach, his hands close, his arms give slightly as it arrives, and the joints bend.
  - fail: His arms stretch like rubber; or his hands detach; or his arms bend mid-forearm.
- P3 [major · trajectory_momentum]
  - expect: The ball travels in an arc to him and stops at the catch.
  - fail: It changes direction in mid-air; or stops in the air before his hands; or keeps going after the catch.
- P4 [major · gravity_direction]
  - expect: He stays on his feet and the ball's arc dips.
  - fail: He floats; or the ball curves upward; or the ball hangs.
- P5 [fatal · shape_identity]
  - expect: His limbs keep their number and stay attached, and one ball stays one ball.
  - fail: A limb detaches; or the ball duplicates; or he merges with the ball.
- P6 [minor · attribute_drift]
  - expect: His clothing and the ball stay the same.
  - fail: His clothing changes colour; or the ball changes; or the background rearranges.

**Note.** Biomechanics scene: the body is the physics. Gait, posture, style and skill are not judged; only that limbs stay attached, bend at joints, keep ground contact and pass through nothing.

## MECH-0202 · biomechanics · train

**Caption.** A swimmer does front crawl across a pool and reaches the far wall.

**Expectation (hidden).** The arms come over one at a time and pull through the water, the legs kick, and the head turns to breathe; each arm stays attached and bends only at elbow and shoulder.

**Declared violation types.** shape_identity, permanence_count

**SA**
- S1 [core] A swimmer swims front crawl in a pool.
- S2 [core] They cross the pool.
- S3 [core] They reach the far wall.
- S4 [minor] The stroke is front crawl, with the arms coming over one at a time.

**PC**
- P1 [core · shape_identity]
  - expect: The arms come over one at a time and pull through, the legs kick, the head turns to breathe, and the arms bend at elbow and shoulder.
  - fail: Both arms come over together; or an arm bends mid-forearm; or the legs pass through each other.
- P2 [core · permanence_count]
  - expect: Each arm stays attached and the swimmer stays one person.
  - fail: An arm detaches or vanishes; or a second swimmer appears in the lane; or a limb duplicates.
- P3 [major · missing_consequence]
  - expect: Each stroke splashes and leaves a wake.
  - fail: The arms move through the water leaving the surface glassy; or splashes appear where no arm is; or the wake runs ahead of the swimmer.
- P4 [major · gravity_direction]
  - expect: The body stays at the surface, mostly under the water.
  - fail: It floats above the water; or sinks and swims along the bottom; or rises out of the pool.
- P5 [fatal · shape_identity]
  - expect: The swimmer keeps their shape and passes through nothing.
  - fail: They pass through the lane rope; or merge with the wall; or turn into another figure.
- P6 [minor · attribute_drift]
  - expect: The swimsuit and the pool stay the same.
  - fail: The swimsuit changes colour; or the lane markings shift; or the pool changes.

**Note.** Biomechanics scene: the body is the physics. Gait, posture, style and skill are not judged; only that limbs stay attached, bend at joints, keep ground contact and pass through nothing.

## MECH-0203 · biomechanics · train

**Caption.** A girl rides a kick scooter along a path, pushing off the ground with one foot and gliding between pushes.

**Expectation (hidden).** One foot stays on the board while the other kicks; the scooter speeds up on each kick and coasts between them.

**Declared violation types.** shape_identity, causeless_motion

**SA**
- S1 [core] A girl rides a kick scooter along a path.
- S2 [core] She pushes off the ground with one foot.
- S3 [core] The scooter glides between pushes.
- S4 [minor] One foot stays on the board.
- S5 [minor] Each push comes first and the glide follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The scooter speeds up on each kick and coasts, slowing gently, between them.
  - fail: It speeds up between kicks with both feet on the board; or stops dead between kicks; or moves from rest with no kick.
- P2 [core · shape_identity]
  - expect: One foot stays on the board while the other kicks, and the legs bend at the joints.
  - fail: Both feet leave the board while it moves on; or a leg bends mid-shin; or a leg detaches.
- P3 [major · solidity]
  - expect: The kicking foot touches the path and the wheels stay on the ground.
  - fail: The foot passes through the path; or the scooter floats; or the foot kicks air well above the ground and she speeds up.
- P4 [major · gravity_direction]
  - expect: She stays upright over the board.
  - fail: She leans far over and does not fall; or she floats; or she sinks.
- P5 [fatal · shape_identity]
  - expect: Her limbs keep their number and stay attached, and one scooter stays one scooter.
  - fail: A limb detaches; or the scooter duplicates; or she merges with the scooter.
- P6 [minor · attribute_drift]
  - expect: Her clothing, the scooter and the path stay the same.
  - fail: Her clothing changes colour; or the scooter changes; or the path rearranges.

**Note.** Biomechanics scene: the body is the physics. Gait, posture, style and skill are not judged; only that limbs stay attached, bend at joints, keep ground contact and pass through nothing.

## MECH-0204 · biomechanics · train

**Caption.** A man slips on a wet floor in a supermarket aisle and falls down.

**Expectation (hidden).** His foot shoots forward, his arms fly up, and he goes down to the floor; his body stays in one piece and bends only at the joints.

**Declared violation types.** gravity_direction, shape_identity

**SA**
- S1 [core] A man walks along a supermarket aisle.
- S2 [core] He slips on a wet patch of floor.
- S3 [core] He falls to the floor.
- S4 [minor] The floor is visibly wet where he slips.
- S5 [minor] The slip comes first and the fall follows.

**PC**
- P1 [core · gravity_direction]
  - expect: Once his balance goes he comes down to the floor and stays.
  - fail: He hangs mid-fall; or rises; or bounces back to his feet.
- P2 [core · shape_identity]
  - expect: His foot shoots forward, his arms fly up, and his body bends only at the joints.
  - fail: His body folds mid-torso; or a limb detaches; or his legs pass through each other.
- P3 [major · causeless_motion]
  - expect: The slip starts where his foot meets the wet patch.
  - fail: He slips on dry floor away from the patch; or falls before reaching the patch; or his foot slides with no contact.
- P4 [major · solidity]
  - expect: He lands on the floor, not in it.
  - fail: He passes into the floor; or passes through a shelf; or a shelf passes through him.
- P5 [fatal · shape_identity]
  - expect: His limbs keep their number and stay attached.
  - fail: A limb detaches or vanishes; or a second figure appears; or he merges with the shelving.
- P6 [minor · attribute_drift]
  - expect: His clothing and the aisle stay the same.
  - fail: His clothing changes colour; or the shelves rearrange; or the wet patch moves.

**Note.** Biomechanics scene: the body is the physics. Gait, posture, style and skill are not judged; only that limbs stay attached, bend at joints, keep ground contact and pass through nothing.

## MECH-0205 · biomechanics · train

**Caption.** A couple dances a slow waltz around a living room, holding each other.

**Expectation (hidden).** They step in time with their feet on the floor; their bodies stay separate and do not pass through one another or merge.

**Declared violation types.** shape_identity, solidity

**SA**
- S1 [core] Two people dance together in a living room.
- S2 [core] They hold each other.
- S3 [core] They move around the room.
- S4 [minor] The pace is slow.

**PC**
- P1 [core · solidity]
  - expect: Their bodies stay separate and do not pass through one another.
  - fail: They pass through each other; or merge; or one's arm passes through the other's body.
- P2 [core · shape_identity]
  - expect: They step in time with their feet on the floor, their limbs bend at the joints, and each keeps their own limbs.
  - fail: A limb detaches; or a limb bends mid-bone; or the pair share a limb.
- P3 [major · gravity_direction]
  - expect: They stay upright with their weight over their feet.
  - fail: They float; or lean impossibly without falling; or sink into the floor.
- P4 [major · trajectory_momentum]
  - expect: They move together as a pair, turning.
  - fail: One jumps position between frames; or they move in opposite directions while holding on; or they slide with their feet planted.
- P5 [fatal · permanence_count]
  - expect: Two people stay two.
  - fail: A third appears; or one vanishes; or they merge into one.
- P6 [minor · attribute_drift]
  - expect: Their clothing and the room stay the same.
  - fail: Clothing changes colour; or the furniture rearranges; or the room changes.

**Note.** Biomechanics scene: the body is the physics. Gait, posture, style and skill are not judged; only that limbs stay attached, bend at joints, keep ground contact and pass through nothing.

## MECH-0206 · biomechanics · train

**Caption.** Two hands struggle to twist the lid off a tight jar and finally get it open, lid in hand.

**Expectation (hidden).** The hands grip jar and lid and the forearms twist in opposite directions; the lid turns and comes off only after the twist, not before.

**Declared violation types.** shape_identity, missing_consequence

**SA**
- S1 [core] Two hands grip a jar and its lid.
- S2 [core] They twist against each other.
- S3 [core] The lid comes off.
- S4 [core] The lid ends up in a hand.
- S5 [minor] The effort is visible before the lid gives.
- S6 [minor] The twist comes first and the lid comes off after.

**PC**
- P1 [core · missing_consequence]
  - expect: The lid turns and comes off only after the twist, not before.
  - fail: The lid comes off before any twist; or the hands twist with the lid fixed for the whole clip and then it is in hand; or the lid lifts off with no turn.
- P2 [core · shape_identity]
  - expect: The hands grip, the forearms twist in opposite directions, and the fingers stay attached.
  - fail: Fingers pass through the lid; or a hand detaches; or the hands merge with the jar.
- P3 [major · causeless_motion]
  - expect: The jar stays still in one hand and the lid moves only with the other.
  - fail: The lid spins on its own; or the jar turns while the hands are still; or the lid floats off.
- P4 [major · material_response]
  - expect: The jar and the lid stay rigid.
  - fail: The jar bends; or the lid stretches; or the jar shatters from the twist.
- P5 [fatal · permanence_count]
  - expect: One jar and one lid keep their number.
  - fail: The lid duplicates; or the jar vanishes; or the lid turns into another object.
- P6 [minor · attribute_drift]
  - expect: The jar's label and the background stay the same.
  - fail: The label changes; or the hands change; or the background rearranges.

**Note.** The hands are the physics here: grip and twist. The person behind them is not judged.

## MECH-0207 · biomechanics · train

**Caption.** A pigeon flies in and lands on a park railing.

**Expectation (hidden).** It flares its wings to slow, extends its legs, grips the railing, and folds its wings; it does not stop dead in mid-air or land before reaching the rail.

**Declared violation types.** shape_identity, trajectory_momentum

**SA**
- S1 [core] A pigeon flies in toward a railing.
- S2 [core] It lands on the railing.
- S3 [minor] The setting is a park.
- S4 [minor] The flight comes first and the landing follows.

**PC**
- P1 [core · trajectory_momentum]
  - expect: It flares its wings to slow, extends its legs, and grips the rail; it does not stop dead in mid-air.
  - fail: It stops dead in the air and drops; or lands before reaching the rail; or passes through the rail.
- P2 [core · shape_identity]
  - expect: Its wings flap and fold at the joints, its legs extend, and it keeps two wings and two legs.
  - fail: A wing detaches; or the wings bend like rubber along the feathers; or a third leg appears.
- P3 [major · gravity_direction]
  - expect: Once landed it stays on the rail.
  - fail: It hovers above the rail without flapping; or rises after landing without flapping; or sinks through the rail.
- P4 [major · solidity]
  - expect: Its feet grip the top of the rail.
  - fail: Its feet pass through the rail; or the rail passes through the bird; or it sits inside the rail.
- P5 [fatal · shape_identity]
  - expect: One pigeon keeps its shape and stays one bird.
  - fail: It splits into two; or merges with the rail; or turns into another bird.
- P6 [minor · attribute_drift]
  - expect: The pigeon's plumage and the railing stay the same.
  - fail: The plumage changes colour; or the railing changes; or the park rearranges.

**Note.** The pigeon is self-driven: its approach and timing are its own. Only the body's integrity and the landing are judged.

## MECH-0208 · biomechanics · train

**Caption.** A child does a forward roll on a gym mat and comes up sitting.

**Expectation (hidden).** She tucks her head and rolls over her back along the mat; her body stays whole and does not sink into the mat.

**Declared violation types.** shape_identity, solidity

**SA**
- S1 [core] A child is on a gym mat.
- S2 [core] She does a forward roll.
- S3 [core] She comes up sitting.
- S4 [minor] The roll comes first and the sitting follows.

**PC**
- P1 [core · shape_identity]
  - expect: She tucks her head and rolls over her back, her body bends at the joints, and her limbs stay attached.
  - fail: A limb detaches; or her body folds mid-torso like cloth; or her head passes through her body.
- P2 [core · solidity]
  - expect: She rolls along the surface of the mat, not into it.
  - fail: She sinks into the mat; or passes through the floor; or the mat passes through her.
- P3 [major · trajectory_momentum]
  - expect: The roll carries her forward along the mat and she ends further along.
  - fail: She rolls backward; or ends where she started after a forward roll; or jumps up to sitting with no roll between.
- P4 [major · gravity_direction]
  - expect: She comes down onto the mat through the roll and sits.
  - fail: She hovers; or rises; or hangs upside down.
- P5 [fatal · shape_identity]
  - expect: Her limbs keep their number and she stays one child.
  - fail: A second figure appears; or she merges with the mat; or a limb vanishes.
- P6 [minor · attribute_drift]
  - expect: Her clothing and the mat stay the same.
  - fail: Her clothing changes colour; or the mat changes; or the gym rearranges.

**Note.** Biomechanics scene: the body is the physics. Gait, posture, style and skill are not judged; only that limbs stay attached, bend at joints, keep ground contact and pass through nothing.

## MECH-0209 · biomechanics · train

**Caption.** A man pushes a broken-down car along a flat empty street, and the car slowly starts to roll.

**Expectation (hidden).** He leans forward with straight arms against the car and drives with his legs; the car begins to move only after he pushes and only while he pushes.

**Declared violation types.** shape_identity, causeless_motion

**SA**
- S1 [core] A man pushes a car along a flat street.
- S2 [core] The car starts to roll.
- S3 [minor] The street is flat and empty.
- S4 [minor] The car starts slowly.
- S5 [minor] The push comes first and the roll follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The car begins to move only after he pushes and only while he pushes, and it gathers speed slowly.
  - fail: The car moves before he touches it; or rolls with his hands off it; or surges away fast from a push.
- P2 [core · shape_identity]
  - expect: He leans forward with his arms against the car and drives with his legs, and his limbs bend at the joints.
  - fail: His arms bend mid-forearm; or a limb detaches; or his hands pass through the car.
- P3 [major · solidity]
  - expect: His hands are on the car body and his feet on the road.
  - fail: His hands pass through the car; or he passes into the car; or his feet sink into the road.
- P4 [major · trajectory_momentum]
  - expect: The car rolls in the direction he pushes, in a straight line.
  - fail: It rolls toward him; or turns sharply on its own; or rolls backward.
- P5 [fatal · shape_identity]
  - expect: His limbs keep their number, and one car stays one car.
  - fail: A limb detaches; or the car duplicates; or he merges with the car.
- P6 [minor · attribute_drift]
  - expect: His clothing, the car and the street stay the same.
  - fail: His clothing changes colour; or the car changes colour; or the street rearranges.

**Note.** Biomechanics scene: the body is the physics. Gait, posture, style and skill are not judged; only that limbs stay attached, bend at joints, keep ground contact and pass through nothing.

## MECH-0210 · soft_material · train

**Caption.** The laces of a sneaker are tied into a bow and the loops pulled tight.

**Expectation (hidden).** The laces cross, loop, and pull through each other only where the fingers guide them; the knot tightens as the loops are pulled and stays tied; the laces never pass through themselves or change length.

**Declared violation types.** shape_identity, solidity, permanence_count

**SA**
- S1 [core] The laces of a sneaker are handled.
- S2 [core] They are tied into a bow.
- S3 [core] The loops are pulled tight.
- S4 [minor] The tying comes first and the tightening follows.

**PC**
- P1 [core · solidity]
  - expect: The laces cross, loop and pull through each other only where the fingers guide them, and they never pass through themselves.
  - fail: A lace passes through another lace or through itself; or a lace passes through the shoe; or the knot forms with the laces never crossing.
- P2 [core · shape_identity]
  - expect: The knot tightens as the loops are pulled and stays tied, and the laces keep their length.
  - fail: The knot loosens as it is pulled; or the laces grow or shrink; or the bow unties itself.
- P3 [major · permanence_count]
  - expect: There are two lace ends and two loops throughout.
  - fail: A third end appears; or a loop vanishes; or the laces multiply.
- P4 [major · material_response]
  - expect: The laces are flexible cord that bends and droops.
  - fail: They are rigid rods; or stretch like elastic; or melt together.
- P5 [fatal · shape_identity]
  - expect: The shoe and the hands keep their shape.
  - fail: Fingers pass through the shoe; or a finger detaches; or the shoe duplicates.
- P6 [minor · attribute_drift]
  - expect: The laces' colour and the shoe stay the same.
  - fail: The laces change colour; or the shoe changes; or the background rearranges.

**Note.** The hands are kept as the minimal trigger; the person is not judged.

## MECH-0211 · soft_material · train

**Caption.** A bath towel is folded in half and then in half again.

**Expectation (hidden).** The towel bends along the fold line and the halves lie flat on each other; the towel gets smaller and thicker with each fold; it does not stiffen, stretch, or fold on its own.

**Declared violation types.** shape_identity, material_response

**SA**
- S1 [core] A bath towel is laid out.
- S2 [core] It is folded in half.
- S3 [core] It is folded in half again.
- S4 [minor] The first fold comes before the second.

**PC**
- P1 [core · shape_identity]
  - expect: The towel gets smaller and thicker with each fold, and the halves lie flat on each other.
  - fail: The towel stays the same size after folding; or it grows; or a fold produces more towel.
- P2 [core · material_response]
  - expect: The towel bends along the fold line as soft cloth and does not stiffen or stretch.
  - fail: It is rigid like cardboard; or it stretches; or it snaps.
- P3 [major · causeless_motion]
  - expect: It folds only as the hands move it.
  - fail: It folds on its own; or unfolds by itself; or slides.
- P4 [major · solidity]
  - expect: The layers lie on each other, not through each other.
  - fail: A layer passes through another; or the hands pass through the towel; or the towel passes through the surface beneath.
- P5 [fatal · permanence_count]
  - expect: One towel keeps its number.
  - fail: It duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The towel's colour and the surface stay the same.
  - fail: The towel changes colour; or the surface changes; or the background rearranges.

**Note.** The hands are kept as the minimal trigger; the person is not judged.

## MECH-0212 · soft_material · train

**Caption.** A sheet of paper is crumpled into a tight ball and dropped on the desk.

**Expectation (hidden).** The sheet wrinkles and folds in on itself as it is crushed; the ball keeps its crumpled shape and creases after release and does not unfold flat again.

**Declared violation types.** shape_identity, process_direction

**SA**
- S1 [core] A sheet of paper is held.
- S2 [core] It is crumpled into a ball.
- S3 [core] The ball is dropped on the desk.
- S4 [minor] The ball is tight rather than loose.
- S5 [minor] The crumpling comes first and the drop follows.

**PC**
- P1 [core · process_direction]
  - expect: The ball keeps its crumpled shape and creases after release and does not unfold flat.
  - fail: It unfolds flat on its own; or the creases vanish; or it re-crumples by itself.
- P2 [core · shape_identity]
  - expect: The sheet wrinkles and folds in on itself as it is crushed, getting smaller.
  - fail: It stays flat under crushing; or it grows; or it tears into pieces.
- P3 [major · gravity_direction]
  - expect: Dropped, it falls to the desk and stays.
  - fail: It floats; or rises; or hangs.
- P4 [major · material_response]
  - expect: The paper creases sharply and is light.
  - fail: It is rubbery; or melts; or is a rigid plate.
- P5 [fatal · permanence_count]
  - expect: One sheet becomes one ball.
  - fail: The ball duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The paper's colour and the desk stay the same.
  - fail: The paper changes colour; or the desk changes; or the background rearranges.

**Note.** The hands are kept as the minimal trigger; the person is not judged.

## MECH-0213 · soft_material · train

**Caption.** A paper map is unfolded on the hood of a car and smoothed flat.

**Expectation (hidden).** The map opens along its existing creases and lies flat only where pressed, springing up slightly at the folds; it does not open by itself or change size.

**Declared violation types.** shape_identity, material_response

**SA**
- S1 [core] A folded paper map is on the hood of a car.
- S2 [core] It is unfolded.
- S3 [core] It is smoothed flat.
- S4 [minor] The unfolding comes first and the smoothing follows.

**PC**
- P1 [core · shape_identity]
  - expect: The map opens along its existing creases and gets larger as it opens without changing its total size.
  - fail: It opens with no creases; or grows beyond its folded panels; or shrinks.
- P2 [core · material_response]
  - expect: It lies flat only where pressed and springs up slightly at the folds.
  - fail: It is a rigid plate; or stretches; or snaps flat by itself.
- P3 [major · causeless_motion]
  - expect: It opens only as the hands move it.
  - fail: It opens by itself; or refolds itself; or slides off the hood.
- P4 [major · solidity]
  - expect: The panels lie on the hood, not through it.
  - fail: The map passes through the hood; or the hands pass through the map; or a panel passes through another.
- P5 [fatal · permanence_count]
  - expect: One map keeps its number.
  - fail: It duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The map's printing and the car stay the same.
  - fail: The printing changes; or the car changes colour; or the background rearranges.

**Note.** The hands are kept as the minimal trigger; the person is not judged.

## MECH-0214 · soft_material · train

**Caption.** A yoga mat is rolled up from one end into a tight cylinder and stood against the wall.

**Expectation (hidden).** The roll grows thicker as more mat winds onto it; the layers sit on top of each other and do not pass through one another; the mat does not roll itself.

**Declared violation types.** shape_identity, solidity

**SA**
- S1 [core] A yoga mat lies flat.
- S2 [core] It is rolled up from one end.
- S3 [core] It forms a cylinder.
- S4 [core] It is stood against the wall.
- S5 [minor] The roll is tight.
- S6 [minor] The rolling comes first and the standing up follows.

**PC**
- P1 [core · solidity]
  - expect: The layers sit on top of each other and do not pass through one another.
  - fail: A layer passes through another; or the mat passes through the floor; or the hands pass through the mat.
- P2 [core · shape_identity]
  - expect: The roll grows thicker as more mat winds on, and the flat part shrinks.
  - fail: The roll stays the same thickness; or the flat part does not shrink; or the mat grows.
- P3 [major · causeless_motion]
  - expect: The mat rolls only as the hands roll it.
  - fail: It rolls itself; or unrolls itself; or slides.
- P4 [major · gravity_direction]
  - expect: Stood against the wall, it leans on it and stays.
  - fail: It floats; or falls through the wall; or stands balanced away from the wall with nothing holding it.
- P5 [fatal · permanence_count]
  - expect: One mat keeps its number.
  - fail: It duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The mat's colour and the room stay the same.
  - fail: The mat changes colour; or the wall changes; or the room rearranges.

**Note.** The hands are kept as the minimal trigger; the person is not judged.

## MECH-0215 · soft_material · train

**Caption.** A long garden hose is coiled into loops on the lawn.

**Expectation (hidden).** Each loop lies on top of the last, the hose bends smoothly without kinking, and the length of hose on the ground shrinks as the coil grows; the hose does not pass through itself.

**Declared violation types.** shape_identity, solidity, permanence_count

**SA**
- S1 [core] A garden hose lies on a lawn.
- S2 [core] It is coiled into loops.
- S3 [minor] The loops lie on the lawn.
- S4 [minor] The coiling proceeds loop by loop.

**PC**
- P1 [core · solidity]
  - expect: Each loop lies on top of the last, and the hose does not pass through itself.
  - fail: It passes through itself; or passes through the lawn; or loops run into one another.
- P2 [core · shape_identity]
  - expect: The length of hose still on the ground shrinks as the coil grows, and the hose bends smoothly without kinking.
  - fail: The loose hose does not shrink; or the hose stretches; or it kinks like wire.
- P3 [major · permanence_count]
  - expect: One continuous hose with two ends.
  - fail: The hose splits; or the ends multiply; or a loop vanishes.
- P4 [major · causeless_motion]
  - expect: It coils only as the hands move it.
  - fail: It coils itself; or uncoils; or slides.
- P5 [fatal · shape_identity]
  - expect: The hose stays one hose and the hands keep their shape.
  - fail: The hose merges with itself; or the hands pass through it; or it turns into another object.
- P6 [minor · attribute_drift]
  - expect: The hose's colour and the lawn stay the same.
  - fail: The hose changes colour; or the lawn changes; or the garden rearranges.

**Note.** The hands are kept as the minimal trigger; the person is not judged.

## MECH-0216 · soft_material · train

**Caption.** A tablecloth is shaken out and let settle over a dining table, and the edges hang down over the sides.

**Expectation (hidden).** The cloth billows, then falls and drapes over the table top with the overhang hanging straight down under gravity; it does not float, stay rigid, or hang upward.

**Declared violation types.** gravity_direction, material_response

**SA**
- S1 [core] A tablecloth is shaken out over a dining table.
- S2 [core] It settles onto the table.
- S3 [core] The edges hang down over the sides.
- S4 [minor] The shake comes first and the settling follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The cloth billows, then falls and drapes, with the overhang hanging straight down.
  - fail: It floats; or the edges hang upward; or it stays billowed in the air.
- P2 [core · material_response]
  - expect: The soft cloth billows, folds and drapes.
  - fail: It is a rigid sheet; or it stretches; or it tears.
- P3 [major · process_direction]
  - expect: It settles and stays.
  - fail: It rises again; or re-billows with no shake; or slides off.
- P4 [major · solidity]
  - expect: It lies on the table top, not through it.
  - fail: It passes through the table; or the table passes through it; or it sinks into the top.
- P5 [fatal · permanence_count]
  - expect: One cloth keeps its number.
  - fail: It duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The cloth's pattern and the table stay the same.
  - fail: The pattern changes; or the table changes; or the room rearranges.

**Note.** The hands are kept as the minimal trigger; the person is not judged.

## MECH-0217 · soft_material · train

**Caption.** The drawstring of a cloth bag is pulled, and the bag's opening gathers shut.

**Expectation (hidden).** The fabric around the opening bunches into gathers as the string is pulled through it; the opening closes only as the string tightens.

**Declared violation types.** shape_identity, missing_consequence

**SA**
- S1 [core] A cloth bag has a drawstring.
- S2 [core] The drawstring is pulled.
- S3 [core] The opening gathers shut.
- S4 [minor] The pull comes first and the closing follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The opening closes only as the string tightens.
  - fail: It closes before the pull; or the string is pulled and the opening stays open; or it closes with no string.
- P2 [core · shape_identity]
  - expect: The fabric bunches into gathers as the string passes through it, and the bag keeps its size.
  - fail: The fabric shrinks smoothly with no gathers; or the bag grows; or the opening seals like a zip.
- P3 [major · solidity]
  - expect: The string runs through its channel, not through the fabric.
  - fail: The string passes through the cloth; or the hands pass through the bag; or the string passes through itself.
- P4 [major · material_response]
  - expect: The string is flexible and the gathers are soft.
  - fail: The string is rigid; or the fabric is rigid; or the string stretches.
- P5 [fatal · permanence_count]
  - expect: One bag keeps its number.
  - fail: It duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The bag's colour and the background stay the same.
  - fail: The bag changes colour; or the string changes; or the background rearranges.

**Note.** The hands are kept as the minimal trigger; the person is not judged.

## MECH-0218 · soft_material · train

**Caption.** A wet shirt is hung on a clothesline by its shoulders, and the shirt hangs down and drips.

**Expectation (hidden).** The shirt drapes straight down from the pegs, its wet fabric clinging and heavy; drips fall from the lowest edge; the shirt does not stand out stiffly or float.

**Declared violation types.** gravity_direction, material_response

**SA**
- S1 [core] A wet shirt is hung on a clothesline by its shoulders.
- S2 [core] The shirt hangs down.
- S3 [core] It drips.
- S4 [minor] The shirt is wet.
- S5 [minor] The hanging comes first and the dripping follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The shirt drapes straight down from the pegs, and drips fall from its lowest edge.
  - fail: It stands out stiffly; or floats; or drips rise.
- P2 [core · material_response]
  - expect: The wet fabric clings and hangs heavy.
  - fail: It is rigid; or billows like dry cloth in still air; or stretches.
- P3 [major · process_direction]
  - expect: The dripping continues and slows.
  - fail: Drips stop and then restart; or the shirt gets wetter; or it drips before it is hung.
- P4 [major · solidity]
  - expect: The pegs hold the shoulders on the line.
  - fail: The shirt passes through the line; or the pegs pass through the shirt; or the shirt hangs with nothing holding it.
- P5 [fatal · permanence_count]
  - expect: One shirt keeps its number.
  - fail: It duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The shirt's colour and the yard stay the same.
  - fail: The shirt changes colour; or the line changes; or the yard rearranges.

## MECH-0219 · soft_material · train

**Caption.** A long scarf is wrapped twice around a wooden post and its end tucked in.

**Expectation (hidden).** The scarf bends around the post in layers that lie on top of each other, and the free end gets shorter as it is wrapped; the scarf does not pass through itself or the post.

**Declared violation types.** shape_identity, solidity, permanence_count

**SA**
- S1 [core] A long scarf is wrapped around a wooden post.
- S2 [core] It goes around twice.
- S3 [core] Its end is tucked in.
- S4 [minor] The wrapping comes first and the tuck follows.

**PC**
- P1 [core · solidity]
  - expect: The scarf bends around the post in layers that lie on top of each other, and it does not pass through itself or the post.
  - fail: It passes through the post; or passes through itself; or the layers run into one another.
- P2 [core · shape_identity]
  - expect: The free end gets shorter as it is wrapped, and the scarf keeps its length.
  - fail: The free end does not shorten; or the scarf grows; or it shrinks.
- P3 [major · permanence_count]
  - expect: One scarf with two ends.
  - fail: The ends multiply; or the scarf splits; or a wrap vanishes.
- P4 [major · material_response]
  - expect: The soft cloth drapes and bends.
  - fail: It is rigid; or stretches; or snaps.
- P5 [fatal · shape_identity]
  - expect: The scarf stays one scarf and the post keeps its shape.
  - fail: The scarf merges with the post; or the post duplicates; or the hands pass through the scarf.
- P6 [minor · attribute_drift]
  - expect: The scarf's pattern and the post stay the same.
  - fail: The pattern changes; or the post changes; or the background rearranges.

**Note.** The hands are kept as the minimal trigger; the person is not judged.

## MECH-0220 · soft_material · train

**Caption.** A knot is tied in a thick rope and both ends pulled hard so the knot tightens.

**Expectation (hidden).** The rope loops through itself only where the hands pass it, the knot shrinks and hardens as the ends are pulled, and it holds; the rope does not stretch like elastic or merge with itself.

**Declared violation types.** shape_identity, solidity, material_response

**SA**
- S1 [core] A knot is tied in a thick rope.
- S2 [core] Both ends are pulled hard.
- S3 [core] The knot tightens.
- S4 [minor] The tying comes first and the pulling follows.

**PC**
- P1 [core · solidity]
  - expect: The rope loops through itself only where the hands pass it, and it does not merge with or pass through itself.
  - fail: It passes through itself; or merges with itself; or the knot forms with no crossing.
- P2 [core · material_response]
  - expect: The knot shrinks and hardens as the ends are pulled, and the rope does not stretch like elastic.
  - fail: It stretches; or the knot loosens under the pull; or the rope snaps.
- P3 [major · shape_identity]
  - expect: The rope keeps its length and thickness.
  - fail: It grows; or thins; or changes into another material.
- P4 [major · missing_consequence]
  - expect: The pull tightens the knot and the knot holds when released.
  - fail: The pull produces no tightening; or the knot unties on release; or it tightens with no pull.
- P5 [fatal · permanence_count]
  - expect: One rope keeps its number and its two ends.
  - fail: The rope splits; or the ends multiply; or the knot vanishes.
- P6 [minor · attribute_drift]
  - expect: The rope's colour and the background stay the same.
  - fail: The rope changes colour; or the hands change; or the background rearranges.

**Note.** The hands are kept as the minimal trigger; the person is not judged.

## MECH-0221 · soft_material · train

**Caption.** A rolled-up rug is given a push and unrolls across a wooden floor, and the rug lies flat.

**Expectation (hidden).** The roll gets thinner as it travels and the unrolled part lies flat behind it; the roll slows and stops when the rug runs out; the rug does not roll back up.

**Declared violation types.** shape_identity, trajectory_momentum

**SA**
- S1 [core] A rolled-up rug is on a wooden floor.
- S2 [core] It is given a push.
- S3 [core] It unrolls across the floor.
- S4 [core] The rug lies flat.
- S5 [minor] The push comes first, then the unrolling, then the rug lies flat.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The roll travels in the direction of the push, slows, and stops when the rug runs out.
  - fail: It rolls back toward the push; or keeps rolling past the rug's end; or stops dead mid-rug with nothing in its way.
- P2 [core · shape_identity]
  - expect: The roll gets thinner as it travels and the unrolled part lies flat behind it.
  - fail: The roll stays thick; or the rug rolls back up; or the unrolled part curls up.
- P3 [major · causeless_motion]
  - expect: It moves only after the push.
  - fail: It unrolls before the push; or re-rolls; or slides sideways.
- P4 [major · solidity]
  - expect: It lies on the floor, not through it.
  - fail: It passes through the floor; or the layers run into one another; or it floats.
- P5 [fatal · permanence_count]
  - expect: One rug keeps its number.
  - fail: It duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The rug's pattern and the floor stay the same.
  - fail: The pattern changes; or the floorboards shift; or the room rearranges.

## MECH-0222 · soft_material · train

**Caption.** A letter is folded into thirds and slid into an envelope.

**Expectation (hidden).** The paper creases at the folds and becomes a smaller rectangle that fits into the envelope; the letter goes into the opening, not through the envelope's face.

**Declared violation types.** shape_identity, solidity

**SA**
- S1 [core] A letter is held.
- S2 [core] It is folded into thirds.
- S3 [core] It is slid into an envelope.
- S4 [minor] The folding comes first and the sliding in follows.

**PC**
- P1 [core · shape_identity]
  - expect: The paper creases at the folds and becomes a smaller rectangle that fits the envelope.
  - fail: It stays full size; or grows; or folds into a different shape.
- P2 [core · solidity]
  - expect: The letter goes into the opening, not through the envelope's face.
  - fail: It passes through the face; or the hands pass through the envelope; or the envelope passes through the letter.
- P3 [major · material_response]
  - expect: The paper creases sharply and lies flat.
  - fail: It is rubbery; or a rigid plate; or it tears.
- P4 [major · causeless_motion]
  - expect: It moves only as the hands move it.
  - fail: It folds itself; or slides in by itself; or jumps.
- P5 [fatal · permanence_count]
  - expect: One letter and one envelope keep their number.
  - fail: The letter duplicates; or the envelope vanishes; or the letter turns into another object.
- P6 [minor · attribute_drift]
  - expect: The paper and the envelope stay the same.
  - fail: The paper changes colour; or the envelope changes; or the background rearranges.

**Note.** The hands are kept as the minimal trigger; the person is not judged.

## MECH-0223 · soft_material · train

**Caption.** A blanket is pulled off a bed by one corner and dragged across the floor.

**Expectation (hidden).** The blanket slides off the bed and trails on the floor in soft folds, following the pull and bunching where it catches; it does not stay stiff or move ahead of the pull.

**Declared violation types.** material_response, shape_identity

**SA**
- S1 [core] A blanket lies on a bed.
- S2 [core] It is pulled by one corner.
- S3 [core] It slides off the bed.
- S4 [core] It is dragged across the floor.
- S5 [minor] The pull comes first, then the slide off, then the drag.

**PC**
- P1 [core · material_response]
  - expect: The blanket slides off and trails in soft folds, bunching where it catches.
  - fail: It is a rigid sheet; or it stretches; or it tears.
- P2 [core · shape_identity]
  - expect: It follows the pull and does not move ahead of it, and it keeps its size.
  - fail: It moves ahead of the pull; or grows; or shrinks.
- P3 [major · causeless_motion]
  - expect: It moves only while it is pulled.
  - fail: It slides off by itself; or moves after the pull stops; or jumps.
- P4 [major · gravity_direction]
  - expect: It falls off the bed edge to the floor and lies on it.
  - fail: It floats; or hangs in the air; or rises.
- P5 [fatal · permanence_count]
  - expect: One blanket keeps its number.
  - fail: It duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The blanket's pattern and the room stay the same.
  - fail: The pattern changes; or the bed changes; or the room rearranges.

**Note.** The hands are kept as the minimal trigger; the person is not judged.

## MECH-0224 · soft_material · train

**Caption.** A sheet of wrapping paper is folded around a shoebox, creasing at the corners.

**Expectation (hidden).** The paper wraps around the box following its edges, creases where pressed, and the box's shape shows through; the paper does not stretch, shrink, or pass through the box.

**Declared violation types.** shape_identity, solidity

**SA**
- S1 [core] A shoebox sits on a sheet of wrapping paper.
- S2 [core] The paper is folded around the box.
- S3 [core] It creases at the corners.
- S4 [minor] The folding comes first and the creases follow.

**PC**
- P1 [core · shape_identity]
  - expect: The paper wraps following the box's edges and the box's shape shows through, and the paper does not stretch or shrink.
  - fail: The paper stretches; or shrinks; or the box changes shape.
- P2 [core · solidity]
  - expect: The paper lies on the box, not through it.
  - fail: It passes through the box; or the box passes through the paper; or the hands pass through.
- P3 [major · material_response]
  - expect: The paper creases sharply where it is pressed.
  - fail: It is rubbery; or a rigid plate; or it tears everywhere.
- P4 [major · causeless_motion]
  - expect: It moves only as the hands move it.
  - fail: It wraps itself; or unwraps; or slides.
- P5 [fatal · permanence_count]
  - expect: One box and one sheet keep their number.
  - fail: The box duplicates; or the paper vanishes; or the box turns into another object.
- P6 [minor · attribute_drift]
  - expect: The paper's pattern and the box stay the same.
  - fail: The pattern changes; or the box changes; or the background rearranges.

**Note.** The hands are kept as the minimal trigger; the person is not judged.

## MECH-0225 · occlusion_containment · train

**Caption.** A ball rolls across a living-room floor, disappears behind a sofa, and comes out the other side.

**Expectation (hidden).** The same ball reappears at the far side, at about the time and speed its motion behind the sofa implies; it does not emerge changed, doubled, or from the wrong side.

**Declared violation types.** permanence_count, trajectory_momentum

**SA**
- S1 [core] A ball rolls across a living-room floor.
- S2 [core] It disappears behind a sofa.
- S3 [core] It comes out the other side.
- S4 [minor] The roll in comes first and the emergence follows.

**PC**
- P1 [core · permanence_count]
  - expect: The same ball reappears at the far side, not changed, doubled, or from the wrong side.
  - fail: A different ball emerges; or two balls come out; or it emerges from the side it entered; or nothing comes out and a ball appears elsewhere.
- P2 [core · trajectory_momentum]
  - expect: It reappears at about the time and speed its motion implies, continuing the same line.
  - fail: It emerges instantly; or long after it should; or emerges going the other way.
- P3 [major · solidity]
  - expect: The ball is hidden by the sofa and is not visible through it.
  - fail: It shows through the sofa; or passes through the sofa's front; or the sofa passes through the ball.
- P4 [major · causeless_motion]
  - expect: It rolls straight and slows gently.
  - fail: It curves on the open floor; or speeds up; or stops and restarts.
- P5 [fatal · shape_identity]
  - expect: The ball and the sofa keep their shape.
  - fail: The ball turns into another object; or the sofa changes shape; or the ball merges with the sofa.
- P6 [minor · attribute_drift]
  - expect: The ball's colour and the room stay the same.
  - fail: The ball changes colour; or the sofa changes; or the room rearranges.

## MECH-0226 · occlusion_containment · train

**Caption.** The lid of a small wooden box is closed over a set of keys lying inside, then opened again.

**Expectation (hidden).** The keys are hidden while the lid is shut and the same keys are there when it opens; they do not vanish, change, or appear outside the box while it is closed.

**Declared violation types.** permanence_count, shape_identity

**SA**
- S1 [core] A set of keys lies inside a small wooden box.
- S2 [core] The lid is closed over them.
- S3 [core] The lid is opened again.
- S4 [minor] The closing comes first and the opening follows.

**PC**
- P1 [core · permanence_count]
  - expect: The same keys are there when the lid opens, and they do not vanish, change, or appear outside while it is closed.
  - fail: The keys are gone when the lid opens; or different keys are there; or keys appear outside while the box is shut.
- P2 [core · shape_identity]
  - expect: The keys keep their number and shape.
  - fail: The keys multiply; or a key changes shape; or the keys merge.
- P3 [major · solidity]
  - expect: The keys are hidden while the lid is shut and do not show through it.
  - fail: They show through the lid; or the lid passes through the keys; or the keys pass through the box.
- P4 [major · causeless_motion]
  - expect: The box and the keys stay put, and the lid moves only by the hand.
  - fail: The lid opens by itself; or the keys jump; or the box slides.
- P5 [fatal · permanence_count]
  - expect: One box keeps its number.
  - fail: The box duplicates; or vanishes; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The box's wood and the background stay the same.
  - fail: The box changes colour; or the keys change colour; or the background rearranges.

## MECH-0227 · occlusion_containment · train

**Caption.** An upturned cup is placed over a coin on a table, slid to the side, and lifted to reveal the coin.

**Expectation (hidden).** The coin is hidden under the cup and is found where the cup was slid to, having moved with it; the coin does not show through the cup or stay behind at the first spot.

**Declared violation types.** permanence_count, solidity

**SA**
- S1 [core] A coin lies on a table.
- S2 [core] An upturned cup is placed over it.
- S3 [core] The cup is slid to the side.
- S4 [core] The cup is lifted and the coin is revealed.
- S5 [minor] The cover comes first, then the slide, then the lift.

**PC**
- P1 [core · permanence_count]
  - expect: The coin is found where the cup was slid to, having moved with it.
  - fail: The coin is left behind at the first spot while the cup slides away; or the coin vanishes; or two coins are revealed.
- P2 [core · solidity]
  - expect: The coin does not show through the cup, and the cup does not pass through the table.
  - fail: The coin shows through the cup; or the cup sinks into the table; or the coin passes through the cup.
- P3 [major · causeless_motion]
  - expect: The coin and the cup move only by the hand.
  - fail: The coin slides by itself; or the cup moves alone; or the coin jumps.
- P4 [major · gravity_direction]
  - expect: The coin stays flat on the table.
  - fail: The coin floats; or stands on edge and stays; or rises up into the cup.
- P5 [fatal · permanence_count]
  - expect: One cup and one coin keep their number.
  - fail: The cup duplicates; or the coin turns into another object; or the cup vanishes.
- P6 [minor · attribute_drift]
  - expect: The cup, the coin and the table stay the same.
  - fail: The cup changes colour; or the coin changes; or the table rearranges.

## MECH-0228 · occlusion_containment · train

**Caption.** A dog trots along a street and passes behind a wide pillar, disappearing and then emerging on the far side.

**Expectation (hidden).** The dog is hidden for a moment consistent with its pace and reappears at the same size and gait; its body does not show through the pillar or change while hidden.

**Declared violation types.** permanence_count, trajectory_momentum

**SA**
- S1 [core] A dog trots along a street.
- S2 [core] It passes behind a wide pillar.
- S3 [core] It emerges on the far side.
- S4 [minor] The disappearance comes first and the emergence follows.

**PC**
- P1 [core · permanence_count]
  - expect: The same dog reappears at the same size and gait.
  - fail: A different dog emerges; or two dogs; or nothing emerges and the dog appears elsewhere.
- P2 [core · trajectory_momentum]
  - expect: It is hidden for a moment consistent with its pace and emerges continuing the same way.
  - fail: It emerges instantly; or after far too long; or emerges going back.
- P3 [major · solidity]
  - expect: Its body does not show through the pillar.
  - fail: It shows through; or passes through the pillar face; or the pillar passes through the dog.
- P4 [major · shape_identity]
  - expect: It keeps its legs and tail across the occlusion.
  - fail: The leg count changes; or the tail vanishes; or its size changes.
- P5 [fatal · shape_identity]
  - expect: One dog stays one dog.
  - fail: It splits into two; or merges with the pillar; or turns into another animal.
- P6 [minor · attribute_drift]
  - expect: The dog's coat and the street stay the same.
  - fail: The coat changes pattern; or the pillar changes; or the street rearranges.

**Note.** The dog is self-driven: its pace is its own. Only permanence and the timing of the reappearance are judged.

## MECH-0229 · occlusion_containment · train

**Caption.** A cat climbs into a paper grocery bag on the floor, and the bag rustles and shifts as the cat moves inside it.

**Expectation (hidden).** The bag bulges and moves where the cat pushes from inside; the cat's body does not show through the paper and the cat does not appear elsewhere while inside.

**Declared violation types.** permanence_count, solidity, shape_identity

**SA**
- S1 [core] A paper grocery bag stands on the floor.
- S2 [core] A cat climbs into it.
- S3 [core] The bag shifts and moves as the cat moves inside.
- S4 [minor] The climb in comes first and the movement of the bag follows.

**PC**
- P1 [core · permanence_count]
  - expect: The cat does not appear elsewhere while it is inside.
  - fail: The cat appears outside while the bag still moves; or a second cat appears; or the cat vanishes and the bag goes still.
- P2 [core · solidity]
  - expect: The bag bulges where the cat pushes from inside, and the cat does not show through the paper.
  - fail: The cat shows through the paper; or passes through the bag wall; or the bag passes through the cat.
- P3 [major · shape_identity]
  - expect: The bag keeps its size, bulging and crumpling.
  - fail: The bag grows to fit; or shrinks; or changes into another bag.
- P4 [major · causeless_motion]
  - expect: The bag moves only where the cat pushes.
  - fail: The bag moves with no cat inside; or slides across the room; or jumps.
- P5 [fatal · shape_identity]
  - expect: One cat stays one cat.
  - fail: It splits; or merges with the bag; or turns into another animal.
- P6 [minor · attribute_drift]
  - expect: The bag's printing and the room stay the same.
  - fail: The printing changes; or the floor changes; or the room rearranges.

**Note.** The cat is self-driven: its movements inside are its own. Only containment and the bag's response are judged.

## MECH-0230 · occlusion_containment · train

**Caption.** Three apples are dropped one by one into an empty cloth bag, and the bag sags and bulges.

**Expectation (hidden).** The bag hangs lower and bulges more with each apple; the bulges match the apples' size and sit at the bottom; the apples do not fall through the cloth.

**Declared violation types.** permanence_count, gravity_direction, material_response

**SA**
- S1 [core] An empty cloth bag is held open.
- S2 [core] Apples are dropped into it one by one.
- S3 [core] The bag sags and bulges.
- S4 [minor] Three apples are dropped in.
- S5 [minor] Each drop comes before the sag it causes.

**PC**
- P1 [core · permanence_count]
  - expect: The bag hangs lower and bulges more with each apple, and the apples stay inside.
  - fail: The bag is unchanged after apples go in; or an apple falls through the cloth; or an apple appears outside.
- P2 [core · gravity_direction]
  - expect: The apples fall into the bag and sit at the bottom, and the bag hangs down.
  - fail: Apples float in the bag; or the bag rises; or the bag bulges at the top.
- P3 [major · material_response]
  - expect: The bulges match the apples' size and the cloth drapes.
  - fail: The bag is rigid; or the bulges are the wrong size; or the cloth stretches like elastic.
- P4 [major · process_direction]
  - expect: The sag only increases as apples are added.
  - fail: The bag lifts as apples go in; or the bulges disappear; or it sags before any apple.
- P5 [fatal · shape_identity]
  - expect: One bag and the apples keep their number.
  - fail: The bag duplicates; or an apple vanishes in mid-air; or an apple turns into another object.
- P6 [minor · attribute_drift]
  - expect: The bag's colour and the background stay the same.
  - fail: The bag changes colour; or the apples change colour; or the background rearranges.

## MECH-0231 · occlusion_containment · train

**Caption.** A glass of water is poured into an opaque metal jug, and the water disappears from view inside the jug.

**Expectation (hidden).** The level in the glass falls as it pours; the water is unseen once inside the jug and does not show through or leak from its sides.

**Declared violation types.** permanence_count, material_response

**SA**
- S1 [core] A glass of water and an opaque metal jug are present.
- S2 [core] The water is poured into the jug.
- S3 [core] The water is out of sight inside the jug.
- S4 [minor] The pour comes first and the water disappears as it enters.

**PC**
- P1 [core · permanence_count]
  - expect: The level in the glass falls as it pours, and the water is unseen once inside and does not leak from the sides.
  - fail: The glass level is unchanged; or water leaks from the jug's sides; or water reappears in the glass.
- P2 [core · material_response]
  - expect: The stream falls as a liquid, and the jug stays opaque and rigid.
  - fail: The stream is a rigid rod; or the jug becomes transparent; or the jug bulges.
- P3 [major · gravity_direction]
  - expect: The stream falls into the jug's opening.
  - fail: It curves; or misses and rises; or hangs.
- P4 [major · solidity]
  - expect: Water does not show through the metal.
  - fail: It shows through; or passes through the wall; or the jug passes through the glass.
- P5 [fatal · permanence_count]
  - expect: One glass and one jug keep their number.
  - fail: The glass duplicates; or the jug vanishes; or water appears elsewhere.
- P6 [minor · attribute_drift]
  - expect: The jug, the glass and the background stay the same.
  - fail: The jug changes colour; or the glass changes; or the background rearranges.

## MECH-0232 · occlusion_containment · train

**Caption.** A toy car is pushed into one end of a cardboard tunnel and rolls out the other end.

**Expectation (hidden).** The car exits after a delay matching its speed and the tunnel's length, moving in the same direction; the same car comes out and nothing exits before it enters.

**Declared violation types.** permanence_count, trajectory_momentum

**SA**
- S1 [core] A toy car is pushed into one end of a cardboard tunnel.
- S2 [core] It rolls out the other end.
- S3 [minor] The tunnel is cardboard.
- S4 [minor] The entry comes first and the exit follows.

**PC**
- P1 [core · permanence_count]
  - expect: The same car comes out, and nothing exits before it enters.
  - fail: A different car exits; or two cars; or a car exits before one has entered.
- P2 [core · trajectory_momentum]
  - expect: It exits after a delay matching its speed and the tunnel's length, moving in the same direction.
  - fail: It exits instantly; or after far too long; or exits going back.
- P3 [major · solidity]
  - expect: It is hidden inside and does not show through the cardboard.
  - fail: It shows through; or passes through the tunnel wall; or exits through the roof.
- P4 [major · causeless_motion]
  - expect: It rolls straight and slows gently.
  - fail: It speeds up inside; or stops and restarts; or curves.
- P5 [fatal · shape_identity]
  - expect: One car and one tunnel keep their shape.
  - fail: The car turns into another object; or the tunnel changes shape; or the car merges with the tunnel.
- P6 [minor · attribute_drift]
  - expect: The car's colour and the tunnel stay the same.
  - fail: The car changes colour; or the tunnel changes; or the background rearranges.

## MECH-0233 · occlusion_containment · train

**Caption.** A coat lies on a table; an arm slides into one sleeve and the hand emerges from the cuff.

**Expectation (hidden).** The sleeve bulges and moves as the arm passes through; the hand appears at the cuff only after the arm has travelled the sleeve's length; the arm does not show through the fabric.

**Declared violation types.** permanence_count, solidity, shape_identity

**SA**
- S1 [core] A coat lies on a table.
- S2 [core] An arm slides into one sleeve.
- S3 [core] The hand emerges from the cuff.
- S4 [minor] The arm enters first and the hand emerges after.

**PC**
- P1 [core · permanence_count]
  - expect: The hand appears at the cuff only after the arm has travelled the sleeve's length, and it is the same hand.
  - fail: The hand appears before the arm is in; or appears elsewhere; or two hands appear.
- P2 [core · solidity]
  - expect: The sleeve bulges as the arm passes, and the arm does not show through the fabric.
  - fail: The arm shows through; or passes through the sleeve wall; or the sleeve passes through the arm.
- P3 [major · shape_identity]
  - expect: The arm and hand keep their shape and the sleeve keeps its length.
  - fail: The arm stretches; or the sleeve grows; or the hand changes.
- P4 [major · material_response]
  - expect: The fabric bulges and shifts softly.
  - fail: It is rigid; or stretches like elastic; or tears.
- P5 [fatal · shape_identity]
  - expect: One arm and one coat keep their number.
  - fail: The arm detaches; or a second coat appears; or the arm merges with the coat.
- P6 [minor · attribute_drift]
  - expect: The coat's colour and the table stay the same.
  - fail: The coat changes colour; or the table changes; or the background rearranges.

**Note.** The arm is the physics here: it is what travels the sleeve. The person is not judged.

## MECH-0234 · occlusion_containment · train

**Caption.** A large dog stands behind a floor-length curtain, and the curtain bulges where it stands with its paws showing beneath the hem.

**Expectation (hidden).** The bulge matches the dog's body and moves when it moves; only its paws are visible below; it does not show through the fabric or appear elsewhere.

**Declared violation types.** permanence_count, solidity

**SA**
- S1 [core] A floor-length curtain hangs.
- S2 [core] It bulges where a dog stands behind it.
- S3 [core] The dog's paws show beneath the hem.
- S4 [minor] The dog is large.

**PC**
- P1 [core · solidity]
  - expect: The bulge matches the dog's body, and the dog does not show through the fabric.
  - fail: The dog shows through; or passes through the curtain; or the curtain passes through the dog.
- P2 [core · permanence_count]
  - expect: The bulge moves when the dog moves, the paws stay beneath the hem, and the dog does not appear elsewhere.
  - fail: The bulge stays while the paws walk away; or the dog appears beside the curtain while the bulge remains; or the paws vanish with the bulge present.
- P3 [major · gravity_direction]
  - expect: The curtain hangs down with its hem at the floor.
  - fail: It floats; or the hem rises; or it hangs sideways.
- P4 [major · material_response]
  - expect: The cloth drapes over the dog.
  - fail: It is rigid; or stretches; or tears.
- P5 [fatal · shape_identity]
  - expect: One dog and one curtain keep their number.
  - fail: Two sets of paws appear; or the curtain duplicates; or the dog turns into another animal.
- P6 [minor · attribute_drift]
  - expect: The curtain's colour and the room stay the same.
  - fail: The curtain changes colour; or the floor changes; or the room rearranges.

**Note.** The dog is self-driven: its movements are its own. Only occlusion and the curtain's response are judged.

## MECH-0235 · occlusion_containment · train

**Caption.** A dog walks into its doghouse and a moment later pokes its head back out of the doorway.

**Expectation (hidden).** The dog is out of sight while inside; its head comes out through the doorway only, not through the walls or roof; it is the same dog.

**Declared violation types.** permanence_count, solidity

**SA**
- S1 [core] A dog walks into its doghouse.
- S2 [core] A moment later it pokes its head out of the doorway.
- S3 [minor] The dog is out of sight between going in and looking out.
- S4 [minor] The entry comes first and the head comes out after.

**PC**
- P1 [core · permanence_count]
  - expect: It is the same dog, and it is out of sight while inside.
  - fail: A different dog looks out; or two dogs; or the dog appears outside while it is inside.
- P2 [core · solidity]
  - expect: The head comes out through the doorway only, not through the walls or the roof.
  - fail: The head comes through a wall; or the body through the roof; or the house passes through the dog.
- P3 [major · shape_identity]
  - expect: The dog keeps its shape.
  - fail: The head is detached; or its size changes; or it turns into another animal.
- P4 [major · causeless_motion]
  - expect: The doghouse stays put.
  - fail: It slides; or lifts; or shakes with no dog inside.
- P5 [fatal · shape_identity]
  - expect: One dog and one doghouse keep their number.
  - fail: The dog splits; or the doghouse duplicates; or the dog merges with the house.
- P6 [minor · attribute_drift]
  - expect: The dog's coat and the doghouse stay the same.
  - fail: The coat changes pattern; or the doghouse changes colour; or the yard rearranges.

**Note.** The dog is self-driven: when it looks out is its own. Only permanence and the doorway are judged.

## MECH-0236 · occlusion_containment · train

**Caption.** A large hardcover book is pushed into a shoebox that is too small for it, and the book will not go in.

**Expectation (hidden).** The book stops against the box's edges or bends the box outward; neither the book nor the box shrinks, and the book does not pass through the box's sides.

**Declared violation types.** solidity, shape_identity

**SA**
- S1 [core] A large hardcover book and a smaller shoebox are present.
- S2 [core] The book is pushed toward the box's opening.
- S3 [core] The book does not go in.
- S4 [minor] The box is too small for the book.

**PC**
- P1 [core · solidity]
  - expect: The book stops against the box's edges or bends the box outward, and it does not pass through the sides.
  - fail: It passes through the sides; or slides in with the box unchanged; or the box passes through the book.
- P2 [core · shape_identity]
  - expect: Neither the book nor the box shrinks.
  - fail: The book shrinks; or the box grows; or the book folds.
- P3 [major · material_response]
  - expect: The cardboard bows or dents, and the book stays rigid.
  - fail: The book bends like rubber; or the box shatters; or the box stretches.
- P4 [major · causeless_motion]
  - expect: They move only by the hand.
  - fail: The book jumps in; or the box slides away; or the book floats.
- P5 [fatal · permanence_count]
  - expect: One book and one box keep their number.
  - fail: The book duplicates; or the box vanishes; or the book turns into another object.
- P6 [minor · attribute_drift]
  - expect: The book's cover and the box stay the same.
  - fail: The cover changes; or the box changes colour; or the background rearranges.

**Note.** The hands are kept as the minimal trigger; the person is not judged.

## MECH-0237 · occlusion_containment · train

**Caption.** A bucket with a tennis ball inside is tipped over, and the ball rolls out onto the floor.

**Expectation (hidden).** The ball is hidden inside the upright bucket and comes out only when the rim tilts low enough; it is the same ball and rolls away from the opening.

**Declared violation types.** permanence_count, gravity_direction

**SA**
- S1 [core] A bucket stands upright with a tennis ball inside.
- S2 [core] The bucket is tipped over.
- S3 [core] The ball rolls out onto the floor.
- S4 [minor] The tip comes first and the roll out follows.

**PC**
- P1 [core · permanence_count]
  - expect: It is the same ball, hidden while the bucket is upright, and it comes out only through the opening.
  - fail: A different ball comes out; or two balls; or the ball passes through the bucket's side.
- P2 [core · gravity_direction]
  - expect: The ball comes out only when the rim tilts low enough and rolls down and away from the opening.
  - fail: It comes out while the bucket is upright; or rolls uphill back in; or floats.
- P3 [major · solidity]
  - expect: The ball is not visible through the bucket.
  - fail: It shows through; or the bucket passes through the ball; or the ball passes through the floor.
- P4 [major · causeless_motion]
  - expect: It rolls straight and slows.
  - fail: It curves; or speeds up; or stops and restarts.
- P5 [fatal · shape_identity]
  - expect: One bucket and one ball keep their shape.
  - fail: The bucket changes shape; or the ball turns into another object; or the ball merges with the bucket.
- P6 [minor · attribute_drift]
  - expect: The bucket's colour and the floor stay the same.
  - fail: The bucket changes colour; or the ball changes; or the floor rearranges.

## MECH-0238 · occlusion_containment · train

**Caption.** A blanket is thrown over a wooden chair, and the shape of the chair shows through the blanket.

**Expectation (hidden).** The blanket settles onto the chair's back and seat and hangs down at the edges; the chair does not show through the fabric, and the blanket's bumps match the chair beneath.

**Declared violation types.** shape_identity, gravity_direction, material_response

**SA**
- S1 [core] A blanket is thrown over a wooden chair.
- S2 [core] The blanket settles on the chair.
- S3 [core] The chair's shape shows through the blanket.
- S4 [minor] The throw comes first and the settling follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The blanket settles onto the back and seat and hangs down at the edges.
  - fail: It floats; or hangs upward; or stays in the air.
- P2 [core · shape_identity]
  - expect: The blanket's bumps match the chair beneath, and the chair itself is not seen through the fabric.
  - fail: The bumps do not match the chair; or the chair is visible through the blanket as if it were transparent; or the chair changes shape.
- P3 [major · material_response]
  - expect: The soft cloth drapes and folds.
  - fail: It is rigid; or stretches; or tears.
- P4 [major · solidity]
  - expect: The blanket lies on the chair, not through it.
  - fail: It passes through the chair; or the chair passes through the blanket; or it sinks into the seat.
- P5 [fatal · permanence_count]
  - expect: One blanket and one chair keep their number.
  - fail: The blanket duplicates; or the chair vanishes; or the blanket turns into another object.
- P6 [minor · attribute_drift]
  - expect: The blanket's pattern and the room stay the same.
  - fail: The pattern changes; or the room rearranges; or the floor changes.

## MECH-0239 · occlusion_containment · train

**Caption.** A car drives along a road, passes behind a parked truck, and reappears on the far side of it.

**Expectation (hidden).** The car is hidden for a time consistent with its speed and the truck's length and emerges at the same speed and heading; it is the same car and does not show through the truck.

**Declared violation types.** permanence_count, trajectory_momentum

**SA**
- S1 [core] A car drives along a road.
- S2 [core] It passes behind a parked truck.
- S3 [core] It reappears on the far side of the truck.
- S4 [minor] The disappearance comes first and the reappearance follows.

**PC**
- P1 [core · permanence_count]
  - expect: It is the same car, and it does not show through the truck.
  - fail: A different car emerges; or two cars; or the car appears elsewhere.
- P2 [core · trajectory_momentum]
  - expect: It is hidden for a time consistent with its speed and the truck's length and emerges at the same speed and heading.
  - fail: It emerges instantly; or after far too long; or emerges going back.
- P3 [major · solidity]
  - expect: The car is not visible through the truck.
  - fail: It shows through; or passes through the truck; or the truck passes through the car.
- P4 [major · causeless_motion]
  - expect: The parked truck stays still.
  - fail: The truck moves; or vanishes; or the road changes.
- P5 [fatal · shape_identity]
  - expect: One car and one truck keep their shape.
  - fail: The car turns into another vehicle; or the truck changes shape; or the car merges with the truck.
- P6 [minor · attribute_drift]
  - expect: The car's colour and the street stay the same.
  - fail: The car changes colour; or the truck changes colour; or the street rearranges.

## MECH-0240 · occlusion_containment · train

**Caption.** A piggy bank with a coin inside is shaken, and the coin rattles inside without coming into view.

**Expectation (hidden).** The coin stays inside; it does not fall out of the bank's solid sides or appear outside; the bank's shape is unchanged.

**Declared violation types.** permanence_count, solidity

**SA**
- S1 [core] A piggy bank is held.
- S2 [core] It is shaken.
- S3 [core] No coin comes into view.
- S4 [minor] The shake is repeated.

**PC**
- P1 [core · permanence_count]
  - expect: The coin stays inside and does not appear outside.
  - fail: A coin appears outside; or a coin is visible through the bank; or a coin falls out of a solid side.
- P2 [core · solidity]
  - expect: The bank's sides stay solid and nothing passes through them.
  - fail: A coin passes through; or the hand passes through; or the bank cracks open.
- P3 [major · shape_identity]
  - expect: The bank keeps its shape.
  - fail: It changes shape; or grows; or turns into another object.
- P4 [major · causeless_motion]
  - expect: It moves only with the hand.
  - fail: It shakes itself; or jumps; or floats.
- P5 [fatal · permanence_count]
  - expect: One bank keeps its number.
  - fail: It duplicates; or vanishes; or a second bank appears.
- P6 [minor · attribute_drift]
  - expect: The bank's colour and the background stay the same.
  - fail: The bank changes colour; or the hand changes; or the background rearranges.

**Note.** The hands are kept as the minimal trigger; the person is not judged. The rattle is not audible in the frames; only containment is judged.

## MECH-0241 · occlusion_containment · train

**Caption.** An opaque metal jug is tipped over an empty glass, and water pours out of it into the glass.

**Expectation (hidden).** Water appears only from the spout once the jug tilts far enough, and the level in the glass rises; the jug's sides stay opaque.

**Declared violation types.** permanence_count, material_response

**SA**
- S1 [core] An opaque metal jug is tipped over an empty glass.
- S2 [core] Water pours out of the spout.
- S3 [core] The water goes into the glass.
- S4 [minor] The glass is empty at the start.
- S5 [minor] The tip comes first and the pour follows.

**PC**
- P1 [core · permanence_count]
  - expect: Water appears only from the spout once the jug tilts far enough, and the level in the glass rises.
  - fail: Water appears in the glass with no stream; or water comes from the jug's side; or the glass level does not rise.
- P2 [core · material_response]
  - expect: The stream is a liquid, and the jug's sides stay opaque and rigid.
  - fail: The stream is a rigid rod; or the jug becomes transparent; or the jug bulges.
- P3 [major · gravity_direction]
  - expect: The stream falls straight down into the glass.
  - fail: It curves upward; or hangs; or flows back into the jug.
- P4 [major · missing_consequence]
  - expect: Pouring happens only while the jug is tilted.
  - fail: It pours upright; or is tilted with nothing coming out; or continues after it is righted.
- P5 [fatal · permanence_count]
  - expect: One jug and one glass keep their number.
  - fail: The jug duplicates; or water passes through the glass; or the jug vanishes.
- P6 [minor · attribute_drift]
  - expect: The jug, the glass and the background stay the same.
  - fail: The jug changes colour; or the glass changes; or the background rearranges.

## MECH-0242 · deformation · train

**Caption.** A loaded toolbox resting on a crushed cardboard box in a garage is lifted away, and the box stays crumpled.

**Expectation (hidden).** The box keeps its caved-in top and buckled sides after the weight is gone; it does not spring back to shape.

**Declared violation types.** material_response, process_direction

**SA**
- S1 [core] A toolbox rests on a crushed cardboard box in a garage.
- S2 [core] The toolbox is lifted away.
- S3 [core] The box stays crumpled.
- S4 [minor] The box is already crushed at the start.
- S5 [minor] The lift comes first and the box stays as it was.

**PC**
- P1 [core · process_direction]
  - expect: The box keeps its caved-in top and buckled sides after the weight is gone.
  - fail: It springs back to shape; or it collapses further with nothing on it; or it re-inflates slowly.
- P2 [core · material_response]
  - expect: The cardboard holds its creases: the box is crumpled, neither torn to shreds nor rigid.
  - fail: The box turns out rigid and un-dented when the toolbox lifts; or it shreds; or it flows.
- P3 [major · causeless_motion]
  - expect: The box stays where it is.
  - fail: It slides; or lifts with the toolbox; or jumps.
- P4 [major · gravity_direction]
  - expect: The toolbox rises only as it is lifted, and the box stays on the floor.
  - fail: The toolbox floats; or the box rises; or the toolbox drops back.
- P5 [fatal · permanence_count]
  - expect: One box and one toolbox keep their number.
  - fail: The box vanishes or a second appears; or the toolbox passes through the box; or the box turns into another object.
- P6 [minor · attribute_drift]
  - expect: The box's printing, the toolbox and the garage stay the same.
  - fail: The printing changes; or the toolbox changes colour; or the garage rearranges.

