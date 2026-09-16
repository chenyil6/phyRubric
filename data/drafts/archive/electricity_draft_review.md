# Electricity caption rewrite draft — changed records only

Two principles: (1) **no people** unless the body is the physics; (2) the key change is **visible within 5-10 s**. Tags: **person** = whole person removed (passive voice, object-state or environment trigger, or a machine in place of the worker; a body part only where it is the acting tool; hair kept where hair is the charged object) · **timescale** = slow process cut to its seconds-scale sub-event · **expectation** = re-worded to match, not loosened · **scene** = a different scene testing the same physics · **keep_person** = body is the phenomenon, left as is · **note** = unchanged, comment only · **delete** = proposed deletion (apply_draft.py skips it). Unchanged records are omitted here but present in the JSON.

Counts: 202 records; applied 162, expectation 23, keep_person 1, note 2, person 160, scene 19, timescale 2, unchanged 37.

## Proposed deletions


## Delete candidates (user decides; a rewrite is still given)

- **ELEC-0036** (switch_light): the clap must be seen, so hands stay. Delete candidate: the judge cannot verify the sound, only the timing of the hands
- **ELEC-0138** (spark): physics weak: flint on flint gives only a faint glow; flint on steel is the classic case but duplicates ELEC-0139; delete candidate
- **ELEC-0184** (static): the flinch was the only visible sign of the shock; the spark is the visible physics. Delete candidate if such a small spark is judged unrenderable

## Near-duplicate clusters (thin out to 3-5 per phenomenon)

- **switch_light / plug_power: whole string lights or dies together**: ELEC-0009, ELEC-0027, ELEC-0059→ELEC-0058, ELEC-0064→ELEC-0063  († = removed)
- **plug_power: non-events (nothing changes on screen)**: ELEC-0050†, ELEC-0071†, ELEC-0079†  († = removed)
- **lightning: 'X is lit for an instant' with no other physics**: ELEC-0089→ELEC-0085, ELEC-0103†, ELEC-0107→ELEC-0099, ELEC-0108†, ELEC-0110†, ELEC-0111†, ELEC-0113→ELEC-0102, ELEC-0114†, ELEC-0115→ELEC-0103, ELEC-0121†, ELEC-0122→ELEC-0106, ELEC-0123†, ELEC-0124†, ELEC-0125†, ELEC-0087→ELEC-0083, ELEC-0092→ELEC-0088  († = removed)
- **lightning: flash first, reaction later**: ELEC-0094†, ELEC-0100→ELEC-0094, ELEC-0119†  († = removed)
- **spark: sparks trail behind a moving vehicle**: ELEC-0130→ELEC-0111, ELEC-0136→ELEC-0117, ELEC-0137→ELEC-0118, ELEC-0145†, ELEC-0146→ELEC-0126, ELEC-0149→ELEC-0128, ELEC-0157→ELEC-0133, ELEC-0159†, ELEC-0163†, ELEC-0166†  († = removed)
- **spark: grinding-wheel spark fans**: ELEC-0127→ELEC-0108, ELEC-0134→ELEC-0115, ELEC-0148†, ELEC-0161†  († = removed)
- **magnet: small steel object jumps up to a lowered magnet**: ELEC-0169→ELEC-0141, ELEC-0176†, ELEC-0182→ELEC-0153, ELEC-0195→ELEC-0164, ELEC-0201†, ELEC-0209→ELEC-0176  († = removed)
- **magnet: magnet drives an object through a barrier**: ELEC-0171→ELEC-0143, ELEC-0172→ELEC-0144, ELEC-0204→ELEC-0172  († = removed)
- **magnet: object sticks to a vertical steel surface**: ELEC-0168→ELEC-0140, ELEC-0180→ELEC-0151, ELEC-0184†, ELEC-0194†, ELEC-0197→ELEC-0166, ELEC-0203→ELEC-0171, ELEC-0205†, ELEC-0208→ELEC-0175  († = removed)
- **static: bits jump to a rubbed balloon / ruler**: ELEC-0212→ELEC-0179, ELEC-0221†, ELEC-0227†, ELEC-0244→ELEC-0199, ELEC-0249→ELEC-0202  († = removed)
- **static: hair stands up**: ELEC-0211→ELEC-0178, ELEC-0213→ELEC-0180, ELEC-0218→ELEC-0185, ELEC-0224→ELEC-0189, ELEC-0228†, ELEC-0240†, ELEC-0250†  († = removed)
- **static: sparks in fabric in the dark**: ELEC-0223→ELEC-0188, ELEC-0232→ELEC-0192, ELEC-0242→ELEC-0197  († = removed)
- **static: shock felt (flinch only)**: ELEC-0217→ELEC-0184, ELEC-0222†, ELEC-0233†, ELEC-0248†  († = removed)
- **static: fabric / film clings**: ELEC-0214→ELEC-0181, ELEC-0215→ELEC-0182, ELEC-0225†, ELEC-0226→ELEC-0190, ELEC-0229→ELEC-0191, ELEC-0235→ELEC-0194, ELEC-0236→ELEC-0195, ELEC-0237†, ELEC-0243→ELEC-0198, ELEC-0245†  († = removed)

† = proposed deletion above


## switch_light (40 of 42 touched)

### ELEC-0001  `person`
- old caption: A woman flips the wall switch in a dark hallway, and the ceiling light comes on.
- **new caption:** The wall switch in a dark hallway is flipped up, and the ceiling light comes on.

### ELEC-0002  `person`  — 'the same wall switch' referred to ELEC-0001; made standalone
- old caption: A man flips the same wall switch back down, and the ceiling light goes off.
- **new caption:** The wall switch in a lit hallway is flipped down, and the ceiling light goes off.

### ELEC-0003  `person + scene`  — user: one action per caption (was on-then-off)
- old caption: A child pulls the cord on a bedside lamp, and the lamp lights up; she pulls it again and it goes dark.
- **new caption:** The cord of a bedside lamp is pulled, and the lamp lights up.
- old expectation: Each pull changes the lamp's state at the moment of the click, alternating on and off; the lamp never changes without a pull.
- **new expectation:** The lamp comes on at the click of the pull and stays on; it does not light before the pull or flicker afterwards.

### ELEC-0004  `person + scene`  — user: one action per caption (was on-then-off)
- old caption: A man presses the button on a flashlight, and the beam comes on; he presses it again and the beam goes out.
- **new caption:** A flashlight lying on a table and pointed at a wall is switched on, and a bright spot appears on the wall.
- old expectation: The beam appears and disappears exactly with the clicks; while on, the beam is steady.
- **new expectation:** The spot appears on the wall exactly at the click and stays steady; nothing is lit before the switch.

### ELEC-0005  `person`
- old caption: A woman points a remote at a television and presses the power button, and the screen lights up.
- **new caption:** The power button on a remote pointed at a television is pressed, and the screen lights up.

### ELEC-0006  `person`
- old caption: A driver turns the headlight knob on the dashboard, and the headlights come on and the dashboard dials light up.
- **new caption:** The headlight knob on a car's dashboard is turned, and the headlights come on and the dashboard dials light up.

