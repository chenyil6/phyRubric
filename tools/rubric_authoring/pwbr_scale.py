# phyworldbench 246-280: Scale and Proportions.
# Same authoring flow as the earlier blocks. Cross-check against KS[i] -- id 262 is one of the
# eleven dict-wrapped records.
#
# Every scenario here is a COMPARISON: two objects of different size or thickness under the same
# influence. So SA asserts that both objects are present and both are subjected to the influence,
# and PC judges the relative behaviour. Relative judgements ('the pebble is faster than the
# boulder') need no measurement, so they do not fall under _policy.json's numeric exclusion; what
# is excluded is any absolute amount.
#
# This category has the worst physics in the benchmark, in three distinct ways.
#
# First, the gravity-driven scenarios reward the Aristotelian misconception outright. 247 and 249
# require the smaller body to accelerate visibly faster down the slope, when gravitational
# acceleration -- sliding or rolling -- is independent of mass; and 260 requires the LARGER stone
# to roll faster, so the benchmark's own standards for the same situation contradict each other in
# opposite directions. Both entries here follow the mass-independence and their notes say so.
#
# Second, several standards demand something video cannot show or physics does not provide: 257
# wants rocks to visibly change colour as they warm by a campfire, 266 wants audio-frequency bell
# vibration to be watched, 280 asserts that the larger balloon pops at HIGHER pressure when the
# membrane law gives the opposite.
#
# Third, the benchmark contradicts itself between records: 268 requires a full-scale bridge to
# show no visible bending under load while 279 requires a suspension bridge to dip noticeably; 271
# requires a skyscraper to show no significant sway while 277 requires a tall building to
# oscillate visibly.


def both(a, b):
    return [('core', f'{a[0].upper()}{a[1:]} is present.'),
            ('core', f'{b[0].upper()}{b[1:]} is present.')]


def cons2(a, b):
    return ('fatal',
            f'{a[0].upper()}{a[1:]} and {b} each keep their own identity and size for the whole '
            f'shot, and neither passes through anything solid.',
            f'either object changes size or identity mid-shot, passes through something solid, or '
            f'disappears and re-appears')


def same_scene(a, b):
    return ('major', f'{a[0].upper()}{a[1:]} and {b} are in the same scene under the same '
                     f'conditions, so the comparison is like for like.',
            f'the two are shown in different places or under plainly different conditions and '
            f'cut together')


def fixed(o):
    pl = ' and ' in o
    return ('minor',
            f'{o[0].upper()}{o[1:]} stay put and keep their shape throughout.' if pl else
            f'{o[0].upper()}{o[1:]} stays put and keeps its shape throughout.',
            f'{o} shift, flex or change shape on their own' if pl else
            f'{o} shifts, flexes or changes shape on its own')


# ---- Consistency of Forces Across Scales (246-252) -----------------------
add('applied-force-mass-response', 246,
    'The kids set the toy moving easily, while the full-sized plane barely responds to the same '
    'pushing.',
    S(*both('a small toy airplane', 'a full-sized airplane'),
      ('core', 'Kids push both along the ground.'),
      ('minor', 'The pushes read as comparable effort rather than one being token.')),
    P(cons2('the toy', 'the full-sized airplane'),
      ('core', 'The toy responds far more to the pushing: it gets moving quickly and covers ground, '
               'while the full-sized plane moves barely or not at all.',
       'the airliner rolls away as readily as the toy under a child\'s push, or the toy is the one '
       'that will not move'),
      ('core', 'Each moves only while and after being pushed, in the direction of the push.',
       'either one sets off before being touched, or moves against the direction it is pushed'),
      ('major', 'If the big plane does move, it starts imperceptibly slowly and keeps its slow '
                'pace; it does not surge.',
       'the full-sized plane jumps from rest to walking pace under a single push'),
      ('major', 'The toy, once released, slows and stops rather than rolling on for ever.',
       'the toy holds its speed indefinitely after the push ends'),
      same_scene('the toy', 'the full-sized airplane'),
      ('minor', 'The kids brace and lean into the big plane far more than into the toy.',
       'a child moves the airliner one-handed with the same posture as for the toy')),
    note="Their standards -- more effort for the larger plane, slower acceleration and less ground "
         "per push -- are correct here, because this is an APPLIED force: the same push on a "
         "thousand-fold mass gives a thousand-fold smaller acceleration. This is the one scenario "
         "in the first subcategory where 'bigger responds less' is right, and it is worth saying "
         "why: it contrasts with 247, 249 and 260, where the driving force is gravity, which scales "
         "with the mass and cancels out. The caption's premise -- children budging a full-sized "
         "aircraft -- is generous, and the rubric allows the correct outcome that it fails to move "
         "at all.")

add('slope-descent-mass-independence', 247,
    'The same push starts the pebble off faster, but on the slope itself both gather speed at the '
    'same rate.',
    S(*both('a small pebble', 'a large boulder'),
      ('core', 'Both are rolled down a hill.'),
      ('minor', 'Both are started with a comparable push, as the caption says.')),
    P(cons2('the pebble', 'the boulder'),
      ('core', 'Both gather speed on the way down.',
       'either stone rolls downhill at a constant speed throughout, or slows while still on the '
       'slope with nothing in its way'),
      ('core', 'On the slope itself the boulder gains speed at least as readily as the pebble: it '
               'is not left visibly crawling while the pebble accelerates away.',
       'the boulder creeps down the hill, accelerating far more slowly than the pebble, as though '
       'its weight held it back'),
      ('major', 'Any early lead the pebble has comes from the start, where the same push moves the '
                'light stone off faster.',
       'the two leave the top at the same speed and the pebble then out-accelerates the boulder on '
       'the open slope'),
      ('major', 'Both roll: they turn as they travel, and neither slides down frozen.',
       'either stone glides down the slope without turning at all'),
      ('major', 'The boulder is harder to stop or deflect: bumps that scatter the pebble barely '
                'disturb it.',
       'the boulder is knocked off course by small stones that the pebble rolls straight over'),
      same_scene('the pebble', 'the boulder'),
      ('minor', "Each stone's surface mottling turns with it as it rolls.",
       'the markings on a stone hold still in space while the stone rotates under them')),
    note="Their second standard requires the pebble to accelerate quickly and overtake the boulder "
         "'early in the descent', which rewards the Aristotelian misconception: gravity-driven "
         "acceleration is independent of mass, rolling or sliding, so on the slope the two gain "
         "speed at the same rate. What IS real is the start -- the caption applies the same force "
         "to both, and the same impulse launches the light pebble faster -- so the rubric puts the "
         "pebble's lead at the start and requires equal acceleration on the slope. Note that their "
         "standard for scenario 260, the same situation, demands the OPPOSITE (the larger stone "
         "faster), so the benchmark contradicts itself between the two records.")

add('drag-dominated-comparison', 248,
    'The stone drops fast and straight while the feather settles slowly, carried by the air.',
    S(*both('a feather', 'a stone'),
      ('core', 'Both are dropped in the air.'),
      ('minor', 'Both are released from rest rather than thrown.')),
    P(cons2('the feather', 'the stone'),
      ('core', 'The stone falls much faster than the feather and lands well before it.',
       'the two fall together at the same rate in open air, or the feather lands first'),
      ('core', 'The feather drifts: it rocks, glides sideways and takes a wandering path down.',
       'the feather drops straight down like a pellet, only slower'),
      ('major', 'The stone speeds up as it falls.',
       'the stone drifts down at one unchanging slow speed'),
      ('major', 'The feather settles at a slow, roughly steady rate rather than accelerating '
                'throughout.',
       'the feather keeps gaining speed all the way down like a dense object'),
      ('major', 'Both go downward overall; neither hangs or climbs.',
       'the feather hovers at one height indefinitely, or either object rises'),
      same_scene('the feather', 'the stone'),
      ('minor', 'The feather reads as light throughout: it never dents or scatters what it lands '
                'on.',
       'the feather lands with a thud, denting or scattering what it hits')),
    note="Their standards -- the stone much faster with a clear consistent difference, the feather "
         "slow and gentle -- are correct and are used. The additions distinguish HOW each falls, "
         "not just how fast: the stone accelerates while the feather reaches a slow terminal drift "
         "almost at once and takes an unsteady path. Scenario 54, 'A feather falls to the ground', "
         "carries air-resistance-descent for the feather alone; scenario 250 is the deliberate "
         "vacuum contrast where this difference must vanish.")

