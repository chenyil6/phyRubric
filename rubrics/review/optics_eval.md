# Rubric review

50 rubrics. SA = caption adherence (core/minor); PC = physics (fatal/core/major/minor, each tagged with a violation type). Expectation is the hidden field from data/, shown for the reviewer only.

# Optics

## OPT-0251 · shadow · eval

**Caption.** A rowing boat drifts across a clear shallow bay in sunshine, and its shadow slides along the sandy bottom beneath it.

**Expectation (hidden).** The shadow lies on the sea floor on the side away from the sun, keeps the boat's outline, and moves with the boat; it does not lag behind, float on the surface, or point toward the sun.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A rowing boat drifts across a clear shallow bay in sunshine.
- S2 [core] Its shadow slides along the sandy bottom beneath it.
- S3 [minor] The shadow keeps the boat's outline.
- S4 [minor] The shadow lies on the side away from the sun.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow lies on the sea floor away from the sun and moves with the boat.
  - fail: It lags behind; or floats on the surface; or points toward the sun.
- P2 [core · shape_identity]
  - expect: The shadow keeps the boat's outline.
  - fail: It is a different shape; or splits; or is a plain blob.
- P3 [major · causeless_motion]
  - expect: The shadow does not move on its own.
  - fail: It moves with the boat still; or drifts across the sand by itself.
- P4 [major · gravity_direction]
  - expect: The boat floats at the surface and the shadow lies on the bottom.
  - fail: The boat sinks; or the shadow rises off the sand; or the boat lifts out of the water.
- P5 [fatal · permanence_count]
  - expect: One boat and one shadow.
  - fail: A second boat or shadow appears; or the boat vanishes; or the shadow becomes solid.
- P6 [minor · attribute_drift]
  - expect: The boat and the bay stay the same, and the shadow stays dark.
  - fail: The boat changes colour; or the shadow turns coloured; or the sand changes.

## OPT-0252 · shadow · eval

**Caption.** Steam rises from a kettle spout in a sunlit kitchen, and a faint, shifting shadow of the plume drifts on the wall behind it.

**Expectation (hidden).** The shadow is on the side of the plume away from the window, moves and thins as the steam does, and is fainter than the kettle's own shadow; it does not appear on the sunlit side or stay still while the steam moves.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] Steam rises from a kettle spout in a sunlit kitchen.
- S2 [core] A faint, shifting shadow of the plume drifts on the wall behind it.
- S3 [minor] The shadow is fainter than the kettle's own shadow.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow is on the side of the plume away from the window and moves and thins as the steam does.
  - fail: It is on the sunlit side; or stays still while the steam moves; or it is as dark as the kettle's shadow.
- P2 [core · causeless_motion]
  - expect: The shadow moves only as the steam moves.
  - fail: It drifts with the steam still; or moves before the plume; or lingers after the steam has gone.
- P3 [major · gravity_direction]
  - expect: The steam rises.
  - fail: It sinks; or hangs; or flows sideways with no draught.
- P4 [major · shape_identity]
  - expect: The shadow is a soft shifting wisp like the plume.
  - fail: It is a hard-edged shape; or splits into unrelated pieces; or is a solid block.
- P5 [fatal · permanence_count]
  - expect: One kettle and one plume.
  - fail: A second kettle appears; or the plume comes from nowhere; or the shadow becomes solid.
- P6 [minor · attribute_drift]
  - expect: The kettle and the wall stay the same, and the shadow stays dark.
  - fail: The kettle changes colour; or the shadow turns coloured; or the wall changes.

## OPT-0253 · shadow · eval

**Caption.** A sunlit glass door swings open, and the shadow of its frame sweeps across the floor as it turns.

**Expectation (hidden).** The frame's shadow turns with the door and stays attached to the hinge side; the glass panes cast little shadow while the frame casts a dark one; the shadow does not move before the door does.

**Declared violation types.** causeless_motion, shape_identity

**SA**
- S1 [core] A sunlit glass door swings open.
- S2 [core] The shadow of its frame sweeps across the floor as it turns.
- S3 [minor] The glass panes cast little shadow while the frame casts a dark one.
- S4 [minor] The door moves first and the shadow follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The frame's shadow turns with the door and does not move before the door does.
  - fail: It moves before the door; or stays still while the door swings; or swings the opposite way.
- P2 [core · shape_identity]
  - expect: The frame casts a dark shadow and the panes cast little, and the shadow stays attached at the hinge side.
  - fail: The panes cast solid dark shadow; or the shadow detaches from the hinge; or it is a different shape from the frame.
- P3 [major · missing_consequence]
  - expect: The shadow lies on the floor away from the sun.
  - fail: It lies toward the sun; or on the ceiling; or it is missing in sunlight.
- P4 [major · trajectory_momentum]
  - expect: The door swings in an arc on its hinges.
  - fail: It slides; or lifts; or spins.
- P5 [fatal · permanence_count]
  - expect: One door and one shadow.
  - fail: A second door appears; or the shadow becomes solid; or the door passes through the frame.
- P6 [minor · attribute_drift]
  - expect: The door and the floor stay the same, and the shadow stays dark.
  - fail: The frame changes colour; or the shadow turns coloured; or the floor changes.

## OPT-0254 · shadow · eval

**Caption.** An upside-down bicycle's front wheel is spun in front of a wall lit by a lamp, and the shadows of its spokes whirl across the wall.

**Expectation (hidden).** The spoke shadows turn in step with the wheel and slow as it slows; the rim's shadow stays put while the spokes' shadows move; the shadows fall on the side of the wheel away from the lamp.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] An upside-down bicycle's front wheel is spun in front of a wall lit by a lamp.
- S2 [core] The shadows of its spokes whirl across the wall.
- S3 [minor] The rim's shadow stays put while the spokes' shadows move.
- S4 [minor] The spin comes first and the whirl follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The spoke shadows turn in step with the wheel and slow as it slows.
  - fail: They are still while the wheel turns; or keep whirling after it stops; or turn the opposite way.
- P2 [core · causeless_motion]
  - expect: The shadows move only as the wheel moves, and the rim's shadow stays put.
  - fail: The rim's shadow moves; or the spokes' shadows move with the wheel still; or the shadows drift.
- P3 [major · missing_consequence]
  - expect: The shadows fall on the side away from the lamp.
  - fail: They fall toward the lamp; or on the ceiling; or are missing with the lamp on.
- P4 [major · shape_identity]
  - expect: The shadows are thin spoke lines radiating from the hub.
  - fail: They are unrelated shapes; or merge into a solid disc while the spokes are plainly separate; or there are more than the spokes.
- P5 [fatal · permanence_count]
  - expect: One bicycle and one lamp.
  - fail: A second wheel appears; or the lamp vanishes; or a shadow becomes solid.
- P6 [minor · attribute_drift]
  - expect: The bicycle and the wall stay the same, and the shadows stay dark.
  - fail: The frame changes colour; or the shadows turn coloured; or the wall changes.

**Note.** The hand spinning the wheel is the minimal trigger; the person is not judged.

## OPT-0255 · shadow · eval

**Caption.** A parked bicycle casts a sharp shadow on a sunny wall, and a passing cloud makes the shadow fade and then return.

**Expectation (hidden).** The shadow softens and vanishes as the cloud covers the sun and comes back in the same place when the sun returns; the bike does not move.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A parked bicycle casts a sharp shadow on a sunny wall.
- S2 [core] A cloud passes.
- S3 [core] The shadow fades.
- S4 [core] It returns.
- S5 [minor] The cloud comes first, then the fade, then the return.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow softens and vanishes as the cloud covers the sun and comes back in the same place when the sun returns.
  - fail: It stays sharp with the sun covered; or returns in a different place; or fades with the sun still shining.
- P2 [core · process_direction]
  - expect: The fade and return follow the cloud smoothly.
  - fail: The shadow flickers; or snaps off and on; or fades and never returns in sunlight.
- P3 [major · causeless_motion]
  - expect: The bike does not move.
  - fail: It rolls; or tips; or its shadow moves while it stands.
- P4 [major · shape_identity]
  - expect: The returned shadow is the same bicycle outline.
  - fail: It is a different shape; or splits; or is missing the wheels.
- P5 [fatal · permanence_count]
  - expect: One bicycle and one shadow.
  - fail: A second bicycle appears; or the shadow becomes solid; or the bike vanishes.
- P6 [minor · attribute_drift]
  - expect: The bicycle and the wall stay the same, and the shadow stays dark.
  - fail: The bike changes colour; or the shadow turns coloured; or the wall changes.

## OPT-0256 · shadow · eval

**Caption.** A vase on a table is lit by two lamps from different sides and casts two shadows; one lamp is switched off, and the shadow on the far side of that lamp vanishes while the other stays.

**Expectation (hidden).** Each shadow lies away from its own lamp; when one lamp goes off, only the shadow opposite it disappears and the remaining shadow does not move or darken; the vase itself stays lit by the other lamp.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A vase on a table is lit by two lamps from different sides.
- S2 [core] It casts two shadows.
- S3 [core] One lamp is switched off.
- S4 [core] The shadow on the far side of that lamp vanishes while the other stays.
- S5 [minor] The switch comes first and the shadow vanishes with it.

**PC**
- P1 [core · missing_consequence]
  - expect: Each shadow lies away from its own lamp, and when one lamp goes off only the shadow opposite it disappears.
  - fail: Both shadows vanish; or the wrong shadow vanishes; or both remain with one lamp off.
- P2 [core · permanence_count]
  - expect: The remaining shadow does not move or darken, and the vase stays lit by the other lamp.
  - fail: The remaining shadow moves; or the vase goes dark; or a new shadow appears.
- P3 [major · shape_identity]
  - expect: Each shadow keeps the vase's outline.
  - fail: A shadow is a different shape; or splits; or the two merge.
- P4 [major · causeless_motion]
  - expect: The vase and lamps stay put.
  - fail: The vase slides; or a lamp moves by itself; or a shadow drifts.
- P5 [fatal · permanence_count]
  - expect: One vase and two lamps.
  - fail: The vase duplicates; or a lamp vanishes; or a shadow becomes solid.
- P6 [minor · attribute_drift]
  - expect: The vase and the table stay the same, and the shadows stay dark.
  - fail: The vase changes colour; or a shadow turns coloured; or the table changes.