### ELEC-0007  `person + expectation`
- old caption: A boy unscrews a glowing bulb from a table lamp, and the bulb goes dark as it comes loose.
- **new caption:** A glowing bulb is unscrewed from a table lamp, and it goes dark as it comes loose.
- old expectation: The bulb goes out at the moment it loses contact in the socket and stays dark in his hand; it does not keep glowing once removed.
- **new expectation:** The bulb goes out at the moment it loses contact in the socket and stays dark once removed; it does not keep glowing on its own.

### ELEC-0009  `person`  — cluster: ELEC-0009 / 0027 (Christmas lights, switch) / 0059 (same string unplugged) / 0064 (garland, battery pack) all test 'all bulbs together'
- old caption: A man plugs a string of fairy lights into the wall socket, and the whole string lights up along its length.
- **new caption:** A string of fairy lights is plugged into a wall socket, and the whole string lights up along its length.

### ELEC-0010  `person`
- old caption: A woman presses the button on an electric kettle, and a small light on the kettle comes on and the switch stays down.
- **new caption:** The button on an electric kettle is pressed, and a small light on the kettle comes on and the switch stays down.

### ELEC-0011  `person`
- old caption: A child turns the knob of a night light in a dark bedroom, and the little lamp glows.
- **new caption:** The knob of a night light in a dark bedroom is turned, and the little lamp glows.

### ELEC-0012  `person`
- old caption: A man switches on a power strip with four lamps plugged into it, and all four lamps come on at once.
- **new caption:** A power strip with four lamps plugged into it is switched on, and all four lamps come on at once.

### ELEC-0013  `person`
- old caption: A woman presses the power button on a laptop, and the screen lights up and the keyboard glows.
- **new caption:** The power button on a laptop is pressed, and the screen lights up and the keyboard glows.

### ELEC-0014  `person`
- old caption: A boy flicks a light switch up and down several times quickly, and the ceiling light goes on and off in step with each flick.
- **new caption:** A light switch is flicked up and down several times in quick succession, and the ceiling light goes on and off in step with each flick.

### ELEC-0015  `person + expectation`  — 'until the elevator arrives' cannot be checked in a short clip
- old caption: A man presses the button on a wall to call an elevator, and the button lights up.
- **new caption:** The call button beside an elevator is pressed, and the button lights up.
- old expectation: The button glows from the moment it is pressed and stays lit until the elevator arrives; it does not light before being pressed.
- **new expectation:** The button glows from the moment it is pressed and stays lit; it does not light before being pressed.

### ELEC-0016  `person`
- old caption: A woman pulls the chain on a ceiling fan light, and the light above the fan comes on while the blades stay still.
- **new caption:** The light chain on a ceiling fan is pulled, and the light above the fan comes on while the blades stay still.

### ELEC-0017  `person + scene`  — user: one action per caption (was on-then-off)
- old caption: A man switches on a hairdryer, and it roars and blows hot air; he switches it off and it winds down.
- **new caption:** A hairdryer resting on a counter with ribbons tied to its nozzle is switched on, and the ribbons stream out in the airflow.
- old expectation: The airflow starts with the switch and stops within a second of it being turned off; the dryer does not run with the switch off.
- **new expectation:** The ribbons hang slack before the switch, lift and stream the moment it is on, and keep streaming while it runs; they do not move while the dryer is off.

### ELEC-0018  `person`
- old caption: A child presses the button on an electric toothbrush, and the head starts buzzing and vibrating.
- **new caption:** The button on an electric toothbrush lying on a counter is pressed, and the head starts buzzing and vibrating.

### ELEC-0019  `person`
- old caption: A woman presses the button on a garage door opener, and the garage light comes on and the door begins to rise.
- **new caption:** The button on a garage door remote is pressed, and the garage light comes on and the door begins to rise.

### ELEC-0020  `person`
- old caption: A man plugs in and switches on a neon shop sign, and the tubes flicker and then glow steadily.
- **new caption:** A neon shop sign is switched on, and the tubes flicker and then glow steadily.

### ELEC-0021  `person + scene`  — user: one action per caption (was on-then-off)
- old caption: A woman taps the top of a touch-sensitive lamp, and it lights up; she taps again and it goes off.
- **new caption:** The top of a touch-sensitive lamp is tapped, and it lights up.
- old expectation: The lamp changes state at each touch and only at a touch; it does not change while her hand is away.
- **new expectation:** The lamp lights at the touch and stays on; it does not change state without a touch.

### ELEC-0022  `person + scene`  — user rule: one action per caption
- old caption: A boy turns on a remote-controlled toy car with the switch on its underside, and its headlights light up and it responds to the controller.
- **new caption:** The switch on the underside of a remote-controlled toy car is flicked on, and its headlights light up.
- old expectation: The lights come on with the switch and the car moves only when the controller is used; it does not move or light while switched off.
- **new expectation:** The headlights come on with the switch and stay on; the car stays still and does not drive off, since no controller is used; nothing lights while the switch is off.

### ELEC-0023  `person`
- old caption: A woman opens a microwave door, and the light inside the microwave comes on.
- **new caption:** A microwave door is opened, and the light inside the microwave comes on.

### ELEC-0024  `person + scene`  — user: one action per caption (was on-then-off)
- old caption: A man presses the start button on a blender, and the blades spin and the contents whirl; he presses stop and the blades come to rest.
- **new caption:** The start button on a blender is pressed, and the blades spin and the contents whirl.
- old expectation: The blades spin only between the two presses, winding down within a second or two of stop; the contents settle after the blades stop.
- **new expectation:** The blades and contents are still before the press and spin the instant it is pressed, running steadily; nothing moves before the button is touched.

### ELEC-0025  `person + scene`  — user: one action per caption (was on-then-off)
- old caption: A woman turns the knob of a desk fan from off to high, and the blades spin up to speed; she turns it back to off and they slow and stop.
- **new caption:** The knob of a desk fan is turned from off to high, and the blades spin up to speed.
- old expectation: The blades speed up as the knob is turned up and coast to a stop after it is turned off; they do not spin with the knob at off.
- **new expectation:** The blades are still while the knob is at off, start as it turns and speed up to a steady spin; they do not spin with the knob at off.

### ELEC-0027  `person`  — near-duplicate of ELEC-0009
- old caption: A man switches on a string of Christmas lights wound around a tree, and the tree lights up from the plug to the top all at once.
- **new caption:** A string of Christmas lights wound around a tree is switched on, and the tree lights up from the plug to the top all at once.

### ELEC-0028  `person`
- old caption: A cyclist presses the button on her bike's rear light, and it begins to blink red.
- **new caption:** The button on a bicycle's rear light is pressed, and it begins to blink red.

### ELEC-0029  `person`  — user: one action per caption; the stop half duplicated the same cause-effect and crowded the 5 s clip
- old caption: A worker presses the green start button on a conveyor belt, and the belt begins to move; he presses the red button and it stops.
- **new caption:** The green start button on a conveyor belt is pressed, and the belt begins to move.
- old expectation: The belt moves only between the two presses and stops within a moment of the red button; it does not move on its own.
- **new expectation:** The belt is still before the press and starts moving the instant the button is pressed, running steadily in one direction and carrying anything on it along; nothing moves before the press and nothing else in the scene starts moving on its own.

