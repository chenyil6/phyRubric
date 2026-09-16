#!/usr/bin/env python3
"""Build data/drafts/optics_draft.json: proposed rewrites of the Optics train captions.

Same rules as scripts/make_heat_draft.py:
  person      - a human who is only the lit / reflected / shadow-casting subject is replaced by an object,
                animal or vehicle (the physics is identical); a human who only operates something becomes
                passive voice; "X looks through Y" becomes the camera's view through Y.  Hands stay only
                where the hand IS the phenomenon (hand shadows, fingers glowing red, a hand wiping a streak).
  timescale   - rare in optics (most effects are instant); slow fog-clearing is rephrased.
  expectation - only where the caption change requires it (e.g. "her arm" -> "the surface below").
  keep_person - the person is the phenomenon and was left as is.
Captions state the event only; how it should look lives in the expectation.  Notes flag possible
deletions / duplicates for the user's decision; nothing is deleted here.
"""
import json
from pathlib import Path

SRC = Path("/u/hchen56/phyRubric/data/train/optics.json")          # current file (renumbered, partly rewritten)
DST = Path("/u/hchen56/phyRubric/data/drafts/optics_draft.json")
MAP = Path("/u/hchen56/phyRubric/data/optics_id_map.json")          # original id -> current id
ORIG_COMMIT = "b55cde0"                                              # optics.json with the original ids/captions
# Overrides below are keyed by ORIGINAL ids (the ones in the review conversation before renumbering).

DELETE: dict[str, str] = {   # filled in as the user decides
    "OPT-0045": "two lamps + two switches + two walls in 5 s; the physics (shadow falls away from the lit lamp) is already covered by OPT-0004 and OPT-0037",
    "OPT-0050": "hat brim shading a face: contrived once the person is replaced by a statue; the brim shadow adds nothing over OPT-0013 (umbrella) and OPT-0032 (tilted book)",
    "OPT-0141": "second pass (was OPT-0139): glasses only sharpen the view for the wearer; for the camera they blur it, so a correct video cannot show the caption",
    "OPT-0133": "second pass (was OPT-0131): ruler in a rock pool: same waterline-bend effect as the stick in the pond",
    "OPT-0076": "second pass (was OPT-0074): double reflection (small mirror behind a head into a wall mirror) is hard to read in a 5 s clip",
    "OPT-0053": "second pass (was OPT-0051): object into still reflecting water: three items, kept the bicycle wheel in the puddle and the coin in the fountain",
    "OPT-0102": "second pass (was OPT-0100): bent at the waterline: five items, kept straw, spoon in oil, stick in pond",
    "OPT-0115": "second pass (was OPT-0113): bent at the waterline: five items, kept straw, spoon in oil, stick in pond",
    "OPT-0136": "second pass (was OPT-0134): distortion behind a glass of water: three items, kept the line card and the bottle over a sign",
}

O: dict[str, tuple] = {}
def o(i, c=None, e=None, ch=(), note=""):
    O[f"OPT-{i:04d}"] = (c, e, list(ch), note)

# ---------------------------------------------------------------- shadow
o(1, "A wooden puppet hanging in a sunny window lifts one arm as its string is pulled, and its shadow on the wall lifts its arm too.",
     "The shadow's arm moves at the same instant and in the same direction as the puppet's; the shadow stays joined at the feet and falls on the side away from the sun.", ["person"])
o(2, "A riderless skateboard rolls past a streetlamp at night, and its shadow swings around it as it passes under the light.",
     "The shadow points away from the lamp: it trails behind the board as it approaches, shortens under the lamp, and stretches out ahead once it has passed; it never points toward the lamp.", ["person"])
o(4, "A desk lamp is moved from the left side of a vase to the right side, and the vase's shadow swings from the right side of the vase to the left.", None, ["person"])
o(5, "A pair of hands held in a flashlight beam pointed at a wall forms a bird shape, and a bird-shaped shadow appears on the wall.",
     "The shadow matches the outline of the hands and changes the instant the fingers move; it is larger than the hands and appears only where the beam hits the wall.", ["person"], "hands are the shadow-casting shape: kept minimal")
o(6, "A balloon drifts across the beam of a projector during a slideshow, and its dark silhouette appears on the screen over the slides.",
     "The silhouette appears where the balloon blocks the beam and moves with it; the slide image is missing inside the silhouette and returns when the balloon has passed.", ["person"])
o(7, "A tall wooden lifeguard chair stands on a beach with the low sun behind it, and its long shadow stretches across the sand in front of it.",
     "The shadow lies on the ground away from the sun, starts at the chair's legs, and is longer than the chair is tall; it does not float or point toward the sun.", ["person"])
o(8, "A flashlight is brought closer to a toy dinosaur standing in front of a wall, and the dinosaur's shadow on the wall grows larger.", None, ["person"])
o(9, "The shadow of a cloud sweeps across a sunlit hillside, darkening the grass as it passes.",
     "The dark patch moves steadily in one direction with a soft edge, the grass under it dims and brightens again once it has passed, and the trees' own shadows fade inside the patch and return behind it; the patch does not jump, stop dead, or brighten the ground.",
     ["person", "timescale"], "user's choice: a moving cloud shadow is visible within seconds; the old full dim-then-brighten cycle takes tens of seconds and duplicated OPT-0163")
