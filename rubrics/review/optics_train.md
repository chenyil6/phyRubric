# Rubric review

227 rubrics. SA = caption adherence (core/minor); PC = physics (fatal/core/major/minor, each tagged with a violation type). Expectation is the hidden field from data/, shown for the reviewer only.

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

## OPT-0003 · shadow · train

**Caption.** A dog runs across a sunlit lawn, and its shadow runs along the grass beside it.

**Expectation (hidden).** The shadow keeps pace with the dog, touches it at the paws, and lies on the side away from the sun; it does not lag, lead, or detach.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A dog runs across a lawn.
- S2 [core] The lawn is in sunlight.
- S3 [core] The dog's shadow is visible on the grass.
- S4 [core] The shadow runs along beside the dog.
- S5 [minor] The shadow touches the dog at its paws.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow keeps pace with the dog, moving when it moves and in the same direction.
  - fail: The shadow lags behind or runs ahead; or it stays still while the dog runs; or it moves the opposite way.
- P2 [core · shape_identity]
  - expect: The shadow keeps the dog's outline, its legs moving in step with the dog's.
  - fail: The shadow is a different animal's shape; or its legs are still while the dog's move; or it splits into two.
- P3 [major · missing_consequence]
  - expect: The shadow lies on the side of the dog away from the sun and is attached at the paws.
  - fail: It lies toward the sun; or it is detached from the paws on flat ground; or it switches sides while the sun stays put.
- P4 [major · causeless_motion]
  - expect: The shadow does not move on its own.
  - fail: It moves while the dog stands still; or it changes length with the dog still; or it drifts across the grass by itself.
- P5 [fatal · permanence_count]
  - expect: One dog and one shadow of it; the dog keeps its parts and passes through nothing.
  - fail: The dog duplicates or vanishes; or a second shadow appears under one sun; or the shadow becomes a solid object; or the dog passes through a fence.
- P6 [minor · attribute_drift]
  - expect: The dog's coat and the lawn stay the same, and the shadow stays dark rather than coloured.
  - fail: The coat changes colour; or the shadow turns bright or coloured; or the lawn's texture changes.

**Note.** Self-driven animal: where it goes and how it moves are not judged. Only the shadow's relation to it is.

## OPT-0004 · shadow · train

**Caption.** A desk lamp is moved from the left side of a vase to the right side, and the vase's shadow swings from the right side of the vase to the left.

**Expectation (hidden).** The shadow always falls on the side opposite the lamp and moves smoothly as the lamp moves; it does not stay put or move with the lamp.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A desk lamp stands to the left of a vase.
- S2 [core] The lamp is moved to the right side of the vase.
- S3 [core] The vase's shadow is visible.
- S4 [core] The shadow swings from the right of the vase to the left.
- S5 [minor] The lamp moves first and the shadow follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow always falls on the side of the vase opposite the lamp and moves smoothly as the lamp moves.
  - fail: The shadow stays put while the lamp moves; or it moves with the lamp to the same side; or it jumps from one side to the other.
- P2 [core · shape_identity]
  - expect: The shadow keeps the vase's outline, stretching or shortening with the angle.
  - fail: It becomes a different shape; or splits into two under one lamp; or keeps a fixed shape while the lamp plainly moves.
- P3 [major · causeless_motion]
  - expect: The shadow moves only while the lamp moves.
  - fail: It moves with the lamp still; or it keeps moving after the lamp has stopped; or it moves before the lamp.
- P4 [major · missing_consequence]
  - expect: The shadow starts at the vase's base and lies on the table.
  - fail: It floats detached from the base; or it appears on the ceiling; or it is missing with the lamp plainly on.
- P5 [fatal · permanence_count]
  - expect: One lamp, one vase and one shadow; nothing appears, vanishes or passes through the table.
  - fail: A second vase or shadow appears; or the vase vanishes; or the lamp passes through the vase; or the shadow becomes solid.
- P6 [minor · attribute_drift]
  - expect: The vase, the lamp and the table stay the same, and the shadow stays dark.
  - fail: The vase changes colour; or the shadow turns coloured; or the table pattern shifts.

## OPT-0005 · shadow · train

**Caption.** A pair of hands held in a flashlight beam pointed at a wall forms a bird shape, and a bird-shaped shadow appears on the wall.

**Expectation (hidden).** The shadow matches the outline of the hands and changes the instant the fingers move; it is larger than the hands and appears only where the beam hits the wall.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A pair of hands is held in a flashlight beam pointed at a wall.
- S2 [core] The hands form a bird shape.
- S3 [core] A bird-shaped shadow appears on the wall.
- S4 [minor] The shadow is larger than the hands.
- S5 [minor] The hands are shaped first and the shadow appears with them.

**PC**
- P1 [core · shape_identity]
  - expect: The shadow matches the outline of the hands and changes the instant the fingers move.
  - fail: The shadow is a different shape from the hands; or it stays fixed while the fingers move; or it changes while the hands are still.
- P2 [core · missing_consequence]
  - expect: The shadow appears only where the beam hits the wall, on the far side of the hands from the flashlight.
  - fail: It appears outside the lit patch; or between the hands and the flashlight; or with the flashlight off.
- P3 [major · causeless_motion]
  - expect: The shadow does not move on its own.
  - fail: It drifts across the wall with the hands still; or it flaps by itself; or it moves before the hands.
- P4 [major · shape_identity]
  - expect: The shadow is one connected dark shape, larger than the hands, with a soft edge.
  - fail: It splits into pieces unrelated to the fingers; or it is smaller than the hands; or it has a hard geometric outline unlike the hands.
- P5 [fatal · permanence_count]
  - expect: Two hands and one shadow; the hands keep their fingers and nothing passes through the wall.
  - fail: A finger vanishes or an extra appears; or a second shadow appears under one beam; or the hands pass through the wall; or the shadow becomes solid.
- P6 [minor · attribute_drift]
  - expect: The wall and the flashlight stay the same, and the shadow stays dark.
  - fail: The wall changes colour; or the shadow turns coloured; or the flashlight changes.

**Note.** The hands are the object casting the shadow; the person is not judged.

## OPT-0006 · shadow · train

**Caption.** A balloon drifts across the beam of a projector during a slideshow, and its dark silhouette appears on the screen over the slides.

**Expectation (hidden).** The silhouette appears where the balloon blocks the beam and moves with it; the slide image is missing inside the silhouette and returns when the balloon has passed.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A projector shows slides on a screen.
- S2 [core] A balloon drifts across the beam.
- S3 [core] Its dark silhouette appears on the screen over the slides.
- S4 [minor] The silhouette moves with the balloon.
- S5 [minor] The balloon enters the beam first and the silhouette appears with it.

**PC**
- P1 [core · missing_consequence]
  - expect: The silhouette appears where the balloon blocks the beam and moves with it.
  - fail: The silhouette appears with the balloon outside the beam; or it stays still while the balloon drifts; or it moves the opposite way.
- P2 [core · shape_identity]
  - expect: The slide image is missing inside the silhouette and returns when the balloon has passed.
  - fail: The slide shows through the silhouette; or the silhouette leaves a dark patch after the balloon has gone; or the silhouette is a different shape from the balloon.
- P3 [major · causeless_motion]
  - expect: The silhouette does not move on its own.
  - fail: It drifts with the balloon still; or it appears before the balloon enters; or it lingers after the balloon has left.
- P4 [major · gravity_direction]
  - expect: The balloon drifts gently and does not shoot or drop like a stone.
  - fail: It shoots off; or drops like a stone; or hangs rigidly still in a draught.
- P5 [fatal · permanence_count]
  - expect: One balloon and one silhouette; the projector and screen stay one each.
  - fail: A second silhouette appears under one beam; or the balloon vanishes; or the silhouette becomes solid; or the balloon passes through the screen.
- P6 [minor · attribute_drift]
  - expect: The balloon's colour and the slides stay the same, and the silhouette stays dark.
  - fail: The balloon changes colour; or the silhouette turns bright; or the slide changes with no click.

## OPT-0007 · shadow · train

**Caption.** A tall wooden lifeguard chair stands on a beach with the low sun behind it, and its long shadow stretches across the sand in front of it.

**Expectation (hidden).** The shadow lies on the ground away from the sun, starts at the chair's legs, and is longer than the chair is tall; it does not float or point toward the sun.

**Declared violation types.** missing_consequence, gravity_direction

**SA**
- S1 [core] A tall wooden lifeguard chair stands on a beach.
- S2 [core] The sun is low behind it.
- S3 [core] Its long shadow stretches across the sand in front of it.
- S4 [minor] The shadow is longer than the chair is tall.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow lies on the ground away from the sun and starts at the chair's legs.
  - fail: It points toward the sun; or it floats detached from the legs; or it is missing under a plainly low sun.
- P2 [core · shape_identity]
  - expect: The shadow keeps the chair's outline, stretched long by the low sun.
  - fail: It is a different shape; or it is short under a low sun; or it splits into two.
- P3 [major · causeless_motion]
  - expect: The shadow stays still with the chair still.
  - fail: It drifts across the sand by itself; or it changes length with nothing moving; or it swings round.
- P4 [major · gravity_direction]
  - expect: The chair stands on the sand and the shadow lies flat on it.
  - fail: The chair floats; or the shadow stands up off the sand; or the shadow climbs the chair.
- P5 [fatal · permanence_count]
  - expect: One chair and one shadow; the chair keeps its parts.
  - fail: The chair duplicates or vanishes; or a second shadow appears; or the shadow becomes solid; or a leg vanishes.
- P6 [minor · attribute_drift]
  - expect: The chair's paint and the beach stay the same, and the shadow stays dark.
  - fail: The chair changes colour; or the shadow turns coloured; or the sand texture changes.

## OPT-0008 · shadow · train

**Caption.** A flashlight is brought closer to a toy dinosaur standing in front of a wall, and the dinosaur's shadow on the wall grows larger.

**Expectation (hidden).** The shadow grows as the light approaches and shrinks as it backs away, keeping the dinosaur's outline; it does not stay the same size.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A toy dinosaur stands in front of a wall.
- S2 [core] A flashlight lights it.
- S3 [core] The flashlight is brought closer to the dinosaur.
- S4 [core] The dinosaur's shadow on the wall grows larger.
- S5 [minor] The flashlight moves first and the shadow grows with it.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow grows as the light approaches and shrinks as it backs away.
  - fail: The shadow stays the same size while the light moves; or it shrinks as the light comes closer; or it changes size with the light still.
- P2 [core · shape_identity]
  - expect: The shadow keeps the dinosaur's outline as it grows.
  - fail: It becomes a different shape; or splits; or the head and tail change places.
- P3 [major · missing_consequence]
  - expect: The shadow is on the wall behind the dinosaur, away from the flashlight.
  - fail: It is between the dinosaur and the flashlight; or on the ceiling; or missing with the light plainly on.
- P4 [major · causeless_motion]
  - expect: The dinosaur stays where it stands.
  - fail: It slides; or turns by itself; or lifts off.
- P5 [fatal · permanence_count]
  - expect: One dinosaur, one flashlight and one shadow.
  - fail: A second shadow appears under one light; or the dinosaur vanishes; or the shadow becomes solid; or the flashlight passes through the dinosaur.
- P6 [minor · attribute_drift]
  - expect: The dinosaur's colour and the wall stay the same, and the shadow stays dark.
  - fail: The dinosaur changes colour; or the shadow turns coloured; or the wall changes.

## OPT-0009 · shadow · train

**Caption.** The shadow of a cloud sweeps across a sunlit hillside, darkening the grass as it passes.

**Expectation (hidden).** The dark patch moves steadily in one direction with a soft edge, the grass under it dims and brightens again once it has passed, and the trees' own shadows fade inside the patch and return behind it; the patch does not jump, stop dead, or brighten the ground.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A hillside is in sunlight.
- S2 [core] The shadow of a cloud sweeps across it.
- S3 [core] The grass darkens as the shadow passes.
- S4 [minor] The shadow has a soft edge.
- S5 [minor] The grass brightens again once the shadow has passed.

**PC**
- P1 [core · process_direction]
  - expect: The dark patch moves steadily in one direction, and the grass under it dims and brightens again once it has passed.
  - fail: The patch jumps; or stops dead; or the grass stays dark after the patch has gone.
- P2 [core · missing_consequence]
  - expect: The trees' own shadows fade inside the patch and return behind it.
  - fail: Tree shadows stay sharp inside the cloud shadow; or they vanish outside it; or they point a different way inside it.
- P3 [major · attribute_drift]
  - expect: The patch darkens the ground and never brightens it.
  - fail: The ground is brighter inside the patch; or the patch is a colour rather than a darkening; or it glows.
- P4 [major · shape_identity]
  - expect: The patch is one soft-edged region.
  - fail: It has a hard geometric edge; or splits into many small patches; or forms a recognisable object shape.
- P5 [fatal · permanence_count]
  - expect: The hillside keeps its trees and features.
  - fail: Trees appear or vanish as the shadow passes; or the hillside changes shape; or the patch becomes a solid object.
- P6 [minor · attribute_drift]
  - expect: The grass colour and the landscape stay the same apart from the dimming.
  - fail: The grass changes colour rather than brightness; or the landscape rearranges; or the sky changes.

## OPT-0010 · shadow · train

**Caption.** A frog jumps straight up from a sunlit stone, and its shadow stays on the stone and separates from its feet while it is in the air.

**Expectation (hidden).** The shadow remains on the surface the whole time; the gap between the frog's feet and the shadow opens as it rises and closes when it lands.

**Declared violation types.** missing_consequence, gravity_direction

**SA**
- S1 [core] A frog sits on a sunlit stone.
- S2 [core] It jumps straight up.
- S3 [core] Its shadow stays on the stone.
- S4 [core] The shadow separates from its feet while it is in the air.
- S5 [minor] The gap closes when the frog lands.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow remains on the surface the whole time, and the gap between the frog's feet and the shadow opens as it rises and closes when it lands.
  - fail: The shadow rises with the frog; or stays attached to its feet in mid-air; or the gap stays open after landing.
- P2 [core · gravity_direction]
  - expect: The frog rises, slows, and comes back down onto the stone.
  - fail: It hangs in the air; or keeps rising; or lands somewhere else with a straight-up jump.
- P3 [major · shape_identity]
  - expect: The shadow keeps the frog's outline.
  - fail: It becomes a different shape; or splits; or vanishes in mid-jump.
- P4 [major · missing_consequence]
  - expect: The shadow lies on the side away from the sun.
  - fail: It lies toward the sun; or switches sides during the jump; or it is missing in plain sunlight.
- P5 [fatal · permanence_count]
  - expect: One frog and one shadow; the frog keeps its legs.
  - fail: A second frog or shadow appears; or the frog vanishes; or the shadow becomes solid; or a leg detaches.
- P6 [minor · attribute_drift]
  - expect: The frog's colour and the stone stay the same, and the shadow stays dark.
  - fail: The frog changes colour; or the shadow turns coloured; or the stone changes.

**Note.** Self-driven animal: where it goes and how it moves are not judged. Only the shadow's relation to it is.

## OPT-0011 · shadow · train

**Caption.** A tractor drives along a sunlit field track, and its shadow rolls along the ground beside it.

**Expectation (hidden).** The shadow moves at the same speed as the tractor, touches it at the wheels, and shows the wheels turning; it stays on the side away from the sun.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A tractor drives along a field track.
- S2 [core] The track is in sunlight.
- S3 [core] The tractor's shadow rolls along the ground beside it.
- S4 [minor] The shadow shows the wheels turning.
- S5 [minor] The shadow touches the tractor at the wheels.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow moves at the same speed as the tractor and touches it at the wheels.
  - fail: It lags or leads; or is detached from the wheels on flat ground; or stays still while the tractor moves.
- P2 [core · shape_identity]
  - expect: The shadow keeps the tractor's outline and its wheels turn in step.
  - fail: It is a different vehicle's shape; or its wheels are still while the tractor's turn; or it splits.
- P3 [major · missing_consequence]
  - expect: The shadow lies on the side away from the sun.
  - fail: It lies toward the sun; or switches sides with the sun fixed; or it is missing in sunlight.
- P4 [major · causeless_motion]
  - expect: The shadow does not move on its own.
  - fail: It moves with the tractor stopped; or changes length with the tractor still.
- P5 [fatal · permanence_count]
  - expect: One tractor and one shadow.
  - fail: The tractor duplicates or vanishes; or a second shadow appears; or the shadow becomes solid; or the tractor passes through a fence.
- P6 [minor · attribute_drift]
  - expect: The tractor's paint and the field stay the same, and the shadow stays dark.
  - fail: The tractor changes colour; or the shadow turns coloured; or the field changes.

## OPT-0012 · shadow · train

**Caption.** A ball is thrown across a sunlit yard, and the ball's shadow slides along the ground beneath it and meets the ball where it lands.

**Expectation (hidden).** The shadow tracks the ball's path on the ground, separating from it while it is high and rejoining at the landing spot; it does not lag or vanish in flight.

**Declared violation types.** missing_consequence, trajectory_momentum

**SA**
- S1 [core] A ball is thrown across a sunlit yard.
- S2 [core] The ball's shadow slides along the ground beneath it.
- S3 [core] The shadow meets the ball where it lands.
- S4 [minor] The throw comes first and the shadow tracks the flight.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow tracks the ball's path on the ground, separating from it while it is high and rejoining at the landing spot.
  - fail: It lags or vanishes in flight; or stays attached to the ball in mid-air; or fails to meet it at landing.
- P2 [core · trajectory_momentum]
  - expect: The ball follows one smooth arc.
  - fail: It flies flat; or hangs; or changes direction in mid-air.
- P3 [major · shape_identity]
  - expect: The shadow keeps the ball's round outline.
  - fail: It becomes a different shape; or splits; or becomes a long streak.
- P4 [major · missing_consequence]
  - expect: The shadow lies on the side away from the sun.
  - fail: It lies toward the sun; or switches sides during the flight; or it is missing in sunlight.
- P5 [fatal · permanence_count]
  - expect: One ball and one shadow.
  - fail: A second ball or shadow appears; or the ball vanishes; or the shadow becomes solid.
- P6 [minor · attribute_drift]
  - expect: The ball's colour and the yard stay the same, and the shadow stays dark.
  - fail: The ball changes colour; or the shadow turns coloured; or the yard changes.

## OPT-0013 · shadow · train

**Caption.** A patio umbrella is opened in the sun, and a round shadow appears on the ground beneath it.

**Expectation (hidden).** The shadow appears as the umbrella opens, matches its round outline, and lies on the side away from the sun; it moves when the umbrella is tilted.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A patio umbrella is opened.
- S2 [core] It is in sunlight.
- S3 [core] A round shadow appears on the ground beneath it.
- S4 [minor] The shadow appears as the umbrella opens.
- S5 [minor] The shadow moves when the umbrella is tilted.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow appears as the umbrella opens and lies on the side away from the sun.
  - fail: The shadow is there before the umbrella opens; or it lies toward the sun; or it is missing with the umbrella open in sunlight.
- P2 [core · shape_identity]
  - expect: The shadow matches the umbrella's round outline.
  - fail: It is a different shape; or splits; or stays small when the umbrella is fully open.
- P3 [major · causeless_motion]
  - expect: The shadow moves only when the umbrella moves.
  - fail: It drifts by itself; or it stays put when the umbrella is tilted; or it moves before the umbrella.
- P4 [major · material_response]
  - expect: The canopy opens as taut fabric on ribs.
  - fail: It is rigid like a plate; or floats off; or tears.
- P5 [fatal · permanence_count]
  - expect: One umbrella and one shadow.
  - fail: A second shadow appears; or the umbrella vanishes; or the shadow becomes solid; or the pole passes through the table.
- P6 [minor · attribute_drift]
  - expect: The umbrella's colour and the patio stay the same, and the shadow stays dark.
  - fail: The canopy changes colour; or the shadow turns coloured; or the patio changes.

## OPT-0014 · shadow · train

**Caption.** A car drives under a highway bridge on a sunny day, and its shadow disappears in the bridge's shade and reappears on the far side.

**Expectation (hidden).** The car's own shadow vanishes while the car is in the larger shadow and comes back as soon as the car is in sunlight again.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A car drives under a highway bridge.
- S2 [core] The day is sunny.
- S3 [core] The car's shadow disappears in the bridge's shade.
- S4 [core] It reappears on the far side.
- S5 [minor] The shadow vanishes when the car enters the shade and returns when it leaves.

**PC**
- P1 [core · missing_consequence]
  - expect: The car's own shadow vanishes while the car is in the larger shadow and comes back as soon as it is in sunlight again.
  - fail: The shadow stays visible in the bridge's shade; or it is missing in sunlight; or it returns before the car is out of the shade.
- P2 [core · permanence_count]
  - expect: The car itself is unchanged by entering and leaving the shade.
  - fail: The car vanishes in the shade; or a second car appears; or the car changes when it comes out.
- P3 [major · missing_consequence]
  - expect: In sunlight the shadow lies on the side away from the sun, attached at the wheels.
  - fail: It lies toward the sun; or is detached from the wheels; or switches sides.
- P4 [major · causeless_motion]
  - expect: The car drives steadily and the shadow moves only with it.
  - fail: The shadow moves with the car stopped; or the car jumps position; or the shadow drifts.
- P5 [fatal · permanence_count]
  - expect: One car and one shadow; the bridge stays one bridge.
  - fail: A second shadow appears in sunlight; or the shadow becomes solid; or the car passes through a pier.
- P6 [minor · attribute_drift]
  - expect: The car's colour and the road stay the same, and the shadow stays dark.
  - fail: The car changes colour; or the shadow turns coloured; or the bridge changes.

## OPT-0015 · shadow · train

**Caption.** A ball rolls from a sunlit pavement into the shade of a building, and its shadow disappears.

**Expectation (hidden).** The shadow is visible only while the ball is in the sun and fades as it enters the shade; it would return if the ball rolled back into sunlight.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A ball rolls along a sunlit pavement.
- S2 [core] It rolls into the shade of a building.
- S3 [core] Its shadow disappears.
- S4 [minor] The shadow is visible only while the ball is in the sun.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow is visible while the ball is in the sun and fades as it enters the shade.
  - fail: The shadow stays visible in the shade; or it is missing in sunlight; or it vanishes before the ball reaches the shade.
- P2 [core · permanence_count]
  - expect: The ball itself is unchanged as it enters the shade.
  - fail: The ball vanishes; or a second ball appears; or the ball changes as it enters the shade.
- P3 [major · missing_consequence]
  - expect: In sunlight the shadow lies on the side away from the sun, attached at the contact point.
  - fail: It lies toward the sun; or is detached; or switches sides.
- P4 [major · causeless_motion]
  - expect: The ball rolls straight and slows gently.
  - fail: It curves; or speeds up; or stops and restarts.
- P5 [fatal · permanence_count]
  - expect: One ball and one shadow.
  - fail: A second shadow appears in sunlight; or the shadow becomes solid; or the ball passes through the wall.
- P6 [minor · attribute_drift]
  - expect: The ball's colour and the pavement stay the same, and the shadow stays dark.
  - fail: The ball changes colour; or the shadow turns coloured; or the building changes.

## OPT-0016 · shadow · train

**Caption.** A lit candle is carried in a circle around a vase on a table, and the vase's shadow sweeps around the table opposite the candle.

**Expectation (hidden).** The shadow always points away from the candle, rotating as the candle circles; its length changes as the candle moves closer or further.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A vase stands on a table.
- S2 [core] A lit candle is carried in a circle around it.
- S3 [core] The vase's shadow sweeps around the table opposite the candle.
- S4 [minor] The shadow's length changes as the candle's distance changes.
- S5 [minor] The candle moves first and the shadow follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow always points away from the candle and rotates as the candle circles.
  - fail: It points toward the candle; or stays fixed while the candle moves; or rotates the wrong way.
- P2 [core · shape_identity]
  - expect: The shadow keeps the vase's outline, lengthening and shortening with the candle's distance.
  - fail: It is a different shape; or splits into two under one flame; or keeps one length while the distance plainly changes.
- P3 [major · causeless_motion]
  - expect: The shadow moves only as the candle moves.
  - fail: It moves with the candle still; or it lags and jumps; or it moves before the candle.
- P4 [major · gravity_direction]
  - expect: The flame points upward and the shadow lies on the table.
  - fail: The flame points sideways in still air; or the shadow stands up off the table; or the shadow floats.
- P5 [fatal · permanence_count]
  - expect: One vase, one candle and one shadow.
  - fail: A second shadow or vase appears; or the candle passes through the vase; or the shadow becomes solid.
- P6 [minor · attribute_drift]
  - expect: The vase, the table and the candle stay the same, and the shadow stays dark.
  - fail: The vase changes colour; or the shadow turns coloured; or the table changes.

## OPT-0017 · shadow · train

**Caption.** A flock of birds flies over a sunlit field, and their shadows race across the grass below them.

**Expectation (hidden).** Each shadow moves at the same speed and direction as its bird, offset toward the side away from the sun; the shadows do not appear where no bird passes.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A flock of birds flies over a sunlit field.
- S2 [core] Their shadows race across the grass below them.
- S3 [minor] Each bird has a shadow.
- S4 [minor] The shadows move together with the flock.

**PC**
- P1 [core · missing_consequence]
  - expect: Each shadow moves at the same speed and direction as its bird.
  - fail: The shadows lag or lead; or move the opposite way; or stay still while the birds fly.
- P2 [core · permanence_count]
  - expect: There are as many shadows as birds, and none appears where no bird passes.
  - fail: Shadows appear with no bird above; or there are more shadows than birds; or shadows persist after the birds have gone.
- P3 [major · missing_consequence]
  - expect: The shadows are offset toward the side away from the sun.
  - fail: They lie toward the sun; or directly below with a plainly low sun; or in different directions for one flock.
- P4 [major · causeless_motion]
  - expect: The shadows do not move on their own.
  - fail: A shadow moves while its bird hovers; or the shadows scatter while the flock holds together.
- P5 [fatal · shape_identity]
  - expect: The birds keep their wings and the shadows keep bird shapes.
  - fail: A bird loses a wing; or a shadow becomes a solid object; or shadows merge into one blob under a spread flock.
- P6 [minor · attribute_drift]
  - expect: The field and the birds stay the same, and the shadows stay dark.
  - fail: The field changes; or the shadows turn coloured; or the birds change colour.

**Note.** Self-driven animal: where it goes and how it moves are not judged. Only the shadow's relation to it is.

## OPT-0018 · shadow · train

**Caption.** A kite flies high over a beach in the sun, and its small shadow moves across the sand as the kite sways.

**Expectation (hidden).** The shadow moves in step with the kite's motion, far from the kite itself; it does not stay still while the kite moves.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A kite flies high over a beach in the sun.
- S2 [core] Its small shadow moves across the sand.
- S3 [core] The shadow moves as the kite sways.
- S4 [minor] The shadow is far from the kite itself.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow moves in step with the kite's motion.
  - fail: It stays still while the kite moves; or moves the opposite way; or lags and jumps.
- P2 [core · shape_identity]
  - expect: The shadow keeps the kite's outline, small and soft-edged at that height.
  - fail: It is a different shape; or it is huge and sharp; or it splits.
- P3 [major · missing_consequence]
  - expect: The shadow lies on the side away from the sun, far from the kite's foot of string.
  - fail: It lies toward the sun; or directly beneath under a plainly low sun; or it is missing in sunlight.
- P4 [major · causeless_motion]
  - expect: The shadow does not move on its own.
  - fail: It moves with the kite still; or drifts across the sand by itself.
- P5 [fatal · permanence_count]
  - expect: One kite and one shadow.
  - fail: A second shadow appears; or the kite vanishes; or the shadow becomes solid; or the kite passes through its string.
- P6 [minor · attribute_drift]
  - expect: The kite's colours and the beach stay the same, and the shadow stays dark.
  - fail: The kite changes colour; or the shadow turns coloured; or the sand changes.

## OPT-0019 · shadow · train

**Caption.** A ball rolls through the shadow of a signpost on a sunny pavement, and the post's shadow slides over the ball as it passes.

**Expectation (hidden).** The post's shadow appears on the ball's surface while the ball is inside it, and the ball's own shadow continues on the ground beyond; nothing about the post changes.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A ball rolls along a sunny pavement.
- S2 [core] It passes through the shadow of a signpost.
- S3 [core] The post's shadow slides over the ball as it passes.
- S4 [minor] The ball's own shadow continues on the ground beyond.

**PC**
- P1 [core · missing_consequence]
  - expect: The post's shadow appears on the ball's surface while the ball is inside it and slides off as the ball leaves.
  - fail: The ball stays fully lit inside the post's shadow; or the dark band stays on the ball after it has passed; or the band appears before the ball reaches the shadow.
- P2 [core · shape_identity]
  - expect: The post's shadow on the ground is unchanged by the ball passing through it.
  - fail: The post's shadow bends or moves as the ball passes; or it vanishes; or it follows the ball.
- P3 [major · missing_consequence]
  - expect: The ball's own shadow continues on the ground on the side away from the sun.
  - fail: The ball has no shadow in sunlight; or its shadow lies toward the sun; or its shadow vanishes inside the post's shadow and does not return.
- P4 [major · causeless_motion]
  - expect: The ball rolls straight and slows gently.
  - fail: It curves; or speeds up; or stops and restarts.
- P5 [fatal · permanence_count]
  - expect: One ball, one post and its shadow.
  - fail: A second ball appears; or the post vanishes; or the ball passes through the post; or a shadow becomes solid.
- P6 [minor · attribute_drift]
  - expect: The ball's colour and the pavement stay the same, and the shadows stay dark.
  - fail: The ball changes colour; or a shadow turns coloured; or the pavement changes.

## OPT-0020 · shadow · train

**Caption.** A parked bicycle is lit from behind by a car's headlights at night, and a long shadow of the bicycle stretches down the road ahead of it.

**Expectation (hidden).** The shadow points away from the headlights, grows sharper and shorter as the car approaches, and swings as the car passes.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A bicycle is parked at night.
- S2 [core] A car's headlights light it from behind.
- S3 [core] A long shadow of the bicycle stretches down the road ahead of it.
- S4 [minor] The shadow changes as the car approaches and passes.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow points away from the headlights and grows sharper and shorter as the car approaches, swinging as the car passes.
  - fail: It points toward the headlights; or stays fixed while the car moves; or grows longer as the car nears.
- P2 [core · shape_identity]
  - expect: The shadow keeps the bicycle's outline, wheels and frame, stretched long.
  - fail: It is a different shape; or splits under one car's lights into unrelated pieces; or it is short with the lights far off.
- P3 [major · causeless_motion]
  - expect: The bicycle stays parked and the shadow moves only with the lights.
  - fail: The bicycle rolls by itself; or the shadow moves with the car stopped; or the shadow swings before the lights reach it.
- P4 [major · missing_consequence]
  - expect: The shadow starts at the wheels and lies on the road.
  - fail: It floats detached from the wheels; or it appears on a wall the lights cannot reach; or it is missing with the lights plainly on it.
- P5 [fatal · permanence_count]
  - expect: One bicycle and one shadow per car.
  - fail: A second bicycle appears; or the shadow becomes solid; or the car passes through the bicycle.
- P6 [minor · attribute_drift]
  - expect: The bicycle and the road stay the same, and the shadow stays dark.
  - fail: The bicycle changes colour; or the shadow turns coloured; or the road markings shift.

## OPT-0021 · shadow · train

**Caption.** A hand reaches across a table toward a lamp, and the shadow of the arm sweeps across the table on the far side of the lamp from the arm.

**Expectation (hidden).** The arm's shadow lies away from the lamp and moves as the arm moves; it is not cast toward the lamp.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A lamp stands on a table.
- S2 [core] A hand reaches across the table toward it.
- S3 [core] The shadow of the arm sweeps across the table on the far side of the lamp from the arm.
- S4 [minor] The arm moves first and the shadow follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The arm's shadow lies away from the lamp and moves as the arm moves.
  - fail: It is cast toward the lamp; or it stays still while the arm moves; or it moves the opposite way.
- P2 [core · shape_identity]
  - expect: The shadow keeps the arm's outline with the hand at its end.
  - fail: It is a different shape; or the hand is missing from it; or it splits.
- P3 [major · causeless_motion]
  - expect: The shadow does not move on its own.
  - fail: It moves with the arm still; or it moves before the arm; or it lingers after the arm is withdrawn.
- P4 [major · missing_consequence]
  - expect: The shadow lies on the table and stretches longer the closer the arm comes to the lamp.
  - fail: It floats above the table; or it shrinks as the arm nears the lamp; or it is missing with the lamp on.
- P5 [fatal · permanence_count]
  - expect: One lamp, one arm and one shadow; the hand passes through nothing.
  - fail: The hand passes through the lamp; or a second shadow appears; or the shadow becomes solid; or a finger vanishes.
- P6 [minor · attribute_drift]
  - expect: The lamp and the table stay the same, and the shadow stays dark.
  - fail: The lamp changes; or the shadow turns coloured; or the table changes.

**Note.** The arm is the object casting the shadow; the person is not judged.

## OPT-0022 · shadow · train

**Caption.** A ceiling fan is switched on under a bright bulb, and the spinning blades throw moving shadows across the room.

**Expectation (hidden).** The shadows sweep around as fast as the blades and stop when the fan stops; they appear on the surfaces below and beside the fan, away from the bulb.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A ceiling fan is under a bright bulb.
- S2 [core] The fan is switched on.
- S3 [core] The spinning blades throw moving shadows across the room.
- S4 [minor] The shadows sweep as fast as the blades.
- S5 [minor] The fan starts first and the shadows move with it.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadows sweep around as fast as the blades and stop when the fan stops.
  - fail: The shadows are still while the blades turn; or they keep sweeping after the fan stops; or they sweep before the fan starts.
- P2 [core · shape_identity]
  - expect: The shadows are blade shapes, one per blade, radiating from the fan's centre.
  - fail: There are more shadows than blades; or they are unrelated shapes; or they merge into a solid disc while the blades are plainly separate.
- P3 [major · missing_consequence]
  - expect: The shadows appear on the surfaces below and beside the fan, away from the bulb.
  - fail: They appear on the ceiling above the bulb; or on the bulb side of the blades; or they are missing with the bulb on.
- P4 [major · causeless_motion]
  - expect: The shadows move only while the blades turn, and the bulb stays steady.
  - fail: The shadows sweep with the blades still; or the bulb flickers or moves; or the shadows change with nothing moving.
- P5 [fatal · permanence_count]
  - expect: One fan with its blades and one bulb.
  - fail: A blade vanishes; or a second fan appears; or a shadow becomes solid; or the fan detaches.
- P6 [minor · attribute_drift]
  - expect: The blades' colour and the room stay the same, and the shadows stay dark.
  - fail: The blades change colour; or the shadows turn coloured; or the room rearranges.

## OPT-0023 · shadow · train

**Caption.** A ball bounces on a sunny court, and its shadow on the ground meets the ball at each bounce and separates as it rises.

**Expectation (hidden).** The shadow stays on the ground under the ball's path; the ball touches its shadow only at the bounce; the two never swap places.

**Declared violation types.** missing_consequence, trajectory_momentum

**SA**
- S1 [core] A ball bounces on a sunny court.
- S2 [core] Its shadow on the ground meets the ball at each bounce.
- S3 [core] The shadow separates from the ball as it rises.
- S4 [minor] The shadow stays on the ground throughout.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow stays on the ground under the ball's path, and the ball touches its shadow only at each bounce.
  - fail: The shadow rises with the ball; or the two swap places; or the shadow is missing in flight.
- P2 [core · trajectory_momentum]
  - expect: Each bounce is lower than the last and the ball comes down each time.
  - fail: A bounce is higher than the one before; or the ball hangs; or it bounces sideways off flat ground.
- P3 [major · shape_identity]
  - expect: The shadow keeps the ball's round outline.
  - fail: It is a different shape; or splits; or streaks.
- P4 [major · missing_consequence]
  - expect: The shadow lies on the side away from the sun.
  - fail: It lies toward the sun; or switches sides during the bounces; or it is missing in sunlight.
- P5 [fatal · permanence_count]
  - expect: One ball and one shadow.
  - fail: A second ball or shadow appears; or the ball vanishes; or the shadow becomes solid.
- P6 [minor · attribute_drift]
  - expect: The ball's colour and the court stay the same, and the shadow stays dark.
  - fail: The ball changes colour; or the shadow turns coloured; or the court lines shift.

## OPT-0024 · shadow · train

**Caption.** An empty swing sways in the afternoon sun, and its shadow swings back and forth across the ground.

**Expectation (hidden).** The shadow moves in time with the swing, stretching and shortening as the seat rises and falls; it lies on the side away from the sun.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] An empty swing sways in the afternoon sun.
- S2 [core] Its shadow swings back and forth across the ground.
- S3 [minor] The shadow stretches and shortens as the seat rises and falls.
- S4 [minor] The swing moves first and the shadow follows in time.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow moves in time with the swing, stretching and shortening as the seat rises and falls.
  - fail: It is still while the swing moves; or it swings out of time; or it keeps one length while the seat plainly rises.
- P2 [core · shape_identity]
  - expect: The shadow keeps the seat and chains' outline and stays joined to the frame's shadow.
  - fail: It is a different shape; or the chains' shadow detaches from the seat's; or it splits.
- P3 [major · missing_consequence]
  - expect: The shadow lies on the side away from the sun.
  - fail: It lies toward the sun; or switches sides; or it is missing in sunlight.
- P4 [major · causeless_motion]
  - expect: The swing dies down and the shadow with it; nothing else moves the shadow.
  - fail: The shadow swings with the seat still; or it swings harder as the seat dies down.
- P5 [fatal · permanence_count]
  - expect: One swing and one shadow.
  - fail: A second seat or shadow appears; or the seat vanishes; or the shadow becomes solid; or a chain detaches.
- P6 [minor · attribute_drift]
  - expect: The swing and the playground stay the same, and the shadow stays dark.
  - fail: The seat changes colour; or the shadow turns coloured; or the ground changes.

## OPT-0025 · shadow · train

**Caption.** A drone hovers over a sunlit parking lot and then flies to one side, and its small shadow on the asphalt moves with it.

**Expectation (hidden).** The shadow stays beneath the drone offset away from the sun, moves when the drone moves, and shows the shape of the drone's arms.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A drone hovers over a sunlit parking lot.
- S2 [core] It flies to one side.
- S3 [core] Its small shadow on the asphalt moves with it.
- S4 [minor] The shadow shows the shape of the drone's arms.
- S5 [minor] The drone moves first and the shadow follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow stays beneath the drone, offset away from the sun, and moves when the drone moves.
  - fail: It stays still while the drone flies; or moves the opposite way; or lies toward the sun.
- P2 [core · shape_identity]
  - expect: The shadow shows the drone's arms and body.
  - fail: It is a plain blob unlike the drone; or a different shape; or it splits.
- P3 [major · causeless_motion]
  - expect: The shadow does not move on its own.
  - fail: It moves with the drone hovering still; or it drifts across the asphalt by itself.
- P4 [major · gravity_direction]
  - expect: The shadow lies on the ground; the drone stays in the air while its rotors run.
  - fail: The shadow rises off the ground; or the drone drops with the rotors running; or it climbs while descending.
- P5 [fatal · permanence_count]
  - expect: One drone and one shadow.
  - fail: A second drone or shadow appears; or the drone vanishes; or the shadow becomes solid; or an arm detaches.
- P6 [minor · attribute_drift]
  - expect: The drone's colour and the lot stay the same, and the shadow stays dark.
  - fail: The drone changes colour; or the shadow turns coloured; or the lot markings shift.

## OPT-0026 · shadow · train

**Caption.** A pigeon lands on a sunny square, and as it touches down its shadow on the paving joins it at its feet.

**Expectation (hidden).** The shadow is on the ground before the bird lands and the two meet at the moment of landing; the shadow lies away from the sun.

**Declared violation types.** missing_consequence, gravity_direction

**SA**
- S1 [core] A pigeon lands on a sunny square.
- S2 [core] Its shadow is on the paving.
- S3 [core] The shadow joins the bird at its feet as it touches down.
- S4 [minor] The shadow is on the ground before the bird lands.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow is on the ground before the bird lands, and the two meet at the moment of landing.
  - fail: The shadow appears only after landing; or they meet before the feet touch; or the shadow rises to meet the bird.
- P2 [core · gravity_direction]
  - expect: The bird comes down onto the paving and stays.
  - fail: It hovers just above; or bounces back up; or sinks into the paving.
- P3 [major · shape_identity]
  - expect: The shadow keeps the bird's outline, wings folding as the bird's fold.
  - fail: It is a different shape; or its wings stay spread while the bird's fold; or it splits.
- P4 [major · missing_consequence]
  - expect: The shadow lies on the side away from the sun.
  - fail: It lies toward the sun; or switches sides; or it is missing in sunlight.
- P5 [fatal · permanence_count]
  - expect: One pigeon and one shadow.
  - fail: A second bird or shadow appears; or the bird vanishes; or the shadow becomes solid; or a wing detaches.
- P6 [minor · attribute_drift]
  - expect: The plumage and the paving stay the same, and the shadow stays dark.
  - fail: The plumage changes; or the shadow turns coloured; or the paving changes.

**Note.** Self-driven animal: where it goes and how it moves are not judged. Only the shadow's relation to it is.

## OPT-0027 · shadow · train

**Caption.** The curtains of a sunny window are pulled open, and the shadow of the window frame appears on the floor.

**Expectation (hidden).** A bright patch with the dark bars of the frame inside it appears on the floor as the curtains open, on the side away from the window, and the bars match the frame's layout; the pattern vanishes when the curtains close.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] The curtains of a sunny window are pulled open.
- S2 [core] The shadow of the window frame appears on the floor.
- S3 [minor] The bars of the frame's shadow match the frame's layout.
- S4 [minor] The curtains open first and the pattern appears with them.

**PC**
- P1 [core · missing_consequence]
  - expect: A bright patch with the dark bars of the frame appears on the floor as the curtains open, on the side away from the window.
  - fail: The pattern is there with the curtains shut; or it appears on the window side; or the curtains open and no pattern appears in sunlight.
- P2 [core · shape_identity]
  - expect: The bars match the frame's layout.
  - fail: The bars are a different pattern from the frame; or there are more bars than the frame has; or the pattern is a solid shape.
- P3 [major · causeless_motion]
  - expect: The pattern does not move on its own.
  - fail: It slides across the floor with the curtains still; or it appears and vanishes with no curtain movement.
- P4 [major · process_direction]
  - expect: The patch widens as the curtains open and would narrow as they close.
  - fail: It narrows as the curtains open; or it is full width before the curtains move; or it flickers.
- P5 [fatal · permanence_count]
  - expect: One window and one pattern of it.
  - fail: A second window's pattern appears; or the frame vanishes; or the pattern becomes solid; or the curtains pass through the frame.
- P6 [minor · attribute_drift]
  - expect: The curtains, the frame and the floor stay the same, and the bars stay dark.
  - fail: The curtains change colour; or the bars turn coloured; or the floor changes.

## OPT-0028 · shadow · train

**Caption.** A hand is held in front of a projector lens, and a dark hand shape covers part of the picture on the screen.

**Expectation (hidden).** The dark shape matches the hand, is much larger than the hand, and disappears the moment the hand is withdrawn.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A projector shows a picture on a screen.
- S2 [core] A hand is held in front of the lens.
- S3 [core] A dark hand shape covers part of the picture on the screen.
- S4 [minor] The dark shape is much larger than the hand.
- S5 [minor] The dark shape disappears when the hand is withdrawn.

**PC**
- P1 [core · shape_identity]
  - expect: The dark shape matches the hand and changes the instant the fingers move.
  - fail: It is a different shape from the hand; or it stays fixed while the fingers move; or it changes while the hand is still.
- P2 [core · missing_consequence]
  - expect: The dark shape appears only while the hand is in the beam and disappears the moment the hand is withdrawn.
  - fail: It lingers after the hand is gone; or it appears with the hand outside the beam; or it appears before the hand enters.
- P3 [major · causeless_motion]
  - expect: The dark shape does not move on its own.
  - fail: It drifts across the screen with the hand still; or it moves before the hand.
- P4 [major · shape_identity]
  - expect: The dark shape is much larger than the hand and has a soft edge.
  - fail: It is smaller than the hand; or has a hard geometric edge unlike a hand; or it splits into unrelated pieces.
- P5 [fatal · permanence_count]
  - expect: One hand and one dark shape.
  - fail: A second dark shape appears under one beam; or the hand loses a finger; or the shape becomes solid; or the hand passes through the lens.
- P6 [minor · attribute_drift]
  - expect: The picture and the screen stay the same, and the shape stays dark.
  - fail: The picture changes with no click; or the shape turns bright; or the screen changes.

**Note.** The hand is the object blocking the beam; the person is not judged.

## OPT-0029 · shadow · train

**Caption.** A fox trots toward a streetlamp at night, and its shadow behind it shrinks until it is directly under the light.

**Expectation (hidden).** The shadow trails behind the fox on the side away from the lamp and shortens steadily as it approaches; it does not grow or move ahead of the fox.

**Declared violation types.** missing_consequence, trajectory_momentum

**SA**
- S1 [core] A fox trots toward a streetlamp at night.
- S2 [core] Its shadow is behind it.
- S3 [core] The shadow shrinks until the fox is directly under the light.
- S4 [minor] The shadow shortens steadily as the fox approaches.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow trails behind the fox on the side away from the lamp and shortens steadily as it approaches.
  - fail: It grows as the fox approaches; or it moves ahead of the fox toward the lamp; or it stays one length.
- P2 [core · trajectory_momentum]
  - expect: The fox moves steadily toward the lamp and the shadow shortens in step.
  - fail: The shadow shortens with the fox still; or the fox moves and the shadow keeps its length; or the shadow jumps.
- P3 [major · shape_identity]
  - expect: The shadow keeps the fox's outline with legs moving in step.
  - fail: It is a different shape; or its legs are still while the fox's move; or it splits.
- P4 [major · missing_consequence]
  - expect: The shadow is attached at the paws and lies on the ground.
  - fail: It floats detached; or it climbs a wall the lamp cannot cast onto; or it is missing under the lamp's light.
- P5 [fatal · permanence_count]
  - expect: One fox and one shadow.
  - fail: A second fox or shadow appears; or the fox vanishes; or the shadow becomes solid; or the fox passes through the lamp post.
- P6 [minor · attribute_drift]
  - expect: The fox's coat and the street stay the same, and the shadow stays dark.
  - fail: The coat changes colour; or the shadow turns coloured; or the lamp changes.

**Note.** Self-driven animal: where it goes and how it moves are not judged. Only the shadow's relation to it is.

## OPT-0030 · shadow · train

**Caption.** A flag flutters on a pole in the sun, and its shadow flutters on the wall behind it.

**Expectation (hidden).** The shadow moves in time with the cloth, on the wall away from the sun, and stops when the flag hangs still.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A flag flutters on a pole in the sun.
- S2 [core] Its shadow flutters on the wall behind it.
- S3 [minor] The shadow moves in time with the cloth.
- S4 [minor] The shadow stops when the flag hangs still.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow moves in time with the cloth and stops when the flag hangs still.
  - fail: It is still while the flag flutters; or it flutters while the flag hangs still; or it moves out of time.
- P2 [core · shape_identity]
  - expect: The shadow keeps the flag's outline, rippling as the flag ripples.
  - fail: It is a different shape; or a rigid rectangle while the flag ripples; or it splits.
- P3 [major · missing_consequence]
  - expect: The shadow lies on the wall away from the sun, joined to the pole's shadow.
  - fail: It lies toward the sun; or detached from the pole's shadow; or it is missing in sunlight.
- P4 [major · causeless_motion]
  - expect: The flag moves only with the wind, and the shadow only with the flag.
  - fail: The flag whips in still air; or the shadow moves before the flag; or the shadow drifts along the wall by itself.
- P5 [fatal · permanence_count]
  - expect: One flag, one pole and one shadow.
  - fail: A second flag or shadow appears; or the flag vanishes; or the shadow becomes solid; or the flag passes through the pole.
- P6 [minor · attribute_drift]
  - expect: The flag's colours and the wall stay the same, and the shadow stays dark.
  - fail: The flag changes colours; or the shadow turns coloured; or the wall changes.

## OPT-0031 · shadow · train

**Caption.** A cat walks along a sunlit windowsill inside a house, and its shadow moves across the floor of the room.

**Expectation (hidden).** The shadow moves with the cat, falls on the room side away from the window, and shows the cat's outline including the tail.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A cat walks along a sunlit windowsill inside a house.
- S2 [core] Its shadow moves across the floor of the room.
- S3 [minor] The shadow shows the cat's outline including the tail.
- S4 [minor] The shadow falls on the room side, away from the window.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow moves with the cat and falls on the room side away from the window.
  - fail: It is still while the cat walks; or it falls on the window side; or it moves the opposite way.
- P2 [core · shape_identity]
  - expect: The shadow shows the cat's outline including the tail, legs moving in step.
  - fail: It is a different shape; or the tail is missing while the cat's is plain; or it splits.
- P3 [major · causeless_motion]
  - expect: The shadow does not move on its own.
  - fail: It moves with the cat sitting still; or it drifts across the floor by itself.
- P4 [major · missing_consequence]
  - expect: The shadow is stretched across the floor by the low angle and does not float.
  - fail: It floats above the floor; or it is a tiny patch under a plainly low sun; or it is missing in sunlight.
- P5 [fatal · permanence_count]
  - expect: One cat and one shadow.
  - fail: A second cat or shadow appears; or the cat vanishes; or the shadow becomes solid; or the cat passes through the glass.
- P6 [minor · attribute_drift]
  - expect: The cat's markings and the room stay the same, and the shadow stays dark.
  - fail: The markings change; or the shadow turns coloured; or the room rearranges.

**Note.** Self-driven animal: where it goes and how it moves are not judged. Only the shadow's relation to it is.

## OPT-0032 · shadow · train

**Caption.** A book is held up between a lamp and a wall, and a rectangular shadow appears on the wall; as the book is tilted the shadow narrows.

**Expectation (hidden).** The shadow appears where the book blocks the light and changes shape as the book turns; it does not remain a full rectangle when the book is edge-on.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A book is held up between a lamp and a wall.
- S2 [core] A rectangular shadow appears on the wall.
- S3 [core] The book is tilted.
- S4 [core] The shadow narrows.
- S5 [minor] The tilt comes first and the shadow narrows with it.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow appears where the book blocks the light and changes shape as the book turns.
  - fail: The shadow stays a full rectangle when the book is edge-on; or it changes with the book still; or it is missing with the lamp on.
- P2 [core · shape_identity]
  - expect: The shadow is the book's outline: a rectangle face-on, narrowing to a bar edge-on.
  - fail: It is a different shape from the book; or it widens as the book turns edge-on; or it splits.
- P3 [major · missing_consequence]
  - expect: The shadow is on the wall behind the book, away from the lamp.
  - fail: It is between the book and the lamp; or on the ceiling; or it is missing.
- P4 [major · causeless_motion]
  - expect: The shadow moves only as the book moves.
  - fail: It drifts with the book still; or it moves before the book; or it lingers after the book is lowered.
- P5 [fatal · permanence_count]
  - expect: One book, one lamp and one shadow.
  - fail: A second shadow appears under one lamp; or the book vanishes; or the shadow becomes solid; or the hand passes through the book.
- P6 [minor · attribute_drift]
  - expect: The book's cover and the wall stay the same, and the shadow stays dark.
  - fail: The cover changes; or the shadow turns coloured; or the wall changes.

**Note.** The hand holding the book is the minimal trigger; the person is not judged.

## OPT-0033 · shadow · train

**Caption.** A robot vacuum travels the length of a corridor lit by a single ceiling light, and its shadow on the floor changes side as it passes beneath the light.

**Expectation (hidden).** The shadow is ahead of the vacuum before the light and behind it after, always pointing away from the bulb.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A robot vacuum travels the length of a corridor.
- S2 [core] The corridor is lit by a single ceiling light.
- S3 [core] Its shadow on the floor changes side as it passes beneath the light.
- S4 [minor] The shadow is ahead before the light and behind after.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow is ahead of the vacuum before the light and behind it after, always pointing away from the bulb.
  - fail: It stays on one side the whole way; or points toward the bulb; or switches sides at the wrong place.
- P2 [core · shape_identity]
  - expect: The shadow keeps the vacuum's round outline, short beneath the light and longer away from it.
  - fail: It is a different shape; or one length throughout; or it splits.
- P3 [major · causeless_motion]
  - expect: The vacuum moves steadily and the shadow only with it.
  - fail: The shadow moves with the vacuum stopped; or the vacuum jumps position; or the shadow drifts.
- P4 [major · missing_consequence]
  - expect: The shadow is attached at the vacuum's base and lies on the floor.
  - fail: It floats detached; or it appears on the ceiling; or it is missing under the light.
- P5 [fatal · permanence_count]
  - expect: One vacuum, one light and one shadow.
  - fail: A second shadow appears under one light; or the vacuum vanishes; or the shadow becomes solid; or the vacuum passes through a wall.
- P6 [minor · attribute_drift]
  - expect: The vacuum and the corridor stay the same, and the shadow stays dark.
  - fail: The vacuum changes colour; or the shadow turns coloured; or the corridor changes.

## OPT-0034 · shadow · train

**Caption.** A remote-controlled car launches off a small ramp in the sun, and its shadow stays on the ground while it is airborne and rejoins it on landing.

**Expectation (hidden).** The shadow stays on the ground while the car is in the air, separated from it, and meets the wheels at the moment of landing.

**Declared violation types.** missing_consequence, gravity_direction

**SA**
- S1 [core] A remote-controlled car launches off a small ramp in the sun.
- S2 [core] Its shadow stays on the ground while it is airborne.
- S3 [core] The shadow rejoins the car on landing.
- S4 [minor] The launch comes first, then the separation, then the rejoining.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow stays on the ground while the car is in the air, separated from it, and meets the wheels at the moment of landing.
  - fail: The shadow rises with the car; or stays attached in mid-air; or fails to meet the wheels on landing.
- P2 [core · gravity_direction]
  - expect: The car rises off the ramp, arcs, and comes down.
  - fail: It hangs in the air; or keeps rising; or drops straight down off the ramp.
- P3 [major · shape_identity]
  - expect: The shadow keeps the car's outline.
  - fail: It is a different shape; or splits; or streaks.
- P4 [major · missing_consequence]
  - expect: The shadow lies on the side away from the sun.
  - fail: It lies toward the sun; or switches sides in flight; or it is missing in sunlight.
- P5 [fatal · permanence_count]
  - expect: One car, one ramp and one shadow.
  - fail: A second car or shadow appears; or the car vanishes; or the shadow becomes solid; or the car passes through the ramp.
- P6 [minor · attribute_drift]
  - expect: The car's colour and the ground stay the same, and the shadow stays dark.
  - fail: The car changes colour; or the shadow turns coloured; or the ramp changes.

## OPT-0035 · shadow · train

**Caption.** A toy car is lifted off a sunlit table, and its shadow stays on the table and grows fainter as the car is raised higher.

**Expectation (hidden).** The shadow separates from the car as it lifts and remains on the surface; it does not rise with the car.

**Declared violation types.** missing_consequence, gravity_direction

**SA**
- S1 [core] A toy car sits on a sunlit table.
- S2 [core] It is lifted off the table.
- S3 [core] Its shadow stays on the table.
- S4 [core] The shadow grows fainter as the car is raised higher.
- S5 [minor] The lift comes first and the shadow separates as the car rises.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow separates from the car as it lifts and remains on the surface, on the side away from the sun.
  - fail: The shadow rises with the car; or stays attached to the wheels in mid-air; or vanishes the instant the car lifts.
- P2 [core · process_direction]
  - expect: The shadow gets fainter and softer the higher the car is raised.
  - fail: It gets sharper and darker as the car rises; or stays the same at every height; or flickers.
- P3 [major · shape_identity]
  - expect: The shadow keeps the car's outline, blurring as it fades.
  - fail: It is a different shape; or splits; or sharpens into a different object.
- P4 [major · gravity_direction]
  - expect: The car rises only as the hand lifts it, and the shadow stays down on the table.
  - fail: The car floats up on its own; or the shadow lifts off the table; or the car sinks into the table.
- P5 [fatal · permanence_count]
  - expect: One car and one shadow.
  - fail: A second car or shadow appears; or the car vanishes; or the shadow becomes solid; or the hand passes through the car.
- P6 [minor · attribute_drift]
  - expect: The car's colour and the table stay the same, and the shadow stays dark.
  - fail: The car changes colour; or the shadow turns coloured; or the table changes.

**Note.** The hand lifting is the minimal trigger; the person is not judged.

## OPT-0036 · shadow · train

**Caption.** A garden hose sprays an arc of water in the evening sun, and the shadow of the arc falls on the soil beside it.

**Expectation (hidden).** The shadow follows the curve of the stream and lands on the side away from the sun; it flickers as the water moves and disappears when the tap is closed.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A garden hose sprays an arc of water in the evening sun.
- S2 [core] The shadow of the arc falls on the soil beside it.
- S3 [minor] The shadow follows the curve of the stream.
- S4 [minor] The shadow flickers as the water moves.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow follows the curve of the stream and lands on the side away from the sun.
  - fail: It lies toward the sun; or it is a straight line under a curved stream; or it is missing in sunlight.
- P2 [core · shape_identity]
  - expect: The shadow keeps the arc's shape and flickers as the water moves.
  - fail: It is rigid and unflickering while the water plainly moves; or it is a different shape; or it splits into unrelated pieces.
- P3 [major · causeless_motion]
  - expect: The shadow moves only as the stream moves and would vanish if the tap were closed.
  - fail: It moves with the stream steady; or it stays after the water stops; or it appears before the water.
- P4 [major · gravity_direction]
  - expect: The stream arcs and falls, and the shadow lies on the soil.
  - fail: The stream curves upward; or the shadow stands up off the soil; or the water hangs.
- P5 [fatal · permanence_count]
  - expect: One hose and one stream with its shadow.
  - fail: A second stream appears; or the shadow becomes solid; or water appears from nowhere.
- P6 [minor · attribute_drift]
  - expect: The hose and the garden stay the same, and the shadow stays dark.
  - fail: The hose changes colour; or the shadow turns coloured; or the garden rearranges.

## OPT-0037 · shadow · train

**Caption.** Two lamps light a statue on a table from different sides, and the statue casts two shadows in different directions.

**Expectation (hidden).** Each shadow points away from one lamp; when one lamp is switched off its shadow vanishes and the other remains.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A statue stands on a table.
- S2 [core] Two lamps light it from different sides.
- S3 [core] The statue casts two shadows in different directions.
- S4 [minor] Each shadow points away from one lamp.

**PC**
- P1 [core · missing_consequence]
  - expect: Each shadow points away from one lamp, and the two lie in different directions.
  - fail: Both shadows lie on the same side; or a shadow points toward its lamp; or there is only one shadow under two lamps.
- P2 [core · permanence_count]
  - expect: There are exactly two shadows for two lamps, and if a lamp is switched off its shadow vanishes while the other remains.
  - fail: A third shadow appears; or a shadow remains with its lamp off; or both vanish when one lamp goes off.
- P3 [major · shape_identity]
  - expect: Each shadow keeps the statue's outline.
  - fail: A shadow is a different shape; or one splits; or the two merge into one blob while the lamps are plainly on different sides.
- P4 [major · causeless_motion]
  - expect: The shadows do not move with the statue and lamps still.
  - fail: A shadow drifts by itself; or swings round with nothing moving; or changes length.
- P5 [fatal · permanence_count]
  - expect: One statue and two lamps.
  - fail: The statue duplicates or vanishes; or a lamp vanishes; or a shadow becomes solid; or the statue passes through the table.
- P6 [minor · attribute_drift]
  - expect: The statue, the lamps and the table stay the same, and the shadows stay dark.
  - fail: The statue changes colour; or a shadow turns coloured; or the table changes.

## OPT-0038 · shadow · train

**Caption.** A park bench stands beside a wall at dusk as the streetlights come on, and a shadow of the bench appears on the wall away from the nearest light.

**Expectation (hidden).** The shadow appears only when the lights come on and points away from the lamp that lit up; it does not appear before the light.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A park bench stands beside a wall at dusk.
- S2 [core] The streetlights come on.
- S3 [core] A shadow of the bench appears on the wall, away from the nearest light.
- S4 [minor] The shadow appears only when the lights come on.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow appears only when the lights come on and points away from the lamp that lit up.
  - fail: It is there before the lights; or it points toward the lamp; or the lights come on and no shadow appears.
- P2 [core · shape_identity]
  - expect: The shadow keeps the bench's outline, slats and legs.
  - fail: It is a different shape; or splits under one lamp; or it is a plain blob.
- P3 [major · causeless_motion]
  - expect: The shadow does not move with the bench and lamp fixed.
  - fail: It drifts across the wall; or swings round; or changes length.
- P4 [major · missing_consequence]
  - expect: The shadow is attached at the bench's legs and lies on the wall and ground behind it.
  - fail: It floats detached; or appears on the lamp side; or it is missing with the lamp on.
- P5 [fatal · permanence_count]
  - expect: One bench and one shadow per lamp.
  - fail: The bench duplicates or vanishes; or the shadow becomes solid; or the bench passes through the wall.
- P6 [minor · attribute_drift]
  - expect: The bench and the wall stay the same, and the shadow stays dark.
  - fail: The bench changes colour; or the shadow turns coloured; or the wall changes.

## OPT-0039 · shadow · train

**Caption.** A horse trots across a sunlit paddock, and its shadow trots along the grass beside it, legs moving in step.

**Expectation (hidden).** The shadow's legs move in time with the horse's, it stays attached at the hooves, and it lies away from the sun.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A horse trots across a sunlit paddock.
- S2 [core] Its shadow trots along the grass beside it.
- S3 [core] The shadow's legs move in step with the horse's.
- S4 [minor] The shadow stays attached at the hooves.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow's legs move in time with the horse's and it stays attached at the hooves.
  - fail: The shadow's legs are still while the horse's move; or it lags or leads; or it is detached from the hooves on flat ground.
- P2 [core · shape_identity]
  - expect: The shadow keeps the horse's outline, head, legs and tail.
  - fail: It is a different animal's shape; or splits; or loses a leg the horse still has.
- P3 [major · missing_consequence]
  - expect: The shadow lies on the side away from the sun.
  - fail: It lies toward the sun; or switches sides with the sun fixed; or it is missing in sunlight.
- P4 [major · causeless_motion]
  - expect: The shadow does not move on its own.
  - fail: It moves with the horse standing still; or drifts across the grass by itself.
- P5 [fatal · permanence_count]
  - expect: One horse and one shadow.
  - fail: A second horse or shadow appears; or the horse vanishes; or the shadow becomes solid; or the horse passes through the fence.
- P6 [minor · attribute_drift]
  - expect: The horse's coat and the paddock stay the same, and the shadow stays dark.
  - fail: The coat changes colour; or the shadow turns coloured; or the paddock changes.

**Note.** Self-driven animal: where it goes and how it moves are not judged. Only the shadow's relation to it is.

## OPT-0040 · shadow · train

**Caption.** A pendulum swings in front of a wall lit by a lamp, and its shadow on the wall swings with it.

**Expectation (hidden).** The shadow moves in step with the pendulum, in the same rhythm, and never leads it or moves on its own; it falls on the wall on the side away from the lamp, and the string's shadow stays joined to the shadow of the pivot; when the pendulum stops, the shadow stops.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A pendulum swings in front of a wall.
- S2 [core] A lamp lights the wall.
- S3 [core] The pendulum's shadow on the wall swings with it.
- S4 [minor] The shadow moves in the same rhythm as the pendulum.
- S5 [minor] When the pendulum stops the shadow stops.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow moves in step with the pendulum, in the same rhythm, and never leads it or moves on its own.
  - fail: It swings out of time; or it leads the pendulum; or it swings while the pendulum hangs still.
- P2 [core · shape_identity]
  - expect: The string's shadow stays joined to the shadow of the pivot and the bob's shadow to the string's.
  - fail: The bob's shadow detaches from the string's; or the pivot's shadow moves; or the shadow splits.
- P3 [major · missing_consequence]
  - expect: The shadow falls on the wall on the side away from the lamp.
  - fail: It falls on the lamp side; or on the ceiling; or it is missing with the lamp on.
- P4 [major · material_response]
  - expect: The string stays taut and straight through the swing.
  - fail: It goes slack at the ends; or bends mid-length; or stretches.
- P5 [fatal · permanence_count]
  - expect: One pendulum and one shadow.
  - fail: A second bob or shadow appears; or the bob vanishes; or the shadow becomes solid; or the string passes through the bob.
- P6 [minor · attribute_drift]
  - expect: The pendulum and the wall stay the same, and the shadow stays dark.
  - fail: The bob changes colour; or the shadow turns coloured; or the wall changes.

## OPT-0041 · shadow · train

**Caption.** A dog walks between a campfire and a tent at night, and a huge shadow of the dog sweeps across the tent wall.

**Expectation (hidden).** The shadow is on the tent side away from the fire, is larger than the dog, and moves the opposite way to the dog as it approaches the fire; it flickers with the flames.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A campfire burns at night beside a tent.
- S2 [core] A dog walks between the fire and the tent.
- S3 [core] A huge shadow of the dog sweeps across the tent wall.
- S4 [minor] The shadow is larger than the dog.
- S5 [minor] The shadow flickers with the flames.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow is on the tent side away from the fire and moves as the dog moves.
  - fail: It is on the fire side; or it stays still while the dog walks; or it is missing with the fire lit.
- P2 [core · shape_identity]
  - expect: The shadow keeps the dog's outline, larger than the dog and flickering with the flames.
  - fail: It is a different animal's shape; or smaller than the dog; or rigid and unflickering while the flames plainly move.
- P3 [major · trajectory_momentum]
  - expect: The shadow moves the opposite way to the dog across the tent wall as the dog approaches the fire.
  - fail: It moves the same way; or stays put; or jumps.
- P4 [major · causeless_motion]
  - expect: The shadow does not move except with the dog and the flames.
  - fail: It sweeps with the dog still and the flames steady; or it moves before the dog.
- P5 [fatal · permanence_count]
  - expect: One dog, one fire and one shadow.
  - fail: A second dog or shadow appears; or the dog vanishes; or the shadow becomes solid; or the dog passes through the tent.
- P6 [minor · attribute_drift]
  - expect: The dog's coat and the tent stay the same, and the shadow stays dark.
  - fail: The coat changes colour; or the shadow turns coloured; or the tent changes.

**Note.** Self-driven animal: where it goes and how it moves are not judged. Only the shadow's relation to it is.

## OPT-0042 · shadow · train

**Caption.** A bus passes a row of parked cars on a sunny street, and its shadow slides over the cars one after another.

**Expectation (hidden).** The shadow moves at the bus's speed and darkens each car as it passes; it does not appear on the sunlit side of the bus.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A bus passes a row of parked cars on a sunny street.
- S2 [core] Its shadow slides over the cars one after another.
- S3 [minor] The shadow darkens each car as it passes.
- S4 [minor] The shadow moves at the bus's speed.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow moves at the bus's speed and darkens each car in turn as it passes.
  - fail: It lags or leads; or a car stays dark after the bus has passed; or a car darkens before the shadow reaches it.
- P2 [core · shape_identity]
  - expect: The shadow keeps the bus's outline, draping over the cars' shapes.
  - fail: It is a different shape; or splits; or the cars change shape under it.
- P3 [major · missing_consequence]
  - expect: The shadow lies on the side away from the sun and does not appear on the sunlit side of the bus.
  - fail: It lies toward the sun; or on both sides; or it is missing in sunlight.
- P4 [major · causeless_motion]
  - expect: The parked cars stay still and the shadow moves only with the bus.
  - fail: A car moves; or the shadow moves with the bus stopped; or the shadow drifts.
- P5 [fatal · permanence_count]
  - expect: One bus and one shadow, and the cars keep their number.
  - fail: A second bus appears; or a car vanishes; or the shadow becomes solid; or the bus passes through a car.
- P6 [minor · attribute_drift]
  - expect: The bus's livery and the cars stay the same, and the shadow stays dark.
  - fail: The livery changes; or the shadow turns coloured; or a car changes colour rather than brightness.

## OPT-0043 · shadow · train

**Caption.** A leaf is held up against the sun, and its shadow falls on the ground below.

**Expectation (hidden).** The shadow has the leaf's outline, lies on the surface below and away from the sun, and moves when the leaf moves.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A leaf is held up against the sun.
- S2 [core] Its shadow falls on the ground below.
- S3 [minor] The shadow has the leaf's outline.
- S4 [minor] The shadow moves when the leaf moves.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow lies on the surface below, away from the sun, and moves when the leaf moves.
  - fail: It lies toward the sun; or stays still while the leaf moves; or it is missing in sunlight.
- P2 [core · shape_identity]
  - expect: The shadow has the leaf's outline.
  - fail: It is a different shape; or splits; or it is a plain blob unlike the leaf.
- P3 [major · causeless_motion]
  - expect: The shadow does not move on its own.
  - fail: It drifts with the leaf still; or moves before the leaf.
- P4 [major · missing_consequence]
  - expect: The shadow is joined to the shadow of the hand or stem holding the leaf.
  - fail: The leaf's shadow floats with no shadow of what holds it; or it is separated from the hand's shadow.
- P5 [fatal · permanence_count]
  - expect: One leaf and one shadow.
  - fail: A second leaf or shadow appears; or the leaf vanishes; or the shadow becomes solid.
- P6 [minor · attribute_drift]
  - expect: The leaf's colour and the ground stay the same, and the shadow stays dark.
  - fail: The leaf changes colour; or the shadow turns coloured; or the ground changes.

**Note.** The hand holding the leaf is the minimal trigger; the person is not judged.

## OPT-0044 · shadow · train

**Caption.** A car drives along a road with the morning sun on its left, and its shadow runs along the ground on its right.

**Expectation (hidden).** The shadow stays on the car's right, attached at the wheels, and moves with the car; it does not switch sides while the sun stays put.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A car drives along a road.
- S2 [core] The morning sun is on its left.
- S3 [core] Its shadow runs along the ground on its right.
- S4 [minor] The shadow stays attached at the wheels.
- S5 [minor] The shadow moves with the car.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow stays on the car's right, attached at the wheels, and moves with the car.
  - fail: It is on the left with the sun on the left; or it switches sides while the sun stays put; or it lags or is detached.
- P2 [core · shape_identity]
  - expect: The shadow keeps the car's outline and its wheels turn in step.
  - fail: It is a different vehicle's shape; or its wheels are still; or it splits.
- P3 [major · causeless_motion]
  - expect: The shadow does not move on its own.
  - fail: It moves with the car stopped; or changes length with the car still.
- P4 [major · trajectory_momentum]
  - expect: The car travels steadily along the road.
  - fail: It jumps position; or moves backward; or swerves with no cause.
- P5 [fatal · permanence_count]
  - expect: One car and one shadow.
  - fail: A second car or shadow appears; or the car vanishes; or the shadow becomes solid; or the car passes through a sign.
- P6 [minor · attribute_drift]
  - expect: The car's colour and the road stay the same, and the shadow stays dark.
  - fail: The car changes colour; or the shadow turns coloured; or the road markings shift.

## OPT-0045 · shadow · train

**Caption.** A tree sways in the wind on a sunny day, and the pattern of leaf shadows on the ground beneath it shifts and dances.

**Expectation (hidden).** The shadow pattern moves in time with the branches and settles when the wind drops; it lies on the ground away from the sun.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A tree sways in the wind on a sunny day.
- S2 [core] The pattern of leaf shadows on the ground beneath it shifts and dances.
- S3 [minor] The pattern settles when the wind drops.
- S4 [minor] The pattern lies on the ground away from the sun.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow pattern moves in time with the branches and settles when the wind drops.
  - fail: It is still while the branches sway; or it dances while the tree is still; or it moves out of time.
- P2 [core · shape_identity]
  - expect: The pattern is dappled light and leaf-shaped shadows, not a solid shape.
  - fail: It is one solid disc; or a geometric pattern unlike leaves; or it forms a recognisable object.
- P3 [major · missing_consequence]
  - expect: The pattern lies on the ground away from the sun, under the tree's crown.
  - fail: It lies toward the sun; or far from the tree; or it is missing in sunlight.
- P4 [major · causeless_motion]
  - expect: The branches move only with the wind.
  - fail: They whip about in still air; or move against other wind signs; or a branch detaches.
- P5 [fatal · permanence_count]
  - expect: One tree with its branches.
  - fail: The tree duplicates or vanishes; or a branch vanishes; or the shadow pattern becomes solid.
- P6 [minor · attribute_drift]
  - expect: The tree's leaves and the ground stay the same, and the shadows stay dark.
  - fail: The leaves change colour; or the shadows turn coloured; or the ground changes.

## OPT-0046 · shadow · train

**Caption.** A lamppost on a pier casts its shadow onto the water below, and the shadow rides the ripples.

**Expectation (hidden).** The shadow lies on the water surface away from the sun and wobbles with the waves; it stays attached to the base of the post.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A lamppost stands on a pier.
- S2 [core] It casts its shadow onto the water below.
- S3 [core] The shadow rides the ripples.
- S4 [minor] The shadow stays attached to the base of the post.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow lies on the water surface away from the sun and stays attached to the base of the post.
  - fail: It lies toward the sun; or it detaches from the post's base; or it is missing in sunlight.
- P2 [core · shape_identity]
  - expect: The shadow keeps the post's long outline and wobbles with the waves.
  - fail: It is rigid and straight on a plainly rippled surface; or a different shape; or it splits into pieces unrelated to the ripples.
- P3 [major · causeless_motion]
  - expect: The post stays still and the shadow moves only with the water.
  - fail: The post sways; or the shadow moves on a flat calm; or the shadow swings round.
- P4 [major · material_response]
  - expect: The ripples pass and the water surface stays liquid.
  - fail: The water is rigid like glass with a wobbling shadow; or the ripples freeze; or the water flows uphill.
- P5 [fatal · permanence_count]
  - expect: One lamppost and one shadow.
  - fail: A second post or shadow appears; or the post vanishes; or the shadow becomes solid; or the post passes through the pier.
- P6 [minor · attribute_drift]
  - expect: The post and the pier stay the same, and the shadow stays dark.
  - fail: The post changes colour; or the shadow turns coloured; or the pier changes.

## OPT-0047 · shadow · train

**Caption.** A cat walks along the base of a sunlit wall, and its shadow walks along the wall beside it.

**Expectation (hidden).** The shadow on the wall keeps pace, its paws at ground level; it lies on the side away from the sun.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A cat walks along the base of a sunlit wall.
- S2 [core] Its shadow walks along the wall beside it.
- S3 [minor] The shadow's paws are at ground level.
- S4 [minor] The shadow lies on the side away from the sun.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow on the wall keeps pace with the cat, its paws at ground level.
  - fail: It lags or leads; or its paws float up the wall; or it is still while the cat walks.
- P2 [core · shape_identity]
  - expect: The shadow keeps the cat's outline, legs moving in step.
  - fail: It is a different animal's shape; or its legs are still; or it splits.
- P3 [major · missing_consequence]
  - expect: The shadow lies on the side away from the sun.
  - fail: It lies toward the sun; or switches sides; or it is missing in sunlight.
- P4 [major · causeless_motion]
  - expect: The shadow does not move on its own.
  - fail: It moves with the cat sitting; or drifts along the wall by itself.
- P5 [fatal · permanence_count]
  - expect: One cat and one shadow.
  - fail: A second cat or shadow appears; or the cat vanishes; or the shadow becomes solid; or the cat passes through the wall.
- P6 [minor · attribute_drift]
  - expect: The cat's markings and the wall stay the same, and the shadow stays dark.
  - fail: The markings change; or the shadow turns coloured; or the wall changes.

**Note.** Self-driven animal: where it goes and how it moves are not judged. Only the shadow's relation to it is.

## OPT-0048 · shadow · train

**Caption.** A lantern inside a tent is turned up to full brightness, and sharp shadows of the tent poles appear on the canvas.

**Expectation (hidden).** The shadows appear as the lantern brightens and fall away from it; they shift when the lantern is moved and fade when it is dimmed.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A lantern is inside a tent.
- S2 [core] It is turned up to full brightness.
- S3 [core] Sharp shadows of the tent poles appear on the canvas.
- S4 [minor] The shadows appear as the lantern brightens.
- S5 [minor] The shadows fall away from the lantern.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadows appear as the lantern brightens and fall away from it.
  - fail: They are there with the lantern dim; or they point toward the lantern; or the lantern brightens and no shadows appear.
- P2 [core · shape_identity]
  - expect: The shadows are the poles' outlines, one per pole, sharpening as the light strengthens.
  - fail: There are more shadows than poles; or they are unrelated shapes; or they stay blurred at full brightness.
- P3 [major · causeless_motion]
  - expect: The shadows do not move with the lantern and poles fixed, and would shift if the lantern moved.
  - fail: They drift by themselves; or swing round; or change with nothing moving.
- P4 [major · process_direction]
  - expect: The shadows sharpen and darken as the lantern is turned up, and would fade if it were dimmed.
  - fail: They fade as the lantern brightens; or flicker with a steady lantern; or appear fully sharp before the lantern is turned up.
- P5 [fatal · permanence_count]
  - expect: One lantern and the tent's poles.
  - fail: A pole vanishes; or a second lantern appears; or a shadow becomes solid; or the lantern passes through the canvas.
- P6 [minor · attribute_drift]
  - expect: The canvas and the lantern stay the same, and the shadows stay dark.
  - fail: The canvas changes colour; or the shadows turn coloured; or the lantern changes shape.

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

## OPT-0051 · reflection · train

**Caption.** A mountain stands beside a still lake at dawn, and an upside-down image of the mountain lies on the water.

**Expectation (hidden).** The image is inverted and meets the real mountain at the shoreline; its peak points downward; it blurs where the surface is disturbed.

**Declared violation types.** shape_identity, missing_consequence

**SA**
- S1 [core] A mountain stands beside a still lake at dawn.
- S2 [core] An upside-down image of the mountain lies on the water.
- S3 [minor] The image meets the real mountain at the shoreline.
- S4 [minor] The lake is still.

**PC**
- P1 [core · shape_identity]
  - expect: The image is inverted, its peak pointing downward, and meets the real mountain at the shoreline.
  - fail: The image is upright; or it is offset from the shoreline; or it is a different mountain's outline.
- P2 [core · missing_consequence]
  - expect: The image blurs where the surface is disturbed and is sharp where the water is still.
  - fail: It stays sharp across plain ripples; or blurs on a glassy surface; or it is missing on still water.
- P3 [major · causeless_motion]
  - expect: The image does not move with the mountain and water still.
  - fail: It drifts across the lake; or shifts while the surface is calm; or the mountain moves.
- P4 [major · attribute_drift]
  - expect: The image has the mountain's colours, slightly dimmer.
  - fail: It is a different colour; or brighter than the mountain; or it changes colour on its own.
- P5 [fatal · permanence_count]
  - expect: One mountain and one reflection of it; the reflection stays on the water.
  - fail: A second mountain appears; or the reflection rises off the water; or the mountain vanishes; or the reflection becomes solid.
- P6 [minor · attribute_drift]
  - expect: The sky, the shore and the mountain stay the same.
  - fail: The sky changes colour abruptly; or the shore rearranges; or the mountain changes shape.

## OPT-0052 · reflection · train

**Caption.** A cat walks up to a floor-length mirror and sees another cat approaching it in the glass.

**Expectation (hidden).** The reflected cat approaches as the real cat does, mirrored, and their noses meet at the glass; the reflection cannot step out of the mirror.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A cat walks up to a floor-length mirror.
- S2 [core] Another cat approaches it in the glass.
- S3 [minor] The reflected cat is a mirror image of the real one.
- S4 [minor] Their noses meet at the glass.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflected cat approaches as the real cat does, at the same time and pace, and their noses meet at the glass.
  - fail: The reflection stays still while the cat walks; or moves first or later; or the noses meet away from the glass.
- P2 [core · shape_identity]
  - expect: The reflection is a mirror image: the same cat, same markings, facing the real one across the surface.
  - fail: It is a different cat; or shows the cat's back; or it is a rotated copy with the markings on the wrong side.
- P3 [major · causeless_motion]
  - expect: The reflection does not move on its own.
  - fail: It moves while the cat sits still; or it turns away by itself.
- P4 [major · material_response]
  - expect: The mirror is flat and rigid: the reflection is undistorted.
  - fail: The surface ripples; or the reflection warps while the cat is unchanged; or the mirror bends.
- P5 [fatal · permanence_count]
  - expect: One cat and one reflection; the reflection stays inside the mirror.
  - fail: The reflection steps out of the mirror; or a second cat appears in the room; or the cat passes into the glass; or the cat vanishes.
- P6 [minor · attribute_drift]
  - expect: The cat's markings and the mirror frame stay the same, and the reflection's colours match the cat's.
  - fail: The cat changes colour; or the frame changes; or the reflection's colours drift from the cat's.

**Note.** Self-driven animal: where it goes and how it moves are not judged. Only the reflection's relation to it is. Mirror geometry: each point of the image lies directly across the mirror surface from the real point, so the image is a mirror copy, not a rotated one.

## OPT-0053 · reflection · train

**Caption.** A pigeon walks past a puddle on a pavement, and its reflection passes across the puddle upside down.

**Expectation (hidden).** The reflection appears only within the puddle's edges, moves with the bird, and is inverted; it does not extend onto dry pavement.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A pigeon walks past a puddle on a pavement.
- S2 [core] Its reflection passes across the puddle.
- S3 [core] The reflection is upside down.
- S4 [minor] The reflection appears only within the puddle's edges.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflection appears only within the puddle's edges and moves with the bird.
  - fail: It extends onto dry pavement; or stays still while the bird walks; or it is missing on plainly still water.
- P2 [core · shape_identity]
  - expect: The reflection is inverted, joined at the feet when the bird is at the water's edge.
  - fail: It is upright; or offset from the bird's position; or a different bird's shape.
- P3 [major · causeless_motion]
  - expect: The reflection does not move on its own.
  - fail: It moves while the bird stands still; or it drifts across the puddle.
- P4 [major · material_response]
  - expect: The puddle is liquid: the reflection wavers where the surface is disturbed.
  - fail: It is rigid like glass; or the reflection wavers on a flat calm; or the water flows uphill.
- P5 [fatal · permanence_count]
  - expect: One pigeon and one reflection; the reflection stays on the water.
  - fail: A second bird appears; or the reflection leaves the puddle; or the bird vanishes; or the reflection becomes solid.
- P6 [minor · attribute_drift]
  - expect: The plumage and the pavement stay the same, and the reflection's colours match the bird's.
  - fail: The plumage changes; or the pavement changes; or the reflection's colours drift.

**Note.** Self-driven animal: where it goes and how it moves are not judged. Only the reflection's relation to it is.

## OPT-0054 · reflection · train

**Caption.** A car drives past an office building with a glass front, and the car's reflection glides across the windows.

**Expectation (hidden).** The reflection moves in step with the car and is mirrored; it jumps slightly at the frames between panes and disappears where the glass ends.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A car drives past an office building with a glass front.
- S2 [core] The car's reflection glides across the windows.
- S3 [minor] The reflection is mirrored.
- S4 [minor] The reflection disappears where the glass ends.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflection moves in step with the car and appears only in the glass, jumping slightly at the frames between panes.
  - fail: It stays still while the car moves; or continues across solid wall; or it is missing in plainly reflective glass.
- P2 [core · shape_identity]
  - expect: The reflection is a mirror image of the car, same colours and size, with any lettering reversed.
  - fail: It is a different vehicle or colour; or upside down; or its lettering reads the right way round.
- P3 [major · causeless_motion]
  - expect: Nothing moves in the reflection that is not moving in reality.
  - fail: The reflection moves while the car has stopped; or shows the car heading a different way.
- P4 [major · material_response]
  - expect: The panes are flat and rigid: the reflection is undistorted and the interior is seen through.
  - fail: The glass ripples; or the reflection warps as it slides; or the frames bend.
- P5 [fatal · permanence_count]
  - expect: One car and one reflection per pane.
  - fail: A second car appears; or the car drives into the glass; or the reflection steps out; or the car vanishes.
- P6 [minor · attribute_drift]
  - expect: The building, the car and the street stay the same.
  - fail: The car changes colour; or the building's frames change; or the street rearranges.

## OPT-0055 · reflection · train

**Caption.** A pendulum clock swings in front of a hallway mirror, and the reflected pendulum swings in time with it, mirrored.

**Expectation (hidden).** The reflected swing is simultaneous and mirrored; the reflection stops when the pendulum stops.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A pendulum clock swings in front of a hallway mirror.
- S2 [core] The reflected pendulum swings in time with it.
- S3 [core] The reflection is mirrored.
- S4 [minor] The reflection stops when the pendulum stops.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflected swing is simultaneous with the real one and stops when the pendulum stops.
  - fail: It swings out of time; or it swings while the pendulum hangs still; or it stops while the pendulum swings.
- P2 [core · shape_identity]
  - expect: The reflection is a mirror image: the pendulum's swing to one side of the frame appears on the same side in the mirror.
  - fail: The reflected swing is on the other side of the frame, as in a rotated copy; or the reflection is upside down; or it shows a different clock.
- P3 [major · causeless_motion]
  - expect: The reflection does not move on its own.
  - fail: It shifts or turns while the clock is still; or slides across the mirror with nothing moving.
- P4 [major · material_response]
  - expect: The mirror is flat and rigid: the reflection is undistorted.
  - fail: The surface ripples; or the reflection warps; or the mirror bends.
- P5 [fatal · permanence_count]
  - expect: One clock and one reflection; the reflection stays in the mirror.
  - fail: A second clock appears; or the reflection leaves the mirror; or the pendulum vanishes; or the clock passes into the glass.
- P6 [minor · attribute_drift]
  - expect: The clock, the mirror frame and the hallway stay the same.
  - fail: The clock changes colour; or the frame changes; or the hallway rearranges.

**Note.** Mirror geometry: each point of the image lies directly across the mirror surface from the real point, so the image is a mirror copy, not a rotated one.

## OPT-0056 · reflection · train

**Caption.** A robot vacuum turns in front of a floor-length mirror, and its reflection turns with it in mirror image.

**Expectation (hidden).** Every turn is matched instantly and mirrored; the reflection never gets ahead or faces a different way.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A robot vacuum is in front of a floor-length mirror.
- S2 [core] It turns.
- S3 [core] Its reflection turns with it in mirror image.
- S4 [minor] The reflection's turn is simultaneous with the real one.

**PC**
- P1 [core · missing_consequence]
  - expect: Every turn is matched instantly by the reflection.
  - fail: The reflection turns first or later; or it stays still while the vacuum turns; or it turns while the vacuum is still.
- P2 [core · shape_identity]
  - expect: The reflection is a mirror image, facing the real vacuum across the surface, and never faces a different way.
  - fail: It is a rotated copy rather than mirrored; or it faces away; or it is a different object.
- P3 [major · causeless_motion]
  - expect: The reflection does not move on its own.
  - fail: It slides across the mirror with the vacuum still; or spins by itself.
- P4 [major · material_response]
  - expect: The mirror is flat and rigid: the reflection is undistorted.
  - fail: The surface ripples; or the reflection warps; or the mirror bends.
- P5 [fatal · permanence_count]
  - expect: One vacuum and one reflection; the reflection stays in the mirror.
  - fail: A second vacuum appears; or the reflection leaves the mirror; or the vacuum passes into the glass; or it vanishes.
- P6 [minor · attribute_drift]
  - expect: The vacuum and the mirror frame stay the same.
  - fail: The vacuum changes colour; or the frame changes; or the floor changes.

**Note.** Mirror geometry: each point of the image lies directly across the mirror surface from the real point, so the image is a mirror copy, not a rotated one.

## OPT-0057 · reflection · train

**Caption.** A hand mirror is tilted downward, and the reflection in it shifts from the ceiling to the floor.

**Expectation (hidden).** The scene in the mirror sweeps smoothly as the mirror tilts; it shows what lies in the direction the mirror faces, not the same view throughout.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A hand mirror is held up.
- S2 [core] It is tilted downward.
- S3 [core] The reflection in it shifts from the ceiling to the floor.
- S4 [minor] The tilt comes first and the view shifts with it.

**PC**
- P1 [core · missing_consequence]
  - expect: The scene in the mirror sweeps smoothly as the mirror tilts and shows what lies in the direction the mirror faces.
  - fail: The view stays the same as the mirror tilts; or it shows the ceiling with the mirror facing down; or it jumps.
- P2 [core · causeless_motion]
  - expect: The view changes only while the mirror moves.
  - fail: It sweeps with the mirror still; or it changes before the tilt; or it keeps moving after the tilt stops.
- P3 [major · shape_identity]
  - expect: The reflected room matches the real room, mirrored.
  - fail: It shows a different room; or it is not mirrored; or objects appear in it that are not in the room.
- P4 [major · material_response]
  - expect: The mirror is flat and rigid: the view is undistorted.
  - fail: The surface ripples; or the view warps; or the mirror bends.
- P5 [fatal · permanence_count]
  - expect: One mirror in one hand.
  - fail: The mirror duplicates or vanishes; or the hand passes through it; or the reflection becomes solid.
- P6 [minor · attribute_drift]
  - expect: The mirror's frame and the room stay the same.
  - fail: The frame changes; or the room rearranges; or the hand changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0058 · reflection · train

**Caption.** A cloth is draped over a wall mirror, and the reflection of the room disappears behind the cloth.

**Expectation (hidden).** The reflected room is visible until the cloth covers the glass and is gone wherever the cloth hangs; it returns when the cloth is pulled off.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A wall mirror reflects the room.
- S2 [core] A cloth is draped over it.
- S3 [core] The reflection disappears behind the cloth.
- S4 [minor] The reflection is gone wherever the cloth hangs and visible where it does not.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflected room is visible until the cloth covers the glass and is gone wherever the cloth hangs.
  - fail: The reflection shows through the cloth; or it vanishes before the cloth arrives; or it stays visible on covered glass.
- P2 [core · permanence_count]
  - expect: The reflection would return when the cloth is pulled off, and the real room is unchanged.
  - fail: The room changes while covered; or the mirror vanishes; or a reflection appears on the cloth itself.
- P3 [major · gravity_direction]
  - expect: The cloth hangs down over the mirror.
  - fail: It floats; or hangs upward; or stays out stiffly.
- P4 [major · material_response]
  - expect: The cloth drapes and folds.
  - fail: It is rigid like a board; or stretches; or passes through the mirror.
- P5 [fatal · permanence_count]
  - expect: One mirror and one cloth.
  - fail: A second mirror appears; or the cloth duplicates; or the cloth passes through the wall.
- P6 [minor · attribute_drift]
  - expect: The cloth's colour and the room stay the same.
  - fail: The cloth changes colour; or the frame changes; or the room rearranges.

## OPT-0059 · reflection · train

**Caption.** A car approaches from behind, and its image grows larger in the rear-view mirror of the car ahead.

**Expectation (hidden).** The reflected car grows as the real one closes in and shrinks if it falls back; it is seen behind, not ahead.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A car approaches from behind another car.
- S2 [core] Its image grows larger in the rear-view mirror of the car ahead.
- S3 [minor] The image is seen behind, not ahead.
- S4 [minor] The image grows as the car closes in.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflected car grows as the real one closes in and would shrink if it fell back.
  - fail: The image stays one size as the car closes; or it shrinks as the car nears; or it grows with the gap unchanged.
- P2 [core · shape_identity]
  - expect: The image is a mirror image of the following car, seen behind, with any lettering reversed.
  - fail: It is a different car; or it shows the road ahead; or its lettering reads the right way round.
- P3 [major · causeless_motion]
  - expect: The image moves only as the cars move.
  - fail: It jumps; or moves while both cars are stopped; or drifts across the mirror.
- P4 [major · material_response]
  - expect: The mirror is flat and rigid: the image is undistorted.
  - fail: The mirror ripples; or the image warps; or the mirror bends.
- P5 [fatal · permanence_count]
  - expect: Two cars and one mirror image of the following one.
  - fail: A third car appears; or the image leaves the mirror; or a car vanishes; or the image becomes solid.
- P6 [minor · attribute_drift]
  - expect: The cars' colours and the road stay the same.
  - fail: A car changes colour; or the mirror changes; or the road rearranges.

## OPT-0060 · reflection · train

**Caption.** A ball rolls out of a room past a wall mirror, and its reflection leaves the mirror at the same time.

**Expectation (hidden).** The reflection slides out of the frame as the ball passes the mirror's edge and the mirror shows only the empty room afterwards; the reflection does not remain.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A ball rolls out of a room past a wall mirror.
- S2 [core] Its reflection leaves the mirror at the same time.
- S3 [minor] Afterwards the mirror shows only the empty room.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflection slides out of the frame as the ball passes the mirror's edge, at the same time.
  - fail: The reflection remains after the ball has gone; or leaves before the ball reaches the edge; or stays still while the ball rolls.
- P2 [core · permanence_count]
  - expect: After the ball has passed, the mirror shows only the empty room.
  - fail: A ball remains in the mirror; or a second ball appears; or the room in the mirror changes.
- P3 [major · shape_identity]
  - expect: The reflection is a mirror image of the ball, same colour and size.
  - fail: It is a different colour or size; or a different object; or it is not mirrored.
- P4 [major · causeless_motion]
  - expect: The ball rolls straight and slows gently.
  - fail: It curves; or speeds up; or restarts.
- P5 [fatal · permanence_count]
  - expect: One ball and one mirror; the reflection stays in the mirror.
  - fail: The reflection steps out; or the ball passes into the glass; or the ball vanishes; or the mirror duplicates.
- P6 [minor · attribute_drift]
  - expect: The ball's colour and the room stay the same.
  - fail: The ball changes colour; or the frame changes; or the room rearranges.

## OPT-0061 · reflection · train

**Caption.** A candle burns on a table by a dark window at night, and a second flame appears in the glass beside the real one.

**Expectation (hidden).** The reflected flame flickers in step with the real one and is mirrored; it vanishes if the candle is blown out or the room light is turned up.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A candle burns on a table by a dark window at night.
- S2 [core] A second flame appears in the glass beside the real one.
- S3 [minor] The reflected flame flickers in step with the real one.
- S4 [minor] The reflected flame is mirrored.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflected flame flickers in step with the real one and would vanish if the candle went out.
  - fail: It flickers out of time; or it stays steady while the real flame flickers; or it remains with the candle out.
- P2 [core · shape_identity]
  - expect: The reflection is a mirror image of the candle and flame, dimmer, at the same height across the glass.
  - fail: It is a different candle; or brighter than the real flame; or at a different height; or upside down.
- P3 [major · causeless_motion]
  - expect: The reflection does not move on its own.
  - fail: It slides across the glass; or shifts while the candle is still.
- P4 [major · gravity_direction]
  - expect: Both flames point upward.
  - fail: The real flame points sideways in still air; or the reflected flame points down; or a flame detaches.
- P5 [fatal · permanence_count]
  - expect: One candle and one reflection; the reflection stays in the glass.
  - fail: A second candle appears in the room; or the reflection comes out of the glass; or the candle vanishes; or the reflection becomes solid.
- P6 [minor · attribute_drift]
  - expect: The candle, the table and the window frame stay the same.
  - fail: The candle changes colour; or the frame changes; or the table changes.

## OPT-0062 · reflection · train

**Caption.** A luggage trolley is pushed across a polished marble lobby floor, and its reflection moves upside down beneath it.

**Expectation (hidden).** The reflection meets the trolley at its wheels, is inverted, and moves exactly with it; it is dimmer than the trolley.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A luggage trolley is pushed across a polished marble lobby floor.
- S2 [core] Its reflection moves upside down beneath it.
- S3 [minor] The reflection meets the trolley at its wheels.
- S4 [minor] The reflection is dimmer than the trolley.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflection meets the trolley at its wheels and moves exactly with it.
  - fail: It is offset from the wheels; or stays still while the trolley moves; or lags.
- P2 [core · shape_identity]
  - expect: The reflection is inverted, the trolley's shape hanging downward from the wheels.
  - fail: It is upright; or a different object; or it is beside the trolley rather than beneath.
- P3 [major · causeless_motion]
  - expect: The reflection does not move on its own.
  - fail: It moves with the trolley stopped; or drifts across the floor.
- P4 [major · material_response]
  - expect: The floor is flat and rigid: the reflection is undistorted.
  - fail: The floor ripples; or the reflection warps; or the floor bends.
- P5 [fatal · permanence_count]
  - expect: One trolley and one reflection; the reflection stays in the floor.
  - fail: A second trolley appears; or the reflection rises out of the floor; or the trolley sinks into it; or the trolley vanishes.
- P6 [minor · attribute_drift]
  - expect: The trolley and the lobby stay the same.
  - fail: The trolley changes colour; or the floor changes; or the lobby rearranges.

## OPT-0063 · reflection · train

**Caption.** A duck paddles across a calm pond, and its reflection glides along under it, breaking up in the wake it leaves.

**Expectation (hidden).** The reflection is inverted, stays directly beneath the duck, and wavers in the ripples behind it; the water ahead shows a clear image.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A duck paddles across a calm pond.
- S2 [core] Its reflection glides along under it.
- S3 [core] The reflection breaks up in the wake it leaves.
- S4 [minor] The water ahead shows a clear image.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflection stays directly beneath the duck and moves with it, wavering in the ripples behind.
  - fail: It is offset from the duck; or stays still while the duck paddles; or it is sharp in the wake and broken ahead.
- P2 [core · shape_identity]
  - expect: The reflection is inverted and joined at the waterline.
  - fail: It is upright; or detached from the duck; or a different bird.
- P3 [major · causeless_motion]
  - expect: The reflection does not move on its own.
  - fail: It moves with the duck still; or drifts across the pond.
- P4 [major · material_response]
  - expect: The water is liquid: ripples spread from the duck and the surface ahead stays flat.
  - fail: The surface is rigid; or ripples run ahead of the duck; or the water flows uphill.
- P5 [fatal · permanence_count]
  - expect: One duck and one reflection; the reflection stays on the water.
  - fail: A second duck appears; or the reflection rises off the water; or the duck vanishes; or the reflection becomes solid.
- P6 [minor · attribute_drift]
  - expect: The duck's plumage and the pond stay the same.
  - fail: The plumage changes; or the pond changes colour; or the shore rearranges.

**Note.** Self-driven animal: where it goes and how it moves are not judged. Only the reflection's relation to it is.

## OPT-0064 · reflection · train

**Caption.** Traffic lights change from red to green above a wet street at night, and their reflections on the road change colour at the same moment.

**Expectation (hidden).** The coloured streaks on the wet road match the lights and switch colour when they do; they lie below the lights and stretch toward the viewer.

**Declared violation types.** missing_consequence, attribute_drift

**SA**
- S1 [core] Traffic lights hang above a wet street at night.
- S2 [core] They change from red to green.
- S3 [core] Their reflections on the road change colour at the same moment.
- S4 [minor] The reflections lie below the lights and stretch toward the viewer.

**PC**
- P1 [core · missing_consequence]
  - expect: The coloured streaks on the wet road switch colour when the lights do, at the same moment.
  - fail: The streaks stay red after the light is green; or they change before the light; or they show a colour the lights never show.
- P2 [core · attribute_drift]
  - expect: The streaks match the lights' colours and lie below them.
  - fail: They are a different colour from the lights; or they lie above the lights; or they are the wrong number.
- P3 [major · causeless_motion]
  - expect: The streaks do not move on their own.
  - fail: They drift across the road; or flicker with steady lights; or shift sideways.
- P4 [major · material_response]
  - expect: The road is wet: the streaks shimmer where puddles ripple and are absent where the road is dry.
  - fail: They are sharp mirror images on rough tarmac; or they appear on dry patches; or the water is rigid.
- P5 [fatal · permanence_count]
  - expect: The lights keep their number and stay on their pole.
  - fail: A light vanishes or appears; or the pole moves; or a streak becomes solid.
- P6 [minor · attribute_drift]
  - expect: The pole, the street and the buildings stay the same.
  - fail: The pole changes; or the buildings rearrange; or the road markings shift.

## OPT-0065 · reflection · train

**Caption.** A balloon on a string turns slowly in an elevator with mirrored walls, and its reflections turn with it in every wall.

**Expectation (hidden).** All reflections move at the same instant, each mirrored relative to its wall; none turns a different way.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A balloon on a string turns slowly in an elevator.
- S2 [core] The elevator has mirrored walls.
- S3 [core] Its reflections turn with it in every wall.
- S4 [minor] All the reflections move at the same instant.
- S5 [minor] Each reflection is mirrored relative to its wall.

**PC**
- P1 [core · missing_consequence]
  - expect: All reflections move at the same instant as the balloon.
  - fail: A reflection lags; or one turns while the balloon is still; or one stays still while the balloon turns.
- P2 [core · shape_identity]
  - expect: Each reflection is a mirror image relative to its own wall, and none turns a different way.
  - fail: A reflection turns the wrong way; or one is a different colour; or one is upside down.
- P3 [major · causeless_motion]
  - expect: The reflections do not move on their own.
  - fail: A reflection drifts across its wall; or shifts while the balloon hangs still.
- P4 [major · material_response]
  - expect: The walls are flat and rigid: the reflections are undistorted.
  - fail: A wall ripples; or a reflection warps; or a wall bends.
- P5 [fatal · permanence_count]
  - expect: One balloon and one reflection per wall.
  - fail: A second balloon appears in the elevator; or a reflection steps out of its wall; or the balloon vanishes; or the string passes through a wall.
- P6 [minor · attribute_drift]
  - expect: The balloon's colour and the elevator stay the same.
  - fail: The balloon changes colour; or the walls change; or the string changes.

**Note.** Mirror geometry: each point of the image lies directly across the mirror surface from the real point, so the image is a mirror copy, not a rotated one.

## OPT-0066 · reflection · train

**Caption.** A bicycle wheel rolls through a puddle showing the reflection of a building, and the image shatters into ripples.

**Expectation (hidden).** The reflection breaks up at the moment the wheel enters and reforms as the ripples die; it does not stay sharp while the water moves.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A puddle shows the reflection of a building.
- S2 [core] A bicycle wheel rolls through the puddle.
- S3 [core] The image shatters into ripples.
- S4 [minor] The wheel enters first and the image breaks at that moment.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflection breaks up at the moment the wheel enters and reforms as the ripples die.
  - fail: It stays sharp while the water moves; or breaks before the wheel arrives; or never reforms on still water.
- P2 [core · shape_identity]
  - expect: Before and after, the reflection is the inverted building; the building itself is unchanged.
  - fail: The building changes; or the reflection is upright; or a different building appears in the puddle.
- P3 [major · material_response]
  - expect: The water is liquid: ripples spread from the wheel and fade.
  - fail: The surface is rigid; or the ripples freeze; or the water leaps.
- P4 [major · causeless_motion]
  - expect: The wheel rolls straight through and the water moves only where it is disturbed.
  - fail: The wheel jinks; or the water churns before it arrives; or ripples appear elsewhere.
- P5 [fatal · permanence_count]
  - expect: One puddle, one wheel and one building.
  - fail: The wheel vanishes; or a second building appears; or the wheel passes through the pavement; or the reflection becomes solid.
- P6 [minor · attribute_drift]
  - expect: The building and the pavement stay the same.
  - fail: The building changes colour; or the pavement changes; or the wheel changes.

## OPT-0067 · reflection · train

**Caption.** A car approaches from behind a parked car, and its image appears in the parked car's side mirror and grows larger.

**Expectation (hidden).** The image appears in the mirror before the car passes and grows as it nears; it leaves the mirror as the car draws alongside.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A car approaches from behind a parked car.
- S2 [core] Its image appears in the parked car's side mirror.
- S3 [core] The image grows larger.
- S4 [minor] The image leaves the mirror as the car draws alongside.

**PC**
- P1 [core · missing_consequence]
  - expect: The image appears in the mirror before the car passes and grows as it nears.
  - fail: It stays one size; or shrinks as the car nears; or appears only after the car has passed.
- P2 [core · shape_identity]
  - expect: The image is a mirror image of the approaching car, seen behind.
  - fail: It is a different car; or it shows the road ahead; or it is upside down.
- P3 [major · causeless_motion]
  - expect: The image moves only as the car moves.
  - fail: It jumps; or moves with the car stopped; or drifts.
- P4 [major · material_response]
  - expect: The mirror is rigid: the image is undistorted.
  - fail: The mirror ripples; or the image warps; or the mirror bends.
- P5 [fatal · permanence_count]
  - expect: Two cars and one image of the approaching one.
  - fail: A third car appears; or the image leaves the mirror; or a car vanishes; or the cars pass through each other.
- P6 [minor · attribute_drift]
  - expect: The cars' colours and the street stay the same.
  - fail: A car changes colour; or the mirror changes; or the street rearranges.

## OPT-0068 · reflection · train

**Caption.** A wristwatch lying on a sunny table is turned so its face catches the sunlight, and a bright spot of light appears on the wall and slides as the watch turns.

**Expectation (hidden).** The spot appears when the watch face is angled to the sun, moves as the watch turns, and disappears when the angle is lost; it does not move on its own.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A wristwatch lies on a sunny table.
- S2 [core] It is turned so its face catches the sunlight.
- S3 [core] A bright spot of light appears on the wall.
- S4 [core] The spot slides as the watch turns.
- S5 [minor] The spot disappears when the angle is lost.

**PC**
- P1 [core · missing_consequence]
  - expect: The spot appears when the watch face is angled to the sun, moves as the watch turns, and disappears when the angle is lost.
  - fail: The spot is there with the face turned away; or it stays still while the watch turns; or it remains when the angle is lost.
- P2 [core · causeless_motion]
  - expect: The spot does not move on its own.
  - fail: It slides with the watch still; or it moves before the watch; or it flickers with the watch steady.
- P3 [major · shape_identity]
  - expect: The spot is one bright patch, small and roughly the face's shape.
  - fail: It splits into several; or it is a huge flood of light; or it is a sharp geometric shape unlike the face.
- P4 [major · trajectory_momentum]
  - expect: The spot moves the opposite way to the watch's tilt, as a reflected beam does.
  - fail: It moves the same way as the tilt; or it jumps; or it moves crosswise.
- P5 [fatal · permanence_count]
  - expect: One watch and one spot.
  - fail: A second spot appears; or the watch duplicates; or the spot becomes solid; or the hand passes through the watch.
- P6 [minor · attribute_drift]
  - expect: The watch, the table and the wall stay the same.
  - fail: The watch changes; or the wall changes colour; or the table changes.

**Note.** The hand turning the watch is the minimal trigger; the person is not judged.

## OPT-0069 · reflection · train

**Caption.** A hand mirror in a sunny doorway is tilted, sending a patch of sunlight dancing across the shaded room.

**Expectation (hidden).** The bright patch moves as the mirror tilts, in the direction opposite to the tilt, and vanishes when the mirror is turned from the sun.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A hand mirror is in a sunny doorway.
- S2 [core] It is tilted.
- S3 [core] A patch of sunlight dances across the shaded room.
- S4 [minor] The patch vanishes when the mirror is turned from the sun.

**PC**
- P1 [core · missing_consequence]
  - expect: The bright patch moves as the mirror tilts and vanishes when the mirror is turned from the sun.
  - fail: It stays still while the mirror tilts; or it remains with the mirror turned away; or it is there with no sun on the mirror.
- P2 [core · causeless_motion]
  - expect: The patch does not move on its own.
  - fail: It dances with the mirror still; or it moves before the tilt; or it flickers with the mirror steady.
- P3 [major · trajectory_momentum]
  - expect: The patch moves in the direction opposite to the tilt, as a reflected beam does.
  - fail: It moves the same way as the tilt; or it jumps; or it moves crosswise.
- P4 [major · shape_identity]
  - expect: The patch is one bright shape roughly the mirror's outline.
  - fail: It splits into several; or it is a sharp geometric shape unlike the mirror; or it floods the whole room.
- P5 [fatal · permanence_count]
  - expect: One mirror and one patch.
  - fail: A second patch appears; or the mirror duplicates; or the patch becomes solid; or the hand passes through the mirror.
- P6 [minor · attribute_drift]
  - expect: The room and the mirror stay the same.
  - fail: The room rearranges; or the mirror changes; or the walls change colour.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0070 · reflection · train

**Caption.** A lamp beside a dark window is switched on at night, and the reflection of the lamp and the room appears in the glass.

**Expectation (hidden).** The reflection appears with the lamp and is mirrored; when the lamp is turned off it fades from the glass.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A lamp stands beside a dark window at night.
- S2 [core] It is switched on.
- S3 [core] The reflection of the lamp and the room appears in the glass.
- S4 [minor] The reflection is mirrored.
- S5 [minor] The lamp comes on first and the reflection appears with it.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflection appears with the lamp and would fade if the lamp were turned off.
  - fail: The reflection is there with the lamp off; or the lamp comes on and no reflection appears; or the reflection remains after the lamp goes off.
- P2 [core · shape_identity]
  - expect: The reflection is a mirror image of the lamp and room, at the same height across the glass.
  - fail: It is a different room; or upside down; or a rotated copy rather than mirrored.
- P3 [major · causeless_motion]
  - expect: The reflection does not move on its own.
  - fail: It slides across the glass; or shifts while the room is still.
- P4 [major · material_response]
  - expect: The glass is flat and rigid: the reflection is undistorted.
  - fail: The glass ripples; or the reflection warps; or the window bends.
- P5 [fatal · permanence_count]
  - expect: One lamp and one reflection; the reflection stays in the glass.
  - fail: A second lamp appears in the room; or the reflection comes out of the glass; or the lamp vanishes; or the lamp passes into the window.
- P6 [minor · attribute_drift]
  - expect: The lamp, the room and the window frame stay the same.
  - fail: The lamp changes colour; or the frame changes; or the room rearranges.

## OPT-0071 · reflection · train

**Caption.** A dog sits in front of a glossy black oven door and tilts its head, and its reflection tilts its head the other way.

**Expectation (hidden).** The reflected dog moves at the same time, mirrored, and is dimmer than the real dog; it stays inside the door's surface.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A dog sits in front of a glossy black oven door.
- S2 [core] It tilts its head.
- S3 [core] Its reflection tilts its head the other way.
- S4 [minor] The reflection is dimmer than the real dog.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflected dog moves at the same time as the real one.
  - fail: It moves first or later; or it stays still while the dog tilts; or it tilts while the dog is still.
- P2 [core · shape_identity]
  - expect: The reflection is a mirror image: the same dog facing the real one, tilting to the mirrored side.
  - fail: It tilts the same way as a rotated copy would; or it is a different dog; or it shows the dog's back.
- P3 [major · causeless_motion]
  - expect: The reflection does not move on its own.
  - fail: It shifts while the dog is still; or it slides across the door.
- P4 [major · material_response]
  - expect: The door is flat and rigid: the reflection is undistorted and dim.
  - fail: The door ripples; or the reflection warps; or it is brighter than the dog.
- P5 [fatal · permanence_count]
  - expect: One dog and one reflection; the reflection stays in the door.
  - fail: A second dog appears; or the reflection steps out; or the dog vanishes; or the dog passes into the door.
- P6 [minor · attribute_drift]
  - expect: The dog's coat and the kitchen stay the same.
  - fail: The coat changes; or the oven changes; or the kitchen rearranges.

**Note.** Self-driven animal: where it goes and how it moves are not judged. Only the reflection's relation to it is. Mirror geometry: each point of the image lies directly across the mirror surface from the real point, so the image is a mirror copy, not a rotated one.

## OPT-0072 · reflection · train

**Caption.** A breeze crosses a lake that has been reflecting a boathouse, and the reflection wobbles and blurs, then sharpens again as the water calms.

**Expectation (hidden).** The image distorts exactly where ripples pass and returns to a clear inverted image when the surface is still; the boathouse itself is unaffected.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A lake reflects a boathouse.
- S2 [core] A breeze crosses the lake.
- S3 [core] The reflection wobbles and blurs.
- S4 [core] It sharpens again as the water calms.
- S5 [minor] The breeze comes first, then the blur, then the sharpening.

**PC**
- P1 [core · missing_consequence]
  - expect: The image distorts exactly where ripples pass and returns to a clear inverted image when the surface is still.
  - fail: It stays sharp across plain ripples; or blurs on flat water; or never sharpens again on a calm surface.
- P2 [core · shape_identity]
  - expect: The boathouse itself is unaffected and the sharp reflection is its inverted image.
  - fail: The boathouse wobbles; or the reflection is upright; or a different building appears.
- P3 [major · causeless_motion]
  - expect: The water moves only with the breeze.
  - fail: Ripples run against other wind signs; or the surface churns in still air; or the ripples freeze.
- P4 [major · material_response]
  - expect: The surface is liquid: ripples pass and fade.
  - fail: The water is rigid like glass; or the ripples hold their shape; or the water leaps.
- P5 [fatal · permanence_count]
  - expect: One boathouse and one reflection; the reflection stays on the water.
  - fail: A second boathouse appears; or the reflection rises off the water; or the boathouse vanishes; or the reflection becomes solid.
- P6 [minor · attribute_drift]
  - expect: The boathouse's colours and the shore stay the same.
  - fail: The boathouse changes colour; or the shore rearranges; or the sky changes abruptly.

## OPT-0073 · reflection · train

**Caption.** A car drives along a canal-side road, and its reflection travels upside down on the water beside it.

**Expectation (hidden).** The reflection keeps pace, is inverted, and wavers with the water; it is missing where reeds or a boat break the surface.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A car drives along a canal-side road.
- S2 [core] Its reflection travels upside down on the water beside it.
- S3 [minor] The reflection keeps pace with the car.
- S4 [minor] The reflection is missing where reeds or a boat break the surface.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflection keeps pace with the car and is missing where reeds or a boat break the surface.
  - fail: It lags; or stays still while the car moves; or it shows across reeds as if they were not there.
- P2 [core · shape_identity]
  - expect: The reflection is inverted, the car's shape hanging down from the bank.
  - fail: It is upright; or a different vehicle; or it is far from the bank's line.
- P3 [major · causeless_motion]
  - expect: The reflection does not move on its own.
  - fail: It moves with the car stopped; or drifts along the canal.
- P4 [major · material_response]
  - expect: The water is liquid: the reflection wavers with the surface.
  - fail: It is rigid and sharp on a plainly rippled surface; or it wavers on glassy water; or the water flows uphill.
- P5 [fatal · permanence_count]
  - expect: One car and one reflection; the reflection stays on the water.
  - fail: A second car appears; or the reflection rises off the water; or the car vanishes; or the car drives into the canal.
- P6 [minor · attribute_drift]
  - expect: The car's colour and the canal bank stay the same.
  - fail: The car changes colour; or the bank rearranges; or the reeds change.

## OPT-0074 · reflection · train

**Caption.** Breath is blown on a polished silver tray that reflects the room, and the reflected image fogs over and returns.

**Expectation (hidden).** The reflection blurs under the breath and comes back as the fog clears; the tray itself does not change.

**Declared violation types.** missing_consequence, attribute_drift

**SA**
- S1 [core] A polished silver tray reflects the room.
- S2 [core] Breath is blown on it.
- S3 [core] The reflected image fogs over.
- S4 [core] It returns as the fog clears.
- S5 [minor] The breath comes first, then the fog, then the clearing.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflection blurs under the breath and comes back as the fog clears.
  - fail: It stays sharp under the breath; or fogs before the breath; or never clears.
- P2 [core · attribute_drift]
  - expect: The tray itself does not change; only its surface fogs.
  - fail: The tray changes colour; or bends; or the fog is a different colour from a misted surface.
- P3 [major · process_direction]
  - expect: The fog forms quickly and clears gradually.
  - fail: It clears instantly; or forms slowly after the breath; or flickers.
- P4 [major · shape_identity]
  - expect: The reflection that returns is the same room, mirrored.
  - fail: A different scene appears; or the reflection is upright where it was inverted; or objects appear that are not in the room.
- P5 [fatal · permanence_count]
  - expect: One tray and one reflection.
  - fail: The tray duplicates or vanishes; or the reflection becomes solid; or the breath is visible as an object.
- P6 [minor · attribute_drift]
  - expect: The room and the tray's rim stay the same.
  - fail: The room rearranges; or the rim changes; or the table changes.

**Note.** The breath is the trigger; the person is not judged.

## OPT-0075 · reflection · train

**Caption.** A swan glides across a still lake at sunset, and its reflection glides beneath it with the orange sky behind both.

**Expectation (hidden).** The reflected swan is inverted and directly under the real one; it moves with the swan and breaks up only in the ripples the swan makes.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A swan glides across a still lake at sunset.
- S2 [core] Its reflection glides beneath it.
- S3 [core] The orange sky is behind both.
- S4 [minor] The reflection is inverted and directly under the swan.
- S5 [minor] The reflection breaks up only in the ripples the swan makes.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflected swan is directly under the real one and moves with it, breaking up only in the swan's own ripples.
  - fail: It is offset; or stays still while the swan glides; or it is broken on flat water ahead.
- P2 [core · shape_identity]
  - expect: The reflection is inverted and joined at the waterline, with the orange sky reflected around it.
  - fail: It is upright; or detached; or the reflected sky is a different colour.
- P3 [major · causeless_motion]
  - expect: The reflection does not move on its own.
  - fail: It moves with the swan still; or drifts across the lake.
- P4 [major · material_response]
  - expect: The water is liquid: ripples spread from the swan and the surface elsewhere stays flat.
  - fail: The surface is rigid; or ripples run ahead of the swan; or the water leaps.
- P5 [fatal · permanence_count]
  - expect: One swan and one reflection; the reflection stays on the water.
  - fail: A second swan appears; or the reflection rises off the water; or the swan vanishes; or the reflection becomes solid.
- P6 [minor · attribute_drift]
  - expect: The swan's plumage and the sky stay the same.
  - fail: The plumage changes; or the sky changes colour abruptly; or the shore rearranges.

**Note.** Self-driven animal: where it goes and how it moves are not judged. Only the reflection's relation to it is.

## OPT-0076 · reflection · train

**Caption.** A hat on a mannequin head is turned from side to side in front of a shop mirror, and the reflection turns in mirror image.

**Expectation (hidden).** The reflection turns at the same time, to the mirrored side, wearing the same hat; it does not turn the same way as the head.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A hat is on a mannequin head in front of a shop mirror.
- S2 [core] The head is turned from side to side.
- S3 [core] The reflection turns in mirror image.
- S4 [minor] The reflection wears the same hat.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflection turns at the same time as the head.
  - fail: It turns first or later; or it stays still while the head turns; or it turns while the head is still.
- P2 [core · shape_identity]
  - expect: The reflection turns to the mirrored side, facing the real head across the surface, wearing the same hat.
  - fail: It turns the same way as a rotated copy would; or it wears a different hat; or it shows the back of the head.
- P3 [major · causeless_motion]
  - expect: The reflection does not move on its own.
  - fail: It shifts while the head is still; or slides across the mirror.
- P4 [major · material_response]
  - expect: The mirror is flat and rigid: the reflection is undistorted.
  - fail: The surface ripples; or the reflection warps; or the mirror bends.
- P5 [fatal · permanence_count]
  - expect: One head, one hat and one reflection; the reflection stays in the mirror.
  - fail: A second head appears; or the reflection steps out; or the hat vanishes; or the head passes into the glass.
- P6 [minor · attribute_drift]
  - expect: The hat's colour and the shop stay the same.
  - fail: The hat changes colour; or the frame changes; or the shop rearranges.

**Note.** Mirror geometry: each point of the image lies directly across the mirror surface from the real point, so the image is a mirror copy, not a rotated one. The hand turning the head is the minimal trigger; the person is not judged.

## OPT-0077 · reflection · train

**Caption.** A flashlight is pointed at a mirror on the wall, and a spot of light appears on the opposite wall.

**Expectation (hidden).** The spot appears when the beam hits the mirror and moves the opposite way when the flashlight is angled; it vanishes when the beam leaves the mirror.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A mirror hangs on a wall.
- S2 [core] A flashlight is pointed at it.
- S3 [core] A spot of light appears on the opposite wall.
- S4 [minor] The spot moves when the flashlight is angled.
- S5 [minor] The spot vanishes when the beam leaves the mirror.

**PC**
- P1 [core · missing_consequence]
  - expect: The spot appears when the beam hits the mirror and vanishes when the beam leaves it.
  - fail: The spot is there with the beam off the mirror; or the beam hits the mirror and no spot appears; or the spot remains after the beam has left.
- P2 [core · trajectory_momentum]
  - expect: The spot moves the opposite way when the flashlight is angled, as a reflected beam does.
  - fail: It moves the same way as the flashlight; or stays still while the flashlight turns; or jumps.
- P3 [major · causeless_motion]
  - expect: The spot does not move on its own.
  - fail: It slides with the flashlight still; or flickers with the beam steady.
- P4 [major · shape_identity]
  - expect: The spot is one bright patch with a soft edge.
  - fail: It splits into several under one beam; or it is a sharp geometric shape; or it floods the room.
- P5 [fatal · permanence_count]
  - expect: One flashlight, one mirror and one spot.
  - fail: A second spot appears; or the mirror duplicates; or the spot becomes solid; or the beam passes through the wall.
- P6 [minor · attribute_drift]
  - expect: The walls and the mirror frame stay the same.
  - fail: A wall changes colour; or the frame changes; or the room rearranges.

## OPT-0078 · reflection · train

**Caption.** A seagull walks across a wet beach at low tide, and its reflection shows beneath it on the thin sheet of water.

**Expectation (hidden).** The inverted reflection appears only where the sand is covered by water and follows the bird's steps; it breaks up in its footprints.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A seagull walks across a wet beach at low tide.
- S2 [core] Its reflection shows beneath it on the thin sheet of water.
- S3 [minor] The reflection appears only where the sand is covered by water.
- S4 [minor] The reflection breaks up in the bird's footprints.

**PC**
- P1 [core · missing_consequence]
  - expect: The inverted reflection appears only where the sand is covered by water and follows the bird's steps.
  - fail: It appears on dry sand; or stays still while the bird walks; or it is missing on plainly wet sand.
- P2 [core · shape_identity]
  - expect: The reflection is inverted and joined at the feet.
  - fail: It is upright; or detached; or a different bird.
- P3 [major · material_response]
  - expect: The water is a thin liquid sheet: the reflection breaks up in the footprints.
  - fail: It is rigid like glass; or the footprints leave the reflection intact; or the water flows uphill.
- P4 [major · causeless_motion]
  - expect: The reflection does not move on its own.
  - fail: It moves with the bird still; or drifts across the sand.
- P5 [fatal · permanence_count]
  - expect: One seagull and one reflection.
  - fail: A second bird appears; or the reflection rises off the sand; or the bird vanishes; or the reflection becomes solid.
- P6 [minor · attribute_drift]
  - expect: The plumage and the beach stay the same.
  - fail: The plumage changes; or the beach rearranges; or the sea changes.

**Note.** Self-driven animal: where it goes and how it moves are not judged. Only the reflection's relation to it is.

## OPT-0079 · reflection · train

**Caption.** A checkerboard card is reflected in the bowl of a shiny spoon, and as the spoon turns slowly the reflected pattern stretches and shifts.

**Expectation (hidden).** The reflected pattern is small and warped by the curve and changes with the spoon's angle; it stays inside the metal.

**Declared violation types.** shape_identity, missing_consequence

**SA**
- S1 [core] A checkerboard card is reflected in the bowl of a shiny spoon.
- S2 [core] The spoon turns slowly.
- S3 [core] The reflected pattern stretches and shifts.
- S4 [minor] The reflection is small and warped by the curve.
- S5 [minor] The spoon turns first and the pattern shifts with it.

**PC**
- P1 [core · shape_identity]
  - expect: The reflected pattern is small and warped by the curve and stays inside the metal.
  - fail: It is flat and undistorted; or larger than the spoon's bowl; or it appears outside the metal.
- P2 [core · missing_consequence]
  - expect: The pattern changes with the spoon's angle and only then.
  - fail: It stays fixed as the spoon turns; or it shifts with the spoon still; or it shows a different card.
- P3 [major · causeless_motion]
  - expect: The card stays put.
  - fail: It slides; or turns by itself; or lifts.
- P4 [major · material_response]
  - expect: The spoon is rigid polished metal.
  - fail: It bends; or its surface ripples; or it goes dull.
- P5 [fatal · permanence_count]
  - expect: One spoon and one card.
  - fail: The spoon duplicates; or the card vanishes; or the reflection becomes solid; or the hand passes through the spoon.
- P6 [minor · attribute_drift]
  - expect: The card's pattern and the table stay the same.
  - fail: The card changes pattern; or the table changes; or the spoon changes shape.

**Note.** The hand turning the spoon is the minimal trigger; the person is not judged.

## OPT-0080 · reflection · train

**Caption.** A puck slides across a frozen pond, and a faint reflection slides beneath it on the ice.

**Expectation (hidden).** The reflection is inverted, dim, and moves with the puck; it disappears where the ice is scratched or snow-covered.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A puck slides across a frozen pond.
- S2 [core] A faint reflection slides beneath it on the ice.
- S3 [minor] The reflection is inverted and dim.
- S4 [minor] The reflection disappears where the ice is scratched or snow-covered.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflection moves with the puck and disappears where the ice is scratched or snow-covered.
  - fail: It stays still while the puck slides; or shows on snow; or lags.
- P2 [core · shape_identity]
  - expect: The reflection is inverted, dim, and joined at the puck's contact with the ice.
  - fail: It is upright; or brighter than the puck; or detached.
- P3 [major · causeless_motion]
  - expect: The puck slides straight and slows gently.
  - fail: It curves; or speeds up; or restarts.
- P4 [major · material_response]
  - expect: The ice is rigid: the reflection is undistorted.
  - fail: The ice ripples; or the reflection warps; or the puck sinks.
- P5 [fatal · permanence_count]
  - expect: One puck and one reflection.
  - fail: A second puck appears; or the reflection rises off the ice; or the puck vanishes; or the reflection becomes solid.
- P6 [minor · attribute_drift]
  - expect: The puck and the pond stay the same.
  - fail: The puck changes colour; or the pond changes; or the snow patches move.

## OPT-0081 · reflection · train

**Caption.** A car passes a shop with a mirrored sign, and the car's headlights flash in the mirror as it goes by.

**Expectation (hidden).** The flash appears as the lights line up with the mirror and disappears as the car moves on; it moves across the mirror with the car.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A shop has a mirrored sign.
- S2 [core] A car passes the shop.
- S3 [core] The car's headlights flash in the mirror as it goes by.
- S4 [minor] The flash moves across the mirror with the car.

**PC**
- P1 [core · missing_consequence]
  - expect: The flash appears as the lights line up with the mirror and disappears as the car moves on.
  - fail: The flash is there with no car; or it stays after the car has passed; or the car passes and no flash appears.
- P2 [core · trajectory_momentum]
  - expect: The flash moves across the mirror with the car.
  - fail: It stays fixed; or moves the opposite way; or jumps.
- P3 [major · causeless_motion]
  - expect: The flash does not move on its own.
  - fail: It flickers with the car stopped; or drifts.
- P4 [major · material_response]
  - expect: The sign is flat and rigid.
  - fail: It ripples; or bends; or the flash warps.
- P5 [fatal · permanence_count]
  - expect: One car and one sign.
  - fail: A second car appears; or the sign duplicates; or the car vanishes; or the car passes through the sign.
- P6 [minor · attribute_drift]
  - expect: The sign and the shop stay the same.
  - fail: The sign changes; or the shop front changes; or the street rearranges.

## OPT-0082 · reflection · train

**Caption.** A coin is dropped into a fountain whose still water reflects the sky, and rings spread out that break up the reflected clouds.

**Expectation (hidden).** The rings start where the coin enters, distort the reflected sky as they pass, and the image settles when the surface is still again.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A fountain's still water reflects the sky.
- S2 [core] A coin is dropped into it.
- S3 [core] Rings spread out.
- S4 [core] The rings break up the reflected clouds.
- S5 [minor] The coin lands first and the rings follow.

**PC**
- P1 [core · missing_consequence]
  - expect: The rings start where the coin enters and distort the reflected sky as they pass.
  - fail: Rings start elsewhere; or the reflection stays sharp through the rings; or rings appear before the coin lands.
- P2 [core · process_direction]
  - expect: The rings spread outward and fade, and the image settles when the surface is still again.
  - fail: Rings run inward; or they hold their shape; or the image never settles on still water.
- P3 [major · gravity_direction]
  - expect: The coin sinks.
  - fail: It floats; or hangs; or comes back up.
- P4 [major · shape_identity]
  - expect: The reflected sky is the sky's image, inverted, and the clouds' shapes return unchanged when the water settles.
  - fail: A different sky appears in the water; or the reflection is upright where it should be inverted; or the reflected clouds change shape while the real sky is unchanged.
- P5 [fatal · permanence_count]
  - expect: One coin and one fountain.
  - fail: A second coin appears; or the coin vanishes in the air; or the reflection becomes solid; or the coin passes through the basin.
- P6 [minor · attribute_drift]
  - expect: The fountain and the sky stay the same.
  - fail: The fountain changes; or the sky changes abruptly; or the surroundings rearrange.

## OPT-0083 · reflection · train

**Caption.** A candle burns between two facing mirrors, and a line of flames stretches away in both directions, all flickering together.

**Expectation (hidden).** The copies get smaller and dimmer further along the line and all flicker in time with the real flame; none moves independently.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A candle burns between two facing mirrors.
- S2 [core] A line of flames stretches away in both directions.
- S3 [core] All the flames flicker together.
- S4 [minor] The copies get smaller and dimmer further along the line.

**PC**
- P1 [core · missing_consequence]
  - expect: All the copies flicker in time with the real flame and none moves independently.
  - fail: A copy flickers out of time; or one stays steady; or one moves on its own.
- P2 [core · shape_identity]
  - expect: The copies get smaller and dimmer further along the line and alternate in mirror image.
  - fail: They are all the same size; or grow along the line; or they are rotated copies.
- P3 [major · causeless_motion]
  - expect: The line does not move with the candle and mirrors still.
  - fail: The line drifts; or a copy shifts; or the candle moves.
- P4 [major · gravity_direction]
  - expect: All the flames point upward.
  - fail: A flame points down or sideways in still air; or a flame detaches.
- P5 [fatal · permanence_count]
  - expect: One real candle and its copies; the copies stay in the mirrors.
  - fail: A second real candle appears; or a copy steps out; or the candle vanishes; or a copy becomes solid.
- P6 [minor · attribute_drift]
  - expect: The candle and the mirror frames stay the same.
  - fail: The candle changes colour; or a frame changes; or the room rearranges.

**Note.** Mirror geometry: each point of the image lies directly across the mirror surface from the real point, so the image is a mirror copy, not a rotated one.

## OPT-0084 · reflection · train

**Caption.** A hand wipes a streak across a steamed-up mirror, and the room appears in the clear streak.

**Expectation (hidden).** The reflection appears only where the fog is wiped away and is blurred elsewhere; the streak slowly fogs over again.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A mirror is steamed up.
- S2 [core] A hand wipes a streak across it.
- S3 [core] The room appears in the clear streak.
- S4 [minor] The reflection is blurred elsewhere.
- S5 [minor] The streak slowly fogs over again.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflection appears only where the fog is wiped away and is blurred elsewhere.
  - fail: The reflection is sharp through the fog; or the wiped streak stays blank; or a sharp reflection appears where the hand never wiped.
- P2 [core · permanence_count]
  - expect: The streak matches the hand's path and slowly fogs over again.
  - fail: The streak is a different shape from the wipe; or it clears further by itself; or it fogs instantly.
- P3 [major · shape_identity]
  - expect: The reflection in the streak is the room, mirrored.
  - fail: It is a different room; or upright where it should be mirrored; or objects appear that are not in the room.
- P4 [major · material_response]
  - expect: The fog is a film of moisture the hand smears.
  - fail: It is a solid coating; or it peels; or the hand passes through the mirror.
- P5 [fatal · permanence_count]
  - expect: One mirror and one hand.
  - fail: The mirror duplicates; or a second hand appears; or the reflection becomes solid.
- P6 [minor · attribute_drift]
  - expect: The mirror frame and the room stay the same.
  - fail: The frame changes; or the room rearranges; or the wall changes colour.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0085 · reflection · train

**Caption.** A heron stands in shallow water on a still morning, and its reflection stands upside down beneath it; when it steps forward the reflection ripples.

**Expectation (hidden).** The reflection is inverted and joined at the legs; it wavers when the bird moves and is sharp when the bird is still.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A heron stands in shallow water on a still morning.
- S2 [core] Its reflection stands upside down beneath it.
- S3 [core] It steps forward.
- S4 [core] The reflection ripples.
- S5 [minor] The reflection is sharp when the bird is still.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflection wavers when the bird moves and is sharp when the bird is still.
  - fail: It is sharp while the bird steps; or it wavers with the bird still on flat water; or it is missing.
- P2 [core · shape_identity]
  - expect: The reflection is inverted and joined at the legs.
  - fail: It is upright; or detached; or a different bird.
- P3 [major · material_response]
  - expect: The water is liquid: ripples spread from the step and fade.
  - fail: It is rigid; or the ripples freeze; or ripples appear where the bird did not step.
- P4 [major · causeless_motion]
  - expect: The reflection does not move on its own.
  - fail: It moves with the bird still; or drifts.
- P5 [fatal · permanence_count]
  - expect: One heron and one reflection; the reflection stays on the water.
  - fail: A second heron appears; or the reflection rises off the water; or the bird vanishes; or the reflection becomes solid.
- P6 [minor · attribute_drift]
  - expect: The plumage and the water stay the same.
  - fail: The plumage changes; or the water changes colour; or the bank rearranges.

**Note.** Self-driven animal: where it goes and how it moves are not judged. Only the reflection's relation to it is.

## OPT-0086 · reflection · train

**Caption.** A car's side mirror is adjusted from inside, and the view in the mirror sweeps from the sky down to the road behind.

**Expectation (hidden).** The view moves smoothly as the mirror tilts and shows the scene behind the car, not in front; it stops changing when the adjustment stops.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A car's side mirror is adjusted from inside.
- S2 [core] The view in the mirror sweeps from the sky down to the road behind.
- S3 [minor] The view stops changing when the adjustment stops.
- S4 [minor] The mirror shows the scene behind the car.

**PC**
- P1 [core · missing_consequence]
  - expect: The view moves smoothly as the mirror tilts and shows the scene behind the car, not in front.
  - fail: It stays fixed as the mirror tilts; or it shows the road ahead; or it jumps.
- P2 [core · causeless_motion]
  - expect: The view changes only while the mirror moves and stops when the adjustment stops.
  - fail: It sweeps with the mirror still; or keeps moving after the adjustment stops; or changes before it.
- P3 [major · shape_identity]
  - expect: The reflected scene is mirrored.
  - fail: Lettering reads the right way round; or the scene is not mirrored; or it is upside down.
- P4 [major · material_response]
  - expect: The mirror is rigid: the view is undistorted.
  - fail: It ripples; or warps; or bends.
- P5 [fatal · permanence_count]
  - expect: One mirror on one car.
  - fail: The mirror duplicates or vanishes; or the reflection becomes solid; or the mirror passes through the door.
- P6 [minor · attribute_drift]
  - expect: The car and the surroundings stay the same.
  - fail: The car changes colour; or the mirror housing changes; or the surroundings rearrange.

## OPT-0087 · reflection · train

**Caption.** A soap bubble drifts past a bright window, and a tiny reflection of the window curves across the bubble's surface.

**Expectation (hidden).** The bright window is visible as a small curved highlight that moves across the bubble as it drifts; it vanishes when the bubble pops.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A soap bubble drifts past a bright window.
- S2 [core] A tiny reflection of the window curves across the bubble's surface.
- S3 [minor] The reflection moves across the bubble as it drifts.
- S4 [minor] The reflection vanishes when the bubble pops.

**PC**
- P1 [core · missing_consequence]
  - expect: The window shows as a small curved highlight that moves across the bubble as it drifts.
  - fail: The highlight stays fixed on the bubble while it drifts past the window; or it is missing beside a bright window; or it shows something not in the room.
- P2 [core · shape_identity]
  - expect: The highlight is curved to the bubble and stays on its surface.
  - fail: It is a flat rectangle; or it floats off the bubble; or it is larger than the bubble.
- P3 [major · material_response]
  - expect: The bubble is a thin iridescent film that wobbles and pops into nothing.
  - fail: It is rigid; or bounces like a ball; or pops into shards.
- P4 [major · gravity_direction]
  - expect: The bubble drifts and sinks slowly.
  - fail: It rises steadily; or drops like a stone; or hangs still.
- P5 [fatal · permanence_count]
  - expect: One bubble and one highlight.
  - fail: A second bubble appears from nowhere; or the popped bubble reappears; or the highlight becomes solid.
- P6 [minor · attribute_drift]
  - expect: The window and the room stay the same.
  - fail: The window changes; or the room rearranges; or the bubble changes colour abruptly.

## OPT-0088 · reflection · train

**Caption.** A pair of sunglasses lies on a table facing a lamp, and the lamp shows as two small images in the lenses.

**Expectation (hidden).** The small images move if the lamp or glasses move and are curved to the lenses; they show the lamp, not what is behind the glasses.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A pair of sunglasses lies on a table facing a lamp.
- S2 [core] The lamp shows as two small images in the lenses.
- S3 [minor] The images are curved to the lenses.
- S4 [minor] The images show the lamp, not what is behind the glasses.

**PC**
- P1 [core · missing_consequence]
  - expect: The images show the lamp and would move if the lamp or glasses moved.
  - fail: They show something behind the glasses; or they are missing with the lamp on; or they show a different lamp.
- P2 [core · shape_identity]
  - expect: There are two images, one per lens, each curved to its lens.
  - fail: There is one image or three; or they are flat; or they are larger than the lenses.
- P3 [major · causeless_motion]
  - expect: The images do not move with the lamp and glasses still.
  - fail: They drift across the lenses; or flicker with a steady lamp.
- P4 [major · material_response]
  - expect: The lenses are rigid.
  - fail: They ripple; or bend; or go opaque.
- P5 [fatal · permanence_count]
  - expect: One pair of glasses and one lamp.
  - fail: The glasses duplicate; or the lamp vanishes; or an image becomes solid.
- P6 [minor · attribute_drift]
  - expect: The glasses, the lamp and the table stay the same.
  - fail: The frames change colour; or the lamp changes; or the table changes.

## OPT-0089 · reflection · train

**Caption.** A motorboat crosses a glassy lake at low speed, and its reflection travels with it, broken only by the wake.

**Expectation (hidden).** The reflection is inverted and attached at the waterline; it distorts in the wake behind.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A motorboat crosses a glassy lake at low speed.
- S2 [core] Its reflection travels with it.
- S3 [minor] The reflection is broken only by the wake.
- S4 [minor] The reflection is attached at the waterline.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflection travels with the boat and distorts only in the wake behind.
  - fail: It stays still while the boat moves; or it is broken ahead of the boat; or it lags.
- P2 [core · shape_identity]
  - expect: The reflection is inverted and attached at the waterline.
  - fail: It is upright; or detached; or a different boat.
- P3 [major · material_response]
  - expect: The water is liquid: the wake spreads behind and the surface ahead is flat.
  - fail: It is rigid; or the wake runs ahead; or the water leaps.
- P4 [major · causeless_motion]
  - expect: The reflection does not move on its own.
  - fail: It moves with the boat stopped; or drifts.
- P5 [fatal · permanence_count]
  - expect: One boat and one reflection; the reflection stays on the water.
  - fail: A second boat appears; or the reflection rises off the water; or the boat vanishes; or the reflection becomes solid.
- P6 [minor · attribute_drift]
  - expect: The boat and the shore stay the same.
  - fail: The boat changes colour; or the shore rearranges; or the sky changes abruptly.

## OPT-0090 · reflection · train

**Caption.** A compact mirror is opened and angled toward a ring on a table, and the ring appears in the little mirror.

**Expectation (hidden).** The ring comes into view when the mirror is angled toward it and slides out of view when the angle changes; the image is mirrored.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A compact mirror is opened.
- S2 [core] It is angled toward a ring on a table.
- S3 [core] The ring appears in the little mirror.
- S4 [minor] The image is mirrored.
- S5 [minor] The ring slides out of view when the angle changes.

**PC**
- P1 [core · missing_consequence]
  - expect: The ring comes into view when the mirror is angled toward it and slides out of view when the angle changes.
  - fail: The ring is in the mirror with the mirror facing away; or the mirror is angled at it and shows nothing; or the image stays fixed as the angle changes.
- P2 [core · shape_identity]
  - expect: The image is the ring, mirrored.
  - fail: It is a different object; or not mirrored; or larger than the ring.
- P3 [major · causeless_motion]
  - expect: The ring stays put and the image changes only as the mirror moves.
  - fail: The ring slides; or the image shifts with the mirror still.
- P4 [major · material_response]
  - expect: The mirror is flat and rigid: the image is undistorted.
  - fail: It ripples; or warps; or bends.
- P5 [fatal · permanence_count]
  - expect: One mirror and one ring.
  - fail: The ring duplicates; or the mirror vanishes; or the image becomes solid; or the hand passes through the mirror.
- P6 [minor · attribute_drift]
  - expect: The ring, the mirror and the table stay the same.
  - fail: The ring changes colour; or the compact changes; or the table changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0091 · reflection · train

**Caption.** A neon sign glows above a rain-soaked street at night, and its coloured reflection streaks down the wet pavement toward the viewer.

**Expectation (hidden).** The reflection has the same colours as the sign, lies below it on the wet surface, and shimmers where puddles ripple; it fades where the pavement is dry.

**Declared violation types.** missing_consequence, attribute_drift

**SA**
- S1 [core] A neon sign glows above a rain-soaked street at night.
- S2 [core] Its coloured reflection streaks down the wet pavement toward the viewer.
- S3 [minor] The reflection has the same colours as the sign.
- S4 [minor] The reflection fades where the pavement is dry.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflection lies below the sign on the wet surface and fades where the pavement is dry.
  - fail: It lies above the sign; or shows on dry pavement; or it is missing on plainly wet ground.
- P2 [core · attribute_drift]
  - expect: The reflection has the same colours as the sign.
  - fail: It is a different colour; or brighter than the sign; or it changes colour with the sign steady.
- P3 [major · material_response]
  - expect: The pavement is wet: the reflection shimmers where puddles ripple.
  - fail: It is a sharp mirror image on rough ground; or it is rigid on rippling puddles; or the water flows uphill.
- P4 [major · causeless_motion]
  - expect: The reflection does not move on its own.
  - fail: It drifts along the pavement; or flickers with the sign steady.
- P5 [fatal · permanence_count]
  - expect: One sign and one reflection.
  - fail: A second sign appears; or the reflection becomes solid; or the sign vanishes.
- P6 [minor · attribute_drift]
  - expect: The sign's lettering and the street stay the same.
  - fail: The lettering changes; or the street rearranges; or the buildings change.

## OPT-0092 · reflection · train

**Caption.** A cat bats at its reflection in a shiny chrome kettle, and the reflected paw bats back from inside the metal.

**Expectation (hidden).** The reflection moves at the same time, mirrored and warped by the curve of the kettle; the reflected paw cannot leave the surface.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A cat is in front of a shiny chrome kettle.
- S2 [core] It bats at its reflection.
- S3 [core] The reflected paw bats back from inside the metal.
- S4 [minor] The reflection is warped by the curve of the kettle.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflection moves at the same time as the cat.
  - fail: It moves first or later; or stays still while the cat bats; or bats while the cat is still.
- P2 [core · shape_identity]
  - expect: The reflection is a mirror image, warped by the curve, and the reflected paw cannot leave the surface.
  - fail: The reflected paw comes out of the kettle; or the reflection is flat and undistorted on a plainly curved surface; or it is a different animal.
- P3 [major · causeless_motion]
  - expect: The kettle stays put.
  - fail: It slides; or rocks by itself; or lifts.
- P4 [major · material_response]
  - expect: The kettle is rigid polished metal.
  - fail: It dents under the paw; or its surface ripples; or it goes dull.
- P5 [fatal · permanence_count]
  - expect: One cat and one kettle; the reflection stays in the metal.
  - fail: A second cat appears; or the reflection steps out; or the cat passes into the kettle; or the cat vanishes.
- P6 [minor · attribute_drift]
  - expect: The cat's markings and the kitchen stay the same.
  - fail: The markings change; or the kettle changes colour; or the kitchen rearranges.

**Note.** Self-driven animal: where it goes and how it moves are not judged. Only the reflection's relation to it is.

## OPT-0093 · reflection · train

**Caption.** The reflection of a moored boat lies on clear still water, and when the boat rocks the reflection breaks apart and then settles.

**Expectation (hidden).** The reflection is inverted and clear while the water is flat; it wavers and fragments as the boat rocks and returns when the water calms.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A moored boat's reflection lies on clear still water.
- S2 [core] The boat rocks.
- S3 [core] The reflection breaks apart.
- S4 [core] It settles again.
- S5 [minor] The rocking comes first, then the break-up, then the settling.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflection wavers and fragments as the boat rocks and returns when the water calms.
  - fail: It stays sharp while the boat rocks; or breaks up with the boat still; or never returns on calm water.
- P2 [core · shape_identity]
  - expect: The clear reflection is the boat inverted, attached at the waterline.
  - fail: It is upright; or detached; or a different boat.
- P3 [major · material_response]
  - expect: The water is liquid: ripples spread from the hull and fade.
  - fail: It is rigid; or the ripples freeze; or the water leaps.
- P4 [major · causeless_motion]
  - expect: The reflection does not move with the boat and water still.
  - fail: It drifts; or shifts on a flat calm.
- P5 [fatal · permanence_count]
  - expect: One boat and one reflection; the reflection stays on the water.
  - fail: A second boat appears; or the reflection rises off the water; or the boat vanishes; or the reflection becomes solid.
- P6 [minor · attribute_drift]
  - expect: The boat and the mooring stay the same.
  - fail: The boat changes colour; or the mooring changes; or the shore rearranges.

## OPT-0094 · reflection · train

**Caption.** A disco ball turns under the stage lights, and dozens of small bright spots sweep across the walls.

**Expectation (hidden).** The spots move when the ball turns and stop when it stops; they appear on the walls away from the lights.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A disco ball turns under stage lights.
- S2 [core] Dozens of small bright spots sweep across the walls.
- S3 [minor] The spots move when the ball turns and stop when it stops.
- S4 [minor] The spots appear on the walls away from the lights.

**PC**
- P1 [core · missing_consequence]
  - expect: The spots move when the ball turns and stop when it stops.
  - fail: They are still while the ball turns; or sweep while the ball is still; or move out of time with it.
- P2 [core · causeless_motion]
  - expect: The spots do not move on their own.
  - fail: They dance with the ball stopped; or flicker with steady lights.
- P3 [major · shape_identity]
  - expect: The spots are many small bright patches, each roughly a facet's shape.
  - fail: They merge into one flood; or they are sharp geometric shapes unlike facets; or they are a single spot.
- P4 [major · trajectory_momentum]
  - expect: The spots all sweep the same way round the room as the ball turns one way.
  - fail: Some sweep the opposite way; or they jump; or they move crosswise.
- P5 [fatal · permanence_count]
  - expect: One ball and its lights.
  - fail: A second ball appears; or the ball vanishes; or a spot becomes solid.
- P6 [minor · attribute_drift]
  - expect: The room and the stage lights stay the same.
  - fail: The room rearranges; or the lights change colour abruptly; or the ball changes.

## OPT-0095 · reflection · train

**Caption.** A sheet of glass is held at an angle to a window, and the garden outside appears faintly in the glass over the room behind it.

**Expectation (hidden).** The reflected garden is dim and mirrored, shifts as the glass tilts, and disappears when the glass is laid flat away from the window.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A sheet of glass is held at an angle to a window.
- S2 [core] The garden outside appears faintly in the glass over the room behind it.
- S3 [minor] The reflected garden shifts as the glass tilts.
- S4 [minor] The reflected garden is dim and mirrored.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflected garden shifts as the glass tilts and would disappear if the glass were laid flat away from the window.
  - fail: It stays fixed as the glass tilts; or it is there with the glass facing away from the window; or it is missing with the glass angled to the window.
- P2 [core · shape_identity]
  - expect: The reflected garden is dim and mirrored, seen over the room behind the glass.
  - fail: It is brighter than the room; or not mirrored; or the room behind is hidden.
- P3 [major · causeless_motion]
  - expect: The reflection changes only as the glass moves.
  - fail: It shifts with the glass still; or moves before the tilt.
- P4 [major · material_response]
  - expect: The glass is flat and rigid: the reflection is undistorted.
  - fail: It ripples; or warps; or bends.
- P5 [fatal · permanence_count]
  - expect: One sheet of glass and one window.
  - fail: The glass duplicates; or the hand passes through it; or the reflection becomes solid.
- P6 [minor · attribute_drift]
  - expect: The garden, the room and the window stay the same.
  - fail: The garden changes; or the room rearranges; or the window changes.

**Note.** The hands holding the glass are the minimal trigger; the person is not judged.

## OPT-0096 · reflection · train

**Caption.** A red ball rolls along a hallway of polished steel panels, and a blurry reflection rolls alongside in each panel.

**Expectation (hidden).** Each panel shows a mirrored, slightly warped copy of the ball moving in step; the copies vanish at the gaps between panels.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A red ball rolls along a hallway of polished steel panels.
- S2 [core] A blurry reflection rolls alongside in each panel.
- S3 [minor] The copies vanish at the gaps between panels.
- S4 [minor] Each copy is mirrored and slightly warped.

**PC**
- P1 [core · missing_consequence]
  - expect: Each panel shows a copy of the ball moving in step, and the copies vanish at the gaps between panels.
  - fail: A copy stays still while the ball rolls; or a copy shows across a gap; or a panel shows no copy.
- P2 [core · shape_identity]
  - expect: Each copy is a mirrored, slightly warped red ball.
  - fail: A copy is a different colour; or a different object; or perfectly sharp on a plainly brushed surface.
- P3 [major · causeless_motion]
  - expect: The ball rolls straight and slows gently.
  - fail: It curves; or speeds up; or restarts.
- P4 [major · material_response]
  - expect: The panels are rigid metal.
  - fail: A panel ripples; or bends; or the ball dents it.
- P5 [fatal · permanence_count]
  - expect: One ball and one copy per panel.
  - fail: A second ball appears in the hallway; or a copy steps out; or the ball vanishes; or the ball passes into a panel.
- P6 [minor · attribute_drift]
  - expect: The ball's colour and the hallway stay the same.
  - fail: The ball changes colour; or the panels change; or the hallway rearranges.

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

## OPT-0099 · refraction_transparency · train

**Caption.** A bird hops across a lawn outside a clear window and is seen through the glass.

**Expectation (hidden).** The bird is fully visible through the pane, undistorted, and moves continuously behind it; the glass does not make it vanish or appear inside.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A bird hops across a lawn outside a clear window.
- S2 [core] It is seen through the glass.
- S3 [minor] The bird is fully visible and undistorted through the pane.

**PC**
- P1 [core · missing_consequence]
  - expect: The bird is fully visible through the pane and moves continuously behind it.
  - fail: The glass hides the bird; or the bird flickers in and out of view behind clear glass; or it is distorted by a flat pane.
- P2 [core · permanence_count]
  - expect: The glass does not make the bird vanish or appear inside the room.
  - fail: The bird vanishes behind the glass; or it appears inside the room; or a second bird appears.
- P3 [major · solidity]
  - expect: The bird stays outside the window.
  - fail: It passes through the glass; or the glass passes through it; or it perches inside the pane.
- P4 [major · material_response]
  - expect: The pane is flat and rigid.
  - fail: It ripples; or bends; or goes opaque.
- P5 [fatal · shape_identity]
  - expect: One bird keeps its shape.
  - fail: It splits; or turns into another animal; or merges with the frame.
- P6 [minor · attribute_drift]
  - expect: The plumage, the lawn and the window frame stay the same.
  - fail: The plumage changes; or the lawn rearranges; or the frame changes.

**Note.** The bird is self-driven; only transparency and containment are judged.

## OPT-0100 · refraction_transparency · train

**Caption.** Rain streams down a window, and the trees outside seen through the wet glass wobble and blur where the water runs.

**Expectation (hidden).** The view is distorted only along the running water and clear elsewhere; the distortion moves downward with the drops.

**Declared violation types.** shape_identity, missing_consequence

**SA**
- S1 [core] Rain streams down a window.
- S2 [core] Trees outside are seen through the wet glass.
- S3 [core] The view wobbles and blurs where the water runs.
- S4 [minor] The distortion moves downward with the drops.

**PC**
- P1 [core · missing_consequence]
  - expect: The view is distorted only along the running water and clear elsewhere.
  - fail: The whole pane is blurred with only a few tracks; or the tracks leave the view sharp; or the blur is where no water runs.
- P2 [core · shape_identity]
  - expect: The trees themselves are unchanged; only their image wobbles along the tracks.
  - fail: The trees bend; or a different scene appears in a track; or the trees change shape between tracks.
- P3 [major · gravity_direction]
  - expect: The water runs downward and the distortion moves with it.
  - fail: Water runs up the glass; or the tracks are still while blur moves; or drops hang without moving.
- P4 [major · material_response]
  - expect: The water is liquid running in tracks and the glass is rigid.
  - fail: The water is rigid; or the glass ripples; or the drops bounce.
- P5 [fatal · permanence_count]
  - expect: One window and the trees outside.
  - fail: A tree vanishes; or a second window appears; or the water becomes solid.
- P6 [minor · attribute_drift]
  - expect: The frame and the trees' colours stay the same.
  - fail: The frame changes; or the trees change colour; or the room changes.

## OPT-0101 · refraction_transparency · train

**Caption.** A magnifying glass is moved over a page of small print, and the letters under the lens appear much larger.

**Expectation (hidden).** Only the letters seen through the lens are enlarged and they shift as the lens moves; the print outside the lens stays small.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A magnifying glass is moved over a page of small print.
- S2 [core] The letters under the lens appear much larger.
- S3 [minor] The print outside the lens stays small.
- S4 [minor] The enlarged letters shift as the lens moves.

**PC**
- P1 [core · missing_consequence]
  - expect: Only the letters seen through the lens are enlarged, and they shift as the lens moves.
  - fail: Letters outside the lens are enlarged; or the letters under the lens are the same size; or the enlarged patch stays put while the lens moves.
- P2 [core · shape_identity]
  - expect: The page itself is unchanged; the enlarged letters are the same words, larger.
  - fail: The letters under the lens are different words; or the page's print changes; or the enlarged letters are mirrored.
- P3 [major · causeless_motion]
  - expect: The page stays put and the image changes only as the lens moves.
  - fail: The page slides; or the image shifts with the lens still; or letters move by themselves.
- P4 [major · material_response]
  - expect: The lens is rigid glass.
  - fail: It bends; or ripples; or goes opaque.
- P5 [fatal · permanence_count]
  - expect: One lens and one page.
  - fail: The lens duplicates; or the page vanishes; or the hand passes through the lens.
- P6 [minor · attribute_drift]
  - expect: The page and the lens frame stay the same.
  - fail: The paper changes colour; or the frame changes; or the desk changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0102 · refraction_transparency · train

**Caption.** A pair of reading glasses is slid across a menu, and the text seen through the lenses appears slightly larger than the text around the frames.

**Expectation (hidden).** The change happens only in the area seen through the lenses and moves with the glasses; the menu itself does not change.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A pair of reading glasses is slid across a menu.
- S2 [core] The text seen through the lenses appears slightly larger than the text around the frames.
- S3 [minor] The enlargement moves with the glasses.

**PC**
- P1 [core · missing_consequence]
  - expect: The change happens only in the area seen through the lenses and moves with the glasses.
  - fail: Text outside the frames is enlarged; or text under the lenses is unchanged; or the enlarged patch stays put while the glasses slide.
- P2 [core · shape_identity]
  - expect: The menu itself does not change; the enlarged text is the same text.
  - fail: The text under the lenses is different; or the menu changes; or the enlarged text is mirrored.
- P3 [major · causeless_motion]
  - expect: The menu stays put and the glasses move only as pushed.
  - fail: The menu slides; or the glasses move by themselves; or the image shifts with the glasses still.
- P4 [major · material_response]
  - expect: The lenses are rigid.
  - fail: They bend; or ripple; or go opaque.
- P5 [fatal · permanence_count]
  - expect: One pair of glasses and one menu.
  - fail: The glasses duplicate; or the menu vanishes; or the hand passes through the glasses.
- P6 [minor · attribute_drift]
  - expect: The menu and the frames stay the same.
  - fail: The menu changes colour; or the frames change; or the table changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0103 · refraction_transparency · train

**Caption.** The tiles on the floor of a clear pool are seen through the water, their grid wavering slightly with the surface.

**Expectation (hidden).** The tiles are visible and their grid wavers slightly with the water surface; they do not disappear or move on their own.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] The tiles on the floor of a clear pool are seen through the water.
- S2 [core] Their grid wavers slightly with the surface.
- S3 [minor] The tiles are visible throughout.

**PC**
- P1 [core · missing_consequence]
  - expect: The tiles are visible through the water and their grid wavers with the surface.
  - fail: The water hides the tiles; or the grid is rigid on a plainly rippled surface; or the grid wavers on a flat calm.
- P2 [core · shape_identity]
  - expect: The tiles themselves do not move; only their image wavers.
  - fail: Tiles slide across the floor; or the grid changes pattern; or tiles appear and vanish.
- P3 [major · material_response]
  - expect: The water is liquid: ripples pass and fade.
  - fail: It is rigid; or ripples freeze; or the water leaps.
- P4 [major · causeless_motion]
  - expect: The surface moves only with a visible cause.
  - fail: It churns with nothing disturbing it; or ripples run against the wind; or the whole pool jumps.
- P5 [fatal · permanence_count]
  - expect: One pool with its tiles.
  - fail: Tiles vanish; or a second floor appears; or the water becomes solid.
- P6 [minor · attribute_drift]
  - expect: The tiles' colours and the pool's edge stay the same.
  - fail: The tiles change colour; or the edge moves; or the surroundings rearrange.

## OPT-0104 · refraction_transparency · train

**Caption.** A glass of water is set in front of a card printed with a straight vertical line, and the line seen through the glass looks shifted and wider.

**Expectation (hidden).** The line appears displaced only behind the water-filled part of the glass and returns to normal when the glass is moved away.

**Declared violation types.** shape_identity, missing_consequence

**SA**
- S1 [core] A card is printed with a straight vertical line.
- S2 [core] A glass of water is set in front of it.
- S3 [core] The line seen through the glass looks shifted and wider.
- S4 [minor] The line returns to normal when the glass is moved away.

**PC**
- P1 [core · missing_consequence]
  - expect: The line appears displaced only behind the water-filled part of the glass and returns to normal when the glass is moved.
  - fail: The line is displaced beside the glass; or it is unchanged behind the water; or it stays displaced after the glass is gone.
- P2 [core · shape_identity]
  - expect: The card and its line are unchanged; the shift is an appearance.
  - fail: The line on the card moves; or a second line is printed; or the card bends.
- P3 [major · material_response]
  - expect: The water surface is level and the glass is rigid.
  - fail: The water tilts and holds; or the glass warps; or the water goes opaque.
- P4 [major · causeless_motion]
  - expect: The card and the glass stay put unless moved by the hand.
  - fail: The card slides; or the glass moves by itself; or the image shifts with both still.
- P5 [fatal · permanence_count]
  - expect: One glass and one card.
  - fail: The glass duplicates; or the card vanishes; or the glass passes through the card.
- P6 [minor · attribute_drift]
  - expect: The card, the glass and the table stay the same.
  - fail: The card changes colour; or the glass changes shape; or the table changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0105 · refraction_transparency · train

**Caption.** A drop of water lands on a phone screen, and the tiny pixels under the drop appear magnified.

**Expectation (hidden).** The enlarged pattern shows only within the drop and moves if the drop slides; the screen beyond the drop is unchanged.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A drop of water lands on a phone screen.
- S2 [core] The tiny pixels under the drop appear magnified.
- S3 [minor] The screen beyond the drop is unchanged.

**PC**
- P1 [core · missing_consequence]
  - expect: The enlarged pattern shows only within the drop and would move if the drop slid.
  - fail: Pixels outside the drop are enlarged; or the drop shows nothing different; or the enlarged patch is offset from the drop.
- P2 [core · shape_identity]
  - expect: The screen itself is unchanged; the magnified pattern is its own pixels.
  - fail: The screen's picture changes; or a different pattern appears in the drop; or the drop shows a mirror image.
- P3 [major · material_response]
  - expect: The drop is a rounded bead of liquid.
  - fail: It is a rigid lens; or it spreads flat and thin instantly; or it bounces.
- P4 [major · gravity_direction]
  - expect: The drop lands and sits on the screen.
  - fail: It hangs above the screen; or rises; or slides uphill.
- P5 [fatal · permanence_count]
  - expect: One drop and one phone.
  - fail: The drop duplicates; or the phone vanishes; or the drop passes through the screen.
- P6 [minor · attribute_drift]
  - expect: The phone and the surroundings stay the same.
  - fail: The phone changes; or the table changes; or the screen colours shift.

## OPT-0106 · refraction_transparency · train

**Caption.** A clear ice cube is held up to a window, and the scene outside is visible through the ice, slightly blurred.

**Expectation (hidden).** Light and shapes come through the cube; the view is distorted at its edges and where it has cracks; the cube does not block the view like a stone.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A clear ice cube is held up to a window.
- S2 [core] The scene outside is visible through the ice.
- S3 [minor] The view is slightly blurred.
- S4 [minor] The view is distorted at the cube's edges and cracks.

**PC**
- P1 [core · missing_consequence]
  - expect: Light and shapes come through the cube, distorted at its edges and cracks.
  - fail: The cube blocks the view like a stone; or the view is perfectly sharp with no distortion; or the cube shows a different scene.
- P2 [core · shape_identity]
  - expect: The scene outside is unchanged; only its image through the ice is blurred.
  - fail: The scene changes; or objects appear in the cube that are not outside; or the image is upside down.
- P3 [major · material_response]
  - expect: The ice is rigid and clear, and may drip.
  - fail: It flows; or goes opaque; or shatters untouched.
- P4 [major · causeless_motion]
  - expect: The cube moves only with the hand.
  - fail: It floats; or turns by itself; or jumps.
- P5 [fatal · permanence_count]
  - expect: One cube and one window.
  - fail: The cube duplicates; or vanishes; or the hand passes through it.
- P6 [minor · attribute_drift]
  - expect: The window and the scene stay the same.
  - fail: The frame changes; or the scene rearranges; or the cube changes colour.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0107 · refraction_transparency · train

**Caption.** A cat moves behind a frosted glass door, and only a blurred shape of it is visible through the glass.

**Expectation (hidden).** The blur moves as the cat moves and sharpens as it comes closer to the glass; details never become clear through the frosting.

**Declared violation types.** shape_identity, permanence_count

**SA**
- S1 [core] A cat moves behind a frosted glass door.
- S2 [core] Only a blurred shape of it is visible through the glass.
- S3 [minor] The blur moves as the cat moves.
- S4 [minor] The blur sharpens as the cat comes closer to the glass.

**PC**
- P1 [core · shape_identity]
  - expect: Only a blur is seen; details never become clear through the frosting.
  - fail: The cat is sharp through the frosted glass; or the blur is a different shape from a cat; or the blur has crisp edges.
- P2 [core · missing_consequence]
  - expect: The blur moves as the cat moves and sharpens as it nears the glass.
  - fail: The blur stays still while the cat moves; or it sharpens as the cat moves away; or it moves with no cat.
- P3 [major · permanence_count]
  - expect: The cat does not appear on the near side while the blur is behind the glass.
  - fail: The cat appears in the room; or two blurs appear for one cat; or the blur vanishes while the cat is plainly behind the glass.
- P4 [major · solidity]
  - expect: The cat stays behind the door.
  - fail: It passes through the glass; or the door passes through it; or it appears inside the pane.
- P5 [fatal · shape_identity]
  - expect: One cat stays one cat.
  - fail: It splits; or turns into another animal; or merges with the door.
- P6 [minor · attribute_drift]
  - expect: The door and the frosting stay the same.
  - fail: The frosting clears; or the door changes; or the room changes.

**Note.** The cat is self-driven; only the frosted view is judged.

## OPT-0108 · refraction_transparency · train

**Caption.** Windshield wipers sweep in heavy rain, and each sweep clears a sharp view of the road that blurs again as rain lands.

**Expectation (hidden).** The view is clear immediately behind each wiper stroke and degrades between strokes; the rain does not clear itself.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] Windshield wipers sweep in heavy rain.
- S2 [core] Each sweep clears a sharp view of the road.
- S3 [core] The view blurs again as rain lands.
- S4 [minor] Each sweep comes first and the clear view follows it.

**PC**
- P1 [core · missing_consequence]
  - expect: The view is clear immediately behind each wiper stroke and degrades between strokes.
  - fail: The view stays blurred behind the wiper; or it is clear with no wipe; or the rain clears itself.
- P2 [core · process_direction]
  - expect: Clearing and re-blurring alternate with the strokes.
  - fail: The view stays clear through heavy rain with the wipers stopped; or it blurs during a stroke; or it flickers.
- P3 [major · causeless_motion]
  - expect: The wipers sweep in their arc and the rain falls.
  - fail: The wipers stop mid-arc with nothing wrong; or rain falls upward; or the wipers pass through each other.
- P4 [major · material_response]
  - expect: Raindrops are liquid that spread and run.
  - fail: They are rigid beads; or they bounce off; or they freeze in place.
- P5 [fatal · permanence_count]
  - expect: Two wipers and one windshield.
  - fail: A wiper vanishes; or a third appears; or the windshield duplicates.
- P6 [minor · attribute_drift]
  - expect: The car interior and the road stay the same.
  - fail: The dashboard changes; or the road rearranges; or the wipers change.

## OPT-0109 · refraction_transparency · train

**Caption.** A patterned card is seen through a round fishbowl, and the pattern appears stretched and warped through the bowl; as the card is moved the warp changes.

**Expectation (hidden).** The distortion appears only through the water-filled bowl and changes as the card moves; the pattern is normal when seen past the bowl's edge.

**Declared violation types.** shape_identity, missing_consequence

**SA**
- S1 [core] A patterned card is seen through a round fishbowl.
- S2 [core] The pattern appears stretched and warped through the bowl.
- S3 [core] The card is moved.
- S4 [core] The warp changes.
- S5 [minor] The pattern is normal seen past the bowl's edge.

**PC**
- P1 [core · missing_consequence]
  - expect: The distortion appears only through the water-filled bowl and changes as the card moves.
  - fail: The pattern is warped beside the bowl; or unwarped through it; or the warp stays fixed as the card moves.
- P2 [core · shape_identity]
  - expect: The card and its pattern are unchanged; the warp is an appearance.
  - fail: The card bends; or the pattern changes; or a different pattern appears through the bowl.
- P3 [major · material_response]
  - expect: The bowl is rigid and the water level.
  - fail: The bowl warps; or the water tilts and holds; or the water goes opaque.
- P4 [major · causeless_motion]
  - expect: The bowl stays put and the card moves only with the hand.
  - fail: The bowl slides; or the card moves by itself; or the image shifts with both still.
- P5 [fatal · permanence_count]
  - expect: One bowl and one card.
  - fail: The bowl duplicates; or the card vanishes; or the card passes through the bowl.
- P6 [minor · attribute_drift]
  - expect: The card's colours and the table stay the same.
  - fail: The card changes colour; or the table changes; or the bowl changes shape.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0110 · refraction_transparency · train

**Caption.** Seen from under the water, the wavering shapes of the trees and the pool ladder show through the surface.

**Expectation (hidden).** The shapes are visible but their outlines ripple with the surface; they steady when the water is calm.

**Declared violation types.** shape_identity, missing_consequence

**SA**
- S1 [core] The view is from under the water.
- S2 [core] The wavering shapes of trees and a pool ladder show through the surface.
- S3 [minor] The shapes steady when the water is calm.

**PC**
- P1 [core · missing_consequence]
  - expect: The shapes are visible through the surface and their outlines ripple with it.
  - fail: The surface is opaque; or the shapes are rigid on a plainly rippled surface; or they ripple on a flat calm.
- P2 [core · shape_identity]
  - expect: The trees and ladder themselves do not move; only their image wavers.
  - fail: The ladder bends; or the trees sway with no wind; or a different scene appears.
- P3 [major · material_response]
  - expect: The surface is liquid: ripples pass and fade.
  - fail: It is rigid; or ripples freeze; or the water leaps.
- P4 [major · causeless_motion]
  - expect: The surface moves only with a visible cause.
  - fail: It churns with nothing disturbing it; or the view jumps; or the ladder moves.
- P5 [fatal · permanence_count]
  - expect: One ladder and the trees.
  - fail: The ladder vanishes; or a second appears; or the water becomes solid.
- P6 [minor · attribute_drift]
  - expect: The pool and the trees stay the same.
  - fail: The pool walls change; or the trees change colour; or the sky changes.

## OPT-0111 · refraction_transparency · train

**Caption.** Cakes on display are clearly visible through a bakery's front window as a tram passes behind the camera.

**Expectation (hidden).** The cakes appear sharp and in place behind the glass; the reflection of the street is faint over them; nothing is hidden by the pane.

**Declared violation types.** missing_consequence, solidity

**SA**
- S1 [core] Cakes are on display behind a bakery's front window.
- S2 [core] They are clearly visible through the glass.
- S3 [minor] A tram passes behind the camera, reflected faintly.
- S4 [minor] Nothing is hidden by the pane.

**PC**
- P1 [core · missing_consequence]
  - expect: The cakes appear sharp and in place behind the glass, with the street's reflection faint over them.
  - fail: The glass hides the cakes; or the reflection swamps the view; or the cakes are distorted by a flat pane.
- P2 [core · solidity]
  - expect: The cakes stay behind the glass and the reflection stays in it.
  - fail: A cake passes through the glass; or the reflected tram enters the shop; or the glass passes through a cake.
- P3 [major · causeless_motion]
  - expect: The cakes stay put.
  - fail: A cake slides; or rotates; or lifts.
- P4 [major · material_response]
  - expect: The pane is flat and rigid.
  - fail: It ripples; or bends; or goes opaque.
- P5 [fatal · permanence_count]
  - expect: The cakes keep their number.
  - fail: A cake vanishes; or appears; or a cake turns into another.
- P6 [minor · attribute_drift]
  - expect: The display and the shop front stay the same.
  - fail: The cakes change colour; or the shelves rearrange; or the frame changes.

## OPT-0112 · refraction_transparency · train

**Caption.** Water is poured into a clear jug standing in front of a patterned tile wall, and the pattern seen through the jug shifts as the water rises.

**Expectation (hidden).** The pattern looks different behind the filled part than behind the empty part, with the boundary at the water level; the wall itself does not change.

**Declared violation types.** shape_identity, missing_consequence

**SA**
- S1 [core] A clear jug stands in front of a patterned tile wall.
- S2 [core] Water is poured into it.
- S3 [core] The pattern seen through the jug shifts as the water rises.
- S4 [minor] The boundary of the shift is at the water level.

**PC**
- P1 [core · missing_consequence]
  - expect: The pattern looks different behind the filled part than behind the empty part, with the boundary at the water level.
  - fail: The pattern is the same above and below the water; or the boundary is away from the water level; or the shift is beside the jug.
- P2 [core · shape_identity]
  - expect: The wall itself does not change.
  - fail: The tiles move; or the pattern changes; or a different wall appears.
- P3 [major · process_direction]
  - expect: The water level rises steadily while pouring.
  - fail: It falls while pouring; or jumps; or is full before the pour.
- P4 [major · material_response]
  - expect: The stream falls as liquid and the jug is rigid.
  - fail: The stream is a rod; or the jug bends; or the water goes opaque.
- P5 [fatal · permanence_count]
  - expect: One jug, and water comes only from the pour.
  - fail: Water appears with no stream; or the jug duplicates; or water passes through the jug.
- P6 [minor · attribute_drift]
  - expect: The tiles' colours and the jug stay the same.
  - fail: The tiles change colour; or the jug changes shape; or the counter changes.

## OPT-0113 · refraction_transparency · train

**Caption.** A shopping cart is pushed up to a clear glass door which swings open, the cart having been fully visible through it as it approached.

**Expectation (hidden).** The cart is seen through the glass the whole way; the door opens on its hinges when pushed and the cart goes through the opening, not through the glass.

**Declared violation types.** missing_consequence, solidity

**SA**
- S1 [core] A shopping cart is pushed up to a clear glass door.
- S2 [core] The cart is fully visible through the door as it approaches.
- S3 [core] The door swings open.
- S4 [core] The cart goes through the opening.
- S5 [minor] The door opens first and the cart passes after.

**PC**
- P1 [core · missing_consequence]
  - expect: The cart is seen through the glass the whole way and the door opens on its hinges when pushed.
  - fail: The glass hides the cart; or the door opens with nothing pushing it; or it stays shut while the cart passes.
- P2 [core · solidity]
  - expect: The cart goes through the opening, not through the glass.
  - fail: It passes through the pane; or the door passes through it; or the cart is inside the glass.
- P3 [major · trajectory_momentum]
  - expect: The door swings in an arc on its hinges.
  - fail: It slides; or lifts; or spins.
- P4 [major · causeless_motion]
  - expect: The cart moves only as pushed.
  - fail: It rolls by itself; or jumps; or stops dead with no obstacle.
- P5 [fatal · permanence_count]
  - expect: One cart and one door.
  - fail: The cart duplicates; or the door vanishes; or the cart turns into another object.
- P6 [minor · attribute_drift]
  - expect: The cart and the doorway stay the same.
  - fail: The cart changes colour; or the frame changes; or the shop rearranges.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0114 · refraction_transparency · train

**Caption.** Coins lie on the bottom of a clear fountain, and they appear to shimmer and shift as the surface ripples.

**Expectation (hidden).** The coins are visible through the water and their apparent position wobbles with the ripples while they lie still; they do not actually move.

**Declared violation types.** shape_identity, causeless_motion

**SA**
- S1 [core] Coins lie on the bottom of a clear fountain.
- S2 [core] The surface ripples.
- S3 [core] The coins appear to shimmer and shift.
- S4 [minor] The coins are visible through the water throughout.

**PC**
- P1 [core · shape_identity]
  - expect: The coins lie still; only their apparent position wobbles with the ripples.
  - fail: The coins slide across the bottom; or a coin flips; or coins appear and vanish.
- P2 [core · causeless_motion]
  - expect: The wobble follows the ripples and stops when the water is still.
  - fail: The image wobbles on a flat calm; or the coins are sharp on a plainly rippled surface; or the wobble continues after the water settles.
- P3 [major · missing_consequence]
  - expect: The coins are visible through the water.
  - fail: The water hides them; or they are seen only above the surface; or a different set appears.
- P4 [major · material_response]
  - expect: The water is liquid: ripples pass and fade.
  - fail: It is rigid; or ripples freeze; or the water leaps.
- P5 [fatal · permanence_count]
  - expect: The coins keep their number.
  - fail: Coins vanish; or appear; or merge.
- P6 [minor · attribute_drift]
  - expect: The fountain and the coins' colours stay the same.
  - fail: The basin changes; or the coins change colour; or the surroundings rearrange.

## OPT-0115 · refraction_transparency · train

**Caption.** A clear plastic ruler is laid over a line of text, and the text is readable through the ruler.

**Expectation (hidden).** The letters are seen through the plastic with at most a slight shift at the ruler's edges; the ruler does not hide them.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A clear plastic ruler is laid over a line of text.
- S2 [core] The text is readable through the ruler.
- S3 [minor] There is at most a slight shift at the ruler's edges.

**PC**
- P1 [core · missing_consequence]
  - expect: The letters are seen through the plastic and the ruler does not hide them.
  - fail: The ruler hides the text; or it shows different text; or the text is heavily warped by a flat ruler.
- P2 [core · shape_identity]
  - expect: The text is unchanged; any shift is at the ruler's edges only.
  - fail: The text changes; or letters move under the ruler; or the text is mirrored.
- P3 [major · causeless_motion]
  - expect: The ruler and the page stay put unless moved.
  - fail: The ruler slides by itself; or the page moves; or the text shifts with both still.
- P4 [major · material_response]
  - expect: The ruler is rigid and clear.
  - fail: It bends; or goes opaque; or ripples.
- P5 [fatal · permanence_count]
  - expect: One ruler and one page.
  - fail: The ruler duplicates; or the page vanishes; or the ruler passes through the page.
- P6 [minor · attribute_drift]
  - expect: The page and the ruler's markings stay the same.
  - fail: The paper changes colour; or the markings change; or the desk changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0116 · refraction_transparency · train

**Caption.** Sunlight passes through a clear glass of water on a table, and a bright patch of light appears on the table on the far side of the glass.

**Expectation (hidden).** The bright patch lies on the side of the glass away from the sun and moves when the glass is moved; it disappears when the glass is taken away.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A clear glass of water stands on a table in sunlight.
- S2 [core] Sunlight passes through it.
- S3 [core] A bright patch of light appears on the table on the far side of the glass.
- S4 [minor] The patch moves when the glass is moved.

**PC**
- P1 [core · missing_consequence]
  - expect: The bright patch lies on the side of the glass away from the sun and would disappear if the glass were taken away.
  - fail: It lies on the sun side; or it is there with no glass; or the glass is in sunlight and no patch appears.
- P2 [core · causeless_motion]
  - expect: The patch moves only when the glass moves.
  - fail: It drifts with the glass still; or it stays put while the glass is moved; or it flickers in steady sun.
- P3 [major · shape_identity]
  - expect: The patch is one bright shape roughly the glass's footprint.
  - fail: It splits into several; or it is a sharp geometric shape unlike the glass; or it floods the table.
- P4 [major · material_response]
  - expect: The glass is rigid and the water level.
  - fail: The glass bends; or the water tilts and holds; or the water goes opaque.
- P5 [fatal · permanence_count]
  - expect: One glass and one patch.
  - fail: A second glass appears; or the patch becomes solid; or the glass vanishes.
- P6 [minor · attribute_drift]
  - expect: The glass and the table stay the same.
  - fail: The glass changes shape; or the table changes; or the water changes colour.

## OPT-0117 · refraction_transparency · train

**Caption.** A spoon stands in a clear glass jar of oil and looks kinked where it enters the oil; when it is lifted out the kink vanishes.

**Expectation (hidden).** The kink appears at the surface of the oil and vanishes when the spoon is lifted out; the spoon is straight.

**Declared violation types.** shape_identity, missing_consequence

**SA**
- S1 [core] A spoon stands in a clear glass jar of oil.
- S2 [core] It looks kinked where it enters the oil.
- S3 [core] It is lifted out.
- S4 [core] The kink vanishes.
- S5 [minor] The lift comes first and the kink vanishes with it.

**PC**
- P1 [core · missing_consequence]
  - expect: The kink sits at the surface of the oil and vanishes when the spoon is lifted out.
  - fail: The kink is above or below the surface; or it stays when the spoon is out; or the spoon looks straight in the oil.
- P2 [core · shape_identity]
  - expect: The spoon is straight and rigid; the kink is an appearance.
  - fail: The spoon is physically bent when out; or the kink stays at a fixed point on the spoon as it is raised; or the spoon flexes.
- P3 [major · material_response]
  - expect: The oil surface is level and the jar rigid.
  - fail: The oil tilts and holds; or the jar warps; or the oil goes opaque.
- P4 [major · causeless_motion]
  - expect: The spoon moves only with the hand.
  - fail: It rises by itself; or slides; or jumps.
- P5 [fatal · permanence_count]
  - expect: One spoon and one jar.
  - fail: The spoon duplicates; or the jar vanishes; or the spoon passes through the jar.
- P6 [minor · attribute_drift]
  - expect: The spoon, the oil's colour and the jar stay the same.
  - fail: The spoon changes colour; or the oil changes colour; or the jar changes shape.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0118 · refraction_transparency · train

**Caption.** Raindrops cover a window, and the street outside appears as many tiny warped pictures within the drops.

**Expectation (hidden).** Each drop shows a small distorted picture of the scene; the pictures move as the drops run down; the view between drops is normal.

**Declared violation types.** shape_identity, missing_consequence

**SA**
- S1 [core] Raindrops cover a window.
- S2 [core] The street outside appears as many tiny warped pictures within the drops.
- S3 [minor] The pictures move as the drops run down.
- S4 [minor] The view between the drops is normal.

**PC**
- P1 [core · shape_identity]
  - expect: Each drop shows a small distorted picture of the scene, and the view between drops is normal.
  - fail: The drops are blank; or the view between them is warped; or a drop shows a different scene.
- P2 [core · missing_consequence]
  - expect: The pictures move as the drops run down.
  - fail: The pictures stay put while drops run; or drops run with the pictures fixed; or pictures move with the drops still.
- P3 [major · gravity_direction]
  - expect: The drops run downward.
  - fail: They run up; or sideways on a vertical pane; or hang without moving.
- P4 [major · material_response]
  - expect: The drops are liquid beads that merge and run.
  - fail: They are rigid; or bounce; or freeze.
- P5 [fatal · permanence_count]
  - expect: One window and the street outside.
  - fail: A second window appears; or the street vanishes; or a drop becomes solid.
- P6 [minor · attribute_drift]
  - expect: The frame and the street stay the same.
  - fail: The frame changes; or the street rearranges; or the drops change colour.

## OPT-0119 · refraction_transparency · train

**Caption.** A snorkel mask is lowered under the water, and the blurred rocks below come into sharp view through the mask.

**Expectation (hidden).** The rocks are clear through the mask and look nearer and larger than they are; the view blurs again when the mask is lifted out.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A snorkel mask is lowered under the water.
- S2 [core] Blurred rocks below come into sharp view through the mask.
- S3 [minor] The rocks look nearer and larger through the mask.
- S4 [minor] The view blurs again when the mask is lifted out.

**PC**
- P1 [core · missing_consequence]
  - expect: The rocks are clear through the mask and blurred outside it.
  - fail: They are blurred through the mask; or sharp outside it; or the mask shows a different scene.
- P2 [core · shape_identity]
  - expect: The rocks are unchanged; they look nearer and larger through the mask.
  - fail: They look smaller; or they move; or a different bottom appears.
- P3 [major · causeless_motion]
  - expect: The mask moves only with the hand.
  - fail: It floats away; or dives by itself; or jumps.
- P4 [major · material_response]
  - expect: The mask's glass is rigid and the water liquid.
  - fail: The glass bends; or the water is rigid; or the mask fills and stays clear.
- P5 [fatal · permanence_count]
  - expect: One mask and the rocks.
  - fail: The mask duplicates; or the rocks vanish; or the hand passes through the mask.
- P6 [minor · attribute_drift]
  - expect: The mask and the water's colour stay the same.
  - fail: The mask changes colour; or the water changes; or the rocks change colour.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0120 · refraction_transparency · train

**Caption.** A clear glass jar of water is held in front of a printed face on a poster, and the eyes seen through the jar look stretched wide.

**Expectation (hidden).** The stretching appears only in the part of the face seen through the water and changes as the jar moves; the face beside the jar is normal.

**Declared violation types.** shape_identity, missing_consequence

**SA**
- S1 [core] A printed face is on a poster.
- S2 [core] A clear glass jar of water is held in front of it.
- S3 [core] The eyes seen through the jar look stretched wide.
- S4 [minor] The face beside the jar is normal.
- S5 [minor] The stretch changes as the jar moves.

**PC**
- P1 [core · missing_consequence]
  - expect: The stretching appears only in the part of the face seen through the water and changes as the jar moves.
  - fail: The face is stretched beside the jar; or unchanged through it; or the stretch stays fixed as the jar moves.
- P2 [core · shape_identity]
  - expect: The poster is unchanged; the stretch is an appearance.
  - fail: The poster bends; or the printed face changes; or a different face appears.
- P3 [major · material_response]
  - expect: The jar is rigid and the water level.
  - fail: The jar warps; or the water tilts and holds; or goes opaque.
- P4 [major · causeless_motion]
  - expect: The jar moves only with the hand.
  - fail: It floats; or slides; or jumps.
- P5 [fatal · permanence_count]
  - expect: One jar and one poster.
  - fail: The jar duplicates; or the poster vanishes; or the jar passes through the poster.
- P6 [minor · attribute_drift]
  - expect: The poster's colours and the jar stay the same.
  - fail: The poster changes colour; or the jar changes shape; or the wall changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0121 · refraction_transparency · train

**Caption.** A garden is seen through a pane of old wavy glass, and the plants seem to bend and shift as the camera moves.

**Expectation (hidden).** The distortion changes with the viewpoint while the plants stay still; through a flat pane beside it the view is undistorted.

**Declared violation types.** shape_identity, causeless_motion

**SA**
- S1 [core] A garden is seen through a pane of old wavy glass.
- S2 [core] The camera moves.
- S3 [core] The plants seem to bend and shift.
- S4 [minor] Through a flat pane beside it the view is undistorted.

**PC**
- P1 [core · shape_identity]
  - expect: The plants stay still; the distortion changes with the viewpoint.
  - fail: The plants sway with no wind; or they change shape; or a different garden appears.
- P2 [core · causeless_motion]
  - expect: The distortion changes only as the camera moves.
  - fail: The view wobbles with the camera still; or it stays fixed as the camera moves; or the glass ripples.
- P3 [major · missing_consequence]
  - expect: Through a flat pane beside it the view is undistorted.
  - fail: The flat pane distorts too; or the wavy pane is undistorted; or both are opaque.
- P4 [major · material_response]
  - expect: The glass is rigid.
  - fail: It flows; or bends; or shatters untouched.
- P5 [fatal · permanence_count]
  - expect: One window and one garden.
  - fail: A second window appears; or a plant vanishes; or the glass becomes solid opaque.
- P6 [minor · attribute_drift]
  - expect: The frame and the garden's colours stay the same.
  - fail: The frame changes; or the plants change colour; or the room changes.

## OPT-0122 · refraction_transparency · train

**Caption.** A clear glass marble is held up in front of a lamp, and the room appears tiny and warped inside the marble.

**Expectation (hidden).** The small distorted image is inside the marble and moves as the marble moves; the room around the marble is normal.

**Declared violation types.** shape_identity, missing_consequence

**SA**
- S1 [core] A clear glass marble is held up in front of a lamp.
- S2 [core] The room appears tiny and warped inside the marble.
- S3 [minor] The image moves as the marble moves.
- S4 [minor] The room around the marble is normal.

**PC**
- P1 [core · shape_identity]
  - expect: The small distorted image is inside the marble and the room around it is normal.
  - fail: The image is outside the marble; or the room around it is warped; or the marble is opaque.
- P2 [core · missing_consequence]
  - expect: The image moves as the marble moves.
  - fail: It stays fixed while the marble moves; or it moves with the marble still; or it shows a different room.
- P3 [major · causeless_motion]
  - expect: The marble moves only with the hand.
  - fail: It floats; or rolls by itself; or jumps.
- P4 [major · material_response]
  - expect: The marble is rigid glass.
  - fail: It bends; or melts; or ripples.
- P5 [fatal · permanence_count]
  - expect: One marble and one lamp.
  - fail: The marble duplicates; or the lamp vanishes; or the hand passes through the marble.
- P6 [minor · attribute_drift]
  - expect: The lamp and the room stay the same.
  - fail: The lamp changes; or the room rearranges; or the marble changes colour.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0123 · refraction_transparency · train

**Caption.** Tongs reach into a bakery's glass counter from the open back and lift out a pastry that was visible through the glass.

**Expectation (hidden).** The pastry is clearly visible through the glass, the tongs enter from behind rather than through the pane, and the pastry lifted is the one that was seen.

**Declared violation types.** missing_consequence, solidity

**SA**
- S1 [core] A pastry is visible through a bakery's glass counter.
- S2 [core] Tongs reach in from the open back.
- S3 [core] They lift out the pastry.
- S4 [minor] The pastry lifted is the one that was seen.
- S5 [minor] The tongs enter from behind, not through the pane.

**PC**
- P1 [core · missing_consequence]
  - expect: The pastry is clearly visible through the glass and the tongs lift the one that was seen.
  - fail: The glass hides the pastry; or a different pastry is lifted; or the pastry changes as it is lifted.
- P2 [core · solidity]
  - expect: The tongs enter from behind rather than through the pane.
  - fail: The tongs pass through the glass; or the pastry passes through the glass; or the glass passes through the tongs.
- P3 [major · causeless_motion]
  - expect: The pastry moves only in the tongs.
  - fail: It rises by itself; or slides; or jumps.
- P4 [major · material_response]
  - expect: The tongs are rigid and the pastry firm.
  - fail: The tongs bend like rubber; or the pastry flows; or the glass ripples.
- P5 [fatal · permanence_count]
  - expect: The pastries keep their number apart from the one lifted.
  - fail: A pastry vanishes; or appears; or the lifted one duplicates.
- P6 [minor · attribute_drift]
  - expect: The counter and the pastries stay the same.
  - fail: The pastries change colour; or the counter changes; or the shop rearranges.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0124 · refraction_transparency · train

**Caption.** A field slides past a train window and is clearly visible through the glass.

**Expectation (hidden).** The view moves continuously past the window and stays visible; the glass does not turn opaque or freeze the scene.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A field slides past a train window.
- S2 [core] It is clearly visible through the glass.
- S3 [minor] The view moves continuously.

**PC**
- P1 [core · missing_consequence]
  - expect: The view moves continuously past the window and stays visible.
  - fail: The glass is opaque; or the view freezes; or it jumps.
- P2 [core · permanence_count]
  - expect: The scene does not vanish or turn into a different scene.
  - fail: The field vanishes; or a different landscape appears abruptly; or the view is a static picture.
- P3 [major · trajectory_momentum]
  - expect: The view slides one way at a steady pace.
  - fail: It reverses; or speeds up and stops jerkily; or the near and far ground move the wrong way relative to each other.
- P4 [major · material_response]
  - expect: The pane is flat and rigid.
  - fail: It ripples; or bends; or goes opaque.
- P5 [fatal · shape_identity]
  - expect: One window in one carriage.
  - fail: A second window appears; or the frame vanishes; or the field passes into the carriage.
- P6 [minor · attribute_drift]
  - expect: The carriage interior stays the same.
  - fail: The seats change; or the frame changes; or the field changes colour abruptly.

## OPT-0125 · refraction_transparency · train

**Caption.** A coin is dropped into a tall clear vase of water, and the coin appears to jump sideways as it passes through the surface.

**Expectation (hidden).** The apparent shift happens at the waterline; underneath, the coin sinks straight to the bottom and is visible through the glass.

**Declared violation types.** shape_identity, trajectory_momentum

**SA**
- S1 [core] A coin is dropped into a tall clear vase of water.
- S2 [core] The coin appears to jump sideways as it passes through the surface.
- S3 [core] It sinks to the bottom.
- S4 [minor] The coin is visible through the glass.
- S5 [minor] The apparent shift is at the waterline.

**PC**
- P1 [core · shape_identity]
  - expect: The apparent shift happens at the waterline; the coin itself falls straight.
  - fail: The shift is above or below the surface; or the coin actually swerves; or it changes shape.
- P2 [core · trajectory_momentum]
  - expect: Underneath, the coin sinks straight to the bottom.
  - fail: It floats; or hangs; or drifts sideways.
- P3 [major · missing_consequence]
  - expect: The coin is visible through the glass and water throughout.
  - fail: The water hides it; or it vanishes below the surface; or a different coin appears.
- P4 [major · material_response]
  - expect: The water surface splashes and settles level; the vase is rigid.
  - fail: The surface tilts and holds; or the vase bends; or the water goes opaque.
- P5 [fatal · permanence_count]
  - expect: One coin and one vase.
  - fail: The coin duplicates; or the vase vanishes; or the coin passes through the vase.
- P6 [minor · attribute_drift]
  - expect: The coin and the vase stay the same.
  - fail: The coin changes colour; or the vase changes shape; or the table changes.

## OPT-0126 · refraction_transparency · train

**Caption.** A glass paperweight is slid over a newspaper, and the letters under it look swollen and bent.

**Expectation (hidden).** The distortion is confined to the area under the glass and shifts as the paperweight is slid; the letters outside it are normal.

**Declared violation types.** shape_identity, missing_consequence

**SA**
- S1 [core] A glass paperweight is slid over a newspaper.
- S2 [core] The letters under it look swollen and bent.
- S3 [minor] The distortion shifts as the paperweight is slid.
- S4 [minor] The letters outside it are normal.

**PC**
- P1 [core · missing_consequence]
  - expect: The distortion is confined to the area under the glass and shifts as it is slid.
  - fail: Letters beside the glass are distorted; or letters under it are unchanged; or the distortion stays put as it slides.
- P2 [core · shape_identity]
  - expect: The newspaper is unchanged; the swelling is an appearance.
  - fail: The print changes; or letters move; or the paper bends.
- P3 [major · causeless_motion]
  - expect: The paperweight moves only with the hand and the paper stays put.
  - fail: It slides by itself; or the paper moves; or the image shifts with both still.
- P4 [major · material_response]
  - expect: The paperweight is rigid glass.
  - fail: It bends; or ripples; or goes opaque.
- P5 [fatal · permanence_count]
  - expect: One paperweight and one newspaper.
  - fail: It duplicates; or the paper vanishes; or it passes through the paper.
- P6 [minor · attribute_drift]
  - expect: The newspaper and the desk stay the same.
  - fail: The paper changes colour; or the desk changes; or the glass changes colour.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0127 · refraction_transparency · train

**Caption.** A bathroom window is fogged after a shower, and where a hairdryer blows on the glass the view of the yard outside sharpens.

**Expectation (hidden).** The view goes from blurred to clear where the warm air dries the glass; it does not blur again while the glass is dry.

**Declared violation types.** process_direction, shape_identity

**SA**
- S1 [core] A bathroom window is fogged after a shower.
- S2 [core] A hairdryer blows on the glass.
- S3 [core] The view of the yard outside sharpens where the air blows.
- S4 [minor] The view stays clear while the glass is dry.

**PC**
- P1 [core · process_direction]
  - expect: The view goes from blurred to clear where the warm air dries the glass and does not blur again while dry.
  - fail: It blurs again under the dryer; or it clears where no air blows; or it flickers.
- P2 [core · shape_identity]
  - expect: The yard outside is unchanged; only the fog changes.
  - fail: The yard changes; or a different scene appears; or the glass warps.
- P3 [major · missing_consequence]
  - expect: The clear patch is where the dryer is aimed.
  - fail: It is elsewhere; or the whole pane clears at once from one spot; or the patch appears before the dryer.
- P4 [major · material_response]
  - expect: The fog is a film of moisture that evaporates.
  - fail: It peels; or is a solid coating; or drips as ice.
- P5 [fatal · permanence_count]
  - expect: One window and one dryer.
  - fail: The window duplicates; or the dryer vanishes; or the dryer passes through the glass.
- P6 [minor · attribute_drift]
  - expect: The frame and the bathroom stay the same.
  - fail: The frame changes; or the room rearranges; or the dryer changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0128 · refraction_transparency · train

**Caption.** A loupe is held over a ring, and the ring's details appear greatly enlarged through it.

**Expectation (hidden).** The enlargement applies only to what is seen through the loupe; the rest of the ring and the desk look normal size.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A loupe is held over a ring.
- S2 [core] The ring's details appear greatly enlarged through it.
- S3 [minor] The rest of the ring and the desk look normal size.

**PC**
- P1 [core · missing_consequence]
  - expect: The enlargement applies only to what is seen through the loupe.
  - fail: The desk is enlarged; or the ring is unchanged through the loupe; or the enlarged view is offset from the loupe.
- P2 [core · shape_identity]
  - expect: The ring is unchanged; the enlarged details are its own.
  - fail: A different ring appears; or the ring changes; or the image is mirrored.
- P3 [major · causeless_motion]
  - expect: The loupe moves only with the hand and the ring stays put.
  - fail: The loupe floats; or the ring slides; or the image shifts with both still.
- P4 [major · material_response]
  - expect: The loupe's lens is rigid.
  - fail: It bends; or ripples; or goes opaque.
- P5 [fatal · permanence_count]
  - expect: One loupe and one ring.
  - fail: The loupe duplicates; or the ring vanishes; or the hand passes through the loupe.
- P6 [minor · attribute_drift]
  - expect: The ring and the desk stay the same.
  - fail: The ring changes colour; or the desk changes; or the loupe changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0129 · refraction_transparency · train

**Caption.** From under the clear sea, the underside of a boat shows as a wavering dark shape through the surface.

**Expectation (hidden).** The shape is visible but its edges ripple with the surface; it steadies as the water calms.

**Declared violation types.** shape_identity, missing_consequence

**SA**
- S1 [core] The view is from under the clear sea.
- S2 [core] The underside of a boat shows as a wavering dark shape through the surface.
- S3 [minor] The shape steadies as the water calms.

**PC**
- P1 [core · shape_identity]
  - expect: The shape is the boat's hull, dark against the sky, and steadies when the water is calm.
  - fail: It is a different object; or it is sharp on a plainly rippled surface; or it never steadies on calm water.
- P2 [core · missing_consequence]
  - expect: The shape is visible through the surface and its edges ripple with it.
  - fail: The surface is opaque; or the edges are rigid while the surface ripples; or the shape ripples on a flat calm.
- P3 [major · gravity_direction]
  - expect: The hull sits at the surface, not below the viewer.
  - fail: The hull is below; or it rises out of sight; or it sinks.
- P4 [major · material_response]
  - expect: The surface is liquid: ripples pass and fade.
  - fail: It is rigid; or ripples freeze; or the water leaps.
- P5 [fatal · permanence_count]
  - expect: One boat.
  - fail: A second hull appears; or the boat vanishes; or the water becomes solid.
- P6 [minor · attribute_drift]
  - expect: The water's colour and the hull stay the same.
  - fail: The water changes colour; or the hull changes; or the light changes abruptly.

## OPT-0130 · refraction_transparency · train

**Caption.** Vegetable pieces lie at the bottom of a pot of clear water, and they seem to shift and swim as the water is stirred.

**Expectation (hidden).** The pieces on the bottom stay put while the moving water makes their images wobble; they look still again when the stirring stops.

**Declared violation types.** shape_identity, causeless_motion

**SA**
- S1 [core] Vegetable pieces lie at the bottom of a pot of clear water.
- S2 [core] The water is stirred.
- S3 [core] The pieces seem to shift and swim.
- S4 [minor] They look still again when the stirring stops.

**PC**
- P1 [core · shape_identity]
  - expect: The pieces on the bottom stay put while the moving water makes their images wobble.
  - fail: The pieces actually slide about; or they change shape; or pieces appear and vanish.
- P2 [core · causeless_motion]
  - expect: The wobble follows the stirring and stops when the water settles.
  - fail: The images wobble with the water still; or they are sharp while the water is plainly moving; or the wobble goes on after the water settles.
- P3 [major · missing_consequence]
  - expect: The pieces are visible through the water.
  - fail: The water hides them; or a different set appears; or they are seen only above the surface.
- P4 [major · material_response]
  - expect: The water is liquid: it swirls and settles.
  - fail: It is rigid; or the swirl freezes; or the water leaps.
- P5 [fatal · permanence_count]
  - expect: The pieces keep their number.
  - fail: Pieces vanish; or appear; or merge.
- P6 [minor · attribute_drift]
  - expect: The pot and the pieces' colours stay the same.
  - fail: The pot changes; or the pieces change colour; or the stove changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0131 · refraction_transparency · train

**Caption.** A clear glass bottle of water is held sideways in front of a lit sign, and the letters seen through the bottle appear stretched.

**Expectation (hidden).** The stretching happens only where the sign is seen through the water-filled bottle and changes as the bottle turns; the sign itself is unchanged.

**Declared violation types.** shape_identity, missing_consequence

**SA**
- S1 [core] A clear glass bottle of water is held sideways in front of a lit sign.
- S2 [core] The letters seen through the bottle appear stretched.
- S3 [minor] The stretch changes as the bottle turns.
- S4 [minor] The sign itself is unchanged.

**PC**
- P1 [core · missing_consequence]
  - expect: The stretching happens only where the sign is seen through the water-filled bottle and changes as the bottle turns.
  - fail: Letters beside the bottle are stretched; or letters through it are unchanged; or the stretch stays fixed as the bottle turns.
- P2 [core · shape_identity]
  - expect: The sign itself is unchanged.
  - fail: The sign's letters change; or it moves; or a different sign appears.
- P3 [major · material_response]
  - expect: The bottle is rigid and the water level inside it.
  - fail: The bottle bends; or the water tilts and holds; or goes opaque.
- P4 [major · causeless_motion]
  - expect: The bottle moves only with the hand.
  - fail: It floats; or turns by itself; or jumps.
- P5 [fatal · permanence_count]
  - expect: One bottle and one sign.
  - fail: The bottle duplicates; or the sign vanishes; or the hand passes through the bottle.
- P6 [minor · attribute_drift]
  - expect: The sign's colours and the bottle stay the same.
  - fail: The sign changes colour; or the bottle changes shape; or the background changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0132 · refraction_transparency · train

**Caption.** A patch of a wet window is wiped dry with a cloth, and the view through the patch becomes sharp.

**Expectation (hidden).** The clear patch matches the wiped area and the view outside it stays blurred by the water; the outside scene does not change.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A window is wet.
- S2 [core] A patch is wiped dry with a cloth.
- S3 [core] The view through the patch becomes sharp.
- S4 [minor] The view outside the patch stays blurred.

**PC**
- P1 [core · missing_consequence]
  - expect: The clear patch matches the wiped area and the view outside it stays blurred by the water.
  - fail: The whole pane clears from one wipe; or the wiped patch stays blurred; or a clear patch appears where nothing was wiped.
- P2 [core · shape_identity]
  - expect: The outside scene does not change.
  - fail: The scene changes; or a different view appears in the patch; or the glass warps.
- P3 [major · material_response]
  - expect: The water is a film the cloth removes.
  - fail: It is a solid coating; or it reforms instantly; or the cloth passes through the glass.
- P4 [major · causeless_motion]
  - expect: The cloth moves only with the hand.
  - fail: It wipes by itself; or floats; or jumps.
- P5 [fatal · permanence_count]
  - expect: One window and one cloth.
  - fail: The window duplicates; or the cloth vanishes; or the cloth passes through the pane.
- P6 [minor · attribute_drift]
  - expect: The frame and the room stay the same.
  - fail: The frame changes; or the room rearranges; or the cloth changes colour.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0133 · refraction_transparency · train

**Caption.** A stone is dropped into a clear stream and sinks, its image wavering with the current until it rests on the bed.

**Expectation (hidden).** The stone is visible through the moving water and appears to waver while its actual path is a steady sink; it stays visible on the bottom.

**Declared violation types.** shape_identity, trajectory_momentum

**SA**
- S1 [core] A stone is dropped into a clear stream.
- S2 [core] It sinks.
- S3 [core] Its image wavers with the current.
- S4 [core] It rests on the bed.
- S5 [minor] The drop comes first, then the sink, then the rest.

**PC**
- P1 [core · shape_identity]
  - expect: The stone's actual path is a steady sink; only its image wavers.
  - fail: The stone swerves; or it changes shape; or it splits.
- P2 [core · trajectory_momentum]
  - expect: It sinks to the bed and stays there.
  - fail: It floats; or hangs; or drifts away downstream while sinking straight in a still pool.
- P3 [major · missing_consequence]
  - expect: The stone is visible through the moving water throughout.
  - fail: The water hides it; or it vanishes; or a different stone appears.
- P4 [major · material_response]
  - expect: The water is liquid and flows.
  - fail: It is rigid; or flows uphill; or freezes.
- P5 [fatal · permanence_count]
  - expect: One stone.
  - fail: It duplicates; or vanishes; or passes through the bed.
- P6 [minor · attribute_drift]
  - expect: The stream bed and the stone stay the same.
  - fail: The bed rearranges; or the stone changes colour; or the banks change.

## OPT-0134 · refraction_transparency · train

**Caption.** A clear glass beaker of water is placed in front of a ruled sheet, and the lines behind the beaker appear closer together and shifted.

**Expectation (hidden).** The change is confined to the view through the water and vanishes when the beaker is emptied or moved aside.

**Declared violation types.** shape_identity, missing_consequence

**SA**
- S1 [core] A ruled sheet is present.
- S2 [core] A clear glass beaker of water is placed in front of it.
- S3 [core] The lines behind the beaker appear closer together and shifted.
- S4 [minor] The change vanishes when the beaker is emptied or moved.

**PC**
- P1 [core · missing_consequence]
  - expect: The change is confined to the view through the water and vanishes when the beaker is moved aside.
  - fail: Lines beside the beaker change; or lines behind it are unchanged; or the change stays after the beaker is gone.
- P2 [core · shape_identity]
  - expect: The sheet is unchanged; the shift is an appearance.
  - fail: The lines on the sheet move; or the sheet bends; or a different pattern appears.
- P3 [major · material_response]
  - expect: The beaker is rigid and the water level.
  - fail: The beaker bends; or the water tilts and holds; or goes opaque.
- P4 [major · causeless_motion]
  - expect: The beaker and the sheet stay put unless moved.
  - fail: The beaker slides; or the sheet moves; or the image shifts with both still.
- P5 [fatal · permanence_count]
  - expect: One beaker and one sheet.
  - fail: The beaker duplicates; or the sheet vanishes; or the beaker passes through the sheet.
- P6 [minor · attribute_drift]
  - expect: The sheet and the beaker stay the same.
  - fail: The sheet changes colour; or the beaker changes shape; or the table changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0135 · refraction_transparency · train

**Caption.** A shop display is seen through a window streaked with rain, and the mannequins appear smeared where the water runs.

**Expectation (hidden).** The smearing follows the water tracks and moves downward with them; the mannequins are clear through dry parts of the glass.

**Declared violation types.** shape_identity, missing_consequence

**SA**
- S1 [core] A shop display is seen through a window.
- S2 [core] The window is streaked with rain.
- S3 [core] The mannequins appear smeared where the water runs.
- S4 [minor] The mannequins are clear through dry parts of the glass.

**PC**
- P1 [core · shape_identity]
  - expect: The smearing follows the water tracks and the mannequins are clear through dry glass.
  - fail: The whole pane is smeared; or the tracks leave the view sharp; or the smear is where no water runs.
- P2 [core · missing_consequence]
  - expect: The smear moves downward with the water.
  - fail: The tracks are still while the smear moves; or the smear moves up; or the water runs with the smear fixed.
- P3 [major · gravity_direction]
  - expect: The rain runs down the glass.
  - fail: It runs up; or hangs; or runs sideways on a vertical pane.
- P4 [major · causeless_motion]
  - expect: The mannequins stay still.
  - fail: They move; or turn; or a mannequin vanishes.
- P5 [fatal · permanence_count]
  - expect: The mannequins keep their number.
  - fail: One vanishes; or appears; or two merge.
- P6 [minor · attribute_drift]
  - expect: The display and the frame stay the same.
  - fail: The clothes change colour; or the frame changes; or the shop rearranges.

## OPT-0136 · refraction_transparency · train

**Caption.** A clear glass of water is held up in front of a doorway, and the doorway seen through it appears flipped left-to-right and squeezed thin.

**Expectation (hidden).** The flipped, narrowed image appears only through the water and shifts as the glass moves; the room seen around the glass is normal.

**Declared violation types.** shape_identity, missing_consequence

**SA**
- S1 [core] A clear glass of water is held up in front of a doorway.
- S2 [core] The doorway seen through it appears flipped left-to-right and squeezed thin.
- S3 [minor] The image shifts as the glass moves.
- S4 [minor] The room seen around the glass is normal.

**PC**
- P1 [core · shape_identity]
  - expect: The flipped, narrowed image appears only through the water and the room around the glass is normal.
  - fail: The room around the glass is flipped; or the doorway through the glass is unchanged; or the image is upside down.
- P2 [core · missing_consequence]
  - expect: The image shifts as the glass moves.
  - fail: It stays fixed while the glass moves; or it shifts with the glass still; or it shows a different room.
- P3 [major · material_response]
  - expect: The glass is rigid and the water level.
  - fail: The glass bends; or the water tilts and holds; or goes opaque.
- P4 [major · causeless_motion]
  - expect: The glass moves only with the hand.
  - fail: It floats; or slides; or jumps.
- P5 [fatal · permanence_count]
  - expect: One glass and one doorway.
  - fail: The glass duplicates; or the doorway vanishes; or the hand passes through the glass.
- P6 [minor · attribute_drift]
  - expect: The doorway and the room stay the same.
  - fail: The door changes colour; or the room rearranges; or the glass changes shape.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0137 · refraction_transparency · train

**Caption.** A straight stick is lowered into a clear pond, and the underwater part appears to angle away from the part above the surface.

**Expectation (hidden).** The apparent bend is at the surface and its size changes with the stick's angle; the stick is straight when lifted out.

**Declared violation types.** shape_identity, missing_consequence

**SA**
- S1 [core] A straight stick is lowered into a clear pond.
- S2 [core] The underwater part appears to angle away from the part above the surface.
- S3 [minor] The apparent bend is at the surface.
- S4 [minor] The stick is straight when lifted out.

**PC**
- P1 [core · missing_consequence]
  - expect: The apparent bend is at the surface and its size changes with the stick's angle.
  - fail: The bend is above or below the surface; or it stays the same at every angle; or the stick looks straight in the water.
- P2 [core · shape_identity]
  - expect: The stick is straight and rigid; the bend is an appearance that is absent out of the water.
  - fail: The stick is physically bent when out; or the bend stays at a fixed point on the stick as it is raised; or the stick flexes.
- P3 [major · material_response]
  - expect: The pond surface is level and the water clear.
  - fail: The surface tilts and holds; or the water goes opaque; or the water leaps.
- P4 [major · causeless_motion]
  - expect: The stick moves only with the hand.
  - fail: It floats up; or sinks away; or jumps.
- P5 [fatal · permanence_count]
  - expect: One stick.
  - fail: It duplicates; or vanishes below the surface; or passes through the bed.
- P6 [minor · attribute_drift]
  - expect: The stick and the pond stay the same.
  - fail: The stick changes colour underwater; or the pond changes; or the bank rearranges.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0138 · refraction_transparency · train

**Caption.** A car's side window is fogged from the inside, blurring the passing city; a patch is wiped clear.

**Expectation (hidden).** The view is blurred everywhere except where the patch is wiped, where it turns sharp; the city outside does not change.

**Declared violation types.** shape_identity, process_direction

**SA**
- S1 [core] A car's side window is fogged from the inside.
- S2 [core] The passing city is blurred through it.
- S3 [core] A patch is wiped clear.
- S4 [minor] The view is sharp through the patch and blurred elsewhere.

**PC**
- P1 [core · shape_identity]
  - expect: The view is blurred everywhere except where the patch is wiped, and there it is sharp.
  - fail: The whole window clears from one wipe; or the wiped patch stays blurred; or a clear patch appears where nothing was wiped.
- P2 [core · process_direction]
  - expect: The patch stays clear while wiped and does not fog again instantly.
  - fail: It fogs over the instant the hand leaves; or it clears further by itself; or it flickers.
- P3 [major · missing_consequence]
  - expect: The city outside does not change and slides past.
  - fail: The city changes; or freezes; or a different view appears in the patch.
- P4 [major · material_response]
  - expect: The fog is a film the hand smears.
  - fail: It is a solid coating; or it peels; or the hand passes through the glass.
- P5 [fatal · permanence_count]
  - expect: One window and one hand.
  - fail: The window duplicates; or a second hand appears; or the fog becomes solid.
- P6 [minor · attribute_drift]
  - expect: The car interior stays the same.
  - fail: The door panel changes; or the frame changes; or the seats change.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0139 · refraction_transparency · train

**Caption.** A glass of water is placed on a line drawn on a piece of paper, and the line under the glass appears broken from the line outside it.

**Expectation (hidden).** The apparent break is at the glass edges and the line returns to one straight line when the glass is lifted.

**Declared violation types.** shape_identity, missing_consequence

**SA**
- S1 [core] A line is drawn on a piece of paper.
- S2 [core] A glass of water is placed on it.
- S3 [core] The line under the glass appears broken from the line outside it.
- S4 [minor] The line returns to one straight line when the glass is lifted.

**PC**
- P1 [core · missing_consequence]
  - expect: The apparent break is at the glass edges and the line returns to one straight line when the glass is lifted.
  - fail: The break is away from the glass; or the line is unbroken under the glass; or the break stays after the glass is lifted.
- P2 [core · shape_identity]
  - expect: The paper and its line are unchanged; the break is an appearance.
  - fail: The drawn line moves; or the paper bends; or a second line appears.
- P3 [major · material_response]
  - expect: The glass is rigid and the water level.
  - fail: The glass bends; or the water tilts and holds; or goes opaque.
- P4 [major · causeless_motion]
  - expect: The glass and the paper stay put unless moved.
  - fail: The glass slides; or the paper moves; or the image shifts with both still.
- P5 [fatal · permanence_count]
  - expect: One glass and one sheet.
  - fail: The glass duplicates; or the paper vanishes; or the glass passes through the paper.
- P6 [minor · attribute_drift]
  - expect: The paper and the glass stay the same.
  - fail: The paper changes colour; or the glass changes shape; or the table changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0140 · refraction_transparency · train

**Caption.** A pair of binoculars is held up to the camera toward a distant bird, and the bird appears large and close through the lenses.

**Expectation (hidden).** The enlarged view appears only through the eyepieces and follows where the binoculars point; the bird seen beside them is small.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A pair of binoculars is held up to the camera toward a distant bird.
- S2 [core] The bird appears large and close through the lenses.
- S3 [minor] The bird seen beside the binoculars is small.
- S4 [minor] The enlarged view follows where the binoculars point.

**PC**
- P1 [core · missing_consequence]
  - expect: The enlarged view appears only through the eyepieces and follows where the binoculars point.
  - fail: The bird is large beside the binoculars; or small through them; or the enlarged view stays fixed as they turn.
- P2 [core · shape_identity]
  - expect: The bird is the same bird, enlarged.
  - fail: A different bird appears; or the bird changes; or the image is mirrored.
- P3 [major · causeless_motion]
  - expect: The binoculars move only with the hands.
  - fail: They float; or turn by themselves; or jump.
- P4 [major · material_response]
  - expect: The binoculars are rigid.
  - fail: They bend; or the lenses ripple; or go opaque.
- P5 [fatal · permanence_count]
  - expect: One pair of binoculars and one bird.
  - fail: They duplicate; or the bird vanishes; or the hands pass through them.
- P6 [minor · attribute_drift]
  - expect: The binoculars and the scenery stay the same.
  - fail: They change colour; or the scenery rearranges; or the bird changes colour.

**Note.** The hand is the minimal trigger; the person is not judged. The bird is self-driven.

## OPT-0141 · refraction_transparency · train

**Caption.** A clear lid is lifted from a pot, and the food that was visible through the lid is seen the same underneath.

**Expectation (hidden).** The food seen through the lid matches what is there when the lid comes off; the lid did not hide or change it.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A clear lid is on a pot.
- S2 [core] Food is visible through the lid.
- S3 [core] The lid is lifted.
- S4 [core] The same food is seen underneath.
- S5 [minor] The lift comes first and the food is seen after.

**PC**
- P1 [core · missing_consequence]
  - expect: The food seen through the lid matches what is there when the lid comes off.
  - fail: The lid hides the food; or different food is underneath; or the food changes as the lid lifts.
- P2 [core · permanence_count]
  - expect: The lid did not hide or change the food.
  - fail: Food vanishes when the lid lifts; or appears; or doubles.
- P3 [major · causeless_motion]
  - expect: The lid moves only with the hand and the pot stays put.
  - fail: The lid floats off; or the pot slides; or the food moves.
- P4 [major · material_response]
  - expect: The lid is rigid and clear, possibly steamed.
  - fail: It bends; or ripples; or goes solid opaque.
- P5 [fatal · permanence_count]
  - expect: One lid and one pot.
  - fail: The lid duplicates; or the pot vanishes; or the lid passes through the pot.
- P6 [minor · attribute_drift]
  - expect: The pot and the stove stay the same.
  - fail: The pot changes colour; or the stove changes; or the food changes colour abruptly.

**Note.** The hand is the minimal trigger; the person is not judged.

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

## OPT-0144 · illumination · train

**Caption.** A flashlight is switched on under a blanket, and the blanket glows from inside where the light is.

**Expectation (hidden).** The glow is brightest where the flashlight is nearest the cloth and moves if the light moves; it stops when the light is switched off.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A flashlight is under a blanket.
- S2 [core] It is switched on.
- S3 [core] The blanket glows from inside where the light is.
- S4 [minor] The glow is brightest where the flashlight is nearest the cloth.
- S5 [minor] The switch comes first and the glow follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The glow is brightest where the flashlight is nearest the cloth and moves if the light moves.
  - fail: The glow is far from the flashlight; or the whole blanket glows evenly; or the glow stays put while the light moves.
- P2 [core · causeless_motion]
  - expect: The glow appears with the switch and stops when the light is switched off.
  - fail: The blanket glows with the light off; or the glow lingers after switching off; or it appears before the switch.
- P3 [major · shape_identity]
  - expect: The glow is one soft patch through the cloth.
  - fail: It is a sharp-edged spot as if on a wall; or it splits into several; or it is a geometric shape.
- P4 [major · material_response]
  - expect: The blanket is cloth that drapes over the flashlight.
  - fail: It is rigid; or transparent; or floats.
- P5 [fatal · permanence_count]
  - expect: One flashlight and one blanket.
  - fail: A second glow appears with one flashlight; or the blanket vanishes; or the flashlight passes through the cloth.
- P6 [minor · attribute_drift]
  - expect: The blanket's colour and the room stay the same.
  - fail: The blanket changes colour; or the room rearranges; or the glow changes colour.

**Note.** Illumination: the on/off causality of electric lights belongs to Electricity; here only where the light goes once it exists is judged.

## OPT-0145 · illumination · train

**Caption.** A lighthouse beam sweeps around in the night, lighting up the sea and cliffs in turn as it passes.

**Expectation (hidden).** Each part of the scene brightens only as the beam crosses it and darkens again after; the beam rotates steadily.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A lighthouse beam sweeps around in the night.
- S2 [core] It lights up the sea and cliffs in turn as it passes.
- S3 [minor] The beam rotates steadily.

**PC**
- P1 [core · missing_consequence]
  - expect: Each part of the scene brightens only as the beam crosses it and darkens again after.
  - fail: A patch stays lit after the beam has passed; or brightens before the beam arrives; or the whole scene is lit at once.
- P2 [core · causeless_motion]
  - expect: The beam rotates steadily and the lit patch moves with it.
  - fail: The beam stops and starts; or reverses; or the lit patch moves while the beam is still.
- P3 [major · shape_identity]
  - expect: The beam is one straight cone from the lamp.
  - fail: It bends; or splits into several; or it is a flood in all directions.
- P4 [major · trajectory_momentum]
  - expect: The lit patch sweeps one way round.
  - fail: It jumps; or sweeps the opposite way to the beam; or moves crosswise.
- P5 [fatal · permanence_count]
  - expect: One lighthouse and one beam.
  - fail: A second beam appears; or the lighthouse vanishes; or the beam becomes solid.
- P6 [minor · attribute_drift]
  - expect: The cliffs and the sea stay the same.
  - fail: The cliffs change shape; or the sea changes; or the beam changes colour.

**Note.** Illumination: the on/off causality of electric lights belongs to Electricity; here only where the light goes once it exists is judged.

## OPT-0146 · illumination · train

**Caption.** A spotlight follows a remote-controlled car across a dark stage, and the circle of light moves with it.

**Expectation (hidden).** The lit circle stays centred on the car and the rest of the stage stays dark; the car's shadow falls on the floor away from the spotlight.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A remote-controlled car crosses a dark stage.
- S2 [core] A spotlight follows it.
- S3 [core] The circle of light moves with the car.
- S4 [minor] The rest of the stage stays dark.

**PC**
- P1 [core · missing_consequence]
  - expect: The lit circle stays centred on the car and the rest of the stage stays dark.
  - fail: The circle lags or leads the car; or the whole stage is lit; or the circle is elsewhere.
- P2 [core · causeless_motion]
  - expect: The circle moves only as the car and spotlight move.
  - fail: It moves with the car stopped; or it jumps; or it stays put while the car drives.
- P3 [major · missing_consequence]
  - expect: The car's shadow falls on the floor away from the spotlight.
  - fail: The shadow points toward the spotlight; or there is no shadow in the beam; or shadows fall in several directions under one light.
- P4 [major · shape_identity]
  - expect: The circle is one round patch with a soft edge.
  - fail: It splits; or is a sharp square; or it floods the stage.
- P5 [fatal · permanence_count]
  - expect: One car and one circle of light.
  - fail: A second car appears; or two circles under one spotlight; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The car and the stage stay the same.
  - fail: The car changes colour; or the stage changes; or the light changes colour.

**Note.** Illumination: the on/off causality of electric lights belongs to Electricity; here only where the light goes once it exists is judged.

## OPT-0147 · illumination · train

**Caption.** A refrigerator door is opened in a dark kitchen, and light from inside the fridge spills out across the floor.

**Expectation (hidden).** The light appears as the door opens, widens with the door, and lights the floor in front of it; it disappears when the door closes.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A refrigerator stands in a dark kitchen.
- S2 [core] Its door is opened.
- S3 [core] Light from inside spills out across the floor.
- S4 [minor] The light widens as the door opens.

**PC**
- P1 [core · missing_consequence]
  - expect: The light appears as the door opens, widens with the door, and lights the floor in front of it.
  - fail: Light spills with the door shut; or the floor stays dark with the door open; or the light is behind the fridge.
- P2 [core · process_direction]
  - expect: The lit area grows as the door swings wider and would shrink as it closes.
  - fail: It shrinks as the door opens; or is full width before the door moves; or flickers.
- P3 [major · causeless_motion]
  - expect: The lit area moves only with the door.
  - fail: It drifts with the door still; or appears before the door moves.
- P4 [major · shape_identity]
  - expect: The lit area is a wedge on the floor spreading from the door.
  - fail: It is a round spot; or it is on the ceiling only; or it splits.
- P5 [fatal · permanence_count]
  - expect: One fridge and one door.
  - fail: A second door appears; or the fridge vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The kitchen and the fridge stay the same.
  - fail: The fridge changes colour; or the kitchen rearranges; or the light changes colour.

**Note.** Illumination: the on/off causality of electric lights belongs to Electricity; here only where the light goes once it exists is judged.

## OPT-0148 · illumination · train

**Caption.** A phone lying face-up on a table in a dark room lights up, and its glow lights the objects around it from below.

**Expectation (hidden).** The objects are lit on the sides facing the screen and the glow changes when the screen's picture changes; it goes dark when the screen turns off.

**Declared violation types.** missing_consequence, attribute_drift

**SA**
- S1 [core] A phone lies face-up on a table in a dark room.
- S2 [core] It lights up.
- S3 [core] Its glow lights the objects around it from below.
- S4 [minor] The objects are lit on the sides facing the screen.

**PC**
- P1 [core · missing_consequence]
  - expect: The objects are lit on the sides facing the screen and the glow changes when the screen's picture changes.
  - fail: They are lit from above; or the glow is unchanged when the picture changes; or the far side of the room is lit.
- P2 [core · attribute_drift]
  - expect: The glow takes the screen's colour.
  - fail: It is a different colour from the screen; or it is white with a coloured screen; or it changes colour with the screen steady.
- P3 [major · causeless_motion]
  - expect: The glow stops when the screen turns off.
  - fail: The objects stay lit with the screen dark; or lit before it lights; or the glow moves with the phone still.
- P4 [major · shape_identity]
  - expect: The glow is a soft spread from the screen.
  - fail: It is a sharp beam; or it splits; or it is a geometric shape.
- P5 [fatal · permanence_count]
  - expect: One phone and the objects around it.
  - fail: A second phone appears; or an object vanishes; or the glow becomes solid.
- P6 [minor · attribute_drift]
  - expect: The objects and the table stay the same.
  - fail: An object changes colour rather than brightness; or moves; or the table changes.

**Note.** Illumination: the on/off causality of electric lights belongs to Electricity; here only where the light goes once it exists is judged.

## OPT-0149 · illumination · train

**Caption.** A desk lamp is moved closer to an open book, and the page becomes brighter.

**Expectation (hidden).** The page brightens as the lamp approaches and dims when it is moved back; the lamp's shadow of the book's edge shifts accordingly.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A desk lamp lights an open book.
- S2 [core] The lamp is moved closer to the book.
- S3 [core] The page becomes brighter.
- S4 [minor] The lamp moves first and the page brightens with it.

**PC**
- P1 [core · missing_consequence]
  - expect: The page brightens as the lamp approaches and would dim as it moved back.
  - fail: The page stays the same brightness; or dims as the lamp nears; or brightens with the lamp still.
- P2 [core · causeless_motion]
  - expect: The brightness changes only as the lamp moves.
  - fail: It flickers with the lamp still; or changes before the lamp moves.
- P3 [major · missing_consequence]
  - expect: The shadow of the book's edge shifts as the lamp moves.
  - fail: The shadow stays fixed; or points toward the lamp; or there is no shadow.
- P4 [major · shape_identity]
  - expect: The lit area is a soft pool over the book.
  - fail: It is a sharp spot; or splits; or floods the room.
- P5 [fatal · permanence_count]
  - expect: One lamp and one book.
  - fail: A second lamp appears; or the book vanishes; or the lamp passes through the book.
- P6 [minor · attribute_drift]
  - expect: The book and the desk stay the same.
  - fail: The page changes colour rather than brightness; or the desk changes; or the lamp changes colour.

**Note.** Illumination: the on/off causality of electric lights belongs to Electricity; here only where the light goes once it exists is judged.

## OPT-0150 · illumination · train

**Caption.** A dimmer knob is turned slowly, and the ceiling lights fade from bright to a dim glow.

**Expectation (hidden).** The brightness follows the knob smoothly, down when turned down and up when turned up; it does not jump or change on its own.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A dimmer knob is turned slowly.
- S2 [core] The ceiling lights fade from bright to a dim glow.
- S3 [minor] The brightness follows the knob smoothly.

**PC**
- P1 [core · missing_consequence]
  - expect: The brightness follows the knob, down when turned down.
  - fail: The lights stay bright; or brighten as the knob is turned down; or change with the knob still.
- P2 [core · process_direction]
  - expect: The fade is smooth and does not jump or reverse on its own.
  - fail: It jumps; or flickers; or brightens again with the knob steady.
- P3 [major · causeless_motion]
  - expect: Nothing else in the room changes brightness.
  - fail: A lamp elsewhere changes; or daylight changes; or the lit area moves.
- P4 [major · attribute_drift]
  - expect: The light dims without changing colour.
  - fail: It turns a different colour; or changes to another kind of light; or the walls change colour.
- P5 [fatal · permanence_count]
  - expect: The lights keep their number.
  - fail: A light vanishes; or appears; or the knob duplicates.
- P6 [minor · attribute_drift]
  - expect: The room stays the same.
  - fail: The furniture rearranges; or the ceiling changes; or the knob changes.

**Note.** The hand is the minimal trigger; the person is not judged. Illumination: the on/off causality of electric lights belongs to Electricity; here only where the light goes once it exists is judged.

## OPT-0151 · illumination · train

**Caption.** A cloud slides across the sun over a picnic table, and the whole scene dims.

**Expectation (hidden).** The dimming is gradual and affects everything at once; sharp shadows soften as the cloud moves in front of the sun.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A picnic table is in sunlight.
- S2 [core] A cloud slides across the sun.
- S3 [core] The whole scene dims.
- S4 [minor] Sharp shadows soften as the cloud moves in.

**PC**
- P1 [core · missing_consequence]
  - expect: The dimming affects everything at once and the sharp shadows soften.
  - fail: Only part of the scene dims; or the shadows stay sharp; or the scene brightens.
- P2 [core · process_direction]
  - expect: The dimming is gradual and follows the cloud.
  - fail: It is instant; or it flickers; or it brightens while the cloud still covers the sun.
- P3 [major · causeless_motion]
  - expect: The cloud moves steadily and nothing on the table moves.
  - fail: The cloud jumps; or objects on the table move; or the shadows swing round.
- P4 [major · attribute_drift]
  - expect: Colours stay the same, only dimmer.
  - fail: Objects change colour; or the grass changes colour; or the sky changes abruptly.
- P5 [fatal · permanence_count]
  - expect: One table and its objects.
  - fail: An object vanishes; or appears; or the table duplicates.
- P6 [minor · attribute_drift]
  - expect: The table setting stays the same.
  - fail: Items rearrange; or the table changes; or the surroundings change.

## OPT-0152 · illumination · train

**Caption.** Heavy curtains in a dim bedroom are pulled open, and daylight floods in and brightens the room.

**Expectation (hidden).** The light enters through the widening gap and the room brightens as the curtains open; the brightest part is nearest the window.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] Heavy curtains hang in a dim bedroom.
- S2 [core] They are pulled open.
- S3 [core] Daylight floods in and brightens the room.
- S4 [minor] The brightest part is nearest the window.

**PC**
- P1 [core · missing_consequence]
  - expect: The light enters through the widening gap and the room brightens as the curtains open, brightest nearest the window.
  - fail: The room is bright with the curtains shut; or stays dim with them open; or the far wall is brightest.
- P2 [core · causeless_motion]
  - expect: The brightening follows the curtains.
  - fail: The room brightens before the curtains move; or with them still; or it dims as they open.
- P3 [major · process_direction]
  - expect: The lit area grows as the gap widens.
  - fail: It shrinks; or is full before the curtains move; or flickers.
- P4 [major · material_response]
  - expect: The curtains are cloth that gathers as it is drawn.
  - fail: They are rigid; or float; or pass through the rail.
- P5 [fatal · permanence_count]
  - expect: One window and its curtains.
  - fail: A second window appears; or a curtain vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The room stays the same.
  - fail: Furniture rearranges; or the walls change colour; or the curtains change colour.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0153 · illumination · train

**Caption.** A match is struck in a dark cave, and the flame lights the rock walls around it for a moment.

**Expectation (hidden).** The nearby walls brighten with a warm flicker and the light fades as the match burns down; the far reaches stay dark.

**Declared violation types.** missing_consequence, attribute_drift

**SA**
- S1 [core] A match is struck in a dark cave.
- S2 [core] The flame lights the rock walls around it for a moment.
- S3 [minor] The far reaches stay dark.

**PC**
- P1 [core · missing_consequence]
  - expect: The nearby walls brighten with a warm flicker and the far reaches stay dark.
  - fail: The far walls are as bright as the near; or the near walls stay dark; or the light comes from elsewhere.
- P2 [core · attribute_drift]
  - expect: The light is warm and flickers with the flame.
  - fail: It is a steady white; or a different colour; or the walls change colour rather than brightness.
- P3 [major · process_direction]
  - expect: The light fades as the match burns down.
  - fail: It brightens as the match burns; or stays constant; or goes out and returns.
- P4 [major · gravity_direction]
  - expect: The flame points upward.
  - fail: It points down or sideways in still air; or detaches; or floats.
- P5 [fatal · permanence_count]
  - expect: One match and one flame.
  - fail: A second flame appears; or the match vanishes; or the flame becomes solid.
- P6 [minor · attribute_drift]
  - expect: The rock and the cave stay the same.
  - fail: The rock changes shape; or the cave rearranges; or the match changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0154 · illumination · train

**Caption.** A lantern is carried through a dark campsite, and the pool of light moves along the ground with it.

**Expectation (hidden).** The lit area travels with the lantern and the tents brighten as it passes and darken behind it.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A lantern is carried through a dark campsite.
- S2 [core] The pool of light moves along the ground with it.
- S3 [minor] The tents brighten as it passes and darken behind it.

**PC**
- P1 [core · missing_consequence]
  - expect: The lit area travels with the lantern and the tents brighten as it passes and darken behind.
  - fail: The lit area stays put while the lantern moves; or tents stay lit after it has passed; or light appears ahead of it.
- P2 [core · causeless_motion]
  - expect: The light moves only with the lantern.
  - fail: It drifts with the lantern still; or moves the opposite way; or jumps.
- P3 [major · shape_identity]
  - expect: The pool is one soft patch around the lantern.
  - fail: It is a sharp beam; or splits; or floods the whole site.
- P4 [major · missing_consequence]
  - expect: Shadows point away from the lantern.
  - fail: They point toward it; or in several directions; or there are none.
- P5 [fatal · permanence_count]
  - expect: One lantern and one pool of light.
  - fail: A second pool appears with one lantern; or the lantern vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The tents and the ground stay the same.
  - fail: A tent changes colour rather than brightness; or moves; or the ground changes.

**Note.** The hand is the minimal trigger; the person is not judged. Illumination: the on/off causality of electric lights belongs to Electricity; here only where the light goes once it exists is judged.

## OPT-0155 · illumination · train

**Caption.** A headlamp is turned from side to side in a dark cave, and the beam sweeps across the cave walls with each turn.

**Expectation (hidden).** The lit patch moves exactly with the lamp and the wall it turns away from goes dark; the light is brightest where the beam is centred.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A headlamp is worn in a dark cave.
- S2 [core] It is turned from side to side.
- S3 [core] The beam sweeps across the cave walls with each turn.
- S4 [minor] The wall the lamp turns away from goes dark.

**PC**
- P1 [core · missing_consequence]
  - expect: The lit patch moves exactly with the lamp and the wall it turns away from goes dark.
  - fail: The patch stays put while the lamp turns; or the wall stays lit after the beam leaves; or the patch moves opposite.
- P2 [core · causeless_motion]
  - expect: The patch moves only as the lamp turns.
  - fail: It drifts with the lamp still; or moves before the turn; or flickers.
- P3 [major · shape_identity]
  - expect: The patch is one bright spot, brightest at its centre.
  - fail: It splits; or is a sharp square; or it is even edge to edge.
- P4 [major · missing_consequence]
  - expect: Shadows on the wall point away from the lamp.
  - fail: They point toward it; or in several directions; or there are none on rough rock.
- P5 [fatal · permanence_count]
  - expect: One lamp and one patch.
  - fail: A second patch appears; or the lamp vanishes; or the beam becomes solid.
- P6 [minor · attribute_drift]
  - expect: The cave walls stay the same.
  - fail: The rock changes shape; or changes colour rather than brightness; or the cave rearranges.

**Note.** The head turning is the trigger; the person is not judged. Illumination: the on/off causality of electric lights belongs to Electricity; here only where the light goes once it exists is judged.

## OPT-0156 · illumination · train

**Caption.** A laser pointer's red dot moves across a projected slide as the pointer is moved.

**Expectation (hidden).** The dot appears only while the button is pressed, moves with the pointer, and disappears when it is released; it does not linger.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A laser pointer's red dot is on a projected slide.
- S2 [core] The pointer is moved.
- S3 [core] The dot moves across the slide.
- S4 [minor] The dot appears only while the button is pressed and disappears when released.

**PC**
- P1 [core · missing_consequence]
  - expect: The dot moves with the pointer and appears only while the button is pressed.
  - fail: The dot stays put while the pointer moves; or it remains after release; or it appears with no pointer.
- P2 [core · causeless_motion]
  - expect: The dot does not move on its own or linger.
  - fail: It drifts with the pointer still; or leaves a trail; or jumps.
- P3 [major · shape_identity]
  - expect: The dot is one small red spot.
  - fail: It splits; or is a large patch; or changes shape.
- P4 [major · attribute_drift]
  - expect: The dot is red on every part of the slide.
  - fail: It changes colour; or is white; or the slide changes with no click.
- P5 [fatal · permanence_count]
  - expect: One pointer and one dot.
  - fail: A second dot appears; or the pointer vanishes; or the dot becomes solid.
- P6 [minor · attribute_drift]
  - expect: The slide and the screen stay the same.
  - fail: The slide changes with no click; or the screen changes; or the room changes.

**Note.** The hand is the minimal trigger; the person is not judged. Illumination: the on/off causality of electric lights belongs to Electricity; here only where the light goes once it exists is judged.

## OPT-0157 · illumination · train

**Caption.** A camera flash fires in a dim hall, and the whole room is lit for an instant.

**Expectation (hidden).** The flash is a single brief burst that lights everything facing the camera and is gone; the room returns to dim immediately.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A dim hall is present.
- S2 [core] A camera flash fires.
- S3 [core] The whole room is lit for an instant.
- S4 [minor] The room returns to dim immediately.

**PC**
- P1 [core · process_direction]
  - expect: The flash is a single brief burst and the room returns to dim immediately.
  - fail: The room stays lit; or brightens gradually; or flashes repeatedly with one press.
- P2 [core · missing_consequence]
  - expect: Everything facing the camera is lit and shadows point away from it.
  - fail: Only part of the room lights; or shadows point toward the camera; or the far side is lit and the near dark.
- P3 [major · causeless_motion]
  - expect: Nothing else changes brightness.
  - fail: Another light comes on; or the room dims before the flash; or the lit area moves.
- P4 [major · attribute_drift]
  - expect: Colours stay the same, only brighter for the instant.
  - fail: Objects change colour; or the flash is coloured; or the walls change.
- P5 [fatal · permanence_count]
  - expect: The room's objects keep their number.
  - fail: An object vanishes; or appears; or the camera duplicates.
- P6 [minor · attribute_drift]
  - expect: The hall stays the same.
  - fail: Furniture rearranges; or the walls change; or the camera changes.

## OPT-0158 · illumination · train

**Caption.** A car enters a tunnel on a sunny day, and the inside of the car dims until the overhead tunnel lights take over.

**Expectation (hidden).** The light in the car drops as the tunnel entrance passes overhead and takes on the tunnel lamps' colour; it brightens again at the exit.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A car enters a tunnel on a sunny day.
- S2 [core] The inside of the car dims.
- S3 [core] The overhead tunnel lights take over.
- S4 [minor] The light takes on the tunnel lamps' colour.

**PC**
- P1 [core · missing_consequence]
  - expect: The light in the car drops as the entrance passes overhead and takes on the tunnel lamps' colour.
  - fail: The car stays sunlit in the tunnel; or dims before the entrance; or the light stays white under coloured lamps.
- P2 [core · process_direction]
  - expect: The dimming happens at the entrance and holds inside.
  - fail: The car brightens inside; or flickers with steady lamps; or dims and brightens randomly.
- P3 [major · causeless_motion]
  - expect: The car drives steadily and the lamps pass overhead in turn.
  - fail: The car jumps position; or the lamps move; or the car stops with no cause.
- P4 [major · attribute_drift]
  - expect: Only the light changes; the interior's colours are the same under it.
  - fail: The seats change colour rather than tint; or the dashboard changes; or the interior rearranges.
- P5 [fatal · permanence_count]
  - expect: One car and one tunnel.
  - fail: A second car appears inside; or the tunnel vanishes; or the car passes through the wall.
- P6 [minor · attribute_drift]
  - expect: The interior stays the same.
  - fail: Objects move; or the windows change; or the tunnel changes shape.

## OPT-0159 · illumination · train

**Caption.** A flashlight pointed at a wall is swung up to the ceiling, and the lit spot leaves the wall and appears on the ceiling.

**Expectation (hidden).** The spot travels up the wall and onto the ceiling continuously with the beam; the wall goes dark once the beam has left it.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A flashlight is pointed at a wall.
- S2 [core] It is swung up to the ceiling.
- S3 [core] The lit spot leaves the wall and appears on the ceiling.
- S4 [minor] The wall goes dark once the beam has left it.

**PC**
- P1 [core · missing_consequence]
  - expect: The spot travels up the wall and onto the ceiling continuously with the beam, and the wall goes dark once the beam has left.
  - fail: The spot jumps; or the wall stays lit; or the spot stays on the wall while the beam is on the ceiling.
- P2 [core · causeless_motion]
  - expect: The spot moves only as the flashlight swings.
  - fail: It drifts with the flashlight still; or moves before the swing; or flickers.
- P3 [major · shape_identity]
  - expect: The spot is one patch that stretches as the beam grazes the corner.
  - fail: It splits; or is a sharp square; or keeps a fixed shape across the corner.
- P4 [major · trajectory_momentum]
  - expect: The spot moves the same way the beam swings.
  - fail: It moves the opposite way; or crosswise; or jumps.
- P5 [fatal · permanence_count]
  - expect: One flashlight and one spot.
  - fail: A second spot appears; or the flashlight vanishes; or the spot becomes solid.
- P6 [minor · attribute_drift]
  - expect: The wall and the ceiling stay the same.
  - fail: The wall changes colour; or the ceiling changes; or the flashlight changes.

**Note.** The hand is the minimal trigger; the person is not judged. Illumination: the on/off causality of electric lights belongs to Electricity; here only where the light goes once it exists is judged.

## OPT-0160 · illumination · train

**Caption.** A hand is cupped over the front of a flashlight, and the beam is blocked and the room goes dark.

**Expectation (hidden).** The light disappears the instant the hand covers the lens and the fingers glow red at the edges; the beam returns when the hand is removed.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A flashlight is on.
- S2 [core] A hand is cupped over its front.
- S3 [core] The beam is blocked and the room goes dark.
- S4 [minor] The fingers glow red at the edges.
- S5 [minor] The hand comes first and the dark follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The light disappears the instant the hand covers the lens and would return when the hand is removed.
  - fail: The room stays lit with the lens covered; or goes dark before the hand arrives; or stays dark after the hand is removed.
- P2 [core · process_direction]
  - expect: The change is at the moment of covering and holds while covered.
  - fail: The room fades slowly; or flickers; or brightens while covered.
- P3 [major · attribute_drift]
  - expect: The fingers glow red where the light passes through them.
  - fail: They glow white; or do not glow at all; or the glow is away from the lens.
- P4 [major · causeless_motion]
  - expect: The hand moves only as the person moves it.
  - fail: It floats; or passes through the flashlight; or the flashlight moves by itself.
- P5 [fatal · permanence_count]
  - expect: One flashlight and one hand.
  - fail: The flashlight duplicates; or a second hand appears; or the hand passes through the lens.
- P6 [minor · attribute_drift]
  - expect: The room stays the same.
  - fail: Furniture rearranges; or the walls change; or the flashlight changes.

**Note.** The hand is the object blocking the beam; the person is not judged.

## OPT-0161 · illumination · train

**Caption.** A door to a lit hallway is opened into a dark room, and a wedge of light spreads across the floor as the door swings.

**Expectation (hidden).** The lit wedge widens with the door and narrows as it closes; the door's shadow edge moves with it.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A door leads from a lit hallway into a dark room.
- S2 [core] The door is opened.
- S3 [core] A wedge of light spreads across the floor as the door swings.
- S4 [minor] The wedge widens with the door.

**PC**
- P1 [core · missing_consequence]
  - expect: The lit wedge widens with the door and would narrow as it closes, and the door's shadow edge moves with it.
  - fail: The wedge is there with the door shut; or stays narrow with the door wide; or the shadow edge stays fixed.
- P2 [core · causeless_motion]
  - expect: The wedge changes only as the door moves.
  - fail: It grows with the door still; or before the door moves; or flickers.
- P3 [major · shape_identity]
  - expect: The wedge is a bright fan on the floor spreading from the doorway.
  - fail: It is a round spot; or splits; or is on the ceiling only.
- P4 [major · trajectory_momentum]
  - expect: The door swings in an arc on its hinges.
  - fail: It slides; or lifts; or spins.
- P5 [fatal · permanence_count]
  - expect: One door and one wedge.
  - fail: A second door appears; or the wedge becomes solid; or the door passes through the frame.
- P6 [minor · attribute_drift]
  - expect: The room and the hallway stay the same.
  - fail: Furniture rearranges; or the walls change; or the light changes colour.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0162 · illumination · train

**Caption.** Two identical white vases stand at different distances from a single lamp in a dark room, and the nearer one is lit far more brightly than the farther one.

**Expectation (hidden).** Brightness falls off with distance from the lamp; if the far vase is moved toward the lamp it brightens.

**Declared violation types.** missing_consequence, attribute_drift

**SA**
- S1 [core] Two identical white vases stand in a dark room.
- S2 [core] A single lamp lights them from different distances.
- S3 [core] The nearer one is lit far more brightly than the farther one.
- S4 [minor] The far vase would brighten if moved toward the lamp.

**PC**
- P1 [core · missing_consequence]
  - expect: Brightness falls off with distance from the lamp: the near vase is bright and the far one dim.
  - fail: Both are equally bright; or the far one is brighter; or neither is lit with the lamp on.
- P2 [core · attribute_drift]
  - expect: Both vases are white; only their brightness differs.
  - fail: One changes colour; or the far one is a different colour; or both change colour.
- P3 [major · missing_consequence]
  - expect: Each vase's shadow points away from the lamp.
  - fail: Shadows point toward the lamp; or in different directions; or there are none.
- P4 [major · causeless_motion]
  - expect: The vases and the lamp stay put.
  - fail: A vase slides; or the lamp moves by itself; or the lit side changes with nothing moving.
- P5 [fatal · permanence_count]
  - expect: Two vases and one lamp.
  - fail: A third vase appears; or one vanishes; or the lamp duplicates.
- P6 [minor · attribute_drift]
  - expect: The room stays the same.
  - fail: The table changes; or the walls change; or the vases change shape.

**Note.** Illumination: the on/off causality of electric lights belongs to Electricity; here only where the light goes once it exists is judged.

## OPT-0163 · illumination · train

**Caption.** A lit candle is carried down a dark staircase, and the light on the walls travels with the candle.

**Expectation (hidden).** The walls are brightest near the flame and darken behind as the candle moves on; the light flickers with the flame.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A lit candle is carried down a dark staircase.
- S2 [core] The light on the walls travels with the candle.
- S3 [minor] The light flickers with the flame.
- S4 [minor] The walls darken behind as the candle moves on.

**PC**
- P1 [core · missing_consequence]
  - expect: The walls are brightest near the flame and darken behind as the candle moves on.
  - fail: The light stays put while the candle moves; or walls stay lit behind; or light appears ahead.
- P2 [core · causeless_motion]
  - expect: The lit area moves only with the candle and flickers only with the flame.
  - fail: It drifts with the candle still; or pulses with a steady flame; or jumps.
- P3 [major · gravity_direction]
  - expect: The flame points upward.
  - fail: It points down or sideways in still air; or detaches; or floats.
- P4 [major · missing_consequence]
  - expect: Shadows on the walls point away from the flame.
  - fail: They point toward it; or in several directions; or there are none.
- P5 [fatal · permanence_count]
  - expect: One candle and one flame.
  - fail: A second flame appears; or the candle vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The staircase stays the same.
  - fail: The steps change; or the walls change colour rather than brightness; or the candle changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0164 · illumination · train

**Caption.** A lighter is struck in a dark garage and held up, and the small flame lights the nearby tools and bench.

**Expectation (hidden).** Only things near the flame are visible, lit from the flame's direction; the light flickers and goes out when the lighter closes.

**Declared violation types.** missing_consequence, attribute_drift

**SA**
- S1 [core] A lighter is struck in a dark garage.
- S2 [core] It is held up.
- S3 [core] The small flame lights the nearby tools and bench.
- S4 [minor] Only things near the flame are visible.
- S5 [minor] The light flickers.

**PC**
- P1 [core · missing_consequence]
  - expect: Only things near the flame are visible, lit from the flame's direction.
  - fail: The far wall is as bright as the bench; or the near tools stay dark; or the light comes from elsewhere.
- P2 [core · attribute_drift]
  - expect: The light is warm and flickers with the flame.
  - fail: It is steady white; or a different colour; or the tools change colour rather than brightness.
- P3 [major · causeless_motion]
  - expect: The lit area moves only with the lighter and would go out when it closes.
  - fail: It drifts with the lighter still; or stays lit after the flame is out; or appears before the strike.
- P4 [major · gravity_direction]
  - expect: The flame points upward.
  - fail: It points down or sideways in still air; or detaches; or floats.
- P5 [fatal · permanence_count]
  - expect: One lighter and one flame.
  - fail: A second flame appears; or the lighter vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The bench and tools stay the same.
  - fail: Tools rearrange; or the bench changes; or the lighter changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0165 · illumination · train

**Caption.** A cinema's house lights dim before the film starts, and the seats fade from view until only the screen glows.

**Expectation (hidden).** The dimming is gradual, the seats go dark, and the screen's light on the front rows changes with the picture.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A cinema's house lights are on.
- S2 [core] They dim before the film starts.
- S3 [core] The seats fade from view.
- S4 [core] Only the screen glows.
- S5 [minor] The dimming is gradual.

**PC**
- P1 [core · process_direction]
  - expect: The dimming is gradual and the seats go dark until only the screen glows.
  - fail: The lights snap off; or brighten again; or the seats stay visible with the lights out.
- P2 [core · missing_consequence]
  - expect: The screen's light on the front rows changes with the picture.
  - fail: The front rows are lit with the screen dark; or stay dark with a bright screen; or are lit from behind.
- P3 [major · causeless_motion]
  - expect: Nothing moves in the hall.
  - fail: Seats move; or the screen shifts; or the lit area wanders.
- P4 [major · attribute_drift]
  - expect: Colours dim without changing hue.
  - fail: The seats change colour; or the walls change; or the light turns another colour.
- P5 [fatal · permanence_count]
  - expect: The seats keep their number.
  - fail: Seats vanish; or appear; or the screen duplicates.
- P6 [minor · attribute_drift]
  - expect: The hall stays the same.
  - fail: The rows rearrange; or the screen changes size; or the curtains change.

**Note.** Illumination: the on/off causality of electric lights belongs to Electricity; here only where the light goes once it exists is judged.

## OPT-0166 · illumination · train

**Caption.** A row of paper lanterns hanging in a garden is lit one by one, and each glows as its candle is lit.

**Expectation (hidden).** A lantern glows only after its candle is lit and lights the leaves nearest to it; unlit lanterns stay dark.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A row of paper lanterns hangs in a garden.
- S2 [core] They are lit one by one.
- S3 [core] Each glows as its candle is lit.
- S4 [minor] Unlit lanterns stay dark.

**PC**
- P1 [core · missing_consequence]
  - expect: A lantern glows only after its candle is lit and lights the leaves nearest to it.
  - fail: A lantern glows before it is lit; or stays dark after; or the leaves far away brighten more than the near ones.
- P2 [core · permanence_count]
  - expect: The lanterns keep their number and each is lit once.
  - fail: A lantern vanishes; or appears; or one glows in two places.
- P3 [major · process_direction]
  - expect: Lit lanterns stay lit.
  - fail: One goes out on its own; or flickers off and on; or dims as the next is lit.
- P4 [major · causeless_motion]
  - expect: The lanterns hang still and sway only if touched.
  - fail: They swing wildly untouched; or float up; or one moves along the row.
- P5 [fatal · shape_identity]
  - expect: Each lantern keeps its shape.
  - fail: One changes shape; or merges with its neighbour; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The lanterns' colours and the garden stay the same.
  - fail: A lantern changes colour; or the garden rearranges; or the string changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0167 · illumination · train

**Caption.** A flashlight shines through cupped fingers, and the fingers glow red where the light passes through them.

**Expectation (hidden).** The glow appears where the flesh is thin and disappears when the flashlight is turned off; the light beyond the hand is dim.

**Declared violation types.** missing_consequence, attribute_drift

**SA**
- S1 [core] A flashlight shines through cupped fingers.
- S2 [core] The fingers glow red where the light passes through them.
- S3 [minor] The light beyond the hand is dim.

**PC**
- P1 [core · missing_consequence]
  - expect: The glow appears where the flesh is thin and would disappear when the flashlight is turned off.
  - fail: The fingers glow with the light off; or the thick palm glows and the thin fingers do not; or the glow is elsewhere.
- P2 [core · attribute_drift]
  - expect: The glow is red.
  - fail: It is white or blue; or it changes colour with a steady light; or the fingers change colour when the light is off.
- P3 [major · missing_consequence]
  - expect: The light beyond the hand is dim compared with the glow.
  - fail: The room beyond is fully lit; or the beam passes through the hand unhindered; or the wall behind is brighter than the fingers.
- P4 [major · causeless_motion]
  - expect: The hand and flashlight move only as the person moves them.
  - fail: They float; or the flashlight moves by itself; or the glow moves with both still.
- P5 [fatal · permanence_count]
  - expect: One hand and one flashlight.
  - fail: A second hand appears; or a finger vanishes; or the hand passes through the lens.
- P6 [minor · attribute_drift]
  - expect: The room stays the same.
  - fail: The walls change; or the flashlight changes; or the room rearranges.

**Note.** The hand is the object the light passes through; the person is not judged.

## OPT-0168 · illumination · train

**Caption.** A stage's lights are turned up gradually, and the dark set becomes visible piece by piece as the brightness rises.

**Expectation (hidden).** The scene brightens smoothly with no jumps; shadows appear away from the lamps; it does not brighten before the lights come up.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A stage is dark.
- S2 [core] Its lights are turned up gradually.
- S3 [core] The set becomes visible piece by piece as the brightness rises.
- S4 [minor] Shadows appear away from the lamps.

**PC**
- P1 [core · process_direction]
  - expect: The scene brightens smoothly with no jumps and does not brighten before the lights come up.
  - fail: It jumps to full; or flickers; or it is lit before the lights rise.
- P2 [core · missing_consequence]
  - expect: Shadows appear away from the lamps.
  - fail: Shadows point toward the lamps; or in several directions under one lamp; or there are none.
- P3 [major · causeless_motion]
  - expect: Nothing on the set moves.
  - fail: Set pieces move; or the lit area wanders; or a lamp swings.
- P4 [major · attribute_drift]
  - expect: Colours emerge without changing hue.
  - fail: The set changes colour as it brightens; or the lights change colour; or the backdrop changes.
- P5 [fatal · permanence_count]
  - expect: The set pieces keep their number.
  - fail: A piece vanishes; or appears; or a lamp duplicates.
- P6 [minor · attribute_drift]
  - expect: The set stays the same.
  - fail: Pieces rearrange; or the backdrop changes; or the stage changes.

**Note.** Illumination: the on/off causality of electric lights belongs to Electricity; here only where the light goes once it exists is judged.

## OPT-0169 · illumination · train

**Caption.** Seen from inside a dim shop, the open doorway to the sunlit street stands out as a bright rectangle and the floor near the door is lit.

**Expectation (hidden).** The interior is dim relative to the doorway, the floor near the door is lit, and it grows darker deeper into the shop.

**Declared violation types.** missing_consequence, attribute_drift

**SA**
- S1 [core] The view is from inside a dim shop.
- S2 [core] The open doorway to the sunlit street stands out as a bright rectangle.
- S3 [core] The floor near the door is lit.
- S4 [minor] It grows darker deeper into the shop.

**PC**
- P1 [core · missing_consequence]
  - expect: The interior is dim relative to the doorway, the floor near the door is lit, and it grows darker deeper in.
  - fail: The back of the shop is as bright as the door; or the floor by the door is dark; or the light comes from the back.
- P2 [core · attribute_drift]
  - expect: The interior's colours are the same, only dimmer.
  - fail: Objects change colour with depth; or the doorway is a colour; or the floor changes colour.
- P3 [major · causeless_motion]
  - expect: The lit area stays put with the door and sun fixed.
  - fail: It wanders; or flickers; or the door moves by itself.
- P4 [major · shape_identity]
  - expect: The bright rectangle is the doorway's shape.
  - fail: It is round; or splits; or is larger than the door.
- P5 [fatal · permanence_count]
  - expect: One doorway.
  - fail: A second doorway appears; or it vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The shop stays the same.
  - fail: Shelves rearrange; or the door changes; or the street changes.

## OPT-0170 · illumination · train

**Caption.** A firework bursts high in the night sky, and for a moment the rooftops below are lit.

**Expectation (hidden).** The rooftops brighten at the burst and dim as it fades; the light comes from above; the ground is lit only briefly.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A firework bursts high in the night sky.
- S2 [core] For a moment the rooftops below are lit.
- S3 [minor] The light comes from above.
- S4 [minor] The ground is lit only briefly.

**PC**
- P1 [core · missing_consequence]
  - expect: The rooftops brighten at the burst and dim as it fades, lit from above.
  - fail: They stay lit after the burst fades; or brighten before it; or are lit from below.
- P2 [core · process_direction]
  - expect: The light is a brief burst that fades.
  - fail: It stays bright; or flickers on and off; or brightens after the burst.
- P3 [major · gravity_direction]
  - expect: The sparks spread and fall.
  - fail: They rise indefinitely; or hang; or fall upward.
- P4 [major · attribute_drift]
  - expect: The rooftops take the burst's colour for the instant.
  - fail: They are a different colour from the burst; or change colour permanently; or are white under a coloured burst.
- P5 [fatal · permanence_count]
  - expect: The rooftops keep their number.
  - fail: A building vanishes; or appears; or the burst becomes solid.
- P6 [minor · attribute_drift]
  - expect: The skyline stays the same.
  - fail: Buildings rearrange; or change shape; or the sky changes abruptly.

## OPT-0171 · illumination · train

**Caption.** A desk lamp is turned to point at the wall, and the wall brightens while the desk beneath it goes dim.

**Expectation (hidden).** The lit area moves with the lamp head; whatever the lamp is aimed at is brightest and what it turns away from darkens.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A desk lamp lights a desk.
- S2 [core] It is turned to point at the wall.
- S3 [core] The wall brightens.
- S4 [core] The desk beneath goes dim.
- S5 [minor] The turn comes first and the light moves with it.

**PC**
- P1 [core · missing_consequence]
  - expect: The lit area moves with the lamp head: the wall brightens and the desk dims.
  - fail: Both stay as they were; or the desk brightens; or the wall stays dark with the lamp on it.
- P2 [core · causeless_motion]
  - expect: The lit area moves only as the lamp turns.
  - fail: It drifts with the lamp still; or moves before the turn; or flickers.
- P3 [major · shape_identity]
  - expect: The lit area is one soft pool.
  - fail: It splits; or is a sharp square; or floods the room.
- P4 [major · missing_consequence]
  - expect: Shadows point away from the lamp head.
  - fail: They point toward it; or in several directions; or there are none.
- P5 [fatal · permanence_count]
  - expect: One lamp.
  - fail: A second lamp appears; or it vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The desk and the wall stay the same.
  - fail: The wall changes colour rather than brightness; or the desk changes; or the lamp changes.

**Note.** The hand is the minimal trigger; the person is not judged. Illumination: the on/off causality of electric lights belongs to Electricity; here only where the light goes once it exists is judged.

## OPT-0172 · illumination · train

**Caption.** A car drives past a house at night, and its headlights sweep across the front windows, lighting the curtains for a moment.

**Expectation (hidden).** The light moves along the wall in the direction the car travels and is gone once the car has passed; the wall does not stay lit.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A car drives past a house at night.
- S2 [core] Its headlights sweep across the front windows.
- S3 [core] The curtains are lit for a moment.
- S4 [minor] The light is gone once the car has passed.

**PC**
- P1 [core · missing_consequence]
  - expect: The light moves along the wall in the direction the car travels and is gone once the car has passed.
  - fail: The wall stays lit; or the light moves the opposite way; or it is there with no car.
- P2 [core · causeless_motion]
  - expect: The light moves only as the car moves.
  - fail: It moves with the car stopped; or jumps; or lingers.
- P3 [major · shape_identity]
  - expect: The lit patch is a soft sweep, not a hard shape.
  - fail: It is a sharp square; or splits; or is a spot that stays.
- P4 [major · trajectory_momentum]
  - expect: The car travels steadily past.
  - fail: It jumps position; or reverses; or stops with no cause.
- P5 [fatal · permanence_count]
  - expect: One car and one house.
  - fail: A second car appears; or the house vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The house and the curtains stay the same.
  - fail: The curtains change colour rather than brightness; or the house changes; or the street rearranges.

## OPT-0173 · illumination · train

**Caption.** A lamp with a coloured shade is switched on, and the shade glows while the desk below is lit through its open bottom.

**Expectation (hidden).** The shade glows evenly with the bulb inside and the brightest spot is directly beneath the shade; the light stops when the lamp is off.

**Declared violation types.** missing_consequence, attribute_drift

**SA**
- S1 [core] A lamp has a coloured shade.
- S2 [core] It is switched on.
- S3 [core] The shade glows.
- S4 [core] The desk below is lit through the open bottom.
- S5 [minor] The brightest spot is directly beneath the shade.

**PC**
- P1 [core · missing_consequence]
  - expect: The shade glows evenly with the bulb inside and the brightest spot is directly beneath.
  - fail: The shade stays dark with the lamp on; or the brightest spot is far to one side; or the desk stays dark.
- P2 [core · attribute_drift]
  - expect: The glow through the shade is the shade's colour and the desk below is lit whiter.
  - fail: The shade glows a different colour; or the desk is the shade's colour; or the glow changes colour.
- P3 [major · causeless_motion]
  - expect: The light would stop when the lamp is off and the lit area stays put.
  - fail: The shade glows with the lamp off; or the lit area wanders; or flickers.
- P4 [major · shape_identity]
  - expect: The lit area below is a round pool.
  - fail: It is a sharp square; or splits; or is on the ceiling only.
- P5 [fatal · permanence_count]
  - expect: One lamp.
  - fail: A second lamp appears; or it vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The desk and the room stay the same.
  - fail: The desk changes; or the room rearranges; or the shade changes shape.

**Note.** Illumination: the on/off causality of electric lights belongs to Electricity; here only where the light goes once it exists is judged.

## OPT-0174 · illumination · train

**Caption.** A dog walks through an office with motion-sensor lights, and the ceiling panels switch on ahead of it and go off behind it.

**Expectation (hidden).** Each panel lights as the dog approaches and its patch of floor brightens; panels far behind it go dark after a delay.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A dog walks through an office with motion-sensor lights.
- S2 [core] The ceiling panels switch on ahead of it.
- S3 [core] They go off behind it.
- S4 [minor] Each panel's patch of floor brightens as it lights.

**PC**
- P1 [core · missing_consequence]
  - expect: Each panel lights as the dog approaches and its patch of floor brightens.
  - fail: Panels light far from the dog; or stay dark as it passes beneath; or the floor stays dark under a lit panel.
- P2 [core · process_direction]
  - expect: Panels behind the dog go dark after a delay and do not flicker.
  - fail: They stay lit indefinitely; or go off before the dog has passed; or flicker.
- P3 [major · causeless_motion]
  - expect: The lighting follows the dog's path.
  - fail: Panels light in a pattern unrelated to the dog; or the dog jumps position; or lights come on with the dog gone.
- P4 [major · missing_consequence]
  - expect: The dog's shadow falls away from the lit panel above.
  - fail: It points toward the panel; or in several directions; or there is none.
- P5 [fatal · permanence_count]
  - expect: The panels keep their number.
  - fail: A panel vanishes; or appears; or the dog duplicates.
- P6 [minor · attribute_drift]
  - expect: The office stays the same.
  - fail: Desks rearrange; or the panels change colour; or the dog changes.

**Note.** The dog is self-driven; only the lights' response to its position is judged. Illumination: the on/off causality of electric lights belongs to Electricity; here only where the light goes once it exists is judged.

## OPT-0175 · illumination · train

**Caption.** The last candle on a dinner table is blown out, and the table falls into darkness.

**Expectation (hidden).** The warm light on the table disappears with the flame; the room stays dark afterwards.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] The last candle on a dinner table is lit.
- S2 [core] It is blown out.
- S3 [core] The table falls into darkness.
- S4 [minor] The room stays dark afterwards.

**PC**
- P1 [core · missing_consequence]
  - expect: The warm light on the table disappears with the flame.
  - fail: The table stays lit with the flame out; or goes dark before the flame; or another light appears.
- P2 [core · process_direction]
  - expect: The room stays dark afterwards.
  - fail: The candle relights; or the room brightens with no source; or the light flickers back.
- P3 [major · causeless_motion]
  - expect: The flame goes out with the breath.
  - fail: It goes out with no breath; or leans toward the breath; or stays lit through the puff.
- P4 [major · gravity_direction]
  - expect: The smoke rises.
  - fail: It sinks; or hangs; or flows sideways with no draught.
- P5 [fatal · permanence_count]
  - expect: One candle.
  - fail: A second candle appears; or it vanishes; or the flame becomes solid.
- P6 [minor · attribute_drift]
  - expect: The table setting stays the same.
  - fail: Items rearrange; or the cloth changes; or the candle changes.

**Note.** The breath is the trigger; the person is not judged.

## OPT-0176 · illumination · train

**Caption.** A garage door rolls up in the morning, and daylight moves across the floor from the front to the back as the door opens.

**Expectation (hidden).** The lit region on the floor grows inward as the door rises; the rear of the garage brightens last.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A garage door is shut in the morning.
- S2 [core] It rolls up.
- S3 [core] Daylight moves across the floor from the front to the back.
- S4 [minor] The rear of the garage brightens last.

**PC**
- P1 [core · missing_consequence]
  - expect: The lit region on the floor grows inward as the door rises and the rear brightens last.
  - fail: The rear brightens first; or the floor is lit with the door shut; or the lit region shrinks as the door rises.
- P2 [core · causeless_motion]
  - expect: The lit region moves only as the door moves.
  - fail: It grows with the door still; or before the door moves; or flickers.
- P3 [major · process_direction]
  - expect: The door rises steadily and the light grows with it.
  - fail: The door jumps; or reverses; or the light jumps.
- P4 [major · shape_identity]
  - expect: The lit region is a band across the floor spreading from the doorway.
  - fail: It is a round spot; or splits; or is on the ceiling only.
- P5 [fatal · permanence_count]
  - expect: One door and one garage.
  - fail: A second door appears; or the garage vanishes; or the door passes through the frame.
- P6 [minor · attribute_drift]
  - expect: The garage and its contents stay the same.
  - fail: Items rearrange; or the walls change; or the door changes colour.

## OPT-0177 · illumination · train

**Caption.** An underwater torch is switched on in murky water, and a cone of lit particles appears in front of it.

**Expectation (hidden).** The lit cone points where the torch points, fades with distance, and moves with the torch; the water behind stays dark.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] An underwater torch is in murky water.
- S2 [core] It is switched on.
- S3 [core] A cone of lit particles appears in front of it.
- S4 [minor] The water behind stays dark.

**PC**
- P1 [core · missing_consequence]
  - expect: The lit cone points where the torch points, fades with distance, and moves with the torch.
  - fail: The cone points elsewhere; or is even to its end; or stays put while the torch moves.
- P2 [core · causeless_motion]
  - expect: The cone appears with the switch and moves only with the torch.
  - fail: It is there with the torch off; or drifts with the torch still; or flickers.
- P3 [major · shape_identity]
  - expect: The cone is one soft-edged beam of lit particles.
  - fail: It is a sharp rod; or splits; or floods the whole water.
- P4 [major · material_response]
  - expect: The particles drift slowly in the water.
  - fail: They are rigid and still; or shoot about; or the water is clear with a visible beam.
- P5 [fatal · permanence_count]
  - expect: One torch and one cone.
  - fail: A second cone appears; or the torch vanishes; or the beam becomes solid.
- P6 [minor · attribute_drift]
  - expect: The water's colour and the torch stay the same.
  - fail: The water changes colour; or the torch changes; or the beam changes colour.

**Note.** The hand is the minimal trigger; the person is not judged. Illumination: the on/off causality of electric lights belongs to Electricity; here only where the light goes once it exists is judged.

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

## OPT-0180 · color_mixing · train

**Caption.** A red stage light is switched on over a white curtain, and the curtain turns red under the light.

**Expectation (hidden).** The curtain looks red only while the red light is on and where the light reaches; it looks white again when the light changes.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] A white curtain hangs on a stage.
- S2 [core] A red stage light is switched on over it.
- S3 [core] The curtain turns red under the light.
- S4 [minor] The switch comes first and the colour follows.

**PC**
- P1 [core · attribute_drift]
  - expect: The curtain looks red only where the light's light reaches and while it is on.
  - fail: The curtain is red with the light off; or stays white under the red light; or turns a different colour from the light.
- P2 [core · missing_consequence]
  - expect: The change happens at the same instant as the light and is confined to where its light falls.
  - fail: The curtain changes before the light; or long after; or surfaces the light cannot reach change too.
- P3 [major · shape_identity]
  - expect: The curtain's folds show as darker and lighter red, not as colour changes.
  - fail: The folds are a different colour; or the curtain is flat red with no shading; or the folds vanish.
- P4 [major · causeless_motion]
  - expect: Nothing moves; only the light changes.
  - fail: The curtain moves; or the light moves by itself; or the lit area wanders.
- P5 [fatal · permanence_count]
  - expect: One light and one curtain.
  - fail: A second light appears; or the curtain vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The curtain's shape and the surroundings stay the same.
  - fail: The curtain changes shape; or the surroundings rearrange; or the light changes shape.

## OPT-0181 · color_mixing · train

**Caption.** Sunlight shines through a stained-glass window, and coloured patches of light lie across the church floor.

**Expectation (hidden).** Each patch has the colour of the glass it came through and lies on the floor away from the window; the patches fade when a cloud covers the sun.

**Declared violation types.** missing_consequence, attribute_drift

**SA**
- S1 [core] Sunlight shines through a stained-glass window.
- S2 [core] Coloured patches of light lie across the church floor.
- S3 [minor] Each patch has the colour of the glass it came through.
- S4 [minor] The patches lie on the side away from the window.

**PC**
- P1 [core · attribute_drift]
  - expect: Each patch has the colour of the glass it came through.
  - fail: A patch is a colour not in the window; or all patches are white; or the patches swap colours.
- P2 [core · missing_consequence]
  - expect: The patches lie on the floor away from the window and would fade if a cloud covered the sun.
  - fail: They lie on the window side; or on the ceiling; or they stay bright with the sun plainly gone.
- P3 [major · shape_identity]
  - expect: The patches together form the window's pattern, stretched by the angle.
  - fail: They form a different pattern; or are round blobs; or one patch splits.
- P4 [major · causeless_motion]
  - expect: The patches do not move with the sun steady.
  - fail: They drift across the floor; or flicker; or swing round.
- P5 [fatal · permanence_count]
  - expect: One window and its patches.
  - fail: A second window's patches appear; or the window vanishes; or a patch becomes solid.
- P6 [minor · attribute_drift]
  - expect: The window and the floor stay the same.
  - fail: The glass changes pattern; or the floor changes; or the pews rearrange.

## OPT-0182 · color_mixing · train

**Caption.** A piece of blue cellophane is taped over a flashlight, and the beam on the wall turns blue.

**Expectation (hidden).** The lit spot on the wall changes to blue as soon as the film covers the lens and goes white again when it is removed.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] A flashlight is on.
- S2 [core] A piece of blue cellophane is taped over it.
- S3 [core] The beam on the wall turns blue.
- S4 [minor] The spot goes white again when the film is removed.
- S5 [minor] The film goes on first and the colour changes with it.

**PC**
- P1 [core · attribute_drift]
  - expect: The spot looks blue only where the film's light reaches and while it is on.
  - fail: The spot is blue with the film off; or stays white under the blue light; or turns a different colour from the light.
- P2 [core · missing_consequence]
  - expect: The change happens at the same instant as the film and is confined to where its light falls.
  - fail: The spot changes before the film; or long after; or surfaces the light cannot reach change too.
- P3 [major · shape_identity]
  - expect: The spot keeps its shape and place; only its colour changes.
  - fail: The spot moves when the film goes on; or changes shape; or splits.
- P4 [major · causeless_motion]
  - expect: Nothing moves; only the light changes.
  - fail: The spot moves; or the film moves by itself; or the lit area wanders.
- P5 [fatal · permanence_count]
  - expect: One film and one spot.
  - fail: A second film appears; or the spot vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The spot's shape and the surroundings stay the same.
  - fail: The spot changes shape; or the surroundings rearrange; or the film changes shape.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0183 · color_mixing · train

**Caption.** A garden hose sprays a fine mist with the sun behind it, and a small rainbow appears in the spray.

**Expectation (hidden).** The rainbow appears within the mist while the spray runs and disappears when the water is turned off; it is not on the ground or in the dry air.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A garden hose sprays a fine mist.
- S2 [core] The sun is behind it.
- S3 [core] A small rainbow appears in the spray.
- S4 [minor] The rainbow disappears when the water is turned off.

**PC**
- P1 [core · missing_consequence]
  - expect: The rainbow appears within the mist while the spray runs and is not on the ground or in dry air.
  - fail: It is on the ground; or in dry air beside the spray; or the spray runs in sunlight with no rainbow.
- P2 [core · permanence_count]
  - expect: The rainbow exists only with the mist and would vanish when the water is turned off.
  - fail: It stays with the water off; or appears before the spray; or two rainbows appear from one spray.
- P3 [major · attribute_drift]
  - expect: The rainbow shows the spectrum's order in a band.
  - fail: It is a single colour; or the colours are in random order; or it changes colours.
- P4 [major · gravity_direction]
  - expect: The mist drifts and falls.
  - fail: It rises indefinitely; or hangs; or falls upward.
- P5 [fatal · permanence_count]
  - expect: One hose and one spray.
  - fail: A second hose appears; or the spray comes from nowhere; or the rainbow becomes solid.
- P6 [minor · attribute_drift]
  - expect: The garden and the hose stay the same.
  - fail: The garden rearranges; or the hose changes colour; or the sky changes abruptly.

## OPT-0184 · color_mixing · train

**Caption.** A ray of sunlight hits a glass prism on a windowsill, and a band of rainbow colours appears on the wall.

**Expectation (hidden).** The coloured band appears on the side away from the sun and moves when the prism is turned; it disappears when the prism is taken away.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A glass prism sits on a windowsill.
- S2 [core] A ray of sunlight hits it.
- S3 [core] A band of rainbow colours appears on the wall.
- S4 [minor] The band moves when the prism is turned.
- S5 [minor] The band lies on the side away from the sun.

**PC**
- P1 [core · missing_consequence]
  - expect: The coloured band appears on the side away from the sun and would disappear if the prism were removed.
  - fail: It is on the sun side; or there with no prism; or the prism is in sunlight with no band.
- P2 [core · causeless_motion]
  - expect: The band moves only when the prism is turned.
  - fail: It drifts with the prism still; or stays put while the prism turns; or flickers in steady sun.
- P3 [major · attribute_drift]
  - expect: The band shows the spectrum's order.
  - fail: It is a single colour; or the order is random; or it changes colours with the prism steady.
- P4 [major · shape_identity]
  - expect: The band is one elongated strip.
  - fail: It splits into several; or is a round spot; or floods the wall.
- P5 [fatal · permanence_count]
  - expect: One prism and one band.
  - fail: A second prism appears; or the band becomes solid; or the prism vanishes.
- P6 [minor · attribute_drift]
  - expect: The sill and the wall stay the same.
  - fail: The sill changes; or the wall changes colour; or the prism changes shape.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0185 · color_mixing · train

**Caption.** A crystal chandelier catches afternoon sunlight, and little flecks of rainbow light scatter across the walls and ceiling.

**Expectation (hidden).** The flecks appear only while the sun hits the crystals and move when the chandelier sways; they vanish when the sun is blocked.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A crystal chandelier hangs in afternoon sunlight.
- S2 [core] Little flecks of rainbow light scatter across the walls and ceiling.
- S3 [minor] The flecks move when the chandelier sways.
- S4 [minor] They vanish when the sun is blocked.

**PC**
- P1 [core · missing_consequence]
  - expect: The flecks appear only while the sun hits the crystals and vanish when the sun is blocked.
  - fail: They are there with the sun blocked; or the crystals are in sun with no flecks; or the flecks are on the sun side only.
- P2 [core · causeless_motion]
  - expect: The flecks move only when the chandelier sways.
  - fail: They dance with the chandelier still; or stay put while it sways; or flicker in steady sun.
- P3 [major · attribute_drift]
  - expect: The flecks are rainbow-coloured.
  - fail: They are all white; or a single colour; or they change colour with nothing moving.
- P4 [major · shape_identity]
  - expect: The flecks are many small spots.
  - fail: They merge into one flood; or are large squares; or a single spot.
- P5 [fatal · permanence_count]
  - expect: One chandelier.
  - fail: A second appears; or it vanishes; or a fleck becomes solid.
- P6 [minor · attribute_drift]
  - expect: The room stays the same.
  - fail: Furniture rearranges; or the walls change; or the chandelier changes shape.

## OPT-0186 · color_mixing · train

**Caption.** Blue ink is dripped into a glass of clear water, and the blue spreads in swirls until the water is evenly tinted.

**Expectation (hidden).** The colour spreads outward and downward from the drop and gets paler as it spreads; it does not gather back into a drop.

**Declared violation types.** process_direction, attribute_drift

**SA**
- S1 [core] A glass of clear water is present.
- S2 [core] Blue ink is dripped into it.
- S3 [core] The blue spreads in swirls.
- S4 [core] The water becomes evenly tinted.
- S5 [minor] The drop comes first and the spread follows.

**PC**
- P1 [core · process_direction]
  - expect: The blue spreads from the drop through the water in swirls, outward and downward, getting paler as it spreads and never gathers back; coloured areas stay coloured.
  - fail: The water returns to its original colour where it was blue; or the blue gathers back into the drop; or the blue appears before the drop arrives.
- P2 [core · attribute_drift]
  - expect: The result is blue, and un-reached water keeps its original colour.
  - fail: The water turns a colour other than blue; or the un-reached water changes; or the blue is darker than the drop itself.
- P3 [major · material_response]
  - expect: The water behaves as it should: streaks and swirls where stirred or spread, settling where it flows.
  - fail: The water is rigid and unmarked; or it flows like water when it is a paste; or it bounces like rubber.
- P4 [major · causeless_motion]
  - expect: The water moves only where stirred or where the blue flows.
  - fail: The water swirls by itself; or the blue spreads faster than stirring or flow carries it; or the container moves.
- P5 [fatal · permanence_count]
  - expect: The amount of water stays the same and the container keeps its shape.
  - fail: The container fills or empties on its own; or a second container appears; or the drop passes through the container.
- P6 [minor · attribute_drift]
  - expect: The container and the background stay the same.
  - fail: The container changes colour; or the background rearranges; or the tool changes.

## OPT-0187 · color_mixing · train

**Caption.** A spoonful of turmeric is stirred into a pot of white rice, and the rice turns yellow where the spice is mixed in.

**Expectation (hidden).** Yellow spreads from the spoon through the rice as it is stirred, and streaks even out; the rice does not return to white.

**Declared violation types.** attribute_drift, process_direction

**SA**
- S1 [core] A pot of white rice is present.
- S2 [core] A spoonful of turmeric is stirred into it.
- S3 [core] The rice turns yellow where the spice is mixed in.
- S4 [minor] Streaks even out with stirring.
- S5 [minor] The spoon goes in first and the colour follows.

**PC**
- P1 [core · process_direction]
  - expect: The yellow spreads from the spoon through the rice as it is stirred, streaks evening out and never gathers back; coloured areas stay coloured.
  - fail: The rice returns to its original colour where it was yellow; or the yellow gathers back into the spoon; or the yellow appears before the spoon arrives.
- P2 [core · attribute_drift]
  - expect: The result is yellow, and un-reached rice keeps its original colour.
  - fail: The rice turns a colour other than yellow; or the un-reached rice changes; or the yellow is darker than the spoon itself.
- P3 [major · material_response]
  - expect: The rice behaves as it should: streaks and swirls where stirred or spread, settling where it flows.
  - fail: The rice is rigid and unmarked; or it flows like water when it is a paste; or it bounces like rubber.
- P4 [major · causeless_motion]
  - expect: The rice moves only where stirred or where the yellow flows.
  - fail: The rice swirls by itself; or the yellow spreads faster than stirring or flow carries it; or the container moves.
- P5 [fatal · permanence_count]
  - expect: The amount of rice stays the same and the container keeps its shape.
  - fail: The container fills or empties on its own; or a second container appears; or the spoon passes through the container.
- P6 [minor · attribute_drift]
  - expect: The container and the background stay the same.
  - fail: The container changes colour; or the background rearranges; or the tool changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0188 · color_mixing · train

**Caption.** Red and white paint on a paper plate are swirled together with a brush, and the swirl turns pink.

**Expectation (hidden).** Pink appears where the brush blends the two and the streaks become uniform with more mixing; the colours do not separate.

**Declared violation types.** attribute_drift, process_direction

**SA**
- S1 [core] Red and white paint sit on a paper plate.
- S2 [core] A brush swirls them together.
- S3 [core] The swirl turns pink.
- S4 [minor] The streaks become uniform with more mixing.
- S5 [minor] The colours are separate first, then swirled, then pink.

**PC**
- P1 [core · process_direction]
  - expect: The pink spreads from the brush through the paint where the brush blends the two, streaks becoming uniform and never gathers back; coloured areas stay coloured.
  - fail: The paint returns to its original colour where it was pink; or the pink gathers back into the brush; or the pink appears before the brush arrives.
- P2 [core · attribute_drift]
  - expect: The result is pink, and un-reached paint keeps its original colour.
  - fail: The paint turns a colour other than pink; or the un-reached paint changes; or the pink is darker than the brush itself.
- P3 [major · material_response]
  - expect: The paint behaves as it should: streaks and swirls where stirred or spread, settling where it flows.
  - fail: The paint is rigid and unmarked; or it flows like water when it is a paste; or it bounces like rubber.
- P4 [major · causeless_motion]
  - expect: The paint moves only where stirred or where the pink flows.
  - fail: The paint swirls by itself; or the pink spreads faster than stirring or flow carries it; or the container moves.
- P5 [fatal · permanence_count]
  - expect: The amount of paint stays the same and the container keeps its shape.
  - fail: The container fills or empties on its own; or a second container appears; or the brush passes through the container.
- P6 [minor · attribute_drift]
  - expect: The container and the background stay the same.
  - fail: The container changes colour; or the background rearranges; or the tool changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0189 · color_mixing · train

**Caption.** A party light is switched from white to green, and the white walls of the room turn green.

**Expectation (hidden).** The walls change colour with the light and at the same instant; things in the light's shadow stay unchanged.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] A party light lights a room with white walls.
- S2 [core] It is switched from white to green.
- S3 [core] The walls turn green.
- S4 [minor] Things in the light's shadow stay unchanged.
- S5 [minor] The switch comes first and the colour changes with it.

**PC**
- P1 [core · attribute_drift]
  - expect: The wall looks green only where the light's light reaches and while it is on.
  - fail: The wall is green with the light off; or stays white under the green light; or turns a different colour from the light.
- P2 [core · missing_consequence]
  - expect: The change happens at the same instant as the light and is confined to where its light falls.
  - fail: The wall changes before the light; or long after; or surfaces the light cannot reach change too.
- P3 [major · shape_identity]
  - expect: Objects in the light's shadow keep their own colour.
  - fail: Shadowed objects turn green too; or lit objects stay white; or the shadows vanish.
- P4 [major · causeless_motion]
  - expect: Nothing moves; only the light changes.
  - fail: The wall moves; or the light moves by itself; or the lit area wanders.
- P5 [fatal · permanence_count]
  - expect: One light and one wall.
  - fail: A second light appears; or the wall vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The wall's shape and the surroundings stay the same.
  - fail: The wall changes shape; or the surroundings rearrange; or the light changes shape.

## OPT-0190 · color_mixing · train

**Caption.** A car brakes on a rain-wet street at night, and red light from its brake lights spreads over the wet road behind it.

**Expectation (hidden).** The red glow appears on the road when the lights come on and disappears when they go off; it lies behind the car, not in front.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] A car is on a rain-wet street at night.
- S2 [core] It brakes.
- S3 [core] Red light from its brake lights spreads over the wet road behind it.
- S4 [minor] The glow lies behind the car, not in front.

**PC**
- P1 [core · attribute_drift]
  - expect: The glow on the road is red and lies behind the car.
  - fail: It is white; or lies in front; or is a colour the lights do not show.
- P2 [core · missing_consequence]
  - expect: The glow appears when the lights come on and would disappear when they go off.
  - fail: It is there with the lights off; or the lights are on with no glow; or it stays after they go off.
- P3 [major · material_response]
  - expect: The road is wet: the glow shimmers where puddles ripple and is absent where dry.
  - fail: It is a sharp mirror image on rough tarmac; or shows on dry patches; or the water is rigid.
- P4 [major · causeless_motion]
  - expect: The glow moves only with the car.
  - fail: It drifts with the car stopped; or flickers with steady lights; or moves ahead of the car.
- P5 [fatal · permanence_count]
  - expect: One car and its two brake lights.
  - fail: A light vanishes; or a third appears; or the car duplicates.
- P6 [minor · attribute_drift]
  - expect: The car and the street stay the same.
  - fail: The car changes colour; or the street rearranges; or the buildings change.

## OPT-0191 · color_mixing · train

**Caption.** Morning sun shines through red curtains, and the white bedroom walls take on a red tint.

**Expectation (hidden).** The tint is strongest where the light through the curtain falls and disappears when the curtains are opened; the walls are white in ordinary light.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] Morning sun shines through red curtains.
- S2 [core] The white bedroom walls take on a red tint.
- S3 [minor] The tint is strongest where the light through the curtain falls.
- S4 [minor] The walls are white where ordinary light reaches them.

**PC**
- P1 [core · attribute_drift]
  - expect: The wall looks red only where the curtain's light reaches and while it is on.
  - fail: The wall is red with the curtain off; or stays white under the red light; or turns a different colour from the light.
- P2 [core · missing_consequence]
  - expect: The change happens at the same instant as the curtain and is confined to where its light falls.
  - fail: The wall changes before the curtain; or long after; or surfaces the light cannot reach change too.
- P3 [major · shape_identity]
  - expect: The tint follows the shape of the light through the curtain.
  - fail: The tint is a hard-edged square unlike the window; or covers walls the window cannot light; or splits.
- P4 [major · causeless_motion]
  - expect: Nothing moves; only the light changes.
  - fail: The wall moves; or the curtain moves by itself; or the lit area wanders.
- P5 [fatal · permanence_count]
  - expect: One curtain and one wall.
  - fail: A second curtain appears; or the wall vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The wall's shape and the surroundings stay the same.
  - fail: The wall changes shape; or the surroundings rearrange; or the curtain changes shape.

## OPT-0192 · color_mixing · train

**Caption.** A smart bulb is switched from white to purple, and the room's white ceiling turns purple.

**Expectation (hidden).** The ceiling colour changes with the bulb and returns to white when the bulb does; surfaces the bulb does not reach are unchanged.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] A smart bulb lights a room with a white ceiling.
- S2 [core] It is switched from white to purple.
- S3 [core] The ceiling turns purple.
- S4 [minor] Surfaces the bulb does not reach are unchanged.
- S5 [minor] The switch comes first and the colour changes with it.

**PC**
- P1 [core · attribute_drift]
  - expect: The ceiling looks purple only where the bulb's light reaches and while it is on.
  - fail: The ceiling is purple with the bulb off; or stays white under the purple light; or turns a different colour from the light.
- P2 [core · missing_consequence]
  - expect: The change happens at the same instant as the bulb and is confined to where its light falls.
  - fail: The ceiling changes before the bulb; or long after; or surfaces the light cannot reach change too.
- P3 [major · shape_identity]
  - expect: The ceiling's features show as darker and lighter purple, not as colour changes.
  - fail: Features are a different colour; or the ceiling is flat purple with no shading; or features vanish.
- P4 [major · causeless_motion]
  - expect: Nothing moves; only the light changes.
  - fail: The ceiling moves; or the bulb moves by itself; or the lit area wanders.
- P5 [fatal · permanence_count]
  - expect: One bulb and one ceiling.
  - fail: A second bulb appears; or the ceiling vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The ceiling's shape and the surroundings stay the same.
  - fail: The ceiling changes shape; or the surroundings rearrange; or the bulb changes shape.

## OPT-0193 · color_mixing · train

**Caption.** A sheet of red plastic is held up in front of the camera, and everything seen through it looks red.

**Expectation (hidden).** Only the view through the plastic is tinted; the scene beyond its edges is normal; the tint vanishes when the plastic is lowered.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] A sheet of red plastic is held up in front of the camera.
- S2 [core] Everything seen through it looks red.
- S3 [minor] The scene beyond its edges is normal.
- S4 [minor] The tint vanishes when the plastic is lowered.

**PC**
- P1 [core · attribute_drift]
  - expect: Only the view through the plastic is tinted red; beyond its edges the scene is normal.
  - fail: The whole scene is red; or the view through the plastic is normal; or the tint is a different colour.
- P2 [core · missing_consequence]
  - expect: The tint moves with the plastic and would vanish when it is lowered.
  - fail: It stays put while the plastic moves; or remains after it is lowered; or appears before it is raised.
- P3 [major · shape_identity]
  - expect: The scene through the plastic is the same scene, tinted, not a different picture.
  - fail: A different scene appears; or objects appear that are not there; or the image is mirrored.
- P4 [major · material_response]
  - expect: The plastic is a thin flexible sheet.
  - fail: It is rigid glass; or it flows; or it tears.
- P5 [fatal · permanence_count]
  - expect: One sheet.
  - fail: It duplicates; or vanishes; or the hand passes through it.
- P6 [minor · attribute_drift]
  - expect: The scene stays the same.
  - fail: It rearranges; or objects move; or the sheet changes colour.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0194 · color_mixing · train

**Caption.** A purple bath bomb is dropped into a tub of clear water, and the colour billows out and turns the whole bath purple.

**Expectation (hidden).** The colour spreads from the bath bomb as it fizzes, thinning as it goes, until the water is evenly coloured; the water does not clear again.

**Declared violation types.** process_direction, attribute_drift

**SA**
- S1 [core] A tub of clear water is present.
- S2 [core] A purple bath bomb is dropped in.
- S3 [core] The colour billows out.
- S4 [core] The whole bath turns purple.
- S5 [minor] The bath bomb fizzes as the colour spreads.

**PC**
- P1 [core · process_direction]
  - expect: The purple spreads from the bath bomb through the water as it fizzes, thinning as it goes, until the water is evenly coloured and never gathers back; coloured areas stay coloured.
  - fail: The water returns to its original colour where it was purple; or the purple gathers back into the bath bomb; or the purple appears before the bath bomb arrives.
- P2 [core · attribute_drift]
  - expect: The result is purple, and un-reached water keeps its original colour.
  - fail: The water turns a colour other than purple; or the un-reached water changes; or the purple is darker than the bath bomb itself.
- P3 [major · material_response]
  - expect: The water behaves as it should: streaks and swirls where stirred or spread, settling where it flows.
  - fail: The water is rigid and unmarked; or it flows like water when it is a paste; or it bounces like rubber.
- P4 [major · causeless_motion]
  - expect: The water moves only where stirred or where the purple flows.
  - fail: The water swirls by itself; or the purple spreads faster than stirring or flow carries it; or the container moves.
- P5 [fatal · permanence_count]
  - expect: The amount of water stays the same and the container keeps its shape.
  - fail: The container fills or empties on its own; or a second container appears; or the bath bomb passes through the container.
- P6 [minor · attribute_drift]
  - expect: The container and the background stay the same.
  - fail: The container changes colour; or the background rearranges; or the tool changes.

## OPT-0195 · color_mixing · train

**Caption.** Snow falls under an orange streetlamp, and the snow on the ground beneath the lamp looks orange while the snow farther away looks white.

**Expectation (hidden).** The tint is strongest directly under the lamp and fades with distance; snow outside the lamp's reach stays white.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] Snow falls under an orange streetlamp.
- S2 [core] The snow on the ground beneath the lamp looks orange.
- S3 [core] The snow farther away looks white.
- S4 [minor] The tint fades with distance from the lamp.

**PC**
- P1 [core · attribute_drift]
  - expect: The snow looks orange only where the lamp's light reaches and while it is on.
  - fail: The snow is orange with the lamp off; or stays white under the orange light; or turns a different colour from the light.
- P2 [core · missing_consequence]
  - expect: The change happens at the same instant as the lamp and is confined to where its light falls.
  - fail: The snow changes before the lamp; or long after; or surfaces the light cannot reach change too.
- P3 [major · gravity_direction]
  - expect: The snow falls downward through the light.
  - fail: It rises; or hangs; or falls sideways in still air.
- P4 [major · causeless_motion]
  - expect: Nothing moves; only the light changes.
  - fail: The snow moves; or the lamp moves by itself; or the lit area wanders.
- P5 [fatal · permanence_count]
  - expect: One lamp and one snow.
  - fail: A second lamp appears; or the snow vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The snow's shape and the surroundings stay the same.
  - fail: The snow changes shape; or the surroundings rearrange; or the lamp changes shape.

## OPT-0196 · color_mixing · train

**Caption.** Blue paint is dabbed onto a wet patch of yellow watercolour, and the colours bleed into each other making green where they meet.

**Expectation (hidden).** The green forms along the boundary and widens as the paint spreads; the pure colours remain farther from the join.

**Declared violation types.** process_direction, attribute_drift

**SA**
- S1 [core] A wet patch of yellow watercolour is on paper.
- S2 [core] Blue paint is dabbed onto it.
- S3 [core] The colours bleed into each other.
- S4 [core] Green forms where they meet.
- S5 [minor] The pure colours remain farther from the join.

**PC**
- P1 [core · process_direction]
  - expect: The green forms along the boundary and widens as the paint spreads; it does not retreat.
  - fail: The green shrinks; or the colours separate again; or green appears where the paints have not met.
- P2 [core · attribute_drift]
  - expect: The mix is green, and the pure yellow and blue remain at the edges.
  - fail: The mix is a colour other than green; or the pure colours change; or the whole patch turns one colour at once.
- P3 [major · material_response]
  - expect: Wet watercolour bleeds and feathers on the paper.
  - fail: It stays as hard-edged blobs; or beads up and rolls; or the paper stays dry.
- P4 [major · causeless_motion]
  - expect: The paint spreads only where wet and where dabbed.
  - fail: It jumps across dry paper; or the paper moves; or the brush moves by itself.
- P5 [fatal · permanence_count]
  - expect: One sheet and one brush.
  - fail: The sheet duplicates; or the brush vanishes; or paint appears from nowhere.
- P6 [minor · attribute_drift]
  - expect: The paper and the table stay the same.
  - fail: The paper changes shape; or the table changes; or the brush changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0197 · color_mixing · train

**Caption.** Sunlight passes through a glass of red wine on a white tablecloth, and a red patch of light appears on the cloth beside the glass.

**Expectation (hidden).** The red patch lies on the side away from the sun and moves when the glass moves; it disappears when the glass is lifted.

**Declared violation types.** missing_consequence, attribute_drift

**SA**
- S1 [core] A glass of red wine stands on a white tablecloth.
- S2 [core] Sunlight passes through it.
- S3 [core] A red patch of light appears on the cloth beside the glass.
- S4 [minor] The patch lies on the side away from the sun.
- S5 [minor] The patch moves when the glass moves.

**PC**
- P1 [core · missing_consequence]
  - expect: The red patch lies on the side away from the sun and would disappear if the glass were lifted.
  - fail: It lies on the sun side; or is there with no glass; or the glass is in sun with no patch.
- P2 [core · attribute_drift]
  - expect: The patch is the wine's red.
  - fail: It is white; or a different colour; or it changes colour with the glass still.
- P3 [major · causeless_motion]
  - expect: The patch moves only when the glass moves.
  - fail: It drifts with the glass still; or stays put while the glass moves; or flickers in steady sun.
- P4 [major · shape_identity]
  - expect: The patch is one soft shape roughly the glass's footprint.
  - fail: It splits; or is a sharp square; or floods the cloth.
- P5 [fatal · permanence_count]
  - expect: One glass and one patch.
  - fail: A second glass appears; or the patch becomes solid; or the glass vanishes.
- P6 [minor · attribute_drift]
  - expect: The cloth and the glass stay the same.
  - fail: The cloth changes colour; or the glass changes shape; or the table setting rearranges.

## OPT-0198 · color_mixing · train

**Caption.** A little green food colouring is poured into a bowl of white cake batter and stirred, and the batter turns pale green.

**Expectation (hidden).** Green streaks spread with each stir and even out; the batter does not turn back to white.

**Declared violation types.** attribute_drift, process_direction

**SA**
- S1 [core] A bowl of white cake batter is present.
- S2 [core] Green food colouring is poured in.
- S3 [core] The batter is stirred.
- S4 [core] The batter turns pale green.
- S5 [minor] Green streaks spread with each stir and even out.

**PC**
- P1 [core · process_direction]
  - expect: The pale green spreads from the colouring through the batter with each stir, streaks evening out and never gathers back; coloured areas stay coloured.
  - fail: The batter returns to its original colour where it was pale green; or the pale green gathers back into the colouring; or the pale green appears before the colouring arrives.
- P2 [core · attribute_drift]
  - expect: The result is pale green, and un-reached batter keeps its original colour.
  - fail: The batter turns a colour other than pale green; or the un-reached batter changes; or the pale green is darker than the colouring itself.
- P3 [major · material_response]
  - expect: The batter behaves as it should: streaks and swirls where stirred or spread, settling where it flows.
  - fail: The batter is rigid and unmarked; or it flows like water when it is a paste; or it bounces like rubber.
- P4 [major · causeless_motion]
  - expect: The batter moves only where stirred or where the pale green flows.
  - fail: The batter swirls by itself; or the pale green spreads faster than stirring or flow carries it; or the container moves.
- P5 [fatal · permanence_count]
  - expect: The amount of batter stays the same and the container keeps its shape.
  - fail: The container fills or empties on its own; or a second container appears; or the colouring passes through the container.
- P6 [minor · attribute_drift]
  - expect: The container and the background stay the same.
  - fail: The container changes colour; or the background rearranges; or the tool changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0199 · color_mixing · train

**Caption.** A red and a blue spotlight are crossed on a white backdrop, and the area where they overlap glows purple.

**Expectation (hidden).** The overlap is a different colour from either beam alone and disappears when one light is turned off; the single-colour areas stay red and blue.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] A red and a blue spotlight are crossed on a white backdrop.
- S2 [core] The area where they overlap glows purple.
- S3 [minor] The single-colour areas stay red and blue.
- S4 [minor] The overlap disappears when one light is turned off.

**PC**
- P1 [core · attribute_drift]
  - expect: The overlap is a different colour from either beam alone, and the single-colour areas stay red and blue.
  - fail: The overlap is red or blue; or the single areas change colour; or the overlap is a colour unrelated to both.
- P2 [core · missing_consequence]
  - expect: The overlap exists only where both beams fall and would disappear if one light were turned off.
  - fail: The purple area is outside both beams; or stays with one light off; or there is no overlap where the beams plainly cross.
- P3 [major · causeless_motion]
  - expect: The beams and the coloured areas do not move with the lights fixed.
  - fail: An area drifts; or the beams swing; or the colours flicker.
- P4 [major · shape_identity]
  - expect: Each beam is one soft-edged patch and the overlap is their intersection.
  - fail: A beam splits; or the overlap is larger than either beam; or the patches are sharp squares.
- P5 [fatal · permanence_count]
  - expect: Two spotlights and one backdrop.
  - fail: A third light appears; or the backdrop vanishes; or a patch becomes solid.
- P6 [minor · attribute_drift]
  - expect: The backdrop and the stage stay the same.
  - fail: The backdrop changes shape; or the stage rearranges; or the lights change shape.

## OPT-0200 · color_mixing · train

**Caption.** A white lamp is seen through a jar of yellow juice and looks yellow through the jar.

**Expectation (hidden).** The lamp is tinted only where seen through the juice; beside the jar it looks white.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] A jar of yellow juice is present.
- S2 [core] A white lamp is seen through it.
- S3 [core] The lamp looks yellow through the jar.
- S4 [minor] Beside the jar the lamp looks white.

**PC**
- P1 [core · attribute_drift]
  - expect: The lamp looks yellow only where the jar's light reaches and while it is on.
  - fail: The lamp is yellow with the jar off; or stays white under the yellow light; or turns a different colour from the light.
- P2 [core · missing_consequence]
  - expect: The change happens at the same instant as the jar and is confined to where its light falls.
  - fail: The lamp changes before the jar; or long after; or surfaces the light cannot reach change too.
- P3 [major · shape_identity]
  - expect: The lamp is the same lamp, tinted, and shifted only by the jar's curve.
  - fail: A different lamp appears; or it is mirrored; or it is enlarged far beyond the jar.
- P4 [major · causeless_motion]
  - expect: Nothing moves; only the light changes.
  - fail: The lamp moves; or the jar moves by itself; or the lit area wanders.
- P5 [fatal · permanence_count]
  - expect: One jar and one lamp.
  - fail: A second jar appears; or the lamp vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The lamp's shape and the surroundings stay the same.
  - fail: The lamp changes shape; or the surroundings rearrange; or the jar changes shape.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0201 · color_mixing · train

**Caption.** A pair of yellow-tinted sunglasses is held up in front of a white wall, and the wall looks yellow through the lenses.

**Expectation (hidden).** The tint appears only through the lenses; when the glasses are lowered the wall is white.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] A pair of yellow-tinted sunglasses is held up in front of a white wall.
- S2 [core] The wall looks yellow through the lenses.
- S3 [minor] When the glasses are lowered the wall is white.

**PC**
- P1 [core · attribute_drift]
  - expect: The wall looks yellow only where the lens's light reaches and while it is on.
  - fail: The wall is yellow with the lens off; or stays white under the yellow light; or turns a different colour from the light.
- P2 [core · missing_consequence]
  - expect: The change happens at the same instant as the lens and is confined to where its light falls.
  - fail: The wall changes before the lens; or long after; or surfaces the light cannot reach change too.
- P3 [major · shape_identity]
  - expect: The wall through the lenses is the same wall, tinted.
  - fail: A different scene appears; or it is mirrored; or it is heavily warped by flat lenses.
- P4 [major · causeless_motion]
  - expect: Nothing moves; only the light changes.
  - fail: The wall moves; or the lens moves by itself; or the lit area wanders.
- P5 [fatal · permanence_count]
  - expect: One lens and one wall.
  - fail: A second lens appears; or the wall vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The wall's shape and the surroundings stay the same.
  - fail: The wall changes shape; or the surroundings rearrange; or the lens changes shape.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0202 · color_mixing · train

**Caption.** A brush loaded with red paint is swirled through a jar of clean water, and the water turns pink and cloudy.

**Expectation (hidden).** Colour streams off the brush and spreads through the jar, getting more even with each swirl; the water does not clear.

**Declared violation types.** process_direction, attribute_drift

**SA**
- S1 [core] A jar of clean water is present.
- S2 [core] A brush loaded with red paint is swirled through it.
- S3 [core] The water turns pink and cloudy.
- S4 [minor] The colour gets more even with each swirl.

**PC**
- P1 [core · process_direction]
  - expect: The pink spreads from the brush through the water streaming off the brush and getting more even with each swirl and never gathers back; coloured areas stay coloured.
  - fail: The water returns to its original colour where it was pink; or the pink gathers back into the brush; or the pink appears before the brush arrives.
- P2 [core · attribute_drift]
  - expect: The result is pink, and un-reached water keeps its original colour.
  - fail: The water turns a colour other than pink; or the un-reached water changes; or the pink is darker than the brush itself.
- P3 [major · material_response]
  - expect: The water behaves as it should: streaks and swirls where stirred or spread, settling where it flows.
  - fail: The water is rigid and unmarked; or it flows like water when it is a paste; or it bounces like rubber.
- P4 [major · causeless_motion]
  - expect: The water moves only where stirred or where the pink flows.
  - fail: The water swirls by itself; or the pink spreads faster than stirring or flow carries it; or the container moves.
- P5 [fatal · permanence_count]
  - expect: The amount of water stays the same and the container keeps its shape.
  - fail: The container fills or empties on its own; or a second container appears; or the brush passes through the container.
- P6 [minor · attribute_drift]
  - expect: The container and the background stay the same.
  - fail: The container changes colour; or the background rearranges; or the tool changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0203 · color_mixing · train

**Caption.** Two shades of hair dye are squeezed into a bowl and whisked together, and the mixture becomes one uniform colour.

**Expectation (hidden).** Streaks of the two shades blend with each stroke until the bowl is a single even colour; the shades do not separate again.

**Declared violation types.** attribute_drift, process_direction

**SA**
- S1 [core] Two shades of hair dye are squeezed into a bowl.
- S2 [core] They are whisked together.
- S3 [core] The mixture becomes one uniform colour.
- S4 [minor] Streaks of the two shades blend with each stroke.

**PC**
- P1 [core · process_direction]
  - expect: The single blended colour spreads from the whisk through the dye stroke by stroke until the bowl is even and never gathers back; coloured areas stay coloured.
  - fail: The dye returns to its original colour where it was single blended colour; or the single blended colour gathers back into the whisk; or the single blended colour appears before the whisk arrives.
- P2 [core · attribute_drift]
  - expect: The result is single blended colour, and un-reached dye keeps its original colour.
  - fail: The dye turns a colour other than single blended colour; or the un-reached dye changes; or the single blended colour is darker than the whisk itself.
- P3 [major · material_response]
  - expect: The dye behaves as it should: streaks and swirls where stirred or spread, settling where it flows.
  - fail: The dye is rigid and unmarked; or it flows like water when it is a paste; or it bounces like rubber.
- P4 [major · causeless_motion]
  - expect: The dye moves only where stirred or where the single blended colour flows.
  - fail: The dye swirls by itself; or the single blended colour spreads faster than stirring or flow carries it; or the container moves.
- P5 [fatal · permanence_count]
  - expect: The amount of dye stays the same and the container keeps its shape.
  - fail: The container fills or empties on its own; or a second container appears; or the whisk passes through the container.
- P6 [minor · attribute_drift]
  - expect: The container and the background stay the same.
  - fail: The container changes colour; or the background rearranges; or the tool changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0204 · color_mixing · train

**Caption.** A theatre spotlight with a blue filter is aimed at a white piano, and the piano turns blue under the beam.

**Expectation (hidden).** The piano looks blue where the beam hits and white where it does not; it returns to white when the filter is removed.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] A white piano stands on a stage.
- S2 [core] A theatre spotlight with a blue filter is aimed at it.
- S3 [core] The piano turns blue under the beam.
- S4 [minor] The piano is white where the beam does not reach.
- S5 [minor] It returns to white when the filter is removed.

**PC**
- P1 [core · attribute_drift]
  - expect: The piano looks blue only where the spotlight's light reaches and while it is on.
  - fail: The piano is blue with the spotlight off; or stays white under the blue light; or turns a different colour from the light.
- P2 [core · missing_consequence]
  - expect: The change happens at the same instant as the spotlight and is confined to where its light falls.
  - fail: The piano changes before the spotlight; or long after; or surfaces the light cannot reach change too.
- P3 [major · shape_identity]
  - expect: The piano's shape and shading show in blue, not as colour changes.
  - fail: Parts are a different colour; or the piano is flat blue with no shading; or the piano changes shape.
- P4 [major · causeless_motion]
  - expect: Nothing moves; only the light changes.
  - fail: The piano moves; or the spotlight moves by itself; or the lit area wanders.
- P5 [fatal · permanence_count]
  - expect: One spotlight and one piano.
  - fail: A second spotlight appears; or the piano vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The piano's shape and the surroundings stay the same.
  - fail: The piano changes shape; or the surroundings rearrange; or the spotlight changes shape.

## OPT-0205 · color_mixing · train

**Caption.** Sunlight passes through a blue glass bottle on a windowsill, and a blue patch of light lies on the counter beside it.

**Expectation (hidden).** The patch is on the side away from the sun and matches the bottle's colour; it moves when the bottle is moved.

**Declared violation types.** missing_consequence, attribute_drift

**SA**
- S1 [core] A blue glass bottle stands on a windowsill in sunlight.
- S2 [core] Sunlight passes through it.
- S3 [core] A blue patch of light lies on the counter beside it.
- S4 [minor] The patch is on the side away from the sun.
- S5 [minor] The patch moves when the bottle is moved.

**PC**
- P1 [core · missing_consequence]
  - expect: The patch is on the side away from the sun and moves when the bottle is moved.
  - fail: It lies on the sun side; or stays put while the bottle moves; or is there with no bottle.
- P2 [core · attribute_drift]
  - expect: The patch matches the bottle's blue.
  - fail: It is white; or a different colour; or it changes colour with the bottle still.
- P3 [major · causeless_motion]
  - expect: The patch does not move on its own.
  - fail: It drifts with the bottle still; or flickers in steady sun.
- P4 [major · shape_identity]
  - expect: The patch is one soft shape roughly the bottle's footprint.
  - fail: It splits; or is a sharp square; or floods the counter.
- P5 [fatal · permanence_count]
  - expect: One bottle and one patch.
  - fail: A second bottle appears; or the patch becomes solid; or the bottle vanishes.
- P6 [minor · attribute_drift]
  - expect: The sill and the counter stay the same.
  - fail: The sill changes; or the counter changes colour; or the bottle changes shape.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0206 · color_mixing · train

**Caption.** Yellow and red watercolour are dripped onto a wet sheet of paper, and where they run together an orange band forms.

**Expectation (hidden).** The orange forms only where the two colours meet and spreads as they bleed; the pure colours remain at the edges.

**Declared violation types.** process_direction, attribute_drift

**SA**
- S1 [core] A wet sheet of paper is present.
- S2 [core] Yellow and red watercolour are dripped onto it.
- S3 [core] They run together.
- S4 [core] An orange band forms where they meet.
- S5 [minor] The pure colours remain at the edges.

**PC**
- P1 [core · process_direction]
  - expect: The orange forms only where the two colours meet and spreads as they bleed; it does not retreat.
  - fail: The orange shrinks; or the colours separate again; or orange appears where they have not met.
- P2 [core · attribute_drift]
  - expect: The mix is orange, and the pure yellow and red remain at the edges.
  - fail: The mix is a colour other than orange; or the pure colours change; or the whole sheet turns one colour at once.
- P3 [major · material_response]
  - expect: Wet watercolour bleeds and feathers on the paper.
  - fail: It stays as hard-edged blobs; or beads up and rolls; or the paper stays dry.
- P4 [major · gravity_direction]
  - expect: The drops fall onto the paper and the paint runs where the paper slopes.
  - fail: The drops rise; or the paint runs uphill; or the drops hang.
- P5 [fatal · permanence_count]
  - expect: One sheet.
  - fail: It duplicates; or vanishes; or paint appears from nowhere.
- P6 [minor · attribute_drift]
  - expect: The paper and the table stay the same.
  - fail: The paper changes shape; or the table changes; or the dropper changes.

## OPT-0207 · color_mixing · train

**Caption.** A green glass is held up to the light in front of a white wall, and the wall looks green through it.

**Expectation (hidden).** The tint is only in the view through the glass; the wall around it is white and returns to white when the glass is lowered.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] A green glass is held up to the light in front of a white wall.
- S2 [core] The wall looks green through it.
- S3 [minor] The wall around the glass is white.
- S4 [minor] The wall returns to white when the glass is lowered.

**PC**
- P1 [core · attribute_drift]
  - expect: The wall looks green only where the glass's light reaches and while it is on.
  - fail: The wall is green with the glass off; or stays white under the green light; or turns a different colour from the light.
- P2 [core · missing_consequence]
  - expect: The change happens at the same instant as the glass and is confined to where its light falls.
  - fail: The wall changes before the glass; or long after; or surfaces the light cannot reach change too.
- P3 [major · shape_identity]
  - expect: The wall through the glass is the same wall, tinted and shifted only by the glass's curve.
  - fail: A different scene appears; or it is mirrored; or it is enlarged far beyond the glass.
- P4 [major · causeless_motion]
  - expect: Nothing moves; only the light changes.
  - fail: The wall moves; or the glass moves by itself; or the lit area wanders.
- P5 [fatal · permanence_count]
  - expect: One glass and one wall.
  - fail: A second glass appears; or the wall vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The wall's shape and the surroundings stay the same.
  - fail: The wall changes shape; or the surroundings rearrange; or the glass changes shape.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0208 · color_mixing · train

**Caption.** A fountain's spray in a park is lit at night by coloured lamps, and the falling water glows in the lamps' colours.

**Expectation (hidden).** The water takes the colour of whatever lamp lights it and changes when the lamps change; unlit water is dark.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] A fountain's spray in a park is lit at night by coloured lamps.
- S2 [core] The falling water glows in the lamps' colours.
- S3 [minor] The water changes colour when the lamps change.
- S4 [minor] Unlit water is dark.

**PC**
- P1 [core · attribute_drift]
  - expect: The water takes the colour of whatever lamp lights it and unlit water is dark.
  - fail: The water is white under coloured lamps; or glows with the lamps off; or is a colour the lamps do not show.
- P2 [core · missing_consequence]
  - expect: The water changes colour when the lamps change, at the same moment.
  - fail: It changes before the lamps; or long after; or the lamps change and the water does not.
- P3 [major · gravity_direction]
  - expect: The spray rises and falls back.
  - fail: It rises indefinitely; or hangs; or falls upward.
- P4 [major · material_response]
  - expect: The water is liquid spray that breaks into drops.
  - fail: It is a rigid rod; or beads bounce; or it is solid.
- P5 [fatal · permanence_count]
  - expect: One fountain and its lamps.
  - fail: A second fountain appears; or a lamp vanishes; or the spray becomes solid.
- P6 [minor · attribute_drift]
  - expect: The fountain and the park stay the same.
  - fail: The basin changes; or the park rearranges; or the lamps change shape.

## OPT-0209 · color_mixing · train

**Caption.** A spoonful of beet juice is dropped into a bowl of white yogurt and folded in, and the yogurt turns pink with darker streaks that fade as it is mixed.

**Expectation (hidden).** The pink spreads from the juice as the spoon moves and evens out with more folding; the yogurt does not become white again.

**Declared violation types.** attribute_drift, process_direction

**SA**
- S1 [core] A bowl of white yogurt is present.
- S2 [core] A spoonful of beet juice is dropped in.
- S3 [core] It is folded in.
- S4 [core] The yogurt turns pink with darker streaks.
- S5 [minor] The streaks fade as it is mixed.

**PC**
- P1 [core · process_direction]
  - expect: The pink spreads from the spoon through the yogurt as the spoon folds it, streaks evening out and never gathers back; coloured areas stay coloured.
  - fail: The yogurt returns to its original colour where it was pink; or the pink gathers back into the spoon; or the pink appears before the spoon arrives.
- P2 [core · attribute_drift]
  - expect: The result is pink, and un-reached yogurt keeps its original colour.
  - fail: The yogurt turns a colour other than pink; or the un-reached yogurt changes; or the pink is darker than the spoon itself.
- P3 [major · material_response]
  - expect: The yogurt behaves as it should: streaks and swirls where stirred or spread, settling where it flows.
  - fail: The yogurt is rigid and unmarked; or it flows like water when it is a paste; or it bounces like rubber.
- P4 [major · causeless_motion]
  - expect: The yogurt moves only where stirred or where the pink flows.
  - fail: The yogurt swirls by itself; or the pink spreads faster than stirring or flow carries it; or the container moves.
- P5 [fatal · permanence_count]
  - expect: The amount of yogurt stays the same and the container keeps its shape.
  - fail: The container fills or empties on its own; or a second container appears; or the spoon passes through the container.
- P6 [minor · attribute_drift]
  - expect: The container and the background stay the same.
  - fail: The container changes colour; or the background rearranges; or the tool changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0210 · color_mixing · train

**Caption.** Sunlight through a sprinkler's fan of water forms a rainbow that shifts as the sprinkler swings.

**Expectation (hidden).** The rainbow is inside the spray and moves with it; it disappears when the sprinkler stops or the sun is covered.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A sprinkler throws a fan of water in sunlight.
- S2 [core] A rainbow forms in the spray.
- S3 [core] The rainbow shifts as the sprinkler swings.
- S4 [minor] The rainbow is inside the spray.

**PC**
- P1 [core · missing_consequence]
  - expect: The rainbow is inside the spray and would disappear if the sprinkler stopped or the sun were covered.
  - fail: It is on the ground; or in dry air; or stays with the water off.
- P2 [core · causeless_motion]
  - expect: The rainbow moves with the spray and only then.
  - fail: It stays put while the spray swings; or moves with the spray still; or flickers in steady sun.
- P3 [major · attribute_drift]
  - expect: The rainbow shows the spectrum's order.
  - fail: It is a single colour; or the order is random; or it changes colours.
- P4 [major · gravity_direction]
  - expect: The spray arcs and falls.
  - fail: It rises indefinitely; or hangs; or falls upward.
- P5 [fatal · permanence_count]
  - expect: One sprinkler and one spray.
  - fail: A second sprinkler appears; or the spray comes from nowhere; or the rainbow becomes solid.
- P6 [minor · attribute_drift]
  - expect: The lawn and the sprinkler stay the same.
  - fail: The lawn changes; or the sprinkler changes; or the sky changes abruptly.

## OPT-0211 · color_mixing · train

**Caption.** A stage floods with yellow light, and the white set and curtains all look yellow at once.

**Expectation (hidden).** Every lit white surface changes together to yellow and back when the light changes; shadowed folds stay darker.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] A stage has a white set and curtains.
- S2 [core] It floods with yellow light.
- S3 [core] The set and curtains all look yellow at once.
- S4 [minor] Shadowed folds stay darker.
- S5 [minor] The light comes first and the colour changes with it.

**PC**
- P1 [core · attribute_drift]
  - expect: The set looks yellow only where the light's light reaches and while it is on.
  - fail: The set is yellow with the light off; or stays white under the yellow light; or turns a different colour from the light.
- P2 [core · missing_consequence]
  - expect: The change happens at the same instant as the light and is confined to where its light falls.
  - fail: The set changes before the light; or long after; or surfaces the light cannot reach change too.
- P3 [major · shape_identity]
  - expect: The folds show as darker and lighter yellow, not as colour changes.
  - fail: Folds are a different colour; or the set is flat yellow with no shading; or the folds vanish.
- P4 [major · causeless_motion]
  - expect: Nothing moves; only the light changes.
  - fail: The set moves; or the light moves by itself; or the lit area wanders.
- P5 [fatal · permanence_count]
  - expect: One light and one set.
  - fail: A second light appears; or the set vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The set's shape and the surroundings stay the same.
  - fail: The set changes shape; or the surroundings rearrange; or the light changes shape.

## OPT-0212 · color_mixing · train

**Caption.** Blue drops are added to a glass of yellow lemonade and swirled, and the drink turns green.

**Expectation (hidden).** Green appears where the blue meets the yellow and spreads until the whole glass is green; the drink does not separate back into yellow and blue.

**Declared violation types.** attribute_drift, process_direction

**SA**
- S1 [core] A glass of yellow lemonade is present.
- S2 [core] Blue drops are added.
- S3 [core] It is swirled.
- S4 [core] The drink turns green.
- S5 [minor] Green appears where the blue meets the yellow and spreads.

**PC**
- P1 [core · process_direction]
  - expect: The green spreads from the drops through the lemonade where the blue meets the yellow, until the whole glass is green and never gathers back; coloured areas stay coloured.
  - fail: The lemonade returns to its original colour where it was green; or the green gathers back into the drops; or the green appears before the drops arrives.
- P2 [core · attribute_drift]
  - expect: The result is green, and un-reached lemonade keeps its original colour.
  - fail: The lemonade turns a colour other than green; or the un-reached lemonade changes; or the green is darker than the drops itself.
- P3 [major · material_response]
  - expect: The lemonade behaves as it should: streaks and swirls where stirred or spread, settling where it flows.
  - fail: The lemonade is rigid and unmarked; or it flows like water when it is a paste; or it bounces like rubber.
- P4 [major · causeless_motion]
  - expect: The lemonade moves only where stirred or where the green flows.
  - fail: The lemonade swirls by itself; or the green spreads faster than stirring or flow carries it; or the container moves.
- P5 [fatal · permanence_count]
  - expect: The amount of lemonade stays the same and the container keeps its shape.
  - fail: The container fills or empties on its own; or a second container appears; or the drops passes through the container.
- P6 [minor · attribute_drift]
  - expect: The container and the background stay the same.
  - fail: The container changes colour; or the background rearranges; or the tool changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0213 · color_mixing · train

**Caption.** A tattoo shop's red neon sign shines on the wet white van parked outside, and the van's side glows pink-red.

**Expectation (hidden).** The van is tinted where the sign's light reaches and white elsewhere; the tint goes when the sign is switched off.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] A white van is parked outside a tattoo shop.
- S2 [core] The shop's red neon sign shines on its wet side.
- S3 [core] The van's side glows pink-red.
- S4 [minor] The van is white where the sign's light does not reach.

**PC**
- P1 [core · attribute_drift]
  - expect: The van looks pink-red only where the sign's light reaches and while it is on.
  - fail: The van is pink-red with the sign off; or stays white under the pink-red light; or turns a different colour from the light.
- P2 [core · missing_consequence]
  - expect: The change happens at the same instant as the sign and is confined to where its light falls.
  - fail: The van changes before the sign; or long after; or surfaces the light cannot reach change too.
- P3 [major · material_response]
  - expect: The wet side shows a shimmering reflection of the sign.
  - fail: The side is dry and matt with a sharp reflection; or the reflection is rigid on rippling water; or the van's paint changes.
- P4 [major · causeless_motion]
  - expect: Nothing moves; only the light changes.
  - fail: The van moves; or the sign moves by itself; or the lit area wanders.
- P5 [fatal · permanence_count]
  - expect: One sign and one van.
  - fail: A second sign appears; or the van vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The van's shape and the surroundings stay the same.
  - fail: The van changes shape; or the surroundings rearrange; or the sign changes shape.

## OPT-0214 · color_mixing · train

**Caption.** A roller of white paint is run over a patch of wet red paint on a wall, and it leaves a pink streak where they blend.

**Expectation (hidden).** Pink appears only along the roller's path through the red; the untouched red stays red and the pink does not turn white again.

**Declared violation types.** attribute_drift, process_direction

**SA**
- S1 [core] A patch of wet red paint is on a wall.
- S2 [core] A roller of white paint is run over it.
- S3 [core] It leaves a pink streak where they blend.
- S4 [minor] The untouched red stays red.

**PC**
- P1 [core · process_direction]
  - expect: Pink appears only along the roller's path through the red and does not turn white again.
  - fail: Pink appears where the roller has not passed; or the streak turns white; or the pink retreats.
- P2 [core · attribute_drift]
  - expect: The blend is pink, and the untouched red stays red.
  - fail: The blend is a colour other than pink; or the untouched red changes; or the white paint stays white over the red.
- P3 [major · material_response]
  - expect: Wet paint smears and blends under the roller.
  - fail: The paints stay as separate hard layers; or the paint flows like water; or the roller passes without marking.
- P4 [major · causeless_motion]
  - expect: Paint moves only where the roller pushes it.
  - fail: Paint runs by itself; or the roller moves by itself; or the wall changes.
- P5 [fatal · permanence_count]
  - expect: One roller and one wall.
  - fail: A second roller appears; or the wall vanishes; or paint appears from nowhere.
- P6 [minor · attribute_drift]
  - expect: The wall and the room stay the same.
  - fail: The wall changes shape; or the room rearranges; or the roller changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0215 · color_mixing · train

**Caption.** Sunset light through a window falls on a white cat, and its fur takes on an orange glow.

**Expectation (hidden).** The fur looks orange only on the side facing the window and while the sunset light lasts; it is white in ordinary light.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] A white cat sits by a window.
- S2 [core] Sunset light falls on it.
- S3 [core] Its fur takes on an orange glow.
- S4 [minor] The glow is on the side facing the window.

**PC**
- P1 [core · attribute_drift]
  - expect: The fur looks orange only where the sunset's light reaches and while it is on.
  - fail: The fur is orange with the sunset off; or stays white under the orange light; or turns a different colour from the light.
- P2 [core · missing_consequence]
  - expect: The change happens at the same instant as the sunset and is confined to where its light falls.
  - fail: The fur changes before the sunset; or long after; or surfaces the light cannot reach change too.
- P3 [major · shape_identity]
  - expect: The cat's shape and fur texture show in orange, not as a colour change of the fur itself.
  - fail: The fur is orange on the side away from the window; or the cat is flat orange with no shading; or the cat changes shape.
- P4 [major · causeless_motion]
  - expect: Nothing moves; only the light changes.
  - fail: The fur moves; or the sunset moves by itself; or the lit area wanders.
- P5 [fatal · permanence_count]
  - expect: One sunset and one fur.
  - fail: A second sunset appears; or the fur vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The fur's shape and the surroundings stay the same.
  - fail: The fur changes shape; or the surroundings rearrange; or the sunset changes shape.

**Note.** The cat is self-driven; only the light on it is judged.

## OPT-0216 · color_mixing · train

**Caption.** A red plastic cup is placed upside down over a phone's white flashlight, and the cup glows red and throws a red circle onto the ceiling.

**Expectation (hidden).** The glow and the circle appear when the cup covers the light and are the cup's colour; they vanish when the cup is lifted or the light is switched off.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] A phone's white flashlight is on.
- S2 [core] A red plastic cup is placed upside down over it.
- S3 [core] The cup glows red.
- S4 [core] It throws a red circle onto the ceiling.
- S5 [minor] The cup goes on first and the glow appears with it.

**PC**
- P1 [core · attribute_drift]
  - expect: The glow and the circle are the cup's red.
  - fail: They are white; or a different colour; or the ceiling circle is white while the cup glows red.
- P2 [core · missing_consequence]
  - expect: The glow and the circle appear when the cup covers the light and would vanish when it is lifted or the light is off.
  - fail: They are there before the cup; or remain after it is lifted; or the cup covers the light and nothing glows.
- P3 [major · shape_identity]
  - expect: The circle is one round patch on the ceiling.
  - fail: It splits; or is a sharp square; or it is on the wall.
- P4 [major · causeless_motion]
  - expect: The cup and phone stay put.
  - fail: The cup slides; or the phone moves; or the circle wanders.
- P5 [fatal · permanence_count]
  - expect: One cup and one phone.
  - fail: The cup duplicates; or the phone vanishes; or the light passes through the table.
- P6 [minor · attribute_drift]
  - expect: The table and the room stay the same.
  - fail: The table changes; or the room rearranges; or the cup changes shape.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0217 · color_mixing · train

**Caption.** A car wash's foaming brushes turn from white to blue when the blue soap is sprayed on, and rinse back to white under clear water.

**Expectation (hidden).** The colour spreads with the soap and washes out with the rinse water running downward; the brushes do not turn blue before the soap arrives.

**Declared violation types.** attribute_drift, process_direction

**SA**
- S1 [core] A car wash's foaming brushes are white.
- S2 [core] Blue soap is sprayed on.
- S3 [core] They turn blue.
- S4 [core] They rinse back to white under clear water.
- S5 [minor] The soap comes first, then the blue, then the rinse.

**PC**
- P1 [core · process_direction]
  - expect: The colour spreads with the soap and washes out with the rinse water running downward.
  - fail: The brushes turn blue before the soap arrives; or stay blue through the rinse; or turn white before the rinse.
- P2 [core · attribute_drift]
  - expect: The brushes are the soap's blue while soaped and white when rinsed.
  - fail: They turn a different colour; or stay white under blue soap; or are blue with no soap.
- P3 [major · gravity_direction]
  - expect: The rinse water runs down the brushes.
  - fail: It runs up; or hangs; or floats.
- P4 [major · material_response]
  - expect: The brushes are soft strands that hold foam and drip.
  - fail: They are rigid rods; or the foam is solid; or the strands melt.
- P5 [fatal · permanence_count]
  - expect: The brushes keep their number.
  - fail: A brush vanishes; or appears; or the soap becomes solid.
- P6 [minor · attribute_drift]
  - expect: The car wash and the car stay the same.
  - fail: The car changes colour; or the bay changes; or the brushes change shape.

## OPT-0218 · color_mixing · train

**Caption.** A red laser dot lands on a white wall, and when it is moved onto a green plant the dot becomes hard to see.

**Expectation (hidden).** The dot is bright red on the white wall and dim on the green leaves; it stays red wherever it lands and moves with the pointer.

**Declared violation types.** attribute_drift, causeless_motion

**SA**
- S1 [core] A red laser dot is on a white wall.
- S2 [core] It is moved onto a green plant.
- S3 [core] The dot becomes hard to see.
- S4 [minor] The dot stays red wherever it lands.

**PC**
- P1 [core · attribute_drift]
  - expect: The dot is bright red on the white wall and dim on the green leaves, and stays red wherever it lands.
  - fail: It is bright on the green leaves; or turns green; or is dim on the white wall.
- P2 [core · causeless_motion]
  - expect: The dot moves with the pointer and only then.
  - fail: It drifts with the pointer still; or stays put while the pointer moves; or leaves a trail.
- P3 [major · shape_identity]
  - expect: The dot is one small spot.
  - fail: It splits; or is a large patch; or changes shape.
- P4 [major · missing_consequence]
  - expect: The dot lands where the pointer aims.
  - fail: It is far from the aim; or appears with no pointer; or two dots from one pointer.
- P5 [fatal · permanence_count]
  - expect: One pointer, one wall and one plant.
  - fail: The plant duplicates; or the wall vanishes; or the dot becomes solid.
- P6 [minor · attribute_drift]
  - expect: The wall and the plant stay the same.
  - fail: The plant changes; or the wall changes colour; or the pointer changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0219 · color_mixing · train

**Caption.** A sheer red scarf is draped over a white lamp, and the room's light turns warm red.

**Expectation (hidden).** The room's light changes as the scarf covers the lamp and returns to white when it is lifted; the scarf glows from within.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] A white lamp lights a room.
- S2 [core] A sheer red scarf is draped over it.
- S3 [core] The room's light turns warm red.
- S4 [minor] The scarf glows from within.
- S5 [minor] The scarf goes on first and the light changes with it.

**PC**
- P1 [core · attribute_drift]
  - expect: The room looks red only where the scarf's light reaches and while it is on.
  - fail: The room is red with the scarf off; or stays white under the red light; or turns a different colour from the light.
- P2 [core · missing_consequence]
  - expect: The change happens at the same instant as the scarf and is confined to where its light falls.
  - fail: The room changes before the scarf; or long after; or surfaces the light cannot reach change too.
- P3 [major · material_response]
  - expect: The scarf is sheer cloth that drapes over the lamp and glows.
  - fail: It is rigid; or opaque so the room goes dark; or it floats.
- P4 [major · causeless_motion]
  - expect: Nothing moves; only the light changes.
  - fail: The room moves; or the scarf moves by itself; or the lit area wanders.
- P5 [fatal · permanence_count]
  - expect: One scarf and one room.
  - fail: A second scarf appears; or the room vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The room's shape and the surroundings stay the same.
  - fail: The room changes shape; or the surroundings rearrange; or the scarf changes shape.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0220 · color_mixing · train

**Caption.** The corner of a white paper towel is dipped into a cup of blue dye, and the blue creeps up the towel.

**Expectation (hidden).** The colour climbs from the wet corner upward and stops advancing when the towel is lifted out; it does not spread from the dry end.

**Declared violation types.** process_direction, attribute_drift

**SA**
- S1 [core] A cup of blue dye is present.
- S2 [core] The corner of a white paper towel is dipped into it.
- S3 [core] The blue creeps up the towel.
- S4 [minor] The colour stops advancing when the towel is lifted out.

**PC**
- P1 [core · process_direction]
  - expect: The colour climbs from the wet corner upward and stops advancing when the towel is lifted out; it does not retreat.
  - fail: It spreads from the dry end; or retreats; or keeps climbing fast after the towel is out.
- P2 [core · attribute_drift]
  - expect: The wet part is the dye's blue and the dry part stays white.
  - fail: The wet part is a different colour; or the dry part changes; or the whole towel turns blue at once.
- P3 [major · material_response]
  - expect: The towel is absorbent paper that darkens where wet.
  - fail: The dye beads off it; or the towel dissolves; or it stays dry in the cup.
- P4 [major · causeless_motion]
  - expect: The towel moves only with the hand.
  - fail: It dips itself; or floats; or jumps.
- P5 [fatal · permanence_count]
  - expect: One towel and one cup.
  - fail: The towel duplicates; or the cup vanishes; or dye appears from nowhere.
- P6 [minor · attribute_drift]
  - expect: The cup and the table stay the same.
  - fail: The cup changes colour; or the table changes; or the dye changes colour.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0221 · color_mixing · train

**Caption.** A clear-cut crystal pendant is turned in sunlight, and coloured sparkles dance across the ceiling.

**Expectation (hidden).** The sparkles move as the pendant turns and disappear when it is put down or the sun goes in.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A clear-cut crystal pendant is turned in sunlight.
- S2 [core] Coloured sparkles dance across the ceiling.
- S3 [minor] The sparkles disappear when the pendant is put down or the sun goes in.

**PC**
- P1 [core · missing_consequence]
  - expect: The sparkles move as the pendant turns and would disappear if it were put down or the sun went in.
  - fail: They stay put while the pendant turns; or are there with no sun; or the pendant turns in sun with no sparkles.
- P2 [core · causeless_motion]
  - expect: The sparkles do not move on their own.
  - fail: They dance with the pendant still; or flicker in steady sun; or drift.
- P3 [major · attribute_drift]
  - expect: The sparkles are rainbow-coloured.
  - fail: They are all white; or a single colour; or change colour with nothing moving.
- P4 [major · shape_identity]
  - expect: The sparkles are many small spots.
  - fail: They merge into one flood; or are large squares; or a single spot.
- P5 [fatal · permanence_count]
  - expect: One pendant.
  - fail: It duplicates; or vanishes; or a sparkle becomes solid.
- P6 [minor · attribute_drift]
  - expect: The room stays the same.
  - fail: Furniture rearranges; or the ceiling changes; or the pendant changes shape.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0222 · color_mixing · train

**Caption.** Grenadine is poured into a glass of orange juice, and the red sinks and spreads through the bottom of the glass while the top stays orange.

**Expectation (hidden).** The red drops through the juice and gathers low, blending into a red-orange band; it does not float on top or stay a separate blob.

**Declared violation types.** process_direction, gravity_direction, attribute_drift

**SA**
- S1 [core] A glass of orange juice is present.
- S2 [core] Grenadine is poured in.
- S3 [core] The red sinks and spreads through the bottom of the glass.
- S4 [core] The top stays orange.
- S5 [minor] The pour comes first and the sinking follows.

**PC**
- P1 [core · gravity_direction]
  - expect: The red drops through the juice and gathers low.
  - fail: It floats on top; or hangs in the middle; or rises after sinking.
- P2 [core · process_direction]
  - expect: The red band at the bottom grows while pouring and blends into red-orange at its edge; it does not stay a separate blob.
  - fail: It stays a sharp blob; or the layers swap; or the red vanishes.
- P3 [major · attribute_drift]
  - expect: The bottom is red to red-orange and the top stays orange.
  - fail: The whole glass turns red at once; or the top turns red first; or the mix is a colour other than red-orange.
- P4 [major · material_response]
  - expect: Both are liquids that mix at their boundary.
  - fail: The grenadine is a solid lump; or beads bounce; or the juice is rigid.
- P5 [fatal · permanence_count]
  - expect: One glass, and grenadine comes only from the pour.
  - fail: Red appears with no pour; or the glass duplicates; or liquid passes through the glass.
- P6 [minor · attribute_drift]
  - expect: The glass and the table stay the same.
  - fail: The glass changes shape; or the table changes; or the juice changes colour abruptly.

## OPT-0223 · color_mixing · train

**Caption.** A stripe of translucent blue watercolour is painted over a dry yellow stripe, and the overlap looks green.

**Expectation (hidden).** Only the overlapping band is green; the yellow and blue outside the overlap keep their colours.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] A dry yellow stripe is on paper.
- S2 [core] A stripe of translucent blue watercolour is painted over it.
- S3 [core] The overlap looks green.
- S4 [minor] The yellow and blue outside the overlap keep their colours.

**PC**
- P1 [core · attribute_drift]
  - expect: Only the overlapping band is green, and the yellow and blue outside it keep their colours.
  - fail: The overlap is a colour other than green; or the pure stripes change; or the whole sheet turns green.
- P2 [core · missing_consequence]
  - expect: The green appears as the blue is painted over the yellow and only there.
  - fail: Green appears before the brush arrives; or where the stripes do not cross; or the brush passes and no green appears.
- P3 [major · material_response]
  - expect: The watercolour is translucent and lies as a wash on the dry paper.
  - fail: It is opaque and hides the yellow; or it beads off; or the paper dissolves.
- P4 [major · causeless_motion]
  - expect: Paint goes only where the brush puts it.
  - fail: It spreads by itself on dry paper; or the brush moves by itself; or the paper moves.
- P5 [fatal · permanence_count]
  - expect: One sheet and one brush.
  - fail: The sheet duplicates; or the brush vanishes; or paint appears from nowhere.
- P6 [minor · attribute_drift]
  - expect: The paper and the table stay the same.
  - fail: The paper changes shape; or the table changes; or the brush changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0224 · color_mixing · train

**Caption.** Sunlight enters a room through a red balloon held up to the window, and a soft red glow falls on the white wall behind it.

**Expectation (hidden).** The glow is on the side away from the window and moves with the balloon; the wall is white when the balloon is lowered.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] A red balloon is held up to a window.
- S2 [core] Sunlight enters through it.
- S3 [core] A soft red glow falls on the white wall behind it.
- S4 [minor] The glow is on the side away from the window.
- S5 [minor] The glow moves with the balloon.

**PC**
- P1 [core · attribute_drift]
  - expect: The wall looks red only where the balloon's light reaches and while it is on.
  - fail: The wall is red with the balloon off; or stays white under the red light; or turns a different colour from the light.
- P2 [core · missing_consequence]
  - expect: The change happens at the same instant as the balloon and is confined to where its light falls.
  - fail: The wall changes before the balloon; or long after; or surfaces the light cannot reach change too.
- P3 [major · shape_identity]
  - expect: The glow is one soft patch roughly the balloon's shape.
  - fail: It splits; or is a sharp square; or floods the wall.
- P4 [major · causeless_motion]
  - expect: Nothing moves; only the light changes.
  - fail: The wall moves; or the balloon moves by itself; or the lit area wanders.
- P5 [fatal · permanence_count]
  - expect: One balloon and one wall.
  - fail: A second balloon appears; or the wall vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The wall's shape and the surroundings stay the same.
  - fail: The wall changes shape; or the surroundings rearrange; or the balloon changes shape.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0225 · color_mixing · train

**Caption.** A spoonful of matcha powder is stirred into a glass of milk, and the milk turns pale green.

**Expectation (hidden).** Green swirls spread from the spoon and even out; the milk does not return to white.

**Declared violation types.** attribute_drift, process_direction

**SA**
- S1 [core] A glass of milk is present.
- S2 [core] A spoonful of matcha powder is stirred in.
- S3 [core] The milk turns pale green.
- S4 [minor] Green swirls spread from the spoon and even out.

**PC**
- P1 [core · process_direction]
  - expect: The pale green spreads from the spoon through the milk in swirls from the spoon, evening out and never gathers back; coloured areas stay coloured.
  - fail: The milk returns to its original colour where it was pale green; or the pale green gathers back into the spoon; or the pale green appears before the spoon arrives.
- P2 [core · attribute_drift]
  - expect: The result is pale green, and un-reached milk keeps its original colour.
  - fail: The milk turns a colour other than pale green; or the un-reached milk changes; or the pale green is darker than the spoon itself.
- P3 [major · material_response]
  - expect: The milk behaves as it should: streaks and swirls where stirred or spread, settling where it flows.
  - fail: The milk is rigid and unmarked; or it flows like water when it is a paste; or it bounces like rubber.
- P4 [major · causeless_motion]
  - expect: The milk moves only where stirred or where the pale green flows.
  - fail: The milk swirls by itself; or the pale green spreads faster than stirring or flow carries it; or the container moves.
- P5 [fatal · permanence_count]
  - expect: The amount of milk stays the same and the container keeps its shape.
  - fail: The container fills or empties on its own; or a second container appears; or the spoon passes through the container.
- P6 [minor · attribute_drift]
  - expect: The container and the background stay the same.
  - fail: The container changes colour; or the background rearranges; or the tool changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0226 · color_mixing · train

**Caption.** A concert's lights switch from blue to red, and the white smoke over the stage changes from blue to red at the same instant.

**Expectation (hidden).** The smoke shows the colour of whatever light is on it and changes with the lights; unlit smoke is grey.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] White smoke hangs over a concert stage.
- S2 [core] The lights switch from blue to red.
- S3 [core] The smoke changes from blue to red at the same instant.
- S4 [minor] Unlit smoke is grey.

**PC**
- P1 [core · attribute_drift]
  - expect: The smoke shows the colour of whatever light is on it and unlit smoke is grey.
  - fail: The smoke is white under coloured lights; or glows with the lights off; or is a colour the lights do not show.
- P2 [core · missing_consequence]
  - expect: The smoke changes colour at the same instant as the lights.
  - fail: It changes before the lights; or long after; or the lights change and the smoke does not.
- P3 [major · material_response]
  - expect: The smoke is diffuse and drifts.
  - fail: It is a solid shape; or rigid; or it drops like liquid.
- P4 [major · causeless_motion]
  - expect: The smoke drifts slowly and does not jump.
  - fail: It jumps; or whips about in still air; or vanishes at once.
- P5 [fatal · permanence_count]
  - expect: One stage and its lights.
  - fail: The stage duplicates; or the lights vanish; or the smoke becomes solid.
- P6 [minor · attribute_drift]
  - expect: The stage and the set stay the same.
  - fail: The set rearranges; or the stage changes; or the lights change shape.

## OPT-0227 · color_mixing · train

**Caption.** A rainbow over a field is fading as the rain moves away and the sky clears.

**Expectation (hidden).** The rainbow appears opposite the sun, keeps its arc shape while visible, and fades gradually; it does not move across the sky or become brighter as the rain ends.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A rainbow arches over a field.
- S2 [core] It is fading as the rain moves away and the sky clears.
- S3 [minor] The rainbow keeps its arc shape while visible.
- S4 [minor] The rainbow is opposite the sun.

**PC**
- P1 [core · process_direction]
  - expect: The rainbow fades gradually and does not brighten as the rain ends.
  - fail: It brightens; or fades and returns; or vanishes in an instant.
- P2 [core · permanence_count]
  - expect: The rainbow keeps its arc shape and place while visible and does not move across the sky.
  - fail: It moves across the sky; or changes shape; or a second rainbow appears as it fades.
- P3 [major · attribute_drift]
  - expect: The bands show the spectrum's order.
  - fail: They are in random order; or a single colour; or the colours change.
- P4 [major · causeless_motion]
  - expect: The field and the clouds move only with the wind.
  - fail: The field changes; or the clouds jump; or the rainbow swings.
- P5 [fatal · shape_identity]
  - expect: The field and the sky keep their layout.
  - fail: The horizon changes; or the field rearranges; or the rainbow becomes solid.
- P6 [minor · attribute_drift]
  - expect: The field's colours stay the same.
  - fail: The grass changes colour; or the trees change; or the sky changes colour abruptly.

