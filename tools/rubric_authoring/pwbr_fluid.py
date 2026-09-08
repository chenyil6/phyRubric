# phyworldbench 106-140: Fluid and Particle Dynamics.
# Same authoring flow as the earlier blocks: items come from the caption plus first-principles
# physics, then physics_prompt and key_standards are diffed for coverage; conflicts are followed
# on the side of physics and recorded in `note`. Cross-check against KS[i], never against
# SRC[i]['key_standards'] -- id 121 is one of the eleven records whose standards are wrapped in a
# dict, and reading it raw yields the bare string 'standards'.
#
# Two things recur across this category and shape most of the items. First, a fluid or a cloud of
# particles has no fixed shape, so `cons`-style identity items do not apply to it; what stands in
# for them is provenance (it comes out of a source, not out of nothing) and irreversibility (a
# disturbance dies down, a mixture does not unmix, a pile does not un-pile). Second, the
# benchmark's standards for this category lean heavily on rendering words -- smooth, seamless,
# controlled, uniform, without abrupt stops -- which name no physical observable and are excluded
# by _policy.json's not_penalized list. Where a standard consists only of those, it is not used
# and the note says so.


def cons(o):
    return ('fatal',
            f'{o[0].upper()}{o[1:]} keeps its own shape and identity for the whole shot, and it '
            f'does not pass through any solid surface.',
            f'{o} turns into a different object, passes through something solid, or disappears '
            f'and re-appears')


def fromsrc(stuff, src):
    return ('fatal',
            f'{stuff[0].upper()}{stuff[1:]} enters the shot from {src} rather than appearing out '
            f'of nothing.',
            f'{stuff} materialises in mid-air away from {src}, or is already there in full before '
            f'{src} has produced any')


def ripples_fade(what='the rings'):
    return ('major',
            f'{what[0].upper()}{what[1:]} weaken as they widen, and the surface settles back '
            f'toward calm.',
            f'{what} hold their height however far they travel, or grow stronger the further out '
            f'they get')


def floatline(o):
    return ('core',
            f'{o[0].upper()}{o[1:]} rides at the surface with about the same part of it under '
            f'water throughout.',
            f'{o} sinks out of sight, lifts entirely clear of the water, or slides up and down '
            f'through the surface with no wave to account for it')


def fixed(o):
    pl = ' and ' in o
    return ('minor',
            f'{o[0].upper()}{o[1:]} stay put and keep their shape throughout.' if pl else
            f'{o[0].upper()}{o[1:]} stays put and keeps its shape throughout.',
            f'{o} shift, flex or change shape on their own' if pl else
            f'{o} shifts, flexes or changes shape on its own')


def marks(o, mk):
    return ('minor',
            f'{mk[0].upper()}{mk[1:]} stay attached to {o} and move with it.',
            f'{mk} slide across the surface, detach, or change from one moment to the next')


# ---- Water Motion (106-112) ----------------------------------------------
add('gravity-draining', 106,
    'An opened drain lets the bathtub empty, and the outflow weakens as the water gets shallower.',
    S(('core', 'A bathtub holding water is present.'),
      ('core', 'The drain is open and water goes down it.'),
      ('minor', 'There is a good depth of water at the start rather than the tub already being '
                'empty.'),
      ('minor', 'The vessel reads as a bathtub rather than a sink or a basin.')),
    P(('fatal', 'Water leaves through the drain and the level in the tub goes down.',
       'the level holds or rises while water plainly pours down an open drain, or water climbs up '
       'out of the drain into the tub'),
      ('core', 'The level only ever falls once the drain is open; it never comes back up on its own.',
       'the level rises again part-way through with nothing filling the tub'),
      ('core', 'The surface flow converges on the drain from around the tub.',
       'the water streams away from the drain, or it disappears through a spot on the tub where '
       'there is no opening'),
      ('major', 'The outflow weakens as the tub empties: it is strongest while the water is deep '
                'and weakest at the end.',
       'the last of the water leaves as hard as the first did, or the flow gets stronger as the '
       'level drops'),
      ('minor', 'Any swirl over the drain sits above the opening and keeps turning the same way '
                'for as long as it lasts.',
       'the swirl wanders off across the tub, or it reverses its direction of rotation on its own',
       'a swirl or a dimple forms over the drain at all'),
      fixed('the tub')),
    note="Their first key standard requires a visible vortex. Whether a draining tub forms one "
         "depends on the residual circulation left in the water: plenty of real tubs drain with "
         "nothing more than a dimple over the opening, so requiring a vortex would fail a correct "
         "clip. It sits behind a precondition here, and what is asked of it is only that it stay "
         "over the drain and not reverse. Their second standard's 'smoothly' is a rendering "
         "property and is not used. Neither standard names the one thing that discriminates here: "
         "the outflow slows as the head of water above the drain drops, so a tub that empties at a "
         "constant rate is wrong.")

add('impact-ripples', 107,
    'A stone breaks a still surface, sinks, and leaves rings that spread outward and fade.',
    S(('core', 'A stone is present.'),
      ('core', 'It is dropped into the pond and goes into the water.'),
      ('core', 'The pond surface is still before the stone lands, as the caption says.'),
      ('minor', 'The setting reads as a pond rather than a container of water.')),
    P(cons('the stone'),
      ('core', 'Rings spread outward from the point where the stone went in, and they only ever '
               'travel outward.',
       'the rings close back in toward the entry point, or they start from somewhere the stone did '
       'not land'),
      ('core', 'The stone sinks and stays under.',
       'the stone rests on the surface or bobs back up into view'),
      ('major', 'The rings start when the stone reaches the water, not before.',
       'ripples are already spreading while the stone is still in the air'),
      ripples_fade(),
      ('minor', 'The set of rings stays centred on the entry point as it widens.',
       'the rings drift off across the pond, away from where the stone went in'),
      fixed('the pond and its banks')),
    note="Their sole key standard asks for 'a concentric pattern', which a clip of static "
         "concentric rings satisfies exactly. What discriminates is outward-only travel, the decay "
         "as the rings widen, and the timing against the stone's entry, none of which their "
         "standard names. That the stone sinks is also unstated and is the commonest thing to get "
         "wrong about a stone.")

add('drip-impact', 108,
    'Separate drops fall from a faucet into standing water, each making its own rings that fade.',
    S(('core', 'A faucet is present.'),
      ('core', 'Water drips from it as separate drops rather than as a running stream.'),
      ('core', 'The sink below holds standing water, as the caption says.'),
      ('minor', 'The setting reads as a sink rather than an open body of water.')),
    P(fromsrc('the drops', 'the faucet'),
      ('core', 'Each drop that lands makes its own rings, starting where and when it hits.',
       'rings appear where no drop landed, or a drop lands and the surface does not respond at all'),
      ('core', 'A drop merges into the standing water on impact rather than staying a separate '
               'bead on top of it.',
       'the drop lands and rests on the surface as an intact ball'),
      ('major', 'Each drop speeds up as it falls.',
       'a drop drifts down at one unchanging speed, or slows on the way to the water'),
      ripples_fade('the rings from each drop'),
      ('minor', 'A small splash or crown is thrown up at the impact and collapses back.',
       'the surface dents inward with nothing at all thrown up',
       'the shot is close enough to the impact to show what happens at it'),
      fixed('the faucet and the basin')),
    note="Their second key standard requires a crown at each impact. Crowns are real but they are "
         "marginal at this resolution and frame rate -- they last a few frames -- so requiring one "
         "would fail correct footage that simply cannot resolve it; it sits behind a precondition "
         "here. Their standards omit the drop's acceleration and the merging, which are the items "
         "that catch a drop drifting down at constant speed or sitting on the surface as an intact "
         "bead.")