### ELEC-0030  `person`
- old caption: A woman turns the key in a car's ignition, and the dashboard lights up before the engine starts.
- **new caption:** The key in a car's ignition is turned, and the dashboard lights up before the engine starts.

### ELEC-0031  `person + scene`  — user: one action per caption (was on-then-off)
- old caption: A boy switches on a battery-powered lantern in a tent, and the tent lights up; he switches it off and the tent goes dark.
- **new caption:** A battery-powered lantern in a tent is switched on, and the tent lights up.
- old expectation: The light responds instantly to the switch each way and stays steady while on.
- **new expectation:** The tent is dark before the switch and steadily lit from the lantern after it; the light does not appear before the switch.

### ELEC-0032  `person`  — the fingertip is the acting tool for the whole event (the glow lasts only while pressed)
- old caption: A man presses the doorbell button beside a front door, and a small light in the doorbell button glows while he presses.
- **new caption:** A fingertip holds down the doorbell button beside a front door, and a small light in the button glows while it is pressed and goes out when it is released.

### ELEC-0033  `person + timescale + expectation`  — a cold coil takes tens of seconds to glow visibly; the fading of an already red-hot coil is seen within seconds
- old caption: A woman turns the dial on an electric stove burner, and the coil begins to glow red; she turns it off and the glow fades.
- **new caption:** The dial of an electric stove burner is turned off, and the red-hot coil's glow dims.
- old expectation: The glow builds gradually after the dial is turned and fades gradually after it is turned off; the coil does not glow with the dial at off.
- **new expectation:** The glow fades gradually after the dial is turned, from bright to dull red to dark, and never brightens again; it does not go out instantly like a lamp.

### ELEC-0034  `person`
- old caption: A child presses the power button on a handheld game console, and the screen lights up with the start logo.
- **new caption:** The power button on a handheld game console is pressed, and the screen lights up with the start logo.

### ELEC-0035  `person`
- old caption: A man flips the switch on a wall-mounted heater, and its indicator light comes on and its fan starts.
- **new caption:** The switch on a wall-mounted heater is flipped, and its indicator light comes on and its fan starts.

### ELEC-0036  `person`  — the clap must be seen, so hands stay. Delete candidate: the judge cannot verify the sound, only the timing of the hands
- old caption: A woman claps her hands twice in a room with a clap-activated lamp, and the lamp comes on.
- **new caption:** A pair of hands claps twice in a room with a clap-activated lamp, and the lamp comes on.

### ELEC-0037  `person`
- old caption: A man switches on a fluorescent tube in a garage, and it blinks a few times before staying lit.
- **new caption:** A fluorescent tube in a garage is switched on, and it blinks a few times before staying lit.

### ELEC-0038  `person + expectation`  — 'speaker cone can be seen vibrating' is not visible on a toy; dropped
- old caption: A child presses a button on a toy piano, and the key lights up and the toy's speaker cone can be seen vibrating.
- **new caption:** A key on a toy piano is pressed, and the key lights up while it is held down and goes dark when it is released.
- old expectation: The key lights while pressed and goes dark when released; nothing lights or vibrates before the press.
- **new expectation:** The key lights while pressed and goes dark when released; nothing lights before the press.

### ELEC-0039  `person`
- old caption: A woman presses the wall button for an outdoor floodlight, and the yard lights up.
- **new caption:** The wall button for an outdoor floodlight is pressed, and the yard lights up.

### ELEC-0040  `person`
- old caption: A man turns on a shop's escalator with a key switch, and the steps begin to move upward.
- **new caption:** A shop escalator is started with its key switch, and the steps begin to move upward.

### ELEC-0041  `person`
- old caption: A woman presses the button on a coffee machine, and a light comes on and coffee begins to drip into the cup.
- **new caption:** The button on a coffee machine is pressed, and a light comes on and coffee begins to drip into the cup.

### ELEC-0042  `person`
- old caption: A boy switches off the lamp beside his bed, and only the glow of his alarm clock remains in the room.
- **new caption:** The bedside lamp is switched off, and only the glow of the alarm clock's display remains in the dark room.


## plug_power (36 of 38 touched)

### ELEC-0043  `person`
- old caption: A woman pulls the plug of a running table lamp out of the wall socket, and the lamp goes out.
- **new caption:** The plug of a lit table lamp is pulled out of the wall socket, and the lamp goes out.

### ELEC-0044  `person`
- old caption: A man plugs a desk fan into a socket with its switch already on, and the blades start turning.
- **new caption:** A desk fan with its switch already on is plugged into a socket, and the blades start turning.

### ELEC-0045  `person`
- old caption: A child pulls the plug of a television while a programme is playing, and the screen goes black.
- **new caption:** The plug of a television is pulled while a programme is playing, and the screen goes black.

### ELEC-0046  `person`
- old caption: A boy takes the batteries out of a toy robot that is walking, and the robot stops mid-step.
- **new caption:** The batteries are pulled out of a walking toy robot, and the robot stops mid-step.

### ELEC-0047  `person`
- old caption: A woman plugs a charging cable into her phone, and a charging symbol appears on the screen.
- **new caption:** A charging cable is plugged into a phone lying on a table, and a charging symbol appears on the screen.

### ELEC-0048  `person`  — the trip was decorative; the yank is enough
- old caption: A man trips over an extension cord and pulls it out of the wall, and the lamp, radio and heater plugged into it all go off together.
- **new caption:** An extension cord is yanked out of the wall socket, and the lamp, radio and heater plugged into it all go off together.

### ELEC-0049  `person + scene`  — user rule: one action per caption
- old caption: A girl slides two batteries into a flashlight and screws the cap back on, and when she presses the switch the light comes on.
- **new caption:** Two batteries are slid into a flashlight whose switch is already on, and the light comes on as the cap is screwed down.
- old expectation: The light works only once the batteries are in and the switch is pressed; with the cap off or batteries out it stays dark.
- **new expectation:** The flashlight is dark until the cap closes the circuit and lights at that moment, staying on; it does not light with the batteries out or the cap off.

### ELEC-0050  `person`
- old caption: A woman plugs a charging cable into an electric car, and a light on the charging port comes on.
- **new caption:** A charging cable is plugged into an electric car, and a light on the charging port comes on.

### ELEC-0051  `person`  — judgeability: 'stops blowing' is visible only if something is in the airflow; consider ribbons as in ELEC-0017
- old caption: A man is using a running hairdryer when its cord is pulled out of the socket, and the dryer falls silent and stops blowing.
- **new caption:** The cord of a running hairdryer is pulled out of the socket, and the dryer falls silent and stops blowing.

### ELEC-0052  `person + scene`  — user: one action per caption (was on-then-off)
- old caption: A cook plugs in a blender and presses the button, and the blades spin; she unplugs it and the blades slow and stop.
- **new caption:** A blender with its button held down is plugged into a wall socket, and the blades start spinning.
- old expectation: The blades spin only while the blender is plugged in and the button held; they coast briefly to a stop when unplugged.
- **new expectation:** Nothing moves until the plug goes in; the blades start the instant it does and run steadily; the held button alone does nothing while unplugged.