o(10, "A frog jumps straight up from a sunlit stone, and its shadow stays on the stone and separates from its feet while it is in the air.",
      "The shadow remains on the surface the whole time; the gap between the frog's feet and the shadow opens as it rises and closes when it lands.", ["person"])
o(11, "A tractor drives along a sunlit field track, and its shadow rolls along the ground beside it.",
      "The shadow moves at the same speed as the tractor, touches it at the wheels, and shows the wheels turning; it stays on the side away from the sun.", ["person"])
o(12, "A ball is thrown across a sunlit yard, and the ball's shadow slides along the ground beneath it and meets the ball where it lands.", None, ["person"])
o(13, "A patio umbrella is opened in the sun, and a round shadow appears on the ground beneath it.",
      "The shadow appears as the umbrella opens, matches its round outline, and lies on the side away from the sun; it moves when the umbrella is tilted.", ["person"])
o(15, "A ball rolls from a sunlit pavement into the shade of a building, and its shadow disappears.",
      "The shadow is visible only while the ball is in the sun and fades as it enters the shade; it would return if the ball rolled back into sunlight.", ["person"])
o(16, "A lit candle is carried in a circle around a vase on a table, and the vase's shadow sweeps around the table opposite the candle.", None, ["person"])
o(18, None, "The shadow moves in step with the kite's motion, far from the kite itself; it does not stay still while the kite moves.", ["expectation"], "expectation mentioned 'the child'")
o(19, "A ball rolls through the shadow of a signpost on a sunny pavement, and the post's shadow slides over the ball as it passes.",
      "The post's shadow appears on the ball's surface while the ball is inside it, and the ball's own shadow continues on the ground beyond; nothing about the post changes.", ["person"])
o(20, "A parked bicycle is lit from behind by a car's headlights at night, and a long shadow of the bicycle stretches down the road ahead of it.", None, ["person"])
o(21, "A hand reaches across a table toward a lamp, and the shadow of the arm sweeps across the table on the far side of the lamp from the arm.", None, ["person"], "the arm is the shadow-caster: kept minimal")
o(24, "An empty swing sways in the afternoon sun, and its shadow swings back and forth across the ground.",
      "The shadow moves in time with the swing, stretching and shortening as the seat rises and falls; it lies on the side away from the sun.", ["person"])
o(27, "The curtains of a sunny window are pulled open, and the shadow of the window frame appears on the floor.",
      "A bright patch with the dark bars of the frame inside it appears on the floor as the curtains open, on the side away from the window, and the bars match the frame's layout; the pattern vanishes when the curtains close.",
      ["person"], "user dropped 'as a cross' so the frame layout is not prescribed; expectation asks the bars to match whatever frame is shown")
o(28, "A hand is held in front of a projector lens, and a dark hand shape covers part of the picture on the screen.", None, ["person"], "hand is the shadow shape: kept minimal")
o(29, "A fox trots toward a streetlamp at night, and its shadow behind it shrinks until it is directly under the light.",
      "The shadow trails behind the fox on the side away from the lamp and shortens steadily as it approaches; it does not grow or move ahead of the fox.", ["person"])
o(32, "A book is held up between a lamp and a wall, and a rectangular shadow appears on the wall; as the book is tilted the shadow narrows.", None, ["person"])
o(33, "A robot vacuum travels the length of a corridor lit by a single ceiling light, and its shadow on the floor changes side as it passes beneath the light.",
      "The shadow is ahead of the vacuum before the light and behind it after, always pointing away from the bulb.", ["person"])
o(34, "A remote-controlled car launches off a small ramp in the sun, and its shadow stays on the ground while it is airborne and rejoins it on landing.",
      "The shadow stays on the ground while the car is in the air, separated from it, and meets the wheels at the moment of landing.", ["person"])
o(35, "A toy car is lifted off a sunlit table, and its shadow stays on the table and grows fainter as the car is raised higher.", None, ["person"])
o(36, "A garden hose sprays an arc of water in the evening sun, and the shadow of the arc falls on the soil beside it.", None, ["person"])
o(38, "A park bench stands beside a wall at dusk as the streetlights come on, and a shadow of the bench appears on the wall away from the nearest light.", None, ["person"])
o(40, "A pendulum swings in front of a wall lit by a lamp, and its shadow on the wall swings with it.",
      "The shadow moves in step with the pendulum, in the same rhythm, and never leads it or moves on its own; it falls on the wall on the side away from the lamp, and the string's shadow stays joined to the shadow of the pivot; when the pendulum stops, the shadow stops.",
      ["person"], "geometry fixed (lamp onto a wall, swing plane parallel to it) so the shadow must swing; expectation lists only invariants")
o(41, "A dog walks between a campfire and a tent at night, and a huge shadow of the dog sweeps across the tent wall.",
      "The shadow is on the tent side away from the fire, is larger than the dog, and moves the opposite way to the dog as it approaches the fire; it flickers with the flames.", ["person"])
o(43, "A leaf is held up against the sun, and its shadow falls on the ground below.",
      "The shadow has the leaf's outline, lies on the surface below and away from the sun, and moves when the leaf moves.", ["person"])