add('dive-entry-splash', 109,
    'A swimmer enters the pool, throwing up a splash and sending waves out that then die down.',
    S(('core', 'A swimmer is present.'),
      ('core', 'The swimmer goes from above the water into the pool.'),
      ('minor', 'The entry is a dive -- head or hands first -- rather than a step or a fall.'),
      ('minor', 'The setting reads as a pool rather than open water.')),
    P(('fatal', 'The swimmer and the water meet at the surface: the swimmer breaks through it and '
                'goes under rather than passing through it as if it were not there.',
       'the swimmer sinks through the surface leaving it undisturbed, or lands on the water and '
       'stays on top of it'),
      ('core', 'The entry throws water up and out, and the thrown water falls back.',
       'the water surface stays glassy through the entry, or the thrown water hangs in the air '
       'instead of coming back down'),
      ('core', 'Waves travel outward from the entry point and the pool settles back toward calm '
               'afterwards.',
       'the waves keep their size for the rest of the shot, or they build up after the entry with '
       'nothing further disturbing the water'),
      ('major', 'The splash happens at the moment of entry, not before it.',
       'the water is already erupting while the swimmer is still in the air'),
      ('major', 'The water fills back in over where the swimmer went through rather than leaving '
                'a standing hole.',
       'an open cavity stays in the water after the swimmer has passed'),
      ('minor', 'Waves that reach a wall come back off it.',
       'waves run into the wall and vanish, or they carry on through it',
       'a pool wall is in shot and waves reach it'),
      fixed('the pool and its edges')),
    note="Their first key standard asks that the waves 'reflect realistically off the pool walls'. "
         "Whether any wall is in shot is a framing accident, so reflection sits behind a "
         "precondition rather than being required. Scenario 75, 'A diver stands on a platform and "
         "jumps into a pool', is the same physical situation in the Potential to Kinetic Energy "
         "subcategory of category 3 and carries this mechanism; 75 is judged for the fall and the "
         "speed gained on the way down, this one for the entry and the water's response.")

add('displacement-wake', 110,
    'A boat pushes water aside as it travels, trailing a wake that widens behind it and fades.',
    S(('core', 'A boat is present.'),
      ('core', 'It travels across the water.'),
      ('minor', 'The body of water reads as a lake rather than a river or the sea.'),
      ('minor', 'The boat is under way for the whole shot rather than sitting still.')),
    P(cons('the boat'),
      ('core', 'The wake trails behind the boat: it starts at the hull and spreads back and out '
               'from there.',
       'the wake runs out ahead of the boat, or it sits somewhere on the water unconnected to the '
       'hull'),
      ('core', 'The near end of the wake travels with the boat, staying at the hull as the boat '
               'moves on.',
       'the wake stays pinned to one patch of water while the boat drives away from it'),
      ('major', 'The wake widens the further behind the boat it gets.',
       'the wake keeps one width all the way back, or it narrows to a point behind the boat'),
      ('major', 'Water the boat has passed settles back down after it, rather than staying churned '
                'for the rest of the shot.',
       'the whole surface behind the boat stays as rough as it was at the hull'),
      floatline('the boat'),
      fixed('the far shore and anything moored')),
    note="Their key standards ask for a V-shaped wake and 'realistic ripples'. Realistic names no "
         "observable and is not used. A static V painted on the water satisfies the shape "
         "requirement, so the items that do the work here are the ones their standards leave out: "
         "the apex travels with the hull, the wake widens with distance astern, and the water "
         "recovers behind it.")

add('stirred-vortex', 111,
    'A spoon spins the water in a glass into a dip at the centre, which unwinds once the stirring '
    'stops.',
    S(('core', 'A glass of water is present.'),
      ('core', 'A spoon is in the water and is moved around in it.'),
      ('minor', 'The water is calm before the stirring starts.'),
      ('minor', 'The vessel reads as a drinking glass rather than a bowl or a pan.')),
    P(cons('the spoon'),
      ('core', 'The water turns the same way the spoon is driven round.',
       'the water circles against the direction the spoon is moving'),
      ('core', 'The surface dips at the centre and rides higher at the glass wall while the water '
               'spins.',
       'the water heaps up into a mound at the centre, or the surface stays dead flat through '
       'vigorous stirring'),
      ('major', 'The spin dies down once the spoon stops or is lifted out.',
       'the water keeps turning at full speed indefinitely after the stirring stops'),
      ('major', 'The water stays in the glass.',
       'water climbs over the rim and out although the stirring is ordinary, or the level drops '
       'with nothing leaving the glass'),
      ('minor', 'The whole body of water turns together rather than one patch spinning while the '
                'rest sits still.',
       'an isolated swirl turns in otherwise motionless water'),
      fixed('the glass')),
    note="Their second key standard is 'the water movement is smooth and continuous', a rendering "
         "property, and it is not used. Their first standard is satisfied by water circling for "
         "ever at one speed, which is the commonest wrong answer here; the discriminator is the "
         "spin-down after the spoon stops, so that is a rubric item. The dip at the centre is also "
         "unstated and is worth having, since a mound at the centre is the intuitive-looking error.")

add('breaking-wave', 112,
    'A wave steepens in the shallows, curls over and breaks into foam, runs up the sand and drains '
    'back.',
    S(('core', 'A wave is present and travelling toward the shore.'),
      ('core', 'It breaks as it reaches the shore.'),
      ('core', 'White foam appears as it collapses, as the caption says.'),
      ('minor', 'The shore reads as sand rather than rock or shingle.')),
    P(('fatal', 'The wave travels toward the shore and breaks there.',
       'the wave travels out to sea, or it breaks in deep water far from the shore with nothing '
       'shallow under it'),
      ('core', 'The wave steepens and stands up as it comes into the shallows, before it topples.',
       'it keeps the same low profile right up to the beach and then collapses without ever '
       'steepening'),
      ('core', 'The face topples forward, over the direction of travel.',
       'the crest folds backward out to sea, or the wave simply flattens without any curl'),
      ('major', 'Water that has run up the sand drains back down toward the sea.',
       'the run-up stays where it stopped, or it keeps advancing up the beach for the rest of the '
       'shot'),
      ('major', 'The foam appears where the wave breaks and thins out afterwards.',
       'foam is already lying on an unbroken wave face, or it stays as bright and thick as it was '
       'at the moment of breaking'),
      ('minor', 'The run-up reaches its furthest point and stops there rather than climbing at an '
                'unchanging pace.',
       'the water sheets up the beach at one speed without ever slowing'),
      fixed('the beach')),
    note="Their third key standard, that 'the water should spread smoothly onto the sand', is a "
         "rendering property and is not used. Their standards cover the curl and the foam but stop "
         "at the moment of collapse; the two items that catch a wrong clip are on either side of "
         "it -- the shoaling that makes the wave stand up before it breaks, and the backwash that "
         "takes the run-up back down the beach.")

# ---- Smoke and Gas Dynamics (113-119) ------------------------------------
add('blow-out-and-smoke', 113,
    'A flame is bent by the blown air and goes out, and only then does smoke rise off the wick.',
    S(('core', 'A lit candle is present.'),
      ('core', 'The flame goes out during the shot.'),
      ('core', 'Smoke rises from the wick, as the caption says.'),
      ('minor', 'The flame reacts to the air before it goes out rather than simply cutting off.')),
    P(('fatal', 'Once out, the flame stays out.',
       'the flame comes back on its own with nothing relighting the wick'),
      ('core', 'The smoke starts after the flame goes out, not while it is still burning strongly.',
       'a plume of smoke is already streaming off a healthy flame before anything is blown at it'),
      ('core', 'The flame leans away from where the air comes from.',
       'the flame leans into the blown air, or it stands straight up through a draught strong '
       'enough to put it out'),
      ('major', 'The smoke rises off the wick and drifts, spreading out and thinning as it goes.',
       'the smoke holds one rigid shape all the way up, or it sinks to the table instead of rising'),
      ('major', 'The smoke comes off the wick and nowhere else.',
       'smoke appears in the air above the candle with a clear gap below it, or it rises from the '
       'candle body'),
      ('minor', 'The wick is left dark and unlit after the flame goes.',
       'the wick still glows brightly once the flame is gone and the smoke is rising'),
      fixed('the candle')),
    note="Their standards cover the flicker and the smoke separately but not the order between "
         "them, which is the whole physics of the scenario: the visible smoke is unburnt wax vapour "
         "that only escapes once there is no flame to consume it. A clip that shows a candle "
         "smoking heavily while burning well satisfies both of their standards and is wrong.")

