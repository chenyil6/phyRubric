#!/usr/bin/env python3
"""Build data/drafts/acoustics_draft.json (+ _review.md): proposed rewrites of the Acoustics train captions.

Two principles (user, 2026-09-11):
  1. no people      - the player / striker is removed: plain passive voice ("A snare drum is struck once with a stick"),
                      an object-state trigger (a saw blade falls onto a bench, a weight plate slips off a rack, a door
                      blows shut in a gust) or a machine in place of the person (a pile driver for a stamping crowd).
                      A hand is named only when it is the acting tool for the whole event (a single slap on a
                      trampoline mat, a palm damping strings).  Wind instruments keep breath implicit ("A trumpet is
                      blown") - the mouth is the air source and cannot be replaced.
  2. 5-10 s visible - every acoustic item is already seconds-scale (a struck object rings and settles in 1-5 s).  The
                      real weakness of this branch is visibility: a faint shimmer on a rim or a lampshade may not be
                      resolvable at 480p.  Such items are flagged as delete candidates, not deleted.
`delete` = proposed deletion (none here; only candidates).  Captions state the event only; the how lives in the
expectation.  Expectations that asked for an action not in the caption ("stops when a finger touches it") are trimmed.
"""
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data/train/acoustics.json"
DST = ROOT / "data/drafts/acoustics_draft.json"
REVIEW = ROOT / "data/drafts/acoustics_draft_review.md"

O: dict[str, tuple] = {}


def o(i, c=None, e=None, ch=(), note=""):
    O[f"ACOU-{i:04d}"] = (c, e, list(ch), note)


def keep(i, note):
    o(i, None, None, ["keep_person"], note)


def delete(i, reason):
    o(i, None, None, ["delete"], reason)


def flag(i, note):
    o(i, None, None, ["note"], note)


# ---------------------------------------------------------------- struck_vibration
o(1, "A snare drum is struck once with a stick, and the drum skin shivers visibly and then settles.", None, ["person"])
o(2, "The low string of an acoustic guitar is plucked, and the string blurs into a wide band before slowly sharpening to a line again.", None, ["person"])
o(3, "A hanging gong is struck with a padded mallet, and the gong's face trembles and its edges go fuzzy before calming.", None, ["person"])
o(4, "A steel ruler lies flat on a desk under a heavy book with part sticking over the edge; the free end is flicked and waggles up and down before coming to rest.",
  "The free end vibrates fast right after the flick with the tip blurring, the swings get smaller, and it stops within seconds; the part under the book stays still.",
  ["person", "expectation"], "the book replaces the hand holding the ruler down")
o(5, "A taut rubber band stretched between two nails is flicked, and the band blurs and hums before going still.", None, ["person"])
o(6, "The rim of a wine glass is tapped with a spoon, and the glass rings while its rim shimmers faintly.",
  "The shimmer appears at the tap and fades over a second or two; the glass does not move before the tap and does not shatter from a light tap.",
  ["person", "expectation"], "'touching the rim with a finger stops it' asked for an action not in the caption; visibility weak (rim shimmer at 480p) - delete candidate")
o(7, "A struck tuning fork is dipped into a glass of water, and the water sprays up where the prongs touch it.",
     "The water is still before the prongs reach it, spray and ripples burst out only at the moment of contact and only while the prongs touch the surface, and the surface settles once the fork is lifted; the spray does not start before contact or continue with the fork out of the water.",
     ["person", "scene"], "user: the blur of a vibrating fork is invisible at video resolution; the water spray makes the vibration judgeable")
o(8, "A single string on an upright bass is plucked, and the thick string swings visibly from side to side before settling.",
  "The swing is widest right after the pluck and shrinks steadily until the string is still.", ["person", "expectation"])
o(9, "A large cymbal on a stand is struck, and the cymbal wobbles on its stand and its edge blurs before it steadies.", None, ["person"])
o(10, "A metal pot lid hanging from a hook is banged with a wooden spoon, and the lid rings and quivers on its hook.", None, ["person"],
  "the hook replaces 'her other hand'")
