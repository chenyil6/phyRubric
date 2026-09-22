# Rubric review

252 rubrics. SA = caption adherence (core/minor); PC = physics (fatal/core/major/minor, each tagged with a violation type). Expectation is the hidden field from data/, shown for the reviewer only.

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

## ELEC-0003 · switch_light · train

**Caption.** The cord of a bedside lamp is pulled, and the lamp lights up.

**Expectation (hidden).** The lamp comes on at the click of the pull and stays on; it does not light before the pull or flicker afterwards.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A bedside lamp with a pull cord.
- S2 [core] The cord is pulled.
- S3 [core] The lamp lights up.
- S4 [minor] The lamp is dark before the pull.
- S5 [minor] The order is dark, pull, lit.

**PC**
- P1 [core · missing_consequence]
  - expect: The lamp comes on at the moment the cord is pulled, and only then.
  - fail: The cord is pulled and the lamp stays dark; or the lamp is lit before the cord moves; or the lamp comes on while the cord hangs untouched; or the lamp comes on well after the pull with nothing else happening.
- P2 [core · process_direction]
  - expect: Once on, the lamp stays lit steadily for the rest of the clip.
  - fail: The lamp goes off again by itself; or flickers on and off after the pull; or dims back to dark; or the cord pulls itself again.
- P3 [major · missing_consequence]
  - expect: When the lamp is on its light reaches its surroundings: the shade glows and the bedside table and wall nearby brighten, with shadows pointing away from the lamp.
  - fail: The bulb glows while the shade and the table beneath stay as dark as before; or the surroundings brighten while the lamp stays dark; or the light comes from a place other than the lamp.
- P4 [major · material_response]
  - expect: The cord is a limp string or chain that hangs straight down from the lamp, is drawn taut by the pull and hangs slack again afterwards.
  - fail: The cord stands rigid or stays stretched out sideways after the pull; or stretches like elastic; or the lamp tips or lifts with the pull and hangs in the air.
- P5 [fatal · permanence_count]
  - expect: One lamp with one cord on one table; the lamp and table keep their shape; the hand passes through nothing.
  - fail: A second lamp or cord appears; or the lamp vanishes or moves across the table by itself; or the hand passes through the shade or the cord; or the lamp changes shape.
- P6 [minor · attribute_drift]
  - expect: The shade's colour, the table and the bedding stay the same apart from the light.
  - fail: The shade changes colour rather than brightness; or the table's contents rearrange; or the bedding changes pattern.

## ELEC-0004 · switch_light · train

**Caption.** A flashlight lying on a table and pointed at a wall is switched on, and a bright spot appears on the wall.

**Expectation (hidden).** The spot appears on the wall exactly at the click and stays steady; nothing is lit before the switch.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A flashlight lies on a table, pointed at a wall.
- S2 [core] The flashlight is switched on.
- S3 [core] A bright spot appears on the wall.
- S4 [minor] The wall is unlit by the flashlight before the switch.
- S5 [minor] The order is off, switch, spot on the wall.

**PC**
- P1 [core · missing_consequence]
  - expect: The spot appears on the wall at the moment the switch is pressed, and only then; it lies where the flashlight points.
  - fail: The switch is pressed and the wall stays as before; or the spot is on the wall before the switch is touched; or the spot appears on a part of the wall the flashlight does not point at; or the lens glows while the wall stays dark.
- P2 [core · process_direction]
  - expect: Once on, the spot stays steady on the wall for the rest of the clip while the flashlight lies still.
  - fail: The spot goes out again by itself; or flickers; or the spot wanders across the wall while the flashlight lies still; or the spot grows and shrinks with the flashlight untouched.
- P3 [major · missing_consequence]
  - expect: The lit lens and the spot appear together; the beam's path lights any dust or objects between them, and the spot is brightest at its centre.
  - fail: The lens is dark while the spot is on the wall; or the spot is lit while the lens stays dark; or an object placed in the beam casts no shadow on the wall.
- P4 [major · causeless_motion]
  - expect: The flashlight stays where it lies as it is switched on, apart from a small nudge from the hand; nothing else on the table moves.
  - fail: The flashlight rolls or slides across the table with nothing touching it; or lifts off the table; or other items on the table shift at the switch.
- P5 [fatal · permanence_count]
  - expect: One flashlight and one spot; the flashlight keeps its shape; the hand passes through nothing.
  - fail: A second flashlight or a second spot appears; or the flashlight vanishes; or the hand passes through the flashlight; or the wall changes shape.
- P6 [minor · attribute_drift]
  - expect: The flashlight's colour, the table and the wall's colour stay the same apart from the light.
  - fail: The flashlight changes colour; or the wall changes colour rather than brightness; or the table's contents rearrange.

## ELEC-0005 · switch_light · train

**Caption.** The power button on a remote pointed at a television is pressed, and the screen lights up.

**Expectation (hidden).** The screen comes on a moment after the button press and stays on; it does not light before the press or when the remote points elsewhere.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A television with a dark screen.
- S2 [core] A remote is pointed at the television.
- S3 [core] The power button on the remote is pressed.
- S4 [core] The screen lights up.
- S5 [minor] The remote is aimed at the television, not elsewhere.
- S6 [minor] The order is dark, press, lit.

**PC**
- P1 [core · missing_consequence]
  - expect: The screen comes on at or just after the press, and only then.
  - fail: The button is pressed and the screen stays dark to the end of the clip; or the screen is lit before the press; or the screen comes on while the remote lies untouched; or the screen comes on while the remote points away from the television.
- P2 [core · process_direction]
  - expect: Once on, the screen stays on for the rest of the clip and shows a steady picture or menu.
  - fail: The screen goes dark again by itself; or flickers on and off; or the picture appears and shrinks back to black; or the screen turns on and off with each frame.
- P3 [major · missing_consequence]
  - expect: The screen's glow reaches its surroundings: the wall behind and the shelf beneath brighten with the screen, and the standby light, if any, changes state at the press.
  - fail: The screen is lit while the room around it stays as dark as before; or the room brightens while the screen stays dark; or the standby light stays as it was while the screen comes on.
- P4 [major · causeless_motion]
  - expect: The television and the remote stay where they are, apart from the hand's movement; nothing else in the room moves at the press.
  - fail: The television shifts or turns at the press; or the remote moves with no hand on it; or objects on the shelf jump.
- P5 [fatal · permanence_count]
  - expect: One television and one remote; the television keeps its shape; the hand passes through nothing.
  - fail: A second screen or remote appears; or the television vanishes; or the remote passes through the hand; or the television changes size or shape.
- P6 [minor · attribute_drift]
  - expect: The television's frame, the remote's buttons and the room stay the same apart from the screen.
  - fail: The frame changes colour; or the remote's button layout changes; or the room's contents rearrange.

**Note.** The picture that appears on the screen is not judged; any content counts as lit.

## ELEC-0006 · switch_light · train

**Caption.** The headlight knob on a car's dashboard is turned, and the headlights come on and the dashboard dials light up.

**Expectation (hidden).** Both the headlights and the dials come on together as the knob turns, and go off together when it is turned back.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A car's dashboard with a headlight knob.
- S2 [core] The knob is turned.
- S3 [core] The headlights come on.
- S4 [core] The dashboard dials light up.
- S5 [minor] The headlights and the dials are dark before the turn.
- S6 [minor] The order is dark, turn, both lit.

**PC**
- P1 [core · missing_consequence]
  - expect: The headlights and the dashboard dials come on together at the moment the knob turns, and only then.
  - fail: The knob is turned and the headlights stay dark; or the dials stay dark while the headlights come on; or the headlights come on before the knob moves; or the dials light up well before the headlights.
- P2 [core · process_direction]
  - expect: Once on, the headlights and dials stay lit while the knob stays in its on position.
  - fail: The headlights go off again with the knob untouched; or the dials flicker on and off; or the knob turns back by itself; or the headlights dim back to dark.
- P3 [major · missing_consequence] (if: The view ahead of the car is visible.)
  - expect: The headlights light the road or wall ahead of the car: the ground in front brightens with two beams from the front of the car.
  - fail: The headlights glow while the ground ahead stays as dark as before; or the ground ahead brightens while the lamps stay dark; or the lit patch lies behind or beside the car.
- P4 [major · causeless_motion]
  - expect: The car stays still as the knob is turned; nothing on the dashboard moves apart from the knob and the needles.
  - fail: The car rolls or rocks at the turn; or the steering wheel turns by itself; or the wipers sweep; or the needles spin round the dials.
- P5 [fatal · permanence_count]
  - expect: One dashboard with its knob and dials in fixed places; the hand passes through nothing.
  - fail: Dials appear or vanish; or the knob moves along the dashboard; or the hand passes through the dashboard; or a second steering wheel appears.
- P6 [minor · attribute_drift]
  - expect: The dashboard's colours and the layout of its controls stay the same apart from the lighting.
  - fail: The dashboard changes colour rather than brightness; or the dial markings change; or the trim changes.

## ELEC-0007 · switch_light · train

**Caption.** A glowing bulb is unscrewed from a table lamp, and it goes dark as it comes loose.

**Expectation (hidden).** The bulb goes out at the moment it loses contact in the socket and stays dark once removed; it does not keep glowing on its own.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A table lamp with its bulb glowing.
- S2 [core] The bulb is unscrewed from the socket.
- S3 [core] The bulb goes dark as it comes loose.
- S4 [minor] The bulb is turned in the socket before it comes out.
- S5 [minor] The order is glowing, turning, dark, out.

**PC**
- P1 [core · missing_consequence]
  - expect: The bulb goes dark at the moment it comes loose in the socket, and only then; the lamp's own switch is not touched.
  - fail: The bulb is fully out of the socket and still glowing; or the bulb goes dark before it has been turned; or the bulb goes dark with the hand not yet on it; or the bulb relights once out.
- P2 [core · process_direction]
  - expect: Once dark, the bulb stays dark while it is out of the socket.
  - fail: The bulb glows in the hand away from the lamp; or flickers on and off as it is withdrawn; or the socket glows after the bulb is out.
- P3 [major · missing_consequence]
  - expect: The light the lamp cast disappears with the bulb: the shade darkens and the surfaces it lit go dimmer.
  - fail: The bulb is dark while its light on the table and wall stays; or the shade keeps glowing with the bulb out; or the room brightens as the bulb goes dark.
- P4 [major · trajectory_momentum]
  - expect: The bulb turns about its axis in the socket and rises out of it along that axis; the lamp stays put.
  - fail: The bulb comes straight out without turning; or slides sideways out of the socket; or the lamp turns with the bulb; or the lamp lifts off the table.
- P5 [fatal · solidity]
  - expect: One bulb leaves one socket whole; the bulb, socket and shade keep their shapes; fingers pass through nothing.
  - fail: The bulb passes through the shade or the lamp's body; or a second bulb appears in the socket; or the bulb changes shape or splits; or fingers pass through the bulb.
- P6 [minor · attribute_drift]
  - expect: The shade's colour, the lamp's base and the table stay the same apart from the light.
  - fail: The shade changes colour rather than brightness; or the base changes shape; or the table's contents rearrange.

## ELEC-0008 · switch_light · train

**Caption.** An old bulb in a ceiling fixture flashes bright for an instant and then goes dark for good.

**Expectation (hidden).** The flash is brief, the room goes dark right after, and the bulb does not come back on however long one waits; the switch stays where it was.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A ceiling fixture with a bulb, lit.
- S2 [core] The bulb flashes bright for an instant.
- S3 [core] The bulb goes dark.
- S4 [minor] The bulb stays dark for the rest of the clip.
- S5 [minor] The order is lit, flash, dark.

**PC**
- P1 [core · process_direction]
  - expect: The flash is a single brief brightening and the bulb then goes dark and stays dark; it does not come back on however long the clip runs.
  - fail: The bulb comes back on after going dark; or flickers between lit and dark repeatedly; or the flash lasts to the end of the clip; or the bulb dims slowly instead of flashing and going out.
- P2 [core · permanence_count]
  - expect: One fixture with one bulb; the bulb stays in the fixture, dark rather than gone; the room's contents are the same before and after.
  - fail: The bulb vanishes rather than going dark; or a second bulb appears; or the fixture moves along the ceiling; or furniture appears or vanishes between the lit and dark frames.
- P3 [major · missing_consequence]
  - expect: The room's light follows the bulb: it brightens at the flash and goes dim when the bulb dies, with whatever remains lit coming from windows or other sources present before.
  - fail: The bulb goes dark while the room stays as bright; or the room darkens while the bulb still glows; or the room brightens as the bulb dies; or light stays pooled under the dark fixture.
- P4 [major · causeless_motion]
  - expect: The fixture hangs still through the flash; nothing in the room moves at the flash or the blackout.
  - fail: The fixture swings at the flash; or the light switch on the wall moves by itself; or objects in the room shift at the moment the bulb dies.
- P5 [fatal · shape_identity]
  - expect: The fixture and bulb keep their shapes; the bulb does not shatter into the room or melt.
  - fail: The bulb explodes and fragments fly; or the fixture melts or changes shape; or the bulb turns into a different object; or the ceiling opens.
- P6 [minor · attribute_drift]
  - expect: The fixture's design, the ceiling and the room's colours stay the same apart from brightness.
  - fail: The fixture changes shape or colour; or the ceiling changes colour rather than brightness; or the walls change colour.

**Note.** A faint glow fading in the filament after the flash is the expected look of a dying bulb and is not a violation.

## ELEC-0009 · switch_light · train

**Caption.** A string of fairy lights is plugged into a wall socket, and the whole string lights up along its length.

**Expectation (hidden).** All the bulbs come on together the moment the plug goes in; none light before, and none stay dark while the rest glow.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A string of fairy lights and a wall socket.
- S2 [core] The string's plug is pushed into the socket.
- S3 [core] The whole string lights up along its length.
- S4 [minor] The string is dark before the plug goes in.
- S5 [minor] The order is dark, plug in, lit.

**PC**
- P1 [core · missing_consequence]
  - expect: The bulbs come on at the moment the plug seats in the socket, and only then, all together.
  - fail: The plug is in and the string stays dark; or the bulbs are lit before the plug reaches the socket; or the string lights up while the plug lies loose; or the bulbs come on one after another from one end rather than together.
- P2 [core · permanence_count]
  - expect: The lit bulbs are the same bulbs seen dark: the same number at the same spots along the wire, and none stays dark while the rest glow.
  - fail: Lit points appear along the wire where no bulb hung; or bulbs seen on the dark string are gone once lit; or lit bulbs multiply or shift along the wire; or a stretch of the string stays dark while the rest glows.
- P3 [major · process_direction]
  - expect: Once on, the string stays lit while the plug stays in, and the glow sits at the bulbs.
  - fail: The string goes dark again with the plug seated and untouched; or flickers on and off; or the glow spreads onto the bare wire between bulbs; or the plug backs out of the socket by itself.
- P4 [major · material_response]
  - expect: The wire hangs or lies slack in curves and stays attached at both ends; the plug enters the socket as a rigid piece.
  - fail: The wire stands rigid in the air; or stretches like elastic as the plug is pushed in; or the wire floats; or the plug bends as it goes in.
- P5 [fatal · solidity]
  - expect: One string, one plug, one socket; the plug enters the socket rather than the wall; fingers stay outside the wall.
  - fail: The plug passes into the wall beside the socket; or the wire passes through a wall or piece of furniture; or the string splits in two; or a second plug appears.
- P6 [minor · attribute_drift]
  - expect: The wire's colour, the socket's design and the background stay the same apart from the light.
  - fail: The wire changes colour; or the socket changes design or moves; or the background rearranges.

## ELEC-0010 · switch_light · train

**Caption.** The button on an electric kettle is pressed, and a small light on the kettle comes on and the switch stays down.

**Expectation (hidden).** The indicator lights at the press and stays lit while the switch is down; when the switch pops up later, the light goes out.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] An electric kettle with a button or switch.
- S2 [core] The button is pressed.
- S3 [core] A small light on the kettle comes on.
- S4 [core] The switch stays down after the press.
- S5 [minor] The light is dark before the press.
- S6 [minor] The order is dark, press, lit with the switch down.

**PC**
- P1 [core · missing_consequence]
  - expect: The light comes on at the moment the switch goes down, and only then; while the switch is down the light stays on.
  - fail: The switch is down and the light stays dark; or the light is lit before the switch is touched; or the light comes on with the switch still up; or the switch goes down and springs back up at once with the light staying on.
- P2 [core · process_direction]
  - expect: The switch stays down and the light stays lit for the rest of the clip; if the switch pops up, the light goes out with it.
  - fail: The light goes out with the switch still down; or the switch pops up and the light stays lit; or the light flickers on and off; or the switch goes up and down by itself.
- P3 [major · process_direction] (if: Steam is visible.)
  - expect: Any steam from the spout appears only after the switch is down and grows from there.
  - fail: Steam pours from the spout before the button is pressed; or steam appears and shrinks back into the spout; or steam rises from the base rather than the spout.
- P4 [major · causeless_motion]
  - expect: The kettle stays on its base as the button is pressed; the base and counter stay still.
  - fail: The kettle slides or lifts off its base at the press; or the base moves by itself; or items on the counter jump.
- P5 [fatal · permanence_count]
  - expect: One kettle on one base; the kettle keeps its shape with the lid on; the finger passes through nothing.
  - fail: A second kettle appears; or the kettle vanishes; or the finger passes into the kettle; or the kettle's spout or handle moves or vanishes.
- P6 [minor · attribute_drift]
  - expect: The kettle's colour, the base and the counter stay the same apart from the light.
  - fail: The kettle changes colour; or the switch moves to a different place on the kettle; or items on the counter change.

## ELEC-0011 · switch_light · train

**Caption.** The knob of a night light in a dark bedroom is turned, and the little lamp glows.

**Expectation (hidden).** The glow appears when the knob clicks and stays steady; turning the knob back puts it out.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A night light in a dark bedroom.
- S2 [core] The knob of the night light is turned.
- S3 [core] The little lamp glows.
- S4 [minor] The room is dark before the turn.
- S5 [minor] The order is dark, turn, glow.

**PC**
- P1 [core · missing_consequence]
  - expect: The glow appears at the moment the knob turns, and only then.
  - fail: The knob is turned and the lamp stays dark; or the lamp glows before the knob is touched; or the lamp comes on with the knob untouched; or the glow appears somewhere other than the lamp.
- P2 [core · process_direction]
  - expect: Once on, the glow stays steady for the rest of the clip while the knob is left alone.
  - fail: The lamp goes dark again by itself; or flickers on and off; or the knob turns back by itself; or the glow brightens and dims repeatedly.
- P3 [major · missing_consequence]
  - expect: The glow lights the wall and surface around the lamp, centred on it, and the room is dimmer further away.
  - fail: The lamp glows while the wall beside it stays as dark as before; or the room brightens while the lamp stays dark; or the pool of light sits away from the lamp.
- P4 [major · causeless_motion]
  - expect: The night light stays where it is as the knob turns; nothing else in the room moves.
  - fail: The night light slides or tips at the turn; or the bedding or curtains move; or objects on the nightstand shift.
- P5 [fatal · permanence_count]
  - expect: One night light; it keeps its shape and place; the hand passes through nothing.
  - fail: A second night light appears; or the night light vanishes; or the hand passes through it; or the night light changes shape.
- P6 [minor · attribute_drift]
  - expect: The night light's colour and shape, the wall and the room's contents stay the same apart from the glow.
  - fail: The night light changes colour rather than brightness; or the wall changes colour; or the nightstand's contents rearrange.

## ELEC-0012 · switch_light · train

**Caption.** A power strip with four lamps plugged into it is switched on, and all four lamps come on at once.

**Expectation (hidden).** The four lamps light at the same instant as the strip's switch; none lights early or stays off.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A power strip with four lamps plugged into it.
- S2 [core] The strip's switch is turned on.
- S3 [core] All four lamps come on.
- S4 [minor] The lamps come on at the same moment, not one after another.
- S5 [minor] The lamps are dark before the switch.

**PC**
- P1 [core · missing_consequence]
  - expect: All four lamps come on at the moment the strip's switch is pressed, and only then.
  - fail: The switch is pressed and one or more lamps stay dark; or a lamp is lit before the switch is touched; or the lamps light one after another; or the lamps come on with the switch untouched.
- P2 [core · permanence_count]
  - expect: The four lamps seen dark are the four lamps seen lit: the same lamps in the same places, none appearing or vanishing.
  - fail: A fifth lamp appears lit; or a lamp vanishes at the switch; or a lamp changes place; or the strip gains or loses sockets.
- P3 [major · process_direction]
  - expect: Once on, all four lamps stay lit while the switch stays on.
  - fail: A lamp goes out again with the switch untouched; or lamps flicker; or the switch flips back by itself; or a lamp dims to dark while the others glow.
- P4 [major · missing_consequence]
  - expect: The lamps' light reaches their surroundings: shades glow and the surfaces beneath brighten, with shadows pointing away from each lamp.
  - fail: The bulbs glow while the shades and surfaces stay as dark as before; or the surroundings brighten while the lamps stay dark; or the light comes from elsewhere.
- P5 [fatal · solidity]
  - expect: One strip with four plugs in it; the strip and lamps keep their shape; cords stay attached; the hand passes through nothing.
  - fail: A plug passes into the strip's body beside a socket; or a cord splits or detaches; or a lamp changes shape; or the hand passes through the strip.
- P6 [minor · attribute_drift]
  - expect: The lamps' shade colours, the strip's colour and the floor stay the same apart from the light.
  - fail: A shade changes colour rather than brightness; or the strip changes colour; or the cords change colour.

## ELEC-0013 · switch_light · train

**Caption.** The power button on a laptop is pressed, and the screen lights up and the keyboard glows.

**Expectation (hidden).** The screen and keys light shortly after the press; nothing lights before the button is touched.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A laptop with its screen dark.
- S2 [core] The power button is pressed.
- S3 [core] The screen lights up.
- S4 [core] The keyboard glows.
- S5 [minor] The keys are unlit before the press.
- S6 [minor] The order is dark, press, screen and keys lit.

**PC**
- P1 [core · missing_consequence]
  - expect: The screen and the keyboard light shortly after the press, and only then.
  - fail: The button is pressed and the screen stays dark to the end of the clip; or the screen is lit before the press; or the keys glow while the screen stays dark to the end; or the laptop lights up with nothing touching it.
- P2 [core · process_direction]
  - expect: Once on, the screen and keyboard stay lit for the rest of the clip.
  - fail: The screen goes dark again by itself; or the keyboard glow switches on and off; or the screen flickers between lit and dark; or the screen lights and shrinks back to black.
- P3 [major · missing_consequence]
  - expect: The screen's glow reaches the keys and the desk in front of it; the keyboard glow sits at the keys.
  - fail: The screen is lit while the keys and desk in front stay as dark as before; or the glow lies on the desk while the screen is dark; or the keyboard glow sits between the keys and not on them.
- P4 [major · causeless_motion]
  - expect: The laptop stays put on the desk as the button is pressed; the lid does not move by itself.
  - fail: The laptop slides or turns on the desk at the press; or the lid opens further or closes by itself; or items on the desk jump.
- P5 [fatal · permanence_count]
  - expect: One laptop with one screen and one keyboard; the laptop keeps its shape; the finger passes through nothing.
  - fail: A second screen appears; or keys appear or vanish; or the finger passes into the keyboard; or the laptop changes shape.
- P6 [minor · attribute_drift]
  - expect: The laptop's colour, its key layout and the desk stay the same apart from the light.
  - fail: The laptop changes colour; or the key layout changes; or the desk's contents rearrange.

**Note.** What the screen shows is not judged; any content counts as lit.

## ELEC-0014 · switch_light · train

**Caption.** A light switch is flicked up and down several times in quick succession, and the ceiling light goes on and off in step with each flick.

**Expectation (hidden).** Every flick changes the light's state immediately; the light never lags a flick or changes on its own.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A light switch and a ceiling light in the same room.
- S2 [core] The switch is flicked up and down several times in quick succession.
- S3 [core] The ceiling light goes on and off with the flicks.
- S4 [minor] There are several flicks, not one.
- S5 [minor] Each change of the light follows a flick.

**PC**
- P1 [core · missing_consequence]
  - expect: Every flick changes the light's state at once: each time the switch moves the light goes from off to on or on to off.
  - fail: The switch moves and the light stays as it was; or the light changes while the switch is still; or the light changes only after a delay while the switch has already moved again; or the light changes twice for one flick.
- P2 [core · process_direction]
  - expect: Between flicks the light holds its state; after the last flick it stays in that state for the rest of the clip.
  - fail: The light flickers between flicks with the switch still; or changes state after the flicking has stopped; or dims gradually rather than switching; or the switch moves by itself.
- P3 [major · missing_consequence]
  - expect: The room brightens and darkens with the light: the walls and floor under the fixture follow each change.
  - fail: The fixture goes dark while the room stays as bright; or the room changes brightness while the fixture stays as it was; or light stays pooled under the dark fixture.
- P4 [major · causeless_motion]
  - expect: Nothing else in the room moves as the switch is flicked; the fixture hangs still.
  - fail: Doors or objects move at the flicks; or the fixture swings; or the switch plate slides on the wall.
- P5 [fatal · permanence_count]
  - expect: One switch and one ceiling light; both stay in place; the hand passes through nothing.
  - fail: A second switch or light appears; or the fixture vanishes or moves across the ceiling; or the hand passes into the wall; or the room's contents appear or vanish between lit and dark frames.
- P6 [minor · attribute_drift]
  - expect: The wall colour, the fixture and the room's contents stay the same apart from brightness.
  - fail: The wall changes colour rather than brightness; or the fixture changes shape; or pictures or furniture change.

## ELEC-0015 · switch_light · train

**Caption.** The call button beside an elevator is pressed, and the button lights up.

**Expectation (hidden).** The button glows from the moment it is pressed and stays lit; it does not light before being pressed.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A call button beside an elevator.
- S2 [core] The button is pressed.
- S3 [core] The button lights up.
- S4 [minor] The button is dark before the press.
- S5 [minor] The order is dark, press, lit.

**PC**
- P1 [core · missing_consequence]
  - expect: The button lights at the moment it is pressed, and only then.
  - fail: The button is pressed and stays dark; or the button is lit before it is pressed; or the button lights with nothing touching it; or a different button lights instead.
- P2 [core · process_direction]
  - expect: Once lit, the button stays lit for the rest of the clip, or goes out only when the elevator doors open.
  - fail: The button goes dark again with the doors still closed; or flickers on and off; or brightens and dims repeatedly; or lights and goes out with each frame.
- P3 [major · causeless_motion]
  - expect: The button and its plate stay in the wall as they are pressed; the doors stay closed until they open in one motion.
  - fail: The plate moves along the wall; or the button sinks deep into the wall and stays sunk; or the doors jerk open and shut repeatedly; or the floor indicator numbers spin.
- P4 [major · missing_consequence]
  - expect: The button's glow lights the plate around it faintly; the glow is at the button and nowhere else.
  - fail: The glow appears on the wall away from the button while the button stays dark; or the whole plate lights up as brightly as the button; or the glow floats in front of the wall.
- P5 [fatal · permanence_count]
  - expect: One button plate with its buttons in fixed places; the doors and wall keep their shape; the finger passes through nothing.
  - fail: Buttons appear or vanish; or a second plate appears; or the finger passes into the wall; or the elevator doors change shape or vanish.
- P6 [minor · attribute_drift]
  - expect: The plate's finish, the doors' colour and the wall stay the same apart from the glow.
  - fail: The plate changes colour; or the doors change colour; or the floor numbers change style.

## ELEC-0016 · switch_light · train

**Caption.** The light chain on a ceiling fan is pulled, and the light above the fan comes on while the blades stay still.

**Expectation (hidden).** Only the light responds to that chain; the blades do not start turning; a second chain would be needed for the fan.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A ceiling fan with a light above or beneath it and a pull chain.
- S2 [core] The light chain is pulled.
- S3 [core] The light comes on.
- S4 [core] The blades stay still.
- S5 [minor] The light is dark before the pull.
- S6 [minor] The order is dark and still, pull, lit and still.

**PC**
- P1 [core · missing_consequence]
  - expect: The light comes on at the moment the chain is pulled, and only then.
  - fail: The chain is pulled and the light stays dark; or the light is lit before the chain moves; or the light comes on with the chain hanging untouched; or the light comes on well after the pull with nothing else happening.
- P2 [core · causeless_motion]
  - expect: The blades stay still before, during and after the pull; the fan does not start turning by itself.
  - fail: The blades start turning when the chain is pulled; or the blades turn slowly by themselves before the pull; or the blades spin up after the light is on with nothing touched; or the blades jerk or rock.
- P3 [major · process_direction]
  - expect: Once on, the light stays lit for the rest of the clip.
  - fail: The light goes off again by itself; or flickers on and off; or dims back to dark; or the chain pulls itself again.
- P4 [major · material_response]
  - expect: The chain hangs straight down, is drawn taut by the pull and swings then hangs slack again; the fan body stays fixed to the ceiling.
  - fail: The chain stands rigid or stays stretched out sideways after the pull; or stretches like elastic; or the fan body swings or tilts with the pull; or the chain floats.
- P5 [fatal · permanence_count]
  - expect: One fan with a fixed number of blades and one light; the fan stays on the ceiling; the hand passes through nothing.
  - fail: Blades appear or vanish; or the fan moves across the ceiling; or a second chain or light appears; or the hand passes through the chain or the fan.
- P6 [minor · attribute_drift]
  - expect: The fan's colour, the blade finish and the ceiling stay the same apart from the light.
  - fail: The fan changes colour; or the blades change shape; or the ceiling changes colour rather than brightness.

## ELEC-0017 · switch_light · train

**Caption.** A hairdryer resting on a counter with ribbons tied to its nozzle is switched on, and the ribbons stream out in the airflow.

**Expectation (hidden).** The ribbons hang slack before the switch, lift and stream the moment it is on, and keep streaming while it runs; they do not move while the dryer is off.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A hairdryer rests on a counter with ribbons tied to its nozzle.
- S2 [core] The hairdryer is switched on.
- S3 [core] The ribbons stream out in the airflow.
- S4 [minor] The ribbons hang slack before the switch.
- S5 [minor] The order is slack, switch, streaming.

**PC**
- P1 [core · missing_consequence]
  - expect: The ribbons lift and stream away from the nozzle at the moment the switch is moved, and only then.
  - fail: The switch is moved and the ribbons hang slack to the end of the clip; or the ribbons stream before the switch is touched; or the ribbons stream while the dryer lies untouched; or the ribbons blow toward the nozzle.
- P2 [core · process_direction]
  - expect: While the dryer runs the ribbons keep streaming and fluttering in the same direction; they drop slack only if the dryer is switched off.
  - fail: The ribbons fall slack while the dryer is still on; or stream and drop repeatedly with the switch untouched; or stiffen into a fixed shape; or the switch moves back by itself.
- P3 [major · trajectory_momentum]
  - expect: The ribbons stream away from the nozzle along the direction it points, rippling along their length.
  - fail: The ribbons stream sideways or backward from the nozzle; or stand straight up from a nozzle pointing along the counter; or each ribbon streams in a different direction.
- P4 [major · causeless_motion]
  - expect: The dryer stays where it rests as it runs, apart from a small shift; other items on the counter stay put unless in the airflow.
  - fail: The dryer slides or spins across the counter; or lifts into the air; or items behind the dryer blow away; or light items in the airflow stay perfectly still.
- P5 [fatal · permanence_count]
  - expect: One dryer with its ribbons tied on; the ribbons stay attached to the nozzle; the dryer keeps its shape.
  - fail: Ribbons detach and fly off; or ribbons appear or vanish; or a second dryer appears; or the dryer changes shape.
- P6 [minor · attribute_drift]
  - expect: The dryer's colour, the ribbons' colours and the counter stay the same.
  - fail: The dryer changes colour; or a ribbon changes colour or length; or the counter's contents rearrange.

## ELEC-0018 · switch_light · train

**Caption.** The button on an electric toothbrush lying on a counter is pressed, and the head starts buzzing and vibrating.

**Expectation (hidden).** The vibration starts at the press and stops at the next press; the brush does not vibrate on its own.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] An electric toothbrush lies on a counter.
- S2 [core] Its button is pressed.
- S3 [core] The head starts vibrating.
- S4 [minor] The brush is still before the press.
- S5 [minor] The order is still, press, vibrating.

**PC**
- P1 [core · missing_consequence]
  - expect: The head begins to vibrate at the moment the button is pressed, and only then.
  - fail: The button is pressed and the brush stays still to the end of the clip; or the head vibrates before the press; or the brush buzzes while lying untouched; or the handle vibrates while the head is still.
- P2 [core · causeless_motion]
  - expect: Before the press nothing on the brush moves; afterwards the head vibrates steadily until the button is pressed again.
  - fail: The brush stops and restarts with the button untouched; or the brush jumps across the counter by itself; or the head vibrates in bursts with nothing pressed; or the brush rolls away with no hand on it.
- P3 [major · trajectory_momentum]
  - expect: The vibration is a small rapid shake of the head; the handle stays in place or drifts slowly on the counter.
  - fail: The head swings in wide arcs; or the whole brush spins round; or the brush lifts off the counter; or the head rotates like a drill bit while the caption's brush is a plain head.
- P4 [major · material_response]
  - expect: The brush is a rigid plastic handle with a stiff head; it keeps its shape while vibrating.
  - fail: The handle bends or wobbles like rubber; or the head stretches; or the bristles flow like liquid.
- P5 [fatal · permanence_count]
  - expect: One toothbrush; it keeps its head and handle; the finger passes through nothing.
  - fail: A second brush appears; or the head detaches; or the brush vanishes; or the finger passes into the handle.
- P6 [minor · attribute_drift]
  - expect: The brush's colour and the counter stay the same.
  - fail: The brush changes colour; or the bristles change colour; or the counter's contents rearrange.

**Note.** The buzz is sound and is not judged; vibration is read from visible shaking of the head or blur at its edges.

## ELEC-0019 · switch_light · train

**Caption.** The button on a garage door remote is pressed, and the garage light comes on and the door begins to rise.

**Expectation (hidden).** The light and the door motor respond together right after the press; the door does not move before the button is pressed.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A garage with its door closed and a remote in view.
- S2 [core] The remote's button is pressed.
- S3 [core] The garage light comes on.
- S4 [core] The door begins to rise.
- S5 [minor] The light is off and the door still before the press.
- S6 [minor] The order is press, then light and door together.

**PC**
- P1 [core · missing_consequence]
  - expect: The light comes on and the door starts to rise together, right after the press, and only then.
  - fail: The button is pressed and neither light nor door responds to the end of the clip; or the door rises while the light stays dark; or the light comes on while the door stays shut to the end; or the door begins to move before the button is pressed.
- P2 [core · causeless_motion]
  - expect: The door is still before the press and moves only after it, rising steadily in one direction.
  - fail: The door rises before the press; or stops and starts with nothing pressed; or rises and drops back; or rattles in place without rising.
- P3 [major · trajectory_momentum]
  - expect: The door rises along its tracks as one panel or as hinged sections following each other, its bottom edge lifting off the ground.
  - fail: The door swings outward like a gate while its tracks show a roll-up door; or the sections separate; or the door rises faster at one side so it tilts; or the door lifts as a whole off its tracks.
- P4 [major · missing_consequence]
  - expect: The light lights the garage: the floor and walls inside brighten from the fixture.
  - fail: The fixture glows while the garage stays as dark as before; or the garage brightens while the fixture stays dark; or the light comes from a place other than the fixture.
- P5 [fatal · solidity]
  - expect: One door in its frame; the door passes through nothing and stays attached; the light fixture stays on the ceiling.
  - fail: The door passes through its frame or the ceiling; or a second door appears; or the door vanishes; or the fixture drops or vanishes.
- P6 [minor · attribute_drift]
  - expect: The door's colour and panelling, the remote and the garage contents stay the same apart from the light.
  - fail: The door changes colour or panel pattern; or the remote changes shape; or the garage contents rearrange.

## ELEC-0020 · switch_light · train

**Caption.** A neon shop sign is switched on, and the tubes flicker and then glow steadily.

**Expectation (hidden).** The glow appears only after the switch and settles to a steady light; when switched off the tubes go dark at once.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A neon shop sign, dark.
- S2 [core] The sign is switched on.
- S3 [core] The tubes flicker.
- S4 [core] The tubes then glow steadily.
- S5 [minor] The sign is dark before the switch.
- S6 [minor] The order is dark, switch, flicker, steady glow.

**PC**
- P1 [core · missing_consequence]
  - expect: The tubes begin to light at the switch, and only then.
  - fail: The switch is thrown and the sign stays dark to the end of the clip; or the tubes glow before the switch is touched; or the sign lights up with the switch untouched; or only the frame lights and the tubes stay dark.
- P2 [core · process_direction]
  - expect: The flicker comes first and settles into a steady glow that lasts for the rest of the clip; the sign does not go back to flickering or dark.
  - fail: The sign glows steadily and then starts flickering; or goes dark again after glowing; or flickers to the end of the clip without ever settling; or the glow fades out and returns.
- P3 [major · permanence_count]
  - expect: The lit tubes are the tubes seen dark: the same shapes and letters in the same places; the glow follows the tube's path.
  - fail: Lit letters appear where no tube was; or a tube seen dark is gone once lit; or the glow spreads off the tubes into the air; or the letters change shape or spelling.
- P4 [major · missing_consequence]
  - expect: The sign's glow reaches its surroundings: the wall behind and the pavement below take on the sign's colour.
  - fail: The tubes glow while the wall behind stays as dark as before; or the wall brightens while the tubes stay dark; or the glow on the wall is a different colour from the tubes.
- P5 [fatal · shape_identity]
  - expect: The sign keeps its tubes, frame and mounting; nothing passes through the wall.
  - fail: The sign vanishes or a second sign appears; or the tubes bend into new shapes; or the sign passes into the wall; or the frame melts.
- P6 [minor · attribute_drift]
  - expect: The sign's tube colours and the shopfront stay the same apart from the glow.
  - fail: A tube changes colour once steady; or the shopfront changes; or the lettering changes font.

## ELEC-0021 · switch_light · train

**Caption.** The top of a touch-sensitive lamp is tapped, and it lights up.

**Expectation (hidden).** The lamp lights at the touch and stays on; it does not change state without a touch.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A lamp with a touch-sensitive body.
- S2 [core] The top of the lamp is tapped.
- S3 [core] The lamp lights up.
- S4 [minor] The lamp is dark before the tap.
- S5 [minor] The order is dark, tap, lit.

**PC**
- P1 [core · missing_consequence]
  - expect: The lamp lights at the moment the fingertip touches it, and only then.
  - fail: The lamp is tapped and stays dark; or the lamp is lit before the touch; or the lamp comes on while the hand is still away from it; or the lamp lights when the table beside it is tapped.
- P2 [core · process_direction]
  - expect: Once lit the lamp stays lit steadily until it is touched again.
  - fail: The lamp goes dark again with nothing touching it; or flickers on and off; or changes brightness repeatedly with the hand withdrawn; or lights and fades out at once.
- P3 [major · missing_consequence]
  - expect: The lamp's light reaches its surroundings: the shade glows and nearby surfaces brighten, with shadows pointing away from the lamp.
  - fail: The bulb glows while the shade and table stay as dark as before; or the surroundings brighten while the lamp stays dark; or the light comes from a place other than the lamp.
- P4 [major · causeless_motion]
  - expect: The lamp stays put as it is tapped; nothing else on the table moves.
  - fail: The lamp slides, tips or lifts at the tap; or items on the table jump; or the shade turns by itself.
- P5 [fatal · permanence_count]
  - expect: One lamp; it keeps its shape; the finger touches its surface and passes through nothing.
  - fail: A second lamp appears; or the lamp vanishes; or the finger passes into the lamp; or the lamp changes shape.
- P6 [minor · attribute_drift]
  - expect: The lamp's colour and shade, the table and the wall stay the same apart from the light.
  - fail: The shade changes colour rather than brightness; or the base changes; or the table's contents rearrange.

## ELEC-0022 · switch_light · train

**Caption.** The switch on the underside of a remote-controlled toy car is flicked on, and its headlights light up.

**Expectation (hidden).** The headlights come on with the switch and stay on; the car stays still and does not drive off, since no controller is used; nothing lights while the switch is off.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A remote-controlled toy car, upside down or tilted so its underside is in view.
- S2 [core] A switch on the underside is flicked on.
- S3 [core] The car's headlights light up.
- S4 [minor] No controller is used: no hand holds a transmitter.
- S5 [minor] The order is dark, flick, headlights lit.

**PC**
- P1 [core · missing_consequence]
  - expect: The headlights come on at the moment the switch is flicked, and only then, and stay on.
  - fail: The switch is flicked and the headlights stay dark; or the headlights are lit before the switch moves; or they come on with the switch untouched; or they go out again with the switch still on.
- P2 [core · causeless_motion]
  - expect: The car stays still: its wheels do not turn and it does not drive off, since no controller is used.
  - fail: The wheels spin up when the switch is flicked; or the car drives away by itself; or the car jerks or rocks with nothing touching it; or the steering turns by itself.
- P3 [major · missing_consequence] (if: The surface in front of the headlights is in view.)
  - expect: The headlights' glow reaches the surface in front of them.
  - fail: The lamps glow while the surface in front of them stays as dark as before; or the surface brightens while the lamps stay dark; or the lit patch lies behind the car.
- P4 [major · material_response]
  - expect: The car is a rigid plastic body on wheels; it keeps its shape as it is handled and set down.
  - fail: The body bends or squashes in the hand; or the wheels sag; or the car flexes like rubber when set down.
- P5 [fatal · permanence_count]
  - expect: One car with its wheels and lights attached; the finger passes through nothing.
  - fail: A wheel or light vanishes or appears; or a second car appears; or the finger passes into the car; or the car changes shape.
- P6 [minor · attribute_drift]
  - expect: The car's colour and decals and the surface it sits on stay the same apart from the light.
  - fail: The car changes colour; or its decals change; or the surface changes.

## ELEC-0023 · switch_light · train

**Caption.** A microwave door is opened, and the light inside the microwave comes on.

**Expectation (hidden).** The interior lights as the door opens and goes dark when it shuts; the turntable does not turn while the door is open.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A microwave with its door closed and interior dark.
- S2 [core] The door is opened.
- S3 [core] The light inside comes on.
- S4 [minor] The interior is dark before the door opens.
- S5 [minor] The order is closed and dark, open, lit.

**PC**
- P1 [core · missing_consequence]
  - expect: The interior lights as the door opens, and only then; if the door is shut again the light goes off with it.
  - fail: The door is open and the interior stays dark; or the interior is lit through the window before the door moves; or the light comes on with the door still shut and untouched; or the light stays on after the door has been shut.
- P2 [core · process_direction]
  - expect: Once open, the interior stays lit for as long as the door is open; the turntable does not turn.
  - fail: The light goes off with the door still open; or flickers; or the turntable turns while the door is open; or the door swings shut by itself.
- P3 [major · missing_consequence]
  - expect: The light comes from inside the cavity: the interior walls and anything inside are lit, and light spills out through the open door onto the counter.
  - fail: The cavity is dark while the counter in front brightens; or the interior glows while nothing inside casts a shadow; or the light comes from the door rather than the cavity.
- P4 [major · trajectory_momentum]
  - expect: The door swings open about its hinge as one rigid panel and stays where it is put.
  - fail: The door bends as it opens; or opens from the hinge side; or swings open and shut repeatedly; or comes off its hinge.
- P5 [fatal · permanence_count]
  - expect: One microwave with one door; the door stays attached; the hand passes through nothing; the interior's contents are the same as the door opens.
  - fail: The door detaches; or a second door appears; or the hand passes through the door; or food appears or vanishes inside as the light comes on.
- P6 [minor · attribute_drift]
  - expect: The microwave's colour, its controls and the counter stay the same apart from the light.
  - fail: The microwave changes colour; or the controls rearrange; or the counter's contents change.

## ELEC-0024 · switch_light · train

**Caption.** The start button on a blender is pressed, and the blades spin and the contents whirl.

**Expectation (hidden).** The blades and contents are still before the press and spin the instant it is pressed, running steadily; nothing moves before the button is touched.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A blender with contents in its jug.
- S2 [core] The start button is pressed.
- S3 [core] The blades spin.
- S4 [core] The contents whirl.
- S5 [minor] The blades and contents are still before the press.
- S6 [minor] The order is still, press, spinning and whirling.

**PC**
- P1 [core · missing_consequence]
  - expect: The blades start to spin and the contents start to move at the moment the button is pressed, and only then.
  - fail: The button is pressed and the blades stay still to the end of the clip; or the contents whirl before the press; or the blades spin while the contents stay still; or the contents whirl while the blades are still.
- P2 [core · causeless_motion]
  - expect: Before the press nothing in the jug moves; afterwards the blender runs steadily and does not stop, start or reverse on its own.
  - fail: The blades stop and restart with the button untouched; or the contents swirl before the button is touched; or the blades reverse direction; or the jug spins round with the blades.
- P3 [major · trajectory_momentum]
  - expect: The contents swirl round the jug in the direction of the blades, climbing the walls and dipping at the centre.
  - fail: The contents rise straight up as a column; or swirl against the blades' direction; or stay flat and still at the surface while the blades spin below; or the contents leap out of a closed jug.
- P4 [major · material_response]
  - expect: The contents flow as liquid or soft food; the jug stays rigid and the blades stay stiff.
  - fail: The contents move as a solid block; or the jug wobbles or bulges; or the blades bend or flop like rubber.
- P5 [fatal · permanence_count]
  - expect: One blender with one jug; the contents stay inside the jug; the finger passes through nothing.
  - fail: The contents pass through the jug's walls; or the jug vanishes or duplicates; or the finger passes into the base; or the contents change into something else or vanish.
- P6 [minor · attribute_drift]
  - expect: The blender's colour, the jug and the counter stay the same; the contents change only by mixing.
  - fail: The blender changes colour; or the jug changes shape; or the counter's contents rearrange.

**Note.** The contents turning smoother or changing colour as they blend is the expected result and is not judged.

## ELEC-0025 · switch_light · train

**Caption.** The knob of a desk fan is turned from off to high, and the blades spin up to speed.

**Expectation (hidden).** The blades are still while the knob is at off, start as it turns and speed up to a steady spin; they do not spin with the knob at off.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A desk fan with a knob.
- S2 [core] The knob is turned from off to high.
- S3 [core] The blades spin up to speed.
- S4 [minor] The blades are still before the knob turns.
- S5 [minor] The order is still, turn, spinning.

**PC**
- P1 [core · missing_consequence]
  - expect: The blades begin to turn as the knob leaves its off position, and only then, and speed up to a steady spin.
  - fail: The knob is turned and the blades stay still to the end of the clip; or the blades spin before the knob moves; or the blades start with the knob untouched; or the blades spin at full speed from the first frame with the knob at off.
- P2 [core · process_direction]
  - expect: The spin builds one way from still to steady and holds while the knob stays at high; it does not stop or slow on its own.
  - fail: The blades slow and stop with the knob still at high; or spin up and down repeatedly; or reverse direction; or the knob turns back by itself.
- P3 [major · trajectory_momentum]
  - expect: The blades spin about the hub as one piece with a smooth speed-up; the head may oscillate if built to.
  - fail: The blades wobble off the hub; or move independently of each other; or the spin jumps abruptly between fast and still; or the whole fan spins on its base.
- P4 [major · missing_consequence] (if: Light items such as paper, ribbons or hair are in front of the fan.)
  - expect: Light items in front of the fan flutter in the airflow once the blades spin and are still before.
  - fail: Ribbons or paper flutter before the blades turn; or nothing in front moves while the fan runs; or the flutter blows toward the fan.
- P5 [fatal · permanence_count]
  - expect: One fan with a fixed number of blades; the fan stays on the desk; the hand passes through nothing.
  - fail: Blades appear or vanish; or the fan duplicates; or the fan lifts off the desk; or the hand passes through the cage.
- P6 [minor · attribute_drift]
  - expect: The fan's colour, the cage pattern and the desk stay the same.
  - fail: The fan changes colour; or the cage pattern changes; or items on the desk rearrange.

## ELEC-0026 · switch_light · train

**Caption.** A traffic light at a quiet crossing changes from red to green, and the red lamp goes dark as the green lamp lights.

**Expectation (hidden).** Only one lamp is lit at a time and the change is instantaneous; the amber lamp does not light at the same time as green.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A traffic light at a crossing, showing red.
- S2 [core] The light changes to green.
- S3 [core] The red lamp goes dark.
- S4 [core] The green lamp lights.
- S5 [minor] The crossing is quiet: little or no traffic.
- S6 [minor] The red goes dark as the green lights, not long before or after.

**PC**
- P1 [core · missing_consequence]
  - expect: The red lamp goes dark and the green lamp lights at the same moment; only one lamp is lit at a time before and after.
  - fail: The red and green lamps are both lit together for a stretch; or the red goes dark and the green stays dark to the end of the clip; or the green lights while the red stays lit to the end; or the amber lamp lights together with the green.
- P2 [core · permanence_count]
  - expect: The signal head keeps its lamps in their fixed positions: red at top, amber in the middle, green at bottom, each staying where it is whether lit or dark.
  - fail: A lamp changes place on the head; or a fourth lamp appears; or a lamp vanishes rather than going dark; or the green glow appears in the red lamp's position.
- P3 [major · process_direction]
  - expect: Once the green is lit it stays lit for the rest of the clip and the red stays dark.
  - fail: The red comes back on while the green is still lit; or the green flickers; or the lamps swap back and forth; or the green fades slowly to dark.
- P4 [major · causeless_motion]
  - expect: The signal head and its pole stay still through the change; parked vehicles and street furniture do not move at the change.
  - fail: The head swings or turns at the change; or the pole moves; or a parked car jumps forward at the change; or signs shift.
- P5 [fatal · shape_identity]
  - expect: The signal head, pole and surroundings keep their shapes; nothing passes through anything.
  - fail: The head changes shape or merges with the pole; or a vehicle passes through the pole; or the head duplicates; or the road surface changes.
- P6 [minor · attribute_drift]
  - expect: The pole's colour, the head's housing and the crossing markings stay the same apart from the lamps.
  - fail: The housing changes colour; or the road markings change; or the pole changes shape.

**Note.** Vehicles moving off when the light turns green are driven and are not judged.

## ELEC-0027 · switch_light · train

**Caption.** A string of Christmas lights wound around a tree is switched on, and the tree lights up from the plug to the top all at once.

**Expectation (hidden).** Every bulb comes on together at the switch; none stays dark or comes on later; the lights do not brighten gradually.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A tree wound with a string of Christmas lights.
- S2 [core] The lights are switched on.
- S3 [core] The whole string lights up at once, from the plug end to the top.
- S4 [minor] The tree is dark before the switch.
- S5 [minor] The order is dark, switch, lit.

**PC**
- P1 [core · missing_consequence]
  - expect: Every bulb comes on together at the switch, and only then.
  - fail: The switch is thrown and the string stays dark; or the bulbs are lit before the switch is touched; or the bulbs come on one after another up the tree; or the string lights with the switch untouched.
- P2 [core · permanence_count]
  - expect: The lit bulbs are the same bulbs seen dark: the same number at the same spots along the wire; none stays dark while the rest glow.
  - fail: Lit points appear where no bulb hung; or bulbs seen dark are gone once lit; or lit bulbs multiply or shift along the wire; or a stretch of the string stays dark while the rest glows.
- P3 [major · process_direction]
  - expect: Once on, the lights stay lit steadily while the switch stays on.
  - fail: The lights go dark again with the switch untouched; or flicker; or brighten gradually from dim to full; or the switch moves back by itself.
- P4 [major · missing_consequence]
  - expect: The lights' glow reaches the tree: branches and ornaments near each bulb take on its colour.
  - fail: The bulbs glow while the branches around them stay as dark as before; or the tree brightens while the bulbs stay dark; or the glow sits on the wire between bulbs.
- P5 [fatal · shape_identity]
  - expect: One tree and one string; the tree keeps its shape and the string stays one continuous wire; nothing passes through the tree.
  - fail: The tree changes shape or vanishes; or the string splits or detaches; or ornaments appear or vanish at the switch; or the wire passes through the trunk.
- P6 [minor · attribute_drift]
  - expect: The tree's foliage, the ornaments' colours and the room stay the same apart from the light.
  - fail: The foliage changes colour rather than brightness; or ornaments change colour; or the room's contents rearrange.

## ELEC-0028 · switch_light · train

**Caption.** The button on a bicycle's rear light is pressed, and it begins to blink red.

**Expectation (hidden).** The blinking starts at the press and continues at a steady rhythm; another press stops it.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A bicycle's rear light.
- S2 [core] The button on the light is pressed.
- S3 [core] The light begins to blink red.
- S4 [minor] The light is dark before the press.
- S5 [minor] The order is dark, press, blinking.

**PC**
- P1 [core · missing_consequence]
  - expect: The blinking starts at the moment the button is pressed, and only then.
  - fail: The button is pressed and the light stays dark to the end of the clip; or the light blinks before the press; or the light comes on with nothing touching it; or the light glows steadily without blinking.
- P2 [core · process_direction]
  - expect: Once started, the light blinks at a steady rhythm for the rest of the clip and does not stop by itself.
  - fail: The blinking stops with the button untouched; or the rhythm changes abruptly; or the light switches to steady on; or the blinking fades out.
- P3 [major · missing_consequence] (if: The light is close to a surface that could show its glow.)
  - expect: Each blink lights the surface near the lamp: the mudguard, tyre or ground behind the bicycle glows red with each flash.
  - fail: The lamp blinks while the surface beside it stays as dark as before; or the surface glows while the lamp is dark; or the glow on the surface is a different colour from the lamp.
- P4 [major · causeless_motion]
  - expect: The bicycle stays where it stands as the button is pressed; the wheels do not turn.
  - fail: The bicycle rolls or tips at the press; or a wheel turns by itself; or the light swings on its mount.
- P5 [fatal · permanence_count]
  - expect: One rear light on one bicycle; the light stays on its mount; the finger passes through nothing.
  - fail: A second light appears; or the light detaches and floats; or the finger passes through the light; or the bicycle changes shape.
- P6 [minor · attribute_drift]
  - expect: The bicycle's frame colour, the light's housing and the background stay the same apart from the blinking.
  - fail: The frame changes colour; or the light's housing changes shape; or the blink changes colour from red.

## ELEC-0029 · switch_light · train

**Caption.** The green start button on a conveyor belt is pressed, and the belt begins to move.

**Expectation (hidden).** The belt is still before the press and starts moving the instant the button is pressed, running steadily in one direction and carrying anything on it along; nothing moves before the press and nothing else in the scene starts moving on its own.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A conveyor belt with a green start button.
- S2 [core] The green button is pressed.
- S3 [core] The belt begins to move.
- S4 [minor] The belt is still before the press.
- S5 [minor] The order is still, press, moving.

**PC**
- P1 [core · missing_consequence]
  - expect: The belt starts to move at the moment the button is pressed, and only then, and carries anything on it along.
  - fail: The button is pressed and the belt stays still to the end of the clip; or the belt moves before the press; or the belt moves with the button untouched; or the belt moves while items on it stay in place.
- P2 [core · causeless_motion]
  - expect: Before the press nothing on the belt or its frame moves; afterwards the belt runs steadily in one direction and nothing else in the scene starts moving on its own.
  - fail: The belt stops and restarts with nothing pressed; or reverses direction; or other machines in the scene start moving at the press; or items on the belt slide against the belt's direction.
- P3 [major · trajectory_momentum]
  - expect: The belt's surface moves as one continuous sheet over its rollers in one direction; items on it ride along at the belt's speed.
  - fail: The belt surface moves in patches at different speeds; or an item on the belt races ahead of the belt or lags behind while resting on it; or the rollers turn while the belt stays still; or the belt surface moves sideways off its rollers.
- P4 [major · material_response]
  - expect: The belt is a flexible band that bends round its rollers and lies flat between them; the frame stays rigid.
  - fail: The belt stands rigid off its rollers; or ripples like water; or the frame bends as the belt starts; or the belt stretches visibly.
- P5 [fatal · permanence_count]
  - expect: One belt on one frame; items on the belt keep their number and pass through nothing; the finger passes through nothing.
  - fail: Items on the belt appear or vanish; or an item sinks into the belt; or the belt splits; or the finger passes into the control panel.
- P6 [minor · attribute_drift]
  - expect: The belt's colour, the frame and the button's colour stay the same.
  - fail: The belt changes colour; or the frame changes; or the button changes colour or place.

## ELEC-0030 · switch_light · train

**Caption.** The key in a car's ignition is turned, and the dashboard lights up before the engine starts.

**Expectation (hidden).** The dashboard lights come on with the key turn; they do not light with the key out or before it is turned.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A car's ignition with a key in it, and the dashboard in view.
- S2 [core] The key is turned.
- S3 [core] The dashboard lights up.
- S4 [minor] The dashboard is dark before the turn.
- S5 [minor] The dashboard lights before any sign of the engine starting.

**PC**
- P1 [core · missing_consequence]
  - expect: The dashboard lights come on at the moment the key turns, and only then.
  - fail: The key is turned and the dashboard stays dark to the end of the clip; or the dashboard is lit before the key moves; or the dashboard lights with no key in the ignition; or the lights come on well after the turn with nothing else happening.
- P2 [core · process_direction]
  - expect: Once lit, the dashboard stays lit while the key stays turned; warning lights may go out one by one but the display does not go dark as a whole.
  - fail: The dashboard goes dark again with the key untouched; or flickers on and off; or the key turns back by itself; or the dashboard lights and goes dark repeatedly.
- P3 [major · causeless_motion]
  - expect: The car stays still as the key turns; the steering wheel and pedals do not move by themselves.
  - fail: The car rolls or rocks at the turn; or the steering wheel turns by itself; or the wipers sweep; or the gear lever moves.
- P4 [major · trajectory_momentum] (if: Dial needles are visible.)
  - expect: The needles on the dials sweep from rest to a position and settle; they do not spin round.
  - fail: A needle spins round its dial repeatedly; or needles jump between positions frame to frame; or a needle bends.
- P5 [fatal · permanence_count]
  - expect: One key in one ignition; one dashboard with its dials in fixed places; the hand passes through nothing.
  - fail: Dials appear or vanish; or a second key appears; or the hand passes through the wheel or dashboard; or the ignition moves along the column.
- P6 [minor · attribute_drift]
  - expect: The dashboard's colours and layout and the steering wheel stay the same apart from the lighting.
  - fail: The dashboard changes colour rather than brightness; or the layout changes; or the wheel changes shape.

**Note.** Whether the engine starts is not judged; the caption's event is the dashboard lighting first.

## ELEC-0031 · switch_light · train

**Caption.** A battery-powered lantern in a tent is switched on, and the tent lights up.

**Expectation (hidden).** The tent is dark before the switch and steadily lit from the lantern after it; the light does not appear before the switch.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A lantern inside a tent.
- S2 [core] The lantern is switched on.
- S3 [core] The tent lights up.
- S4 [minor] The lantern is battery powered: no cord runs from it.
- S5 [minor] The order is dark, switch, lit.

**PC**
- P1 [core · missing_consequence]
  - expect: The lantern lights at the moment its switch is moved, and only then.
  - fail: The switch is moved and the lantern stays dark; or the tent is lit before the switch is touched; or the lantern comes on with nothing touching it; or the tent brightens while the lantern stays dark.
- P2 [core · process_direction]
  - expect: Once on, the lantern stays lit steadily and the tent stays lit for the rest of the clip.
  - fail: The lantern goes out again by itself; or flickers; or dims back to dark; or the switch moves back by itself.
- P3 [major · missing_consequence]
  - expect: The light comes from the lantern: the tent's walls and floor brighten most nearest it, and shadows of objects point away from it.
  - fail: The lantern glows while the tent walls stay as dark as before; or the light comes from a place other than the lantern; or shadows point toward the lantern; or the tent is lit evenly with no brighter side.
- P4 [major · causeless_motion]
  - expect: The lantern stays where it is as it is switched on; the tent and its contents stay put.
  - fail: The lantern slides or swings with nothing touching it; or the tent walls billow at the switch; or objects in the tent shift.
- P5 [fatal · permanence_count]
  - expect: One lantern; the tent's contents are the same before and after; the hand passes through nothing.
  - fail: A second lantern appears; or objects appear or vanish between dark and lit frames; or the hand passes through the lantern; or the tent changes shape.
- P6 [minor · attribute_drift]
  - expect: The tent's fabric colour, the lantern's colour and the gear inside stay the same apart from brightness.
  - fail: The fabric changes colour rather than brightness; or the lantern changes colour; or the gear rearranges.

## ELEC-0032 · switch_light · train

**Caption.** A fingertip holds down the doorbell button beside a front door, and a small light in the button glows while it is pressed and goes out when it is released.

**Expectation (hidden).** The glow appears only while the button is pressed and goes out when released.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A doorbell button beside a front door.
- S2 [core] A fingertip holds the button down.
- S3 [core] A small light in the button glows while it is pressed.
- S4 [core] The light goes out when the button is released.
- S5 [minor] The button is dark before the press.
- S6 [minor] The order is dark, press and glow, release and dark.

**PC**
- P1 [core · missing_consequence]
  - expect: The light comes on when the fingertip presses the button and goes out when the finger lifts; it glows only while pressed.
  - fail: The button is pressed and stays dark; or glows before the finger reaches it; or stays lit after the finger has lifted; or goes out while the finger still holds it down.
- P2 [core · process_direction]
  - expect: While the button is held the glow is steady; after release the button stays dark for the rest of the clip.
  - fail: The glow flickers while the button is held steady; or comes back on after release with nothing touching it; or the button lights and goes out repeatedly during one press.
- P3 [major · causeless_motion]
  - expect: The door, the frame and the button plate stay still; only the finger and the button's small travel move.
  - fail: The door opens at the press with no one behind it; or the plate slides on the wall; or the button sinks deep into the wall and stays sunk.
- P4 [major · missing_consequence]
  - expect: The glow is small: it lights the button and its rim and no more.
  - fail: The whole doorway lights up when the button glows; or the glow appears on the wall away from the button; or the porch light comes on at the press.
- P5 [fatal · permanence_count]
  - expect: One button on one plate; the finger touches the button and passes through nothing; the door keeps its shape.
  - fail: A second button appears; or the finger passes into the wall; or the plate vanishes; or the door changes shape.
- P6 [minor · attribute_drift]
  - expect: The door's colour, the plate's finish and the wall stay the same apart from the glow.
  - fail: The door changes colour; or the plate changes shape or finish; or the glow changes colour.

**Note.** The hand is kept because the caption's event is the press; the person is otherwise not judged. The chime is sound and is not judged.

## ELEC-0033 · switch_light · train

**Caption.** The dial of an electric stove burner is turned off, and the red-hot coil's glow dims.

**Expectation (hidden).** The glow fades gradually after the dial is turned, from bright to dull red to dark, and never brightens again; it does not go out instantly like a lamp.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] An electric stove with a coil burner glowing red.
- S2 [core] The burner's dial is turned to off.
- S3 [core] The coil's glow dims.
- S4 [minor] The coil is glowing before the dial is turned.
- S5 [minor] The order is glowing, turn, dimming.

**PC**
- P1 [core · missing_consequence]
  - expect: The glow begins to fade after the dial is turned, and not before.
  - fail: The dial is turned and the coil stays at full glow to the end of the clip; or the coil begins to fade before the dial is touched; or the coil brightens after the dial is turned; or the glow goes out instantly like a lamp at the turn.
- P2 [core · process_direction]
  - expect: The fade runs one way, from bright through dull red toward dark, and never brightens again; it is gradual, not a switch-off.
  - fail: The glow brightens again after dimming; or goes dark and returns; or pulses; or the coil turns from red to a brighter colour.
- P3 [major · process_direction]
  - expect: The fade starts at the coil's outer parts or evenly and does not skip about; the whole coil follows the same one-way change.
  - fail: One part of the coil goes dark while another brightens; or the glow jumps between segments; or the glow moves along the coil like a travelling light.
- P4 [major · causeless_motion]
  - expect: The stove and anything on it stay still as the dial is turned; the coil does not move.
  - fail: The coil lifts or shifts at the turn; or a pan on the stove slides; or the dial turns back by itself.
- P5 [fatal · permanence_count]
  - expect: One coil on one stove; the coil keeps its spiral shape; the hand passes through nothing.
  - fail: The coil vanishes rather than going dark; or a second coil appears glowing; or the coil changes shape or melts; or the hand passes through the dial or stove.
- P6 [minor · attribute_drift]
  - expect: The stove top's colour, the other burners and the surroundings stay the same apart from the glow.
  - fail: The stove changes colour; or another burner lights or goes out; or items on the counter rearrange.

**Note.** How fast the glow fades and how far it has faded by the end are not judged, only that it fades one way after the turn.

## ELEC-0034 · switch_light · train

**Caption.** The power button on a handheld game console is pressed, and the screen lights up with the start logo.

**Expectation (hidden).** The screen lights only after the press and stays on; it does not display anything before.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A handheld game console with its screen dark.
- S2 [core] The power button is pressed.
- S3 [core] The screen lights up.
- S4 [core] A start logo appears on the screen.
- S5 [minor] The screen shows nothing before the press.
- S6 [minor] The order is dark, press, lit with logo.

**PC**
- P1 [core · missing_consequence]
  - expect: The screen lights after the press, and only then.
  - fail: The button is pressed and the screen stays dark to the end of the clip; or the screen is lit before the press; or the screen comes on with nothing touching the console; or the buttons light while the screen stays dark to the end.
- P2 [core · process_direction]
  - expect: Once on, the screen stays lit for the rest of the clip; the logo appears and may give way to a menu but the screen does not return to dark.
  - fail: The screen goes dark again by itself; or flickers on and off; or the logo appears and the screen shrinks back to black; or the logo fades in and out repeatedly.
- P3 [major · missing_consequence]
  - expect: The screen's glow reaches the console's face and the fingers near it.
  - fail: The screen is lit while the console's bezel and the fingers beside it stay as dark as before; or the surroundings brighten while the screen stays dark.
- P4 [major · causeless_motion]
  - expect: The console moves only with the hands; nothing else nearby moves at the press.
  - fail: The console jumps or twists with no hand moving it; or objects nearby shift at the press; or the console's buttons press themselves.
- P5 [fatal · permanence_count]
  - expect: One console with one screen; it keeps its shape; the finger passes through nothing.
  - fail: A second screen appears; or the console changes shape; or the finger passes into the console; or the buttons rearrange.
- P6 [minor · attribute_drift]
  - expect: The console's colour and button layout stay the same apart from the screen.
  - fail: The console changes colour; or the buttons change layout; or the logo changes into a different logo and back.

**Note.** What the logo looks like is not judged; any picture appearing at start-up counts.

## ELEC-0035 · switch_light · train

**Caption.** The switch on a wall-mounted heater is flipped, and its indicator light comes on and its fan starts.

**Expectation (hidden).** The light and fan start together with the switch; both stop when it is switched off.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A heater mounted on a wall, with a switch.
- S2 [core] The switch is flipped.
- S3 [core] Its indicator light comes on.
- S4 [core] Its fan starts.
- S5 [minor] The light is off and the fan still before the flip.
- S6 [minor] The order is flip, then light and fan together.

**PC**
- P1 [core · missing_consequence]
  - expect: The light comes on and the fan starts together at the moment the switch is flipped, and only then.
  - fail: The switch is flipped and neither light nor fan responds to the end of the clip; or the light comes on while the fan stays still to the end; or the fan runs while the light stays dark; or the fan starts before the switch moves.
- P2 [core · causeless_motion]
  - expect: Before the flip the fan is still; afterwards it runs steadily and does not stop, start or reverse on its own.
  - fail: The fan stops and restarts with the switch untouched; or turns slowly by itself before the flip; or reverses direction; or the heater rocks on the wall.
- P3 [major · missing_consequence] (if: Light items such as curtains, paper or tassels are in front of the heater's outlet.)
  - expect: Light items in the heater's airflow flutter once the fan runs and are still before.
  - fail: Curtains or paper near the outlet flutter before the fan starts; or nothing in the airflow moves while the fan runs; or the flutter blows toward the heater.
- P4 [major · process_direction]
  - expect: Once on, the light stays lit and the fan keeps running while the switch stays on.
  - fail: The light goes out again with the switch on; or flickers; or the switch flips back by itself; or the fan slows to a stop with the switch on.
- P5 [fatal · permanence_count]
  - expect: One heater fixed to the wall; it keeps its shape and place; the hand passes through nothing.
  - fail: The heater drops off the wall or moves along it; or a second heater appears; or the hand passes into the heater; or the grille changes shape.
- P6 [minor · attribute_drift]
  - expect: The heater's colour, its grille and the wall stay the same apart from the light.
  - fail: The heater changes colour; or the grille pattern changes; or the wall changes colour.

**Note.** The fan may be hidden behind the grille; it is judged from visible blade motion or the movement of items in its airflow.

## ELEC-0036 · switch_light · train

**Caption.** A pair of hands claps twice in a room with a clap-activated lamp, and the lamp comes on.

**Expectation (hidden).** The lamp lights right after the second clap and not before; it stays on until the next double clap.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A room with a lamp that is dark.
- S2 [core] A pair of hands claps twice.
- S3 [core] The lamp comes on.
- S4 [minor] The lamp lights after the second clap, not the first.
- S5 [minor] The order is dark, two claps, lit.

**PC**
- P1 [core · missing_consequence]
  - expect: The lamp lights right after the second clap, and only then.
  - fail: The lamp stays dark after the two claps to the end of the clip; or the lamp lights before the hands have met; or the lamp lights after the first clap; or the lamp lights with the hands still.
- P2 [core · process_direction]
  - expect: Once lit, the lamp stays on steadily until another double clap.
  - fail: The lamp goes dark again with the hands still; or flickers on and off; or dims and brightens repeatedly; or lights and goes out at once.
- P3 [major · missing_consequence]
  - expect: The lamp's light reaches its surroundings: the shade glows and nearby surfaces brighten with shadows pointing away from the lamp.
  - fail: The bulb glows while the shade and surroundings stay as dark as before; or the room brightens while the lamp stays dark; or the light comes from a place other than the lamp.
- P4 [major · trajectory_momentum]
  - expect: The hands come together and part twice, meeting palm to palm.
  - fail: The hands pass through each other; or one hand claps alone; or the hands meet once and the second clap is a wave; or the hands merge.
- P5 [fatal · permanence_count]
  - expect: One lamp and one pair of hands; the lamp keeps its shape; the hands keep their fingers.
  - fail: A second lamp appears; or the lamp vanishes; or a hand gains or loses fingers; or a third hand appears.
- P6 [minor · attribute_drift]
  - expect: The shade's colour, the room's colours and its contents stay the same apart from the light.
  - fail: The shade changes colour rather than brightness; or the room's contents rearrange; or the walls change colour.

**Note.** The hands are kept because the clap is the caption's cause; the person is otherwise not judged. The sound is not judged; the clap is read from the hands meeting.

## ELEC-0037 · switch_light · train

**Caption.** A fluorescent tube in a garage is switched on, and it blinks a few times before staying lit.

**Expectation (hidden).** The blinking begins only after the switch and ends in a steady light; the tube does not light before the switch.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A fluorescent tube in a garage, dark.
- S2 [core] The tube is switched on.
- S3 [core] The tube blinks a few times.
- S4 [core] The tube then stays lit.
- S5 [minor] The garage is dark before the switch.
- S6 [minor] The order is dark, switch, blinking, steady.

**PC**
- P1 [core · missing_consequence]
  - expect: The tube begins to blink at the switch, and only then.
  - fail: The switch is thrown and the tube stays dark to the end of the clip; or the tube blinks or glows before the switch is touched; or the tube lights with the switch untouched; or a different lamp lights instead.
- P2 [core · process_direction]
  - expect: The blinking comes first and ends in a steady light that lasts for the rest of the clip; the tube does not go back to blinking or dark.
  - fail: The tube glows steadily and then starts blinking; or goes dark again after settling; or blinks to the end of the clip without settling; or the steady glow fades out.
- P3 [major · missing_consequence]
  - expect: The garage lights with the tube: the floor and walls under it brighten with each blink and stay bright once the tube is steady.
  - fail: The tube glows while the garage stays as dark as before; or the garage brightens while the tube stays dark; or the garage stays lit during a blink's dark phase.
- P4 [major · causeless_motion]
  - expect: The fixture hangs still through the blinking; nothing in the garage moves at the switch.
  - fail: The fixture swings at the switch; or tools or objects shift with the blinks; or the door moves by itself.
- P5 [fatal · permanence_count]
  - expect: One tube in one fixture; the fixture stays on the ceiling; the garage's contents are the same before and after.
  - fail: A second tube appears; or the fixture vanishes or moves; or tools or vehicles appear or vanish between dark and lit frames; or the tube changes length.
- P6 [minor · attribute_drift]
  - expect: The garage's wall colours and contents stay the same apart from brightness.
  - fail: The walls change colour rather than brightness; or the tools rearrange; or the tube changes colour once steady.

## ELEC-0038 · switch_light · train

**Caption.** A key on a toy piano is pressed, and the key lights up while it is held down and goes dark when it is released.

**Expectation (hidden).** The key lights while pressed and goes dark when released; nothing lights before the press.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A toy piano with keys.
- S2 [core] A key is pressed and held down.
- S3 [core] The key lights up while it is held.
- S4 [core] The key goes dark when it is released.
- S5 [minor] The key is dark before the press.
- S6 [minor] The order is dark, press and lit, release and dark.

**PC**
- P1 [core · missing_consequence]
  - expect: The key lights when it is pressed down and goes dark when it is released; it glows only while held.
  - fail: The key is pressed and stays dark; or lights before the finger reaches it; or stays lit after the finger lifts; or goes dark while the finger still holds it down.
- P2 [core · causeless_motion]
  - expect: Only the pressed key moves and lights; the other keys stay still and dark; the piano stays put.
  - fail: Other keys light or move while only one is pressed; or a key sinks by itself; or the piano slides or rocks at the press; or the pressed key stays down after release.
- P3 [major · process_direction]
  - expect: While held the glow is steady; after release the key stays dark for the rest of the clip.
  - fail: The glow flickers while the key is held steady; or comes back on after release; or the key lights and goes dark repeatedly during one press.
- P4 [major · material_response]
  - expect: The key is a rigid lever that dips at the press and springs back up on release.
  - fail: The key bends or squashes under the finger; or sinks into the body and stays sunk; or the whole keyboard dips as one piece.
- P5 [fatal · permanence_count]
  - expect: One piano with a fixed row of keys; the finger passes through nothing.
  - fail: Keys appear or vanish; or the finger passes into the key or body; or a second piano appears; or the piano changes shape.
- P6 [minor · attribute_drift]
  - expect: The piano's colours and the key layout stay the same apart from the glow.
  - fail: The piano changes colour; or the keys change order or colour; or the glow changes colour during the press.

**Note.** The hand is kept because the press is the caption's cause; the person is otherwise not judged. Sound is not judged.

## ELEC-0039 · switch_light · train

**Caption.** The wall button for an outdoor floodlight is pressed, and the yard lights up.

**Expectation (hidden).** The floodlight comes on at the press and lights the yard; pressing again turns it off and the yard goes dark.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] An outdoor yard at night with a floodlight, and a wall button.
- S2 [core] The button is pressed.
- S3 [core] The yard lights up.
- S4 [minor] The yard is dark before the press.
- S5 [minor] The order is dark, press, lit.

**PC**
- P1 [core · missing_consequence]
  - expect: The floodlight comes on at the press, and only then, and the yard brightens with it.
  - fail: The button is pressed and the yard stays dark; or the yard is lit before the press; or the floodlight comes on with nothing touching the button; or the floodlight glows while the yard stays as dark as before.
- P2 [core · process_direction]
  - expect: Once on, the floodlight stays lit and the yard stays lit for the rest of the clip.
  - fail: The floodlight goes out again by itself; or flickers; or dims back to dark; or the button presses itself again.
- P3 [major · missing_consequence]
  - expect: The light comes from the floodlight: the ground and objects nearest it are brightest and shadows point away from it.
  - fail: The yard is lit evenly with no brighter side; or shadows point toward the floodlight; or the light comes from a place other than the fixture.
- P4 [major · causeless_motion]
  - expect: Nothing in the yard moves at the press; the fixture stays fixed to its mount.
  - fail: Garden furniture or plants jump at the press; or the fixture swings; or a gate opens by itself.
- P5 [fatal · permanence_count]
  - expect: One floodlight and one button; the yard's contents are the same before and after; the hand passes through nothing.
  - fail: Objects appear or vanish between dark and lit frames; or a second floodlight appears; or the hand passes into the wall; or the fixture vanishes.
- P6 [minor · attribute_drift]
  - expect: The wall's colour, the fixture and the yard's contents stay the same apart from brightness.
  - fail: The wall changes colour rather than brightness; or the fixture changes shape; or the plants change colour.

## ELEC-0040 · switch_light · train

**Caption.** A shop escalator is started with its key switch, and the steps begin to move upward.

**Expectation (hidden).** The steps start moving only after the key is turned and run steadily; they stop when the key is turned back.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A shop escalator, still, with a key switch.
- S2 [core] The key switch is turned.
- S3 [core] The steps begin to move upward.
- S4 [minor] The steps are still before the key is turned.
- S5 [minor] The order is still, key, moving.

**PC**
- P1 [core · missing_consequence]
  - expect: The steps start moving at the moment the key is turned, and only then.
  - fail: The key is turned and the steps stay still to the end of the clip; or the steps move before the key is turned; or the steps move with the key untouched; or the steps move downward.
- P2 [core · causeless_motion]
  - expect: Before the turn nothing on the escalator moves; afterwards the steps run steadily upward and do not stop, start or reverse on their own.
  - fail: The steps stop and restart with the key untouched; or reverse direction; or jerk in place; or the handrail runs while the steps stay still.
- P3 [major · trajectory_momentum]
  - expect: The steps move together as a continuous chain up the slope, each step keeping its place relative to the next; the handrails move with them.
  - fail: Steps move at different speeds and open gaps; or a step slides sideways; or the handrail runs against the steps; or the steps move up while the treads stay flat at the landing forever.
- P4 [major · material_response]
  - expect: The steps are rigid metal treads that keep their shape; the handrail is a continuous band.
  - fail: A step bends or sags; or the treads ripple like fabric; or the handrail stretches or snaps; or the steps flow like liquid.
- P5 [fatal · permanence_count]
  - expect: One escalator with its steps and rails; steps emerge from and vanish into the landings only at the ends; the hand passes through nothing.
  - fail: A step vanishes in the middle of the run; or steps appear from nowhere mid-slope; or the escalator duplicates; or the hand passes through the switch panel.
- P6 [minor · attribute_drift]
  - expect: The escalator's finish, the handrail colour and the shop around stay the same.
  - fail: The treads change colour; or the handrail changes colour; or the shop's displays rearrange.

## ELEC-0041 · switch_light · train

**Caption.** The button on a coffee machine is pressed, and a light comes on and coffee begins to drip into the cup.

**Expectation (hidden).** The indicator lights with the press and the dripping begins shortly after; nothing happens before the button.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A coffee machine with a cup beneath its spout.
- S2 [core] The button is pressed.
- S3 [core] A light on the machine comes on.
- S4 [core] Coffee begins to drip into the cup.
- S5 [minor] The light is dark and the spout dry before the press.
- S6 [minor] The order is press, light, then dripping.

**PC**
- P1 [core · missing_consequence]
  - expect: The light comes on at the press and the coffee begins to flow shortly after; neither happens before the press.
  - fail: The button is pressed and the light stays dark; or coffee drips before the button is touched; or the light comes on and no coffee appears to the end of the clip; or the coffee flows with the light dark to the end.
- P2 [core · process_direction]
  - expect: Once started, the light stays on and the coffee keeps flowing while the machine runs; the cup fills and does not empty.
  - fail: The light goes out with coffee still flowing; or the flow stops and restarts with the button untouched; or the cup's level falls while coffee still drips in; or coffee flows back up into the spout.
- P3 [major · gravity_direction]
  - expect: The coffee falls straight down from the spout into the cup and pools at the bottom.
  - fail: The coffee arcs sideways past the cup with nothing deflecting it; or rises from the spout; or hangs in the air; or the cup's surface tilts with the cup level.
- P4 [major · causeless_motion]
  - expect: The cup and the machine stay where they are as the coffee flows.
  - fail: The cup slides or spins under the spout by itself; or the machine shifts at the press; or the cup lifts to the spout.
- P5 [fatal · permanence_count]
  - expect: One machine, one spout, one cup; the coffee enters the cup through its open top; the finger passes through nothing.
  - fail: Coffee passes through the cup's side; or a second cup appears; or the cup vanishes or changes shape; or the finger passes into the machine.
- P6 [minor · attribute_drift]
  - expect: The machine's colour, the cup's colour and the counter stay the same apart from the light.
  - fail: The machine changes colour; or the cup changes colour or size; or the counter's contents rearrange.

## ELEC-0042 · switch_light · train

**Caption.** The bedside lamp is switched off, and only the glow of the alarm clock's display remains in the dark room.

**Expectation (hidden).** The lamp goes out at the switch and the clock's display stays lit because it is on a different supply; nothing else in the room turns off.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A bedroom with a lit bedside lamp and an alarm clock with a glowing display.
- S2 [core] The lamp is switched off.
- S3 [core] The room goes dark apart from the clock's display.
- S4 [minor] The clock's display stays lit after the lamp is off.
- S5 [minor] The order is lit, switch, dark with the clock glowing.

**PC**
- P1 [core · missing_consequence]
  - expect: The lamp goes out at the moment its switch is moved, and only then; the clock's display stays lit through the change.
  - fail: The switch is moved and the lamp stays lit; or the lamp goes out before the switch is touched; or the clock's display goes dark with the lamp; or the lamp goes out with the switch untouched.
- P2 [core · permanence_count]
  - expect: The room's contents are the same before and after: the same clock, lamp and furniture in the same places, seen lit and then dim; the clock keeps its one display.
  - fail: Furniture or objects appear or vanish between lit and dark frames; or a second glowing display appears; or the clock changes place; or the lamp vanishes rather than going dark.
- P3 [major · process_direction]
  - expect: Once off, the lamp stays dark and the clock's display stays lit for the rest of the clip.
  - fail: The lamp comes back on by itself; or flickers; or the clock's display goes out later with nothing touched; or the display brightens to light the whole room.
- P4 [major · missing_consequence]
  - expect: The light the lamp cast disappears with it: the walls and bedding go dim, and the only glow left is around the clock's display.
  - fail: The lamp is dark while its light on the wall stays; or the room stays as bright with the lamp dark; or the clock's small display lights the whole room like a lamp.
- P5 [fatal · shape_identity]
  - expect: The lamp, clock and furniture keep their shapes; nothing passes through anything.
  - fail: The lamp changes shape; or the clock morphs into another object; or the hand passes through the lamp or the nightstand; or the bed changes shape.
- P6 [minor · attribute_drift]
  - expect: The lampshade's colour, the clock's digits and the bedding stay the same apart from brightness.
  - fail: The shade changes colour rather than brightness; or the digits change colour or font; or the bedding changes pattern.

**Note.** The clock's display is on a different supply and staying lit is the caption's point; the digits changing as time passes is not a violation.

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

## ELEC-0045 · plug_power · train

**Caption.** The plug of a television is pulled while a programme is playing, and the screen goes black.

**Expectation (hidden).** The picture and sound stop at once when the plug comes out and the screen stays dark; the standby light goes off too.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A television showing a programme.
- S2 [core] Its plug is pulled from the socket.
- S3 [core] The screen goes black.
- S4 [minor] The picture is moving before the pull.
- S5 [minor] The order is playing, pull, black.

**PC**
- P1 [core · missing_consequence]
  - expect: The screen goes black at the moment the plug leaves the socket, and only then; any standby light goes off with it.
  - fail: The plug is out and the picture still plays; or the screen goes black before the plug moves; or the screen goes black with the plug still seated and untouched; or the standby light stays lit with the plug out.
- P2 [core · process_direction]
  - expect: Once unplugged the screen stays black for the rest of the clip while the plug is out.
  - fail: The picture comes back while the plug is out; or the screen flickers between picture and black; or a logo or menu appears on the unplugged screen; or the screen dims slowly rather than going black.
- P3 [major · missing_consequence]
  - expect: The screen's glow on the wall and shelf disappears with the picture.
  - fail: The screen is black while its glow still lies on the wall; or the room brightens as the screen goes black; or the glow remains around the screen's edges.
- P4 [major · material_response]
  - expect: The cord follows the plug: it slackens and drops once the plug is free and stays attached at both ends.
  - fail: The cord stretches like elastic; or stands rigid in the air after the plug is out; or the cord floats.
- P5 [fatal · permanence_count]
  - expect: One television, one cord, one plug, one socket; the plug leaves the socket whole; nothing passes through the wall.
  - fail: The plug vanishes or a second plug appears; or the plug passes through the wall; or the cord splits or detaches; or the television changes shape.
- P6 [minor · attribute_drift]
  - expect: The television's frame, the stand and the room stay the same apart from the screen.
  - fail: The frame changes colour; or the stand changes; or the room's contents rearrange.

**Note.** The sound stopping is not judged.

## ELEC-0046 · plug_power · train

**Caption.** The batteries are pulled out of a walking toy robot, and the robot stops mid-step.

**Expectation (hidden).** The robot's motion and lights stop the moment the batteries come out; it does not finish the step or move again until batteries are replaced.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A toy robot walks.
- S2 [core] Its batteries are pulled out.
- S3 [core] The robot stops mid-step.
- S4 [minor] The robot's lights, if any, go off with the batteries.
- S5 [minor] The order is walking, batteries out, stopped.

**PC**
- P1 [core · missing_consequence]
  - expect: The robot's movement and any lights stop at the moment the batteries come out, and only then.
  - fail: The batteries are out and the robot walks on; or the robot stops before the batteries move; or the robot's lights stay lit with the batteries out; or the robot finishes its step and takes another with the batteries out.
- P2 [core · causeless_motion]
  - expect: Once stopped the robot stays frozen in its pose and does not move again while the batteries are out.
  - fail: The robot moves again with the batteries out; or twitches or rocks by itself; or its arms or head move after the stop; or the robot walks before the batteries were in.
- P3 [major · gravity_direction]
  - expect: The stopped robot stands on the surface or falls over if off balance; the removed batteries are held or fall to the surface.
  - fail: The robot hangs in mid-step with a foot in the air and does not settle; or the robot floats; or a dropped battery rises or hangs in the air.
- P4 [major · trajectory_momentum]
  - expect: While walking the robot moves forward in the direction it faces, its feet lifting and landing in turn.
  - fail: The robot slides without moving its legs; or moves sideways to its facing; or its feet pass through the floor; or it lifts off the floor as it walks.
- P5 [fatal · permanence_count]
  - expect: One robot with its limbs attached; the batteries come out of an opening; nothing vanishes or passes through the robot's body.
  - fail: The batteries pass through the robot's shell; or a limb detaches; or a second robot appears; or the batteries vanish in the hand.
- P6 [minor · attribute_drift]
  - expect: The robot's colours and markings and the surface stay the same apart from the lights.
  - fail: The robot changes colour; or its markings change; or the surface changes.

**Note.** The robot is a powered toy; its walking before the batteries come out is the caption's setup and is not judged for gait.

## ELEC-0047 · plug_power · train

**Caption.** A charging cable is plugged into a phone lying on a table, and a charging symbol appears on the screen.

**Expectation (hidden).** The symbol appears right after the plug clicks in and disappears when it is pulled out; it does not appear before connection.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A phone lies on a table with its screen in view.
- S2 [core] A charging cable is plugged into it.
- S3 [core] A charging symbol appears on the screen.
- S4 [minor] The screen shows no charging symbol before the cable is in.
- S5 [minor] The order is plug in, then symbol.

**PC**
- P1 [core · missing_consequence]
  - expect: The charging symbol appears right after the connector seats in the phone, and only then.
  - fail: The connector is seated and no symbol appears to the end of the clip; or the symbol is on the screen before the connector reaches the phone; or the symbol appears while the cable lies loose; or the screen goes dark as the connector seats.
- P2 [core · process_direction]
  - expect: Once shown, the symbol stays while the cable stays in; if the cable is pulled the symbol goes.
  - fail: The symbol vanishes with the cable still seated; or flashes on and off; or the symbol stays after the cable is pulled out; or the connector backs out by itself.
- P3 [major · material_response]
  - expect: The cable is a flexible cord that lies in a curve on the table and stays attached to the connector.
  - fail: The cable stands rigid in the air; or stretches like elastic; or floats; or the connector detaches from the cable.
- P4 [major · causeless_motion]
  - expect: The phone stays where it lies as the cable goes in, apart from a small nudge; nothing else on the table moves.
  - fail: The phone slides across the table; or lifts; or flips over; or items on the table jump.
- P5 [fatal · solidity]
  - expect: One phone and one connector on one cable; the connector enters the port rather than the phone's body; fingers pass through nothing.
  - fail: The connector passes into the phone's side away from the port; or a second connector appears; or the connector vanishes; or the phone changes shape.
- P6 [minor · attribute_drift]
  - expect: The phone's case, the cable's colour and the table stay the same apart from the screen.
  - fail: The phone changes colour; or the cable changes colour; or the table's contents rearrange.

## ELEC-0048 · plug_power · train

**Caption.** An extension cord is yanked out of the wall socket, and the lamp, radio and heater plugged into it all go off together.

**Expectation (hidden).** All three devices stop at the same instant the cord comes out; none keeps running.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] An extension cord in a wall socket with a lamp, a radio and a heater plugged into it.
- S2 [core] The cord is yanked out of the socket.
- S3 [core] The lamp, the radio and the heater all go off together.
- S4 [minor] All three are running before the yank: lamp lit, radio display lit, heater glowing or fan running.
- S5 [minor] The order is running, yank, all off.

**PC**
- P1 [core · missing_consequence]
  - expect: All three devices go off at the moment the cord leaves the socket, and only then.
  - fail: The cord is out and a device keeps running to the end of the clip; or a device goes off before the cord moves; or the devices go off one after another over the clip; or a device goes off with the cord still seated.
- P2 [core · permanence_count]
  - expect: The three devices, the cord and the socket are the same before and after: the same items in the same places, dark rather than gone.
  - fail: A device vanishes rather than switching off; or a fourth device appears; or a device changes place; or the cord splits into two cords.
- P3 [major · process_direction]
  - expect: Once the cord is out the devices stay off; the heater's glow, if any, only fades and does not return.
  - fail: A device comes back on with the cord out; or the lamp flickers; or the heater's glow brightens after the yank; or the cord jumps back into the socket.
- P4 [major · material_response]
  - expect: The cord is drawn taut by the yank and goes slack once the plug is free; it stays attached at both ends.
  - fail: The cord stretches like elastic; or stands rigid in the air after the plug is out; or the cord floats; or the devices are dragged across the floor by the yank.
- P5 [fatal · solidity]
  - expect: The plug leaves the socket whole; nothing passes through the wall; the devices keep their shape.
  - fail: The plug passes through the wall beside the socket; or the cord passes through a device; or a device changes shape; or the socket comes off the wall.
- P6 [minor · attribute_drift]
  - expect: The devices' colours, the cord's colour and the room stay the same apart from the lights.
  - fail: A device changes colour; or the cord changes colour; or the room's contents rearrange.

**Note.** The radio falling silent is sound and is not judged; the radio counts through its display or dial light.

## ELEC-0049 · plug_power · train

**Caption.** Two batteries are slid into a flashlight whose switch is already on, and the light comes on as the cap is screwed down.

**Expectation (hidden).** The flashlight is dark until the cap closes the circuit and lights at that moment, staying on; it does not light with the batteries out or the cap off.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A flashlight with its cap off and its switch on.
- S2 [core] Two batteries are slid into the flashlight.
- S3 [core] The cap is screwed down.
- S4 [core] The light comes on as the cap closes.
- S5 [minor] The flashlight is dark before the cap is screwed down.
- S6 [minor] The order is batteries in, cap on, light.

**PC**
- P1 [core · missing_consequence]
  - expect: The light comes on as the cap closes on the barrel, and only then; it stays dark with the batteries in but the cap off.
  - fail: The light comes on as the batteries slide in with the cap still off; or the cap is screwed down and the light stays dark to the end of the clip; or the light is on before the batteries go in; or the light comes on with the cap lying loose.
- P2 [core · process_direction]
  - expect: Once on, the light stays on steadily while the cap stays screwed down.
  - fail: The light goes out again with the cap on; or flickers; or the cap unscrews itself; or the beam fades to dark.
- P3 [major · missing_consequence]
  - expect: The lit lens throws a beam: the surface it points at brightens.
  - fail: The lens glows while the surface it points at stays as dark as before; or the surface brightens while the lens stays dark; or the lit patch is behind the flashlight.
- P4 [major · trajectory_momentum]
  - expect: The batteries slide into the barrel along its axis; the cap turns on the barrel's thread and tightens.
  - fail: A battery enters sideways through the barrel's wall; or the cap goes on without turning and then is shown screwed; or the barrel turns instead of the cap while the hand holds the barrel; or the cap turns and does not advance.
- P5 [fatal · solidity]
  - expect: Two batteries inside one barrel; the batteries enter the open end and are hidden once in; the cap closes on the barrel; fingers pass through nothing.
  - fail: A battery passes through the barrel's wall; or a third battery appears; or a battery vanishes in mid-air; or the cap merges with the barrel.
- P6 [minor · attribute_drift]
  - expect: The flashlight's colour, the batteries' labels and the surface stay the same apart from the light.
  - fail: The flashlight changes colour; or the batteries change size or label; or the surface changes.

## ELEC-0050 · plug_power · train

**Caption.** A charging cable is plugged into an electric car, and a light on the charging port comes on.

**Expectation (hidden).** The port light comes on after the cable clicks in and goes off when it is removed; it does not light before connection.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] An electric car with its charging port open.
- S2 [core] A charging cable is plugged into the port.
- S3 [core] A light on the port comes on.
- S4 [minor] The port light is off before the cable is in.
- S5 [minor] The order is plug in, then light.

**PC**
- P1 [core · missing_consequence]
  - expect: The port light comes on after the connector seats in the port, and only then.
  - fail: The connector is seated and the light stays dark to the end of the clip; or the light is on before the connector reaches the port; or the light comes on with the cable hanging loose; or a light elsewhere on the car comes on while the port light stays dark.
- P2 [core · process_direction]
  - expect: Once on, the light stays on or settles to a steady pattern while the cable stays in; it goes off only if the cable is removed.
  - fail: The light goes out again with the cable seated; or switches off and on at random; or the light stays on after the cable is pulled; or the connector backs out by itself.
- P3 [major · material_response]
  - expect: The cable is a thick flexible lead that hangs in a curve from the connector to the charger and stays attached.
  - fail: The cable stands rigid in the air; or stretches like elastic; or floats; or the connector detaches from the cable.
- P4 [major · causeless_motion]
  - expect: The car stays still as the cable goes in; the port flap does not move by itself.
  - fail: The car rolls or rocks; or the flap closes on the cable by itself; or the charger post shifts.
- P5 [fatal · solidity]
  - expect: One connector in one port; the connector enters the port rather than the body panel; the hand passes through nothing.
  - fail: The connector passes into the panel beside the port; or a second connector appears; or the connector vanishes; or the car's panel changes shape.
- P6 [minor · attribute_drift]
  - expect: The car's paint, the cable's colour and the surroundings stay the same apart from the light.
  - fail: The car changes colour; or the cable changes colour; or the charger post changes shape.

## ELEC-0051 · plug_power · train

**Caption.** The cord of a running hairdryer is pulled out of the socket, and the dryer falls silent and stops blowing.

**Expectation (hidden).** The airflow and noise stop within a second of the plug coming out even though the switch is still on.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A hairdryer runs: its blower is on.
- S2 [core] Its cord is pulled out of the socket.
- S3 [core] The dryer stops blowing.
- S4 [minor] The dryer's switch stays on.
- S5 [minor] The order is running, pull, stopped.

**PC**
- P1 [core · missing_consequence]
  - expect: The blowing stops at the moment the plug leaves the socket, and only then, even though the switch is still on.
  - fail: The plug is out and the dryer blows on to the end of the clip; or the dryer stops before the plug moves; or the dryer stops with the plug still seated; or the airflow stops but the heating element glows on.
- P2 [core · process_direction]
  - expect: Once unplugged the dryer stays stopped; it does not start again while the plug is out.
  - fail: The dryer starts blowing again with the plug out; or blows in bursts after the pull; or the plug jumps back into the socket; or the switch moves by itself.
- P3 [major · missing_consequence] (if: Hair, ribbons or other light items are in the airflow.)
  - expect: Anything in the airflow flutters while the dryer runs and settles once it stops.
  - fail: Hair or ribbons stream after the plug is out; or nothing in front of the nozzle moves while the dryer runs; or the flutter blows toward the nozzle.
- P4 [major · material_response]
  - expect: The cord follows the plug: it slackens and drops once the plug is free and stays attached at both ends.
  - fail: The cord stretches like elastic; or stands rigid in the air after the plug is out; or floats.
- P5 [fatal · permanence_count]
  - expect: One dryer, one cord, one plug, one socket; the plug leaves the socket whole; nothing passes through the wall.
  - fail: The plug vanishes or a second plug appears; or the plug passes through the wall; or the cord splits or detaches; or the dryer changes shape.
- P6 [minor · attribute_drift]
  - expect: The dryer's colour, the cord and the room stay the same.
  - fail: The dryer changes colour; or the cord changes colour; or the room's contents rearrange.

**Note.** The dryer falling silent is sound and is not judged; stopping is read from the airflow's effect or the fan blur ending.

## ELEC-0052 · plug_power · train

**Caption.** A blender with its button held down is plugged into a wall socket, and the blades start spinning.

**Expectation (hidden).** Nothing moves until the plug goes in; the blades start the instant it does and run steadily; the held button alone does nothing while unplugged.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A blender with its button held down.
- S2 [core] The blender is plugged into a wall socket.
- S3 [core] The blades start spinning.
- S4 [minor] The blades are still before the plug goes in, though the button is held.
- S5 [minor] The order is button held, plug in, blades spin.

**PC**
- P1 [core · missing_consequence]
  - expect: The blades start at the moment the plug seats in the socket, and only then; holding the button alone does nothing while unplugged.
  - fail: The blades spin before the plug reaches the socket; or the plug is in and the blades stay still to the end of the clip; or the blades start with the plug lying loose; or the blades spin only when the button is released.
- P2 [core · causeless_motion]
  - expect: Before the plug is in nothing in the jug moves; afterwards the blades run steadily while the button is held and do not stop, start or reverse on their own.
  - fail: The blades stop and restart with the plug in and the button held; or the contents swirl before the plug is in; or the blades reverse; or the jug spins with the blades.
- P3 [major · trajectory_momentum] (if: The jug has contents.)
  - expect: Any contents swirl round the jug in the blades' direction, climbing the walls and dipping at the centre.
  - fail: The contents rise as a column; or swirl against the blades; or stay flat and still while the blades spin; or leap out of a closed jug.
- P4 [major · material_response]
  - expect: The cord hangs slack from the plug to the blender and stays attached; the jug and blades stay rigid.
  - fail: The cord stands rigid in the air or stretches like elastic; or the jug wobbles or bulges; or the blades flop like rubber.
- P5 [fatal · solidity]
  - expect: One blender, one plug, one socket; the plug enters the socket rather than the wall; the hand passes through nothing.
  - fail: The plug passes into the wall beside the socket; or a second plug or jug appears; or the hand passes through the blender; or the contents pass through the jug's walls.
- P6 [minor · attribute_drift]
  - expect: The blender's colour, the jug and the counter stay the same.
  - fail: The blender changes colour; or the jug changes shape; or the counter's contents rearrange.

## ELEC-0053 · plug_power · train

**Caption.** The cord of a running vacuum cleaner snags on a doorframe and jerks out of the socket, and the vacuum stops.

**Expectation (hidden).** The motor winds down within a second or two of the plug coming out and the machine is silent; it does not restart until plugged in.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A vacuum cleaner runs, its cord running to a socket.
- S2 [core] The cord snags on a doorframe.
- S3 [core] The plug jerks out of the socket.
- S4 [core] The vacuum stops.
- S5 [minor] The cord is drawn taut against the doorframe before the plug comes out.
- S6 [minor] The order is running, snag, plug out, stopped.

**PC**
- P1 [core · missing_consequence]
  - expect: The vacuum stops at the moment the plug leaves the socket, and only then: its brush roll or the fluff at its head stops moving and any light on it goes out.
  - fail: The plug is out and the vacuum runs on to the end of the clip; or the vacuum stops before the cord has gone taut; or the vacuum stops with the plug still seated; or the vacuum's light stays lit with the plug out.
- P2 [core · process_direction]
  - expect: Once unplugged the vacuum stays stopped; it does not start again while the plug is out.
  - fail: The vacuum starts again with the plug out; or runs in bursts; or the plug jumps back into the socket by itself; or the cord re-threads itself round the frame.
- P3 [major · material_response]
  - expect: The cord is drawn taut against the frame before the plug comes out; once free it goes slack and drops.
  - fail: The plug comes out while the cord hangs slack; or the cord stays stretched straight in the air after the plug is free; or the cord stretches like elastic; or the plug flies up and stays aloft.
- P4 [major · trajectory_momentum]
  - expect: The vacuum keeps moving only as far as it was being pushed; the cord's snag does not throw it about.
  - fail: The vacuum is flung backward by the snag; or lifts off the floor; or reverses on its own; or spins round.
- P5 [fatal · permanence_count]
  - expect: One vacuum, one cord, one plug, one socket; the cord stays continuous and passes through neither the frame nor the wall.
  - fail: The cord passes through the doorframe; or splits or detaches; or the plug vanishes; or a second vacuum appears.
- P6 [minor · attribute_drift]
  - expect: The vacuum's colour, the cord and the doorframe stay the same.
  - fail: The vacuum changes colour; or the cord changes colour; or the doorframe changes.

**Note.** The motor's sound is not judged; stopping is read from visible motion at the head, any indicator light and the dust or fluff settling. Who pushes the vacuum is not judged.

## ELEC-0054 · plug_power · train

**Caption.** A battery pack is clipped into a remote-control car, and the car's lights come on.

**Expectation (hidden).** The lights are off and the car is still before the pack goes in; the lights come on the instant the pack clicks into place and stay on; the car does not drive off by itself and nothing happens before the pack is in.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A remote-control car and a battery pack.
- S2 [core] The pack is clipped into the car.
- S3 [core] The car's lights come on.
- S4 [minor] The car is dark and still before the pack goes in.
- S5 [minor] The order is pack in, then lights.

**PC**
- P1 [core · missing_consequence]
  - expect: The lights come on at the moment the pack clicks into place, and only then, and stay on.
  - fail: The pack is in and the lights stay dark; or the lights are lit before the pack reaches the car; or the lights come on with the pack lying loose; or the lights go out again with the pack seated.
- P2 [core · causeless_motion]
  - expect: The car stays still: its wheels do not turn and it does not drive off, since no controller is used.
  - fail: The wheels spin up when the pack goes in; or the car drives away by itself; or the car jerks or rocks with nothing touching it; or the steering turns.
- P3 [major · missing_consequence] (if: The surface in front of the lights is in view.)
  - expect: The lights' glow reaches the surface in front of or behind them.
  - fail: The lamps glow while the surface in front stays as dark as before; or the surface brightens while the lamps stay dark; or the lit patch is far from the lamps.
- P4 [major · material_response]
  - expect: The pack slides into its bay as a rigid block and seats with a stop; the car keeps its shape.
  - fail: The pack squashes or bends as it goes in; or the car body deforms around it; or the pack hangs half out once clipped.
- P5 [fatal · permanence_count]
  - expect: One car and one pack; the pack stays in once clipped; the pack enters the bay rather than the car's shell; fingers pass through nothing.
  - fail: The pack vanishes after clipping in or a second pack appears; or the pack passes through the shell; or a wheel or light vanishes; or fingers pass through the car.
- P6 [minor · attribute_drift]
  - expect: The car's colour and decals and the surface stay the same apart from the lights.
  - fail: The car changes colour; or its decals change; or the surface changes.

## ELEC-0055 · plug_power · train

**Caption.** A power bank is connected to a phone by a cable, and a light on the power bank comes on and the phone shows it is charging.

**Expectation (hidden).** Both indicators appear after the cable is connected and disappear when it is removed.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A power bank, a phone and a cable.
- S2 [core] The cable connects the power bank to the phone.
- S3 [core] A light on the power bank comes on.
- S4 [core] The phone shows that it is charging.
- S5 [minor] The bank's light is off and the phone shows no charging sign before the cable is in.
- S6 [minor] The order is connect, then both indicators.

**PC**
- P1 [core · missing_consequence]
  - expect: The bank's light comes on and the phone's charging sign appears once the cable is connected at both ends, and only then.
  - fail: The cable is connected and neither indicator appears to the end of the clip; or the bank's light is on with the cable loose; or the phone shows charging while the cable is not in it; or one indicator appears and the other never does with both ends seated.
- P2 [core · process_direction]
  - expect: Once shown, both indicators stay while the cable stays in; they go only if the cable is pulled.
  - fail: An indicator vanishes with the cable seated; or flashes on and off at random; or the phone's screen goes dark as the cable seats; or the connector backs out by itself.
- P3 [major · material_response]
  - expect: The cable is a flexible cord that lies in a curve between the two and stays attached at both ends.
  - fail: The cable stands rigid in the air; or stretches like elastic; or floats; or a connector detaches from the cable.
- P4 [major · causeless_motion]
  - expect: The phone and the bank stay where they lie as the cable goes in, apart from small nudges.
  - fail: The phone or bank slides across the table by itself; or lifts; or flips over; or other items on the table jump.
- P5 [fatal · solidity]
  - expect: One phone, one bank, one cable; each connector enters a port rather than a body; fingers pass through nothing.
  - fail: A connector passes into the phone's or bank's body away from the port; or a second cable appears; or the bank vanishes; or the phone changes shape.
- P6 [minor · attribute_drift]
  - expect: The bank's colour, the phone's case and the table stay the same apart from the indicators.
  - fail: The bank changes colour; or the phone changes colour; or the table's contents rearrange.

## ELEC-0056 · plug_power · train

**Caption.** In a garden at dusk, the solar lights along the path flicker on one after another.

**Expectation (hidden).** The lights come on while the sky is already dim and stay lit; they do not come on in full daylight and do not go out again.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A garden path lined with solar lights, at dusk.
- S2 [core] The lights come on.
- S3 [core] They come on one after another, not all at once.
- S4 [minor] The sky is dim: dusk, not full daylight or full night.
- S5 [minor] Each light flickers or fades in as it comes on.

**PC**
- P1 [core · missing_consequence]
  - expect: Each light, once on, lights the path and plants around it; the lights come on while the sky is already dim.
  - fail: A light glows while the ground around it stays as dark as before; or the ground brightens while the light stays dark; or the lights come on in bright daylight with the sky full sun; or a light comes on and the rest never do to the end of the clip.
- P2 [core · process_direction]
  - expect: Once on, each light stays lit for the rest of the clip; the number of lit lamps only grows.
  - fail: A light goes out again after coming on; or lights flicker on and off repeatedly; or all the lights go out at once; or the sky brightens back to daylight.
- P3 [major · causeless_motion]
  - expect: The lights stay in their places along the path; plants sway only in the breeze; nothing moves as the lights come on.
  - fail: A light moves or tips as it comes on; or plants jump at the light; or the path shifts.
- P4 [major · permanence_count]
  - expect: The lit lights are the same lamps seen dark in the same places along the path.
  - fail: Lit points appear where no lamp stood; or a lamp seen dark is gone once the others are lit; or lamps multiply; or lamps change place along the path.
- P5 [fatal · shape_identity]
  - expect: The lamps, path and plants keep their shapes; nothing passes through anything.
  - fail: A lamp changes shape or merges with a plant; or the path changes route; or a lamp sinks into the ground; or plants turn into other objects.
- P6 [minor · attribute_drift]
  - expect: The lamps' housings, the path's surface and the plants keep their colours apart from the light and the dusk.
  - fail: A housing changes colour; or the path changes surface; or the plants change colour rather than brightness.

**Note.** The lights coming on without anyone touching them is the caption's event: the trigger is the dusk, not a hand.

## ELEC-0057 · plug_power · train

**Caption.** A portable generator at a campsite is started, and the string of lights connected to it comes on.

**Expectation (hidden).** The lights come on once the generator is running and go out when it is switched off; they do not light while the generator is silent.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A portable generator at a campsite with a string of lights connected to it.
- S2 [core] The generator is started.
- S3 [core] The string of lights comes on.
- S4 [minor] The lights are dark before the generator starts.
- S5 [minor] The order is start, then lights.

**PC**
- P1 [core · missing_consequence]
  - expect: The lights come on once the generator is running, and only then: after the start action, not before.
  - fail: The lights are lit before the start action; or the generator is started and the lights stay dark to the end of the clip; or the lights come on with nothing done to the generator; or the lights come on while the generator is being switched off.
- P2 [core · process_direction]
  - expect: Once on, the lights stay lit while the generator runs; they go out only if it is switched off.
  - fail: The lights go out again with the generator running; or flicker on and off; or the string lights up one bulb at a time along its length; or the lights go out and come back with nothing touched.
- P3 [major · missing_consequence]
  - expect: The generator running shows: its pull cord returns, its housing vibrates or exhaust shimmer or smoke appears; the lights' glow reaches the tent or ground near them.
  - fail: The bulbs glow while the ground and tent near them stay as dark as before; or exhaust or vibration appear before the start action; or the generator's cord stays pulled out in the air.
- P4 [major · gravity_direction] (if: Exhaust or the pull cord is visible.)
  - expect: Any exhaust or smoke from the generator rises and drifts; the pull cord hangs or retracts.
  - fail: Exhaust sinks and pools on the ground; or hangs as a fixed shape; or the pull cord stands rigid in the air after release.
- P5 [fatal · permanence_count]
  - expect: One generator and one string; the string stays continuous and attached; nothing passes through the generator.
  - fail: The string splits or detaches; or a second generator appears; or the generator vanishes; or a hand passes through the generator.
- P6 [minor · attribute_drift]
  - expect: The generator's colour, the string's bulbs and the campsite stay the same apart from the light.
  - fail: The generator changes colour; or bulbs change colour; or the campsite rearranges.

**Note.** The generator's engine sound is not judged; the start is read from the hand's action on the starter and the lights responding.

## ELEC-0058 · plug_power · train

**Caption.** A string of fairy lights is unplugged from the wall, and the whole string goes dark.

**Expectation (hidden).** Every bulb goes out at the same instant the plug is pulled; none stays lit.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A string of fairy lights, lit, with its plug in a wall socket.
- S2 [core] The plug is pulled out.
- S3 [core] The whole string goes dark.
- S4 [minor] Every bulb goes dark, none stays lit.
- S5 [minor] The order is lit, pull, dark.

**PC**
- P1 [core · missing_consequence]
  - expect: All the bulbs go dark at the moment the plug leaves the socket, and only then, together.
  - fail: The plug is out and bulbs still glow; or the string goes dark before the plug moves; or the bulbs go out one after another along the string; or the string goes dark with the plug still seated.
- P2 [core · permanence_count]
  - expect: The dark bulbs are the same bulbs seen lit: the same number at the same spots along the wire.
  - fail: Bulbs vanish rather than going dark; or new bulbs appear along the wire; or bulbs shift along the wire; or the wire shortens or lengthens.
- P3 [major · process_direction]
  - expect: Once unplugged the string stays dark while the plug is out.
  - fail: Bulbs come back on with the plug out; or the string flickers; or the plug jumps back into the socket by itself; or the bulbs glow faintly on.
- P4 [major · material_response]
  - expect: The cord follows the plug: it slackens and drops once the plug is free; the string stays where it hangs.
  - fail: The cord stretches like elastic; or stands rigid in the air after the plug is out; or the string falls from its hooks as the plug is pulled.
- P5 [fatal · solidity]
  - expect: One string, one plug, one socket; the plug leaves the socket whole; nothing passes through the wall.
  - fail: The plug passes through the wall beside the socket; or the wire splits or detaches; or a second plug appears; or the socket comes off the wall.
- P6 [minor · attribute_drift]
  - expect: The wire's colour, the socket and the background stay the same apart from the light.
  - fail: The wire changes colour; or the socket changes design; or the background rearranges.

## ELEC-0059 · plug_power · train

**Caption.** The battery is unlatched from an e-bike, and the display on the handlebars goes dark.

**Expectation (hidden).** The display goes off when the battery is unlatched and comes back when it is clicked in again.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] An e-bike with a battery and a display on the handlebars.
- S2 [core] The battery is unlatched from the bike.
- S3 [core] The display goes dark.
- S4 [minor] The display is lit before the battery is unlatched.
- S5 [minor] The order is lit, unlatch, dark.

**PC**
- P1 [core · missing_consequence]
  - expect: The display goes dark at the moment the battery is unlatched or lifted from its contacts, and only then.
  - fail: The battery is off the bike and the display still shows; or the display goes dark before the battery is touched; or the display goes dark with the battery still latched and untouched; or the bike's lights stay on with the battery off.
- P2 [core · process_direction]
  - expect: Once dark, the display stays dark while the battery is off; it comes back only when the battery is clicked in again.
  - fail: The display comes back with the battery off; or flickers; or the battery latches itself back in; or the display lights while the battery lies on the ground.
- P3 [major · gravity_direction]
  - expect: The battery is a heavy block that stays in the hand or is set down; if dropped it falls.
  - fail: The battery floats free of the bike; or hangs in the air; or rises from the hand.
- P4 [major · causeless_motion]
  - expect: The bike stays where it stands as the battery is unlatched; the wheels do not turn.
  - fail: The bike rolls or tips as the battery comes out; or a wheel turns by itself; or the handlebars turn.
- P5 [fatal · solidity]
  - expect: One battery and one bike; the battery leaves its cradle as a whole block and passes through nothing; the hand passes through nothing.
  - fail: The battery passes through the frame; or a second battery appears; or the battery vanishes; or the frame changes shape.
- P6 [minor · attribute_drift]
  - expect: The bike's colour, the battery's casing and the background stay the same apart from the display.
  - fail: The bike changes colour; or the battery changes shape or colour; or the background rearranges.

## ELEC-0060 · plug_power · train

**Caption.** A toy train is placed on its track and the track's power pack switched on, and the train begins to run.

**Expectation (hidden).** The train moves only after the power pack is switched on and stops when it is switched off; it does not run on unpowered track.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A toy train and a track with a power pack.
- S2 [core] The train is placed on the track.
- S3 [core] The power pack is switched on.
- S4 [core] The train begins to run.
- S5 [minor] The train is still on the track before the pack is switched on.
- S6 [minor] The order is place, switch, run.

**PC**
- P1 [core · missing_consequence]
  - expect: The train starts to move when the pack is switched on, and only then.
  - fail: The pack is on and the train stays still to the end of the clip; or the train runs before the pack is touched; or the train moves while being placed; or the train runs with the pack switched off.
- P2 [core · causeless_motion]
  - expect: Before the switch the train is still; afterwards it runs steadily along the track and does not stop, start or reverse on its own.
  - fail: The train stops and restarts with the pack untouched; or reverses; or the train jerks in place without moving on; or the track moves under the train.
- P3 [major · trajectory_momentum]
  - expect: The train follows the track, its wheels on the rails, round curves and along straights.
  - fail: The train leaves the rails and runs across the floor; or floats above the track; or takes a curve by sliding sideways off the rails; or the carriages separate and run at different speeds.
- P4 [major · material_response]
  - expect: The train and track are rigid toys; the track stays where it is laid.
  - fail: The track bends or ripples as the train passes; or a carriage squashes; or the rails stretch.
- P5 [fatal · permanence_count]
  - expect: One train with its carriages on one track; nothing appears, vanishes or passes through the track.
  - fail: A carriage vanishes or appears; or a second train appears; or the train passes through the track or a tunnel wall; or carriages merge.
- P6 [minor · attribute_drift]
  - expect: The train's colours, the track's layout and the surroundings stay the same.
  - fail: The train changes colour; or the track's layout changes between frames; or the surroundings rearrange.

## ELEC-0061 · plug_power · train

**Caption.** A glowing electric heater is unplugged, and the orange glow of its elements fades to dark.

**Expectation (hidden).** The fan stops at once and the glow fades gradually over a few seconds; the elements do not glow brighter after unplugging.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] An electric heater with elements glowing orange.
- S2 [core] The heater is unplugged.
- S3 [core] The glow fades to dark.
- S4 [minor] The elements are glowing before the pull.
- S5 [minor] The order is glowing, unplug, fading.

**PC**
- P1 [core · missing_consequence]
  - expect: The glow begins to fade after the plug leaves the socket, not before; any fan stops at once.
  - fail: The plug is out and the elements stay at full glow to the end of the clip; or the glow fades before the plug moves; or the glow fades with the plug still seated; or the fan runs on with the plug out.
- P2 [core · process_direction]
  - expect: The fade runs one way, from bright orange through dull red toward dark, and never brightens again; it is gradual, not a switch-off.
  - fail: The elements brighten after unplugging; or go dark and return; or pulse; or the glow goes out instantly like a lamp and the elements show no dull red.
- P3 [major · process_direction]
  - expect: The whole element follows the same one-way fade; the glow does not skip about.
  - fail: One part of an element goes dark while another brightens; or the glow moves along the element like a travelling light; or a dark element relights.
- P4 [major · material_response]
  - expect: The cord follows the plug: it slackens and drops once the plug is free; the heater stays put.
  - fail: The cord stretches like elastic; or stands rigid in the air after the plug is out; or the heater is dragged over by the pull.
- P5 [fatal · permanence_count]
  - expect: One heater, one cord, one plug, one socket; the elements keep their shape; the plug leaves the socket whole.
  - fail: An element vanishes rather than going dark; or the plug passes through the wall; or the cord splits; or the heater changes shape.
- P6 [minor · attribute_drift]
  - expect: The heater's casing, the grille and the room stay the same apart from the glow.
  - fail: The casing changes colour; or the grille pattern changes; or the room's contents rearrange.

**Note.** How fast the glow fades and how far it has faded by the end are not judged, only that it fades one way after the pull.

## ELEC-0062 · plug_power · train

**Caption.** A toaster is unplugged while its coils are glowing, and the coils fade and the lever pops up.

**Expectation (hidden).** The glow dies down after the plug is pulled and the bread stays in until the lever releases; the coils do not keep glowing.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A toaster with its coils glowing.
- S2 [core] The toaster is unplugged.
- S3 [core] The coils fade.
- S4 [core] The lever pops up.
- S5 [minor] The coils are glowing before the pull.
- S6 [minor] The order is glowing, unplug, fading, lever up.

**PC**
- P1 [core · missing_consequence]
  - expect: The coils begin to fade after the plug leaves the socket, not before, and the lever releases.
  - fail: The plug is out and the coils stay at full glow to the end of the clip; or the coils fade before the plug moves; or the coils fade with the plug still seated; or the lever stays down and the coils stay glowing with the plug out.
- P2 [core · process_direction]
  - expect: The glow fades one way, from bright through dull red toward dark, and never returns; the lever, once up, stays up.
  - fail: The coils brighten after the pull; or go dark and relight; or the lever pops up and drops back down by itself; or the glow goes out instantly with no dull red.
- P3 [major · trajectory_momentum]
  - expect: The lever moves straight up its slot and stops at the top; any bread rises with the carriage and stops.
  - fail: The lever moves down; or shoots up and out of the toaster; or moves sideways; or the bread flies out of the slots and up into the air.
- P4 [major · material_response]
  - expect: The cord follows the plug: it slackens and drops once the plug is free; the toaster stays put.
  - fail: The cord stretches like elastic; or stands rigid in the air after the plug is out; or the toaster is dragged across the counter by the pull.
- P5 [fatal · permanence_count]
  - expect: One toaster, one cord, one plug, one socket; the coils and lever keep their shape; the plug leaves the socket whole.
  - fail: A coil vanishes rather than going dark; or the plug passes through the wall; or the cord splits; or the toaster changes shape; or bread appears from nowhere.
- P6 [minor · attribute_drift]
  - expect: The toaster's casing, the lever and the counter stay the same apart from the glow.
  - fail: The casing changes colour; or the lever changes shape or place; or the counter's contents rearrange.

**Note.** How fast the coils fade is not judged, only that they fade one way after the pull. Whether bread is in the toaster is not required.

## ELEC-0063 · plug_power · train

**Caption.** The switch on a battery pack attached to a garland of lights is slid on, and the garland lights up.

**Expectation (hidden).** All the bulbs come on together at the switch; the garland goes dark when the switch is slid back.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A garland of small lights with a battery pack attached to it.
- S2 [core] The switch on the battery pack is slid to its on position.
- S3 [core] The garland lights up.
- S4 [minor] The garland is dark before the switch is slid.
- S5 [minor] The order is dark, slide, lit.

**PC**
- P1 [core · missing_consequence]
  - expect: The bulbs come on at the moment the switch slides across, and only then.
  - fail: The switch is slid and the garland stays dark; or the bulbs are lit before the switch moves; or the garland lights up while the switch sits untouched.
- P2 [core · permanence_count]
  - expect: The lit bulbs are the same bulbs seen dark: the same number at the same spots along the wire, and the whole string comes on together.
  - fail: Lit points appear along the wire where no bulb hung before; or bulbs seen on the dark string are gone once lit; or lit bulbs multiply or shift along the wire; or the bulbs come on one after another from one end rather than together.
- P3 [major · process_direction]
  - expect: Once on, the garland stays lit while the switch stays in its on position, and the glow sits at the bulbs.
  - fail: The garland goes dark again with the switch untouched; or the switch slides back by itself; or the glow spreads onto the bare wire between the bulbs.
- P4 [major · causeless_motion]
  - expect: Sliding the switch moves only the switch: the pack, wire and garland stay where they lie apart from a small nudge.
  - fail: The garland jumps or rearranges as the switch is slid; or the pack slides away with nothing touching it; or the wire lifts off the surface by itself.
- P5 [fatal · shape_identity]
  - expect: The pack keeps its box shape, the garland stays one continuous wire and fingers stay outside the pack.
  - fail: The pack changes shape or turns into another object; or the string splits in two or fuses with itself; or fingers pass through the pack; or the pack vanishes.
- P6 [minor · attribute_drift]
  - expect: The wire's colour, the pack's markings and the background stay the same apart from the light.
  - fail: The wire changes colour; or the pack's markings change; or the background rearranges.

## ELEC-0064 · plug_power · train

**Caption.** A battery pack is clipped into a cordless drill and the trigger pulled, and the drill bit spins.

**Expectation (hidden).** The bit spins only with the battery in and the trigger pulled; with the pack removed the trigger does nothing.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A cordless drill with a bit in its chuck, and a separate battery pack.
- S2 [core] The battery pack is clipped into the drill.
- S3 [core] The trigger is pulled.
- S4 [core] The drill bit spins.
- S5 [minor] No cord runs from the drill.
- S6 [minor] The order is pack in, trigger pulled, bit spins.

**PC**
- P1 [core · missing_consequence]
  - expect: The bit starts turning when the trigger is pulled with the pack seated, and only then.
  - fail: The trigger is pulled with the pack in and the bit stays still; or the bit spins before the trigger is pulled; or the bit spins with the pack lying loose beside the drill.
- P2 [core · causeless_motion]
  - expect: The bit turns only while the trigger is held: it stops when the trigger is released and does not start, stop or reverse on its own.
  - fail: The bit stops dead and restarts while the trigger is held steady; or reverses direction on its own; or keeps spinning to the end of the clip after the finger has lifted off the trigger.
- P3 [major · trajectory_momentum]
  - expect: The bit spins about its own axis, held in the chuck; chuck and bit turn together.
  - fail: The bit wobbles off its axis or bends while turning; or the chuck turns while the bit stays still; or the bit turns while the chuck is still; or the whole drill body spins with the bit.
- P4 [major · material_response]
  - expect: The pack slides onto the drill as a rigid block and seats with a stop; drill and pack keep their shapes.
  - fail: The pack squashes or bends as it goes in; or the drill handle deforms around it; or the pack hangs a gap away from the drill once clipped.
- P5 [fatal · permanence_count]
  - expect: One drill, one pack, one bit; the pack stays clipped once in and fingers stay outside the drill.
  - fail: The pack vanishes after clipping in or a second pack appears; or the bit vanishes or a second bit appears; or the pack passes into the handle rather than onto it; or fingers pass through the drill.
- P6 [minor · attribute_drift]
  - expect: The drill's colour, the pack's label and the bench stay the same.
  - fail: The drill changes colour; or the bit changes length or type; or items on the bench rearrange.

## ELEC-0065 · plug_power · train

**Caption.** A robot vacuum finishes cleaning and drives onto its charging dock, and a charging light on the dock comes on.

**Expectation (hidden).** The light comes on once the robot is seated on the dock's contacts and stays on; it is off while the robot is away.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A robot vacuum on a floor, and its charging dock.
- S2 [core] The robot drives onto the dock and comes to rest against it.
- S3 [core] A light on the dock comes on.
- S4 [minor] The robot is driving about the floor before it heads to the dock.
- S5 [minor] The light is on the dock, not on the robot.
- S6 [minor] The order is drive, dock, light.

**PC**
- P1 [core · missing_consequence]
  - expect: The dock light is off while the robot is away and comes on when the robot comes to rest against the dock, and only then.
  - fail: The robot sits on the dock and the light stays off; or the light is on while the robot is still crossing the floor; or the light comes on as the robot passes by without stopping at the dock.
- P2 [core · process_direction]
  - expect: Once the robot is seated the light stays on for the rest of the clip while the robot stays on the dock.
  - fail: The light goes out again with the robot still seated on the dock; or the robot leaves the dock and the light stays lit; or the light shifts from the dock to a spot on the robot.
- P3 [major · trajectory_momentum]
  - expect: The robot rolls across the floor on its wheels and comes to rest with its front against the dock.
  - fail: The robot lifts off the floor as it nears the dock; or rides up on top of the dock; or slides sideways with its body facing away from its direction of travel.
- P4 [major · causeless_motion]
  - expect: The dock stays in place on the floor as the robot arrives; nothing else in the room moves.
  - fail: The dock slides or turns by itself before the robot reaches it; or the dock jumps to a new spot; or furniture or rugs shift as the robot docks.
- P5 [fatal · permanence_count]
  - expect: One robot and one dock; the robot keeps its body and does not pass into the dock or the wall.
  - fail: The robot vanishes or a second robot appears; or the robot merges into the dock; or the robot passes through the wall or a piece of furniture; or the dock changes shape.
- P6 [minor · attribute_drift]
  - expect: The floor pattern, the robot's colour and the dock's shape stay the same.
  - fail: The robot changes colour; or the floor pattern changes; or the dock light moves to a different place on the dock.

**Note.** The robot is a self-driven machine: its turning, slowing and stopping are not causeless motion. 'Finishes cleaning' is read as the robot driving on the floor before it heads to the dock.

## ELEC-0066 · plug_power · train

**Caption.** An electric kettle is lifted off its base while it is boiling, and the kettle's light goes off and the boiling quiets.

**Expectation (hidden).** The light goes out as the kettle leaves the base; the boiling dies down over a few seconds; it resumes only if replaced and switched on.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] An electric kettle sits on its base, with steam or churning water showing it is boiling.
- S2 [core] The kettle's light is lit at the start.
- S3 [core] The kettle is lifted off its base.
- S4 [core] The kettle's light goes off.
- S5 [minor] The steaming or churning eases after the lift.
- S6 [minor] The order is boiling on the base, lift, light off.

**PC**
- P1 [core · missing_consequence]
  - expect: The light goes out at the moment the kettle parts from the base, and only then.
  - fail: The kettle is off its base and its light still shines; or the light goes out before the kettle moves; or the light goes out with the kettle still seated and only afterwards is the kettle lifted.
- P2 [core · process_direction]
  - expect: After the lift the boil dies down one way: the steam plume thins and any churning at the surface settles, and neither returns while the kettle is off its base.
  - fail: The steam plume grows thicker after the lift; or the water churns harder once off the base; or the boil dies down and then returns with the kettle still in the air; or the light comes back on with the kettle off the base.
- P3 [major · gravity_direction] (if: Steam is visible.)
  - expect: Steam leaves the spout and rises, drifting upward and spreading; it does not sink or pool.
  - fail: Steam falls from the spout toward the counter; or hangs as a fixed shape that moves with the kettle like a solid; or steam rises from the empty base after the kettle is lifted.
- P4 [major · causeless_motion]
  - expect: The base stays on the counter as the kettle lifts off it; the counter and nearby items do not move.
  - fail: The base lifts with the kettle and hangs beneath it; or the base slides across the counter by itself; or nearby items jump as the kettle is lifted.
- P5 [fatal · permanence_count]
  - expect: One kettle and one base; the kettle keeps its shape with the lid on and does not pass through the base or the counter.
  - fail: The kettle passes through its base or the counter; or a second kettle appears; or the base vanishes; or the kettle changes shape or its spout moves.
- P6 [minor · attribute_drift]
  - expect: The kettle's colour, the base and the counter stay the same apart from the light and steam.
  - fail: The kettle changes colour; or the base changes design; or items on the counter change.

**Note.** 'The boiling quiets' is read visually: the steam plume thins and any visible churning settles. Sound is not judged, nor how far the boil has died down by the end of the clip.

## ELEC-0067 · plug_power · train

**Caption.** A camera's screen goes dark mid-recording as its battery runs out.

**Expectation (hidden).** The screen and the camera's lights go off together and stay off; the camera does not come back to life on its own.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A camera with its screen lit and showing a picture.
- S2 [core] The screen shows recording in progress: a record mark, a running counter or a lit record light.
- S3 [core] The screen goes dark.
- S4 [minor] No button is pressed and no battery is removed at the moment the screen goes dark.
- S5 [minor] The camera is lit and recording first and dark afterwards.

**PC**
- P1 [core · missing_consequence]
  - expect: The screen and any record or power light on the camera go dark together at one moment.
  - fail: The screen goes dark while the record light stays lit to the end of the clip; or the record light goes out while the screen keeps showing its picture; or the screen dims to a black picture with the counter still running on it.
- P2 [core · process_direction]
  - expect: Once dark, the screen and lights stay off for the rest of the clip; the camera does not restart by itself.
  - fail: The screen comes back on by itself; or switches between lit and dark several times; or the record light starts blinking again after the screen has gone dark.
- P3 [major · causeless_motion]
  - expect: The camera body stays put as the screen goes dark; nothing else in the scene changes at that moment.
  - fail: The camera shifts or tilts at the blackout with nothing touching it; or the screen swings shut by itself; or objects in the background move at the same instant.
- P4 [major · missing_consequence]
  - expect: The glow the screen cast on nearby surfaces disappears with it.
  - fail: The screen is black while its glow still lies on the table or hands beside it; or the surroundings brighten as the screen goes dark; or a glow remains around the screen's edges with the screen black.
- P5 [fatal · permanence_count]
  - expect: One camera; its screen stays part of the body and does not vanish or detach; nothing passes through the camera.
  - fail: The screen vanishes rather than going dark; or a second camera appears; or the camera changes shape; or a hand passes through the camera.
- P6 [minor · attribute_drift]
  - expect: The camera's colour, its buttons and the surface it rests on stay the same.
  - fail: The camera changes colour; or buttons move about the body; or the surface beneath changes pattern.

**Note.** The battery running out is invisible and is taken as given; the screen going dark is the caption's event, not a violation. What is judged is that screen and lights go together and stay off.

## ELEC-0068 · plug_power · train

**Caption.** A digital alarm clock is unplugged, and its glowing display goes blank.

**Expectation (hidden).** The display goes dark the instant the plug is pulled and lights again, blinking, when plugged in elsewhere.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A digital alarm clock with its display glowing.
- S2 [core] Its plug is pulled out of the socket.
- S3 [core] The display goes blank.
- S4 [minor] A cord runs from the clock to the plug.
- S5 [minor] The order is glowing, unplugged, blank.

**PC**
- P1 [core · missing_consequence]
  - expect: The display goes blank at the moment the plug leaves the socket, and only then.
  - fail: The plug is out and the digits still glow; or the display goes blank before the plug moves; or it goes blank with the plug still seated and the cord slack.
- P2 [core · process_direction]
  - expect: Once unplugged the display stays blank while the plug is out; digits do not return while no plug sits in a socket.
  - fail: The digits come back while the plug is out; or the display switches between lit and blank after unplugging; or the display lights up blinking with the plug lying loose.
- P3 [major · causeless_motion]
  - expect: The clock stays where it sits as the plug is pulled, apart from a tug along the cord; the cord hangs slack once the plug is free.
  - fail: The clock slides or turns with the cord slack; or the cord stands rigid in the air or floats; or the socket shifts along the wall.
- P4 [major · missing_consequence] (if: The plug is pushed into a socket again.)
  - expect: When plugged in again the display lights, blinking or showing a reset time, once the plug seats.
  - fail: The plug is seated again and the display stays blank to the end of the clip; or the display lights before the plug reaches the socket; or the display comes on and then goes blank again with the plug seated.
- P5 [fatal · permanence_count]
  - expect: One clock, one cord, one plug, one socket; the plug leaves the socket whole and nothing passes through the wall or the table.
  - fail: The plug vanishes or a second plug appears; or the plug passes through the wall; or the cord splits or detaches from the clock; or the clock changes shape.
- P6 [minor · attribute_drift]
  - expect: The clock's casing colour, its buttons and the surface it sits on stay the same apart from the display.
  - fail: The casing changes colour; or the buttons rearrange; or the digits change colour or font before going blank.

## ELEC-0069 · plug_power · train

**Caption.** A charger already plugged into the wall is connected to a laptop, and the small light on the connector comes on.

**Expectation (hidden).** The connector light is off before the plug seats in the laptop and comes on only then.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A laptop is present.
- S2 [core] A charger cable with a connector at its free end.
- S3 [core] The connector is pushed into the laptop.
- S4 [core] The small light on the connector comes on.
- S5 [minor] The charger's other end is already plugged into the wall.
- S6 [minor] The order is connect, then light.

**PC**
- P1 [core · missing_consequence]
  - expect: The connector light is dark while the connector is loose and comes on when it seats in the laptop's port, and only then.
  - fail: The connector is seated and its light stays dark; or the light is lit while the connector is still away from the laptop; or the laptop's own charging light comes on while the connector's light stays dark.
- P2 [core · process_direction]
  - expect: Once seated the light stays on while the connector stays in the port.
  - fail: The light goes out again with the connector still seated; or switches between lit and dark while the connector is untouched; or the connector backs out of the port by itself.
- P3 [major · missing_consequence] (if: The laptop's screen is on and facing the viewer.)
  - expect: The screen's battery indicator changes to charging when the connector seats and not before.
  - fail: The screen shows a charging symbol before the connector reaches the port; or the screen goes dark as the connector seats; or the screen's picture changes to a different one at the moment of connecting.
- P4 [major · material_response]
  - expect: The cable hangs slack from the connector in a curve and stays attached to it.
  - fail: The cable stands rigid in the air; or stretches like elastic as the connector is moved; or floats above the desk.
- P5 [fatal · permanence_count]
  - expect: One laptop and one connector on one cable; the connector enters the port rather than the laptop's body; fingers stay outside the laptop.
  - fail: The connector passes into the laptop's side away from the port; or a second connector or cable appears; or the connector vanishes; or the laptop changes shape.
- P6 [minor · attribute_drift]
  - expect: The laptop's colour, the cable's colour and the desk stay the same apart from the light.
  - fail: The laptop changes colour; or the cable changes colour or thickness; or the port moves along the laptop's side.

## ELEC-0070 · plug_power · train

**Caption.** A lamp is plugged into a socket and the socket switched on at the wall, and the lamp lights.

**Expectation (hidden).** The lamp lights only when the socket switch is on; with the plug in but the socket off it stays dark.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A lamp with a cord and plug, and a wall socket with its own switch.
- S2 [core] The plug is pushed into the socket.
- S3 [core] The socket switch is turned on.
- S4 [core] The lamp lights.
- S5 [minor] The switch is on the socket at the wall, not on the lamp.
- S6 [minor] The order is plug in, switch on, lamp lights.

**PC**
- P1 [core · missing_consequence]
  - expect: The lamp stays dark after the plug goes in and lights when the socket switch is turned on, and only then.
  - fail: The lamp lights as the plug goes in with the switch untouched; or the switch is turned and the lamp stays dark; or the lamp is lit before the plug reaches the socket.
- P2 [core · process_direction]
  - expect: Once lit the lamp stays lit steadily while the switch stays on.
  - fail: The lamp goes out again with the switch still on; or switches between lit and dark; or the socket switch flips back by itself.
- P3 [major · missing_consequence]
  - expect: The lamp's light reaches its surroundings: the shade glows and nearby surfaces brighten, with shadows pointing away from the lamp.
  - fail: The bulb glows while the shade and the surface beneath stay as dark as before; or the surroundings brighten while the lamp stays dark; or the light comes from a place other than the lamp.
- P4 [major · material_response]
  - expect: The cord hangs in a slack curve from the plug to the lamp and stays attached at both ends.
  - fail: The cord stands rigid between plug and lamp; or stretches like elastic as the plug is pushed in; or floats above the floor.
- P5 [fatal · permanence_count]
  - expect: One lamp, one plug, one socket with one switch; the plug enters the socket rather than the wall; fingers stay outside the wall.
  - fail: The plug passes into the wall beside the socket; or a second plug or lamp appears; or the socket switch vanishes or moves; or the lamp changes shape.
- P6 [minor · attribute_drift]
  - expect: The lamp's shade colour, the wall and the socket design stay the same apart from the light.
  - fail: The shade changes colour rather than brightness; or the wall changes colour; or the socket changes shape.

## ELEC-0071 · plug_power · train

**Caption.** Jumper cables from a running car are clamped onto a dead car's battery, and the dead car's dashboard lights come on.

**Expectation (hidden).** The lights on the dead car appear only after both clamps are connected; they were off before.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] Jumper cables with clamps lead from a second car to the open engine bay of the first.
- S2 [core] The clamps are fixed onto the dead car's battery terminals.
- S3 [core] The dead car's dashboard lights come on.
- S4 [minor] The dashboard is dark before the clamps go on.
- S5 [minor] The order is clamps on, then lights.

**PC**
- P1 [core · missing_consequence]
  - expect: The dashboard lights come on when the second clamp is seated on the battery, and only then.
  - fail: Both clamps are on the battery and the dashboard stays dark to the end of the clip; or the dashboard lights while the clamps are still off the battery; or the lights come on with one clamp hanging loose beside its terminal.
- P2 [core · process_direction]
  - expect: Once lit the dashboard stays lit while the clamps stay on the terminals.
  - fail: The dashboard goes dark again with the clamps still on; or the lights switch on and off with the clamps untouched; or a clamp springs off its terminal by itself.
- P3 [major · material_response]
  - expect: The cable hangs slack from each clamp, and the clamps are rigid jaws that grip the terminal posts.
  - fail: The cable stands rigid in the air or stretches like elastic; or a clamp bends like rubber around the post; or a clamp hangs on the post with its jaws still wide open.
- P4 [major · causeless_motion]
  - expect: The battery and the parts around it stay put as the clamps go on; the dead car does not move.
  - fail: The battery slides in its tray with nothing touching it; or the bonnet swings by itself; or the dead car rolls or rocks as the clamps go on.
- P5 [fatal · permanence_count]
  - expect: Two clamps on one battery; the clamps stay outside the battery casing; the cables stay continuous and the cars keep their shape.
  - fail: A clamp passes into the battery casing; or a third clamp appears or one vanishes; or a cable splits or detaches; or the battery changes shape.
- P6 [minor · attribute_drift]
  - expect: The cable colours, the battery's label and the engine bay stay the same.
  - fail: A cable changes colour; or the battery's label changes; or engine parts change shape or place.

**Note.** 'Running' has no visible sign the judge needs; the second car's engine is not judged. The battery and the dashboard are unlikely to share one view: S3 is judged on whatever view of the dead car's dashboard the clip gives, and P1 on the order of clamp seating and dashboard lighting as far as both are shown.

## ELEC-0072 · plug_power · train

**Caption.** A running sewing machine is unplugged, and the needle stops and its work light goes out.

**Expectation (hidden).** The needle stops within a stitch and the light goes off at the same time; the foot pedal does nothing afterwards.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A sewing machine runs with its needle moving up and down and its work light lit.
- S2 [core] Its plug is pulled out of the socket.
- S3 [core] The needle stops.
- S4 [core] The work light goes out.
- S5 [minor] A cord runs from the machine to the plug.
- S6 [minor] The order is running, unplugged, needle still and light off.

**PC**
- P1 [core · missing_consequence]
  - expect: The needle stops and the work light goes out together at the moment the plug leaves the socket.
  - fail: The plug is out and the needle keeps stitching; or the light stays lit with the plug out; or the needle stops long before the plug moves; or the light goes out while the needle carries on running.
- P2 [core · process_direction]
  - expect: Once unplugged the needle stays still and the light stays off; the machine does not run again while the plug is out.
  - fail: The needle starts stitching again with the plug out; or the light comes back on while unplugged; or the handwheel keeps turning after the needle has stopped.
- P3 [major · trajectory_momentum]
  - expect: While running, the needle moves straight up and down at one spot and the fabric passes under it in one direction.
  - fail: The needle wanders across the fabric; or the fabric reverses direction while the needle runs; or the fabric keeps feeding after the needle has stopped.
- P4 [major · material_response]
  - expect: The cord slackens and drops when the plug is free; the thread stays a limp thread and the fabric drapes as cloth.
  - fail: The cord stands rigid in the air or stretches like elastic; or the thread stands stiff above the fabric like wire; or the fabric moves like a rigid plate.
- P5 [fatal · permanence_count]
  - expect: One machine, one needle, one plug; the needle passes only through the fabric and the hole in the plate; the plug leaves the socket whole.
  - fail: The needle passes through the plate beside its hole; or a second needle appears; or the plug vanishes; or the machine changes shape.
- P6 [minor · attribute_drift]
  - expect: The machine's colour, the fabric's pattern and the thread stay the same apart from the light.
  - fail: The machine changes colour; or the fabric changes pattern; or the thread changes colour.

## ELEC-0073 · plug_power · train

**Caption.** A coin-cell battery is pressed into a wristwatch lying face up, and the second hand starts to tick.

**Expectation (hidden).** The hand begins moving only after the battery is seated; it was still before.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A wristwatch lies face up.
- S2 [core] A coin-cell battery is pressed into the watch.
- S3 [core] The second hand starts to move.
- S4 [minor] The second hand is still before the battery goes in.
- S5 [minor] The order is battery in, then the hand moves.

**PC**
- P1 [core · missing_consequence]
  - expect: The second hand is still while the battery is out and starts moving once the battery is seated, and only then.
  - fail: The battery is in and the second hand stays still to the end of the clip; or the hand moves before the battery reaches the watch; or the hand starts while the battery lies loose beside the watch.
- P2 [core · causeless_motion]
  - expect: Before the battery is seated nothing on the dial moves; afterwards only the second hand moves, advancing steadily.
  - fail: The hour or minute hand sweeps round on its own; or the second hand stops and restarts with the battery seated; or the second hand jumps to a new spot on the dial.
- P3 [major · process_direction]
  - expect: The second hand advances clockwise around the dial.
  - fail: The second hand runs anticlockwise; or swings back and forth about one spot; or reverses part-way round.
- P4 [major · material_response]
  - expect: The battery stays a rigid flat disc and seats into an opening in the watch; the watch stays put as it is pressed.
  - fail: The battery bends or squashes under the finger; or the watch slides or flips as the battery is pressed with nothing else touching it; or the battery pops out and hangs in the air.
- P5 [fatal · solidity]
  - expect: One watch and one battery; the battery enters an opening rather than sinking through the glass or case; the hands stay attached at the centre.
  - fail: The battery sinks through the watch glass or the case wall; or a second battery appears or the battery vanishes; or a hand detaches from the centre; or the watch changes shape.
- P6 [minor · attribute_drift]
  - expect: The dial's markings, the strap and the surface beneath stay the same.
  - fail: The dial numerals change; or the strap changes colour; or the battery changes size.

**Note.** A watch's battery compartment is in the back, hidden when the watch lies face up; the judge accepts whatever opening the battery visibly enters and does not fail the clip for where the compartment is.

## ELEC-0074 · plug_power · train

**Caption.** A power cut hits a kitchen, and the fridge hum stops, the oven clock goes blank and the ceiling light goes out all at once.

**Expectation (hidden).** Everything electrical in the room stops at the same instant; when power returns the light and clock come back together.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A kitchen with its ceiling light lit and an oven whose clock display is lit.
- S2 [core] The ceiling light goes out.
- S3 [core] The oven clock goes blank.
- S4 [minor] A fridge is in view.
- S5 [minor] The light and the clock go off at the same moment.

**PC**
- P1 [core · missing_consequence]
  - expect: The ceiling light and the oven clock go dark at the same moment.
  - fail: The light goes out and the clock stays lit to the end of the clip; or the clock goes blank while the light stays on; or the light goes out first and the clock goes blank only later; or a lit display on the fridge stays lit after the light and clock have gone dark.
- P2 [core · permanence_count]
  - expect: The kitchen's contents are the same before and after the cut: the same fridge, oven and furniture in the same places, whether seen dim or lit again.
  - fail: Items on the counters appear or vanish between the lit and dark frames; or the fridge or oven changes place; or a lit window or lamp appears in the dark that was not there before.
- P3 [major · missing_consequence]
  - expect: When the ceiling light goes out the room darkens with it: light from the fixture leaves the walls and floor, and whatever light remains comes from windows or sources present before.
  - fail: The fixture goes dark while the room stays as bright; or the room darkens while the fixture still glows; or light stays pooled under the dark fixture.
- P4 [major · process_direction]
  - expect: Once off, the light and the clock stay off; if power returns they come back together.
  - fail: The light comes back while the clock stays blank to the end of the clip; or the clock comes back while the light stays out; or the light switches on and off repeatedly while the clock stays blank.
- P5 [fatal · shape_identity]
  - expect: The fridge, oven, cabinets and fixture keep their shapes; the fixture stays on the ceiling and nothing passes through a wall or counter.
  - fail: The fixture drops or vanishes rather than going dark; or an appliance or cabinet changes shape; or a hand or object passes through a counter or wall.
- P6 [minor · attribute_drift]
  - expect: Wall and cabinet colours and the items on the counters stay the same apart from brightness.
  - fail: Cabinets change colour rather than brightness; or the oven's control layout changes; or items on the counter change colour.

**Note.** The fridge hum is sound and is not judged; the fridge counts only through any lit display or indicator it has. The moment of the cut is read from the light and the clock going dark.

## ELEC-0075 · plug_power · train

**Caption.** A nightlight is plugged into a low wall socket, and it begins to glow.

**Expectation (hidden).** The glow appears as the prongs go into the socket and stays steady; it goes out when the nightlight is pulled out.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A nightlight and a wall socket set low on the wall.
- S2 [core] The nightlight is pushed into the socket.
- S3 [core] The nightlight glows.
- S4 [minor] The socket is low, near the floor.
- S5 [minor] The nightlight is dark before it goes in.
- S6 [minor] The order is plug in, then glow.

**PC**
- P1 [core · missing_consequence]
  - expect: The glow appears when the nightlight's prongs seat in the socket, and only then.
  - fail: The nightlight is seated and stays dark; or it glows while still held away from the wall; or it lights up while lying on the floor.
- P2 [core · process_direction]
  - expect: Once in, the nightlight glows steadily for the rest of the clip and goes dark only if pulled out.
  - fail: The glow fades out with the nightlight still in the socket; or switches on and off; or the nightlight glows on after being pulled out of the socket.
- P3 [major · missing_consequence] (if: The room is dim.)
  - expect: The glow lights the wall around the socket and the floor beneath, centred on the nightlight.
  - fail: The nightlight glows while the wall around it stays as dark as before; or the wall brightens while the nightlight is dark; or the pool of light sits away from the nightlight.
- P4 [major · gravity_direction]
  - expect: Once seated the nightlight hangs on the socket with nothing else holding it and does not sag or fall.
  - fail: The nightlight drops off the socket once the hand withdraws; or slides down the wall; or hovers a gap away from the socket.
- P5 [fatal · permanence_count]
  - expect: One nightlight and one socket; the prongs enter the socket holes rather than the wall; fingers stay outside the wall.
  - fail: The nightlight passes into the wall beside the socket; or a second nightlight appears; or the socket moves along the wall or vanishes; or the nightlight changes shape.
- P6 [minor · attribute_drift]
  - expect: The nightlight's colour and shape, the wall and the skirting stay the same apart from the glow.
  - fail: The nightlight changes colour rather than brightness; or the wall changes colour; or the socket changes design.

## ELEC-0076 · plug_power · train

**Caption.** An aquarium pump is plugged into the wall, and bubbles start rising from the air stone in the tank.

**Expectation (hidden).** The bubbles begin only after the pump is plugged in and stop when it is unplugged; they rise upward through the water.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] An aquarium tank with water and an air stone in it.
- S2 [core] The pump's plug is pushed into a wall socket.
- S3 [core] Bubbles rise from the air stone.
- S4 [minor] No bubbles rise before the plug goes in.
- S5 [minor] The order is plug in, then bubbles.

**PC**
- P1 [core · missing_consequence]
  - expect: Bubbles begin at the air stone when the plug seats in the socket, and only then.
  - fail: The plug is in and no bubbles come from the stone; or bubbles stream before the plug reaches the socket; or bubbles appear elsewhere in the tank while the stone gives none.
- P2 [core · causeless_motion]
  - expect: Before plugging in the water is still with no bubbles; afterwards the stream runs continuously while the plug stays in.
  - fail: Bubbles start and stop with the plug seated and untouched; or the water surface churns before any bubble rises; or the air tubing whips about by itself.
- P3 [major · gravity_direction]
  - expect: Bubbles rise from the stone to the surface and break there; none sink or hover.
  - fail: Bubbles sink toward the gravel; or hang still in the water; or run back down into the stone.
- P4 [major · missing_consequence]
  - expect: Where the stream reaches the surface the water ripples, and plants in the stream sway with it.
  - fail: The stream reaches the surface and the surface directly above the stone stays glassy still; or ripples appear far from the stream while the surface above it is still; or plants far from the stream sway while those in it stay rigid.
- P5 [fatal · permanence_count]
  - expect: One tank, one air stone, one plug; bubbles form at the stone; the tank's glass stays whole.
  - fail: Bubbles appear from nowhere in mid-water away from the stone; or the air stone vanishes or a second one appears; or water passes through the glass; or the plug passes into the wall beside the socket.
- P6 [minor · attribute_drift]
  - expect: The gravel, decorations and the tank's frame stay the same.
  - fail: The gravel changes colour; or decorations move or change; or the air stone changes shape.

**Note.** Fish are self-driven and are not judged.

## ELEC-0077 · plug_power · train

**Caption.** A laptop is unplugged from its charger, and the charging light on it goes off while the screen stays on.

**Expectation (hidden).** The charging light goes out with the unplugging but the laptop keeps running on its battery; the screen does not go dark.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A laptop with its screen on and a charger connected to it, its charging light lit.
- S2 [core] The charger connector is pulled out of the laptop.
- S3 [core] The charging light goes off.
- S4 [core] The screen stays on after the pull.
- S5 [minor] The charging light is on the laptop itself.
- S6 [minor] The order is lit, pull, light off with the screen still on.

**PC**
- P1 [core · missing_consequence]
  - expect: The charging light goes out at the moment the connector leaves the port, and only then.
  - fail: The connector is out and the charging light still shines; or the light goes out before the connector moves; or the light goes out with the connector still seated and untouched.
- P2 [core · permanence_count]
  - expect: The screen's contents carry on through the pull, apart from a battery indicator changing state; windows and icons stay where they were.
  - fail: Icons or windows vanish or appear at the moment of unplugging; or the screen's picture jumps to a different one at the pull; or a second charging light appears elsewhere on the laptop.
- P3 [major · process_direction]
  - expect: Once the connector is out the charging light stays off.
  - fail: The charging light comes back on with the connector out; or blinks after the pull; or the connector slides back into the port by itself.
- P4 [major · material_response]
  - expect: The cable follows the connector: it slackens and drops as the connector comes free and stays attached to it.
  - fail: The cable stands rigid in the air; or stretches like elastic; or the connector floats beside the port.
- P5 [fatal · shape_identity]
  - expect: One laptop and one connector on one cable; the connector leaves the port whole; the laptop keeps its shape and fingers stay outside it.
  - fail: The connector passes out through the laptop's body rather than the port; or the connector vanishes or duplicates; or the laptop's lid or keyboard changes shape; or the cable splits.
- P6 [minor · attribute_drift]
  - expect: The laptop's colour, its keyboard layout and the desk stay the same apart from the light.
  - fail: The laptop changes colour; or the keyboard layout changes; or the port moves along the side.

**Note.** A screen that goes dark at the pull fails S4 only: a laptop with a flat battery does go dark when unplugged, so no PC item fails for it.

## ELEC-0078 · plug_power · train

**Caption.** An electric blanket is plugged in and switched on, and its small control light comes on.

**Expectation (hidden).** The light comes on after both the plug and the switch and goes off when either is undone.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] An electric blanket with a cord and a small controller.
- S2 [core] The blanket's plug is pushed into a socket.
- S3 [core] The switch on the controller is turned on.
- S4 [core] The small light on the controller comes on.
- S5 [minor] The light is on the blanket's controller, not elsewhere.
- S6 [minor] The order is plug in, switch on, light.

**PC**
- P1 [core · missing_consequence]
  - expect: The control light stays dark after the plug goes in and comes on when the switch is turned on, and only then.
  - fail: The light comes on as the plug goes in with the switch untouched; or the switch is turned and the light stays dark; or the light is lit before the plug reaches the socket.
- P2 [core · process_direction]
  - expect: Once lit the light stays on while the plug and switch stay as they are; it goes off only if the switch is turned back or the plug pulled.
  - fail: The light goes out with the switch on and the plug in; or switches on and off untouched; or stays lit after the plug has been pulled out.
- P3 [major · causeless_motion]
  - expect: The blanket lies as it was laid and moves only where the controller or cord is handled.
  - fail: The blanket ripples or shifts by itself as the light comes on; or lifts off the bed; or the cord slides across the blanket with nothing touching it.
- P4 [major · material_response]
  - expect: The blanket drapes as cloth, the cord hangs slack and the controller is a rigid block.
  - fail: The blanket stands stiff like a board; or the cord stands rigid in the air or stretches like elastic; or the controller bends when pressed.
- P5 [fatal · permanence_count]
  - expect: One blanket, one cord, one controller, one plug; the plug enters the socket rather than the wall and the controller stays on top of the blanket.
  - fail: The plug passes into the wall beside the socket; or a second controller or plug appears; or the controller sinks into the blanket; or the cord splits or detaches.
- P6 [minor · attribute_drift]
  - expect: The blanket's colour and pattern, the controller's markings and the bed stay the same apart from the light.
  - fail: The blanket changes colour or pattern; or the controller's markings change; or the bedding changes.

## ELEC-0079 · plug_power · train

**Caption.** A battery-powered toy car slows and stops as its battery runs flat, and its headlights dim and go out.

**Expectation (hidden).** The car loses speed gradually and stops; the lights dim and go out around the same time and do not come back; it does not speed up again.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A toy car drives along with its headlights lit.
- S2 [core] The car slows and stops.
- S3 [core] The headlights dim and go out.
- S4 [minor] The car is battery powered: no cord or track feeds it.
- S5 [minor] The lights dim before they go out.
- S6 [minor] Moving and lit comes first, slowing and dimming follow, and the car is stopped and dark at the end.

**PC**
- P1 [core · missing_consequence]
  - expect: The headlights dim as the car slows and go out around the time it stops; the two fade together.
  - fail: The car stops while the headlights stay at full brightness to the end of the clip; or the lights go out while the car drives on to the end of the clip; or the lights go out well before the car begins to slow.
- P2 [core · process_direction]
  - expect: Slowing, stopping and dimming run one way: the car does not speed up or move again, and the lights do not brighten or come back.
  - fail: The car speeds up again after slowing; or moves off again after stopping with nothing touching it; or the headlights come back on after going out; or the lights brighten as the car slows.
- P3 [major · trajectory_momentum]
  - expect: The car rolls on its wheels along the surface in the direction it faces; its wheels turn while it moves and stop when it stops.
  - fail: The car slides sideways or drifts with its wheels still; or the wheels keep turning after the body has stopped; or the car lifts off the surface as it slows.
- P4 [major · causeless_motion]
  - expect: Nothing else on the floor moves when the car slows and stops.
  - fail: Objects nearby shift as the car stops; or the car rocks or slides after halting with nothing touching it; or the rug slides beneath it.
- P5 [fatal · permanence_count]
  - expect: One toy car with its wheels and lights attached; it stays on the surface and passes through nothing.
  - fail: The car vanishes or a second car appears; or a wheel detaches or a headlight vanishes rather than going dark; or the car passes through a piece of furniture or a wall; or it changes shape.
- P6 [minor · attribute_drift]
  - expect: The car's colour and markings and the floor stay the same apart from the lights.
  - fail: The car changes colour; or its decals change; or the floor pattern changes.

**Note.** The car is a powered toy: its slowing and stopping are the caption's event, not causeless motion. How quickly it slows is not judged.

## ELEC-0080 · plug_power · train

**Caption.** An electric lawnmower reaches the end of its cord and the plug pulls out of the socket, and the mower stops.

**Expectation (hidden).** The blades and motor stop within a second or two of the plug coming out; the mower does not keep cutting.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] An electric lawnmower on a lawn with a cord running from it to a socket.
- S2 [core] The plug pulls out of the socket.
- S3 [core] The mower stops.
- S4 [minor] The cord is drawn straight and taut before the plug comes out.
- S5 [minor] The order is mowing, cord taut, plug out, mower stops.

**PC**
- P1 [core · missing_consequence]
  - expect: The mower stops when the plug leaves the socket: its travel ends and any stream of cut grass from the chute ceases.
  - fail: The plug is out and the mower carries on mowing to the end of the clip; or the mower halts and its grass stream stops before the cord has gone taut; or grass keeps flying from the chute with the plug lying loose.
- P2 [core · process_direction]
  - expect: Once the plug is out the mower stays stopped; it does not start again with the plug lying loose, and the cut strip behind it stays cut.
  - fail: The mower starts up again with the plug out; or grass discharge resumes with the plug on the ground; or the plug jumps back into the socket by itself; or the cut strip behind the mower returns to uncut.
- P3 [major · material_response]
  - expect: The cord is drawn straight and taut before the plug comes out; once free it goes slack and drops to the grass.
  - fail: The plug comes out while the cord hangs slack; or the cord stays stretched straight in the air after the plug is free; or the cord stretches like elastic; or the plug flies upward and stays aloft.
- P4 [major · trajectory_momentum]
  - expect: The mower stays on the grass on its wheels; if it moves after the plug comes out it only coasts on in the direction it was going.
  - fail: The mower reverses direction on its own as the plug comes out; or lifts off the grass; or slides sideways across the lawn.
- P5 [fatal · permanence_count]
  - expect: One mower, one cord, one plug, one socket; the plug leaves the socket whole and the mower passes through nothing.
  - fail: The plug vanishes or a second plug appears; or the cord splits or detaches from the mower; or the mower passes through a fence or tree; or the mower changes shape.
- P6 [minor · attribute_drift]
  - expect: The mower's colour, the cord's colour and the socket or reel stay the same.
  - fail: The mower changes colour; or the cord changes colour; or the socket or reel changes design.

**Note.** The motor and blades are hidden under the deck: 'the mower stops' is read from the mower's travel, the grass stream from the chute and any visible blade blur; sound is not judged. Who or what pushes the mower is not judged.

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

## ELEC-0083 · lightning · train

**Caption.** An empty living room lit by a single lamp during a storm brightens for an instant as lightning flashes through the window.

**Expectation (hidden).** The room brightens sharply from the window side and returns to its lamp-lit state immediately; sharp window-frame shadows appear only during the flash.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] An empty living room lit by a single lamp.
- S2 [core] A window is in view or its light falls into the room.
- S3 [core] The room brightens for an instant, as from a flash outside the window.
- S4 [minor] A storm shows outside the window: dark sky, rain or streaked glass.
- S5 [minor] The lamp is lit before, during and after the flash.
- S6 [minor] The order is lamp-lit, flash, lamp-lit again.

**PC**
- P1 [core · process_direction]
  - expect: The brightening is brief: the room lights up and returns to its lamp-lit state; flashes may repeat but each ends.
  - fail: The room stays bright to the end of the clip after the flash; or brightens steadily without ending; or the flash fades in slowly like a dimmer being turned up; or the room ends darker than its lamp-lit state with the lamp still lit.
- P2 [core · missing_consequence]
  - expect: The flash light enters from the window side: surfaces facing the window brighten most and the far side of the room least.
  - fail: The whole room brightens evenly with no side brighter; or the brightening comes from the lamp's side while the window side stays as it was; or the window glass stays dark while the room lights up.
- P3 [major · process_direction]
  - expect: Sharp shadows of the window frame appear on the floor or the wall opposite only during the flash and vanish with it; the lamp's own soft shadows remain as before.
  - fail: The frame's shadow stays on the wall after the room has returned to lamp light; or the shadow appears before the flash; or the shadow lies on the window side of the objects rather than away from the window.
- P4 [major · causeless_motion]
  - expect: Nothing in the room moves at the flash: furniture, pictures, the lamp and the curtains stay as they were, apart from curtains stirring in a draught.
  - fail: Furniture or pictures shift at the flash; or the lamp moves or swings; or a door opens by itself; or the curtains fly up sharply at the instant of the flash while nothing else stirs.
- P5 [fatal · permanence_count]
  - expect: The room's contents are the same before, during and after the flash: the flash reveals what was there and creates or removes nothing.
  - fail: Furniture or pictures appear or vanish between the dim and lit frames; or the lamp vanishes or duplicates; or the window moves along the wall; or the room's layout changes after the flash.
- P6 [minor · attribute_drift]
  - expect: Wall colours, the lampshade and the curtains keep their colours apart from brightness.
  - fail: The walls change colour rather than brightness; or the lampshade changes colour; or the curtains change pattern.

## ELEC-0084 · lightning · train

**Caption.** Lightning strikes a tall tree in a field, and the tree is lit brilliantly for a moment and then smoke rises from its top.

**Expectation (hidden).** The bolt ends at the tree, the flash is instantaneous, and the smoke appears after the flash and rises; the tree does not glow afterwards.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A tall tree stands in a field.
- S2 [core] A lightning bolt comes down and strikes the tree.
- S3 [core] The tree is lit brilliantly for a moment.
- S4 [core] Smoke rises from the top of the tree afterwards.
- S5 [minor] The bolt ends at the tree, not beside it.
- S6 [minor] The bolt and flash come first and the smoke follows.

**PC**
- P1 [core · process_direction]
  - expect: The bolt and its flash are brief: they appear and are gone, and the tree returns to its unlit look; the smoke appears only after the flash and grows from there.
  - fail: The bolt stands as a steady lit line for the rest of the clip; or the tree keeps glowing after the bolt is gone; or smoke rises from the tree before the bolt arrives; or the smoke shrinks back into the tree.
- P2 [core · permanence_count]
  - expect: The tree that is struck is the tree seen before: the same trunk and crown in the same place, whole or split, and the bolt ends at it.
  - fail: The tree vanishes with the flash; or a second tree appears where the bolt struck; or the tree changes place between dark and lit frames; or the tree turns into a different tree or object after the flash.
- P3 [major · gravity_direction]
  - expect: The smoke rises from the top of the tree, drifting upward and spreading; anything knocked off the tree falls to the ground.
  - fail: The smoke sinks down the trunk and pools on the ground; or hangs as a fixed shape that does not drift; or branches or bark knocked off rise or hang in the air.
- P4 [major · shape_identity]
  - expect: The bolt is a jagged, branching bright line with a main channel from the cloud to the tree.
  - fail: The bolt is a perfectly straight beam; or a smooth wave; or a wide glowing tube; or a bolt that hangs in mid-air touching neither cloud nor tree while the tree lights up.
- P5 [major · missing_consequence]
  - expect: The flash lights its surroundings: the field and the cloud undersides brighten during the bolt, lit from the bolt's direction.
  - fail: The bolt is visible while the field around the tree stays as dark as before; or the field lights up while no bolt is present; or the ground is lit far from the tree while the ground around the tree stays dark.
- P6 [fatal · solidity]
  - expect: The tree stays a solid trunk rooted in the ground; the bolt ends at the tree and does not pass through it into the ground; the field stays ground.
  - fail: The bolt continues below the tree as a lit line under the ground; or the tree becomes transparent with the bolt seen through it; or the trunk melts or flows; or the ground splits open and swallows the tree.
- P7 [minor · attribute_drift]
  - expect: The tree's foliage colour, the field and the sky keep their colours apart from the flash.
  - fail: The foliage changes colour rather than brightness; or the field changes colour; or the sky turns to daylight after the flash.

## ELEC-0085 · lightning · train

**Caption.** Lightning flashes far beyond a mountain range at night, and the outline of the peaks stands out against the lit sky for an instant.

**Expectation (hidden).** The sky behind the mountains brightens briefly and the peaks appear as dark shapes; the light is gone in a fraction of a second.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] A mountain range at night.
- S2 [core] Lightning flashes in the sky beyond the range.
- S3 [core] The peaks stand out as dark outlines against the lit sky.
- S4 [minor] The flash is far off, behind the mountains rather than over the foreground.
- S5 [minor] The sky returns to dark after the flash.

**PC**
- P1 [core · process_direction]
  - expect: Each flash is brief: the sky brightens and returns to dark; flashes may repeat but each ends.
  - fail: The sky stays lit for the rest of the clip; or brightens steadily without ending; or turns to daylight; or the light fades in slowly like a sunrise.
- P2 [core · missing_consequence]
  - expect: The light comes from behind the range: the sky and clouds beyond the peaks brighten while the near faces of the mountains stay dark, so the peaks are silhouettes.
  - fail: The near faces of the mountains light up while the sky behind stays dark; or the foreground brightens more than the sky; or the peaks glow brighter than the sky behind them.
- P3 [major · permanence_count]
  - expect: The outline of the range is the same in lit and dark frames: the same peaks in the same places.
  - fail: Peaks appear or vanish between the dark and lit frames; or the ridge line changes shape; or the range shifts across the frame while the foreground stays put.
- P4 [major · causeless_motion]
  - expect: The mountains and the foreground stay still through the flash; only the light changes; clouds drift slowly if at all.
  - fail: The mountains shift or shake at the flash; or foreground trees or rocks move at the flash; or clouds jump to new shapes between one frame and the next.
- P5 [fatal · shape_identity]
  - expect: The mountains stay solid ground; the flash does not pass through them or light them from within.
  - fail: A mountain becomes transparent with the flash seen through it; or the range melts into cloud; or a bolt emerges from inside a peak; or the range morphs into a different landscape.
- P6 [minor · attribute_drift]
  - expect: The night colours of sky and land are consistent before and after; the flash whitens or blues the sky only briefly.
  - fail: The sky changes colour permanently after the flash; or the mountains change colour; or the foreground changes colour.

## ELEC-0086 · lightning · train

**Caption.** A lightning bolt strikes the sea beyond a beach at night, and the water and the wet sand flash bright and then go dark.

**Expectation (hidden).** The bolt descends to the water, the flash reflects in the wet sand and sea surface, and everything returns to dark at once.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A beach at night with the sea beyond it.
- S2 [core] A lightning bolt comes down to the sea.
- S3 [core] The water and the wet sand flash bright.
- S4 [core] The scene goes dark again.
- S5 [minor] The bolt ends at the sea, not on the beach.
- S6 [minor] The order is bolt, flash, dark.

**PC**
- P1 [core · process_direction]
  - expect: The bolt and flash are brief; sea, sand and sky return to dark together.
  - fail: The bolt stands as a steady line for the rest of the clip; or the sea keeps glowing after the bolt is gone; or the sand stays lit while the sky is dark again; or the flash fades in slowly.
- P2 [core · permanence_count]
  - expect: The beach, the shoreline and the sea are the same before and after: the flash reveals what was there.
  - fail: Rocks, boats or structures appear or vanish between dark and lit frames; or the shoreline moves; or a bolt hangs in place after the flash as a glowing pillar on the water; or a second bolt stands frozen beside the first.
- P3 [major · missing_consequence]
  - expect: The flash is mirrored in the wet sand and the sea surface: bright patches lie below the lit sky, strongest where the surfaces are wettest, during the flash only.
  - fail: The sky flashes while the wet sand and sea stay as dark as before; or the reflection lies on the dry sand and not on the wet; or the mirrored light remains after the sky is dark; or the reflection appears before the sky flashes.
- P4 [major · shape_identity]
  - expect: The bolt is a jagged, branching bright line with a main channel from cloud to sea.
  - fail: The bolt is a perfectly straight beam; or a smooth curve; or a wide glowing tube; or a bolt that hangs in mid-air touching neither cloud nor sea.
- P5 [fatal · solidity]
  - expect: The sea stays a surface of water with waves and the sand stays ground; nothing passes through either.
  - fail: The bolt continues below the sea surface as a lit line under the water; or the sand splits open or heaves at the strike; or the sea's surface turns into a solid sheet; or the sea vanishes leaving bare ground.
- P6 [minor · attribute_drift]
  - expect: The sand, the sea and the sky keep their night colours apart from the flash.
  - fail: The sky turns to daylight after the flash; or the sand changes colour; or the sea changes colour permanently.

## ELEC-0087 · lightning · train

**Caption.** Several flashes of lightning light up a stormy sky over a highway one after another, each one lighting the wet road for an instant.

**Expectation (hidden).** Each flash is separate and brief with darkness between; the road reflects each flash; the flashes do not merge into a steady glow.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A highway under a stormy sky.
- S2 [core] Lightning flashes in the sky more than once.
- S3 [core] Each flash lights the wet road.
- S4 [minor] The road looks wet: shiny or streaked with reflections.
- S5 [minor] The flashes come one after another, with darker sky between them.

**PC**
- P1 [core · process_direction]
  - expect: Each flash is separate and brief: the sky brightens, returns to dark, and brightens again; between flashes the scene is at its dark storm level.
  - fail: The flashes merge into a steady glow that lasts to the end of the clip; or the sky brightens steadily without dropping back; or a flash fades in slowly like a dimmer; or the sky turns to daylight.
- P2 [core · permanence_count]
  - expect: The road, its markings, the vehicles and the roadside are the same across dark and lit frames; each flash reveals the same scene.
  - fail: Vehicles appear or vanish between dark and lit frames; or lane markings jump to new places; or roadside signs or poles appear or vanish; or the road bends differently between frames.
- P3 [major · missing_consequence]
  - expect: The wet road mirrors each flash: bright streaks and patches lie on the surface below the lit sky, during the flash only.
  - fail: The sky flashes while the wet road stays as dark as before; or the road lights up while the sky stays dark; or the road's reflection stays lit after the sky is dark.
- P4 [major · trajectory_momentum] (if: Vehicles are moving on the highway.)
  - expect: Vehicles keep their direction and lane through each flash; headlights and tail lights stay steady.
  - fail: A vehicle jumps ahead or back between dark and lit frames; or changes direction at a flash; or its headlights go out at the flash and return afterwards.
- P5 [fatal · shape_identity]
  - expect: Vehicles, signs and the road keep their shapes; nothing passes through anything; any bolt seen ends at the ground or in the air, not inside a vehicle or structure.
  - fail: A vehicle changes shape or merges with another; or a bolt passes through a vehicle or bridge and lights it like a lamp; or the road surface turns into open water; or a sign morphs into another object.
- P6 [minor · attribute_drift]
  - expect: The road surface, the vehicles' colours and the roadside keep their colours apart from brightness.
  - fail: A vehicle changes colour; or the lane markings change colour; or the sky changes colour permanently after a flash.

## ELEC-0088 · lightning · train

**Caption.** Lightning flashes outside an empty parked car in a rainstorm, and the inside of the car lights up through the rain-streaked windows for an instant.

**Expectation (hidden).** The interior brightens for an instant from the window side, the raindrops on the glass glint, and the cabin is dim again right after.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] A parked car with its interior in view and no one inside.
- S2 [core] Rain streaks the windows.
- S3 [core] A flash from outside lights the interior for an instant.
- S4 [minor] The car is stationary: the scene outside the windows does not move past.
- S5 [minor] The interior is dim before and after the flash.

**PC**
- P1 [core · process_direction]
  - expect: The brightening is brief: the cabin lights up and returns to dim; flashes may repeat but each ends.
  - fail: The cabin stays lit to the end of the clip after the flash; or brightens steadily; or the dashboard or dome light comes on at the flash and stays on; or the flash fades in slowly.
- P2 [core · missing_consequence]
  - expect: The light enters through the windows: the glass is the brightest part, surfaces facing the windows brighten most, and pillars and seat backs throw shadows away from the windows.
  - fail: The cabin brightens evenly with no direction; or the windows stay dark while the cabin lights up; or the light comes from inside the car with the windows unchanged; or shadows point toward the windows.
- P3 [major · gravity_direction]
  - expect: Rain runs down the windows and falls past them downward.
  - fail: Streaks on the glass run upward; or the water on the glass flows toward the roof; or rain outside rises or hangs still.
- P4 [major · causeless_motion]
  - expect: The car and its contents stay still at the flash: nothing inside moves and the car does not rock.
  - fail: Items inside shift at the flash; or the steering wheel turns by itself; or a door opens; or the car rocks at the instant of the flash.
- P5 [fatal · permanence_count]
  - expect: The cabin's contents are the same before, during and after: the same seats, mirror, dashboard and items; the flash reveals what was there.
  - fail: Items appear or vanish between dim and lit frames; or a person appears in a seat; or the dashboard changes layout; or a window changes shape or place.
- P6 [minor · attribute_drift]
  - expect: The seats' colours, the dashboard and the view outside keep their colours apart from brightness.
  - fail: The seats change colour rather than brightness; or the dashboard changes colour; or the scene outside the windows jumps to a different place.

## ELEC-0089 · lightning · train

**Caption.** Lightning flashes over a wet city street at night, and the flash is mirrored in the puddles and the wet pavement.

**Expectation (hidden).** The reflections appear and vanish with the flash and lie below the sky in the water; the streetlights keep their steady glow.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] A city street at night with wet pavement and puddles.
- S2 [core] Lightning flashes over the street.
- S3 [core] The flash is mirrored in the puddles and the wet pavement.
- S4 [minor] Streetlights are lit.
- S5 [minor] The mirrored flash appears with the flash in the sky, not before it.

**PC**
- P1 [core · process_direction]
  - expect: The flash is brief; the sky and its reflections return to dark together; flashes may repeat but each ends.
  - fail: The sky stays lit for the rest of the clip; or the reflection remains lit after the sky is dark; or the flash fades in slowly; or the sky turns to daylight.
- P2 [core · missing_consequence]
  - expect: The reflections lie in the wet surfaces below the lit sky, with the dark shapes of buildings between; they appear only during the flash.
  - fail: The sky flashes while puddles and pavement stay as dark as before; or the puddles brighten while the sky stays dark; or the bright patch in a puddle sits under a building where no sky is above it; or the reflection appears before the sky flashes.
- P3 [major · causeless_motion]
  - expect: Streetlights, lit windows and signs keep their steady glow through the flash; nothing in the street moves at the flash.
  - fail: Streetlights blink out at the flash or all change together; or lit windows go dark at once; or parked cars or bins shift at the flash.
- P4 [major · permanence_count]
  - expect: Buildings, cars and street furniture are the same across dark and lit frames.
  - fail: Buildings or cars appear or vanish between dark and lit frames; or puddles appear or vanish between frames; or a sign changes place.
- P5 [fatal · solidity]
  - expect: The street stays a street: the puddles are thin water on a solid surface, buildings keep their shape and nothing passes through anything.
  - fail: A puddle swallows an object; or a building changes shape; or a bolt passes through a building and lights its inside; or the street surface ripples like open water.
- P6 [minor · attribute_drift]
  - expect: Building and sign colours and the pavement stay the same apart from brightness.
  - fail: Signs change lettering or colour; or buildings change colour; or a puddle changes shape while nothing disturbs it.

## ELEC-0090 · lightning · train

**Caption.** A lightning bolt hits the metal rod on top of a tall building, and the rod and roof flash bright for an instant.

**Expectation (hidden).** The bolt ends at the rod, the flash is brief, and the building is unchanged afterwards; the bolt does not linger or move along the roof.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A tall building with a metal rod on top.
- S2 [core] A lightning bolt comes down to the rod.
- S3 [core] The rod and the roof flash bright for an instant.
- S4 [minor] The bolt ends at the rod, not elsewhere on the roof or on the building's side.
- S5 [minor] The order is bolt, flash, dark.

**PC**
- P1 [core · process_direction]
  - expect: The bolt appears and is gone; the rod and roof return to their unlit look and stay so.
  - fail: The bolt stands as a steady lit line for the rest of the clip; or the rod glows on after the bolt is gone; or the bolt's foot creeps along the roof; or the flash fades in slowly.
- P2 [core · permanence_count]
  - expect: The building, its rod and the skyline are the same before and after the strike.
  - fail: The rod vanishes or bends after the strike; or a second rod or building appears; or the roof line changes between dark and lit frames; or the building changes place.
- P3 [major · shape_identity]
  - expect: The bolt is a jagged, branching line whose main channel ends at the tip of the rod.
  - fail: The bolt is a straight beam or a smooth arc; or a wide glowing tube; or it ends at a point in mid-air beside the rod while the rod lights up.
- P4 [major · missing_consequence]
  - expect: The flash lights the surroundings: the roof, nearby facades and the cloud undersides brighten during the bolt, lit from the bolt.
  - fail: The bolt is visible while the roof and nearby facades stay as dark as before; or the street below is lit while the roof beside the rod stays dark; or the roof brightens with no bolt present.
- P5 [fatal · solidity]
  - expect: The bolt ends at the rod and does not pass through the roof into the building; the building stays solid.
  - fail: The bolt continues down through the roof and lights the floors inside like lamps; or the roof opens or caves in; or the bolt passes through the building's wall; or the rod sinks into the roof.
- P6 [minor · attribute_drift]
  - expect: The facade's colour, the windows' lit pattern and the sky keep their look apart from the flash.
  - fail: The facade changes colour rather than brightness; or the lit windows change pattern all at once; or the sky turns to daylight after the flash.

## ELEC-0091 · lightning · train

**Caption.** Heat lightning flickers silently on the horizon beyond a lake on a summer night, lighting the far clouds again and again.

**Expectation (hidden).** Each flicker is brief and lights only the distant clouds; the near shore stays dark; the flickers do not merge into steady light.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A lake at night with the horizon beyond it.
- S2 [core] Lightning flickers at the horizon, lighting the far clouds.
- S3 [core] The flickers repeat: the far clouds light up more than once.
- S4 [minor] The flickers are distant, at the horizon rather than overhead.
- S5 [minor] The near shore stays dark.

**PC**
- P1 [core · process_direction]
  - expect: Each flicker is brief with the clouds dark between; the flickers repeat but never merge into one steady light.
  - fail: The far clouds stay lit for the rest of the clip; or the glow brightens steadily; or the sky turns to daylight; or a flicker fades in slowly.
- P2 [core · permanence_count]
  - expect: The horizon, the far cloud bank and the shoreline are the same across lit and dark frames.
  - fail: The clouds change shape abruptly between one flicker and the next; or the shoreline shifts; or trees or buildings on the far shore appear or vanish; or a second horizon line appears.
- P3 [major · missing_consequence]
  - expect: The light stays far off: the far clouds brighten while the near shore, foreground trees and anything on the water near the viewer stay dark.
  - fail: The near shore and foreground light up as brightly as the far clouds; or the flash lights the foreground from the near side; or a bright reflection appears on the lake with no glow in the sky.
- P4 [major · causeless_motion]
  - expect: The lake surface moves only as slow ripples; trees and objects on the shore stay still; nothing moves at a flicker.
  - fail: The water heaves or jumps at a flicker; or trees sway sharply at the flicker with nothing else stirring; or objects on the shore shift at the flash.
- P5 [fatal · shape_identity]
  - expect: Land, water and cloud keep their identities: the lake stays water and the clouds stay cloud.
  - fail: The clouds turn into solid objects; or the lake turns into solid ground; or a bolt emerges from the lake; or the far shore morphs into a different landscape.
- P6 [minor · attribute_drift]
  - expect: The night colours of sky, water and shore are consistent before and after each flicker.
  - fail: The sky changes colour permanently after a flicker; or the water changes colour; or the shore changes colour.

## ELEC-0092 · lightning · train

**Caption.** A jagged lightning bolt descends from a cloud to a hilltop, branching as it comes down.

**Expectation (hidden).** The bolt runs from cloud to ground with side branches that end in the air, is brightest along the main channel, and is gone in a fraction of a second.

**Declared violation types.** gravity_direction, process_direction, shape_identity

**SA**
- S1 [core] A cloud above a hilltop.
- S2 [core] A lightning bolt descends from the cloud to the hilltop.
- S3 [core] The bolt is jagged.
- S4 [core] The bolt branches as it comes down.
- S5 [minor] The bolt reaches the hilltop, not the slope or the valley.

**PC**
- P1 [core · shape_identity]
  - expect: The bolt is a jagged line with one main channel from cloud to hilltop and side branches that leave the channel and end in the air; the main channel is brightest.
  - fail: The bolt is a perfectly straight beam; or a smooth wave; or a wide glowing tube; or every branch reaches the ground so that several equal bolts stand side by side; or branches join back into the channel to form loops.
- P2 [core · process_direction]
  - expect: The bolt appears and is gone within a moment, perhaps flickering; the hilltop and sky return to dark.
  - fail: The bolt stands as a steady lit line for the rest of the clip; or grows slowly from cloud to ground like a line being drawn; or retracts back up into the cloud; or the hilltop keeps glowing after the bolt is gone.
- P3 [major · missing_consequence]
  - expect: The flash lights the hill, the cloud's underside and the surrounding ground during the bolt, from the bolt's direction.
  - fail: The bolt is visible while the hill and cloud stay as dark as before; or the ground is lit while no bolt is present; or the lit area is far from the bolt while the hill under it stays dark.
- P4 [major · gravity_direction] (if: Rain or wind-blown items are visible.)
  - expect: Rain falls downward and blown items move with the storm and settle.
  - fail: Rain rises or hangs still; or leaves or debris climb steadily; or rain falls sideways while the trees stand still.
- P5 [fatal · permanence_count]
  - expect: The hill, the cloud and any trees or structures are the same before and after; the flash reveals what was there.
  - fail: Trees or structures appear or vanish between dark and lit frames; or the hill changes shape; or the bolt leaves a glowing pillar standing on the hilltop; or the bolt passes through the hill.
- P6 [minor · attribute_drift]
  - expect: The hill's colour, the cloud and the sky keep their colours apart from the flash.
  - fail: The hill changes colour rather than brightness; or the sky turns to daylight after the flash; or the cloud changes colour permanently.

**Note.** The data record declares gravity_direction; nothing about a bolt has a gravity direction, so it is covered only by the gated rain item. Consider replacing it with missing_consequence on the data record.

## ELEC-0093 · lightning · train

**Caption.** Lightning jumps between two clouds high over a plain, lighting both from inside, with no bolt reaching the ground.

**Expectation (hidden).** The flash is inside and between the clouds and brief; the ground below is lit only by the glow, and nothing on the ground is struck.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] Two clouds high over a plain.
- S2 [core] Lightning flashes between the clouds, lighting both from inside.
- S3 [core] No bolt reaches the ground.
- S4 [minor] The plain below is flat open land.
- S5 [minor] The two clouds are separate, with the flash spanning the gap or lighting both.

**PC**
- P1 [core · process_direction]
  - expect: The flash is brief; both clouds return to dark; flashes may repeat but each ends.
  - fail: The clouds stay lit for the rest of the clip; or the glow brightens steadily; or the sky turns to daylight; or the flash fades in slowly.
- P2 [core · permanence_count]
  - expect: The two clouds and the plain are the same across dark and lit frames: the same cloud shapes and the same ground features.
  - fail: A cloud appears or vanishes between frames; or the cloud shapes change abruptly at the flash; or features on the plain appear or vanish; or a third cloud appears already lit.
- P3 [major · missing_consequence]
  - expect: The light comes from within and between the clouds: their bodies and edges glow with their texture revealed, and the plain brightens only faintly as a glow from above.
  - fail: The plain lights up brightly while the clouds stay dark; or the glow is a flat wash over the frame with no cloud structure; or a spot on the ground lights up as if struck while no bolt reaches it.
- P4 [major · causeless_motion]
  - expect: The clouds drift only slowly; the plain and anything on it stay still through the flash.
  - fail: The clouds jump or swirl at the flash; or objects on the plain shift at the flash; or the horizon tilts at the flash.
- P5 [fatal · shape_identity]
  - expect: Clouds stay cloud and the plain stays ground; nothing on the ground is struck or changed.
  - fail: A cloud turns into a solid object; or a bolt strikes the plain and leaves a glowing mark; or the ground splits or heaves; or the plain turns into water or sky.
- P6 [minor · attribute_drift]
  - expect: The sky's night colour and the plain's colour are consistent before and after the flash.
  - fail: The sky changes colour permanently after the flash; or the plain changes colour; or the clouds change colour when not lit.

## ELEC-0094 · lightning · train

**Caption.** A dog lying in a hallway jumps up as a lightning flash lights the windows and the house shakes with thunder.

**Expectation (hidden).** The flash comes first and the dog reacts after; the light is gone almost immediately.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] A dog lies in a hallway.
- S2 [core] A lightning flash lights the windows.
- S3 [core] The dog jumps up.
- S4 [minor] A window or windows are in view in the hallway.
- S5 [minor] The flash comes first and the dog jumps after it.

**PC**
- P1 [core · process_direction]
  - expect: The flash is brief: the windows and the hallway brighten and return to their earlier light; flashes may repeat but each ends.
  - fail: The hallway stays bright to the end of the clip after the flash; or brightens steadily without ending; or the flash fades in slowly; or the windows stay lit while the hallway is dark again.
- P2 [core · missing_consequence]
  - expect: The light enters through the windows: the windows are the brightest part, the walls and floor near them brighten most, and shadows of the frames fall away from the windows during the flash.
  - fail: The hallway brightens evenly while the windows stay as they were; or the light comes from the far end of the hallway with the windows dark; or the window frames' shadows point toward the windows.
- P3 [major · causeless_motion]
  - expect: The flash moves nothing but the dog: furniture, pictures, doors and rugs stay put.
  - fail: Pictures, furniture or doors shift at the flash; or the rug slides; or the dog is lifted off the floor without its legs pushing.
- P4 [major · trajectory_momentum]
  - expect: The dog rises by pushing off with its legs and lands back on the floor, its body moving as one animal.
  - fail: The dog rises straight up and hangs in the air; or slides across the floor without its legs moving; or lands and slides on with nothing pushing it.
- P5 [fatal · shape_identity]
  - expect: One dog with the same body, legs and tail throughout; the hallway's walls, doors and windows keep their shape and nothing passes through anything.
  - fail: The dog gains or loses a leg or its head changes shape; or a second dog appears; or the dog passes through a wall or door; or a window changes shape or moves along the wall.
- P6 [minor · attribute_drift]
  - expect: The dog's coat colour, the wall colours and the pictures stay the same apart from brightness.
  - fail: The dog's coat changes colour or pattern; or the walls change colour; or pictures on the wall change.

**Note.** The dog is kept because its reaction is the caption's event; a dog starting to move is not causeless motion. Thunder is sound and the house 'shaking' is not judged.

## ELEC-0095 · lightning · train

**Caption.** Lightning strikes a dry hillside, and after the flash a small patch of grass smoulders and smokes.

**Expectation (hidden).** The smoke appears at the strike point after the flash and rises; the flash itself is instantaneous and the bolt does not remain.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A dry hillside.
- S2 [core] A lightning bolt strikes the hillside.
- S3 [core] After the flash a small patch of grass smoulders and smokes.
- S4 [minor] The smoking patch is at the point where the bolt struck.
- S5 [minor] The bolt and flash come first and the smoke follows.

**PC**
- P1 [core · process_direction]
  - expect: The bolt and flash are brief and gone; the smoke appears at the strike point only afterwards and grows from there; the bolt does not remain.
  - fail: The bolt stands as a steady lit line for the rest of the clip; or smoke rises from the patch before the bolt arrives; or the smoke shrinks back into the ground; or the patch glows like a lamp after the bolt is gone.
- P2 [core · permanence_count]
  - expect: The hillside, its grass, rocks and any trees are the same before and after the flash; the only new thing is smoke at the strike point.
  - fail: Rocks or trees appear or vanish between dark and lit frames; or the hill changes shape; or a second smoking patch appears where no bolt struck; or a burnt object appears at the strike point that was not there.
- P3 [major · gravity_direction]
  - expect: The smoke rises from the patch and drifts upward and away; anything thrown up by the strike falls back to the ground.
  - fail: The smoke sinks and flows down the slope like water; or hangs as a fixed shape; or soil or grass thrown up by the strike rises and stays aloft.
- P4 [major · shape_identity]
  - expect: The bolt is a jagged, branching bright line with a main channel from the sky to the strike point.
  - fail: The bolt is a perfectly straight beam; or a smooth wave; or a wide glowing tube; or a bolt that hangs in mid-air not reaching the hillside while the patch starts smoking.
- P5 [fatal · solidity]
  - expect: The ground stays ground: the bolt ends at the surface and does not pass through it, and the hillside stays whole.
  - fail: The bolt continues below the surface as a lit line under the ground; or the hillside splits open; or the strike point turns into a hole that swallows the grass; or the ground becomes transparent.
- P6 [minor · attribute_drift]
  - expect: The grass colour, the sky and the ground keep their colours apart from the flash and the scorched patch.
  - fail: The grass changes colour away from the strike point; or the sky turns to daylight after the flash; or the ground changes colour over the whole slope.

## ELEC-0096 · lightning · train

**Caption.** An airliner flying through a storm cloud is hit by lightning, and a flash runs along its wing before the plane flies on.

**Expectation (hidden).** The flash is brief and the plane continues on its course unchanged; the flash does not persist on the aircraft.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] An airliner flies through or beside a storm cloud.
- S2 [core] Lightning hits the plane.
- S3 [core] A flash runs along its wing.
- S4 [core] The plane flies on afterwards.
- S5 [minor] The flash is on the wing, not on the tail or nose alone.
- S6 [minor] The order is flying, flash, flying on.

**PC**
- P1 [core · process_direction]
  - expect: The flash is brief: it appears on the wing and is gone, and the wing returns to its unlit look; the plane carries on.
  - fail: The flash stays on the wing as a steady glow for the rest of the clip; or the wing keeps glowing after the bolt is gone; or the flash moves slowly along the wing like a light being drawn; or the flash returns to the same spot and lingers.
- P2 [core · permanence_count]
  - expect: The plane is the same before and after the strike: the same fuselage, wings, engines and tail, none appearing or vanishing.
  - fail: A wing or engine vanishes or duplicates; or the plane changes into a different aircraft; or a second plane appears at the flash; or part of the plane detaches and hangs in the air.
- P3 [major · trajectory_momentum]
  - expect: The plane keeps its heading and steady motion through the strike; the flash does not push it off course.
  - fail: The plane stops in mid-air at the flash; or jumps to a new position between dark and lit frames; or reverses direction; or is knocked sideways at the instant of the flash.
- P4 [major · shape_identity]
  - expect: The bolt, where seen, is a jagged bright line meeting the plane at a point; the plane keeps its rigid shape.
  - fail: The bolt is a straight beam or a smooth curve; or a wide glowing tube; or the wing bends or ripples at the strike; or the bolt wraps around the fuselage as a ring.
- P5 [fatal · solidity]
  - expect: The plane stays a solid body: the bolt meets its surface and does not pass through the cabin; nothing passes into or through the plane.
  - fail: The bolt passes through the fuselage and out the other side; or the cabin lights up from within as if the bolt were inside it; or the plane passes through a solid object; or the plane melts or splits apart.
- P6 [minor · attribute_drift]
  - expect: The plane's livery and the cloud's colour stay the same apart from the flash.
  - fail: The livery changes colour or markings; or the cloud changes colour permanently; or the plane's windows change pattern.

## ELEC-0097 · lightning · train

**Caption.** Lightning flashes over a park during heavy rain, and for an instant every falling raindrop is lit against the dark.

**Expectation (hidden).** The rain is visible as bright streaks only during the flash and falls downward; the scene is dark again right after.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] A park in heavy rain, dark.
- S2 [core] Lightning flashes over the park.
- S3 [core] For an instant the falling raindrops are lit against the dark.
- S4 [minor] The rain is heavy: many drops or streaks fill the frame.
- S5 [minor] The scene is dark again after the flash.

**PC**
- P1 [core · process_direction]
  - expect: The flash is brief: the rain and the park brighten and return to dark; flashes may repeat but each ends.
  - fail: The park stays lit for the rest of the clip after the flash; or the light brightens steadily; or the flash fades in slowly; or the sky turns to daylight.
- P2 [core · missing_consequence]
  - expect: During the flash the raindrops show as bright streaks or specks across the frame and the wet ground and leaves glint; between flashes they are dim.
  - fail: The sky flashes while the rain stays as dim as before; or the rain is lit brightly while the sky and ground stay dark; or the raindrops stay lit after the sky is dark; or the wet ground stays dull while the rain and sky are lit.
- P3 [major · gravity_direction]
  - expect: The rain falls downward, as streaks slanting at most with the wind, before, during and after the flash.
  - fail: The rain rises or hangs still; or the streaks change direction at the flash; or the drops slant one way while the trees bend the other; or rain falls upward from the ground.
- P4 [major · permanence_count]
  - expect: The trees, benches, paths and lamps of the park are the same across dark and lit frames.
  - fail: Trees or benches appear or vanish between dark and lit frames; or paths change route; or lamp posts move; or a person appears at the flash.
- P5 [fatal · shape_identity]
  - expect: Trees, benches and lamp posts keep their shapes; nothing passes through anything; any bolt seen ends in the air or at the ground, not inside a tree lit like a lamp.
  - fail: A tree changes shape or merges with another; or a bolt passes through a tree and lights its interior; or a bench morphs into another object; or the ground turns into open water.
- P6 [minor · attribute_drift]
  - expect: The park's colours are consistent before and after: the flash whitens the scene only briefly.
  - fail: The grass or trees change colour permanently after the flash; or the sky changes colour permanently; or the path changes colour.

## ELEC-0098 · lightning · train

**Caption.** A lightning bolt strikes a lone tree on a golf course, and the tree's trunk splits with a shower of splinters.

**Expectation (hidden).** The split happens at the flash and the splinters fall to the ground; the tree does not glow afterward and does not knit back together.

**Declared violation types.** process_direction, material_response

**SA**
- S1 [core] A lone tree on a golf course.
- S2 [core] A lightning bolt strikes the tree.
- S3 [core] The trunk splits.
- S4 [core] Splinters fly from the trunk.
- S5 [minor] The bolt ends at the tree, not beside it.
- S6 [minor] The bolt comes first, the split and splinters follow.

**PC**
- P1 [core · process_direction]
  - expect: The bolt and flash are brief; the split happens at the flash and remains; the trunk does not glow afterwards and the split does not close.
  - fail: The bolt stands as a steady lit line for the rest of the clip; or the trunk splits before the bolt arrives; or the split closes and the trunk knits back together; or the trunk glows like an ember for the rest of the clip; or splinters fly back into the trunk.
- P2 [core · material_response]
  - expect: The trunk splits as wood: it cracks along its length into fibrous pieces that stay stiff; pieces knocked off fly outward as solid fragments.
  - fail: The trunk bends or folds like rubber; or flows or melts at the strike; or the wood shatters into powder like glass; or the split edges stretch like taffy.
- P3 [major · gravity_direction]
  - expect: The splinters fly out from the trunk and fall to the ground, arcing downward; loose pieces come to rest on the grass.
  - fail: Splinters rise and hang in the air; or fall upward; or stop in mid-air; or drift sideways without dropping.
- P4 [major · missing_consequence]
  - expect: The flash lights the tree, the fairway and the cloud undersides during the bolt.
  - fail: The bolt is visible while the tree and fairway stay as dark as before; or the fairway lights up while no bolt is present; or the ground is lit far from the tree while the tree's surroundings stay dark.
- P5 [fatal · permanence_count]
  - expect: One tree, split or whole; the pieces that fly off come from the trunk; the course and its features are the same before and after.
  - fail: The tree vanishes or a second tree appears; or splinters appear in the air from nowhere; or the tree turns into a different object; or the bolt passes through the tree into the ground as a lit line.
- P6 [minor · attribute_drift]
  - expect: The grass, the sky and the tree's foliage keep their colours apart from the flash and the damage.
  - fail: The grass changes colour; or the sky turns to daylight after the flash; or the foliage changes colour rather than brightness.

## ELEC-0099 · lightning · train

**Caption.** A lightning flash lights a bedroom through the curtains, and the shadow of the window frame appears on the wall for an instant.

**Expectation (hidden).** The shadow appears only during the flash on the wall away from the window and disappears with it.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] A bedroom with a curtained window.
- S2 [core] A lightning flash lights the room through the curtains.
- S3 [core] The shadow of the window frame appears on the wall for an instant.
- S4 [minor] The room is dim before and after the flash.
- S5 [minor] The shadow appears with the flash, not before it.

**PC**
- P1 [core · process_direction]
  - expect: The flash is brief: the room brightens and returns to dim; the frame's shadow appears and vanishes with it.
  - fail: The room stays lit to the end of the clip after the flash; or the shadow stays on the wall after the room is dim again; or the flash fades in slowly; or the shadow appears before the room brightens.
- P2 [core · missing_consequence]
  - expect: The light comes through the window: the curtains glow brightest, the wall facing the window brightens most, and the frame's shadow lies on the wall away from the window with its bars matching the frame.
  - fail: The room brightens evenly while the curtains stay as they were; or the shadow lies on the window wall itself; or the shadow is a shape unrelated to the window frame; or the wall brightens while the curtains stay dark.
- P3 [major · causeless_motion]
  - expect: Nothing in the room moves at the flash: bed, curtains and objects stay as they were, apart from curtains stirring in a draught.
  - fail: The curtains fly up at the instant of the flash while nothing else stirs; or objects on the nightstand shift; or the bedding moves; or a door opens by itself.
- P4 [major · permanence_count]
  - expect: The room's contents are the same before, during and after the flash.
  - fail: Furniture or pictures appear or vanish between dim and lit frames; or the window moves along the wall; or a person appears in the bed; or the room's layout changes.
- P5 [fatal · shape_identity]
  - expect: Walls, window and furniture keep their shapes; nothing passes through anything; the shadow is a shadow, not an object.
  - fail: The window changes shape; or the shadow becomes a solid object or remains as a painted mark; or the bed or wardrobe changes shape; or an object passes through the wall.
- P6 [minor · attribute_drift]
  - expect: The curtain fabric, the wall colour and the bedding keep their colours apart from brightness.
  - fail: The curtains change colour or pattern; or the wall changes colour rather than brightness; or the bedding changes colour.

## ELEC-0100 · lightning · train

**Caption.** Lightning strikes a field of wind turbines, and one turbine's blade tip flashes brightly for an instant.

**Expectation (hidden).** The bolt ends at the highest point, the flash is brief, and the blades keep turning as before.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A field of wind turbines.
- S2 [core] Lightning strikes among the turbines.
- S3 [core] One turbine's blade tip flashes brightly for an instant.
- S4 [minor] The flash is at a blade tip, not on the tower or the ground.
- S5 [minor] The blades are turning.

**PC**
- P1 [core · process_direction]
  - expect: The bolt and the flash at the tip are brief and gone; the tip returns to its unlit look.
  - fail: The bolt stands as a steady lit line for the rest of the clip; or the blade tip keeps glowing after the bolt is gone; or the glow travels along the blade; or the flash fades in slowly.
- P2 [core · permanence_count]
  - expect: The turbines are the same before and after: the same towers, the same number of blades on each, in the same places.
  - fail: A turbine or blade vanishes or appears; or a blade detaches at the flash; or a turbine changes place between dark and lit frames; or a bolt hangs frozen in the air after the flash.
- P3 [major · trajectory_momentum]
  - expect: The struck turbine's blades keep turning as before, about the hub, in the same direction; the other turbines keep their rhythm.
  - fail: The blades stop dead at the flash; or reverse direction; or jump to a new angle between dark and lit frames; or a blade bends as it turns.
- P4 [major · missing_consequence]
  - expect: The flash lights the nearby towers, the ground and the cloud undersides during the bolt, from the bolt's direction.
  - fail: The bolt is visible while the towers and ground stay as dark as before; or the field lights up while no bolt is present; or the ground far off is lit while the struck turbine's surroundings stay dark.
- P5 [fatal · solidity]
  - expect: The bolt ends at the blade tip and does not pass through the blade or tower; the turbines stay solid.
  - fail: The bolt passes through the blade and continues; or the tower lights up from within like a lamp; or the bolt passes through a tower; or a blade passes through another blade or the tower.
- P6 [minor · attribute_drift]
  - expect: The turbines' colour, the ground and the sky keep their colours apart from the flash.
  - fail: A tower changes colour; or the sky turns to daylight after the flash; or the ground changes colour.

## ELEC-0101 · lightning · train

**Caption.** A bolt of lightning strikes the ground in a desert, and a puff of dust rises from the spot after the flash.

**Expectation (hidden).** The bolt comes down to the ground, the dust rises after the flash, and there is no glow left on the sand.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A desert landscape.
- S2 [core] A bolt of lightning strikes the ground.
- S3 [core] A puff of dust rises from the strike point after the flash.
- S4 [minor] The strike point is on open ground, not on a rock or plant.
- S5 [minor] The bolt and flash come first and the dust follows.

**PC**
- P1 [core · process_direction]
  - expect: The bolt and flash are brief and gone; the dust appears at the strike point only afterwards and spreads from there; no glow is left on the sand.
  - fail: The bolt stands as a steady lit line for the rest of the clip; or the dust rises before the bolt arrives; or the dust puff shrinks back into the ground; or the strike point glows like an ember afterwards.
- P2 [core · permanence_count]
  - expect: The desert and whatever is in it are the same before and after; the flash reveals what was there and the dust is the only new thing.
  - fail: Rocks or plants appear or vanish between dark and lit frames; or the dunes change shape; or an object appears at the strike point; or a second dust puff rises where no bolt struck.
- P3 [major · gravity_direction]
  - expect: The dust rises as a puff, billows upward and spreads, then thins; grains thrown up fall back to the sand.
  - fail: The dust flows along the ground like water and never rises; or hangs as a fixed shape; or grains rise steadily and stay aloft; or the puff moves as a solid ball.
- P4 [major · shape_identity]
  - expect: The bolt is a jagged, branching bright line with a main channel from the sky to the strike point.
  - fail: The bolt is a perfectly straight beam; or a smooth wave; or a wide glowing tube; or a bolt that hangs in mid-air not reaching the ground while the dust rises.
- P5 [fatal · solidity]
  - expect: The ground stays ground: the bolt ends at the surface and does not continue beneath it; the sand does not open.
  - fail: The bolt continues below the surface as a lit line under the sand; or the ground splits open; or a hole appears that swallows the sand; or the sand becomes transparent.
- P6 [minor · attribute_drift]
  - expect: The sand's colour, the sky and any distant features keep their colours apart from the flash.
  - fail: The sand changes colour; or the sky turns to daylight after the flash; or distant hills change shape or colour.

## ELEC-0102 · lightning · train

**Caption.** Lightning flashes behind a lighthouse on a stormy coast, and the lighthouse is silhouetted while its own beam keeps sweeping.

**Expectation (hidden).** The flash is instantaneous and does not interrupt the steady rotation of the lighthouse beam.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] A lighthouse on a stormy coast.
- S2 [core] Its beam sweeps.
- S3 [core] Lightning flashes behind the lighthouse.
- S4 [core] The lighthouse stands as a dark silhouette against the flash.
- S5 [minor] The beam keeps sweeping through and after the flash.

**PC**
- P1 [core · process_direction]
  - expect: The flash is brief: the sky behind the lighthouse brightens and returns to dark; flashes may repeat but each ends.
  - fail: The sky stays lit for the rest of the clip; or brightens steadily; or the flash fades in slowly; or the sky turns to daylight.
- P2 [core · missing_consequence]
  - expect: The light comes from behind the lighthouse: the sky beyond it brightens while its near face stays dark; its own beam keeps sweeping at the same steady pace through the flash.
  - fail: The near face of the lighthouse lights up while the sky behind stays dark; or the beam stops, jumps or reverses at the flash; or the beam goes out at the flash and returns afterwards; or the lighthouse glows brighter than the sky behind it.
- P3 [major · trajectory_momentum]
  - expect: The beam turns steadily about the lantern room in one direction, sweeping the sea and cloud.
  - fail: The beam sweeps in one direction and then the other; or turns about a point other than the lantern; or two beams sweep in opposite directions from one lantern; or the beam bends.
- P4 [major · permanence_count]
  - expect: The lighthouse, the rocks and the coastline are the same across dark and lit frames.
  - fail: The lighthouse changes place or a second one appears; or rocks appear or vanish between frames; or the coastline changes shape; or the lantern room vanishes.
- P5 [fatal · shape_identity]
  - expect: The lighthouse keeps its tower shape and stays solid; the flash does not pass through it or light it from within.
  - fail: The tower becomes transparent with the flash seen through it; or the tower bends or changes shape; or a bolt emerges from the tower; or the tower merges with the rocks.
- P6 [minor · attribute_drift]
  - expect: The tower's paint, the rocks and the sea keep their colours apart from the flash and the beam.
  - fail: The tower changes colour or stripe pattern; or the sea changes colour permanently; or the sky changes colour permanently after the flash.

## ELEC-0103 · lightning · train

**Caption.** Lightning flashes above a mountain hut in a snowstorm, and the falling snow is lit brightly for an instant.

**Expectation (hidden).** The snowflakes appear as bright specks during the flash and are dim again after; they keep falling.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] A mountain hut in falling snow.
- S2 [core] Lightning flashes above the hut.
- S3 [core] The falling snow is lit brightly for an instant.
- S4 [minor] Snow is falling before and after the flash.
- S5 [minor] The scene is dim again after the flash.

**PC**
- P1 [core · process_direction]
  - expect: The flash is brief: the snow and the hut brighten and return to dim; flashes may repeat but each ends.
  - fail: The scene stays lit for the rest of the clip after the flash; or brightens steadily; or the flash fades in slowly; or the sky turns to daylight.
- P2 [core · missing_consequence]
  - expect: During the flash the snowflakes show as bright specks or streaks across the frame and the snow on the ground and roof glints; between flashes they are dim.
  - fail: The sky flashes while the falling snow stays as dim as before; or the flakes are lit brightly while the sky and ground stay dark; or the flakes stay lit after the sky is dark; or the ground snow stays dull while the flakes and sky are lit.
- P3 [major · gravity_direction]
  - expect: The snow falls downward, drifting with the wind, before, during and after the flash.
  - fail: The flakes rise or hang still; or change direction at the flash; or fall upward from the ground; or stop falling at the flash and resume afterwards.
- P4 [major · permanence_count]
  - expect: The hut, the trees and the slope are the same across dark and lit frames.
  - fail: The hut changes place or a second hut appears; or trees appear or vanish between frames; or the slope changes shape; or a lit window appears in the hut that was dark before.
- P5 [fatal · shape_identity]
  - expect: The hut and trees keep their shapes; nothing passes through anything; any bolt seen ends in the air or at the ground, not inside the hut.
  - fail: The hut changes shape; or a bolt passes through the hut and lights its interior; or a tree morphs into another object; or the snow on the ground turns into water.
- P6 [minor · attribute_drift]
  - expect: The hut's wood, the snow and the sky keep their colours apart from the flash.
  - fail: The hut changes colour; or the snow changes colour permanently; or the sky changes colour permanently after the flash.

## ELEC-0104 · lightning · train

**Caption.** A lightning bolt forks into two branches before reaching the ground, both branches lighting up together.

**Expectation (hidden).** The branches share a single trunk from the cloud, appear simultaneously, and vanish together; they do not appear one after another.

**Declared violation types.** shape_identity, process_direction

**SA**
- S1 [core] A lightning bolt descends from the sky toward the ground.
- S2 [core] The bolt forks into two branches before reaching the ground.
- S3 [core] Both branches light up together.
- S4 [minor] The two branches share one trunk above the fork.
- S5 [minor] The branches appear at the same moment, not one after the other.

**PC**
- P1 [core · shape_identity]
  - expect: The bolt is a jagged bright line with a single trunk from the cloud that splits at one point into two jagged branches, each continuing downward.
  - fail: The bolt is a perfectly straight beam or a smooth curve; or a wide glowing tube; or the two branches have no trunk and start separately from the cloud; or the branches cross or rejoin below the fork; or a branch turns and climbs back upward.
- P2 [core · process_direction]
  - expect: The whole bolt, trunk and both branches, appears and vanishes together within a moment, perhaps flickering; the sky returns to dark.
  - fail: One branch appears after the other has vanished; or the bolt stands as a steady lit line for the rest of the clip; or the bolt grows slowly like a line being drawn; or one branch remains lit after the rest is gone.
- P3 [major · missing_consequence]
  - expect: The flash lights the ground beneath both branches and the cloud underside during the bolt.
  - fail: The bolt is visible while the ground and cloud stay as dark as before; or the ground is lit under one branch only while the other branch is as bright; or the ground lights up while no bolt is present.
- P4 [major · causeless_motion]
  - expect: The ground, trees and structures below stay still through the flash; only the light changes.
  - fail: Trees or structures shift at the flash; or the horizon tilts; or objects on the ground jump between dark and lit frames.
- P5 [fatal · permanence_count]
  - expect: The landscape below is the same before and after the flash; the flash reveals what was there.
  - fail: Trees or structures appear or vanish between dark and lit frames; or the landscape changes layout; or a bolt hangs frozen in the sky after the flash; or a glowing pillar stands where a branch struck.
- P6 [minor · attribute_drift]
  - expect: The sky's night colour and the ground's colour are consistent before and after the flash.
  - fail: The sky turns to daylight after the flash; or the ground changes colour; or the cloud changes colour permanently.

## ELEC-0105 · lightning · train

**Caption.** A distant lightning bolt strikes the sea far out from a cliff, so small in the distance that it is over before the eye can follow it.

**Expectation (hidden).** The bolt is a thin bright line from cloud to sea, gone at once; the sea around it is lit only briefly.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A cliff with the sea stretching out from it.
- S2 [core] A lightning bolt strikes the sea far out.
- S3 [core] The bolt is small and distant.
- S4 [minor] The bolt is brief: it is over almost as soon as it appears.
- S5 [minor] The bolt strikes the sea, not the cliff or the shore.

**PC**
- P1 [core · process_direction]
  - expect: The bolt and its flash are brief and gone; the sea around it is lit only during the flash and returns to dark.
  - fail: The bolt stands as a steady lit line for the rest of the clip; or the sea keeps glowing where it struck; or the bolt fades in slowly; or the sky stays lit after the bolt is gone.
- P2 [core · permanence_count]
  - expect: The cliff, the shore and the sea are the same across dark and lit frames; the flash reveals what was there.
  - fail: Boats or rocks appear or vanish between dark and lit frames; or the cliff changes shape; or a glowing pillar stands on the sea after the flash; or a second bolt hangs frozen in the sky.
- P3 [major · shape_identity]
  - expect: The bolt is a thin jagged line from cloud to sea, small with distance.
  - fail: The bolt is a perfectly straight beam; or a smooth curve; or a wide glowing tube out of scale with its distance; or a bolt that hangs in mid-air touching neither cloud nor sea.
- P4 [major · missing_consequence]
  - expect: The flash lights the far sea and the cloud undersides around the bolt during the strike; the cliff and near shore brighten less or not at all.
  - fail: The bolt is visible while the far sea and clouds stay as dark as before; or the near cliff lights up as brightly as the strike point; or the sea is lit while no bolt is present.
- P5 [fatal · solidity]
  - expect: The sea stays water and the cliff stays rock; nothing passes through either.
  - fail: The bolt continues below the sea surface as a lit line under the water; or the cliff becomes transparent; or the cliff face splits or moves; or the sea turns into solid ground.
- P6 [minor · attribute_drift]
  - expect: The sea, the cliff and the sky keep their colours apart from the flash.
  - fail: The sea changes colour permanently; or the cliff changes colour; or the sky turns to daylight after the flash.

## ELEC-0106 · lightning · train

**Caption.** The canvas of a pitched tent lights up from a lightning flash outside, then goes dark again.

**Expectation (hidden).** The canvas glows for a fraction of a second, brightest on the side toward the flash, and returns to dark.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] A pitched tent, its canvas in view.
- S2 [core] The canvas lights up from a flash outside.
- S3 [core] The canvas goes dark again.
- S4 [minor] The tent is dim before the flash.
- S5 [minor] The order is dim, lit, dark again.

**PC**
- P1 [core · process_direction]
  - expect: The glow on the canvas is brief: it appears and is gone, and the canvas returns to dim; flashes may repeat but each ends.
  - fail: The canvas stays lit for the rest of the clip after the flash; or brightens steadily; or the flash fades in slowly like a lantern being turned up; or the canvas glows on after the sky is dark.
- P2 [core · missing_consequence]
  - expect: The canvas is brightest on the side toward the flash and dimmer on the far side; the light shows through the fabric with the poles and seams as dark lines.
  - fail: The canvas lights evenly all round with no brighter side; or the side away from the lit sky is the brightest; or the canvas lights up while the sky around the tent stays dark; or the glow sits at one spot on the canvas like a lamp inside.
- P3 [major · causeless_motion]
  - expect: The tent and its surroundings stay still at the flash; the canvas may ripple in the wind but does not jump at the flash.
  - fail: The tent shifts or its poles move at the flash; or objects around the tent jump; or the canvas snaps taut or collapses at the instant of the flash.
- P4 [major · permanence_count]
  - expect: The tent, the ground and the surroundings are the same across dim and lit frames.
  - fail: Trees or objects around the tent appear or vanish between frames; or the tent changes place; or a second tent appears; or a figure appears inside the tent at the flash.
- P5 [fatal · shape_identity]
  - expect: The tent keeps its shape and the canvas stays cloth; nothing passes through it.
  - fail: The tent changes shape between frames; or the canvas becomes a solid wall or turns transparent like glass; or a bolt passes through the tent; or the tent merges with the ground.
- P6 [minor · attribute_drift]
  - expect: The canvas colour, the ground and the surroundings keep their colours apart from brightness.
  - fail: The canvas changes colour rather than brightness; or the ground changes colour; or the tent's pattern or logo changes.

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

## ELEC-0109 · spark · train

**Caption.** The plug of a running heater is yanked out of the wall socket, and a small spark snaps at the prongs as they come out.

**Expectation (hidden).** The spark is a brief flash at the socket at the instant of disconnection and is gone at once; the heater stops.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A heater runs with its plug in a wall socket.
- S2 [core] The plug is yanked out of the socket.
- S3 [core] A small spark snaps at the prongs as they come out.
- S4 [minor] The pull is quick: a yank rather than a slow withdrawal.
- S5 [minor] The spark comes as the plug leaves the socket, not before.

**PC**
- P1 [core · process_direction]
  - expect: The spark is a single brief flash at the socket at the instant the prongs part from it, and is gone; the heater's glow or fan stops after the plug is out.
  - fail: The spark glows on at the prongs after the plug is clear of the wall; or sparks appear while the plug is still seated and untouched; or a spark appears at the prongs while the plug lies loose on the floor; or the heater keeps running at full glow to the end of the clip with the plug out.
- P2 [core · permanence_count]
  - expect: One plug, one cord, one socket; the plug comes out whole and the socket stays on the wall; the spark leaves nothing behind.
  - fail: The plug vanishes or a second plug appears; or the socket comes off the wall or vanishes; or the cord splits or detaches; or a glowing dot stays on the wall where the spark was.
- P3 [major · gravity_direction]
  - expect: Any spark fragments fall from the socket toward the floor and go dark within a short distance.
  - fail: Sparks rise from the socket and gather above it; or hang in the air; or lie glowing on the floor for the rest of the clip.
- P4 [major · material_response]
  - expect: The cord follows the plug: it goes slack and drops once the plug is free and stays attached at both ends.
  - fail: The cord stretches like elastic during the yank; or stands rigid in the air after the plug is out; or the cord floats.
- P5 [fatal · solidity]
  - expect: The plug leaves the socket through its holes; the hand and plug pass through nothing; the heater keeps its shape.
  - fail: The plug passes out through the wall beside the socket; or fingers pass through the plug or the wall; or the heater changes shape; or the plug merges with the socket.
- P6 [minor · attribute_drift]
  - expect: The heater's colour, the socket's design and the wall stay the same.
  - fail: The heater changes colour; or the socket changes design or moves along the wall; or the cord changes colour.

**Note.** The heater's stopping is read from its visible glow or fan; how quickly it fades is not judged.

## ELEC-0110 · spark · train

**Caption.** The second jumper-cable clamp is touched to a car battery terminal, and a spark jumps at the contact.

**Expectation (hidden).** The spark appears exactly as the clamp meets the terminal and vanishes; there is no spark while the clamp is held away.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A car battery with jumper cables; one clamp is already attached.
- S2 [core] The second clamp is touched to a battery terminal.
- S3 [core] A spark jumps at the contact.
- S4 [minor] The clamp is a jumper-cable clamp: a sprung jaw on a thick cable.
- S5 [minor] The spark comes as the clamp meets the terminal, not before.

**PC**
- P1 [core · process_direction]
  - expect: The spark is a brief flash at the point where the clamp meets the terminal, and is gone; there is no spark while the clamp is held away.
  - fail: A spark appears while the clamp is still clear of the terminal; or the spark glows on at the contact for the rest of the clip; or sparks keep flashing while the clamp sits seated and untouched; or the spark appears somewhere other than where the clamp touches.
- P2 [core · permanence_count]
  - expect: Two clamps on one battery; the clamps, cables and terminals keep their number and stay whole; the spark leaves nothing behind.
  - fail: A third clamp appears or one vanishes; or a cable splits or detaches; or a terminal vanishes; or a glowing dot stays on the terminal after the spark.
- P3 [major · gravity_direction]
  - expect: Any spark fragments fall from the contact point toward the engine bay floor and go dark within a short distance.
  - fail: Sparks rise and gather above the battery; or hang in the air; or lie glowing on the engine parts for the rest of the clip.
- P4 [major · material_response]
  - expect: The clamp is a rigid jaw that grips the post; the cable hangs slack from the clamp.
  - fail: The clamp bends like rubber around the post; or hangs on the post with its jaws still wide open; or the cable stands rigid in the air or stretches like elastic.
- P5 [fatal · solidity]
  - expect: The clamp meets the outside of the terminal and stays outside the battery casing; nothing passes through anything.
  - fail: The clamp passes into the battery casing; or the cable passes through the bonnet or an engine part; or the battery changes shape; or a hand passes through the clamp.
- P6 [minor · attribute_drift]
  - expect: The cable colours, the battery's label and the engine bay stay the same.
  - fail: A cable changes colour; or the battery's label changes; or engine parts change shape or place.

## ELEC-0111 · spark · train

**Caption.** A tram passes under a wire on a wet night, and its pole throws off blue-white sparks where it rubs the wire.

**Expectation (hidden).** The sparks appear at the contact point and move along with the tram; they flash and die instantly and do not fall as burning drops.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A tram at night on a wet street.
- S2 [core] A pole on the tram's roof reaches up to an overhead wire.
- S3 [core] Sparks fly off where the pole rubs the wire.
- S4 [minor] The sparks are blue-white.
- S5 [minor] The street or the tram's surfaces look wet.

**PC**
- P1 [core · process_direction]
  - expect: Sparks appear only at the point where the pole touches the wire, travel along with the tram, and each flash is gone at once.
  - fail: Sparks appear at a point on the wire away from where the pole touches; or a flash stays lit at one spot on the wire after the tram has moved on; or sparks come from the pole while it is clear of the wire; or the whole wire glows.
- P2 [core · permanence_count]
  - expect: One tram, one pole, one wire; sparks leave nothing behind on the wire or the street.
  - fail: Glowing dots stay on the wire or the street after the tram passes; or a second pole appears; or the wire ends in mid-air; or the tram duplicates or changes shape.
- P3 [major · gravity_direction]
  - expect: Spark fragments fall from the contact point and go dark within a short distance; they do not reach the street as burning drops.
  - fail: Sparks rise and gather above the wire; or hang in the air; or fall to the street and lie there glowing like lamps.
- P4 [major · missing_consequence] (if: The wet street below the wire is in view.)
  - expect: The wet street and the tram's wet surfaces mirror each flash briefly below it.
  - fail: The sparks flash while the wet street below stays as dark as before; or a reflection lies on the street where no spark is above it; or the reflection stays lit after the spark is gone.
- P5 [fatal · solidity]
  - expect: The pole touches the underside of the wire and stays a rigid arm; the tram runs on its rails and passes through nothing.
  - fail: The pole passes through the wire; or the wire passes through the pole; or the tram passes through a vehicle, pole or building; or the pole detaches and floats.
- P6 [minor · attribute_drift]
  - expect: The tram's livery, the wire's route and the street stay the same.
  - fail: The tram changes colour; or the wire changes route between frames; or the street's markings change.

**Note.** The tram is a powered vehicle; its motion is not judged. Spark count and brightness are not judged.

## ELEC-0112 · spark · train

**Caption.** A moth flies into a hanging bug zapper on a porch, and there is a brief crackle and flash at the grid.

**Expectation (hidden).** The flash happens at the moment of contact and is over instantly; the grid is dark before and after.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A bug zapper hangs on a porch.
- S2 [core] A moth flies toward the zapper.
- S3 [core] The moth reaches the grid.
- S4 [core] A brief flash appears at the grid.
- S5 [minor] The flash comes as the moth meets the grid, not before.

**PC**
- P1 [core · process_direction]
  - expect: The flash is brief and at the point where the moth meets the grid; the grid is dark before and after.
  - fail: The grid flashes while the moth is still well clear of it; or the flash glows on for the rest of the clip; or the flash appears at a place on the grid away from the moth; or the grid flashes repeatedly with nothing touching it.
- P2 [core · permanence_count]
  - expect: One zapper and one moth; the zapper keeps its shape and place; the flash leaves nothing glowing behind.
  - fail: A second zapper or moth appears from nowhere; or the zapper vanishes; or a glowing spot stays on the grid after the flash; or the moth passes through the grid and flies on unchanged.
- P3 [major · gravity_direction] (if: The moth's fate after the flash is in view.)
  - expect: After the flash the moth drops or falls away from the grid; anything that falls goes downward.
  - fail: The moth rises from the grid after the flash and hangs in the air; or falls upward; or a fallen moth rises back to the grid.
- P4 [major · causeless_motion]
  - expect: The zapper hangs still or swings only gently; the porch furniture stays put.
  - fail: The zapper swings hard at the flash with nothing touching it; or jumps to a new spot; or porch furniture shifts at the flash.
- P5 [fatal · solidity]
  - expect: The zapper is a rigid cage that stays whole; the moth meets the grid from outside.
  - fail: The grid bends or melts; or the moth passes through the cage wall and out the other side unchanged; or the zapper's housing changes shape; or the hook detaches and the zapper hangs in the air.
- P6 [minor · attribute_drift]
  - expect: The zapper's colour and the porch's colours stay the same apart from the flash.
  - fail: The zapper changes colour; or the porch wall changes colour; or the zapper's glow changes colour when it is not flashing.

**Note.** The moth is an animal and its flight is not judged. The crackle is sound and is not judged.

## ELEC-0113 · spark · train

**Caption.** A downed power line lies in a wet street, and it sparks and jumps where its broken end touches the ground.

**Expectation (hidden).** Sparks flash at the contact point in bursts and the cable end twitches with each burst; the sparks do not travel down the street.

**Declared violation types.** process_direction, causeless_motion

**SA**
- S1 [core] A power line lies down in a wet street.
- S2 [core] Its broken end touches the ground.
- S3 [core] Sparks flash at the point of contact.
- S4 [core] The cable end jumps or twitches.
- S5 [minor] The street is wet.
- S6 [minor] The sparks and the jumps come in bursts rather than steadily.

**PC**
- P1 [core · process_direction]
  - expect: The sparks flash in bursts at the broken end where it meets the ground, each burst brief and gone; they stay at the contact point.
  - fail: The sparks travel down the street along the ground away from the cable end; or the cable's whole length glows; or a spark stays lit at one spot for the rest of the clip; or sparks appear from an intact part of the cable away from the broken end.
- P2 [core · causeless_motion]
  - expect: The cable end twitches or jumps with each burst and lies still between bursts; the rest of the cable moves only where dragged by the end.
  - fail: The cable end jumps while no spark is flashing and no burst has just ended; or the cable slithers along the street steadily like a snake; or the end jumps up and hangs in the air; or the cable moves away from the sparks while the sparks stay behind.
- P3 [major · gravity_direction]
  - expect: Spark fragments fly out and fall to the wet ground, going dark within a short distance; the cable end falls back after each jump.
  - fail: Sparks rise steadily and gather above the cable; or hang in the air; or lie glowing on the ground for the rest of the clip; or the cable end stays in the air after a jump.
- P4 [major · missing_consequence]
  - expect: The wet street mirrors each burst briefly around the contact point.
  - fail: The sparks flash while the wet street around them stays as dark as before; or a reflection lies far from the cable end; or the reflection stays lit after the burst is gone.
- P5 [fatal · permanence_count]
  - expect: One cable with one broken end; it stays a continuous cable and passes through nothing.
  - fail: The cable splits into more pieces; or a second broken end appears; or the cable passes into the street surface; or the cable vanishes.
- P6 [minor · attribute_drift]
  - expect: The cable's colour, the street markings and the surroundings stay the same.
  - fail: The cable changes colour or thickness; or the street markings change; or buildings or cars around change.

## ELEC-0114 · spark · train

**Caption.** A flint gas-lighter is clicked over a stove burner, and a spark jumps from its tip and the gas ignites.

**Expectation (hidden).** The spark is a brief flash at the tip; the flame appears right after it, not before; with no gas the spark alone does not stay lit.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] A stove burner.
- S2 [core] A flint gas-lighter is held over the burner and clicked.
- S3 [core] A spark jumps from the lighter's tip.
- S4 [core] The gas at the burner ignites.
- S5 [minor] The flame is on the burner, not on the lighter.
- S6 [minor] The click and spark come first and the flame follows.

**PC**
- P1 [core · process_direction]
  - expect: The spark is a brief flash at the lighter's tip at the click, and is gone; it does not stay lit.
  - fail: The spark glows on at the tip after the click; or a spark appears while the lighter is not being clicked; or the spark appears somewhere other than the tip; or the spark drifts away from the tip as a lit point.
- P2 [core · missing_consequence]
  - expect: The flame appears at the burner after the spark and spreads round the burner's ring; once lit it stays alight.
  - fail: The flame appears before the spark; or the spark comes and no flame appears though the click is repeated to the end of the clip; or the flame appears at a part of the stove away from the burner under the lighter; or the flame goes out by itself and relights.
- P3 [major · gravity_direction]
  - expect: The flame stands upward from the burner; any spark fragments fall.
  - fail: The flame hangs downward or streams sideways with nothing blowing it; or the flame detaches from the burner and floats; or sparks rise and hang in the air.
- P4 [major · material_response]
  - expect: The lighter is a rigid tool held over the burner; the burner and its grate stay hard and keep their shape.
  - fail: The lighter bends or droops; or the burner ring deforms as it lights; or the grate melts or sags.
- P5 [fatal · permanence_count]
  - expect: One lighter and one burner; the flame is at the burner alone; nothing appears, vanishes or passes through the stove.
  - fail: A second lighter appears; or the burner vanishes; or the lighter passes through the grate; or the flame appears at a second burner that was not lit.
- P6 [minor · attribute_drift]
  - expect: The stove top, the grate and the lighter keep their colours and the burner keeps its place.
  - fail: The stove changes colour; or the burner moves on the stove top; or the lighter changes colour or shape.

**Note.** The gas is invisible before ignition; a flame appearing after the spark is the caption's event and needs no visible gas.

## ELEC-0115 · spark · train

**Caption.** A knife is pressed against a spinning sharpening wheel, and a stream of sparks flies off the blade's edge.

**Expectation (hidden).** The sparks fly off tangent to the wheel's motion, arc downward, and go dark; they stop when the blade is lifted.

**Declared violation types.** trajectory_momentum, gravity_direction, permanence_count

**SA**
- S1 [core] A sharpening wheel spins.
- S2 [core] A knife is pressed against the wheel.
- S3 [core] A stream of sparks flies off the blade's edge.
- S4 [minor] The sparks come from where the blade meets the wheel.
- S5 [minor] Contact comes first and the sparks follow.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The sparks leave the contact point along the direction the wheel's rim is moving, in one stream, and curve downward as they fly.
  - fail: Sparks radiate equally in all directions from the contact; or the stream points opposite to the rim's motion; or the stream's direction jumps about while the knife and wheel are steady.
- P2 [core · gravity_direction]
  - expect: Sparks that fly far arc downward and go out; none rise or hover.
  - fail: Sparks rise steadily and gather above the wheel; or hang in the air; or lie on the bench glowing like lamps.
- P3 [major · process_direction]
  - expect: Sparks appear only while the blade is on the wheel and stop when it lifts off.
  - fail: Sparks stream while the blade is clear of the wheel; or continue after the knife has been withdrawn; or sparks flow back toward the wheel.
- P4 [major · permanence_count]
  - expect: Sparks are transient: each fades in flight and none accumulate; the knife and wheel keep their number.
  - fail: Sparks persist as fixed bright dots; or a glowing pile builds on the floor; or sparks appear from a point away from the contact; or a second knife appears.
- P5 [fatal · solidity]
  - expect: The blade's edge touches the wheel's surface and stays outside the wheel; knife and wheel keep their shape.
  - fail: The blade sinks into the wheel; or the wheel passes through the blade; or the blade bends like rubber; or the wheel changes shape while spinning.
- P6 [minor · attribute_drift]
  - expect: The knife's handle, the wheel's colour and the bench stay the same.
  - fail: The handle changes colour; or the wheel changes colour or size; or the bench contents rearrange.

## ELEC-0116 · spark · train

**Caption.** A frayed lamp cord is bumped, and a spark flashes at the bare spot and the lamp flickers.

**Expectation (hidden).** The spark is at the damaged spot only and is over instantly; the flicker coincides with the spark.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] A lamp is lit, its cord in view.
- S2 [core] The cord has a frayed or bare spot.
- S3 [core] The cord is bumped.
- S4 [core] A spark flashes at the bare spot.
- S5 [core] The lamp flickers.
- S6 [minor] The bump comes first; the spark and flicker follow.

**PC**
- P1 [core · process_direction]
  - expect: The spark is a brief flash at the bare spot at the moment of the bump, and is gone; it does not stay lit or spread along the cord.
  - fail: The spark glows on at the bare spot after the bump; or a spark appears while the cord lies untouched; or the spark appears at a part of the cord away from the bare spot; or the whole cord glows.
- P2 [core · missing_consequence]
  - expect: The lamp flickers at the same moment as the spark and then returns to steady light or goes out.
  - fail: The lamp flickers with no spark at the cord and no bump; or the spark flashes while the lamp stays perfectly steady; or the lamp flickers long before the bump; or the flicker continues to the end of the clip after a single bump.
- P3 [major · missing_consequence]
  - expect: The light the lamp casts on its surroundings dips and returns with the flicker.
  - fail: The bulb dims while the light on the table and wall stays constant; or the surroundings dim while the bulb stays steady.
- P4 [major · material_response]
  - expect: The cord is a limp flexible cord: it shifts where bumped and lies slack afterwards.
  - fail: The cord stands rigid in the air; or stretches like elastic; or springs about like a coil after the bump.
- P5 [fatal · permanence_count]
  - expect: One lamp with one cord; the cord stays continuous and the lamp stays where it is; nothing passes through anything.
  - fail: The cord splits into two at the bare spot; or the lamp vanishes or duplicates; or the bare spot moves along the cord; or a hand passes through the cord.
- P6 [minor · attribute_drift]
  - expect: The lampshade's colour, the cord's colour and the table stay the same apart from the light.
  - fail: The shade changes colour rather than brightness; or the cord changes colour; or the table's contents rearrange.

## ELEC-0117 · spark · train

**Caption.** Bumper cars race under a metal ceiling grid, and their poles throw small sparks where they scrape along it.

**Expectation (hidden).** The sparks appear at the pole tips and move with the cars; each flash is brief; there are no sparks from cars whose poles are not touching.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] Bumper cars drive on a floor under a metal ceiling grid.
- S2 [core] Poles rise from the cars to the grid.
- S3 [core] Small sparks fly where the poles scrape along the grid.
- S4 [minor] More than one car is driving.
- S5 [minor] The sparks are at the top of the poles, at the grid.

**PC**
- P1 [core · process_direction]
  - expect: Sparks appear only at the tips of poles that touch the grid and move with each car; each flash is brief and gone.
  - fail: Sparks appear at a point on the grid with no pole beneath; or a flash stays lit at one spot after the car has moved on; or sparks come from the pole's middle or from the car body; or the whole grid glows.
- P2 [core · permanence_count]
  - expect: Each car has one pole to the grid; sparks leave nothing behind on the grid.
  - fail: Glowing dots stay on the grid after a car passes; or a car has two poles or none while sparking; or a car appears or vanishes; or a pole detaches and stays in the air.
- P3 [major · gravity_direction]
  - expect: Spark fragments fall from the grid toward the floor and go dark within a short distance.
  - fail: Sparks rise above the grid and gather; or hang in the air; or lie glowing on the floor for the rest of the clip.
- P4 [major · material_response]
  - expect: Each pole is a rigid rod from car to grid, bending only slightly; the grid stays a fixed flat ceiling.
  - fail: A pole bends like rubber or curls; or the grid sags or ripples where a pole touches; or a pole stretches longer as the car moves.
- P5 [fatal · solidity]
  - expect: The poles touch the underside of the grid; cars pass through neither each other nor the walls.
  - fail: A pole passes up through the grid; or two cars merge as they bump; or a car passes through the barrier wall; or a car passes through another car.
- P6 [minor · attribute_drift]
  - expect: The cars' colours and numbers, the floor and the grid stay the same.
  - fail: A car changes colour or number; or the floor pattern changes; or the grid changes spacing.

**Note.** The cars are driven vehicles; their steering, speed and bumps are not judged.

## ELEC-0118 · spark · train

**Caption.** A subway train pulls out of a station, and a flash of sparks lights the tunnel where its shoe touches the rail.

**Expectation (hidden).** The flash is at track level beside the train, brief, and lights the tunnel walls for an instant; it does not remain.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A subway train in a station.
- S2 [core] The train pulls out.
- S3 [core] A flash of sparks appears at track level beside the train.
- S4 [core] The flash lights the tunnel or platform for an instant.
- S5 [minor] The flash is low down, where the train meets the rail, not on the roof.

**PC**
- P1 [core · process_direction]
  - expect: The flash is brief and at track level where the train's shoe meets the rail; the light it throws on the tunnel walls comes and goes with it.
  - fail: The flash stays lit at one spot for the rest of the clip; or the tunnel walls stay lit after the flash is gone; or sparks appear at track level with the train standing still and nothing moving; or the sparks appear on the train's roof or windows.
- P2 [core · permanence_count]
  - expect: One train, one track; the flash leaves nothing behind on the rail or platform.
  - fail: Glowing dots stay on the rail or the platform after the flash; or a second train appears; or a carriage vanishes; or the rail ends in mid-air.
- P3 [major · gravity_direction]
  - expect: Spark fragments fall to the track bed and go dark within a short distance.
  - fail: Sparks rise and gather above the train; or hang in the air; or lie glowing on the platform for the rest of the clip.
- P4 [major · missing_consequence]
  - expect: The flash lights its surroundings: the tunnel wall, the platform edge and the train's side near the flash brighten during it, from the flash's direction.
  - fail: The sparks are visible while the tunnel wall beside them stays as dark as before; or the far end of the platform lights up while the wall beside the flash stays dark; or the tunnel lights up while no spark is present.
- P5 [fatal · solidity]
  - expect: The train stays on its rails and passes through nothing; the platform and tunnel keep their shape.
  - fail: The train passes through the platform edge or a pillar; or the carriages merge or split; or the tunnel wall changes shape; or the train sinks into the track bed.
- P6 [minor · attribute_drift]
  - expect: The train's livery, the platform's signs and the tunnel stay the same apart from the flash.
  - fail: The train changes colour; or the signs change lettering; or the tunnel changes colour permanently.

**Note.** The train is a powered vehicle; its acceleration is not judged.

## ELEC-0119 · spark · train

**Caption.** An overloaded power drill is run hard, and small sparks flicker through the vents on its motor housing.

**Expectation (hidden).** The sparks are visible only inside the vents while the motor runs and stop when the trigger is released.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A power drill is running.
- S2 [core] The drill is run hard: it is pressed into work or held under load.
- S3 [core] Small sparks flicker through the vents on its motor housing.
- S4 [minor] The sparks are inside the housing, seen through the vent slots.
- S5 [minor] The sparks flicker while the drill runs.

**PC**
- P1 [core · process_direction]
  - expect: The sparks are visible only inside the vents while the motor runs, flickering; they stop when the trigger is released and the motor winds down.
  - fail: Sparks keep flickering in the vents after the trigger is released and the chuck has stopped; or sparks come out of the housing and fly across the room; or the vents glow steadily like a lamp; or sparks appear at the chuck rather than the vents.
- P2 [core · permanence_count]
  - expect: One drill with its vents in fixed places; the sparks leave nothing behind.
  - fail: Glowing dots stay on the housing after the motor stops; or the vents change number or place; or a second drill appears; or the drill vanishes.
- P3 [major · gravity_direction] (if: Sparks are seen leaving the vents.)
  - expect: Any spark fragment that escapes the vents falls and goes dark within a short distance.
  - fail: Escaping sparks rise and gather above the drill; or hang in the air; or lie glowing on the bench for the rest of the clip.
- P4 [major · trajectory_momentum]
  - expect: The chuck and bit spin about the drill's axis while the trigger is held; the drill body is held steady.
  - fail: The bit wobbles off its axis or bends while turning; or the chuck turns while the bit stays still; or the whole drill body spins with the bit.
- P5 [fatal · solidity]
  - expect: The drill keeps its shape; the housing stays whole and the bit passes only into the work.
  - fail: The housing melts or bulges; or the bit passes through the work and the bench beneath as if through air; or the drill changes shape; or a hand passes through the drill.
- P6 [minor · attribute_drift]
  - expect: The drill's colour and markings and the bench stay the same.
  - fail: The drill changes colour; or its markings change; or items on the bench rearrange.

## ELEC-0120 · spark · train

**Caption.** A striker is scraped down a ferro rod held over a pile of tinder, and sparks spray onto the tinder below.

**Expectation (hidden).** The sparks fly in the direction of the stroke and fall downward onto the tinder, going dark on the way or as they land.

**Declared violation types.** gravity_direction, trajectory_momentum, permanence_count

**SA**
- S1 [core] A ferro rod is held over a pile of tinder.
- S2 [core] A striker is scraped down the rod.
- S3 [core] Sparks spray from the rod onto the tinder below.
- S4 [minor] The rod is above the tinder, so the sparks travel downward to it.
- S5 [minor] The scrape comes first and the sparks follow.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The sparks leave the rod in the direction of the stroke, in a spray, and continue downward toward the tinder.
  - fail: Sparks fly back up the rod against the stroke; or spray equally in all directions; or leave the rod sideways away from the tinder while the stroke points down at it.
- P2 [core · gravity_direction]
  - expect: The sparks fall onto the tinder below, arcing downward, and go dark on the way or as they land.
  - fail: Sparks rise above the rod and gather; or hang in the air; or drift sideways without dropping; or bounce back up from the tinder and climb.
- P3 [major · process_direction]
  - expect: Sparks appear only during the stroke, while the striker is moving along the rod, and stop when it stops.
  - fail: Sparks stream from the rod while the striker is held still on it; or continue after the striker has left the rod; or sparks flow back into the rod.
- P4 [major · permanence_count]
  - expect: Sparks are transient: each fades within a short flight and none accumulate as lasting lights; the rod and striker keep their number.
  - fail: Sparks persist as fixed bright dots on the tinder for the rest of the clip; or a glowing pile builds without any flame; or sparks appear from a point away from the rod; or a second rod appears.
- P5 [fatal · solidity]
  - expect: The striker scrapes along the rod's surface; rod, striker and hands stay whole and pass through nothing.
  - fail: The striker passes through the rod; or the rod passes through the hand; or the tinder pile turns into a solid block; or the rod vanishes.
- P6 [minor · attribute_drift]
  - expect: The rod's colour and length, the tinder and the ground stay the same.
  - fail: The rod changes colour or length; or the tinder changes colour before any glow; or the ground changes.

**Note.** Whether the tinder catches is not judged; a glow or flame appearing where sparks landed is not a violation.

## ELEC-0121 · spark · train

**Caption.** The blade of a chop saw comes down on a steel bar clamped in its jaws, and a long plume of sparks shoots out behind the blade and rains onto the floor.

**Expectation (hidden).** The plume points away from the direction of cut, the sparks arc down, and they fade before or as they hit the floor.

**Declared violation types.** trajectory_momentum, gravity_direction, permanence_count

**SA**
- S1 [core] A chop saw with a steel bar clamped in its jaws.
- S2 [core] The blade comes down onto the bar.
- S3 [core] A long plume of sparks shoots out behind the blade.
- S4 [core] The sparks rain down onto the floor.
- S5 [minor] The plume points away from the cut, behind the blade.
- S6 [minor] The blade meets the bar first and the plume follows.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The plume leaves the cut along the direction the blade's rim is moving, away from the operator's side, as one long stream that curves downward.
  - fail: The plume points into the blade against the rim's motion; or sparks radiate equally in all directions; or the plume's direction jumps about while the saw is steady.
- P2 [core · gravity_direction]
  - expect: The sparks arc downward and fade before or as they reach the floor.
  - fail: Sparks rise steadily and gather above the saw; or hang in the air; or lie on the floor glowing like lamps for the rest of the clip; or the plume climbs without arcing down.
- P3 [major · process_direction]
  - expect: Sparks appear only while the blade is in the bar and stop when it lifts clear.
  - fail: Sparks stream while the blade is above the bar; or continue after the blade has lifted; or sparks flow back into the cut.
- P4 [major · permanence_count]
  - expect: Sparks are transient: each fades in flight and none accumulate; the saw and bar keep their number.
  - fail: Sparks persist as fixed bright dots; or a glowing pile builds on the floor; or sparks appear from a point away from the cut; or a second blade appears.
- P5 [fatal · solidity]
  - expect: The blade cuts into the bar along a narrow line; the bar stays clamped and the saw keeps its shape.
  - fail: The blade passes through the bar leaving it whole; or the bar passes through the jaws; or the blade bends like rubber; or the saw changes shape.
- P6 [minor · attribute_drift]
  - expect: The saw's colour, the bar and the floor stay the same apart from the cut and any scorch marks.
  - fail: The saw changes colour; or the bar changes length or thickness away from the cut; or the floor pattern changes.

## ELEC-0122 · spark · train

**Caption.** A bad connection in a fuse box sparks and pops, and the lights in the house go out.

**Expectation (hidden).** The spark is brief and at the box; the lights go out immediately after; they do not come back on by themselves.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] A fuse box with its lid open or its connections in view.
- S2 [core] A connection in the box sparks.
- S3 [core] The lights in the house go out.
- S4 [minor] The lights are lit before the spark.
- S5 [minor] The spark comes first and the lights go out after.

**PC**
- P1 [core · process_direction]
  - expect: The spark is a brief flash at one connection in the box, and is gone; it does not stay lit or spread across the box.
  - fail: The spark glows on at the connection for the rest of the clip; or several connections flash one after another; or the whole box glows; or a spark appears again after the lights are already out.
- P2 [core · missing_consequence]
  - expect: The lights go out at the spark and stay out; they do not come back on by themselves.
  - fail: The spark flashes and the lights stay lit to the end of the clip; or the lights go out before the spark; or the lights come back on by themselves; or the lights flicker on and off repeatedly.
- P3 [major · missing_consequence]
  - expect: The light the lamps cast disappears with them: the room around the box goes dim and whatever remains lit is daylight or the spark.
  - fail: A lamp goes dark while its light on the walls stays; or the room stays as bright with every lamp dark; or a lamp elsewhere brightens as the others go out.
- P4 [major · gravity_direction]
  - expect: Any spark fragments fall from the box and go dark within a short distance; any smoke rises.
  - fail: Sparks rise from the box and gather above it; or hang in the air; or smoke sinks from the box and pools on the floor.
- P5 [fatal · permanence_count]
  - expect: One fuse box on the wall; its parts stay in place; nothing appears, vanishes or passes through the wall.
  - fail: The box vanishes or a second box appears; or fuses or wires appear or vanish; or the box sinks into the wall; or the box changes shape.
- P6 [minor · attribute_drift]
  - expect: The box's colour and labels and the wall stay the same apart from the light.
  - fail: The box changes colour; or the labels change; or the wall changes colour rather than brightness.

**Note.** The pop is sound and is not judged.

## ELEC-0123 · spark · train

**Caption.** A power hammer in a forge pounds a red-hot steel bar, and tiny sparks fly off with each blow.

**Expectation (hidden).** Sparks appear only at the moment of each strike, scatter outward from the impact, and go dark as they fall.

**Declared violation types.** trajectory_momentum, gravity_direction, permanence_count

**SA**
- S1 [core] A power hammer in a forge.
- S2 [core] A red-hot steel bar is under the hammer.
- S3 [core] The hammer pounds the bar with repeated blows.
- S4 [core] Tiny sparks fly off with each blow.
- S5 [minor] The bar glows red or orange.
- S6 [minor] Each blow comes first and its sparks follow.

**PC**
- P1 [core · trajectory_momentum]
  - expect: At each blow the sparks scatter outward from the point of impact, away from the hammer face, and curve downward as they fly.
  - fail: Sparks fly upward into the hammer's face; or move toward the impact point instead of away; or the scatter direction jumps about while the hammer and bar are steady.
- P2 [core · gravity_direction]
  - expect: The sparks arc downward and go dark as they fall; none rise or hover.
  - fail: Sparks rise steadily and gather above the hammer; or hang in the air; or lie on the anvil or floor glowing like lamps for the rest of the clip.
- P3 [major · process_direction]
  - expect: Sparks appear only at the moment of each strike and are gone before the next; between blows none fly.
  - fail: Sparks stream from the bar while the hammer is raised and not in contact; or continue after the hammer has stopped; or sparks flow back into the bar.
- P4 [major · permanence_count]
  - expect: Sparks are transient: each fades in flight and none accumulate; the bar and hammer keep their number.
  - fail: Sparks persist as fixed bright dots; or a glowing pile builds on the floor; or sparks appear from a point away from the impact; or a second bar appears under the hammer.
- P5 [fatal · solidity]
  - expect: The hammer strikes the bar's surface and squashes it; it does not pass through the bar or the anvil; the bar stays one piece.
  - fail: The hammer passes through the bar leaving it unchanged; or the bar passes into the anvil; or the bar splits into pieces with no cut; or the hammer changes shape.
- P6 [minor · attribute_drift]
  - expect: The hammer's colour, the anvil and the forge behind stay the same; the bar's glow changes only in brightness.
  - fail: The hammer changes colour; or the forge background rearranges; or the bar's glow changes colour from red toward blue or green.

**Note.** The bar flattening under the hammer is the expected material response; how much it deforms is not judged.

## ELEC-0124 · spark · train

**Caption.** A metal rake is dragged along a concrete path in the dark, and faint sparks flick from the tines.

**Expectation (hidden).** The sparks appear where the metal scrapes the concrete and stop when the rake is lifted; they die instantly.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A concrete path in the dark.
- S2 [core] A metal rake is dragged along the path.
- S3 [core] Faint sparks flick from the tines.
- S4 [minor] The sparks are at the tines, where the metal meets the concrete.
- S5 [minor] The drag comes first and the sparks follow.

**PC**
- P1 [core · process_direction]
  - expect: Sparks appear only where the tines scrape the concrete and only while the rake is moving; each flick is brief and gone; they stop when the rake lifts.
  - fail: Sparks appear while the rake is lifted clear of the path; or continue after the rake has stopped; or a spark stays lit at one spot for the rest of the clip; or sparks come from the handle or the rake's back.
- P2 [core · permanence_count]
  - expect: One rake with its tines; the sparks leave nothing behind on the path.
  - fail: Glowing dots stay on the path after the rake has passed; or tines appear or vanish; or a second rake appears; or the rake vanishes.
- P3 [major · trajectory_momentum]
  - expect: The sparks flick out behind the tines, along the direction of the drag, and drop to the path.
  - fail: Sparks fly ahead of the tines against the drag; or radiate equally in all directions; or climb steadily and stay aloft.
- P4 [major · material_response]
  - expect: The rake is a rigid tool: the tines bend only slightly as they scrape and the handle stays straight.
  - fail: The tines bend back like rubber and stay bent; or the handle bows or wobbles like a rope; or the concrete grooves or ripples under the tines.
- P5 [fatal · solidity]
  - expect: The tines scrape the path's surface and stay above it; the rake passes through nothing.
  - fail: The tines sink through the concrete; or the rake passes through a wall, kerb or plant; or the rake merges with the path; or the path surface opens.
- P6 [minor · attribute_drift]
  - expect: The rake's colour, the path's surface and the surroundings stay the same.
  - fail: The rake changes colour; or the path changes texture; or the surroundings rearrange.

**Note.** Who or what drags the rake is not judged.

## ELEC-0125 · spark · train

**Caption.** A live wire brushes against a metal bracket, and a bright spark flashes and leaves a black mark.

**Expectation (hidden).** The flash is instantaneous at the contact point and the dark mark remains afterwards; the wire does not keep glowing.

**Declared violation types.** process_direction, attribute_drift

**SA**
- S1 [core] A wire and a metal bracket.
- S2 [core] The wire brushes against the bracket.
- S3 [core] A bright spark flashes at the contact.
- S4 [core] A black mark is left on the metal where the spark was.
- S5 [minor] The wire touches the bracket first and the spark follows.

**PC**
- P1 [core · process_direction]
  - expect: The spark is a brief flash at the point where the wire meets the bracket, and is gone; neither wire nor bracket glows afterwards.
  - fail: The wire glows on after the flash; or the spark stays lit at the contact for the rest of the clip; or a spark appears while the wire is clear of the bracket; or the flash appears at a place away from where the wire touches.
- P2 [core · attribute_drift]
  - expect: The black mark appears at the contact point at the flash and stays there, unchanged, for the rest of the clip.
  - fail: The mark appears before the spark; or fades away or vanishes after appearing; or appears at a place away from the contact; or spreads over the bracket after the flash.
- P3 [major · gravity_direction]
  - expect: Any spark fragments fall from the contact point and go dark within a short distance; any smoke rises.
  - fail: Sparks rise and gather above the bracket; or hang in the air; or lie glowing below for the rest of the clip; or smoke sinks and pools.
- P4 [major · material_response]
  - expect: The wire is flexible and bends where it brushes; the bracket is rigid and keeps its shape.
  - fail: The wire stands rigid like a rod and stays where it is pushed; or the bracket bends like rubber where the wire touches; or the bracket melts or drips at the spark.
- P5 [fatal · solidity]
  - expect: The wire touches the bracket's surface and stays outside it; nothing passes through anything and nothing vanishes.
  - fail: The wire passes into or through the bracket; or the bracket vanishes; or a second wire appears; or the wire's end detaches and floats.
- P6 [minor · attribute_drift]
  - expect: The wire's insulation colour, the bracket's finish away from the mark and the background stay the same.
  - fail: The insulation changes colour; or the bracket changes colour away from the mark; or the background rearranges.

## ELEC-0126 · spark · train

**Caption.** A motorcycle leaning hard through a turn scrapes its metal footpeg along the track, and sparks trail out behind it.

**Expectation (hidden).** The sparks stream backward from the point of contact and die out along the track; they stop when the peg lifts off the track.

**Declared violation types.** trajectory_momentum, permanence_count

**SA**
- S1 [core] A motorcycle leans hard through a turn on a track.
- S2 [core] Its metal footpeg scrapes along the track surface.
- S3 [core] Sparks trail out behind the motorcycle.
- S4 [minor] The sparks come from the peg's contact with the track.
- S5 [minor] The scrape comes first and the sparks trail after.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The sparks stream backward from the contact point along the track, opposite to the motorcycle's motion, low over the surface, and die out along the way.
  - fail: Sparks fly ahead of the motorcycle; or spray equally in all directions from the peg; or the trail lies off to one side while the machine runs straight on; or the trail moves along with the bike as a fixed cloud.
- P2 [core · permanence_count]
  - expect: Sparks are transient: each fades within a short distance and none remain on the track; one motorcycle with one rider and its footpegs.
  - fail: Glowing dots stay on the track behind the bike for the rest of the clip; or a glowing line remains along the track; or the footpeg vanishes or duplicates; or a second motorcycle appears from nowhere.
- P3 [major · process_direction]
  - expect: Sparks appear only while the peg touches the track and stop when the machine straightens and the peg lifts.
  - fail: Sparks continue after the bike has straightened and the peg is clear of the track; or sparks trail from a peg that is high off the track; or sparks flow back to the peg.
- P4 [major · gravity_direction]
  - expect: Sparks that lift off the track arc back down and go dark; none rise or hover.
  - fail: Sparks rise steadily and gather above the track; or hang in the air; or climb along the bike's side.
- P5 [fatal · solidity]
  - expect: The peg scrapes the track's surface; the motorcycle and rider stay whole and pass through nothing.
  - fail: The peg or the wheel sinks into the track; or the bike passes through a barrier or kerb; or the bike and rider merge or change shape; or a wheel detaches.
- P6 [minor · attribute_drift]
  - expect: The bike's livery, the rider's gear and the track markings stay the same.
  - fail: The bike changes colour; or the rider's suit changes colour; or the track's lines change.

**Note.** The rider is kept because leaning the machine is what brings the peg to the track; riding technique is not judged.

## ELEC-0127 · spark · train

**Caption.** A phone charger is plugged into a worn socket, and a small spark flashes at the plug as it goes in.

**Expectation (hidden).** The spark is a single brief flash at the moment of contact; the charger then works normally.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A phone charger with its plug, and a wall socket.
- S2 [core] The plug is pushed into the socket.
- S3 [core] A small spark flashes at the plug as it goes in.
- S4 [minor] The socket looks worn: scuffed, loose or discoloured.
- S5 [minor] The spark comes as the prongs enter, not before.

**PC**
- P1 [core · process_direction]
  - expect: The spark is a single brief flash at the socket as the prongs make contact, and is gone; nothing glows afterwards.
  - fail: The spark glows on at the socket after the plug is seated; or sparks appear while the plug is still held away from the wall; or sparks keep flashing with the plug seated and untouched; or the flash appears on the cord or the charger body.
- P2 [core · permanence_count]
  - expect: One plug, one cord, one socket; the plug goes in whole and the spark leaves nothing behind.
  - fail: The plug vanishes or a second plug appears; or the socket vanishes or moves along the wall; or a glowing dot stays on the socket after the flash; or the cord splits.
- P3 [major · gravity_direction]
  - expect: Any spark fragments fall from the socket and go dark within a short distance.
  - fail: Sparks rise from the socket and gather above it; or hang in the air; or lie glowing on the floor for the rest of the clip.
- P4 [major · missing_consequence] (if: The charger has an indicator light in view.)
  - expect: Once seated, the charger works: its indicator light, if it has one, comes on and stays on.
  - fail: The charger's indicator light comes on while the plug is still clear of the wall; or the indicator flickers on and off with the plug seated and untouched; or the indicator lights and then goes dark for the rest of the clip while the plug stays in.
- P5 [fatal · solidity]
  - expect: The prongs enter the socket's holes; the plug and hand pass through nothing; the charger keeps its shape.
  - fail: The plug passes into the wall beside the socket; or fingers pass through the plug or the wall; or the charger changes shape; or the plug merges with the socket.
- P6 [minor · attribute_drift]
  - expect: The charger's colour, the cord and the wall stay the same.
  - fail: The charger changes colour; or the cord changes colour or thickness; or the wall changes colour.

## ELEC-0128 · spark · train

**Caption.** A locomotive brakes hard into a station, and sparks fly from its wheels where the brakes grip.

**Expectation (hidden).** The sparks appear at the wheels only while braking and stream backward and down; they stop as the train stops.

**Declared violation types.** trajectory_momentum, permanence_count

**SA**
- S1 [core] A locomotive approaches a station.
- S2 [core] It brakes hard: it slows sharply.
- S3 [core] Sparks fly from its wheels.
- S4 [minor] The sparks come from the wheels, at rail level, not from the roof or body.
- S5 [minor] The braking comes first and the sparks follow.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The sparks stream backward and downward from the wheels, opposite to the train's motion, along the rails.
  - fail: Sparks fly forward ahead of the wheels; or spray upward past the windows; or radiate equally in all directions; or the spark trail moves ahead of the train.
- P2 [core · permanence_count]
  - expect: Sparks are transient and leave nothing on the rails; the locomotive keeps its wheels and shape.
  - fail: Glowing dots stay on the rails behind the train; or a glowing line remains along the track; or a wheel vanishes or appears; or a second locomotive appears.
- P3 [major · process_direction]
  - expect: Sparks appear only while the train is braking and moving; they stop as it comes to rest.
  - fail: Sparks keep flying from the wheels after the train has stopped; or sparks fly while the train coasts with no slowing; or sparks flow back into the wheels.
- P4 [major · gravity_direction]
  - expect: Sparks that leave the wheels arc down to the track bed and go dark within a short distance.
  - fail: Sparks rise steadily and gather above the train; or hang in the air; or lie glowing on the platform for the rest of the clip.
- P5 [fatal · solidity]
  - expect: The locomotive stays on the rails and passes through nothing; the wheels turn on the rails.
  - fail: The locomotive passes through the platform or a buffer; or the wheels sink into the track bed; or carriages merge or split; or the locomotive changes shape.
- P6 [minor · attribute_drift]
  - expect: The locomotive's livery, the platform's signs and the rails stay the same.
  - fail: The livery changes colour; or the number on the locomotive changes; or the signs change lettering.

**Note.** The train is a powered vehicle; how fast it slows is not judged.

## ELEC-0129 · spark · train

**Caption.** A CNC plasma cutter slices a steel sheet, and a fountain of sparks pours from the underside of the cut.

**Expectation (hidden).** The sparks fall away beneath the sheet along the line of the cut, fading as they drop; they stop when the torch stops.

**Declared violation types.** gravity_direction, trajectory_momentum, permanence_count

**SA**
- S1 [core] A CNC plasma cutter over a steel sheet.
- S2 [core] The torch cuts the sheet: a bright point moves along it.
- S3 [core] A fountain of sparks pours from the underside of the cut.
- S4 [minor] The sparks come from below the sheet, under the torch.
- S5 [minor] The torch's cut comes first and the sparks follow it.

**PC**
- P1 [core · gravity_direction]
  - expect: The sparks pour downward from the underside of the sheet, spreading as they fall, and fade as they drop.
  - fail: Sparks rise from the underside and gather above the sheet; or hang in the air beneath it; or lie on the floor glowing like lamps for the rest of the clip; or the fountain climbs without arcing down.
- P2 [core · trajectory_momentum]
  - expect: The spark fountain stays beneath the torch and moves along with it, following the line of the cut.
  - fail: The fountain lags far behind the torch or runs ahead of it; or sparks pour from a part of the sheet away from the cut; or the fountain stays fixed while the torch moves on.
- P3 [major · process_direction]
  - expect: Sparks appear only while the torch is cutting and stop when the torch stops or lifts.
  - fail: Sparks pour from the sheet while the torch is off and still; or continue after the torch has lifted; or sparks flow back up into the cut.
- P4 [major · permanence_count]
  - expect: Sparks are transient and leave nothing glowing behind; the sheet stays one sheet with a cut line where the torch has been.
  - fail: Glowing dots stay on the floor for the rest of the clip; or a cut line appears where the torch has not been; or the cut heals behind the torch; or a second torch appears.
- P5 [fatal · solidity]
  - expect: The torch cuts a narrow line through the sheet; the sheet stays flat on its bed and the machine keeps its shape.
  - fail: The torch passes through the sheet leaving it unmarked; or the sheet bends like cloth; or the torch head sinks into the sheet; or the gantry passes through the sheet.
- P6 [minor · attribute_drift]
  - expect: The sheet's colour away from the cut, the machine and the workshop stay the same.
  - fail: The sheet changes colour away from the cut; or the machine changes colour; or the workshop background rearranges.

## ELEC-0130 · spark · train

**Caption.** A stovetop lighter is clicked, and a blue spark jumps between its two metal tips.

**Expectation (hidden).** The spark is a brief bridge between the tips at the click and is gone; there is no spark while the button is not pressed.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A stovetop lighter with two metal tips.
- S2 [core] The lighter is clicked.
- S3 [core] A spark jumps between the two tips.
- S4 [minor] The spark is blue.
- S5 [minor] The click comes first and the spark follows.

**PC**
- P1 [core · process_direction]
  - expect: The spark is a brief bridge between the two tips at the click, and is gone; there is no spark while the button is not pressed.
  - fail: The spark glows on between the tips after the click; or a spark appears while the lighter lies untouched; or the spark appears at a place other than between the tips; or the spark drifts away from the tips as a lit point.
- P2 [core · permanence_count]
  - expect: One lighter with two tips; the tips stay in place and the spark leaves nothing behind.
  - fail: A tip vanishes or a third tip appears; or a second lighter appears; or a glowing dot stays between the tips after the flash; or the lighter changes shape.
- P3 [major · shape_identity]
  - expect: The spark is a thin line or arc spanning the gap between the tips.
  - fail: The spark is a ball that hangs in the gap; or a wide glowing sheet; or a line that spans from a tip to somewhere other than the other tip.
- P4 [major · causeless_motion]
  - expect: The lighter moves only in the hand; the tips do not move relative to each other; nothing nearby moves at the click.
  - fail: The tips spread apart or close at the click; or the lighter jumps in the hand at the spark; or objects nearby shift at the click.
- P5 [fatal · solidity]
  - expect: The lighter stays a rigid tool; the tips do not pass through each other or into the body; the hand passes through nothing.
  - fail: The tips merge into one; or the tips pass through each other; or the lighter melts or bends; or fingers pass through the lighter.
- P6 [minor · attribute_drift]
  - expect: The lighter's colour and the background stay the same.
  - fail: The lighter changes colour; or the tips change length; or the background rearranges.

## ELEC-0131 · spark · train

**Caption.** A loose wire in an open junction box shorts against the box, and a flash and puff of smoke come from the spot.

**Expectation (hidden).** The flash is instantaneous and the smoke rises after it; the wire does not glow afterward.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] An open junction box with wires inside.
- S2 [core] A loose wire touches the box.
- S3 [core] A flash comes from the spot.
- S4 [core] A puff of smoke comes from the spot.
- S5 [minor] The flash comes first and the smoke follows.

**PC**
- P1 [core · process_direction]
  - expect: The flash is brief at the point where the wire meets the box, and is gone; the smoke appears after the flash and rises; the wire does not glow afterwards.
  - fail: The wire glows on after the flash; or the flash stays lit at the spot for the rest of the clip; or smoke rises before the flash; or the smoke shrinks back into the box.
- P2 [core · permanence_count]
  - expect: One box with its wires; the wires stay continuous and in the box; the flash leaves nothing glowing behind.
  - fail: A wire vanishes or a new wire appears; or the box vanishes or duplicates; or a glowing dot stays at the spot after the flash; or a wire's end detaches and floats.
- P3 [major · gravity_direction]
  - expect: The smoke rises from the spot and spreads; any spark fragments fall and go dark within a short distance.
  - fail: The smoke sinks from the box and pools below; or hangs as a fixed shape; or sparks rise and gather above the box; or sparks lie glowing on the floor for the rest of the clip.
- P4 [major · material_response]
  - expect: The wire is flexible and lies where it fell; the box is a rigid metal or plastic housing that keeps its shape.
  - fail: The wire stands rigid like a rod; or the box bends or ripples at the flash; or the box melts and sags.
- P5 [fatal · solidity]
  - expect: The wire touches the inside of the box and stays inside it; nothing passes through the box's walls.
  - fail: The wire passes through the box's wall; or the box sinks into the wall behind it; or the wires merge into one; or the box changes shape.
- P6 [minor · attribute_drift]
  - expect: The wires' insulation colours, the box's finish away from the spot and the wall stay the same.
  - fail: A wire changes colour; or the box changes colour away from the spot; or the wall changes colour.

## ELEC-0132 · spark · train

**Caption.** A horse's iron shoe strikes a stone on a path in the dusk, and a spark flashes under the hoof.

**Expectation (hidden).** The spark appears at the instant of the strike and is gone; there is no spark on soft ground.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A horse walks on a path in the dusk.
- S2 [core] One hoof strikes a stone.
- S3 [core] A spark flashes under the hoof.
- S4 [minor] The horse wears iron shoes.
- S5 [minor] The strike comes first and the spark follows.

**PC**
- P1 [core · process_direction]
  - expect: The spark is a brief flash at the instant the shoe strikes the stone, and is gone; nothing glows before or after.
  - fail: The spark glows on under the hoof after it has lifted; or a spark appears while the hoof is in the air; or the stone glows after the strike; or sparks flash on steps where the hoof lands on soft ground.
- P2 [core · permanence_count]
  - expect: One horse with four hooves; the stone stays where it is; the spark leaves nothing behind.
  - fail: A glowing dot stays on the path after the strike; or the stone vanishes or appears from nowhere; or a hoof vanishes or a fifth appears; or a second horse appears.
- P3 [major · gravity_direction]
  - expect: Any spark fragments fly out from under the hoof and fall to the path, going dark within a short distance.
  - fail: Sparks rise and gather above the horse; or hang in the air; or lie glowing on the path for the rest of the clip.
- P4 [major · trajectory_momentum]
  - expect: The hoof comes down onto the stone, bears weight and lifts again as the horse walks on; the stone stays put or skids a little.
  - fail: The hoof passes through the stone; or the stone flies far off as if kicked hard while the hoof merely lands; or the hoof stops in mid-air above the stone and the spark flashes anyway.
- P5 [fatal · shape_identity]
  - expect: One horse with its legs, head and tail throughout; the horse passes through nothing.
  - fail: The horse gains or loses a leg; or its body changes shape; or the horse passes through a fence or tree; or the horse merges with its shadow.
- P6 [minor · attribute_drift]
  - expect: The horse's coat colour, its tack and the path stay the same.
  - fail: The coat changes colour or pattern; or the tack changes; or the path changes surface.

**Note.** The horse is an animal; its gait is not judged. The horse is kept because the shoe striking the stone is the caption's physics.

## ELEC-0133 · spark · train

**Caption.** A car with a dragging exhaust pipe drives down a road at night, and sparks trail behind it where the pipe scrapes the asphalt.

**Expectation (hidden).** Sparks appear along the contact and stream behind the car; they stop when the pipe lifts off the road.

**Declared violation types.** trajectory_momentum, permanence_count

**SA**
- S1 [core] A car drives along a road at night.
- S2 [core] Its exhaust pipe hangs down and drags on the road.
- S3 [core] Sparks trail behind the car where the pipe scrapes the asphalt.
- S4 [minor] The sparks come from the pipe's contact point, low at the back of the car.
- S5 [minor] The scrape comes first and the sparks trail after.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The sparks stream backward from the contact point along the road, opposite to the car's motion, low over the surface, and die out along the way.
  - fail: Sparks fly ahead of the car; or spray equally in all directions; or the trail moves along with the car as a fixed cloud; or the trail lies off to one side while the car runs straight.
- P2 [core · permanence_count]
  - expect: Sparks are transient and leave nothing on the road; one car with one dragging pipe.
  - fail: Glowing dots stay on the road behind the car for the rest of the clip; or a glowing line remains along the road; or the pipe vanishes or duplicates; or a second car appears from nowhere.
- P3 [major · process_direction]
  - expect: Sparks appear only while the pipe touches the road and stop when it lifts or the car stops.
  - fail: Sparks continue after the car has stopped; or sparks trail from a pipe that is clearly off the road; or sparks flow back into the pipe.
- P4 [major · gravity_direction]
  - expect: Sparks that lift off the road arc back down and go dark; none rise or hover.
  - fail: Sparks rise steadily and gather above the car; or hang in the air; or climb up the car's back.
- P5 [fatal · solidity]
  - expect: The pipe scrapes the road's surface; the car stays whole and passes through nothing.
  - fail: The pipe sinks into the asphalt; or the car passes through another vehicle or a barrier; or the pipe detaches and floats; or the car changes shape.
- P6 [minor · attribute_drift]
  - expect: The car's colour and lights, the road markings and the roadside stay the same.
  - fail: The car changes colour; or its lights change layout; or the road markings change.

**Note.** The car is a driven vehicle; its speed and steering are not judged.

## ELEC-0134 · spark · train

**Caption.** An arc welder is struck behind a screen in a garage, and the arc lights the whole garage in blue-white, throwing hard shadows.

**Expectation (hidden).** The intense light appears only while the arc is struck, flickers, and the garage goes back to normal light when it stops.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A garage interior with a welding screen.
- S2 [core] An arc is struck behind the screen: a bright light appears there.
- S3 [core] The arc lights the whole garage in blue-white.
- S4 [core] Hard shadows are thrown across the garage.
- S5 [minor] The light comes from behind the screen, not from a lamp.

**PC**
- P1 [core · missing_consequence]
  - expect: While the arc burns, the garage is lit from the arc's position: surfaces facing the screen are brightest, and the shadows of tools, benches and the screen itself stretch away from the arc with sharp edges.
  - fail: The garage brightens evenly with no shadows; or the shadows point toward the arc; or the light comes from a place other than behind the screen; or the arc is visible but the garage stays lit only as before.
- P2 [core · process_direction]
  - expect: The intense light appears only while the arc is struck, flickers with it, and the garage returns to its earlier lighting when the arc stops.
  - fail: The garage stays lit blue-white after the arc has gone out; or the light fades in slowly like a dimmer; or the light stays perfectly steady with no flicker while the arc burns; or the garage darkens below its earlier level when the arc stops.
- P3 [major · causeless_motion]
  - expect: The screen, benches and tools stay put as the arc comes and goes; only the light changes.
  - fail: Tools or benches shift at the arc's start; or the screen falls or slides by itself; or objects jump between lit and unlit frames.
- P4 [major · gravity_direction] (if: Sparks are visible beyond the screen.)
  - expect: Any sparks that fly from behind the screen fall and go dark within a short distance.
  - fail: Sparks rise and gather above the screen; or hang in the air; or lie glowing on the floor for the rest of the clip.
- P5 [fatal · permanence_count]
  - expect: The garage's contents are the same in lit and unlit frames; the screen stays one screen in one place.
  - fail: Tools, benches or vehicles appear or vanish between lit and unlit frames; or the screen duplicates or vanishes; or the arc light passes through the screen and shows the welder as if the screen were glass; or the garage's layout changes.
- P6 [minor · attribute_drift]
  - expect: Wall colours, tool colours and the screen's colour are consistent apart from the arc's blue-white cast.
  - fail: The walls change colour permanently after the arc; or tools change colour; or the screen changes colour or pattern.

**Note.** The welder behind the screen is not judged; whoever strikes the arc may be out of view.

## ELEC-0135 · spark · train

**Caption.** An old-fashioned knife switch is thrown closed, and a small arc snaps at the contacts as they close.

**Expectation (hidden).** The arc appears at the contacts at the moment of closing and vanishes; the connected lamp comes on.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] An old-fashioned knife switch with a hinged blade and contacts.
- S2 [core] The switch is thrown closed.
- S3 [core] A small arc snaps at the contacts as they close.
- S4 [minor] The arc is at the contacts, not on the handle.
- S5 [minor] The blade closes first and the arc comes as it meets the contacts.

**PC**
- P1 [core · process_direction]
  - expect: The arc is a brief flash at the contacts at the moment of closing, and is gone; the switch stays closed.
  - fail: The arc glows on between the contacts after the switch is closed; or an arc appears while the blade is still far from the contacts; or the switch springs back open by itself; or the arc appears at the handle or the base.
- P2 [core · permanence_count]
  - expect: One switch with one blade and its contacts; the parts stay attached; the arc leaves nothing behind.
  - fail: The blade vanishes or a second blade appears; or a contact vanishes; or a glowing dot stays on the contacts after the flash; or the switch changes shape.
- P3 [major · missing_consequence] (if: A lamp or other device wired to the switch is in view.)
  - expect: A device wired to the switch comes on as the switch closes and stays on while it is closed.
  - fail: The device comes on before the blade reaches the contacts; or the switch is closed and the device stays off to the end of the clip; or the device comes on and goes off again with the switch closed and untouched.
- P4 [major · trajectory_momentum]
  - expect: The blade swings about its hinge in one motion down onto the contacts and stays there.
  - fail: The blade bends as it swings; or slides sideways off its hinge; or bounces up and down on the contacts several times; or the base moves as the blade is thrown.
- P5 [fatal · solidity]
  - expect: The blade seats between the contact jaws from outside; the hand passes through nothing; the switch stays on its base.
  - fail: The blade passes through the contacts or the base; or fingers pass through the handle; or the switch sinks into the board; or the blade merges with the contacts.
- P6 [minor · attribute_drift]
  - expect: The switch's metal and base colours, the board and the wiring stay the same.
  - fail: The base changes colour; or the wiring changes route; or the blade changes shape or length.

## ELEC-0136 · spark · train

**Caption.** An electric igniter is fired, and it sparks briefly at the wire ends before the fuse catches.

**Expectation (hidden).** The spark comes first at the wire ends, then the fuse glows and burns along its length; the spark itself does not persist.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] An electric igniter with wire ends at a fuse.
- S2 [core] The igniter is fired.
- S3 [core] It sparks briefly at the wire ends.
- S4 [core] The fuse catches.
- S5 [minor] The spark comes first and the fuse catches after.

**PC**
- P1 [core · process_direction]
  - expect: The spark is a brief flash at the wire ends, and is gone; the fuse then glows at that spot and burns along its length in one direction, never back.
  - fail: The spark glows on at the wire ends for the rest of the clip; or the fuse burns before the spark; or the burning point runs back the way it came; or the fuse relights where it has already burnt.
- P2 [core · missing_consequence]
  - expect: After the spark, the fuse catches at the wire ends and a glowing point travels away along it.
  - fail: The spark comes and the fuse stays unlit to the end of the clip; or the fuse catches at a point far from the wire ends; or the fuse burns along its whole length at once; or the glowing point jumps from place to place.
- P3 [major · gravity_direction]
  - expect: Any sparks or embers thrown off fall and go dark within a short distance; smoke from the fuse rises.
  - fail: Sparks rise and gather above the fuse; or hang in the air; or smoke sinks and pools; or embers lie glowing beside the fuse for the rest of the clip.
- P4 [major · material_response]
  - expect: The fuse is a thin cord that stays where it lies; behind the burning point it is blackened or gone, ahead it is unburnt.
  - fail: The fuse stands rigid and stays whole behind the burning point; or the fuse grows longer; or the unburnt part ahead blackens before the point reaches it.
- P5 [fatal · permanence_count]
  - expect: One igniter, one fuse; the fuse's burnt part does not return; nothing appears, vanishes or passes through anything.
  - fail: A second fuse appears; or the burnt part of the fuse comes back unburnt; or the igniter vanishes; or the wire ends pass through the fuse or the ground.
- P6 [minor · attribute_drift]
  - expect: The igniter's colour, the unburnt fuse's colour and the ground stay the same.
  - fail: The igniter changes colour; or the unburnt fuse changes colour ahead of the flame; or the ground changes.

**Note.** What the fuse leads to is not judged; the clip ends with the fuse burning.

## ELEC-0137 · spark · train

**Caption.** A lathe cuts a spinning steel bar, and glowing chips and sparks curl off the tool and drop into the tray.

**Expectation (hidden).** The sparks and chips fall downward from the cutting point and darken as they cool; they appear only while cutting.

**Declared violation types.** gravity_direction, permanence_count, process_direction

**SA**
- S1 [core] A lathe with a steel bar spinning in it.
- S2 [core] A cutting tool is against the bar.
- S3 [core] Glowing chips and sparks come off the tool.
- S4 [core] They drop into the tray below.
- S5 [minor] The chips curl as they come off.
- S6 [minor] The cut comes first and the chips and sparks follow.

**PC**
- P1 [core · gravity_direction]
  - expect: The chips and sparks fall downward from the cutting point into the tray, arcing as they go.
  - fail: Chips or sparks rise from the tool and gather above the lathe; or hang in the air; or drift sideways without dropping; or chips climb up the bar.
- P2 [core · process_direction]
  - expect: Chips and sparks appear only while the tool is cutting, and the glowing chips darken as they cool in the tray; nothing goes back to glowing.
  - fail: Chips come off while the tool is clear of the bar; or continue after the bar has stopped spinning; or chips in the tray brighten from dark to glowing; or chips flow back onto the bar.
- P3 [core · permanence_count]
  - expect: The chips are material removed from the bar: they pile up in the tray and none vanish in mid-air; the bar stays one bar, thinner where cut.
  - fail: Chips vanish before reaching the tray; or the pile in the tray shrinks while chips keep arriving; or the bar grows thicker as it is cut; or a second bar appears.
- P4 [major · trajectory_momentum]
  - expect: The chips leave the tool along the bar's direction of spin, curling away from the cutting edge.
  - fail: Chips fly against the direction of spin; or spray equally in all directions; or leave from a point on the bar away from the tool.
- P5 [fatal · solidity]
  - expect: The tool cuts into the bar's surface; the bar stays held in the chuck and the lathe keeps its shape.
  - fail: The tool passes through the bar leaving it unmarked; or the bar passes through the chuck; or the tool bends like rubber; or the lathe changes shape.
- P6 [minor · attribute_drift]
  - expect: The lathe's colour, the bar's uncut surface and the tray stay the same.
  - fail: The lathe changes colour; or the bar's uncut part changes finish; or the tray changes shape or place.

**Note.** Glowing chips are the expected look of hot metal; their colour and count are not judged.

## ELEC-0138 · spark · train

**Caption.** Two pieces of flint are struck together in the dark, and a tiny spark jumps between them.

**Expectation (hidden).** The spark appears at the point of impact at the instant of the strike and is gone; nothing glows before or after.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] Two pieces of flint, held in the dark.
- S2 [core] The pieces are struck together.
- S3 [core] A tiny spark jumps between them.
- S4 [minor] The scene is dark before the strike.
- S5 [minor] The strike comes first and the spark follows.

**PC**
- P1 [core · process_direction]
  - expect: The spark appears at the point of impact at the instant of the strike, and is gone; nothing glows before or after.
  - fail: The spark glows on between the pieces after the strike; or a spark appears while the pieces are apart and still; or a piece of flint glows after the strike; or the spark drifts away as a lit point.
- P2 [core · permanence_count]
  - expect: Two pieces of flint throughout; the spark leaves nothing behind.
  - fail: A third piece appears or a piece vanishes; or a glowing dot stays in the air after the spark; or the pieces merge into one; or the spark leaves a lit trail.
- P3 [major · gravity_direction]
  - expect: Any spark fragments fall from the strike point and go dark within a short distance.
  - fail: Sparks rise and gather above the hands; or hang in the air; or lie glowing on the ground for the rest of the clip.
- P4 [major · missing_consequence]
  - expect: During the spark the hands and the flint nearest to it brighten briefly; the rest stays dark.
  - fail: The spark is visible while the hands and flint around it stay as dark as before; or the whole scene lights up as if a lamp came on; or the surroundings stay lit after the spark is gone.
- P5 [fatal · solidity]
  - expect: The pieces meet at their surfaces and rebound or stop; neither passes through the other or through the hands.
  - fail: One piece passes through the other; or a piece passes through a hand; or the flints melt or bend; or a piece vanishes at the strike.
- P6 [minor · attribute_drift]
  - expect: The flints' colour and shape and the dark background stay the same.
  - fail: A flint changes colour or shape between strikes; or the background rearranges; or the hands change.

**Note.** The hands are kept because striking is the caption's action; how they hold the flint is not judged.

## ELEC-0139 · spark · train

**Caption.** A demolition hammer chips a concrete floor, and an occasional spark flicks where the bit strikes embedded stone.

**Expectation (hidden).** Sparks appear only at some blows, at the point of impact, and are gone at once.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A demolition hammer with its bit on a concrete floor.
- S2 [core] The hammer chips the floor: the bit strikes repeatedly and pieces break off.
- S3 [core] A spark flicks where the bit strikes embedded stone.
- S4 [minor] Sparks come only at some blows, not every one.
- S5 [minor] The strike comes first and the spark follows.

**PC**
- P1 [core · process_direction]
  - expect: Sparks appear only at the moment of a blow, at the point where the bit meets the floor, and each is gone at once; between blows nothing glows.
  - fail: A spark stays lit on the floor after the bit lifts; or sparks appear while the hammer is held off the floor; or the bit glows steadily; or sparks appear at a point away from the bit.
- P2 [core · permanence_count]
  - expect: One hammer with one bit; chips that break off are pieces of the floor and stay on the floor; sparks leave nothing behind.
  - fail: Glowing dots stay on the floor after a blow; or chips vanish in mid-air; or the bit duplicates or vanishes; or chips appear from nowhere away from the bit.
- P3 [major · gravity_direction]
  - expect: Chips and any spark fragments fly out from the bit and fall to the floor, going dark within a short distance.
  - fail: Chips or sparks rise and hang in the air; or climb steadily; or sparks lie glowing on the floor for the rest of the clip.
- P4 [major · material_response]
  - expect: The concrete breaks into hard chips and leaves a pitted hole; the bit stays a rigid steel point.
  - fail: The concrete dents like clay and springs back; or the floor ripples like water; or the bit bends or curls; or the hole closes up between blows.
- P5 [fatal · solidity]
  - expect: The bit strikes the floor's surface and enters only as far as the hole it makes; the hammer keeps its shape.
  - fail: The bit passes deep through the floor as if through air; or the hammer sinks into the floor; or the hammer changes shape; or the floor turns transparent.
- P6 [minor · attribute_drift]
  - expect: The hammer's colour and the floor's surface away from the hole stay the same.
  - fail: The hammer changes colour; or the floor changes texture away from the hole; or the surroundings rearrange.

**Note.** Who holds the hammer is not judged.

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

## ELEC-0141 · magnet · train

**Caption.** A magnet is lowered toward a pile of paperclips on a desk, and the clips jump up and cling to it.

**Expectation (hidden).** The clips leap only when the magnet comes close and hang from it in chains; they fall when the magnet is pulled away.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A pile of paperclips on a desk.
- S2 [core] A magnet is lowered toward the pile.
- S3 [core] The clips jump up and cling to the magnet.
- S4 [minor] The clips are loose in a pile, not in a box.
- S5 [minor] The lowering comes first and the jump follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The clips lie still until the magnet is close above them, then leap up to it; clips far from the magnet stay put, and the leaping stops when the magnet is taken away.
  - fail: Clips jump while the magnet is still high above or off to one side; or clips across the desk slide toward the magnet; or clips move before the magnet has been lowered; or clips keep hopping after the magnet is well away.
- P2 [core · gravity_direction]
  - expect: Clips on the magnet hang from its underside and sides in chains, touching it or each other; any that drop off fall back to the desk.
  - fail: Clips hover in the air between desk and magnet touching nothing; or a clip that lets go drifts upward or sideways; or clips rise past the magnet; or the chains stand straight up above the magnet.
- P3 [major · trajectory_momentum]
  - expect: Each clip moves along the line from its spot to the magnet and stops on it or on a clip already there; the chains travel with the magnet as it moves.
  - fail: A clip flies past the magnet and off; or clips circle the magnet in the air; or chains stay hanging in place when the magnet is moved away; or clips bounce off and back several times.
- P4 [major · material_response]
  - expect: The clips stay rigid bent wire; the magnet stays a hard block; the desk does not dent.
  - fail: Clips bend or straighten as they jump; or melt together into a lump; or the magnet squashes; or the desk surface dents under the pile.
- P5 [fatal · permanence_count]
  - expect: The clips on the magnet are the clips from the pile; none appear from nowhere or vanish; the magnet passes through nothing.
  - fail: Clips multiply on the magnet; or clips vanish in mid-air; or the magnet passes into the desk; or two clips merge into one.
- P6 [minor · attribute_drift]
  - expect: The magnet's colour and shape, the clips' colour and the desk stay the same.
  - fail: The magnet changes colour or shape; or the clips change colour; or the desk's contents rearrange.

## ELEC-0142 · magnet · train

**Caption.** A magnet is swept over a mix of nails and plastic beads spilled on the floor, and the nails stick to the magnet while the beads stay behind.

**Expectation (hidden).** Only the nails lift; the plastic beads do not move; the nails cling to the magnet until pulled off.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] Nails and plastic beads spilled together on a floor.
- S2 [core] A magnet is swept over the mix.
- S3 [core] The nails stick to the magnet.
- S4 [core] The beads stay behind on the floor.
- S5 [minor] The beads are plastic: coloured, round, not metallic.
- S6 [minor] The sweep comes first and the nails lift as it passes.

**PC**
- P1 [core · missing_consequence]
  - expect: As the magnet passes close over the mix, nails beneath it jump up and cling to it; the beads do not move toward the magnet.
  - fail: The magnet passes close over nails and they stay on the floor; or beads jump up and cling to the magnet; or nails rise beside the magnet without touching it; or nails stick to the magnet while it is still high above them.
- P2 [core · permanence_count]
  - expect: The nails on the magnet are nails from the floor; nails and beads keep their number and kind; the beads left behind are the beads that were there.
  - fail: Nails multiply on the magnet; or nails vanish in mid-air; or a bead turns into a nail or a nail into a bead; or beads vanish as the magnet passes.
- P3 [major · gravity_direction]
  - expect: The nails hang from the magnet in contact with it; any that drop fall back to the floor; the beads lie where they were.
  - fail: Nails hang in the air below the magnet without touching it; or a nail that comes off drifts sideways or upward; or beads float; or the nails stand upright above the magnet.
- P4 [major · causeless_motion]
  - expect: Beads move only if nudged by the magnet or a nail; nothing else on the floor stirs; nails on the magnet stay put.
  - fail: Beads roll toward or away from the magnet with nothing touching them; or nails on the magnet crawl about; or the mix rearranges away from the magnet's path.
- P5 [fatal · solidity]
  - expect: Nails and beads stay outside the magnet's body and above the floor; the magnet passes through nothing.
  - fail: A nail sinks into the magnet; or the magnet passes through the floor; or nails pass through beads; or the magnet merges with the nails into one lump.
- P6 [minor · attribute_drift]
  - expect: The magnet's colour, the beads' colours and the floor stay the same.
  - fail: The magnet changes colour or shape; or the beads change colour; or the floor pattern changes.

## ELEC-0143 · magnet · train

**Caption.** A sheet of paper lies over a paperclip, and a magnet is moved across the top of the paper; the clip follows the magnet under the paper.

**Expectation (hidden).** The clip moves exactly with the magnet, never passing through the paper; it stops when the magnet stops.

**Declared violation types.** causeless_motion, solidity

**SA**
- S1 [core] A paperclip lies under a sheet of paper.
- S2 [core] A magnet is moved across the top of the paper.
- S3 [core] The clip follows the magnet beneath the paper.
- S4 [minor] The clip stays under the paper the whole time.
- S5 [minor] The magnet's movement comes first and the clip follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The clip moves only where and when the magnet above it moves, staying beneath it, and stops when the magnet stops.
  - fail: The clip moves in a different direction from the magnet; or keeps moving after the magnet has stopped; or stays still while the magnet passes over it; or the clip sets off before the magnet has begun to move.
- P2 [core · solidity]
  - expect: The paper stays between magnet and clip: the clip is seen through or under the paper and never comes up through it; the magnet stays on top.
  - fail: The clip passes up through the paper and sits on the magnet; or the magnet sinks through the paper; or the clip and magnet are seen touching with no paper between; or the clip passes through the table.
- P3 [major · material_response]
  - expect: The paper is a flat flexible sheet: it lifts slightly or ripples where the clip drags beneath it and lies flat again.
  - fail: The paper stays perfectly rigid like a board while the clip drags under it; or stretches like rubber; or tears where the clip moves; or the paper flows like liquid.
- P4 [major · causeless_motion]
  - expect: The paper stays on the table as the magnet moves, apart from small drags; other items on the table do not move.
  - fail: The paper slides across the table with the magnet; or lifts off the table; or other items on the table shift as the magnet passes.
- P5 [fatal · permanence_count]
  - expect: One magnet, one clip, one sheet; nothing appears, vanishes or merges.
  - fail: A second clip or magnet appears; or the clip vanishes; or clip and magnet fuse into one object; or the paper duplicates.
- P6 [minor · attribute_drift]
  - expect: The magnet's colour, the paper's colour and the table stay the same.
  - fail: The magnet changes colour or shape; or the paper changes colour or size; or the table surface changes.

**Note.** The clip may be hidden by the paper for parts of the clip; P1 is judged on the moments when its position beneath the paper can be seen.

## ELEC-0144 · magnet · train

**Caption.** A magnet is slid along the underside of a thin wooden table, and a toy car with a metal base on top of the table follows it.

**Expectation (hidden).** The car moves only where the magnet below moves and stays on the table surface; it does not move when the magnet is taken away.

**Declared violation types.** causeless_motion, solidity

**SA**
- S1 [core] A toy car sits on top of a thin wooden table.
- S2 [core] A magnet is slid along the underside of the table.
- S3 [core] The car follows the magnet across the table top.
- S4 [minor] The car has a metal base: a metal underside or chassis is stated or shown.
- S5 [minor] The magnet's movement comes first and the car follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The car moves only where and when the magnet below it moves, staying above it, and stops when the magnet stops.
  - fail: The car moves in a different direction from the magnet beneath; or keeps rolling after the magnet has stopped; or stays still while the magnet passes under it; or the car sets off before the magnet moves.
- P2 [core · solidity]
  - expect: The table top stays between magnet and car: the magnet stays below the table and the car on its surface.
  - fail: The magnet passes up through the table top; or the car sinks into the table; or the car and magnet are seen touching with no wood between; or the car passes through the table's edge.
- P3 [major · trajectory_momentum]
  - expect: The car rides along on its wheels on the table's surface, following the magnet's path.
  - fail: The car lifts off the table; or slides sideways with its wheels still while its wheels face along the path; or flips over as it follows; or the car jumps ahead of the magnet.
- P4 [major · causeless_motion]
  - expect: The table stays where it is; other items on the table do not move as the magnet passes beneath.
  - fail: The table slides or rocks; or other items on the table shift as the magnet passes; or the car spins in place with the magnet still.
- P5 [fatal · permanence_count]
  - expect: One car, one magnet, one table; nothing appears, vanishes or merges.
  - fail: A second car or magnet appears; or the car vanishes; or the car changes into another object; or the table changes shape.
- P6 [minor · attribute_drift]
  - expect: The car's colour, the table's grain and the surroundings stay the same.
  - fail: The car changes colour; or the table changes colour or pattern; or the surroundings rearrange.

**Note.** The magnet is mostly hidden beneath the table; P1 is judged on the moments when both magnet and car are in view. The car moving while no magnet is in view is not a violation.

## ELEC-0145 · magnet · train

**Caption.** A kitchen knife is brought up to a magnetic strip on the wall, and the knife snaps onto the strip and stays there.

**Expectation (hidden).** The blade jumps the last little gap and hangs on the strip without support; it does not fall until pulled off.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] A magnetic knife strip on a wall.
- S2 [core] A kitchen knife is brought up to the strip.
- S3 [core] The knife snaps onto the strip.
- S4 [core] The knife stays on the strip after the hand withdraws.
- S5 [minor] The blade lies flat against the strip.
- S6 [minor] The order is approach, snap, hold.

**PC**
- P1 [core · missing_consequence]
  - expect: Over the last small gap the blade is drawn onto the strip and stays pressed to it with nothing else holding it once the hand withdraws.
  - fail: The knife stops a gap short of the strip and hangs there; or drops when the hand lets go; or slides down the strip; or bounces off the strip and falls.
- P2 [core · gravity_direction]
  - expect: The knife hangs on the vertical strip; if it comes off it falls straight down.
  - fail: The knife floats away from the strip; or drifts upward along the wall; or hangs a gap from the strip without touching; or a fallen knife rises back to the strip.
- P3 [major · trajectory_momentum]
  - expect: The snap is toward the strip along the line from the blade to it, and the knife stops on contact.
  - fail: The knife jumps away from the strip; or darts sideways past it; or slides toward and away several times before settling; or the knife keeps moving along the strip after landing.
- P4 [major · causeless_motion]
  - expect: Once on the strip the knife stays put; the strip stays fixed to the wall; other knives on the strip do not move.
  - fail: The knife creeps along the strip after release; or rotates by itself; or the strip shifts on the wall; or other knives on the strip drop or move.
- P5 [fatal · solidity]
  - expect: One knife on one strip; the blade touches the strip's surface and does not sink into it or the wall; the hand passes through nothing.
  - fail: The blade sinks into the strip or the wall; or a second knife appears; or the knife vanishes; or the hand passes through the blade or the strip.
- P6 [minor · attribute_drift]
  - expect: The knife's handle colour, the strip and the wall stay the same.
  - fail: The handle changes colour; or the blade changes length or shape; or the strip changes place or colour.

## ELEC-0146 · magnet · train

**Caption.** A phone is brought near a magnetic mount on a car's dashboard, and the phone snaps onto the mount and holds.

**Expectation (hidden).** The phone jumps the last bit of distance and stays in place while the car moves; it comes off only when pulled.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A magnetic phone mount on a car's dashboard.
- S2 [core] A phone is brought near the mount.
- S3 [core] The phone snaps onto the mount.
- S4 [core] The phone holds on the mount after the hand withdraws.
- S5 [minor] The mount is on the dashboard, not on a vent or window.
- S6 [minor] The order is approach, snap, hold.

**PC**
- P1 [core · causeless_motion]
  - expect: The phone moves only in the hand until the last small gap, jumps that gap onto the mount, and then stays still on it; it does not move once held.
  - fail: The phone jumps to the mount from far away; or slides about on the mount after the hand leaves; or springs off the mount with nothing pulling it; or the mount moves toward the phone.
- P2 [core · gravity_direction]
  - expect: Once on the mount the phone is held with nothing else supporting it; if it comes off it falls downward.
  - fail: The phone drops the instant the hand lets go; or hangs a gap from the mount without touching; or floats away from the mount; or a fallen phone rises back.
- P3 [major · trajectory_momentum]
  - expect: The snap is toward the mount along the line between them, and the phone stops flat on the mount's face.
  - fail: The phone jumps away from the mount; or darts sideways past it; or lands at an angle and then swings flat by itself repeatedly; or bounces on and off.
- P4 [major · causeless_motion]
  - expect: The mount stays fixed to the dashboard; nothing else in the car moves as the phone attaches.
  - fail: The mount shifts or tips as the phone lands; or the dashboard items jump; or the steering wheel turns by itself.
- P5 [fatal · solidity]
  - expect: One phone on one mount; the phone touches the mount's face and does not sink into it or the dashboard; the hand passes through nothing.
  - fail: The phone sinks into the mount or dashboard; or a second phone appears; or the phone vanishes; or the hand passes through the phone.
- P6 [minor · attribute_drift]
  - expect: The phone's case colour, the mount and the dashboard stay the same.
  - fail: The phone changes colour or size; or the mount changes shape; or the dashboard changes.

**Note.** Whether the car is moving is not judged; if it moves, the phone staying on the mount is the caption's point.

## ELEC-0147 · magnet · train

**Caption.** Two toy train cars with magnetic couplers are pushed together, and they snap together and roll as one.

**Expectation (hidden).** The cars pull together over the last gap and stay joined while rolling; they separate only when pulled apart.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] Two toy train cars on a track or floor, apart.
- S2 [core] The cars are pushed together.
- S3 [core] Their couplers snap together.
- S4 [core] The joined cars roll as one.
- S5 [minor] The couplers meet end to end.
- S6 [minor] The order is push, snap, roll together.

**PC**
- P1 [core · missing_consequence]
  - expect: Over the last small gap the couplers pull together and the cars stay joined; when one is moved the other follows without a gap opening.
  - fail: The cars stop with a gap between the couplers and stay that way; or the couplers touch and drift apart; or one car is moved and the other stays behind; or the cars part while rolling with nothing pulling them.
- P2 [core · causeless_motion]
  - expect: The cars move only when pushed or pulled along; once joined they stop together and stay still.
  - fail: A car sets off by itself before it is pushed; or the joined pair keeps rolling and stops and starts on its own; or a car slides sideways off the line; or the cars spring apart.
- P3 [major · trajectory_momentum]
  - expect: The cars roll on their wheels along the track or floor in one line, the following car tracking the leading one.
  - fail: The cars lift off the track; or the second car swings out and rolls beside the first while joined; or a car reverses while the other goes on; or the wheels stay still while the cars slide.
- P4 [major · material_response]
  - expect: The cars are rigid toys that keep their shape as they meet; the couplers stay small hard fittings.
  - fail: A car squashes or bends at the meeting; or the couplers stretch like rubber; or the cars flex as they roll.
- P5 [fatal · permanence_count]
  - expect: Two cars throughout, joined but separate; nothing merges, vanishes or passes through anything.
  - fail: The two cars merge into one long car; or a third car appears; or a car vanishes; or one car passes through the other.
- P6 [minor · attribute_drift]
  - expect: The cars' colours and markings and the track stay the same.
  - fail: A car changes colour; or its markings change; or the track changes route.

## ELEC-0148 · magnet · train

**Caption.** Two bar magnets are brought together end to end, and they snap together with a click.

**Expectation (hidden).** The magnets pull together over the last short distance and stick; they do not drift apart once joined.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] Two bar magnets.
- S2 [core] They are brought together end to end.
- S3 [core] They snap together.
- S4 [minor] The ends meet squarely, end to end rather than side by side.
- S5 [minor] The approach comes first and the snap follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The magnets move only in the hands until the last short gap, then jump together; once joined they stay joined and still.
  - fail: A magnet jumps while they are still far apart; or the joined pair drifts apart with nothing pulling; or the magnets slide about on the table after joining; or a magnet moves before either hand has moved.
- P2 [core · missing_consequence]
  - expect: Over the last short gap the ends pull into contact and stay pressed together; if one is lifted the other comes with it.
  - fail: The ends stop with a gap between them and stay that way; or touch and then fall apart; or one is lifted and the other stays behind; or the ends push apart as they near.
- P3 [major · trajectory_momentum]
  - expect: The jump is along the line joining the two ends, toward each other, and they meet face to face and stop.
  - fail: A magnet jumps away from the other; or darts sideways past it; or the two slide toward and away several times before joining; or they spin round each other in the air.
- P4 [major · material_response]
  - expect: The magnets are rigid bars that keep their shape as they meet.
  - fail: A bar bends or squashes at the meeting; or the ends flatten together; or a bar stretches like rubber.
- P5 [fatal · permanence_count]
  - expect: Two bars throughout, joined but separate; neither passes into the other or vanishes.
  - fail: The two bars merge into one longer bar with no seam; or a third bar appears; or a bar vanishes; or one bar passes through the other.
- P6 [minor · attribute_drift]
  - expect: The bars' colours and markings and the surface beneath stay the same.
  - fail: A bar changes colour or its markings change; or a bar changes length; or the surface changes.

**Note.** The click is sound and is not judged.

## ELEC-0149 · magnet · train

**Caption.** One bar magnet is pushed toward the like end of another lying on a table, and the second magnet slides away from the first.

**Expectation (hidden).** The free magnet moves away as the other approaches and stops when the gap is large enough; when one is flipped they snap together instead.

**Declared violation types.** causeless_motion, trajectory_momentum

**SA**
- S1 [core] Two bar magnets, one lying on a table.
- S2 [core] One magnet is pushed toward the like end of the other.
- S3 [core] The second magnet slides away from the first.
- S4 [minor] The pushed magnet is moved by hand; the other is not touched.
- S5 [minor] The approach comes first and the sliding away follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The free magnet lies still until the other is close, moves away only while the other approaches, and stops once the gap is large enough or the other stops.
  - fail: The free magnet moves while the other is still far away; or keeps sliding to the end of the clip after the other has stopped; or moves before the other has begun to approach; or slides about with the pushed magnet held still.
- P2 [core · trajectory_momentum]
  - expect: The free magnet slides straight away along the line joining the two, on the table surface, and may turn end for end but does not move toward the other.
  - fail: The free magnet moves toward the pushed one and sticks; or slides off sideways at right angles to the approach; or lifts off the table; or moves away and then comes back and joins.
- P3 [major · causeless_motion]
  - expect: Other items on the table stay still; the table does not move.
  - fail: Other items slide as the magnet approaches; or the table shifts; or the pushed magnet is pushed back into the hand.
- P4 [major · material_response]
  - expect: Both bars stay rigid and keep their shape; the table surface stays flat.
  - fail: A bar bends or squashes; or the table dents; or a bar stretches.
- P5 [fatal · permanence_count]
  - expect: Two bars throughout; neither vanishes, duplicates or passes through the other or the table.
  - fail: A third bar appears; or a bar vanishes; or one bar passes through the other; or a bar sinks into the table.
- P6 [minor · attribute_drift]
  - expect: The bars' colours and pole markings and the table stay the same.
  - fail: A bar changes colour; or its pole markings swap; or the table surface changes.

**Note.** The free magnet turning end for end and then snapping onto the other is the expected behaviour when the like poles are not kept aligned; it is not a violation.

## ELEC-0150 · magnet · train

**Caption.** A cabinet door with a magnetic latch is swung shut, and the door pulls itself closed the last little way and stays closed.

**Expectation (hidden).** The door snaps closed just before it reaches the frame and does not swing open on its own afterward.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A cabinet door with a magnetic latch.
- S2 [core] The door is swung shut.
- S3 [core] The door pulls itself closed the last little way.
- S4 [core] The door stays closed.
- S5 [minor] The final pull happens after the hand has let go.
- S6 [minor] The order is swing, pull shut, stay closed.

**PC**
- P1 [core · causeless_motion]
  - expect: The door moves while it is being swung and, on its own, only over the last small gap; left standing at a wide angle it stays there.
  - fail: The door, left standing wide open, swings shut with nothing touching it; or reverses and opens while the hand still pushes it; or swings open and shut several times before closing.
- P2 [core · missing_consequence]
  - expect: Once the door reaches the last small gap it closes fully against the frame and stays shut for the rest of the clip.
  - fail: The door stops a gap short of closed and rests there; or springs back open after touching the frame; or bounces open and shut on the frame; or opens again by itself later in the clip.
- P3 [major · trajectory_momentum]
  - expect: The door swings about its hinges as one panel toward the frame, its free edge sweeping an arc.
  - fail: The door bends or ripples as it swings; or the hinge side moves along the frame; or the door slides across the opening rather than hinging; or the door moves away from the frame as a whole.
- P4 [major · causeless_motion]
  - expect: The cabinet and its contents stay still as the door shuts; neighbouring doors do not move.
  - fail: The cabinet rocks or slides; or a neighbouring door swings open at the shut; or items on the cabinet jump.
- P5 [fatal · solidity]
  - expect: One door on its hinges; the door passes through neither the frame nor a neighbouring door; the hand passes through nothing.
  - fail: The door passes through the frame; or the door detaches from its hinges; or a second door appears; or the hand passes through the door.
- P6 [minor · attribute_drift]
  - expect: The door's colour and handle and the cabinet's finish stay the same.
  - fail: The door changes colour; or the handle changes side or shape; or the cabinet's finish changes.

## ELEC-0151 · magnet · train

**Caption.** A magnetic parts tray is set on the side of a car and screws dropped into it, and the tray and the screws stay put.

**Expectation (hidden).** The tray holds on the vertical steel panel and the screws stick to its floor even when the tray is tilted; the tray does not slide down.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] A magnetic parts tray and a car.
- S2 [core] The tray is set on the side of the car.
- S3 [core] Screws are dropped into the tray.
- S4 [core] The tray and the screws stay put.
- S5 [minor] The tray is on a vertical or sloping steel panel, not on a flat top.
- S6 [minor] The order is tray placed, screws dropped, both hold.

**PC**
- P1 [core · missing_consequence]
  - expect: Once let go, the tray stays where it was placed on the panel with nothing else supporting it; the screws land in the tray and stay there, even as the tray is jostled or tilted.
  - fail: The tray drops when released; or slides down the panel; or stands off the panel with a gap; or screws slide out of a tilted tray and fall.
- P2 [core · gravity_direction]
  - expect: The screws fall downward into the tray and come to rest on its floor; anything that misses the tray falls to the ground.
  - fail: Screws float above the tray; or rise after landing; or a screw that misses hangs in the air; or screws climb the tray's walls.
- P3 [major · causeless_motion]
  - expect: The tray stays still once placed; the screws lie still once landed; the car does not move.
  - fail: The tray creeps along the panel; or screws hop about in the tray with nothing touching them; or the car rocks or rolls as the screws land.
- P4 [major · material_response]
  - expect: The tray is a rigid dish; the screws are hard pieces that clatter and settle; the car's panel does not dent.
  - fail: The tray bends or sags; or screws squash or stick together into a lump; or the panel dents under the tray.
- P5 [fatal · permanence_count]
  - expect: One tray; the screws in the tray are the screws that were dropped; nothing passes into the tray's floor or the car's panel.
  - fail: Screws multiply in the tray; or vanish in mid-air; or the tray sinks into the panel; or a second tray appears.
- P6 [minor · attribute_drift]
  - expect: The tray's colour, the car's paint and the screws' finish stay the same.
  - fail: The tray changes colour or shape; or the car changes colour; or the screws change size.

## ELEC-0152 · magnet · train

**Caption.** The flap of a handbag with a magnetic clasp is let fall, and the flap snaps down and holds.

**Expectation (hidden).** The flap is drawn shut over the last small gap and stays closed until pulled open.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A handbag with a flap and a magnetic clasp.
- S2 [core] The flap is let fall.
- S3 [core] The flap snaps down onto the clasp.
- S4 [core] The flap holds closed.
- S5 [minor] The flap moves on its own after being let go, not pushed down.
- S6 [minor] The order is release, fall, snap, hold.

**PC**
- P1 [core · causeless_motion]
  - expect: The flap falls when released, snaps to over the last small gap and then stays shut; it does not lift or open again by itself.
  - fail: The flap opens again with nothing touching it; or flaps up and down repeatedly; or moves before it is released; or the bag jumps as the flap lands.
- P2 [core · missing_consequence]
  - expect: Over the last small gap the flap is drawn onto the clasp and stays pressed shut for the rest of the clip.
  - fail: The flap stops a gap short of the clasp and hangs there; or bounces back open after touching; or slides off the clasp; or rests closed but lifts when the bag is moved.
- P3 [major · gravity_direction]
  - expect: The flap falls downward from where it is released toward the bag's front.
  - fail: The flap rises when released; or hangs in the air; or falls sideways away from the bag.
- P4 [major · material_response]
  - expect: The flap is a stiff or leathery panel that swings down from its fold; the bag keeps its shape.
  - fail: The flap flops like wet cloth; or stretches; or the bag collapses as the flap lands; or the flap stays rigid in the air.
- P5 [fatal · solidity]
  - expect: One bag with one flap; the flap lands on the bag's outside and does not pass into it; the hand passes through nothing.
  - fail: The flap sinks into the bag; or the flap detaches; or a second flap appears; or the hand passes through the bag.
- P6 [minor · attribute_drift]
  - expect: The bag's colour, its hardware and the surface it sits on stay the same.
  - fail: The bag changes colour; or the clasp changes shape or place; or the surface changes.

## ELEC-0153 · magnet · train

**Caption.** A horseshoe magnet is lowered over a steel key on a table, and the key jumps up and sticks to the magnet.

**Expectation (hidden).** The key lifts when the magnet is close enough and hangs from the poles; it stays until pulled off.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A steel key lies on a table.
- S2 [core] A horseshoe magnet is lowered over the key.
- S3 [core] The key jumps up and sticks to the magnet.
- S4 [minor] The magnet is horseshoe shaped.
- S5 [minor] The lowering comes first and the jump follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The key lies still until the magnet is close above it, then leaps up to the magnet's poles; it does not move while the magnet is far off, and stays put on the magnet.
  - fail: The key jumps while the magnet is still high above; or slides about the table before the magnet is near; or the key springs off the magnet with nothing touching it; or the magnet is drawn down to the table instead.
- P2 [core · gravity_direction]
  - expect: The key hangs from the magnet's poles in contact with them and rises with the magnet; if it comes off it falls back to the table.
  - fail: The key hangs in the air below the magnet without touching it; or floats up past the magnet; or a key that comes off drifts sideways or upward; or the key stays in the air after the magnet is moved away.
- P3 [major · trajectory_momentum]
  - expect: The key moves straight up from the table to the magnet's poles and stops there.
  - fail: The key flies past the magnet and off; or circles the magnet; or bounces off and back several times; or the key moves away from the magnet.
- P4 [major · material_response]
  - expect: The key stays a rigid piece of metal and the magnet a hard block; the table does not dent.
  - fail: The key bends as it jumps; or the magnet squashes; or the key melts onto the magnet; or the table dents.
- P5 [fatal · permanence_count]
  - expect: One key and one magnet; the key stays outside the magnet's body; nothing appears, vanishes or passes through the table.
  - fail: A second key appears; or the key vanishes in mid-air; or the key sinks into the magnet; or the magnet passes through the table.
- P6 [minor · attribute_drift]
  - expect: The magnet's colours, the key's shape and the table stay the same.
  - fail: The magnet changes colour; or the key changes shape or size; or the table changes.

## ELEC-0154 · magnet · train

**Caption.** A magnet held to a refrigerator is slid down the door, and it slides and stays stuck the whole way.

**Expectation (hidden).** The magnet moves only while it is pushed and stays on the door when released at any point; it does not drop off.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] A magnet held to a refrigerator door.
- S2 [core] The magnet is slid down the door.
- S3 [core] The magnet stays stuck to the door the whole way.
- S4 [minor] The slide is downward.
- S5 [minor] The magnet stays on the door if released at the end.

**PC**
- P1 [core · missing_consequence]
  - expect: The magnet stays in contact with the door throughout the slide, and holds where it is left when the hand lets go.
  - fail: The magnet lifts off the door during the slide; or drops when released; or slides on by itself after the hand stops; or stands off the door at a gap.
- P2 [core · gravity_direction]
  - expect: The magnet moves only as pushed; if it comes off the door it falls straight down.
  - fail: The magnet floats away from the door; or rises up the door with no hand on it; or hangs in the air after coming off; or drifts sideways away from the door.
- P3 [major · causeless_motion]
  - expect: The magnet moves only while the hand pushes it; other magnets and papers on the door stay put.
  - fail: The magnet slides on after the hand has stopped; or moves before the hand touches it; or other magnets on the door slide or drop; or the door swings open.
- P4 [major · material_response]
  - expect: The magnet stays a rigid piece; the door's surface stays flat and undented along the slide.
  - fail: The magnet squashes or smears along the door; or the door dents or ripples where the magnet passes; or the magnet stretches.
- P5 [fatal · solidity]
  - expect: One magnet on the outside of the door; it does not sink into the door; the hand passes through nothing.
  - fail: The magnet sinks into the door; or a second magnet appears along the path; or the magnet vanishes; or the fingers pass through the magnet.
- P6 [minor · attribute_drift]
  - expect: The magnet's colour and design and the other items on the door stay the same.
  - fail: The magnet changes colour or shape; or notes on the door change; or the door changes colour.

## ELEC-0155 · magnet · train

**Caption.** A magnet is moved toward a steel saucepan on the counter, and the magnet jumps the last gap and clicks onto the pan.

**Expectation (hidden).** The magnet leaps the last small gap and sticks; it stays on the pan when released.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A steel saucepan on a counter.
- S2 [core] A magnet is moved toward the pan.
- S3 [core] The magnet jumps the last gap and lands on the pan.
- S4 [core] The magnet stays on the pan when released.
- S5 [minor] The magnet is moved by hand until the last gap, then jumps on its own.
- S6 [minor] The order is approach, jump, hold.

**PC**
- P1 [core · causeless_motion]
  - expect: The magnet moves only in the hand until the last small gap, jumps that gap onto the pan, and then stays still on it.
  - fail: The magnet jumps from far away; or slides about on the pan after landing; or springs off the pan with nothing pulling it; or the pan slides toward the magnet.
- P2 [core · missing_consequence]
  - expect: Over the last small gap the magnet is drawn onto the pan and stays pressed to it with nothing else holding it once the hand withdraws.
  - fail: The magnet stops a gap short of the pan and hangs there; or drops when the hand lets go; or slides down the pan's side; or bounces off and falls.
- P3 [major · trajectory_momentum]
  - expect: The jump is toward the pan along the line between them, and the magnet stops on contact.
  - fail: The magnet jumps away from the pan; or darts sideways past it; or slides toward and away several times before settling; or keeps moving over the pan's surface after landing.
- P4 [major · causeless_motion]
  - expect: The pan stays where it is on the counter; nothing else on the counter moves.
  - fail: The pan slides or tips as the magnet lands; or the lid rattles or lifts; or other items on the counter shift.
- P5 [fatal · solidity]
  - expect: One magnet on one pan; the magnet touches the pan's surface and does not sink in; the hand passes through nothing.
  - fail: The magnet sinks into the pan; or a second magnet appears; or the magnet vanishes; or the hand passes through the pan.
- P6 [minor · attribute_drift]
  - expect: The magnet's colour, the pan's finish and the counter stay the same.
  - fail: The magnet changes colour or shape; or the pan changes colour; or the counter's contents rearrange.

**Note.** The click is sound and is not judged.

## ELEC-0156 · magnet · train

**Caption.** A screwdriver with a magnetic tip is held to a loose screw, and the screw clings to the tip and is lifted away.

**Expectation (hidden).** The screw hangs from the tip while the driver is moved and does not fall until it is placed into a hole.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] A screwdriver and a loose screw.
- S2 [core] The screwdriver's tip is held to the screw.
- S3 [core] The screw clings to the tip.
- S4 [core] The screw is lifted away on the tip.
- S5 [minor] The screw is loose and not in a hole when picked up.
- S6 [minor] The order is tip to screw, cling, lift.

**PC**
- P1 [core · missing_consequence]
  - expect: When the tip touches the screw's head the screw stays on the tip, hanging from it as the driver is lifted and moved, and does not fall until placed or pulled off.
  - fail: The tip touches the screw and the screw stays behind as the driver lifts; or the screw drops off during the lift with nothing touching it; or the screw hangs a gap from the tip; or the screw stays on the tip while the driver is pushed through it.
- P2 [core · gravity_direction]
  - expect: The screw hangs from the tip in contact with it, its head at the tip; if it comes off it falls downward.
  - fail: The screw hangs in the air below the tip without touching it; or floats up along the shaft; or a screw that comes off drifts sideways or upward; or the screw stands out from the tip pointing upward with no support.
- P3 [major · causeless_motion]
  - expect: The screw moves only with the driver; other screws or parts nearby stay still.
  - fail: The screw hops to the tip from far away; or other screws slide toward the driver; or the screw turns on the tip by itself; or the driver moves with no hand on it.
- P4 [major · material_response]
  - expect: The screw and the tip stay hard and keep their shape; the screw sits on the tip as a separate piece.
  - fail: The screw squashes or bends on the tip; or the tip droops under the screw; or the shaft stretches as it is raised.
- P5 [fatal · permanence_count]
  - expect: One screw on one driver; the screw does not sink into the tip, vanish or duplicate.
  - fail: The screw vanishes from the tip during the lift; or a second screw appears on the tip; or the screw sinks into the shaft; or the driver passes through the workpiece.
- P6 [minor · attribute_drift]
  - expect: The driver's handle colour, the screw's size and the surface beneath stay the same.
  - fail: The handle changes colour; or the screw changes size or type; or the surface changes.

## ELEC-0157 · magnet · train

**Caption.** A steel washer is dropped near a strong magnet on a table, and the washer swerves toward the magnet and sticks to it.

**Expectation (hidden).** The washer's fall bends toward the magnet only when close, and it clicks onto the magnet rather than landing where it was dropped.

**Declared violation types.** trajectory_momentum, causeless_motion

**SA**
- S1 [core] A strong magnet on a table.
- S2 [core] A steel washer is dropped near the magnet.
- S3 [core] The washer swerves toward the magnet as it falls.
- S4 [core] The washer sticks to the magnet.
- S5 [minor] The washer is let go from above, not placed.
- S6 [minor] The drop comes first, the swerve follows, then the sticking.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The washer falls downward and, as it comes close to the magnet, its path bends toward the magnet and ends on its surface.
  - fail: The washer curves away from the magnet; or falls straight to the table and then rises back up to the magnet; or veers in a direction that is neither downward nor toward the magnet; or lands where dropped with the magnet beside it and then slides to it only after coming to rest.
- P2 [core · causeless_motion]
  - expect: The washer on the magnet stays stuck; the magnet stays where it is; nothing else on the table moves.
  - fail: The washer slides about on the magnet or drops off with nothing touching it; or the magnet lifts or turns as the washer lands; or other items on the table hop toward the magnet.
- P3 [major · gravity_direction]
  - expect: The fall is downward; the washer on the magnet is held even on its side; a washer that missed would lie on the table.
  - fail: The washer hovers in the air touching nothing; or drifts upward after release; or hangs beside the magnet without touching it.
- P4 [major · material_response]
  - expect: The washer stays a flat rigid ring and the magnet a hard block; neither dents on contact.
  - fail: The washer bends or folds; or the magnet dents where the washer strikes; or the washer melts onto the magnet.
- P5 [fatal · permanence_count]
  - expect: One washer and one magnet; the washer does not vanish, split or pass into the magnet or the table.
  - fail: The washer vanishes in mid-air; or two washers appear; or the washer sinks into the magnet or through the table; or the magnet changes into another object.
- P6 [minor · attribute_drift]
  - expect: The magnet's colour and shape, the washer's size and the table stay the same.
  - fail: The magnet changes colour; or the washer changes size; or the table surface changes.

## ELEC-0158 · magnet · train

**Caption.** Magnetic tiles are stacked one onto another, and each tile clicks onto the last and the tower stands.

**Expectation (hidden).** Each tile is pulled into place over the last small gap and the assembly holds its shape when lifted.

**Declared violation types.** missing_consequence, gravity_direction

**SA**
- S1 [core] Magnetic tiles.
- S2 [core] The tiles are stacked one onto another.
- S3 [core] Each tile clicks onto the last.
- S4 [core] The stacked tower stands.
- S5 [minor] The tiles are flat pieces stacked face to face or edge to edge.
- S6 [minor] Each tile is placed after the one before it.

**PC**
- P1 [core · missing_consequence]
  - expect: As each tile nears the stack it is drawn over the last small gap into place and stays there; the stack holds together as it is built and if lifted.
  - fail: A tile stops a gap short of the stack and rests there; or slides off after touching; or the stack falls apart when a tile is added; or the stack is lifted and the lower tiles stay behind.
- P2 [core · gravity_direction]
  - expect: The tower stands on the table under its own weight; a tile that is knocked loose falls downward.
  - fail: The tower floats above the table; or a tile hovers beside the stack without touching; or a loose tile rises; or the tower leans far past its base and stands.
- P3 [major · causeless_motion]
  - expect: Tiles move only in the hand and over the last small gap; once placed they stay put and the tower does not shift by itself.
  - fail: A tile jumps to the stack from far away; or tiles rearrange themselves after placing; or the tower slides across the table; or a placed tile spins in place.
- P4 [major · material_response]
  - expect: The tiles are rigid flat pieces that keep their shape; they meet face to face without deforming.
  - fail: A tile bends or flexes; or tiles squash together; or a tile stretches; or the tiles flow into one another.
- P5 [fatal · permanence_count]
  - expect: The tiles in the tower are the tiles that were placed, one at a time; none appear from nowhere, vanish or merge; the tower does not pass through the table.
  - fail: Tiles appear in the tower that were not placed; or a tile vanishes; or two tiles merge into one thick piece; or the tower sinks into the table.
- P6 [minor · attribute_drift]
  - expect: The tiles' colours and shapes and the table stay the same.
  - fail: A tile changes colour once placed; or a tile changes shape; or the table changes.

**Note.** The click is sound and is not judged.

## ELEC-0159 · magnet · train

**Caption.** A travel chess board with magnetic pieces is tilted steeply, and the pieces stay in their squares while a coin placed on the board slides off.

**Expectation (hidden).** The pieces cling to the board even when it is steeply tilted; a non-magnetic coin placed on the board slides off.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] A travel chess board with chess pieces standing on its squares.
- S2 [core] The board is tilted steeply.
- S3 [core] The pieces stay in their squares as the board tilts.
- S4 [core] A coin placed on the board slides off it.
- S5 [minor] The tilt is steep: the board ends up far from level.
- S6 [minor] The coin slides while the board is tilted, not before it.

**PC**
- P1 [core · missing_consequence]
  - expect: As the board tilts, and while it is held tilted, every piece stays on its own square, standing on the board with nothing but the board touching it.
  - fail: Pieces slide down the board as it tilts; or topple and roll toward the lower edge; or drop off the board; or lift away from the board and hang in the air.
- P2 [core · gravity_direction]
  - expect: The coin slides down the slope toward the board's lower edge and drops from that edge, falling downward.
  - fail: The coin moves up the slope; or slides off the board's upper edge; or leaves the lower edge and travels upward or stays in the air; or begins to slide and then halts part-way down with nothing touching it.
- P3 [major · causeless_motion]
  - expect: The pieces move only with the board: none changes square, spins or hops on its own, and the board moves only while the hands tilt it.
  - fail: A piece changes square while the board is held still; or a piece turns in place with nothing touching it; or the board tilts further or rights itself with no hand moving it.
- P4 [major · trajectory_momentum]
  - expect: The coin travels in one line down the slope, leaves the edge, lands below the board and comes to rest.
  - fail: The coin zigzags across the slope or reverses direction before reaching the edge; or slides off and returns onto the board; or, after landing, moves back toward the board.
- P5 [fatal · permanence_count]
  - expect: The pieces and the coin keep their number and shapes throughout; nothing sinks into the board or passes through it.
  - fail: A piece vanishes or a new piece appears; or two pieces merge or a piece turns into a different piece; or the coin passes through the board or a piece; or the coin vanishes before reaching the table.
- P6 [minor · attribute_drift]
  - expect: The pieces' colours, the board's squares and the coin's face stay the same.
  - fail: A piece changes colour; or the board's squares change pattern; or the coin changes colour or size.

## ELEC-0160 · magnet · train

**Caption.** A scrapyard crane lowers a large round magnet onto a pile of scrap steel and lifts, and a clump of steel rises with it.

**Expectation (hidden).** The steel pieces cling to the magnet's underside as it rises and drop all at once when the magnet is switched off over the truck.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] A scrapyard crane with a large round magnet hanging from it.
- S2 [core] A pile of scrap steel below the magnet.
- S3 [core] The magnet is lowered onto the pile.
- S4 [core] The magnet lifts and a clump of scrap rises with it, hanging from its underside.
- S5 [minor] The magnet is a large round disc.
- S6 [minor] The order is lower, touch the pile, lift.

**PC**
- P1 [core · missing_consequence]
  - expect: When the magnet lifts off the pile, pieces of scrap come up with it, held against its underside and touching it.
  - fail: The magnet rises with nothing attached; or scrap rises beside the magnet with a gap between them; or pieces leave the pile and rise while the magnet is still high above it and not descending.
- P2 [core · gravity_direction]
  - expect: The held scrap hangs from the underside of the magnet, below it; pieces that come loose during the lift fall straight down onto the pile.
  - fail: Scrap sits on top of the magnet or clings to its cable; or a loose piece drifts upward or sideways after separating; or a piece hangs in the air below the clump without touching it.
- P3 [major · causeless_motion]
  - expect: The rest of the pile stays as it was; only scrap where the magnet touched is disturbed.
  - fail: Scrap elsewhere in the pile shifts or jumps as the magnet lifts with nothing touching it; or the whole pile heaves; or pieces on the ground slide toward the crane.
- P4 [major · material_response]
  - expect: The cable hangs straight and taut from the boom to the magnet while the magnet hangs from it; the scrap pieces stay rigid metal and keep their bent shapes.
  - fail: The cable goes slack and curls while the magnet hangs from it; or the cable stretches like elastic as the load lifts; or scrap pieces sag or flow like dough.
- P5 [major · gravity_direction] (if: The magnet releases its load during the clip.)
  - expect: When the magnet lets go, all the held pieces drop at once, straight down, and land below the magnet.
  - fail: Released pieces hang in the air below the magnet; or drift upward or sideways as they fall; or land and then bounce back up onto the magnet.
- P6 [fatal · permanence_count]
  - expect: One magnet on one cable; scrap pieces keep their number and shapes and stay outside the magnet; the magnet does not pass into the pile.
  - fail: Scrap pieces multiply on the magnet as it rises; or pieces vanish in mid-air; or the magnet sinks into the pile and rises through it; or the clump merges into one smooth mass.
- P7 [minor · attribute_drift]
  - expect: The magnet's colour, the crane and the yard behind stay the same.
  - fail: The magnet changes colour or size; or the crane's boom changes shape; or the untouched parts of the pile change contents.

## ELEC-0161 · magnet · train

**Caption.** A magnetic name badge is placed on a jacket hanging on a hook by putting the magnet inside the fabric, and the badge holds in place.

**Expectation (hidden).** The badge stays put through the cloth without piercing it and does not slide down; it comes off only when the inner magnet is pulled away.

**Declared violation types.** gravity_direction, solidity

**SA**
- S1 [core] A jacket hangs on a hook.
- S2 [core] A name badge is placed on the outside of the jacket.
- S3 [core] A magnet is put inside the jacket, behind the fabric beneath the badge.
- S4 [core] The badge holds in place after the hands withdraw.
- S5 [minor] The badge is a name badge: a small flat plate or label.
- S6 [minor] The order is badge placed, magnet inside, hands away, badge holds.

**PC**
- P1 [core · solidity]
  - expect: The badge and the inner magnet sit on opposite faces of the cloth with the fabric between them: the badge stays outside and the magnet inside, and neither passes through the jacket.
  - fail: The badge sinks into the fabric; or the inner magnet, once inside, emerges through the cloth beside the badge; or badge and magnet are seen touching with no cloth between them; or the badge passes through the jacket and hangs inside it.
- P2 [core · gravity_direction]
  - expect: After the hands withdraw the badge stays where it was placed on the hanging jacket, flat against the cloth with nothing visible supporting it.
  - fail: The badge drops to the floor as the hands leave; or slides down the jacket front; or lifts off the cloth and hangs in the air; or the inner magnet falls out of the jacket while the badge stays on.
- P3 [major · material_response]
  - expect: The jacket is cloth: it dimples or wrinkles where badge and magnet press it, hangs from the hook and swings when touched.
  - fail: The fabric stays board-stiff and flat while pushed on; or stretches and sags like elastic below the badge; or the jacket stands out rigid instead of hanging.
- P4 [major · causeless_motion]
  - expect: Once placed the badge stays still on the jacket; the jacket swings only when hands touch it and then comes to rest.
  - fail: The badge creeps across the jacket after the hands leave; or turns on its own; or the jacket, hanging still, starts swinging with nothing touching it.
- P5 [fatal · permanence_count]
  - expect: One badge, one inner magnet, one jacket and one hook; the jacket stays on the hook; hands pass through nothing.
  - fail: A second badge appears; or the badge vanishes; or the jacket passes through the hook and falls; or a hand passes through the jacket; or the hook detaches from the wall.
- P6 [minor · attribute_drift]
  - expect: The badge's lettering and colour, the jacket's colour and the hook stay the same.
  - fail: The badge's lettering changes; or the jacket changes colour; or the hook moves along the wall.

## ELEC-0162 · magnet · train

**Caption.** A door blown open by a draught swings until it reaches a magnetic doorstop, and the door snaps to the stop and holds open.

**Expectation (hidden).** The door pulls onto the stop over the last small gap and stays there; it does not drift closed on its own.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A door swings toward open.
- S2 [core] A magnetic doorstop stands at the end of the door's travel, on the floor or wall.
- S3 [core] The door reaches the stop and snaps onto it.
- S4 [core] The door holds open on the stop.
- S5 [minor] No hand pushes the door: it swings as if blown.
- S6 [minor] The swing comes first, the snap onto the stop follows, and the hold comes last.

**PC**
- P1 [core · missing_consequence]
  - expect: As the door nears the stop it closes the last gap onto it and comes to rest touching it.
  - fail: The door reaches the stop and bounces back off it; or halts a gap short of the stop and hangs there; or swings on past where the stop stands; or rests held open with door and stop not touching.
- P2 [core · causeless_motion]
  - expect: Once on the stop the door stays held open for the rest of the clip; it does not drift or swing closed with nothing touching it.
  - fail: The door swings back toward closed after coming to rest on the stop; or rocks open and shut on the stop; or jumps to a different angle between one moment and the next.
- P3 [major · trajectory_momentum]
  - expect: The door swings about its hinges as one panel, in one direction toward the stop, its free edge sweeping an arc.
  - fail: The door reverses and swings toward closed before it has reached the stop; or the hinge side moves along the frame; or the door moves away from the frame as a whole.
- P4 [major · material_response]
  - expect: The door is a rigid panel that keeps its flat shape through the swing; the stop stays fixed to the floor or wall as the door lands on it.
  - fail: The door bends or ripples as it swings; or the stop slides across the floor when the door meets it; or the door's edge squashes against the stop.
- P5 [fatal · solidity]
  - expect: One door on its hinges and one stop; the door passes through neither wall, furniture nor stop, and stays attached to its frame.
  - fail: The door passes through the wall or a piece of furniture; or the stop vanishes or reappears in a new spot; or a second door appears; or the door detaches from its frame.
- P6 [minor · attribute_drift]
  - expect: The door's colour and handle, the floor and the stop stay the same.
  - fail: The door changes colour; or the handle changes side or shape; or the floor pattern changes.

**Note.** The draught is invisible: the door beginning to swing with nothing visible pushing it is not a violation. What is judged is the arrival onto the stop and the door staying there.

## ELEC-0163 · magnet · train

**Caption.** A magnet is brought near a compass, and the needle swings to point at the magnet.

**Expectation (hidden).** The needle turns only as the magnet approaches and follows the magnet as it moves; it does not move before the magnet is near.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A compass with a visible needle.
- S2 [core] A magnet is brought near the compass.
- S3 [core] The needle swings round to point at the magnet.
- S4 [minor] It is the magnet that moves toward the compass, not the compass toward the magnet.
- S5 [minor] The approach comes first and the needle's swing follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The needle rests until the magnet comes near, then turns as the magnet approaches; while the magnet is held still the needle settles and stays.
  - fail: The needle spins or swings while the magnet is far off and not moving; or keeps turning after the magnet has stopped and the needle has already settled once; or the compass housing turns while the needle stays fixed to it.
- P2 [core · missing_consequence]
  - expect: With the magnet near, the needle lines up along the line from its pivot to the magnet, one end toward it, and turns to follow the magnet as it moves round.
  - fail: The needle keeps its old heading as the magnet arrives beside the compass; or settles across the line to the magnet rather than along it; or turns the opposite way to the magnet as the magnet circles the compass.
- P3 [major · material_response]
  - expect: The needle stays one straight rigid bar turning about its centre pivot.
  - fail: The needle bends or curls as it turns; or turns about one of its ends; or slides off the pivot across the dial.
- P4 [major · causeless_motion]
  - expect: The compass housing and the dial markings stay put; the needle alone turns; other items on the table stay still.
  - fail: The dial markings rotate along with the needle; or the compass housing lifts off the table; or paper or plastic items on the table shift as the magnet passes.
- P5 [fatal · permanence_count]
  - expect: One magnet and one compass with one needle; the magnet stays outside the compass.
  - fail: A second needle appears; or the needle vanishes; or the magnet passes into the compass housing; or the magnet duplicates or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The dial's markings, the magnet's colour and the table stay the same.
  - fail: The dial's letters change or move; or the magnet changes colour or shape; or the table surface changes.

**Note.** Either end of the needle may point at the magnet; which end is not judged.

## ELEC-0164 · magnet · train

**Caption.** A magnetic wand is dragged over a tray of iron filings, and the filings clump onto the wand in fuzzy bristles.

**Expectation (hidden).** The filings jump to the wand as it passes near and hang from it in spikes; they fall off when the wand is set down away from them.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A tray of iron filings.
- S2 [core] A magnetic wand is dragged over the tray.
- S3 [core] Filings gather onto the wand.
- S4 [minor] The gathered filings stand off the wand as fuzzy bristles or spikes.
- S5 [minor] The wand's pass comes first and the clumping follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The filings lie still until the wand comes over them and gather only where the wand is close; filings away from the wand stay put, and stay put after it has passed.
  - fail: Filings rise or crawl toward the wand while it is still across the tray from them; or the whole tray of filings stirs at once; or filings jump up where the wand has not been; or filings in the tray keep shifting after the wand has left the tray.
- P2 [core · gravity_direction]
  - expect: Filings on the wand hang from it and stand out from it in spikes, in contact with it; any that come loose fall down into the tray.
  - fail: Loose filings drift upward or float in the air away from the wand; or filings hang in a cloud below the wand without touching it; or filings that drop off fall sideways or upward.
- P3 [major · material_response]
  - expect: The bristles are short stiff spikes standing out from the wand; the filings remain separate grains and the tray stays rigid.
  - fail: The filings coat the wand as a smooth paint-like skin; or run up the wand like a liquid; or the tray bends as the wand passes over it.
- P4 [major · trajectory_momentum]
  - expect: The clumps travel with the wand as it moves, staying attached; the tray stays where it is.
  - fail: Clumps stay hanging in mid-air where the wand was after it has moved on; or the tray slides along beneath the wand; or filings on the wand crawl along it toward one end while the wand is held level.
- P5 [fatal · permanence_count]
  - expect: One wand and one tray; filings leave the tray only onto the wand and return only by falling; the wand does not pass through the tray.
  - fail: The wand passes through the tray's rim or bottom; or a second wand appears; or the clumps vanish from the wand in mid-air with nothing falling; or the tray's filings disappear without being on the wand.
- P6 [minor · attribute_drift]
  - expect: The wand's colour and length, the tray and the surface it sits on stay the same; the filings stay dark grey.
  - fail: The wand changes colour or length; or the filings change colour; or the tray changes shape or pattern.

## ELEC-0165 · magnet · train

**Caption.** A handful of steel pins is dropped near a magnet, and the pins swing toward it as they fall and stick along its sides.

**Expectation (hidden).** The pins deviate from a straight fall only close to the magnet and end up clinging to it; those that fall far away land normally.

**Declared violation types.** trajectory_momentum, causeless_motion

**SA**
- S1 [core] A magnet is present.
- S2 [core] A handful of steel pins is dropped near it.
- S3 [core] The falling pins swing toward the magnet.
- S4 [core] Pins end up stuck along the magnet's sides.
- S5 [minor] The pins are let go together as a handful, not placed one by one.
- S6 [minor] The drop comes first; the swing and the sticking follow.

**PC**
- P1 [core · trajectory_momentum]
  - expect: Each pin falls downward and, as it comes close to the magnet, its path bends toward the magnet's body and ends on its surface.
  - fail: Pins curve away from the magnet; or fall straight past it onto the surface below and then rise back up to it; or veer in a direction that is neither downward nor toward the magnet.
- P2 [core · causeless_motion]
  - expect: Pins stuck on the magnet stay stuck; pins that land away from it lie where they fall; the magnet stays where it is.
  - fail: Pins on the magnet crawl over it or drop off while nothing touches it; or pins lying on the table hop back into the air; or the magnet lifts or turns with nothing touching it.
- P3 [major · gravity_direction]
  - expect: The pins fall downward; those that miss the magnet land on the surface below, and the pins on the magnet hang along its sides or lie on top of it.
  - fail: Pins float in the air touching nothing; or drift upward after release; or pins that missed the magnet stay suspended above the table.
- P4 [major · material_response]
  - expect: The pins stay straight rigid pins and the magnet stays a hard block; the pins attach with their sides or tips on the magnet's surface.
  - fail: Pins bend or curl in flight or on the magnet; or the magnet's body dents where pins strike; or pins soften and drape over the magnet's edges like threads.
- P5 [fatal · permanence_count]
  - expect: The pins that were dropped are the pins that end on the magnet and on the table; none passes into the magnet or through the table.
  - fail: Pins vanish in mid-air; or new pins appear on the magnet without having fallen; or a pin passes into the magnet's body; or pins pass through the table.
- P6 [minor · attribute_drift]
  - expect: The magnet's colour and shape, the table and any background items stay the same.
  - fail: The magnet changes colour; or changes shape; or the table surface changes pattern.

## ELEC-0166 · magnet · train

**Caption.** A magnetic hook is hung on the side of a steel filing cabinet and a coat hung on it, and the hook holds.

**Expectation (hidden).** The hook stays on the vertical steel with the coat's weight and does not slide down or fall.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] A steel filing cabinet with a flat vertical side.
- S2 [core] A magnetic hook is placed on the side of the cabinet.
- S3 [core] A coat is hung on the hook.
- S4 [core] The hook stays on the cabinet with the coat hanging from it.
- S5 [minor] The hook is on the cabinet's vertical side, not its top.
- S6 [minor] The order is hook placed, coat hung, hook holds.

**PC**
- P1 [core · missing_consequence]
  - expect: Once let go, the hook stays where it was placed on the vertical side, touching the steel, and keeps its place when the coat's weight comes onto it.
  - fail: The hook drops when released; or slides down the side, before or after the coat is hung; or stands off the steel with a gap between; or wanders across the side.
- P2 [core · gravity_direction]
  - expect: The coat hangs downward from the hook, its weight pulling straight down; if anything gives way, hook and coat fall to the floor.
  - fail: The coat hangs out sideways or rises from the hook; or floats when let go; or the coat's loop hangs in the air below the hook without touching it; or the hook comes off the cabinet and stays in the air.
- P3 [major · material_response]
  - expect: The coat is cloth: it drapes from the hook in folds, swings when let go and settles; the hook stays rigid and the cabinet's side stays flat.
  - fail: The coat stands stiff and flat like a board; or stretches downward like elastic; or the hook bends under the coat; or the cabinet's side dents around the hook.
- P4 [major · causeless_motion]
  - expect: The coat swings only when handled and comes to rest; the hook does not move after release; the cabinet stays put.
  - fail: The coat, hanging still, starts swinging with nothing touching it; or the hook rotates or jumps to a new spot; or the cabinet slides or tips.
- P5 [fatal · solidity]
  - expect: One hook, one coat and one cabinet; the hook's base rests on the steel without sinking in; the coat does not pass through the hook or the cabinet.
  - fail: The hook sinks into the cabinet's side; or the coat passes through the hook and stays hung; or a second hook or coat appears; or the coat vanishes.
- P6 [minor · attribute_drift]
  - expect: The cabinet's colour and drawer fronts, the hook's colour and the coat's colour stay the same.
  - fail: The coat changes colour; or the drawer handles change; or the hook changes shape or colour.

## ELEC-0167 · magnet · train

**Caption.** A magnet is held against a plastic toy and released, and the magnet falls to the floor.

**Expectation (hidden).** The magnet does not stick to the plastic and drops straight down when released; against a steel toy it would hold.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] A plastic toy.
- S2 [core] A magnet is held against the toy.
- S3 [core] The magnet is released: the hand lets go.
- S4 [core] The magnet falls to the floor.
- S5 [minor] The toy looks like moulded plastic.
- S6 [minor] The order is hold, release, fall.

**PC**
- P1 [core · missing_consequence]
  - expect: The instant the hand opens, the magnet leaves the plastic surface and begins to fall.
  - fail: The magnet stays on the plastic after release with nothing supporting it; or creeps down the toy's surface still in contact with it; or hangs at a gap from the toy; or the toy lifts away with the magnet.
- P2 [core · gravity_direction]
  - expect: The magnet falls straight down from where it was let go and comes to rest on the floor below.
  - fail: The magnet drifts upward or sideways after release; or halts in mid-air; or lands and then rises back up to the toy.
- P3 [major · causeless_motion]
  - expect: The toy stays put as the magnet is released and falls; once landed the magnet lies still.
  - fail: The toy tips, slides or lifts as the magnet drops; or the landed magnet slides toward the toy with nothing pushing it; or the magnet starts moving again after coming to rest.
- P4 [major · material_response]
  - expect: The toy and the magnet keep their shapes; the floor stays flat where the magnet lands.
  - fail: The toy stays dented after the magnet has left it; or the magnet squashes or flattens on landing; or the floor dents under the magnet.
- P5 [fatal · permanence_count]
  - expect: One magnet and one toy; the magnet passes through neither the toy nor the floor and does not vanish on the way down.
  - fail: The magnet vanishes in mid-fall; or a second magnet appears; or the magnet passes into the toy or through the floor; or the toy turns into another object.
- P6 [minor · attribute_drift]
  - expect: The toy's colours, the magnet's colour and shape and the floor stay the same.
  - fail: The toy changes colour; or the magnet changes shape or colour between release and landing; or the floor pattern changes.

**Note.** P1 assumes the toy shown is plastic, as the caption says. A toy that plainly reads as metal fails S1 and S5; the magnet holding on such a toy is then not a P1 failure.

## ELEC-0168 · magnet · train

**Caption.** The two ends of a bracelet with a magnetic clasp are brought close on a table, and they jump together and hold.

**Expectation (hidden).** The ends pull together over the last small gap and stay joined when the bracelet is lifted.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A bracelet lies on a table with its two ends apart.
- S2 [core] The two ends are brought close together.
- S3 [core] The ends jump together and join.
- S4 [core] The joined ends hold together.
- S5 [minor] The bracelet has a clasp at its ends: it is the end pieces that meet.
- S6 [minor] The order is apart, brought close, jump together, hold.

**PC**
- P1 [core · causeless_motion]
  - expect: The ends lie still until they are brought close; the jump happens only when the two clasp pieces are next to each other.
  - fail: The ends creep toward each other before either is touched or moved; or the bracelet moves along the table with no hand on it; or the joined ends spring apart with nothing pulling on them.
- P2 [core · missing_consequence]
  - expect: Over the last small gap the clasp pieces snap into contact and stay pressed together; if the bracelet is lifted it hangs as a closed loop.
  - fail: The ends stop with a gap between them and stay that way; or touch and then slide apart on the table; or the clasp opens as the bracelet is lifted with nothing pulling on it.
- P3 [major · trajectory_momentum]
  - expect: The jump is along the line joining the two clasp pieces, toward each other, and they meet face to face.
  - fail: One end jumps away from the other; or an end darts sideways past its partner; or the ends slide toward and away from each other several times before joining.
- P4 [major · material_response]
  - expect: The band bends as a chain or strap and lies on the table; the clasp pieces stay hard and keep their shape as they meet.
  - fail: The band stands rigid off the table like a bar; or stretches like elastic as an end is drawn along; or a clasp piece flattens as it meets its partner.
- P5 [fatal · permanence_count]
  - expect: One bracelet with two ends; the ends join by touching and remain two pieces; the hand passes through nothing.
  - fail: The two ends merge into a single piece with no seam; or the bracelet splits into more pieces; or an end vanishes; or the fingers pass through the bracelet.
- P6 [minor · attribute_drift]
  - expect: The bracelet's colour, its links and clasp shape and the table surface stay the same.
  - fail: The bracelet changes colour; or the links change pattern; or the table surface changes.

## ELEC-0169 · magnet · train

**Caption.** A steel bolt is tossed toward a strong magnet fixed to a workbench, and the bolt swerves and clacks onto the magnet.

**Expectation (hidden).** The bolt's path bends toward the magnet only when close and it stops dead on contact; a plastic bolt thrown the same way would fly past.

**Declared violation types.** trajectory_momentum, causeless_motion

**SA**
- S1 [core] A magnet fixed to a workbench.
- S2 [core] A steel bolt is tossed toward the magnet.
- S3 [core] The bolt's flight swerves toward the magnet.
- S4 [core] The bolt lands on the magnet and stays there.
- S5 [minor] The bolt travels through the air: it is thrown, not placed by hand.
- S6 [minor] The toss comes first, the swerve follows, then the landing.

**PC**
- P1 [core · trajectory_momentum]
  - expect: The bolt flies from the toss along a downward-sagging arc; as it nears the magnet its path bends toward the magnet and ends on its surface.
  - fail: The bolt bends away from the magnet; or flies past it and then turns back; or curves toward a place on the bench other than the magnet and stops there.
- P2 [core · causeless_motion]
  - expect: On contact the bolt stops on the magnet and stays there; the magnet stays fixed to the bench and the bolt does not move again.
  - fail: The bolt bounces off the magnet and lands away from it; or keeps sliding across the magnet after landing; or drops off the magnet while nothing touches it; or the magnet shifts on the bench when the bolt hits.
- P3 [major · gravity_direction]
  - expect: The flight sags downward; a bolt that misses falls to the bench or floor; a bolt on the magnet stays held even on the magnet's side.
  - fail: The bolt climbs steadily through its flight with no downward arc; or hangs in the air; or a missed bolt floats instead of falling.
- P4 [major · material_response]
  - expect: The bolt stays a rigid piece of steel and does not bend or squash on hitting the magnet; the magnet and bench keep their shape.
  - fail: The bolt bends or crumples on impact; or the magnet's face dents where the bolt hits; or the bench surface ripples.
- P5 [fatal · permanence_count]
  - expect: One bolt and one magnet fixed to the bench; the bolt does not pass into the magnet or the bench, does not split and does not vanish.
  - fail: The bolt vanishes in flight; or two bolts appear; or the bolt sinks into the magnet or through the bench; or the magnet leaves the bench and follows the bolt.
- P6 [minor · attribute_drift]
  - expect: The magnet's colour, the bench top and the tools on it stay the same; the bolt keeps its size.
  - fail: The magnet changes colour or shape; or tools on the bench move or vanish; or the bolt changes size between toss and landing.

## ELEC-0170 · magnet · train

**Caption.** One block is lifted out of a box of magnetic building blocks, and the others cling to it in a hanging chain.

**Expectation (hidden).** Lifting one block lifts those stuck to it in a hanging chain; the chain breaks where the pull exceeds the hold.

**Declared violation types.** missing_consequence, gravity_direction

**SA**
- S1 [core] A box of magnetic building blocks.
- S2 [core] One block is lifted out of the box.
- S3 [core] Other blocks come up with it, hanging from it in a chain.
- S4 [minor] The chain hangs below the lifted block, one block from another.
- S5 [minor] The lift comes first and the chain forms as the block rises.

**PC**
- P1 [core · missing_consequence]
  - expect: As the lifted block rises, blocks in contact with it come up too, each held to the one above, forming a chain that hangs from the lifted block.
  - fail: The top block comes up alone while the blocks that were touching it stay behind; or blocks rise alongside it with gaps between them; or blocks leave the box before the top block has moved.
- P2 [core · gravity_direction]
  - expect: The chain hangs downward from the lifted block; a block that lets go falls down into the box or onto the table.
  - fail: Blocks stand up above the lifted block or trail off sideways in the air; or a block that comes loose floats or drifts upward; or a detached block hangs in the air below the chain without touching it.
- P3 [major · trajectory_momentum]
  - expect: The hanging chain swings beneath the lifted block as it moves and settles below it.
  - fail: The chain stays fixed in the air where it was while the top block moves on; or the chain swings with nothing touching it while the top block is held still; or the lower blocks move before the top block does.
- P4 [major · causeless_motion]
  - expect: The blocks left in the box stay still as the chain lifts away; the box stays where it is.
  - fail: Blocks left in the box shift or rearrange as the chain rises with nothing touching them; or the box slides across the table; or a chained block spins on its own while the rest of the chain hangs still.
- P5 [fatal · permanence_count]
  - expect: The blocks keep their number and shapes; those in the chain plus those in the box are the blocks that were in the box; no block passes through another or through the box.
  - fail: Blocks appear in the chain that were not in the box; or blocks vanish in mid-air; or two blocks merge into one longer piece; or a block passes through the box's wall.
- P6 [minor · attribute_drift]
  - expect: The blocks keep their colours; the box and the table stay the same.
  - fail: A block changes colour as it rises; or the box changes pattern; or the table surface changes.

## ELEC-0171 · magnet · train

**Caption.** A magnet is stuck to a steel lamp post with a lost-cat poster under it, and the poster stays up.

**Expectation (hidden).** The magnet holds the poster on the curved steel; the poster flaps in the wind but does not fall.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] A steel lamp post.
- S2 [core] A poster is held against the post.
- S3 [core] A magnet is stuck onto the post over the poster.
- S4 [core] The poster stays up after the hand withdraws.
- S5 [minor] The poster is a lost-cat notice: a picture or words about a cat.
- S6 [minor] The magnet lies over the poster, pinning it to the post.

**PC**
- P1 [core · missing_consequence]
  - expect: After the hand withdraws the magnet stays on the post with the poster pinned beneath it, both touching the post.
  - fail: The magnet drops off when released; or slides down the post; or stands off the post at a gap with the poster hanging between; or the magnet stays but the poster slips out from under it.
- P2 [core · gravity_direction]
  - expect: The poster hangs down from the magnet along the post; free edges and corners may lift in the wind and fall back; anything that comes loose falls.
  - fail: The poster slides up the post or floats away upward; or a torn-off piece drifts upward rather than falling; or the poster stands out sideways from the magnet like a flag while nothing else in the scene moves.
- P3 [major · causeless_motion]
  - expect: The magnet, once placed, stays at its spot; the poster moves only as flaps at its free edges; the post stands still.
  - fail: The magnet creeps round or along the post; or the poster slides sideways round the post while the magnet stays put; or the lamp post sways or shifts.
- P4 [major · material_response]
  - expect: The poster bends as paper: it wraps to the post where pinned and its free parts flutter and fall back; the magnet stays hard.
  - fail: The poster stretches like rubber when tugged; or hangs and sways in heavy folds like wet cloth; or the magnet flattens and spreads on the post.
- P5 [fatal · solidity]
  - expect: One magnet, one poster and one post, layered magnet on poster on post; nothing sinks into or passes through the post.
  - fail: The magnet sinks into the post; or the poster passes through the post or the magnet; or a second magnet or poster appears; or the poster vanishes.
- P6 [minor · attribute_drift]
  - expect: The poster's picture and text, the magnet's colour and the post's paint stay the same.
  - fail: The cat picture or lettering changes; or the magnet changes colour; or the post changes colour.

## ELEC-0172 · magnet · train

**Caption.** A magnet is moved in circles under a shallow dish of water with a paperclip floating on a piece of foam, and the clip follows the magnet around the dish.

**Expectation (hidden).** The foam boat moves only where the magnet below moves and stops when it stops; the magnet stays under the dish.

**Declared violation types.** causeless_motion, solidity

**SA**
- S1 [core] A shallow dish of water with a paperclip riding on a piece of foam floating on it.
- S2 [core] A magnet is moved in circles beneath the dish.
- S3 [core] The clip on its foam follows the magnet round the dish.
- S4 [minor] The dish is shallow, with the water surface in view.
- S5 [minor] The magnet is under the dish, not in the water.
- S6 [minor] The magnet's movement comes first and the clip follows it.

**PC**
- P1 [core · causeless_motion]
  - expect: The foam with its clip moves only where and when the magnet below moves, staying above it, and stops when the magnet stops.
  - fail: The clip moves in a different direction from the magnet beneath it; or keeps circling after the magnet has stopped; or stays still while the magnet passes beneath it; or the clip sets off before the magnet has begun to move.
- P2 [core · solidity]
  - expect: The magnet stays beneath the dish's bottom, outside the water; the clip rides on top of the foam at the surface.
  - fail: The magnet passes up through the dish bottom into the water; or the clip sinks through the foam; or the clip passes through the dish's wall; or the magnet is seen inside the water.
- P3 [major · gravity_direction]
  - expect: The foam floats level on the surface; the water stays in the dish with a flat surface apart from ripples.
  - fail: The foam sinks below the surface while moving; or the water heaps up on one side of the dish while the dish is still; or the foam lifts off the water into the air.
- P4 [major · causeless_motion]
  - expect: The dish stays still on the table; the water moves only as ripples and eddies from the moving foam.
  - fail: The dish slides or rotates on the table; or the water swirls as a whole before the foam moves; or other items on the table shift as the magnet passes.
- P5 [fatal · permanence_count]
  - expect: One magnet, one clip, one piece of foam and one dish; the clip stays on its foam; nothing appears, vanishes or merges.
  - fail: A second clip or magnet appears; or the foam vanishes leaving the clip afloat by itself; or clip and foam fuse into one object; or the dish changes shape.
- P6 [minor · attribute_drift]
  - expect: The dish's colour, the foam's and clip's colours and the table surface stay the same.
  - fail: The foam changes colour or size; or the clip changes shape; or the dish's pattern changes.

**Note.** The magnet may be hidden by the dish for parts of the clip; P1 is judged on the moments when both magnet and clip are in view. The clip moving while no magnet is in view is not a violation.

## ELEC-0173 · magnet · train

**Caption.** A magnet is dropped into a bowl of dry rice mixed with steel ball bearings and pulled out again, and the bearings cling to it while the rice falls away.

**Expectation (hidden).** Only the bearings come out on the magnet; rice grains fall back into the bowl.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A bowl of dry rice with steel ball bearings mixed through it.
- S2 [core] A magnet is dropped into the bowl.
- S3 [core] The magnet is pulled out again.
- S4 [core] Bearings cling to the magnet as it comes out while rice falls away.
- S5 [minor] The rice is dry, loose grains.
- S6 [minor] The order is drop in, pull out, bearings on the magnet.

**PC**
- P1 [core · missing_consequence]
  - expect: As the magnet rises out of the rice, bearings that touched it come up clinging to its surface while the rice grains fall off.
  - fail: The magnet comes out bare with bearings lying at the surface where it was; or rice grains hang from the magnet's bare surface in the air; or bearings rise out of the rice alongside the magnet without touching it.
- P2 [core · permanence_count]
  - expect: The bearings on the magnet are bearings from the bowl; rice and bearings keep their number and kind, neither appearing, vanishing nor turning into the other.
  - fail: The bearings on the magnet multiply as it rises; or bearings vanish from the magnet in the air with nothing falling; or rice grains turn into bearings or bearings into rice; or the bowl's contents jump in level or empty out.
- P3 [major · gravity_direction]
  - expect: Rice carried up with the magnet falls back down into the bowl; bearings hang on the magnet's underside and sides; a bearing that comes off drops.
  - fail: Rice grains rise or hover after leaving the magnet; or a bearing that comes off drifts sideways or upward; or grains stream down from the magnet and then curve back up.
- P4 [major · material_response]
  - expect: The rice behaves as loose grains: the magnet sinks in and parts it, the surface is disturbed where the magnet entered, and grains pour off the magnet in streams.
  - fail: The rice surface is unmarked after the magnet has been in and out; or the rice lifts as one solid slab; or the grains stretch or smear like a paste.
- P5 [fatal · solidity]
  - expect: One magnet and one bowl; the magnet enters the rice, not the bowl's wall; the bowl keeps its shape and the hand passes through nothing.
  - fail: The magnet passes through the bowl's bottom or side; or the bowl changes shape; or a second magnet appears; or the hand passes through the bowl's rim.
- P6 [minor · attribute_drift]
  - expect: The bowl's colour, the magnet's colour and shape and the rice's colour stay the same.
  - fail: The bowl changes colour or pattern; or the magnet changes shape between entering and emerging; or the rice changes colour.

## ELEC-0174 · magnet · train

**Caption.** A laptop lid is lowered, and it snaps shut over the last small gap and stays closed thanks to the magnets inside.

**Expectation (hidden).** The lid is drawn closed at the end of its travel and does not spring open on its own.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] An open laptop.
- S2 [core] The lid is lowered toward the base.
- S3 [core] Over the last small gap the lid closes onto the base.
- S4 [core] The lid stays closed.
- S5 [minor] The final gap closes as a snap: the lid completes its travel after the hand stops pushing.
- S6 [minor] The order is lower, snap shut, stay closed.

**PC**
- P1 [core · causeless_motion]
  - expect: The lid moves down while it is being lowered and, on its own, only over the last small gap; left standing at a wide angle it stays there.
  - fail: The lid, left standing at a wide angle, swings shut with nothing touching it; or reverses and rises while the hand still presses it down; or swings open and shut several times before closing.
- P2 [core · missing_consequence]
  - expect: Once the lid reaches the last small gap it closes fully onto the base and stays shut for the rest of the clip.
  - fail: The lid stops a gap short of closed and rests there; or springs back open after touching the base; or bounces open and shut on the base; or opens again by itself later in the clip.
- P3 [major · material_response]
  - expect: The lid stays a rigid flat panel hinged at the back; its front edge comes down onto the base's front edge.
  - fail: The lid bends or bows as it closes; or one corner rests shut while the other stands open; or the hinge side lifts off the base as the front closes; or the lid slides across the base rather than hinging down.
- P4 [major · causeless_motion]
  - expect: The base and the things beside it stay still as the lid snaps shut.
  - fail: The base slides or tips on the desk as the lid comes down; or a mouse, cup or papers beside the laptop jump at the snap; or the laptop turns on the desk.
- P5 [fatal · solidity]
  - expect: One laptop with one lid and one base; the lid closes onto the base without passing into it; the hand passes through nothing.
  - fail: The lid sinks into the base; or the lid detaches from its hinge; or a second laptop or lid appears; or fingers pass through the lid.
- P6 [minor · attribute_drift]
  - expect: The laptop's colour, its logo and stickers, and the desk stay the same.
  - fail: The lid changes colour; or a logo or sticker moves or vanishes; or the desk surface changes.

## ELEC-0175 · magnet · train

**Caption.** A magnetic letter is stuck to a fridge and holds; the same letter is stuck to the wooden cupboard next to it and falls off.

**Expectation (hidden).** The letter stays on the steel door and drops straight down from the wood; the same letter behaves differently on the two surfaces.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] A fridge and a wooden cupboard side by side.
- S2 [core] A magnetic letter is pressed to the fridge and holds when let go.
- S3 [core] The same letter is pressed to the wooden cupboard.
- S4 [core] The letter falls off the cupboard.
- S5 [minor] One and the same letter is used on both surfaces.
- S6 [minor] The fridge comes first and the cupboard second.

**PC**
- P1 [core · missing_consequence]
  - expect: On the fridge the letter stays where it is placed after the hand withdraws; on the wood it leaves the surface as the hand lets go.
  - fail: The letter drops or slides down the fridge after release; or stays on the wooden cupboard with nothing holding it; or hangs a gap away from either surface.
- P2 [core · gravity_direction]
  - expect: Leaving the cupboard, the letter falls straight down and lands on the floor or counter below.
  - fail: The letter moves upward or sideways as it leaves the cupboard; or halts in mid-air; or lands below and then rises back toward the cupboard.
- P3 [major · causeless_motion]
  - expect: On the fridge the letter stays still once placed and comes off only when the hand takes it; neither door moves by itself.
  - fail: The letter creeps across or turns on the fridge after release; or comes off the fridge with no hand near it; or the fridge door or the cupboard door swings on its own.
- P4 [major · trajectory_momentum]
  - expect: The fallen letter may bounce or tumble on landing and then comes to rest.
  - fail: The letter bounces higher on each bounce; or slides along the floor toward the fridge with nothing pushing it; or starts moving again after coming to rest.
- P5 [fatal · permanence_count]
  - expect: One letter throughout, the same shape on both surfaces; it sinks into neither door and does not vanish.
  - fail: A second letter appears so that one is on the fridge while another is on the cupboard; or the letter changes into a different letter; or it sinks into a door; or it vanishes instead of falling.
- P6 [minor · attribute_drift]
  - expect: The letter's colour, the other magnets on the fridge and the cupboard's grain stay the same.
  - fail: The letter changes colour between surfaces; or other fridge magnets move or vanish; or the cupboard changes colour.

## ELEC-0176 · magnet · train

**Caption.** A magnetic pickup tool is lowered into an engine bay toward a dropped nut, and the nut clicks onto its tip and is lifted out.

**Expectation (hidden).** The nut jumps to the tip when it is close and hangs from it as the tool is withdrawn; it does not fall until pulled off.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] An engine bay with a nut lying loose in it.
- S2 [core] A magnetic pickup tool is lowered toward the nut.
- S3 [core] The nut attaches to the tool's tip.
- S4 [core] The tool is lifted out of the bay with the nut on its tip.
- S5 [minor] The nut is a single small nut.
- S6 [minor] The order is lower, attach, lift out.

**PC**
- P1 [core · causeless_motion]
  - expect: The nut lies still until the tip is close to it, then moves to the tip; it does not move while the tip is elsewhere.
  - fail: The nut slides or jumps while the tip is still high above it or off to one side; or the nut hops before the tool enters the bay; or the nut moves away from the tip as it approaches.
- P2 [core · gravity_direction]
  - expect: Once on the tip the nut hangs from it in contact and rises with the tool, staying attached through the lift unless pulled off.
  - fail: The nut hangs in the air below the tip without touching it; or rises ahead of the tip; or drops off during the lift with nothing touching it; or floats up out of the bay on its own.
- P3 [major · causeless_motion]
  - expect: Hoses, cables and engine parts stay still as the tool passes; only the nut responds; once out, the nut stays put on the tip.
  - fail: Hoses or cables sway toward the tool with nothing touching them; or an engine part shifts as the tool passes; or the nut turns or slides about on the tip after the tool is out.
- P4 [major · material_response]
  - expect: The nut and the tool's tip stay hard and keep their shape; the nut sits on the tip's face or edge as a separate piece.
  - fail: The nut squashes or stretches as it meets the tip; or the tip droops under the nut; or the tool's shaft stretches longer as it is raised.
- P5 [fatal · permanence_count]
  - expect: One nut and one tool; the nut is lifted out whole, outside the tool and the engine parts; nothing vanishes.
  - fail: The nut vanishes from the tip during the lift; or a second nut appears on the tip; or the tool passes through a hose or engine part; or the nut sinks into the tip.
- P6 [minor · attribute_drift]
  - expect: The engine bay's parts, hoses and colours and the tool's colour stay the same.
  - fail: Hoses change colour or route; or engine parts change shape; or the tool changes colour or length.

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

## ELEC-0178 · static · train

**Caption.** A balloon rubbed on a wool sweater is held near a head of long hair, and the hair rises toward the balloon.

**Expectation (hidden).** The hairs lift toward the balloon only when it is close and follow it as it moves; they fall back when it is taken away.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A balloon and a wool sweater; the balloon is rubbed on the sweater.
- S2 [core] The balloon is held near a head of long hair.
- S3 [core] The hair rises toward the balloon.
- S4 [minor] The hair is long.
- S5 [minor] The rub comes first, then the approach, then the hair rises.

**PC**
- P1 [core · causeless_motion]
  - expect: The hair lies as it was until the balloon is close, lifts toward the balloon only where it is near, follows the balloon as it moves, and falls back when the balloon is taken away.
  - fail: The hair rises before the balloon is brought near; or stays lifted after the balloon has been taken well away; or hair on the far side of the head rises while the balloon is on the near side; or the hair leans away from the balloon.
- P2 [core · gravity_direction]
  - expect: The lifted strands point toward the balloon and stay rooted to the head; strands not near the balloon hang down.
  - fail: Strands detach and float up to the balloon; or hair far from the balloon stands straight up; or the whole head of hair hangs sideways with nothing pulling it; or lifted strands stay standing after the balloon is gone.
- P3 [major · material_response]
  - expect: The balloon is a light elastic shell that keeps its round shape and dents only where pressed; the hair is fine strands that lift individually.
  - fail: The balloon keeps a deep dent after the hand leaves; or stretches out like taffy; or the hair lifts as one stiff sheet like a board; or the hair sticks to the balloon as a solid mass.
- P4 [major · causeless_motion]
  - expect: The sweater, once the rub is done, lies still; other light items nearby do not stir.
  - fail: The sweater slides or lifts by itself; or paper or fabric near the balloon jumps while the balloon is far from it; or the balloon moves through the air with no hand on it.
- P5 [fatal · permanence_count]
  - expect: One balloon and one head of hair; the balloon passes through nothing and does not vanish or duplicate; the hair stays attached to the head.
  - fail: The balloon passes into the head or the hair; or a second balloon appears; or the balloon vanishes; or a clump of hair detaches and hangs on the balloon.
- P6 [minor · attribute_drift]
  - expect: The balloon's colour, the sweater's pattern and the hair's colour stay the same.
  - fail: The balloon changes colour or size, small dents aside; or the sweater changes pattern; or the hair changes colour or length.

**Note.** The person is kept because the hair is the physics; their posture and movement are not judged.

## ELEC-0179 · static · train

**Caption.** A balloon rubbed on a wool jumper is lowered over small torn scraps of paper on a table, and the scraps jump up and cling to the balloon.

**Expectation (hidden).** The scraps leap only when the balloon is near and hang from it; some drop off after a while.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A balloon is rubbed on a wool jumper.
- S2 [core] Small torn scraps of paper lie on a table.
- S3 [core] The balloon is lowered over the scraps.
- S4 [core] The scraps jump up and cling to the balloon.
- S5 [minor] The scraps are small: torn pieces, not whole sheets.
- S6 [minor] The rub comes first, then the lowering, then the jump.

**PC**
- P1 [core · causeless_motion]
  - expect: The scraps lie still until the balloon is close above them, then leap up to it; scraps far from the balloon stay put.
  - fail: Scraps jump while the balloon is still high above or off to one side; or scraps across the table stir while the balloon is far from them; or the scraps move before the balloon has been rubbed and brought near; or scraps slide away from the balloon.
- P2 [core · gravity_direction]
  - expect: Scraps that reach the balloon hang from its underside or cling to its sides, touching it; any that drop off fall back to the table.
  - fail: Scraps hover in the air between table and balloon without touching either; or a scrap that lets go drifts upward or sideways; or scraps rise past the balloon and continue upward; or scraps on the balloon's top stand upright away from it.
- P3 [major · material_response]
  - expect: The balloon is a light elastic shell that keeps its round shape; the scraps are limp paper that bend and flutter.
  - fail: The balloon keeps a deep dent after the hand leaves; or stretches out like taffy; or the scraps stand rigid like cards on the balloon; or the scraps stretch.
- P4 [major · trajectory_momentum]
  - expect: Each scrap moves along the line from its spot to the balloon and stops on the balloon; scraps travel with the balloon as it is moved.
  - fail: A scrap flies past the balloon and off; or scraps circle the balloon in the air; or scraps stay hanging in place when the balloon is moved away; or scraps bounce off the balloon and back again several times.
- P5 [fatal · permanence_count]
  - expect: The scraps on the balloon are the scraps from the table; the balloon stays one balloon and passes through nothing.
  - fail: Scraps multiply on the balloon; or scraps vanish in mid-air; or the balloon passes into the table; or scraps merge into one sheet.
- P6 [minor · attribute_drift]
  - expect: The balloon's colour, the scraps' colour and the table surface stay the same.
  - fail: The balloon changes colour or size; or the scraps change colour; or the table changes pattern.

## ELEC-0180 · static · train

**Caption.** A wool sweater is pulled off over the head in a dry room, and the hair underneath stands up in all directions.

**Expectation (hidden).** The hair rises as the sweater comes off and stays up for a moment before settling; it does not stand up before the sweater moves.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A person wears a wool sweater.
- S2 [core] The sweater is pulled off over the head.
- S3 [core] The hair underneath stands up in all directions.
- S4 [minor] The room is indoors and dry-looking: no water or steam.
- S5 [minor] The hair is flat before the sweater moves and stands up as it comes off.

**PC**
- P1 [core · causeless_motion]
  - expect: The hair lies flat until the sweater passes over it, rises as the sweater comes off, stays up for a moment and then settles; it does not rise on its own before.
  - fail: The hair stands up before the sweater has moved; or rises long after the sweater is off with nothing near it; or stays fully standing to the end of the clip with no sweater near; or rises and falls repeatedly with the sweater gone.
- P2 [core · gravity_direction]
  - expect: The standing strands stay rooted to the head and fan outward; when they settle they fall back down onto the head.
  - fail: Strands detach and float up to the ceiling; or the hair settles upward; or the hair stands as a stiff column; or strands hang toward the sweater across the room.
- P3 [major · material_response]
  - expect: The sweater stretches and folds as knitwear as it comes off; the hair is fine strands that lift individually.
  - fail: The sweater stays a rigid shape as it lifts; or the hair lifts as one stiff sheet; or the sweater stretches out like elastic and snaps back.
- P4 [major · causeless_motion]
  - expect: Once off, the sweater lies still where it is put; nothing else in the room stirs.
  - fail: The sweater floats or slides by itself; or objects nearby jump as the sweater comes off; or the person's clothing underneath ripples with nothing touching it.
- P5 [fatal · shape_identity]
  - expect: One person with one head of hair; the sweater passes over the head, not through it; the person and the room keep their shapes.
  - fail: The sweater passes through the head or body; or the head changes shape; or a second sweater appears; or hair detaches and hangs in the air.
- P6 [minor · attribute_drift]
  - expect: The sweater's colour and pattern, the hair's colour and the room stay the same.
  - fail: The sweater changes colour; or the hair changes colour or length; or the room's contents rearrange.

**Note.** The person is kept because the hair is the physics; their movements are not judged.

## ELEC-0181 · static · train

**Caption.** A shirt is lifted out of a tumble dryer, and a sock clings to it and hangs on until it is peeled off.

**Expectation (hidden).** The sock stays stuck to the shirt as it is lifted, hanging on the fabric, and comes away with a pull; it does not fall on its own.

**Declared violation types.** missing_consequence, gravity_direction

**SA**
- S1 [core] A tumble dryer with its door open.
- S2 [core] A shirt is lifted out.
- S3 [core] A sock clings to the shirt and hangs on.
- S4 [core] The sock is peeled off the shirt.
- S5 [minor] The sock stays on until it is peeled, not falling by itself.
- S6 [minor] The lift comes first, the cling shows, then the peel.

**PC**
- P1 [core · missing_consequence]
  - expect: As the shirt is lifted the sock stays pressed against it, hanging on the fabric with nothing else holding it, until a hand peels it away.
  - fail: The sock drops off the shirt on its own as it is lifted; or hangs a gap away from the shirt without touching; or the sock slides down the shirt and falls; or the sock stays on the shirt while the hand pulls it and the fabric between them stretches without parting.
- P2 [core · gravity_direction]
  - expect: The shirt hangs down from the hand; the sock hangs on the shirt's surface; once peeled free the sock, if let go, falls.
  - fail: The peeled sock floats or rises; or the shirt stands out sideways or rises from the hand; or the sock hangs in the air after the shirt is moved away; or the sock climbs the shirt.
- P3 [major · material_response]
  - expect: Shirt and sock are cloth: they drape and fold; the sock lifts off with a small tug and both keep their shapes.
  - fail: The shirt stands stiff like a board; or the sock stretches out long like elastic as it is peeled; or the shirt tears where the sock was; or the fabrics flow like liquid.
- P4 [major · causeless_motion]
  - expect: Clothes left in the dryer stay still; the dryer stays put; the sock moves only with the shirt or the hand.
  - fail: Clothes in the drum jump or rearrange as the shirt is lifted; or the sock crawls across the shirt by itself; or the dryer door swings by itself.
- P5 [fatal · permanence_count]
  - expect: One shirt and one sock; the sock is a separate garment on the shirt's surface; nothing merges, vanishes or passes through anything.
  - fail: The sock merges into the shirt's fabric; or a second sock appears; or the sock vanishes rather than being peeled; or the shirt passes through the dryer door.
- P6 [minor · attribute_drift]
  - expect: The shirt's colour and pattern, the sock's colour and the dryer stay the same.
  - fail: The shirt changes colour; or the sock changes colour or becomes a different garment; or the dryer changes.

## ELEC-0182 · static · train

**Caption.** A sheet of plastic wrap is torn from its box, and it clings to the side of the box and folds onto itself instead of hanging straight.

**Expectation (hidden).** The wrap sticks to the box and to itself where it touches and has to be pulled free; it does not hang straight like paper.

**Declared violation types.** missing_consequence, material_response

**SA**
- S1 [core] A box of plastic wrap.
- S2 [core] A sheet of wrap is torn from the box.
- S3 [core] The sheet clings to the side of the box.
- S4 [core] The sheet folds onto itself and sticks there.
- S5 [minor] The wrap is thin and transparent.
- S6 [minor] The tear comes first and the clinging follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The torn sheet does not hang straight: it lies against the box's side where it touches and its folds stick to each other, staying so until pulled apart.
  - fail: The sheet hangs straight down from the hand like paper and touches nothing; or a fold that touches the box falls away on its own; or folds that meet slide apart with nothing pulling them; or the sheet stands out stiff from the box.
- P2 [core · material_response]
  - expect: The wrap is a thin limp film: it crumples, wrinkles and folds, stretches slightly when tugged, and peels off with a pull.
  - fail: The wrap holds a flat rigid shape like a card; or drapes in heavy folds like cloth; or stretches out long like rubber and snaps back; or tears into shards like glass.
- P3 [major · gravity_direction]
  - expect: Parts of the sheet not stuck to anything hang downward; if the sheet is let go entirely it falls.
  - fail: A free edge rises or stands out sideways with nothing near it; or the sheet floats when let go; or the sheet climbs up the box.
- P4 [major · causeless_motion]
  - expect: The box stays where it is while the sheet is torn and clings; the sheet moves only with the hand or as it settles onto the box.
  - fail: The box slides or tips by itself; or the sheet crawls across the box after settling; or the sheet jumps between spots on the box with nothing touching it.
- P5 [fatal · permanence_count]
  - expect: One sheet torn from one box; the sheet stays one piece and passes through nothing; the box keeps its shape.
  - fail: The sheet splits into several pieces after the tear; or vanishes; or passes through the box; or the box changes shape or a second box appears.
- P6 [minor · attribute_drift]
  - expect: The box's colours and lettering and the counter stay the same.
  - fail: The box changes colour or lettering; or the counter changes; or the wrap changes colour.

## ELEC-0183 · static · train

**Caption.** A box of packing peanuts is tipped over a table, and many of the foam pieces stick to the sides and flaps of the box instead of falling out.

**Expectation (hidden).** The pieces cling to the cardboard instead of falling and stay there when the box is lifted; the pieces that do fall land normally.

**Declared violation types.** missing_consequence, gravity_direction

**SA**
- S1 [core] A box of packing peanuts.
- S2 [core] The box is tipped over a table.
- S3 [core] Many foam pieces stick to the sides and flaps of the box instead of falling out.
- S4 [minor] Some pieces do fall out onto the table.
- S5 [minor] The tipping comes first and the clinging shows as the box empties.

**PC**
- P1 [core · missing_consequence]
  - expect: As the box tips, pieces that touch the cardboard stay pressed against the sides and flaps, hanging on with nothing else holding them, and stay when the box is lifted or shaken lightly.
  - fail: Every piece pours out and none stays on the cardboard; or pieces cling a gap away from the cardboard without touching; or the clinging pieces drop off all together the moment the box stops moving; or pieces cling to the table's edge.
- P2 [core · gravity_direction]
  - expect: Pieces that do not cling fall from the box onto the table and come to rest there; the clinging pieces sit on the cardboard, even on its underside.
  - fail: Falling pieces rise or drift upward; or hang in the air between box and table; or land and then hop back up into the box; or pieces roll uphill on the table.
- P3 [major · material_response]
  - expect: The peanuts are light foam pieces that bounce a little and lie loose; the box is stiff cardboard that keeps its shape.
  - fail: The pieces splat or flatten like dough; or merge into a foam mass; or the box bends like cloth; or the box swells or shrinks.
- P4 [major · trajectory_momentum]
  - expect: The pieces fall out through the box's opening and scatter on the table beneath it.
  - fail: Pieces fly out sideways far across the room; or leave the box through its closed sides; or land far from where they fell; or a pile grows on the table where no piece has landed.
- P5 [fatal · permanence_count]
  - expect: The pieces on the table and on the box came from the box; none appear from nowhere or vanish; the box stays one box.
  - fail: Pieces multiply on the table beyond what fell; or pieces vanish in mid-air; or the box duplicates; or the box passes through the table.
- P6 [minor · attribute_drift]
  - expect: The box's colour and printing, the peanuts' colour and the table stay the same.
  - fail: The box changes colour; or the peanuts change colour or shape; or the table changes.

## ELEC-0184 · static · train

**Caption.** In a dark hallway a fingertip is brought slowly toward a metal doorknob, and a tiny spark jumps from the fingertip to the knob just before they touch.

**Expectation (hidden).** The spark is a single brief flash at the moment of near-contact; nothing glows before or after.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A dark hallway with a metal doorknob.
- S2 [core] A fingertip is brought slowly toward the knob.
- S3 [core] A tiny spark jumps from the fingertip to the knob just before they touch.
- S4 [minor] The approach is slow.
- S5 [minor] The spark comes as the finger nears the knob, not while it is far away.

**PC**
- P1 [core · missing_consequence]
  - expect: The spark is a thin bright line spanning the last small gap between fingertip and knob, appearing when they are almost touching.
  - fail: The spark appears while the finger is still well away from the knob; or the spark spans from the finger to a place other than the knob; or the spark is a glow on the knob with no line to the finger; or the finger touches the knob and only then a spark appears at a distance.
- P2 [core · process_direction]
  - expect: The spark is a single brief flash and is gone; nothing glows before or after, and the knob is dark once the finger touches it.
  - fail: The spark glows on between finger and knob for the rest of the clip; or the knob glows before the finger approaches; or sparks flash repeatedly while the finger rests on the knob; or the spark drifts away as a lit point.
- P3 [major · causeless_motion]
  - expect: The knob and door stay still as the finger approaches; the finger's movement is the only motion.
  - fail: The knob turns or the door swings as the spark jumps with no hand on it; or the finger is thrown back without the arm moving it; or objects in the hallway shift at the flash.
- P4 [major · missing_consequence]
  - expect: The spark's light is small: it brightens the fingertip and the knob for an instant and no more.
  - fail: The whole hallway lights up at the spark as if a lamp came on; or the knob's surroundings stay lit after the spark; or the fingertip glows on.
- P5 [fatal · solidity]
  - expect: The finger stops at the knob's surface or touches it; neither passes through the other; the knob stays on the door.
  - fail: The finger passes into the knob or the door; or the knob detaches and floats; or the door changes shape; or a second hand appears from nowhere.
- P6 [minor · attribute_drift]
  - expect: The door's colour, the knob's finish and the hallway stay the same apart from the flash.
  - fail: The door changes colour; or the knob changes shape or finish; or the hallway's contents rearrange.

**Note.** The hand is kept because the spark jumps from it; the person is otherwise not judged.

## ELEC-0185 · static · train

**Caption.** A child slides down a plastic playground slide, and at the bottom her hair is standing up from her head.

**Expectation (hidden).** The hair rises during or right after the slide and settles slowly; it is flat before the slide.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A child on a plastic playground slide.
- S2 [core] The child slides down.
- S3 [core] At the bottom the child's hair is standing up from her head.
- S4 [minor] The slide is plastic: smooth moulded plastic, not metal.
- S5 [minor] The hair lies flat or hangs at the top and stands up by the bottom.

**PC**
- P1 [core · causeless_motion]
  - expect: The hair rises during or just after the slide and settles slowly afterwards; it does not stand up before the slide begins.
  - fail: The hair stands up at the top before the child has moved; or rises long after the child has left the slide with nothing near it; or drops flat the instant the slide ends and then rises again; or rises and falls repeatedly at the bottom.
- P2 [core · gravity_direction]
  - expect: The standing strands stay rooted to the head and fan out; as they settle they fall back onto the head; the child's body follows the slide downward.
  - fail: Strands detach and float away; or the hair settles upward; or the child rises up the slide without pushing; or the hair stands as a stiff column that stays to the end.
- P3 [major · trajectory_momentum]
  - expect: The child moves down the slide along its surface and slows or stops at the bottom.
  - fail: The child stops half way and starts again with nothing pushing; or leaves the slide's surface and floats down; or moves up the slide; or slides sideways off the chute.
- P4 [major · material_response]
  - expect: The slide is a rigid plastic chute that keeps its shape under the child; the hair is fine strands.
  - fail: The slide bends or sags like fabric; or ripples as the child passes; or the hair lifts as one stiff sheet.
- P5 [fatal · shape_identity]
  - expect: One child with the same body, limbs and hair throughout; the child passes through nothing and the slide keeps its shape.
  - fail: The child gains or loses a limb or changes size; or passes through the slide; or a second child appears from nowhere; or the slide changes shape.
- P6 [minor · attribute_drift]
  - expect: The slide's colour, the child's clothing and the playground stay the same.
  - fail: The slide changes colour; or the child's clothes change colour; or the playground rearranges.

**Note.** The child is kept because the hair is the physics; the sliding posture is not judged.

## ELEC-0186 · static · train

**Caption.** A hand strokes a cat's back on a dry winter day, and the fur stands up along its back and clings to the hand.

**Expectation (hidden).** The fur lifts where the hand passes and follows the hand slightly; it settles after the stroking stops.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A cat, with a hand stroking its back.
- S2 [core] The fur stands up along its back.
- S3 [core] The fur clings to the hand.
- S4 [minor] The setting reads as a dry winter day: indoors or wintry, no water.
- S5 [minor] The stroke comes first and the fur rises where it has passed.

**PC**
- P1 [core · causeless_motion]
  - expect: The fur lifts where the hand passes and follows the hand slightly as it lifts away; fur the hand has not touched lies flat; the fur settles after the stroking stops.
  - fail: The fur stands up all over before the hand has touched it; or fur on the belly or legs rises while the hand strokes the back; or the fur stays fully standing to the end with the hand gone; or the fur rises and falls repeatedly with the hand still.
- P2 [core · missing_consequence]
  - expect: As the hand lifts off the back, the fur beneath it rises toward the hand and follows it for a small distance before settling.
  - fail: The hand lifts and the fur beneath stays as flat as before; or the fur leans away from the hand; or the fur follows the hand across the room at a distance; or the fur rises toward a hand that has not touched it.
- P3 [major · gravity_direction]
  - expect: The standing fur stays rooted to the cat and fans out from its back; when it settles it falls back onto the body.
  - fail: Tufts detach and float up to the hand; or the fur settles upward; or the fur stands as a stiff crest that never moves; or the fur hangs sideways away from the hand.
- P4 [major · material_response]
  - expect: The fur is fine hairs that lift individually; the cat's body gives under the hand as a soft animal.
  - fail: The fur lifts as one stiff sheet like a board; or the cat's back stays rigid as the hand presses; or the fur stretches like elastic.
- P5 [fatal · shape_identity]
  - expect: One cat with its head, legs and tail throughout; the hand touches its surface and passes through nothing.
  - fail: The cat gains or loses a limb or its body changes shape; or the hand passes into the cat; or a second cat appears; or the cat merges with the surface it lies on.
- P6 [minor · attribute_drift]
  - expect: The cat's coat colour and pattern, the hand and the surroundings stay the same.
  - fail: The coat changes colour or pattern; or the surroundings rearrange; or the hand changes.

**Note.** The cat is an animal and may move on its own; its movements are not causeless motion. The hand is kept because it charges the fur.

## ELEC-0187 · static · train

**Caption.** An old television screen is wiped with a dry cloth, and dust and a few hairs jump onto the screen and stick.

**Expectation (hidden).** The light specks are drawn to the screen after the rubbing and stay on it; they do not fall off at once.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] An old television with a glass screen.
- S2 [core] The screen is wiped with a dry cloth.
- S3 [core] Dust and a few hairs jump onto the screen.
- S4 [core] They stick to the screen.
- S5 [minor] The cloth is dry: no water or spray.
- S6 [minor] The wipe comes first and the specks jump after.

**PC**
- P1 [core · causeless_motion]
  - expect: The specks lie still until the screen has been rubbed, then move to the screen only when close to it; specks far away stay put; once on the screen they stay.
  - fail: Specks jump to the screen before the cloth has touched it; or specks far across the room stream to the screen; or the specks on the screen crawl about after landing; or specks jump off the screen with nothing touching them.
- P2 [core · gravity_direction]
  - expect: Specks and hairs on the screen cling to the glass, even on its upper part, and stay there; any that come loose fall.
  - fail: Specks hover in front of the screen without touching it; or fall off the screen the instant they land; or a loose speck drifts upward; or hairs stand out from the screen like bristles.
- P3 [major · material_response]
  - expect: The cloth is soft fabric that folds as it wipes; the screen is rigid glass that keeps its curve.
  - fail: The cloth stays stiff like a board; or the screen bends or ripples under the cloth; or the glass dents; or the hairs stretch.
- P4 [major · process_direction]
  - expect: Where the cloth wipes, the screen is cleaner behind it; the wiped area does not regain the dust it had.
  - fail: The dust reappears where the cloth has just passed; or the screen gets dustier as it is wiped; or dust on the screen fades away without being wiped.
- P5 [fatal · permanence_count]
  - expect: One television and one cloth; the screen stays whole; the cloth passes through nothing.
  - fail: The cloth passes into the screen; or the television changes shape or vanishes; or a second cloth appears; or the screen turns into a picture of a scene.
- P6 [minor · attribute_drift]
  - expect: The television's casing colour, the cloth's colour and the room stay the same.
  - fail: The casing changes colour; or the cloth changes colour; or the room rearranges.

**Note.** Who wipes is not judged. The screen showing a picture is not required; a picture on the screen is not a violation.

## ELEC-0188 · static · train

**Caption.** A fleece blanket is shaken out in a dark bedroom, and small flickers of light run through the fabric.

**Expectation (hidden).** The flickers appear only as the fabric separates and are gone at once; there is no glow while the blanket is still.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A fleece blanket in a dark bedroom.
- S2 [core] The blanket is shaken out.
- S3 [core] Small flickers of light run through the fabric.
- S4 [minor] The room is dark.
- S5 [minor] The flickers come while the blanket moves, not while it is still.

**PC**
- P1 [core · process_direction]
  - expect: The flickers appear only as the fabric moves and separates from itself, and each is gone at once; while the blanket is still there is no glow.
  - fail: The blanket glows steadily like a lamp; or flickers keep running through it after it has been laid still; or a flicker stays lit at one spot; or the fabric glows before it is shaken.
- P2 [core · permanence_count]
  - expect: One blanket; the flickers leave nothing behind on the fabric.
  - fail: Glowing dots stay on the blanket after the flicker; or a second blanket appears; or the blanket vanishes; or the flickers detach and float in the room.
- P3 [major · material_response]
  - expect: The blanket is soft fabric: it billows, folds and drapes as it is shaken and falls in folds when let go.
  - fail: The blanket stands stiff like a board; or stretches out like elastic; or hangs in the air as a fixed shape after the shake; or flows like liquid.
- P4 [major · missing_consequence]
  - expect: The flickers are small: they brighten only the fabric right around them and not the room.
  - fail: The room lights up with each flicker as if a lamp came on; or the flickers throw shadows across the walls; or the flickers stay lit and light the room.
- P5 [fatal · solidity]
  - expect: The blanket passes through nothing; the bed and furniture keep their shapes.
  - fail: The blanket passes through the bed or a wall; or the blanket merges with the bedding; or furniture changes shape; or a hand passes through the blanket.
- P6 [minor · attribute_drift]
  - expect: The blanket's colour and pattern and the room stay the same apart from the flickers.
  - fail: The blanket changes colour or pattern; or the room's contents rearrange; or the flickers change the blanket's colour where they pass.

**Note.** Who shakes the blanket is not judged.

## ELEC-0189 · static · train

**Caption.** A wool hat is pulled off, and the hair underneath stays lifted in the shape of the hat's inside before slowly settling.

**Expectation (hidden).** The hair rises as the hat leaves and drifts back down over a few seconds; it does not stand up before the hat moves.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A person wears a wool hat.
- S2 [core] The hat is pulled off.
- S3 [core] The hair underneath stays lifted in the shape of the hat's inside.
- S4 [core] The hair slowly settles.
- S5 [minor] The hat is a knitted wool hat.
- S6 [minor] The hair is flat under the hat, lifted as it comes off, and settled at the end.

**PC**
- P1 [core · causeless_motion]
  - expect: The hair rises as the hat leaves it and settles gradually afterwards; it does not stand up before the hat moves and does not rise again once settled.
  - fail: The hair stands up before the hat has moved; or drops flat the instant the hat is off and then rises; or rises again after settling with nothing near it; or the hair follows the hat across the room.
- P2 [core · gravity_direction]
  - expect: The lifted strands stay rooted to the head and fall back down onto it as they settle.
  - fail: Strands detach and float upward; or the hair settles upward; or the hair stays lifted as a rigid shape to the end of the clip; or the hair hangs sideways with nothing pulling it.
- P3 [major · material_response]
  - expect: The hat stretches and folds as knitwear as it is pulled off; the hair is fine strands that lift individually.
  - fail: The hat stays a rigid shape as it lifts; or the hair lifts as one stiff sheet; or the hat stretches out like elastic and snaps back.
- P4 [major · causeless_motion]
  - expect: Once off, the hat moves only with the hand; nothing else in the scene stirs.
  - fail: The hat floats or slides by itself; or objects nearby jump as the hat comes off; or the person's collar or scarf rises with nothing touching it.
- P5 [fatal · shape_identity]
  - expect: One person with one head of hair and one hat; the hat passes over the head, not through it; the head keeps its shape.
  - fail: The hat passes through the head; or the head changes shape; or a second hat appears; or a clump of hair detaches and stays in the hat as it lifts away.
- P6 [minor · attribute_drift]
  - expect: The hat's colour and pattern, the hair's colour and the background stay the same.
  - fail: The hat changes colour; or the hair changes colour or length; or the background rearranges.

**Note.** The person is kept because the hair is the physics; their movements are not judged.

## ELEC-0190 · static · train

**Caption.** A thin plastic bag is torn off a roll, and it clings to the roll and to the dispenser instead of dropping away.

**Expectation (hidden).** The bag lies against the roll and dispenser and stays there; it comes off only when peeled.

**Declared violation types.** missing_consequence, gravity_direction

**SA**
- S1 [core] A roll of thin plastic bags in a dispenser.
- S2 [core] A bag is torn off the roll.
- S3 [core] The bag clings to the roll and to the dispenser instead of dropping away.
- S4 [minor] The bag is thin and flimsy.
- S5 [minor] The tear comes first and the clinging follows.

**PC**
- P1 [core · missing_consequence]
  - expect: Once torn, the bag lies against the roll and the dispenser where it touches them and stays there, coming away only when peeled.
  - fail: The bag drops straight away from the roll and hangs free like paper; or a part that touches the dispenser falls away on its own; or the bag stands out stiff away from the roll; or the bag hangs a gap away from the dispenser without touching.
- P2 [core · gravity_direction]
  - expect: Parts of the bag not stuck to anything hang downward; if the bag is let go entirely it falls.
  - fail: A free edge rises or stands out sideways with nothing near it; or the bag floats when let go; or the bag climbs up the dispenser.
- P3 [major · material_response]
  - expect: The bag is a thin limp film: it crumples, wrinkles and clings, and peels off with a pull; the roll stays a roll.
  - fail: The bag holds a flat rigid shape like a card; or drapes in heavy folds like cloth; or stretches out long like rubber; or the roll sags like dough.
- P4 [major · causeless_motion]
  - expect: The dispenser and the roll stay where they are while the bag is torn; the bag moves only with the hand or as it settles.
  - fail: The dispenser slides or swings by itself; or the roll unwinds on its own; or the bag crawls across the dispenser after settling.
- P5 [fatal · permanence_count]
  - expect: One bag torn from the roll; it stays one piece and passes through nothing; the dispenser keeps its shape.
  - fail: The bag splits into several pieces after the tear; or vanishes; or passes through the dispenser; or a second bag appears already torn.
- P6 [minor · attribute_drift]
  - expect: The dispenser's colour, the roll and the surroundings stay the same.
  - fail: The dispenser changes colour or shape; or the roll changes colour; or the surroundings rearrange.

## ELEC-0191 · static · train

**Caption.** A sheet of cling film is lifted off a bowl, and the film clings back to the bowl's rim and to itself.

**Expectation (hidden).** The film sticks and stretches at the points of contact and has to be pulled free; it does not lift cleanly like paper.

**Declared violation types.** missing_consequence, material_response

**SA**
- S1 [core] A bowl covered with cling film.
- S2 [core] The film is lifted off the bowl.
- S3 [core] The film clings back to the bowl's rim.
- S4 [core] The film clings to itself.
- S5 [minor] The film is thin and transparent.
- S6 [minor] The lift comes first and the clinging follows.

**PC**
- P1 [core · missing_consequence]
  - expect: As the film is lifted, parts that touch the rim stay stuck to it and folds that meet stick to each other; they part only when pulled.
  - fail: The film lifts cleanly away and hangs straight like paper touching nothing; or a part on the rim falls away by itself; or folds that meet slide apart with nothing pulling them; or the film stands out stiff from the hand.
- P2 [core · material_response]
  - expect: The film is a thin limp sheet: it wrinkles, folds and stretches slightly where it is pulled from the rim, and peels off with a tug.
  - fail: The film holds a flat rigid shape like a lid; or drapes in heavy folds like cloth; or stretches out long like rubber and snaps back; or tears into shards.
- P3 [major · gravity_direction]
  - expect: Parts of the film not stuck to anything hang downward from the hand; if let go the film falls onto the bowl or table.
  - fail: A free edge rises or stands out sideways with nothing near it; or the film floats when let go; or the film climbs up the hand.
- P4 [major · causeless_motion]
  - expect: The bowl stays where it is while the film is lifted, apart from a small drag; the film moves only with the hand or as it settles.
  - fail: The bowl lifts off the table with the film and hangs from it; or the bowl slides across the table by itself; or the film crawls over the rim after settling.
- P5 [fatal · permanence_count]
  - expect: One sheet of film and one bowl; the film stays one piece and passes through nothing; the bowl keeps its shape.
  - fail: The film splits into several pieces; or vanishes; or passes through the bowl; or the bowl changes shape or duplicates; or the bowl's contents appear or vanish.
- P6 [minor · attribute_drift]
  - expect: The bowl's colour and pattern, its contents and the table stay the same.
  - fail: The bowl changes colour; or its contents change; or the table changes.

## ELEC-0192 · static · train

**Caption.** A fleece jacket is pulled off over a cotton shirt in the dark, and tiny sparks crackle where the fabrics separate.

**Expectation (hidden).** The sparks appear only as the fabrics separate and vanish instantly; nothing glows once the movement stops.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A person wears a fleece jacket over a cotton shirt, in the dark.
- S2 [core] The jacket is pulled off.
- S3 [core] Tiny sparks flash where the fabrics separate.
- S4 [minor] The room is dark.
- S5 [minor] The sparks come as the fabrics part, not while the jacket is still.

**PC**
- P1 [core · process_direction]
  - expect: The sparks appear only along the line where the fleece is parting from the shirt and each is gone at once; nothing glows before the jacket moves or after it is off.
  - fail: The fabric glows steadily like a lamp; or sparks keep flashing after the jacket has been laid still; or a spark stays lit at one spot; or sparks appear on parts of the jacket far from where it is parting.
- P2 [core · permanence_count]
  - expect: One jacket and one shirt; the sparks leave nothing behind on either.
  - fail: Glowing dots stay on the shirt or jacket after the flash; or a second jacket appears; or the jacket vanishes; or the sparks detach and float about the room.
- P3 [major · material_response]
  - expect: Both garments are soft cloth: the fleece stretches and folds as it comes off and the shirt stays on the body.
  - fail: The jacket stays a rigid shape as it lifts; or stretches out like elastic and snaps back; or the shirt comes off with the jacket as one piece; or the fabric flows like liquid.
- P4 [major · missing_consequence]
  - expect: The sparks are small: they brighten only the fabric right around them and not the room.
  - fail: The room lights up with each spark as if a lamp came on; or the sparks throw shadows across the walls; or the sparks stay lit and light the room.
- P5 [fatal · shape_identity]
  - expect: One person with the same body throughout; the jacket comes off over the body, not through it.
  - fail: The jacket passes through the body or arms; or the body changes shape; or the jacket merges with the shirt; or an arm detaches with the sleeve.
- P6 [minor · attribute_drift]
  - expect: The jacket's colour, the shirt's colour and the room stay the same apart from the sparks.
  - fail: The jacket changes colour; or the shirt changes colour; or the room's contents rearrange.

**Note.** The person is kept because the fabrics on the body are the physics; their movements are not judged. The crackle is sound and is not judged.

## ELEC-0193 · static · train

**Caption.** The sleeve of a wool sweater brushes past a hanging plastic shower curtain, and the curtain clings to the sleeve and follows it for a moment.

**Expectation (hidden).** The curtain lifts toward the sleeve where it touched and trails after it briefly before falling back; it does not move before the sleeve passes.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A plastic shower curtain hangs from its rail.
- S2 [core] The sleeve of a wool sweater brushes past the curtain.
- S3 [core] The curtain clings to the sleeve.
- S4 [core] The curtain follows the sleeve for a moment.
- S5 [minor] The sweater is wool: knitted, fuzzy.
- S6 [minor] The brush comes first; the cling and follow come after.

**PC**
- P1 [core · causeless_motion]
  - expect: The curtain hangs still until the sleeve touches it; where it touched, it lifts toward the sleeve and trails after it briefly, then swings back and settles; the rest of the curtain moves only as it is pulled.
  - fail: The curtain swings toward the sleeve before the sleeve has reached it; or keeps following the sleeve across the room at a distance; or a part of the curtain far from the sleeve lifts toward it; or the curtain keeps swinging hard long after the sleeve is gone.
- P2 [core · missing_consequence]
  - expect: As the sleeve moves on, the curtain where it touched stays pressed to the sleeve for a moment and is drawn after it before letting go.
  - fail: The curtain falls away from the sleeve the instant contact ends with no trailing; or the curtain hangs a gap away from the sleeve while following; or the curtain leans away from the sleeve as it passes.
- P3 [major · material_response]
  - expect: The curtain is a thin flexible sheet hanging in folds: it lifts, drapes over the sleeve and swings back under its own weight; the rail stays fixed.
  - fail: The curtain lifts as a rigid flat board; or stretches out like elastic; or stays hanging in the air in the shape the sleeve left; or the rail bends.
- P4 [major · gravity_direction]
  - expect: The curtain hangs down from its rings; once released it swings back to hanging straight.
  - fail: The curtain rises toward the ceiling; or hangs out sideways with nothing near it after the sleeve is gone; or the curtain floats off its rail.
- P5 [fatal · solidity]
  - expect: The curtain stays on its rail and passes through neither the sleeve nor the bath; the sleeve passes through nothing.
  - fail: The sleeve passes through the curtain; or the curtain passes through the bath's edge or the wall; or the curtain detaches from the rail and hangs in the air; or the curtain merges with the sleeve.
- P6 [minor · attribute_drift]
  - expect: The curtain's colour and pattern, the sweater's colour and the bathroom stay the same.
  - fail: The curtain changes colour or pattern; or the sweater changes colour; or bathroom fittings change.

**Note.** The person wearing the sweater is kept because the sleeve charges the curtain; their movements are not judged.

## ELEC-0194 · static · train

**Caption.** A stack of freshly printed sheets is lifted from a printer, and the sheets cling together; a single sheet lifted from the top clings to the stack rather than falling.

**Expectation (hidden).** The sheets stick and have to be fanned apart; the single sheet hangs on the stack rather than dropping.

**Declared violation types.** missing_consequence, material_response

**SA**
- S1 [core] A stack of printed sheets in a printer's tray.
- S2 [core] The stack is lifted from the printer.
- S3 [core] The sheets cling together.
- S4 [core] A single sheet lifted from the top clings to the stack rather than falling.
- S5 [minor] The sheets are printed: text or images on them.
- S6 [minor] The stack is lifted first; the single sheet is lifted after.

**PC**
- P1 [core · missing_consequence]
  - expect: The sheets hold together as the stack is lifted, with no sheet sliding out; when the top sheet is lifted by an edge it hangs against the stack, and comes free only when pulled or fanned.
  - fail: Sheets slide apart and fall out of the stack as it is lifted; or the top sheet lifts cleanly away with no cling and hangs free; or the top sheet hangs a gap away from the stack without touching; or the top sheet falls off by itself.
- P2 [core · material_response]
  - expect: The sheets are paper: they flex and curl a little, stay flat sheets and part with a fanning motion; the stack stays a block of sheets.
  - fail: The sheets bend like cloth and hang in heavy folds; or stretch like elastic; or the stack moves as one rigid solid block that cannot be fanned; or a sheet tears when lifted.
- P3 [major · gravity_direction]
  - expect: Parts of a sheet not held or stuck hang downward; a sheet let go falls onto the stack or the table.
  - fail: A sheet rises or floats when let go; or hangs out sideways with nothing holding it; or the stack rises from the hand.
- P4 [major · causeless_motion]
  - expect: The printer stays put as the stack is lifted; the sheets move only with the hand.
  - fail: The printer slides or lifts with the stack; or sheets in the tray jump by themselves; or the stack fans open with nothing touching it.
- P5 [fatal · permanence_count]
  - expect: The stack keeps its sheets: the same sheets, none vanishing or appearing; the sheets pass through nothing.
  - fail: Sheets vanish from the stack in the air; or the stack grows thicker as it is lifted; or a sheet passes through another; or the printer changes shape.
- P6 [minor · attribute_drift]
  - expect: The printing on the sheets, the printer's colour and the desk stay the same.
  - fail: The printed content changes between frames; or the printer changes colour; or the desk changes.

## ELEC-0195 · static · train

**Caption.** A fleece blanket is lifted out of the dryer, and a dryer sheet clings to its underside and rides along as the blanket is carried.

**Expectation (hidden).** The sheet stays stuck to the fabric even when hanging upside down and comes off only when peeled; it does not drop on its own.

**Declared violation types.** missing_consequence, gravity_direction

**SA**
- S1 [core] A dryer with its door open.
- S2 [core] A fleece blanket is lifted out.
- S3 [core] A dryer sheet clings to the blanket's underside.
- S4 [core] The dryer sheet rides along as the blanket is carried.
- S5 [minor] The dryer sheet is a thin flat sheet, not a sock or other garment.
- S6 [minor] The lift comes first and the clinging sheet shows as the blanket is carried.

**PC**
- P1 [core · missing_consequence]
  - expect: The dryer sheet stays pressed against the blanket's underside, hanging on with nothing else holding it, as the blanket is lifted and carried; it comes off only when peeled.
  - fail: The sheet drops off on its own as the blanket is lifted; or hangs a gap away from the blanket; or slides down the blanket and falls; or the sheet stays in the air where the blanket was when it is carried on.
- P2 [core · gravity_direction]
  - expect: The blanket hangs down from the arms; the dryer sheet clings to the fabric even on the underside; once peeled free and let go, the sheet falls.
  - fail: The peeled sheet floats or rises; or the blanket stands out sideways from the arms; or the sheet climbs up the blanket; or the sheet hangs below the blanket without touching it.
- P3 [major · material_response]
  - expect: The blanket is soft fleece that drapes in folds; the dryer sheet is a thin limp sheet that lies flat against it and wrinkles.
  - fail: The blanket stands stiff like a board; or the sheet holds a flat rigid shape away from the fabric; or the sheet stretches like elastic when peeled; or the blanket flows like liquid.
- P4 [major · causeless_motion]
  - expect: Clothes left in the dryer stay still; the dryer stays put; the sheet moves only with the blanket.
  - fail: Clothes in the drum rearrange as the blanket is lifted; or the dryer door swings by itself; or the sheet crawls across the blanket by itself.
- P5 [fatal · permanence_count]
  - expect: One blanket and one dryer sheet; the sheet is a separate item on the blanket's surface; nothing merges, vanishes or passes through anything.
  - fail: The sheet merges into the blanket; or a second sheet appears; or the sheet vanishes rather than being peeled; or the blanket passes through the dryer door.
- P6 [minor · attribute_drift]
  - expect: The blanket's colour and pattern, the sheet's colour and the dryer stay the same.
  - fail: The blanket changes colour; or the sheet changes colour or becomes a different item; or the dryer changes.

## ELEC-0196 · static · train

**Caption.** A sheet of bubble wrap is unrolled on a table, and small bits of dust and fluff jump onto it from the table.

**Expectation (hidden).** The fluff moves toward the plastic only when it is close and stays clinging; it does not move before the wrap is unrolled.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A roll of bubble wrap on a table.
- S2 [core] The wrap is unrolled along the table.
- S3 [core] Bits of dust and fluff jump onto the wrap from the table.
- S4 [minor] The dust and fluff are small light specks.
- S5 [minor] The unrolling comes first and the specks jump after.

**PC**
- P1 [core · causeless_motion]
  - expect: The specks lie still until the wrap is unrolled close to them, then move to the plastic only when it is near; specks far from the wrap stay put; once on the wrap they stay.
  - fail: Specks jump before the wrap has been unrolled toward them; or specks far across the table stream to the wrap; or specks crawl about on the wrap after landing; or specks jump off the wrap with nothing touching them.
- P2 [core · gravity_direction]
  - expect: Specks on the wrap cling to the plastic and stay; any that come loose fall back to the table.
  - fail: Specks hover above the wrap without touching it; or a loose speck drifts upward; or specks rise off the table and float past the wrap; or fluff stands upright away from the plastic.
- P3 [major · material_response]
  - expect: The wrap is a flexible plastic sheet with rows of bubbles: it unrolls, lies flat or in gentle curves and keeps its bubbles.
  - fail: The wrap stands rigid like a board as it unrolls; or stretches like elastic; or the bubbles flatten or vanish as it unrolls; or the sheet flows like liquid.
- P4 [major · trajectory_momentum]
  - expect: Each speck moves along the line from its spot to the nearest part of the wrap and stops on it.
  - fail: A speck flies past the wrap and off the table; or specks circle in the air above the wrap; or specks bounce off and back several times; or specks move away from the wrap.
- P5 [fatal · permanence_count]
  - expect: One roll of wrap; the specks on the wrap are the specks from the table; nothing appears, vanishes or passes through the table.
  - fail: Specks multiply on the wrap; or specks vanish in mid-air; or the roll duplicates; or the wrap passes through the table.
- P6 [minor · attribute_drift]
  - expect: The wrap's colour, the table's surface and the surroundings stay the same.
  - fail: The wrap changes colour; or the table changes pattern; or the surroundings rearrange.

**Note.** Who unrolls the wrap is not judged.

## ELEC-0197 · static · train

**Caption.** A nylon jacket is pulled off a hanger in a dark closet, and faint flickers of light run across the fabric.

**Expectation (hidden).** The flickers appear only as the jacket moves against itself or the hanger and vanish instantly.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A nylon jacket on a hanger in a dark closet.
- S2 [core] The jacket is pulled off the hanger.
- S3 [core] Faint flickers of light run across the fabric.
- S4 [minor] The closet is dark.
- S5 [minor] The flickers come while the jacket moves, not while it hangs still.

**PC**
- P1 [core · process_direction]
  - expect: The flickers appear only as the jacket moves against itself or the hanger, and each is gone at once; while the jacket is still there is no glow.
  - fail: The jacket glows steadily like a lamp; or flickers keep running across it after it has been laid still; or a flicker stays lit at one spot; or the fabric glows before it is touched.
- P2 [core · permanence_count]
  - expect: One jacket and one hanger; the flickers leave nothing behind on the fabric.
  - fail: Glowing dots stay on the jacket after a flicker; or a second jacket appears; or the hanger vanishes; or the flickers detach and float in the closet.
- P3 [major · material_response]
  - expect: The jacket is light slippery cloth: it slides off the hanger, folds and swings, and hangs in folds when held.
  - fail: The jacket stays a rigid shape as it comes off; or stretches like elastic; or hangs in the air as a fixed shape; or flows like liquid.
- P4 [major · missing_consequence]
  - expect: The flickers are small: they brighten only the fabric right around them and not the closet.
  - fail: The closet lights up with each flicker as if a lamp came on; or the flickers throw shadows across the clothes; or the flickers stay lit and light the closet.
- P5 [fatal · solidity]
  - expect: The jacket comes off the hanger over its shoulders, not through it; the hanger stays on the rail; nothing passes through anything.
  - fail: The jacket passes through the hanger or the rail; or the hanger detaches and floats; or the jacket merges with the clothes beside it; or the rail changes shape.
- P6 [minor · attribute_drift]
  - expect: The jacket's colour, the hanger and the other clothes stay the same apart from the flickers.
  - fail: The jacket changes colour; or the other clothes rearrange; or the hanger changes shape.

**Note.** Who pulls the jacket is not judged.

## ELEC-0198 · static · train

**Caption.** A sticker is peeled from its backing sheet, and the thin backing curls toward the sticker and clings to it instead of lying flat.

**Expectation (hidden).** The backing lifts and clings to the sticker where they come close and has to be pulled apart; it does not fall flat straight away.

**Declared violation types.** missing_consequence, material_response

**SA**
- S1 [core] A sticker on its backing sheet.
- S2 [core] The sticker is peeled from the backing.
- S3 [core] The thin backing curls toward the sticker.
- S4 [core] The backing clings to the sticker instead of lying flat.
- S5 [minor] The backing is thin and flexible.
- S6 [minor] The peel comes first and the curl and cling follow.

**PC**
- P1 [core · missing_consequence]
  - expect: As the sticker lifts, the backing near it curls up toward the sticker and clings to it where they come close; it has to be pulled apart and does not drop flat straight away.
  - fail: The backing lies flat and still as the sticker lifts, never rising toward it; or the backing curls away from the sticker; or the backing hangs a gap from the sticker without touching; or the backing drops flat the instant the sticker is off.
- P2 [core · material_response]
  - expect: The backing is a thin flexible sheet that curls and bends; the sticker is a thin flat film that keeps its shape and its printed face.
  - fail: The backing stays rigid like a card; or stretches out like rubber; or the sticker stretches or tears as it lifts; or the sticker flows like liquid.
- P3 [major · gravity_direction]
  - expect: Parts of the backing not stuck to the sticker hang downward or lie on the table; if let go the backing falls.
  - fail: A free part of the backing rises or floats with nothing near it; or the backing climbs up the hand; or the backing hangs in the air after the sticker is moved away.
- P4 [major · causeless_motion]
  - expect: The table and other items stay still while the sticker is peeled; the backing moves only toward the sticker or with the hand.
  - fail: The backing slides across the table by itself; or other papers on the table jump; or the backing flaps repeatedly with nothing touching it.
- P5 [fatal · permanence_count]
  - expect: One sticker and one backing sheet; both stay whole and pass through nothing.
  - fail: The sticker duplicates or vanishes; or the backing splits into pieces; or the sticker passes through the backing; or the backing merges with the table.
- P6 [minor · attribute_drift]
  - expect: The sticker's printed design, the backing's colour and the table stay the same.
  - fail: The sticker's design changes; or the backing changes colour; or the table changes.

## ELEC-0199 · static · train

**Caption.** A balloon rubbed on a sweater is held over a bowl of sugar, and a fine dusting of sugar jumps up to the balloon.

**Expectation (hidden).** Only the finest grains lift and cling to the balloon; the bulk of the sugar stays in the bowl.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A balloon is rubbed on a sweater.
- S2 [core] A bowl of sugar.
- S3 [core] The balloon is held over the bowl.
- S4 [core] A fine dusting of sugar jumps up to the balloon.
- S5 [minor] Only a fine dusting lifts; the bulk of the sugar stays in the bowl.
- S6 [minor] The rub comes first, then the hold, then the sugar jumps.

**PC**
- P1 [core · causeless_motion]
  - expect: The sugar lies still until the balloon is close above it, then the finest grains leap up to the balloon; grains lift only beneath the balloon and stop when it is taken away.
  - fail: Sugar leaps before the balloon is brought near; or grains lift from parts of the bowl far from the balloon; or the whole bowl of sugar stirs; or grains keep leaping after the balloon is well away.
- P2 [core · gravity_direction]
  - expect: The grains that lift cling to the balloon's underside; the bulk of the sugar stays in the bowl; any grain that lets go falls back into the bowl.
  - fail: Grains hover in the air between bowl and balloon without touching either; or the whole heap rises out of the bowl; or a grain that lets go drifts upward or sideways; or grains climb past the balloon and continue up.
- P3 [major · material_response]
  - expect: The balloon is a light elastic shell that keeps its round shape; the sugar is loose grains that lift as separate specks.
  - fail: The balloon keeps a deep dent after the hand leaves; or stretches out like taffy; or the sugar lifts as a solid lump; or the sugar flows up like liquid.
- P4 [major · trajectory_momentum]
  - expect: Each grain moves straight up from the sugar's surface to the balloon and stops on it.
  - fail: Grains fly past the balloon and off; or circle the balloon in the air; or bounce off and back several times; or grains move away from the balloon.
- P5 [fatal · permanence_count]
  - expect: One balloon and one bowl; the grains on the balloon came from the bowl; the balloon passes through nothing.
  - fail: Sugar multiplies on the balloon; or grains vanish in mid-air; or the balloon passes into the bowl; or the bowl's sugar level jumps or the bowl vanishes.
- P6 [minor · attribute_drift]
  - expect: The balloon's colour, the bowl and the sugar's colour stay the same.
  - fail: The balloon changes colour or size; or the bowl changes; or the sugar changes colour.

## ELEC-0200 · static · train

**Caption.** A balloon rubbed on a wool sweater is held beside a feather duster standing in a jar, and the feathers lean toward the balloon.

**Expectation (hidden).** The feathers lift toward the balloon while it is close and fall back when it is pulled away.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A balloon is rubbed on a wool sweater.
- S2 [core] A feather duster stands in a jar.
- S3 [core] The balloon is held beside the duster.
- S4 [core] The feathers lean toward the balloon.
- S5 [minor] The duster stands upright in the jar.
- S6 [minor] The rub comes first, then the approach, then the lean.

**PC**
- P1 [core · causeless_motion]
  - expect: The feathers hang as they were until the balloon is close, lean toward it only where it is near, follow it as it moves and fall back when it is pulled away.
  - fail: The feathers lean before the balloon is brought near; or stay leaning after the balloon has been taken well away; or feathers on the far side lean away from the balloon; or the feathers wave back and forth with the balloon held still.
- P2 [core · gravity_direction]
  - expect: The leaning feathers stay attached to the duster's head; when the balloon leaves they fall back to hanging; the duster stays in the jar.
  - fail: Feathers detach and float to the balloon; or the duster rises out of the jar toward the balloon; or feathers stand straight up with the balloon far off; or the feathers settle upward.
- P3 [major · material_response]
  - expect: The feathers are soft and lift individually; the balloon keeps its round shape and dents only where pressed; the jar is rigid.
  - fail: The feathers move as one stiff block; or the balloon keeps a deep dent after the hand leaves; or stretches out like taffy; or the jar bends.
- P4 [major · causeless_motion]
  - expect: The jar stays where it is; the sweater and other items nearby do not stir.
  - fail: The jar slides toward the balloon; or tips over with nothing touching it; or paper or fabric nearby jumps while the balloon is far from it.
- P5 [fatal · permanence_count]
  - expect: One balloon, one duster, one jar; the balloon passes through nothing and does not vanish or duplicate.
  - fail: The balloon passes into the duster or the jar; or a second balloon or duster appears; or the balloon vanishes; or a clump of feathers detaches and hangs on the balloon.
- P6 [minor · attribute_drift]
  - expect: The balloon's colour, the feathers' colours and the jar stay the same.
  - fail: The balloon changes colour or size, small dents aside; or the feathers change colour; or the jar changes shape.

## ELEC-0201 · static · train

**Caption.** A bag of styrofoam beads is poured into a bowl, and beads stick to the bag's sides and to the rim rather than all falling in.

**Expectation (hidden).** Some beads cling to the bag and the rim while most fall; the clinging beads stay until brushed off.

**Declared violation types.** missing_consequence, gravity_direction

**SA**
- S1 [core] A bag of styrofoam beads and a bowl.
- S2 [core] The beads are poured from the bag into the bowl.
- S3 [core] Beads stick to the bag's sides and to the bowl's rim rather than all falling in.
- S4 [minor] Most of the beads do fall into the bowl.
- S5 [minor] The pour comes first and the clinging shows as it goes on.

**PC**
- P1 [core · missing_consequence]
  - expect: As the beads pour, some stay pressed against the inside of the bag and on the rim of the bowl, hanging on with nothing else holding them, and remain until brushed off.
  - fail: Every bead pours out and none stays on the bag or rim; or beads cling a gap away from the plastic without touching; or the clinging beads drop off all together the instant the pour stops; or beads cling to the far side of the room.
- P2 [core · gravity_direction]
  - expect: Beads that do not cling fall from the bag into the bowl and come to rest there; clinging beads sit on the bag's sides, even its underside, and on the rim.
  - fail: Falling beads rise or drift upward; or hang in the air between bag and bowl; or land and then hop back up into the bag; or beads roll up the bowl's side and out.
- P3 [major · material_response]
  - expect: The beads are light foam spheres that bounce a little and lie loose; the bag is thin flexible plastic that crumples.
  - fail: The beads splat or flatten like dough; or merge into a foam mass; or the bag stays rigid like a box; or the bag stretches like rubber.
- P4 [major · trajectory_momentum]
  - expect: The beads leave through the bag's opening in a stream into the bowl beneath it.
  - fail: Beads fly out sideways far across the room; or leave through the bag's closed sides; or the stream bends away from the bowl with nothing deflecting it; or a pile grows where no bead has landed.
- P5 [fatal · permanence_count]
  - expect: The beads in the bowl and on the bag came from the bag; none appear from nowhere or vanish; the bag and bowl stay one each.
  - fail: Beads multiply in the bowl beyond what poured; or beads vanish in mid-air; or the bag duplicates; or the bag passes through the bowl.
- P6 [minor · attribute_drift]
  - expect: The bag's colour and printing, the beads' colour and the bowl stay the same.
  - fail: The bag changes colour; or the beads change colour or size; or the bowl changes.

## ELEC-0202 · static · train

**Caption.** A balloon rubbed on a carpet is rolled near a pile of fine sawdust, and sawdust jumps onto the balloon.

**Expectation (hidden).** The dust leaps only when the balloon is close and coats the side facing the pile; it stays on as the balloon is lifted.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A balloon is rubbed on a carpet.
- S2 [core] A pile of fine sawdust.
- S3 [core] The balloon is rolled near the pile.
- S4 [core] Sawdust jumps onto the balloon.
- S5 [minor] The sawdust is fine, like powder or small flakes.
- S6 [minor] The rub comes first, then the roll near, then the jump.

**PC**
- P1 [core · causeless_motion]
  - expect: The sawdust lies still until the balloon is close, then leaps only from the part of the pile near the balloon; the rest of the pile stays put and the leaping stops when the balloon is taken away.
  - fail: Sawdust leaps before the balloon is brought near; or the whole pile stirs at once; or dust rises from parts of the pile far from the balloon; or dust keeps leaping after the balloon is well away.
- P2 [core · gravity_direction]
  - expect: The dust that lifts coats the side of the balloon facing the pile and stays on as the balloon is lifted; any that comes loose falls back to the pile.
  - fail: Dust hovers in the air around the balloon without touching it; or the dust falls off the balloon as soon as it is lifted; or loose dust drifts upward; or the whole pile rises from the floor.
- P3 [major · material_response]
  - expect: The balloon is a light elastic shell that keeps its round shape; the sawdust is loose fine particles that lift as separate specks.
  - fail: The balloon keeps a deep dent after the hand leaves; or stretches out like taffy; or the sawdust lifts as a solid slab; or the dust flows up like liquid.
- P4 [major · trajectory_momentum]
  - expect: The balloon rolls along the carpet as a ball; the dust moves from the pile to the balloon's near side and stops there.
  - fail: The balloon slides without rolling or rolls uphill by itself; or dust flies past the balloon and off; or dust circles the balloon in the air; or dust moves away from the balloon.
- P5 [fatal · permanence_count]
  - expect: One balloon and one pile; the dust on the balloon came from the pile; the balloon passes through nothing.
  - fail: Dust multiplies on the balloon; or dust vanishes in mid-air; or the balloon passes into the floor or the pile; or a second balloon appears.
- P6 [minor · attribute_drift]
  - expect: The balloon's colour, the carpet's pattern and the sawdust's colour stay the same.
  - fail: The balloon changes colour or size; or the carpet changes pattern; or the sawdust changes colour.

## ELEC-0251 · switch_light · eval

**Caption.** A bank of switches in a school gym is flipped one at a time, and the rows of ceiling lights come on one row at a time.

**Expectation (hidden).** Each row lights at its own switch and only then; rows whose switch is untouched stay dark.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A school gym with rows of ceiling lights and a bank of switches.
- S2 [core] The switches are flipped one at a time.
- S3 [core] The rows of ceiling lights come on one row at a time.
- S4 [minor] The lights are dark before the first flip.
- S5 [minor] Each row lights after its own flip, in the order the switches are flipped.

**PC**
- P1 [core · missing_consequence]
  - expect: Each flip is followed at that moment by one row lighting; rows whose switch is untouched stay dark.
  - fail: A switch is flipped and no row lights; or a row lights with no switch flipped; or several rows light at one flip; or a row lights before its switch is touched.
- P2 [core · permanence_count]
  - expect: The rows that light are the fixtures seen dark: the same number of rows and fixtures in the same positions.
  - fail: A lit row appears where no fixtures hung; or fixtures vanish when lit; or the number of rows changes between frames; or fixtures shift along the ceiling.
- P3 [major · missing_consequence]
  - expect: The floor under each lit row brightens, with the lit area growing row by row.
  - fail: A row glows while the floor beneath stays as dark as before; or the whole floor brightens at the first row; or the floor brightens while the fixtures stay dark.
- P4 [major · process_direction]
  - expect: Once a row is lit it stays lit; the sequence only adds rows.
  - fail: A lit row goes dark by itself; or rows flicker; or a row goes dark when the next switch is flipped; or rows go dark and relight.
- P5 [fatal · shape_identity]
  - expect: The gym's walls, floor markings and fixtures keep their shapes; the hand passes through nothing.
  - fail: The fixtures change shape; or the hand passes through the switch plate; or the floor markings change; or the gym's layout changes between dark and lit frames.
- P6 [minor · attribute_drift]
  - expect: The wall and floor colours and the switch plate stay the same apart from brightness.
  - fail: The floor changes colour rather than brightness; or the switch plate changes layout; or the walls change colour.

## ELEC-0252 · switch_light · eval

**Caption.** The key switch on the base of a desk lamp is turned, and the lamp lights.

**Expectation (hidden).** The lamp lights exactly at the click and stays lit; it does not light before the key turns or flicker on its own.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A desk lamp with a key switch on its base.
- S2 [core] The key switch is turned.
- S3 [core] The lamp lights.
- S4 [minor] The lamp is dark before the turn.
- S5 [minor] The order is dark, turn, lit.

**PC**
- P1 [core · missing_consequence]
  - expect: The lamp lights at the moment the key clicks over, and only then.
  - fail: The key is turned and the lamp stays dark; or the lamp is lit before the key moves; or the lamp comes on with the key untouched; or the lamp comes on well after the turn with nothing else happening.
- P2 [core · process_direction]
  - expect: Once on, the lamp stays lit steadily for the rest of the clip.
  - fail: The lamp goes off again by itself; or flickers on and off; or dims back to dark; or the key turns back by itself.
- P3 [major · missing_consequence]
  - expect: The lamp's light reaches its surroundings: the shade glows and the desk beneath brightens, with shadows pointing away from the lamp.
  - fail: The bulb glows while the shade and desk stay as dark as before; or the surroundings brighten while the lamp stays dark; or the light comes from a place other than the lamp.
- P4 [major · causeless_motion]
  - expect: The lamp stays put as the key is turned; nothing else on the desk moves.
  - fail: The lamp slides, tips or lifts at the turn; or the shade swings by itself; or items on the desk jump.
- P5 [fatal · permanence_count]
  - expect: One lamp with one key switch; the lamp keeps its shape; the hand passes through nothing.
  - fail: A second lamp appears; or the lamp vanishes; or the hand passes through the base; or the lamp changes shape.
- P6 [minor · attribute_drift]
  - expect: The shade's colour, the base and the desk stay the same apart from the light.
  - fail: The shade changes colour rather than brightness; or the base changes shape; or the desk's contents rearrange.

## ELEC-0253 · switch_light · eval

**Caption.** A cat walks up the steps of a dark porch, and the motion-sensor light above the door comes on.

**Expectation (hidden).** The light comes on as the cat enters the sensor's range and not before; the porch brightens at that instant and stays lit while the cat is there; the light does not come on with nothing moving.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A dark porch with steps and a light above the door.
- S2 [core] A cat walks up the steps.
- S3 [core] The light above the door comes on.
- S4 [minor] The light is above the door, not on the steps or in the garden.
- S5 [minor] The cat's approach comes first and the light follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The light comes on as the cat comes up the steps, and not before; the porch brightens at that instant.
  - fail: The light is on before the cat appears; or the cat reaches the door and the light stays dark to the end of the clip; or the light comes on with the cat nowhere near and nothing else moving; or the fixture glows while the porch stays dark.
- P2 [core · causeless_motion]
  - expect: Nothing on the porch moves apart from the cat; the fixture stays still and the door stays shut.
  - fail: The door opens by itself; or objects on the porch shift as the light comes on; or the fixture swings; or the cat is carried up the steps without its legs moving.
- P3 [major · process_direction]
  - expect: Once on, the light stays on while the cat is on the porch.
  - fail: The light goes out while the cat still moves on the porch; or flickers on and off; or dims back down and up.
- P4 [major · missing_consequence]
  - expect: The light comes from above the door: the door and the top steps brighten most, with shadows pointing down and away from the fixture.
  - fail: The porch brightens evenly as if lit from the garden; or the shadows point toward the fixture; or the light comes from a place other than the fixture.
- P5 [fatal · shape_identity]
  - expect: One cat with its body, legs and tail; the porch keeps its shape; the cat passes through nothing.
  - fail: The cat gains or loses a limb or changes size; or passes through the door or railing; or a second cat appears; or the steps change shape.
- P6 [minor · attribute_drift]
  - expect: The cat's coat, the door's colour and the porch furniture stay the same apart from brightness.
  - fail: The coat changes colour or pattern; or the door changes colour; or the furniture rearranges.

**Note.** The cat is an animal and its walking is not judged; it is kept because its motion is the sensor's trigger.

## ELEC-0254 · switch_light · eval

**Caption.** The touch panel of an induction hob is tapped, and the ring's indicator light comes on.

**Expectation (hidden).** The indicator lights at the tap and not before; it stays on until the panel is tapped again.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] An induction hob with a touch panel.
- S2 [core] The panel is tapped.
- S3 [core] A ring's indicator light comes on.
- S4 [minor] The indicator is dark before the tap.
- S5 [minor] The order is dark, tap, lit.

**PC**
- P1 [core · missing_consequence]
  - expect: The indicator lights at the moment the fingertip touches the panel, and only then.
  - fail: The panel is tapped and the indicator stays dark; or the indicator is lit before the touch; or it comes on with the hand away from the panel; or a different ring's indicator lights instead.
- P2 [core · process_direction]
  - expect: Once on, the indicator stays on steadily until the panel is tapped again.
  - fail: The indicator goes out with nothing touching the panel; or flickers; or cycles through symbols with the hand withdrawn; or lights and goes out at once.
- P3 [major · causeless_motion]
  - expect: The hob and anything on it stay still as the panel is tapped.
  - fail: A pan on the hob slides or rattles at the tap; or the hob shifts; or the panel's symbols move across the glass.
- P4 [major · missing_consequence]
  - expect: The indicator's glow is small and sits at its ring's marker on the glass.
  - fail: The glow appears away from any ring marker; or the whole glass lights up; or the ring itself glows red like a coil.
- P5 [fatal · solidity]
  - expect: One hob with its glass top whole; the finger touches the glass and passes through nothing.
  - fail: The finger passes into the glass; or the hob changes shape; or a pan sinks into the glass; or a second hob appears.
- P6 [minor · attribute_drift]
  - expect: The hob's glass, its printed markings and the counter stay the same apart from the light.
  - fail: The markings change layout; or the glass changes colour; or the counter's contents rearrange.

## ELEC-0255 · switch_light · eval

**Caption.** The button on a toy light-sabre is pressed, and the blade lights up from the handle outward to the tip.

**Expectation (hidden).** The glow starts at the handle end at the press and runs to the tip in a fraction of a second; the blade is dark before the press and does not light from the tip first.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A toy light-sabre with a handle and a blade.
- S2 [core] The button on the handle is pressed.
- S3 [core] The blade lights up.
- S4 [core] The glow runs from the handle outward to the tip.
- S5 [minor] The blade is dark before the press.
- S6 [minor] The order is dark, press, lit from the handle to the tip.

**PC**
- P1 [core · missing_consequence]
  - expect: The blade begins to light at the press, and only then.
  - fail: The button is pressed and the blade stays dark to the end of the clip; or the blade is lit before the press; or the blade lights with nothing touching the handle; or only the handle lights.
- P2 [core · process_direction]
  - expect: The glow starts at the handle end and travels to the tip, then the whole blade stays lit; it does not start at the tip or run back.
  - fail: The glow starts at the tip and runs toward the handle; or runs to the tip and then retreats; or lights in patches out of order; or the blade goes dark again by itself.
- P3 [major · missing_consequence]
  - expect: The lit blade throws its colour onto the hand, the handle and nearby surfaces.
  - fail: The blade glows while the hand and surroundings stay as dark as before; or the surroundings glow while the blade is dark; or the glow on the surroundings is a different colour from the blade.
- P4 [major · material_response]
  - expect: The blade is a rigid tube that stays straight and fixed to the handle.
  - fail: The blade bends or droops; or stretches longer as it lights; or wobbles like rubber; or detaches from the handle.
- P5 [fatal · permanence_count]
  - expect: One sabre with one blade; it keeps its shape; the hand passes through nothing.
  - fail: A second blade appears; or the blade vanishes; or the hand passes through the handle; or the sabre changes shape.
- P6 [minor · attribute_drift]
  - expect: The handle's colour and the background stay the same; the blade keeps one colour once lit.
  - fail: The handle changes colour; or the blade changes colour after lighting; or the background rearranges.

## ELEC-0256 · switch_light · eval

**Caption.** The switch on a rotating shop display stand is pressed, and the stand begins to turn with its lights on.

**Expectation (hidden).** The stand turns and lights only after the switch; it stops and darkens when switched off.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A rotating shop display stand with a switch.
- S2 [core] The switch is pressed.
- S3 [core] The stand begins to turn.
- S4 [core] Its lights are on as it turns.
- S5 [minor] The stand is still and dark before the press.
- S6 [minor] The order is still, press, turning and lit.

**PC**
- P1 [core · missing_consequence]
  - expect: The stand starts to turn and its lights come on together at the press, and only then.
  - fail: The switch is pressed and the stand stays still to the end of the clip; or the stand turns before the press; or the lights come on while the stand stays still to the end; or the stand turns while its lights stay dark to the end.
- P2 [core · causeless_motion]
  - expect: Before the press nothing on the stand moves; afterwards it turns steadily and does not stop, start or reverse on its own; the items on it ride round with it.
  - fail: The stand stops and restarts with the switch untouched; or reverses; or items on the stand stay fixed while the stand turns beneath them; or items slide off with the stand turning slowly.
- P3 [major · trajectory_momentum]
  - expect: The stand turns about its own upright axis; items on it keep their places relative to each other.
  - fail: The stand wobbles off its axis; or moves across the floor; or items swap places as it turns; or the top turns while the base turns the other way.
- P4 [major · process_direction]
  - expect: Once on, the lights stay lit and the stand keeps turning while the switch stays on.
  - fail: The lights go out again with the switch on; or flicker; or the switch presses itself again; or the stand slows to a stop with the switch on.
- P5 [fatal · permanence_count]
  - expect: One stand with its items; the items keep their number and pass through nothing; the hand passes through nothing.
  - fail: Items on the stand appear or vanish as it turns; or an item sinks into the shelf; or the stand duplicates; or the hand passes into the stand.
- P6 [minor · attribute_drift]
  - expect: The stand's colour and the items' colours stay the same apart from the light.
  - fail: The stand changes colour; or an item changes colour or shape; or the shop background rearranges.

## ELEC-0257 · switch_light · eval

**Caption.** The light switch of a bathroom that also powers the extractor fan is flipped, and the fan blades spin up as the light comes on.

**Expectation (hidden).** The fan starts with the light and stops a while after it is switched off; it does not spin with the switch off.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A bathroom with a light and an extractor fan.
- S2 [core] The light switch is flipped.
- S3 [core] The light comes on.
- S4 [core] The fan blades spin up.
- S5 [minor] The light is off and the fan still before the flip.
- S6 [minor] The fan starts as the light comes on, not long before or after.

**PC**
- P1 [core · missing_consequence]
  - expect: The light comes on and the fan starts together at the moment the switch is flipped, and only then.
  - fail: The switch is flipped and neither responds to the end of the clip; or the light comes on while the fan stays still to the end; or the fan runs while the light stays dark to the end; or the fan starts before the switch moves.
- P2 [core · causeless_motion]
  - expect: Before the flip the fan is still; afterwards it runs steadily and does not stop, start or reverse on its own.
  - fail: The fan stops and restarts with the switch untouched; or turns slowly by itself before the flip; or reverses direction; or the fan grille rattles off.
- P3 [major · process_direction]
  - expect: Once on, the light stays lit and the fan keeps running while the switch stays on.
  - fail: The light goes out again with the switch on; or flickers; or the switch flips back by itself; or the fan winds down to a stop with the switch on.
- P4 [major · missing_consequence]
  - expect: The light lights the bathroom: the walls and fittings brighten from the fixture.
  - fail: The fixture glows while the room stays as dark as before; or the room brightens while the fixture stays dark; or the light comes from a place other than the fixture.
- P5 [fatal · permanence_count]
  - expect: One light and one fan; both stay fixed in place; the hand passes through nothing.
  - fail: The fan drops from the wall or ceiling; or a second fan or light appears; or the hand passes into the wall; or the fixture vanishes.
- P6 [minor · attribute_drift]
  - expect: The tiles, the fittings and the fan's grille stay the same apart from brightness.
  - fail: The tiles change colour rather than brightness; or the grille changes pattern; or fittings move.

**Note.** The fan may be behind a grille; it is judged from visible blade motion or blur behind the grille.

## ELEC-0258 · switch_light · eval

**Caption.** The big red button on a toy fire engine is pressed, and its roof lights flash.

**Expectation (hidden).** The flashing starts at the press and stops after a set time or another press; the lights are dark before.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A toy fire engine with a big red button.
- S2 [core] The button is pressed.
- S3 [core] The roof lights flash.
- S4 [minor] The roof lights are dark before the press.
- S5 [minor] The order is dark, press, flashing.

**PC**
- P1 [core · missing_consequence]
  - expect: The roof lights start flashing at the moment the button is pressed, and only then.
  - fail: The button is pressed and the lights stay dark to the end of the clip; or the lights flash before the press; or the lights come on with nothing touching the engine; or a different part of the toy lights while the roof stays dark.
- P2 [core · process_direction]
  - expect: Once started, the lights flash at a steady rhythm; they stop only after a stretch or at another press and do not stop and restart on their own.
  - fail: The flashing stops and restarts by itself; or the rhythm jumps about; or the lights settle to a steady glow and then flash again; or the flashing fades out and returns.
- P3 [major · missing_consequence]
  - expect: Each flash lights the roof and the surface around the engine in the lights' colour.
  - fail: The lights flash while the roof and surface beside them stay as dark as before; or the surface glows while the lights are dark; or the glow on the surface is a different colour from the lights.
- P4 [major · causeless_motion]
  - expect: The engine stays where it stands apart from the hand's nudge; its ladder and doors do not move by themselves.
  - fail: The engine lifts or slides across the floor with no hand on it; or the ladder rises by itself; or the doors open; or nearby toys jump at the press.
- P5 [fatal · permanence_count]
  - expect: One engine with its roof lights and wheels attached; the finger passes through nothing.
  - fail: A light or wheel vanishes or appears; or a second engine appears; or the finger passes into the toy; or the engine changes shape.
- P6 [minor · attribute_drift]
  - expect: The engine's red paint and decals and the floor stay the same apart from the flashing.
  - fail: The paint changes colour; or the decals change; or the floor pattern changes.

**Note.** The siren is sound and is not judged.

## ELEC-0259 · switch_light · eval

**Caption.** The switch for a porch light is flipped at dusk, and the porch is lit while the garden beyond stays dark.

**Expectation (hidden).** The light comes on at the switch, lights the porch, and goes off at the switch; nothing else changes.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A porch with a light, and the garden beyond, at dusk.
- S2 [core] The porch light's switch is flipped.
- S3 [core] The porch is lit.
- S4 [core] The garden beyond stays dark.
- S5 [minor] The sky is dim: dusk, not full night or daylight.
- S6 [minor] The order is dim, flip, porch lit.

**PC**
- P1 [core · missing_consequence]
  - expect: The porch light comes on at the flip, and only then, and the porch brightens with it.
  - fail: The switch is flipped and the porch stays as it was; or the porch is lit before the flip; or the light comes on with the switch untouched; or the fixture glows while the porch stays as dark as before.
- P2 [core · process_direction]
  - expect: Once on, the light stays lit and the porch stays lit for the rest of the clip.
  - fail: The light goes out again by itself; or flickers; or dims back to dusk; or the switch flips back by itself.
- P3 [major · missing_consequence]
  - expect: The light falls off with distance: the porch is brightest near the fixture and the garden beyond stays at its dusk level.
  - fail: The garden lights up as brightly as the porch; or the garden brightens while the porch stays dark; or the light comes from the garden side; or the porch brightens evenly with no falloff.
- P4 [major · causeless_motion]
  - expect: Nothing on the porch or in the garden moves at the flip; the fixture stays fixed.
  - fail: Porch furniture shifts at the flip; or the fixture swings; or plants in the garden jump; or the door opens by itself.
- P5 [fatal · permanence_count]
  - expect: One porch light and one switch; the porch's and garden's contents are the same before and after; the hand passes through nothing.
  - fail: Objects appear or vanish between dim and lit frames; or a second light appears; or the hand passes into the wall; or the fixture vanishes.
- P6 [minor · attribute_drift]
  - expect: The porch's colours, the fixture and the garden's plants stay the same apart from brightness.
  - fail: The porch changes colour rather than brightness; or the fixture changes shape; or the sky jumps from dusk to full night or back.

## ELEC-0260 · plug_power · eval

**Caption.** A running record player is unplugged, and the turntable slows to a stop while the needle still rests on the record.

**Expectation (hidden).** The turntable coasts to a stop within a few seconds of the plug coming out and does not start again; the needle stays down; nothing keeps spinning with the power gone.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A record player runs, its turntable spinning with the needle on the record.
- S2 [core] The player is unplugged.
- S3 [core] The turntable slows to a stop.
- S4 [core] The needle stays resting on the record.
- S5 [minor] The turntable slows before it stops rather than halting at once.
- S6 [minor] The order is spinning, unplug, slowing, stopped.

**PC**
- P1 [core · missing_consequence]
  - expect: The turntable begins to slow after the plug leaves the socket, not before, and comes to rest.
  - fail: The plug is out and the turntable spins at full speed to the end of the clip; or the turntable slows before the plug moves; or the turntable slows with the plug still seated; or the player's light stays lit with the plug out.
- P2 [core · causeless_motion]
  - expect: The turntable coasts down one way and, once stopped, does not move again while the plug is out.
  - fail: The turntable halts dead at the instant the plug comes out; or starts again with the plug out; or speeds up after the pull; or reverses direction.
- P3 [major · causeless_motion]
  - expect: The tone arm stays resting where it is on the record; it does not lift or swing by itself.
  - fail: The arm lifts and returns to its rest by itself; or the needle skips across the record; or the arm swings out; or the record lifts off the platter.
- P4 [major · material_response]
  - expect: The cord follows the plug: it slackens and drops once the plug is free and stays attached at both ends.
  - fail: The cord stretches like elastic; or stands rigid in the air after the plug is out; or the player is dragged by the pull.
- P5 [fatal · permanence_count]
  - expect: One player, one record, one arm; the plug leaves the socket whole; nothing vanishes or passes through the wall.
  - fail: The record vanishes or a second appears; or the plug passes through the wall; or the arm detaches; or the cord splits.
- P6 [minor · attribute_drift]
  - expect: The player's casing, the record's label and the surface stay the same.
  - fail: The casing changes colour; or the record's label changes; or the surface's contents rearrange.

**Note.** The sound stopping is not judged; how many turns the platter coasts is not judged.

## ELEC-0261 · plug_power · eval

**Caption.** Batteries are slid into a toy keyboard whose power switch is already on, and its keys light up.

**Expectation (hidden).** The keys light only once the batteries are seated and not before; they stay lit afterwards.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A toy keyboard with its power switch on and a battery compartment open.
- S2 [core] Batteries are slid into the compartment.
- S3 [core] The keys light up.
- S4 [minor] The keys are dark before the batteries are in.
- S5 [minor] The order is batteries in, then keys lit.

**PC**
- P1 [core · missing_consequence]
  - expect: The keys light once the batteries are seated, and only then.
  - fail: The batteries are in and the keys stay dark to the end of the clip; or the keys are lit before the batteries reach the keyboard; or the keys light with the batteries lying loose; or the keys light while a battery is still half out.
- P2 [core · process_direction]
  - expect: Once lit, the keys stay lit for the rest of the clip.
  - fail: The keys go dark again with the batteries in; or flicker; or light and go out repeatedly; or the batteries slide back out by themselves.
- P3 [major · trajectory_momentum]
  - expect: Each battery slides into its slot along the slot's length and seats with a stop.
  - fail: A battery enters through the keyboard's casing away from the compartment; or floats into place; or seats and then pops out by itself; or two batteries occupy one slot.
- P4 [major · causeless_motion]
  - expect: The keyboard stays put as the batteries go in; its keys do not press themselves.
  - fail: The keyboard slides or lifts; or keys go down by themselves; or the compartment lid snaps shut on its own.
- P5 [fatal · solidity]
  - expect: The batteries enter the compartment and are seen there; none passes through the casing; fingers pass through nothing.
  - fail: A battery passes through the casing; or a battery vanishes in the hand; or an extra battery appears; or the keyboard changes shape.
- P6 [minor · attribute_drift]
  - expect: The keyboard's colours and key layout stay the same apart from the light.
  - fail: The keyboard changes colour; or keys change layout; or the batteries change size or label.

## ELEC-0262 · plug_power · eval

**Caption.** A lamp is plugged into the far end of a long extension cord, and the moment the cord's plug goes into the wall socket at the other side of the room the lamp lights.

**Expectation (hidden).** The lamp lights at the instant the far plug goes in, with no delay for the length of the cord; it is dark before and stays lit after.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A lamp plugged into the far end of a long extension cord.
- S2 [core] The cord's plug is pushed into a wall socket at the other side of the room.
- S3 [core] The lamp lights.
- S4 [minor] The cord runs across the room from the socket to the lamp.
- S5 [minor] The lamp lights as the plug goes in, not before and with no delay.

**PC**
- P1 [core · missing_consequence]
  - expect: The lamp lights at the instant the plug seats in the wall socket, and only then; there is no delay for the cord's length.
  - fail: The plug is in and the lamp stays dark to the end of the clip; or the lamp is lit before the plug reaches the socket; or the lamp lights with the plug lying loose; or a glow travels along the cord toward the lamp.
- P2 [core · causeless_motion]
  - expect: The cord lies still along its route and the lamp stays where it stands; nothing moves as the plug goes in.
  - fail: The cord snakes or jumps across the floor by itself; or the lamp slides or turns; or the shade swings; or the socket end of the cord moves while the hand is at the lamp.
- P3 [major · process_direction]
  - expect: Once on, the lamp stays lit steadily for the rest of the clip.
  - fail: The lamp goes out again by itself; or flickers; or dims back to dark; or the plug backs out of the socket by itself.
- P4 [major · missing_consequence]
  - expect: The lamp's light reaches its surroundings: the shade glows and the floor and wall near it brighten.
  - fail: The bulb glows while the shade and the floor near it stay as dark as before; or the surroundings brighten while the lamp stays dark; or the light comes from the socket end of the room.
- P5 [fatal · solidity]
  - expect: One cord from one socket to one lamp; the plug enters the socket rather than the wall; the cord stays continuous; fingers pass through nothing.
  - fail: The plug passes into the wall beside the socket; or the cord splits or detaches; or a second lamp appears; or the cord passes through furniture.
- P6 [minor · attribute_drift]
  - expect: The cord's colour, the lamp's shade and the room stay the same apart from the light.
  - fail: The cord changes colour; or the shade changes colour rather than brightness; or the room's contents rearrange.

## ELEC-0263 · plug_power · eval

**Caption.** A cordless drill running on a bench slows and stops as its battery runs flat, and it only twitches when the trigger is pulled again.

**Expectation (hidden).** The drill slows gradually and stops; further trigger pulls produce at most a twitch; it does not run again at full speed without charging.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] A cordless drill running on a bench.
- S2 [core] The drill slows and stops.
- S3 [core] The trigger is pulled again.
- S4 [core] The drill only twitches.
- S5 [minor] No cord runs from the drill.
- S6 [minor] The order is running, slowing, stopped, trigger pulled, twitch.

**PC**
- P1 [core · process_direction]
  - expect: The slowing runs one way from running to stopped; the drill does not speed up again on its own.
  - fail: The drill speeds up again after slowing; or stops and restarts at full speed with nothing touched; or runs faster than before after the stop; or the chuck spins with nothing pulling the trigger after the stop.
- P2 [core · missing_consequence]
  - expect: When the trigger is pulled again the chuck turns only a little or briefly and stops; it does not run at full speed.
  - fail: The trigger is pulled again and the drill runs at full speed to the end of the clip; or the twitch grows into steady spinning; or the trigger is pulled and the bit spins while the chuck stays still.
- P3 [major · trajectory_momentum]
  - expect: The chuck and bit spin about the drill's axis while running and stay on that axis as they slow.
  - fail: The bit wobbles off its axis or bends; or the chuck turns while the bit stays still; or the whole drill body spins on the bench.
- P4 [major · causeless_motion]
  - expect: The drill stays on the bench as it runs and slows, apart from a small shift; it does not walk off.
  - fail: The drill crawls across the bench and falls; or lifts into the air; or jumps when it stops; or bench items shift at the stop.
- P5 [fatal · permanence_count]
  - expect: One drill with its bit and battery pack; nothing vanishes or passes through the bench.
  - fail: The bit vanishes or a second bit appears; or the pack detaches and floats; or the drill duplicates; or the bit sinks into the bench.
- P6 [minor · attribute_drift]
  - expect: The drill's colour, its markings and the bench stay the same.
  - fail: The drill changes colour; or its markings change; or the bench's contents rearrange.

**Note.** The motor's sound is not judged; running and stopping are read from the chuck's visible spin and blur. Who pulls the trigger is not judged.

## ELEC-0264 · plug_power · eval

**Caption.** A power cut hits a restaurant, and every light and the neon sign in the window go dark at once while the candles on the tables keep burning.

**Expectation (hidden).** All electric lights fail at the same instant; the candle flames are unaffected.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A restaurant with electric lights on and a neon sign in the window.
- S2 [core] Candles burn on the tables.
- S3 [core] Every electric light and the neon sign go dark at once.
- S4 [core] The candles keep burning.
- S5 [minor] The lights and the sign go dark at the same moment.
- S6 [minor] The order is lit, cut, dark with candles burning.

**PC**
- P1 [core · missing_consequence]
  - expect: Every electric light and the sign go dark at the same instant; the candle flames carry on unchanged.
  - fail: A lamp stays lit after the others are dark; or the sign goes dark before or after the lamps; or the candles go out with the lights; or the candle flames flare or jump at the cut.
- P2 [core · permanence_count]
  - expect: The room's contents are the same before and after the cut: the same tables, chairs, candles and lamps in the same places, dark rather than gone.
  - fail: Candles appear or vanish between lit and dark frames; or tables or chairs appear or vanish; or the sign vanishes rather than going dark; or a lamp changes place.
- P3 [major · process_direction]
  - expect: Once dark, the lights and sign stay dark; if power returns they come back together.
  - fail: A lamp comes back on alone; or the sign flickers on and off; or the lights return while the sign stays dark to the end; or the candles go out one by one after the cut.
- P4 [major · missing_consequence]
  - expect: With the lamps dark the room's light comes from the candles: warm pools around each flame and dimness between.
  - fail: The room stays as bright with every lamp dark; or the candles burn with no glow around them; or light stays pooled under a dark lamp; or the room brightens as the lamps go out.
- P5 [fatal · shape_identity]
  - expect: Tables, chairs, lamps and the sign keep their shapes; nothing passes through a wall or table.
  - fail: A lamp or the sign changes shape; or a chair merges with a table; or an object passes through a wall; or the candles turn into lamps.
- P6 [minor · attribute_drift]
  - expect: The tablecloths, the walls and the sign's tube colours stay the same apart from brightness.
  - fail: The tablecloths change colour rather than brightness; or the walls change colour; or the sign's lettering changes.

**Note.** People at the tables, if any, are not judged.

## ELEC-0265 · plug_power · eval

**Caption.** The handle of a wind-up torch is cranked, and the bulb brightens as the handle turns and fades when the cranking stops.

**Expectation (hidden).** The bulb is dark before the crank moves, brightens with the turning, and dims within a moment of the handle stopping; it does not stay bright with the handle still.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A wind-up torch with a crank handle.
- S2 [core] The handle is cranked.
- S3 [core] The bulb brightens as the handle turns.
- S4 [core] The bulb fades when the cranking stops.
- S5 [minor] The bulb is dark before the handle moves.
- S6 [minor] The order is dark, crank and glow, stop and fade.

**PC**
- P1 [core · missing_consequence]
  - expect: The bulb lights while the handle turns and fades within a moment of the handle stopping; it does not glow with the handle still.
  - fail: The handle turns and the bulb stays dark to the end of the clip; or the bulb is lit before the handle moves; or the bulb stays bright long after the handle has stopped; or the bulb brightens after the cranking has stopped.
- P2 [core · causeless_motion]
  - expect: The handle turns only while the hand cranks it; it does not spin on its own or keep turning after release.
  - fail: The handle spins by itself; or keeps turning after the hand lets go; or the torch spins with the handle; or the handle turns the other way by itself.
- P3 [major · process_direction]
  - expect: Once the cranking stops the fade runs one way to dark and does not brighten again without cranking.
  - fail: The bulb brightens again with the handle still; or pulses on and off with the handle still; or goes dark and relights by itself.
- P4 [major · missing_consequence]
  - expect: While lit, the bulb throws a beam: the surface it points at brightens with it and dims as it fades.
  - fail: The lens glows while the surface it points at stays as dark as before; or the surface brightens while the lens is dark; or the lit patch lies behind the torch.
- P5 [fatal · permanence_count]
  - expect: One torch with one handle; the handle stays attached; the hand passes through nothing.
  - fail: The handle detaches and floats; or a second torch appears; or the hand passes through the torch; or the torch changes shape.
- P6 [minor · attribute_drift]
  - expect: The torch's colour and the surroundings stay the same apart from the light.
  - fail: The torch changes colour; or the handle changes shape; or the surroundings rearrange.

**Note.** The hand is kept because cranking is the caption's cause; the person is otherwise not judged.

## ELEC-0266 · plug_power · eval

**Caption.** A remote-control boat slows and stops in the middle of a pond as its battery runs flat.

**Expectation (hidden).** The boat loses speed gradually and drifts to a stop; the controller no longer moves it.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A remote-control boat on a pond.
- S2 [core] The boat slows.
- S3 [core] The boat stops in the middle of the pond.
- S4 [minor] The boat is moving under its own power at the start: a wake or bow wave shows.
- S5 [minor] The order is moving, slowing, stopped.

**PC**
- P1 [core · missing_consequence]
  - expect: The boat loses speed gradually and comes to a stop; it does not speed up again.
  - fail: The boat runs at full speed to the end of the clip; or speeds up again after slowing; or stops and sets off again under power; or the boat stops dead in an instant with its wake vanishing at once.
- P2 [core · causeless_motion]
  - expect: Once stopped the boat drifts only slowly with the water; it does not dart off or turn sharply by itself.
  - fail: The stopped boat darts forward or backward; or spins in place; or moves against the ripples with nothing driving it; or drifts fast across the pond.
- P3 [major · trajectory_momentum]
  - expect: As it slows the boat keeps its heading and its wake dies away behind it; the bow wave flattens.
  - fail: The boat turns sharply as it slows with nothing steering; or reverses; or the wake persists behind a stopped boat; or the wake runs ahead of the boat.
- P4 [major · gravity_direction]
  - expect: The boat floats level on the surface throughout; it does not sink or lift.
  - fail: The boat sinks lower as it slows; or lifts out of the water; or tips over with nothing pushing it; or the water heaps around a still boat.
- P5 [fatal · permanence_count]
  - expect: One boat on one pond; the boat keeps its hull and fittings; nothing passes through the water's surface or vanishes.
  - fail: The boat vanishes or a second boat appears; or the boat passes through a reed bed or the bank; or the hull changes shape; or the boat sinks through the surface without any water entering.
- P6 [minor · attribute_drift]
  - expect: The boat's colours and the pond's surroundings stay the same.
  - fail: The boat changes colour; or its fittings change; or the surroundings rearrange.

**Note.** Whoever holds the controller is out of view and is not judged; how quickly the boat slows is not judged.

## ELEC-0267 · plug_power · eval

**Caption.** A wireless earbud is dropped into its charging case, and a small light on the case begins to blink.

**Expectation (hidden).** The light starts only when the earbud is seated in the case and stops when it is taken out.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A wireless earbud and its charging case, open.
- S2 [core] The earbud is dropped into the case.
- S3 [core] A small light on the case begins to blink.
- S4 [minor] The case's light is off before the earbud is in.
- S5 [minor] The order is drop, seat, blink.

**PC**
- P1 [core · missing_consequence]
  - expect: The light starts blinking once the earbud is seated in its slot, and only then.
  - fail: The earbud is seated and the light stays dark to the end of the clip; or the light blinks before the earbud reaches the case; or the light blinks with the earbud lying beside the case; or the earbud's own light blinks while the case stays dark.
- P2 [core · process_direction]
  - expect: Once started, the light blinks steadily while the earbud stays in; it stops only if the earbud is taken out or the lid is shut.
  - fail: The light stops blinking with the earbud seated and the lid open; or blinks at a rhythm that jumps about; or the earbud pops back out by itself; or the light stays lit steadily after one blink.
- P3 [major · gravity_direction]
  - expect: The earbud falls down into its slot and comes to rest there.
  - fail: The earbud hovers above the slot; or rises out of the case; or falls and bounces out onto the table and rises back in.
- P4 [major · causeless_motion]
  - expect: The case stays where it sits as the earbud drops in; the lid does not move by itself.
  - fail: The case slides or flips; or the lid snaps shut by itself; or the second earbud jumps out of its slot.
- P5 [fatal · permanence_count]
  - expect: One earbud dropped into one case; the earbud stays a separate piece in its slot; nothing merges or vanishes.
  - fail: The earbud merges into the case; or vanishes on the way in; or a second identical earbud appears in the hand; or the case changes shape.
- P6 [minor · attribute_drift]
  - expect: The case's colour, the earbud's colour and the table stay the same apart from the light.
  - fail: The case changes colour; or the earbud changes colour or size; or the table's contents rearrange.

## ELEC-0268 · plug_power · eval

**Caption.** The safety key is pulled from a running treadmill, and the belt slows and stops.

**Expectation (hidden).** The belt coasts to a stop within a second or two of the key coming out and does not move again until the key is back.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A treadmill with its belt running.
- S2 [core] The safety key is pulled out.
- S3 [core] The belt slows and stops.
- S4 [minor] The key is on a cord or clip that comes away from the console.
- S5 [minor] The order is running, key out, slowing, stopped.

**PC**
- P1 [core · missing_consequence]
  - expect: The belt begins to slow when the key comes out, not before, and comes to rest; the console's display changes or goes dark with it.
  - fail: The key is out and the belt runs on to the end of the clip; or the belt slows before the key is touched; or the belt slows with the key still in place; or the display shows the belt running after it has stopped.
- P2 [core · causeless_motion]
  - expect: The slowing runs one way; once stopped the belt does not move again while the key is out.
  - fail: The belt starts again with the key out; or speeds up after the pull; or reverses direction; or jerks in place after stopping.
- P3 [major · trajectory_momentum]
  - expect: The belt's surface moves as one sheet over the deck in one direction until it stops.
  - fail: The belt surface moves in patches at different speeds; or slides sideways off the deck; or the rollers turn while the belt stays still.
- P4 [major · material_response]
  - expect: The key's cord goes slack once the key is out and hangs from the key or the clip.
  - fail: The cord stretches like elastic; or stands rigid in the air; or the key floats; or the cord pulls the console over.
- P5 [fatal · permanence_count]
  - expect: One treadmill, one belt, one key; the key leaves its socket whole; nothing passes through the console.
  - fail: The key vanishes or a second key appears; or the key passes through the console; or the belt splits; or the treadmill changes shape.
- P6 [minor · attribute_drift]
  - expect: The treadmill's colour, the console layout and the room stay the same apart from the display.
  - fail: The treadmill changes colour; or the console's buttons rearrange; or the room's contents change.

**Note.** Who pulls the key is not judged. Whether anyone is on the belt is not required.

## ELEC-0269 · lightning · eval

**Caption.** Lightning flashes over a vineyard at night, and the rows of vines are lit for an instant before the dark returns.

**Expectation (hidden).** The flash is brief and lights everything at once; the vines are dark again immediately.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] A vineyard at night with rows of vines.
- S2 [core] Lightning flashes over the vineyard.
- S3 [core] The rows of vines are lit for an instant.
- S4 [core] The dark returns.
- S5 [minor] The vines are in rows.
- S6 [minor] The order is dark, flash, dark.

**PC**
- P1 [core · process_direction]
  - expect: The flash is brief: the vineyard brightens and returns to dark; flashes may repeat but each ends.
  - fail: The vineyard stays lit for the rest of the clip after the flash; or brightens steadily; or the flash fades in slowly like a dimmer; or the sky turns to daylight.
- P2 [core · missing_consequence]
  - expect: The flash lights the whole scene at once: the rows, the ground between them and the cloud undersides brighten together during the flash, from the sky's direction.
  - fail: The sky flashes while the vines stay as dark as before; or the vines light up while the sky stays dark; or the light sweeps across the rows one after another; or the rows are lit from below.
- P3 [major · permanence_count]
  - expect: The rows, posts and any buildings are the same across dark and lit frames.
  - fail: Rows or posts appear or vanish between dark and lit frames; or a building appears; or the rows change direction; or the vines change shape.
- P4 [major · causeless_motion]
  - expect: The vines and posts stay still through the flash; leaves stir only in the wind.
  - fail: The vines shake sharply at the flash with nothing else stirring; or posts move; or the ground shifts.
- P5 [fatal · shape_identity]
  - expect: The vines and posts keep their shapes and stay rooted; nothing passes through anything; any bolt seen ends in the air or at the ground.
  - fail: A row merges into a wall; or a bolt passes through a vine and lights it like a lamp; or a post morphs into another object; or the ground turns into water.
- P6 [minor · attribute_drift]
  - expect: The foliage colour, the soil and the sky are consistent before and after the flash.
  - fail: The foliage changes colour permanently; or the soil changes colour; or the sky turns to daylight after the flash.

## ELEC-0270 · lightning · eval

**Caption.** A lightning bolt strikes a hilltop radio mast, and the mast is outlined in a bright flash.

**Expectation (hidden).** The bolt ends at the mast's tip, the flash lasts a fraction of a second, and the mast stands unchanged afterwards.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A radio mast on a hilltop.
- S2 [core] A lightning bolt strikes the mast.
- S3 [core] The mast is outlined in a bright flash.
- S4 [minor] The bolt ends at the mast's tip.
- S5 [minor] The order is bolt, flash, dark.

**PC**
- P1 [core · process_direction]
  - expect: The bolt and the flash on the mast are brief and gone; the mast returns to its unlit look and stays so.
  - fail: The bolt stands as a steady lit line for the rest of the clip; or the mast glows on after the bolt is gone; or the flash travels slowly down the mast; or the flash fades in slowly.
- P2 [core · permanence_count]
  - expect: The mast, its guy wires and the hilltop are the same before and after the strike.
  - fail: The mast vanishes or bends after the strike; or a second mast appears; or a guy wire vanishes or appears; or the mast changes place between dark and lit frames.
- P3 [major · shape_identity]
  - expect: The bolt is a jagged, branching line whose main channel ends at the mast's tip.
  - fail: The bolt is a straight beam or a smooth arc; or a wide glowing tube; or it ends in mid-air beside the mast while the mast lights up; or it strikes the mast's base with the tip untouched.
- P4 [major · missing_consequence]
  - expect: The flash lights the surroundings: the hilltop and cloud undersides brighten during the bolt, from the bolt's direction.
  - fail: The bolt is visible while the hilltop stays as dark as before; or the valley below is lit while the hilltop around the mast stays dark; or the hilltop brightens with no bolt present.
- P5 [fatal · solidity]
  - expect: The bolt ends at the mast and does not pass through it into the ground; the mast stays a solid structure.
  - fail: The bolt continues below the mast as a lit line under the ground; or the mast becomes transparent; or the mast melts or bends like rubber; or the hilltop splits.
- P6 [minor · attribute_drift]
  - expect: The mast's colour, the hilltop and the sky keep their colours apart from the flash.
  - fail: The mast changes colour; or the hilltop changes colour; or the sky turns to daylight after the flash.

## ELEC-0271 · lightning · eval

**Caption.** Lightning flashes over a harbour at night, and the moored boats and their masts are lit for an instant before the dark returns.

**Expectation (hidden).** The flash is brief and lights the whole harbour at once; the boats are dark again immediately; their own deck lights stay steady throughout.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A harbour at night with moored boats and their masts.
- S2 [core] Lightning flashes over the harbour.
- S3 [core] The boats and masts are lit for an instant.
- S4 [core] The dark returns.
- S5 [minor] The boats' own deck lights are on.
- S6 [minor] The order is dark, flash, dark.

**PC**
- P1 [core · missing_consequence]
  - expect: The flash lights the whole harbour at once: boats, masts, water and cloud undersides brighten together during the flash and darken together after it.
  - fail: The sky flashes while the boats stay as dark as before; or the boats light up while the sky stays dark; or the light sweeps across the harbour boat by boat; or the water stays lit after the boats are dark.
- P2 [core · causeless_motion]
  - expect: The boats' own deck lights stay steady through the flash; the boats ride only on the water's slow movement.
  - fail: Deck lights blink out at the flash or all change together; or the boats jump or heel at the flash; or masts sway sharply with nothing else stirring; or moorings shift.
- P3 [major · process_direction]
  - expect: The flash is brief: the harbour returns to dark; flashes may repeat but each ends.
  - fail: The harbour stays lit for the rest of the clip; or brightens steadily; or the flash fades in slowly; or the sky turns to daylight.
- P4 [major · permanence_count]
  - expect: The boats, masts and quay are the same across dark and lit frames.
  - fail: Boats or masts appear or vanish between dark and lit frames; or a boat changes place; or the quay changes shape; or masts multiply.
- P5 [fatal · shape_identity]
  - expect: Boats, masts and quay keep their shapes; nothing passes through anything; any bolt seen ends in the air or at the water.
  - fail: A boat changes shape or merges with another; or a bolt passes through a mast and lights the hull like a lamp; or the water turns solid; or a mast bends.
- P6 [minor · attribute_drift]
  - expect: The hull colours, the quay and the sky are consistent before and after the flash.
  - fail: A hull changes colour permanently; or the quay changes colour; or the sky turns to daylight after the flash.

## ELEC-0272 · lightning · eval

**Caption.** Lightning flashes over a snowy village at night, and the snow-covered roofs and street flash white for an instant.

**Expectation (hidden).** The whole scene brightens together for a fraction of a second and returns to dark; the house lights stay steady.

**Declared violation types.** process_direction, missing_consequence

**SA**
- S1 [core] A snowy village at night with snow-covered roofs and a street.
- S2 [core] Lightning flashes over the village.
- S3 [core] The roofs and street flash white for an instant.
- S4 [minor] The houses' own lights are on.
- S5 [minor] The scene returns to dark after the flash.

**PC**
- P1 [core · process_direction]
  - expect: The flash is brief: the village brightens and returns to dark; flashes may repeat but each ends.
  - fail: The village stays lit for the rest of the clip; or brightens steadily; or the flash fades in slowly; or the sky turns to daylight.
- P2 [core · missing_consequence]
  - expect: The whole scene brightens together during the flash: the snow on roofs and street turns bright white, lit from the sky; the house lights stay steady.
  - fail: The sky flashes while the snow stays as dim as before; or the snow lights up while the sky stays dark; or the house lights blink out at the flash; or the light sweeps across the village roof by roof.
- P3 [major · permanence_count]
  - expect: The houses, roofs and street are the same across dark and lit frames.
  - fail: Houses appear or vanish between dark and lit frames; or a roof changes shape; or the street changes route; or lit windows change pattern all at once.
- P4 [major · gravity_direction] (if: Snow is falling.)
  - expect: Falling snow, if any, keeps falling downward through the flash; snow on the roofs stays put.
  - fail: Snowflakes rise or hang still; or snow slides off every roof at the flash; or flakes change direction at the flash.
- P5 [fatal · shape_identity]
  - expect: Houses and street keep their shapes; nothing passes through anything; any bolt seen ends in the air or at the ground.
  - fail: A house changes shape or merges with another; or a bolt passes through a house and lights it from within; or the snow turns into water; or the street becomes a river.
- P6 [minor · attribute_drift]
  - expect: The houses' colours, the snow and the sky are consistent before and after the flash.
  - fail: A house changes colour permanently; or the snow changes colour permanently; or the sky turns to daylight after the flash.

## ELEC-0273 · lightning · eval

**Caption.** A bolt of lightning forks from a cloud to a lone barn in a field, and smoke rises from the barn roof after the flash.

**Expectation (hidden).** The bolt is brief and ends at the barn; the smoke appears after and rises; the roof does not glow.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A lone barn in a field under a cloud.
- S2 [core] A lightning bolt forks from the cloud to the barn.
- S3 [core] Smoke rises from the barn roof after the flash.
- S4 [minor] The bolt is forked or branched.
- S5 [minor] The bolt and flash come first and the smoke follows.

**PC**
- P1 [core · process_direction]
  - expect: The bolt and its flash are brief and gone; the smoke appears at the roof only afterwards and grows from there; the roof does not glow.
  - fail: The bolt stands as a steady lit line for the rest of the clip; or smoke rises from the roof before the bolt arrives; or the smoke shrinks back into the roof; or the roof glows like an ember after the bolt is gone.
- P2 [core · permanence_count]
  - expect: The barn and the field are the same before and after: the same building in the same place, whole or scorched, with the smoke the only new thing.
  - fail: The barn vanishes with the flash; or a second barn appears; or the barn changes place between dark and lit frames; or a burnt object appears on the roof that was not there.
- P3 [major · gravity_direction]
  - expect: The smoke rises from the roof and drifts upward and away; anything knocked off the roof falls.
  - fail: The smoke sinks down the walls and pools on the ground; or hangs as a fixed shape; or shingles knocked off rise or hang in the air.
- P4 [major · shape_identity]
  - expect: The bolt is a jagged line with a main channel from the cloud to the barn and side branches that end in the air.
  - fail: The bolt is a perfectly straight beam; or a smooth wave; or a wide glowing tube; or a bolt that hangs in mid-air touching neither cloud nor barn while the roof starts smoking.
- P5 [fatal · solidity]
  - expect: The bolt ends at the roof and does not pass through the barn into the ground; the barn stays a solid building.
  - fail: The bolt continues below the barn as a lit line under the ground; or the barn's interior lights up as if the bolt were inside; or the walls become transparent; or the barn melts.
- P6 [minor · attribute_drift]
  - expect: The barn's paint, the field and the sky keep their colours apart from the flash and the scorch.
  - fail: The barn changes colour away from the strike; or the field changes colour; or the sky turns to daylight after the flash.

## ELEC-0274 · lightning · eval

**Caption.** Lightning flickers inside a thunderhead over a desert highway, lighting the cloud from within again and again.

**Expectation (hidden).** Each flicker is brief and lights the cloud, not the ground directly; no bolt reaches the road.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A thunderhead over a desert highway.
- S2 [core] Lightning flickers inside the cloud, lighting it from within.
- S3 [core] The flickers repeat: the cloud lights up more than once.
- S4 [minor] No bolt reaches the road or the ground.
- S5 [minor] The flickers are inside the cloud, not below it.

**PC**
- P1 [core · process_direction]
  - expect: Each flicker is brief with the cloud dark between; the flickers repeat but never merge into a steady glow.
  - fail: The cloud stays lit for the rest of the clip; or the glow brightens steadily; or the sky turns to daylight; or a flicker fades in slowly.
- P2 [core · permanence_count]
  - expect: The cloud, the highway and the desert are the same across dark and lit frames.
  - fail: The cloud changes shape abruptly between flickers; or the road changes route; or vehicles or signs appear or vanish between frames; or a second cloud appears already lit.
- P3 [major · missing_consequence]
  - expect: The light comes from within the cloud: its body and edges glow with their texture revealed, and the road below brightens only faintly as a glow from above.
  - fail: The road lights up brightly while the cloud stays dark; or the glow is a flat wash over the frame with no cloud structure; or a spot on the road lights up as if struck while no bolt reaches it.
- P4 [major · causeless_motion]
  - expect: The cloud drifts only slowly; the road and anything on it stay still or move steadily through the flickers.
  - fail: The cloud jumps or swirls at a flicker; or a vehicle jumps ahead between dark and lit frames; or signs or poles shift at the flash.
- P5 [fatal · shape_identity]
  - expect: Cloud stays cloud and the road stays ground; nothing on the ground is struck or changed.
  - fail: The cloud turns into a solid object; or a bolt strikes the road and leaves a glowing mark; or the road splits; or the desert turns into water.
- P6 [minor · attribute_drift]
  - expect: The sky's night colour, the road and the desert are consistent before and after each flicker.
  - fail: The sky changes colour permanently; or the road changes colour; or the cloud changes colour when not lit.

**Note.** Vehicles on the highway, if any, are driven and are not judged.

## ELEC-0275 · lightning · eval

**Caption.** Lightning flashes over a city at night, and the flash is mirrored at the same instant in hundreds of windows of a glass tower.

**Expectation (hidden).** Every window that faces the flash brightens together and darkens together with it; the reflections last only as long as the flash; the tower's interior lights stay steady.

**Declared violation types.** missing_consequence, permanence_count

**SA**
- S1 [core] A city at night with a glass tower.
- S2 [core] Lightning flashes over the city.
- S3 [core] The flash is mirrored in many windows of the tower.
- S4 [minor] The reflections appear at the same instant as the flash.
- S5 [minor] The tower's interior lights are on.

**PC**
- P1 [core · missing_consequence]
  - expect: Every window facing the flash brightens together with it and darkens together after it; the reflections last only as long as the flash.
  - fail: The sky flashes while the tower's windows stay as they were; or the windows brighten one after another; or the reflections stay bright after the sky is dark; or the windows brighten while the sky stays dark.
- P2 [core · permanence_count]
  - expect: The tower and its windows are the same across dark and lit frames: the same grid of windows, the same lit interiors; the reflections add no new windows.
  - fail: Windows appear or vanish between dark and lit frames; or the tower changes shape; or lit interior windows go dark all at once at the flash; or a second tower appears.
- P3 [major · process_direction]
  - expect: The flash is brief: sky and reflections return to dark together; flashes may repeat but each ends.
  - fail: The sky stays lit for the rest of the clip; or brightens steadily; or the flash fades in slowly; or the sky turns to daylight.
- P4 [major · causeless_motion]
  - expect: The tower's interior lights stay steady through the flash; nothing in the city moves at the flash.
  - fail: Interior lights blink out at the flash; or street lights all change together; or vehicles jump between frames; or the tower sways.
- P5 [fatal · shape_identity]
  - expect: The tower and the buildings around it keep their shapes; the flash does not pass through the tower.
  - fail: The tower changes shape or merges with a neighbour; or a bolt passes through the tower and lights its floors like lamps; or the tower becomes transparent showing the flash through it; or the tower vanishes.
- P6 [minor · attribute_drift]
  - expect: The tower's glass colour, the city lights and the sky are consistent before and after the flash.
  - fail: The glass changes colour permanently; or the city lights change colour; or the sky turns to daylight after the flash.

## ELEC-0276 · lightning · eval

**Caption.** Lightning flashes over a wet street at night, and the sky and the wet road brighten for an instant while the streetlamps burn steadily throughout.

**Expectation (hidden).** The flash lights the road and sky together and is gone in a fraction of a second; the lamps neither brighten nor go out with it; puddles mirror the flash.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A wet street at night with streetlamps lit.
- S2 [core] Lightning flashes over the street.
- S3 [core] The sky and the wet road brighten for an instant.
- S4 [core] The streetlamps burn steadily throughout.
- S5 [minor] The road looks wet: shiny or with puddles.
- S6 [minor] The order is dark, flash, dark.

**PC**
- P1 [core · missing_consequence]
  - expect: The flash lights the road and sky together: the wet surface and puddles mirror the lit sky during the flash and darken with it.
  - fail: The sky flashes while the wet road stays as dark as before; or the road brightens while the sky stays dark; or the road's reflection stays lit after the sky is dark; or the reflection appears before the sky flashes.
- P2 [core · causeless_motion]
  - expect: The streetlamps keep their steady glow through the flash, neither brightening nor going out; nothing in the street moves at the flash.
  - fail: A streetlamp goes out at the flash; or the lamps brighten with the flash; or all the lamps change together; or parked cars or bins shift at the flash.
- P3 [major · process_direction]
  - expect: The flash is brief: sky and road return to dark; flashes may repeat but each ends.
  - fail: The sky stays lit for the rest of the clip; or brightens steadily; or the flash fades in slowly; or the sky turns to daylight.
- P4 [major · permanence_count]
  - expect: The buildings, lamps, cars and puddles are the same across dark and lit frames.
  - fail: Buildings or cars appear or vanish between frames; or lamp posts move; or puddles appear or vanish; or a lamp post duplicates.
- P5 [fatal · solidity]
  - expect: The street stays a street: puddles are thin water on a solid surface; buildings keep their shape; nothing passes through anything.
  - fail: A puddle swallows an object; or a building changes shape; or a bolt passes through a building and lights its inside; or the road ripples like open water.
- P6 [minor · attribute_drift]
  - expect: The lamps' colour, the buildings and the road markings stay the same apart from brightness.
  - fail: The lamps change colour; or the buildings change colour; or the road markings change.

## ELEC-0277 · spark · eval

**Caption.** A power saw cuts into the roof of a wrecked car, and sparks spray from the blade across the wet road.

**Expectation (hidden).** Sparks fly out along the blade's direction, arc down onto the road, and die; they appear only while the blade is cutting.

**Declared violation types.** gravity_direction, permanence_count, process_direction

**SA**
- S1 [core] A wrecked car on a wet road.
- S2 [core] A power saw cuts into the car's roof.
- S3 [core] Sparks spray from the blade.
- S4 [core] The sparks fly across the wet road.
- S5 [minor] The sparks come from where the blade meets the roof.
- S6 [minor] The cut comes first and the sparks follow.

**PC**
- P1 [core · gravity_direction]
  - expect: The sparks arc downward as they fly and go dark on or before reaching the road; none rise or hover.
  - fail: Sparks rise steadily and gather above the car; or hang in the air; or lie on the road glowing like lamps for the rest of the clip; or the spray climbs without arcing down.
- P2 [core · process_direction]
  - expect: Sparks appear only while the blade is in the metal and stop when it lifts; each spark is gone within a short flight.
  - fail: Sparks stream while the blade is clear of the roof; or continue after the saw has been withdrawn; or sparks flow back into the cut; or a spark stays lit at one spot.
- P3 [core · permanence_count]
  - expect: Sparks are transient and none accumulate; the saw, the car and the road keep their number and shape apart from the cut.
  - fail: Sparks persist as fixed bright dots; or a glowing pile builds on the road; or sparks appear from a point away from the blade; or a second saw appears.
- P4 [major · trajectory_momentum]
  - expect: The spray leaves the cut along the direction the blade's rim is moving, in one fan.
  - fail: Sparks radiate equally in all directions from the cut; or the spray points opposite to the rim's motion; or the spray's direction jumps about while the saw is steady.
- P5 [major · missing_consequence]
  - expect: The wet road mirrors the spray briefly beneath it.
  - fail: The sparks fly over the wet road while it stays as dark as before; or a reflection lies where no spark is above it; or the reflection stays lit after the sparks are gone.
- P6 [fatal · solidity]
  - expect: The blade cuts into the roof along a narrow line; the saw and the car keep their shape; the blade passes through nothing else.
  - fail: The blade passes through the roof leaving it unmarked; or the saw sinks into the car; or the car's roof bends like cloth; or the blade bends like rubber.
- P7 [minor · attribute_drift]
  - expect: The car's colour away from the cut, the saw and the road stay the same.
  - fail: The car changes colour; or the saw changes colour; or the road markings change.

**Note.** Who holds the saw is not judged.

## ELEC-0278 · spark · eval

**Caption.** A skateboard's metal truck grinds along a steel rail at night, and sparks flick off where it scrapes.

**Expectation (hidden).** The sparks appear only while the metal is scraping, trail behind the board, and go dark within a fraction of a second; none appear once the board leaves the rail.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A skateboard grinds along a steel rail at night.
- S2 [core] Its metal truck scrapes the rail.
- S3 [core] Sparks flick off where it scrapes.
- S4 [minor] The sparks come from the truck's contact with the rail.
- S5 [minor] The scrape comes first and the sparks follow.

**PC**
- P1 [core · causeless_motion]
  - expect: Sparks appear only where and while the truck scrapes the rail; none appear before the board reaches the rail or after it leaves.
  - fail: Sparks flick from the truck while the board is in the air or on the ground; or sparks appear on the rail where no truck touches; or sparks keep coming after the board has left the rail; or the rail glows along its length.
- P2 [core · process_direction]
  - expect: Each spark is gone within a short flight; the sparks trail behind the board and leave nothing on the rail.
  - fail: A spark stays lit at one spot on the rail after the board has passed; or a glowing line remains along the rail; or sparks flow back to the truck; or sparks lie glowing on the ground for the rest of the clip.
- P3 [major · trajectory_momentum]
  - expect: The sparks stream backward from the contact, opposite to the board's motion, and drop away.
  - fail: Sparks fly ahead of the board; or spray equally in all directions; or climb steadily and stay aloft; or the trail moves along with the board as a fixed cloud.
- P4 [major · material_response]
  - expect: The rail is a rigid bar that keeps its shape; the board's deck flexes only slightly and the trucks stay stiff.
  - fail: The rail bends or sags under the board; or the deck folds like cloth; or a truck stretches; or the wheels squash flat.
- P5 [fatal · solidity]
  - expect: The truck rides on the rail's surface; the board and rider pass through nothing; the rail stays whole.
  - fail: The truck sinks into the rail; or the board passes through the rail; or the rider merges with the board; or a wheel detaches and floats.
- P6 [minor · attribute_drift]
  - expect: The board's graphics, the rail and the surroundings stay the same.
  - fail: The deck's graphics change; or the rail changes colour; or the surroundings rearrange.

**Note.** The rider is kept because the grind is the caption's action; riding technique is not judged.

## ELEC-0279 · spark · eval

**Caption.** A pair of skis slides over an exposed rock, and sparks flash from their metal edges.

**Expectation (hidden).** The sparks appear only during the scrape and go dark instantly; none appear on snow.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A pair of skis on snow.
- S2 [core] The skis slide over an exposed rock.
- S3 [core] Sparks flash from their metal edges.
- S4 [minor] The sparks come at the rock, not on the snow.
- S5 [minor] The scrape comes first and the sparks follow.

**PC**
- P1 [core · process_direction]
  - expect: Sparks appear only while the edges cross the rock and are gone at once; none appear while the skis are on snow.
  - fail: Sparks flash while the skis are on snow with no rock beneath; or continue after the skis have left the rock; or a spark stays lit on the rock; or the edges glow along their length.
- P2 [core · permanence_count]
  - expect: Two skis throughout; the sparks leave nothing behind on the rock or the snow.
  - fail: Glowing dots stay on the rock after the skis have passed; or a ski vanishes or a third appears; or the rock vanishes or appears from nowhere; or the skis merge into one.
- P3 [major · gravity_direction]
  - expect: Any spark fragments fall to the snow and go dark within a short distance.
  - fail: Sparks rise and gather above the skis; or hang in the air; or lie glowing on the snow for the rest of the clip.
- P4 [major · trajectory_momentum]
  - expect: The skis slide on in the direction of travel over the rock; the sparks flick out behind the edges.
  - fail: The skis stop dead on the rock and then continue; or leap into the air off the rock; or the sparks fly ahead of the skis; or the skis slide uphill by themselves.
- P5 [fatal · solidity]
  - expect: The skis pass over the rock's surface; they pass through neither the rock nor the snow's surface; the skis keep their shape.
  - fail: A ski passes through the rock; or sinks through the snow as if through air; or a ski bends double; or the rock passes through a ski.
- P6 [minor · attribute_drift]
  - expect: The skis' colours, the snow and the rock stay the same.
  - fail: A ski changes colour or length; or the snow changes colour; or the rock changes shape.

**Note.** The skier, if in view, is kept because the skis are under them; skiing form is not judged.

## ELEC-0280 · spark · eval

**Caption.** A lawnmower's blade strikes a hidden stone, and a spark flicks out from under the deck.

**Expectation (hidden).** The spark appears at the instant of the strike, flies out low and dies at once; there are no sparks while the mower cuts grass alone.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A lawnmower cuts grass.
- S2 [core] Its blade strikes a hidden stone.
- S3 [core] A spark flicks out from under the deck.
- S4 [minor] The spark comes from under the deck, low to the ground.
- S5 [minor] The strike comes first and the spark follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The spark appears at the instant of the strike and only then; while the mower cuts grass alone nothing flashes under the deck.
  - fail: Sparks flick from under the deck while the mower runs over plain grass; or sparks appear while the mower stands still; or the spark appears before the mower reaches the stone; or sparks keep coming after the strike.
- P2 [core · missing_consequence]
  - expect: The spark flies out low from under the deck's edge and dies at once; the stone, if it appears, is thrown out or stays under the deck.
  - fail: The spark appears on top of the deck or at the handle; or the spark hangs in the air; or the stone flies straight up through the deck; or the spark leaves a glowing mark on the grass.
- P3 [major · gravity_direction]
  - expect: The spark and any thrown stone fall to the ground and come to rest; the spark goes dark within a short distance.
  - fail: The spark rises and hangs in the air; or climbs steadily; or the stone rises and stays aloft; or lies glowing on the grass for the rest of the clip.
- P4 [major · material_response]
  - expect: The mower is a rigid machine that jolts at the strike and rolls on; the deck keeps its shape.
  - fail: The deck bends or dents deeply and springs back; or the mower bounces high into the air; or the handle wobbles like rubber.
- P5 [fatal · solidity]
  - expect: One mower on the grass; the mower passes through nothing; the stone does not pass through the deck.
  - fail: The mower passes through a tree or fence; or the stone passes up through the deck; or the mower sinks into the lawn; or a second mower appears.
- P6 [minor · attribute_drift]
  - expect: The mower's colour, the lawn and the surroundings stay the same apart from the cut strip.
  - fail: The mower changes colour; or the lawn changes colour away from the cut; or the surroundings rearrange.

**Note.** Who pushes the mower is not judged. The strike itself is hidden under the deck; it is read from the mower's jolt and the spark.

## ELEC-0281 · spark · eval

**Caption.** A pad of steel wool is touched to the terminals of a battery, and sparks race through the wool as its strands glow orange.

**Expectation (hidden).** The glow starts at the point of contact and runs along the strands in branching lines; the burnt strands go dark and crumble; nothing glows before the contact.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A pad of steel wool and a battery.
- S2 [core] The wool is touched to the battery's terminals.
- S3 [core] The strands glow orange and the glow races through the wool.
- S4 [minor] The wool is dark before the contact.
- S5 [minor] The contact comes first and the glow follows.

**PC**
- P1 [core · missing_consequence]
  - expect: The glow starts at the point of contact with the terminals and runs outward along the strands in branching lines.
  - fail: The wool is touched to the terminals and stays dark to the end of the clip; or the glow starts at a part of the pad far from the contact; or the whole pad lights at once with no spreading; or the glow appears while the wool is held away from the battery.
- P2 [core · process_direction]
  - expect: The glow spreads one way through the wool; burnt strands go dark and crumble behind the glowing front and do not relight.
  - fail: The glow retreats back toward the contact; or burnt strands relight; or the glow flashes on and off across the pad; or the pad returns to its unburnt look.
- P3 [major · gravity_direction]
  - expect: Sparks and burnt fragments that fall off drop downward and go dark; smoke, if any, rises.
  - fail: Sparks rise and gather above the pad; or hang in the air; or fragments float; or smoke sinks and pools.
- P4 [major · material_response]
  - expect: The wool is a tangle of fine strands: it compresses under the fingers, and burnt strands thin and crumble to dark specks.
  - fail: The pad stays a rigid block; or burnt strands stay thick and bright grey; or the pad melts into a pool; or the strands stretch like elastic.
- P5 [fatal · permanence_count]
  - expect: One pad and one battery; the pad stays one tangle, shrinking only as it burns; nothing appears, vanishes or passes through the battery.
  - fail: A second pad appears; or the pad vanishes in one step; or the pad passes into the battery; or the battery changes shape.
- P6 [minor · attribute_drift]
  - expect: The battery's label and the surface beneath stay the same; the glow keeps one orange colour.
  - fail: The battery's label changes; or the surface changes; or the glow turns blue or green.

**Note.** The hands are kept because they bring the wool to the terminals; the person is otherwise not judged. How far the glow spreads by the end is not judged.

## ELEC-0282 · spark · eval

**Caption.** A model train runs over a stretch of dirty track, and tiny sparks flicker under its wheels.

**Expectation (hidden).** The sparks appear only under the moving wheels and only on the dirty stretch; they are brief and do not appear while the train stands still.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A model train on a track.
- S2 [core] The train runs over a stretch of track.
- S3 [core] Tiny sparks flicker under its wheels.
- S4 [minor] The sparks are under the wheels, at rail level.
- S5 [minor] The train is moving when the sparks appear.

**PC**
- P1 [core · causeless_motion]
  - expect: The sparks appear only under the moving wheels and only on the dirty stretch; none appear while the train stands still or on clean track.
  - fail: Sparks flicker under a train that is standing still; or sparks appear on the track where no wheel is; or sparks appear along the whole route with no dirty stretch; or sparks keep flickering after the train has passed.
- P2 [core · missing_consequence]
  - expect: Each spark is at a wheel's contact with the rail, brief and gone; the train keeps running through the sparks.
  - fail: The sparks appear on the train's roof or body away from the wheels; or a spark stays lit at one spot; or the whole rail glows; or the train stops dead as each spark appears.
- P3 [major · gravity_direction]
  - expect: Any spark fragments fall to the track bed and go dark within a short distance.
  - fail: Sparks rise and gather above the train; or hang in the air; or lie glowing on the track for the rest of the clip.
- P4 [major · trajectory_momentum]
  - expect: The train follows the track on its wheels, its carriages in line.
  - fail: The train leaves the rails and runs across the table; or floats above the track; or carriages separate and run at different speeds; or the train jumps ahead between frames.
- P5 [fatal · permanence_count]
  - expect: One train with its carriages on one track; nothing appears, vanishes or passes through the track.
  - fail: A carriage vanishes or appears; or a second train appears; or the train passes through the track or scenery; or carriages merge.
- P6 [minor · attribute_drift]
  - expect: The train's livery, the track and the scenery stay the same.
  - fail: The train changes colour; or the track changes layout between frames; or the scenery rearranges.

**Note.** Which stretch of track is dirty is read from where the sparks appear; a stretch that looks the same as the rest is not a violation.

## ELEC-0283 · spark · eval

**Caption.** A tall blade of grass blows against the wire of an electric fence, and a tiny spark clicks at the contact each time it touches.

**Expectation (hidden).** The spark appears exactly when the grass touches the wire and not while it hangs clear; each spark is brief and repeats with each touch; the grass does not catch fire.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] An electric fence wire.
- S2 [core] A tall blade of grass blows against the wire.
- S3 [core] A tiny spark appears at the contact each time the grass touches.
- S4 [minor] The grass touches more than once as it blows.
- S5 [minor] Each spark comes as the grass meets the wire, not while it hangs clear.

**PC**
- P1 [core · missing_consequence]
  - expect: A spark appears exactly at the point where the grass meets the wire, each time it touches, and is gone; while the grass hangs clear there is none.
  - fail: The grass touches the wire and no spark appears at any touch to the end of the clip; or sparks appear while the grass hangs clear of the wire; or the spark appears at a place on the wire away from the grass; or the spark glows on between touches.
- P2 [core · causeless_motion]
  - expect: The grass moves only in the wind, swaying to and from the wire; the wire stays still; the grass is not thrown by the spark.
  - fail: The grass is flung away from the wire at each spark; or the wire sways with nothing touching it; or the grass moves toward the wire against the wind of the other grass; or the grass stands still while sparks appear.
- P3 [major · process_direction]
  - expect: The sparks repeat with each touch and each is brief; the grass does not catch fire or char and the wire does not glow.
  - fail: The grass catches fire; or the grass blackens and shrivels; or the wire glows along its length; or a spark stays lit.
- P4 [major · material_response]
  - expect: The grass is a limp blade that bends in the wind; the wire is a taut strand between posts.
  - fail: The grass stands rigid like a rod; or the wire sags and swings like rope; or the grass stretches; or the wire bends where the grass touches.
- P5 [fatal · permanence_count]
  - expect: One wire and one blade of grass in contact; the grass stays rooted; nothing passes through the wire or vanishes.
  - fail: The grass passes through the wire; or the grass detaches and floats; or a second wire appears; or the blade of grass vanishes.
- P6 [minor · attribute_drift]
  - expect: The grass's colour, the wire and the posts stay the same.
  - fail: The grass changes colour; or the wire changes thickness; or the posts move.

**Note.** The click is sound and is not judged. The wind is invisible; the grass swaying is not causeless motion.

## ELEC-0284 · spark · eval

**Caption.** A neon sign's box shorts in the rain, and sparks drop from beneath the sign onto the wet pavement.

**Expectation (hidden).** The sparks fall downward from the sign box and go dark before or as they land; the sign flickers with each spark.

**Declared violation types.** gravity_direction, permanence_count, process_direction

**SA**
- S1 [core] A neon sign in the rain.
- S2 [core] The sign's box shorts: sparks come from beneath the sign.
- S3 [core] The sparks drop onto the wet pavement.
- S4 [minor] Rain is falling.
- S5 [minor] The sign flickers as the sparks come.

**PC**
- P1 [core · gravity_direction]
  - expect: The sparks fall downward from beneath the sign box and go dark before or as they land on the pavement.
  - fail: Sparks rise from the box and gather above the sign; or hang in the air; or lie glowing on the pavement for the rest of the clip; or drift sideways without dropping.
- P2 [core · permanence_count]
  - expect: Sparks are transient and leave nothing behind; the sign, its box and the pavement keep their shape.
  - fail: Glowing dots stay on the pavement after the sparks; or a glowing pile builds; or the sign duplicates or vanishes; or the box changes shape.
- P3 [core · process_direction]
  - expect: Sparks come in bursts from the box and each is gone within a short fall; the sign's tubes flicker with the bursts and do not glow steadily brighter.
  - fail: The sparks stream steadily as a fixed fountain to the end of the clip; or sparks flow back up into the box; or the tubes brighten steadily to a glare; or the tubes flicker while no sparks come and stay steady when they do.
- P4 [major · missing_consequence]
  - expect: The wet pavement mirrors each burst briefly beneath it; the rain falls downward.
  - fail: The sparks fall over the wet pavement while it stays as dark as before; or the reflection lies far from the sparks; or rain rises or hangs still.
- P5 [major · trajectory_momentum]
  - expect: The sparks leave the box's underside and fall in arcs or straight lines to the pavement.
  - fail: Sparks fly upward past the sign's face; or spray far out sideways from a still box; or sparks leave from the sign's top.
- P6 [fatal · solidity]
  - expect: The sign stays fixed to its mounting; nothing passes through the wall or the sign; the sparks come from the box, not from inside the wall.
  - fail: The sign detaches and hangs in the air; or sparks pass through the wall; or the box melts; or the sign merges with the shopfront.
- P7 [minor · attribute_drift]
  - expect: The sign's tube colours, the shopfront and the pavement stay the same apart from the flicker.
  - fail: A tube changes colour; or the lettering changes; or the shopfront changes.

## ELEC-0285 · magnet · eval

**Caption.** A magnet is touched to a steel food can and holds; touched to an aluminium drink can beside it, it falls off.

**Expectation (hidden).** The magnet stays on the steel can even when let go and drops from the aluminium can at once; the cans do not move on their own.

**Declared violation types.** missing_consequence, solidity

**SA**
- S1 [core] A steel food can and an aluminium drink can side by side.
- S2 [core] A magnet is touched to the steel can and holds there.
- S3 [core] The magnet is touched to the aluminium can.
- S4 [core] The magnet falls off the aluminium can.
- S5 [minor] The steel can comes first and the drink can second.
- S6 [minor] The same magnet is used on both cans.

**PC**
- P1 [core · missing_consequence]
  - expect: On the steel can the magnet stays where it is placed after the hand withdraws; on the drink can it leaves the surface as the hand lets go.
  - fail: The magnet drops or slides down the steel can after release; or stays on the drink can with nothing holding it; or hangs a gap away from either can; or the drink can lifts away with the magnet.
- P2 [core · solidity]
  - expect: The magnet touches the outside of each can and stays outside; the cans keep their shape; the hand passes through nothing.
  - fail: The magnet sinks into a can; or passes through a can's wall; or a can dents deeply at the touch and stays dented; or the hand passes through a can.
- P3 [major · gravity_direction]
  - expect: Leaving the drink can, the magnet falls straight down and lands on the surface below.
  - fail: The magnet drifts upward or sideways after release; or halts in mid-air; or lands and rises back to the can.
- P4 [major · causeless_motion]
  - expect: The cans stay where they stand; neither slides, tips or rolls on its own as the magnet is placed or falls.
  - fail: A can slides toward the magnet; or tips over with nothing touching it; or the drink can rolls away as the magnet falls; or the magnet creeps across the steel can.
- P5 [fatal · permanence_count]
  - expect: One magnet and two cans throughout; nothing appears, vanishes or passes through the table.
  - fail: A second magnet appears so that one is on each can; or a can vanishes; or the magnet vanishes in mid-fall; or the magnet passes through the table.
- P6 [minor · attribute_drift]
  - expect: The cans' labels and colours, the magnet and the surface stay the same.
  - fail: A can's label changes; or the magnet changes colour or shape; or the surface changes.

**Note.** P1 assumes the cans are as the caption says; a drink can that plainly reads as steel fails S1, and the magnet holding on it is then not a P1 failure.

## ELEC-0286 · magnet · eval

**Caption.** A toy fishing rod with a magnet on its line is dangled over paper fish fitted with steel clips, and a fish jumps up to the magnet and hangs from it.

**Expectation (hidden).** The fish lifts only when the magnet is close, snaps to it by its clip, and hangs from the line as it is raised; fish without clips stay put.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A toy fishing rod with a magnet on its line.
- S2 [core] Paper fish fitted with steel clips lie below.
- S3 [core] The magnet is dangled over the fish.
- S4 [core] A fish jumps up to the magnet and hangs from it.
- S5 [minor] The fish attaches by its clip.
- S6 [minor] The dangle comes first and the jump follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The fish lie still until the magnet is close, then one leaps by its clip to the magnet; fish away from the magnet stay put.
  - fail: A fish jumps while the magnet is still high above; or fish across the pool slide toward the rod; or fish move before the magnet is lowered; or a fish jumps by its tail with the clip untouched.
- P2 [core · missing_consequence]
  - expect: Once the clip meets the magnet the fish hangs from it and rises with the line as the rod is lifted, staying attached until pulled off.
  - fail: The clip touches the magnet and the fish drops back; or the fish hangs a gap below the magnet without touching it; or the fish rises beside the magnet unattached; or the fish stays in the air when the rod is moved away.
- P3 [major · gravity_direction]
  - expect: The line hangs straight down from the rod tip with the magnet at its end; the fish hangs below the magnet; anything that comes loose falls.
  - fail: The line stands out sideways or curves upward; or the fish hangs above the magnet; or a fish that comes off floats; or the magnet rises up the line.
- P4 [major · material_response]
  - expect: The fish are paper cut-outs that flex and swing; the line is a limp thread; the rod is a rigid stick.
  - fail: A fish is a rigid slab; or the line stands stiff like wire; or the rod bends double under a paper fish; or the fish stretches.
- P5 [fatal · permanence_count]
  - expect: The fish on the magnet is one of the fish from below; fish keep their number; nothing merges or passes through the floor.
  - fail: A fish appears on the magnet from nowhere; or a fish vanishes; or two fish merge; or the magnet passes through the floor of the pool.
- P6 [minor · attribute_drift]
  - expect: The fish's colours, the rod and the pool stay the same.
  - fail: A fish changes colour or shape; or the rod changes colour; or the pool changes.

**Note.** Who holds the rod is not judged.

## ELEC-0287 · magnet · eval

**Caption.** A magnet is slid up the outside of a glass of water, and a steel nut lying at the bottom rises up the inside of the glass behind it.

**Expectation (hidden).** The nut moves only where the magnet moves, staying on the inner face opposite the magnet, and stops when the magnet stops; it does not pass through the glass or drift on its own.

**Declared violation types.** causeless_motion, solidity

**SA**
- S1 [core] A glass of water with a steel nut lying at the bottom.
- S2 [core] A magnet is slid up the outside of the glass.
- S3 [core] The nut rises up the inside of the glass behind the magnet.
- S4 [minor] The nut stays on the inner face of the glass, opposite the magnet.
- S5 [minor] The magnet's movement comes first and the nut follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The nut moves only where and when the magnet moves, staying opposite it on the inner face, and stops when the magnet stops.
  - fail: The nut moves in a different direction from the magnet; or keeps rising after the magnet has stopped; or stays at the bottom while the magnet passes up beside it; or the nut sets off before the magnet has moved.
- P2 [core · solidity]
  - expect: The glass wall stays between magnet and nut: the nut stays inside the water and the magnet outside; neither passes through the glass.
  - fail: The nut passes through the glass onto the magnet; or the magnet passes into the water; or nut and magnet are seen touching with no glass between; or the nut passes through the bottom of the glass.
- P3 [major · gravity_direction]
  - expect: If the magnet is taken away the nut sinks back down through the water; the water stays level in the glass.
  - fail: The nut hangs in the water with the magnet gone; or rises on its own; or the water heaps up on the magnet's side; or the water rises out of the glass.
- P4 [major · material_response]
  - expect: The nut is a hard piece that slides along the inner face; the glass stays rigid; the water moves only in small ripples.
  - fail: The nut squashes against the glass; or the glass bends where the magnet presses; or the water moves as a solid block; or the nut leaves a groove in the glass.
- P5 [fatal · permanence_count]
  - expect: One nut, one magnet, one glass; nothing appears, vanishes or merges.
  - fail: A second nut appears; or the nut vanishes; or nut and magnet fuse; or the glass duplicates or changes shape.
- P6 [minor · attribute_drift]
  - expect: The glass, the water's colour and the magnet stay the same.
  - fail: The water changes colour; or the magnet changes colour or shape; or the glass changes shape.

## ELEC-0288 · magnet · eval

**Caption.** Sheets of paper are slid one at a time under a fridge magnet, and after several sheets the magnet loses its grip and slides down the door.

**Expectation (hidden).** The magnet holds through the first sheets and slips only once the stack is thick; it slides downward, not up or sideways; it does not hold no matter how thick the stack.

**Declared violation types.** missing_consequence, gravity_direction

**SA**
- S1 [core] A fridge magnet on a fridge door.
- S2 [core] Sheets of paper are slid one at a time under the magnet.
- S3 [core] After several sheets the magnet loses its grip and slides down the door.
- S4 [minor] The magnet holds through the first sheets.
- S5 [minor] The sheets go in one at a time, not as a stack.

**PC**
- P1 [core · missing_consequence]
  - expect: The magnet holds the first sheets against the door and gives way only when the stack has grown thick; it does not hold no matter how thick the stack.
  - fail: The magnet drops at the first sheet; or holds every sheet to the end of the clip however thick the stack; or the magnet slides while no new sheet is being added and the stack is still thin; or the stack stays up after the magnet has slid off.
- P2 [core · gravity_direction]
  - expect: When the magnet loses grip it slides downward along the door or drops; it does not move up or sideways.
  - fail: The magnet slides up the door; or moves sideways along the door; or floats away from the door; or slides down and then rises back.
- P3 [major · material_response]
  - expect: The sheets are paper: they slide in flat, bend slightly and hang as a stack; the magnet stays a hard piece.
  - fail: The sheets stand rigid like boards; or stretch; or the magnet squashes; or the paper flows into the door.
- P4 [major · causeless_motion]
  - expect: The magnet stays still between sheets; the fridge door does not move; other items on the door stay put.
  - fail: The magnet creeps while no sheet is being slid; or other magnets on the door drop; or the door swings open; or the sheets slide out by themselves.
- P5 [fatal · solidity]
  - expect: One magnet on the outside of the door with the sheets between; nothing sinks into or passes through the door.
  - fail: The magnet sinks into the door; or a sheet passes through the door or the magnet; or a second magnet appears; or the sheets vanish.
- P6 [minor · attribute_drift]
  - expect: The magnet's colour and design, the door and the sheets stay the same.
  - fail: The magnet changes colour or shape; or the door changes colour; or the sheets change size.

**Note.** How many sheets it takes is not judged, only that the magnet holds at first and gives way later.

## ELEC-0289 · magnet · eval

**Caption.** Two toy train cars are pushed together end to end and their magnetic couplers push apart; one car is turned around and the couplers snap together.

**Expectation (hidden).** With one orientation the cars separate over the last gap; after turning one car they pull together over that gap and stay joined; nothing happens while the cars are far apart.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] Two toy train cars with magnetic couplers.
- S2 [core] The cars are pushed together end to end and the couplers push apart.
- S3 [core] One car is turned around.
- S4 [core] The couplers snap together.
- S5 [minor] The same two cars are used throughout.
- S6 [minor] The order is push apart, turn, snap together.

**PC**
- P1 [core · causeless_motion]
  - expect: The cars move only when pushed or turned by hand and over the last small gap; while far apart nothing happens; once joined they stay joined and still.
  - fail: A car moves while the other is still far away; or the joined pair drifts apart; or a car slides about after being set down; or the cars spring apart after joining with nothing pulling them.
- P2 [core · missing_consequence]
  - expect: In the first orientation the couplers separate over the last gap; after one car is turned they pull together over that gap and stay joined.
  - fail: The couplers join in the first orientation; or after the turn they stop with a gap and stay that way; or they touch and slide apart after the turn; or the cars join and separate repeatedly.
- P3 [major · trajectory_momentum]
  - expect: The pushed-apart car slides straight back along the line of the track; the snap is along that line and the cars meet coupler to coupler.
  - fail: A car flies off sideways when pushed apart; or the cars jump together from far away; or a car lifts off the track; or the cars meet side to side.
- P4 [major · material_response]
  - expect: The cars are rigid toys that keep their shape; the couplers stay small hard fittings.
  - fail: A car squashes or bends; or the couplers stretch like rubber; or the cars flex as they roll.
- P5 [fatal · permanence_count]
  - expect: Two cars throughout, joined but separate at the end; nothing merges, vanishes or passes through anything.
  - fail: The two cars merge into one; or a third car appears; or a car vanishes during the turn; or one car passes through the other.
- P6 [minor · attribute_drift]
  - expect: The cars' colours and markings and the track stay the same.
  - fail: A car changes colour or markings; or the turned car becomes a different car; or the track changes.

## ELEC-0290 · magnet · eval

**Caption.** A ring magnet is dropped down a pencil standing upright toward another ring magnet at the base with like poles facing, and it stops and floats a little above the lower one.

**Expectation (hidden).** The falling ring slows and hovers with a visible gap above the lower ring instead of landing on it; it bobs and settles; it does not fall through the gap or fly off the pencil.

**Declared violation types.** gravity_direction, missing_consequence

**SA**
- S1 [core] A pencil stands upright with a ring magnet at its base.
- S2 [core] A second ring magnet is dropped down the pencil.
- S3 [core] The falling ring stops above the lower one.
- S4 [core] The upper ring floats with a gap above the lower one.
- S5 [minor] The falling ring is threaded onto the pencil.
- S6 [minor] The order is drop, slow, hover.

**PC**
- P1 [core · gravity_direction]
  - expect: The upper ring falls down the pencil, slows as it nears the lower ring and comes to hover with a visible gap above it; it does not land on it.
  - fail: The upper ring lands on the lower ring and rests there; or the upper ring rises back up the pencil; or it hovers high up the pencil far from the lower ring; or the lower ring rises to meet it.
- P2 [core · missing_consequence]
  - expect: The hovering ring bobs and settles at a steady height with the pencil through its centre; it stays there while nothing touches it.
  - fail: The upper ring passes through the gap and the lower ring; or flies off the pencil; or its bobbing grows until it flies up; or it settles and then drops onto the lower ring with nothing touching it.
- P3 [major · trajectory_momentum]
  - expect: The upper ring travels straight down along the pencil, staying threaded on it.
  - fail: The ring leaves the pencil and falls beside it; or tilts and jams then continues through the pencil; or spins off sideways; or moves upward at first.
- P4 [major · causeless_motion]
  - expect: The pencil stays upright and still; the lower ring stays at the base; the table does not move.
  - fail: The pencil topples or slides; or the lower ring slides up or off; or the table shifts; or the pencil spins.
- P5 [fatal · solidity]
  - expect: Two rings threaded on one pencil; the rings stay outside the pencil and each other; the pencil stays solid.
  - fail: A ring passes through the pencil's side; or the rings merge into one; or a third ring appears; or a ring passes through the table.
- P6 [minor · attribute_drift]
  - expect: The rings' colours, the pencil and the table stay the same.
  - fail: A ring changes colour or size; or the pencil changes colour or length; or the table changes.

## ELEC-0291 · magnet · eval

**Caption.** A steel paperclip hangs on a thread, and as a magnet is brought near it the clip swings toward the magnet and hangs at an angle in the air.

**Expectation (hidden).** The clip leans toward the magnet only when the magnet is close, tilting more as it approaches, and falls back to vertical when the magnet is taken away; it does not swing away from the magnet.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A steel paperclip hangs on a thread.
- S2 [core] A magnet is brought near the clip.
- S3 [core] The clip swings toward the magnet.
- S4 [core] The clip hangs at an angle in the air, leaning toward the magnet.
- S5 [minor] The thread stays taut with the clip at its end.
- S6 [minor] The approach comes first and the lean follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The clip hangs straight until the magnet is close, leans toward it more as it approaches, follows it as it moves and swings back to vertical when the magnet is taken away.
  - fail: The clip swings while the magnet is far off and still; or leans away from the magnet; or stays leaning after the magnet has been taken well away; or swings to and fro with the magnet held still.
- P2 [core · gravity_direction]
  - expect: The clip hangs from the thread, which stays taut from its anchor to the clip; the lean is toward the magnet and the thread points from the anchor to the clip.
  - fail: The thread goes slack while the clip hangs in the air; or the clip rises above its anchor; or the clip floats with the thread curving; or the clip hangs at an angle with no magnet near.
- P3 [major · trajectory_momentum]
  - expect: The clip moves along an arc about the thread's anchor; if it reaches the magnet it stops on it.
  - fail: The clip moves in a straight line off its arc; or the anchor point moves with the clip; or the clip reaches the magnet and bounces off repeatedly; or the thread stretches to let the clip reach.
- P4 [major · material_response]
  - expect: The thread is a limp line that stays straight under the clip's weight; the clip stays a rigid bent wire.
  - fail: The thread stands rigid like a rod; or stretches like elastic; or the clip bends as it leans; or the thread curls.
- P5 [fatal · permanence_count]
  - expect: One clip on one thread and one magnet; the clip stays on the thread; nothing appears, vanishes or passes into the magnet.
  - fail: The clip detaches from the thread and hangs in the air; or a second clip appears; or the clip sinks into the magnet; or the thread splits.
- P6 [minor · attribute_drift]
  - expect: The clip's colour, the thread and the magnet stay the same.
  - fail: The clip changes shape or colour; or the thread changes colour or length; or the magnet changes shape.

**Note.** Who holds the magnet is not judged.

## ELEC-0292 · magnet · eval

**Caption.** A magnet swinging on a string over a steel tray dips low on one swing and snaps down onto the tray, stopping dead.

**Expectation (hidden).** The magnet swings freely while high, is pulled down sharply only when it comes close to the steel, and stays stuck where it lands; it does not stick to the tray from far away or bounce off.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A magnet swings on a string over a steel tray.
- S2 [core] On one swing the magnet dips low toward the tray.
- S3 [core] The magnet snaps down onto the tray.
- S4 [core] The magnet stops dead on the tray.
- S5 [minor] The magnet swings freely before the dip.
- S6 [minor] The order is swinging, dip, snap, stopped.

**PC**
- P1 [core · causeless_motion]
  - expect: The magnet swings freely while high above the tray; it is pulled down only when it comes close to the steel; once on the tray it stays stuck and still.
  - fail: The magnet is pulled to the tray from high up; or stops in mid-swing far from the tray; or slides about on the tray after landing; or lifts off the tray again with nothing pulling it.
- P2 [core · missing_consequence]
  - expect: As the magnet comes close it is drawn sharply onto the tray and stops on contact; it does not bounce off.
  - fail: The magnet bounces off the tray and swings on; or hangs a gap above the tray without touching; or lands on the tray and slides off its edge; or dips close and swings away untouched.
- P3 [major · gravity_direction]
  - expect: The string hangs taut from its anchor while the magnet swings and goes slack once the magnet is on the tray; the tray stays on the table.
  - fail: The string stays taut and straight with the magnet on the tray below the anchor's reach; or the string stands rigid in the air; or the tray lifts toward the magnet; or the magnet rises above its anchor.
- P4 [major · trajectory_momentum]
  - expect: The swing is an arc about the anchor until the magnet is drawn down; the pull is toward the tray.
  - fail: The magnet swings in a straight line; or the anchor moves with the magnet; or the magnet is drawn sideways away from the tray; or the swing widens with nothing pushing it.
- P5 [fatal · permanence_count]
  - expect: One magnet on one string and one tray; the magnet stays on the string; nothing sinks into the tray or vanishes.
  - fail: The magnet detaches from the string in mid-air; or sinks into the tray; or a second magnet appears; or the tray vanishes.
- P6 [minor · attribute_drift]
  - expect: The magnet's colour, the string and the tray stay the same.
  - fail: The magnet changes colour or shape; or the tray changes colour; or the string changes length between swings.

**Note.** Who set the magnet swinging is not judged; the swing already under way is the caption's setup.

## ELEC-0293 · static · eval

**Caption.** A plastic cup pulled from a stack clings to the fingers and has to be shaken off.

**Expectation (hidden).** The cup stays on her hand when she opens her fingers and drops only after a shake; the other cups in the stack stay put.

**Declared violation types.** missing_consequence, gravity_direction

**SA**
- S1 [core] A stack of plastic cups.
- S2 [core] A cup is pulled from the stack.
- S3 [core] The cup clings to the fingers.
- S4 [core] The cup is shaken off.
- S5 [minor] The cup stays on the hand when the fingers open, before the shake.
- S6 [minor] The order is pull, cling, shake, drop.

**PC**
- P1 [core · missing_consequence]
  - expect: When the fingers open the cup stays against the hand with nothing gripping it, and comes away only with a shake.
  - fail: The cup drops the instant the fingers open; or hangs a gap away from the hand; or stays on the hand through the shake to the end of the clip; or the cup clings to the far side of the room.
- P2 [core · gravity_direction]
  - expect: Once shaken free the cup falls downward and lands; the other cups in the stack stay where they are.
  - fail: The freed cup floats or rises; or hangs in the air after the shake; or the stack rises toward the hand; or the cup climbs the arm.
- P3 [major · material_response]
  - expect: The cup is thin plastic that flexes in the fingers and springs back; the stack is cups nested one in another.
  - fail: The cup crumples like paper and stays crumpled; or stretches like rubber; or the stack moves as one solid block; or the cup melts.
- P4 [major · causeless_motion]
  - expect: The stack stays put as the cup is pulled; the cups do not move by themselves.
  - fail: The stack slides across the table; or several cups come up with the one pulled and then fly apart; or cups in the stack hop; or the cup crawls across the hand.
- P5 [fatal · permanence_count]
  - expect: One cup pulled from the stack; the cup stays whole and passes through nothing; the hand keeps its fingers.
  - fail: The cup vanishes; or two cups appear on the hand; or the cup passes through the hand; or fingers pass through the cup.
- P6 [minor · attribute_drift]
  - expect: The cups' colour, the stack and the table stay the same.
  - fail: The cup changes colour; or the stack changes height between frames with no cup taken; or the table changes.

**Note.** The hand is kept because the cling to the fingers is the physics; the person is otherwise not judged.

## ELEC-0294 · static · eval

**Caption.** A plastic comb rubbed on a wool scarf is held near a thin stream of water from a tap, and the stream bends toward the comb.

**Expectation (hidden).** The stream curves toward the comb only while the comb is close and straightens when it is moved away; an unrubbed comb has no effect; the water does not bend away from the comb.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A plastic comb is rubbed on a wool scarf.
- S2 [core] A thin stream of water runs from a tap.
- S3 [core] The comb is held near the stream.
- S4 [core] The stream bends toward the comb.
- S5 [minor] The stream is thin and steady.
- S6 [minor] The rub comes first, then the approach, then the bend.

**PC**
- P1 [core · causeless_motion]
  - expect: The stream runs straight down until the comb is close, bends only while the comb is near and straightens when the comb is moved away.
  - fail: The stream bends before the comb is brought near; or stays bent after the comb has been taken well away; or bends back and forth with the comb held still; or the stream bends while the comb is far off.
- P2 [core · missing_consequence]
  - expect: The bend is toward the comb: the stream curves to the comb's side below the point where the comb is held.
  - fail: The stream bends away from the comb; or bends above the comb's height; or the stream breaks up and stops flowing when the comb nears; or the comb draws the water up to it.
- P3 [major · gravity_direction]
  - expect: The water keeps falling downward throughout, bent or straight, and lands in the basin.
  - fail: The water rises toward the comb; or hangs in the air; or the stream flows upward from the basin; or drops fly sideways away from the comb.
- P4 [major · material_response]
  - expect: The water is a continuous thin stream that flexes as a liquid; the comb is a rigid piece.
  - fail: The stream moves as a stiff rod; or the water forms a solid strand that clings to the comb; or the comb bends toward the water; or the stream splits into a fan.
- P5 [fatal · permanence_count]
  - expect: One comb and one stream from one tap; the comb passes through nothing; the water does not vanish in mid-air.
  - fail: A second comb or stream appears; or the water vanishes before reaching the basin; or the comb passes into the tap; or the tap changes shape.
- P6 [minor · attribute_drift]
  - expect: The comb's colour, the scarf and the basin stay the same.
  - fail: The comb changes colour or shape; or the scarf changes pattern; or the basin changes.

**Note.** Who holds the comb is not judged.

## ELEC-0295 · static · eval

**Caption.** A plastic pipe rubbed on a fleece is held near an empty aluminium can lying on its side, and the can rolls toward the pipe.

**Expectation (hidden).** The can starts rolling only when the rubbed pipe is close, follows the pipe as it is moved, and stops when the pipe is taken away; it does not roll away from the pipe.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A plastic pipe is rubbed on a fleece.
- S2 [core] An empty aluminium can lies on its side.
- S3 [core] The pipe is held near the can.
- S4 [core] The can rolls toward the pipe.
- S5 [minor] The can is empty and on its side.
- S6 [minor] The rub comes first, then the approach, then the roll.

**PC**
- P1 [core · causeless_motion]
  - expect: The can lies still until the pipe is close, rolls only while the pipe is near, follows the pipe as it is moved and stops when the pipe is taken away.
  - fail: The can rolls before the pipe is brought near; or keeps rolling after the pipe has been taken well away; or rolls with the pipe held still and far off; or the can rolls before the pipe has been rubbed.
- P2 [core · missing_consequence]
  - expect: The can rolls toward the pipe, not away from it, and follows the pipe's side.
  - fail: The can rolls away from the pipe; or rolls at right angles to the pipe's direction; or lifts toward the pipe; or spins in place without rolling.
- P3 [major · trajectory_momentum]
  - expect: The can rolls on its side along the surface, turning about its axis as it moves.
  - fail: The can slides without turning; or rolls uphill; or tumbles end over end; or leaves the surface.
- P4 [major · material_response]
  - expect: The can is a rigid cylinder that keeps its shape as it rolls; the pipe is a rigid tube.
  - fail: The can dents or squashes as it rolls; or bends toward the pipe; or the pipe droops; or the can stretches.
- P5 [fatal · permanence_count]
  - expect: One can and one pipe; nothing appears, vanishes or passes through the table.
  - fail: A second can appears; or the can vanishes; or the can passes through the pipe or the table; or the pipe duplicates.
- P6 [minor · attribute_drift]
  - expect: The can's label, the pipe's colour and the surface stay the same.
  - fail: The can's label changes; or the pipe changes colour; or the surface changes pattern.

**Note.** Who holds the pipe is not judged.

## ELEC-0296 · static · eval

**Caption.** A small ball of aluminium foil hangs on a thread, and it swings toward a plastic rod that has been rubbed on wool as the rod is brought near.

**Expectation (hidden).** The ball leans toward the rod only when the rod is close and hangs straight again when it is removed; it does not move toward an unrubbed rod.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A small ball of aluminium foil hangs on a thread.
- S2 [core] A plastic rod is rubbed on wool.
- S3 [core] The rod is brought near the ball.
- S4 [core] The ball swings toward the rod.
- S5 [minor] The thread stays taut with the ball at its end.
- S6 [minor] The rub comes first, then the approach, then the swing.

**PC**
- P1 [core · causeless_motion]
  - expect: The ball hangs straight until the rod is close, leans toward it while it is near and hangs straight again when the rod is removed.
  - fail: The ball swings before the rod is brought near; or stays leaning after the rod has been taken well away; or swings to and fro with the rod held still; or the ball moves while the rod is far off.
- P2 [core · missing_consequence]
  - expect: The lean is toward the rod: the ball moves to the rod's side of vertical, along the line from ball to rod.
  - fail: The ball leans away from the rod; or moves at right angles to the line to the rod; or rises straight up; or the rod is drawn to the ball.
- P3 [major · gravity_direction]
  - expect: The ball hangs from the thread, which stays taut from anchor to ball; the ball does not rise above its anchor.
  - fail: The thread goes slack while the ball hangs in the air; or the ball rises above its anchor; or the ball floats with the thread curving; or the ball hangs at an angle with no rod near.
- P4 [major · material_response]
  - expect: The thread is a limp line that stays straight under the ball's weight; the ball is a crumpled foil sphere that keeps its shape.
  - fail: The thread stands rigid like a rod; or stretches like elastic; or the ball flattens or unfolds; or the ball melts.
- P5 [fatal · permanence_count]
  - expect: One ball on one thread and one rod; the ball stays on the thread; nothing appears, vanishes or passes into the rod.
  - fail: The ball detaches from the thread and hangs in the air; or a second ball appears; or the ball sinks into the rod; or the thread splits.
- P6 [minor · attribute_drift]
  - expect: The foil's finish, the thread and the rod's colour stay the same.
  - fail: The ball changes colour or size; or the thread changes colour or length; or the rod changes colour.

**Note.** Who holds the rod is not judged.

## ELEC-0297 · static · eval

**Caption.** The protective film is peeled off a new television screen, and it clings to the hand holding it and crackles.

**Expectation (hidden).** The film sticks to the skin and to itself where it touches and has to be pulled free; it does not drop straight down.

**Declared violation types.** missing_consequence, material_response

**SA**
- S1 [core] A new television with a protective film on its screen.
- S2 [core] The film is peeled off the screen.
- S3 [core] The film clings to the hand holding it.
- S4 [minor] The film is thin and transparent.
- S5 [minor] The peel comes first and the clinging follows.

**PC**
- P1 [core · missing_consequence]
  - expect: As the film comes off it wraps onto the hand and arm where it touches and its folds stick to each other; it has to be pulled free and does not drop straight down.
  - fail: The film hangs straight down from the fingers like paper and touches nothing; or a part on the hand falls away on its own; or folds that meet slide apart with nothing pulling them; or the film stands out stiff from the hand.
- P2 [core · material_response]
  - expect: The film is a thin limp sheet: it wrinkles, folds and stretches slightly, and peels off with a tug.
  - fail: The film holds a flat rigid shape like a board; or drapes in heavy folds like cloth; or stretches out long like rubber and snaps back; or tears into shards like glass.
- P3 [major · gravity_direction]
  - expect: Parts of the film not stuck to anything hang downward; if the film is let go entirely it falls.
  - fail: A free edge rises or stands out sideways with nothing near it; or the film floats when let go; or the film climbs up the arm.
- P4 [major · causeless_motion]
  - expect: The television stays where it stands; the film moves only with the hand or as it settles onto it.
  - fail: The television tips or slides; or the film crawls over the hand after settling; or the film jumps between spots on the arm with nothing touching it.
- P5 [fatal · permanence_count]
  - expect: One film from one screen; the film stays one piece and passes through nothing; the screen keeps its shape.
  - fail: The film splits into several pieces after the peel; or vanishes; or passes through the screen; or a second television appears.
- P6 [minor · attribute_drift]
  - expect: The television's frame, the screen beneath the film and the room stay the same.
  - fail: The frame changes colour; or the screen shows a picture that changes with the peel; or the room's contents rearrange.

**Note.** The hand is kept because the cling to it is the physics; the person is otherwise not judged. The crackle is sound and is not judged.

## ELEC-0298 · static · eval

**Caption.** A plastic pen rubbed on a wool sleeve is held over pepper grains scattered on a plate, and the grains jump onto the pen.

**Expectation (hidden).** Grains leap only when the rubbed pen is close and cling to it; an unrubbed pen does nothing.

**Declared violation types.** causeless_motion, gravity_direction

**SA**
- S1 [core] A plastic pen is rubbed on a wool sleeve.
- S2 [core] Pepper grains are scattered on a plate.
- S3 [core] The pen is held over the grains.
- S4 [core] Grains jump onto the pen.
- S5 [minor] The grains are scattered loose on the plate, not in a pile.
- S6 [minor] The rub comes first, then the hold, then the jump.

**PC**
- P1 [core · causeless_motion]
  - expect: The grains lie still until the pen is close above them, then leap up to it; grains far from the pen stay put and the leaping stops when the pen is taken away.
  - fail: Grains leap before the pen is brought near; or grains across the plate slide toward the pen; or the whole plate of grains stirs at once; or grains keep leaping after the pen is well away.
- P2 [core · gravity_direction]
  - expect: The grains that lift cling to the pen's underside and sides; any that let go fall back to the plate.
  - fail: Grains hover in the air between plate and pen without touching either; or a grain that lets go drifts upward or sideways; or grains rise past the pen and continue up; or the plate lifts toward the pen.
- P3 [major · trajectory_momentum]
  - expect: Each grain moves straight up from the plate to the pen and stops on it.
  - fail: Grains fly past the pen and off; or circle the pen in the air; or bounce off and back several times; or grains move away from the pen.
- P4 [major · material_response]
  - expect: The pen is a rigid stick; the grains are separate hard specks that lift individually.
  - fail: The pen bends toward the plate; or the grains lift as one lump; or grains smear into a paste; or the plate bends.
- P5 [fatal · permanence_count]
  - expect: One pen and one plate; the grains on the pen came from the plate; nothing appears, vanishes or passes through the plate.
  - fail: Grains multiply on the pen; or grains vanish in mid-air; or the pen passes into the plate; or a second pen appears.
- P6 [minor · attribute_drift]
  - expect: The pen's colour, the plate and the sleeve stay the same.
  - fail: The pen changes colour or shape; or the plate changes pattern; or the sleeve changes colour.

**Note.** Who holds the pen is not judged.

## ELEC-0299 · static · eval

**Caption.** A cat rubs against a wool blanket in a dark room, and tiny sparks crackle in its fur.

**Expectation (hidden).** The sparks appear only where the fur moves against the wool and vanish instantly; nothing glows when the cat is still.

**Declared violation types.** process_direction, permanence_count

**SA**
- S1 [core] A cat and a wool blanket in a dark room.
- S2 [core] The cat rubs against the blanket.
- S3 [core] Tiny sparks flash in its fur.
- S4 [minor] The room is dark.
- S5 [minor] The sparks come while the fur moves against the wool, not while the cat is still.

**PC**
- P1 [core · process_direction]
  - expect: The sparks appear only where the fur moves against the wool and each is gone at once; nothing glows while the cat is still.
  - fail: The fur glows steadily like a lamp; or sparks keep flashing after the cat has stopped moving; or a spark stays lit at one spot; or sparks appear on parts of the cat far from the blanket.
- P2 [core · permanence_count]
  - expect: One cat and one blanket; the sparks leave nothing behind on the fur or the wool.
  - fail: Glowing dots stay on the fur after a spark; or a second cat appears; or the blanket vanishes; or the sparks detach and float about the room.
- P3 [major · missing_consequence]
  - expect: The sparks are small: they brighten only the fur right around them and not the room.
  - fail: The room lights up with each spark as if a lamp came on; or the sparks throw shadows across the walls; or the sparks stay lit and light the room.
- P4 [major · material_response]
  - expect: The fur is soft and parts and lifts where it rubs; the blanket is cloth that drapes and shifts under the cat.
  - fail: The fur moves as a rigid shell; or the blanket stands stiff like a board; or the fur stretches like elastic; or the blanket flows like liquid.
- P5 [fatal · shape_identity]
  - expect: One cat with its head, legs and tail; the cat passes through nothing and does not merge with the blanket.
  - fail: The cat gains or loses a limb or changes size; or passes through the blanket or furniture; or merges with the blanket; or a second cat appears from nowhere.
- P6 [minor · attribute_drift]
  - expect: The cat's coat colour and pattern and the blanket's colour stay the same apart from the sparks.
  - fail: The coat changes colour or pattern; or the blanket changes colour; or the room's contents rearrange.

**Note.** The cat is an animal and its movements are not causeless motion. The crackle is sound and is not judged.

## ELEC-0300 · static · eval

**Caption.** Soap bubbles drift past a balloon that has been rubbed on wool, and they curve toward the balloon and cling to it.

**Expectation (hidden).** Bubbles change course toward the balloon only when they come near it and stick or pop on its surface; bubbles far from the balloon drift straight on; none curves away from it.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A balloon that has been rubbed on wool.
- S2 [core] Soap bubbles drift past the balloon.
- S3 [core] The bubbles curve toward the balloon.
- S4 [core] The bubbles cling to the balloon.
- S5 [minor] The bubbles are drifting through the air before they near the balloon.
- S6 [minor] The drift comes first and the curve and cling follow.

**PC**
- P1 [core · causeless_motion]
  - expect: Bubbles change course toward the balloon only when they come near it; bubbles far from the balloon drift straight on; none curves away from it.
  - fail: A bubble curves away from the balloon; or bubbles far across the room swerve toward it; or a bubble changes course with the balloon nowhere near; or bubbles circle the balloon in the air.
- P2 [core · missing_consequence]
  - expect: Bubbles that reach the balloon stick to its surface or pop on it; those stuck stay where they land.
  - fail: A bubble reaches the balloon and bounces off to drift on; or hangs a gap from the balloon without touching; or stuck bubbles slide about on the balloon; or bubbles pass through the balloon and out the other side.
- P3 [major · gravity_direction]
  - expect: Away from the balloon the bubbles drift and sink slowly; none rise steadily away or hang fixed in the air.
  - fail: Bubbles rise steadily to the ceiling with nothing blowing them; or hang fixed in the air; or fall like stones.
- P4 [major · material_response]
  - expect: The bubbles are thin films that wobble, cling as a dome and pop into nothing; the balloon keeps its round shape.
  - fail: A bubble bounces like a rubber ball; or keeps its shape after popping; or the balloon dents deeply and stays dented; or a bubble passes into the balloon as a solid ball.
- P5 [fatal · permanence_count]
  - expect: One balloon; bubbles vanish only by popping; none appear from nowhere in mid-air near the balloon; the balloon passes through nothing.
  - fail: Bubbles appear from nowhere beside the balloon; or a bubble vanishes without popping in mid-drift; or the balloon duplicates or vanishes; or the balloon passes through a wall or table.
- P6 [minor · attribute_drift]
  - expect: The balloon's colour and the room stay the same.
  - fail: The balloon changes colour or size; or the room's contents rearrange; or the bubbles change colour.

**Note.** Who blows the bubbles or holds the balloon is not judged.