add('buoyant-plume', 114,
    'Hot smoke lifts off the fire, breaks into swirls as it climbs, and thins out into the air.',
    S(('core', 'A campfire is present.'),
      ('core', 'Smoke comes off it.'),
      ('minor', 'The smoke rises rather than lying over the ground.'),
      ('minor', 'The fire reads as a campfire rather than a stove or a chimney.')),
    P(fromsrc('the smoke', 'the fire'),
      ('core', 'The smoke goes upward overall, away from the fire.',
       'the plume heads steadily downward, or it holds at one height above the fire without ever '
       'climbing'),
      ('core', 'The smoke thins and pales as it climbs and eventually loses its edge against the '
               'air.',
       'the plume stays as dense and as sharply outlined high up as it is at the fire, or it '
       'gathers back into a tighter column as it rises'),
      ('major', 'The smoke breaks up into swirls and folds rather than climbing as one solid '
                'unchanging shape.',
       'the plume is a rigid body that keeps its exact outline all the way up'),
      ('major', 'The swirling gets looser and wider the further from the fire it is.',
       'the plume is most broken up right at the fire and tidies into a smooth column above it'),
      ('minor', 'Smoke that has drifted off does not come back and re-join the plume.',
       'dispersed smoke gathers itself back into the column'),
      fixed('the fire ring and the wood')),
    note="Their standards ask for swirling turbulence and for upward motion before dispersal, both "
         "of which are right. What they leave out is the direction of the change: turbulence grows "
         "with height because the plume entrains air as it rises, so a clip that is chaotic at the "
         "fire and smooth above it has the physics backwards while still satisfying both standards.")

add('breath-condensation', 115,
    'Warm breath leaves the mouth, clouds in the cold air, and thins away without re-gathering.',
    S(('core', 'A person is present.'),
      ('core', 'They exhale and a visible cloud forms.'),
      ('minor', 'The setting reads as cold -- winter clothing, snow, bare trees or frost.'),
      ('minor', 'The cloud forms at the mouth rather than somewhere else on the person.')),
    P(fromsrc('the breath cloud', 'the mouth'),
      ('core', 'The cloud is densest at the mouth and thins out as it gets further away.',
       'the cloud is thin at the mouth and thickens into a dense mass out in the air'),
      ('core', 'The cloud moves away from the mouth in the direction of the breath and keeps going.',
       'the cloud hangs motionless at the mouth for the whole shot, or it is drawn back in'),
      ('major', 'Once thinned, the cloud does not gather itself back together.',
       'the dispersed cloud re-forms into a dense puff'),
      ('major', 'The cloud grows as it travels and loses its sharp edge.',
       'the cloud keeps one fixed size and a crisp outline all the way out'),
      ('minor', 'The cloud shows swirls and eddies rather than being a featureless blob.',
       'the cloud is a smooth shape with no internal structure at all',
       'the shot is close enough to show detail inside the cloud'),
      fixed('the person')),
    note="Their standards are sound as far as they go. The item added on top is the "
         "irreversibility: condensed breath disperses and cannot re-condense into a dense puff, "
         "and a clip that runs the dispersal backwards or loops it is the failure their 'fades "
         "gradually' does not quite exclude. Their second standard also asks for visible swirls, "
         "which needs a close shot to resolve, so that item carries a precondition.")

add('jet-deflation', 116,
    'Air escapes through the hole and the balloon shrinks and goes limp, the escape weakening as '
    'it empties.',
    S(('core', 'A balloon is present.'),
      ('core', 'It has a hole and air escapes through it.'),
      ('core', 'The balloon loses its inflated shape over the course of the shot.'),
      ('minor', 'The balloon starts inflated and taut rather than already being limp.')),
    P(('fatal', 'The balloon only ever gets smaller once air is escaping.',
       'the balloon swells back up with nothing pumping air into it'),
      ('core', 'The shrinking is fastest at the start and slows as the balloon empties.',
       'the balloon empties at one steady rate right to the end, or it deflates faster and faster '
       'as it goes limp'),
      ('core', 'The skin goes slack: it wrinkles and creases as the balloon loses air rather than '
               'staying drum-tight at a smaller size.',
       'the balloon shrinks as a perfectly taut smaller balloon with no wrinkling anywhere'),
      ('major', 'Air leaves through the hole and nowhere else.',
       'the balloon shrinks while the hole is plainly sealed, or air streams out of an intact part '
       'of the skin'),
      ('major', 'The balloon ends up limp and stays that way.',
       'it settles at a smaller taut size and holds it while air is still visibly rushing out'),
      ('minor', 'The escaping air pushes the balloon the other way, or tugs the neck about.',
       'the balloon hangs perfectly still against a jet strong enough to be plainly visible',
       'the balloon is free to move rather than being held or pinned'),
      marks('the balloon', 'the printing and the seams')),
    note="Both of their key standards are unusable. The first asks that the escaping air 'be "
         "visible as a consistent jet': air is invisible, so a clip that draws a visible jet out of "
         "clear air is inventing something, and 'consistent' is wrong besides -- the jet weakens as "
         "the internal pressure falls, which is the one quantitative trend the scenario has. The "
         "second asks that surrounding smoke be pushed away by the escaping air, but the caption "
         "puts no smoke in the scene, so on almost every clip there is nothing to judge. This "
         "rubric asks for the deflation trend, the slackening skin and the recoil instead.")

add('boiling-and-steam', 117,
    'Vapour leaves the spout of a boiling kettle and becomes a white plume as it cools in the air.',
    S(('core', 'A kettle is present.'),
      ('core', 'It is boiling, with vapour coming off it.'),
      ('minor', 'The vapour comes from the spout rather than from the body or the lid.'),
      ('minor', 'The kettle reads as a kettle rather than a pan or a pot.')),
    P(fromsrc('the plume', 'the kettle'),
      ('core', 'The plume rises and spreads, thinning out into the air.',
       'the plume falls to the worktop, or it holds one dense fixed shape above the spout'),
      ('core', 'The plume goes on for as long as the kettle is boiling.',
       'the plume stops and starts while the kettle boils steadily throughout'),
      ('major', 'The plume leaves the spout fast and slows as it climbs and widens.',
       'the plume drifts out of the spout as slowly as it moves high above it'),
      ('major', 'Vapour that has dispersed does not gather back into the plume.',
       'thinned vapour re-forms into a dense column'),
      ('minor', 'There is a short clear gap at the spout before the white plume begins.',
       'the plume is dense and white from the instant it leaves the metal',
       'the shot is close enough to the spout to show what happens right at it'),
      fixed('the kettle')),
    note="Their second key standard -- the vapour is invisible on leaving and becomes cloudy as it "
         "cools -- is correct physics and is the most interesting thing here, but the clear gap is "
         "usually a centimetre or two of frame and is often below what these clips resolve, so it "
         "is a minor item behind a precondition rather than a core requirement. Their first "
         "standard's 'smoothly' is a rendering property and is not used. Scenario 103, 'A kettle "
         "full of water is placed on a lit stove', is the same physical situation in the Heat "
         "Transfer subcategory of category 3 and carries this mechanism; 103 is judged for the "
         "delay before boiling and the heating, this one for the plume itself.")