## OPT-0257 · shadow · eval

**Caption.** A garden parasol is tilted in bright sun, and its round shadow slides across the patio.

**Expectation (hidden).** The shadow moves in the direction opposite to the tilt of the canopy and stays on the side away from the sun; it keeps roughly its round shape and does not detach from the pole's base.

**Declared violation types.** causeless_motion, shape_identity

**SA**
- S1 [core] A garden parasol is tilted in bright sun.
- S2 [core] Its round shadow slides across the patio.
- S3 [minor] The shadow keeps roughly its round shape.
- S4 [minor] The tilt comes first and the slide follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The shadow moves only as the canopy tilts.
  - fail: It slides with the parasol still; or moves before the tilt; or keeps moving after.
- P2 [core · shape_identity]
  - expect: The shadow keeps roughly its round shape and does not detach from the pole's base.
  - fail: It becomes a different shape; or detaches from the pole; or splits.
- P3 [major · missing_consequence]
  - expect: The shadow moves opposite to the tilt of the canopy and stays on the side away from the sun.
  - fail: It moves the same way as the tilt; or lies toward the sun; or it is missing in sunlight.
- P4 [major · material_response]
  - expect: The canopy is taut fabric on ribs.
  - fail: It is rigid like a plate; or floats off; or tears.
- P5 [fatal · permanence_count]
  - expect: One parasol and one shadow.
  - fail: A second shadow appears; or the parasol vanishes; or the shadow becomes solid.
- P6 [minor · attribute_drift]
  - expect: The parasol and the patio stay the same, and the shadow stays dark.
  - fail: The canopy changes colour; or the shadow turns coloured; or the patio changes.

**Note.** The hand tilting is the minimal trigger; the person is not judged.

## OPT-0258 · shadow · eval

**Caption.** A cat sits on a sunny fence, jumps down, and its shadow leaves the fence and lands with it on the ground.

**Expectation (hidden).** The shadow stays on the surfaces below the cat, separates during the jump, and rejoins at the paws on landing.

**Declared violation types.** missing_consequence, gravity_direction

**SA**
- S1 [core] A cat sits on a sunny fence.
- S2 [core] It jumps down.
- S3 [core] Its shadow leaves the fence and lands with it on the ground.
- S4 [minor] The shadow separates during the jump and rejoins at the paws on landing.

**PC**
- P1 [core · missing_consequence]
  - expect: The shadow stays on the surfaces below the cat, separates during the jump, and rejoins at the paws on landing.
  - fail: It rises with the cat; or stays attached in mid-air; or fails to rejoin on landing.
- P2 [core · gravity_direction]
  - expect: The cat comes down to the ground and stays.
  - fail: It hangs in the air; or rises; or bounces back onto the fence.
- P3 [major · shape_identity]
  - expect: The shadow keeps the cat's outline.
  - fail: It is a different shape; or splits; or vanishes in mid-jump.
- P4 [major · missing_consequence]
  - expect: The shadow lies on the side away from the sun.
  - fail: It lies toward the sun; or switches sides; or it is missing in sunlight.
- P5 [fatal · permanence_count]
  - expect: One cat and one shadow.
  - fail: A second cat or shadow appears; or the cat vanishes; or the shadow becomes solid.
- P6 [minor · attribute_drift]
  - expect: The cat's markings and the fence stay the same, and the shadow stays dark.
  - fail: The markings change; or the shadow turns coloured; or the fence changes.

**Note.** Self-driven animal: where it goes is not judged. Only the shadow's relation to it is.

## OPT-0259 · shadow · eval

**Caption.** A spotlight is swung across a statue on a plinth, and the statue's shadow on the backdrop swings the opposite way.

**Expectation (hidden).** The shadow moves in the direction opposite to the light's movement and always falls away from the spotlight; it stretches when the light is low and shrinks when the light is overhead.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A statue stands on a plinth in front of a backdrop.
- S2 [core] A spotlight is swung across it.
- S3 [core] The statue's shadow on the backdrop swings the opposite way.
- S4 [minor] The light moves first and the shadow follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The shadow moves only as the light moves.
  - fail: It swings with the light still; or before the light; or keeps swinging after.
- P2 [core · missing_consequence]
  - expect: The shadow moves opposite to the light's movement and always falls away from the spotlight.
  - fail: It moves the same way as the light; or falls toward the spotlight; or stays fixed while the light swings.
- P3 [major · shape_identity]
  - expect: The shadow keeps the statue's outline, stretching when the light is low and shrinking when overhead.
  - fail: It is a different shape; or one length throughout; or splits.
- P4 [major · causeless_motion]
  - expect: The statue stays still.
  - fail: It turns; or slides; or lifts.
- P5 [fatal · permanence_count]
  - expect: One statue, one spotlight and one shadow.
  - fail: A second shadow appears; or the statue vanishes; or the shadow becomes solid.
- P6 [minor · attribute_drift]
  - expect: The statue and the backdrop stay the same, and the shadow stays dark.
  - fail: The statue changes colour; or the shadow turns coloured; or the backdrop changes.

## OPT-0260 · shadow · eval

**Caption.** A hot-air balloon drifts low over a field in the morning sun, and its huge shadow glides across the crops below.

**Expectation (hidden).** The shadow moves with the balloon, lies on the side away from the low sun, and is stretched by the low light; it does not fall directly beneath the balloon or stay behind.

**Declared violation types.** causeless_motion, shape_identity

**SA**
- S1 [core] A hot-air balloon drifts low over a field in the morning sun.
- S2 [core] Its huge shadow glides across the crops below.
- S3 [minor] The shadow is stretched by the low light.
- S4 [minor] The shadow lies on the side away from the sun.

**PC**
- P1 [core · causeless_motion]
  - expect: The shadow moves with the balloon and only then.
  - fail: It stays behind while the balloon drifts; or moves with the balloon still; or jumps.
- P2 [core · shape_identity]
  - expect: The shadow keeps the balloon's outline, stretched by the low sun.
  - fail: It is a different shape; or a small round spot under a plainly low sun; or splits.
- P3 [major · missing_consequence]
  - expect: The shadow lies on the side away from the low sun, not directly beneath.
  - fail: It lies toward the sun; or directly beneath under a low sun; or it is missing in sunlight.
- P4 [major · gravity_direction]
  - expect: The balloon drifts gently and the shadow lies on the ground.
  - fail: The balloon drops like a stone; or the shadow stands up off the crops; or the balloon shoots up.
- P5 [fatal · permanence_count]
  - expect: One balloon and one shadow.
  - fail: A second balloon or shadow appears; or the balloon vanishes; or the shadow becomes solid.
- P6 [minor · attribute_drift]
  - expect: The balloon's colours and the field stay the same, and the shadow stays dark.
  - fail: The balloon changes colour; or the shadow turns coloured; or the crops change.

## OPT-0261 · reflection · eval

**Caption.** A bird lands on the edge of a car's side mirror, and its reflection appears in the glass and moves in step with it.

**Expectation (hidden).** The reflection appears the moment the bird is in front of the mirror, moves at the same instant as the bird, and is mirrored; it does not lag or stay after the bird flies off.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A bird lands on the edge of a car's side mirror.
- S2 [core] Its reflection appears in the glass.
- S3 [core] The reflection moves in step with the bird.
- S4 [minor] The reflection is mirrored.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflection appears the moment the bird is in front of the mirror and moves at the same instant as the bird.
  - fail: It lags; or appears before the bird arrives; or stays after the bird flies off.
- P2 [core · permanence_count]
  - expect: There is one bird and one reflection, and the reflection stays in the glass.
  - fail: A second bird appears; or the reflection steps out; or the bird vanishes.
- P3 [major · shape_identity]
  - expect: The reflection is a mirror image of the bird.
  - fail: It is a different bird; or not mirrored; or upside down.
- P4 [major · material_response]
  - expect: The mirror is rigid: the reflection is undistorted.
  - fail: It ripples; or warps; or bends.
- P5 [fatal · shape_identity]
  - expect: The bird keeps its wings and shape.
  - fail: A wing detaches; or the bird splits; or merges with the mirror.
- P6 [minor · attribute_drift]
  - expect: The plumage and the car stay the same.
  - fail: The plumage changes; or the car changes colour; or the mirror housing changes.

**Note.** Self-driven animal: where it goes is not judged. Only the reflection's relation to it is.

## OPT-0262 · reflection · eval

**Caption.** A dog trots along a jetty over a still lake, and its upside-down reflection trots beneath it in the water.

**Expectation (hidden).** The reflection is inverted, joined to the jetty's reflection at the waterline, and moves with the dog; it blurs only where a ripple passes.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A dog trots along a jetty over a still lake.
- S2 [core] Its upside-down reflection trots beneath it in the water.
- S3 [minor] The reflection is joined to the jetty's reflection at the waterline.
- S4 [minor] The reflection blurs only where a ripple passes.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflection moves with the dog and blurs only where a ripple passes.
  - fail: It stays still while the dog trots; or is blurred on flat water; or sharp across plain ripples.
- P2 [core · shape_identity]
  - expect: The reflection is inverted and joined to the jetty's reflection at the waterline.
  - fail: It is upright; or detached from the jetty's reflection; or a different dog.
- P3 [major · causeless_motion]
  - expect: The reflection does not move on its own.
  - fail: It moves with the dog still; or drifts across the lake.
- P4 [major · material_response]
  - expect: The water is liquid: ripples pass and fade.
  - fail: It is rigid; or ripples freeze; or the water leaps.
- P5 [fatal · permanence_count]
  - expect: One dog and one reflection; the reflection stays on the water.
  - fail: A second dog appears; or the reflection rises off the water; or the dog vanishes.
- P6 [minor · attribute_drift]
  - expect: The dog's coat and the jetty stay the same.
  - fail: The coat changes; or the jetty changes; or the water changes colour.

**Note.** Self-driven animal: where it goes is not judged. Only the reflection's relation to it is.

## OPT-0263 · reflection · eval

**Caption.** A dog barks at its own reflection in a shop window, and the reflected dog barks back, faint over the goods on display behind the glass.