o(11, "A small scrap of paper rests on a bass string inside a grand piano with the lid open; the key for that string is pressed, and the paper jumps off the string.",
      "The paper lies still until the key is pressed, is flicked up and off the string the instant the note sounds, and falls onto neighbouring strings or the frame; only the struck string's paper moves, and it does not jump before the key goes down or float back into place.",
      ["person", "scene"], "user: the classic paper-rider demo turns an invisible string vibration into a visible jump; hammer/damper details dropped")
o(12, "A xylophone bar is struck with a mallet, and the bar shivers on its cord for a moment.", None, ["person"])
o(13, "A harp string is plucked, and the string vibrates in a blur that narrows as the note fades.", None, ["person"])
o(14, "A thin sheet-metal door is knocked on, and the panel visibly flexes and rattles under the knocks before going quiet.", None, ["person"])
o(15, "A hanging metal triangle is struck with a rod, and the triangle swings on its loop and its sides shimmer.", None, ["person"])
o(16, "A fork stands upright with its handle pushed into a cork, and its tines are flicked; they blur briefly and then are still.",
  "The blur starts at the flick and is gone within a second; the handle in the cork stays sharp.", ["person", "expectation"],
  "visibility weak: small object, very brief blur - delete candidate")
o(17, "The tip of a long fishing rod standing in a rod holder is flicked, and it whips back and forth in a blur before settling.", None, ["person"])
o(18, "A taut trampoline mat is slapped once by a hand, and the mat ripples outward and shivers before going flat.", None, ["person"],
  "the hand is the acting tool for the single slap")
o(19, "A stretched washing line is plucked, and the line blurs along its length and slowly sharpens.", None, ["person"])
o(20, "A suspended metal wind-chime tube is hit with a stick, and the tube swings and its outline shimmers.", None, ["person"])
o(21, "A long steel saw blade falls flat onto a bench, and the blade twangs and flutters for a moment before lying still.", None, ["person"])
o(22, "The top of a large empty cardboard box is thumped, and the lid panel bounces and quivers before settling.", None, ["person"])
o(23, "A metal spring doorstop mounted on the wall is flicked, and it wobbles wildly and then slows to a stop.", None, ["person"])
o(24, "The body of an acoustic guitar is tapped with a palm, and the strings tremble faintly in response before going still.", None, ["person"],
  "visibility weak: a faint sympathetic tremble - delete candidate")
o(25, "A hanging saucepan is struck with a spoon, and the pan swings and its bottom shimmers.", None, ["person"])
o(26, "The taut head of a large bass drum is slapped once, and the head visibly dips and rebounds several times, each time smaller.", None, ["person"])
o(27, "The wire of a garden fence is plucked, and the wire blurs and hums along its span before settling.",
  "The blur is greatest at the plucked point and fades along the wire until it is still.", ["person", "expectation"], "'stops when the wire is gripped' dropped")
o(28, "A metal garbage-can lid is dropped onto the can, and the lid rings and quivers before settling.",
  "The quiver starts at the impact and dies within a second or two; the lid is still before and after.", ["person", "expectation"])
o(29, "A mallet is run across the bars of a marimba, and each bar shivers in turn as it is struck.", None, ["person"])
o(30, "The thin elastic cord of a paddle ball toy is plucked, and the cord blurs and the ball bounces lightly before both go still.", None, ["person"])
o(31, "A hanging handbell is swung so that its clapper strikes it, and the bell swings and its rim shimmers.", None, ["person"])
o(32, "A strip of thin sheet metal clamped at one end in a vise is flicked, and the free end vibrates in a blur that slowly stops.", None, ["person"])
o(33, "The taut skin of a tambourine is struck, and the skin shivers and the metal jingles rattle before quieting.", None, ["person"])
o(34, "A thin metal lampshade is tapped with a pen, and the shade rings and its edge blurs faintly before settling.", None, ["person"],
  "visibility weak - delete candidate")