add('expanding-smoke-cloud', 118,
    'Thick smoke pours from the grenade, the cloud growing outward and thinning as it mixes into '
    'the air.',
    S(('core', 'A smoke grenade is present.'),
      ('core', 'It is producing smoke.'),
      ('minor', 'The smoke starts after the grenade is set off rather than being there from the '
                'first frame.'),
      ('minor', 'The smoke is thick and opaque near the source, as the caption says.')),
    P(fromsrc('the smoke', 'the grenade'),
      ('core', 'The cloud grows: the region it covers only ever gets larger while the grenade is '
               'still going.',
       'the cloud shrinks back toward the grenade, or it holds one fixed size and outline while '
       'smoke plainly keeps pouring out'),
      ('core', 'The smoke thins as the cloud grows, going from opaque at the source to see-through '
               'at the edges.',
       'the cloud stays uniformly opaque out to a hard edge however far it spreads'),
      ('major', 'The cloud is thickest at the grenade and gets thinner outward from it.',
       'the densest smoke sits out at the edge of the cloud with clear air around the grenade'),
      ('major', 'The edge of the cloud is ragged and broken up rather than a clean geometric '
                'boundary.',
       'the cloud expands as a smooth even shape with a sharp regular outline'),
      ('minor', 'The cloud drifts as one with any air movement in the scene rather than parts of it '
                'going different ways.',
       'separate patches of the cloud travel in opposite directions with nothing to explain it'),
      fixed('the ground and the grenade body')),
    note="Their first key standard asks that the smoke spread 'uniformly'. Taken literally that "
         "rewards the wrong clip: a smoke grenade is a turbulent source and its cloud is lumpy with "
         "a ragged boundary, so a smooth even hemisphere expanding at a constant rate is the "
         "artificial-looking answer, not the correct one. This rubric asks for monotone growth and "
         "a broken edge instead, and keeps their second standard's thinning, which is sound.")

add('still-air-flame', 119,
    'A candle in still air burns with a nearly steady upright flame and gives off no plume of '
    'smoke.',
    S(('core', 'A lit candle is present.'),
      ('core', 'It burns for the whole shot.'),
      ('minor', 'The setting reads as indoors and still -- nothing else in the shot is being blown '
                'about.'),
      ('minor', 'The flame is upright rather than laid over on its side.')),
    P(('fatal', 'The flame stays attached to the wick.',
       'the flame detaches and floats clear of the wick, or it burns at a spot on the candle where '
       'there is no wick'),
      ('core', 'The flame points upward.',
       'the flame points sideways or downward with nothing blowing on it'),
      ('core', 'The flame is nearly steady, moving only slightly, since there is no draught.',
       'the flame whips and gutters as though in a wind, in a room where nothing else moves'),
      ('major', 'The candle gives off no streaming plume of smoke while it burns cleanly.',
       'a thick plume of smoke pours off the wick throughout although the flame burns evenly'),
      ('major', 'The flame stays about the same size and brightness rather than surging and dying '
                'back.',
       'the flame repeatedly flares up and shrinks away with nothing acting on it'),
      ('minor', 'The lit region above the flame shows at most a faint shimmer.',
       'a strong visible column of moving air or haze stands over the flame'),
      fixed('the candle')),
    note="Their sole key standard is 'the smoke from the candle rises smoothly', which is wrong on "
         "both counts. A candle burning steadily in still air is burning close to completely and "
         "produces no visible smoke at all -- visible smoke means the flame is being disturbed or "
         "starved, which is the opposite of what the caption describes -- so a clip that invents a "
         "smoking candle satisfies their standard and gets the physics backwards. 'Smoothly' is a "
         "rendering property besides. The real content of the scenario is that the flame is nearly "
         "still because nothing is moving the air, and that is what this rubric asks for. Scenario "
         "113 is the same candle being blown out and is where a smoke plume does belong.")

# ---- Particle Behavior (120-126) -----------------------------------------
add('wind-borne-sand', 120,
    'Wind lifts sand off the dune, carries it low across the surface and drops it again downwind.',
    S(('core', 'Sand dunes are present.'),
      ('core', 'Sand is lifted off the surface and carried along.'),
      ('minor', 'There are signs of wind beyond the sand itself -- streaming, bending grass, or '
                'drifting haze.'),
      ('minor', 'The setting reads as dunes rather than a flat beach or a sandpit.')),
    P(fromsrc('the moving sand', 'the dune surface'),
      ('core', 'The sand travels one way, consistent across the shot, rather than different patches '
               'going different ways.',
       'sand streams in opposing directions at the same time, or the transport direction reverses '
       'with nothing changing in the scene'),
      ('core', 'Carried sand comes back down to the surface rather than staying up indefinitely.',
       'the lifted sand hangs in the air for the whole shot without ever settling'),
      ('major', 'The sand is carried close to the surface, hopping and skimming along it, with the '
                'most movement in a shallow layer just above the dune.',
       'the grains are lofted high and drift about the sky like dust'),
      ('major', 'The sand is picked up from the exposed windward faces and crests rather than from '
                'sheltered hollows.',
       'sand lifts off the sheltered side of the dune while the exposed crest stays undisturbed'),
      ('minor', 'The dune keeps its overall shape through the shot; only the surface layer moves.',
       'the whole dune slides or reshapes itself over a few seconds'),
      ('minor', 'Grains stay grains: they do not merge into sheets or smear.',
       'the moving sand becomes a continuous ribbon or a smear rather than many separate grains',
       'the shot is close enough to resolve individual grains')),
    note="Their standards are sound but say nothing about height, and that is where these clips go "
         "wrong: saltation keeps blown sand in a shallow layer just above the surface, so a clip "
         "that lofts grains into the sky like dust satisfies both standards -- picked up, carried, "
         "settling -- while showing the wrong process. Requiring the low trajectory and a single "
         "consistent transport direction is what separates the two.")

add('sprinkled-grains', 121,
    'Salt grains fall from the hand, land where they hit and stay there, building an uneven '
    'scatter.',
    S(('core', 'Salt is present and is sprinkled or poured out.'),
      ('core', 'The grains land on a table surface.'),
      ('minor', 'The grains come from a hand, a shaker or a container above the table.'),
      ('minor', 'The surface reads as a table rather than the ground or a plate.')),
    P(fromsrc('the salt', 'the hand or shaker above the table'),
      ('core', 'Grains stop where they land and stay put.',
       'the landed grains keep sliding about the table, or they drift across it with nothing '
       'pushing them'),
      ('core', 'The salt on the table only accumulates while more is being sprinkled.',
       'grains vanish off the table as more falls, or the amount on the surface goes down while '
       'sprinkling continues'),
      ('major', 'The grains fall downward and speed up on the way.',
       'grains drift sideways or upward on the way to the table, or float down at one slow rate'),
      ('major', 'The scatter is uneven -- denser under the hand, sparser out from it, with no '
                'regular pattern.',
       'the grains land in a neat geometric arrangement, or spread themselves into an even film'),
      ('minor', 'The grains stay separate solid grains rather than fusing or dissolving on the dry '
                'table.',
       'the salt melts into a liquid or merges into a continuous crust on contact'),
      fixed('the table')),
    note="This is one of the eleven records whose key_standards are wrapped in a dict, so reading "
         "them raw yields the string 'standards'. The real standards -- random scattering on "
         "contact, uneven clusters -- are used here and are sound. What they omit is that grains "
         "come to rest: the commonest wrong answer is salt that keeps creeping about the table "
         "after landing, which their two standards do not exclude.")