add('slope-descent-mass-independence', 249,
    'Released together on identical ramps, the toy car and the real car gather speed together.',
    S(*both('a toy car', 'a real car'),
      ('core', 'Each rolls down a ramp, and the ramps are alike.'),
      ('minor', 'Both are released rather than driven or pushed off.')),
    P(cons2('the toy car', 'the real car'),
      ('core', 'Both gather speed on the way down.',
       'either car holds one speed on the slope, or slows on the way down with nothing in its way'),
      ('core', 'Neither car visibly out-accelerates the other on the ramps: released together, they '
               'stay roughly abreast.',
       'the toy pulls away down the ramp while the real car crawls, or the real car charges ahead '
       'while the toy dawdles'),
      ('major', 'The wheels of each car turn with its motion.',
       'either car slides down with its wheels locked and unturning'),
      ('major', 'Both run straight down their ramps.',
       'either car swerves off its ramp with nothing deflecting it'),
      ('major', 'At the bottom, the real car runs on farther before stopping than the toy does.',
       'the toy coasts on across the ground while the real car stops dead at the ramp foot'),
      same_scene('the toy car', 'the real car'),
      ('minor', 'Each car keeps its size against its own ramp all the way down.',
       'either car visibly grows or shrinks against its ramp as it descends')),
    note="Their sole standard, that the toy accelerates 'observably faster' initially, rewards the "
         "same misconception as 247: on identical slopes, gravity-driven acceleration does not "
         "depend on mass, so the two cars gain speed together, and if anything the toy loses more "
         "to bearing friction and air drag at its scale. Their physics_prompt's 'accelerating "
         "proportionally to their size' has no meaning at all. The one real size effect is at the "
         "bottom: the real car carries relatively more momentum against its losses and coasts "
         "farther, which is the major item here.")

add('vacuum-free-fall', 250,
    'With no air, the feather and the stone fall side by side at the same rate.',
    S(*both('a feather', 'a stone'),
      ('core', 'They are dropped inside a vacuum chamber.'),
      ('minor', 'The chamber reads as a sealed apparatus rather than open air.')),
    P(cons2('the feather', 'the stone'),
      ('core', 'The feather and the stone fall at the same rate and stay level with each other all '
               'the way down.',
       'the stone pulls ahead of the feather on the way down, or the feather leads'),
      ('core', 'The feather falls straight, without the rocking, gliding drift it shows in air.',
       'the feather flutters and wanders on the way down as though air were catching it'),
      ('major', 'Both accelerate: they leave slowly and are moving fastest at the bottom.',
       'the pair descend at one unchanging speed from the moment of release'),
      ('major', 'Both land together.',
       'one lands clearly before the other after a level start'),
      ('minor', 'They are released together, from rest, at the same height.',
       'one is let go before the other, or from a different height, so the comparison is spoiled'),
      fixed('the chamber')),
    note="Their sole standard -- identical downward velocity with no lag -- is correct and is the "
         "core here. The additions are the feather's path, which must lose its fluttering once "
         "there is no air to cause it, and the shared acceleration: equal rates does not mean "
         "constant speed, and a pair drifting down together at fixed speed is as wrong as a stone "
         "outpacing the feather. Scenario 248 is the deliberate in-air contrast.")

add('glide-scaling', 251,
    'Both fly and both descend, but the paper plane dies away quickly while the glider carries on '
    'far.',
    S(*both('a paper airplane', 'a full-sized glider'),
      ('core', 'Both are thrown or launched into flight.'),
      ('minor', 'Both are unpowered -- no propeller or engine on the glider.')),
    P(cons2('the paper airplane', 'the glider'),
      ('core', 'The paper plane loses speed and height quickly, while the glider carries its speed '
               'on and covers far more distance.',
       'the paper plane sails on as far as the glider, or the glider stalls and drops as soon as '
       'the paper plane does'),
      ('core', 'Both descend overall: neither climbs steadily or holds height indefinitely without '
               'power.',
       'either aircraft cruises on at fixed height for the whole shot, or climbs away with nothing '
       'driving it'),
      ('major', 'The glider descends along a shallower slope than the paper plane.',
       'the glider comes down as steeply as the paper plane, or more steeply'),
      ('major', 'Each flies nose first along its path.',
       'either aircraft travels sideways or tail first while still tracking a smooth path'),
      ('minor', 'The paper plane is the twitchier of the two: it wavers and porpoises where the '
                'glider flies smoothly.',
       'the glider jitters about while the little paper plane holds a perfectly steady line'),
      same_scene('the paper airplane', 'the glider')),
    note="Their standards -- the paper plane slowing noticeably faster, the glider travelling much "
         "farther -- are correct scaling and are used: the larger aircraft flies at higher Reynolds "
         "number with a better lift-to-drag ratio, so it keeps its speed and glides flatter. The "
         "addition is that both still descend, which keeps this consistent with scenario 4, the "
         "paper airplane alone, whose benchmark standard wrongly demanded level flight.")

add('impulse-scaling', 252,
    'The small hammer moves the nail a little with each tap; the sledgehammer drives it home in one '
    'blow.',
    S(*both('a small hammer', 'a sledgehammer'),
      ('core', 'Each is used to strike a nail.'),
      ('minor', 'The nails and the material they are driven into read as alike.')),
    P(('fatal', 'A nail moves only when and where a hammer strikes it.',
       'a nail sinks in before the blow lands, or goes on sinking between blows with nothing '
       'touching it'),
      ('core', 'Each tap of the small hammer advances its nail a little, and it takes several to '
               'drive it.',
       'the small hammer sinks the nail flush in a single light tap'),
      ('core', 'The sledgehammer drives its nail far deeper per blow than the small hammer does.',
       'the sledgehammer blow moves the nail no further than one tap of the small hammer'),
      ('major', 'Nails only ever go further in; they do not rise back out between blows.',
       'a nail creeps back out of the wood after the hammer lifts'),
      ('major', 'The nail advances along its own line, staying straight or bending -- not '
                'teleporting deeper.',
       'the nail is suddenly deeper without having moved through the intervening depth'),
      ('minor', 'The sledgehammer is swung slower and with the whole body; the small hammer is '
                'flicked from the wrist.',
       'the sledgehammer is flicked about one-handed as lightly as the tack hammer'),
      ('minor', 'The struck material marks around the nail -- dents or fibres raised -- under the '
                'heavy blows.',
       'repeated sledgehammer blows leave the surface around the nail perfectly pristine')),
    note="Their standards -- light taps advancing the nail gradually, a single powerful strike "
         "driving it much deeper -- are correct and are used. The additions are monotonicity (a "
         "nail never backs out on its own) and the way each tool is handled, which is how a clip "
         "shows mass without any number: a sledgehammer is swung slowly with the whole body "
         "because it is heavy, and a clip that waves it like a wand has the mass wrong.")

# ---- Environmental Effects on Different Scales (253-259) ------------------
add('droplet-load-scaling', 253,
    'Each raindrop is a real load to the flower and nothing at all to the tree.',
    S(*both('a small flower', 'a large tree'),
      ('core', 'Light rain falls on both.'),
      ('minor', 'The rain reads as light -- separate drops rather than a downpour.')),
    P(cons2('the flower', 'the tree'),
      ('core', 'The flower visibly moves under the rain: it dips or trembles when drops strike it.',
       'the flower stands rigid and untouched while drops plainly land on it'),
      ('core', 'The tree as a structure is unmoved by the rain: its trunk and branches do not stir '
               'for the drops.',
       'the tree\'s branches bow and sway under light raindrops as the flower does'),
      ('major', 'The flower moves when it is struck, and springs back between drops.',
       'the flower stays pressed down permanently under light rain, or it sways continuously '
       'without regard to when drops hit it'),
      ('major', 'On the tree, at most individual leaves twitch when hit; the movement stays at leaf '
                'scale.',
       'a whole limb of the tree jerks each time a raindrop lands'),
      ('minor', 'Drops that land run off or cling as droplets on both plants.',
       'the rain vanishes on contact, leaving both plants dry'),
      ('minor', 'Falling drops move downward.',
       'raindrops drift upward or hang in the air')),
    note="Their standards -- the drops visibly bend the flower, the tree remains upright and "
         "unaffected -- are correct and are used. The refinement is where the tree's stillness "
         "lives: individual leaves may twitch when struck, but the structure does not move, so the "
         "rubric separates leaf-scale response from branch-scale response. The flower's recovery "
         "between drops is the other addition, and is what distinguishes a load response from a "
         "flower simply drooping.")

