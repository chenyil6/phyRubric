#!/usr/bin/env python3
"""Build data/drafts/electricity_draft.json (+ _review.md): proposed rewrites of the Electricity train captions.

Two principles (user, 2026-09-11):
  1. no people      - a person who only flips / plugs / holds is removed: plain passive voice ("The wall switch is
                      flipped up"), an object-state or environment trigger (a door blown open by a draught, a cord that
                      snags on a doorframe), or a machine in place of the worker (robotic welder, power hammer, CNC
                      plasma cutter).  A body part is named only when it is the acting tool for the whole event
                      (a fingertip holding a doorbell, a hand stroking a cat).  Where the body IS the charged object
                      (hair standing up) only the hair / head remains, no identity.  keep_person = the body cannot be
                      removed (hair after a slide, hair on a trampoline).
  2. 5-10 s visible - the key change must happen inside a ~5 s clip.  Electricity is almost all instantaneous; the
                      few slow items (stove coil warming up, dusk falling, a storm approaching) are cut to their
                      seconds-scale sub-event or flagged for deletion.
Also flagged in notes: physics that is wrong or doubtful, non-events (nothing changes on screen), items whose only
visible content is a human reaction (a flinch), and near-duplicate clusters.  `delete` = proposed deletion;
apply_draft.py skips delete-tagged records.  Captions state the event only; the how lives in the expectation.
"""
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data/train/electricity.json"
DST = ROOT / "data/drafts/electricity_draft.json"
REVIEW = ROOT / "data/drafts/electricity_draft_review.md"

O: dict[str, tuple] = {}


def o(i, c=None, e=None, ch=(), note=""):
    O[f"ELEC-{i:04d}"] = (c, e, list(ch), note)


def keep(i, note):
    o(i, None, None, ["keep_person"], note)


def delete(i, reason):
    o(i, None, None, ["delete"], reason)


def flag(i, note):
    o(i, None, None, ["note"], note)


# ---------------------------------------------------------------- switch_light
o(1, "The wall switch in a dark hallway is flipped up, and the ceiling light comes on.", None, ["person"])
o(2, "The wall switch in a lit hallway is flipped down, and the ceiling light goes off.", None, ["person"],
  "'the same wall switch' referred to ELEC-0001; made standalone")
o(3, "The cord of a bedside lamp is pulled, and the lamp lights up; it is pulled again and the lamp goes dark.", None, ["person"])
o(4, "A flashlight lying on a table and pointed at a wall is switched on, and a bright spot appears on the wall; switched off again, the spot goes out.",
  "The spot appears and disappears exactly with the clicks; while on, the beam is steady.", ["person", "expectation"],
  "the beam is made visible as a spot on the wall so there is something to judge")
o(5, "The power button on a remote pointed at a television is pressed, and the screen lights up.", None, ["person"])
o(6, "The headlight knob on a car's dashboard is turned, and the headlights come on and the dashboard dials light up.", None, ["person"])
o(7, "A glowing bulb is unscrewed from a table lamp, and it goes dark as it comes loose.",
  "The bulb goes out at the moment it loses contact in the socket and stays dark once removed; it does not keep glowing on its own.",
  ["person", "expectation"])
o(9, "A string of fairy lights is plugged into a wall socket, and the whole string lights up along its length.", None, ["person"],
  "cluster: ELEC-0009 / 0027 (Christmas lights, switch) / 0059 (same string unplugged) / 0064 (garland, battery pack) all test 'all bulbs together'")
o(10, "The button on an electric kettle is pressed, and a small light on the kettle comes on and the switch stays down.", None, ["person"])
o(11, "The knob of a night light in a dark bedroom is turned, and the little lamp glows.", None, ["person"])
o(12, "A power strip with four lamps plugged into it is switched on, and all four lamps come on at once.", None, ["person"])
o(13, "The power button on a laptop is pressed, and the screen lights up and the keyboard glows.", None, ["person"])
o(14, "A light switch is flicked up and down several times in quick succession, and the ceiling light goes on and off in step with each flick.", None, ["person"])
o(15, "The call button beside an elevator is pressed, and the button lights up.",
  "The button glows from the moment it is pressed and stays lit; it does not light before being pressed.", ["person", "expectation"],
  "'until the elevator arrives' cannot be checked in a short clip")
o(16, "The light chain on a ceiling fan is pulled, and the light above the fan comes on while the blades stay still.", None, ["person"])
o(17, "A hairdryer resting on a counter with ribbons tied to its nozzle is switched on, and the ribbons stream out in the airflow; switched off, they fall slack.",
  "The ribbons lift and stream the moment the switch is on and drop within a second of it being turned off; they do not move with the switch off.",
  ["person", "expectation", "scene"], "'roars and blows hot air' is invisible; the ribbons make the airflow judgeable")
o(18, "The button on an electric toothbrush lying on a counter is pressed, and the head starts buzzing and vibrating.", None, ["person"])
o(19, "The button on a garage door remote is pressed, and the garage light comes on and the door begins to rise.", None, ["person"])
o(20, "A neon shop sign is switched on, and the tubes flicker and then glow steadily.", None, ["person"])
o(21, "The top of a touch-sensitive lamp is tapped, and it lights up; it is tapped again and goes off.",
  "The lamp changes state at each touch and only at a touch; it does not change between touches.", ["person", "expectation"])
o(22, "The switch on the underside of a remote-controlled toy car is flicked on, and its headlights light up; it drives off when the controller is pressed.", None, ["person"])
o(23, "A microwave door is opened, and the light inside the microwave comes on.", None, ["person"])
o(24, "The start button on a blender is pressed, and the blades spin and the contents whirl; the stop button is pressed and the blades come to rest.", None, ["person"])
o(25, "The knob of a desk fan is turned from off to high, and the blades spin up to speed; it is turned back to off and they slow and stop.", None, ["person"])
o(27, "A string of Christmas lights wound around a tree is switched on, and the tree lights up from the plug to the top all at once.", None, ["person"],
  "near-duplicate of ELEC-0009")