### ELEC-0053  `person`
- old caption: A woman vacuums a hallway and the vacuum's cord is yanked from the socket by the doorframe, and the vacuum stops.
- **new caption:** The cord of a running vacuum cleaner snags on a doorframe and jerks out of the socket, and the vacuum stops.

### ELEC-0054  `person + scene`  — user: the swap was too many steps for 5 s and a flat vs charged pack looks identical; one action, one consequence, no driving (needs the controller)
- old caption: A boy swaps a flat battery pack in a remote-control car for a charged one, and the car's lights come on and it drives.
- **new caption:** A battery pack is clipped into a remote-control car, and the car's lights come on.
- old expectation: The car is dead with the flat pack and works only after the charged pack is clipped in; it does not move before.
- **new expectation:** The lights are off and the car is still before the pack goes in; the lights come on the instant the pack clicks into place and stay on; the car does not drive off by itself and nothing happens before the pack is in.

### ELEC-0055  `person`
- old caption: A woman connects a power bank to her phone, and a light on the power bank comes on and the phone shows it is charging.
- **new caption:** A power bank is connected to a phone by a cable, and a light on the power bank comes on and the phone shows it is charging.

### ELEC-0056  `timescale + expectation`  — the darkening takes minutes; the clip shows only the switch-on moment. Weak: the cause is not visible
- old caption: Dusk falls on a garden, and the solar garden lights along the path come on one by one.
- **new caption:** In a garden at dusk, the solar lights along the path flicker on one after another.
- old expectation: The lights come on as the sky darkens and stay lit; they do not come on in full daylight.
- **new expectation:** The lights come on while the sky is already dim and stay lit; they do not come on in full daylight and do not go out again.

### ELEC-0057  `person`
- old caption: A camper starts a portable generator, and the string of lights connected to it comes on.
- **new caption:** A portable generator at a campsite is started, and the string of lights connected to it comes on.

### ELEC-0058  `person`  — reverse of ELEC-0009; near-duplicate
- old caption: A man unplugs a string of fairy lights from the wall, and the whole string goes dark.
- **new caption:** A string of fairy lights is unplugged from the wall, and the whole string goes dark.

### ELEC-0059  `person`
- old caption: A woman removes the battery from an e-bike, and the display on the handlebars goes dark.
- **new caption:** The battery is unlatched from an e-bike, and the display on the handlebars goes dark.

### ELEC-0060  `person`
- old caption: A child places a toy train on its track and switches on the track's power pack, and the train begins to run.
- **new caption:** A toy train is placed on its track and the track's power pack switched on, and the train begins to run.

### ELEC-0061  `person`
- old caption: A man unplugs a glowing electric heater, and the orange glow of its elements fades to dark.
- **new caption:** A glowing electric heater is unplugged, and the orange glow of its elements fades to dark.

### ELEC-0062  `person`
- old caption: A woman unplugs a toaster while its coils are glowing, and the coils fade and the lever pops up.
- **new caption:** A toaster is unplugged while its coils are glowing, and the coils fade and the lever pops up.

### ELEC-0063  `person`  — near-duplicate of ELEC-0009/0027
- old caption: A girl slides the switch on a battery pack attached to a garland of lights, and the garland lights up.
- **new caption:** The switch on a battery pack attached to a garland of lights is slid on, and the garland lights up.

### ELEC-0064  `person`
- old caption: A carpenter clips a battery pack into a cordless drill and pulls the trigger, and the drill bit spins.
- **new caption:** A battery pack is clipped into a cordless drill and the trigger pulled, and the drill bit spins.

### ELEC-0066  `person`
- old caption: A woman lifts an electric kettle off its base while it is boiling, and the kettle's light goes off and the boiling quiets.
- **new caption:** An electric kettle is lifted off its base while it is boiling, and the kettle's light goes off and the boiling quiets.

### ELEC-0067  `person + scene`  — user rule: one action per caption
- old caption: A photographer's camera screen goes dark mid-shot as the battery runs out, and the camera will not turn back on.
- **new caption:** A camera's screen goes dark mid-recording as its battery runs out.
- old expectation: The screen and lights go off and stay off despite button presses; the camera does not revive until a charged battery is inserted.
- **new expectation:** The screen and the camera's lights go off together and stay off; the camera does not come back to life on its own.

### ELEC-0068  `person`
- old caption: A man unplugs a digital alarm clock to move it, and its glowing display goes blank.
- **new caption:** A digital alarm clock is unplugged, and its glowing display goes blank.

### ELEC-0069  `person`
- old caption: A woman plugs a laptop charger into the wall and then into the laptop, and the small light on the charger connector comes on.
- **new caption:** A laptop charger is plugged into the wall and then into the laptop, and the small light on the charger connector comes on.

### ELEC-0070  `person`
- old caption: A man plugs a lamp into a socket and switches on the socket at the wall, and the lamp lights.
- **new caption:** A lamp is plugged into a socket and the socket switched on at the wall, and the lamp lights.

### ELEC-0071  `person`
- old caption: A worker connects jumper cables from a running car to a dead car, and the dead car's dashboard lights come on.
- **new caption:** Jumper cables from a running car are clamped onto a dead car's battery, and the dead car's dashboard lights come on.

### ELEC-0072  `person`
- old caption: A woman unplugs a running sewing machine, and the needle stops and its work light goes out.
- **new caption:** A running sewing machine is unplugged, and the needle stops and its work light goes out.

### ELEC-0073  `person`
- old caption: A man puts a coin-cell battery into a wristwatch, and the second hand starts to tick.
- **new caption:** A coin-cell battery is pressed into a wristwatch lying face up, and the second hand starts to tick.

### ELEC-0075  `person`
- old caption: A child plugs a nightlight into a low wall socket, and it begins to glow.
- **new caption:** A nightlight is plugged into a low wall socket, and it begins to glow.

### ELEC-0076  `person`
- old caption: A man plugs an aquarium pump into the wall, and bubbles start rising from the air stone in the tank.
- **new caption:** An aquarium pump is plugged into the wall, and bubbles start rising from the air stone in the tank.

### ELEC-0077  `person`
- old caption: A teenager's laptop is unplugged from its charger, and the charging light on it goes off while the screen stays on.
- **new caption:** A laptop is unplugged from its charger, and the charging light on it goes off while the screen stays on.

### ELEC-0078  `person`
- old caption: A woman plugs an electric blanket in and switches it on, and its small control light comes on.
- **new caption:** An electric blanket is plugged in and switched on, and its small control light comes on.

### ELEC-0079  `person + scene + expectation`  — the scooter needs a rider; a toy car shows the same power loss unmanned
- old caption: A boy's electric scooter slows and stops as its battery runs flat, and its display goes dark.
- **new caption:** A battery-powered toy car slows and stops as its battery runs flat, and its headlights dim and go out.
- old expectation: The scooter loses power gradually and stops; the display goes off; pressing the throttle does nothing afterward.
- **new expectation:** The car loses speed gradually and stops; the lights dim and go out around the same time and do not come back; it does not speed up again.

### ELEC-0080  `person`
- old caption: A man wheels an electric lawnmower out of range and its cord pulls out of the socket, and the mower stops.
- **new caption:** An electric lawnmower reaches the end of its cord and the plug pulls out of the socket, and the mower stops.