**Expectation (hidden).** The reflected dog moves at the same instant and is mirrored; it is fainter than the real dog and overlaps the display behind the glass; it does not move on its own.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A dog barks at its own reflection in a shop window.
- S2 [core] The reflected dog barks back.
- S3 [minor] The reflection is faint over the goods on display behind the glass.
- S4 [minor] The reflection is mirrored.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflected dog moves at the same instant as the real one.
  - fail: It moves first or later; or stays still while the dog barks; or barks while the dog is still.
- P2 [core · causeless_motion]
  - expect: The reflection does not move on its own.
  - fail: It moves while the dog sits still; or turns away by itself; or slides across the glass.
- P3 [major · shape_identity]
  - expect: The reflection is a mirror image, fainter than the real dog, overlapping the display.
  - fail: It is a different dog; or brighter than the real one; or it hides the display completely; or it is a rotated copy.
- P4 [major · material_response]
  - expect: The pane is flat and rigid.
  - fail: It ripples; or warps; or bends.
- P5 [fatal · permanence_count]
  - expect: One dog and one reflection; the reflection stays in the glass.
  - fail: A second dog appears; or the reflection steps out; or the dog passes into the glass.
- P6 [minor · attribute_drift]
  - expect: The dog's coat and the display stay the same.
  - fail: The coat changes; or the goods rearrange; or the frame changes.

**Note.** Self-driven animal: where it goes is not judged. Only the reflection's relation to it is. Mirror geometry: each point of the image lies directly across the surface from the real point, so the image is a mirror copy, not a rotated one.

## OPT-0264 · reflection · eval

**Caption.** A phone lying on a coffee table lights up, and its glowing reflection appears in the dark television screen facing it.

**Expectation (hidden).** The reflection appears at the instant the phone lights and disappears when it goes dark; it is mirrored and dimmer than the phone; nothing appears in the screen before the phone lights.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A phone lies on a coffee table.
- S2 [core] It lights up.
- S3 [core] Its glowing reflection appears in the dark television screen facing it.
- S4 [minor] The reflection is dimmer than the phone.
- S5 [minor] The phone lights first and the reflection appears with it.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflection appears at the instant the phone lights and would disappear when it goes dark.
  - fail: It appears before the phone lights; or stays after it goes dark; or the phone lights and no reflection appears.
- P2 [core · permanence_count]
  - expect: Nothing appears in the screen before the phone lights, and there is one reflection.
  - fail: A glow is in the screen before; or two reflections; or the reflection comes out of the screen.
- P3 [major · shape_identity]
  - expect: The reflection is a mirror image of the phone, dimmer.
  - fail: It is brighter than the phone; or a different shape; or not mirrored.
- P4 [major · causeless_motion]
  - expect: The phone and the screen stay put.
  - fail: The phone slides; or the screen turns; or the reflection drifts.
- P5 [fatal · permanence_count]
  - expect: One phone and one television.
  - fail: A second phone appears; or the television vanishes; or the phone passes into the screen.
- P6 [minor · attribute_drift]
  - expect: The table and the room stay the same.
  - fail: The table changes; or the room rearranges; or the television changes.

## OPT-0265 · reflection · eval

**Caption.** A bird flies over a puddle, and its reflection crosses the puddle upside down and leaves at the puddle's edge.

**Expectation (hidden).** The reflected bird appears only within the puddle, inverted, and moves in step with the real bird; it does not continue onto the dry pavement.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A bird flies over a puddle.
- S2 [core] Its reflection crosses the puddle upside down.
- S3 [core] The reflection leaves at the puddle's edge.
- S4 [minor] The reflection appears only within the puddle.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflected bird appears only within the puddle and moves in step with the real bird.
  - fail: It continues onto dry pavement; or lags; or is missing over plainly still water.
- P2 [core · shape_identity]
  - expect: The reflection is inverted and the same bird.
  - fail: It is upright; or a different bird; or a rotated copy.
- P3 [major · causeless_motion]
  - expect: The reflection does not move on its own.
  - fail: It moves with the bird hovering; or drifts across the puddle.
- P4 [major · material_response]
  - expect: The puddle is liquid: the reflection wavers where the surface is disturbed.
  - fail: It is rigid; or wavers on a flat calm; or the water flows uphill.
- P5 [fatal · permanence_count]
  - expect: One bird and one reflection.
  - fail: A second bird appears; or the reflection rises off the water; or the bird vanishes.
- P6 [minor · attribute_drift]
  - expect: The plumage and the pavement stay the same.
  - fail: The plumage changes; or the pavement changes; or the puddle moves.

**Note.** Self-driven animal: where it goes is not judged. Only the reflection's relation to it is.

## OPT-0266 · reflection · eval

**Caption.** A mirrored wardrobe door swings shut, and the reflected room sweeps across the mirror until it shows only the wall.

**Expectation (hidden).** The scene in the mirror slides smoothly as the door turns and changes to whatever the mirror faces; it does not stay fixed on one view.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A mirrored wardrobe door swings shut.
- S2 [core] The reflected room sweeps across the mirror.
- S3 [core] The mirror ends up showing only the wall.
- S4 [minor] The door moves first and the view sweeps with it.

**PC**
- P1 [core · missing_consequence]
  - expect: The scene in the mirror slides smoothly as the door turns and changes to whatever the mirror faces.
  - fail: It stays fixed on one view; or jumps; or shows the room when the mirror faces the wall.
- P2 [core · causeless_motion]
  - expect: The view changes only while the door moves.
  - fail: It sweeps with the door still; or before the door moves; or keeps moving after the door stops.
- P3 [major · shape_identity]
  - expect: The reflected room is the real room, mirrored.
  - fail: It is a different room; or not mirrored; or objects appear that are not there.
- P4 [major · trajectory_momentum]
  - expect: The door swings in an arc on its hinges.
  - fail: It slides; or lifts; or spins.
- P5 [fatal · permanence_count]
  - expect: One door and one mirror.
  - fail: A second door appears; or the mirror vanishes; or the reflection becomes solid.
- P6 [minor · attribute_drift]
  - expect: The wardrobe and the room stay the same.
  - fail: The wardrobe changes colour; or the room rearranges; or the frame changes.

**Note.** The hand closing the door is the minimal trigger; the person is not judged.

## OPT-0267 · reflection · eval

**Caption.** A shopping trolley rolls along an aisle under a convex security mirror, and its small curved reflection slides across the mirror.

**Expectation (hidden).** The reflection is much smaller than the trolley and bulges with the mirror's curve; it moves the same way as the trolley and leaves the mirror when the trolley leaves its view.

**Declared violation types.** shape_identity, causeless_motion

**SA**
- S1 [core] A shopping trolley rolls along an aisle under a convex security mirror.
- S2 [core] Its small curved reflection slides across the mirror.
- S3 [minor] The reflection is much smaller than the trolley and bulges with the curve.
- S4 [minor] The reflection leaves the mirror when the trolley leaves its view.

**PC**
- P1 [core · shape_identity]
  - expect: The reflection is much smaller than the trolley and bulges with the mirror's curve.
  - fail: It is life-size; or flat and undistorted on a plainly convex mirror; or a different object.
- P2 [core · causeless_motion]
  - expect: The reflection moves the same way as the trolley and only then.
  - fail: It moves the opposite way; or with the trolley still; or stays while the trolley leaves.
- P3 [major · missing_consequence]
  - expect: The reflection leaves the mirror when the trolley leaves its view.
  - fail: It stays after; or is missing while the trolley is plainly in view; or appears before.
- P4 [major · material_response]
  - expect: The mirror is rigid.
  - fail: It ripples; or bends; or goes dull.
- P5 [fatal · permanence_count]
  - expect: One trolley and one mirror.
  - fail: A second trolley appears; or the mirror vanishes; or the reflection steps out.
- P6 [minor · attribute_drift]
  - expect: The aisle and the trolley stay the same.
  - fail: The shelves rearrange; or the trolley changes; or the mirror changes shape.

## OPT-0268 · reflection · eval

**Caption.** A dog drinks from a still pond, and its reflection breaks into ripples where its tongue touches the water.

**Expectation (hidden).** The reflection is inverted and sharp until the tongue touches; it fragments where ripples spread and settles when the dog stops.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A dog drinks from a still pond.
- S2 [core] Its reflection breaks into ripples where its tongue touches the water.
- S3 [minor] The reflection is sharp until the tongue touches.
- S4 [minor] The reflection settles when the dog stops.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflection is sharp until the tongue touches, fragments where ripples spread, and settles when the dog stops.
  - fail: It is broken before the tongue touches; or stays sharp through the ripples; or never settles on still water.
- P2 [core · shape_identity]
  - expect: The reflection is inverted and the same dog.
  - fail: It is upright; or a different dog; or a rotated copy.
- P3 [major · material_response]
  - expect: The water is liquid: ripples spread from the tongue and fade.
  - fail: It is rigid; or ripples freeze; or ripples start away from the tongue.
- P4 [major · causeless_motion]
  - expect: The reflection does not move on its own.
  - fail: It moves with the dog still; or drifts.
- P5 [fatal · permanence_count]
  - expect: One dog and one reflection; the reflection stays on the water.
  - fail: A second dog appears; or the reflection rises off the water; or the dog vanishes.
- P6 [minor · attribute_drift]
  - expect: The dog's coat and the pond stay the same.
  - fail: The coat changes; or the pond changes colour; or the bank rearranges.

**Note.** Self-driven animal: where it goes is not judged. Only the reflection's relation to it is.

## OPT-0269 · reflection · eval

**Caption.** A car drives past a puddle at night, and the reflections of its headlights slide across the puddle's surface.

**Expectation (hidden).** The reflected lights move with the car and appear only within the puddle's edges; they vanish when the car has passed.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A car drives past a puddle at night.
- S2 [core] The reflections of its headlights slide across the puddle's surface.
- S3 [minor] The reflections appear only within the puddle's edges.
- S4 [minor] They vanish when the car has passed.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflected lights move with the car and appear only within the puddle's edges.
  - fail: They show on dry pavement; or stay still while the car moves; or remain after the car has passed.
- P2 [core · causeless_motion]
  - expect: The reflections move only as the car moves.
  - fail: They drift with the car stopped; or flicker; or jump.
- P3 [major · shape_identity]
  - expect: There are as many reflected lights as headlights.
  - fail: There are more; or one; or they are a different shape from the lights.
