# Rubric review

96 rubrics. SA = caption adherence (core/minor); PC = physics (fatal/core/major/minor, each tagged with a violation type). Expectation is the hidden field from data/, shown for the reviewer only.

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

## ACOU-0005 · struck_vibration · train

**Caption.** A taut rubber band stretched between two nails is flicked, and the band blurs and hums before going still.

**Expectation (hidden).** The band becomes a fuzzy band right after the flick and narrows back to a line; it does not start moving on its own.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A rubber band is stretched between two nails.
- S2 [core] The band is flicked.
- S3 [core] The band blurs: it vibrates visibly.
- S4 [core] The band goes still again, a sharp line.
- S5 [minor] The band is taut, a straight line between the nails, before the flick.
- S6 [minor] The order is flick, blur, stillness.

**PC**
- P1 [core · causeless_motion]
  - expect: The band is a sharp, still line until the finger reaches it; it blurs at the flick and only then, and does not start again by itself.
  - fail: The band is already fuzzy before the finger arrives; or blurs while the finger is still well away from it; or stays a sharp line as the finger snaps it; or goes still and blurs again with nothing touching it.
- P2 [core · process_direction]
  - expect: The fuzzy band is widest right after the flick and only narrows until the band is a line again.
  - fail: The fuzzy band widens again after it has begun to narrow; or keeps the same width for the whole clip; or goes from a wide blur to a sharp line in a single instant with no narrowing in between.
- P3 [major · material_response]
  - expect: The band vibrates as a stretched elastic between two fixed ends: the blur lies between the nails, widest near the middle, and both ends stay looped on their nails.
  - fail: The band slips off a nail; or the blur is widest at a nail and absent in the middle; or the band sags and hangs slack between the nails; or the band stretches longer and stays stretched.
- P4 [major · causeless_motion]
  - expect: The nails and the board or wall they stand in stay fixed; only the band moves.
  - fail: A nail bends or leans with the flick; or a nail slides along the board; or the board or wall behind the band ripples.
- P5 [fatal · permanence_count]
  - expect: One band and two nails throughout; the band stays one loop and passes through nothing.
  - fail: A second band appears; or the band splits into two strands; or the band passes through a nail or through the finger; or a nail vanishes.
- P6 [minor · attribute_drift]
  - expect: The band's colour, the nail heads and the board behind stay the same.
  - fail: The band changes colour; or the nail heads change shape; or the board's grain or colour changes.

**Note.** The hum is inaudible in the frames and is not judged; the blur is its visible sign.

## ACOU-0006 · struck_vibration · train

**Caption.** A wine glass half full of water is tapped on the rim with a spoon, and the water surface inside breaks into fine ripples while the glass rings.

**Expectation (hidden).** The ripples appear only at the tap and fade as the ringing dies; the glass itself is not seen moving and the water does not slosh as if the glass had been shaken.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A wine glass about half full of water.
- S2 [core] A spoon taps the rim of the glass.
- S3 [core] The water surface breaks into ripples.
- S4 [minor] The ripples are fine and small, not a large slosh.
- S5 [minor] The tap lands on the rim, not on the bowl or the stem.
- S6 [minor] The tap comes first and the ripples follow.

**PC**
- P1 [core · causeless_motion]
  - expect: The water surface is flat and still until the spoon touches the rim; ripples appear at the tap and only then.
  - fail: Ripples are on the surface before the spoon reaches the rim; or appear while the spoon is well away from the glass; or the spoon strikes the rim and the surface stays mirror-flat; or the water ripples again after settling with the spoon nowhere near.
- P2 [core · process_direction]
  - expect: The ripples are strongest right after the tap and fade steadily to a flat surface.
  - fail: The ripples grow stronger after the tap with no second tap; or keep the same strength for the whole clip; or the surface goes flat and breaks up again on its own; or a fully rippled surface turns flat in a single instant.
- P3 [major · material_response]
  - expect: The ripples are a fine pattern on the water's surface; the glass stays a rigid vessel and the water stays inside it.
  - fail: The glass bowl flexes or wobbles like rubber at the tap; or the water sloshes as one wave up the side of the bowl; or droplets fly out of the glass.
- P4 [major · causeless_motion] (if: The glass stands on a table or other surface rather than being held.)
  - expect: The glass stands where it is; the rim tap leaves it in place and only the water surface moves.
  - fail: The glass slides or rocks on its base at the tap; or tilts and holds the tilt; or moves across the surface it stands on with nothing touching it.
- P5 [fatal · permanence_count]
  - expect: One glass, one spoon, the same amount of water; nothing passes through anything.
  - fail: The spoon passes through the rim or into the bowl wall; or the water level jumps up or down; or a second glass appears; or the glass changes shape.
- P6 [minor · attribute_drift]
  - expect: The glass's tint, the water's colour and the setting around them stay the same.
  - fail: The water changes colour; or the glass's tint or pattern changes; or objects around the glass shift by themselves.

**Note.** The ringing is inaudible and is not judged; the ripples are its visible sign. The caption does not say whether the glass stands or is held, so P4 applies only when it stands on a surface.

## ACOU-0007 · struck_vibration · train

**Caption.** A struck tuning fork is dipped into a glass of water, and the water sprays up where the prongs touch it.

**Expectation (hidden).** The water is still before the prongs reach it, spray and ripples burst out only at the moment of contact and only while the prongs touch the surface, and the surface settles once the fork is lifted; the spray does not start before contact or continue with the fork out of the water.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A tuning fork and a glass of water are present.
- S2 [core] The fork is lowered so that its prongs touch the water.
- S3 [core] Water sprays up where the prongs meet the surface.
- S4 [minor] The fork has been struck: a strike is seen, or the prongs are blurred or shivering before they reach the water.
- S5 [minor] The spray comes from the point where the prongs touch, not from elsewhere on the surface.
- S6 [minor] The prongs reach the water first and the spray follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The water surface is flat until the prongs touch it; spray and ripples burst out at the point of contact and only there.
  - fail: The surface ripples or spits before the prongs reach it; or spray rises from a part of the surface the prongs are not touching; or the prongs enter the water and the surface stays flat around them; or the water sprays while the fork is held above the surface.
- P2 [core · process_direction]
  - expect: The spraying lasts only while the prongs are in the water and dies down as the fork's shiver fades; when the fork is lifted the spray stops and the surface settles.
  - fail: Spray continues from the surface after the fork is lifted clear; or the disturbed surface never settles though the fork is out of the water; or the surface is calm while the prongs are in and erupts once they are out; or the spray grows stronger the longer the prongs stay in.
- P3 [major · gravity_direction]
  - expect: Droplets thrown up fall back onto the surface, the glass or the table; the water level in the glass stays where it is.
  - fail: Droplets hang in the air; or rise and drift away upward; or water climbs the prongs above the surface and stays there.
- P4 [major · material_response]
  - expect: The fork stays a rigid metal fork and the glass a rigid vessel; the water behaves as a liquid, breaking into drops and ripples.
  - fail: The prongs bend or splay apart as they enter the water; or the water surface bulges and holds its shape like jelly; or the glass wall flexes; or the prongs leave a hole in the water that stays open.
- P5 [fatal · permanence_count]
  - expect: One fork and one glass; the fork passes through the water surface only and through nothing solid; nothing appears or vanishes.
  - fail: The prongs pass through the glass wall or its base; or a second fork or glass appears; or the fork vanishes while the glass is still in view; or the fork gains or loses a prong.
- P6 [minor · attribute_drift]
  - expect: The glass's shape and tint, the fork's finish and the table around them stay the same.
  - fail: The glass changes tint or shape; or the fork changes colour; or items on the table shift without being touched.

**Note.** The strike may happen before the clip begins; S4 fails only when neither a strike nor a shivering fork is seen. The sound of the fork is not judged.

## ACOU-0008 · struck_vibration · train

**Caption.** A single string of an upright bass is plucked, and the thick string swings visibly from side to side before settling.

**Expectation (hidden).** The swing is widest right after the pluck and shrinks steadily; the string does not stop dead or swing wider on its own.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] An upright bass is present.
- S2 [core] One string is plucked.
- S3 [core] The plucked string swings visibly from side to side.
- S4 [core] The string settles to stillness.
- S5 [minor] Only a single string is plucked; the others are not.
- S6 [minor] The order is pluck, swing, settle.

**PC**
- P1 [core · causeless_motion]
  - expect: The string hangs as a sharp, still line until the finger pulls it; it swings from the pluck and only then; the other strings stay still.
  - fail: The string swings before the finger reaches it; or a different string swings from the one plucked; or all the strings swing together; or the string goes still and swings again with the hand away from it.
- P2 [core · process_direction]
  - expect: The swing is widest right after the release and shrinks steadily until the string hangs straight.
  - fail: The swing widens again after it has begun to shrink; or holds the same width for the whole clip; or the string stops dead from a wide swing to a straight line.
- P3 [major · material_response]
  - expect: The string stays anchored at the nut and the bridge: the swing is widest between them and both ends stay put.
  - fail: An end of the string lifts off the bridge or the nut; or the swing is widest at the bridge with the middle still; or the string sags and hangs loose like a rope; or the string stretches visibly longer.
- P4 [major · causeless_motion]
  - expect: The bass's body, neck and bridge stay still; only the plucked string swings.
  - fail: The neck bends with the pluck; or the body rocks on its endpin; or the bridge slides across the top.
- P5 [fatal · permanence_count]
  - expect: The same set of strings throughout; the plucked string stays one string and passes through nothing.
  - fail: A string appears or vanishes; or the plucked string splits into two; or the string passes through the fingerboard or the finger; or the bass changes shape.
- P6 [minor · attribute_drift]
  - expect: The bass's varnish, the fingerboard and the tuning pegs stay the same.
  - fail: The body changes colour; or the fingerboard's markings change; or a tuning peg moves while untouched.

## ACOU-0009 · struck_vibration · train

**Caption.** A large cymbal is struck, and the cymbal wobbles on its stand and its edge blurs before it steadies.

**Expectation (hidden).** The wobble and blur begin at the strike and die away over several seconds; the cymbal does not move before the stick reaches it.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A large cymbal on a stand.
- S2 [core] The cymbal is struck.
- S3 [core] The cymbal wobbles on its stand and its edge blurs.
- S4 [core] The cymbal steadies.
- S5 [minor] The cymbal stays seated on its stand through the wobble.
- S6 [minor] The order is strike, wobble, steady.

**PC**
- P1 [core · causeless_motion]
  - expect: The cymbal hangs still on its stand until the stick reaches it; the wobble and the edge blur begin at the strike and only then.
  - fail: The cymbal is already rocking or blurred before the stick arrives; or wobbles while the stick is well away; or is hit and stays rigidly still; or steadies and starts wobbling again with nothing touching it.
- P2 [core · process_direction]
  - expect: The wobble is largest right after the strike and shrinks steadily; the edge blur narrows until the rim is sharp and still.
  - fail: The wobble grows after the strike with no second hit; or holds the same size for the whole clip; or the cymbal stops dead from a large wobble.
- P3 [major · material_response]
  - expect: The cymbal stays a rigid metal disc that tilts and rocks as a whole about the stand's tip.
  - fail: The cymbal folds or creases; or the stick sinks into the metal; or a dent appears where the stick lands and stays; or the rim curls.
- P4 [major · trajectory_momentum]
  - expect: The cymbal wobbles about the stand's tip, staying centred on it and tilting one way then the other; the stand stays put.
  - fail: The cymbal slides off the stand's tip; or spins round and round like a plate; or lifts clear of the stand and hangs in the air; or the stand's base slides across the floor.
- P5 [fatal · permanence_count]
  - expect: One cymbal, one stand and one stick; the stick passes through nothing and the cymbal stays one disc.
  - fail: The stick passes through the cymbal; or the cymbal splits or a second cymbal appears; or the stand vanishes; or the cymbal changes into another object.
- P6 [minor · attribute_drift]
  - expect: The cymbal's finish and lathing, the stand's colour and the background stay the same.
  - fail: The cymbal changes colour or finish; or the stand's height changes between frames; or the background changes.

## ACOU-0010 · struck_vibration · train

**Caption.** Grains of rice lie on an upturned metal pot lid on a table; the lid is struck once with a spoon and the grains jump.

**Expectation (hidden).** The grains are still before the strike, jump up together at the moment of the strike and land back on the lid or scatter off its edge; they do not jump before the strike or keep jumping once the lid is quiet.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] An upturned metal pot lid lies on a table with grains of rice on it.
- S2 [core] A spoon strikes the lid.
- S3 [core] The grains jump.
- S4 [minor] The strike is a single hit.
- S5 [minor] The lid rests upturned on the table rather than sitting on a pot.
- S6 [minor] The strike comes first and the jump follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The grains lie still on the lid until the spoon lands; they jump at the strike and only then.
  - fail: Grains skitter or hop before the spoon reaches the lid; or jump while the spoon is well away; or the spoon strikes and every grain stays put; or the grains lift one after another in a wave rather than together at the blow.
- P2 [core · process_direction]
  - expect: The first hop is the biggest; later hops are smaller until the grains lie still on the lid.
  - fail: The grains keep hopping at the same height for the whole clip after the one strike; or hop higher with each bounce; or lie still and then hop again with the spoon away from the lid.
- P3 [major · gravity_direction]
  - expect: Grains that jump fall back onto the lid, onto the table or off the lid's edge.
  - fail: Grains hang in the air above the lid; or drift upward and away; or grains that fell off the edge return onto the lid.
- P4 [major · material_response]
  - expect: The lid is a rigid metal disc: the spoon rebounds from it and the lid may chatter on the table but keeps its shape.
  - fail: The spoon sinks into the lid or leaves a dent that stays; or the lid flexes like rubber; or the lid flips over and the grains stay stuck to it.
- P5 [fatal · permanence_count]
  - expect: The grains keep their number, allowing for some rolling off; one lid and one spoon; nothing passes through anything.
  - fail: New grains appear on the lid after the strike; or all the grains disappear at once; or the spoon passes through the lid; or the lid sinks into the table.
- P6 [minor · attribute_drift]
  - expect: The lid's finish, the grains' colour and the table's surface stay the same.
  - fail: The lid changes colour or gains a pattern; or the grains change colour; or the table surface changes texture.

## ACOU-0011 · struck_vibration · train

**Caption.** A small scrap of paper rests on a bass string inside a grand piano with the lid open; the key for that string is pressed, and the paper jumps off the string.

**Expectation (hidden).** The paper lies still until the key is pressed, is flicked up and off the string the instant the note sounds, and falls onto neighbouring strings or the frame; only the struck string's paper moves, and it does not jump before the key goes down or float back into place.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A grand piano with its lid open and its strings in view.
- S2 [core] A small scrap of paper rests on one of the bass strings.
- S3 [core] A key is pressed: a hand on the keyboard or a hammer rising to the strings.
- S4 [core] The paper jumps off the string.
- S5 [minor] The paper sits on a thick bass string, not a thin treble one.
- S6 [minor] The key press comes first and the paper's jump follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The paper lies still on its string until the key is pressed; it is flung off as the hammer strikes and only then.
  - fail: The paper hops or slides before any key goes down or hammer moves; or jumps while the keys and hammers are seen at rest; or the hammer strikes the string and the paper stays flat on it; or paper on a string that was not struck jumps too.
- P2 [core · process_direction]
  - expect: Once flung off, the paper falls and comes to rest on neighbouring strings or the frame and stays there.
  - fail: The paper returns to its spot on the string it left; or keeps hopping on and off the string for the whole clip after a single press; or is at rest on the frame and then jumps back up with no further key press.
- P3 [major · gravity_direction]
  - expect: After the flick the paper falls, fluttering down onto the strings below or the frame.
  - fail: The paper hangs in the air above the strings; or drifts upward toward the raised lid; or slides along a string without dropping.
- P4 [major · causeless_motion]
  - expect: Only the struck string and its hammer move: the string blurs, the hammer rises and falls back; the neighbouring strings stay sharp and the other hammers stay down.
  - fail: Several hammers rise for one key press; or the neighbouring strings blur along with the struck one; or the strings sway like slack ropes.
- P5 [fatal · permanence_count]
  - expect: One scrap of paper and the same strings and hammers; the paper passes through nothing and nothing appears or vanishes.
  - fail: The paper vanishes in mid-air; or a second scrap appears; or the paper passes through a string or the frame; or a string or hammer vanishes.
- P6 [minor · attribute_drift]
  - expect: The piano's frame colour, the strings' spacing and the lid stay the same.
  - fail: The frame changes colour; or the strings change spacing while untouched; or the lid changes angle by itself; or the paper changes colour or size while at rest.

**Note.** The keyboard may be out of frame; a hammer rising toward the strings counts as the key press for S3 and P1. The sound of the note is not judged.

## ACOU-0012 · struck_vibration · train

**Caption.** A few grains of salt lie on a xylophone bar; the bar is struck with a mallet and the grains jump off.

**Expectation (hidden).** The salt is still until the strike, leaps off the bar at the strike and does not return; only the struck bar's salt moves.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A xylophone with a few grains of salt lying on one bar.
- S2 [core] A mallet strikes that bar.
- S3 [core] The grains jump off the bar.
- S4 [minor] The salt is a few grains, not a heap.
- S5 [minor] The mallet strikes the bar carrying the salt, not a different bar.
- S6 [minor] The strike comes first and the jump follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The grains lie still until the mallet hits the bar; they leap at the strike and only then; salt or dust on other bars stays put.
  - fail: Grains hop before the mallet lands; or leap while the mallet is still on its way down, clear of the bar; or the mallet lands and the grains stay where they are; or grains on a bar that was not struck jump too.
- P2 [core · process_direction]
  - expect: The grains leave the bar and come to rest in the gaps, on the frame or on neighbouring bars; they do not return to the struck bar or keep hopping.
  - fail: Grains settle back onto the struck bar in their original places; or keep hopping on the bar for the whole clip after one strike; or come to rest and then jump again with the mallet away.
- P3 [major · gravity_direction]
  - expect: The grains fall after the leap, landing on the frame, in the gaps between bars or on other bars.
  - fail: Grains hang in the air above the bar; or rise and drift away upward; or grains that fell between the bars climb back up onto a bar.
- P4 [major · material_response]
  - expect: The bar is a rigid slab: the mallet rebounds from it and the bar stays seated in its cradle.
  - fail: The mallet sinks into the bar; or the bar bends like rubber under the stroke; or the bar leaps out of its cradle.
- P5 [fatal · permanence_count]
  - expect: The grains keep their number, allowing for some passing out of view; one mallet; the bars keep their count and shape, and nothing passes through anything.
  - fail: New grains appear on the bar after the strike; or all the grains vanish in one frame; or the mallet passes through a bar; or bars change count or merge.
- P6 [minor · attribute_drift]
  - expect: The bars' colours and lettering, the frame and the mallet head stay the same.
  - fail: A bar changes colour or its letter changes; or the mallet head changes colour or size; or the frame changes.

## ACOU-0013 · struck_vibration · train

**Caption.** A thin sheet-metal door is knocked on, and the panel visibly flexes and rattles under the knocks before going quiet.

**Expectation (hidden).** The panel moves at each knock and the rattle dies out between knocks; the door does not keep shaking after the knocking stops.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A thin sheet-metal door.
- S2 [core] The door is knocked on: a hand raps the panel.
- S3 [core] The panel flexes and rattles with the knocks.
- S4 [core] The panel goes still after the knocking.
- S5 [minor] The knocking is a series of raps rather than a single blow.
- S6 [minor] The flexing comes with the knocks and the stillness follows the last knock.

**PC**
- P1 [core · causeless_motion]
  - expect: The panel is still before the first knock; each flex begins as the knuckles land; the panel does not move by itself between or after knocks.
  - fail: The panel is already shaking before the hand reaches it; or flexes while the hand is drawn back and away; or the hand raps and the panel stays rigid; or the door starts rattling again after it has gone still with nothing touching it.
- P2 [core · process_direction]
  - expect: Each knock's shake fades before or as the next knock lands, and after the last knock the rattle dies away to stillness.
  - fail: The rattle grows after the knocking stops; or keeps the same shaking for the whole clip after the last knock; or the panel stops dead from a hard shake the instant the hand leaves it.
- P3 [major · material_response]
  - expect: The panel flexes as a thin sheet: it dimples inward at the knuckles and springs back flat; the frame and hinges stay rigid.
  - fail: A dimple stays pressed in after the hand lifts; or the panel folds like cloth; or the door frame bends with each knock; or a wave rolls across the whole panel like water.
- P4 [major · causeless_motion]
  - expect: The wall, the door frame and any neighbouring panels stay still; only the knocked panel shivers.
  - fail: The wall beside the door shakes; or a neighbouring panel rattles while the knocked one is still; or the door frame jumps in the wall.
- P5 [fatal · solidity]
  - expect: One door with its panel, frame and handle; the hand passes through nothing and the door stays one piece.
  - fail: The hand passes into or through the panel; or the panel splits or a hole opens where the hand lands; or the handle vanishes or moves to another spot; or the door changes into another object.
- P6 [minor · attribute_drift]
  - expect: The door's paint, any rust or marks on it, and the surroundings stay the same.
  - fail: The door changes colour; or marks and scratches on it shift or vanish; or the surroundings change.

## ACOU-0014 · struck_vibration · train

**Caption.** A long wooden fishing rod is tapped against a post, and the tip whips back and forth in a blur before settling.

**Expectation (hidden).** The tip's swings are large right after the tap and shrink steadily; the handle end barely moves.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A long fishing rod and a post are present.
- S2 [core] The rod is tapped against the post.
- S3 [core] The tip whips back and forth in a blur.
- S4 [core] The tip settles.
- S5 [minor] The rod is long and wooden.
- S6 [minor] The tap comes first and the whipping follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The rod is still until it meets the post; the tip begins to whip at the tap and only then.
  - fail: The tip is already whipping before the rod touches the post; or whips while the rod is held away from the post; or the rod knocks the post and the tip stays rigid; or the tip settles and starts whipping again with no second tap.