add('wind-response-scaling', 254,
    'The breeze picks the leaf up and carries it, while the branch only sways in place.',
    S(*both('a leaf', 'a tree branch'),
      ('core', 'A light breeze blows over them.'),
      ('minor', 'The breeze shows in other things too -- grass, dust or other foliage.')),
    P(cons2('the leaf', 'the branch'),
      ('core', 'The leaf is picked up and carried: it travels with the breeze rather than staying '
               'where it was.',
       'the leaf stays put on the ground through a breeze that plainly moves other things, or it '
       'shoots off faster than the wind that carries it'),
      ('core', 'The branch stays attached and in place: it sways about its position but is not '
               'carried anywhere.',
       'the branch is torn off and carried along by a light breeze, or it whips about violently'),
      ('major', 'The leaf tumbles and skips rather than sliding along smoothly like a puck.',
       'the leaf glides along the ground at constant height and attitude as though on rails'),
      ('major', 'Leaf and branch respond to the same gusts at the same times.',
       'the leaf flies about while the branch and everything else stand in dead calm'),
      ('major', 'The branch bends away from the wind when it sways, most at its thin end.',
       'the branch sways into the wind, or bends most at its thick base'),
      ('minor', 'When the breeze eases, the leaf settles and the branch comes back to rest.',
       'both carry on moving just as hard after the air has plainly gone still')),
    note="Their first standard is half rendering ('smoothly and naturally, with no abrupt changes') "
         "but its physical half -- the leaf lifted and carried -- is used; their second, the branch "
         "swaying with limited movement, is used as written. The additions are the coupling in time "
         "(one breeze drives both) and the tumbling character of leaf transport, which is what "
         "separates a blown leaf from a leaf slid across the ground. Scenario 29, the tumbleweed, "
         "carries wind-driven-tumbling for the carried case alone; scenario 216 carries the bending "
         "branch alone.")

add('wave-response-scaling', 255,
    'The small boat rides up and down with every wave; the big boat barely notices them.',
    S(*both('a small boat', 'a large boat'),
      ('core', 'Both float on ocean waves.'),
      ('minor', 'Waves are visible and comparable around both boats.')),
    P(cons2('the small boat', 'the large boat'),
      ('core', 'The small boat rises and falls markedly with the waves, pitching and rolling as '
               'they pass.',
       'the small boat sits glassy-still in a visible swell'),
      ('core', 'The large boat moves far less in the same water: the waves that toss the small boat '
               'leave it nearly steady.',
       'the large boat pitches and rolls as hard as the small one in the same swell'),
      ('major', 'The small boat moves in time with the waves passing under it.',
       'the small boat bobs to a rhythm unrelated to the waves around it'),
      ('major', 'Both stay afloat at their waterlines; neither ships water or rides up out of the '
                'sea.',
       'either boat sinks lower and lower, or lifts clear of the water, with nothing acting on it'),
      ('major', 'Waves pass under the boats and carry on; the boats do not travel along with the '
                'crests.',
       'a boat surfs along with a wave crest across the whole shot without power'),
      same_scene('the small boat', 'the large boat'),
      ('minor', "Each boat's markings and fittings move with its hull.",
       'the hull markings hold still against the sea while the boat pitches under them')),
    note="Their standards -- significant vertical motion for the small boat, minimal movement for "
         "the large -- are correct and are used: a hull short against the wavelength follows the "
         "surface while a hull long against it averages the waves out. The additions are phase (the "
         "small boat must move in time with the waves that cause it) and the distinction between "
         "the wave shape travelling and the water and boats staying, which scenario 128 carries for "
         "a buoy.")

add('surface-freezing', 256,
    'Overnight cold freezes the shallow puddle solid but only puts a lid on the deep pond.',
    S(*both('a small puddle', 'a deep pond'),
      ('core', 'Both freeze overnight -- ice forms on both during the shot.'),
      ('minor', 'The passage of the night is conveyed -- darkness, a timelapse, or morning light at '
                'the end.')),
    P(('fatal', 'Ice forms from the surface and edges of the water, not from the middle of the '
                'depth upward.',
       'ice appears as a slab in mid-water with liquid above it, or forms at the bottom while the '
       'surface stays open'),
      ('core', 'The puddle ends up frozen through: solid, walkable-looking ice with no liquid '
               'remaining.',
       'the puddle still sloshes as liquid at the end while the pond has frozen over'),
      ('core', 'The pond freezes only at its surface: a lid of ice with liquid water below.',
       'the whole depth of the pond turns solid overnight'),
      ('major', 'The puddle skins over before the pond does.',
       'the deep pond is sealed with ice while the shallow puddle beside it is still open water'),
      ('major', 'Freezing only advances while it stays cold; ice does not retreat overnight.',
       'ice forms and then melts back repeatedly through a night that reads as continuously cold'),
      ('minor', 'The ice is distinguishable from the open water -- duller, frosted, or catching the '
                'light differently.',
       'frozen and unfrozen water look identical, with nothing marking where the ice is'),
      ('minor', 'Frost appears on the surroundings as well.',
       'the ground and plants around freezing water stay conspicuously frost-free')),
    note="Their standards -- the puddle freezing completely and quickly, the pond only at the "
         "surface with liquid beneath -- are correct and are used. The addition is where ice is "
         "allowed to form: it grows from the surface down and the edges in, because water loses "
         "heat at the top and ice floats, so a clip that freezes the pond from the bottom up has "
         "the mechanism backwards even if it gets the end state right.")

add('thermal-mass-response', 257,
    'The fire warms both stones invisibly: neither the small rock nor the boulder glows or changes '
    'colour.',
    S(('core', 'A campfire is present and burning.'),
      ('core', 'A small rock and a large boulder are near it.'),
      ('minor', 'Both stones are at comparable distances from the fire.'),
      ('minor', 'The fire burns through the shot rather than dying at once.')),
    P(cons2('the small rock', 'the boulder'),
      ('core', 'Neither stone glows, changes colour or shimmers from the warming: rock heated by a '
               'campfire stays looking like rock.',
       'either stone begins to glow, change colour or radiate visibly as it warms'),
      ('core', 'The stones do not move, soften or deform from being warmed.',
       'a stone slumps, cracks apart or shifts merely from sitting near the fire'),
      ('major', 'Any visible signs of warming are indirect and belong to the surface: dampness '
                'drying, frost or snow receding, at most a heat shimmer in the air above.',
       'visible change is painted onto the stone itself rather than carried by water, frost or the '
       'air',
       'the stones are damp, frosted or snow-dusted at the start'),
      ('major', 'If such indirect signs appear, they appear on the small rock before the boulder.',
       'the boulder dries or sheds its frost before the small rock does',
       'drying or frost retreat is visible on either stone'),
      ('major', 'Shadows of the stones fall away from the fire and flicker with it.',
       'the shadows of the stones point toward the flames, or hold rigid while the flames move'),
      ('minor', 'The fire lights the near faces of both stones, and the flicker on them follows the '
                'flames.',
       'the stones stay unlit by a fire right beside them, or the light on them holds steady while '
       'the flames dance'),
      fixed('the fireplace and the ground')),
    note="Both of their standards require the stones to 'visibly change appearance or color' as "
         "they warm and cool, which video cannot deliver honestly: campfire-warmed rock stays far "
         "below incandescence, and temperature has no direct visual signature. A clip that obliges "
         "-- a rock blushing red as it warms -- is inventing exactly the effect a physics judge "
         "should penalise, so this rubric inverts their standards into a prohibition. The real "
         "thermal-mass comparison they were after survives only in indirect, water-borne signs "
         "(drying, frost retreat), which are gated behind a precondition since most clips will not "
         "provide them.")