- P4 [major · material_response]
  - expect: The puddle is liquid: the reflections shimmer where it ripples.
  - fail: It is rigid glass; or the reflections are sharp on a rippled surface; or the water flows uphill.
- P5 [fatal · permanence_count]
  - expect: One car and one puddle.
  - fail: A second car appears; or the puddle moves; or a reflection becomes solid.
- P6 [minor · attribute_drift]
  - expect: The car and the street stay the same.
  - fail: The car changes colour; or the street rearranges; or the puddle changes shape.

## OPT-0270 · reflection · eval

**Caption.** A car with a glossy black bonnet drives under a bridge, and the sky reflected in the bonnet is replaced by the dark underside of the bridge and then by sky again.

**Expectation (hidden).** The reflection changes exactly as the car passes beneath the bridge and back into the open; it shows what is above the car, not what is ahead; the bonnet does not keep reflecting sky under the bridge.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A car with a glossy black bonnet drives under a bridge.
- S2 [core] The sky reflected in the bonnet is replaced by the dark underside of the bridge.
- S3 [core] Sky returns as the car emerges.
- S4 [minor] The change happens exactly as the car passes beneath.

**PC**
- P1 [core · missing_consequence]
  - expect: The reflection changes exactly as the car passes beneath the bridge and back into the open, showing what is above the car.
  - fail: The bonnet keeps reflecting sky under the bridge; or shows the bridge before reaching it; or shows what is ahead rather than above.
- P2 [core · causeless_motion]
  - expect: The reflection changes only with the car's position.
  - fail: It flickers with the car stopped; or changes with no bridge; or jumps.
- P3 [major · shape_identity]
  - expect: The reflected sky and bridge are mirror images, stretched by the bonnet's curve.
  - fail: A different scene appears; or the reflection is sharp and flat on a curved bonnet; or it is upside down.
- P4 [major · trajectory_momentum]
  - expect: The car travels steadily under and out.
  - fail: It jumps position; or reverses; or stops with no cause.
- P5 [fatal · permanence_count]
  - expect: One car and one bridge.
  - fail: A second car appears; or the bridge vanishes; or the car passes through a pier.
- P6 [minor · attribute_drift]
  - expect: The car's paint and the road stay the same.
  - fail: The paint changes colour; or the road rearranges; or the bridge changes.

## OPT-0271 · refraction_transparency · eval

**Caption.** A straw stands in a glass holding a layer of oil floating on water, and it looks bent twice, once at the oil's surface and again at the boundary between oil and water.

**Expectation (hidden).** Both kinks sit exactly at the two liquid surfaces and vanish when the straw is lifted out; the straw itself is straight and the part above the liquid is unchanged.

**Declared violation types.** shape_identity, missing_consequence

**SA**
- S1 [core] A straw stands in a glass holding a layer of oil floating on water.
- S2 [core] It looks bent twice: at the oil's surface and at the oil-water boundary.
- S3 [minor] The part above the liquid is unchanged.
- S4 [minor] Both kinks vanish when the straw is lifted out.

**PC**
- P1 [core · shape_identity]
  - expect: The straw itself is straight; both kinks are appearances that vanish out of the liquid.
  - fail: The straw is physically bent when out; or a kink stays at a fixed point on the straw as it is raised; or the straw flexes.
- P2 [core · missing_consequence]
  - expect: Both kinks sit exactly at the two liquid surfaces.
  - fail: A kink is away from a surface; or there is only one kink with two plain boundaries; or the straw looks straight through both layers.
- P3 [major · gravity_direction]
  - expect: The oil floats on the water with a level boundary.
  - fail: The oil is below the water; or the layers mix; or the boundary tilts and holds.
- P4 [major · causeless_motion]
  - expect: The straw moves only with the hand.
  - fail: It rises by itself; or slides; or jumps.
- P5 [fatal · permanence_count]
  - expect: One straw and one glass.
  - fail: The straw duplicates; or the glass vanishes; or the straw passes through the glass.
- P6 [minor · attribute_drift]
  - expect: The straw and the glass stay the same.
  - fail: The straw changes colour; or the glass changes shape; or the table changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0272 · refraction_transparency · eval

**Caption.** Rain drips from a twig, and each hanging drop shows a tiny upside-down image of the garden behind it that vanishes when the drop falls.

**Expectation (hidden).** The image is inverted and confined to the drop; it swells with the drop and disappears the instant the drop falls; the garden itself is unchanged.

**Declared violation types.** shape_identity, permanence_count

**SA**
- S1 [core] Rain drips from a twig.
- S2 [core] Each hanging drop shows a tiny upside-down image of the garden behind it.
- S3 [core] The image vanishes when the drop falls.
- S4 [minor] The image swells with the drop.

**PC**
- P1 [core · shape_identity]
  - expect: The image is inverted and confined to the drop, and the garden itself is unchanged.
  - fail: The image is upright; or extends beyond the drop; or the garden changes.
- P2 [core · permanence_count]
  - expect: The image swells with the drop and disappears the instant the drop falls.
  - fail: It stays after the drop falls; or is there with no drop; or two images in one drop.
- P3 [major · gravity_direction]
  - expect: The drops hang below the twig and fall downward.
  - fail: They hang above; or rise; or fall sideways in still air.
- P4 [major · material_response]
  - expect: The drops are liquid beads that swell and let go.
  - fail: They are rigid; or bounce back up; or freeze.
- P5 [fatal · permanence_count]
  - expect: One twig.
  - fail: It duplicates; or vanishes; or a drop becomes solid.
- P6 [minor · attribute_drift]
  - expect: The twig and the garden stay the same.
  - fail: The twig changes; or the garden rearranges; or the drops change colour.

## OPT-0273 · refraction_transparency · eval

**Caption.** A menu is slid under the clear glass top of a café table, and it stays legible through the glass.

**Expectation (hidden).** The menu is seen sharply through the glass with only a faint reflection over it; the glass neither hides nor distorts it.

**Declared violation types.** missing_consequence, solidity

**SA**
- S1 [core] A menu is slid under the clear glass top of a café table.
- S2 [core] It stays legible through the glass.
- S3 [minor] Only a faint reflection lies over it.

**PC**
- P1 [core · missing_consequence]
  - expect: The menu is seen sharply through the glass with only a faint reflection over it.
  - fail: The glass hides it; or the reflection swamps it; or it is warped by a flat pane.
- P2 [core · solidity]
  - expect: The menu goes under the glass, not through it.
  - fail: It passes through the glass; or the glass passes through it; or it is inside the pane.
- P3 [major · causeless_motion]
  - expect: The menu moves only as pushed.
  - fail: It slides by itself; or jumps; or the glass moves.
- P4 [major · material_response]
  - expect: The glass is flat and rigid.
  - fail: It ripples; or bends; or goes opaque.
- P5 [fatal · permanence_count]
  - expect: One menu and one table.
  - fail: The menu duplicates; or the table vanishes; or the menu turns into another object.
- P6 [minor · attribute_drift]
  - expect: The menu's print and the café stay the same.
  - fail: The print changes; or the café rearranges; or the table changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0274 · refraction_transparency · eval

**Caption.** A goldfish swims around a round bowl, and seen through the curved glass it appears to swell and shrink as it passes the curve.

**Expectation (hidden).** The size change happens only through the curved glass and water; the fish keeps its true size and shape.

**Declared violation types.** shape_identity, missing_consequence

**SA**
- S1 [core] A goldfish swims around a round bowl.
- S2 [core] Seen through the curved glass it appears to swell and shrink as it passes the curve.
- S3 [minor] The fish keeps its true size and shape.

**PC**
- P1 [core · shape_identity]
  - expect: The fish keeps its true size and shape; the swell and shrink are appearances through the curve.
  - fail: The fish actually changes size; or changes shape; or splits.
- P2 [core · missing_consequence]
  - expect: The size change happens only through the curved glass and water.
  - fail: The fish is unchanged through the curve; or changes seen from above the water; or the bowl is opaque.
- P3 [major · solidity]
  - expect: The fish stays inside the water.
  - fail: It passes through the glass; or swims out; or appears outside.
- P4 [major · material_response]
  - expect: The bowl is rigid and the water level.
  - fail: The bowl warps; or the water tilts and holds; or goes opaque.
- P5 [fatal · permanence_count]
  - expect: One fish and one bowl.
  - fail: A second fish appears; or the fish vanishes; or the bowl duplicates.
- P6 [minor · attribute_drift]
  - expect: The fish's colour and the bowl stay the same.
  - fail: The fish changes colour; or the bowl changes shape; or the table changes.

**Note.** The fish is self-driven; only the view through the curve is judged.

## OPT-0275 · refraction_transparency · eval

**Caption.** A coin lies at the bottom of an empty clear jug; as water is poured in, the coin appears to lift toward the surface and look larger.

**Expectation (hidden).** The apparent rise and enlargement grow as the water deepens and disappear if the water is poured out; the coin itself does not move from the bottom.

**Declared violation types.** shape_identity, causeless_motion

**SA**
- S1 [core] A coin lies at the bottom of an empty clear jug.
- S2 [core] Water is poured in.
- S3 [core] The coin appears to lift toward the surface and look larger.
- S4 [minor] The effect grows as the water deepens.

**PC**
- P1 [core · shape_identity]
  - expect: The coin itself does not move from the bottom; the rise and enlargement are appearances.
  - fail: The coin actually lifts; or slides; or changes size.
- P2 [core · causeless_motion]
  - expect: The apparent rise and enlargement grow as the water deepens and only then.
  - fail: The coin looks raised with the jug empty; or the effect shrinks as water is added; or it changes with no pouring.
- P3 [major · process_direction]
  - expect: The water level rises steadily while pouring.
  - fail: It falls while pouring; or jumps; or is full before the pour.
- P4 [major · material_response]
  - expect: The stream falls as liquid and the jug is rigid.
  - fail: The stream is a rod; or the jug bends; or the water goes opaque.
- P5 [fatal · permanence_count]
  - expect: One coin and one jug.
  - fail: The coin duplicates; or the jug vanishes; or water passes through the jug.
- P6 [minor · attribute_drift]
  - expect: The coin and the jug stay the same.
  - fail: The coin changes colour; or the jug changes shape; or the table changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0276 · refraction_transparency · eval