o(44, "A car drives along a road with the morning sun on its left, and its shadow runs along the ground on its right.",
      "The shadow stays on the car's right, attached at the wheels, and moves with the car; it does not switch sides while the sun stays put.", ["person"])
o(45, "The lamp beside a bookshelf is switched off and a lamp on the other side of the room is switched on, and the shelf's shadow jumps from one wall to the other.", None, ["person"])
o(47, "A lamppost on a pier casts its shadow onto the water below, and the shadow rides the ripples.",
      "The shadow lies on the water surface away from the sun and wobbles with the waves; it stays attached to the base of the post.", ["person"])
o(48, "A cat walks along the base of a sunlit wall, and its shadow walks along the wall beside it.",
      "The shadow on the wall keeps pace, its paws at ground level; it lies on the side away from the sun.", ["person"])
o(49, "A lantern inside a tent is turned up to full brightness, and sharp shadows of the tent poles appear on the canvas.", None, ["person"])
o(50, "A wide-brimmed hat is tilted on a sunlit statue's head, and the shadow of the brim moves down over the statue's eyes and nose.",
      "The shaded area appears under the brim on the side away from the sun and moves down the face as the hat tilts; it does not appear on the sunlit side.", ["person"])

# ---------------------------------------------------------------- reflection
o(51, "A toy robot in front of a mirror raises its right arm, and its reflection raises the arm on the opposite side.",
      "The reflected arm rises at the same instant and mirrored left-right; the reflection faces the robot and matches its colours; it does not lag or move differently.", ["person"])
o(52, "A bus drives slowly past a row of shop windows, and its reflection moves along in the glass beside it.",
      "The reflection keeps pace and disappears where the glass ends; it is mirrored and shows the same movement at the same time.", ["person"])
o(53, "A pebble is dropped into a calm pond that reflects the trees, and the reflection breaks into ripples.",
      "The reflection is upside down and clear while the water is still, shatters into wavering pieces when the pebble lands, and settles back as the ripples fade.", ["person"], "possible duplicate of OPT-0069 / 0086 (object into still reflecting water)")
o(56, "A pigeon walks past a puddle on a pavement, and its reflection passes across the puddle upside down.",
      "The reflection appears only within the puddle's edges, moves with the bird, and is inverted; it does not extend onto dry pavement.", ["person"])
o(58, "A pendulum clock swings in front of a hallway mirror, and the reflected pendulum swings in time with it, mirrored.",
      "The reflected swing is simultaneous and mirrored; the reflection stops when the pendulum stops.", ["person"], "was a near-duplicate of OPT-0051 (waving at a mirror); new object keeps it distinct")
o(59, "A robot vacuum turns in front of a floor-length mirror, and its reflection turns with it in mirror image.",
      "Every turn is matched instantly and mirrored; the reflection never gets ahead or faces a different way.", ["person"])
o(60, "A hand mirror is tilted downward, and the reflection in it shifts from the ceiling to the floor.", None, ["person"])
o(61, "A cloth is draped over a wall mirror, and the reflection of the room disappears behind the cloth.", None, ["person"])
o(62, "A car approaches from behind, and its image grows larger in the rear-view mirror of the car ahead.", None, ["person"])
o(63, "A ball rolls out of a room past a wall mirror, and its reflection leaves the mirror at the same time.",
      "The reflection slides out of the frame as the ball passes the mirror's edge and the mirror shows only the empty room afterwards; the reflection does not remain.", ["person"])
o(65, "A luggage trolley is pushed across a polished marble lobby floor, and its reflection moves upside down beneath it.",
      "The reflection meets the trolley at its wheels, is inverted, and moves exactly with it; it is dimmer than the trolley.", ["person"])
o(68, "A balloon on a string turns slowly in an elevator with mirrored walls, and its reflections turn with it in every wall.",
      "All reflections move at the same instant, each mirrored relative to its wall; none turns a different way.", ["person"])
o(69, "A bicycle wheel rolls through a puddle showing the reflection of a building, and the image shatters into ripples.",
      "The reflection breaks up at the moment the wheel enters and reforms as the ripples die; it does not stay sharp while the water moves.", ["person"])
o(70, "A car approaches from behind a parked car, and its image appears in the parked car's side mirror and grows larger.",
      "The image appears in the mirror before the car passes and grows as it nears; it leaves the mirror as the car draws alongside.", ["person"])
o(71, "A wristwatch lying on a sunny table is turned so its face catches the sunlight, and a bright spot of light appears on the wall and slides as the watch turns.",
      "The spot appears when the watch face is angled to the sun, moves as the watch turns, and disappears when the angle is lost; it does not move on its own.", ["person"])
o(72, "A hand mirror in a sunny doorway is tilted, sending a patch of sunlight dancing across the shaded room.", None, ["person"])
o(73, "A lamp beside a dark window is switched on at night, and the reflection of the lamp and the room appears in the glass.",
      "The reflection appears with the lamp and is mirrored; when the lamp is turned off it fades from the glass.", ["person"])