## lightning (4 of 26 touched)

### ELEC-0083  `person`
- old caption: A family sits in a living room during a storm, and a flash of lightning through the window lights the whole room for an instant.
- **new caption:** An empty living room lit by a single lamp during a storm brightens for an instant as lightning flashes through the window.

### ELEC-0088  `person`
- old caption: A couple sits in a parked car in a rainstorm, and a lightning flash lights the inside of the car through the rain-streaked windows.
- **new caption:** Lightning flashes outside an empty parked car in a rainstorm, and the inside of the car lights up through the rain-streaked windows for an instant.

### ELEC-0094  `note`  — an animal's reaction, not a person's; it is the only visible sign of thunder, so keep this as the single flash-then-reaction item
- caption unchanged: A dog lying in a hallway jumps up as a lightning flash lights the windows and the house shakes with thunder.

### ELEC-0106  `person`
- old caption: A camper in a tent sees the canvas light up from a lightning flash outside, then go dark again.
- **new caption:** The canvas of a pitched tent lights up from a lightning flash outside, then goes dark again.


## spark (23 of 33 touched)

### ELEC-0107  `person + scene + expectation`  — the welder becomes a machine; same physics
- old caption: A welder touches the rod to a steel beam, and a shower of bright sparks bursts from the joint and falls to the floor.
- **new caption:** A robotic welding arm touches down on a steel car body on an assembly line, and a shower of bright sparks bursts from the joint and falls to the floor.
- old expectation: Sparks appear only while the rod touches the metal, fly outward and downward, and go dark within a short distance; they do not rise or linger on the floor as lights.
- **new expectation:** Sparks appear only while the arm's tip touches the metal, fly outward and downward, and go dark within a short distance; they do not rise or linger on the floor as lights.

### ELEC-0108  `person`
- old caption: A worker presses a spinning angle grinder against a metal pipe, and a fan of orange sparks streams off the wheel.
- **new caption:** A spinning angle grinder is pressed against a metal pipe clamped in a vise, and a fan of orange sparks streams off the wheel.

### ELEC-0109  `person`
- old caption: A man yanks the plug of a running heater out of the wall socket, and a small spark snaps at the prongs as they come out.
- **new caption:** The plug of a running heater is yanked out of the wall socket, and a small spark snaps at the prongs as they come out.

### ELEC-0110  `person`
- old caption: A mechanic touches the second jumper-cable clamp to a car battery terminal, and a spark jumps at the contact.
- **new caption:** The second jumper-cable clamp is touched to a car battery terminal, and a spark jumps at the contact.

### ELEC-0114  `person`
- old caption: A cook strikes a flint gas-lighter over a stove burner, and a spark jumps from its tip and the gas ignites.
- **new caption:** A flint gas-lighter is clicked over a stove burner, and a spark jumps from its tip and the gas ignites.

### ELEC-0117  `note`  — riders in the bumper cars are incidental and not named; left as is
- caption unchanged: Bumper cars race under a metal ceiling grid, and their poles throw small sparks where they scrape along it.

### ELEC-0120  `person`
- old caption: A hiker strikes a ferro rod with a striker, and sparks spray onto the tinder below.
- **new caption:** A striker is scraped down a ferro rod held over a pile of tinder, and sparks spray onto the tinder below.

### ELEC-0121  `person`
- old caption: A worker cuts a steel bar with a cut-off saw, and a long plume of sparks shoots out behind the blade and rains onto the floor.
- **new caption:** The blade of a chop saw comes down on a steel bar clamped in its jaws, and a long plume of sparks shoots out behind the blade and rains onto the floor.

### ELEC-0123  `person + scene`  — blacksmith replaced by a power hammer
- old caption: A blacksmith hammers a red-hot bar on an anvil, and tiny sparks fly off with each blow.
- **new caption:** A power hammer in a forge pounds a red-hot steel bar, and tiny sparks fly off with each blow.

### ELEC-0124  `person`
- old caption: A boy drags a metal rake along a concrete path in the dark, and faint sparks flick from the tines.
- **new caption:** A metal rake is dragged along a concrete path in the dark, and faint sparks flick from the tines.

### ELEC-0125  `person`
- old caption: A worker touches a live wire to a metal bracket by mistake, and a bright spark flashes and leaves a black mark.
- **new caption:** A live wire brushes against a metal bracket, and a bright spark flashes and leaves a black mark.

### ELEC-0126  `person + scene + expectation`  — the rider stays as part of the vehicle but is no longer the subject; the footpeg replaces the knee slider
- old caption: A stunt rider drags a metal knee slider along the track in a turn, and sparks trail out behind it.
- **new caption:** A motorcycle leaning hard through a turn scrapes its metal footpeg along the track, and sparks trail out behind it.
- old expectation: The sparks stream backward from the point of contact and die out along the track; they stop when the slider lifts.
- **new expectation:** The sparks stream backward from the point of contact and die out along the track; they stop when the peg lifts off the track.

### ELEC-0127  `person`
- old caption: A woman plugs a phone charger into a worn socket, and a small spark flashes at the plug as it goes in.
- **new caption:** A phone charger is plugged into a worn socket, and a small spark flashes at the plug as it goes in.

### ELEC-0129  `person`
- old caption: A worker with a plasma cutter slices a steel sheet, and a fountain of sparks pours from the underside of the cut.
- **new caption:** A CNC plasma cutter slices a steel sheet, and a fountain of sparks pours from the underside of the cut.

### ELEC-0130  `person`
- old caption: A cook flicks a stovetop lighter, and a blue spark jumps between its two metal tips.
- **new caption:** A stovetop lighter is clicked, and a blue spark jumps between its two metal tips.

### ELEC-0131  `person`
- old caption: An electrician tests a wire and it shorts against the box, and a flash and puff of smoke come from the spot.
- **new caption:** A loose wire in an open junction box shorts against the box, and a flash and puff of smoke come from the spot.

### ELEC-0133  `person + scene + expectation`  — skateboarder replaced by an unmanned friction-spark scene
- old caption: A skateboarder grinds a metal rail at night, and sparks trail from the truck along the rail.
- **new caption:** A car with a dragging exhaust pipe drives down a road at night, and sparks trail behind it where the pipe scrapes the asphalt.
- old expectation: Sparks appear along the contact and stream behind the board; they stop when the board leaves the rail.
- **new expectation:** Sparks appear along the contact and stream behind the car; they stop when the pipe lifts off the road.

### ELEC-0134  `person`
- old caption: A worker starts an arc welder and the arc lights the whole garage in blue-white, throwing hard shadows.
- **new caption:** An arc welder is struck behind a screen in a garage, and the arc lights the whole garage in blue-white, throwing hard shadows.

### ELEC-0135  `person`
- old caption: A man throws a switch on an old-fashioned knife switch panel, and a small arc snaps at the contacts as they close.
- **new caption:** An old-fashioned knife switch is thrown closed, and a small arc snaps at the contacts as they close.

### ELEC-0136  `person`
- old caption: Fireworks technicians test an igniter and it sparks briefly at the wire ends before the fuse catches.
- **new caption:** An electric igniter is fired, and it sparks briefly at the wire ends before the fuse catches.