**Caption.** A cat sits behind a glass patio door watching a bird on the lawn, paws at the glass, and cannot reach the bird.

**Expectation (hidden).** The bird is visible through the glass and the paw stops at the pane; the cat does not pass through and the bird is not hidden.

**Declared violation types.** missing_consequence, solidity

**SA**
- S1 [core] A cat sits behind a glass patio door.
- S2 [core] A bird is on the lawn outside.
- S3 [core] The cat paws at the glass.
- S4 [core] It cannot reach the bird.
- S5 [minor] The bird is visible through the glass.

**PC**
- P1 [core · missing_consequence]
  - expect: The bird is visible through the glass.
  - fail: The glass hides the bird; or the bird flickers in and out behind clear glass; or a different bird appears.
- P2 [core · solidity]
  - expect: The paw stops at the pane and the cat does not pass through.
  - fail: The paw passes through the glass; or the cat passes through; or the bird passes in.
- P3 [major · material_response]
  - expect: The pane is flat and rigid.
  - fail: It ripples under the paw; or bends; or goes opaque.
- P4 [major · causeless_motion]
  - expect: The door stays shut.
  - fail: It opens by itself; or slides; or vanishes.
- P5 [fatal · shape_identity]
  - expect: One cat and one bird keep their shape.
  - fail: The cat splits; or the bird merges with the glass; or a second cat appears.
- P6 [minor · attribute_drift]
  - expect: The cat's markings and the lawn stay the same.
  - fail: The markings change; or the lawn rearranges; or the door frame changes.

**Note.** Both animals are self-driven; only transparency and the barrier are judged.

## OPT-0277 · refraction_transparency · eval

**Caption.** A ball rolls past a wall of glass bricks, and seen through the bricks it appears as a broken row of warped pieces that move together.

**Expectation (hidden).** The distorted pieces move in step with the ball and only within the bricks; the ball looks whole and normal where it passes the open edge of the wall.

**Declared violation types.** shape_identity, permanence_count

**SA**
- S1 [core] A ball rolls past a wall of glass bricks.
- S2 [core] Seen through the bricks it appears as a broken row of warped pieces.
- S3 [core] The pieces move together.
- S4 [minor] The ball looks whole and normal past the open edge of the wall.

**PC**
- P1 [core · shape_identity]
  - expect: The ball is whole and normal where it passes the open edge; the broken pieces are appearances through the bricks.
  - fail: The ball is broken past the edge; or it is whole and sharp through the bricks; or it changes shape.
- P2 [core · permanence_count]
  - expect: The distorted pieces move in step with the ball and only within the bricks.
  - fail: The pieces lag; or appear outside the bricks; or remain after the ball has passed.
- P3 [major · causeless_motion]
  - expect: The ball rolls straight and slows gently.
  - fail: It curves; or speeds up; or restarts.
- P4 [major · material_response]
  - expect: The bricks are rigid glass.
  - fail: They ripple; or bend; or go opaque.
- P5 [fatal · permanence_count]
  - expect: One ball and one wall.
  - fail: A second ball appears; or the wall vanishes; or the ball passes through a brick.
- P6 [minor · attribute_drift]
  - expect: The ball's colour and the wall stay the same.
  - fail: The ball changes colour; or the wall changes; or the floor changes.

## OPT-0278 · refraction_transparency · eval

**Caption.** Street lights are seen through a glass of fizzy water, and they wobble and sparkle as bubbles rise through the glass.

**Expectation (hidden).** The distortion changes with the rising bubbles and the lights are steady when seen past the glass; the lights themselves do not move.

**Declared violation types.** shape_identity, causeless_motion

**SA**
- S1 [core] Street lights are seen through a glass of fizzy water.
- S2 [core] They wobble and sparkle as bubbles rise through the glass.
- S3 [minor] The lights are steady when seen past the glass.

**PC**
- P1 [core · shape_identity]
  - expect: The lights themselves do not move; the wobble is through the glass only.
  - fail: The lights move; or are wobbly past the glass; or a different set of lights appears.
- P2 [core · causeless_motion]
  - expect: The distortion changes with the rising bubbles and only then.
  - fail: The view wobbles with no bubbles; or is steady while bubbles plainly rise; or the glass moves.
- P3 [major · gravity_direction]
  - expect: The bubbles rise.
  - fail: They sink; or hang; or go sideways.
- P4 [major · material_response]
  - expect: The glass is rigid and the water liquid.
  - fail: The glass bends; or the water is rigid; or goes opaque.
- P5 [fatal · permanence_count]
  - expect: One glass.
  - fail: It duplicates; or vanishes; or bubbles appear from nowhere outside it.
- P6 [minor · attribute_drift]
  - expect: The glass and the street stay the same.
  - fail: The glass changes shape; or the street rearranges; or the water changes colour.

## OPT-0279 · refraction_transparency · eval

**Caption.** A candle burns behind a full round wine glass, and seen through the glass the flame appears tiny and upside down.

**Expectation (hidden).** The inverted small flame appears only through the liquid-filled part of the glass and flickers in step with the real flame; the flame seen past the glass is upright and normal.

**Declared violation types.** shape_identity, missing_consequence

**SA**
- S1 [core] A candle burns behind a full round wine glass.
- S2 [core] Seen through the glass the flame appears tiny and upside down.
- S3 [minor] The tiny flame flickers in step with the real flame.
- S4 [minor] The flame seen past the glass is upright and normal.

**PC**
- P1 [core · shape_identity]
  - expect: The inverted small flame appears only through the liquid-filled part of the glass; past the glass the flame is upright and normal.
  - fail: The flame is inverted past the glass; or upright through it; or a different flame appears.
- P2 [core · missing_consequence]
  - expect: The tiny flame flickers in step with the real flame.
  - fail: It flickers out of time; or is steady while the real flame flickers; or flickers with the real flame out.
- P3 [major · gravity_direction]
  - expect: The real flame points upward.
  - fail: It points down or sideways in still air; or detaches; or floats.
- P4 [major · material_response]
  - expect: The glass is rigid and the liquid level.
  - fail: The glass bends; or the liquid tilts and holds; or goes opaque.
- P5 [fatal · permanence_count]
  - expect: One candle and one glass.
  - fail: A second candle appears; or the glass vanishes; or the candle passes through the glass.
- P6 [minor · attribute_drift]
  - expect: The candle, the wine and the glass stay the same.
  - fail: The candle changes colour; or the wine changes colour; or the glass changes shape.

## OPT-0280 · refraction_transparency · eval

**Caption.** A laser pointer's beam enters a tank of slightly milky water at an angle, and the beam bends where it crosses the surface.

**Expectation (hidden).** The beam is straight in the air and straight in the water but kinks at the surface, bending toward the vertical; the kink moves with the entry point and there is no bend when the beam is aimed straight down.

**Declared violation types.** missing_consequence, shape_identity

**SA**
- S1 [core] A laser pointer's beam enters a tank of slightly milky water at an angle.
- S2 [core] The beam bends where it crosses the surface.
- S3 [minor] The beam is straight in the air and straight in the water.
- S4 [minor] The kink moves with the entry point.

**PC**
- P1 [core · missing_consequence]
  - expect: The beam is straight in the air and in the water and kinks only at the surface, bending toward the vertical.
  - fail: The beam curves in the air; or in the water; or passes straight through the surface with no kink at an angle.
- P2 [core · shape_identity]
  - expect: The kink moves with the entry point and there would be no bend if the beam were aimed straight down.
  - fail: The kink stays put while the entry point moves; or it bends the wrong way; or it splits into two beams.
- P3 [major · causeless_motion]
  - expect: The beam moves only with the pointer.
  - fail: It drifts with the pointer still; or flickers; or jumps.
- P4 [major · material_response]
  - expect: The water surface is level and the beam is visible in the milky water.
  - fail: The surface tilts and holds; or the beam is invisible in the water; or the water is rigid.
- P5 [fatal · permanence_count]
  - expect: One pointer, one beam and one tank.
  - fail: A second beam appears; or the tank vanishes; or the beam becomes solid.
- P6 [minor · attribute_drift]
  - expect: The tank and the room stay the same.
  - fail: The tank changes shape; or the room rearranges; or the beam changes colour.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0281 · illumination · eval

**Caption.** A lit lantern is lowered into a well on a rope, and the circle of lit stone around it slides down the shaft.

**Expectation (hidden).** The brightest ring of wall is level with the lantern and moves down with it; the wall above darkens as the lantern passes; the light does not stay at the top or light the whole shaft evenly.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A lit lantern is lowered into a well on a rope.
- S2 [core] The circle of lit stone around it slides down the shaft.
- S3 [minor] The wall above darkens as the lantern passes.

**PC**
- P1 [core · missing_consequence]
  - expect: The brightest ring of wall is level with the lantern and moves down with it, and the wall above darkens as it passes.
  - fail: The light stays at the top; or the whole shaft is lit evenly; or the bright ring is far from the lantern.
- P2 [core · causeless_motion]
  - expect: The lit ring moves only as the lantern moves.
  - fail: It moves with the lantern still; or before the lantern; or jumps.
- P3 [major · material_response]
  - expect: The rope stays taut and straight above the lantern.
  - fail: It goes slack while the lantern hangs; or stretches; or bends.
- P4 [major · gravity_direction]
  - expect: The lantern hangs below the rope and goes down.
  - fail: It rises; or hangs sideways; or floats.
- P5 [fatal · permanence_count]
  - expect: One lantern and one rope.
  - fail: A second lantern appears; or the rope vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The well's stone and the lantern stay the same.
  - fail: The stone changes; or the lantern changes colour; or the rope changes.

**Note.** The hand is the minimal trigger; the person is not judged. Illumination: the on/off causality of electric lights belongs to Electricity; here only where the light goes once it exists is judged.

## OPT-0282 · illumination · eval

**Caption.** A cat trots along a night street beneath a row of streetlamps, brightening as it passes under each lamp and fading in the dark stretches between.

**Expectation (hidden).** The cat is brightest directly under each lamp and dimmest midway between lamps, repeating for each lamp; its shadow points away from the nearest lamp and swaps sides as it passes beneath.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A cat trots along a night street beneath a row of streetlamps.
- S2 [core] It brightens as it passes under each lamp.
- S3 [core] It fades in the dark stretches between.
- S4 [minor] Its shadow points away from the nearest lamp and swaps sides as it passes beneath.