add('runoff-on-glass', 258,
    'Rain behaves the same on both panes: drops bead, merge and run down each surface along its '
    'slope.',
    S(*both('a car windshield', 'a skyscraper window'),
      ('core', 'Raindrops fall on both.'),
      ('minor', 'Both surfaces are seen closely enough to make out individual drops or streams.')),
    P(('fatal', 'The water runs down each surface, following its slope.',
       'streams run uphill across either pane, or straight down a windshield that is plainly '
       'raked back'),
      ('core', 'The drop physics is the same on both: drops land, bead, merge with neighbours and '
               'release into runnels on the windshield just as on the window.',
       'the two panes show different physics -- drops beading on one and vanishing on the other, '
       'or merging on one and never merging on the other'),
      ('core', 'Runnels only grow or merge as they descend, fed by the drops they collect.',
       'a stream splits into drops that climb back up, or streams shrink away while rain keeps '
       'falling'),
      ('major', 'More rain gives more and faster runoff on both panes alike.',
       'the rain visibly hardens while the runoff on one pane stays unchanged'),
      ('major', 'The paths differ only as the surfaces do: streams on the vertical window run '
                'straighter and faster than on the raked windshield.',
       'water races down the shallow windshield while crawling down the vertical window beside it'),
      ('minor', 'Drops and streams distort what is seen through the glass where they lie.',
       'the glass scene shows through beaded water completely undistorted'),
      ('minor', 'Both panes stay rigid and fixed as the water moves over them.',
       'either pane ripples or flexes under the rain')),
    note="Their standards assert that windshield drops flow 'quickly, forming larger, faster-moving "
         "streams' while skyscraper drops move 'more slowly' in finer patterns -- attributing to "
         "pane SIZE a difference that size does not make, and contradicting their own "
         "physics_prompt, which says the drops behave 'identically' with only runoff patterns "
         "differing. Drop behaviour is set by the surface's tilt and coating, and if anything the "
         "vertical window drains faster than the raked windshield -- the reverse of their claim. "
         "This rubric requires the same drop physics on both and lets only the geometry differ.")

add('flame-gust-response', 259,
    'The gust nearly kills the candle flame but feeds the bonfire, which flares and throws sparks.',
    S(*both('a candle flame', 'a bonfire'),
      ('core', 'A gust of wind arrives during the shot.'),
      ('minor', 'The gust shows in other things too -- smoke, foliage or dust moving.')),
    P(('fatal', 'Both flames react when the gust arrives, and in the direction the gust blows.',
       'the flames lean into the wind, or one flame whips about while the other and everything '
       'else stand in dead calm'),
      ('core', 'The candle flame is nearly overwhelmed: it flattens, gutters and shrinks, and may '
               'go out.',
       'the candle flame burns on upright and steady through a gust that visibly bends the bonfire'),
      ('core', 'The bonfire is fed by the same gust: it brightens and flares rather than shrinking.',
       'the bonfire is snuffed low by the same brief gust, dimming while the candle merely flickers'),
      ('major', 'The bonfire\'s flare carries sparks and embers downwind.',
       'sparks fly off against the wind, or the flare produces no movement of sparks or smoke at '
       'all'),
      ('major', 'After the gust passes, each flame relaxes back: the candle steadies or stays out, '
                'the bonfire settles.',
       'the flames go on raging identically long after the air has stilled'),
      ('minor', 'If the candle goes out, smoke rises from its wick afterwards.',
       'the candle is snuffed and the wick shows nothing at all',
       'the candle goes out during the shot'),
      ('minor', 'The two responses happen at the same moment, driven by the one gust.',
       'the candle reacts to the gust long before or after the bonfire does')),
    note="Their standards -- the candle flame bending, wavering and nearly extinguishing; the "
         "bonfire flaring with sparks and embers carried away -- are correct and unusually "
         "complete, and both are used. The additions are the couplings: both flames answer the "
         "same gust at the same time and in its direction, and both relax when it passes. The "
         "smoke-after-extinction item ties to scenario 113, where the blown-out candle is the whole "
         "scenario.")

# ---- Proportional Energy Transfer (260-266) -------------------------------
add('slope-descent-mass-independence', 260,
    'Rolled together down the slope, the two stones gather speed at the same rate.',
    S(*both('a small stone', 'a large stone'),
      ('core', 'Both are rolled down a slope.'),
      ('minor', 'They start together, from about the same point.')),
    P(cons2('the small stone', 'the large stone'),
      ('core', 'Both gather speed on the way down.',
       'either stone descends at one unchanging speed, or slows mid-slope with nothing in its way'),
      ('core', 'Neither stone visibly out-accelerates the other on the slope: rolled off together, '
               'they descend roughly abreast.',
       'the large stone pulls steadily away from the small one on the slope, or the small one '
       'leaves the large one crawling'),
      ('major', 'Both turn as they travel.',
       'either stone slides down frozen, without rolling'),
      ('major', 'The large stone is the harder to stop: at the bottom it ploughs on farther '
                'through grass or debris than the small one.',
       'the small stone barrels on through obstructions while the large one is stopped by them'),
      ('major', 'Small bumps deflect the small stone more than the large one.',
       'the boulder is bounced off course by pebbles the small stone rolls straight over'),
      same_scene('the small stone', 'the large stone'),
      ('minor', "Each stone's surface texture turns with it as it rolls.",
       'the mottling on a stone holds still in space while the stone rotates under it')),
    note="Their standards require the LARGER stone to roll 'noticeably faster' and farther -- the "
         "mirror image of scenario 247, where the SMALLER body had to be faster, so the benchmark "
         "asserts both directions of the same error for the same situation. Neither is right: "
         "gravity-driven descent is mass-independent, and 'gathering more kinetic energy' (their "
         "physics_prompt) is about energy, not speed. The real size effects are downstream -- more "
         "momentum against obstructions, less deflection by bumps -- and those are the major items "
         "here. The note on 247 records the contradiction from the other side.")

add('spring-compression', 261,
    'Under the same hands, the small spring closes up easily while the large one gives far less.',
    S(*both('a small spring', 'a large spring'),
      ('core', 'Both are compressed by hand.'),
      ('minor', 'The efforts read as comparable -- the same person or grip on each.')),
    P(cons2('the small spring', 'the large spring'),
      ('core', 'The small spring closes visibly further under the same handling than the large one.',
       'the heavy spring squashes flat under a light grip while the small one resists, or both '
       'compress identically'),
      ('core', 'Each spring shortens with its coils closing evenly, and returns to length when '
               'released.',
       'a spring shortens with its coil spacing unchanged, or stays short after the hands open'),
      ('major', 'The compression happens while the hands squeeze and not before or after.',
       'a spring compresses before it is gripped, or goes on compressing after the grip relaxes'),
      ('major', 'The large spring visibly costs more effort: the hands and arms work harder on it.',
       'the compressing hand is as relaxed on the stiff spring as on the soft one'),
      ('major', 'Neither spring\'s coils pass through each other.',
       'coils overlap or interpenetrate as a spring closes'),
      ('minor', 'On release, each spring springs back quickly, the small one moving the faster.',
       'the springs ease back open as slowly as they were squeezed')),
    note="Their standards -- the small spring compressing quickly with less resistance, the large "
         "one slowly with more, under equal force -- are correct and are used. The additions are "
         "the coil mechanics shared with scenario 222 (even closing, no interpenetration, full "
         "return), and effort made visible through the hands, which is how a clip conveys force "
         "without numbers. Scenarios 66 and 222 carry this mechanism for a single spring.")

add('impact-ripples', 262,
    'Both splashes ring the water, but the boulder\'s splash and waves dwarf the pebble\'s.',
    S(*both('a pebble', 'a boulder'),
      ('core', 'Both are thrown into a lake.'),
      ('minor', 'They land far enough apart that the two wave patterns can be told apart.')),
    P(('fatal', 'Each splash and ring pattern starts where and when its stone strikes the water.',
       'waves spread from a point where nothing landed, or before the stone arrives'),
      ('core', 'The boulder\'s entry throws a far bigger splash and taller waves than the pebble\'s.',
       'the two stones raise splashes of about the same size, or the pebble\'s is the bigger'),
      ('core', 'Both sets of rings spread outward and fade with distance.',
       'either set of rings closes inward, holds its height as it spreads, or freezes in place'),
      ('major', 'The boulder\'s waves reach farther and keep going after the pebble\'s rings have '
                'died away.',
       'the pebble\'s rings outlast and outrun the boulder\'s'),
      ('major', 'Both stones sink.',
       'either stone floats on the surface after landing'),
      ('minor', 'Where the two ring patterns meet they pass through each other rather than '
                'stopping.',
       'the ring patterns collide and annihilate at a hard boundary',
       'the two ring patterns spread far enough to overlap'),
      same_scene('the pebble', 'the boulder'),
      ('minor', 'The lake beyond the two ring systems stays calm.',
       'the whole lake churns although only two stones went in')),
    note="This is one of the eleven dict-wrapped records. Its real standards -- larger, "
         "farther-spreading, longer-lasting waves from the boulder, and a larger initial splash -- "
         "are correct and are used. The additions are the fading of both patterns with distance, "
         "which scenario 107 carries for a single stone and whose mechanism this rubric shares, "
         "and the superposition of the two ring systems where they cross.")