### ELEC-0137  `person`
- old caption: A machinist runs a lathe cutting steel, and glowing chips and sparks curl off the tool and drop into the tray.
- **new caption:** A lathe cuts a spinning steel bar, and glowing chips and sparks curl off the tool and drop into the tray.

### ELEC-0138  `person`  — physics weak: flint on flint gives only a faint glow; flint on steel is the classic case but duplicates ELEC-0139; delete candidate
- old caption: A boy strikes two pieces of flint together in the dark, and a tiny spark jumps between them.
- **new caption:** Two pieces of flint are struck together in the dark, and a tiny spark jumps between them.

### ELEC-0139  `person`
- old caption: A worker chips a concrete floor with a steel chisel and hammer, and an occasional spark flicks from where the chisel strikes embedded stone.
- **new caption:** A demolition hammer chips a concrete floor, and an occasional spark flicks where the bit strikes embedded stone.


## magnet (36 of 37 touched)

### ELEC-0140  `person`
- old caption: A woman presses a small magnet against a refrigerator door and lets go, and the magnet stays stuck on the door.
- **new caption:** A small magnet is pressed against a refrigerator door and released, and it stays stuck on the door.

### ELEC-0141  `person`
- old caption: A boy holds a magnet just above a pile of paperclips on a desk, and the clips jump up and cling to the magnet.
- **new caption:** A magnet is lowered toward a pile of paperclips on a desk, and the clips jump up and cling to it.

### ELEC-0142  `person`
- old caption: A man sweeps a magnet over a mix of nails and plastic beads spilled on the floor, and the nails stick to the magnet while the beads stay behind.
- **new caption:** A magnet is swept over a mix of nails and plastic beads spilled on the floor, and the nails stick to the magnet while the beads stay behind.

### ELEC-0143  `person`
- old caption: A girl places a sheet of paper over a paperclip and moves a magnet across the top of the paper, and the clip follows the magnet under the paper.
- **new caption:** A sheet of paper lies over a paperclip, and a magnet is moved across the top of the paper; the clip follows the magnet under the paper.

### ELEC-0144  `person`
- old caption: A child slides a magnet along the underside of a thin wooden table, and a toy car with a metal base on top of the table follows it.
- **new caption:** A magnet is slid along the underside of a thin wooden table, and a toy car with a metal base on top of the table follows it.

### ELEC-0145  `person`
- old caption: A cook holds a kitchen knife up to a magnetic strip on the wall, and the knife snaps onto the strip and stays there.
- **new caption:** A kitchen knife is brought up to a magnetic strip on the wall, and the knife snaps onto the strip and stays there.

### ELEC-0146  `person`
- old caption: A driver brings a phone near a magnetic mount on the dashboard, and the phone snaps onto the mount and holds.
- **new caption:** A phone is brought near a magnetic mount on a car's dashboard, and the phone snaps onto the mount and holds.

### ELEC-0147  `person`
- old caption: A child pushes two toy train cars with magnetic couplers together, and they snap together and roll as one.
- **new caption:** Two toy train cars with magnetic couplers are pushed together, and they snap together and roll as one.

### ELEC-0148  `person`
- old caption: A man brings two bar magnets together end to end, and they snap together with a click.
- **new caption:** Two bar magnets are brought together end to end, and they snap together with a click.

### ELEC-0149  `person`
- old caption: A boy tries to push the like ends of two bar magnets together on a table, and the second magnet slides away from the first.
- **new caption:** One bar magnet is pushed toward the like end of another lying on a table, and the second magnet slides away from the first.

### ELEC-0150  `person`
- old caption: A woman closes a cabinet door with a magnetic latch, and the door pulls itself shut the last inch and stays closed.
- **new caption:** A cabinet door with a magnetic latch is swung shut, and the door pulls itself closed the last little way and stays closed.

### ELEC-0151  `person`
- old caption: A mechanic sets a magnetic parts tray on the side of a car and drops screws into it, and the tray and the screws stay put.
- **new caption:** A magnetic parts tray is set on the side of a car and screws dropped into it, and the tray and the screws stay put.

### ELEC-0152  `person`
- old caption: A woman closes a handbag whose flap has a magnetic clasp, and the flap snaps down and holds.
- **new caption:** The flap of a handbag with a magnetic clasp is let fall, and the flap snaps down and holds.

### ELEC-0153  `person`
- old caption: A man lowers a horseshoe magnet over a steel key on a table, and the key jumps up and sticks to the magnet.
- **new caption:** A horseshoe magnet is lowered over a steel key on a table, and the key jumps up and sticks to the magnet.

### ELEC-0154  `expectation`  — caption was already passive; expectation mentioned 'the hand'
- caption unchanged: A magnet held to a refrigerator is slid down the door, and it slides and stays stuck the whole way.
- old expectation: The magnet moves only where the hand pushes it and stays on the door when released at any point; it does not drop off.
- **new expectation:** The magnet moves only while it is pushed and stays on the door when released at any point; it does not drop off.

### ELEC-0155  `person + expectation`
- old caption: A cook moves a magnet toward a steel saucepan on the counter, and the magnet jumps out of her fingers and clicks onto the pan.
- **new caption:** A magnet is moved toward a steel saucepan on the counter, and the magnet jumps the last gap and clicks onto the pan.
- old expectation: The magnet leaps the last small gap and sticks; it stays on the pan when she lets go.
- **new expectation:** The magnet leaps the last small gap and sticks; it stays on the pan when released.

### ELEC-0156  `person`
- old caption: A carpenter holds a screwdriver with a magnetic tip to a loose screw, and the screw clings to the tip and is lifted away.
- **new caption:** A screwdriver with a magnetic tip is held to a loose screw, and the screw clings to the tip and is lifted away.

### ELEC-0157  `person`
- old caption: A woman drops a steel washer near a strong magnet on a table, and the washer swerves toward the magnet and sticks to it.
- **new caption:** A steel washer is dropped near a strong magnet on a table, and the washer swerves toward the magnet and sticks to it.

### ELEC-0158  `person`
- old caption: A child builds a tower with magnetic tiles, and each tile clicks onto the last and the tower stands.
- **new caption:** Magnetic tiles are stacked one onto another, and each tile clicks onto the last and the tower stands.

### ELEC-0159  `person`
- old caption: A boy tilts a travel chess board with magnetic pieces, and the pieces stay in their squares.
- **new caption:** A travel chess board with magnetic pieces is tilted steeply, and the pieces stay in their squares while a coin placed on the board slides off.

### ELEC-0161  `person`
- old caption: A woman pins a magnetic name badge to her blouse by placing the magnet inside the fabric, and the badge holds in place.
- **new caption:** A magnetic name badge is placed on a jacket hanging on a hook by putting the magnet inside the fabric, and the badge holds in place.

### ELEC-0162  `person`
- old caption: A man swings a door until it reaches a magnetic doorstop, and the door snaps to the stop and holds open.
- **new caption:** A door blown open by a draught swings until it reaches a magnetic doorstop, and the door snaps to the stop and holds open.