**PC**
- P1 [core · missing_consequence]
  - expect: The cat is brightest directly under each lamp and dimmest midway between, repeating for each lamp.
  - fail: It is evenly lit along the street; or brightest between lamps; or dark under a lamp.
- P2 [core · process_direction]
  - expect: The brightening and fading alternate with the lamps.
  - fail: It stays bright; or stays dark; or flickers unrelated to position.
- P3 [major · missing_consequence]
  - expect: Its shadow points away from the nearest lamp and swaps sides as it passes beneath.
  - fail: The shadow points toward the lamp; or stays on one side; or there is none.
- P4 [major · causeless_motion]
  - expect: The lamps stay lit and still.
  - fail: A lamp goes out; or moves; or flickers.
- P5 [fatal · shape_identity]
  - expect: One cat keeps its shape.
  - fail: It splits; or turns into another animal; or a second cat appears.
- P6 [minor · attribute_drift]
  - expect: The cat's coat and the street stay the same.
  - fail: The coat changes colour rather than brightness; or the street rearranges; or the lamps change.

**Note.** The cat is self-driven; only the light on it is judged. Illumination: the on/off causality of electric lights belongs to Electricity; here only where the light goes once it exists is judged.

## OPT-0283 · illumination · eval

**Caption.** A lantern is lit in a dark barn, and the nearby hay and beams brighten while the far end stays in shadow.

**Expectation (hidden).** Brightness is greatest near the lantern and falls off with distance; shadows fall away from it.

**Declared violation types.** missing_consequence, attribute_drift

**SA**
- S1 [core] A lantern is lit in a dark barn.
- S2 [core] The nearby hay and beams brighten.
- S3 [core] The far end stays in shadow.
- S4 [minor] Shadows fall away from the lantern.

**PC**
- P1 [core · missing_consequence]
  - expect: Brightness is greatest near the lantern and falls off with distance, and the far end stays dark.
  - fail: The far end is as bright as the near; or the near hay stays dark; or the light comes from elsewhere.
- P2 [core · attribute_drift]
  - expect: The light is warm and the hay and beams keep their colours under it.
  - fail: Objects change colour rather than brightness; or the light is a different colour; or the barn changes colour.
- P3 [major · missing_consequence]
  - expect: Shadows fall away from the lantern.
  - fail: They point toward it; or in several directions; or there are none.
- P4 [major · causeless_motion]
  - expect: The lit area stays put with the lantern still.
  - fail: It wanders; or flickers wildly; or the lantern moves by itself.
- P5 [fatal · permanence_count]
  - expect: One lantern.
  - fail: A second appears; or it vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The barn and its contents stay the same.
  - fail: Hay bales move; or the beams change; or the lantern changes shape.

**Note.** Illumination: the on/off causality of electric lights belongs to Electricity; here only where the light goes once it exists is judged.

## OPT-0284 · illumination · eval

**Caption.** The flap of a lit tent is unzipped from inside at night, and lantern light spills out onto the grass in a triangle that widens as the flap opens.

**Expectation (hidden).** The lit patch appears only once the flap parts and grows with the opening; it lies in front of the doorway and fades with distance; the grass beside the tent stays dark.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A lit tent's flap is unzipped from inside at night.
- S2 [core] Lantern light spills out onto the grass.
- S3 [core] The lit triangle widens as the flap opens.
- S4 [minor] The grass beside the tent stays dark.

**PC**
- P1 [core · missing_consequence]
  - expect: The lit patch appears only once the flap parts and lies in front of the doorway, fading with distance.
  - fail: Light is on the grass with the flap shut; or the patch is beside the tent; or it is even to its far edge.
- P2 [core · process_direction]
  - expect: The patch grows with the opening.
  - fail: It shrinks as the flap opens; or is full width before the flap moves; or flickers.
- P3 [major · causeless_motion]
  - expect: The patch changes only as the flap moves.
  - fail: It grows with the flap still; or before the zip; or jumps.
- P4 [major · shape_identity]
  - expect: The patch is a triangle spreading from the doorway.
  - fail: It is a round spot; or splits; or is on the tent's roof.
- P5 [fatal · permanence_count]
  - expect: One tent and one lantern.
  - fail: A second tent appears; or the lantern vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The tent and the grass stay the same.
  - fail: The tent changes colour; or the grass changes; or the flap changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0285 · illumination · eval

**Caption.** A car with its headlights on turns a corner at night, and the beams sweep across a row of parked cars.

**Expectation (hidden).** Each parked car brightens as the beams cross it and darkens after; the lit area moves with the turning car.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A car with its headlights on turns a corner at night.
- S2 [core] The beams sweep across a row of parked cars.
- S3 [minor] Each parked car brightens as the beams cross it and darkens after.

**PC**
- P1 [core · missing_consequence]
  - expect: Each parked car brightens as the beams cross it and darkens after, and the lit area moves with the turning car.
  - fail: Cars stay lit after the beams pass; or brighten before; or the lit area stays put while the car turns.
- P2 [core · causeless_motion]
  - expect: The lit area moves only as the car moves.
  - fail: It sweeps with the car stopped; or jumps; or moves the opposite way.
- P3 [major · shape_identity]
  - expect: The beams are two cones from the headlights.
  - fail: There are more; or one; or they are a flood in all directions.
- P4 [major · causeless_motion]
  - expect: The parked cars stay still.
  - fail: One moves; or vanishes; or a car changes colour rather than brightness.
- P5 [fatal · permanence_count]
  - expect: One moving car and the parked cars keep their number.
  - fail: A parked car vanishes; or appears; or the moving car duplicates.
- P6 [minor · attribute_drift]
  - expect: The street stays the same.
  - fail: The buildings rearrange; or the road markings shift; or the cars change colour.

## OPT-0286 · illumination · eval

**Caption.** A flashlight is pressed against the back of a large leaf in a dark room, and the leaf glows green with its veins showing dark.

**Expectation (hidden).** The glow is brightest where the lens touches and fades toward the leaf's edges; the veins are darker than the blade; the glow disappears when the flashlight is switched off.

**Declared violation types.** missing_consequence, attribute_drift

**SA**
- S1 [core] A flashlight is pressed against the back of a large leaf in a dark room.
- S2 [core] The leaf glows green.
- S3 [core] Its veins show dark.
- S4 [minor] The glow is brightest where the lens touches.

**PC**
- P1 [core · missing_consequence]
  - expect: The glow is brightest where the lens touches and fades toward the leaf's edges, and would disappear when the flashlight is off.
  - fail: The whole leaf glows evenly; or the edges are brightest; or the leaf glows with the light off.
- P2 [core · attribute_drift]
  - expect: The glow is green and the veins are darker than the blade.
  - fail: The glow is white; or the veins are brighter than the blade; or the leaf changes colour when the light is off.
- P3 [major · causeless_motion]
  - expect: The leaf and the flashlight stay put.
  - fail: The leaf moves; or the flashlight moves by itself; or the glow wanders.
- P4 [major · shape_identity]
  - expect: The glow follows the leaf's outline.
  - fail: It is a round spot larger than the leaf; or splits; or the leaf changes shape.
- P5 [fatal · permanence_count]
  - expect: One leaf and one flashlight.
  - fail: A second leaf appears; or the flashlight vanishes; or the light passes through the leaf as a beam.
- P6 [minor · attribute_drift]
  - expect: The room stays the same.
  - fail: The room rearranges; or the flashlight changes; or the leaf's stem changes.

**Note.** The hand is the minimal trigger; the person is not judged. Illumination: the on/off causality of electric lights belongs to Electricity; here only where the light goes once it exists is judged.

## OPT-0287 · illumination · eval

**Caption.** A moth flutters through the beam of a projector in a dark hall and is brightly lit only while it is inside the cone of light.

**Expectation (hidden).** The moth is dim outside the beam, flares bright as it enters, and dims again as it leaves; its shadow appears on the screen while it is in the beam.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A moth flutters through the beam of a projector in a dark hall.
- S2 [core] It is brightly lit only while inside the cone of light.
- S3 [minor] Its shadow appears on the screen while it is in the beam.

**PC**
- P1 [core · missing_consequence]
  - expect: The moth is dim outside the beam, flares bright as it enters, and dims again as it leaves.
  - fail: It is bright outside the beam; or dark inside it; or stays bright after leaving.
- P2 [core · causeless_motion]
  - expect: The brightness changes only with the moth's position in the beam.
  - fail: It flickers with the moth still; or the beam moves; or the hall brightens.
- P3 [major · missing_consequence]
  - expect: Its shadow appears on the screen while it is in the beam.
  - fail: There is no shadow in the beam; or a shadow outside it; or the shadow is away from the beam's line.
- P4 [major · shape_identity]
  - expect: The beam is one cone from the projector.
  - fail: It bends; or splits; or floods the hall.
- P5 [fatal · shape_identity]
  - expect: One moth keeps its wings.
  - fail: It splits; or a wing detaches; or a second moth appears.
- P6 [minor · attribute_drift]
  - expect: The hall and the screen stay the same.
  - fail: The picture changes with no click; or the hall rearranges; or the projector changes.

**Note.** The moth is self-driven; only the light on it is judged. Illumination: the on/off causality of electric lights belongs to Electricity; here only where the light goes once it exists is judged.

## OPT-0288 · illumination · eval

**Caption.** A candle is carried behind a paper screen in a dark room, and a soft glow travels across the screen with it.

**Expectation (hidden).** The glow is brightest opposite the flame and fades outward; it moves with the candle and flickers with it; the screen is dark where the candle is not.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A paper screen stands in a dark room.
- S2 [core] A candle is carried behind it.
- S3 [core] A soft glow travels across the screen with it.
- S4 [minor] The glow flickers with the candle.

**PC**
- P1 [core · causeless_motion]
  - expect: The glow moves with the candle and only then, flickering with it.
  - fail: It moves with the candle still; or stays put while the candle moves; or pulses with a steady flame.
- P2 [core · missing_consequence]
  - expect: The glow is brightest opposite the flame and fades outward, and the screen is dark where the candle is not.
  - fail: The whole screen glows evenly; or the brightest spot is far from the candle; or the screen glows with the candle gone.