add('struck-membrane-response', 263,
    'The same stick strike dents the big drumhead visibly more, and both heads recover at once.',
    S(*both('a small drum', 'a large drum'),
      ('core', 'Each is struck with a drumstick.'),
      ('minor', 'The strikes read as comparable -- same player, similar swing.')),
    P(cons2('the small drum', 'the large drum'),
      ('core', 'Each drumhead gives under the stick at the moment of the strike and springs back at '
               'once.',
       'a head stays dented after the stick has left it, or never deflects at all under a plain '
       'strike'),
      ('core', 'The large drum\'s head visibly moves more under the same strike than the small '
               'drum\'s.',
       'the small head billows while the big one stays rigid under equal strikes'),
      ('major', 'The stick rebounds off each head rather than stopping dead or sinking in.',
       'the stick buries itself in the head, or halts on contact with no bounce'),
      ('major', 'Any visible after-motion of a head dies out quickly rather than continuing.',
       'a drumhead goes on visibly waving for the rest of the shot after one strike'),
      ('minor', 'Things resting on or near a drum jump at the strike.',
       'objects sitting on the struck drum stay perfectly still',
       'something rests on or against either drum'),
      ('minor', 'The drums themselves stay put under the strikes.',
       'a drum skids or topples from an ordinary stick strike')),
    note="Their standards ask to compare 'vibrations' and 'surface displacement' between the "
         "drums, but a drumhead's sustained vibration is at audio frequency and is invisible at "
         "video frame rates -- what a clip can actually show is the initial deflection under the "
         "stick and its immediate recovery. The rubric therefore judges the strike-moment "
         "deflection, where the larger, looser head does move visibly more, and requires any "
         "residual waving to die quickly, since a head that visibly oscillates for seconds is the "
         "invented version of resonance. Scenario 266 has the same problem with bells.")

add('trampoline-rebound', 264,
    'The adult dishes the trampoline bed far deeper than the child, and each is thrown back up in '
    'proportion.',
    S(('core', 'A trampoline is present.'),
      ('core', 'A child and an adult jump on it.'),
      ('minor', 'Their jumps are comparable -- similar rhythm and effort.')),
    P(('fatal', 'The bed stretches down only while and where someone is on it, and no one passes '
                'through it.',
       'the bed dishes with nobody on it, or a jumper passes through the mesh'),
      ('core', 'The adult\'s landing dishes the bed visibly deeper than the child\'s.',
       'the child sinks the bed as deep as the adult, or deeper'),
      ('core', 'The bed returns flat between bounces and throws each jumper back up.',
       'the bed keeps a permanent hollow, or a jumper sinks in and stays'),
      ('major', 'The deformation is under the jumper and follows them.',
       'the bed dishes away from where the jumper lands'),
      ('major', 'The child is not flung wildly higher than the adult by the same bed.',
       'the light child is launched out of frame while the adult barely leaves the mat, with '
       'similar effort'),
      ('major', 'Each jumper\'s rise and fall is smooth: slowing at the top, fastest at the bed.',
       'a jumper hangs at the top of their arc, or rises and falls at one constant speed'),
      ('minor', 'The frame and springs stay put; the stretch is in the bed.',
       'the frame flexes as much as the bed with each jump')),
    note="Their standards -- a larger, more noticeable depression from the adult, a lighter, "
         "gentler bounce for the child -- are correct and are used. This scenario is the "
         "comparative version of 80 and 220 and carries their mechanism; the items shared with "
         "those (recovery between bounces, the dish following the jumper) are repeated here, and "
         "the addition is the bound on the child's launch, since 'lighter bounce' fails in clips "
         "by catapulting the small jumper unrealistically high.")

add('shape-rolling-comparison', 265,
    'The ball rolls away smoothly and keeps gaining speed; the cube tumbles in lurches and fights '
    'its own flat faces.',
    S(*both('a cube', 'a basketball'),
      ('core', 'Both start from rest on a hill and descend.'),
      ('minor', 'The slope is comparable for both -- same hill, similar line.')),
    P(cons2('the cube', 'the basketball'),
      ('core', 'The basketball rolls continuously and gains speed steadily down the slope.',
       'the ball descends in fits and starts, or holds one speed on the open slope'),
      ('core', 'The cube moves in lurches: it tips over an edge, lands a face, pauses or slows, and '
               'tips again.',
       'the cube glides down the hill as smoothly and continuously as the ball'),
      ('core', 'The ball outruns the cube.',
       'the cube keeps pace with or beats the ball down the same slope'),
      ('major', 'The ball turns in proportion to the ground it covers.',
       'the ball slides down without turning, or spins wildly while creeping'),
      ('major', 'The cube pivots about its edges as it tumbles rather than rotating smoothly '
                'through its faces.',
       'the cube rotates continuously about its centre as though it were round'),
      ('minor', 'The cube may come to rest on a face partway down a gentle slope; the ball does '
                'not stop on open slope.',
       'the ball parks itself mid-slope while the cube rolls on past it')),
    note="Their standards -- the ball rolling smoothly and continuously while gaining speed, the "
         "cube tumbling with noticeable deceleration whenever a flat face lands -- are correct and "
         "well observed, and both are used. The additions are the mechanics of each: rolling "
         "coupled to distance for the ball, edge-pivoting for the cube, and the asymmetry that a "
         "cube can legitimately stop on a face where a ball cannot stop on an open slope.")

add('struck-bell-response', 266,
    'Each bell swings and rings when struck; the visible motion is the swing and the clapper, not '
    'the ring.',
    S(*both('a small bell', 'a large bell'),
      ('core', 'Both are rung during the shot.'),
      ('minor', 'The manner of ringing is visible -- a clapper, a hammer or a pulled rope.')),
    P(cons2('the small bell', 'the large bell'),
      ('core', 'Each bell moves only when and as it is rung: struck, swung or shaken.',
       'a bell swings or sounds off with nothing acting on it, or fails to move at all when '
       'plainly struck'),
      ('core', 'Neither bell visibly ripples, wobbles or flexes like rubber: a ringing bell looks '
               'still except for its swing.',
       'the body of either bell visibly waves and shimmers like jelly as it rings'),
      ('major', 'The large bell swings slowly and ponderously; the small bell swings quickly.',
       'the great bell flicks back and forth as fast as the hand bell'),
      ('major', 'A swinging bell\'s clapper lags and strikes the inside as the bell reverses.',
       'the clapper stays glued to one wall of the bell through the whole swing, or never touches '
       'it while the bell plainly swings',
       'a clapper is visible inside either bell'),
      ('major', 'Once left alone, each bell\'s swing dies down gradually, the large one taking '
                'longer to settle.',
       'a bell\'s swing keeps its full size indefinitely, or stops dead in an instant'),
      ('minor', 'The bells stay rigid metal throughout -- their shape and shine unchanged by '
                'ringing.',
       'the bell\'s profile distorts with each strike')),
    note="Both of their standards ask to watch the bells' vibration -- slower, more pronounced, "
         "longer-sustained in the large bell -- but bell vibration is at acoustic frequency and "
         "amplitudes far below what video resolves: a ringing bell looks motionless except for its "
         "swing. A clip that shows a bell visibly waving is inventing the effect. The rubric "
         "therefore forbids visible flexing and moves the size comparison to what IS visible: the "
         "pendulum period of the swing, the clapper's lag, and the slow decay of the large bell's "
         "swing. Scenario 263 makes the same correction for drums.")

# ---- Structural Integrity Across Scales (267-273) --------------------------
add('arch-load-test', 267,
    'The small arch is worked to visible deformation early, while the large arch carries far more '
    'before it shows strain.',
    S(*both('a small arch', 'a large arch'),
      ('core', 'Weights are placed on both.'),
      ('minor', 'The loading is progressive -- weight added over the shot rather than all at once.')),
    P(('fatal', 'Each arch deforms only under load: nothing sags or cracks before weight is on it.',
       'an arch slumps before any weight is applied, or goes on deforming after the load is taken '
       'off'),
      ('core', 'The small arch shows visible deformation at loads that leave the large arch '
               'unmoved.',
       'the large arch buckles under a load the small arch carries without strain'),
      ('core', 'An arch deforms by flattening at the crown and spreading at its feet, not by '
               'stretching taller.',
       'a loaded arch grows taller or arches higher under the weight pressing down on it'),
      ('major', 'Deformation grows with load: more weight, more sag.',
       'the deformation shrinks as more weight is piled on'),
      ('major', 'If an arch fails, it fails where the bending is worst -- crown or haunches -- and '
                'the failure is permanent.',
       'an arch collapses and then re-forms, or breaks at a point carrying no load',
       'either arch fails during the shot'),
      ('minor', 'The weights rest on the arches and stay put.',
       'weights hover above the arch or slide about on it'),
      ('minor', 'The supports and ground hold still under both arches.',
       'the ground gives way instead of the arch')),
    note="Their standards -- earlier visible deformation in the small arch, greater absolute load "
         "carried by the large -- are used; in absolute terms they are right, though it is worth "
         "recording that geometric scaling actually makes large structures relatively weaker "
         "(stress grows with size at fixed shape), so the comparison holds only because the loads "
         "are absolute. The additions are the mode of failure -- crown flattening, feet spreading "
         "-- and monotonicity of the deformation with the load.")