o(28, "The button on a bicycle's rear light is pressed, and it begins to blink red.", None, ["person"])
o(29, "The green start button on a conveyor belt is pressed, and the belt begins to move.",
      "The belt is still before the press and starts moving the instant the button is pressed, running steadily in one direction and carrying anything on it along; nothing moves before the press and nothing else in the scene starts moving on its own.",
      ["person"], "user: one action per caption; the stop half duplicated the same cause-effect and crowded the 5 s clip")
o(30, "The key in a car's ignition is turned, and the dashboard lights up before the engine starts.", None, ["person"])
o(31, "A battery-powered lantern in a tent is switched on, and the tent lights up; it is switched off and the tent goes dark.", None, ["person"])
o(32, "A fingertip holds down the doorbell button beside a front door, and a small light in the button glows while it is pressed and goes out when it is released.",
  None, ["person"], "the fingertip is the acting tool for the whole event (the glow lasts only while pressed)")
o(33, "The dial of an electric stove burner is turned off, and the red-hot coil's glow dims.",
  "The glow fades gradually after the dial is turned, from bright to dull red to dark, and never brightens again; it does not go out instantly like a lamp.",
  ["person", "timescale", "expectation"], "a cold coil takes tens of seconds to glow visibly; the fading of an already red-hot coil is seen within seconds")
o(34, "The power button on a handheld game console is pressed, and the screen lights up with the start logo.", None, ["person"])
o(35, "The switch on a wall-mounted heater is flipped, and its indicator light comes on and its fan starts.", None, ["person"])
o(36, "A pair of hands claps twice in a room with a clap-activated lamp, and the lamp comes on.", None, ["person"],
  "the clap must be seen, so hands stay. Delete candidate: the judge cannot verify the sound, only the timing of the hands")
o(37, "A fluorescent tube in a garage is switched on, and it blinks a few times before staying lit.", None, ["person"])
o(38, "A key on a toy piano is pressed, and the key lights up while it is held down and goes dark when it is released.",
  "The key lights while pressed and goes dark when released; nothing lights before the press.", ["person", "expectation"],
  "'speaker cone can be seen vibrating' is not visible on a toy; dropped")
o(39, "The wall button for an outdoor floodlight is pressed, and the yard lights up.", None, ["person"])
o(40, "A shop escalator is started with its key switch, and the steps begin to move upward.", None, ["person"])
o(41, "The button on a coffee machine is pressed, and a light comes on and coffee begins to drip into the cup.", None, ["person"])
o(42, "The bedside lamp is switched off, and only the glow of the alarm clock's display remains in the dark room.", None, ["person"])

# ---------------------------------------------------------------- plug_power
o(43, "The plug of a lit table lamp is pulled out of the wall socket, and the lamp goes out.", None, ["person"])
o(44, "A desk fan with its switch already on is plugged into a socket, and the blades start turning.", None, ["person"])
o(45, "The plug of a television is pulled while a programme is playing, and the screen goes black.", None, ["person"])
o(46, "The batteries are pulled out of a walking toy robot, and the robot stops mid-step.", None, ["person"])
o(47, "A charging cable is plugged into a phone lying on a table, and a charging symbol appears on the screen.", None, ["person"])
o(48, "An extension cord is yanked out of the wall socket, and the lamp, radio and heater plugged into it all go off together.", None, ["person"],
  "the trip was decorative; the yank is enough")
o(49, "Two batteries are slid into a flashlight and the cap screwed back on; when the switch is pressed the light comes on.", None, ["person"])
o(50, "The key is turned in a car with a dead battery, and the dashboard stays dark and nothing happens.", None, ["person"],
  "delete candidate: a non-event. A wrong video (lights come on) is judgeable, but a right one shows nothing happening. Same for ELEC-0071, ELEC-0079")
o(51, "A charging cable is plugged into an electric car, and a light on the charging port comes on.", None, ["person"])
o(52, "The cord of a running hairdryer is pulled out of the socket, and the dryer falls silent and stops blowing.", None, ["person"],
  "judgeability: 'stops blowing' is visible only if something is in the airflow; consider ribbons as in ELEC-0017")
o(53, "A blender is plugged in and its button pressed, and the blades spin; it is unplugged and the blades slow and stop.", None, ["person"])
o(54, "The cord of a running vacuum cleaner snags on a doorframe and jerks out of the socket, and the vacuum stops.", None, ["person"])
o(55, "A battery pack is clipped into a remote-control car, and the car's lights come on.",
      "The lights are off and the car is still before the pack goes in; the lights come on the instant the pack clicks into place and stay on; the car does not drive off by itself and nothing happens before the pack is in.",
      ["person", "scene"], "user: the swap was too many steps for 5 s and a flat vs charged pack looks identical; one action, one consequence, no driving (needs the controller)")
o(56, "A power bank is connected to a phone by a cable, and a light on the power bank comes on and the phone shows it is charging.", None, ["person"])
o(57, "In a garden at dusk, the solar lights along the path flicker on one after another.",
  "The lights come on while the sky is already dim and stay lit; they do not come on in full daylight and do not go out again.",
  ["timescale", "expectation"], "the darkening takes minutes; the clip shows only the switch-on moment. Weak: the cause is not visible")