- P3 [major · shape_identity]
  - expect: The glow is one soft patch through the paper.
  - fail: It is a sharp spot; or splits; or is a geometric shape.
- P4 [major · gravity_direction]
  - expect: The flame points upward.
  - fail: It points down or sideways; or detaches; or floats.
- P5 [fatal · permanence_count]
  - expect: One candle and one screen.
  - fail: A second glow appears with one candle; or the screen vanishes; or the candle passes through the paper.
- P6 [minor · attribute_drift]
  - expect: The screen and the room stay the same.
  - fail: The screen changes colour; or the room rearranges; or the candle changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0289 · illumination · eval

**Caption.** A train runs through a tunnel with its headlight on, lighting the walls ahead of it while the walls behind fall back into darkness.

**Expectation (hidden).** The lit stretch stays ahead of the train and moves with it; the wall brightens as the beam reaches it and darkens once the train has passed; the far end of the tunnel is not lit until the beam reaches it.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A train runs through a tunnel with its headlight on.
- S2 [core] It lights the walls ahead of it.
- S3 [core] The walls behind fall back into darkness.
- S4 [minor] The far end is not lit until the beam reaches it.

**PC**
- P1 [core · missing_consequence]
  - expect: The lit stretch stays ahead of the train and moves with it, and the wall darkens once the train has passed.
  - fail: The walls behind stay lit; or the far end is lit before the beam reaches it; or the lit stretch is behind the train.
- P2 [core · causeless_motion]
  - expect: The lit stretch moves only as the train moves.
  - fail: It moves with the train stopped; or jumps; or the beam swings.
- P3 [major · shape_identity]
  - expect: The beam is one cone from the headlight.
  - fail: It bends; or splits; or floods the whole tunnel.
- P4 [major · trajectory_momentum]
  - expect: The train travels steadily along the track.
  - fail: It jumps position; or reverses; or leaves the rails.
- P5 [fatal · permanence_count]
  - expect: One train and one tunnel.
  - fail: A second train appears; or the tunnel vanishes; or the train passes through the wall.
- P6 [minor · attribute_drift]
  - expect: The tunnel walls and the train stay the same.
  - fail: The walls change; or the train changes colour; or the track changes.

**Note.** Illumination: the on/off causality of electric lights belongs to Electricity; here only where the light goes once it exists is judged.

## OPT-0290 · illumination · eval

**Caption.** The sun comes out from behind a cloud over a beach, and the sand and sea brighten all at once.

**Expectation (hidden).** The whole scene brightens together and sharp shadows appear; it dims again when the next cloud passes.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] The sun comes out from behind a cloud over a beach.
- S2 [core] The sand and sea brighten all at once.
- S3 [minor] Sharp shadows appear.
- S4 [minor] It would dim again when the next cloud passes.

**PC**
- P1 [core · missing_consequence]
  - expect: The whole scene brightens together and sharp shadows appear.
  - fail: Only part brightens; or shadows stay soft in full sun; or the scene dims as the sun comes out.
- P2 [core · process_direction]
  - expect: The brightening follows the cloud's edge and holds while the sun is clear.
  - fail: It flickers; or brightens then dims with the sun still out; or is instant with no cloud edge.
- P3 [major · causeless_motion]
  - expect: The cloud moves steadily and nothing on the beach moves with it.
  - fail: The cloud jumps; or objects move; or shadows swing round.
- P4 [major · attribute_drift]
  - expect: Colours stay the same, only brighter.
  - fail: The sand changes colour; or the sea changes colour; or the sky changes abruptly.
- P5 [fatal · permanence_count]
  - expect: The beach's objects keep their number.
  - fail: An object vanishes; or appears; or duplicates.
- P6 [minor · attribute_drift]
  - expect: The beach stays the same.
  - fail: Items rearrange; or the shoreline moves; or the horizon changes.

## OPT-0291 · color_mixing · eval

**Caption.** A lump of red play-dough is kneaded together with a lump of blue, and the mixture turns purple.

**Expectation (hidden).** Purple appears where the two colours fold together and spreads until no streaks remain; the colours do not separate again.

**Declared violation types.** attribute_drift, process_direction

**SA**
- S1 [core] A lump of red play-dough and a lump of blue are present.
- S2 [core] They are kneaded together.
- S3 [core] The mixture turns purple.
- S4 [minor] Purple appears where the colours fold together.
- S5 [minor] The kneading comes first and the purple follows.

**PC**
- P1 [core · process_direction]
  - expect: Purple appears where the two colours fold together and spreads until no streaks remain; it does not separate again.
  - fail: Purple appears before the kneading; or the colours separate back; or the streaks return.
- P2 [core · attribute_drift]
  - expect: The mix is purple, and unmixed red and blue stay red and blue.
  - fail: The mix is a colour other than purple; or the pure lumps change; or the whole mass turns one colour at once.
- P3 [major · material_response]
  - expect: The dough is a soft paste that folds and stretches under the hands.
  - fail: It is rigid; or flows like water; or bounces like rubber.
- P4 [major · causeless_motion]
  - expect: The dough moves only where the hands work it.
  - fail: It moves by itself; or the table moves; or it folds with no hands.
- P5 [fatal · permanence_count]
  - expect: The amount of dough stays the same.
  - fail: Dough appears from nowhere; or vanishes; or the hands pass through it.
- P6 [minor · attribute_drift]
  - expect: The table and the background stay the same.
  - fail: The table changes; or the background rearranges; or the hands change.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0292 · color_mixing · eval

**Caption.** A squirt of yellow mustard and a squirt of red ketchup are stirred together on a plate, and the mixture turns orange.

**Expectation (hidden).** Orange appears where the two sauces meet and spreads with stirring until the streaks are gone; the mixture does not turn back to separate red and yellow.

**Declared violation types.** attribute_drift, process_direction

**SA**
- S1 [core] A squirt of yellow mustard and a squirt of red ketchup are on a plate.
- S2 [core] They are stirred together.
- S3 [core] The mixture turns orange.
- S4 [minor] Orange appears where the two sauces meet.
- S5 [minor] The stir comes first and the orange follows.

**PC**
- P1 [core · process_direction]
  - expect: Orange appears where the sauces meet and spreads with stirring until the streaks are gone; it does not separate again.
  - fail: Orange appears before stirring; or the sauces separate back; or the orange retreats.
- P2 [core · attribute_drift]
  - expect: The mix is orange, and unstirred yellow and red stay as they were.
  - fail: The mix is a colour other than orange; or the pure sauces change; or the plate turns one colour at once.
- P3 [major · material_response]
  - expect: The sauces are thick liquids that streak under the stirrer.
  - fail: They are rigid; or flow like water; or bounce.
- P4 [major · causeless_motion]
  - expect: The sauces move only where stirred.
  - fail: They swirl by themselves; or the plate moves; or they mix with no stirrer.
- P5 [fatal · permanence_count]
  - expect: The amount of sauce stays the same and the plate keeps its shape.
  - fail: Sauce appears from nowhere; or the plate duplicates; or the stirrer passes through the plate.
- P6 [minor · attribute_drift]
  - expect: The plate and the table stay the same.
  - fail: The plate changes colour; or the table changes; or the stirrer changes.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0293 · color_mixing · eval

**Caption.** A green spotlight is aimed at a white marble statue in a garden at night, and the statue appears green.

**Expectation (hidden).** The statue takes the light's colour only where the beam falls and returns to white when the light is switched off.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] A white marble statue stands in a garden at night.
- S2 [core] A green spotlight is aimed at it.
- S3 [core] The statue appears green.
- S4 [minor] It returns to white when the light is off.

**PC**
- P1 [core · attribute_drift]
  - expect: The statue looks green only where the beam falls and while it is on.
  - fail: It is green with the light off; or stays white under the green beam; or turns a different colour.
- P2 [core · missing_consequence]
  - expect: The change is confined to where the beam falls and happens with the light.
  - fail: Parts outside the beam turn green; or the statue changes before the light; or long after.
- P3 [major · shape_identity]
  - expect: The statue's shape and shading show in green, not as a colour change of the marble.
  - fail: Parts are a different colour; or the statue is flat green with no shading; or the statue changes shape.
- P4 [major · causeless_motion]
  - expect: Nothing moves; only the light changes.
  - fail: The statue moves; or the spotlight swings by itself; or the lit area wanders.
- P5 [fatal · permanence_count]
  - expect: One statue and one spotlight.
  - fail: A second statue appears; or the spotlight vanishes; or the light becomes solid.
- P6 [minor · attribute_drift]
  - expect: The garden stays the same.
  - fail: The plants rearrange; or the plinth changes; or the spotlight changes shape.

## OPT-0294 · color_mixing · eval

**Caption.** A pigeon walks past outside a window fitted with coloured glass panes and appears red, then blue, then yellow as it passes behind each pane.

**Expectation (hidden).** The pigeon takes the colour of whichever pane it is behind and changes at each pane's edge; it looks its normal grey through the clear frame between panes; the panes themselves do not change colour.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] A pigeon walks past outside a window fitted with coloured glass panes.
- S2 [core] It appears red, then blue, then yellow as it passes behind each pane.
- S3 [minor] It looks its normal grey through the clear frame between panes.
- S4 [minor] The colour changes at each pane's edge.

**PC**
- P1 [core · attribute_drift]
  - expect: The pigeon takes the colour of whichever pane it is behind and looks grey through the clear gaps.
  - fail: It is grey behind a coloured pane; or coloured through a clear gap; or a colour the panes do not have.
- P2 [core · missing_consequence]
  - expect: The colour changes exactly at each pane's edge.
  - fail: It changes mid-pane; or lags behind the edge; or changes with the bird still.
- P3 [major · shape_identity]
  - expect: The panes themselves do not change colour and the bird keeps its shape.
  - fail: A pane changes colour; or the bird changes shape; or the panes rearrange.
- P4 [major · causeless_motion]
  - expect: The bird walks steadily and the window stays still.
  - fail: The bird jumps position; or the window moves; or the colours shift with the bird still.
- P5 [fatal · permanence_count]
  - expect: One bird and one window.
  - fail: A second bird appears; or a pane vanishes; or the bird passes through the glass.
- P6 [minor · attribute_drift]
  - expect: The window frame and the ground stay the same.
  - fail: The frame changes; or the ground changes; or the bird's true colour changes when seen through clear glass.

