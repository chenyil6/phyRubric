# Rubric review

50 rubrics. SA = caption adherence (core/minor); PC = physics (fatal/core/major/minor, each tagged with a violation type). Expectation is the hidden field from data/, shown for the reviewer only.

# Mechanics

## MECH-0002 · inertia · train

**Caption.** A woman standing in the aisle of a bus holding the overhead rail sways backward as the bus pulls away from the stop.

**Expectation (hidden).** The sway is toward the rear of the bus and coincides with the bus starting to move; she steadies herself once the bus is moving at a steady speed.

**Declared violation types.** causeless_motion, trajectory_momentum

**SA**
- S1 [core] A woman stands in the aisle of a bus, holding an overhead rail.
- S2 [core] The bus pulls away from a stop: it starts moving and the view outside begins to slide past.
- S3 [core] She sways backward, toward the rear of the bus.
- S4 [minor] Her hand stays on the overhead rail through the sway.
- S5 [minor] The bus starts moving first and the sway follows.

**PC**
- P1 [core · causeless_motion]
  - expect: She stands steady while the bus is at the stop; her sway begins as the bus starts moving and eases once it is running at a steady speed.
  - fail: She sways while the bus is still standing at the stop; or she sways with no start of motion visible outside the windows; or she keeps swaying after the view outside has settled to a steady slide.
- P2 [core · trajectory_momentum]
  - expect: The sway carries her toward the rear of the bus, the rail arrests it, and she comes back upright.
  - fail: She is thrown toward the front of the bus as it pulls away; or she leans sideways across the aisle while the bus goes straight; or she keeps toppling backward past the point where the rail holds her.
- P3 [major · material_response]
  - expect: The overhead rail stays fixed and rigid where she grips it, and her feet stay on the floor of the aisle.
  - fail: The rail bends or stretches as she pulls on it; or the rail comes away from the ceiling and she keeps hanging from it; or her feet leave the floor and she hangs in the air.
- P4 [major · trajectory_momentum] (if: Other standing passengers or hanging straps are visible in the aisle.)
  - expect: Other standing passengers and hanging straps lean or swing the same way at the same moment.
  - fail: Another standing passenger sways toward the front while she sways backward; or the hanging straps stay still while she is plainly swaying; or they swing before the bus begins to move.
- P5 [fatal · shape_identity]
  - expect: The passengers, the rail and the seats keep their number and shape, and nothing passes through anything.
  - fail: Her hand passes through the rail; or she merges with a seat or with another passenger; or a limb detaches, vanishes or a second one appears.
- P6 [minor · attribute_drift]
  - expect: Her clothing, the bus interior and the street seen through the windows stay consistent apart from the motion.
  - fail: Her clothing changes colour; or the seat layout changes between frames; or the street outside jumps to a different place.

**Note.** Inertia scene: the woman is kept because her body is what shows the sway. Her expression, posture and how hard the bus accelerates are not judged; only when and which way she moves.

## MECH-0003 · inertia · train

**Caption.** A full cup of coffee sits in the cup holder of a car, and as the car turns sharply left the coffee sloshes up the right side of the cup and spills over the rim.

**Expectation (hidden).** The slosh is toward the outside of the turn (the right), begins as the turn begins, and the surface settles level again once the car straightens.

**Declared violation types.** causeless_motion, material_response

**SA**
- S1 [core] A full cup of coffee sits in the cup holder of a car.
- S2 [core] The car turns sharply to the left.
- S3 [core] The coffee climbs the right side of the cup.
- S4 [core] The coffee spills over the rim.
- S5 [minor] The cup stays in the holder rather than being held in a hand.
- S6 [minor] The turn begins first, then the climb, then the spill.

**PC**
- P1 [core · causeless_motion]
  - expect: The coffee surface lies level while the car runs straight; it starts to tilt as the turn begins and settles level again once the car straightens.
  - fail: The coffee sloshes while the car is driving straight; or it climbs the cup with no turn visible outside; or it keeps sloshing long after the car has straightened up.
- P2 [core · trajectory_momentum]
  - expect: The coffee rides up the side of the cup away from the direction of the turn, which on a left turn is the right side.
  - fail: The coffee climbs the left side of the cup during a left turn; or it rises evenly all around the rim; or it lifts straight up out of the cup.
- P3 [major · material_response]
  - expect: The coffee behaves as a liquid: the surface tilts as one connected sheet, slops over the rim and runs down the outside of the cup.
  - fail: The coffee surface stays flat and rigid while the cup is plainly tilted; or the coffee leaves the cup as a solid lump that keeps its shape; or the spill gathers into balls that roll away.
- P4 [major · gravity_direction]
  - expect: What goes over the rim runs down the outside of the cup and collects in the holder or on the console below.
  - fail: A run of coffee climbs the outside of the cup; or a drip leaves the rim and floats; or the spill gathers on top of the cup.
- P5 [fatal · permanence_count]
  - expect: One cup stays in the holder, and coffee leaves it only by going over the rim.
  - fail: The cup vanishes or a second one appears; or the coffee level rises while it is spilling; or coffee passes through the wall of the cup; or the cup passes through the holder.
- P6 [minor · attribute_drift]
  - expect: The coffee's colour, the cup and the car interior stay the same.
  - fail: The coffee changes colour; or the cup changes size or pattern; or the dashboard and holder rearrange between frames.

## MECH-0004 · inertia · train

**Caption.** A shopping cart is given a push across an empty parking lot and let go, and it rolls on by itself until it slows to a stop.

**Expectation (hidden).** The cart keeps a straight line after release, slows gradually rather than stopping the instant the hands leave it, and does not speed up or change direction on its own.

**Declared violation types.** causeless_motion, trajectory_momentum

**SA**
- S1 [core] A shopping cart is in a parking lot.
- S2 [core] It is given a push and then let go.
- S3 [core] It rolls on by itself with nothing touching it.
- S4 [core] It slows to a stop.
- S5 [minor] The lot around the cart is empty rather than crowded with traffic.
- S6 [minor] The push and release come first, then the free roll, then the stop.

**PC**
- P1 [core · causeless_motion]
  - expect: After the release the cart keeps rolling with nothing touching it, slows steadily, and stays at rest once it has stopped.
  - fail: The cart stops the moment the hands leave it; or it speeds up after the release with nothing touching it; or it sets off again after coming to rest.
- P2 [core · trajectory_momentum]
  - expect: It holds the straight line it was pushed along, its wheels turning as it goes.
  - fail: The cart curves away on the open, level tarmac with nothing touching it; or it reverses and rolls back the way it came; or its wheels stay still while the cart slides on.
- P3 [major · gravity_direction]
  - expect: The cart stays on its wheels on the ground for the whole roll.
  - fail: The cart lifts off the ground and rolls through the air; or it tips onto two wheels and stays tipped with nothing holding it; or it sinks into the tarmac.
- P4 [major · trajectory_momentum] (if: Items are visible in the cart's basket.)
  - expect: Items in the basket ride along with the cart and lurch forward when it slows.
  - fail: An item in the basket stays behind in mid-air as the cart rolls on; or it slides backward as the cart slows; or it moves before the push.
- P5 [fatal · permanence_count]
  - expect: One cart keeps its wheels and its shape and stays outside every solid thing in the lot.
  - fail: The cart vanishes or a second one appears; or a wheel detaches or a new one appears; or the cart passes through a parked car, a kerb or a lamp post.
- P6 [minor · attribute_drift]
  - expect: The cart's colour, the lot markings and the background stay the same.
  - fail: The cart changes colour; or the painted bay lines shift between frames; or the buildings behind the lot rearrange.

## MECH-0005 · inertia · train

**Caption.** An empty playground swing is given one push and left alone, and it keeps going back and forth on its own before gradually dying down.

**Expectation (hidden).** Each arc is a little smaller than the last; the swing never rises higher than the pushed arc and does not stop at once.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] An empty playground swing is present.
- S2 [core] The swing is given one push and then left alone.
- S3 [core] It keeps going back and forth on its own.
- S4 [core] The swinging dies down.
- S5 [minor] It is pushed once and nothing touches it again.
- S6 [minor] The push comes first, then the free swinging, then the dying down.

**PC**
- P1 [core · process_direction]
  - expect: Each arc carries the seat a little less high than the one before, and the swing never rises above the arc the push gave it.
  - fail: An arc carries the seat higher than the one before it with nothing touching the swing; or the arcs hold exactly the same height and then the swing stops dead; or the swinging builds up on its own.
- P2 [core · causeless_motion]
  - expect: The swing moves because of the one push; nothing else touches it, and it changes only by dying down.
  - fail: The swing gets a fresh shove with nothing visible touching it; or it halts at the end of an arc and hangs there; or it starts up again after hanging still.
- P3 [major · gravity_direction]
  - expect: The seat hangs below its chains and travels along an arc, moving quickest at the bottom and slowest at the ends.
  - fail: The seat rises above the height of the crossbar; or it stays out sideways at the end of an arc instead of swinging back; or it moves quickest at the top of its arc.
- P4 [major · material_response]
  - expect: The chains stay taut and straight and the seat hangs from them, the two moving as one.
  - fail: A chain bunches slack while the seat is swinging out; or a chain grows longer as the swing rises; or the seat swings while the chains hang still.
- P5 [fatal · permanence_count]
  - expect: One seat on its chains keeps its number and shape and stays clear of the frame.
  - fail: The seat vanishes or a second swing appears; or a chain comes away from the bar and the seat keeps swinging; or the seat passes through a chain or through the frame.
- P6 [minor · attribute_drift]
  - expect: The swing's colour, the frame and the playground behind stay the same.
  - fail: The seat changes colour or shape; or the frame changes height between frames; or the ground below rearranges.

## MECH-0006 · inertia · train

**Caption.** A woman is jogging on a treadmill when the belt stops abruptly, and she lurches forward and grabs the handrails.

**Expectation (hidden).** The lurch happens the instant the belt stops, not before; it is forward, in the direction she was running, not backward or sideways; she catches herself on the rails and settles, and does not keep gliding forward after the belt is still.

**Declared violation types.** trajectory_momentum, causeless_motion

**SA**
- S1 [core] A woman is jogging on a treadmill.
- S2 [core] The belt stops abruptly.
- S3 [core] She lurches forward.
- S4 [core] She grabs the handrails.
- S5 [minor] She is running rather than standing still before the belt stops.
- S6 [minor] The belt stops first, then the lurch, then the grab.

**PC**
- P1 [core · causeless_motion]
  - expect: She holds her place on the belt while it runs, and her lurch begins at the moment the belt stops.
  - fail: She lurches forward while the belt is still running at speed; or she is thrown with no change in the belt visible; or she drifts along the stopped belt with nothing driving her.
- P2 [core · trajectory_momentum]
  - expect: The lurch carries her forward, the way she was running, onto the handrails, and she settles once she has caught them.
  - fail: She is thrown backward off the rear of the treadmill when the belt stops; or she is thrown sideways off the deck; or she keeps sliding forward past the rails and off the front.
- P3 [major · missing_consequence]
  - expect: She catches herself on the rails: her hands reach them, close on them, and her forward motion ends there.
  - fail: Her hands pass over the rails and she carries on forward; or she stops in mid-lurch before reaching the rails with nothing holding her; or the rails travel forward with her.
- P4 [major · material_response]
  - expect: The rails and the frame stay rigid under her weight and the belt lies flat on the deck.
  - fail: A handrail bends or bows as she grabs it; or the frame wobbles like rubber; or the belt lifts off the deck in a wave.
- P5 [fatal · shape_identity]
  - expect: One runner and one treadmill keep their number and shape, and nothing passes through anything.
  - fail: Her hand passes through a handrail; or a limb detaches, vanishes or a second one appears; or she sinks into the deck; or the treadmill turns into another machine.
- P6 [minor · attribute_drift]
  - expect: Her clothing, the treadmill's console and the room behind stay the same.
  - fail: Her clothing changes colour; or the console moves to the other side of the frame; or the room behind rearranges between frames.

**Note.** Inertia scene: the runner is kept because her body is what carries the momentum. Her running form and how fast she was jogging are not judged; only when and which way she is thrown.

## MECH-0007 · inertia · train

**Caption.** A phone lying flat on the dashboard of a car slides forward toward the windshield when the car brakes suddenly at a red light.

**Expectation (hidden).** The slide begins as the braking begins and is toward the front of the car; the phone stops when the car stops or when it hits the windshield.

**Declared violation types.** causeless_motion, trajectory_momentum

**SA**
- S1 [core] A phone lies flat on the dashboard of a car.
- S2 [core] The car brakes suddenly at a red light.
- S3 [core] The phone slides forward toward the windshield.
- S4 [minor] A red traffic light is visible ahead of the car.
- S5 [minor] The braking comes first and the slide follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The phone lies still while the car runs at a steady speed and starts to slide as the braking begins.
  - fail: The phone slides while the car is still travelling steadily; or it slides with no braking visible; or it keeps sliding after the car has come to rest.
- P2 [core · trajectory_momentum]
  - expect: The slide carries the phone toward the front of the car and ends at the windshield or when the car stops.
  - fail: The phone slides backward, away from the windshield, under braking; or it slides sideways across the dashboard while the car brakes in a straight line; or it gathers speed the longer it slides.
- P3 [major · gravity_direction]
  - expect: The phone keeps its face against the dashboard as it slides and stays on that surface.
  - fail: The phone lifts off the dashboard and floats; or it stands up on edge and stays there; or it sinks into the dashboard.