add('hourglass-flow', 122,
    'Sand runs through the narrow neck at a steady rate and heaps into a cone with a fixed slope '
    'below.',
    S(('core', 'An hourglass is present.'),
      ('core', 'Sand runs from the upper chamber into the lower one.'),
      ('minor', 'The sand forms a heap in the lower chamber rather than spreading flat.'),
      ('minor', 'The vessel reads as an hourglass rather than a funnel or a jar.')),
    P(('fatal', 'Sand goes from the upper chamber down into the lower one and not the other way.',
       'sand climbs from the lower chamber into the upper one, or the upper level rises while sand '
       'plainly runs out of it'),
      ('core', 'What leaves the top arrives at the bottom: the upper level falls as the lower heap '
               'grows, with neither running on alone.',
       'the upper chamber empties while the lower heap does not grow, or the heap grows while the '
       'upper level holds steady'),
      ('core', 'The flow through the neck holds a steady rate as the upper chamber empties.',
       'the stream slows markedly as the sand above it runs low, the way a draining liquid does, '
       'or it speeds up as the upper chamber empties'),
      ('major', 'The heap below is a cone, highest under the neck, and its sides hold roughly the '
                'same slope as it grows.',
       'the heap builds as a flat layer with no peak under the neck, or its sides steepen into a '
       'pillar as it grows'),
      ('major', 'The stream falls from the neck to the heap along a connected path.',
       'sand appears in the lower chamber with a clear gap between the neck and the heap'),
      ('minor', 'Grains that reach the heap stay on it, sliding down the slope at most.',
       'landed grains bounce back up toward the neck, or the heap collapses flat on its own'),
      fixed('the hourglass')),
    note="Their first standard's requirement of a uniform flow rate is unusually good physics and "
         "is worth stating explicitly, because it is exactly where intuition misleads: a granular "
         "stream through an orifice runs at a rate set by the opening, not by the depth of sand "
         "above it, so it does NOT slow as the upper chamber empties the way a draining liquid "
         "does. Scenario 106 in this same category is the liquid case and has the opposite "
         "requirement. Their 'without clumping' and 'smooth and well-defined surface' are rendering "
         "words and are not used; the physical version of the second is the angle of repose, which "
         "is the item here.")

add('scattered-toss', 123,
    'Tossed rice grains arc up and come down on their own paths, spreading apart and landing over '
    'an area.',
    S(('core', 'A handful of rice is present.'),
      ('core', 'It is thrown into the air.'),
      ('minor', 'The throw starts from a hand rather than the rice already being airborne.'),
      ('minor', 'The grains come down and land within the shot.')),
    P(fromsrc('the rice', 'the hand'),
      ('core', 'Each grain rises, turns over at the top of its path and comes down.',
       'grains climb for the whole shot, or they change direction repeatedly in mid-air with '
       'nothing touching them'),
      ('core', 'The grains spread further apart as they travel and do not come back together.',
       'the grains converge in flight into a tighter clump, or they hold the exact shape of the '
       'handful all the way through'),
      ('major', 'Each grain follows its own path rather than the whole handful moving as one rigid '
                'block.',
       'the grains stay locked in formation and move as a single body'),
      ('major', 'Landed grains stay on the ground.',
       'grains bounce back up to their original height, or they lift off the ground again on their '
       'own'),
      ('minor', 'The grains stay separate solid grains throughout.',
       'grains merge into each other in flight, or break apart into smaller pieces in mid-air'),
      ('minor', 'The grains fall faster than they rise near the ends of their paths, rather than '
                'drifting down at a fixed slow rate.',
       'the grains float down at one unchanging speed after their arc',
       'the shot follows the grains long enough to see the descent')),
    note="Their standards ask for 'realistic arcing motion' and a dispersed landing pattern. "
         "Realistic names no observable. Their dispersion standard is about the landing only, so a "
         "clip in which the handful flies as one rigid clump and then scatters at the last instant "
         "satisfies it; requiring the spread to grow throughout the flight is what catches that. "
         "Scenario 11, 'A stone is thrown across a river', carries projectile-arc for the "
         "single-body version of this.")

add('settling-snowfall', 124,
    'Snowflakes drift slowly down, fluttering as they fall, and build up on the ground.',
    S(('core', 'Snow is falling.'),
      ('core', 'It lands on the ground.'),
      ('minor', 'Snow builds up on the ground over the course of the shot.'),
      ('minor', 'The fall reads as gentle rather than driven or blizzard-like, as the caption says.')),
    P(('fatal', 'The snow comes down from above.',
       'the flakes travel upward from the ground into the sky'),
      ('core', 'The flakes go downward overall, however much they drift on the way.',
       'flakes rise steadily for a stretch with nothing lifting them, or they hang at one height '
       'for the whole shot'),
      ('core', 'The flakes fall slowly -- far slower than a solid object of the same size dropped '
               'in the same shot would.',
       'the flakes drop like gravel, straight and fast, with no drift at all'),
      ('major', 'What is on the ground only builds up; it does not thin out while snow is still '
                'falling.',
       'the accumulated snow gets thinner or disappears while flakes keep landing on it'),
      ('major', 'Flakes drift and flutter on the way down rather than all following the same '
                'straight line at the same speed.',
       'every flake falls along an identical vertical line at an identical rate'),
      ('minor', 'Landed flakes stay on the ground.',
       'flakes bounce off the ground and back into the air, or lift off again on their own'),
      ('minor', 'Flakes stay whole on the way down.',
       'flakes split apart or merge with each other in mid-air',
       'the shot is close enough to resolve individual flakes')),
    note="Their standards are sound. The item added is the fall speed: 'realistic falling "
         "trajectories including drifting and fluttering' constrains the path but not the rate, and "
         "the commonest wrong answer is snow that drifts prettily while descending as fast as "
         "gravel. Scenario 54, 'A feather falls to the ground', carries air-resistance-descent for "
         "the single-body version of the same balance between weight and drag.")

add('fluttering-confetti', 125,
    'Thrown confetti tumbles and spins on the way down, the pieces falling at different rates and '
    'landing over an area.',
    S(('core', 'Confetti is present.'),
      ('core', 'It is thrown into the air.'),
      ('minor', 'The setting reads as a party or a celebration.'),
      ('minor', 'The throw starts from a hand rather than the confetti already being airborne.')),
    P(fromsrc('the confetti', 'the hand'),
      ('core', 'The pieces come down overall rather than climbing or holding station.',
       'the pieces rise steadily for the rest of the shot, or they hang at a fixed height with '
       'nothing holding them up'),
      ('core', 'The pieces fall slowly and unevenly, taking visibly different times to come down.',
       'every piece drops at the same rate along the same kind of path, or they all fall as fast '
       'as solid pellets'),
      ('major', 'The pieces flutter, tip and spin as they fall rather than gliding down flat and '
                'level.',
       'the pieces descend without ever changing their orientation'),
      ('major', 'Landed pieces stay down.',
       'pieces bounce off the floor back to their starting height, or they lift off the floor again '
       'on their own'),
      ('minor', 'Each piece stays one flat solid piece.',
       'pieces merge together in flight, or crumple and re-form as they fall'),
      ('minor', 'The pieces spread apart as they fall and do not gather back together.',
       'the pieces converge into a tight clump in mid-air')),
    note="Their two standards are unusually well chosen for this category -- irregular "
         "trajectories with flutter or spin, and a non-uniform descent -- and this rubric follows "
         "them rather than departing from them. The additions are the ones that hold for every "
         "falling-particle scenario here: the pieces stay whole, they stay down once landed, and "
         "the spread grows rather than shrinking.")

add('rising-sparks', 126,
    'Glowing sparks are carried up off the fire, dimming as they cool, and go out.',
    S(('core', 'A campfire is present.'),
      ('core', 'Sparks come off it.'),
      ('minor', 'The sparks are glowing and stand out against a darker background.'),
      ('minor', 'The sparks rise rather than falling away from the fire.')),
    P(fromsrc('the sparks', 'the fire'),
      ('core', 'The sparks are carried upward off the fire, in the direction the hot air goes.',
       'the sparks stream steadily downward out of the fire, or they leave it sideways in a flat '
       'sheet with the smoke plainly going up'),
      ('core', 'Each spark only ever dims: once it has faded it does not brighten again.',
       'a fading spark flares back to full brightness, or the sparks get brighter the further from '
       'the fire they get'),
      ('major', 'The sparks go out and stop being visible rather than rising as bright points '
                'indefinitely.',
       'the sparks keep their brightness right out of frame with no dimming at all'),
      ('major', 'The sparks take a variety of paths and speeds rather than all following one track.',
       'every spark travels the same line at the same rate, like beads on a wire'),
      ('minor', 'The sparks stay small points rather than growing as they rise.',
       'a spark swells into a large glowing blob as it climbs'),
      ('minor', 'The sparks follow the same air movement the smoke shows.',
       'the sparks and the smoke go opposite ways at the same moment',
       'smoke is visible in the same shot')),
    note="Their standards are sound. The one they leave implicit is the direction of the brightness "
         "change: 'gradually dim and fade out as they ascend' is satisfied by a spark that flickers "
         "brighter and dimmer on the way up so long as it ends dark, and a re-brightening spark is "
         "a violation, since the ember only cools. Making the dimming monotone is what closes that.")