o(76, "A small mirror is angled behind a statue's head so that the back of the head appears in the wall mirror in front of it.",
      "The small mirror shows the back of the head, and that image appears in the big mirror; the view changes as the small mirror is tilted.", ["person"], "double reflection is hard to read in a 5 s clip: candidate for deletion")
o(77, "A car drives along a canal-side road, and its reflection travels upside down on the water beside it.",
      "The reflection keeps pace, is inverted, and wavers with the water; it is missing where reeds or a boat break the surface.", ["person"])
o(78, "A silver tray is polished until the room appears in it, then breath is blown on it and the image fogs and returns.",
      "The image gets clearer as the tray is polished, blurs under the breath, and comes back as the fog clears.", ["person"], "polishing hand + breath are the physics: kept passive/minimal")
o(80, "A hat on a mannequin head is turned from side to side in front of a shop mirror, and the reflection turns in mirror image.",
      "The reflection turns at the same time, to the mirrored side, wearing the same hat; it does not turn the same way as the head.", ["person"])
o(81, "A flashlight is pointed at a mirror on the wall, and a spot of light appears on the opposite wall.", None, ["person"])
o(82, "A seagull walks across a wet beach at low tide, and its reflection shows beneath it on the thin sheet of water.",
      "The inverted reflection appears only where the sand is covered by water and follows the bird's steps; it breaks up in its footprints.", ["person"])
o(83, "A checkerboard card is reflected in the bowl of a shiny spoon, and as the spoon turns slowly the reflected pattern stretches and shifts.",
      "The reflected pattern is small and warped by the curve and changes with the spoon's angle; it stays inside the metal.", ["person"])
o(84, "A puck slides across a frozen pond, and a faint reflection slides beneath it on the ice.",
      "The reflection is inverted, dim, and moves with the puck; it disappears where the ice is scratched or snow-covered.", ["person"])
o(86, "A coin is dropped into a fountain whose still water reflects the sky, and rings spread out that break up the reflected clouds.", None, ["person"])
o(87, "A candle burns between two facing mirrors, and a line of flames stretches away in both directions, all flickering together.",
      "The copies get smaller and dimmer further along the line and all flicker in time with the real flame; none moves independently.", ["person"])
o(88, "A hand wipes a streak across a steamed-up mirror, and the room appears in the clear streak.",
      "The reflection appears only where the fog is wiped away and is blurred elsewhere; the streak slowly fogs over again.", ["person"], "hand does the wiping: kept minimal")
o(90, "A car's side mirror is adjusted from inside, and the view in the mirror sweeps from the sky down to the road behind.",
      "The view moves smoothly as the mirror tilts and shows the scene behind the car, not in front; it stops changing when the adjustment stops.", ["person"])
o(91, "A soap bubble drifts past a bright window, and a tiny reflection of the window curves across the bubble's surface.", None, ["person"])
o(92, "A pair of sunglasses lies on a table facing a lamp, and the lamp shows as two small images in the lenses.",
      "The small images move if the lamp or glasses move and are curved to the lenses; they show the lamp, not what is behind the glasses.", ["person"])
o(93, "A motorboat crosses a glassy lake at low speed, and its reflection travels with it, broken only by the wake.",
      "The reflection is inverted and attached at the waterline; it distorts in the wake behind.", ["person"])
o(94, "A compact mirror is opened and angled toward a ring on a table, and the ring appears in the little mirror.",
      "The ring comes into view when the mirror is angled toward it and slides out of view when the angle changes; the image is mirrored.", ["person"])
o(97, "The reflection of a moored boat lies on clear still water, and when the boat rocks the reflection breaks apart and then settles.",
      "The reflection is inverted and clear while the water is flat; it wavers and fragments as the boat rocks and returns when the water calms.", ["person"])
o(98, "A disco ball turns under the stage lights, and dozens of small bright spots sweep across the walls.",
      "The spots move when the ball turns and stop when it stops; they appear on the walls away from the lights.", ["person"])
o(99, "A sheet of glass is held at an angle to a window, and the garden outside appears faintly in the glass over the room behind it.", None, ["person"])
o(100, "A red ball rolls along a hallway of polished steel panels, and a blurry reflection rolls alongside in each panel.",
       "Each panel shows a mirrored, slightly warped copy of the ball moving in step; the copies vanish at the gaps between panels.", ["person"])

# ---------------------------------------------------------------- refraction_transparency
o(101, "A drinking straw is placed into a glass of water, and it looks bent where it enters the water.", None, ["person"])
o(102, "A dog wades chest-deep into a clear pool, and its legs seen through the water look shorter and bent at the surface.",
       "The underwater part appears foreshortened and offset at the waterline; when the dog climbs out its legs look normal again.", ["person"], "same effect as OPT-0146 (stick in water): possible duplicate")
o(103, "Goldfish swim in an aquarium and are clearly visible through the glass.", None, ["person"])
o(104, "A bird hops across a lawn outside a clear window and is seen through the glass.",
       "The bird is fully visible through the pane, undistorted, and moves continuously behind it; the glass does not make it vanish or appear inside.", ["person"])