o(58, "A portable generator at a campsite is started, and the string of lights connected to it comes on.", None, ["person"])
o(59, "A string of fairy lights is unplugged from the wall, and the whole string goes dark.", None, ["person"], "reverse of ELEC-0009; near-duplicate")
o(60, "The battery is unlatched from an e-bike, and the display on the handlebars goes dark.", None, ["person"])
o(61, "A toy train is placed on its track and the track's power pack switched on, and the train begins to run.", None, ["person"])
o(62, "A glowing electric heater is unplugged, and the orange glow of its elements fades to dark.", None, ["person"])
o(63, "A toaster is unplugged while its coils are glowing, and the coils fade and the lever pops up.", None, ["person"])
o(64, "The switch on a battery pack attached to a garland of lights is slid on, and the garland lights up.", None, ["person"], "near-duplicate of ELEC-0009/0027")
o(65, "A battery pack is clipped into a cordless drill and the trigger pulled, and the drill bit spins.", None, ["person"])
o(67, "An electric kettle is lifted off its base while it is boiling, and the kettle's light goes off and the boiling quiets.", None, ["person"])
o(68, "A camera's screen goes dark mid-recording as its battery runs out, and the camera will not turn back on.", None, ["person"])
o(69, "A digital alarm clock is unplugged, and its glowing display goes blank.", None, ["person"])
o(70, "A laptop charger is plugged into the wall and then into the laptop, and the small light on the charger connector comes on.", None, ["person"])
o(71, "The accelerator pedal of an electric ride-on car with a flat battery is pressed, and the car does not move.", None, ["person"],
  "delete candidate: non-event (see ELEC-0050)")
o(72, "A lamp is plugged into a socket and the socket switched on at the wall, and the lamp lights.", None, ["person"])
o(73, "Headphones are plugged into a phone playing music, and the phone's speaker goes quiet while the headphones take over.", None, ["person"],
  "delete candidate: the only visible change is a tiny on-screen icon; sound is not visible")
o(74, "Jumper cables from a running car are clamped onto a dead car's battery, and the dead car's dashboard lights come on.", None, ["person"])
o(75, "A running sewing machine is unplugged, and the needle stops and its work light goes out.", None, ["person"])
o(76, "A coin-cell battery is pressed into a wristwatch lying face up, and the second hand starts to tick.", None, ["person"])
o(78, "A nightlight is plugged into a low wall socket, and it begins to glow.", None, ["person"])
delete(79, "user: too many steps, and the outcome is 'nothing happens', which a judge cannot distinguish from a model that ignored the caption; the positive version (batteries in, device works) duplicates ELEC-0055")
o(80, "An aquarium pump is plugged into the wall, and bubbles start rising from the air stone in the tank.", None, ["person"])
o(81, "A laptop is unplugged from its charger, and the charging light on it goes off while the screen stays on.", None, ["person"])
o(82, "An electric blanket is plugged in and switched on, and its small control light comes on.", None, ["person"])
o(83, "A battery-powered toy car slows and stops as its battery runs flat, and its headlights dim and go out.",
  "The car loses speed gradually and stops; the lights dim and go out around the same time and do not come back; it does not speed up again.",
  ["person", "scene", "expectation"], "the scooter needs a rider; a toy car shows the same power loss unmanned")
o(84, "An electric lawnmower reaches the end of its cord and the plug pulls out of the socket, and the mower stops.", None, ["person"])

# ---------------------------------------------------------------- lightning
o(87, "An empty living room lit by a single lamp during a storm brightens for an instant as lightning flashes through the window.", None, ["person"])
o(92, "Lightning flashes outside an empty parked car in a rainstorm, and the inside of the car lights up through the rain-streaked windows for an instant.", None, ["person"])
delete(94, "the children's reaction is the only visible content and the sound cannot be judged from frames; ELEC-0100 (dog) already carries the flash-before-thunder idea")
flag(100, "an animal's reaction, not a person's; it is the only visible sign of thunder, so keep this as the single flash-then-reaction item")
delete(105, "a storm approaching takes minutes; 'closer together and brighter' cannot be shown in a 5 s clip, and the remainder duplicates ELEC-0091")
o(117, "Lightning flashes over a river, and a moored rowing boat on the bank is lit for an instant against the dark water.",
  "The boat and its reflection brighten together for a moment; the scene is dark again immediately.", ["person", "expectation"])
delete(119, "after removing the family only 'porch lit for an instant' remains, which duplicates ELEC-0087/0121/0125; the ear-covering is the same idea as ELEC-0100")
o(122, "The canvas of a pitched tent lights up from a lightning flash outside, then goes dark again.", None, ["person"])
o(125, "A lightning flash lights an empty rain-streaked bus shelter for a moment against the dark street.",
  "The shelter brightens for a fraction of a second and its own light continues unchanged afterward.", ["person", "expectation"],
  "near-duplicate of ELEC-0087 (room) / 0121 (house fronts); keep only for scene variety")

# ---------------------------------------------------------------- spark
o(126, "A robotic welding arm touches down on a steel car body on an assembly line, and a shower of bright sparks bursts from the joint and falls to the floor.",
  "Sparks appear only while the arm's tip touches the metal, fly outward and downward, and go dark within a short distance; they do not rise or linger on the floor as lights.",
  ["person", "scene", "expectation"], "the welder becomes a machine; same physics")
o(127, "A spinning angle grinder is pressed against a metal pipe clamped in a vise, and a fan of orange sparks streams off the wheel.", None, ["person"])
o(128, "The plug of a running heater is yanked out of the wall socket, and a small spark snaps at the prongs as they come out.", None, ["person"])
o(129, "The second jumper-cable clamp is touched to a car battery terminal, and a spark jumps at the contact.", None, ["person"])
o(133, "A flint gas-lighter is clicked over a stove burner, and a spark jumps from its tip and the gas ignites.", None, ["person"])
flag(136, "riders in the bumper cars are incidental and not named; left as is")
o(139, "A striker is scraped down a ferro rod held over a pile of tinder, and sparks spray onto the tinder below.", None, ["person"])
o(140, "The blade of a chop saw comes down on a steel bar clamped in its jaws, and a long plume of sparks shoots out behind the blade and rains onto the floor.", None, ["person"])
o(142, "A power hammer in a forge pounds a red-hot steel bar, and tiny sparks fly off with each blow.", None, ["person", "scene"], "blacksmith replaced by a power hammer")
o(143, "A metal rake is dragged along a concrete path in the dark, and faint sparks flick from the tines.", None, ["person"])
o(144, "A live wire brushes against a metal bracket, and a bright spark flashes and leaves a black mark.", None, ["person"])
o(146, "A motorcycle leaning hard through a turn scrapes its metal footpeg along the track, and sparks trail out behind it.",
  "The sparks stream backward from the point of contact and die out along the track; they stop when the peg lifts off the track.", ["person", "scene", "expectation"],
  "the rider stays as part of the vehicle but is no longer the subject; the footpeg replaces the knee slider")