# ---------------------------------------------------------------- sound_driven_vibration
o(37, "A heavy door blows shut in a gust of wind, and a picture frame on the nearby wall swings from side to side before hanging still.", None, ["person"])
o(40, "A bass drum is struck in steady beats next to a shop's plate-glass window, and the window shivers with each hit.",
  "The window's reflection wobbles in time with the drumbeats and steadies when the beats stop.", ["person", "expectation"],
  "marching band removed; a single drum keeps the beat-by-beat shiver")
o(47, "A loud table saw in a workshop is switched on, and the screws in a jar on the bench begin to rattle and shift.", None, ["person"])
o(50, "A door knocker is banged hard and repeatedly on a heavy front door, and a glass of water on the hall table beside it ripples with each knock.",
  "Each ripple ring appears with a knock and fades before the next; the surface is calm when the knocking stops.", ["person", "scene", "expectation"],
  "drummer removed; also a near-duplicate of ACOU-0035 (glass on a subwoofer) - delete candidate")
flag(53, "the motorcycle's rider is implicit and not named; left as is")
o(55, "A heavy weight plate slips off a rack and lands on a gym floor, and the metal plates on the nearby rack ring and shiver.", None, ["person"])
o(57, "A bass drum is banged in a school gym, and a row of basketballs on a rack gently rock in their cradles.", None, ["person"])
o(62, "A pile driver thumps at a building site, and the coffee in a cup on a nearby wall shows a steady wobble in time with the blows.",
  "The wobble matches the rhythm of the blows and settles when the driver stops.", ["person", "scene", "expectation"], "stamping crowd replaced by a machine")
o(64, "A heavy cast-iron pan is dropped onto a stovetop, and the lids of neighbouring pots rattle for a moment.", None, ["person"])
o(66, "A chainsaw is revved on a bench in a garage, and the tools hanging on the pegboard behind it sway and tap against the board.", None, ["person"])

# ---------------------------------------------------------------- source_motion
o(71, "A tuning fork is struck and held up, and the prongs blur; the prongs are touched to a table and the blur stops at once.", None, ["person"])
o(72, "A car engine idles roughly, and the whole hood trembles faintly until the engine is switched off.", None, ["person"])
o(73, "A bow is drawn across a cello string, and the string blurs under the bow and sharpens the moment the bow lifts.", None, ["person"])
o(76, "A chord is strummed on a guitar, and all the strings blur together; a palm is laid across them and each string sharpens the instant it is touched.", None, ["person"],
  "the palm is the acting tool for the damping")
o(78, "A harmonica is played, and the reeds inside can be seen quivering through the openings while the note sounds.",
  "The reeds move only while the note sounds and are still between notes.", ["person", "expectation"], "breath is the physics; the mouth stays implicit")
o(79, "A running lawnmower stands on the grass, and its handle shakes visibly until the engine is cut.", None, ["person"])
o(80, "A bass drum pedal is pressed repeatedly, and the beater swings into the drumhead with each press and the head dips each time.", None, ["person"])
o(82, "A long note is bowed on a violin, and the string under the bow is a blur that clears the instant the bow stops.", None, ["person"])
o(84, "A running electric razor lies on a counter, and its head buzzes and blurs until it is switched off.", None, ["person"])
o(87, "A trumpet is blown, and the bell of the trumpet trembles faintly while the note sounds.",
  "The tremble appears while the note sounds and is gone when it stops.", ["person", "expectation"],
  "breath is the physics; visibility weak (a faint tremble) - delete candidate")
o(88, "A pager on vibrate goes off on a nightstand and rattles against the wood until it stops.",
  "The rattling and small movements happen only while it vibrates and end when the vibration stops.", ["person", "expectation"])