# ---- Buoyancy and Floating (127-133) -------------------------------------
add('oil-water-layering', 127,
    'Poured oil separates from the water and settles as a layer resting on top of it.',
    S(('core', 'A cup of water is present.'),
      ('core', 'Oil is poured into it.'),
      ('minor', 'The oil is recognisable as a separate liquid from the water -- a different colour '
                'or clarity.'),
      ('minor', 'The vessel reads as a cup rather than a bottle or a bowl.')),
    P(('fatal', 'The oil ends up above the water, not below it.',
       'the oil settles underneath the water, or it stays evenly mixed through it for the whole '
       'shot'),
      ('core', 'The oil and water separate into distinct regions with a boundary between them.',
       'the two blend into one uniform liquid and stay that way'),
      ('core', 'The total in the cup grows as oil is added.',
       'the level in the cup does not change while oil is plainly poured in, or it drops'),
      ('major', 'Once separated, the two do not mix back together on their own.',
       'the settled layers churn back into a uniform blend with nothing stirring them'),
      ('major', 'The boundary between the layers settles level rather than staying tilted or '
                'wandering.',
       'the interface holds a permanent slope, or it drifts up and down with nothing acting on it'),
      ('minor', 'Oil that is still coming down through the water moves upward toward the surface.',
       'a blob of oil released in the water sinks toward the bottom',
       'oil is visible below the surface on the way to the top'),
      fixed('the cup')),
    note="Their standards are sound and this rubric follows them. The additions are the "
         "irreversibility -- separated layers do not re-mix without stirring -- and the direction "
         "of travel for oil still in the water, which is what catches a clip that gets the final "
         "arrangement right by having the oil sink and then teleport to the top.")

add('wave-following-float', 128,
    'A buoy sits upright in the water and rides up and down as the waves pass under it.',
    S(('core', 'A buoy is present.'),
      ('core', 'It is in the water.'),
      ('core', 'It moves up and down with the water rather than sitting motionless.'),
      ('minor', 'The setting reads as open ocean rather than a pool or a pond.')),
    P(cons('the buoy'),
      floatline('the buoy'),
      ('core', 'The buoy goes up when the water under it rises and down when it falls.',
       'the buoy rises as a trough passes under it, or it moves up and down out of step with the '
       'water around it'),
      ('major', 'The buoy stays upright, and if a wave tips it, it comes back up.',
       'the buoy lies over on its side and stays there, or it floats upside down'),
      ('major', 'The buoy stays with roughly the same patch of water rather than being carried '
                'steadily off across the surface.',
       'the buoy travels across the ocean at the speed of the wave crests'),
      marks('the buoy', 'its markings and its light')),
    note="Their standards are sound. The addition is the phase: 'rises and falls in response to "
         "the waves' does not fix which way, and a buoy that dips into crests and rises into "
         "troughs satisfies the wording while inverting the physics. The other addition is that "
         "the buoy does not travel with the crests -- surface waves carry the shape along, not the "
         "water, so a floating body bobs roughly in place.")

add('surface-tension-float', 129,
    'A leaf flutters down onto the pond and rests on the surface, dimpling it without sinking.',
    S(('core', 'A leaf is present.'),
      ('core', 'It falls into the pond and reaches the water.'),
      ('minor', 'The leaf floats rather than going under, as the caption says.'),
      ('minor', 'The setting reads as a pond rather than a container of water.')),
    P(cons('the leaf'),
      ('core', 'The leaf stays on the surface and does not sink.',
       'the leaf goes under and settles below the surface'),
      ('core', 'The leaf falls slowly, fluttering and tipping on the way down.',
       'the leaf drops straight and fast like a stone, with no drift or tipping at all'),
      ('major', 'The landing disturbs the water a little and the surface then settles back.',
       'the leaf lands with a heavy splash out of proportion to it, or the surface does not respond '
       'at all to the landing'),
      ('major', 'The leaf rests on top of the water rather than being held partly through the '
                'surface at a fixed depth.',
       'the leaf floats with its middle below the water line and its edges above it, held at one '
       'depth'),
      ('minor', 'The water dips slightly around the leaf where it presses on the surface.',
       'the surface stays perfectly flat right up to the leaf edge, or the leaf sits raised clear '
       'of the water',
       'the shot is close enough to the leaf to show the surface around it'),
      fixed('the pond and its banks')),
    note="Their second key standard, the small depression around the leaf, is correct but it is a "
         "millimetre-scale feature and most of these clips cannot resolve it, so it is a minor item "
         "behind a precondition. Their standards say nothing about the fall, which is the other "
         "half of the caption and the easier thing to get wrong: a leaf is light and broad, so it "
         "flutters down slowly rather than dropping like a stone.")

add('light-float-bob', 130,
    'A thrown beach ball hits the water, pushes under, springs back up and settles riding high.',
    S(('core', 'A beach ball is present.'),
      ('core', 'It is thrown into the pool and reaches the water.'),
      ('minor', 'The ball floats rather than going under, as the caption says.'),
      ('minor', 'The setting reads as a pool rather than open water.')),
    P(cons('the ball'),
      ('core', 'The ball ends up floating with much more of it above the water than below.',
       'the ball settles mostly submerged, or it sinks out of sight'),
      ('core', 'The impact pushes the ball into the water and it comes back up.',
       'the ball stops dead on contact with the surface and settles without ever dipping, or it '
       'stays pushed under after the impact'),
      ('major', 'The bobbing after the impact gets smaller each time until the ball rides steady.',
       'the ball keeps bobbing to the same height indefinitely, or the bobbing grows'),
      ('major', 'The impact throws up water and sends ripples out, and the surface then settles.',
       'the ball lands on a surface that does not respond at all, or the water stays churned for '
       'the rest of the shot'),
      ('minor', 'The ball keeps its round inflated shape through the impact.',
       'the ball flattens against the water and stays deformed'),
      marks('the ball', 'its coloured panels')),
    note="Their first standard asks only that the ball float 'partially submerged, with a "
         "noticeable portion above the surface', which an almost fully sunken ball satisfies. A "
         "beach ball is mostly air, so it rides very high -- that is the discriminating observable "
         "and it is a core item here. Their 'reacting naturally' names no observable; the physical "
         "version is the overshoot at impact and the decay of the bobbing, which is what this "
         "rubric asks for. Scenario 131 is the same mechanism for a cork.")

add('overshoot-then-float', 131,
    'A dropped cork dips below the surface, springs back up and settles floating high in the water.',
    S(('core', 'A cork is present.'),
      ('core', 'It is dropped into the glass of water and reaches the water.'),
      ('minor', 'The cork starts above the water rather than already being in it.'),
      ('minor', 'The vessel reads as a drinking glass.')),
    P(cons('the cork'),
      ('core', 'The cork dips below where the surface was and then rises back up.',
       'the cork stops at the surface on contact and never goes below it, or it stays down after '
       'dipping'),
      ('core', 'The cork settles floating with most of it above the water.',
       'the cork settles mostly under the water, or it sinks to the bottom of the glass'),
      ('major', 'The bobbing dies away until the cork rides steady.',
       'the cork keeps dipping and rising to the same depth for the rest of the shot'),
      ('major', 'The cork speeds up as it falls to the water.',
       'the cork drifts down to the surface at one unchanging slow rate'),
      ('minor', 'The water level in the glass rises slightly when the cork goes in.',
       'the level drops as the cork enters, or it does not change at all',
       'the water line against the glass is visible before and after the cork lands'),
      fixed('the glass')),
    note="Their standards for this scenario are good -- they name the overshoot, which most of the "
         "records in this subcategory leave out -- and this rubric follows them. What they omit is "
         "how high the cork ends up riding, and the decay of the bobbing. Scenario 130 is the same "
         "mechanism for a beach ball; scenario 132 is the contrasting case where the floating body "
         "rides low.")