**Note.** The pigeon is self-driven; only the tint through the panes is judged.

## OPT-0295 · color_mixing · eval

**Caption.** A rainbow appears in the mist at the foot of a waterfall on a sunny day, and fades when a cloud covers the sun.

**Expectation (hidden).** The rainbow sits within the mist opposite the sun, keeps its arc while the sun shines, and disappears when the sun is hidden.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A rainbow appears in the mist at the foot of a waterfall on a sunny day.
- S2 [core] A cloud covers the sun.
- S3 [core] The rainbow fades.
- S4 [minor] The rainbow sits within the mist opposite the sun.

**PC**
- P1 [core · missing_consequence]
  - expect: The rainbow sits within the mist opposite the sun and disappears when the sun is hidden.
  - fail: It is on the rock; or stays bright with the sun hidden; or appears with no sun.
- P2 [core · permanence_count]
  - expect: The rainbow keeps its arc while the sun shines and does not move across the scene.
  - fail: It moves; or changes shape; or a second rainbow appears.
- P3 [major · attribute_drift]
  - expect: The bands show the spectrum's order.
  - fail: They are in random order; or a single colour; or change colours.
- P4 [major · gravity_direction]
  - expect: The waterfall falls and the mist drifts.
  - fail: The water rises; or the mist hangs rigidly; or falls upward.
- P5 [fatal · permanence_count]
  - expect: One waterfall.
  - fail: A second waterfall appears; or it vanishes; or the rainbow becomes solid.
- P6 [minor · attribute_drift]
  - expect: The rocks and the trees stay the same.
  - fail: The rocks rearrange; or the trees change; or the water changes colour.

## OPT-0296 · color_mixing · eval

**Caption.** A white ball on a white table is lit by a red lamp from the left and a blue lamp from the right, and it casts a blue-tinted shadow on one side and a red-tinted shadow on the other.

**Expectation (hidden).** The shadow cast by blocking the red lamp is lit only by the blue lamp and looks blue, and vice versa; the ball itself looks magenta-white where both lights fall; switching off one lamp removes its shadow's colour.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] A white ball is on a white table.
- S2 [core] A red lamp lights it from the left and a blue lamp from the right.
- S3 [core] It casts a blue-tinted shadow on one side and a red-tinted shadow on the other.
- S4 [minor] The ball looks magenta-white where both lights fall.

**PC**
- P1 [core · attribute_drift]
  - expect: The shadow cast by blocking the red lamp is lit only by the blue lamp and looks blue, and vice versa.
  - fail: Both shadows are grey; or the shadows have swapped colours; or a shadow is a colour neither lamp gives.
- P2 [core · missing_consequence]
  - expect: Each coloured shadow lies away from its own lamp, and switching off one lamp would remove its shadow's colour.
  - fail: A shadow lies toward its lamp; or both shadows are on the same side; or a shadow keeps its colour with its lamp off.
- P3 [major · shape_identity]
  - expect: Each shadow keeps the ball's round outline.
  - fail: A shadow is a different shape; or splits; or the two merge into one.
- P4 [major · causeless_motion]
  - expect: The ball and the lamps stay put.
  - fail: The ball rolls; or a lamp moves by itself; or a shadow drifts.
- P5 [fatal · permanence_count]
  - expect: One ball and two lamps.
  - fail: The ball duplicates; or a lamp vanishes; or a shadow becomes solid.
- P6 [minor · attribute_drift]
  - expect: The table and the room stay the same.
  - fail: The table changes; or the room rearranges; or the ball changes size.

## OPT-0297 · color_mixing · eval

**Caption.** A white delivery van drives along a street from beneath orange sodium lamps to beneath white LED lamps, and its paint looks amber and then white.

**Expectation (hidden).** The van's colour follows the light falling on it and changes as it passes from one kind of lamp to the next; it does not look white under the orange lamps or amber under the white ones.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] A white delivery van drives along a street.
- S2 [core] It passes from beneath orange sodium lamps to beneath white LED lamps.
- S3 [core] Its paint looks amber and then white.
- S4 [minor] The colour changes as it passes from one kind of lamp to the next.

**PC**
- P1 [core · attribute_drift]
  - expect: The van's colour follows the light falling on it: amber under the orange lamps and white under the white ones.
  - fail: It looks white under the orange lamps; or amber under the white ones; or a colour neither lamp gives.
- P2 [core · missing_consequence]
  - expect: The change happens as the van passes from one kind of lamp to the next.
  - fail: It changes before reaching the new lamps; or long after; or changes with the van stopped under one kind.
- P3 [major · causeless_motion]
  - expect: The lamps stay lit and still and the van drives steadily.
  - fail: A lamp goes out; or the van jumps position; or the colour flickers under steady lamps.
- P4 [major · shape_identity]
  - expect: The van keeps its shape and markings.
  - fail: It changes shape; or the markings change; or it turns into another vehicle.
- P5 [fatal · permanence_count]
  - expect: One van.
  - fail: It duplicates; or vanishes; or passes through a lamp post.
- P6 [minor · attribute_drift]
  - expect: The street stays the same.
  - fail: The buildings rearrange; or the road markings shift; or the lamps change shape.

## OPT-0298 · color_mixing · eval

**Caption.** A red umbrella is opened in bright sun, and the ground and objects beneath it take on a red tint.

**Expectation (hidden).** The red tint appears only in the umbrella's shade and only after it opens; the ground outside the shade keeps its normal colour; the tint disappears when the umbrella closes.

**Declared violation types.** attribute_drift, missing_consequence

**SA**
- S1 [core] A red umbrella is opened in bright sun.
- S2 [core] The ground and objects beneath it take on a red tint.
- S3 [minor] The ground outside the shade keeps its normal colour.
- S4 [minor] The umbrella opens first and the tint appears with it.

**PC**
- P1 [core · attribute_drift]
  - expect: The red tint appears only in the umbrella's shade and the ground outside keeps its normal colour.
  - fail: The tint is outside the shade; or the shade is plain grey with no tint; or the tint is a different colour.
- P2 [core · missing_consequence]
  - expect: The tint appears only after the umbrella opens and would disappear when it closes.
  - fail: It is there before the umbrella opens; or remains after closing; or the umbrella opens and no tint appears.
- P3 [major · missing_consequence]
  - expect: The shade lies on the side away from the sun.
  - fail: It lies toward the sun; or directly beneath under a low sun; or it is missing in sunlight.
- P4 [major · material_response]
  - expect: The canopy opens as taut fabric on ribs.
  - fail: It is rigid like a plate; or floats off; or tears.
- P5 [fatal · permanence_count]
  - expect: One umbrella.
  - fail: It duplicates; or vanishes; or the shade becomes solid.
- P6 [minor · attribute_drift]
  - expect: The umbrella and the surroundings stay the same.
  - fail: The canopy changes colour; or the ground changes; or the objects rearrange.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0299 · color_mixing · eval

**Caption.** A shiny DVD is tilted in sunlight, and rainbow bands slide across the wall as it turns.

**Expectation (hidden).** The coloured bands appear only while the sun hits the disc, move as the disc tilts, and vanish when the disc is turned away or the sun is covered; the wall itself stays white.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A shiny DVD is tilted in sunlight.
- S2 [core] Rainbow bands slide across the wall as it turns.
- S3 [minor] The bands vanish when the disc is turned away or the sun is covered.
- S4 [minor] The wall itself stays white.

**PC**
- P1 [core · causeless_motion]
  - expect: The bands move as the disc tilts and only then.
  - fail: They slide with the disc still; or stay put while the disc turns; or flicker in steady sun.
- P2 [core · missing_consequence]
  - expect: The bands appear only while the sun hits the disc and would vanish when the disc is turned away or the sun covered.
  - fail: They are there with no sun; or the disc is in sun with no bands; or they remain with the disc turned away.
- P3 [major · attribute_drift]
  - expect: The bands are rainbow-coloured and the wall stays white.
  - fail: They are a single colour; or white; or the wall changes colour.
- P4 [major · shape_identity]
  - expect: The bands are curved streaks.
  - fail: They are a single round spot; or sharp squares; or flood the wall.
- P5 [fatal · permanence_count]
  - expect: One disc.
  - fail: It duplicates; or vanishes; or a band becomes solid.
- P6 [minor · attribute_drift]
  - expect: The room stays the same.
  - fail: The room rearranges; or the wall changes; or the disc changes shape.

**Note.** The hand is the minimal trigger; the person is not judged.

## OPT-0300 · color_mixing · eval

**Caption.** A red sock is dropped into a basin of hot soapy water holding white shirts, and the water around it turns pink.

**Expectation (hidden).** The pink spreads out from the sock through the water and does not clear again; the shirts nearest the sock take on a faint pink tinge; the sock does not turn white.

**Declared violation types.** attribute_drift, process_direction

**SA**
- S1 [core] A basin of hot soapy water holds white shirts.
- S2 [core] A red sock is dropped in.
- S3 [core] The water around it turns pink.
- S4 [minor] The shirts nearest the sock take on a faint pink tinge.
- S5 [minor] The sock goes in first and the pink spreads after.

**PC**
- P1 [core · process_direction]
  - expect: The pink spreads out from the sock through the water and does not clear again.
  - fail: The water clears again; or is pink before the sock; or the pink retreats to the sock.
- P2 [core · attribute_drift]
  - expect: The water is pink and the sock stays red; the nearest shirts take a faint tinge.
  - fail: The sock turns white; or the water turns a colour other than pink; or far shirts turn deep red at once.
- P3 [major · material_response]
  - expect: The water is liquid and the dye drifts in it.
  - fail: The water is rigid; or the dye is a solid lump; or beads bounce.
- P4 [major · gravity_direction]
  - expect: The sock sinks or settles among the shirts.
  - fail: It floats above the water; or rises out; or hangs.
- P5 [fatal · permanence_count]
  - expect: One sock and the shirts keep their number.
  - fail: A second sock appears; or a shirt vanishes; or the sock passes through the basin.
- P6 [minor · attribute_drift]
  - expect: The basin and the room stay the same.
  - fail: The basin changes colour; or the room rearranges; or the shirts change shape.

**Note.** The hand is the minimal trigger; the person is not judged.