- P2 [core · process_direction]
  - expect: The tip's swings are largest right after the tap and shrink steadily until the rod is still; the blur narrows.
  - fail: The swings grow after the tap; or hold the same width for the whole clip; or the tip stops dead from a wide swing.
- P3 [major · material_response]
  - expect: The rod bends as a tapered springy pole: the tip flexes most, the handle end stays nearly straight, and the rod returns straight.
  - fail: The rod kinks and stays bent; or the handle end whips while the tip stays still; or the rod bends into a loop like a rope.
- P4 [major · causeless_motion]
  - expect: The post stays fixed and upright; only the rod moves.
  - fail: The post sways or leans at the tap; or the post's top whips like the rod; or the ground around the post ripples.
- P5 [fatal · permanence_count]
  - expect: One rod and one post; the rod stays one piece and passes through nothing.
  - fail: The rod passes through the post; or the tip breaks off; or a second rod appears; or the post vanishes.
- P6 [minor · attribute_drift]
  - expect: The rod's colour and its line guides, the post and the background stay the same.
  - fail: The rod changes colour; or the line guides move along the rod; or the post changes shape or colour; or the background changes.

## ACOU-0015 · struck_vibration · train

**Caption.** The taut mat of a trampoline is slapped with a hand, and the mat ripples outward and shivers before going flat.

**Expectation (hidden).** The ripples spread from the slap and the shiver fades within a second or two; the mat is flat before the slap.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A trampoline with its mat in view.
- S2 [core] A hand slaps the mat.
- S3 [core] The mat ripples outward from the slap and shivers.
- S4 [core] The mat goes flat again.
- S5 [minor] The mat is flat and taut before the slap.
- S6 [minor] The slap comes first; the rippling and then the flat mat follow.

**PC**
- P1 [core · causeless_motion]
  - expect: The mat lies flat and still until the palm lands; the ripple starts at the point of the slap and only then.
  - fail: The mat is already shivering before the hand arrives; or a ripple starts far from where the hand lands; or the hand slaps and the mat stays flat; or the mat shivers again after going flat with nothing touching it.
- P2 [core · process_direction]
  - expect: The ripples travel outward from the slap point toward the springs and the shiver fades to a flat mat.
  - fail: Ripples travel inward from the edge toward the slap point; or the shiver grows after the slap; or keeps the same strength for the whole clip; or the mat freezes rigid in a rippled shape.
- P3 [major · material_response]
  - expect: The mat behaves as a stretched fabric: it dips under the palm and springs back; the springs and frame stay rigid.
  - fail: The palm's dent stays after the hand lifts; or the mat tears; or the frame bends with the slap; or the mat sags like a loose sheet after springing back.
- P4 [major · causeless_motion]
  - expect: The frame and legs stay fixed on the ground; only the mat and springs move.
  - fail: The frame rocks or jumps at the slap; or a leg lifts off the ground; or the frame slides across the ground.
- P5 [fatal · solidity]
  - expect: One mat in one frame; the hand passes through nothing and the mat stays one sheet.
  - fail: The hand passes through the mat; or the mat splits or a hole opens; or the frame or springs vanish; or the trampoline changes into another object.
- P6 [minor · attribute_drift]
  - expect: The mat's colour, the spring cover and the surroundings stay the same.
  - fail: The mat changes colour; or the spring cover changes pattern; or the ground or background changes.

## ACOU-0016 · struck_vibration · train

**Caption.** A stretched washing line is plucked, and the line blurs along its length and slowly sharpens.

**Expectation (hidden).** The blur begins at the pluck and shrinks toward stillness; the clothes on the line sway slightly and settle.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A washing line stretched between two supports.
- S2 [core] The line is plucked.
- S3 [core] The line blurs along its length.
- S4 [core] The blur sharpens back to a line.
- S5 [minor] The line is taut before the pluck, not sagging loose.
- S6 [minor] The order is pluck, blur, sharpening.

**PC**
- P1 [core · causeless_motion]
  - expect: The line is a sharp, still line until the hand pulls it; the blur begins at the pluck and only then.
  - fail: The line is already blurred before the hand reaches it; or blurs while the hand is well away; or the hand pulls and releases and the line stays sharp; or the line sharpens and blurs again with nothing touching it.
- P2 [core · process_direction]
  - expect: The blur is widest right after the release and only narrows until the line is sharp.
  - fail: The blur widens again after it has begun to narrow; or holds the same width for the whole clip; or the line snaps from blur to sharp in one instant with no narrowing.
- P3 [major · material_response]
  - expect: The line vibrates between its two fixed ends: the blur is a band between the supports and both ends stay attached.
  - fail: The line comes loose from a support; or the blur is at the supports and absent in the middle; or the line stretches and hangs slack afterwards; or a support bends inward with the pluck.
- P4 [major · trajectory_momentum] (if: Clothes or pegs hang on the line.)
  - expect: Clothes and pegs on the line sway a little as the line vibrates, hanging down from it, and settle as the line stills.
  - fail: The clothes stay rigidly still while the line beside them blurs; or swing up above the line; or a peg slides along the line by itself; or the clothes swing in growing arcs.
- P5 [fatal · permanence_count]
  - expect: One line between the same supports; the line passes through nothing and nothing on it appears or vanishes.
  - fail: The line splits into two; or passes through the hand or a peg; or a support vanishes; or clothes appear on or vanish from the line.
- P6 [minor · attribute_drift]
  - expect: The line's colour, the supports and the garden or yard behind stay the same.
  - fail: The line changes colour; or a support changes shape or colour; or the ground or sky behind changes.

**Note.** The caption does not say the line carries washing; P4 is judged only when clothes or pegs are on it. 'Slowly' is not judged as a rate.

## ACOU-0017 · struck_vibration · train

**Caption.** A long steel saw blade is dropped flat onto a bench, and the blade twangs and flutters for a moment before lying still.

**Expectation (hidden).** The flutter starts at the impact and fades quickly; the blade does not keep quivering.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A long steel saw blade and a bench.
- S2 [core] The blade is dropped and lands on the bench.
- S3 [core] The blade flutters on landing.
- S4 [core] The blade lies still afterwards.
- S5 [minor] The blade lands flat, not on its edge or tip.
- S6 [minor] The order is landing, flutter, still.

**PC**
- P1 [core · causeless_motion]
  - expect: The blade falls as a stiff sheet and starts to flutter as it hits the bench and only then; once still it stays still.
  - fail: The blade flutters in mid-air before touching the bench; or lies on the bench and begins fluttering with nothing touching it; or hits the bench and lies dead still with no flutter at all; or starts fluttering again after lying still.
- P2 [core · process_direction]
  - expect: The flutter is strongest at the impact and dies away to stillness.
  - fail: The flutter grows after the impact; or continues unchanged to the end of the clip; or the blade stops dead in mid-flutter with one end raised.
- P3 [major · gravity_direction]
  - expect: The blade falls downward onto the bench and stays on the bench surface.
  - fail: The blade hovers before landing; or rises after landing; or a raised end stays lifted off the bench with nothing under it.
- P4 [major · material_response]
  - expect: The blade flexes as a springy steel strip: it bows and rings flat again; the bench stays rigid.
  - fail: The blade folds and stays bent; or bends like rubber into a deep curve; or the bench top dents or ripples where it lands; or the teeth bend over.
- P5 [fatal · permanence_count]
  - expect: One blade and one bench; the blade passes through nothing and stays one piece.
  - fail: The blade passes into the bench; or splits in two; or vanishes; or a second blade appears.
- P6 [minor · attribute_drift]
  - expect: The blade's teeth, the bench and anything lying on it stay the same.
  - fail: The blade's teeth change pattern; or the bench changes colour; or tools on the bench move by themselves.

**Note.** The twang is inaudible and is not judged; the flutter is its visible sign.

## ACOU-0018 · struck_vibration · train

**Caption.** The top of a large empty cardboard box is thumped, and the lid panel bounces and quivers before settling.

**Expectation (hidden).** The panel moves at the thump and the quiver fades within a second; the box's sides barely move.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A large cardboard box with its lid panel on top.
- S2 [core] The top of the box is thumped by a hand or fist.
- S3 [core] The lid panel bounces and quivers.
- S4 [core] The lid settles.
- S5 [minor] The thump lands on the top of the box, not on a side.
- S6 [minor] The thump comes first; the bounce and quiver follow, then the settling.

**PC**
- P1 [core · causeless_motion]
  - expect: The lid panel is still until the hand lands; it dips and rebounds at the thump and only then.
  - fail: The panel is already quivering before the hand arrives; or quivers while the hand is held away from it; or the hand thumps and the panel stays rigid; or the panel starts quivering again after settling with nothing touching it.
- P2 [core · process_direction]
  - expect: The first dip is the deepest and each later flex is smaller until the panel lies flat and still.
  - fail: The quiver grows after the thump; or holds the same size for the whole clip; or the panel stops dead in mid-bounce.
- P3 [major · material_response]
  - expect: The lid flexes as stiff card: it dents in under the hand and springs back; the side walls stay upright.
  - fail: The hand's dent stays pressed in after the hand lifts; or the panel ripples like cloth; or a side wall caves in and stays; or the lid tears.
- P4 [major · causeless_motion]
  - expect: The box stays where it is; the sides barely move and the box does not slide or rock.
  - fail: The box slides across the floor at the thump; or rocks up onto one edge; or the sides bulge and quiver while the lid stays still.
- P5 [fatal · solidity]
  - expect: One box; the hand passes through nothing and the box stays one piece.
  - fail: The hand passes into the lid; or the lid vanishes or a second lid appears; or the box collapses flat and re-forms; or the box changes into another object.
- P6 [minor · attribute_drift]
  - expect: The box's printing and tape, and the floor and surroundings stay the same.
  - fail: The box's label or printing changes; or the tape moves or vanishes; or the floor changes.

**Note.** 'Empty' cannot be seen through a closed lid and is not judged.

## ACOU-0019 · struck_vibration · train

**Caption.** A metal spring doorstop mounted on the wall is flicked, and it wobbles wildly and then slows to a stop.

**Expectation (hidden).** The wobble is largest right after the flick and shrinks steadily; the base on the wall does not move.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A spring doorstop mounted on a wall.
- S2 [core] The doorstop is flicked.
- S3 [core] It wobbles.
- S4 [core] It slows to a stop.
- S5 [minor] The base stays fixed to the wall.
- S6 [minor] The order is flick, wobble, stop.

**PC**
- P1 [core · causeless_motion]
  - expect: The spring stands still until the finger reaches it; it wobbles from the flick and only then.
  - fail: The spring is already swaying before the finger arrives; or wobbles while the finger is well away; or the finger flicks it and the spring stays rigid; or it stops and begins wobbling again with nothing touching it.
- P2 [core · process_direction]
  - expect: The wobble is widest right after the flick and shrinks steadily until the spring stands still.
  - fail: The swings grow after the flick; or hold the same width for the whole clip; or the spring stops dead from a wide swing.
- P3 [major · material_response]
  - expect: The spring bends and whips as a coil anchored at its base, the rubber tip riding on the free end; the coil straightens as it settles.
  - fail: The coil kinks and stays bent; or the spring stretches out longer and stays stretched; or the coil goes straight and rigid in mid-swing; or the coils separate into loose rings.
- P4 [major · causeless_motion]
  - expect: The base plate stays fixed to the wall; the wall around it does not move.
  - fail: The base plate lifts or rotates on the wall; or the wall ripples at the flick; or the wall around the base bulges.
- P5 [fatal · permanence_count]
  - expect: One doorstop with its base, spring and tip; the spring passes through nothing.
  - fail: The tip flies off and the spring is then whole again; or the spring passes into the wall or floor; or a second doorstop appears; or the doorstop vanishes.
- P6 [minor · attribute_drift]
  - expect: The doorstop's finish, the wall colour and the floor stay the same.
  - fail: The spring changes colour; or the tip changes colour or size; or the wall or floor changes.

**Note.** 'Wildly' is not judged as a magnitude; only the wobble's start and decay are.

## ACOU-0020 · struck_vibration · train

**Caption.** Small paper riders sit on the strings of an acoustic guitar; the body of the guitar is tapped with a palm and the riders jump.

**Expectation (hidden).** The riders lie still until the tap, hop or fall off at the tap, and do not move again once the strings are quiet; the strings are not plucked.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] An acoustic guitar with small paper riders resting on its strings.
- S2 [core] A palm taps the body of the guitar.
- S3 [core] The riders jump.
- S4 [minor] The tap is on the body; the strings are not plucked.
- S5 [minor] The riders are small scraps of paper sitting on the strings.
- S6 [minor] The tap comes first and the jump follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The riders sit still until the palm lands on the body; they hop at the tap and only then.
  - fail: Riders hop or slide before the palm reaches the body; or jump while the hand is well away; or the palm lands and every rider stays put; or the riders hop again after settling with nothing touching the guitar.
- P2 [core · process_direction]
  - expect: The hop is largest at the tap; the riders then come to rest on the strings, the soundboard or the floor and stay there.
  - fail: The riders keep hopping at the same height for the whole clip after one tap; or hop higher with each bounce; or a fallen rider climbs back onto its string.
- P3 [major · gravity_direction]
  - expect: Riders that leave their string fall onto the soundboard, the strings below or the floor.
  - fail: A rider hangs in the air above the strings; or drifts upward away from the guitar; or a fallen rider lifts off the soundboard by itself.
- P4 [major · material_response]
  - expect: The guitar body is rigid under the palm; the strings stay taut at nut and bridge and shiver in place rather than swinging.
  - fail: The soundboard dents in under the palm and stays dented; or the strings sag and swing like slack ropes; or the neck bends with the tap; or a string comes off the bridge.
- P5 [fatal · permanence_count]
  - expect: The riders keep their number, allowing for some falling out of view; the guitar keeps its strings and shape; nothing passes through anything.
  - fail: Riders appear on the strings after the tap; or all the riders vanish at once; or the palm passes into the soundboard; or strings appear or vanish.
- P6 [minor · attribute_drift]
  - expect: The guitar's finish, the fret markers and the riders' colour stay the same.
  - fail: The guitar changes colour; or the fret markers shift; or a rider changes colour or size while at rest.

## ACOU-0021 · struck_vibration · train

**Caption.** The taut head of a large bass drum is slapped, and the head visibly dips and rebounds several times, each time smaller.

**Expectation (hidden).** The first dip is deepest, each rebound is smaller, and the head is flat within a couple of seconds.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A large bass drum with its head in view.
- S2 [core] The head is slapped.
- S3 [core] The head dips and rebounds more than once.
- S4 [minor] Each dip and rebound is smaller than the one before.
- S5 [minor] The strike is a slap with a hand, not a stick or mallet.
- S6 [minor] The slap comes first and the dips follow.

**PC**
- P1 [core · causeless_motion]
  - expect: The head is flat and still until the hand lands; the first dip happens at the slap and only then.
  - fail: The head is already trembling before the hand arrives; or dips while the hand is well away; or the hand lands and the head stays flat; or the head starts dipping again after lying flat with nothing touching it.
- P2 [core · process_direction]
  - expect: The head dips inward under the slap first; the first dip is the deepest and each rebound smaller, until the head lies flat.
  - fail: A later dip is deeper than the first; or the dips stay the same depth for the whole clip; or the head stops dead while bowed in or out; or the head bulges outward toward the hand before dipping in.
- P3 [major · material_response]
  - expect: The head flexes as a stretched skin, dipping under the palm and springing back; the hoop and shell stay rigid.
  - fail: The hand's print stays pressed into the head after the hand lifts; or the head sags loose like cloth; or the shell dents or wobbles like rubber; or the head splits.
- P4 [major · causeless_motion]
  - expect: The drum stays put on its stand or the floor; the shell, hoop and stand do not shift with the slap.
  - fail: The drum rolls or slides at the slap; or the stand rocks and keeps rocking; or the hoop turns on the shell.
- P5 [fatal · solidity]
  - expect: One drum with one head; the hand passes through nothing and the drum stays one object.
  - fail: The hand passes through the head; or a second head or drum appears; or the drum vanishes or changes into another object; or the hoop separates from the shell.
- P6 [minor · attribute_drift]
  - expect: The head's colour and any logo on it, the shell's finish and the surroundings stay the same.
  - fail: The logo on the head changes or moves; or the shell changes colour; or the background changes.

**Note.** Separate dips may not be resolvable in the frames; a shiver that starts at the slap and fades counts as the dips and rebounds for S3 and P2.

## ACOU-0022 · struck_vibration · train

**Caption.** The wire of a garden fence is plucked, and the wire blurs and hums along its span before settling.

**Expectation (hidden).** The blur is greatest at the plucked point and fades along the wire; it stops when the wire is gripped.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A garden fence with a wire strand.
- S2 [core] The wire is plucked.
- S3 [core] The wire blurs along its span.
- S4 [core] The wire settles to a sharp line.
- S5 [minor] One wire is plucked; the other strands are left alone.
- S6 [minor] The order is pluck, blur, settle.

**PC**
- P1 [core · causeless_motion]
  - expect: The wire is sharp and still until the fingers pull it; the blur begins at the pluck and only then; the other wires stay sharp.
  - fail: The wire is already blurred before the hand reaches it; or blurs while the hand is well away; or the hand plucks and the wire stays a sharp line; or a different wire blurs from the one plucked.
- P2 [core · process_direction]
  - expect: The blur is widest right after the release and narrows steadily until the wire is sharp; it does not widen again.
  - fail: The blur widens after it has begun to narrow; or holds the same width for the whole clip; or the wire goes sharp and blurs again with nothing touching it.
- P3 [major · material_response]
  - expect: The wire vibrates between its fixed posts: the blur lies between the posts, widest around the plucked point, and the wire stays attached.
  - fail: The wire pulls free of a post; or the blur is at the posts and absent at the plucked point; or the wire sags into a loop and hangs slack; or a post leans with the pluck.
- P4 [major · missing_consequence] (if: A hand grips the wire while it is still blurred.)
  - expect: When a hand closes on the vibrating wire the blur stops at once and the whole wire is sharp.
  - fail: The wire keeps blurring through and beyond the gripping hand; or the span stays blurred for the rest of the clip while the hand holds it; or the wire starts blurring again after the hand lets go with no new pluck.
- P5 [fatal · permanence_count]
  - expect: The fence keeps its wires and posts; the plucked wire stays one strand and passes through nothing.
  - fail: Wires appear or vanish; or the wire passes through the hand or a post; or the wire splits into two strands; or a post vanishes.
- P6 [minor · attribute_drift]
  - expect: The wire's colour, the posts and the garden behind stay the same.
  - fail: The wire changes colour; or the posts change spacing between frames; or the plants behind change.

**Note.** The hum is inaudible and is not judged. The caption does not say the wire is gripped; P4 applies only if a hand is seen closing on it.

## ACOU-0023 · struck_vibration · train

**Caption.** Salt is sprinkled on the bars of a marimba; a mallet runs across the bars and the salt jumps off each bar in turn.

**Expectation (hidden).** Salt leaves each bar only as that bar is struck, in the order the mallet travels; bars not yet struck keep their salt still.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A marimba with salt on its bars.
- S2 [core] A mallet runs across the bars in a sweep.
- S3 [core] The salt jumps off the bars.
- S4 [minor] The salt is sprinkled: grains are scattered over several bars, not heaped on one.
- S5 [minor] The mallet sweeps across several bars rather than striking a single one.
- S6 [minor] The salt leaves each bar as the mallet reaches it, in the order the mallet travels.

**PC**
- P1 [core · causeless_motion]
  - expect: Salt on each bar lies still until the mallet reaches that bar and jumps only as that bar is struck; bars ahead of the mallet keep their salt still.
  - fail: Salt jumps off bars the mallet has not yet reached; or all the bars' salt jumps at once at the first stroke; or the mallet passes over a bar and its salt stays put; or salt jumps while the mallet is held clear of the bars.
- P2 [core · process_direction]
  - expect: The salt leaves the bars in the order the mallet travels and does not return; grains that have left a bar settle in the gaps, on the frame or on the floor.
  - fail: Salt leaves the bars in the opposite order to the mallet's travel; or grains settle back onto the bar they left; or salt goes on hopping on every bar for the whole clip after the sweep.
- P3 [major · gravity_direction]
  - expect: Grains that jump fall back down into the gaps, onto the frame or onto the floor.
  - fail: Grains hang in the air above the bars; or drift upward; or grains that fell between bars rise back onto a bar.
- P4 [major · material_response]
  - expect: The bars are rigid slabs: the mallet skips across them and each bar stays in its cradle.
  - fail: The mallet sinks into a bar; or bars bend under the sweep; or a bar lifts out of its cradle and stays up.
- P5 [fatal · permanence_count]
  - expect: The bars keep their count and order; the mallet passes through nothing; salt only leaves the bars and never appears anew.
  - fail: Bars change count or merge; or the mallet passes through a bar; or salt appears on a bar after the mallet has cleared it; or the mallet duplicates.
- P6 [minor · attribute_drift]
  - expect: The bars' colours and lettering, the frame and resonators, and the mallet head stay the same.
  - fail: A bar changes colour; or the lettering changes; or the frame or resonators change; or the mallet head changes colour.

**Note.** The sprinkling may happen before the clip; S4 is decided on how the salt lies on the bars. The speed of the sweep is not judged.

## ACOU-0024 · struck_vibration · train

**Caption.** The thin elastic cord of a paddle ball toy is plucked, and the cord blurs and the ball bounces lightly before both go still.

**Expectation (hidden).** The blur and bounce begin at the pluck and decay within a couple of seconds.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A paddle ball toy: a paddle, an elastic cord and a ball joined to it.
- S2 [core] The cord is plucked.
- S3 [core] The cord blurs.
- S4 [core] The ball bounces and then both cord and ball go still.
- S5 [minor] The bounce is light: small bobs on the cord, not a wild swing.
- S6 [minor] The pluck comes first; the blur and bounce follow, then stillness.