add('ice-flotation', 132,
    'An ice cube floats in the drink with most of its bulk below the surface, bobbing gently.',
    S(('core', 'A drink is present.'),
      ('core', 'An ice cube is in it.'),
      ('minor', 'The ice floats rather than resting on the bottom, as the caption says.'),
      ('minor', 'The vessel reads as a glass of drink rather than a pan or a bowl.')),
    P(cons('the ice cube'),
      ('core', 'The ice floats with most of its bulk below the surface and only a little standing '
               'above it.',
       'the ice rides high on the surface the way a cork does, or it sits entirely above the liquid'),
      ('core', 'The ice stays at the surface rather than sinking or being held at a fixed depth '
               'below it.',
       'the ice settles on the bottom of the glass, or it hangs motionless in the middle of the '
       'drink'),
      ('major', 'The ice keeps about the same part of itself submerged as it moves.',
       'the ice slides up and down through the surface with nothing disturbing the drink'),
      ('major', 'The ice bobs or turns only a little, and any motion dies down.',
       'the ice churns around the glass for the whole shot with nothing stirring it'),
      ('minor', 'The ice stays solid and about the same size over these few seconds.',
       'the cube visibly shrinks away to nothing, or it grows'),
      fixed('the glass')),
    note="Their first standard, 'floats partially submerged', is satisfied by an ice cube riding "
         "high like a cork, which is the commonest wrong answer: ice is only slightly less dense "
         "than the liquid, so most of the cube is under the surface and only a little stands proud. "
         "That fraction is the discriminating observable and it is core here. Scenarios 130 and 131 "
         "are the contrasting light-float case. Scenario 100, 'Ice cubes are placed in a glass of "
         "hot water', is the same objects judged for melting instead and carries ice-melting.")

add('current-drift', 133,
    'A log floats down the river, carried along at the speed of the water around it.',
    S(('core', 'A log is present.'),
      ('core', 'It floats in the river.'),
      ('core', 'It travels downstream over the course of the shot.'),
      ('minor', 'The setting reads as a river with a current rather than still water.')),
    P(cons('the log'),
      floatline('the log'),
      ('core', 'The log travels the way the water travels and at about the water\'s speed.',
       'the log moves upstream against the current, or it overtakes the surface water around it'),
      ('major', 'The log keeps moving rather than stopping in open water.',
       'the log comes to a halt in the middle of the flowing river with nothing holding it'),
      ('major', 'The water parts around the log and closes behind it as it goes.',
       'the water surface is undisturbed by the log, or a standing hole follows it downstream'),
      ('minor', 'The log turns only slowly as it drifts, rather than spinning.',
       'the log rotates rapidly in open water with nothing driving it'),
      marks('the log', 'its bark and its cut ends')),
    note="Their physics_prompt asserts that 'the majority of its mass' rides above water, and that "
         "is not generally true: most woods have a density not far below water's, and a soaked log "
         "floats low with roughly half its bulk under. Requiring a high-riding log would fail a "
         "correct clip, so this rubric asks only that the waterline stay put. Their standards are "
         "otherwise sound; the addition is that the log matches the water's speed rather than "
         "merely 'moving steadily', which a log cutting across the current at its own pace would "
         "satisfy.")

# ---- Viscosity and Flow (134-140) ----------------------------------------
add('yield-stress-flow', 134,
    'Nothing comes out of the upended ketchup bottle at first, then it gives way and runs out in a '
    'thick slug.',
    S(('core', 'An open ketchup bottle is present.'),
      ('core', 'It is held upside down.'),
      ('core', 'Ketchup comes out during the shot.'),
      ('minor', 'Nothing flows for a moment after it is inverted, as the caption says.')),
    P(('fatal', 'The ketchup leaves the bottle downward, under gravity.',
       'ketchup flows upward out of the inverted bottle, or it appears below the neck with a gap '
       'between it and the bottle'),
      ('core', 'There is a delay: the ketchup holds in the inverted bottle before any of it moves.',
       'ketchup pours out the instant the bottle is turned over, the way a thin liquid would'),
      ('core', 'What comes out is thick -- it leaves as a slug or a heavy stream, not as a fast '
               'thin jet or a spray.',
       'the ketchup runs out like water, in a thin quick stream'),
      ('major', 'The ketchup that lands heaps up before it spreads.',
       'the ketchup spreads out flat and level the instant it lands'),
      ('major', 'The bottle empties monotonically: what is left inside only goes down.',
       'the level inside the bottle rises again while ketchup is still coming out'),
      ('minor', 'The ketchup keeps its own colour and body rather than thinning to a watery liquid '
                'as it goes.',
       'the ketchup turns pale and runny between leaving the bottle and landing'),
      fixed('the bottle')),
    note="Their first two standards -- the delay, then a rapid flow -- capture the yield-stress "
         "behaviour and are used. Their third, 'smooth and uninterrupted', is not: real ketchup "
         "comes out in glugs as air works back up the bottle, so requiring an uninterrupted flow "
         "would fail correct footage. This rubric asks instead that what emerges be visibly thick "
         "and that it heap on landing, which is what separates ketchup from water.")

add('viscous-thread', 135,
    'Honey runs off the spoon in a slow thick thread that stays unbroken and mounds up in the jar.',
    S(('core', 'A spoon with honey on it is present.'),
      ('core', 'Honey runs off the spoon.'),
      ('core', 'It goes into a jar below.'),
      ('minor', 'The honey reads as honey -- thick, translucent and amber.')),
    P(('fatal', 'The honey runs downward off the spoon into the jar.',
       'the honey runs upward off the spoon, or it appears in the jar with a gap between it and the '
       'spoon'),
      ('core', 'The honey moves slowly, far more slowly than water off the same spoon would.',
       'the honey runs off as fast and freely as water'),
      ('core', 'The falling honey stays a connected thread over this short drop rather than '
               'breaking into separate drops.',
       'the stream breaks up into a string of falling droplets on the way to the jar'),
      ('major', 'The honey mounds up where it lands and only slowly levels out.',
       'the honey spreads flat across the jar the moment it lands'),
      ('major', 'The thread stays attached to the spoon and thins as it stretches rather than '
                'keeping one width.',
       'the thread holds exactly the same thickness from spoon to jar throughout'),
      ('minor', 'Honey clings to the spoon and coats it rather than running off clean.',
       'the spoon comes away completely dry while honey is still falling'),
      fixed('the jar')),
    note="Their standards -- a continuous thick stream, moving slowly -- are sound and are used. "
         "The additions are the two visible consequences of high viscosity that the standards do "
         "not name: honey mounds where it lands instead of levelling, and it coats the spoon it "
         "leaves. Both are what separate a slowed-down water clip from an actual honey clip.")