### ELEC-0163  `person + scene`  — user: one action per caption (was on-then-off)
- old caption: A girl holds a magnet near a compass, and the needle swings to point at the magnet; she takes the magnet away and the needle swings back.
- **new caption:** A magnet is brought near a compass, and the needle swings to point at the magnet.
- old expectation: The needle turns only when the magnet is near and follows it as it moves; it returns to its original direction when the magnet is removed.
- **new expectation:** The needle turns only as the magnet approaches and follows the magnet as it moves; it does not move before the magnet is near.

### ELEC-0164  `person`
- old caption: A child drags a magnetic wand over a tray of iron filings, and the filings clump onto the wand in fuzzy bristles.
- **new caption:** A magnetic wand is dragged over a tray of iron filings, and the filings clump onto the wand in fuzzy bristles.

### ELEC-0165  `person`
- old caption: A woman drops a handful of steel pins near a magnet, and the pins swing toward it as they fall and stick along its sides.
- **new caption:** A handful of steel pins is dropped near a magnet, and the pins swing toward it as they fall and stick along its sides.

### ELEC-0166  `person`
- old caption: A man hangs a magnetic hook on the side of a steel filing cabinet and hangs a coat on it, and the hook holds.
- **new caption:** A magnetic hook is hung on the side of a steel filing cabinet and a coat hung on it, and the hook holds.

### ELEC-0167  `person`
- old caption: A child holds a magnet against a plastic toy, lets go, and the magnet falls to the floor.
- **new caption:** A magnet is held against a plastic toy and released, and the magnet falls to the floor.

### ELEC-0168  `person + expectation`
- old caption: A woman fastens a bracelet with a magnetic clasp, and the two ends jump together and hold.
- **new caption:** The two ends of a bracelet with a magnetic clasp are brought close on a table, and they jump together and hold.
- old expectation: The ends pull together over the last small gap and stay joined as her wrist moves.
- **new expectation:** The ends pull together over the last small gap and stay joined when the bracelet is lifted.

### ELEC-0169  `person`
- old caption: A man tosses a steel bolt toward a strong magnet fixed to a workbench, and the bolt swerves and clacks onto the magnet.
- **new caption:** A steel bolt is tossed toward a strong magnet fixed to a workbench, and the bolt swerves and clacks onto the magnet.

### ELEC-0170  `person`
- old caption: A shopper picks up a box of magnetic building blocks, and the blocks inside cling together in a chain when one is lifted out.
- **new caption:** One block is lifted out of a box of magnetic building blocks, and the others cling to it in a hanging chain.

### ELEC-0171  `person`
- old caption: A woman sticks a magnet to a steel lamp post and hangs a lost-cat poster from it, and the poster stays up.
- **new caption:** A magnet is stuck to a steel lamp post with a lost-cat poster under it, and the poster stays up.

### ELEC-0172  `person`
- old caption: A child moves a magnet in circles under a shallow dish of water with a paperclip floating on a piece of foam, and the clip follows the magnet around the dish.
- **new caption:** A magnet is moved in circles under a shallow dish of water with a paperclip floating on a piece of foam, and the clip follows the magnet around the dish.

### ELEC-0173  `person`
- old caption: A child drops a magnet into a bowl of dry rice mixed with steel ball bearings, and when she pulls it out the bearings cling to it while the rice falls away.
- **new caption:** A magnet is dropped into a bowl of dry rice mixed with steel ball bearings and pulled out again, and the bearings cling to it while the rice falls away.

### ELEC-0174  `person`
- old caption: A woman closes a laptop, and its lid snaps shut over the last centimetre and stays closed thanks to the magnets inside.
- **new caption:** A laptop lid is lowered, and it snaps shut over the last small gap and stays closed thanks to the magnets inside.

### ELEC-0175  `person`
- old caption: A boy sticks a magnetic letter to a fridge, and it holds; he sticks one to the wooden cupboard next to it, and it falls off.
- **new caption:** A magnetic letter is stuck to a fridge and holds; the same letter is stuck to the wooden cupboard next to it and falls off.

### ELEC-0176  `person`
- old caption: A mechanic reaches into an engine bay with a magnetic pickup tool, and a dropped nut clicks onto its tip and is lifted out.
- **new caption:** A magnetic pickup tool is lowered into an engine bay toward a dropped nut, and the nut clicks onto its tip and is lifted out.


## static (26 of 26 touched)

### ELEC-0177  `person`
- old caption: A girl rubs a balloon on her hair and presses it against a wall, and the balloon stays stuck to the wall when she lets go.
- **new caption:** A balloon is rubbed on a wool sweater and pressed against a wall, and it stays stuck to the wall when released.

### ELEC-0178  `person`  — the hair is the charged object; no identity, no face
- old caption: A boy rubs a balloon on his sweater and holds it near his sister's head, and her hair rises toward the balloon.
- **new caption:** A balloon rubbed on a wool sweater is held near a head of long hair, and the hair rises toward the balloon.

### ELEC-0179  `person`  — cluster: five 'bits jump to a rubbed object' items (0212 paper, 0221 foam beads, 0227 tissue + ruler, 0244 sugar, 0249 sawdust)
- old caption: A child rubs a balloon on a wool jumper and lowers it over small torn scraps of paper on a table, and the scraps jump up and cling to the balloon.
- **new caption:** A balloon rubbed on a wool jumper is lowered over small torn scraps of paper on a table, and the scraps jump up and cling to the balloon.

### ELEC-0180  `person`  — hair is the physics; only the head remains
- old caption: A woman pulls a wool sweater off over her head in a dry room, and her hair stands up in all directions.
- **new caption:** A wool sweater is pulled off over the head in a dry room, and the hair underneath stands up in all directions.

### ELEC-0181  `person`
- old caption: A man pulls clothes out of a tumble dryer, and a sock clings to a shirt and has to be peeled off.
- **new caption:** A shirt is lifted out of a tumble dryer, and a sock clings to it and hangs on until it is peeled off.

### ELEC-0182  `person + expectation`
- old caption: A cook tears a sheet of plastic wrap from the roll, and it clings to her hand and folds onto itself.
- **new caption:** A sheet of plastic wrap is torn from its box, and it clings to the side of the box and folds onto itself instead of hanging straight.
- old expectation: The wrap sticks to her fingers and to itself where it touches, and has to be pulled free; it does not hang straight like paper.
- **new expectation:** The wrap sticks to the box and to itself where it touches and has to be pulled free; it does not hang straight like paper.

### ELEC-0183  `person + expectation`
- old caption: A woman opens a box of packing peanuts, and the foam pieces stick to her arms and to the sides of the box.
- **new caption:** A box of packing peanuts is tipped over a table, and many of the foam pieces stick to the sides and flaps of the box instead of falling out.
- old expectation: The pieces cling to skin and cardboard instead of falling off; they follow her arm as she lifts it.
- **new expectation:** The pieces cling to the cardboard instead of falling and stay there when the box is lifted; the pieces that do fall land normally.