- P4 [major · trajectory_momentum] (if: Other loose or hanging objects are visible inside the car.)
  - expect: Other loose objects in the cabin slide or swing forward at the same moment.
  - fail: Another loose object stays put while the phone slides forward; or it slides backward under the same braking; or it moves before the braking begins.
- P5 [fatal · permanence_count]
  - expect: One phone on one dashboard keeps its shape, and it stays inside the car.
  - fail: The phone vanishes or a second one appears; or the phone passes through the windshield; or it turns into another object as it slides.
- P6 [minor · attribute_drift]
  - expect: The phone's case, the dashboard and the street ahead stay consistent.
  - fail: The phone changes colour or size; or the dashboard vents move between frames; or the traffic light shifts to another part of the scene.

## MECH-0008 · inertia · train

**Caption.** A boy takes a short run-up on a field, leaps forward off one foot, and after landing on both feet takes a few stumbling steps forward before he stops.

**Expectation (hidden).** He leaves the ground going forward and comes down along a forward arc; the stumbling steps begin at the instant of landing and go the same way he was travelling, never backward or sideways; he does not hover at the top, and he does not stop dead on the spot the moment his feet touch.

**Declared violation types.** trajectory_momentum, gravity_direction

**SA**
- S1 [core] A boy takes a run-up on a field.
- S2 [core] He leaps forward off one foot.
- S3 [core] He lands on both feet.
- S4 [core] He takes a few stumbling steps forward and comes to a stop.
- S5 [minor] The run-up is short rather than a long approach.
- S6 [minor] The run-up comes first, then the leap, then the landing, then the steps.

**PC**
- P1 [core · gravity_direction]
  - expect: He rises after the take-off, then comes down, falling quicker the nearer he gets to the ground.
  - fail: He keeps rising until he leaves the frame; or he holds still at the top of the leap; or he drops straight down from the take-off point without ever rising.
- P2 [core · trajectory_momentum]
  - expect: His flight carries him forward from where he took off, and the stumbling steps continue that way from the moment he lands.
  - fail: He comes down behind where he took off, having travelled backward through the air; or he stumbles backward or sideways after landing; or he stops dead on the spot as his feet touch down.
- P3 [major · causeless_motion]
  - expect: Once in the air he keeps the course the leap gave him; he is carried along the ground only while his feet are driving him.
  - fail: He changes direction in mid-air; or he gathers speed in mid-air; or he slides on across the grass with his feet planted and still.
- P4 [major · material_response] (if: Grass or loose ground is visibly disturbed by his feet.)
  - expect: The grass flattens where he drives off and where he lands, and springs back or stays pressed.
  - fail: Torn-up grass rises away and hangs in the air; or the ground ripples like water under his feet; or the turf stays untouched where he plainly drove off it.
- P5 [fatal · shape_identity]
  - expect: One boy keeps his limbs, his number and his shape, and he stays above the ground.
  - fail: A limb stretches, detaches or vanishes; or he passes through the ground; or a second figure appears beside him; or his body morphs into another shape in mid-leap.
- P6 [minor · attribute_drift]
  - expect: His clothing, the field and the background stay the same.
  - fail: His clothing changes colour; or the field markings shift between frames; or the background rearranges.

**Note.** Biomechanics scene: the boy is kept because his body is what carries the momentum. Athletic form, technique and how far he jumps are not judged; only the direction and order of the motion.

## MECH-0009 · inertia · train

**Caption.** A serving cart carrying a tray of full water glasses is pushed forward and stopped short, and the water sloshes forward and spills.

**Expectation (hidden).** The water surges in the direction the cart was moving, at the moment it stops; the glasses may slide forward on the tray; the water settles afterwards.

**Declared violation types.** causeless_motion, material_response

**SA**
- S1 [core] A serving cart carries a tray of full water glasses.
- S2 [core] The cart is pushed forward and then stopped short.
- S3 [core] The water sloshes forward.
- S4 [core] The water spills.
- S5 [minor] Several glasses stand on the tray rather than a single one.
- S6 [minor] The cart stops first, then the slosh, then the spill.

**PC**
- P1 [core · causeless_motion]
  - expect: The water surfaces lie level while the cart rolls steadily and surge at the moment it is stopped.
  - fail: The water sloshes while the cart is rolling at a steady speed; or it surges with no stop visible; or it keeps sloshing long after the cart is still.
- P2 [core · trajectory_momentum]
  - expect: The surge carries the water toward the front of the cart, the way it was moving, and over the forward rims.
  - fail: The water surges toward the back of the cart when it stops; or it climbs evenly around every rim; or it lifts straight up out of the glasses.
- P3 [major · material_response]
  - expect: The water tilts as one connected surface, slops over the rim and runs down the outside of the glass onto the tray.
  - fail: A water surface stays flat and rigid while its glass is plainly lurching; or water leaves a glass as a solid lump that keeps its shape; or the spill gathers into balls that roll off the tray.
- P4 [major · gravity_direction]
  - expect: Spilled water runs down the outsides of the glasses and pools on the tray, dripping over its edge.
  - fail: Spilled water climbs the outside of a glass; or a spill floats above the tray; or the puddle gathers on top of a glass.
- P5 [fatal · permanence_count]
  - expect: The glasses keep their number and shape and water leaves them only over the rim.
  - fail: A glass vanishes or a new one appears on the tray; or water passes through the wall of a glass; or a glass merges with the tray; or the water level in a glass rises while it is spilling.
- P6 [minor · attribute_drift]
  - expect: The glasses, the tray and the cart keep their colour and arrangement apart from the slosh.
  - fail: The tray changes colour; or the glasses change size or pattern; or the cart's shelves rearrange between frames.

## MECH-0010 · inertia · train

**Caption.** A ceiling fan running at full speed is switched off at the wall, and the blades keep turning for a while before coming to a stop.

**Expectation (hidden).** The slowing is gradual over several seconds; the blades do not halt instantly, reverse, or speed up after the switch.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A ceiling fan is running at full speed.
- S2 [core] It is switched off at the wall.
- S3 [core] The blades keep turning after the switch.
- S4 [core] They come to a stop.
- S5 [minor] The wall switch is visible.
- S6 [minor] The switch is thrown first, then the blades run on, then they stop.

**PC**
- P1 [core · process_direction]
  - expect: After the switch the blades slow steadily, keeping the direction they were already turning, until they stop.
  - fail: The blades speed up after the switch; or they reverse direction as they slow; or they slow and then pick up again.
- P2 [core · causeless_motion]
  - expect: The blades come to rest only by slowing down, and they stay at rest once stopped.
  - fail: The blades halt in the same frame the switch is thrown; or they stop dead while still turning quickly; or they start turning again after coming to rest.
- P3 [major · material_response]
  - expect: The blades stay flat and rigid and turn together about the hub.
  - fail: A blade bends or droops as it slows; or the blades turn at different speeds from one another; or a blade flexes like cloth.
- P4 [major · gravity_direction]
  - expect: The fan hangs from its mount on the ceiling and stays there while the blades slow.
  - fail: The fan drifts down away from the ceiling; or it tilts and stays tilted with nothing holding it; or it rises up into the ceiling.
- P5 [fatal · permanence_count]
  - expect: The fan keeps its number of blades and its shape throughout.
  - fail: A blade vanishes or an extra one appears; or a blade passes through the ceiling or through the hub; or the fan turns into another fixture.
- P6 [minor · attribute_drift]
  - expect: The blades' colour, the fixture and the room stay the same.
  - fail: The blades change colour; or the light fitting under the fan changes shape; or the room behind rearranges between frames.

## MECH-0011 · inertia · train

**Caption.** A wagon loaded with pumpkins is pulled along a path by its handle and the pull stops suddenly; the wagon rolls on a little and the pumpkins tip forward.

**Expectation (hidden).** The wagon does not stop the instant the pull does; it rolls until the handle checks it; the pumpkins tip forward, not backward.

**Declared violation types.** causeless_motion, trajectory_momentum

**SA**
- S1 [core] A wagon loaded with pumpkins is pulled along a path by its handle.
- S2 [core] The pull stops suddenly.
- S3 [core] The wagon rolls on a little.
- S4 [core] The pumpkins tip forward.
- S5 [minor] Several pumpkins are loaded in the wagon rather than one.
- S6 [minor] The pull stops first, then the wagon rolls on and the pumpkins tip.

**PC**
- P1 [core · causeless_motion]
  - expect: The wagon keeps rolling after the pull stops and comes to rest as the handle checks it.
  - fail: The wagon stops in the same instant the pull does; or it rolls on although nothing ever pulled it; or it sets off again after coming to rest.
- P2 [core · trajectory_momentum]
  - expect: The pumpkins carry on the way the wagon was travelling and tip toward the front of the bed.
  - fail: The pumpkins tip toward the back of the wagon; or they tip sideways while the wagon travels straight; or they stay fixed in place while the wagon jolts to a stop.
- P3 [major · gravity_direction]
  - expect: Pumpkins that tip fall against the front wall or roll down onto one another, and any that leave the wagon drop to the path.
  - fail: A pumpkin rises out of the wagon and floats; or one climbs the wagon's side; or one hangs above the bed after tipping.
- P4 [major · material_response]
  - expect: The pumpkins stay round and firm as they knock together and against the wagon, and the bed stays rigid under them.
  - fail: A pumpkin flattens like dough where it lands and stays flat; or one stretches as it tips; or the wagon's bed sags like cloth beneath them.
- P5 [fatal · permanence_count]
  - expect: The pumpkins keep their number and the wagon stays one wagon with its handle attached.
  - fail: A pumpkin vanishes or a new one appears; or a pumpkin passes through the wagon's wall; or the wagon passes through the kerb of the path.
- P6 [minor · attribute_drift]
  - expect: The pumpkins' colour, the wagon and the path stay the same.
  - fail: A pumpkin changes colour or size; or the wagon changes colour; or the path behind rearranges between frames.

## MECH-0012 · inertia · train

**Caption.** A bowling ball is released at the top of the lane and rolls the full length of the lane to the pins at the far end.

**Expectation (hidden).** The ball keeps nearly constant speed along a straight or gently curving path and does not slow to a stop or wander before reaching the pins.

**Declared violation types.** trajectory_momentum, causeless_motion

**SA**
- S1 [core] A bowling ball is released at the top of a lane.
- S2 [core] It rolls along the lane.
- S3 [core] It reaches the pins at the far end.
- S4 [minor] It travels the full length of the lane rather than part of it.
- S5 [minor] The release comes first and the roll down the lane follows.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The ball holds close to the speed it left the hand with for the whole length of the lane, on a straight or gently curving line.
  - fail: The ball slows to a stop before reaching the pins; or it gathers speed as it travels; or it wanders from side to side across the lane.
- P2 [core · causeless_motion]
  - expect: After the release nothing touches the ball; it turns only gradually and keeps going forward.
  - fail: The ball changes direction sharply on the open lane with nothing touching it; or it reverses back up the lane; or it stops and then sets off again.
- P3 [major · gravity_direction]
  - expect: The ball stays down on the lane surface, its weight on the wood.
  - fail: The ball lifts off the lane and travels through the air; or it sinks into the lane; or it hangs over the gutter without dropping into it.
- P4 [major · material_response]
  - expect: The ball stays a hard sphere and turns as it rolls; the lane surface stays flat under it.
  - fail: The ball squashes or wobbles like rubber as it goes; or its surface ripples while it rolls; or it leaves a dent in the lane behind it.
- P5 [fatal · permanence_count]
  - expect: One ball travels the lane and the rack keeps its pins standing until the ball reaches them.
  - fail: The ball vanishes or a second one appears on the lane; or a pin disappears before the ball arrives; or the ball passes through the lane surface.
- P6 [minor · attribute_drift]
  - expect: The ball's colour and finger holes, the lane markings and the pins stay the same.
  - fail: The ball changes colour as it rolls; or the arrows on the lane shift between frames; or the standing pins change their arrangement before being hit.

## MECH-0013 · inertia · train

**Caption.** A skateboarder riding along a sidewalk hits a raised crack, the board stops dead, and the rider is thrown forward off the board.

**Expectation (hidden).** The rider continues in the direction of travel and stumbles or falls ahead of the stopped board; the rider does not stop with the board.

**Declared violation types.** causeless_motion, trajectory_momentum

**SA**
- S1 [core] A skateboarder rides along a sidewalk.
- S2 [core] The board hits a raised crack.
- S3 [core] The board stops dead.
- S4 [core] The rider is thrown forward off the board.
- S5 [minor] The crack stands raised above the surrounding pavement.
- S6 [minor] The board hits the crack and stops first, then the rider is thrown.

**PC**
- P1 [core · causeless_motion]
  - expect: The board stops where it meets the raised crack and not before, and the rider's fall begins at that moment.
  - fail: The board stops before it reaches the crack; or the rider is thrown while the board is still rolling freely; or the board stops with nothing in its path.
- P2 [core · trajectory_momentum]
  - expect: The rider carries on the way he was travelling and comes down ahead of the stopped board.
  - fail: The rider is thrown backward, behind the board; or the rider stops with the board and stays standing on it; or the rider is thrown sideways off a board that was running straight.
- P3 [major · gravity_direction]
  - expect: Once off the board the rider drops toward the ground and lands on it.
  - fail: The rider hangs in the air after leaving the board; or the rider keeps rising after being thrown; or the rider floats forward at the same height without coming down.
- P4 [major · missing_consequence]
  - expect: The crack checks the board: it stops there, or is thrown back, rather than carrying on as though nothing were in its way.
  - fail: The board rolls over the crack unaffected while the rider is thrown; or the board runs on ahead of the rider; or the crack flattens away as the board reaches it.