o(147, "A phone charger is plugged into a worn socket, and a small spark flashes at the plug as it goes in.", None, ["person"])
o(150, "A CNC plasma cutter slices a steel sheet, and a fountain of sparks pours from the underside of the cut.", None, ["person"])
o(151, "A toy car with metal wheels is scuffed across a rough stone slab, and tiny sparks appear under the wheels.", None, ["person"],
  "physics weak: toy-car wheels rarely spark on stone; delete candidate")
o(152, "A stovetop lighter is clicked, and a blue spark jumps between its two metal tips.", None, ["person"])
o(153, "A piece of steel clamped in a bench vise is filed, and each stroke throws a few sparks that drop to the bench.", None, ["person"],
  "physics doubtful: hand filing does not normally throw sparks; delete candidate (grinding sparks are ELEC-0127/0134/0148)")
o(154, "A loose wire in an open junction box shorts against the box, and a flash and puff of smoke come from the spot.", None, ["person"])
o(156, "A steel rod falls onto a concrete floor in a dim workshop, and a spark flicks from the point of impact.", None, ["person"],
  "physics doubtful: a dropped rod seldom sparks on concrete; delete candidate")
o(157, "A car with a dragging exhaust pipe drives down a road at night, and sparks trail behind it where the pipe scrapes the asphalt.",
  "Sparks appear along the contact and stream behind the car; they stop when the pipe lifts off the road.", ["person", "scene", "expectation"],
  "skateboarder replaced by an unmanned friction-spark scene")
o(158, "An arc welder is struck behind a screen in a garage, and the arc lights the whole garage in blue-white, throwing hard shadows.", None, ["person"])
o(160, "An old-fashioned knife switch is thrown closed, and a small arc snaps at the contacts as they close.", None, ["person"])
o(161, "A wire brush wheel is run over a rusty gate, and sparks and rust flakes fly off the wheel in a fan.", None, ["person"])
o(162, "An electric igniter is fired, and it sparks briefly at the wire ends before the fuse catches.", None, ["person"])
o(164, "A lathe cuts a spinning steel bar, and glowing chips and sparks curl off the tool and drop into the tray.", None, ["person"])
o(165, "Two pieces of flint are struck together in the dark, and a tiny spark jumps between them.", None, ["person"],
  "physics weak: flint on flint gives only a faint glow; flint on steel is the classic case but duplicates ELEC-0139; delete candidate")
o(167, "A demolition hammer chips a concrete floor, and an occasional spark flicks where the bit strikes embedded stone.", None, ["person"])

# ---------------------------------------------------------------- magnet
o(168, "A small magnet is pressed against a refrigerator door and released, and it stays stuck on the door.", None, ["person"])
o(169, "A magnet is lowered toward a pile of paperclips on a desk, and the clips jump up and cling to it.", None, ["person"])
o(170, "A magnet is swept over a mix of nails and plastic beads spilled on the floor, and the nails stick to the magnet while the beads stay behind.", None, ["person"])
o(171, "A sheet of paper lies over a paperclip, and a magnet is moved across the top of the paper; the clip follows the magnet under the paper.", None, ["person"])
o(172, "A magnet is slid along the underside of a thin wooden table, and a toy car with a metal base on top of the table follows it.", None, ["person"])
o(173, "A kitchen knife is brought up to a magnetic strip on the wall, and the knife snaps onto the strip and stays there.", None, ["person"])
o(174, "A phone is brought near a magnetic mount on a car's dashboard, and the phone snaps onto the mount and holds.", None, ["person"])
o(175, "Two toy train cars with magnetic couplers are pushed together, and they snap together and roll as one.", None, ["person"])
o(176, "A toy fishing rod with a magnet on its line is dangled over a bowl of metal fish, and a fish leaps up and sticks to the magnet.", None, ["person"])
o(177, "Two bar magnets are brought together end to end, and they snap together with a click.", None, ["person"])
o(178, "One bar magnet is pushed toward the like end of another lying on a table, and the second magnet slides away from the first.", None, ["person"])
o(179, "A cabinet door with a magnetic latch is swung shut, and the door pulls itself closed the last little way and stays closed.", None, ["person"])
o(180, "A magnetic parts tray is set on the side of a car and screws dropped into it, and the tray and the screws stay put.", None, ["person"])
o(181, "The flap of a handbag with a magnetic clasp is let fall, and the flap snaps down and holds.", None, ["person"])
o(182, "A horseshoe magnet is lowered over a steel key on a table, and the key jumps up and sticks to the magnet.", None, ["person"])
o(183, None, "The magnet moves only while it is pushed and stays on the door when released at any point; it does not drop off.", ["expectation"],
  "caption was already passive; expectation mentioned 'the hand'")
o(184, "A sheet of paper is stuck to a whiteboard with a round magnet, and the paper hangs there.", None, ["person"])
o(185, "A magnet is moved toward a steel saucepan on the counter, and the magnet jumps the last gap and clicks onto the pan.",
  "The magnet leaps the last small gap and sticks; it stays on the pan when released.", ["person", "expectation"])