add('bridge-load-test', 268,
    'The model bridge visibly sags under its heavy load; the real bridge carries its load with '
    'only slight, recoverable flex.',
    S(*both('a small model bridge', 'a full-scale bridge'),
      ('core', 'Both are loaded -- weights on the model, traffic or test load on the real one.'),
      ('minor', 'The loads read as heavy relative to each bridge.')),
    P(('fatal', 'Each bridge deforms only under and during its load.',
       'a span sags before anything is on it, or keeps sagging further after the load is off'),
      ('core', 'The model shows clear deformation under its heavy load -- sagging, twisting or '
               'buckling members.',
       'the toy bridge carries a load that dwarfs it without the slightest visible strain'),
      ('core', 'The full-scale bridge flexes only slightly and recovers: a dip under the load that '
               'passes with it.',
       'the real bridge folds and buckles like the model, or shows no response at all to a heavy '
       'load crossing it'),
      ('major', 'Deformation is greatest under the load and moves with it.',
       'the span dips somewhere other than under the load, or the dip stays behind after the load '
       'moves on'),
      ('major', 'If the model fails, its pieces break or buckle at the loaded points and stay '
                'failed.',
       'the model collapses and springs back whole',
       'the model fails during the shot'),
      ('minor', 'The supports at the ends of each bridge hold still.',
       'the piers or towers lean and shift instead of the span flexing'),
      ('minor', 'The loads behave as dead weight -- resting, rolling or driving across -- rather '
                'than floating.',
       'the test load hovers above the deck it is supposedly loading')),
    note="Their second standard requires the full-scale bridge to show 'no visible bending, "
         "buckling, or strain', which contradicts their own standard for scenario 279, where a "
         "suspension bridge must dip noticeably under a vehicle. Real bridges are designed to "
         "deflect visibly and recover; zero response is the rigid-prop artefact. This rubric "
         "requires slight recoverable flex from the real bridge -- consistent with 279 -- and keeps "
         "their first standard on the model deforming under heavy load.")

add('brittle-shatter-on-strike', 269,
    'The same hammer blow shatters the thin pane but only marks or cracks the thick one.',
    S(*both('a thin glass pane', 'a thick glass pane'),
      ('core', 'Each is struck with a hammer.'),
      ('minor', 'The blows read as comparable -- same hammer, similar swing.')),
    P(('fatal', 'Each pane responds where and when the hammer strikes it.',
       'a pane shatters before the hammer arrives, or the hammer passes through the glass'),
      ('core', 'The thin pane shatters at the blow: sudden, with fragments, and without bending '
               'first.',
       'the thin pane flexes like plastic and survives, or deforms visibly before letting go'),
      ('core', 'The thick pane survives the same blow: at most chips, stress marks or cracks '
               'radiating from the impact.',
       'the thick pane bursts into fragments just as the thin one did'),
      ('major', 'Cracks in the thick pane radiate from the point of impact and only ever grow.',
       'cracks appear far from the blow, or heal over between frames'),
      ('major', 'The thin pane\'s fragments scatter and stay separate.',
       'the shards reassemble, or hang in the air where the pane stood'),
      ('minor', 'The hammer rebounds or follows through; it is not stopped dead in mid-air by the '
                'thin pane.',
       'the hammer halts on the thin glass as though it had hit a wall'),
      ('minor', 'The frames or supports holding the panes stay put.',
       'the frame explodes while the glass survives')),
    note="Their sole standard -- the thin pane shattering into many pieces immediately while the "
         "thick one shows stress marks or minor cracks without shattering -- is correct, complete, "
         "and used nearly as written; the brittle-fracture standards are consistently the "
         "benchmark's best. The additions are crack monotonicity on the thick pane and the "
         "hammer's follow-through, which distinguishes a real strike from an animation of one. "
         "Scenario 234 carries this mechanism for a single plate.")

add('sway-period-scaling', 270,
    'The small tree whips quickly through big angles while the big tree sways slowly through small '
    'ones.',
    S(*both('a small tree', 'a large tree'),
      ('core', 'Both sway in a storm.'),
      ('minor', 'The storm shows around them -- driven rain, flying leaves or bent grass.')),
    P(cons2('the small tree', 'the large tree'),
      ('core', 'The small tree bends through visibly larger angles than the large tree in the same '
               'wind.',
       'the big tree is laid over further than the sapling beside it'),
      ('core', 'The small tree also moves faster: it whips back and forth several times while the '
               'big tree completes one slow sway.',
       'the great tree thrashes as quickly as the sapling, or the sapling heaves as slowly as the '
       'great tree'),
      ('major', 'Both trees bend away from the wind and most at their tops.',
       'either tree bends into the wind, or hinges at the roots with a straight trunk'),
      ('major', 'Both respond to the same gusts at the same times.',
       'one tree thrashes while the other stands in dead calm within the same frame'),
      ('major', 'Both stay rooted; swaying does not walk either tree across the ground.',
       'a tree\'s base slides or hops across the ground as it sways'),
      ('minor', 'Loose leaves and small debris stream downwind past both.',
       'debris flies against the wind that is bending the trees')),
    note="Their standards -- rapid, significant bending in the small tree; minimal, slower movement "
         "in the large -- are correct on both counts, including the count benchmarks usually miss: "
         "the period. A tree's natural sway period grows with its size, so the big tree moves "
         "SLOWLY as well as less, and a clip that thrashes a large tree at sapling frequency is "
         "wrong even if the amplitude is right. Scenario 277 carries this mechanism for buildings, "
         "where the benchmark's own standard for 271 contradicts it.")

add('shaking-response-scaling', 271,
    'The toy block topples at the first shake; the skyscraper rides the shaking with a slow visible '
    'sway.',
    S(*both('a toy building block', 'a skyscraper'),
      ('core', 'Both are subjected to shaking.'),
      ('minor', 'The shaking has a visible source or effect beyond the two objects -- a shaken '
                'table, swaying wires, moving ground.')),
    P(cons2('the toy block', 'the skyscraper'),
      ('core', 'The toy block topples or slides at modest shaking: it goes over early and stays '
               'down.',
       'the block rides out shaking that visibly moves everything else, or it rights itself after '
       'falling'),
      ('core', 'The skyscraper remains standing through the same shaking.',
       'the skyscraper collapses outright at shaking a toy block scene implies'),
      ('major', 'The skyscraper sways: it moves slowly and visibly at the top, more than at the '
                'base.',
       'the tower stays perfectly rigid from base to tip through strong shaking'),
      ('major', 'The block topples by pivoting over an edge, in the direction the shaking throws '
                'it.',
       'the block floats over or topples against the direction of the jolt'),
      ('major', 'The shaking, the block\'s fall and the tower\'s sway happen together in time.',
       'the block falls before the shaking starts, or the tower sways on long after everything '
       'else has stilled'),
      ('minor', 'Small unsecured things near either structure rattle and shift with the shaking.',
       'loose objects sit perfectly still through shaking that topples the block')),
    note="Their second standard requires the skyscraper to remain upright 'with no visible "
         "structural damage or significant sway', and the sway clause is wrong: tall buildings "
         "survive shaking precisely by swaying, slowly and visibly at the top, and their own "
         "standard for scenario 277 requires exactly that of a tall building in wind. This rubric "
         "keeps the upright requirement, drops the no-sway clause, and requires the slow top-heavy "
         "sway instead, sharing the period physics of scenario 270.")