- P5 [fatal · solidity]
  - expect: The board, the rider and the sidewalk stay solid and keep their number.
  - fail: A wheel passes through the sidewalk; or the rider passes through the board or through the ground; or the board vanishes at the crack; or a second board appears.
- P6 [minor · attribute_drift]
  - expect: The rider's clothing, the board's deck and the sidewalk stay the same.
  - fail: The rider's clothing changes colour; or the graphic on the deck changes; or the sidewalk's slabs and joints rearrange between frames.

**Note.** Inertia scene: the rider is kept because the body carrying on past the stopped board is the physics. Skill, stance and whether the fall is graceful are not judged.

## MECH-0014 · inertia · train

**Caption.** A car driving along an icy street brakes hard, its wheels lock, and it slides on past the stop line before it comes to a halt.

**Expectation (hidden).** The car keeps moving in its original direction after the wheels lock and slows only gradually while the wheels are not turning; it comes to rest beyond the line, not on the spot, and does not swerve or stop instantly.

**Declared violation types.** causeless_motion, trajectory_momentum

**SA**
- S1 [core] A car drives along an icy street.
- S2 [core] It brakes hard.
- S3 [core] Its wheels lock.
- S4 [core] It slides on past the stop line and comes to a halt beyond it.
- S5 [minor] The stop line painted on the road is visible.
- S6 [minor] The braking comes first, then the locked wheels, then the slide.

**PC**
- P1 [core · trajectory_momentum]
  - expect: Once the wheels lock the car keeps going the way it was travelling and slows gradually, coming to rest past the line.
  - fail: The car stops on the spot as soon as the wheels lock; or it keeps sliding at its old speed and never comes to rest; or it slides backward.
- P2 [core · causeless_motion]
  - expect: The car slides along its own line on the ice; nothing turns it or sets it going again.
  - fail: The car swerves sharply on the open, straight road with nothing striking it; or it moves off again after coming to rest; or it gathers speed while the wheels are locked.
- P3 [major · missing_consequence]
  - expect: The wheels are visibly still while the body slides on over the ice.
  - fail: The wheels keep rolling with the road while the car is plainly skidding; or the wheels turn backward while the car slides forward; or the wheels lock and the car halts in the same instant.
- P4 [major · material_response] (if: Loose snow, slush or spray is visibly disturbed at the tyres.)
  - expect: Loose snow and ice chips thrown up at the tyres fall back to the road.
  - fail: Spray hangs in the air after the car has stopped; or it is flung forward ahead of the car; or ice chips rise away from the road and keep rising.
- P5 [fatal · permanence_count]
  - expect: One car keeps its shape on the road and stays outside every other solid thing.
  - fail: The car vanishes or a second one appears; or it passes through another vehicle or a kerb; or it changes into a different car mid-slide.
- P6 [minor · attribute_drift]
  - expect: The car's colour, the road markings and the street stay the same.
  - fail: The car changes colour; or the stop line moves along the road between frames; or the buildings alongside rearrange.

## MECH-0015 · inertia · train

**Caption.** A spinning top is set going on a wooden table and left alone; it spins for a while, starts to wobble, and finally topples over.

**Expectation (hidden).** The spin slows gradually and the wobble grows before the fall; the top does not speed up, right itself, or stop upright.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A spinning top is set going on a wooden table.
- S2 [core] It spins for a while.
- S3 [core] It starts to wobble.
- S4 [core] It topples over.
- S5 [minor] The top is left alone once it is spinning.
- S6 [minor] The spinning comes first, then the wobble, then the fall.

**PC**
- P1 [core · process_direction]
  - expect: The spin slows steadily and the wobble grows wider as it slows, ending in the topple.
  - fail: The top spins faster as time passes; or the wobble shrinks and the top rights itself; or the top comes to rest still standing upright.
- P2 [core · causeless_motion]
  - expect: The top keeps spinning with nothing touching it and changes only by slowing down.
  - fail: The top is driven across the table with nothing touching it; or it reverses the way it spins; or it starts spinning again after it has fallen.
- P3 [major · gravity_direction]
  - expect: The top leans further as the wobble grows and comes down onto its side on the table.
  - fail: The top leans right over and hangs there without falling; or it tips upward off the table; or it falls through the table top.
- P4 [major · material_response]
  - expect: The top stays rigid while it spins and lands, and the table stays flat and solid under its tip.
  - fail: The top bends or squashes as it wobbles; or it flows like liquid where it lands; or the table surface dips under the spinning tip.
- P5 [fatal · permanence_count]
  - expect: One top on one table keeps its shape throughout.
  - fail: The top vanishes or a second one appears; or it turns into another object as it falls; or a part of it comes away while it spins.
- P6 [minor · attribute_drift]
  - expect: The top's colours, the table's grain and the surroundings stay the same.
  - fail: The top changes colour as it spins; or the grain of the table shifts between frames; or objects around the table rearrange.

## MECH-0016 · inertia · train

**Caption.** A wet umbrella is flicked sharply and stopped short, and the water drops fly off the tip and keep going in the direction of the flick.

**Expectation (hidden).** The drops leave at the moment the umbrella stops, not before the flick or long after; they travel the way the tip was moving and then drop toward the ground; they do not hang beside the umbrella, follow it back, or scatter in every direction.

**Declared violation types.** trajectory_momentum, causeless_motion, gravity_direction

**SA**
- S1 [core] A wet umbrella is flicked sharply.
- S2 [core] The flick is stopped short.
- S3 [core] Water drops fly off the tip.
- S4 [core] The drops carry on the way the flick was heading.
- S5 [minor] The umbrella is visibly wet before the flick.
- S6 [minor] The flick and its stop come first, then the drops leave the tip.

**PC**
- P1 [core · causeless_motion]
  - expect: The drops leave at the moment the umbrella is stopped, neither before the flick begins nor long after it ends.
  - fail: Drops fly off while the umbrella is being held still; or they leave before the flick starts; or they keep streaming off long after the umbrella has stopped.
- P2 [core · trajectory_momentum]
  - expect: Each drop leaves along the direction the tip was travelling and holds that direction as it flies.
  - fail: The drops follow the umbrella back as it is stopped; or they spray out equally in every direction from the tip; or they hang beside the umbrella without moving away.
- P3 [major · gravity_direction]
  - expect: Once free, the drops curve downward and fall toward the ground.
  - fail: A drop climbs steadily after leaving the tip; or a drop hangs still in the air; or the drops hold a flat line all the way to the edge of the frame.
- P4 [major · material_response]
  - expect: The water leaves as rounded drops or a fine spray, shed from the surface of the fabric.
  - fail: The water leaves as a rigid shard that keeps its shape; or drops stretch into long threads that stay joined to the tip; or the fabric looks dry while water is plainly flying off it.
- P5 [fatal · permanence_count]
  - expect: The umbrella keeps its shape and water leaves it only by flying off it.
  - fail: The umbrella vanishes or turns into another object; or drops appear in the air away from the umbrella; or a rib passes through the fabric.
- P6 [minor · attribute_drift]
  - expect: The umbrella's colour and panels and the background stay the same.
  - fail: The umbrella changes colour during the flick; or its panels change pattern; or the background rearranges between frames.

## MECH-0017 · inertia · train

**Caption.** A family sits in the back seat of a car as it takes a sharp bend on a country road, and all of them lean toward the outside of the bend.

**Expectation (hidden).** The lean begins as the car enters the bend and eases as the road straightens; everyone leans the same way, away from the centre of the curve; nobody leans into the bend, and nobody moves before the car starts turning.

**Declared violation types.** trajectory_momentum, causeless_motion

**SA**
- S1 [core] A family sits in the back seat of a car.
- S2 [core] The car takes a sharp bend on a country road.
- S3 [core] All of them lean toward the outside of the bend.
- S4 [minor] The country road and its bend are visible through the windows.
- S5 [minor] The car enters the bend first and the lean follows.

**PC**
- P1 [core · causeless_motion]
  - expect: They sit upright while the road runs straight, lean as the car enters the bend, and come back upright as it straightens.
  - fail: They lean while the car is travelling straight; or they lean with no bend visible outside; or they stay leaning long after the road has straightened.
- P2 [core · trajectory_momentum]
  - expect: Everyone leans the same way, away from the inside of the curve, for as long as the car is turning.
  - fail: One passenger leans into the bend while the others lean out; or they are thrown forward or backward as the car turns; or one of them leans before the car begins to turn.
- P3 [major · gravity_direction]
  - expect: They stay seated with their weight on the seat while they lean.
  - fail: A passenger lifts off the seat and floats; or a passenger rises up along the seat back; or a head goes up through the roof.
- P4 [major · trajectory_momentum] (if: Loose or hanging items are visible inside the car.)
  - expect: Loose and hanging items in the cabin swing the same way at the same moment.
  - fail: A hanging item swings toward the inside of the bend; or loose objects stay still while the passengers are plainly leaning; or they swing before the car begins to turn.
- P5 [fatal · shape_identity]
  - expect: The passengers, the seats and the belts keep their number and shape.
  - fail: A passenger merges with a neighbour or with the seat; or a limb detaches or an extra one appears; or a head passes through the window.
- P6 [minor · attribute_drift]
  - expect: Clothing colours, the car interior and the view outside stay consistent apart from the turn.
  - fail: A passenger's clothing changes colour; or the seat covers change pattern; or the landscape outside jumps to a different place.

**Note.** Inertia scene: the passengers are kept because their bodies are what show the lean. Expressions, posture and how sharp the bend is are not judged; only when and which way they move.

## MECH-0019 · gravity_fall · train

**Caption.** A hammer resting on the top of a ladder is knocked off and falls to the ground.

**Expectation (hidden).** The hammer drops straight down, speeding up as it falls, and hits the ground; it does not pause or drift sideways.

**Declared violation types.** gravity_direction, causeless_motion

**SA**
- S1 [core] A hammer rests on the top of a ladder.
- S2 [core] It is knocked off the ladder.
- S3 [core] It falls to the ground.
- S4 [minor] The knock comes first and the fall follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The hammer goes downward from the top of the ladder, falling quicker the further it drops, and reaches the ground.
  - fail: The hammer drifts sideways away from the ladder as it falls; or it hangs in the air after leaving the top; or it rises after being knocked off.
- P2 [core · causeless_motion]
  - expect: The hammer lies still on the ladder until it is knocked, and once on the ground it stays there.
  - fail: The hammer sets off before anything reaches it; or it slides off the top with nothing touching it; or it moves again after settling on the ground.
- P3 [major · missing_consequence]
  - expect: The hammer meets the ground and comes to rest there, clattering or bouncing low before it settles.
  - fail: The hammer comes to rest in mid-air short of the ground; or it carries on down past the ground line; or the ground it lands on shows no disturbance at all where a heavy tool struck it.
- P4 [major · material_response]
  - expect: The hammer stays a rigid head on a rigid handle, and the ground takes the impact.
  - fail: The hammer bends or squashes where it lands; or it bounces high off a hard floor like a rubber ball; or it sinks into a hard floor as if into mud.
- P5 [fatal · permanence_count]
  - expect: One hammer and one ladder keep their number and shape, and neither passes through the other.
  - fail: The hammer vanishes on the way down or a second one appears; or it passes through a rung of the ladder; or it turns into another tool as it falls.
- P6 [minor · attribute_drift]
  - expect: The hammer's colour, the ladder and the surroundings stay the same.
  - fail: The hammer changes colour or size; or the ladder changes its number of rungs between frames; or the background rearranges.

## MECH-0020 · gravity_fall · train

**Caption.** A cat nudges a pen off the edge of a desk with its paw and the pen falls to the floor.

**Expectation (hidden).** The pen tips and falls as soon as it is past the edge; it does not hang in the air beyond the desk or drift.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] A cat and a pen are on a desk.
- S2 [core] The cat nudges the pen with its paw toward the edge.
- S3 [core] The pen goes over the edge and falls to the floor.
- S4 [minor] The nudge is made with a paw.
- S5 [minor] The nudge comes first and the fall follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The pen moves when the paw reaches it and only then, and it goes over once it is past the edge.
  - fail: The pen starts moving before the paw reaches it; or the paw pushes the pen and the pen stays where it is; or the pen leaves the desk with the paw never touching it.
- P2 [core · gravity_direction]
  - expect: Once past the edge the pen tips and drops, falling quicker as it goes, and lands on the floor.
  - fail: The pen hangs in the air past the edge of the desk; or it drifts outward while staying level with the desk top; or it rises after leaving the desk.
- P3 [major · causeless_motion]
  - expect: On the desk the pen moves only where it is pushed; on the floor it comes to rest and stays.
  - fail: The pen slides across the desk with nothing touching it; or it rolls off on its own before the cat reaches it; or it sets off again once it has settled on the floor.
- P4 [major · material_response]
  - expect: The pen stays a rigid stick as it falls and lands, clattering on the floor.
  - fail: The pen bends like rope as it falls; or it splashes where it lands; or it flattens against the floor and stays flat.
- P5 [fatal · solidity]
  - expect: The pen, the cat, the desk and the floor stay solid and keep their number.
  - fail: The pen vanishes on the way down or a second one appears; or the pen passes through the desk top or the floor; or the paw passes through the pen.
- P6 [minor · attribute_drift]
  - expect: The pen's colour, the cat's markings and the desk stay the same.
  - fail: The pen changes colour or length; or the cat's markings change between frames; or the things on the desk rearrange.

**Note.** The cat is kept as the minimal trigger for the fall; its gait, posture and whether it looks at the pen are not judged.

## MECH-0021 · gravity_fall · train

**Caption.** The string of a helium balloon tied to a park bench comes loose, and the balloon floats up into the sky.