o(89, "A violin bow is drawn along the edge of a cymbal, and the cymbal's edge shimmers while the bow moves and stills when it lifts.", None, ["person"])
o(91, "The keys of a toy piano are banged, and the small hammers inside can be seen jumping up with each key press.", None, ["person"])
o(92, "A paint shaker at a hardware store is switched on, and the paint can clamped in it blurs with the shaking until the timer stops it.", None, ["person"])
o(93, "A single note is plucked on a banjo, and the banjo's head visibly quivers beneath the strings and then stills.", None, ["person"])
o(96, "A stand mixer runs on high, and the whole mixer trembles on the counter until it is turned down.", None, ["person"])
o(97, "A microphone on a stand is tapped, and the mic head jiggles on its clip with each tap.", None, ["person"])
o(99, "A set of bagpipes is played, and the drones resting on the shoulder tremble faintly while the note holds.",
  "The drones tremble only while the note holds and are still when it stops.", ["person", "expectation"],
  "breath is the physics; the piper remains as a shoulder; visibility weak - delete candidate")
o(100, "A wind-up music box is set going, and the metal comb inside can be seen plucked tooth by tooth as the cylinder turns, until the spring runs down.", None, ["person"])


# ================================================================ user decisions 2026-09-14 (this session)
# Invisible "shimmer/blur" vibrations turned into classic classroom demos (visible secondary effect);
# invisible + redundant items deleted.  Later assignments override the entries above.
o(3, "A gong is struck once with a padded mallet, and a ping-pong ball hanging on a thread against its face is knocked away and swings.",
     "The ball rests against the gong until the strike, is thrown outward the instant the gong sounds and swings back and forth, tapping the gong again as it returns while it rings; the ball does not move before the strike.",
     ["person", "scene"], "demo: hanging ball kicked by the vibrating gong; the face's shimmer is invisible on video")
o(6, "A wine glass half full of water is tapped on the rim with a spoon, and the water surface inside breaks into fine ripples while the glass rings.",
     "The ripples appear only at the tap and fade as the ringing dies; the glass itself is not seen moving and the water does not slosh as if the glass had been shaken.",
     ["person", "scene"], "demo: water inside the rung glass ripples; the rim shimmer is invisible")
o(10, "Grains of rice lie on an upturned metal pot lid on a table; the lid is struck once with a spoon and the grains jump.",
      "The grains are still before the strike, jump up together at the moment of the strike and land back on the lid or scatter off its edge; they do not jump before the strike or keep jumping once the lid is quiet.",
      ["person", "scene"], "demo: rice on the struck lid; replaces the lid quivering in a hand / on a hook")
o(12, "A few grains of salt lie on a xylophone bar; the bar is struck with a mallet and the grains jump off.",
      "The salt is still until the strike, leaps off the bar at the strike and does not return; only the struck bar's salt moves.",
      ["person", "scene"], "demo: salt on the struck bar; the bar's shiver is invisible")
o(24, "Small paper riders sit on the strings of an acoustic guitar; the body of the guitar is tapped with a palm and the riders jump.",
      "The riders lie still until the tap, hop or fall off at the tap, and do not move again once the strings are quiet; the strings are not plucked.",
      ["person", "scene"], "demo: paper riders show the sympathetic vibration of the strings; palm kept as the acting tool")
o(29, "Salt is sprinkled on the bars of a marimba; a mallet runs across the bars and the salt jumps off each bar in turn.",
      "Salt leaves each bar only as that bar is struck, in the order the mallet travels; bars not yet struck keep their salt still.",
      ["person", "scene"], "demo: salt jumping bar by bar also tests the order of events")
o(38, "Thunder rolls over a house, and a strip of paper taped to a loose window pane quivers with each rumble.",
      "The strip flutters only during the rumbles and hangs still between them; it does not flutter before the thunder or keep fluttering afterwards.",
      ["scene"], "visible indicator added: a buzzing pane alone cannot be seen")
o(40, "A marching band's bass drum passes close to a shop window, and a paper sign taped to the inside of the glass quivers with each beat.",
      "The sign twitches in time with the drum beats and is still between them and after the band has passed; it does not move before the drum sounds.",
      ["person", "scene"], "visible indicator added: a shivering pane alone cannot be seen")