o(186, "A screwdriver with a magnetic tip is held to a loose screw, and the screw clings to the tip and is lifted away.", None, ["person"])
o(187, "A steel washer is dropped near a strong magnet on a table, and the washer swerves toward the magnet and sticks to it.", None, ["person"])
o(188, "Magnetic tiles are stacked one onto another, and each tile clicks onto the last and the tower stands.", None, ["person"])
o(189, "A travel chess board with magnetic pieces is tilted steeply, and the pieces stay in their squares while a coin placed on the board slides off.", None, ["person"])
o(191, "A magnetic name badge is placed on a jacket hanging on a hook by putting the magnet inside the fabric, and the badge holds in place.", None, ["person"])
o(192, "A door blown open by a draught swings until it reaches a magnetic doorstop, and the door snaps to the stop and holds open.", None, ["person"])
o(193, "A magnet is brought near a compass, and the needle swings to point at the magnet; the magnet is taken away and the needle swings back.", None, ["person"])
o(194, "A magnetic sign is placed on the side of a steel van, and it stays flat against the panel as the van drives off.", None, ["person"])
o(195, "A magnetic wand is dragged over a tray of iron filings, and the filings clump onto the wand in fuzzy bristles.", None, ["person"])
o(196, "A handful of steel pins is dropped near a magnet, and the pins swing toward it as they fall and stick along its sides.", None, ["person"])
o(197, "A magnetic hook is hung on the side of a steel filing cabinet and a coat hung on it, and the hook holds.", None, ["person"])
o(198, "A magnet is held against a plastic toy and released, and the magnet falls to the floor.", None, ["person"])
o(199, "The two ends of a bracelet with a magnetic clasp are brought close on a table, and they jump together and hold.",
  "The ends pull together over the last small gap and stay joined when the bracelet is lifted.", ["person", "expectation"])
o(200, "A steel bolt is tossed toward a strong magnet fixed to a workbench, and the bolt swerves and clacks onto the magnet.", None, ["person"])
o(201, "A magnet on a string is lowered toward a metal bottle cap on the floor, and the cap jumps up to the magnet before it touches the floor.", None, ["person"])
o(202, "One block is lifted out of a box of magnetic building blocks, and the others cling to it in a hanging chain.", None, ["person"])
o(203, "A magnet is stuck to a steel lamp post with a lost-cat poster under it, and the poster stays up.", None, ["person"])
o(204, "A magnet is moved in circles under a shallow dish of water with a paperclip floating on a piece of foam, and the clip follows the magnet around the dish.", None, ["person"])
o(205, "A magnetic spirit level is placed against a steel beam and released, and the level stays on the beam.", None, ["person"])
o(206, "A magnet is dropped into a bowl of dry rice mixed with steel ball bearings and pulled out again, and the bearings cling to it while the rice falls away.", None, ["person"])
o(207, "A laptop lid is lowered, and it snaps shut over the last small gap and stays closed thanks to the magnets inside.", None, ["person"])
o(208, "A magnetic letter is stuck to a fridge and holds; the same letter is stuck to the wooden cupboard next to it and falls off.", None, ["person"])
o(209, "A magnetic pickup tool is lowered into an engine bay toward a dropped nut, and the nut clicks onto its tip and is lifted out.", None, ["person"])

# ---------------------------------------------------------------- static
o(210, "A balloon is rubbed on a wool sweater and pressed against a wall, and it stays stuck to the wall when released.", None, ["person"])
o(211, "A balloon rubbed on a wool sweater is held near a head of long hair, and the hair rises toward the balloon.", None, ["person"],
  "the hair is the charged object; no identity, no face")
o(212, "A balloon rubbed on a wool jumper is lowered over small torn scraps of paper on a table, and the scraps jump up and cling to the balloon.", None, ["person"],
  "cluster: five 'bits jump to a rubbed object' items (0212 paper, 0221 foam beads, 0227 tissue + ruler, 0244 sugar, 0249 sawdust)")
o(213, "A wool sweater is pulled off over the head in a dry room, and the hair underneath stands up in all directions.", None, ["person"],
  "hair is the physics; only the head remains")
o(214, "A shirt is lifted out of a tumble dryer, and a sock clings to it and hangs on until it is peeled off.", None, ["person"])
o(215, "A sheet of plastic wrap is torn from its box, and it clings to the side of the box and folds onto itself instead of hanging straight.",
  "The wrap sticks to the box and to itself where it touches and has to be pulled free; it does not hang straight like paper.", ["person", "expectation"])
o(216, "A box of packing peanuts is tipped over a table, and many of the foam pieces stick to the sides and flaps of the box instead of falling out.",
  "The pieces cling to the cardboard instead of falling and stay there when the box is lifted; the pieces that do fall land normally.", ["person", "expectation"])
o(217, "In a dark hallway a fingertip is brought slowly toward a metal doorknob, and a tiny spark jumps from the fingertip to the knob just before they touch.",
  "The spark is a single brief flash at the moment of near-contact; nothing glows before or after.", ["person", "expectation"],
  "the flinch was the only visible sign of the shock; the spark is the visible physics. Delete candidate if such a small spark is judged unrenderable")
keep(218, "the hair standing up after the slide is the phenomenon; the child cannot be removed")
o(219, "A hand strokes a cat's back on a dry winter day, and the fur stands up along its back and clings to the hand.",
  "The fur lifts where the hand passes and follows the hand slightly; it settles after the stroking stops.", ["person", "expectation"],
  "the hand is the acting tool for the whole event")
o(220, "An old television screen is wiped with a dry cloth, and dust and a few hairs jump onto the screen and stick.", None, ["person"])
o(221, "A balloon rubbed on a wool sweater is held over a tray of tiny foam beads, and the beads jump up to the balloon.", None, ["person"])
delete(222, "the flinch is the only visible content; a static shock has no visible physics except the spark (ELEC-0217)")
o(223, "A fleece blanket is shaken out in a dark bedroom, and small flickers of light run through the fabric.", None, ["person"])
o(224, "A wool hat is pulled off, and the hair underneath stays lifted in the shape of the hat's inside before slowly settling.", None, ["person"])
delete(225, "skirt clinging to legs is body-based; cling to fabric is covered by ELEC-0214/0236/0245, and ELEC-0237 is the same idea")
o(226, "A thin plastic bag is torn off a roll, and it clings to the roll and to the dispenser instead of dropping away.",
  "The bag lies against the roll and dispenser and stays there; it comes off only when peeled.", ["person", "expectation"])