add('thin-film-spread', 136,
    'Poured oil runs out across the pan and wets it as a thin film whose edge only advances.',
    S(('core', 'A frying pan is present.'),
      ('core', 'Oil is poured into it.'),
      ('core', 'The oil spreads across the pan surface.'),
      ('minor', 'The oil reads as a thin layer rather than a deep pool.')),
    P(('fatal', 'The oil stays in the pan.',
       'the oil runs up the sides and out of a level pan, or it sinks into the metal and disappears'),
      ('core', 'The oil spreads outward from where it lands, and the wetted area only grows.',
       'the wetted area shrinks back toward the pouring point, or oil appears on parts of the pan '
       'that the spreading film never reached'),
      ('core', 'The oil ends as a thin film lying on the pan rather than standing up as a dome or '
               'a bead pile.',
       'the oil settles as a raised mound that holds its own height in the middle of the pan'),
      ('major', 'The oil spreads quickly, the way a thin liquid does, rather than creeping.',
       'the oil advances as slowly as honey would across the same pan'),
      ('major', 'The film keeps the pan wet behind the advancing edge.',
       'the pan dries out behind the leading edge as the oil moves on'),
      ('minor', 'The advancing edge is uneven, running further where the pan is lower.',
       'the edge advances as a perfect circle regardless of how the pan sits'),
      fixed('the pan')),
    note="Their first standard's 'smoothly ... without abrupt stops' is a rendering property and is "
         "not used. Their second asks for a layer 'without visible clumps or thicker regions', "
         "which is too strong: a real thin oil film has an uneven leading edge, pools toward "
         "whichever part of the pan is lowest, and can bead on a non-stick surface, so a clip "
         "showing any of that would be marked wrong for being correct. This rubric asks for a thin "
         "film and monotone spreading, and treats the unevenness as expected rather than as a "
         "fault.")

add('clinging-cascade', 137,
    'Molasses creeps down over the pancakes as one thick unbroken sheet, clinging to what it '
    'covers.',
    S(('core', 'A stack of pancakes is present.'),
      ('core', 'Molasses is poured onto it.'),
      ('core', 'The molasses moves down over the stack.'),
      ('minor', 'The molasses reads as thick and dark rather than thin and watery.')),
    P(('fatal', 'The molasses runs downward over the stack, under gravity.',
       'the molasses climbs up the side of the stack, or it appears part-way down with nothing '
       'above it'),
      ('core', 'The molasses moves slowly, far more slowly than a thin syrup would.',
       'the molasses runs down and off the stack as quickly as water'),
      ('core', 'It stays a connected sheet or stream rather than breaking into separate droplets.',
       'the flow breaks up into individual drops running down the side'),
      ('major', 'The molasses clings to the pancakes it passes over, leaving them coated, rather '
                'than running clear off them.',
       'the molasses slides down leaving the pancake surfaces behind it dry'),
      ('major', 'It mounds on the top of the stack before it goes over the edge.',
       'it reaches the edge and starts down the side without ever building up on top'),
      ('minor', 'The advancing front slows as it thins out further down the stack.',
       'the front runs down the whole stack at one unchanging rate'),
      fixed('the stack of pancakes')),
    note="Their standards -- slow cascade, no break-up into droplets -- are sound and are used. "
         "The additions are the clinging and the mounding: a high-viscosity liquid wets what it "
         "runs over and piles up before it spills, and a clip that has molasses sheeting straight "
         "off dry pancakes satisfies both of their standards while looking nothing like molasses.")

add('bead-holding-flow', 138,
    'Glue squeezes out onto the paper as a raised line that holds its shape where it is laid down.',
    S(('core', 'A bottle of glue is present.'),
      ('core', 'Glue comes out of it onto paper.'),
      ('core', 'The glue forms lines or a trail on the paper, as the caption says.'),
      ('minor', 'The glue reads as thick rather than watery.')),
    P(('fatal', 'The glue comes out of the bottle nozzle and goes onto the paper.',
       'glue appears on the paper with the bottle plainly closed or held away, or it flows from the '
       'paper back into the bottle'),
      ('core', 'The glue holds a raised bead where it lands rather than flattening out to nothing.',
       'the glue spreads instantly into a flat wet sheet across the paper'),
      ('core', 'The glue stays where it is laid down.',
       'the laid line slides across the paper, or it runs off the sheet on level paper'),
      ('major', 'The glue leaves the bottle slowly and thickly rather than jetting or spraying out.',
       'the glue squirts out in a fast thin stream'),
      ('major', 'The line only grows while glue is still coming out; laid glue does not disappear.',
       'parts of the line vanish from the paper while more glue is being applied'),
      ('minor', 'The paper darkens or dampens slightly where the glue sits.',
       'the paper stays visibly bone dry directly under a wet bead',
       'the shot is close enough to the paper to show its surface'),
      fixed('the paper')),
    note="Their first standard, 'a consistent and controlled flow rate', names no physical "
         "observable -- controlled is about the hand, not the fluid -- and is not used. Their "
         "second, thick continuous lines, is the usable half and is here. The item that does the "
         "real work is one they do not have: the bead stands proud of the paper and keeps its "
         "shape, which is what separates glue from water and is the thing a generated clip most "
         "often gets wrong by letting the line spread flat.")

add('cooling-lava-flow', 139,
    'Lava creeps down the volcano, darkening and stiffening as it cools, and its front slows.',
    S(('core', 'A volcano or its slope is present.'),
      ('core', 'Lava flows down the side of it.'),
      ('minor', 'The lava glows, standing out against the darker slope.'),
      ('minor', 'The flow reads as sluggish rather than as fast as water.')),
    P(('fatal', 'The lava flows downhill.',
       'the lava runs uphill, or it appears further down the slope with a gap above it'),
      ('core', 'The lava moves slowly and heavily, far more slowly than water down the same slope.',
       'the lava races down the slope the way a flood would'),
      ('core', 'The lava darkens and crusts over as it goes further from the vent, and does not '
               'brighten back up.',
       'the flow gets brighter and more molten the further downhill it travels, or it holds exactly '
       'one colour and brightness throughout'),
      ('major', 'The front slows as the lava cools and thickens.',
       'the leading edge advances at one unchanging speed all the way down, or it speeds up as it '
       'descends'),
      ('major', 'The brightest lava is at the vent and in cracks in the crust rather than on the '
                'cooled outer surface.',
       'the crusted surface glows brighter than the freshly erupted lava'),
      ('minor', 'The lava stays a connected flow rather than breaking into separate droplets.',
       'the flow breaks up into a shower of falling drops on the slope'),
      fixed('the slope and any rock it passes')),
    note="Their standards -- slow steady descent, visibly thickening texture as it descends -- are "
         "sound and are used. The additions tie the two together: the thickening is caused by "
         "cooling, so the colour change has a direction (darker, never brighter) and it has a "
         "consequence (the front slows). A clip that thickens the texture while brightening the "
         "glow satisfies their wording and has the mechanism backwards.")

add('irreversible-blending', 140,
    'Poured paint spreads out across the canvas and the colours blend where they meet, and stay '
    'blended.',
    S(('core', 'A canvas is present.'),
      ('core', 'Paint is poured onto it.'),
      ('core', 'The paint spreads across the canvas surface.'),
      ('minor', 'The paint reads as thick and coloured rather than as a thin wash.')),
    P(('fatal', 'The paint stays on the canvas.',
       'the paint sinks through the canvas and out of sight, or it lifts off the surface into the '
       'air'),
      ('core', 'The painted area only grows: paint that has landed does not lift back off or shrink '
               'away.',
       'painted regions shrink back or vanish from the canvas while more paint is being poured'),
      ('core', 'Where two colours meet and blend, they stay blended.',
       'blended paint separates back out into the original clean colours'),
      ('major', 'The paint spreads outward from where it lands rather than appearing across the '
                'canvas at once.',
       'paint shows up in places the spreading never reached'),
      ('major', 'The blending happens only where the colours actually touch.',
       'colours change in regions that no other colour has reached'),
      ('minor', 'The spreading slows as the paint thins out away from where it landed.',
       'the paint front advances at one unchanging rate however thin it gets'),
      fixed('the canvas')),
    note="Their first standard, 'flows seamlessly without abrupt stops', is a rendering property "
         "and is not used. Their second, spreading and blending at the edges, is the usable half. "
         "The item added on top is the irreversibility: mixing paint is a one-way process, so a "
         "clip in which blended colours resolve back into clean separate ones -- easy to produce by "
         "running the footage backwards or looping it -- satisfies their standard and is the "
         "clearest possible physics violation in the scene.")