o(71, "A struck tuning fork is brought up to a ping-pong ball hanging on a thread, and the ball is kicked away and swings.",
      "The ball hangs still until the prongs touch it, is knocked outward on contact and swings back, being kicked again if it returns to the ringing fork; nothing moves before contact.",
      ["person", "scene"], "demo: ball kicked by the fork (ACOU-0007 already uses the water demo)")
o(89, "Sand is sprinkled on a cymbal and a violin bow is drawn along its edge, and the sand jumps and gathers into lines.",
      "The sand lies still until the bow moves, dances while the bow is drawn and collects into lines or patches, and settles when the bow lifts; no pattern forms before the bow touches the cymbal.",
      ["person", "scene"], "demo: Chladni-style sand on the bowed cymbal; the edge shimmer is invisible")
o(93, "Grains of rice lie on the head of a banjo; a string is plucked and the grains jump.",
      "The grains are still until the pluck, jump at the pluck and settle as the note fades; they do not move before the string is plucked.",
      ["person", "scene"], "demo: rice on the banjo head")
delete(13, "harp string blur: invisible at video resolution; the plucked-string idea is covered by ACOU-0002/0008/0011")
delete(15, "triangle sides shimmer: invisible; the hanging-ball demo now lives on the gong (ACOU-0003)")
delete(16, "fork tines blur: invisible; the tuning fork in water (ACOU-0007) covers it")
delete(20, "wind-chime tube outline shimmer: invisible; same class as the triangle/handbell")
delete(25, "hanging saucepan bottom shimmer: invisible; rice-on-lid demo (ACOU-0010) covers struck metal")
delete(28, "garbage-can lid quivering in a hand: invisible and duplicates ACOU-0010")
delete(31, "handbell rim shimmer: invisible; ball demo kept on the gong, water demo on the fork")
delete(34, "lampshade edge blur: invisible")
delete(43, "greenhouse glass rattling with fireworks: invisible on video; window-buzz idea kept in ACOU-0038/0040 with paper indicators")
delete(46, "belfry panes quivering with bell strokes: invisible; same as above")
delete(67, "a firework bang does not visibly shiver a lake's reflection: physics not sound")
delete(78, "harmonica reeds seen through the openings: not visible")
delete(82, "violin string blur under the bow: invisible; the cello (ACOU-0073) keeps the bowed-string case")
delete(87, "trumpet bell trembling: not visible")
delete(99, "bagpipe drones trembling: not visible")


# ---- 2026-09-14 second visibility pass (this session); keys are ORIGINAL ids
o(1, "Grains of rice lie on the head of a snare drum; the drum is struck once with a stick and the grains jump.",
     "The grains are still until the strike, leap up together at the strike and settle back within a second or two as the head goes quiet; they do not move before the stick lands.",
     ["person", "scene"], "demo: rice on the snare head; the head's shiver alone is not visible")
o(36, "A heavy truck rumbles past a house, and a teaspoon resting on a stack of plates by the window jiggles and chatters against the top plate.",
     "The spoon starts to jiggle as the truck approaches, moves most as it passes and lies still after it has gone; it does not move in a quiet street.",
     ["person", "scene"], "visible indicator: a spoon on the plates instead of the plates' tiny rattle")
o(45, "A car with a booming stereo pulls up at a light, and the fuzzy dice hanging from its rear-view mirror jiggle with the bass.",
     "The dice twitch in time with the beats and hang still when the music is turned down; they do not swing on their own.",
     ["person", "scene"], "visible indicator: hanging dice instead of the mirror's tiny shake")
o(49, "A subwoofer is turned up in a living room, and a picture frame on the wall behind it slowly tilts askew with the bass.",
     "The frame creeps out of level only while the bass plays, in small jerks, and stays where it ends up when the music stops; it does not straighten itself.",
     ["person", "scene"], "kept only the visible consequence (the tilt); the buzzing is not visible")