**PC**
- P1 [core · causeless_motion]
  - expect: The cord and the ball are at rest until the fingers pluck the cord; the blur and the ball's bobbing begin at the pluck and only then.
  - fail: The ball is already bobbing before the hand reaches the cord; or the cord blurs while the hand is well away; or the cord is plucked and neither cord nor ball moves; or the ball starts bobbing again after both have gone still with nothing touching them.
- P2 [core · process_direction]
  - expect: The cord's blur narrows and the ball's bobs shrink steadily until both are still.
  - fail: The ball's bobs grow after the pluck; or the ball keeps bobbing at the same height for the whole clip; or the ball stops dead in mid-bob.
- P3 [major · material_response]
  - expect: The cord stretches and recoils as elastic, staying joined to paddle and ball; the ball stays a round rubber ball.
  - fail: The cord goes rigid like a rod; or stretches out and hangs long and slack afterwards; or the ball squashes flat and stays flat.
- P4 [major · gravity_direction]
  - expect: The ball hangs down from the cord or rests on the surface beneath it; each bob returns it to the same rest position.
  - fail: The ball hovers with the cord slack beneath it; or rises and stays up; or comes to rest at a different height or place from where it started while the paddle has not moved.
- P5 [fatal · permanence_count]
  - expect: One paddle, one cord and one ball, joined throughout; nothing passes through anything.
  - fail: The ball detaches from the cord; or a second ball appears; or the cord passes through the paddle or the ball; or the toy vanishes.
- P6 [minor · attribute_drift]
  - expect: The paddle's colour and print, the ball's colour and the surroundings stay the same.
  - fail: The paddle's print changes; or the ball changes colour or size; or the background changes.

**Note.** The caption does not say whether the paddle is held up or lying down; P4 reads the ball's rest position from the clip.

## ACOU-0025 · struck_vibration · train

**Caption.** A strip of thin sheet metal clamped at one end in a vise is flicked, and the free end vibrates in a blur that slowly stops.

**Expectation (hidden).** The free end blurs widest at the tip right after the flick and narrows to stillness; the clamped end does not move.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A strip of thin sheet metal clamped at one end in a vise.
- S2 [core] The free end is flicked.
- S3 [core] The free end vibrates in a blur.
- S4 [core] The blur stops and the strip is still.
- S5 [minor] The clamped end stays gripped in the jaws.
- S6 [minor] The order is flick, blur, still.

**PC**
- P1 [core · causeless_motion]
  - expect: The strip stands still until the finger reaches it; it blurs from the flick and only then.
  - fail: The strip is already blurred before the finger arrives; or blurs while the finger is well away; or the finger flicks it and the strip stays sharp; or the strip goes still and blurs again with nothing touching it.
- P2 [core · process_direction]
  - expect: The blur is widest right after the flick and narrows steadily until the strip is a sharp, still line.
  - fail: The blur widens again after it has begun to narrow; or keeps the same width for the whole clip; or the strip snaps from a wide blur to still in a single instant.
- P3 [major · material_response]
  - expect: The strip flexes as a springy sheet from the jaws: the blur is widest at the tip and absent at the clamp, and the strip returns straight.
  - fail: The strip kinks and stays bent; or the blur is widest at the jaws while the tip is sharp; or the strip curls over like paper; or the strip stretches longer.
- P4 [major · causeless_motion]
  - expect: The clamp and the bench stay fixed; only the strip moves.
  - fail: The jaws open or shift with the flick; or the clamp slides along the bench; or the bench top shakes.
- P5 [fatal · permanence_count]
  - expect: One strip in one clamp; the strip stays one piece and passes through nothing.
  - fail: The strip passes through the jaws or the bench; or splits in two; or a second strip appears; or the strip vanishes.
- P6 [minor · attribute_drift]
  - expect: The strip's sheen, the clamp's colour and the bench stay the same.
  - fail: The strip changes colour; or the clamp changes colour or shape; or tools on the bench move by themselves.

**Note.** 'Slowly' is not judged as a rate; only that the blur narrows and does not widen.

## ACOU-0026 · struck_vibration · train

**Caption.** The taut skin of a tambourine is struck, and the skin shivers and the metal jingles rattle before quieting.

**Expectation (hidden).** The skin shiver and the jingle rattle both begin at the strike and fade together within a second or two.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A tambourine with a skin and metal jingles.
- S2 [core] The skin is struck.
- S3 [core] The skin shivers and the jingles rattle.
- S4 [core] The tambourine quiets: skin and jingles are still.
- S5 [minor] The strike lands on the skin, not on the rim.
- S6 [minor] The strike comes first; the shiver and rattle follow, then the quiet.

**PC**
- P1 [core · causeless_motion]
  - expect: The skin is still and the jingles hang at rest until the hand lands on the skin; both begin moving at the strike and only then.
  - fail: The jingles are already rattling before the hand reaches the skin; or the skin trembles while the hand is well away; or the hand strikes and neither skin nor jingles move; or the jingles start rattling again after quieting while the tambourine is held still and nothing strikes it.
- P2 [core · process_direction]
  - expect: The skin's shiver and the jingles' rattle are strongest right after the strike and fade together until both are still.
  - fail: The rattle grows after the strike; or the jingles keep rattling unchanged for the whole clip; or the jingles stop dead in mid-rattle.
- P3 [major · material_response]
  - expect: The skin flexes as a stretched membrane and springs back flat; the frame stays rigid and the jingles stay on their pins.
  - fail: The hand's print stays pressed into the skin; or the frame bends or wobbles like rubber; or a jingle bends or folds; or the skin sags loose.
- P4 [major · trajectory_momentum]
  - expect: The jingles move only within their slots, pivoting on their pins, and settle hanging or lying in place.
  - fail: A jingle slides along the frame to another slot; or spins free of its pin while staying in the frame; or a jingle stays frozen while its partner on the same pin rattles.
- P5 [fatal · permanence_count]
  - expect: One tambourine with its skin, frame and the same jingles; the hand passes through nothing.
  - fail: The hand passes through the skin; or jingles appear or vanish from the frame; or the skin vanishes leaving an open ring; or the tambourine changes into another object.
- P6 [minor · attribute_drift]
  - expect: The skin's colour, the frame's finish and the jingles' shine stay the same.
  - fail: The skin changes colour or gains a pattern; or the frame changes colour; or the jingles change colour or size.

**Note.** The tambourine may be held; small movements of the holding hand are not judged as strikes. Sound is not judged.

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

## ACOU-0030 · sound_driven_vibration · train

**Caption.** Thunder rolls over a house, and a strip of paper taped to a loose window pane quivers with each rumble.

**Expectation (hidden).** The strip flutters only during the rumbles and hangs still between them; it does not flutter before the thunder or keep fluttering afterwards.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A window pane with a strip of paper taped to it.
- S2 [core] The strip quivers.
- S3 [minor] The quivering comes in bouts with still spells between them, as with separate rumbles.
- S4 [minor] The setting is a house: the window belongs to a room or a house wall.

**PC**
- P1 [core · causeless_motion]
  - expect: The strip's free part trembles while its taped end stays fixed to the glass; between bouts it hangs still against the pane.
  - fail: The taped end slides across the glass; or the strip drifts away from the pane and floats as if in a breeze; or it swings in slow wide arcs rather than trembling; or it rises up the pane and stays lifted.
- P2 [core · missing_consequence] (if: Another light loose object hangs at or near the window.)
  - expect: Other light loose things at the window stir at the same moments as the strip and hang still with it between bouts.
  - fail: A curtain edge, blind cord or second strip hangs dead still while the strip quivers hard; or it flutters while the strip is still; or the two move in bouts that never overlap.
- P3 [major · material_response]
  - expect: The strip bends as thin paper: its free end curls and flaps while the taped end holds.
  - fail: The strip stays flat and rigid like a board while shifting; or stretches longer or shorter; or the tape lets go and the strip stays stuck to the glass with nothing holding it.
- P4 [major · gravity_direction]
  - expect: When still, the strip rests against or hangs from the glass under its tape; any untaped part hangs downward.
  - fail: The untaped part points upward or stands out from the glass while still; or the strip floats upward; or it settles higher on the pane after each bout.
- P5 [fatal · permanence_count]
  - expect: One strip on one pane; nothing passes through the glass.
  - fail: A second strip appears; or the strip vanishes; or the strip passes through the glass; or the pane changes shape.
- P6 [minor · attribute_drift]
  - expect: The strip's colour and length, the tape and the window frame stay the same.
  - fail: The strip changes colour or length; or the tape moves to a new spot; or the window frame changes.

**Note.** Thunder cannot be seen and lightning need not be in view; the strip's motion is judged on its own shape. A clip with bouts of quivering and no visible storm passes P1.

## ACOU-0031 · sound_driven_vibration · train

**Caption.** A washing machine spins up to full speed, and the bottle of detergent standing on top of it shakes and creeps toward the edge.

**Expectation (hidden).** The shaking begins as the machine spins up, the bottle inches along in small jumps, and it stops moving when the spin cycle ends.

**Declared violation types.** causeless_motion, trajectory_momentum

**SA**
- S1 [core] A washing machine with a bottle of detergent standing on top of it.
- S2 [core] The machine spins up: the drum turns faster or the machine begins to shake.
- S3 [core] The bottle shakes.
- S4 [core] The bottle creeps toward the edge of the machine.
- S5 [minor] The bottle stays upright while it creeps.
- S6 [minor] The machine starts first; the shaking and creeping follow.

**PC**
- P1 [core · causeless_motion]
  - expect: The bottle is still while the machine is still and shakes only once the machine runs; if the machine stops the bottle stops.
  - fail: The bottle shakes or moves before the machine starts; or slides while the machine top shows no tremble at all; or keeps creeping after the machine has plainly stopped.
- P2 [core · trajectory_momentum]
  - expect: The creep is a series of small hops or shuffles in a roughly steady direction toward the edge, with the bottle flat on its base.
  - fail: The bottle glides in one smooth slide as if pushed; or reverses and travels back to the centre; or leaps a large gap in one bound; or moves as a whole while its base is seen to stay in one place.
- P3 [major · gravity_direction]
  - expect: The bottle stays down on the lid; if it reaches the edge it tips and falls off.
  - fail: The bottle hovers above the lid; or hangs over the edge well past its middle without tipping; or floats off sideways instead of falling.
- P4 [major · material_response]
  - expect: The bottle and the machine stay rigid; the machine shakes as one body.
  - fail: The bottle wobbles like jelly; or the lid ripples; or the machine's body bends.
- P5 [fatal · permanence_count]
  - expect: One bottle, one machine; nothing passes through the lid.
  - fail: A second bottle appears; or the bottle vanishes; or it sinks into the lid; or the machine turns into another object.
- P6 [minor · attribute_drift]
  - expect: The bottle's label and colour, the machine's dials and door and the room stay the same.
  - fail: The label changes; or the bottle changes colour or size; or the dials or door change.

## ACOU-0032 · sound_driven_vibration · train

**Caption.** A marching band's bass drum passes close to a shop window, and a paper sign taped to the inside of the glass quivers with each beat.

**Expectation (hidden).** The sign twitches in time with the drum beats and is still between them and after the band has passed; it does not move before the drum sounds.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A paper sign taped to the inside of a shop window.
- S2 [core] A marching band with a bass drum passes outside the window.
- S3 [core] The sign quivers.
- S4 [minor] The quivering comes in twitches rather than one steady flutter.
- S5 [minor] The sign is still before the drum arrives and after the band has gone.

**PC**
- P1 [core · missing_consequence] (if: The drummer and the beater are in view.)
  - expect: Each visible beat of the drum is followed by a twitch of the sign.
  - fail: The beater strikes repeatedly and the sign never moves; or the sign twitches at moments when the beater is held away; or the sign shakes hardest after the drum has gone and is still while the drum is beside the window.
- P2 [core · causeless_motion]
  - expect: The sign's motion is a tremble at its loose edges with its taped points fixed; with no band outside it hangs still.
  - fail: The sign flaps while the street is empty and stays still as the band passes; or the taped corners slide across the glass; or the sign floats away from the glass; or it swings in slow wide arcs like a curtain.
- P3 [major · material_response]
  - expect: The sign bends as paper: its loose edges curl and flap.
  - fail: The sign stays rigid like a board while shifting; or stretches or shrinks; or tears with nothing touching it.
- P4 [major · gravity_direction]
  - expect: Loose corners hang downward and settle back after each twitch.
  - fail: A loose corner rises and stays up; or the sign lifts up the glass; or it drifts upward.
- P5 [fatal · permanence_count]
  - expect: One sign; the band and its drum keep their count; nothing passes through the glass.
  - fail: A second sign appears; or the sign vanishes; or the drum passes through the glass; or band members merge or vanish.
- P6 [minor · attribute_drift]
  - expect: The sign's lettering and colour and the goods in the window stay the same.
  - fail: The sign's lettering changes; or its colour changes; or goods in the window change shape or colour.

**Note.** The band members are the source of the beats; their marching is not judged.

## ACOU-0033 · sound_driven_vibration · train

**Caption.** A subway train roars through a station, and a hanging sign on the platform trembles on its chains.

**Expectation (hidden).** The trembling starts with the train's arrival, is strongest as it passes, and fades after it leaves.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A subway platform with a sign hanging on chains.
- S2 [core] A train passes through the station.
- S3 [core] The sign trembles on its chains.
- S4 [minor] The train passes through without stopping.
- S5 [minor] The sign is not already trembling before the train appears.

**PC**
- P1 [core · causeless_motion] (if: The train is in view at some point.)
  - expect: The sign hangs still while the platform is quiet and begins to tremble as the train enters.
  - fail: The sign trembles while the train is not yet in view and the platform is quiet; or the train passes and the sign hangs dead still; or the trembling starts only after the train has fully left.
- P2 [core · process_direction]
  - expect: The trembling builds, peaks and dies away in one arc: after its strongest point it only weakens until the sign hangs still.
  - fail: The trembling weakens and then strengthens again with no train in view; or stops dead in a tilted pose with the chains slack; or the sign is trembling in one frame and hanging still in the next.
- P3 [major · gravity_direction]
  - expect: The chains stay taut with the sign hanging below its fixing points; the tremble is a small swing about the hanging point.
  - fail: The chains go slack while the sign stays up; or the sign rises toward the ceiling; or it hangs sideways from a taut chain.
- P4 [major · material_response]
  - expect: The sign panel is rigid and the chains flex only at their links.
  - fail: The sign panel bends or ripples; or the chains stretch; or the chains pass through the sign.
- P5 [fatal · permanence_count]
  - expect: One sign on its chains; the train's carriages keep their count; nothing passes through a pillar or the platform.
  - fail: A second sign appears; or the sign vanishes; or the train passes through a pillar or the platform edge; or carriages appear or vanish mid-train.
- P6 [minor · attribute_drift]
  - expect: The sign's lettering, the platform tiles and posters stay the same.
  - fail: The sign's lettering changes; or the tiles or posters change; or the chains change length.

## ACOU-0034 · sound_driven_vibration · train

**Caption.** A speaker on a table plays a loud bass track, and a handful of grains of rice scattered on the table jump and dance around it.

**Expectation (hidden).** The grains hop in time with the beats, most strongly nearest the speaker, and lie still when the track stops.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A speaker stands on a table.
- S2 [core] Grains of rice are scattered on the table around the speaker.
- S3 [core] The grains jump and move about.
- S4 [minor] The grains are a loose handful, not a heap.
- S5 [minor] The grains move near the speaker, around it rather than far away.

**PC**
- P1 [core · causeless_motion]
  - expect: The grains hop in place in bursts; they do not slide as a body or stream in one direction.
  - fail: All the grains slide together in one direction as if the table were tilted; or grains travel in a stream toward the speaker and climb its side; or grains rise and hang above the table.
- P2 [core · missing_consequence] (if: The speaker's cone is in view.)
  - expect: The grains hop when the cone pumps and lie still when it is still; those nearest the speaker hop most.
  - fail: The cone pumps for a spell and the grains lie dead still; or the grains hop while the cone is plainly still; or grains far from the speaker hop while those touching it lie still.
- P3 [major · gravity_direction]
  - expect: Grains fall back to the table after each hop.
  - fail: Grains hang in the air; or float upward; or stick to the side of the speaker cabinet above the table.
- P4 [major · material_response]
  - expect: The grains stay separate hard grains and the table stays rigid.
  - fail: Grains merge into a lump; or flow like a liquid puddle; or the table top ripples like water.
- P5 [fatal · permanence_count]
  - expect: The grains keep their number, allowing for some falling off the table; one speaker; nothing passes through the table.
  - fail: Grains appear from nowhere; or all the grains vanish at once; or the speaker duplicates; or grains sink into the table top.
- P6 [minor · attribute_drift]
  - expect: The speaker's colour and logo, the table surface and the grains' colour stay the same.
  - fail: The speaker changes colour or shape; or the table pattern changes; or the grains change colour.

## ACOU-0035 · sound_driven_vibration · train

**Caption.** A jackhammer starts up on a street, and the coffee in cups on a café terrace table shows rings of tiny ripples.

**Expectation (hidden).** The ripples appear when the hammer runs and vanish when it pauses; cups farther away ripple less.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A café terrace table with cups of coffee on it.
- S2 [core] A jackhammer on the street starts up: its bit begins to pound.
- S3 [core] The coffee surfaces show rings of ripples.
- S4 [minor] The ripples are fine rings, not sloshing waves.
- S5 [minor] The jackhammer starts first and the ripples follow.

**PC**
- P1 [core · missing_consequence] (if: The jackhammer is in view.)
  - expect: Ripples appear while the hammer pounds and vanish when it pauses.
  - fail: The hammer pounds and the coffee stays glassy; or the coffee ripples while the hammer is lifted and still; or the ripples begin before the hammer starts.
- P2 [core · causeless_motion]
  - expect: The ripples are a fine trembling of the surface in place; the coffee stays level in its cup.
  - fail: The coffee sloshes up one side of the cup as if pushed; or spills over with the cup standing still; or swirls round as if stirred; or a single ring spreads outward from one point with nothing dropped in.
- P3 [major · gravity_direction]
  - expect: The coffee stays in the cups with a level surface and the cups stay on the table.
  - fail: Coffee rises out of a cup; or the surface tilts and stays tilted; or a cup lifts off the table.
- P4 [major · material_response]
  - expect: The cups and table stay rigid and the coffee stays a liquid.
  - fail: The cups wobble like rubber; or the table top ripples like water; or the coffee surface cracks like a skin.
- P5 [fatal · permanence_count]
  - expect: The cups keep their count; one hammer; nothing passes through the table or the pavement.
  - fail: Cups appear or vanish; or a cup sinks into the table; or the hammer bit passes through the pavement without breaking it; or the coffee vanishes.
- P6 [minor · attribute_drift]
  - expect: The cups' patterns, the coffee's colour and the chairs stay the same.
  - fail: Cup patterns change; or the coffee changes colour; or the chairs change shape.

**Note.** The worker holding the jackhammer is a trigger and is not judged.

## ACOU-0036 · sound_driven_vibration · train

**Caption.** A car with a booming stereo pulls up at a light, and the fuzzy dice hanging from its rear-view mirror jiggle with the bass.

**Expectation (hidden).** The dice twitch in time with the beats and hang still when the music is turned down; they do not swing on their own.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] Fuzzy dice hang from a car's rear-view mirror.
- S2 [core] The car pulls up and stops at a traffic light.
- S3 [core] The dice jiggle.
- S4 [minor] The jiggle is a rapid twitch rather than a slow pendulum swing.
- S5 [minor] The dice are still jiggling after the car has stopped.

**PC**
- P1 [core · causeless_motion]
  - expect: The dice hang from their string and twitch about the hanging point with the string taut above them.
  - fail: The dice rise with the string going slack; or move sideways as a pair while the string above them stays perfectly still and straight; or float away from the mirror.
- P2 [core · missing_consequence] (if: Another loose light object hangs or lies in the cabin.)
  - expect: Other loose light things in the cabin twitch at the same moments as the dice.
  - fail: An air freshener, charm or paper hangs dead still while the dice twitch hard; or it twitches while the dice hang still; or the two move at different moments.