o(106, "A magnifying glass is moved over a page of small print, and the letters under the lens appear much larger.", None, ["person"])
o(107, "A pair of reading glasses is slid across a menu, and the text seen through the lenses appears slightly larger than the text around the frames.", None, ["person"])
o(108, "The tiles on the floor of a clear pool are seen through the water, their grid wavering slightly with the surface.", None, ["person"])
o(111, "A clear ice cube is held up to a window, and the scene outside is visible through the ice, slightly blurred.", None, ["person"])
o(112, "A cat moves behind a frosted glass door, and only a blurred shape of it is visible through the glass.",
       "The blur moves as the cat moves and sharpens as it comes closer to the glass; details never become clear through the frosting.", ["person"])
o(113, "Windshield wipers sweep in heavy rain, and each sweep clears a sharp view of the road that blurs again as rain lands.", None, ["person"])
o(114, "A patterned card is seen through a round fishbowl, and the pattern appears stretched and warped through the bowl; as the card is moved the warp changes.",
       "The distortion appears only through the water-filled bowl and changes as the card moves; the pattern is normal when seen past the bowl's edge.", ["person"])
o(115, "A hand is dipped into a clear pond, and the underwater part of the arm looks displaced from the part above the surface.", None, ["person"], "same effect as OPT-0101/0123/0146: possible duplicate")
o(116, "Seen from under the water, the wavering shapes of the trees and the pool ladder show through the surface.",
       "The shapes are visible but their outlines ripple with the surface; they steady when the water is calm.", ["person"])
o(117, "Cakes on display are clearly visible through a bakery's front window as a tram passes behind the camera.", None, ["person"], "static scene: the passing tram only adds motion")
o(118, "Water is poured into a clear jug standing in front of a patterned tile wall, and the pattern seen through the jug shifts as the water rises.", None, ["person"])
o(119, "A shopping cart is pushed up to a clear glass door which swings open, the cart having been fully visible through it as it approached.",
       "The cart is seen through the glass the whole way; the door opens on its hinges when pushed and the cart goes through the opening, not through the glass.", ["person"])
o(120, "Coins lie on the bottom of a clear fountain, and they appear to shimmer and shift as the surface ripples.", None, ["person"])
o(121, "A clear plastic ruler is laid over a line of text, and the text is readable through the ruler.", None, ["person"])
o(123, "A spoon stands in a clear glass jar of oil and looks kinked where it enters the oil; when it is lifted out the kink vanishes.", None, ["person"])
o(124, "Raindrops cover a window, and the street outside appears as many tiny warped pictures within the drops.", None, ["person"])
o(125, "A snorkel mask is lowered under the water, and the blurred rocks below come into sharp view through the mask.", None, ["person"])
o(126, "A clear glass jar of water is held in front of a printed face on a poster, and the eyes seen through the jar look stretched wide.",
       "The stretching appears only in the part of the face seen through the water and changes as the jar moves; the face beside the jar is normal.", ["person"])
o(127, "A garden is seen through a pane of old wavy glass, and the plants seem to bend and shift as the camera moves.",
       "The distortion changes with the viewpoint while the plants stay still; through a flat pane beside it the view is undistorted.", ["person"])
o(128, "A clear glass marble is held up in front of a lamp, and the room appears tiny and warped inside the marble.",
       "The small distorted image is inside the marble and moves as the marble moves; the room around the marble is normal.", ["person"])
o(129, "Tongs reach into a bakery's glass counter from the open back and lift out a pastry that was visible through the glass.",
       "The pastry is clearly visible through the glass, the tongs enter from behind rather than through the pane, and the pastry lifted is the one that was seen.", ["person"])
o(130, "A field slides past a train window and is clearly visible through the glass.", None, ["person"])
o(131, "A coin is dropped into a tall clear vase of water, and the coin appears to jump sideways as it passes through the surface.", None, ["person"])
o(132, "A glass paperweight is slid over a newspaper, and the letters under it look swollen and bent.", None, ["person"])
o(133, "A ruler stands upright in a clear rock pool, and the underwater part looks shorter than the part above the surface.",
       "The underwater part appears foreshortened and displaced at the surface; lifted out, the ruler looks normal.", ["person"], "'closer than they feel' was not visual; now same effect as OPT-0146: candidate for deletion")
o(134, "A bathroom window is fogged after a shower, and where a hairdryer blows on the glass the view of the yard outside sharpens.",
       "The view goes from blurred to clear where the warm air dries the glass; it does not blur again while the glass is dry.", ["timescale"], "natural drying takes minutes")
o(135, "A loupe is held over a ring, and the ring's details appear greatly enlarged through it.", None, ["person"])
o(136, "A hand is held behind a glass of water, and the fingers appear fatter through the glass than beside it.",
       "The widening shows only behind the water; the fingers seen past the glass edge are normal; the hand itself is unchanged.", ["person"], "same effect as OPT-0109/0139: possible duplicate")