**Expectation (hidden).** The balloon rises steadily with the string trailing below it; it does not fall, hover at bench height, or rise faster than a gentle drift.

**Declared violation types.** gravity_direction, trajectory_momentum

**SA**
- S1 [core] A helium balloon is tied by its string to a park bench.
- S2 [core] The string comes loose from the bench.
- S3 [core] The balloon floats up into the sky.
- S4 [minor] The string comes loose first and the rise follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The balloon stays by the bench while it is tied and starts to rise only once the string is free.
  - fail: The balloon rises while its string is still tied to the bench; or it drifts off with the string never coming loose; or it hangs still above the bench long after coming free.
- P2 [core · gravity_direction]
  - expect: The balloon climbs with the string hanging beneath it, the loose end trailing as the lowest part.
  - fail: The balloon drops to the ground once free; or it climbs with the string standing above it; or the string holds out straight sideways and stays there.
- P3 [major · trajectory_momentum]
  - expect: The rise is a steady drift upward that keeps going while the balloon is in view.
  - fail: The balloon shoots upward like a thrown ball; or it stops in mid-air and hangs at bench height; or it reverses and comes back down.
- P4 [major · material_response]
  - expect: The balloon stays a taut rounded shape and the string stays a limp line of fixed length.
  - fail: The balloon deflates and keeps climbing; or the string goes rigid like a rod; or the string grows longer as the balloon climbs.
- P5 [fatal · permanence_count]
  - expect: One balloon on one string keeps its shape and passes through nothing.
  - fail: The balloon vanishes or a second one appears; or the string comes away from the balloon and the balloon goes on trailing it; or the balloon passes through a branch or through the bench.
- P6 [minor · attribute_drift]
  - expect: The balloon's colour, the bench and the park stay the same.
  - fail: The balloon changes colour as it rises; or the bench changes shape between frames; or the park behind rearranges.

## MECH-0022 · gravity_fall · train

**Caption.** Autumn leaves come loose from a tree on a still afternoon and drift down to settle on the lawn.

**Expectation (hidden).** The leaves fall slowly, fluttering and tumbling, always ending lower than they started; none rise again or hang still in the air.

**Declared violation types.** gravity_direction, trajectory_momentum

**SA**
- S1 [core] Leaves come loose from a tree.
- S2 [core] They drift down through the air.
- S3 [core] They settle on the lawn.
- S4 [minor] The afternoon is still: the tree and the grass are not being blown about.
- S5 [minor] The leaves come loose first and the drifting down follows.

**PC**
- P1 [core · gravity_direction]
  - expect: Every leaf ends lower than it started, fluttering and turning on the way but never climbing back toward the branch.
  - fail: A leaf rises back up toward the branches; or a leaf hangs still in mid-air; or a leaf travels upward out of the frame.
- P2 [core · trajectory_momentum]
  - expect: The leaves fall slowly, swinging from side to side, each one on its own path.
  - fail: The leaves drop straight and fast like stones; or they all fall together as one rigid sheet; or a leaf gathers speed until it streaks downward.
- P3 [major · causeless_motion]
  - expect: Leaves come away from the tree and stay put once they are on the lawn; on a still afternoon nothing sweeps them about.
  - fail: A settled leaf lifts off the lawn again with nothing touching it; or leaves are driven sideways as if in a gale while the tree stands still; or a leaf turns sharply in the open air.
- P4 [major · material_response]
  - expect: The leaves stay thin and flexible, curling and turning in the air and lying flat on the grass.
  - fail: A leaf stays rigid like a board for its whole fall; or a leaf bounces off the lawn like a ball; or a leaf shatters where it lands.
- P5 [fatal · permanence_count]
  - expect: The leaves keep their number: none appear in mid-air and none disappear.
  - fail: Leaves appear in the air with no branch above them; or a falling leaf vanishes before reaching the lawn; or a leaf passes through a branch or through the ground.
- P6 [minor · attribute_drift]
  - expect: The leaves' colours, the tree and the lawn stay the same.
  - fail: A leaf changes colour as it falls; or the tree's foliage changes colour between frames; or the lawn behind rearranges.

## MECH-0023 · gravity_fall · train

**Caption.** A ceramic plate slides off the edge of a restaurant counter, drops onto the tiled floor, and shatters.

**Expectation (hidden).** The plate falls straight down and breaks on contact with the tile, pieces scattering outward; it does not bounce whole or break before it lands.

**Declared violation types.** gravity_direction, material_response

**SA**
- S1 [core] A ceramic plate is at the edge of a restaurant counter.
- S2 [core] It slides off the edge.
- S3 [core] It drops onto the floor.
- S4 [core] It shatters.
- S5 [minor] The floor below the counter is tiled.
- S6 [minor] The slide comes first, then the drop, then the shattering.

**PC**
- P1 [core · gravity_direction]
  - expect: The plate falls downward from the counter edge, quicker the further it goes, and reaches the floor.
  - fail: The plate drifts sideways away from the counter as it falls; or it hangs in the air below the counter; or it rises after leaving the edge.
- P2 [core · material_response]
  - expect: The plate stays whole until it meets the tile, then breaks into hard pieces that scatter outward.
  - fail: The plate breaks apart in mid-air before touching the floor; or it bounces off the tile whole and unbroken; or it squashes flat and stays in one soft piece.
- P3 [major · gravity_direction]
  - expect: The fragments stay low, skittering and sliding along the tile before coming to rest.
  - fail: The fragments fly upward and stay up; or a fragment rises and never comes back down; or the pieces float above the tile.
- P4 [major · missing_consequence]
  - expect: The breaking happens at the moment of contact with the floor, and the pieces are the plate's.
  - fail: The plate lands whole and stays whole while pieces appear beside it; or fragments scatter across the floor before the plate arrives; or the plate is gone from the floor and no pieces are left.
- P5 [fatal · permanence_count]
  - expect: One plate falls and nothing passes through the counter or the floor.
  - fail: A second plate appears during the fall; or the plate passes through the tiled floor; or the plate turns into another object on the way down.
- P6 [minor · attribute_drift]
  - expect: The plate's colour and pattern, the counter and the room stay the same.
  - fail: The plate changes colour or pattern as it falls; or the counter changes height between frames; or the room behind rearranges.

## MECH-0024 · gravity_fall · train

**Caption.** A tennis ball is tossed straight up in a backyard and comes back down to the same spot.

**Expectation (hidden).** The ball slows as it rises, pauses for an instant at the top, and descends along nearly the same line, speeding up as it falls.

**Declared violation types.** gravity_direction, trajectory_momentum

**SA**
- S1 [core] A tennis ball is tossed straight up in a backyard.
- S2 [core] It rises and then comes back down.
- S3 [core] It comes down to the spot it went up from.
- S4 [minor] The toss goes straight up rather than off to one side.
- S5 [minor] The rise comes first and the fall follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The ball slows as it rises, hangs for an instant at the top, and falls quicker and quicker on the way back down.
  - fail: The ball climbs at an unchanging speed all the way to the top; or it stays at the top instead of coming back; or it goes quicker the higher it rises.
- P2 [core · trajectory_momentum]
  - expect: It comes down along nearly the line it went up and lands near the spot it left.
  - fail: The ball comes down well away from where it went up with nothing pushing it aside; or it curves off to one side in the open air; or it keeps rising out of the frame and never returns.
- P3 [major · causeless_motion]
  - expect: Once in the air nothing but the fall changes the ball's motion.
  - fail: The ball jinks sideways in mid-air with nothing touching it; or it halts in mid-flight and hangs there; or it sets off again after coming to rest on the ground.
- P4 [major · material_response]
  - expect: The ball stays round and firm, squashing only briefly where it lands.
  - fail: The ball stretches as it flies; or it stays flattened after landing; or it wobbles like jelly in the air.
- P5 [fatal · permanence_count]
  - expect: One ball is in the air throughout and it stays above the ground.
  - fail: The ball vanishes at the top of its flight or a second one appears; or it passes through the ground; or it turns into another object in mid-air.
- P6 [minor · attribute_drift]
  - expect: The ball's colour, the yard and the background stay the same.
  - fail: The ball changes colour in flight; or the fence or wall behind changes between frames; or the yard rearranges.

## MECH-0025 · gravity_fall · train

**Caption.** A stack of coins on the corner of a kitchen counter is knocked off by an elbow and the coins scatter on the floor.

**Expectation (hidden).** The coins separate as they fall and land spread around the spot below the counter; the same coins that left the counter arrive on the floor.

**Declared violation types.** gravity_direction, permanence_count

**SA**
- S1 [core] A stack of coins stands on the corner of a kitchen counter.
- S2 [core] An elbow knocks the stack off the counter.
- S3 [core] The coins scatter on the floor.
- S4 [minor] Several coins are involved rather than a single one.
- S5 [minor] The knock comes first and the scattering follows.

**PC**
- P1 [core · permanence_count]
  - expect: The coins that leave the counter are the coins that arrive on the floor, keeping their number.
  - fail: Coins appear on the floor that were never in the stack; or a coin vanishes on the way down; or the stack still stands whole on the counter after the coins have landed.
- P2 [core · gravity_direction]
  - expect: Every coin travels downward from the counter to the floor.
  - fail: A coin rises after being knocked; or a coin hangs in the air beside the counter; or a coin climbs back onto the counter.
- P3 [major · trajectory_momentum]
  - expect: The stack breaks apart as it goes and the coins spread out on the floor below the corner, each spinning or bouncing to rest.
  - fail: The coins fall as one rigid column and land still stacked; or they gather themselves back into a neat stack on the floor; or a coin rebounds higher than the counter it fell from.
- P4 [major · material_response]
  - expect: The coins stay flat rigid discs, ringing and spinning on the floor.
  - fail: A coin bends or folds where it lands; or a coin splashes on the tiles; or a coin sinks into the floor as if into mud.
- P5 [fatal · solidity]
  - expect: The coins, the counter and the floor stay solid and separate.
  - fail: A coin passes through the counter or through the floor; or two coins merge into one; or a coin turns into another object mid-fall.
- P6 [minor · attribute_drift]
  - expect: The coins' colour, the counter and the kitchen stay the same.
  - fail: A coin changes colour or size as it falls; or the counter's surface changes pattern between frames; or the kitchen behind rearranges.

**Note.** The elbow is kept as the minimal trigger for the fall; the person behind it is not judged.

## MECH-0026 · gravity_fall · train

**Caption.** An egg is cracked on the rim of a bowl and the shell pulled apart above it, and the yolk and white drop into the bowl.

**Expectation (hidden).** The contents fall straight down out of the shell as soon as it opens and do not remain suspended between the shell halves.

**Declared violation types.** gravity_direction, material_response

**SA**
- S1 [core] An egg is cracked on the rim of a bowl.
- S2 [core] The shell is pulled apart above the bowl.
- S3 [core] The yolk and white drop into the bowl.
- S4 [minor] The bowl stays below the shell throughout.
- S5 [minor] The crack comes first, then the shell opens, then the contents fall.

**PC**
- P1 [core · gravity_direction]
  - expect: The contents leave the shell downward as soon as it opens and land in the bowl below.
  - fail: The contents stay suspended between the shell halves after the shell is open; or they rise out of the shell; or they drift sideways past the bowl.
- P2 [core · material_response]
  - expect: The white runs as a thick, stringy liquid and the yolk keeps its rounded blob shape until it lands.
  - fail: The contents pour out as thin water; or the yolk breaks apart like a brittle solid before it lands; or the white holds a rigid shape in the air.
- P3 [major · material_response]
  - expect: The shell is brittle: it cracks and comes apart in pieces rather than bending.
  - fail: The shell stretches like rubber as it is pulled apart; or it flows like a liquid; or the crack closes and the shell becomes whole again.
- P4 [major · missing_consequence]
  - expect: What leaves the shell arrives in the bowl: the pool inside grows as the contents land.
  - fail: The contents fall into the bowl and the bowl stays empty; or a pool appears in the bowl before the shell opens; or the shell empties with nothing arriving below.
- P5 [fatal · permanence_count]
  - expect: One egg's contents fall, and nothing passes through the bowl.
  - fail: A second yolk appears; or the contents pass through the bottom of the bowl; or the shell halves merge back into an uncracked egg.
- P6 [minor · attribute_drift]
  - expect: The yolk's colour, the bowl and the worktop stay the same.
  - fail: The yolk changes colour as it falls; or the bowl changes size or pattern between frames; or the worktop behind rearranges.

## MECH-0027 · gravity_fall · train

**Caption.** A skydiver steps out of the open door of an airplane and drops away below it.

**Expectation (hidden).** The skydiver falls faster at first while the plane moves on ahead; the skydiver does not stay level with the door or rise.

**Declared violation types.** gravity_direction, trajectory_momentum

**SA**
- S1 [core] A skydiver stands at the open door of an airplane.
- S2 [core] The skydiver steps out of the door.
- S3 [core] The skydiver drops away below the plane.
- S4 [minor] The step out comes first and the drop follows.

**PC**
- P1 [core · gravity_direction]
  - expect: Once out of the door the skydiver goes downward and falls quicker as the gap to the plane opens.
  - fail: The skydiver rises above the plane after stepping out; or hangs level with the door; or sinks at one unchanging slow drift as if being lowered on a line.
- P2 [core · trajectory_momentum]
  - expect: The plane flies on ahead while the skydiver falls behind and below it, so the gap grows in both directions.
  - fail: The skydiver stays beside the door while the plane flies on; or the skydiver moves out ahead of the plane; or the plane stops in the air alongside the skydiver.