add('wind-response-scaling', 272,
    'The small tent snaps and billows in wind that leaves the big tent barely stirring.',
    S(*both('a small tent', 'a large tent'),
      ('core', 'Both stand in wind.'),
      ('minor', 'The wind shows around them -- grass, flags or dust moving.')),
    P(cons2('the small tent', 'the large tent'),
      ('core', 'The small tent responds hard: its fabric snaps and billows, its poles flex, the '
               'whole shelter shudders in the gusts.',
       'the small tent stands drum-tight and still in wind that moves everything around it'),
      ('core', 'The large tent responds far less: its panels stir but the structure holds its '
               'shape.',
       'the big tent thrashes and buckles as violently as the small one in the same wind'),
      ('major', 'Both tents answer the same gusts at the same times.',
       'one tent flaps in a private storm while the other and the surroundings sit in calm'),
      ('major', 'The tents deform downwind: fabric bellies away from the wind, and any lean is away '
                'from it.',
       'a tent leans or bellies into the wind'),
      ('major', 'Anchored corners stay anchored unless a peg visibly pulls out; a freed corner '
                'flaps from its remaining attachments.',
       'a corner comes free and the fabric there stays magically taut, or the whole tent departs '
       'while plainly still pegged'),
      ('minor', 'Guy lines on the windward side pull taut in gusts and slacken between them.',
       'the guy lines hang slack while the tent strains downwind',
       'guy lines are visible on either tent'),
      ('minor', 'Both tents keep their colours and panel patterns as the fabric moves.',
       "a tent's panels change colour or pattern as the fabric flaps")),
    note="Their standards -- the small tent flapping vigorously and at risk, the large tent steady "
         "-- are used, with one caution: 'remains steady and unaffected' overstates it, since even "
         "a large tent's panels stir in wind that shakes a small one, and a perfectly motionless "
         "tent is the rigid-prop artefact. The additions are the downwind direction of every "
         "deformation and the gust coupling shared with the other wind scenarios (216, 254, 270).")

add('wave-impact-scaling', 273,
    'The wave bursts over both walls, crumbling the small one and breaking harmlessly on the large '
    'one.',
    S(*both('a small rock wall', 'a large rock wall'),
      ('core', 'A powerful wave strikes them.'),
      ('minor', 'The setting reads as a shore or breakwater where waves arrive.')),
    P(('fatal', 'Each wall responds when and where the wave strikes it.',
       'a wall collapses before the water reaches it, or the wave passes through a wall as though '
       'it were not there'),
      ('core', 'The small wall gives way under the impact: stones shift, gaps open, parts of it '
               'wash down.',
       'the small wall shrugs off the same wave that visibly explodes against everything else'),
      ('core', 'The large wall stands: the wave breaks on it and it keeps its line and its face.',
       'the large wall crumbles as readily as the small one under the same wave'),
      ('major', 'The wave itself bursts on impact: spray and water thrown up and over, then '
                'draining back seaward.',
       'the wave meets the walls without any splash or runback, sliding through them like mist'),
      ('major', 'Displaced stones from the small wall move the way the water pushes them and come '
                'to rest.',
       'dislodged stones fly against the incoming wave, or drift about after the water has drained'),
      ('major', 'Damage to the small wall is permanent: it does not reassemble between waves.',
       'the small wall is whole again after the water recedes'),
      ('minor', 'Both walls end the shot wet on their seaward faces.',
       'a wall that took a breaking wave reads bone dry immediately after')),
    note="Their standards -- the small wall crumbling with debris clearly dispersing, the large "
         "wall intact with little or no visible damage -- are correct and are used. The additions "
         "are about the wave as much as the walls: it must burst and drain back rather than pass "
         "through, the debris must travel with the water, and the damage must persist, which is "
         "the irreversibility item every fracture scenario in this benchmark needs.")

# ---- Scaling of Mechanical Properties (274-280) ----------------------------
add('tension-failure-scaling', 274,
    'Under the same pull, the thin rope stretches and snaps while the thick rope holds.',
    S(*both('a thin rope', 'a thick rope'),
      ('core', 'Both are pulled in a tug-of-war.'),
      ('minor', 'The pulls read as comparable -- similar teams or efforts on each.')),
    P(cons2('the thin rope', 'the thick rope'),
      ('core', 'The thin rope fails under the pull: it parts, and the two ends whip back toward '
               'their own sides.',
       'the parted ends hang slack in mid-air where the break happened, or fly toward the opposing '
       'team'),
      ('core', 'The thick rope holds under the same kind of pull, without visible damage.',
       'the thick rope snaps as readily as the thin one, or falls apart with no one straining on '
       'it'),
      ('major', 'Before it parts, the thin rope is taut and straight between the pullers.',
       'the rope snaps while hanging in a slack curve'),
      ('major', 'When the thin rope parts, the pullers stagger or fall backward as the resistance '
                'vanishes.',
       'both teams stay planted and balanced at the instant the rope gives way'),
      ('major', 'The break is permanent and leaves frayed, fibrous ends.',
       'the rope rejoins itself, or parts with clean fused ends as though cut and sealed'),
      ('minor', 'Both ropes sag when tension is off and straighten when the pull comes on.',
       'a rope stands out straight and rigid with nobody pulling it')),
    note="Their standards -- visible stretch then failure in the thin rope, the thick rope intact "
         "with minimal stretch -- are correct and are used. The additions are the consequences a "
         "clip must carry through: stored elastic energy makes the parted ends whip back and the "
         "pullers stagger, and the break is fibrous and final. A tug-of-war rope that parts with "
         "neither recoil nor a stumble has removed the tension it was supposedly under.")

add('beam-bending-under-load', 275,
    'The long steel beam rests on its two supports and sags just perceptibly at mid-span.',
    S(('core', 'A large steel beam is present.'),
      ('core', 'It rests horizontally on two supports.'),
      ('minor', 'The span between supports is long relative to the beam\'s depth.'),
      ('minor', 'The beam is unloaded apart from its own weight.')),
    P(('fatal', 'The beam rests on its supports and is carried by them.',
       'the beam floats clear of a support, or passes through one'),
      ('core', 'Any sag is slight and at mid-span: a long shallow curve, deepest at the middle.',
       'the beam kinks sharply at one point, or sags deepest near a support'),
      ('core', 'The sag is steady: the beam does not visibly creep further down over the shot.',
       'the beam bends further and further under nothing but its own weight'),
      ('major', 'The beam does not sag grossly: steel under self-weight bows perceptibly, not like '
                'a rope.',
       'the steel beam droops in a deep hanging curve like a cable slung between the supports'),
      ('major', 'The beam stays straight in plan: the bow is downward, not sideways.',
       'the beam snakes sideways while resting flat'),
      ('minor', 'The supports carry the load without sinking or tilting.',
       'a support visibly sinks or leans as the beam rests on it'),
      ('minor', 'The beam\'s section and surface are constant along its length.',
       'the beam is visibly fatter or thinner in the middle than at its ends')),
    note="Their standards -- a slight sag forming a subtle downward curve, and the beam securely "
         "seated on its supports -- are correct and are used. The failure modes to catch sit on "
         "either side of 'slight': a perfectly straight beam rendered as a rigid prop, and a beam "
         "drooping like a rope, which is how clips most often exaggerate compliance. Scenario 67 "
         "carries this mechanism for a plank under an added weight; scenario 276 is the comparative "
         "version.")

add('beam-bending-under-load', 276,
    'The weight bows the small plank visibly -- far more than a thicker plank would give.',
    S(('core', 'A small wooden plank is present.'),
      ('core', 'A weight is on it and it bends.'),
      ('minor', 'The plank is supported at its ends or edges with the weight between.'),
      ('minor', 'The plank reads as thin relative to its span.')),
    P(('fatal', 'The plank bends under and because of the weight.',
       'the plank is bowed before the weight arrives, or straightens while the weight still sits '
       'on it'),
      ('core', 'The bend is a smooth curve, deepest under the weight.',
       'the plank folds at a sharp angle, or bows deepest away from the load'),
      ('core', 'More weight means more bend, and taking the weight off lets the plank spring back.',
       'the plank stays fully bowed after the weight is removed, or gives less as more is added'),
      ('major', 'The weight rides down with the plank, staying in contact.',
       'the weight hovers above the dipping plank, or sinks into its surface'),
      ('major', 'The plank keeps its length and thickness as it bends.',
       'the plank stretches longer or thins as it bows'),
      ('major', 'If the plank is overloaded it cracks or snaps at the deepest bend, and the break '
                'is permanent.',
       'the plank breaks and then behaves as though whole',
       'the plank fails during the shot'),
      ('minor', 'The supports at the ends stay put.',
       'the supports slide together as the plank bows')),
    note="Their sole standard -- the small plank bending visibly more, with significant deformation "
         "-- is the comparative point and is folded into the core items; since only one plank is in "
         "the caption, the comparison lives in degree rather than in a second object on screen. "
         "This scenario is the small-scale twin of 67 and 275 and carries their mechanism; the "
         "recovery item marks the wood as elastic at this load, in contrast to the plastic "
         "deformation block at 225-231.")