o(137, "From under the clear sea, the underside of a boat shows as a wavering dark shape through the surface.", None, ["person"])
o(138, "Vegetable pieces lie at the bottom of a pot of clear water, and they seem to shift and swim as the water is stirred.", None, ["person"])
o(139, "A clear glass bottle of water is held sideways in front of a lit sign, and the letters seen through the bottle appear stretched.", None, ["person"])
o(140, "A patch of a wet window is wiped dry with a cloth, and the view through the patch becomes sharp.", None, ["person"])
o(141, None, None, [], "CANDIDATE FOR DELETION: glasses only sharpen the view for the wearer's eyes; for the camera they blur it, so a correct video cannot show the caption")
o(142, "A stone is dropped into a clear stream and sinks, its image wavering with the current until it rests on the bed.", None, ["person"])
o(143, "A clear glass beaker of water is placed in front of a ruled sheet, and the lines behind the beaker appear closer together and shifted.", None, ["person"])
o(144, "A shop display is seen through a window streaked with rain, and the mannequins appear smeared where the water runs.", None, ["person"])
o(145, "A clear glass of water is held up in front of a doorway, and the doorway seen through it appears flipped left-to-right and squeezed thin.",
       "The flipped, narrowed image appears only through the water and shifts as the glass moves; the room seen around the glass is normal.", ["person"])
o(146, "A straight stick is lowered into a clear pond, and the underwater part appears to angle away from the part above the surface.", None, ["person"])
o(147, "A car's side window fogs from the inside, blurring the passing city, until a patch is wiped clear.",
       "The blur grows with the fog and the view becomes sharp only where the patch is wiped; the city outside does not change.", ["person"])
o(148, "A glass of water is placed on a line drawn on a piece of paper, and the line under the glass appears broken from the line outside it.", None, ["person"])
o(149, "A pair of binoculars is held up to the camera toward a distant bird, and the bird appears large and close through the lenses.",
       "The enlarged view appears only through the eyepieces and follows where the binoculars point; the bird seen beside them is small.", ["person"])
o(150, "A clear lid is lifted from a pot, and the food that was visible through the lid is seen the same underneath.", None, ["person"])

# ---------------------------------------------------------------- illumination
o(151, "The wall switch in a dark living room is flipped, and the ceiling light comes on and the room is lit.", None, ["person"])
o(152, "A bedside lamp is turned off, and the bedroom goes dark except for the faint glow from the window.", None, ["person"])
o(153, "A flashlight is swept across a dark wall, and the bright spot slides along the wall.",
       "The spot moves in the direction the flashlight turns and stays lit only where the beam points; it does not remain on the wall after the beam moves.", ["person"])
o(154, "A single candle burns in a dark room, and it lights the objects nearest to it while the far wall stays dark.",
       "The objects closest to the flame are brightest, brightness falls off with distance, and the light flickers with the flame.", ["person"])
o(156, "A flashlight is switched on under a blanket, and the blanket glows from inside where the light is.",
       "The glow is brightest where the flashlight is nearest the cloth and moves if the light moves; it stops when the light is switched off.", ["person"])
o(158, "A spotlight follows a remote-controlled car across a dark stage, and the circle of light moves with it.",
       "The lit circle stays centred on the car and the rest of the stage stays dark; the car's shadow falls on the floor away from the spotlight.", ["person"])
o(159, "A refrigerator door is opened in a dark kitchen, and light from inside the fridge spills out across the floor.",
       "The light appears as the door opens, widens with the door, and lights the floor in front of it; it disappears when the door closes.", ["person"])
o(160, "A phone lying face-up on a table in a dark room lights up, and its glow lights the objects around it from below.",
       "The objects are lit on the sides facing the screen and the glow changes when the screen's picture changes; it goes dark when the screen turns off.", ["person"])
o(161, "A desk lamp is moved closer to an open book, and the page becomes brighter.", None, ["person"])
o(162, "A dimmer knob is turned slowly, and the ceiling lights fade from bright to a dim glow.", None, ["person"])
o(164, "Heavy curtains in a dim bedroom are pulled open, and daylight floods in and brightens the room.", None, ["person"])
o(165, "A match is struck in a dark cave, and the flame lights the rock walls around it for a moment.", None, ["person"])
o(166, "A lantern is carried through a dark campsite, and the pool of light moves along the ground with it.",
       "The lit area travels with the lantern and the tents brighten as it passes and darken behind it.", ["person"])
o(167, "A headlamp is turned from side to side in a dark cave, and the beam sweeps across the cave walls with each turn.",
       "The lit patch moves exactly with the lamp and the wall it turns away from goes dark; the light is brightest where the beam is centred.", ["person"])
o(168, "A laser pointer's red dot moves across a projected slide as the pointer is moved.",
       "The dot appears only while the button is pressed, moves with the pointer, and disappears when it is released; it does not linger.", ["person"])
o(170, "A camera flash fires in a dim hall, and the whole room is lit for an instant.", None, ["person"])
o(171, "A car enters a tunnel on a sunny day, and the inside of the car dims until the overhead tunnel lights take over.", None, ["person"])
o(172, "A flashlight pointed at a wall is swung up to the ceiling, and the lit spot leaves the wall and appears on the ceiling.", None, ["person"])
o(173, "A television is switched on in a dark room, and the walls and furniture glow with the changing light from the screen.", None, ["person"])
o(174, "A hand is cupped over the front of a flashlight, and the beam is blocked and the room goes dark.",
       "The light disappears the instant the hand covers the lens and the fingers glow red at the edges; the beam returns when the hand is removed.", ["person"], "the hand is the blocker and glows: kept minimal")