- P3 [major · trajectory_momentum] (if: The car's slowing is visible through the windows.)
  - expect: As the car slows, the dice swing toward the windscreen and then back.
  - fail: The dice swing toward the rear as the car brakes; or stay rigidly vertical as the scene outside comes to a halt; or swing sideways only.
- P4 [major · gravity_direction]
  - expect: The dice hang below the mirror on their string and return to hanging straight down after each swing.
  - fail: The dice rest tilted off vertical with a taut string and nothing touching them; or rise above the mirror; or the string arcs upward.
- P5 [fatal · permanence_count]
  - expect: The dice keep their number; one mirror; nothing passes through the windscreen.
  - fail: An extra die appears; or a die vanishes; or the dice pass through the windscreen or mirror; or the dice merge into one.
- P6 [minor · attribute_drift]
  - expect: The dice's colour and pips, the mirror and the dashboard stay the same.
  - fail: The dice change colour or their pips change; or the mirror moves on its own; or the dashboard changes.

**Note.** The car and the stereo are self-driven; the dice swinging forward as the car brakes is inertia, not a violation.

## ACOU-0037 · sound_driven_vibration · train

**Caption.** A loud table saw in a workshop is switched on, and the screws in a jar on the bench begin to rattle and shift.

**Expectation (hidden).** The rattling begins when the saw starts and stops when it is switched off; the screws settle in a slightly different arrangement.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A workshop bench with a table saw and a jar of screws.
- S2 [core] The saw is switched on: the blade starts to spin or a switch is thrown.
- S3 [core] The screws in the jar rattle and shift.
- S4 [minor] The screws stay inside the jar.
- S5 [minor] The saw starts first and the screws move after.

**PC**
- P1 [core · causeless_motion]
  - expect: The screws are still before the saw runs, shift only while the blade turns and stop when it stops.
  - fail: Screws move before the switch is thrown or the blade turns; or keep rattling after the blade has stopped; or the jar slides while the screws inside stay frozen in place.
- P2 [core · missing_consequence]
  - expect: The rattling rearranges the screws: they settle a little differently and do not spring back to the old arrangement.
  - fail: The blade runs, the jar visibly shakes and the screws hold their exact pattern; or the screws return to their old arrangement after the saw stops; or screws climb the jar wall and stay pressed to it above the heap.
- P3 [major · gravity_direction]
  - expect: Screws that hop fall back down; the heap stays at the bottom of the jar.
  - fail: Screws hang in the air inside the jar; or the heap floats up; or screws stick to the lid.
- P4 [major · material_response]
  - expect: The jar is rigid glass, the screws rigid metal and the bench rigid.
  - fail: The jar bulges; or screws bend; or the jar's wall flexes like film; or the bench top ripples.
- P5 [fatal · permanence_count]
  - expect: One jar with a steady count of screws; one saw; nothing passes through the glass or the table.
  - fail: Screws appear outside the jar; or the jar duplicates or vanishes; or screws pass through the glass; or the blade passes through the table.
- P6 [minor · attribute_drift]
  - expect: The jar's label and shape, the saw's colour and the wall behind stay the same.
  - fail: The jar changes shape or label; or the saw changes colour; or the wall behind changes.

## ACOU-0038 · sound_driven_vibration · train

**Caption.** A low-flying jet passes over a house, and a hanging light fitting in the hallway swings gently.

**Expectation (hidden).** The swing starts as the jet passes and dies down over several seconds; the fitting is still beforehand.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A light fitting hangs from the ceiling on a cord or chain.
- S2 [core] The fitting swings.
- S3 [minor] The swing is gentle: a small sway, not a wild one.
- S4 [minor] The setting is a hallway inside a house.

**PC**
- P1 [core · causeless_motion]
  - expect: The swing is a pendulum about the ceiling fixing: the cord stays taut and straight and the fitting arcs below it.
  - fail: The fitting moves sideways with the cord bending or going slack; or the fixing point slides across the ceiling; or the fitting rotates in place without arcing; or rises toward the ceiling.
- P2 [core · process_direction]
  - expect: Once swinging, the arcs shrink until the fitting hangs still; they do not grow or restart.
  - fail: The arcs grow larger over the clip; or the swing stops dead in a tilted pose; or the fitting settles still and then starts swinging again.
- P3 [major · gravity_direction]
  - expect: At rest the fitting hangs straight down beneath its fixing.
  - fail: The fitting rests tilted with the cord taut and nothing touching it; or hangs above its fixing; or the cord arcs upward.
- P4 [major · causeless_motion] (if: Pictures, a mirror or coats hang on the hallway walls.)
  - expect: Other hanging things nearby stir at the same time as the fitting and are still before.
  - fail: A nearby picture or coat swings hard while the fitting is still; or objects on a shelf slide while the fitting hangs still; or the fitting and the other object start at plainly different moments.
- P5 [fatal · permanence_count]
  - expect: One fitting; the ceiling and walls stay intact.
  - fail: A second fitting appears; or the fitting vanishes; or it passes through the ceiling or a wall; or the cord detaches and the fitting stays up.
- P6 [minor · attribute_drift]
  - expect: The shade's colour and shape, the wall pictures and the floor pattern stay the same.
  - fail: The shade changes colour or shape; or the wall pictures change; or the floor pattern shifts.

**Note.** The jet is normally out of view; the swing is judged on its own shape and decay.

## ACOU-0039 · sound_driven_vibration · train

**Caption.** A subwoofer is turned up in a living room, and a picture frame on the wall behind it slowly tilts askew with the bass.

**Expectation (hidden).** The frame creeps out of level only while the bass plays, in small jerks, and stays where it ends up when the music stops; it does not straighten itself.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A living room with a subwoofer and a picture frame hanging on the wall behind it.
- S2 [core] The frame tilts out of level.
- S3 [minor] The tilt is slow and gradual.
- S4 [minor] The frame stays on the wall.
- S5 [minor] Something marks the volume being raised: a hand at a knob, a remote, or the cone beginning to pump.

**PC**
- P1 [core · causeless_motion]
  - expect: The frame turns about its hanging point in small jerks, staying against the wall.
  - fail: The frame swings out from the wall on its hook; or slides sideways along the wall keeping level; or turns in one smooth even sweep; or swings back to level by itself.
- P2 [core · missing_consequence] (if: The subwoofer's cone or grille is in view.)
  - expect: The frame moves only while the cone pumps and is still when the cone is still.
  - fail: The cone pumps for a long spell and the frame never shifts; or the frame jerks while the cone is plainly still; or the frame goes on moving after the cone has stopped.
- P3 [major · gravity_direction]
  - expect: The frame hangs from its hook and, once tilted, rests in its new pose held by the wall.
  - fail: The frame rises up the wall; or hangs above its hook; or floats off the wall.
- P4 [major · material_response]
  - expect: The frame is rigid and the wall solid.
  - fail: The frame bends; or the wall ripples; or the hanging wire stretches visibly.
- P5 [fatal · permanence_count]
  - expect: One frame, one subwoofer; nothing passes through the wall.
  - fail: A second frame appears; or the frame vanishes; or sinks into the wall; or the subwoofer turns into another object.
- P6 [minor · attribute_drift]
  - expect: The picture inside the frame, the wall colour and the subwoofer's look stay the same.
  - fail: The picture inside the frame changes; or the wall colour changes; or the subwoofer changes size or colour.

## ACOU-0040 · sound_driven_vibration · train

**Caption.** A hard rhythm is played on a drum kit in a small room, and a glass of water on a nearby amplifier ripples with each hit.

**Expectation (hidden).** Each ripple ring appears with a drum hit and fades before the next; the surface is calm when the drumming stops.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A drum kit being played: sticks strike the drums.
- S2 [core] A glass of water stands on an amplifier nearby.
- S3 [core] The water surface ripples.
- S4 [minor] The rhythm is hard and steady: repeated strikes through the clip.
- S5 [minor] The ripples come in pulses, one per hit, rather than a continuous shimmer.

**PC**
- P1 [core · missing_consequence]
  - expect: Each ring of ripples appears as a stick lands; the surface calms in any gap between hits.
  - fail: The sticks land repeatedly and the surface stays glassy; or rings appear while the sticks are held up away from the drums; or the water keeps rippling unchanged after the drumming has stopped.
- P2 [core · causeless_motion]
  - expect: The water stays level in the glass; the ripple is a surface tremble, not a slosh.
  - fail: The water sloshes up one side as if the glass were shoved; or spills with the glass standing still; or swirls round as if stirred; or a single ring spreads from one point as if something were dropped in.
- P3 [major · gravity_direction]
  - expect: The glass stands on the amplifier and the water stays in it.
  - fail: The glass rises off the amplifier; or water lifts out of the glass; or the surface stays tilted.
- P4 [major · material_response]
  - expect: The glass is rigid; the drumheads flex as skins under the sticks and the sticks rebound.
  - fail: A stick sinks into a drumhead and stays; or a drumhead shatters; or the glass bulges.
- P5 [fatal · permanence_count]
  - expect: One glass; the drums and sticks keep their count; no stick passes through a head or cymbal.
  - fail: A second glass appears; or the glass vanishes; or a stick passes through a cymbal or head; or drums appear or vanish.
- P6 [minor · attribute_drift]
  - expect: The amplifier's front, the glass and the water's colour stay the same.
  - fail: The amplifier's front changes; or the glass changes shape; or the water changes colour.

**Note.** The drummer is kept as the striking agent; posture and technique are not judged.

## ACOU-0041 · sound_driven_vibration · train

**Caption.** A door slams in a hallway, and a set of keys hanging on a hook beside it swings and jingles.

**Expectation (hidden).** The keys start swinging at the slam and settle within a few seconds; they hang still before.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A hallway door with a set of keys hanging on a hook beside it.
- S2 [core] The door slams shut.
- S3 [core] The keys swing and shake on the hook.
- S4 [minor] The keys stay on the hook.
- S5 [minor] The slam comes first and the swing follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The keys hang still until the door slams and start moving at the slam.
  - fail: The keys swing before the door reaches its frame; or the door slams and the keys hang dead still; or the keys start swinging again after settling with the door already closed.
- P2 [core · process_direction]
  - expect: After the slam the swing shrinks until the keys hang still.
  - fail: The arcs grow after the slam; or the keys stop dead in a tilted pose; or they swing at the same width until the end with no second slam.
- P3 [major · gravity_direction]
  - expect: The keys hang below the hook and at rest hang straight down.
  - fail: The keys rest tilted with nothing touching them; or rise above the hook; or float off the hook without falling.
- P4 [major · trajectory_momentum]
  - expect: The door turns on its hinges into its frame and stops there.
  - fail: The door slides sideways rather than turning on its hinges; or halts short of the frame and is then shown shut with no movement between; or swings shut and open again with nothing touching it.
- P5 [fatal · permanence_count]
  - expect: One set of keys, one hook, one door; nothing passes through the wall or frame.
  - fail: A second set of keys appears; or the keys vanish; or the door passes through its frame or wall; or the hook moves through the wall.
- P6 [minor · attribute_drift]
  - expect: The keys' fobs, the door's colour and the wall stay the same.
  - fail: The keys change number or colour; or the door changes colour; or the wall changes.

## ACOU-0042 · sound_driven_vibration · train

**Caption.** A powerful motorcycle revs its engine at a kerb, and the leaves of a potted plant on the pavement beside it quiver.

**Expectation (hidden).** The leaves shake while the engine revs and go still when it idles down.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A motorcycle stands at a kerb.
- S2 [core] A potted plant stands on the pavement beside it.
- S3 [core] The plant's leaves quiver.
- S4 [minor] The motorcycle is revved: a hand on the throttle, an exhaust puff or the bike's own shudder marks it.
- S5 [minor] The motorcycle stays in place; it does not ride off.

**PC**
- P1 [core · causeless_motion]
  - expect: The leaves tremble on their stems while the pot and the base of the stem stay fixed.
  - fail: The pot slides along the pavement; or the whole plant bends over and stays bent; or leaves float away from the plant; or the leaves keep their exact pose frozen while the pot itself trembles.
- P2 [core · missing_consequence] (if: The motorcycle's shudder or its exhaust puffs are visible.)
  - expect: The leaves quiver while the bike shudders or puffs exhaust and settle when it calms.
  - fail: The bike shudders for a spell and the leaves stay frozen; or the leaves quiver hard while the bike sits with no shudder and no exhaust puff; or the leaves start before the bike shows any sign of running.
- P3 [major · gravity_direction]
  - expect: Leaves hang from their stems and the pot rests on the ground; anything that comes free falls.
  - fail: A leaf that comes free rises; or the pot lifts; or the plant hangs upward.
- P4 [major · material_response]
  - expect: The leaves flex as thin leaves and the stems bend; the pot is rigid.
  - fail: The pot flexes like rubber; or the leaves swing as stiff boards; or the stems stretch.
- P5 [fatal · permanence_count]
  - expect: One bike, one plant; leaves do not multiply.
  - fail: A second plant appears; or the plant vanishes; or the bike passes through the kerb; or leaves multiply in one frame.
- P6 [minor · attribute_drift]
  - expect: The bike's colour, the pot's pattern and the leaves' colour stay the same.
  - fail: The bike changes colour; or the pot changes pattern; or the leaves change colour.

**Note.** A rider on the bike is a trigger and is not judged.

## ACOU-0043 · sound_driven_vibration · train

**Caption.** A concert speaker stack blasts a bass note, and the fabric grille on its front visibly pulses in and out.

**Expectation (hidden).** The grille flutters in time with the low notes and lies flat when the music stops.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A stack of concert speakers with a fabric grille on the front.
- S2 [core] The grille pulses in and out.
- S3 [minor] The pulses are repeated, in beats.
- S4 [minor] The speakers are a stack of several cabinets, not one.
- S5 [minor] The grille is cloth, not a metal mesh.

**PC**
- P1 [core · causeless_motion]
  - expect: The grille moves in and out relative to the cabinet, ballooning and flattening, while the cabinet stays put.
  - fail: The whole cabinet moves in and out with the grille; or the grille slides up or sideways across the front; or the grille peels off and floats; or it flaps only at one corner like a loose flag.
- P2 [core · missing_consequence]
  - expect: Between pulses and after the last one the grille lies flat over its frame.
  - fail: The grille freezes bulged outward or sucked inward and stays so; or it is flat in one frame and bulged in the next and never flattens; or it comes to rest hanging loose off its frame.
- P3 [major · material_response]
  - expect: The fabric stretches and flexes as cloth; the cabinet is rigid.
  - fail: The cabinet's wooden sides bulge; or the grille shatters or cracks; or the grille stretches longer and stays longer.
- P4 [major · causeless_motion] (if: A loose cable, banner or cloth hangs near the stack.)
  - expect: A loose cable, banner or cloth near the stack stirs with the pulses.
  - fail: The cloth hangs dead still while the grille pulses hard; or it flaps while the grille is still; or it streams steadily as in a wind while the grille pulses in beats.
- P5 [fatal · permanence_count]
  - expect: The cabinets keep their count and shape; the grille does not pass into the cabinet.
  - fail: A cabinet appears or vanishes; or cabinets merge; or the grille passes into the cabinet; or the stack changes shape.
- P6 [minor · attribute_drift]
  - expect: The grille's colour, the logos and the stage backdrop stay the same.
  - fail: The grille changes colour; or a logo moves; or the stage backdrop changes.

## ACOU-0044 · sound_driven_vibration · train

**Caption.** A helicopter hovers low over a field, and the surface of a pond beneath it shivers into fine ripples.

**Expectation (hidden).** The ripples appear while the helicopter is overhead and fade after it flies away; the water is calm before.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A helicopter hovers low over a field.
- S2 [core] A pond lies beneath it.
- S3 [core] The pond surface shows fine ripples.
- S4 [minor] The ripples are a fine shiver, not large waves.
- S5 [minor] The helicopter hovers in place rather than flying past.

**PC**
- P1 [core · missing_consequence]
  - expect: Ripples cover the pond while the helicopter is overhead; the water is calm before it arrives and settles after it leaves.
  - fail: The helicopter hangs overhead for a spell and the pond stays glassy; or the ripples are strongest with the helicopter far off and vanish as it comes close; or the pond keeps rippling unchanged long after the helicopter has flown out of view.
- P2 [core · causeless_motion]
  - expect: The ripples are a fine trembling spreading outward from beneath the helicopter; the water stays in the pond.
  - fail: The pond surface tilts as a whole; or water rises out of the pond; or one ring spreads from a point as if a stone were dropped; or the ripples travel as parallel waves from one shore.
- P3 [major · gravity_direction]
  - expect: The helicopter's rotor turns while it hangs in the air.
  - fail: The rotor blades are sharp and motionless while the helicopter stays aloft; or the helicopter jumps from one spot to another; or it drifts upward with its rotor stopped.
- P4 [major · material_response] (if: Grass or reeds stand near the pond.)
  - expect: Grass or reeds around the pond bend away from the helicopter and thrash while it is overhead.
  - fail: The grass stands motionless while the pond shivers; or bends toward the helicopter; or the grass thrashes while the pond stays glassy.
- P5 [fatal · permanence_count]
  - expect: One helicopter; the pond keeps its shape; the helicopter passes through nothing.
  - fail: A second helicopter appears; or the helicopter vanishes; or it passes through trees or wires; or the pond vanishes or changes shape.
- P6 [minor · attribute_drift]
  - expect: The helicopter's colour and markings, the field and the pond's colour stay the same.
  - fail: The helicopter changes colour or markings; or the field's features shift; or the pond changes colour.

## ACOU-0045 · sound_driven_vibration · train

**Caption.** A loud speaker plays a rising bass tone next to a tray of sand, and the sand grains jump and shift into patterns.

**Expectation (hidden).** The grains move only while the tone plays and stop when it stops; grains nearest the speaker move most.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A speaker stands next to a tray of sand.
- S2 [core] The sand grains jump.
- S3 [core] The grains gather into patterns: lines, ridges or patches.
- S4 [minor] The tray holds a thin loose layer of sand.
- S5 [minor] The jumping comes first and the patterns form from it.

**PC**
- P1 [core · causeless_motion]
  - expect: The grains hop in place; the tray stays put and the sand stays in it.
  - fail: The tray slides or spins across the table; or all the sand slides to one side as if the tray were tilted; or sand rises and hangs above the tray.
- P2 [core · missing_consequence]
  - expect: The pattern builds up from the hopping: grains collect into lines or heaps that stay once the hopping stops.
  - fail: A pattern appears fully formed in one step with no hopping before it; or a pattern forms and then dissolves back to even sand while the grains are still; or the pattern slides as a whole across the tray like a picture.
- P3 [major · gravity_direction]
  - expect: Grains fall back into the tray after each hop.
  - fail: Grains hang in the air; or float upward; or grains that leave the tray come back up into it.
- P4 [major · material_response]
  - expect: The grains stay separate and the tray stays rigid.
  - fail: The sand flows like a liquid with a sloshing level surface; or fuses into a solid sheet; or the tray flexes like cloth.
- P5 [fatal · permanence_count]
  - expect: The sand keeps its amount, allowing for grains leaving the tray; one speaker, one tray.
  - fail: Sand appears from nowhere on the tray; or the sand vanishes; or the speaker duplicates; or the tray sinks into the table.
- P6 [minor · attribute_drift]
  - expect: The speaker's colour, the tray's colour and the sand's colour stay the same.
  - fail: The speaker changes colour or shape; or the tray changes colour; or the sand changes colour.

## ACOU-0046 · sound_driven_vibration · train

**Caption.** An excavator drops a load of rubble into a steel skip, and a nearby chain-link fence shivers along its length.

**Expectation (hidden).** The shiver starts at the crash and fades within seconds; the fence is still before.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] An excavator holds a load of rubble above a steel skip.
- S2 [core] The rubble drops into the skip.
- S3 [core] A chain-link fence nearby shivers.
- S4 [minor] The shiver runs along the fence's length, not just one post.
- S5 [minor] The drop comes first and the shiver follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The fence is still until the rubble lands and starts shivering at the impact.
  - fail: The fence shivers before the rubble hits the skip; or the rubble lands and the fence stays dead still; or the fence starts shivering again after settling with no second load.
- P2 [core · process_direction]
  - expect: The shiver is strongest at the impact and fades afterwards.
  - fail: The shiver grows after the impact; or keeps the same strength to the end; or the fence stops dead bowed out in a bent pose.
- P3 [major · gravity_direction]
  - expect: The rubble falls downward into the skip and stays there.
  - fail: Rubble rises out of the skip after landing; or hangs in the air below the bucket; or pieces fall upward; or the bucket opens and the rubble stays in it hanging in place.
- P4 [major · material_response]
  - expect: The mesh flexes between fixed posts; the skip is rigid steel.
  - fail: The mesh stretches like elastic and stays stretched; or a post bends and springs back like rubber; or the skip's side ripples like cloth.
- P5 [fatal · permanence_count]
  - expect: One excavator, one skip, a continuous fence; the rubble does not pass through the skip.
  - fail: Rubble passes through the skip's floor or side; or the skip vanishes; or the fence gains or loses a section; or the excavator's arm passes through the skip.
- P6 [minor · attribute_drift]
  - expect: The excavator's colour, the skip's markings and the fence posts stay the same.
  - fail: The excavator changes colour; or the skip's markings change; or the fence posts move.

## ACOU-0047 · sound_driven_vibration · train

**Caption.** A phone on vibrate buzzes on a glass table, and a spoon lying next to it rattles against the glass.

**Expectation (hidden).** The spoon rattles in bursts with the phone's buzzes and lies still between them.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A phone and a spoon lie side by side on a glass table.
- S2 [core] The phone buzzes: it shivers in place.
- S3 [core] The spoon rattles against the glass: it trembles or hops.
- S4 [minor] The spoon lies close to the phone.
- S5 [minor] The spoon moves while the phone buzzes, not before.

**PC**
- P1 [core · causeless_motion]
  - expect: The spoon moves only while the phone shivers and lies still between buzzes.
  - fail: The spoon rattles while the phone is plainly still; or goes on rattling after the phone has stopped; or slides away in one smooth glide with no tremble.
- P2 [core · missing_consequence]
  - expect: While the phone shivers, the spoon beside it trembles too, and the phone itself creeps or turns a little rather than staying pinned.
  - fail: The phone shivers for a spell and the spoon lies dead still; or the phone's shiver stops and starts while the spoon's rattle runs on unchanged; or the spoon's rattle is strongest when the phone's shiver is weakest.
- P3 [major · gravity_direction]
  - expect: The spoon returns to the glass after each hop and stays on the table.
  - fail: The spoon hovers; or rises; or the phone lifts off the glass.
- P4 [major · material_response]
  - expect: The glass table is rigid and the spoon is rigid.
  - fail: The glass ripples like water; or the spoon bends; or the phone flexes.
- P5 [fatal · permanence_count]
  - expect: One phone, one spoon; nothing passes through the glass.
  - fail: A second spoon appears; or the phone vanishes; or the spoon sinks into the glass; or the phone and spoon merge.
- P6 [minor · attribute_drift]
  - expect: The phone's case, the spoon's shape and the table edge stay the same.
  - fail: The phone changes colour; or the spoon changes shape; or the table's edge changes.

## ACOU-0048 · sound_driven_vibration · train

**Caption.** A train crosses a metal bridge, and the water in a puddle on the road below shows shivering rings.

**Expectation (hidden).** The rings appear as the train crosses and fade after it has passed; the puddle is still before.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A train crosses a metal bridge.
- S2 [core] A puddle lies on the road below the bridge.
- S3 [core] The puddle's surface shows shivering rings.
- S4 [minor] The rings are fine shivers, not splashes.
- S5 [minor] The rings appear while the train is on the bridge.

**PC**
- P1 [core · missing_consequence]
  - expect: Rings cover the puddle while the train is on the bridge; the puddle is still before and settles after.
  - fail: The train crosses and the puddle stays glassy; or the puddle shivers hardest with the bridge empty and calms as the train crosses; or the puddle keeps shivering unchanged long after the train has gone from view.
- P2 [core · causeless_motion]
  - expect: The water stays in the puddle at its level; the shiver is in place.
  - fail: The puddle's water slides across the road; or one ring spreads from a point as from a dropped stone with nothing falling; or the water rises into a bulge; or the puddle's outline moves along the road.
- P3 [major · trajectory_momentum]
  - expect: The train runs along the bridge in one direction without a break.
  - fail: The train jumps forward between frames; or its carriages separate and rejoin; or it moves sideways off the rails without falling.
- P4 [major · gravity_direction]
  - expect: Water stays in the puddle and any drips from the bridge fall downward.
  - fail: Water lifts out of the puddle; or drips from the bridge fall upward; or the puddle climbs the kerb.
- P5 [fatal · permanence_count]
  - expect: One train on one bridge, one puddle; the train passes through no girder.
  - fail: The train passes through the bridge girders; or carriages appear or vanish mid-train; or the puddle vanishes in one frame; or the bridge changes shape.
- P6 [minor · attribute_drift]
  - expect: The train's livery, the road markings and the puddle's colour stay the same.
  - fail: The train's livery changes; or the road markings shift; or the puddle changes colour.

## ACOU-0049 · sound_driven_vibration · train

**Caption.** A stadium crowd stamps in unison, and the beer in a cup on a railing shows a steady wobble in time with the stamps.

**Expectation (hidden).** The wobble matches the rhythm of the stamping and settles when the crowd stops.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A stadium crowd stamps their feet together.
- S2 [core] A cup of beer stands on a railing.
- S3 [core] The beer's surface wobbles.
- S4 [minor] The wobble is steady and rhythmic.
- S5 [minor] The wobble keeps time with the stamping.

**PC**
- P1 [core · missing_consequence]
  - expect: Each stamp is followed by a wobble; when the crowd stops, the surface settles.
  - fail: The crowd stamps repeatedly and the beer stays glassy; or the beer wobbles hard while the crowd is not stamping; or the wobble runs on unchanged well after the stamping has stopped.
- P2 [core · causeless_motion]
  - expect: The beer stays in the cup and wobbles about level; the cup stays put on the railing.
  - fail: The beer rises out of the cup with the cup still; or the cup slides along the railing in one glide; or the beer swirls round as if stirred; or the surface stays tilted to one side.
- P3 [major · gravity_direction]
  - expect: The cup stays down on the railing and any spilled drops fall.
  - fail: The cup hovers; or foam lifts off and floats up; or drops fall upward.
- P4 [major · material_response]
  - expect: The cup and the railing stay rigid and the beer stays liquid.
  - fail: The cup crumples with nothing touching it; or the railing bends; or the beer turns into a solid block.
- P5 [fatal · permanence_count]
  - expect: One cup; the people in the crowd keep their count; nothing passes through the railing.
  - fail: A second cup appears; or the cup vanishes; or sinks into the railing; or people in the crowd merge or vanish.
- P6 [minor · attribute_drift]
  - expect: The cup's logo, the railing's colour and the beer's colour stay the same.
  - fail: The cup's colour or logo changes; or the railing changes colour; or the beer changes colour.

**Note.** The crowd is kept as the source of the stamping; only the timing of the stamps is used, not their behaviour.

## ACOU-0050 · sound_driven_vibration · train

**Caption.** A heavy cast-iron pan is dropped onto a stovetop, and the lids of neighbouring pots rattle for a moment.

**Expectation (hidden).** The rattle starts at the impact and stops within a second or two; the lids are still before.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A stovetop with pots that have lids on.
- S2 [core] A heavy cast-iron pan is dropped onto the stovetop.
- S3 [core] The lids of the neighbouring pots rattle.
- S4 [minor] The pan is dropped rather than set down: it falls the last stretch.
- S5 [minor] The rattle is brief.
- S6 [minor] The pan lands first and the lids rattle after.

**PC**
- P1 [core · causeless_motion]
  - expect: The lids are still until the pan lands and begin rattling at the impact.
  - fail: Lids rattle while the pan is still in the air; or the pan lands and the lids stay dead still; or lids start rattling again after settling with no second impact.
- P2 [core · process_direction]
  - expect: The rattle dies away and the lids come to rest seated on their pots.
  - fail: The rattle grows after the impact; or keeps going unchanged to the end of the clip; or a lid freezes in mid-hop above its pot.
- P3 [major · gravity_direction]
  - expect: The pan falls down onto the stove and stays; lids that hop fall back.
  - fail: The pan hangs in the air before landing; or a lid lifts off and stays up; or the pan lands and then rises again.
- P4 [major · material_response]
  - expect: The pan, the stovetop and the lids stay rigid.
  - fail: The pan bends or splashes like a liquid; or the stovetop ripples; or a lid bends.
- P5 [fatal · permanence_count]
  - expect: The pots and lids keep their count; one pan; nothing passes through the stovetop.
  - fail: A pot or lid appears or vanishes; or the pan passes through the stovetop; or the pan and a pot merge; or the pan vanishes.
- P6 [minor · attribute_drift]
  - expect: The pots' colours, the stove knobs and the pan's size stay the same.
  - fail: Pots change colour; or the stove knobs change; or the pan changes size.

**Note.** The hand that drops the pan is a trigger and is not judged.

## ACOU-0051 · sound_driven_vibration · train

**Caption.** A speaker on the floor of a room plays a deep bass note, and a lit candle on the same floor flickers in time with the beats.

**Expectation (hidden).** The flame flutters with each beat and burns steady when the music stops.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A speaker stands on the floor of a room.
- S2 [core] A lit candle stands on the same floor.
- S3 [core] The flame flickers.
- S4 [minor] The flicker comes in repeated pulses rather than one continuous waver.
- S5 [minor] The candle stays lit throughout.

**PC**
- P1 [core · causeless_motion]
  - expect: The flame stays on the wick and points up between pulses; each flicker is a bend or shiver of the flame.
  - fail: The flame detaches and floats away; or lies flat along the floor and stays so; or the candle slides across the floor without any tremble.
- P2 [core · missing_consequence] (if: The speaker's cone is in view.)
  - expect: The flame flickers while the cone pumps and burns steady when the cone is still.
  - fail: The cone pumps and the flame burns without a stir; or the flame flickers hard while the cone is plainly still; or the flame goes on flickering unchanged after the cone has stopped.
- P3 [major · gravity_direction]
  - expect: At rest the flame points up and any wax drips run down the candle.
  - fail: The flame points downward or sideways when at rest; or wax runs up the candle; or the candle rises off the floor.
- P4 [major · material_response]
  - expect: The candle body stays rigid and the flame stays a flame.
  - fail: The candle bends like rubber; or the flame turns into a solid glowing ball; or the wick stretches longer.
- P5 [fatal · permanence_count]
  - expect: One candle with one flame, one speaker; nothing passes into the floor.
  - fail: A second flame appears on the same wick; or the candle vanishes; or the speaker duplicates; or the candle sinks into the floor.
- P6 [minor · attribute_drift]
  - expect: The candle's colour, the speaker's shape and the floor pattern stay the same.
  - fail: The candle changes colour; or the speaker changes shape; or the floor pattern shifts.

## ACOU-0052 · sound_driven_vibration · train

**Caption.** A chainsaw is revved in a garage, and the tools hanging on the pegboard behind it sway and tap against the board.

**Expectation (hidden).** The tools move while the saw runs and hang still when it is shut off.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A chainsaw in a garage, in front of a pegboard hung with tools.
- S2 [core] The chainsaw is revved: its chain runs or the saw shudders.
- S3 [core] The tools sway and tap against the board.
- S4 [minor] The tools stay on their pegs.
- S5 [minor] The revving comes first and the swaying follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The tools hang still until the saw runs and settle if it stops.
  - fail: Tools sway before the saw starts; or go on swaying after the saw has stopped and settled; or a tool slides along the pegboard from one peg to another.
- P2 [core · missing_consequence]
  - expect: While the saw runs the tools stir and each swing brings them back against the board.
  - fail: The saw shudders for a spell and every tool hangs dead still; or the tools swing away from the board and stay held off it; or a tool swings out from the board and hangs in the air.
- P3 [major · gravity_direction]
  - expect: The tools hang down from their pegs and at rest hang straight.
  - fail: A tool rests tilted with nothing touching it; or rises up the board; or a tool that leaves its peg floats rather than falling.
- P4 [major · material_response]
  - expect: The tools and the pegboard are rigid; the sway is a swing on the peg.
  - fail: A wrench bends; or the pegboard ripples; or a tool's handle stretches.
- P5 [fatal · permanence_count]
  - expect: The tools keep their count; one chainsaw; nothing passes through the board.
  - fail: A tool appears or vanishes; or a tool passes through the board; or two tools merge; or the chainsaw duplicates.
- P6 [minor · attribute_drift]
  - expect: The tools' colours, the pegboard's colour and the saw's colour stay the same.
  - fail: Tools change colour; or the pegboard changes colour; or the saw changes colour.

**Note.** The person revving the saw is a trigger and is not judged.

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

## ACOU-0056 · source_motion · train

**Caption.** A struck tuning fork is brought up to a ping-pong ball hanging on a thread, and the ball is kicked away and swings.

**Expectation (hidden).** The ball hangs still until the prongs touch it, is knocked outward on contact and swings back, being kicked again if it returns to the ringing fork; nothing moves before contact.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A ping-pong ball hangs on a thread.
- S2 [core] A tuning fork is brought up to the ball.
- S3 [core] The ball is kicked away from the fork.
- S4 [core] The ball swings.
- S5 [minor] The fork is shown being struck, or its prongs show a blur.
- S6 [minor] The fork approaches first; the kick and the swing follow.

**PC**
- P1 [core · causeless_motion]
  - expect: The ball hangs still until the prongs touch it and moves off only on contact.
  - fail: The ball swings away before the fork reaches it; or the prongs touch it and it hangs unmoved; or the ball moves toward the fork on its own.
- P2 [core · process_direction]
  - expect: The ball is knocked outward, swings back and is kicked again if it returns to the ringing fork; with the fork withdrawn its swing shrinks.
  - fail: The ball swings ever wider with the fork held away; or stops dead in mid-swing; or is kicked again with the fork withdrawn; or comes to rest pressed against the prongs while they are still blurred.
- P3 [major · gravity_direction]
  - expect: The thread stays taut with the ball hanging below its fixing; at rest the ball hangs straight down.
  - fail: The thread goes slack while the ball stays up; or the ball rises above its fixing; or rests tilted with nothing touching it.
- P4 [major · material_response]
  - expect: The ball and the fork stay rigid and the thread stays straight.
  - fail: The ball dents and stays dented; or the prongs bend; or the thread stretches.
- P5 [fatal · permanence_count]
  - expect: One ball, one fork; the prongs do not pass through the ball.
  - fail: A second ball appears; or the ball vanishes; or the prongs pass through the ball; or the fork changes shape.
- P6 [minor · attribute_drift]
  - expect: The ball's colour, the fork's size and the thread's length stay the same.
  - fail: The ball changes colour; or the fork changes size; or the thread changes length.

**Note.** The hand holding the fork is a trigger and is not judged.

## ACOU-0057 · source_motion · train

**Caption.** A coin stands balanced on the hood of a car idling roughly, and it jitters and topples over.

**Expectation (hidden).** The coin trembles in place while the engine runs and eventually falls flat, staying down; it does not move before the engine starts or stand back up.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A coin stands on its edge on a car's hood.
- S2 [core] The coin jitters.
- S3 [core] The coin topples over and lies flat.
- S4 [minor] The car is stationary.
- S5 [minor] The jitter comes first and the topple follows.

**PC**
- P1 [core · causeless_motion]
  - expect: While standing, the coin trembles in place on the hood.
  - fail: The coin slides across the hood in a smooth glide while standing; or leaps up off the hood; or shifts from place to place with no tremble between.
- P2 [core · missing_consequence]
  - expect: The topple is one way: the coin falls flat and stays flat.
  - fail: The coin falls flat and rights itself; or stops leaning at an angle and stays leaning with nothing touching it; or lies flat and then stands up on its edge again.
- P3 [major · gravity_direction]
  - expect: The coin falls downward onto the hood; on a sloping hood it may slide down.
  - fail: The coin falls upward; or hovers above the hood; or slides up the hood's slope after landing.
- P4 [major · material_response]
  - expect: The coin and the hood stay rigid.
  - fail: The coin bends; or the hood dents under the coin; or the hood ripples like cloth.
- P5 [fatal · permanence_count]
  - expect: One coin, one car; the coin does not pass into the hood.
  - fail: A second coin appears; or the coin vanishes; or it sinks into the hood; or the car changes shape.
- P6 [minor · attribute_drift]
  - expect: The coin's face and size and the car's paint stay the same.
  - fail: The coin changes size or face; or the car changes colour; or the hood's reflections change with nothing moving.

## ACOU-0058 · source_motion · train

**Caption.** A small paper rider sits on the string of a cello; a bow is drawn across that string and the rider is thrown off.

**Expectation (hidden).** The rider stays put until the bow touches the string, is flicked off as soon as the string sounds and does not return; riders on other strings stay still.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A cello with a small paper rider sitting on one string.
- S2 [core] A bow is drawn across that string.
- S3 [core] The rider is thrown off the string.
- S4 [minor] The bow is drawn on the string carrying the rider, not another.
- S5 [minor] The bow moves first and the rider flies off after.

**PC**
- P1 [core · causeless_motion]
  - expect: The rider sits still until the bow touches the string.
  - fail: The rider slides or hops before the bow touches the string; or flies off while the bow is held away; or riders on other strings jump too while their strings are not bowed.
- P2 [core · missing_consequence]
  - expect: Once the bowed string sounds, the rider is flicked off and does not return to the string.
  - fail: The bow saws across the string and the rider sits unmoved; or the rider hops and settles back onto the same string; or the rider is thrown off and then reappears on the string.
- P3 [major · gravity_direction]
  - expect: The rider falls after being thrown, onto the cello's body or the floor.
  - fail: The rider hangs in the air; or rises; or drifts sideways out of view without dropping.
- P4 [major · material_response]
  - expect: The string flexes as a taut string and springs back; the bow is rigid; the cello body is rigid.
  - fail: The string is pulled into a wide bent shape and stays bent after the bow leaves; or the bow bends like rubber; or the cello body ripples.
- P5 [fatal · permanence_count]
  - expect: One rider; the strings keep their count; the bow does not pass through the strings.
  - fail: A second rider appears; or the rider vanishes in mid-air; or the bow passes through the strings; or the strings change count.
- P6 [minor · attribute_drift]
  - expect: The rider's colour and size, the cello's finish and the string spacing stay the same.
  - fail: The rider changes colour or size; or the cello changes colour; or the strings change spacing.

**Note.** The player's bow arm is a trigger and is not judged.

## ACOU-0059 · source_motion · train

**Caption.** A wind-up alarm clock rings, and its little hammer hammers between the two bells and the clock shivers on the table.

**Expectation (hidden).** The hammer swings rapidly and the clock shakes only while it rings; both stop when the button is pressed.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A wind-up alarm clock with two bells on top stands on a table.
- S2 [core] The little hammer swings between the bells.
- S3 [core] The clock shivers on the table.
- S4 [minor] The hammer moves rapidly back and forth.
- S5 [minor] The hammer swings and the clock shivers at the same time.

**PC**
- P1 [core · causeless_motion]
  - expect: The hammer swings from its base between the two bells and the clock trembles in place.
  - fail: The clock shivers while the hammer hangs still; or the clock glides smoothly across the table; or the hammer detaches and floats; or the bells swing on their own while the hammer is still.
- P2 [core · missing_consequence]
  - expect: While the hammer swings the clock shivers; when the hammer stops the clock stands still.
  - fail: The hammer swings hard and the clock stands dead still; or the hammer stops and the clock keeps shivering unchanged; or the hammer swings but stays clear of both bells for the whole clip.
- P3 [major · gravity_direction]
  - expect: The clock stays on the table; if it walks to the edge it falls.
  - fail: The clock lifts off the table; or tips and hangs at an angle unsupported; or rises up on end.
- P4 [major · material_response]
  - expect: The clock case and bells are rigid; the hammer is a rigid head on a thin stalk.
  - fail: The bells dent or wobble like rubber; or the clock case bends; or the hammer stalk stretches.
- P5 [fatal · permanence_count]
  - expect: One clock with two bells and one hammer; the hammer does not pass through a bell.
  - fail: A third bell appears; or the hammer vanishes; or the hammer passes through a bell; or the clock duplicates.
- P6 [minor · attribute_drift]
  - expect: The clock face, its hands and the table stay the same.
  - fail: The clock face changes; or the hands jump; or the table changes.

## ACOU-0060 · source_motion · train

**Caption.** A hand-held massager is switched on and set on a bed, and it shudders and wanders across the sheet.

**Expectation (hidden).** The shudder and wandering start with the switch and stop with it; the massager is still when off.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A hand-held massager is set down on a bed.
- S2 [core] It is switched on: a button is pressed or it begins to shudder.
- S3 [core] It shudders.
- S4 [core] It wanders across the sheet.
- S5 [minor] It is switched on and set down before it starts wandering.

**PC**
- P1 [core · causeless_motion]
  - expect: The massager moves only while it shudders and is still when off.
  - fail: It moves before it is switched on; or glides across the sheet with no shudder; or keeps moving after being switched off.
- P2 [core · missing_consequence]
  - expect: The shudder carries it along in small jerks that match the shuddering.
  - fail: It plainly shudders yet stays pinned in place for the whole clip; or moves in one smooth glide as if pulled by a string; or shudders hard while frozen in place and then glides while its shudder has stopped.
- P3 [major · gravity_direction]
  - expect: It rests on the bed, pressing into the soft surface; if it reaches the edge it falls.
  - fail: It hovers above the sheet; or climbs up the pillow and perches on end; or rises.
- P4 [major · material_response]
  - expect: The bed is soft and dimples under it; the massager is rigid.
  - fail: The bed surface ripples like water; or the massager bends; or it leaves a hard groove carved in the mattress.
- P5 [fatal · permanence_count]
  - expect: One massager; it does not sink into the mattress, duplicate or vanish.
  - fail: A second massager appears; or it vanishes; or it sinks into the mattress and disappears; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: Its colour, the sheet's pattern and the pillows stay the same.
  - fail: It changes colour; or the sheet pattern changes; or the pillows change shape.

**Note.** The hand that switches it on and sets it down is a trigger and is not judged.

## ACOU-0061 · source_motion · train

**Caption.** A blender runs on a kitchen counter, and its base vibrates and inches slightly across the counter.

**Expectation (hidden).** The movement happens only while the motor runs, in small shifts rather than a smooth glide.

**Declared violation types.** causeless_motion, trajectory_momentum

**SA**
- S1 [core] A blender stands on a kitchen counter, running: its blades turn or its contents churn.
- S2 [core] The base vibrates.
- S3 [core] The blender moves across the counter.
- S4 [minor] The movement is slight, a small shift.
- S5 [minor] The blender stays upright.

**PC**
- P1 [core · causeless_motion]
  - expect: The blender moves only while it runs and vibrates; if stopped it stays where it is.
  - fail: The blender moves while its contents are still and the base shows no tremble; or keeps moving after being switched off; or moves before it is running.
- P2 [core · trajectory_momentum]
  - expect: The creep is a series of small shifts in a roughly steady direction, with slow turning at most.
  - fail: The blender glides in one smooth slide; or darts back and forth across the counter; or returns to its exact start over and over; or lifts one side and hops.
- P3 [major · gravity_direction]
  - expect: The blender stays down on the counter; at the edge it would fall.
  - fail: The blender hovers; or hangs over the edge past its middle; or climbs onto an object.
- P4 [major · material_response]
  - expect: The counter and the jar stay rigid; the contents churn inside.
  - fail: The counter ripples; or the jar bends; or the contents pass out through the closed lid.
- P5 [fatal · permanence_count]
  - expect: One blender; nothing passes through the counter.
  - fail: A second blender appears; or it vanishes; or sinks into the counter; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The blender's colour, the counter pattern and the wall behind stay the same.
  - fail: The blender changes colour; or the counter pattern changes; or the wall behind changes.

## ACOU-0062 · source_motion · train

**Caption.** A lawnmower is started, and its handle shakes visibly.

**Expectation (hidden).** The shaking begins with the engine and lasts as long as it runs.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A lawnmower stands on grass or ground.
- S2 [core] The mower is started: a cord is pulled or a button or key is used.
- S3 [core] The handle shakes.
- S4 [minor] The start comes first and the shaking follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The handle is still before the start and shakes only after it.
  - fail: The handle shakes before the cord is pulled or the start is made; or the shaking stops and starts while nothing changes at the engine; or the handle swings as a pendulum in slow wide arcs rather than trembling.
- P2 [core · missing_consequence]
  - expect: Once the start is made the engine shows itself: the handle shakes and keeps shaking while the mower runs.
  - fail: The cord is pulled and the handle stays dead still for the rest of the clip; or exhaust puffs come from the engine while the handle stays still; or the pull cord stays hanging out slack after the pull instead of retracting.
- P3 [major · gravity_direction]
  - expect: The mower rests on its wheels on the ground.
  - fail: The mower lifts off the ground; or tips and hangs at an angle; or rises.
- P4 [major · material_response]
  - expect: The handle is a rigid tube that shakes as a whole; the deck is rigid.
  - fail: The handle bends like rubber; or stretches; or the deck ripples.
- P5 [fatal · permanence_count]
  - expect: One mower; the handle stays attached.
  - fail: A second mower appears; or the mower vanishes; or the handle detaches and floats; or the mower passes into the ground.
- P6 [minor · attribute_drift]
  - expect: The mower's colour, the grass and the wheels stay the same.
  - fail: The mower changes colour; or the grass pattern changes; or the wheels change size.

**Note.** The person starting the mower is a trigger and is not judged.

## ACOU-0063 · source_motion · train

**Caption.** The pedal of a bass drum is pressed repeatedly, and the beater swings into the drumhead with each press and the head dips each time.

**Expectation (hidden).** The beater moves only when the pedal is pressed and the head dips only when the beater lands; nothing moves between presses.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A bass drum with a pedal and a beater.
- S2 [core] The pedal is pressed repeatedly.
- S3 [core] The beater swings into the drumhead with each press.
- S4 [core] The head dips with each hit.
- S5 [minor] There are several presses in the clip.
- S6 [minor] Each press comes before its beater swing and dip.

**PC**
- P1 [core · causeless_motion]
  - expect: The beater moves only when the pedal is pressed and rests between presses.
  - fail: The beater swings while the pedal is up and untouched; or moves toward the head before the pedal goes down; or keeps bouncing between presses with the pedal still.
- P2 [core · missing_consequence]
  - expect: Each time the beater lands the head dips and springs back; no dip without the beater.
  - fail: The beater lands and the head stays flat; or the head dips while the beater is away from it; or the head stays dented after the beater has left; or the pedal is pressed and the beater does not move.
- P3 [major · trajectory_momentum]
  - expect: The beater arcs about its pivot and the pedal hinges at its base.
  - fail: The beater slides straight toward the head without arcing; or the pedal moves up and down as a whole without hinging; or the beater moves in a different direction from the pedal's press.
- P4 [major · material_response]
  - expect: The head flexes as a skin and the rigid beater rebounds from it.
  - fail: The beater sinks into the head and stays; or the head shatters; or the beater rod bends double.
- P5 [fatal · permanence_count]
  - expect: One beater, one pedal, one drum; the beater does not pass through the head.
  - fail: A second beater appears; or the beater passes through the head; or the drum changes shape; or the pedal vanishes.
- P6 [minor · attribute_drift]
  - expect: The drum's finish, the head's logo and the pedal's colour stay the same.
  - fail: The drum changes colour; or the head's logo changes; or the pedal changes colour.

**Note.** The foot on the pedal is a trigger and is not judged.

## ACOU-0064 · source_motion · train

**Caption.** A washing machine on its spin cycle rocks and shudders on the floor, and it settles still as the drum slows to a stop.

**Expectation (hidden).** The shuddering is strongest at full spin and dies away as the drum slows; the machine is still once the drum stops.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A washing machine stands on a floor.
- S2 [core] It rocks and shudders.
- S3 [core] The drum is seen slowing to a stop.
- S4 [core] The machine settles still.
- S5 [minor] The rocking is under way first and the settling follows the slowing.

**PC**
- P1 [core · causeless_motion]
  - expect: The machine rocks in place on its feet; it does not glide.
  - fail: The machine slides across the floor in one smooth glide; or rocks while the drum is plainly still; or starts shuddering again after settling with the drum stopped.
- P2 [core · process_direction]
  - expect: The shudder is strongest at full spin and fades as the drum slows; once the drum stops the machine is still.
  - fail: The shuddering grows as the drum slows; or the drum stops and the machine goes on shuddering unchanged; or the machine stops dead in a tilted pose off its feet.
- P3 [major · gravity_direction]
  - expect: The machine rests on the floor and returns to all its feet after each rock.
  - fail: The machine lifts off the floor entirely; or stays balanced on one corner; or rises.
- P4 [major · material_response]
  - expect: The machine's body, its door glass and the floor stay rigid.
  - fail: The body bends like rubber; or the floor ripples; or the door glass bulges.
- P5 [fatal · permanence_count]
  - expect: One machine; nothing passes through the floor.
  - fail: A second machine appears; or it vanishes; or sinks into the floor; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The dials, the machine's colour and the wall behind stay the same.
  - fail: The dials change; or the machine changes colour; or the wall behind changes.

## ACOU-0065 · source_motion · train

**Caption.** A large bell in a tower is rung by a rope, and it swings back and forth with the clapper striking it on each swing.

**Expectation (hidden).** The bell swings only while the rope is pulled and its swings die down once the pulling stops.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A large bell hangs in a tower.
- S2 [core] A rope pulls it: the rope moves.
- S3 [core] The bell swings back and forth.
- S4 [core] The clapper strikes the bell on each swing.
- S5 [minor] Each pull of the rope precedes a swing.

**PC**
- P1 [core · causeless_motion]
  - expect: The bell swings about its pivot as the rope moves; the rope and the bell move together.
  - fail: The bell swings while the rope hangs slack and still for the whole clip; or the bell swings sideways across its pivot; or spins around its vertical axis; or the rope moves and the bell hangs dead still.
- P2 [core · process_direction]
  - expect: While the rope is pulled the arcs hold or grow; once the pulling stops the arcs shrink.
  - fail: The arcs grow with the rope hanging slack; or the bell stops dead at the top of a swing; or the clapper stays pinned to the centre of the bell throughout while the bell swings.
- P3 [major · gravity_direction]
  - expect: The bell hangs below its pivot with its mouth down at rest; the clapper hangs down inside it.
  - fail: The bell rests tilted with nothing holding it; or the clapper hangs upward; or the bell rises above its pivot and stays.
- P4 [major · trajectory_momentum]
  - expect: The clapper swings inside the bell, hits the rim and falls back.
  - fail: The clapper hangs frozen against one side for the whole swing; or strikes the outside of the bell; or leaves the bell and swings outside it.
- P5 [fatal · permanence_count]
  - expect: One bell with one clapper; a continuous rope; nothing passes through the bell or the beams.
  - fail: A second bell appears; or the clapper vanishes; or the clapper passes through the bell wall; or the rope passes through the wheel or beams.
- P6 [minor · attribute_drift]
  - expect: The bell's colour, the tower stones and the rope stay the same.
  - fail: The bell changes colour; or the tower stones shift; or the rope changes colour.

**Note.** Whoever pulls the rope is a trigger and is not judged.

## ACOU-0066 · source_motion · train

**Caption.** A desk fan with a bent blade is switched on, and the whole fan wobbles visibly on its base as the blades spin.

**Expectation (hidden).** The wobble starts as the blades spin up, keeps a steady rhythm while they turn, and is absent when the blades are still; the fan does not wobble before it is switched on.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A desk fan stands on a surface.
- S2 [core] The fan is switched on: the blades start to spin.
- S3 [core] The whole fan wobbles on its base.
- S4 [minor] One blade is bent, visible while the fan is still.
- S5 [minor] The switch-on comes first and the wobble follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The fan is still before the switch and wobbles only while the blades spin.
  - fail: The fan wobbles before the blades turn; or wobbles while the blades are plainly stopped; or slides across the desk in a smooth glide.
- P2 [core · missing_consequence]
  - expect: While the blades spin the fan wobbles in a steady rhythm, and the wobble ends when the blades stop.
  - fail: The blades spin fast and the fan stands dead still for the whole clip; or the blades stop and the wobble goes on unchanged; or the wobble comes in irregular fits with long still spells while the blades spin steadily.
- P3 [major · gravity_direction]
  - expect: The fan stays on its base; if it walks to the edge it falls.
  - fail: The fan lifts off the desk; or tips and hangs at an angle unsupported; or rises.
- P4 [major · material_response]
  - expect: The cage and base are rigid; the blades are rigid and the bent one stays bent.
  - fail: The cage flexes like cloth; or the base bends; or the bent blade straightens itself while spinning.
- P5 [fatal · permanence_count]
  - expect: One fan; the blades keep their count and stay inside the cage.
  - fail: A second fan appears; or the fan vanishes; or a blade passes through the cage; or the blades change count.
- P6 [minor · attribute_drift]
  - expect: The fan's colour, its cage pattern and the wall behind stay the same.
  - fail: The fan changes colour; or the cage changes pattern; or the wall behind changes.

## ACOU-0067 · source_motion · train

**Caption.** A pager on vibrate goes off on a nightstand and rattles against the wood.

**Expectation (hidden).** The rattling and small movements happen only while it vibrates.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A pager lies on a wooden nightstand.
- S2 [core] The pager goes off: its screen lights or it begins to shiver.
- S3 [core] It rattles against the wood: it shivers and hops in place.
- S4 [minor] It stays on the nightstand.
- S5 [minor] It lies still first and the rattling begins during the clip.

**PC**
- P1 [core · causeless_motion]
  - expect: The pager moves only while it visibly shivers and is still otherwise.
  - fail: The pager slides while lying perfectly still; or keeps moving after the shiver has stopped; or moves in one smooth glide with no shiver.
- P2 [core · missing_consequence] (if: Other small loose objects lie on the nightstand.)
  - expect: Other small loose objects on the nightstand tremble in the same bursts as the pager.
  - fail: A coin, pen or pair of glasses beside it lies dead still while the pager rattles hard; or the other object rattles while the pager is still; or the two rattle at different moments.
- P3 [major · gravity_direction]
  - expect: The pager stays flat on the nightstand; at the edge it would fall.
  - fail: The pager hovers; or stands up on end; or rises.
- P4 [major · material_response]
  - expect: The wood and the pager stay rigid.
  - fail: The wood ripples; or the pager bends; or the pager leaves a groove in the wood.
- P5 [fatal · permanence_count]
  - expect: One pager; it does not pass into the wood, duplicate or vanish.
  - fail: A second pager appears; or it vanishes; or sinks into the wood; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The pager's colour, its screen and the lamp beside it stay the same.
  - fail: The pager changes colour; or its screen shows different content at random; or the lamp beside it changes.

## ACOU-0068 · source_motion · train

**Caption.** Sand is sprinkled on a cymbal and a violin bow is drawn along its edge, and the sand jumps and gathers into lines.

**Expectation (hidden).** The sand lies still until the bow moves, dances while the bow is drawn and collects into lines or patches, and settles when the bow lifts; no pattern forms before the bow touches the cymbal.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] Sand is sprinkled onto a cymbal, or lies sprinkled on it.
- S2 [core] A violin bow is drawn along the cymbal's edge.
- S3 [core] The sand jumps.
- S4 [core] The sand gathers into lines.
- S5 [minor] The bow moves first and the sand jumps after; the lines form from the jumping.

**PC**
- P1 [core · causeless_motion]
  - expect: The sand lies still until the bow touches the edge, hops while the bow moves and settles when it lifts.
  - fail: Sand hops before the bow touches the cymbal; or hops while the bow is held away; or the bow is drawn and the sand lies dead still; or the sand goes on hopping well after the bow has lifted.
- P2 [core · missing_consequence]
  - expect: The hopping gathers the sand into lines or patches that stay after the bow lifts; no pattern exists before the bowing.
  - fail: Lines appear fully formed before or without any hopping; or a pattern forms and then dissolves back to an even sprinkle while the sand is still; or the pattern slides as a whole around the cymbal like a picture.
- P3 [major · gravity_direction]
  - expect: Grains fall back onto the cymbal or off its edge.
  - fail: Grains hang in the air; or float up; or grains that fell off return up onto the cymbal.
- P4 [major · material_response]
  - expect: The cymbal is a rigid metal disc that may wobble; the bow is rigid; the grains stay separate.
  - fail: The cymbal ripples like water; or the bow bends double; or the sand flows as a liquid puddle.
- P5 [fatal · permanence_count]
  - expect: One cymbal, one bow; the sand keeps its amount, allowing for grains falling off.
  - fail: Sand appears from nowhere; or all the sand vanishes; or the bow passes through the cymbal; or the cymbal changes shape.
- P6 [minor · attribute_drift]
  - expect: The cymbal's colour, the bow's length and the stand stay the same.
  - fail: The cymbal changes colour; or the bow changes length; or the stand changes.

**Note.** The hand on the bow is a trigger and is not judged.

## ACOU-0069 · source_motion · train

**Caption.** A generator runs on a building site, and its frame shakes and the loose bolts on it rattle.

**Expectation (hidden).** The shaking and rattling last as long as the engine runs and stay on the frame.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A generator on a building site.
- S2 [core] Its frame shakes.
- S3 [core] Loose bolts on the frame rattle.
- S4 [minor] The generator is running: exhaust, spinning parts or its shake mark it.
- S5 [minor] The bolts stay on the frame.

**PC**
- P1 [core · causeless_motion]
  - expect: The frame trembles in place and the bolts rattle in their holes; the generator does not glide.
  - fail: The generator slides across the ground in a glide; or the bolts rattle while the frame is plainly still; or a bolt hops out and travels away across the ground on its own.
- P2 [core · missing_consequence]
  - expect: While the frame shakes the loose bolts rattle; a bolt that shakes free falls.
  - fail: The frame shakes hard and every bolt sits frozen; or a bolt spins in place while the frame is not trembling; or the shaking stops while the bolts go on rattling.
- P3 [major · gravity_direction]
  - expect: The generator rests on the ground; any bolt that comes free drops.
  - fail: The generator lifts; or a loosened bolt rises; or a bolt hangs in the air.
- P4 [major · material_response]
  - expect: The frame is rigid steel and the casing rigid.
  - fail: The frame bends like rubber; or the casing ripples; or the bolts stretch.
- P5 [fatal · permanence_count]
  - expect: One generator; the bolts keep their count; nothing passes through the frame.
  - fail: A second generator appears; or the generator vanishes; or bolts appear on the frame from nowhere; or a bolt passes through the frame.
- P6 [minor · attribute_drift]
  - expect: The generator's colour, its labels and the site behind stay the same.
  - fail: The generator changes colour; or the site background changes; or the labels change.

## ACOU-0070 · source_motion · train

**Caption.** The keys of a toy piano are banged, and the small hammers inside can be seen jumping up with each key press.

**Expectation (hidden).** Each hammer moves only when its key is pressed and falls back after; hammers of unpressed keys stay down.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A toy piano with its hammers visible.
- S2 [core] Keys are pressed hard.
- S3 [core] A hammer jumps up with each key press.
- S4 [minor] Several keys are banged.
- S5 [minor] Each key press comes before its hammer's jump.

**PC**
- P1 [core · causeless_motion]
  - expect: A hammer moves only when its key is pressed; hammers of untouched keys stay down.
  - fail: A hammer jumps while no key is pressed; or hammers of untouched keys jump along with the pressed one; or a hammer rises before its key goes down.
- P2 [core · missing_consequence]
  - expect: Each pressed key sends its own hammer up; the hammer falls back and the key returns.
  - fail: A key goes down and no hammer moves; or the hammer rises and stays up after the key is released; or the hammer that jumps is far from the pressed key; or the key stays down after release.
- P3 [major · gravity_direction]
  - expect: Hammers fall back down after each jump.
  - fail: A hammer hangs in the air; or floats up; or falls sideways out of the frame.
- P4 [major · material_response]
  - expect: The hammers, keys and piano body are rigid.
  - fail: Keys bend like rubber; or hammers stretch; or the piano body ripples.
- P5 [fatal · permanence_count]
  - expect: The hammers and keys keep their count; nothing passes through the lid.
  - fail: Hammers appear or vanish; or a hammer passes through the lid; or keys change count; or two hammers merge.
- P6 [minor · attribute_drift]
  - expect: The piano's colour, the keys' colours and the hammers' colour stay the same.
  - fail: The piano changes colour; or the keys' colours swap; or the hammers change colour.

**Note.** The hands on the keys are a trigger and are not judged.

## ACOU-0071 · source_motion · train

**Caption.** A paint shaker at a hardware store is switched on, and the paint can clamped in it blurs with the shaking.

**Expectation (hidden).** The can is sharp before the machine starts and blurs only while it runs.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A paint shaker machine with a paint can clamped in it.
- S2 [core] The machine is switched on.
- S3 [core] The can blurs with the shaking.
- S4 [minor] The can is sharp before the machine starts.
- S5 [minor] The switch-on comes first and the blur follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The can and its clamp shake together while the machine's body stays put.
  - fail: The can shakes while the clamp holding it stays sharp and still; or the can blurs before the switch is thrown; or the machine glides across the floor; or the can shakes loose and floats.
- P2 [core · missing_consequence]
  - expect: Once on, the can blurs; once off, it is sharp again.
  - fail: The machine is switched on and the can stays sharp and still for the rest of the clip; or the machine is switched off and the blur continues unchanged; or the blur comes and goes while nothing at the machine changes.
- P3 [major · material_response]
  - expect: The can and the clamp are rigid; the blur is motion, not a change of shape.
  - fail: The can bends or crumples; or stretches taller; or the clamp arms flex like rubber.
- P4 [major · gravity_direction]
  - expect: The can is held by the clamp; if the clamp opens the can drops.
  - fail: The clamp opens and the can hangs in place; or the can rises out of the clamp; or the machine lifts off the floor.
- P5 [fatal · permanence_count]
  - expect: One can, one machine; the can does not pass through the clamp.
  - fail: A second can appears; or the can vanishes; or passes through the clamp; or the machine changes shape.
- P6 [minor · attribute_drift]
  - expect: The can's label, the machine's colour and the shelves behind stay the same.
  - fail: The can's label changes; or the machine changes colour; or the shelves behind change.

## ACOU-0072 · source_motion · train

**Caption.** Grains of rice lie on the head of a banjo; a string is plucked and the grains jump.

**Expectation (hidden).** The grains are still until the pluck, jump at the pluck and settle as the note fades; they do not move before the string is plucked.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A banjo with grains of rice lying on its head.
- S2 [core] A string is plucked.
- S3 [core] The grains jump.
- S4 [minor] A single string is plucked once.
- S5 [minor] The pluck comes first and the jump follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The grains lie still until the string is plucked and jump at the pluck.
  - fail: Grains hop before the string is plucked; or jump with the hand nowhere near the strings; or the string is plucked and the grains lie dead still.
- P2 [core · process_direction]
  - expect: The hop is largest at the pluck and dies down until the grains lie still.
  - fail: The grains keep hopping at the same height for the whole clip; or hop higher and higher after the pluck; or settle and start again with no second pluck.
- P3 [major · gravity_direction]
  - expect: Grains that jump come back down onto the head or fall off its edge.
  - fail: Grains hang in the air; or float upward; or leave the head and come back up onto it.
- P4 [major · material_response]
  - expect: The string springs back after the pluck, the head flexes as a skin and the grains stay separate.
  - fail: The string is pulled far out and stays bent after release; or the head tears; or the grains merge into a lump or flow like liquid.
- P5 [fatal · permanence_count]
  - expect: The grains keep their number, allowing for some falling off; the strings keep their count; the banjo keeps its shape.
  - fail: Grains appear from nowhere; or all the grains vanish at once; or the strings change count; or the banjo changes shape.
- P6 [minor · attribute_drift]
  - expect: The banjo's finish, the head's colour and the strings stay the same.
  - fail: The banjo changes colour; or the head changes texture; or the strings change colour.

**Note.** The plucking hand is a trigger and is not judged.

## ACOU-0073 · source_motion · train

**Caption.** A dental drill is switched on and held up, and its tip becomes a blur.

**Expectation (hidden).** The tip is sharp before the drill starts and blurs only while it runs.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A dental drill is held up.
- S2 [core] It is switched on.
- S3 [core] Its tip becomes a blur.
- S4 [minor] The tip is sharp before the switch-on.
- S5 [minor] The switch-on comes first and the blur follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The blur is at the tip only; the handpiece stays sharp and the blur does not appear before the switch.
  - fail: The tip blurs before the switch; or the whole handpiece blurs while the hand holding it is sharp; or the tip wanders about on its own away from the handpiece.
- P2 [core · missing_consequence]
  - expect: Once on, the tip blurs and stays blurred while the drill runs; once off, it is sharp.
  - fail: The switch is pressed and the tip stays sharp for the rest of the clip; or the drill is switched off and the blur remains unchanged; or the blur flickers on and off while nothing at the switch changes.
- P3 [major · material_response]
  - expect: The handpiece is rigid and the tip stays attached and straight.
  - fail: The handpiece bends; or the tip stretches longer; or the tip flops like rubber.
- P4 [major · gravity_direction] (if: A hose or cord is attached to the drill.)
  - expect: A hose or cord attached to the drill hangs downward from it.
  - fail: The hose arcs upward and stays; or floats; or hangs rigid sideways.
- P5 [fatal · permanence_count]
  - expect: One drill with one tip; nothing duplicates or vanishes.
  - fail: The tip vanishes; or a second drill appears; or the tip passes through the handpiece; or the drill turns into another object.
- P6 [minor · attribute_drift]
  - expect: The handpiece's colour, the tip's shape when still and the background stay the same.
  - fail: The handpiece changes colour; or the background changes; or the tip changes shape when still.

**Note.** The hand holding the drill is a trigger and is not judged.

## ACOU-0074 · source_motion · train

**Caption.** A stand mixer runs on high, and the whole mixer trembles on the counter.

**Expectation (hidden).** The trembling lasts as long as the mixer runs and is strongest at high speed.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A stand mixer stands on a kitchen counter.
- S2 [core] The mixer runs: its beater turns.
- S3 [core] The whole mixer trembles.
- S4 [minor] The speed is high: the beater is a blur or turns fast.
- S5 [minor] The trembling happens while the mixer runs.

**PC**
- P1 [core · causeless_motion]
  - expect: The mixer trembles in place only while the beater turns.
  - fail: The mixer trembles while the beater is plainly still; or slides across the counter in a smooth glide; or keeps trembling after the beater has stopped.
- P2 [core · missing_consequence]
  - expect: While the beater turns, the head and base tremble together.
  - fail: The beater turns at speed and the mixer stands dead still for the whole clip; or the trembling stops while the beater keeps turning at the same speed; or only the bowl trembles while the body is still.
- P3 [major · gravity_direction]
  - expect: The mixer stays on the counter on all its feet.
  - fail: The mixer lifts off; or balances on one foot; or rises.
- P4 [major · material_response]
  - expect: The body, bowl and beater are rigid.
  - fail: The body bends; or the bowl ripples; or the beater stretches.
- P5 [fatal · permanence_count]
  - expect: One mixer; the beater does not pass through the bowl.
  - fail: A second mixer appears; or it vanishes; or the beater passes through the bowl; or the mixer sinks into the counter.
- P6 [minor · attribute_drift]
  - expect: The mixer's colour, the counter pattern and the bowl's colour stay the same.
  - fail: The mixer changes colour; or the counter pattern changes; or the bowl changes colour.

## ACOU-0075 · source_motion · train

**Caption.** A microphone on a stand is tapped, and the mic head jiggles on its clip with each tap.

**Expectation (hidden).** The jiggle begins with each tap and settles before the next; the mic is still without tapping.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A microphone on a stand.
- S2 [core] The microphone is tapped.
- S3 [core] The mic head jiggles on its clip.
- S4 [minor] There are several taps in the clip.
- S5 [minor] Each tap comes before its jiggle.

**PC**
- P1 [core · causeless_motion]
  - expect: The mic is still until tapped and each jiggle begins at a tap.
  - fail: The mic jiggles before the finger touches it; or jiggles with the hand away; or the finger taps and the mic stays dead still.
- P2 [core · process_direction]
  - expect: Each jiggle shrinks after its tap and settles before or as the next tap comes.
  - fail: The jiggle grows after a tap with the hand away; or stops dead in a tilted pose; or the mic keeps jiggling unchanged with no further taps.
- P3 [major · trajectory_momentum]
  - expect: The mic moves away from the finger's push and swings back about its clip.
  - fail: The mic moves toward the tapping finger; or moves in a direction unrelated to the tap; or jumps up out of the clip and settles back.
- P4 [major · material_response]
  - expect: The stand and the mic body are rigid; the clip flexes.
  - fail: The stand bends like rubber; or the mic body flexes; or the cable stretches.
- P5 [fatal · permanence_count]
  - expect: One microphone on one stand; the finger does not pass through the mic.
  - fail: A second microphone appears; or the mic vanishes; or the finger passes through the mic; or the stand changes shape.
- P6 [minor · attribute_drift]
  - expect: The mic's colour, the stand's height and the background stay the same.
  - fail: The mic changes colour; or the stand changes height; or the background changes.

**Note.** The tapping hand is a trigger and is not judged.

## ACOU-0076 · source_motion · train

**Caption.** The figurine on a wind-up music box turns slower and slower as the spring runs down, and finally stops.

**Expectation (hidden).** The turning only slows, never speeds up, easing smoothly to a stop and then staying still; the figurine does not jerk, reverse, or start again after stopping; the mechanism inside need not be visible.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A wind-up music box with a figurine on it.
- S2 [core] The figurine turns.
- S3 [core] It slows down.
- S4 [core] It stops.
- S5 [minor] The slowing is gradual over the clip.
- S6 [minor] Turning, slowing and stopping happen in that order.

**PC**
- P1 [core · process_direction]
  - expect: The turning only slows, never speeds up, eases to a stop and then stays still.
  - fail: The figurine speeds up; or stops and starts again; or reverses direction; or jerks forward in steps.
- P2 [core · causeless_motion]
  - expect: The figurine turns about a fixed axis on the box, and the box stays still.
  - fail: The figurine drifts across the box top; or the box slides; or the figurine's base separates from the box.
- P3 [major · gravity_direction]
  - expect: The figurine stands upright on its stand and the box rests on its surface.
  - fail: The figurine floats up; or leans and hangs with nothing holding it; or the box lifts.
- P4 [major · material_response]
  - expect: The figurine is rigid and holds its pose while turning.
  - fail: The figurine's arms or skirt change pose while turning; or it stretches; or the box lid bends.
- P5 [fatal · permanence_count]
  - expect: One figurine, one box; nothing passes into the box.
  - fail: A second figurine appears; or the figurine vanishes; or sinks into the box; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The figurine's colour and the box's decoration stay the same.
  - fail: The figurine changes colour; or the box's pattern changes; or the box changes colour.

**Note.** The spring and mechanism are inside the box and need not be visible; the slowing is judged on the figurine alone.

## ACOU-0101 · struck_vibration · eval

**Caption.** A large temple bell is struck once with its wooden beam, and a small pebble resting on the bell's shoulder skitters and slides off.

**Expectation (hidden).** The pebble is still before the strike, jumps and slides at the instant of the blow, and falls off or comes to rest lower down; the bell sways slightly on its hanger; the pebble does not move on its own.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A large temple bell with a small pebble resting on its shoulder.
- S2 [core] The bell is struck once with its wooden beam.
- S3 [core] The pebble skitters and slides off the bell.
- S4 [minor] The strike is a single blow.
- S5 [minor] The strike comes first and the pebble moves after.

**PC**
- P1 [core · causeless_motion]
  - expect: The pebble is still until the beam lands and moves at the blow.
  - fail: The pebble skitters before the beam reaches the bell; or moves with the beam hanging away; or the beam lands and the pebble stays put.
- P2 [core · missing_consequence]
  - expect: The blow sends the pebble off the bell: it leaves its spot and comes to rest lower down or on the ground, and does not return.
  - fail: The pebble hops and settles back in its exact spot on the shoulder; or slides off and then climbs back onto the bell; or comes to rest higher on the bell than where it started.
- P3 [major · gravity_direction]
  - expect: The pebble slides down the bell's curve and falls to the ground.
  - fail: The pebble slides upward toward the crown; or hangs in the air beside the bell; or floats away sideways.
- P4 [major · material_response]
  - expect: The bell is rigid and sways as a whole; the beam rebounds; the pebble is rigid.
  - fail: The beam sinks into the bell; or the bell's wall dents and springs back like rubber; or the pebble squashes.
- P5 [fatal · permanence_count]
  - expect: One bell, one beam, one pebble; the beam does not pass through the bell.
  - fail: A second pebble appears; or the pebble vanishes in mid-slide; or the beam passes through the bell; or the bell changes shape.
- P6 [minor · attribute_drift]
  - expect: The bell's colour and inscriptions, the beam and the surroundings stay the same.
  - fail: The bell changes colour or its inscriptions change; or the beam changes length; or the surroundings change.

**Note.** Whoever swings the beam is a trigger and is not judged.

## ACOU-0102 · struck_vibration · eval

**Caption.** A metal bucket half full of water is struck once with a stick, and the water inside jumps into ripples.

**Expectation (hidden).** The ripples appear at the strike, spread and fade within a second or two; the surface is still before and after; the water does not slosh as if the bucket had been tipped.

**Declared violation types.** missing_consequence, causeless_motion

**SA**
- S1 [core] A metal bucket half full of water.
- S2 [core] A stick strikes the bucket once.
- S3 [core] The water surface jumps into ripples.
- S4 [minor] The strike is a single hit.
- S5 [minor] The strike comes first and the ripples follow.

**PC**
- P1 [core · causeless_motion]
  - expect: The surface is still until the strike and the ripples begin at it.
  - fail: Ripples run over the surface before the stick lands; or appear with the stick held away; or the stick lands and the surface stays glassy.
- P2 [core · missing_consequence]
  - expect: The ripples are a fine shiver over the whole surface that fades; the water does not slosh.
  - fail: The water sloshes up one side as if the bucket had been tipped; or a single ring spreads from the centre as if something had been dropped in; or the ripples grow stronger after the strike; or the water leaps out of the bucket.
- P3 [major · gravity_direction]
  - expect: The water stays level in the bucket and any drops fall back.
  - fail: Water rises out of the bucket; or the surface stays tilted; or the bucket lifts.
- P4 [major · material_response]
  - expect: The bucket is rigid metal and the stick rebounds from it.
  - fail: The stick sinks into the bucket wall; or the bucket crumples like paper; or the bucket wall ripples like cloth.
- P5 [fatal · permanence_count]
  - expect: One bucket, one stick; the water keeps its amount.
  - fail: A second bucket appears; or the stick passes through the bucket; or the water vanishes; or the bucket changes shape.
- P6 [minor · attribute_drift]
  - expect: The bucket's colour, the water's colour and the stick stay the same.
  - fail: The bucket changes colour; or the water changes colour; or the stick changes length.

**Note.** The hand on the stick is a trigger and is not judged.

## ACOU-0103 · struck_vibration · eval

**Caption.** A wok with a scattering of sesame seeds in it is struck once with a ladle, and the seeds jump.

**Expectation (hidden).** The seeds leap at the instant of the blow and settle again; they are still before it; the wok itself does not tip or slide.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A wok with a scattering of sesame seeds in it.
- S2 [core] A ladle strikes the wok once.
- S3 [core] The seeds jump.
- S4 [minor] The strike is a single hit.
- S5 [minor] The strike comes first and the jump follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The seeds are still until the ladle hits the wok.
  - fail: Seeds hop before the ladle reaches the wok; or jump with the ladle held away; or the ladle lands and the seeds stay still.
- P2 [core · missing_consequence]
  - expect: The seeds leap at the blow and settle in new places; the wok stays seated, rocking a little at most.
  - fail: The wok tips over or slides across the stove at the tap; or the seeds settle back into their exact previous arrangement; or the seeds keep hopping unchanged to the end of the clip.
- P3 [major · gravity_direction]
  - expect: Seeds fall back into the wok or over its rim.
  - fail: Seeds hang in the air; or float up; or seeds that left the wok come back up into it.
- P4 [major · material_response]
  - expect: The wok is rigid, the ladle rebounds and the seeds stay separate.
  - fail: The ladle sinks into the wok; or the wok ripples like cloth; or the seeds merge into a paste.
- P5 [fatal · permanence_count]
  - expect: The seeds keep their number, allowing for some leaving the wok; one wok, one ladle.
  - fail: Seeds appear from nowhere; or all the seeds vanish at once; or the ladle passes through the wok; or the wok changes shape.
- P6 [minor · attribute_drift]
  - expect: The wok's colour, the stove and the seeds' colour stay the same.
  - fail: The wok changes colour; or the stove changes; or the seeds change colour.

**Note.** The hand on the ladle is a trigger and is not judged.

## ACOU-0104 · struck_vibration · eval

**Caption.** A large hanging sheet of thin steel is struck once with a mallet, and waves ripple visibly across the metal as it booms.

**Expectation (hidden).** The ripples spread from the point of impact across the sheet and fade over a few seconds; the sheet is flat and still before the strike and does not keep waving after the sound dies.

**Declared violation types.** missing_consequence, process_direction

**SA**
- S1 [core] A large thin steel sheet hangs.
- S2 [core] A mallet strikes it once.
- S3 [core] Waves ripple across the metal.
- S4 [minor] The strike is a single hit.
- S5 [minor] The strike comes first and the ripples follow.

**PC**
- P1 [core · missing_consequence]
  - expect: Ripples spread out from the point of impact across the sheet.
  - fail: The mallet lands and the sheet hangs flat and still; or the waves start at the far edge and travel toward the impact point; or the sheet ripples while the mallet is held away.
- P2 [core · process_direction]
  - expect: The ripples are strongest just after the strike and fade until the sheet hangs flat; they do not grow or restart.
  - fail: The waves grow after the strike; or the sheet keeps waving unchanged to the end; or it goes flat and then starts waving again with no second strike; or it freezes in a bent shape.
- P3 [major · gravity_direction]
  - expect: The sheet hangs from its top and returns to hanging straight after any sway.
  - fail: The sheet rises on its hanger; or hangs at an angle with nothing touching it; or its bottom edge lifts and stays out.
- P4 [major · material_response]
  - expect: The thin steel flexes as a sheet and the mallet rebounds from it.
  - fail: The mallet sinks into the sheet; or the sheet tears; or it crumples like foil and stays crumpled.
- P5 [fatal · permanence_count]
  - expect: One sheet, one mallet; the mallet does not pass through the sheet.
  - fail: A second sheet appears; or the mallet passes through the sheet; or the sheet vanishes; or splits into two.
- P6 [minor · attribute_drift]
  - expect: The sheet's colour, the hanger and the mallet stay the same.
  - fail: The sheet changes colour; or the hanger changes; or the mallet's head changes size.

**Note.** The hand on the mallet is a trigger and is not judged.

## ACOU-0105 · struck_vibration · eval

**Caption.** A struck tuning fork is touched to the corner of a sheet of paper lying on a table, and the paper buzzes and skitters.

**Expectation (hidden).** The paper jitters only while the fork touches it and stops when the fork is lifted; an unstruck fork touching it does nothing.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A sheet of paper lies on a table.
- S2 [core] A tuning fork is touched to a corner of the paper.
- S3 [core] The paper buzzes and skitters: it shivers and shifts.
- S4 [minor] The fork is shown being struck, or its prongs show a blur.
- S5 [minor] The touch comes first and the buzzing follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The paper is still until the prongs touch it, moves only during contact and stops when the fork is lifted.
  - fail: The paper skitters before the fork touches it; or moves while the fork is held away; or keeps skittering after the fork is lifted.
- P2 [core · missing_consequence]
  - expect: While the prongs touch, the paper shivers and creeps, most at the touched corner.
  - fail: The prongs rest on the corner for a spell and the paper lies dead still; or the far edge dances while the touched corner stays pinned; or the paper is flung across the table in one leap.
- P3 [major · gravity_direction]
  - expect: The paper stays flat on the table.
  - fail: The paper lifts off the table and floats; or stands up on edge; or rises.
- P4 [major · material_response]
  - expect: The paper flexes as paper and the fork is rigid.
  - fail: The paper tears where the prongs touch; or the prongs bend; or the paper stretches.
- P5 [fatal · permanence_count]
  - expect: One sheet, one fork; the prongs do not pass through the paper.
  - fail: A second sheet appears; or the paper vanishes; or the prongs pass through the paper into the table; or the fork changes shape.
- P6 [minor · attribute_drift]
  - expect: The paper's markings, the table and the fork's size stay the same.
  - fail: The paper's markings change; or the table changes; or the fork changes size.

**Note.** The hand holding the fork is a trigger and is not judged.

## ACOU-0106 · struck_vibration · eval

**Caption.** A ping-pong ball rests on the head of a drum; the drum is struck once and the ball bounces high off the head.

**Expectation (hidden).** The ball leaves the head at the instant of the strike, rises and falls back, bouncing lower each time; it is still before the strike and does not rise before the stick lands.

**Declared violation types.** causeless_motion, trajectory_momentum

**SA**
- S1 [core] A ping-pong ball rests on the head of a drum.
- S2 [core] The drum is struck once.
- S3 [core] The ball bounces off the head.
- S4 [minor] The bounce is high.
- S5 [minor] The strike is a single hit.
- S6 [minor] The strike comes first and the bounce follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The ball is still until the strike and leaves the head at the strike.
  - fail: The ball rises before the stick lands; or hops with the stick held away; or the stick lands and the ball stays seated.
- P2 [core · trajectory_momentum]
  - expect: The ball rises, falls back and bounces lower each time in near-vertical arcs.
  - fail: The ball rises and hangs; or bounces higher on a later bounce with no second strike; or changes direction in mid-air; or stops dead at the top of its arc.
- P3 [major · gravity_direction]
  - expect: The ball comes back down onto the head or falls off the drum.
  - fail: The ball floats upward out of view; or drifts sideways at a steady height; or comes to rest in the air.
- P4 [major · material_response]
  - expect: The head flexes as a skin, the stick rebounds and the ball stays round.
  - fail: The stick sinks into the head; or the ball squashes flat and stays so; or the head tears.
- P5 [fatal · permanence_count]
  - expect: One ball, one drum, one stick; the stick does not pass through the head.
  - fail: A second ball appears; or the ball vanishes in mid-air; or the stick passes through the head; or the drum changes shape.
- P6 [minor · attribute_drift]
  - expect: The ball's colour and size, the drum's shell and the stick stay the same.
  - fail: The ball changes colour or size; or the drum changes colour; or the stick changes length.

## ACOU-0107 · struck_vibration · eval

**Caption.** A pinch of chalk dust lies on a large cymbal; the cymbal is struck once and the dust flies up in a puff.

**Expectation (hidden).** The dust lifts off at the instant of the strike, hangs and drifts down; the cymbal wobbles on its stand; the dust does not move before the blow.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A large cymbal with a pinch of chalk dust on it.
- S2 [core] The cymbal is struck once.
- S3 [core] The dust flies up in a puff.
- S4 [minor] The strike is a single hit.
- S5 [minor] The strike comes first and the puff follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The dust is still until the strike and lifts at the blow.
  - fail: Dust lifts before the stick reaches the cymbal; or puffs with the stick held away; or the stick lands and the dust stays put.
- P2 [core · missing_consequence]
  - expect: The blow lifts the dust and sets the cymbal wobbling on its stand; the dust then drifts down.
  - fail: The stick lands, the dust flies and the cymbal stays perfectly rigid with no wobble; or the dust settles back into its exact original pinch; or the dust puffs up and is then drawn back down onto the cymbal into a heap.
- P3 [major · gravity_direction]
  - expect: The dust cloud drifts and sinks.
  - fail: The dust cloud rises steadily out of view like smoke; or hangs frozen in the air; or falls as a solid lump.
- P4 [major · material_response]
  - expect: The cymbal is a rigid disc and the stick rebounds from it.
  - fail: The stick sinks into the cymbal; or the cymbal ripples like cloth; or bends and stays bent.
- P5 [fatal · permanence_count]
  - expect: One cymbal, one stick; the stick does not pass through the cymbal.
  - fail: A second cymbal appears; or the stick passes through the cymbal; or the cymbal vanishes; or the dust turns into a solid object.
- P6 [minor · attribute_drift]
  - expect: The cymbal's colour, the stand and the dust's colour stay the same.
  - fail: The cymbal changes colour; or the stand changes; or the dust changes colour.

## ACOU-0108 · sound_driven_vibration · eval

**Caption.** A sheet of paper lies loosely over the grille of a large speaker, and it lifts and flaps with each beat of the bass.

**Expectation (hidden).** The paper jumps in time with the beats and lies still between them and when the music stops; it does not move to sound that has no bass.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A sheet of paper lies over the grille of a large speaker.
- S2 [core] The paper lifts and flaps.
- S3 [minor] The flapping comes in beats: repeated lifts with still spells between.
- S4 [minor] The paper stays on the speaker.
- S5 [minor] The speaker is large.

**PC**
- P1 [core · causeless_motion]
  - expect: The paper lifts from the grille and falls back; it does not slide steadily or float off.
  - fail: The paper slides steadily off the grille in one direction with no flap; or floats up and hangs; or flaps while lying on the floor away from the speaker; or its edges flutter as in a draught while the middle never lifts.
- P2 [core · missing_consequence]
  - expect: Each lift is followed by the paper settling back onto the grille; between lifts it lies flat.
  - fail: The paper stays lifted in a hump and never settles; or is flat in one frame and airborne in the next and never comes down; or the lifts go on at the same rhythm after the paper has slid clear of the grille.
- P3 [major · gravity_direction]
  - expect: The paper falls back after each lift.
  - fail: The paper hangs in the air above the grille; or rises steadily out of view; or climbs up the wall behind.
- P4 [major · material_response]
  - expect: The paper flexes as paper and the speaker is rigid.
  - fail: The paper stays rigid like a board while lifting; or the speaker cabinet flexes; or the paper tears with nothing touching it.
- P5 [fatal · permanence_count]
  - expect: One sheet, one speaker; the paper does not pass into the speaker.
  - fail: A second sheet appears; or the paper vanishes; or passes into the speaker; or the speaker changes shape.
- P6 [minor · attribute_drift]
  - expect: The paper's markings, the speaker's colour and the room stay the same.
  - fail: The paper's markings change; or the speaker changes colour; or the room changes.

## ACOU-0109 · sound_driven_vibration · eval

**Caption.** A garbage truck idles outside a house, and a hanging wind chime by the door trembles and tinkles while the engine runs.

**Expectation (hidden).** The trembling lasts while the truck idles and stops after it drives away; the chime is still in quiet air.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A wind chime hangs by a house door.
- S2 [core] A garbage truck stands outside, stationary.
- S3 [core] The chime trembles.
- S4 [minor] The truck is stationary while the chime trembles.
- S5 [minor] The tubes tremble rather than swinging in wide arcs.

**PC**
- P1 [core · missing_consequence] (if: The truck is in view at some point.)
  - expect: The chime trembles while the truck stands idling and stops after it drives away.
  - fail: The truck idles in view and the chime hangs dead still; or the chime trembles hardest after the truck has driven off; or the chime starts trembling only as the truck disappears.
- P2 [core · causeless_motion]
  - expect: The tubes tremble on taut strings hanging from the chime's top; the chime stays on its hook.
  - fail: The tubes rise on slack strings; or the whole chime slides along its hook; or the tubes drift apart from the chime's centre and hang there; or the tubes swing in wide arcs and stop dead.
- P3 [major · gravity_direction]
  - expect: At rest the tubes hang straight down.
  - fail: Tubes rest tilted with nothing touching them; or rise above the top plate; or hang sideways on taut strings.
- P4 [major · material_response]
  - expect: The tubes are rigid and the strings flex.
  - fail: The tubes bend; or the strings stretch; or the top plate flexes like rubber.
- P5 [fatal · permanence_count]
  - expect: One chime whose tubes keep their count; one truck; nothing passes through the door frame.
  - fail: A tube appears or vanishes; or two tubes merge; or the chime passes through the door frame; or the truck vanishes in one frame.
- P6 [minor · attribute_drift]
  - expect: The chime's colour, the door and the truck's colour stay the same.
  - fail: The chime changes colour; or the door changes; or the truck changes colour.

**Note.** The engine cannot be seen running; if the truck is not in view, the trembling alone is not a violation.

## ACOU-0110 · sound_driven_vibration · eval

**Caption.** A heavy book is dropped flat onto a table, and a pencil lying nearby rolls a little while a glass of water shows a ring of ripples.

**Expectation (hidden).** The pencil moves and the ripples appear at the instant of the impact and settle within a second or two; nothing moves before the book lands.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A table with a pencil and a glass of water on it.
- S2 [core] A heavy book is dropped flat onto the table.
- S3 [core] The pencil rolls a little.
- S4 [core] The glass of water shows a ring of ripples.
- S5 [minor] The book lands flat.
- S6 [minor] The book lands first; the pencil and the ripples follow.

**PC**
- P1 [core · causeless_motion]
  - expect: The pencil and the water are still until the book lands and both move at the impact.
  - fail: The pencil rolls before the book lands; or the ripples appear with the book still in the air; or the book lands and both the pencil and the water stay still.
- P2 [core · missing_consequence]
  - expect: The impact moves both: the pencil rolls a short way and stops; the ripple ring appears and fades.
  - fail: The pencil rolls on without stopping across the whole table; or rolls toward the book and climbs onto it; or the ripples grow stronger after the impact; or the water sloshes up the side as if the glass were shoved.
- P3 [major · gravity_direction]
  - expect: The book falls down, lands and stays; the pencil stays on the table.
  - fail: The book hangs in the air before landing; or lands and then rises again; or the pencil lifts off the table.
- P4 [major · material_response]
  - expect: The table, glass and pencil are rigid; the book is a flat rigid slab whose pages may flap.
  - fail: The table top ripples like water; or the glass wobbles like rubber; or the pencil bends; or the book splashes like a liquid.
- P5 [fatal · permanence_count]
  - expect: One book, one pencil, one glass; nothing passes into the table.
  - fail: A second pencil appears; or the glass vanishes; or the book passes into the table; or the pencil passes through the glass.
- P6 [minor · attribute_drift]
  - expect: The book's cover, the pencil's colour and length and the table pattern stay the same.
  - fail: The book's cover changes; or the pencil changes colour or length; or the table pattern changes.

**Note.** The hand that drops the book is a trigger and is not judged.

## ACOU-0111 · sound_driven_vibration · eval

**Caption.** A tuba is played next to a table where a row of dominoes stands on end, and the dominoes shiver on the low notes and one topples.

**Expectation (hidden).** The shivering appears with the low notes and stops between them; the topple happens during a note, and once a domino is down it stays down.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A tuba is played next to a table.
- S2 [core] A row of dominoes stands on end on the table.
- S3 [core] The dominoes shiver.
- S4 [core] One domino topples.
- S5 [minor] The shivering comes in spells with still spells between.
- S6 [minor] The shiver comes first and the topple happens during it.

**PC**
- P1 [core · causeless_motion]
  - expect: The dominoes stand still except during shiver spells; the topple happens during a shiver; the row does not slide as a body.
  - fail: The whole row slides along the table as one; or a domino topples while the row is dead still with no shiver; or dominoes hop into the air.
- P2 [core · missing_consequence]
  - expect: Shiver spells come while the tuba is blown; once a domino is down it stays down.
  - fail: The player blows for a spell and the dominoes stand frozen throughout; or a fallen domino stands back up; or a falling domino stops leaning in mid-fall and stays; or the dominoes shiver only while the player is plainly not blowing.
- P3 [major · gravity_direction]
  - expect: The toppled domino falls flat onto the table toward the side it leans.
  - fail: The domino falls upward; or hangs at an angle unsupported; or falls and rises again.
- P4 [major · material_response]
  - expect: The dominoes, the table and the tuba are rigid.
  - fail: A domino bends; or the table ripples; or the tuba's bell flexes like rubber.
- P5 [fatal · permanence_count]
  - expect: The dominoes keep their count; one tuba; no domino passes through another.
  - fail: A domino appears or vanishes; or two dominoes merge; or a domino passes through another; or the tuba changes shape.
- P6 [minor · attribute_drift]
  - expect: The dominoes' pips, the table and the tuba's colour stay the same.
  - fail: The dominoes' pips change; or the table changes; or the tuba changes colour.

**Note.** The player is kept as the source of the notes; playing technique is not judged.

## ACOU-0112 · sound_driven_vibration · eval

**Caption.** A cement mixer rumbles beside a garden wall, and pebbles on the wall's top shiver and shift.

**Expectation (hidden).** The pebbles move only while the mixer runs and settle when it stops.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A cement mixer beside a garden wall.
- S2 [core] Pebbles lie on top of the wall.
- S3 [core] The pebbles shiver and shift.
- S4 [minor] The mixer is running: its drum turns.
- S5 [minor] The pebbles stay on the wall.

**PC**
- P1 [core · causeless_motion]
  - expect: The pebbles move only while the drum turns and are still when it is stopped.
  - fail: Pebbles shift while the drum is plainly still; or keep shifting after the drum has stopped; or slide along the wall in one smooth glide.
- P2 [core · missing_consequence]
  - expect: While the mixer runs, the pebbles tremble and end up in a new arrangement.
  - fail: The drum turns for the whole clip and the pebbles sit frozen; or the pebbles return to their exact starting spots after moving; or pebbles far from the mixer shift while those nearest it sit still.
- P3 [major · gravity_direction]
  - expect: Pebbles stay on the wall top; any that leave it fall.
  - fail: A pebble hovers; or rises; or a pebble that leaves the wall floats sideways.
- P4 [major · material_response]
  - expect: The pebbles and the wall are rigid; the drum turns on its frame.
  - fail: The wall ripples; or pebbles squash; or the drum wobbles off its frame and stays there.
- P5 [fatal · permanence_count]
  - expect: The pebbles keep their count; one mixer; nothing passes into the wall.
  - fail: Pebbles appear from nowhere; or vanish; or sink into the wall; or the mixer duplicates.
- P6 [minor · attribute_drift]
  - expect: The mixer's colour, the wall's stones and the pebbles' colour stay the same.
  - fail: The mixer changes colour; or the wall's stones change; or the pebbles change colour.

## ACOU-0113 · sound_driven_vibration · eval

**Caption.** A church organ plays a deep pedal note, and the still water in the stone font nearby breaks into fine ripples.

**Expectation (hidden).** The ripples appear when the low note sounds, cover the water surface evenly, and fade within a moment of the note ending; the water is flat before the note and between notes.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A stone font holding water, in a church.
- S2 [core] The water surface breaks into fine ripples.
- S3 [minor] The ripples cover the surface evenly.
- S4 [minor] The water is flat at first and the ripples begin during the clip.
- S5 [minor] An organ is in view: its pipes, console or player.

**PC**
- P1 [core · causeless_motion]
  - expect: The ripples are a fine even shiver; the water stays level in the font.
  - fail: The water sloshes to one side; or a single ring spreads from a point as if something were dropped in; or the water surface tilts; or the water rises into a bulge.
- P2 [core · missing_consequence] (if: The organist is in view at the console.)
  - expect: Ripples appear while the organist holds a pedal or key and fade when the hands and feet lift.
  - fail: The organist's foot holds a pedal and the water stays glassy; or the water ripples while the organist sits with hands and feet off the keys; or the ripples begin before the organist plays.
- P3 [major · gravity_direction]
  - expect: The water stays in the font with a level surface.
  - fail: Water rises out of the font; or hangs in the air; or the surface stays tilted.
- P4 [major · material_response]
  - expect: The font is rigid stone and the water stays liquid.
  - fail: The font's stone ripples; or the water's surface cracks like ice; or the font bends.
- P5 [fatal · permanence_count]
  - expect: One font; the water keeps its amount; nothing passes through the stone.
  - fail: A second font appears; or the water vanishes; or the font changes shape; or water passes through the font's side.
- P6 [minor · attribute_drift]
  - expect: The font's carvings, the church background and the water's colour stay the same.
  - fail: The font's carvings change; or the church background changes; or the water changes colour.

**Note.** Organ pipes do not show sound; if no organist is in view, the ripples alone are not a violation.

## ACOU-0114 · sound_driven_vibration · eval

**Caption.** A heavy freight train passes a level crossing, and the coins in a cup holder of a waiting car rattle.

**Expectation (hidden).** The rattling starts as the train arrives, is strongest as it passes, and stops once it has gone.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] Inside a car waiting at a level crossing: a cup holder with coins in it.
- S2 [core] A freight train passes the crossing, seen through the windows.
- S3 [core] The coins rattle.
- S4 [minor] The car is stationary.
- S5 [minor] The train approaches, the coins rattle, the train passes, the coins settle.

**PC**
- P1 [core · missing_consequence] (if: The train is visible through the windows.)
  - expect: The rattling starts as the train arrives, is strongest as it passes and stops after it has gone.
  - fail: The train passes in view and the coins lie dead still; or the coins rattle hardest after the train has gone; or the coins are still throughout the pass and start rattling once the train is out of view.
- P2 [core · causeless_motion]
  - expect: The coins tremble in the holder; they do not leap out or slide as a group.
  - fail: The coins leap out of the holder; or slide up the holder's side in one glide and hang there; or the holder itself moves in the dashboard; or the coins rattle unchanged with the outside scene still and empty.
- P3 [major · gravity_direction]
  - expect: The coins stay at the bottom of the holder, hopping and falling back.
  - fail: Coins hang in the air; or rise out of the holder; or stick to the holder's wall above the pile.
- P4 [major · material_response]
  - expect: The coins and the dashboard are rigid.
  - fail: Coins bend; or the dashboard ripples; or the holder flexes like rubber.
- P5 [fatal · permanence_count]
  - expect: The coins keep their count; one continuous train; nothing passes through the barrier.
  - fail: Coins appear from nowhere; or vanish; or the train's wagons appear or vanish mid-train; or the train passes through the barrier.
- P6 [minor · attribute_drift]
  - expect: The coins' faces and sizes, the dashboard and the window view stay the same apart from the train.
  - fail: The coins change size or face; or the dashboard changes; or the window view changes to a different scene.

## ACOU-0115 · source_motion · eval

**Caption.** A motorcycle idles at a kerb, and its rear-view mirror blurs and the reflection in it shakes until the engine is switched off.

**Expectation (hidden).** The blur and shaking last exactly as long as the engine runs and stop within a moment of it being cut; the mirror is sharp before the engine starts.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A motorcycle stands at a kerb with a rear-view mirror in view.
- S2 [core] The mirror blurs and the reflection in it shakes.
- S3 [core] The engine is switched off: a key or switch is worked, or the shaking stops.
- S4 [minor] The bike stays at the kerb.
- S5 [minor] The mirror shakes first, the engine is switched off, and the shaking stops.

**PC**
- P1 [core · causeless_motion]
  - expect: The mirror shakes only while the engine runs and is sharp after the engine is cut.
  - fail: The mirror shakes after the engine has been switched off and the bike stands still; or the mirror is blurred while the rest of the bike shows no tremble at all; or the blur comes and goes while nothing changes at the engine.
- P2 [core · missing_consequence]
  - expect: The housing's tremble carries into the reflection: the image jitters with the housing and steadies once the engine cuts.
  - fail: The mirror housing trembles while the reflection inside stays rock steady; or the reflection jitters while the housing is sharp and still; or the switch is worked and the blur continues unchanged to the end.
- P3 [major · gravity_direction]
  - expect: The bike rests on its stand or wheels.
  - fail: The bike lifts; or leans past its stand and hangs; or rises.
- P4 [major · material_response]
  - expect: The mirror and its stalk are rigid; the blur is motion, not a change of shape.
  - fail: The mirror stalk bends like rubber; or the mirror glass bulges; or the housing stretches.
- P5 [fatal · permanence_count]
  - expect: One bike; the mirrors keep their count and stay attached.
  - fail: A second mirror appears; or the mirror vanishes; or the mirror detaches and hangs in the air; or the bike changes shape.
- P6 [minor · attribute_drift]
  - expect: The bike's colour, the kerb and the mirror's shape stay the same.
  - fail: The bike changes colour; or the kerb changes; or the mirror changes shape.

**Note.** What the reflection shows is not judged; only whether it jitters together with the housing. The rider is a trigger.

## ACOU-0116 · source_motion · eval

**Caption.** A large brass singing bowl half full of water is rubbed around its rim with a mallet, and as it sings the water surface breaks into ripples and leaping droplets.

**Expectation (hidden).** The ripples and droplets appear only while the rim is being rubbed and die away when the mallet stops; the water is flat before; the bowl does not tip or spill.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A brass singing bowl half full of water.
- S2 [core] A mallet is rubbed around the bowl's rim.
- S3 [core] The water surface breaks into ripples.
- S4 [core] Droplets leap from the surface.
- S5 [minor] The mallet moves around the rim rather than tapping it.
- S6 [minor] The rubbing comes first; the ripples and droplets follow.

**PC**
- P1 [core · causeless_motion]
  - expect: The water is flat until the mallet moves on the rim; ripples and droplets appear only while it moves and die away when it stops.
  - fail: Ripples or droplets appear before the mallet touches the rim; or appear with the mallet held away; or the mallet circles the rim and the water stays glassy; or the droplets keep leaping well after the mallet has stopped.
- P2 [core · missing_consequence]
  - expect: The ripples form a fine pattern across the surface with droplets leaping up from it and falling back; the bowl stays put and does not spill.
  - fail: The bowl tips or slides while being rubbed; or the water sloshes up one side and spills over; or droplets rise from a single spot while the rest of the surface is glassy; or a single ring spreads from the centre as if something were dropped in.
- P3 [major · gravity_direction]
  - expect: Droplets fall back into the bowl or onto the table.
  - fail: Droplets hang in the air; or rise out of view; or droplets that left the bowl come back up into it.
- P4 [major · material_response]
  - expect: The brass bowl and the mallet are rigid.
  - fail: The bowl's wall ripples like cloth; or the mallet bends; or the bowl dents under the mallet.
- P5 [fatal · permanence_count]
  - expect: One bowl, one mallet; the water keeps its amount.
  - fail: A second bowl appears; or the mallet passes through the bowl wall; or the water vanishes; or the bowl changes shape.
- P6 [minor · attribute_drift]
  - expect: The bowl's colour and engraving, the mallet and the table stay the same.
  - fail: The bowl changes colour or its engraving changes; or the mallet changes length; or the table changes.

**Note.** The hand on the mallet is a trigger and is not judged.

## ACOU-0117 · source_motion · eval

**Caption.** A mechanical metronome is set going, and its pendulum swings from side to side with each tick.

**Expectation (hidden).** The pendulum swings steadily, reversing at each tick, and slows to a stop only when the metronome is stopped; it does not swing before it is started.

**Declared violation types.** causeless_motion, process_direction

**SA**
- S1 [core] A mechanical metronome.
- S2 [core] It is set going: a hand releases or starts the pendulum.
- S3 [core] The pendulum swings from side to side.
- S4 [minor] The swing is steady and repeated.
- S5 [minor] The start comes first and the swinging follows.

**PC**
- P1 [core · causeless_motion]
  - expect: The pendulum is still before the start, then swings about its pivot at the base while the body stays still.
  - fail: The pendulum swings before it is started; or the body rocks or walks across the table; or the weight slides up or down the rod on its own; or the rod bends mid-swing.
- P2 [core · process_direction]
  - expect: While running, the swing keeps a steady width and reverses at each end.
  - fail: The arcs shrink to a stop with nothing touching the metronome; or grow wider and wider; or the pendulum pauses in mid-swing and then continues; or it stops dead at one side with nothing touching it.
- P3 [major · trajectory_momentum]
  - expect: The pendulum passes the centre at speed and slows toward each end; both sides mirror each other.
  - fail: The pendulum moves in jerks; or jumps from one side to the other without passing the centre; or swings in a circle rather than side to side.
- P4 [major · material_response]
  - expect: The rod, the weight and the body are rigid.
  - fail: The rod bends; or the body flexes; or the weight changes shape.
- P5 [fatal · permanence_count]
  - expect: One metronome with one pendulum; nothing passes through the case.
  - fail: A second pendulum appears; or the pendulum vanishes; or passes through the case; or the metronome turns into another object.
- P6 [minor · attribute_drift]
  - expect: The case's colour, the scale markings and the weight's colour stay the same.
  - fail: The case changes colour; or the scale markings change; or the weight changes colour.

**Note.** The hand that starts it is a trigger and is not judged.

## ACOU-0118 · source_motion · eval

**Caption.** A sewing machine runs at speed, and its needle bar blurs up and down while the table beneath it trembles.

**Expectation (hidden).** The blur and trembling last only while the machine runs and stop when it stops; the needle is sharp when still.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A sewing machine on a table, running.
- S2 [core] The needle bar blurs up and down.
- S3 [core] The table trembles.
- S4 [minor] The speed is high: the needle is a blur.
- S5 [minor] The trembling happens while the needle moves.

**PC**
- P1 [core · causeless_motion]
  - expect: The needle bar moves straight up and down in its housing and the table trembles only while the machine runs.
  - fail: The needle bar wanders sideways out of its housing; or the table trembles while the needle is sharp and still; or the trembling goes on after the machine has stopped.
- P2 [core · missing_consequence]
  - expect: While the needle blurs, the machine body and the table tremble; when the needle stops they are still.
  - fail: The needle blurs at speed and the machine body and table stand dead still; or the needle stops and its blur remains; or the hand wheel is sharp and still while the needle blurs.
- P3 [major · gravity_direction]
  - expect: The machine rests on the table.
  - fail: The machine lifts; or tilts and hangs; or rises.
- P4 [major · material_response]
  - expect: The needle and table are rigid; the blur is motion, not bending.
  - fail: The needle bends; or the table top ripples like water; or the machine body flexes.
- P5 [fatal · permanence_count]
  - expect: One machine with one needle; nothing passes into the table.
  - fail: A second needle appears; or the needle vanishes; or the machine sinks into the table; or turns into another object.
- P6 [minor · attribute_drift]
  - expect: The machine's colour, the table pattern and the thread stay the same.
  - fail: The machine changes colour; or the table pattern changes; or the thread changes colour.

## ACOU-0119 · source_motion · eval

**Caption.** A carillon bell in a tower is struck by its hammer, and the hammer swings back while the bell rocks slightly on its mount.

**Expectation (hidden).** The hammer moves only to strike and retreat; the bell's rocking begins at the strike and dies away; nothing moves before the hammer falls.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] A carillon bell in a tower with a hammer beside it.
- S2 [core] The hammer strikes the bell.
- S3 [core] The hammer swings back after the strike.
- S4 [core] The bell rocks on its mount.
- S5 [minor] The rocking is slight.
- S6 [minor] The strike comes first; the swing back and the rocking follow.

**PC**
- P1 [core · causeless_motion]
  - expect: The bell is still before the hammer lands and rocks only from the strike.
  - fail: The bell rocks before the hammer lands; or rocks while the hammer stays retracted; or starts rocking again after settling with no second strike.
- P2 [core · missing_consequence]
  - expect: The hammer strikes and retreats; the bell rocks at the strike and the rocking dies down.
  - fail: The hammer lands and the bell hangs perfectly rigid; or the hammer stays pressed against the bell after landing; or the bell's rocking grows after the strike; or the hammer swings back before it has reached the bell.
- P3 [major · gravity_direction]
  - expect: The bell hangs below its mount and returns to hanging straight; the hammer returns to its rest.
  - fail: The bell rests tilted with nothing holding it; or rises on its mount; or the hammer hangs in mid-air away from its pivot.
- P4 [major · material_response]
  - expect: The bell and the hammer are rigid.
  - fail: The bell's wall dents; or the hammer bends; or the bell wobbles like rubber.
- P5 [fatal · permanence_count]
  - expect: One bell, one hammer; the hammer does not pass through the bell.
  - fail: A second hammer appears; or the hammer passes through the bell; or the bell vanishes; or the bell splits.
- P6 [minor · attribute_drift]
  - expect: The bell's colour, the tower stones and the hammer's size stay the same.
  - fail: The bell changes colour; or the tower stones change; or the hammer changes size.

## ACOU-0120 · source_motion · eval

**Caption.** The keys of an old typewriter are struck one after another, and with each clack a type bar flies up to hit the paper and the carriage jumps one step sideways.

**Expectation (hidden).** A type bar rises and falls with every keystroke and the carriage moves one notch at the same instant; nothing moves between strokes; the carriage steps in one direction only until it is pushed back.

**Declared violation types.** causeless_motion, missing_consequence

**SA**
- S1 [core] An old typewriter with paper in it.
- S2 [core] Keys are struck one after another.
- S3 [core] A type bar flies up to hit the paper with each keystroke.
- S4 [core] The carriage jumps one step sideways with each stroke.
- S5 [minor] There are several strokes in the clip.
- S6 [minor] Each keystroke comes first; its type bar and carriage step follow.

**PC**
- P1 [core · causeless_motion]
  - expect: The type bars and the carriage move only at keystrokes and are still between them.
  - fail: A type bar rises while no key is pressed; or the carriage moves between strokes; or several type bars rise for one keystroke; or the carriage drifts steadily instead of stepping.
- P2 [core · missing_consequence]
  - expect: Each keystroke sends one type bar up to the paper and back, and the carriage steps once, always in the same direction.
  - fail: A key goes down and no type bar moves; or the type bar rises and stays up; or the carriage steps back and forth alternately; or the carriage stays still while type bars strike.
- P3 [major · gravity_direction]
  - expect: Type bars fall back after striking and the carriage rests on its rails.
  - fail: A type bar hangs in the air; or the carriage lifts off its rails; or the paper floats up.
- P4 [major · material_response]
  - expect: The type bars and keys are rigid; the paper flexes.
  - fail: Type bars bend like rubber; or the paper is punched through by a bar; or keys stretch.
- P5 [fatal · permanence_count]
  - expect: The type bars and keys keep their count; one carriage; nothing passes through the roller.
  - fail: Type bars appear or vanish; or a type bar passes through the paper and the roller; or the carriage duplicates; or the typewriter changes shape.
- P6 [minor · attribute_drift]
  - expect: The typewriter's colour, the key lettering and the paper's size stay the same.
  - fail: The key lettering changes; or the typewriter changes colour; or the paper changes size.

**Note.** The hands on the keys are a trigger and are not judged.