- P3 [major · causeless_motion]
  - expect: The skydiver is carried only by the fall and the rushing air; nothing lifts or shoves the body.
  - fail: The skydiver stops falling in mid-air and hangs; or the body shoots sideways with nothing touching it; or the skydiver climbs back up toward the door.
- P4 [major · material_response]
  - expect: The skydiver's clothing and straps flap and stream in the rush of air.
  - fail: The clothing hangs still as if in calm air; or it streams downward against the airflow; or it stays stiff like sheet metal.
- P5 [fatal · shape_identity]
  - expect: One skydiver and one airplane keep their number and shape, and neither passes through the other.
  - fail: A limb detaches or vanishes; or the skydiver passes through the fuselage; or a second figure appears from nowhere in the doorway.
- P6 [minor · attribute_drift]
  - expect: The skydiver's suit, the airplane and the sky stay the same.
  - fail: The suit changes colour during the fall; or the airplane changes shape or markings between frames; or the cloud layer jumps to a different place.

**Note.** Freefall scene: the skydiver's body is what shows the fall. Body position, style and how the parachute is packed are not judged.

## MECH-0028 · gravity_fall · train

**Caption.** A diver stands at the end of a high platform, bends her knees, jumps off, and falls into the pool.

**Expectation (hidden).** She rises briefly then falls faster and faster until she enters the water; she does not slow before entry or hang in the air.

**Declared violation types.** gravity_direction, trajectory_momentum

**SA**
- S1 [core] A diver stands at the end of a high platform.
- S2 [core] She bends her knees.
- S3 [core] She jumps off.
- S4 [core] She falls into the pool.
- S5 [minor] The pool is visible below the platform.
- S6 [minor] The knee bend comes first, then the jump, then the fall.

**PC**
- P1 [core · gravity_direction]
  - expect: She rises briefly off the platform and then falls quicker and quicker toward the water.
  - fail: She slows down on the way to the water; or she hangs in the air below the platform; or she keeps rising from the platform to the top of the frame.
- P2 [core · trajectory_momentum]
  - expect: The jump carries her out from the platform, her path curves over into the fall, and she comes down clear of the platform.
  - fail: She drops straight down against the face of the platform after plainly jumping outward; or she travels backward over the platform in mid-air; or she moves further out the lower she gets, as if pushed.
- P3 [major · causeless_motion]
  - expect: Once she leaves the platform nothing but the fall changes her course.
  - fail: She changes direction in mid-air with nothing touching her; or she stops in mid-fall and hangs there; or she gathers speed upward.
- P4 [major · missing_consequence] (if: She reaches the water within the clip.)
  - expect: Where she enters the water it splashes up and rings spread out from the entry point.
  - fail: She enters the water and the surface stays flat; or the splash rises before she reaches the surface; or she passes into the water leaving no ripple at all.
- P5 [fatal · shape_identity]
  - expect: One diver keeps her limbs, her number and her shape, and she does not pass into the platform.
  - fail: A limb stretches, detaches or vanishes; or she passes through the platform; or a second figure appears on the platform.
- P6 [minor · attribute_drift]
  - expect: Her swimsuit, the platform and the pool surroundings stay the same.
  - fail: Her swimsuit changes colour in mid-air; or the platform changes shape between frames; or the stands behind the pool rearrange.

**Note.** Biomechanics scene: the diver's body is what shows the fall. Technique, form and entry style are not judged; only the direction and order of the motion.

## MECH-0029 · gravity_fall · train

**Caption.** A water balloon is dropped from a second-floor balcony, and it falls straight down and bursts on the pavement.

**Expectation (hidden).** The balloon starts falling the moment it is released, drops straight down and gets faster as it goes, and does not drift sideways, slow, or hover; it bursts only when it hits the pavement, and the water spreads out on the ground and stays there.

**Declared violation types.** gravity_direction, missing_consequence, permanence_count

**SA**
- S1 [core] A water balloon is dropped from a second-floor balcony.
- S2 [core] It falls straight down.
- S3 [core] It bursts on the pavement.
- S4 [minor] The balcony and the pavement below are both visible.
- S5 [minor] The release comes first, then the fall, then the burst.

**PC**
- P1 [core · gravity_direction]
  - expect: The balloon starts to fall at the release, drops along a line below the balcony, and falls quicker the further it goes.
  - fail: The balloon drifts sideways out from under the balcony; or it slows as it falls; or it hangs in the air below the balcony.
- P2 [core · missing_consequence]
  - expect: It bursts where it meets the pavement and not before; the water spreads out on the ground and stays there.
  - fail: The balloon bursts in mid-air before touching the pavement; or it hits the pavement and bounces away still whole; or the water lands and leaves the pavement dry.
- P3 [major · permanence_count]
  - expect: One balloon goes down and the water on the ground is the water it carried.
  - fail: A second balloon appears during the fall; or the balloon vanishes before reaching the pavement; or a wet patch spreads on the ground before the balloon lands.
- P4 [major · material_response]
  - expect: The balloon bulges and wobbles as a bag of liquid on the way down and its skin tears open on impact.
  - fail: The balloon stays a rigid ball through the fall and the impact; or it squashes and springs back whole off the pavement; or it shrinks slowly as if leaking air instead of bursting.
- P5 [fatal · solidity]
  - expect: The balloon, the balcony and the pavement stay solid.
  - fail: The balloon passes through the pavement; or it passes through the balcony rail on the way down; or it merges into the wall of the building.
- P6 [minor · attribute_drift]
  - expect: The balloon's colour, the balcony and the pavement stay the same.
  - fail: The balloon changes colour during the fall; or the balcony railing changes pattern between frames; or the pavement's paving changes layout.

## MECH-0030 · gravity_fall · train

**Caption.** A button on a vending machine is pressed, and a can drops inside the machine and lands in the tray at the bottom.

**Expectation (hidden).** The can starts to fall only after the button is pressed, drops straight down behind the glass without pausing or drifting sideways, and comes to rest in the tray; one can leaves the shelf and the same one arrives below, with no can appearing from nowhere, vanishing on the way, or rising back up.

**Declared violation types.** gravity_direction, permanence_count, missing_consequence

**SA**
- S1 [core] A button on a vending machine is pressed.
- S2 [core] A can drops inside the machine.
- S3 [core] It lands in the tray at the bottom.
- S4 [minor] The can is visible behind the glass as it falls.
- S5 [minor] The press comes first and the drop follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The can starts to fall after the button is pressed and not before.
  - fail: A can drops with no button being pressed; or the button is pressed and nothing in the machine moves; or the can is already lying in the tray before the press.
- P2 [core · gravity_direction]
  - expect: The can drops downward inside the machine, quicker as it falls, and comes to rest in the tray.
  - fail: The can drifts sideways across the shelves as it falls; or it hangs in the air inside the machine; or it climbs back up to its shelf.
- P3 [major · permanence_count]
  - expect: One can leaves the shelf and the same one arrives in the tray.
  - fail: A second can appears during the fall; or the can vanishes on the way down; or the shelf still holds its full row after a can has dropped.
- P4 [major · material_response]
  - expect: The can stays a rigid cylinder and clatters against the glass and the tray.
  - fail: The can bends or crumples as it falls; or it bounces around the tray like a rubber ball without settling; or it sinks into the floor of the tray.
- P5 [fatal · solidity]
  - expect: The can, the glass and the machine's shelves stay solid and separate.
  - fail: The can passes through the glass front; or it passes through the shelf below it; or it merges with another can in the rack.
- P6 [minor · attribute_drift]
  - expect: The can's label, the machine's front and the room stay the same.
  - fail: The can changes label or colour as it falls; or the machine's buttons rearrange between frames; or the room behind the machine changes.

## MECH-0031 · gravity_fall · train

**Caption.** A picture frame hanging on a wall comes loose from its nail and falls to the floor.

**Expectation (hidden).** The frame slides or tips off the nail and drops down along the wall; it does not stay on the wall with nothing holding it or drift outward.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] A picture frame hangs on a wall from a nail.
- S2 [core] It comes loose from the nail.
- S3 [core] It falls to the floor.
- S4 [minor] The frame comes loose first and the fall follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The frame hangs as long as the nail holds it and starts to move only once it is free of the nail.
  - fail: The frame falls while still hooked over the nail; or its wire leaves the nail and the frame stays hanging in place; or the frame slides down the wall with the nail still through its wire.
- P2 [core · gravity_direction]
  - expect: Once free the frame drops down along the wall and reaches the floor.
  - fail: The frame drifts outward away from the wall as it falls; or it stops in the air part way down; or it rises up the wall.
- P3 [major · trajectory_momentum]
  - expect: It tips or slews as it comes off, turns as it drops, and ends lying or leaning at the foot of the wall.
  - fail: The frame stays perfectly level all the way down and lands standing upright; or it swings back up the wall after hitting the floor; or it rebounds higher than the nail it fell from.
- P4 [major · material_response]
  - expect: The frame stays rigid as it lands and the wall stays solid where it brushes past.
  - fail: The frame bends like cloth as it falls; or it bounces off the floor like a ball and stays up in the air; or the wall dents inward where the frame touches it.
- P5 [fatal · permanence_count]
  - expect: One frame on one nail keeps its shape and passes through nothing.
  - fail: The frame vanishes on the way down or a second one appears; or the frame passes through the wall or the floor; or it turns into another object as it falls.
- P6 [minor · attribute_drift]
  - expect: The picture inside the frame, the wall and the room stay the same.
  - fail: The picture inside changes to a different image; or the wall changes colour; or the furniture in the room rearranges between frames.

## MECH-0033 · collision · train

**Caption.** A bowling ball reaches the end of the lane, hits the front pin of a full rack, and the pins fly and scatter.

**Expectation (hidden).** Pins move only after being struck by the ball or another pin, fly back and sideways, and the ball continues into the pit slowed; no pin is passed through.

**Declared violation types.** trajectory_momentum, missing_consequence, solidity

**SA**
- S1 [core] A bowling ball reaches the end of a lane where a full rack of pins stands.
- S2 [core] The ball hits the front pin.
- S3 [core] The pins fly and scatter.
- S4 [minor] The rack is standing full before the ball arrives.
- S5 [minor] The ball reaches the pins first and the scattering follows.

**PC**
- P1 [core · missing_consequence]
  - expect: Each pin moves only after the ball or another pin strikes it, so the disturbance spreads outward from the front pin.
  - fail: Pins topple before the ball reaches them; or the ball reaches the front pin and the rack stands unmoved; or pins at the back fall while the front pin is still standing untouched.
- P2 [core · trajectory_momentum]
  - expect: Struck pins are driven back and out to the sides, away from the ball's line, and the ball carries on into the pit more slowly than it arrived.
  - fail: Pins fly back up the lane toward the bowler, against the ball; or the ball holds its speed unchanged through the rack; or all the pins move off together as one rigid block.
- P3 [major · solidity]
  - expect: The ball and the pins meet solidly and stay outside one another and above the lane.
  - fail: The ball passes through a pin without moving it; or two pins pass through each other; or a pin passes through the lane surface or the back wall.
- P4 [major · gravity_direction]
  - expect: Pins thrown up come back down onto the lane and end lying on it.
  - fail: A pin rises and stays up in the air; or a pin hangs above the lane after being struck; or a pin drifts upward out of the frame.
- P5 [fatal · permanence_count]
  - expect: The pins that stood in the rack are the pins that scatter, and the ball stays one ball.
  - fail: A pin vanishes as it is struck; or extra pins appear during the scatter; or a pin turns into another object.
- P6 [minor · attribute_drift]
  - expect: The ball's colour, the pins' markings and the lane stay the same.
  - fail: The ball changes colour at the impact; or the pins change their stripes between frames; or the back wall of the pit changes.

## MECH-0034 · collision · train

**Caption.** Two bumper cars at a fairground drive straight at each other, meet head-on, and both cars bounce back a little.

**Expectation (hidden).** Both cars stop or rebound at the moment of contact; neither car passes through the other.

**Declared violation types.** trajectory_momentum, causeless_motion

**SA**
- S1 [core] Two bumper cars are being driven at a fairground.
- S2 [core] They drive straight at each other.
- S3 [core] They meet head-on.
- S4 [core] Both cars bounce back a little.
- S5 [minor] Both cars rebound rather than only one.
- S6 [minor] The approach comes first, then the contact, then the rebound.

**PC**
- P1 [core · trajectory_momentum]
  - expect: At the contact both cars stop or reverse, each moving back along the line it came in on.
  - fail: The cars carry on at their old speed through the contact; or only one car is affected while the other drives on unchanged; or both move off together in one direction after a head-on meeting.
- P2 [core · causeless_motion]
  - expect: Each car changes its motion at the moment the bumpers touch and not before.
  - fail: A car bounces back before the bumpers touch; or a car is thrown back with the other never reaching it; or a car stops short of contact and the other rebounds anyway.
- P3 [major · solidity]
  - expect: The two cars meet at their bumpers and stay outside one another.
  - fail: One car passes through the other; or the bumpers overlap and the bodies run into each other; or a car passes through the floor of the rink.
- P4 [major · material_response]
  - expect: The rubber bumpers squash briefly at the contact and spring back, and the shells stay rigid.
  - fail: A bumper stays dented after the contact; or a car body crumples like paper; or the cars stick together at the bumpers and travel on as one.
- P5 [fatal · permanence_count]
  - expect: Two cars and their riders keep their number and shape.
  - fail: A car vanishes at the contact or a third appears; or a car turns into another vehicle; or a rider comes away from a car and stays sitting in mid-air.
- P6 [minor · attribute_drift]
  - expect: The cars' colours, the rink floor and the fairground behind stay the same.
  - fail: A car changes colour at the contact; or the rink's markings shift between frames; or the fairground behind rearranges.