o(176, "Two identical white vases stand at different distances from a single lamp in a dark room, and the nearer one is lit far more brightly than the farther one.",
       "Brightness falls off with distance from the lamp; if the far vase is moved toward the lamp it brightens.", ["person"])
o(177, "A bicycle's headlight is switched on at night, and a cone of light appears on the path ahead.",
       "The lit patch appears in front of the bike when the light is switched on and moves with the bike; the path behind stays dark.", ["person"])
o(178, "A lit candle is carried down a dark staircase, and the light on the walls travels with the candle.", None, ["person"])
o(180, "A lighter is struck in a dark garage and held up, and the small flame lights the nearby tools and bench.",
       "Only things near the flame are visible, lit from the flame's direction; the light flickers and goes out when the lighter closes.", ["person"])
o(181, "A night light is switched on in a dark bedroom, and a soft glow lights the corner around it.", None, ["person"])
o(183, "The door of a lit oven is opened in a dim kitchen, and the food inside is lit by the oven lamp.", None, ["person"])
o(184, "A cinema's house lights dim before the film starts, and the seats fade from view until only the screen glows.",
       "The dimming is gradual, the seats go dark, and the screen's light on the front rows changes with the picture.", ["person"])
o(185, "A floodlight over a building site is switched on at dusk, and the yard is lit while the area behind the light stays dark.", None, ["person"])
o(186, "A row of paper lanterns hanging in a garden is lit one by one, and each glows as its candle is lit.", None, ["person"])
o(187, "A flashlight shines through cupped fingers, and the fingers glow red where the light passes through them.", None, ["person"], "fingers are the translucent object: kept minimal")
o(189, "Seen from inside a dim shop, the open doorway to the sunlit street stands out as a bright rectangle and the floor near the door is lit.",
       "The interior is dim relative to the doorway, the floor near the door is lit, and it grows darker deeper into the shop.", ["person"])
o(190, "A firework bursts high in the night sky, and for a moment the rooftops below are lit.",
       "The rooftops brighten at the burst and dim as it fades; the light comes from above; the ground is lit only briefly.", ["person"])
o(191, "A desk lamp is turned to point at the wall, and the wall brightens while the desk beneath it goes dim.", None, ["person"])
o(193, "A lamp with a coloured shade is switched on, and the shade glows while the desk below is lit through its open bottom.", None, ["person"])
o(194, "A dog walks through an office with motion-sensor lights, and the ceiling panels switch on ahead of it and go off behind it.",
       "Each panel lights as the dog approaches and its patch of floor brightens; panels far behind it go dark after a delay.", ["person"])
o(195, "The last candle on a dinner table is blown out, and the table falls into darkness.",
       "The warm light on the table disappears with the flame; the room stays dark afterwards.", ["person"], "the puff of breath is the trigger: passive")
o(196, "A phone's torch is switched on in a dark basement, and its beam lights the floor and shelves in front of it.",
       "The lit area is where the phone points and moves with it; the space behind remains dark.", ["person"])
o(198, "An underwater torch is switched on in murky water, and a cone of lit particles appears in front of it.",
       "The lit cone points where the torch points, fades with distance, and moves with the torch; the water behind stays dark.", ["person"])
o(199, "A string of fairy lights along a fence is turned on, and small pools of light appear under each bulb.", None, ["person"])
o(200, "A lantern in a tent is turned down to its lowest setting, and the tent interior darkens until only the objects nearest it are visible.",
       "The brightness falls smoothly as the knob is turned; the farthest corners darken first; it does not brighten on its own.", ["person"])

# ---------------------------------------------------------------- color_mixing
o(201, "Yellow and blue paint squeezed side by side on a palette are stirred together with a brush, and the mixture turns green.", None, ["person"])
o(202, "A drop of red food colouring is added to a glass of white icing and stirred, and the icing turns pink.", None, ["person"])
o(203, "A red stage light is switched on over a white curtain, and the curtain turns red under the light.",
       "The curtain looks red only while the red light is on and where the light reaches; it looks white again when the light changes.", ["person"])
o(205, "A piece of blue cellophane is taped over a flashlight, and the beam on the wall turns blue.", None, ["person"])
o(206, "A garden hose sprays a fine mist with the sun behind it, and a small rainbow appears in the spray.", None, ["person"], "close to OPT-0233 (sprinkler rainbow)")
o(209, "Blue ink is dripped into a glass of clear water, and the blue spreads in swirls until the water is evenly tinted.", None, ["person"])
o(210, "A spoonful of turmeric is stirred into a pot of white rice, and the rice turns yellow where the spice is mixed in.", None, ["person"])
o(211, "Red and white paint on a paper plate are swirled together with a brush, and the swirl turns pink.",
       "Pink appears where the brush blends the two and the streaks become uniform with more mixing; the colours do not separate.", ["person"])
o(212, "A party light is switched from white to green, and the white walls of the room turn green.", None, ["person"])
o(215, "A smart bulb is switched from white to purple, and the room's white ceiling turns purple.", None, ["person"])
o(216, "A sheet of red plastic is held up in front of the camera, and everything seen through it looks red.",
       "Only the view through the plastic is tinted; the scene beyond its edges is normal; the tint vanishes when the plastic is lowered.", ["person"])