o(72, "A coin stands balanced on the hood of a car idling roughly, and it jitters and topples over.",
     "The coin trembles in place while the engine runs and eventually falls flat, staying down; it does not move before the engine starts or stand back up.",
     ["person", "scene"], "visible indicator: a balanced coin instead of the hood's faint tremble")
o(73, "A small paper rider sits on the string of a cello; a bow is drawn across that string and the rider is thrown off.",
     "The rider stays put until the bow touches the string, is flicked off as soon as the string sounds and does not return; riders on other strings stay still.",
     ["person", "scene"], "demo: paper rider on the bowed string; the string's blur is not visible")
o(86, "A desk fan with a bent blade is switched on, and the whole fan wobbles visibly on its base as the blades spin.",
     "The wobble starts as the blades spin up, keeps a steady rhythm while they turn, and is absent when the blades are still; the fan does not wobble before it is switched on.",
     ["person", "scene"], "whole-fan wobble is the visible part; base rattle and the switch-off half dropped")
delete(51, "pasta sheets buzzing above a dishwasher: not visible")
delete(55, "weight plates shivering after a dropped weight: not visible")
delete(57, "a bass drum does not visibly rock basketballs on a rack: physics doubtful")
delete(63, "a clock chime does not visibly shake a vase: not visible / doubtful")
delete(76, "strummed strings blurring then damped: high strings invisible; plucked-string idea covered by 2/8/20")
delete(81, "old telephone shaking while ringing: too small; the vibrating pager covers it")
delete(84, "razor head blur: duplicates the buzzing-device cases (phone, toothbrush, massager)")
delete(95, "hand-cranked siren casing vibration: not visible; only the crank is")
delete(98, "fridge compressor shudder and magnet quiver: too small")

o(100, "The figurine on a wind-up music box turns slower and slower as the spring runs down, and finally stops.",
     "The turning only slows, never speeds up, easing smoothly to a stop and then staying still; the figurine does not jerk, reverse, or start again after stopping; the mechanism inside need not be visible.",
     ["person", "scene", "timescale"], "user: the comb-and-pins mechanism is too technical and a full wind-down takes minutes; the clip shows the final slowing")

CLUSTERS = [
    ("struck_vibration: plucked string blurs and sharpens", ["ACOU-0002", "ACOU-0005", "ACOU-0008", "ACOU-0013", "ACOU-0019", "ACOU-0027", "ACOU-0030"]),
    ("struck_vibration: struck metal rings and shimmers", ["ACOU-0003", "ACOU-0006", "ACOU-0009", "ACOU-0010", "ACOU-0015", "ACOU-0020", "ACOU-0025",
                                                          "ACOU-0028", "ACOU-0031", "ACOU-0034"]),
    ("struck_vibration: clamped strip / ruler / rod flicked", ["ACOU-0004", "ACOU-0016", "ACOU-0017", "ACOU-0023", "ACOU-0032"]),
    ("struck_vibration: drum / membrane struck", ["ACOU-0001", "ACOU-0018", "ACOU-0026", "ACOU-0033"]),
    ("sound_driven: liquid surface ripples with a sound source", ["ACOU-0035", "ACOU-0044", "ACOU-0050", "ACOU-0056", "ACOU-0061", "ACOU-0062"]),
    ("sound_driven: glass / window buzzes with a loud source", ["ACOU-0038", "ACOU-0040", "ACOU-0043", "ACOU-0046"]),
    ("sound_driven: hanging object swings after a bang", ["ACOU-0037", "ACOU-0041", "ACOU-0048", "ACOU-0052"]),
    ("sound_driven: small objects rattle / hop with a motor or beat", ["ACOU-0036", "ACOU-0039", "ACOU-0042", "ACOU-0047", "ACOU-0058", "ACOU-0060", "ACOU-0064"]),
    ("source_motion: bowed string blurs only while the bow moves", ["ACOU-0073", "ACOU-0082", "ACOU-0089"]),
    ("source_motion: vibrating device creeps across a surface", ["ACOU-0069", "ACOU-0070", "ACOU-0075", "ACOU-0077"]),
    ("source_motion: motor shakes its own housing", ["ACOU-0072", "ACOU-0079", "ACOU-0083", "ACOU-0086", "ACOU-0090", "ACOU-0096", "ACOU-0098"]),
    ("source_motion: wind instrument trembles with breath", ["ACOU-0078", "ACOU-0087", "ACOU-0099"]),
]