## MECH-0035 · collision · train

**Caption.** A tennis ball is thrown hard against a brick wall and bounces back the way it came.

**Expectation (hidden).** The ball flattens briefly at the wall and rebounds somewhat slower than it arrived; it does not stick, pause on the wall, or pass into it.

**Declared violation types.** trajectory_momentum, solidity

**SA**
- S1 [core] A tennis ball is thrown hard at a brick wall.
- S2 [core] It strikes the wall.
- S3 [core] It bounces back the way it came.
- S4 [minor] The wall is brick.
- S5 [minor] The throw and the strike come first, then the rebound.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The ball leaves the wall back along its incoming line and travels slower than it arrived.
  - fail: The ball leaves the wall quicker than it arrived; or it drops straight down at the wall without coming back; or it carries on sideways along the face of the wall.
- P2 [core · solidity]
  - expect: The ball meets the face of the wall and stays outside it.
  - fail: The ball passes into the brickwork; or it sinks part way in and then comes back out; or it sticks to the wall and hangs there.
- P3 [major · material_response]
  - expect: The ball squashes briefly where it meets the brick and springs back round, and the wall is unmarked.
  - fail: The ball stays flattened after the bounce; or it splatters like a wet lump against the brick; or the wall dents or bulges where the ball hits it.
- P4 [major · gravity_direction]
  - expect: After the rebound the ball's path bends downward toward the ground.
  - fail: The ball climbs steadily after the bounce and keeps climbing; or it holds one flat line away from the wall to the edge of the frame; or it hangs in the air after the rebound.
- P5 [fatal · permanence_count]
  - expect: One ball and one wall are there throughout.
  - fail: The ball vanishes at the wall or a second one appears; or the ball turns into another object at the bounce; or a piece of the wall disappears where the ball strikes.
- P6 [minor · attribute_drift]
  - expect: The ball's colour, the brick pattern and the surroundings stay the same.
  - fail: The ball changes colour at the bounce; or the brick courses shift between frames; or the scene beside the wall rearranges.

## MECH-0036 · collision · train

**Caption.** A shopping cart rolls across a parking lot, runs into a concrete curb, and stops abruptly.

**Expectation (hidden).** The cart stops at the curb with its front wheels jammed against it and may tip forward slightly; it does not roll through or over the curb.

**Declared violation types.** trajectory_momentum, missing_consequence

**SA**
- S1 [core] A shopping cart rolls across a parking lot.
- S2 [core] It runs into a concrete curb.
- S3 [core] It stops abruptly at the curb.
- S4 [minor] The concrete curb in the cart's path is visible.
- S5 [minor] The rolling comes first and the stop at the curb follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The cart's stop happens where its wheels meet the curb, not anywhere else.
  - fail: The cart stops on open tarmac before reaching the curb; or it reaches the curb and rolls on unaffected; or it stops with no curb or obstacle in its path.
- P2 [core · trajectory_momentum]
  - expect: The wheels are checked at the curb while the basket carries on, so the cart jolts and may tip forward before settling back.
  - fail: The cart comes to rest at the curb with no jolt or tip at all; or it bounces back from the curb quicker than it arrived; or it keeps rolling forward at its old speed after the contact.
- P3 [major · solidity]
  - expect: The cart stays on its side of the curb and above the tarmac.
  - fail: The cart's wheels pass through the concrete curb; or the cart sinks into the tarmac at the stop; or the basket passes through the curb while the wheels stay behind it.