### ELEC-0184  `person + expectation`  — the flinch was the only visible sign of the shock; the spark is the visible physics. Delete candidate if such a small spark is judged unrenderable
- old caption: A boy shuffles across a carpet in socks and reaches for a metal doorknob, and he flinches as he touches it.
- **new caption:** In a dark hallway a fingertip is brought slowly toward a metal doorknob, and a tiny spark jumps from the fingertip to the knob just before they touch.
- old expectation: The flinch happens at the instant of contact with the metal, not before; a tiny spark may be seen at the fingertip.
- **new expectation:** The spark is a single brief flash at the moment of near-contact; nothing glows before or after.

### ELEC-0185  `keep_person`  — the hair standing up after the slide is the phenomenon; the child cannot be removed
- caption unchanged: A child slides down a plastic playground slide, and at the bottom her hair is standing up from her head.

### ELEC-0186  `person + expectation`  — the hand is the acting tool for the whole event
- old caption: A woman pets a cat on a dry winter day, and the cat's fur stands up along its back and clings to her hand.
- **new caption:** A hand strokes a cat's back on a dry winter day, and the fur stands up along its back and clings to the hand.
- old expectation: The fur lifts where her hand passes and follows the hand slightly; it settles after she stops.
- **new expectation:** The fur lifts where the hand passes and follows the hand slightly; it settles after the stroking stops.

### ELEC-0187  `person`
- old caption: A man wipes an old television screen with a cloth, and dust and a few hairs jump onto the screen and stick.
- **new caption:** An old television screen is wiped with a dry cloth, and dust and a few hairs jump onto the screen and stick.

### ELEC-0188  `person`
- old caption: A woman shakes out a fleece blanket in a dark bedroom, and small flickers of light run through the fabric.
- **new caption:** A fleece blanket is shaken out in a dark bedroom, and small flickers of light run through the fabric.

### ELEC-0189  `person`
- old caption: A boy pulls off a wool hat, and his hair stays lifted in the shape of the hat's inside before slowly settling.
- **new caption:** A wool hat is pulled off, and the hair underneath stays lifted in the shape of the hat's inside before slowly settling.

### ELEC-0190  `person + expectation`
- old caption: A man pulls a thin plastic bag off a roll, and it clings to his forearm and will not shake off.
- **new caption:** A thin plastic bag is torn off a roll, and it clings to the roll and to the dispenser instead of dropping away.
- old expectation: The bag lies against his arm and stays when he shakes it; it comes off only when peeled.
- **new expectation:** The bag lies against the roll and dispenser and stays there; it comes off only when peeled.

### ELEC-0191  `person`
- old caption: A cook lifts a sheet of cling film off a bowl, and the film clings back to the bowl's rim and to her fingers.
- **new caption:** A sheet of cling film is lifted off a bowl, and the film clings back to the bowl's rim and to itself.

### ELEC-0192  `person + expectation`
- old caption: A man takes off a fleece jacket in the dark, and tiny sparks crackle where it pulls away from his shirt.
- **new caption:** A fleece jacket is pulled off over a cotton shirt in the dark, and tiny sparks crackle where the fabrics separate.
- old expectation: The sparks appear only as the fabrics separate and vanish instantly; nothing glows when he stops moving.
- **new expectation:** The sparks appear only as the fabrics separate and vanish instantly; nothing glows once the movement stops.

### ELEC-0193  `person + expectation`
- old caption: A man in a wool sweater brushes past a hanging plastic shower curtain, and the curtain clings to his sleeve and follows him for a moment.
- **new caption:** The sleeve of a wool sweater brushes past a hanging plastic shower curtain, and the curtain clings to the sleeve and follows it for a moment.
- old expectation: The curtain lifts toward the sleeve where it touched and trails after him briefly before falling back; it does not move before he passes.
- **new expectation:** The curtain lifts toward the sleeve where it touched and trails after it briefly before falling back; it does not move before the sleeve passes.

### ELEC-0194  `person + expectation`
- old caption: A woman takes a freshly printed stack of paper from a printer, and the sheets cling together and to her fingers.
- **new caption:** A stack of freshly printed sheets is lifted from a printer, and the sheets cling together; a single sheet lifted from the top clings to the stack rather than falling.
- old expectation: The sheets stick and have to be fanned apart; a single sheet clings to the hand rather than falling.
- **new expectation:** The sheets stick and have to be fanned apart; the single sheet hangs on the stack rather than dropping.

### ELEC-0195  `person`
- old caption: A woman lifts a fleece blanket out of the dryer, and a dryer sheet clings to its underside and rides along as the blanket is carried.
- **new caption:** A fleece blanket is lifted out of the dryer, and a dryer sheet clings to its underside and rides along as the blanket is carried.

### ELEC-0196  `person`
- old caption: A man unrolls a sheet of bubble wrap, and small bits of dust and fluff jump onto it from the table.
- **new caption:** A sheet of bubble wrap is unrolled on a table, and small bits of dust and fluff jump onto it from the table.

### ELEC-0197  `person`
- old caption: A man pulls a nylon jacket off a hanger in a dark closet, and faint flickers of light run across the fabric.
- **new caption:** A nylon jacket is pulled off a hanger in a dark closet, and faint flickers of light run across the fabric.

### ELEC-0198  `person + expectation`
- old caption: A woman peels a sticker from its backing sheet, and the backing clings to her fingers and curls toward the sticker.
- **new caption:** A sticker is peeled from its backing sheet, and the thin backing curls toward the sticker and clings to it instead of lying flat.
- old expectation: The thin backing sticks to skin and has to be shaken or pulled off; it does not drop straight away.
- **new expectation:** The backing lifts and clings to the sticker where they come close and has to be pulled apart; it does not fall flat straight away.

### ELEC-0199  `person`
- old caption: A child rubs a balloon on a sweater and holds it over a bowl of sugar, and a fine dusting of sugar jumps up to the balloon.
- **new caption:** A balloon rubbed on a sweater is held over a bowl of sugar, and a fine dusting of sugar jumps up to the balloon.

### ELEC-0200  `person + scene + expectation`  — duplicate of ELEC-0211 (hair) once de-personed; feathers give a different object
- old caption: A girl rubs a balloon on her hair and touches it to the tip of her nose, and a few strands of her hair lift toward the balloon.
- **new caption:** A balloon rubbed on a wool sweater is held beside a feather duster standing in a jar, and the feathers lean toward the balloon.
- old expectation: The strands rise toward the balloon while it is close and fall when it is pulled back.
- **new expectation:** The feathers lift toward the balloon while it is close and fall back when it is pulled away.

### ELEC-0201  `person + expectation`
- old caption: A woman opens a bag of styrofoam beads and pours some into a bowl, and beads stick to the bag and to her hands rather than all falling in.
- **new caption:** A bag of styrofoam beads is poured into a bowl, and beads stick to the bag's sides and to the rim rather than all falling in.
- old expectation: Some beads cling to the bag's sides and to skin while most fall; the clinging beads stay until brushed off.
- **new expectation:** Some beads cling to the bag and the rim while most fall; the clinging beads stay until brushed off.

### ELEC-0202  `person`
- old caption: A child rubs an inflated balloon on the carpet and rolls it near a pile of fine sawdust, and sawdust jumps onto the balloon.
- **new caption:** A balloon rubbed on a carpet is rolled near a pile of fine sawdust, and sawdust jumps onto the balloon.