o(227, "A plastic ruler is rubbed on a wool sleeve and held over torn bits of tissue, and the bits rise and stick to the ruler.", None, ["person"])
keep(228, "hair charged by the trampoline mat is the phenomenon; the bouncing child is unavoidable")
o(229, "A sheet of cling film is lifted off a bowl, and the film clings back to the bowl's rim and to itself.", None, ["person"])
delete(230, "physics wrong: an air-filled balloon does not float up to the ceiling however it is rubbed; static only holds it once pressed there (ELEC-0210)")
o(231, "A balloon rubbed on a wool sweater is held beside a tissue-paper ghost taped to a table, and the ghost lifts and leans toward the balloon.", None, ["person"])
o(232, "A fleece jacket is pulled off over a cotton shirt in the dark, and tiny sparks crackle where the fabrics separate.",
  "The sparks appear only as the fabrics separate and vanish instantly; nothing glows once the movement stops.", ["person", "expectation"])
delete(233, "same as ELEC-0222: the flinch is the only visible content")
o(234, "The sleeve of a wool sweater brushes past a hanging plastic shower curtain, and the curtain clings to the sleeve and follows it for a moment.",
  "The curtain lifts toward the sleeve where it touched and trails after it briefly before falling back; it does not move before the sleeve passes.", ["person", "expectation"])
o(235, "A stack of freshly printed sheets is lifted from a printer, and the sheets cling together; a single sheet lifted from the top clings to the stack rather than falling.",
  "The sheets stick and have to be fanned apart; the single sheet hangs on the stack rather than dropping.", ["person", "expectation"])
o(236, "A fleece blanket is lifted out of the dryer, and a dryer sheet clings to its underside and rides along as the blanket is carried.", None, ["person"])
delete(237, "body-based cling, same idea as ELEC-0225")
o(238, "A sheet of bubble wrap is unrolled on a table, and small bits of dust and fluff jump onto it from the table.", None, ["person"])
o(239, "A balloon that has been stuck to a wall for a while is pulled away, and it comes free with a faint tug while tissue scraps on the shelf below lean toward it.",
  "The balloon resists slightly before coming free and the nearby scraps lean toward it; they settle when it is moved away.", ["person", "expectation"],
  "arm hairs replaced by tissue scraps; delete candidate, the tug is hard to see")
o(240, "Long hair is brushed vigorously with a plastic brush, and strands lift and follow the brush as it moves away.", None, ["person"], "hair is the physics")
o(241, "A balloon rubbed on a wool sweater is placed against a wooden door, and the balloon slides slowly down and falls off.", None, ["person"])
o(242, "A nylon jacket is pulled off a hanger in a dark closet, and faint flickers of light run across the fabric.", None, ["person"])
o(243, "A sticker is peeled from its backing sheet, and the thin backing curls toward the sticker and clings to it instead of lying flat.",
  "The backing lifts and clings to the sticker where they come close and has to be pulled apart; it does not fall flat straight away.", ["person", "expectation"])
o(244, "A balloon rubbed on a sweater is held over a bowl of sugar, and a fine dusting of sugar jumps up to the balloon.", None, ["person"])
o(245, "A woollen blanket is shaken out of the dryer, and a small sock flies off, lands against the wall and sticks there.",
  "The sock clings where it lands rather than sliding down; it comes away only with a pull.", ["person", "expectation"])
o(246, "A balloon rubbed on a wool sweater is held beside a feather duster standing in a jar, and the feathers lean toward the balloon.",
  "The feathers lift toward the balloon while it is close and fall back when it is pulled away.", ["person", "scene", "expectation"],
  "duplicate of ELEC-0211 (hair) once de-personed; feathers give a different object")
o(247, "A bag of styrofoam beads is poured into a bowl, and beads stick to the bag's sides and to the rim rather than all falling in.",
  "Some beads cling to the bag and the rim while most fall; the clinging beads stay until brushed off.", ["person", "expectation"])
delete(248, "the dog's flinch is the only visible content; the shock itself is not judgeable")
o(249, "A balloon rubbed on a carpet is rolled near a pile of fine sawdust, and sawdust jumps onto the balloon.", None, ["person"])
o(250, "A dry synthetic scarf is pulled away from a head of long hair, and the hair lifts and follows the scarf as it comes away.", None, ["person"], "hair is the physics")