- P4 [major · trajectory_momentum] (if: Items are visible in the cart's basket.)
  - expect: Items in the basket pitch forward at the moment the cart is stopped.
  - fail: Items in the basket stay still while the cart jolts to a halt; or they pitch backward; or they move before the cart reaches the curb.
- P5 [fatal · permanence_count]
  - expect: One cart and one curb keep their number and shape.
  - fail: The cart vanishes at the curb or a second one appears; or a wheel comes away and hangs in the air; or the curb disappears where the cart meets it.
- P6 [minor · attribute_drift]
  - expect: The cart's colour, the lot markings and the background stay the same.
  - fail: The cart changes colour at the impact; or the painted bay lines shift between frames; or the buildings behind rearrange.

## MECH-0037 · collision · train

**Caption.** A finger tips over the first domino in a long row standing on a table, and the whole row falls one after another.

**Expectation (hidden).** Each domino falls only after the previous one strikes it, the wave running steadily down the row; none fall early and none stand back up.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A long row of dominoes stands on a table.
- S2 [core] A finger tips over the first domino.
- S3 [core] The whole row falls one after another.
- S4 [minor] Only the first domino is touched by the finger.
- S5 [minor] The finger's push comes first and the rest fall in turn.

**PC**
- P1 [core · missing_consequence]
  - expect: Each domino starts to fall only after the one before it strikes it.
  - fail: A domino falls before the one behind it reaches it; or a domino is struck and stays standing while the wave carries on past it; or dominoes further down the row fall while the ones before them still stand.
- P2 [core · process_direction]
  - expect: The wave runs steadily from the pushed end toward the far end and does not turn back; fallen dominoes stay down.
  - fail: The wave reverses and runs back up the row; or a fallen domino stands itself up again; or the row falls from the far end back toward the finger.
- P3 [major · trajectory_momentum]
  - expect: Each domino topples the way the wave is travelling, landing on the next one or on the table.
  - fail: A domino topples backward against the wave; or one is flung clear off the table by the touch of its neighbour; or one spins on the spot instead of toppling.
- P4 [major · material_response]
  - expect: The dominoes stay rigid tiles that clack and slide a little, and the table stays flat under them.
  - fail: A domino bends as it falls; or a domino bounces high off the table; or the table surface ripples as the wave passes along it.
- P5 [fatal · permanence_count]
  - expect: The dominoes keep their number and stay on top of the table.
  - fail: A domino vanishes as it falls or a new one appears in the row; or a domino passes through the one beside it; or a domino sinks into the table.
- P6 [minor · attribute_drift]
  - expect: The dominoes' colour and spots, the table and the room stay the same.
  - fail: A domino changes colour or its spots as it falls; or the table's surface changes pattern between frames; or the room behind rearranges.

**Note.** The finger is kept as the minimal trigger for the first domino; the hand behind it is not judged.

## MECH-0038 · collision · train

**Caption.** A car in a parking lot rolls slowly forward, bumps into the back of a parked car, and stops.

**Expectation (hidden).** The rolling car stops at the bumper and the parked car rocks or is nudged forward a little; neither car deforms much at this speed and neither passes into the other.

**Declared violation types.** trajectory_momentum, material_response

**SA**
- S1 [core] A car rolls slowly forward in a parking lot.
- S2 [core] It bumps into the back of a parked car.
- S3 [core] It stops at the contact.
- S4 [minor] The other car is parked and still before the bump.
- S5 [minor] The roll comes first and the bump and stop follow.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The rolling car stops at the bumper it meets, and the parked car rocks or is nudged forward at that same moment.
  - fail: The rolling car stops short of the parked car and the parked car rocks anyway; or the parked car moves before the contact; or the rolling car holds its speed through the contact.
- P2 [core · material_response]
  - expect: At this rolling pace the bumpers meet with little damage and both bodies keep their shape.
  - fail: Either car crumples deeply at the contact; or a bumper stretches like rubber; or a car body folds up as though struck at speed.
- P3 [major · solidity]
  - expect: The two cars stay outside one another and above the tarmac.
  - fail: The rolling car passes into the parked car's body; or the bumpers overlap and the panels run into each other; or a car sinks into the tarmac at the contact.
- P4 [major · causeless_motion]
  - expect: The parked car stays still until it is struck and settles again afterwards.
  - fail: The parked car rolls away before anything touches it; or it keeps rolling away after the light nudge without slowing; or it moves backward into the rolling car.
- P5 [fatal · permanence_count]
  - expect: Two cars keep their number and shape through the bump.
  - fail: A car vanishes at the contact or a third appears; or a car turns into a different model; or a wheel comes away and hangs in mid-air.
- P6 [minor · attribute_drift]
  - expect: The cars' colours, the lot markings and the background stay the same.
  - fail: A car changes colour at the contact; or the bay lines shift between frames; or the cars parked further off rearrange.

## MECH-0039 · collision · train

**Caption.** A dodgeball thrown hard hits a heavy punching bag hanging in a gym, bounces off it, and drops to the floor.

**Expectation (hidden).** The bag swings back at the moment of impact; the ball rebounds and falls nearby, not passing through the bag or sticking to it.

**Declared violation types.** trajectory_momentum, causeless_motion

**SA**
- S1 [core] A dodgeball is thrown hard at a punching bag hanging in a gym.
- S2 [core] The ball hits the bag.
- S3 [core] It bounces off the bag.
- S4 [core] It drops to the floor.
- S5 [minor] The bag hangs from above rather than standing on the floor.
- S6 [minor] The hit comes first, then the bounce, then the drop.

**PC**
- P1 [core · missing_consequence]
  - expect: The bag gives at the impact: it dents shallowly and swings back where the ball struck it.
  - fail: The bag stays still while the ball plainly strikes it; or the ball rebounds off a bag that never moves at all; or the ball buries itself in the bag with no swing following.
- P2 [core · trajectory_momentum]
  - expect: The ball rebounds back off the bag more slowly than it arrived, and its path then bends down toward the floor.
  - fail: The ball rebounds quicker than it arrived; or it sticks to the bag and hangs there; or it carries on past the bag and out the other side.
- P3 [major · causeless_motion]
  - expect: Nothing moves before the ball arrives; the bag's swing dies away afterwards and the ball stays put once it has settled.
  - fail: The bag swings before the ball reaches it; or the bag swings wider and wider after the single hit; or the ball sets off again across the floor with nothing touching it.
- P4 [major · gravity_direction]
  - expect: After the rebound the ball falls to the floor and settles near the bag.
  - fail: The ball hangs in the air after the rebound; or it climbs steadily after the bounce and keeps climbing; or it travels along in mid-air without ever reaching the floor.
- P5 [major · material_response]
  - expect: The bag is heavy and stiff, swinging as one mass, while the ball squashes briefly and springs back round.
  - fail: The bag folds around the ball and holds that shape; or the bag flies off like a light empty sack at the hit; or the ball stays flattened after the bounce.
- P6 [fatal · solidity]
  - expect: The ball, the bag and its chain stay solid and keep their number.
  - fail: The ball passes through the bag; or the bag passes through the floor; or the ball vanishes at the contact or a second one appears.
- P7 [minor · attribute_drift]
  - expect: The ball's colour, the bag's covering and the gym stay the same.
  - fail: The ball changes colour at the impact; or the bag changes colour or markings between frames; or the gym behind rearranges.

## MECH-0040 · collision · train

**Caption.** A hockey puck slides along the ice, hits the metal goalpost, and deflects off at an angle.

**Expectation (hidden).** The deflection happens at contact and the puck continues sliding in its new direction; the post stays fixed.

**Declared violation types.** trajectory_momentum, solidity

**SA**
- S1 [core] A hockey puck slides along the ice.
- S2 [core] It hits the metal goalpost.
- S3 [core] It deflects off at an angle and slides on.
- S4 [minor] The goalpost is visible where the puck meets it.
- S5 [minor] The slide comes first and the deflection follows.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The puck turns at the post, leaving on a new line away from it, a little slower than it arrived.
  - fail: The puck changes direction before it reaches the post; or it leaves the post quicker than it arrived; or it carries on straight past the post's line unchanged.
- P2 [core · solidity]
  - expect: The puck stays outside the post and the post stays fixed where it stands.
  - fail: The puck passes through the goalpost; or it sinks into the post and comes out the other side; or the post drifts away across the ice with nothing else touching it.
- P3 [major · gravity_direction]
  - expect: The puck stays flat on the ice through the contact and afterwards.
  - fail: The puck lifts off the ice and stays in the air after the deflection; or it hovers above the surface as it slides; or it sinks into the ice.
- P4 [major · material_response]
  - expect: The puck stays a hard rigid disc and the post stays rigid metal at the contact.
  - fail: The puck squashes or bends at the post; or the post bends and stays bent; or the puck sticks to the post.
- P5 [fatal · permanence_count]
  - expect: One puck and one goal frame are there throughout.
  - fail: The puck vanishes at the post or a second one appears; or the puck turns into another object at the deflection; or part of the goal frame disappears.
- P6 [minor · attribute_drift]
  - expect: The puck's colour, the goal's paint and the ice markings stay the same.
  - fail: The puck changes colour at the contact; or the goal frame changes colour between frames; or the lines painted in the ice shift.

## MECH-0041 · collision · train

**Caption.** A toy train runs along a track, hits a wooden block lying across the rails, and stops.

**Expectation (hidden).** The train stops or derails at the block and may push it a little; it does not pass through the block or stop before reaching it.

**Declared violation types.** trajectory_momentum, missing_consequence

**SA**
- S1 [core] A toy train runs along a track.
- S2 [core] A wooden block lies across the rails in its path and the train reaches it.
- S3 [core] The train stops at the block.
- S4 [minor] The block lies across the rails rather than beside them.
- S5 [minor] The train runs first and the stop at the block follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The train is stopped where it meets the block, and the block may be shoved along a little.
  - fail: The train stops before it reaches the block; or it runs over the block and carries on unaffected; or the block flies away before the train touches it.
- P2 [core · trajectory_momentum]
  - expect: The train is checked at the block: it halts there or comes off the rails, rather than carrying on at its old speed.
  - fail: The train carries on at the same speed after meeting the block; or it is thrown back up the track quicker than it came; or it stops and then sets off again on its own.
- P3 [major · solidity]
  - expect: The train, the block and the rails stay solid and separate.
  - fail: The train passes through the block; or the block passes through the rails; or a wheel passes through the track.
- P4 [major · material_response]
  - expect: The train and the wooden block stay rigid at the contact, the block sliding or tipping rather than folding.
  - fail: The block bends or squashes where the train hits it; or the train's body crumples; or the block flows out of the way like a liquid.
- P5 [fatal · permanence_count]
  - expect: One train and one block are there throughout.
  - fail: The block vanishes as the train reaches it; or a second block appears on the rails; or a carriage disappears from the train.
- P6 [minor · attribute_drift]
  - expect: The train's livery, the block and the track stay the same.
  - fail: The train changes colour at the stop; or the block changes size or colour between frames; or the track's layout changes.

## MECH-0042 · collision · train

**Caption.** A putted golf ball rolls across the green, hits the back of the cup's rim, pops up, and drops into the hole.

**Expectation (hidden).** The pop-up happens at the rim, the ball falls back into the hole under gravity, and it does not continue rolling as if the hole were not there.

**Declared violation types.** trajectory_momentum, gravity_direction

**SA**
- S1 [core] A putted golf ball rolls across a green.
- S2 [core] It hits the back of the cup's rim.
- S3 [core] It pops up.
- S4 [core] It drops into the hole.
- S5 [minor] It strikes the far side of the rim rather than dropping straight in.
- S6 [minor] The roll comes first, then the rim, then the pop up, then the drop in.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The hop begins where the ball meets the far rim, and it is a short hop rather than a long flight.
  - fail: The ball pops up before it reaches the cup; or it is flung high across the green at the rim; or it rolls over the hole with no change of motion at all.
- P2 [core · gravity_direction]
  - expect: After the hop the ball falls back down and drops below the level of the green into the hole.
  - fail: The ball hangs above the cup after the hop; or it rises away from the hole and keeps rising; or it settles on top of the hole as if the opening were solid ground.
- P3 [major · solidity]
  - expect: The ball enters the cup through its opening; the turf and the rim stay solid.
  - fail: The ball passes through the turf beside the hole; or it sinks into the green where there is no hole; or it passes through the edge of the rim rather than over it.
- P4 [major · material_response]
  - expect: The ball stays a hard sphere and the turf and the rim stay firm where it touches them.
  - fail: The ball squashes at the rim and stays squashed; or the turf ripples like cloth as the ball rolls over it; or the rim bends where the ball strikes it.
- P5 [fatal · permanence_count]
  - expect: One ball and one hole are there throughout.
  - fail: The ball vanishes before reaching the cup or a second one appears; or a second hole appears on the green; or the ball turns into another object.
- P6 [minor · attribute_drift]
  - expect: The ball's colour, the flag and the green stay the same.
  - fail: The ball changes colour as it rolls; or the hole moves to a different part of the green between frames; or the surroundings of the green rearrange.

## MECH-0043 · collision · train

**Caption.** A curling stone glides down the ice, strikes another stone sitting in the house, and knocks it away while itself slowing to a stop.

**Expectation (hidden).** The struck stone moves off at contact in roughly the direction of the hit; the moving stone loses most of its speed; the stones do not overlap.

**Declared violation types.** trajectory_momentum, missing_consequence

**SA**
- S1 [core] A curling stone glides down the ice.
- S2 [core] It strikes another stone sitting in the house.
- S3 [core] The struck stone is knocked away.
- S4 [core] The striking stone slows to a stop.
- S5 [minor] The target stone is still before the contact.
- S6 [minor] The glide comes first, then the contact, then the two stones' outcomes.

**PC**
- P1 [core · missing_consequence]
  - expect: The resting stone starts moving at the moment the gliding stone reaches it, and only then.
  - fail: The resting stone moves before the gliding stone arrives; or the stones touch and the resting stone stays put; or the gliding stone stops short and the other moves away anyway.
- P2 [core · trajectory_momentum]
  - expect: The struck stone leaves roughly along the line of the hit while the striking stone loses most of its speed.
  - fail: The struck stone moves off back toward the thrower; or the striking stone keeps its speed through the contact; or both stones travel on together side by side at the same speed.
- P3 [major · solidity]
  - expect: The two stones meet at their edges and stay outside one another and on top of the ice.
  - fail: The stones overlap or pass through each other; or one rides up over the other and keeps going; or a stone sinks into the ice.
- P4 [major · causeless_motion]
  - expect: On the ice each stone slides along its own line, curling only gradually and slowing steadily; a stone at rest stays at rest until it is struck.
  - fail: A stone turns sharply on the open ice with nothing touching it; or a stone gathers speed as it slides; or a stone that has come to rest sets off again untouched.
- P5 [fatal · permanence_count]
  - expect: The stones keep their number and shape on the sheet.
  - fail: A stone vanishes at the contact or a third appears; or a stone's handle comes away and floats; or a stone turns into another object.
- P6 [minor · attribute_drift]
  - expect: The stones' handles, the painted house and the ice stay the same.
  - fail: A stone's handle changes colour at the contact; or the rings of the house shift between frames; or the markings on the sheet change.

## MECH-0044 · collision · train

**Caption.** Two rubber balls rolled toward each other across a gym floor meet off-centre and glance away from each other in new directions.

**Expectation (hidden).** Both balls change direction at the instant of contact and move apart, each slower than before; they do not pass through each other, stick together, or change course before they touch.

**Declared violation types.** solidity, trajectory_momentum

**SA**
- S1 [core] Two rubber balls roll toward each other across a gym floor.
- S2 [core] They meet off-centre.
- S3 [core] They glance away from each other in new directions.
- S4 [minor] Both balls change direction, not just one.
- S5 [minor] The approach comes first and the change of direction follows.

**PC**
- P1 [core · trajectory_momentum]
  - expect: Both balls change direction at the instant they touch, move apart from the point of contact, and each is slower than before.
  - fail: A ball changes course before the two touch; or the balls touch and both carry on in their old directions; or a ball leaves the contact quicker than it arrived.
- P2 [core · solidity]
  - expect: The balls meet at their surfaces and stay outside each other.
  - fail: The balls pass through each other; or they overlap and come out the other side; or they merge into a single ball at the contact.
- P3 [major · trajectory_momentum]
  - expect: After an off-centre meeting the two leave on different lines and spread apart.
  - fail: The balls stick together and roll on as a pair; or both leave along exactly the line one of them came in on; or each comes straight back the way it came after a glancing touch.
- P4 [major · causeless_motion]
  - expect: On the open floor each ball rolls in a straight line and slows gradually.
  - fail: A ball curves on the open floor with nothing touching it; or a ball gathers speed as it rolls; or a stopped ball sets off again untouched.
- P5 [fatal · permanence_count]
  - expect: Two balls stay two balls on the floor.
  - fail: A ball vanishes at the contact or a third appears; or a ball passes through the floor; or a ball turns into another object.
- P6 [minor · attribute_drift]
  - expect: The balls' colours, the gym floor and the markings stay the same.
  - fail: A ball changes colour at the contact; or the two balls swap colours; or the floor markings shift between frames.

## MECH-0045 · collision · train

**Caption.** A soccer ball rolled at a slant into a low garden wall bounces off at a slant the other way and rolls on across the lawn.

**Expectation (hidden).** The change of direction happens at the wall and mirrors the angle the ball came in at; the ball keeps rolling after contact, a little slower; it does not stop dead at the wall, pass into it, or come straight back.

**Declared violation types.** trajectory_momentum

**SA**
- S1 [core] A soccer ball rolls at a slant toward a low garden wall.
- S2 [core] It bounces off the wall.
- S3 [core] It rolls on across the lawn in a new direction.
- S4 [minor] The approach is at a slant rather than square to the wall.
- S5 [minor] The approach comes first and the bounce follows.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The ball leaves the wall on the opposite slant, turned away from the wall face, and rolls on a little slower than it arrived.
  - fail: The ball comes straight back along the line it arrived on after a slanting approach; or it stops dead at the wall; or it leaves the wall quicker than it arrived.
- P2 [core · solidity]
  - expect: The ball stays outside the wall and turns at its face.
  - fail: The ball passes into the stone of the wall; or it sinks part way in before coming back out; or it passes through to the other side of the wall.
- P3 [major · causeless_motion]
  - expect: The change of direction happens where the ball meets the wall and nowhere else.
  - fail: The ball turns away before it reaches the wall; or it turns again out on the open lawn with nothing touching it; or it stops and sets off again untouched.
- P4 [major · gravity_direction]
  - expect: The ball stays down on the grass, rolling rather than flying, through the bounce and afterwards.
  - fail: The ball lifts off the lawn and travels through the air after the bounce; or it hovers above the grass; or it sinks into the lawn.
- P5 [fatal · permanence_count]
  - expect: One ball and one wall are there throughout.
  - fail: The ball vanishes at the wall or a second one appears; or the ball turns into another object at the bounce; or a section of the wall disappears where the ball strikes it.
- P6 [minor · attribute_drift]
  - expect: The ball's panels, the wall and the garden stay the same.
  - fail: The ball changes colour or pattern at the bounce; or the wall changes height between frames; or the garden behind rearranges.

## MECH-0046 · collision · train

**Caption.** A basketball thrown from the free-throw line hits the front of the rim, bounces up, and falls to the floor.

**Expectation (hidden).** The bounce begins at the rim, the ball goes up or outward and then falls under gravity; it does not hover at the rim or pass through it.

**Declared violation types.** trajectory_momentum, gravity_direction

**SA**
- S1 [core] A basketball is thrown from the free-throw line.
- S2 [core] It hits the front of the rim.
- S3 [core] It bounces up.
- S4 [core] It falls to the floor.
- S5 [minor] It strikes the front of the rim rather than passing through the hoop.
- S6 [minor] The throw comes first, then the rim, then the bounce, then the fall.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The bounce starts where the ball meets the rim and the ball leaves that point upward or outward, slower than it arrived.
  - fail: The ball changes course before it reaches the rim; or it leaves the rim quicker than it arrived; or it carries on past the rim's line unchanged.
- P2 [core · gravity_direction]
  - expect: After the bounce the ball rises, slows, and comes down to the floor.
  - fail: The ball hangs above the rim after the bounce; or it keeps rising out of the frame; or it sinks from the rim at one unchanging slow drift.
- P3 [major · solidity]
  - expect: The ball stays outside the metal of the rim and outside the backboard.
  - fail: The ball passes through the ring of the rim; or it passes through the backboard; or it sinks into the rim and comes out the other side.
- P4 [major · material_response]
  - expect: The ball squashes briefly at the rim and on the floor and springs back round, and the rim stays rigid.
  - fail: The ball stays flattened after a bounce; or the rim bends and stays bent where the ball strikes it; or the ball sticks to the rim.
- P5 [fatal · permanence_count]
  - expect: One ball and one hoop are there throughout.
  - fail: The ball vanishes at the rim or a second one appears; or the ball turns into another object at the bounce; or the rim disappears from the backboard.
- P6 [minor · attribute_drift]
  - expect: The ball's colour and seams, the backboard markings and the court stay the same.
  - fail: The ball changes colour at the bounce; or the square painted on the backboard shifts between frames; or the court behind rearranges.

## MECH-0047 · collision · train

**Caption.** A soccer ball rolled across a paved yard hits an empty plastic bucket standing in its path; the bucket is knocked over and the ball rolls on more slowly.

**Expectation (hidden).** The bucket moves only when the ball reaches it and topples away from the ball; the ball slows at the contact and carries on in roughly the same direction or stops; it does not pass through the bucket, and the bucket does not move before contact.

**Declared violation types.** trajectory_momentum, missing_consequence

**SA**
- S1 [core] A soccer ball rolls across a paved yard.
- S2 [core] An empty plastic bucket stands in its path and the ball reaches it.
- S3 [core] The bucket is knocked over.
- S4 [core] The ball rolls on more slowly.
- S5 [minor] The bucket is empty and standing upright before the contact.
- S6 [minor] The ball arrives first, then the bucket topples.

**PC**
- P1 [core · missing_consequence]
  - expect: The bucket starts to move at the moment the ball reaches it and not before.
  - fail: The bucket topples before the ball arrives; or the ball reaches the bucket and the bucket stays standing; or the ball stops short of the bucket and it falls over anyway.
- P2 [core · trajectory_momentum]
  - expect: The bucket is knocked away from the ball, the way the ball was travelling, and the ball slows at the contact while carrying on roughly the same way or stopping.
  - fail: The bucket topples toward the ball, against its direction of travel; or the ball gathers speed after the contact; or the ball rebounds off the light empty bucket quicker than it arrived.
- P3 [major · solidity]
  - expect: The ball and the bucket stay outside one another and above the paving.
  - fail: The ball passes through the bucket; or the bucket sinks into the paving; or the ball passes through the ground.
- P4 [major · material_response]
  - expect: The empty bucket is light and stiff: it tips, skids and clatters on the paving rather than folding or flying apart.
  - fail: The bucket crumples like paper where the ball hits it; or it breaks into pieces at the contact; or it stays put as though bolted down while the ball bounces off it.
- P5 [fatal · permanence_count]
  - expect: One ball and one bucket are there throughout.
  - fail: The bucket vanishes as it is struck or a second one appears; or the ball vanishes after the contact; or the bucket turns into another object as it topples.
- P6 [minor · attribute_drift]
  - expect: The ball's panels, the bucket's colour and the yard stay the same.
  - fail: The ball changes colour at the contact; or the bucket changes colour or size between frames; or the paving pattern of the yard changes.

## MECH-0049 · friction_rolling · train

**Caption.** A rubber ball rolls across a polished wooden floor onto a thick shaggy rug and comes to a stop on the rug.

**Expectation (hidden).** The ball rolls freely on the wood and slows noticeably only once it reaches the rug; it does not stop on the wood or speed up on the rug.

**Declared violation types.** causeless_motion, trajectory_momentum

**SA**
- S1 [core] A rubber ball rolls across a polished wooden floor.
- S2 [core] It runs onto a thick shaggy rug.
- S3 [core] It comes to a stop on the rug.
- S4 [minor] The change of surface from bare wood to rug is visible.
- S5 [minor] The roll on the wood comes first, then the rug, then the stop.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The ball rolls freely on the wood, and the marked slowing starts where it reaches the rug, ending in a stop a short way onto it.
  - fail: The ball comes to a stop on the bare wood with nothing in its way; or it crosses onto the rug without slowing at all; or it slows on the rug and then rolls on quicker again.
- P2 [core · causeless_motion]
  - expect: The ball keeps a straight line and stays at rest once it has stopped.
  - fail: The ball curves on the open floor with nothing touching it; or it gathers speed on the rug; or it sets off again after coming to rest.
- P3 [major · gravity_direction]
  - expect: The ball stays down on the floor and on top of the rug throughout.
  - fail: The ball lifts off the floor and travels through the air; or it hovers above the pile of the rug; or it sinks into the floorboards.
- P4 [major · material_response]
  - expect: The shaggy pile is pressed down under the ball and springs back, while the ball stays round and firm.
  - fail: The rug's pile stays undisturbed where the ball plainly rolls over it; or the rug ripples like water right across the room; or the ball squashes into the pile and stays flattened.
- P5 [fatal · permanence_count]
  - expect: One ball, one rug and one floor are there throughout.
  - fail: The ball vanishes at the edge of the rug or a second one appears; or the ball passes through the rug to the floor beneath; or the rug turns into another object.
- P6 [minor · attribute_drift]
  - expect: The ball's colour, the rug's pattern and the room stay the same.
  - fail: The ball changes colour as it rolls; or the rug changes pattern or size between frames; or the room behind rearranges.

## MECH-0050 · friction_rolling · train

**Caption.** A car tries to pull away from a snow-covered kerb, its rear wheels spin in place and throw up snow, and the car stays almost where it is.

**Expectation (hidden).** The wheels turn fast while the car creeps forward only a little and never surges ahead as it would on a dry road; the snow is flung backward from the spinning wheels, not forward or upward from nowhere; the car does not move while the wheels are still, and the wheels do not stop spinning while the car keeps gaining speed.

**Declared violation types.** trajectory_momentum, missing_consequence, causeless_motion

**SA**
- S1 [core] A car at a snow-covered kerb tries to pull away.
- S2 [core] Its rear wheels spin in place.
- S3 [core] Snow is thrown up by the spinning wheels.
- S4 [core] The car stays almost where it is.
- S5 [minor] It is the rear wheels that spin.
- S6 [minor] The wheels start spinning first and the snow is thrown up afterwards.

**PC**
- P1 [core · missing_consequence]
  - expect: The wheels turn fast while the car creeps forward at most a little, never surging away as the spin would carry it on dry road.
  - fail: The car surges away at the speed its wheels are turning; or the car moves while the wheels are still; or the wheels spin with no snow or slush disturbed beneath them.
- P2 [core · trajectory_momentum]
  - expect: Snow thrown by the spinning wheels is flung backward, away from the way the car is trying to go, and falls back to the road.
  - fail: Snow is flung forward ahead of the car from the driven wheels; or it rises away from the road and keeps rising; or the spray hangs in the air after the wheels have stopped.
- P3 [major · causeless_motion]
  - expect: The car moves only while the wheels are driving and stays put once they stop.
  - fail: The car creeps forward with its wheels still; or it rolls backward along the level street with nothing pushing it; or it sets off again after the wheels have stopped turning.
- P4 [major · material_response]
  - expect: The snow under the wheels is loose: it is churned, packed and thrown, while the tyre keeps its shape.
  - fail: The snow stays a smooth unbroken sheet under the spinning wheel; or the snow acts as a solid slab that the wheel grips at once; or the tyre takes the shape of the rut and stays that shape.
- P5 [fatal · permanence_count]
  - expect: One car keeps its wheels and its shape at the kerb.
  - fail: The car vanishes or a second one appears; or a wheel comes away and goes on spinning by itself; or the car passes through the kerb.
- P6 [minor · attribute_drift]
  - expect: The car's colour, the snow cover and the street stay the same.
  - fail: The car changes colour; or the snow on the road behind the car changes depth between frames; or the buildings alongside rearrange.

## MECH-0051 · friction_rolling · train

**Caption.** A woman in smooth-soled shoes steps onto a patch of ice on a sidewalk, her foot slides forward, and she stumbles.

**Expectation (hidden).** The slip happens as the foot lands on the ice, not before; her arms come up to balance; her foot grips normally on the pavement before and after.

**Declared violation types.** trajectory_momentum, causeless_motion

**SA**
- S1 [core] A woman walks along a sidewalk.
- S2 [core] She steps onto a patch of ice.
- S3 [core] Her foot slides forward.
- S4 [core] She stumbles.
- S5 [minor] Her shoes are smooth-soled.
- S6 [minor] The step onto the ice comes first, then the slide, then the stumble.

**PC**
- P1 [core · causeless_motion]
  - expect: Her foot grips the pavement before and after, and the slide starts where the sole lands on the ice.
  - fail: Her foot slides on the bare pavement away from the ice; or she slips before her foot has reached the ice; or her foot holds on the ice as firmly as on the pavement and nothing slides.
- P2 [core · trajectory_momentum]
  - expect: The sliding foot shoots forward, her body goes down and back behind it, and her arms come up as she catches her balance.
  - fail: The sliding foot shoots backward while she topples forward over it; or she stays upright and rigid while her foot slides out from under her; or her whole body slides along the ice with her legs unmoving.
- P3 [major · gravity_direction]
  - expect: She stays on the ground, her weight coming down through her feet or onto the sidewalk.
  - fail: She rises off the ground as she slips; or she hangs in the air part way through the stumble; or she sinks into the sidewalk.
- P4 [major · causeless_motion]
  - expect: Once the stumble is over she stands still; nothing carries her along.
  - fail: She keeps sliding along the pavement past the ice with her feet planted; or she is dragged sideways with nothing touching her; or she starts sliding again after regaining her footing.
- P5 [fatal · shape_identity]
  - expect: One woman keeps her limbs, her number and her shape.
  - fail: A limb stretches, detaches or vanishes; or she passes through the sidewalk; or a second figure appears beside her.
- P6 [minor · attribute_drift]
  - expect: Her clothing, the sidewalk and the street stay the same.
  - fail: Her clothing changes colour during the stumble; or the patch of ice moves to another part of the sidewalk between frames; or the street behind rearranges.

**Note.** Biomechanics scene: the woman is kept because her body is what shows the slip. Posture, footwear style and how gracefully she recovers are not judged; only where the sliding starts and which way it goes.

## MECH-0052 · friction_rolling · train

**Caption.** A hula hoop is rolled along a sidewalk and let go; it rolls on by itself, wobbles, and falls over.

**Expectation (hidden).** The hoop stays upright while fast, leans more as it slows, and falls onto its side; it does not fall while still rolling fast or stand still upright.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A hula hoop is rolled along a sidewalk and let go.
- S2 [core] It rolls on by itself.
- S3 [core] It wobbles.
- S4 [core] It falls over.
- S5 [minor] The hoop is released rather than kept in a hand.
- S6 [minor] The rolling comes first, then the wobble, then the fall.

**PC**
- P1 [core · causeless_motion]
  - expect: After the release nothing touches the hoop: it rolls on, slows, and changes only by slowing.
  - fail: The hoop gathers speed after being let go; or it is driven along with nothing touching it; or it starts rolling again after it has fallen.
- P2 [core · gravity_direction]
  - expect: The hoop leans further as it slows and comes down flat onto the sidewalk.
  - fail: The hoop leans right over and goes on rolling on its edge without falling; or it rights itself and rolls upright again; or it tips upward off the ground.
- P3 [major · trajectory_momentum]
  - expect: It stays upright while it is rolling quickly, and the wobble sets in only as it slows.
  - fail: The hoop topples over while still rolling quickly; or it stands on its edge without moving and stays standing; or its wobble shrinks as it slows.
- P4 [major · material_response]
  - expect: The hoop stays a rigid ring as it rolls and lands, rattling flat on the pavement.
  - fail: The hoop bends out of round as it rolls; or it flops like a loop of rope when it falls; or it bounces high off the pavement.
- P5 [fatal · permanence_count]
  - expect: One hoop on one sidewalk keeps its shape.
  - fail: The hoop vanishes or a second one appears; or it passes through the pavement; or it turns into another object as it falls.
- P6 [minor · attribute_drift]
  - expect: The hoop's colour, the sidewalk and the surroundings stay the same.
  - fail: The hoop changes colour as it rolls; or the paving slabs change pattern between frames; or the scene beside the sidewalk rearranges.

## MECH-0053 · friction_rolling · train

**Caption.** A wheeled suitcase pulled from a smooth airport floor onto a cobblestone street starts bumping and rattling over the stones.

**Expectation (hidden).** The wheels roll smoothly on the floor and jolt over each stone on the cobbles; the change happens exactly at the edge between surfaces.

**Declared violation types.** trajectory_momentum, material_response

**SA**
- S1 [core] A wheeled suitcase is pulled along a smooth airport floor.
- S2 [core] It is pulled onto a cobblestone street.
- S3 [core] It starts bumping and rattling over the stones.
- S4 [minor] The boundary between the smooth floor and the cobbles is visible.
- S5 [minor] The smooth rolling comes first and the bumping follows.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The case rolls smoothly on the flat floor and starts jolting where its wheels cross onto the cobbles.
  - fail: The case bumps while still on the smooth floor; or it rolls over the cobbles as smoothly as it did on the floor; or the jolting begins well after the wheels are onto the stones.
- P2 [core · material_response]
  - expect: Each jolt comes from a wheel riding up and off a stone, so the case lifts and drops with the stones it is passing over.
  - fail: The case shakes without its wheels meeting any stone; or the cobbles flatten under the wheels as the case passes; or the case buzzes evenly like a machine with no relation to the stones beneath it.
- P3 [major · gravity_direction]
  - expect: The case comes back down onto the cobbles after each bump and its wheels stay on the ground.
  - fail: The case stays up in the air between bumps; or it climbs steadily as it is pulled along; or it sinks into the cobbles.
- P4 [major · causeless_motion]
  - expect: The case follows the handle: it goes where the handle takes it and stops when the handle stops.
  - fail: The case rolls on ahead of the handle with nothing pushing it; or it stops dead while the handle keeps moving forward; or it turns aside on the open street with nothing touching it.
- P5 [fatal · permanence_count]
  - expect: One suitcase keeps its wheels, its handle and its shape.
  - fail: The suitcase vanishes at the kerb or a second one appears; or a wheel comes away and the case rolls on as before; or the case passes through the cobbles.
- P6 [minor · attribute_drift]
  - expect: The suitcase's colour, the cobbles and the street stay the same.
  - fail: The suitcase changes colour or size at the kerb; or the pattern of the cobbles changes between frames; or the buildings along the street rearrange.

## MECH-0054 · friction_rolling · train

**Caption.** A piece of chalk is drawn in a large circle across a blackboard, and a white line appears where it has passed.

**Expectation (hidden).** The line grows only at the chalk tip and only while the chalk touches the board; nothing appears ahead of the tip or where the chalk is lifted off; the part already drawn stays put and does not fade, shift or vanish; the shape on the board matches the path the hand traced.

**Declared violation types.** missing_consequence, permanence_count, attribute_drift

**SA**
- S1 [core] A piece of chalk is drawn across a blackboard.
- S2 [core] It is moved in a large circle.
- S3 [core] A white line appears where it has passed.
- S4 [minor] The line traces the circle the chalk made.
- S5 [minor] The chalk moves first and the line appears behind it.

**PC**
- P1 [core · missing_consequence]
  - expect: The line grows at the chalk tip and only while the chalk is touching the board.
  - fail: A length of line appears ahead of the chalk tip; or a line appears where the chalk has been lifted clear of the board; or the chalk is drawn across the board leaving no mark at all.
- P2 [core · permanence_count]
  - expect: The part of the line already drawn stays where it is for the rest of the clip.
  - fail: A drawn part of the line fades away; or a drawn part shifts to another place on the board; or the whole line disappears and is laid down again.
- P3 [major · missing_consequence]
  - expect: The shape on the board matches the path the chalk travelled.
  - fail: The line on the board is a different shape from the path the chalk took; or the circle closes before the chalk has gone all the way round; or the line jumps across a gap the chalk never crossed.
- P4 [major · material_response]
  - expect: The chalk leaves a dusty, slightly broken mark and dust falls from the tip down the face of the board.
  - fail: The line is laid down as an even glowing stripe with no dusty texture; or dust rises upward from the tip and stays up; or the chalk bends or melts against the board.
- P5 [fatal · permanence_count]
  - expect: One piece of chalk and one board are there throughout.
  - fail: The chalk vanishes mid-stroke or a second piece appears; or the chalk passes through the board; or the chalk turns into another object.
- P6 [minor · attribute_drift]
  - expect: The line's colour and the board's surface stay the same.
  - fail: The drawn line changes colour after it is laid down; or the board changes colour behind the line; or the frame and the things around the board rearrange.