add('sway-period-scaling', 277,
    'The tall building sways slowly and visibly at its top in the high wind.',
    S(('core', 'A tall building is present.'),
      ('core', 'High wind blows -- visible in flags, trees, debris or driven rain.'),
      ('minor', 'The building\'s top is in frame, where the sway shows.'),
      ('minor', 'The building reads as a slender tower rather than a squat block.')),
    P(('fatal', 'The building stays rooted: it sways about its base and does not walk, hop or '
                'detach.',
       'the base of the building shifts across the ground, or the tower leaves the ground'),
      ('core', 'The sway is greatest at the top and dies away toward the base.',
       'the whole building tips rigidly from the ground like a felled tree, or the base sways more '
       'than the top'),
      ('core', 'The sway is slow: long, deliberate excursions rather than rapid shaking.',
       'the tower vibrates back and forth quickly like a plucked ruler'),
      ('major', 'The sway is small against the building\'s size: a lean, not a whip.',
       'the top of the tower lashes through huge arcs like a tree in the same wind'),
      ('major', 'The swaying follows the wind: excursions grow in gusts and ease in lulls.',
       'the tower sways rhythmically in dead calm, or ignores visible gusts entirely'),
      ('minor', 'Nearby lighter things -- trees, cables, flags -- move faster and further than the '
                'building.',
       'the skyscraper thrashes while the flags on it hang limp'),
      ('minor', 'The building\'s shape stays its own: floors and windows keep their lines as it '
                'sways.',
       'the facade ripples and shimmers like cloth as the tower moves')),
    note="Their sole standard compares the tall building's oscillation to a shorter one that the "
         "caption does not put on screen, so the comparison is carried in character instead: tall "
         "buildings sway SLOWLY (their natural period grows with height) and modestly, most at the "
         "top. Note that their standard for scenario 271 demands a skyscraper show no significant "
         "sway -- the direct opposite of this record -- and physics sides with this one. Scenario "
         "270 carries this mechanism for trees.")

add('tension-failure-scaling', 278,
    'The same pull parts the small rod while the thicker rod carries it with barely any give.',
    S(*both('a small rod', 'a thicker rod'),
      ('core', 'Both are put under tension, and the small rod snaps.'),
      ('minor', 'The pulls read as comparable -- the same rig or effort on each.')),
    P(cons2('the small rod', 'the thicker rod'),
      ('core', 'The small rod fails under the pull: it parts into two pieces that separate.',
       'the small rod survives while the thick one parts, or neither fails though the caption\'s '
       'event is the snap'),
      ('core', 'What the clip commits to at the break holds together: a rod that visibly stretches '
               'and necks parts at the neck with drawn-out ends, and a rod that never stretches '
               'parts cleanly across.',
       'the rod stretches and thins visibly and then parts with clean square ends, or it parts '
       'with stringy drawn ends having never stretched at all'),
      ('major', 'The thicker rod gives at most slightly under the same pull and does not fail.',
       'the thick rod stretches like taffy or snaps along with the thin one'),
      ('major', 'The break in the small rod is where it is thinnest or most worked, and it is '
                'permanent.',
       'the rod parts at a random point and later appears whole again'),
      ('major', 'At the moment of failure the freed ends spring apart along the line of pull.',
       'the two halves stay exactly in place after parting, still aligned as though joined'),
      ('minor', 'Before failure the small rod is straight and taut along the line of pull.',
       'the rod snaps while slack or bowed sideways under pure tension')),
    note="Their first standard has the small rod 'stretch visibly and eventually snap cleanly', "
         "which mixes two failure modes: visible stretching means ductile necking, whose break is "
         "drawn and fibrous, while a clean flat break belongs to brittle failure with no visible "
         "stretch. Either is correct physics for some material, but not both at once, so the core "
         "item asks for internal consistency between the stretch and the fracture face. Their "
         "second standard, minimal deformation in the thick rod, is used as written. Scenario 274 "
         "carries this mechanism for ropes.")

add('span-deflection-recovery', 279,
    'The bridge dips slightly under the crossing vehicle and rises back as it passes off.',
    S(('core', 'A suspension bridge is present.'),
      ('core', 'A large vehicle crosses it.'),
      ('minor', 'The bridge reads as a suspension bridge -- towers, cables and hangers.'),
      ('minor', 'The vehicle reads as heavy -- a truck, bus or loaded trailer.')),
    P(('fatal', 'The deck carries the vehicle: the wheels stay on the roadway and neither passes '
                'through the other.',
       'the vehicle sinks into the deck, or travels above it without contact'),
      ('core', 'The deck dips where the vehicle is, and the dip travels along with it.',
       'the deck dips somewhere the vehicle is not, or a fixed sag sits mid-span while the vehicle '
       'moves across'),
      ('core', 'The dip is slight against the size of the bridge, and the deck returns to its line '
               'after the vehicle passes.',
       'the deck stays dished after the vehicle has gone, or it plunges like a rope bridge under '
       'one truck'),
      ('major', 'The cables and hangers stay taut and share the work: hangers near the load pull '
                'straight down under it.',
       'hangers go slack and flap while the deck under the load dips, or the cables stay frozen as '
       'the deck moves'),
      ('major', 'The towers stand fixed; the movement is in the deck and cables.',
       'the towers lean and bob with the passing vehicle'),
      ('minor', 'Any residual motion of the deck after the vehicle leaves dies away.',
       'the span keeps bouncing at full size long after the vehicle has gone'),
      ('minor', 'The vehicle itself rides level, responding to the deck with its suspension.',
       'the vehicle tilts wildly on a deck that is barely moving')),
    note="Their sole standard -- deflection proportional to the vehicle's weight, a heavier vehicle "
         "causing a more noticeable dip -- is correct and its visible half is used: with one "
         "vehicle on screen, proportionality is carried by the dip tracking the load and staying "
         "slight. This record is the one that contradicts scenario 268's 'no visible bending' "
         "standard, and physics sides with this one: spans deflect and recover. The cable items "
         "are the suspension-specific additions, since a clip that moves the deck without moving "
         "the cables has broken the structure's logic.")

add('membrane-stretch-limit', 280,
    'Both balloons are inflated toward their limits; the small one reaches its limit first and '
    'pops.',
    S(*both('a small balloon', 'a larger balloon'),
      ('core', 'Both are inflated or pressed -- stretched further under pressure.'),
      ('core', 'One of them pops, as the caption says.'),
      ('minor', 'The two are of the same kind -- alike apart from size.')),
    P(('fatal', 'A popped balloon is gone as an inflated body: it tears to scraps at once and does '
                'not reassemble.',
       'a balloon pops and then reappears whole, or deflates gently into an intact envelope at the '
       'moment of bursting'),
      ('core', 'Each balloon stretches under its inflation: it grows, and its skin reads tauter '
               'and more translucent as it nears its limit.',
       'a balloon swells without its skin changing at all, or shrinks while being inflated'),
      ('core', 'The larger balloon accommodates visibly more total stretch before failing, and its '
               'growth toward the limit is the more gradual.',
       'the larger balloon bursts at once while the small one stretches on far beyond it'),
      ('major', 'The pop is instantaneous -- between one moment and the next -- with the skin '
                'recoiling to shreds.',
       'the balloon tears slowly open over a second or more, peeling like fruit'),
      ('major', 'The stretch before failure is not perfectly uniform: the skin bulges or necks '
                'where it is weakest, and failure starts there.',
       'the balloon remains a perfect uniformly-scaled sphere right up to a burst that starts '
       'everywhere at once'),
      ('minor', 'The bang scatters the scraps outward and they fall.',
       'the shreds of the burst balloon hang in the air where the balloon was'),
      ('minor', 'The surviving balloon is unaffected by the other\'s pop beyond a twitch.',
       'the neighbouring balloon bursts sympathetically with nothing touching it')),
    note="Their second standard asserts that the larger balloon 'pops at a higher pressure', which "
         "has the membrane law backwards: wall tension goes as pressure times radius, so a larger "
         "balloon reaches the same skin tension at LOWER pressure -- the reason a big balloon "
         "inflates a small one when they are connected. Pressure is invisible anyway, so the "
         "rubric keeps only the visible half of their claim -- more total stretch, more gradual "
         "approach to failure -- and drops the pressure ordering. Their 'uniformly thinner' is "
         "also softened: real balloon skin necks and bulges unevenly near its limit, and failure "
         "starts at the weak spot.")