# ---------------------------------------------------------------- build
import subprocess
MAP = ROOT / "data/acoustics_id_map.json"           # original id -> current id (exists once records were removed)
ORIG_COMMIT = "b55cde0"                              # acoustics.json with the original ids/captions
recs = json.loads(SRC.read_text())
orig = {r["id"]: r for r in json.loads(subprocess.run(["git", "-C", str(ROOT), "show", f"{ORIG_COMMIT}:data/train/acoustics.json"],
                                                      capture_output=True, text=True, check=True).stdout)}
old_to_new = json.loads(MAP.read_text())["old_to_new"] if MAP.exists() else {r["id"]: r["id"] for r in recs}
new_to_old = {v: k for k, v in old_to_new.items() if v}
out = []
stats = Counter()
for r in recs:
    oid = new_to_old.get(r["id"], r["id"])
    o_rec = orig[oid]
    c, e, ch, note = O.get(oid, (None, None, [], ""))
    new_c, new_e = (c if c else o_rec["caption"]), (e if e else o_rec["expectation"])
    applied = (r["caption"], r["expectation"]) == (new_c, new_e) and (new_c, new_e) != (o_rec["caption"], o_rec["expectation"])
    new = {
        "id": r["id"], "orig_id": oid, "category": r["category"], "subcategory": r["subcategory"],
        "violation_types": r["violation_types"],
        "caption": new_c, "expectation": new_e,
        "old_caption": o_rec["caption"], "old_expectation": o_rec["expectation"],
        "change": ch, "note": note, "applied_to_acoustics_json": applied,
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
by_id = {n["id"]: n for n in out}
by_sub = defaultdict(list)
for n in out:
    by_sub[n["subcategory"]].append(n)
deletes = [n for n in out if "delete" in n["change"]]
candidates = [n for n in out if "delete candidate" in n["note"].lower() and "delete" not in n["change"]]
lines = ["# Acoustics caption rewrite draft — changed records only", "",
         "Two principles: (1) **no people** unless the body is the physics; (2) the key change is **visible within 5-10 s** "
         "(every acoustic item already is; the branch's weakness is visibility of faint shimmers, flagged as delete candidates). "
         "Tags: **person** = player / striker removed (passive voice, object-state trigger, or a machine); a hand or palm only where it is the acting tool; "
         "breath left implicit for wind instruments · **expectation** = re-worded to match, or an action not in the caption dropped · "
         "**scene** = a different scene testing the same physics · **note** = unchanged, comment only · **delete** = proposed deletion (none). "
         "Unchanged records are omitted here but present in the JSON.", "",
         f"Counts: {len(out)} records; " + ", ".join(f"{k} {v}" for k, v in sorted(stats.items())) + ".", ""]
if deletes:
    lines += ["## Proposed deletions", ""]
    for n in deletes:
        lines.append(f"- **{n['id']}** ({n['subcategory']}): {n['note']}  \n  _{n['old_caption']}_")
    lines.append("")
lines += ["## Delete candidates (user decides; a rewrite is still given)", ""]
for n in candidates:
    lines.append(f"- **{n['id']}** ({n['subcategory']}): {n['note']}")
lines += ["", "## Near-duplicate clusters (thin out to 3-5 per phenomenon)", ""]
for title, ids in CLUSTERS:
    lines.append(f"- **{title}**: " + ", ".join(ids))
lines.append("")
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