CLUSTERS = [
    ("switch_light / plug_power: whole string lights or dies together", ["ELEC-0009", "ELEC-0027", "ELEC-0059", "ELEC-0064"]),
    ("plug_power: non-events (nothing changes on screen)", ["ELEC-0050", "ELEC-0071", "ELEC-0079"]),
    ("lightning: 'X is lit for an instant' with no other physics", ["ELEC-0089", "ELEC-0103", "ELEC-0107", "ELEC-0108", "ELEC-0110", "ELEC-0111",
                                                                   "ELEC-0113", "ELEC-0114", "ELEC-0115", "ELEC-0121", "ELEC-0122", "ELEC-0123",
                                                                   "ELEC-0124", "ELEC-0125", "ELEC-0087", "ELEC-0092"]),
    ("lightning: flash first, reaction later", ["ELEC-0094", "ELEC-0100", "ELEC-0119"]),
    ("spark: sparks trail behind a moving vehicle", ["ELEC-0130", "ELEC-0136", "ELEC-0137", "ELEC-0145", "ELEC-0146", "ELEC-0149", "ELEC-0157",
                                                     "ELEC-0159", "ELEC-0163", "ELEC-0166"]),
    ("spark: grinding-wheel spark fans", ["ELEC-0127", "ELEC-0134", "ELEC-0148", "ELEC-0161"]),
    ("magnet: small steel object jumps up to a lowered magnet", ["ELEC-0169", "ELEC-0176", "ELEC-0182", "ELEC-0195", "ELEC-0201", "ELEC-0209"]),
    ("magnet: magnet drives an object through a barrier", ["ELEC-0171", "ELEC-0172", "ELEC-0204"]),
    ("magnet: object sticks to a vertical steel surface", ["ELEC-0168", "ELEC-0180", "ELEC-0184", "ELEC-0194", "ELEC-0197", "ELEC-0203", "ELEC-0205", "ELEC-0208"]),
    ("static: bits jump to a rubbed balloon / ruler", ["ELEC-0212", "ELEC-0221", "ELEC-0227", "ELEC-0244", "ELEC-0249"]),
    ("static: hair stands up", ["ELEC-0211", "ELEC-0213", "ELEC-0218", "ELEC-0224", "ELEC-0228", "ELEC-0240", "ELEC-0250"]),
    ("static: sparks in fabric in the dark", ["ELEC-0223", "ELEC-0232", "ELEC-0242"]),
    ("static: shock felt (flinch only)", ["ELEC-0217", "ELEC-0222", "ELEC-0233", "ELEC-0248"]),
    ("static: fabric / film clings", ["ELEC-0214", "ELEC-0215", "ELEC-0225", "ELEC-0226", "ELEC-0229", "ELEC-0235", "ELEC-0236", "ELEC-0237", "ELEC-0243", "ELEC-0245"]),
]

# ---------------------------------------------------------------- build

# ---- 2026-09-14 final review pass (this session); keys are ORIGINAL ids
o(3, "The cord of a bedside lamp is pulled, and the lamp lights up.",
     "The lamp comes on at the click of the pull and stays on; it does not light before the pull or flicker afterwards.",
     ["person", "scene"], "user: one action per caption (was on-then-off)")
o(4, "A flashlight lying on a table and pointed at a wall is switched on, and a bright spot appears on the wall.",
     "The spot appears on the wall exactly at the click and stays steady; nothing is lit before the switch.",
     ["person", "scene"], "user: one action per caption (was on-then-off)")
o(17, "A hairdryer resting on a counter with ribbons tied to its nozzle is switched on, and the ribbons stream out in the airflow.",
     "The ribbons hang slack before the switch, lift and stream the moment it is on, and keep streaming while it runs; they do not move while the dryer is off.",
     ["person", "scene"], "user: one action per caption (was on-then-off)")
o(21, "The top of a touch-sensitive lamp is tapped, and it lights up.",
     "The lamp lights at the touch and stays on; it does not change state without a touch.",
     ["person", "scene"], "user: one action per caption (was on-then-off)")
o(24, "The start button on a blender is pressed, and the blades spin and the contents whirl.",
     "The blades and contents are still before the press and spin the instant it is pressed, running steadily; nothing moves before the button is touched.",
     ["person", "scene"], "user: one action per caption (was on-then-off)")
o(25, "The knob of a desk fan is turned from off to high, and the blades spin up to speed.",
     "The blades are still while the knob is at off, start as it turns and speed up to a steady spin; they do not spin with the knob at off.",
     ["person", "scene"], "user: one action per caption (was on-then-off)")
o(31, "A battery-powered lantern in a tent is switched on, and the tent lights up.",
     "The tent is dark before the switch and steadily lit from the lantern after it; the light does not appear before the switch.",
     ["person", "scene"], "user: one action per caption (was on-then-off)")
o(53, "A blender with its button held down is plugged into a wall socket, and the blades start spinning.",
     "Nothing moves until the plug goes in; the blades start the instant it does and run steadily; the held button alone does nothing while unplugged.",
     ["person", "scene"], "user: one action per caption (was on-then-off)")
o(193, "A magnet is brought near a compass, and the needle swings to point at the magnet.",
     "The needle turns only as the magnet approaches and follows the magnet as it moves; it does not move before the magnet is near.",
     ["person", "scene"], "user: one action per caption (was on-then-off)")
delete(50, "final pass: non-event: 'nothing happens' cannot be judged")
delete(71, "final pass: non-event: 'nothing happens' cannot be judged")
delete(73, "final pass: a phone's speaker cone is not visible; only an icon remains")
delete(96, "final pass: lightning-induced flicker is simultaneous, not 'a moment later'")
delete(118, "final pass: a strike does not run a flash along a fence line")
delete(151, "final pass: metal toy wheels on stone do not throw sparks")
delete(156, "final pass: a dropped steel rod does not throw sparks")
delete(239, "final pass: two weak effects; covered by the balloon-on-wall and paper-scraps items")
delete(241, "final pass: wood vs painted wall contrast is not real: both are insulators")
delete(245, "final pass: a sock flying off and sticking to a wall is too contrived")
delete(103, "final pass: lightning-lit cluster: silhouettes duplicate the mountain range item")
delete(108, "final pass: lightning-lit cluster: masts + reflections duplicate sea/puddle items")
delete(110, "final pass: lightning-lit cluster: cloud undersides duplicate the in-cloud flash")
delete(111, "final pass: lightning-lit cluster")
delete(114, "final pass: lightning-lit cluster")
delete(117, "final pass: lightning-lit cluster: boat + reflection duplicates harbour/puddle items")
delete(121, "final pass: lightning-lit cluster")
delete(124, "final pass: lightning-lit cluster")
delete(125, "final pass: lightning-lit cluster")
delete(123, "final pass: strike on a tall object: duplicates the lightning-rod item")
delete(145, "final pass: vehicle spark trail cluster")
delete(159, "final pass: vehicle spark trail cluster")
delete(163, "final pass: vehicle spark trail cluster: icy cable is doubtful")
delete(166, "final pass: vehicle spark trail cluster: duplicates the tram")
delete(148, "final pass: grinding spark cluster")
delete(153, "final pass: grinding spark cluster: filing sparks are tiny")
delete(161, "final pass: grinding spark cluster")
delete(176, "final pass: object-jumps-to-magnet cluster")
delete(201, "final pass: object-jumps-to-magnet cluster")
delete(184, "final pass: sticks-to-vertical-steel cluster")
delete(194, "final pass: sticks-to-vertical-steel cluster")
delete(205, "final pass: sticks-to-vertical-steel cluster")
delete(221, "final pass: light-bits-jump-to-balloon cluster")
delete(227, "final pass: light-bits-jump-to-balloon cluster")
delete(231, "final pass: light-bits-jump-to-balloon cluster")
delete(228, "final pass: hair cluster: trampoline mechanism is weak")
delete(240, "final pass: hair cluster")
delete(250, "final pass: hair cluster")