o(217, "A purple bath bomb is dropped into a tub of clear water, and the colour billows out and turns the whole bath purple.", None, ["person"])
o(219, "Blue paint is dabbed onto a wet patch of yellow watercolour, and the colours bleed into each other making green where they meet.", None, ["person"])
o(221, "A little green food colouring is poured into a bowl of white cake batter and stirred, and the batter turns pale green.", None, ["person"])
o(222, "A red and a blue spotlight are crossed on a white backdrop, and the area where they overlap glows purple.", None, ["person"])
o(223, "A white lamp is seen through a jar of yellow juice and looks yellow through the jar.", None, ["person"])
o(224, "A pair of yellow-tinted sunglasses is held up in front of a white wall, and the wall looks yellow through the lenses.",
       "The tint appears only through the lenses; when the glasses are lowered the wall is white.", ["person"])
o(225, "A brush loaded with red paint is swirled through a jar of clean water, and the water turns pink and cloudy.", None, ["person"])
o(226, "Two shades of hair dye are squeezed into a bowl and whisked together, and the mixture becomes one uniform colour.", None, ["person"])
o(229, "Yellow and red watercolour are dripped onto a wet sheet of paper, and where they run together an orange band forms.", None, ["person"])
o(230, "A green glass is held up to the light in front of a white wall, and the wall looks green through it.",
       "The tint is only in the view through the glass; the wall around it is white and returns to white when the glass is lowered.", ["person"])
o(232, "A spoonful of beet juice is dropped into a bowl of white yogurt and folded in, and the yogurt turns pink with darker streaks that fade as it is mixed.", None, ["person"])
o(234, "A stage floods with yellow light, and the white set and curtains all look yellow at once.",
       "Every lit white surface changes together to yellow and back when the light changes; shadowed folds stay darker.", ["person"])
o(235, "Blue drops are added to a glass of yellow lemonade and swirled, and the drink turns green.", None, ["person"])
o(237, "A roller of white paint is run over a patch of wet red paint on a wall, and it leaves a pink streak where they blend.", None, ["person"])
o(241, "A red laser dot lands on a white wall, and when it is moved onto a green plant the dot becomes hard to see.",
       "The dot is bright red on the white wall and dim on the green leaves; it stays red wherever it lands and moves with the pointer.", ["person"])
o(242, "A sheer red scarf is draped over a white lamp, and the room's light turns warm red.", None, ["person"])
o(243, "The corner of a white paper towel is dipped into a cup of blue dye, and the blue creeps up the towel.", None, ["person"])
o(244, "A clear-cut crystal pendant is turned in sunlight, and coloured sparkles dance across the ceiling.", None, ["person"])
o(245, "Grenadine is poured into a glass of orange juice, and the red sinks and spreads through the bottom of the glass while the top stays orange.", None, ["person"])
o(246, "A stripe of translucent blue watercolour is painted over a dry yellow stripe, and the overlap looks green.", None, ["person"])
o(247, "Sunlight enters a room through a red balloon held up to the window, and a soft red glow falls on the white wall behind it.",
       "The glow is on the side away from the window and moves with the balloon; the wall is white when the balloon is lowered.", ["person"])
o(248, "A spoonful of matcha powder is stirred into a glass of milk, and the milk turns pale green.", None, ["person"])
o(250, "A rainbow over a field is fading as the rain moves away and the sky clears.", None, ["person", "timescale"])

import subprocess
recs = json.loads(SRC.read_text())
orig = {r["id"]: r for r in json.loads(subprocess.run(["git", "-C", str(SRC.parents[2]), "show", f"{ORIG_COMMIT}:data/train/optics.json"],
                                                       capture_output=True, text=True, check=True).stdout)}
old_to_new = json.loads(MAP.read_text())["old_to_new"]
new_to_old = {v: k for k, v in old_to_new.items()}
out = []
stats = {"person": 0, "timescale": 0, "expectation": 0, "keep_person": 0, "unchanged": 0, "applied": 0}
for r in recs:
    oid = new_to_old.get(r["id"], r["id"])
    o_rec = orig[oid]
    c, e, ch, note = O.get(oid, (None, None, [], ""))
    new_c, new_e = c if c else o_rec["caption"], e if e else o_rec["expectation"]
    applied = (r["caption"], r["expectation"]) == (new_c, new_e) and (r["caption"], r["expectation"]) != (o_rec["caption"], o_rec["expectation"])
    out.append({
        "id": r["id"], "orig_id": oid, "category": r["category"], "subcategory": r["subcategory"],
        "violation_types": r["violation_types"],
        "caption": new_c, "expectation": new_e,
        "old_caption": o_rec["caption"], "old_expectation": o_rec["expectation"],
        "change": ch, "note": note, "applied_to_optics_json": applied,
    })
    for k in ch: stats[k] += 1
    if not ch: stats["unchanged"] += 1
    stats["applied"] += applied
DST.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
deleted = [k for k in DELETE if k not in old_to_new]
print(f"wrote {DST} with {len(out)} records (ids {out[0]['id']}..{out[-1]['id']}); {stats}; deleted (not in file): {deleted}")