# ---- 2026-09-14 final pass, addendum: three more multi-step captions cut to one action
o(22, "The switch on the underside of a remote-controlled toy car is flicked on, and its headlights light up.",
     "The headlights come on with the switch and stay on; the car stays still and does not drive off, since no controller is used; nothing lights while the switch is off.",
     ["person", "scene"], "user rule: one action per caption")
o(49, "Two batteries are slid into a flashlight whose switch is already on, and the light comes on as the cap is screwed down.",
     "The flashlight is dark until the cap closes the circuit and lights at that moment, staying on; it does not light with the batteries out or the cap off.",
     ["person", "scene"], "user rule: one action per caption")
o(68, "A camera's screen goes dark mid-recording as its battery runs out.",
     "The screen and the camera's lights go off together and stay off; the camera does not come back to life on its own.",
     ["person", "scene"], "user rule: one action per caption")

import subprocess
MAP = ROOT / "data/electricity_id_map.json"         # original id -> current id (exists once records were removed)
ORIG_COMMIT = "b55cde0"                              # electricity.json with the original ids/captions
recs = json.loads(SRC.read_text())
orig = {r["id"]: r for r in json.loads(subprocess.run(["git", "-C", str(ROOT), "show", f"{ORIG_COMMIT}:data/train/electricity.json"],
                                                      capture_output=True, text=True, check=True).stdout)}
old_to_new = json.loads(MAP.read_text())["old_to_new"] if MAP.exists() else {r["id"]: r["id"] for r in recs}
new_to_old = {v: k for k, v in old_to_new.items() if v}
out = []
stats = Counter()
for r in recs:
    oid = new_to_old.get(r["id"], r["id"])
    o_rec = orig[oid]
    c, e, ch, note = O.get(oid, (None, None, [], ""))      # overrides are keyed by ORIGINAL ids
    new_c, new_e = (c if c else o_rec["caption"]), (e if e else o_rec["expectation"])
    applied = (r["caption"], r["expectation"]) == (new_c, new_e) and (new_c, new_e) != (o_rec["caption"], o_rec["expectation"])
    new = {
        "id": r["id"], "orig_id": oid, "category": r["category"], "subcategory": r["subcategory"],
        "violation_types": r["violation_types"],
        "caption": new_c, "expectation": new_e,
        "old_caption": o_rec["caption"], "old_expectation": o_rec["expectation"],
        "change": ch, "note": note, "applied_to_electricity_json": applied,
    }
    assert not re.search(r"\d", new["caption"]), r["id"]  # no numerals in captions
    for k in ch:
        stats[k] += 1
    if not ch:
        stats["unchanged"] += 1
    if applied:
        stats["applied"] += 1
    out.append(new)
DST.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
removed_ids = [k for k, v in old_to_new.items() if v is None]
print(f"wrote {DST} with {len(out)} records; {dict(stats)}; removed from file: {len(removed_ids)}")

# ---------------------------------------------------------------- review markdown
by_id = {n["orig_id"]: n for n in out}   # clusters below are written with ORIGINAL ids; removed ids are absent
by_sub = defaultdict(list)
for n in out:
    by_sub[n["subcategory"]].append(n)
deletes = [n for n in out if "delete" in n["change"]]
candidates = [n for n in out if "delete candidate" in n["note"].lower() and "delete" not in n["change"]]
lines = ["# Electricity caption rewrite draft — changed records only", "",
         "Two principles: (1) **no people** unless the body is the physics; (2) the key change is **visible within 5-10 s**. "
         "Tags: **person** = whole person removed (passive voice, object-state or environment trigger, or a machine in place of the worker; "
         "a body part only where it is the acting tool; hair kept where hair is the charged object) · **timescale** = slow process cut to its "
         "seconds-scale sub-event · **expectation** = re-worded to match, not loosened · **scene** = a different scene testing the same physics · "
         "**keep_person** = body is the phenomenon, left as is · **note** = unchanged, comment only · **delete** = proposed deletion (apply_draft.py skips it). "
         "Unchanged records are omitted here but present in the JSON.", "",
         f"Counts: {len(out)} records; " + ", ".join(f"{k} {v}" for k, v in sorted(stats.items())) + ".", ""]
lines += ["## Proposed deletions", ""]
for n in deletes:
    lines.append(f"- **{n['id']}** ({n['subcategory']}): {n['note']}  \n  _{n['old_caption']}_")
lines += ["", "## Delete candidates (user decides; a rewrite is still given)", ""]
for n in candidates:
    lines.append(f"- **{n['id']}** ({n['subcategory']}): {n['note']}")
lines += ["", "## Near-duplicate clusters (thin out to 3-5 per phenomenon)", ""]
for title, ids in CLUSTERS:
    lines.append(f"- **{title}**: " + ", ".join((f"{i}→{by_id[i]['id']}" if by_id[i]['id'] != i else i) if i in by_id else f"{i}†" for i in ids) + "  († = removed)")
lines += ["", "† = proposed deletion above", ""]
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
