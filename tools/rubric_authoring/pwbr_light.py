# phyworldbench 176-210: Lighting and Shadows.
# Same authoring flow as the earlier blocks: items come from the caption plus first-principles
# physics, then physics_prompt and key_standards are diffed for coverage; conflicts are followed
# on the side of physics and recorded in `note`. Cross-check against KS[i].
#
# Four things recur across this category.
#
# First, and worst: a large group of standards asks for illumination to stay CONSTANT in scenarios
# whose whole physical content is that it varies. 176 wants a rotating lighthouse beam to keep the
# water 'uniformly consistent', 181 wants even brightness on falling snow, 182 wants headlight
# beams at 'constant intensity and spread' while the car drives through a tunnel. In each case the
# standard is satisfied by a flat static wash -- the artefact the scenario exists to catch -- and
# would fail the correct clip. Those are followed on the side of physics and noted.
#
# Second, the category leans on rendering words even harder than the fluid block did: 'no sudden
# jumps or interruptions', 'without visible artifacts or distortions', 'no abrupt changes',
# 'maintains realistic intensity', 'without exaggerated or artificial effects'. These name no
# physical observable and are excluded by _policy.json's not_penalized list.
#
# Third, geometry is the thing these clips actually get wrong, and almost no standard asks for it:
# which side of an object its shadow falls on, which way a shadow swings when the light moves,
# whether the lit face is the one turned toward the source. Those items are written from scratch
# throughout.
#
# Fourth, id 196's physics_prompt is a copy-paste artefact -- it describes sunlight on a mirror in
# a room, not icicles on a tree -- and its key standard follows the wrong scenario too. That entry
# is written from the caption alone.


def shadow_away(o, src):
    return ('core', f'The shadow of {o} falls on the far side of it from {src}, along the line from '
                    f'{src} past {o}.',
            f'the shadow lies on the same side as {src}, or it points in a direction unrelated to '
            f'where {src} is')


def shadow_tracks(o):
    return ('core', f'The shadow moves as {o} moves, and stops when it stops.',
            f'the shadow drifts about while {o} is still, or it stays put while {o} moves')


def lit_side(o, src):
    return ('major', f'The side of {o} turned toward {src} is the lit one, and the side away from '
                     f'it is darker.',
            f'{o} is brightest on the face turned away from {src}, or it is lit evenly all round '
            f'from a source on one side')


def blocked_only(o):
    return ('major', f'Light is missing only where {o} actually stands in its way.',
            f'shadow appears in places nothing is blocking, or light passes through {o} as though '
            f'it were not there')


def selfglow(o):
    return ('fatal', f'{o[0].upper()}{o[1:]} is lit by the light in the scene and does not give out '
                     f'light of its own.',
            f'{o} glows in its own right, brighter than anything falling on it can account for')


def fixed(o):
    pl = ' and ' in o
    return ('minor',
            f'{o[0].upper()}{o[1:]} stay put and keep their shape throughout.' if pl else
            f'{o[0].upper()}{o[1:]} stays put and keeps its shape throughout.',
            f'{o} shift, flex or change shape on their own' if pl else
            f'{o} shifts, flexes or changes shape on its own')


# ---- Consistency of Illumination (176-182) -------------------------------
add('sweeping-beam', 176,
    'A rotating lighthouse beam sweeps across the water, lighting each patch only as it passes over '
    'it.',
    S(('core', 'A lighthouse or its lamp is present.'),
      ('core', 'A beam sweeps across the water.'),
      ('minor', 'The beam turns steadily rather than jumping from place to place.'),
      ('minor', 'The setting reads as ocean rather than a lake or a harbour basin.')),
    P(('fatal', 'The beam comes from the lighthouse lamp and stays attached to it.',
       'the beam starts out in open air away from the lamp, or it sweeps the water while the lamp '
       'is plainly dark'),
      ('core', 'Any given patch of water brightens as the beam reaches it and darkens again once '
               'the beam has gone by.',
       'the whole water surface stays evenly lit throughout while a beam is plainly sweeping across '
       'it'),
      ('core', 'The beam sweeps in one rotational sense and keeps to it, rather than jumping back '
               'and forth.',
       'the beam reverses its sweep direction on its own part-way round'),
      ('major', 'The lit patch travels along the water continuously, passing through the places in '
                'between.',
       'the lit patch disappears from one part of the water and reappears somewhere else without '
       'crossing the gap'),
      ('major', 'Water outside the beam is darker than water inside it.',
       'the water off the beam is as bright as the water the beam is on'),
      ('minor', 'The lit patch is broader and dimmer the further from the lighthouse it is.',
       'the far end of the beam is as tight and as bright as the near end'),
      fixed('the lighthouse')),
    note="Their second standard asks that 'the intensity and pattern of illumination on the water "
         "should remain uniformly consistent as the beam rotates', which is the opposite of what a "
         "rotating beam does: the whole point is that each patch of water is lit only while the beam "
         "is on it. A flat even wash over the sea satisfies their standard and is exactly the "
         "artefact to catch, so the core item here requires the brightening and darkening instead. "
         "Their first standard's 'no sudden jumps or interruptions' has a usable physical core -- the "
         "lit patch must travel continuously -- and that is kept as a major item; the rendering "
         "reading of it is not used.")

add('moving-torch-beam', 177,
    'A carried flashlight lights what its beam falls on and leaves the rest of the dark room unlit.',
    S(('core', 'A flashlight is present.'),
      ('core', 'It moves across the room.'),
      ('core', 'Its beam lights parts of the room.'),
      ('minor', 'The room is dark apart from the flashlight, as the caption says.')),
    P(('fatal', 'The beam comes from the flashlight and moves with it.',
       'the beam stays pointing at one spot while the flashlight is turned elsewhere, or light comes '
       'out of the room with the flashlight plainly off'),
      ('core', 'Only what the beam is on is lit; the rest of the room stays dark.',
       'the whole room is generally visible although the flashlight is the only light in it'),
      ('core', 'As the flashlight moves, what was lit goes dark and what the beam reaches lights up.',
       'objects stay lit after the beam has moved off them, or they light up before the beam gets '
       'to them'),
      ('major', 'Objects in the beam throw shadows away from the flashlight.',
       'shadows in the lit region point back toward the flashlight, or lit objects cast no shadow at '
       'all in a dark room'),
      ('major', 'Objects nearer the flashlight are lit more strongly than ones further along the '
                'beam.',
       'the far end of the beam is as bright as what is right in front of the lens'),
      ('minor', 'A shadow swings round as the flashlight moves, rather than holding one direction.',
       'the shadows keep pointing the same way while the flashlight is carried past them'),
      fixed('the room and its furniture')),
    note="Their three standards -- objects in the beam are lit, shadow edges stay clear, areas "
         "outside the beam stay dark -- are all usable and are all here. The additions are the ones "
         "that make it a moving light rather than a moving spotlight cut-out: what was lit must go "
         "dark again as the beam leaves it, the shadows must point away from the torch and swing as "
         "it travels, and the beam must fall off with distance. A clip in which shadows keep a fixed "
         "direction while the torch moves across the room satisfies all three of their standards.")

add('advancing-sunrise', 178,
    'Rising sunlight reaches the peaks first and the shadow line works its way down the slopes.',
    S(('core', 'A mountain range is present.'),
      ('core', 'Sunlight reaches it during the shot.'),
      ('core', 'The lit region changes over the shot rather than staying as it began.'),
      ('minor', 'The valleys are still in shadow while the peaks are lit, as the caption says.')),
    P(('fatal', 'The light comes from one direction and everything in the scene is lit consistently '
                'with it.',
       'different peaks are lit from opposite sides at the same time'),
      ('core', 'The peaks light before the valleys, and the boundary between lit and shadowed rock '
               'works its way downward over the shot.',
       'the valleys light first and the peaks last, or the shadow line climbs the slopes as the sun '
       'rises'),
      ('core', 'The lit area only grows while the sun is rising.',
       'lit rock goes back into shadow while the sun is plainly still coming up'),
      ('major', 'Shadows shorten as the sun gets higher.',
       'the shadows lengthen as the sun climbs'),
      ('major', 'Slopes facing the sun are lit and slopes facing away stay dark.',
       'a slope turned away from the sun is the bright one'),
      ('minor', 'The lit rock brightens gradually rather than switching on.',
       'a peak goes from full shadow to full sunlight between one frame and the next'),
      fixed('the mountain range')),
    note="Their standards -- gradual transition, valleys shadowed until the light reaches them -- "
         "are sound and are used, with the third ('no sudden changes ... in brightness') taken in "
         "its physical reading as the gradual brightening rather than as a rendering requirement. "
         "What they omit is direction, which is where these clips go wrong: as the sun rises the "
         "terminator moves DOWN the slopes and the shadows SHORTEN, and a clip that runs either of "
         "those backwards satisfies every one of their standards.")

add('carried-candle-shadows', 179,
    'A carried candle swings the shadows around it, throwing them away from the flame and stretching '
    'them as it goes.',
    S(('core', 'A lit candle is present.'),
      ('core', 'It is carried along a hallway.'),
      ('core', 'Shadows on the walls or floor move as it goes.'),
      ('minor', 'The hallway is otherwise dim, so the candle is the light that matters.')),
    P(('fatal', 'The light comes from the candle flame and travels with it.',
       'the shadows are cast as though the light were somewhere the candle is not, or the hallway '
       'stays lit with the candle plainly out'),
      ('core', 'Shadows fall on the far side of objects from the flame.',
       'a shadow lies between an object and the flame'),
      ('core', 'As the candle moves, the shadows swing round the other way, pivoting about the '
               'objects casting them.',
       'the shadows keep one fixed direction as the candle is carried past, or they swing the same '
       'way the candle goes'),
      ('major', 'Things closer to the candle are lit more strongly than things further off.',
       'the far end of the hallway is as bright as what is right beside the flame'),
      ('major', 'A shadow stretches longer as the candle gets further from what casts it, and '
                'shortens as it comes closer.',
       'the shadows keep exactly one length however far the candle travels'),
      ('minor', 'The flicker of the flame and the flicker of the shadows happen together.',
       'the shadows pulse while the flame burns dead steady, or the flame gutters while the shadows '
       'hold perfectly still'),
      fixed('the hallway and its walls')),
    note="Their first standard, that the candlelight 'flickers naturally but maintains realistic "
         "intensity', names no observable and is not used; the physical residue of it is that the "
         "flicker of the flame and of the shadows must be the same event, which is a minor item "
         "here. Their second standard is the usable one and is kept. The geometry is written from "
         "scratch: a shadow cast by a moving nearby source swings the opposite way to the source and "
         "pivots about the object, and a clip whose shadows merely slide along with the candle "
         "satisfies their 'shift smoothly in direct relation to the candle's movement'.")

add('chopped-illumination', 180,
    'Fan blades cut across the light as they turn, so the shadows below sweep round in time with '
    'them.',
    S(('core', 'A ceiling fan is present.'),
      ('core', 'It spins.'),
      ('core', 'A bright light is behind or above it.'),
      ('minor', 'Shadows or brightness changes are visible in the room below.')),
    P(('fatal', 'The blades block the light only while they are between it and the surface below.',
       'a blade shadow appears on the floor with no blade in the light path, or a blade crosses the '
       'lamp with no effect at all on the light below'),
      ('core', 'The shadows below sweep round in the same rotational sense as the blades.',
       'the shadow pattern turns against the direction the fan turns'),
      ('core', 'The flicker below keeps pace with the blades: it repeats as often as blades pass '
               'the light.',
       'the flicker rate is unrelated to how fast the blades pass, or the light pulses while the fan '
       'is plainly still'),
      ('major', 'The blades themselves are dark against the light and lit on the side facing the '
                'lamp.',
       'the blades are bright on the side turned away from the lamp'),
      ('major', 'Light between the blades reaches the floor, so the room is not evenly dim.',
       'the whole room dims uniformly while the fan turns rather than showing moving light and dark'),
      ('minor', 'The blades keep their spacing, so the shadows keep theirs.',
       'the shadow bands bunch up or spread apart while the blades keep their spacing'),
      fixed('the room and the light fitting')),
    note="Their sole standard, that the illumination varies as blades pass the light, is the right "
         "core requirement and is used. Everything else is written from scratch, and the item that "
         "does the most work is the coupling of rate: the flicker must repeat at the blade-passing "
         "rate, so a clip in which the light pulses at some unrelated rhythm, or pulses while the "
         "fan sits still, is caught. Their standard on its own does not tie the two together.")

add('beam-lit-snow', 181,
    'Snowflakes light up as they pass through the lamp light, brightest near the lamp and dark '
    'outside it.',
    S(('core', 'A streetlamp is present and lit.'),
      ('core', 'Snow is falling.'),
      ('core', 'The lamp lights the falling snow.'),
      ('minor', 'The scene is otherwise dark, so the lamp is the light that matters.')),
    P(selfglow('the snow'),
      ('core', 'Flakes are lit while they are in the lamp light and dark outside it, so each flake '
               'brightens and fades as it falls through.',
       'every flake is equally bright wherever it is, including well outside the lit cone'),
      ('core', 'Flakes closer to the lamp are brighter than flakes further away.',
       'flakes at the far edge of the shot are as bright as ones right under the lamp'),
      ('major', 'The lit region is a cone or pool below and around the lamp rather than filling the '
                'whole frame.',
       'the whole scene is uniformly lit although the lamp is the only source in it'),
      ('major', 'The flakes go on falling through the light rather than the lit region holding a '
                'fixed speckle pattern.',
       'the bright specks stay in the same places while snow is plainly falling'),
      ('minor', 'The lamp itself stays about as bright throughout.',
       'the lamp brightens and dims on its own with nothing switching it'),
      fixed('the lamp and its post')),
    note="Their second standard asks that the illumination on the snowflakes be 'even, with no "
         "abrupt changes in brightness'. That is wrong twice over. Flakes are discrete scatterers "
         "moving through a bounded cone of light, so each one does brighten sharply on entering the "
         "beam and fade on leaving it, and brightness falls off with distance from the lamp -- an "
         "evenly lit snowfall is the flat wash this scenario exists to catch. Their first standard, "
         "that the lamp's own brightness stays steady, is sound and is the minor item here.")

add('travelling-headlights', 182,
    'The headlight beams light the tunnel ahead of the car, and the lit patch travels along the walls '
    'as it drives.',
    S(('core', 'A car or its headlights are present.'),
      ('core', 'The car moves through a tunnel.'),
      ('core', 'The headlights light the tunnel walls or floor.'),
      ('minor', 'There are two beams rather than one, as the caption says.')),
    P(('fatal', 'The beams come from the headlights and point where the car is going.',
       'the lit patch is behind the car as it drives forward, or the tunnel is lit with the '
       'headlights plainly off'),
      ('core', 'The lit patch travels along the tunnel with the car, so a given stretch of wall '
               'brightens as the car comes up to it and darkens behind.',
       'the same stretch of wall stays equally lit throughout while the car drives past it'),
      ('core', 'Tunnel surfaces closer to the headlights are lit more strongly than ones further '
               'ahead.',
       'the far end of the tunnel is as bright as the road right in front of the bumper'),
      ('major', 'The two beams stay a fixed distance apart on the car and move together.',
       'the beams cross over, swap sides, or drift apart from each other'),
      ('major', 'The beams widen and weaken the further from the car they reach.',
       'the beams keep the same width and brightness all the way to the far end of the tunnel'),
      ('minor', 'The car casts its own dark region behind it, away from its lights.',
       'the tunnel behind the car is as brightly lit as the stretch ahead of it'),
      fixed('the tunnel')),
    note="Their first standard, that the beams 'maintain a constant intensity and spread', is not "
         "usable. A beam spreads with distance and its illumination falls off, so the patch it makes "
         "on a wall changes size and brightness continuously as the car moves relative to that wall; "
         "a fixed-size fixed-brightness patch is the artefact. Their second standard's 'without "
         "sudden changes in brightness or flickering' is a rendering property and is not used; what "
         "survives from it is the requirement that the lit patch travel continuously, which the core "
         "item covers.")

# ---- Object Occlusion (183-189) ------------------------------------------
add('near-source-occlusion', 183,
    'A person behind the candles is lit from the front by them and throws a shadow back onto the '
    'wall behind.',
    S(('core', 'A row of candles on a table is present.'),
      ('core', 'A person walks behind the candles.'),
      ('core', 'A shadow of the person appears and moves.'),
      ('minor', 'The candles are lit and are the light that matters in the scene.')),
    P(selfglow('the person'),
      ('core', 'The person is lit on the side facing the candles and darker on the side away from '
               'them.',
       'the person is brightest on the side turned away from the candles'),
      ('core', 'The shadow of the person falls on the far side of them from the candles -- onto the '
               'wall or floor behind.',
       'the shadow lies between the person and the candles'),
      shadow_tracks('the person'),
      ('major', 'The person is lit more strongly the closer they come to the candles.',
       'the person stays exactly as bright while walking from close by the candles to the far end of '
       'the table'),
      ('major', 'The shadow grows and shrinks as the person moves nearer to and further from the '
                'candles.',
       'the shadow holds exactly one size however the person moves relative to the flames'),
      ('minor', 'The candles are in front of the person, so they cross in front of parts of them as '
                'they pass.',
       'the person passes in front of the candle flames although they are walking behind them'),
      fixed('the table and the candles')),
    note="Their second standard says that 'as the person occludes the candles, the light on and "
         "around the candles is visibly blocked', which has the geometry the wrong way round: a "
         "person walking BEHIND a row of candles is downstream of the light, so they do not block "
         "it -- they are lit by it and throw a shadow further back. It is not used as written. The "
         "usable half is their first standard, that the movement results in shadow casting, and the "
         "rest is written from the geometry: lit face toward the flames, shadow away from them, and "
         "both brightness and shadow size changing with distance because a candle is a near source.")

add('screen-shadow', 184,
    'A person crossing the projector beam blocks it, so a shadow of them appears on the screen and '
    'the picture falls on them instead.',
    S(('core', 'A projector screen with a picture on it is present.'),
      ('core', 'A person walks in front of it.'),
      ('core', 'A shadow of the person appears on the screen.'),
      ('minor', 'The person passes between the projector and the screen rather than behind the '
                'screen.')),
    P(('fatal', 'The shadow appears on the screen only where the person actually blocks the beam.',
       'a shadow appears on the screen while the person is plainly out of the light path, or the '
       'beam passes through them and leaves the screen unshadowed'),
      ('core', 'The projected picture falls on the person while they are in the beam.',
       'the person stays plainly unlit by the projector while standing in its beam with a shadow on '
       'the screen behind them'),
      shadow_tracks('the person'),
      ('major', 'The shadow is on the opposite side of the person from the projector.',
       'the shadow appears on the projector side of the person'),
      ('major', 'The screen is darker inside the shadow than outside it.',
       'the shadowed region of the screen is as bright as the rest of the picture'),
      ('minor', 'The shadow is larger than the person and grows as they move toward the projector.',
       'the shadow keeps exactly the size of the person however far along the beam they stand'),
      fixed('the screen')),
    note="Their standards -- the shadow corresponds to the person's shape and movement, and light "
         "is clearly reduced where they block it -- are both sound and both used. The addition that "
         "does the most work is the other half of the same occlusion: the light the person "
         "intercepts lands on them, so the projected picture must appear on their body. A clip that "
         "draws a correct shadow on the screen while leaving the person unlit satisfies both of "
         "their standards and is missing the physics.")

add('window-light-occlusion', 185,
    'A cat crossing the sunlit window blocks the sunlight, so its shadow moves across the floor '
    'away from the window.',
    S(('core', 'A sunny window is present.'),
      ('core', 'A cat walks past it.'),
      ('core', 'A shadow of the cat moves across the floor.'),
      ('minor', 'A patch of sunlight is visible on the floor.')),
    P(blocked_only('the cat'),
      shadow_away('the cat', 'the window'),
      shadow_tracks('the cat'),
      ('major', 'The shadow keeps the cat\'s outline -- head, ears, legs, tail -- rather than being '
                'a shapeless blob.',
       'the shadow is a plain patch with no relation to the shape of the cat'),
      ('major', 'The cat is lit on the side facing the window.',
       'the cat is brightest on the side turned away from the window'),
      ('minor', 'The shadow bends and rides over whatever it falls across rather than staying flat '
                'and unbroken over a step or a wall.',
       'the shadow lies perfectly flat across a raised object as though painted on the floor'),
      fixed('the window and the room')),
    note="Their second standard -- 'the shadow overlaps seamlessly with other objects, without "
         "visible artifacts or distortions' -- is a rendering requirement and is not used as "
         "written. Its physical core is the opposite of seamless: a shadow falling across a raised "
         "object bends over it, so it should NOT stay flat, and that inverted version is the minor "
         "item here. Their first standard is sound and is used.")

add('swaying-branch-shadows', 186,
    'A swaying branch chops the streetlight, so the shadows it throws on the ground shift as it '
    'moves.',
    S(('core', 'A tree branch is present.'),
      ('core', 'A streetlight is present and lit.'),
      ('core', 'The branch sways in front of the light.'),
      ('minor', 'Shadows are visible on the ground below.')),
    P(blocked_only('the branch'),
      shadow_away('the branch', 'the streetlight'),
      shadow_tracks('the branch'),
      ('major', 'The ground under the branch is darker than the ground beside it.',
       'the shadowed ground is as bright as the lit ground around it'),
      ('major', 'The shadow keeps the branching shape -- twigs and leaves -- rather than being a '
                'single solid mass.',
       'the shadow is one plain blob with no branch structure in it'),
      ('minor', 'The shadow sways at the same rhythm as the branch, not faster or slower.',
       'the shadow sways at its own rate while the branch moves at another'),
      fixed('the streetlight and its post')),
    note="Their standards -- a noticeable reduction of light on the ground, shadows moving with the "
         "branch -- are both sound and both used. The additions are the ones this whole subcategory "
         "needs: the shadow must be on the far side of the branch from the lamp, and it must keep "
         "the branch's structure. A single dark blob swaying under a tree satisfies both of their "
         "standards.")

add('partial-occlusion-diffuse', 187,
    'A hand over the lamp blocks part of the light, so a soft shadow of it moves across the table '
    'below.',
    S(('core', 'A table lamp is present and lit.'),
      ('core', 'A hand passes over it.'),
      ('core', 'The shadow on the table below changes as the hand moves.'),
      ('minor', 'The hand passes above or across the lamp rather than touching the table.')),
    P(blocked_only('the hand'),
      shadow_away('the hand', 'the lamp'),
      shadow_tracks('the hand'),
      ('major', 'The shadow keeps the shape of the hand -- fingers separately -- rather than being '
                'one solid patch.',
       'the shadow is a featureless blob with no fingers in it'),
      ('major', 'The shadow gets larger and softer as the hand moves away from the table and '
                'sharper as it comes closer.',
       'the shadow keeps exactly one size and one sharpness however far the hand is from the surface'),
      ('minor', 'Where the hand blocks only part of the lamp, the table is dimmed rather than fully '
                'dark.',
       'a hand held partly across the lamp puts the table into complete darkness'),
      fixed('the lamp and the table')),
    note="Their sole standard, changes in shadow intensity and shape on the table, is the right core "
         "requirement and is used. Everything else is written from scratch. The item worth "
         "singling out is the penumbra behaviour: a table lamp is an extended source, so the "
         "shadow softens and grows as the hand rises, and partial blocking gives partial dimming "
         "rather than darkness. This is the same physics as the 204-210 block.")

add('passing-multiple-lights', 188,
    'A cyclist riding past a row of lamps throws a shadow from each one, and each shadow swings as '
    'they pass it.',
    S(('core', 'A cyclist is present.'),
      ('core', 'A row of lights is present.'),
      ('core', 'The cyclist rides past the lights.'),
      ('minor', 'The scene is at night, so the lamps are the light that matters.')),
    P(selfglow('the cyclist'),
      ('core', 'Each lamp throws its own shadow of the cyclist, on the far side from that lamp.',
       'a single shadow follows the cyclist regardless of which lamps they are between, or shadows '
       'point toward the lamps'),
      ('core', 'Each shadow swings round as the cyclist passes its lamp, lengthening ahead and '
               'shortening as they come level with it.',
       'the shadows keep one fixed direction and length all the way along the row'),
      ('major', 'The cyclist is brightest when level with a lamp and dimmer between lamps.',
       'the cyclist stays exactly as bright between the lamps as under them'),
      ('major', 'Shadows appear only where the cyclist blocks a lamp; the road elsewhere stays lit.',
       'the whole road darkens as the cyclist passes rather than showing separate shadows'),
      ('minor', 'The wheels turn as the bicycle travels, and their shadows turn with them.',
       'the shadow of the wheel stays still while the wheel plainly turns'),
      fixed('the lamps and their posts')),
    note="Their standards ask for shadow casting on the ground and for shadows matching the light "
         "positions, which is the right idea but is met by any shadow that moves. The items here "
         "make it specific to a row of sources: there is one shadow per lamp, each on the far side "
         "from its own lamp, and each swings round and changes length as the rider passes it. The "
         "brightness cycling between lamps is the other addition and is the easiest thing for a clip "
         "to get wrong by keeping the rider evenly lit.")

add('distant-occluder', 189,
    'A bird crossing in front of the sun is a dark shape against it, and the daylight on the ground '
    'does not change.',
    S(('core', 'A bird is present.'),
      ('core', 'The sun is present in the shot.'),
      ('core', 'The bird passes across the sun.'),
      ('minor', 'The bird is small against the sky rather than filling the frame.')),
    P(('fatal', 'The bird passes in front of the sun rather than through it.',
       'the bird passes behind the sun and stays visible through it, or the sun shows through the '
       "bird's body"),
      ('core', 'The bird is a dark shape against the bright sun rather than a lit one.',
       'the bird is brighter than the sky around it as it crosses the sun'),
      ('core', 'The daylight on the ground and on everything else stays as it was while the bird '
               'crosses.',
       'the whole scene dims noticeably as the bird passes the sun, as though the sun had been '
       'covered'),
      ('major', 'The bird keeps flying across and off the sun rather than stopping on it.',
       'the bird holds its position over the sun for the rest of the shot'),
      ('major', 'The bird keeps its outline -- wings and body -- as it crosses.',
       'the bird becomes a shapeless dark patch, or its wings stop moving while it glides across'),
      ('minor', 'Any shadow of the bird on the ground is faint and soft rather than a crisp dark '
                'outline.',
       'a hard-edged bird-shaped shadow tracks across the ground below',
       'a shadow of the bird is visible on the ground'),
      ('minor', 'The sun stays where it is and stays as bright.',
       'the sun moves across the sky or changes brightness during the few seconds of the shot')),
    note="Their sole standard is that 'the intensity of the sunlight dims noticeably as the bird "
         "passes in front of the sun', and it is wrong in the direction that rewards an absurd clip. "
         "A bird subtends a tiny fraction of the sky and is far from the ground, so it removes an "
         "insignificant part of the illumination and its ground shadow is almost entirely penumbra "
         "-- which is why a bird flying overhead casts no visible shadow at all. Following their "
         "standard would score a scene that darkens like an eclipse as correct. This rubric requires "
         "the daylight NOT to change, and puts any ground shadow behind a precondition with softness "
         "required.")

# ---- Chromatic Aberration and Dispersion (190-196) -----------------------
add('thin-film-bubble', 190,
    'Interference in the soap film shows as coloured bands on the bubble that shift as the film '
    'moves.',
    S(('core', 'A soap bubble is present.'),
      ('core', 'Colours are visible on its surface.'),
      ('minor', 'The bubble reads as a thin soap film rather than a coloured glass ball.'),
      ('minor', 'Sunlight or a bright light is falling on it.')),
    P(('fatal', 'The colour is on the bubble film itself rather than being cast elsewhere or coming '
                'from the bubble as its own light.',
       'the bubble glows in its own right, or the colour appears in the air beside it'),
      ('core', 'The colours lie in bands or swirls across the film rather than the bubble being one '
               'flat tint.',
       'the whole bubble is a single uniform colour'),
      ('core', 'The pattern shifts as the film flows and thins, and as the bubble turns.',
       'the coloured pattern is frozen on the surface and unchanged while the bubble plainly moves '
       'and its film drains'),
      ('major', 'The bubble stays see-through: what is behind it shows through the coloured film.',
       'the bubble is opaque, hiding whatever is behind it'),
      ('major', 'The colours change with the angle it is viewed or lit from.',
       'a given patch of film keeps exactly one colour as the bubble rolls round'),
      ('minor', 'The film drains and the pattern coarsens toward the top of the bubble over the '
                'shot.',
       'the film pattern is identical at the end of the shot as at the start, with no drainage at '
       'all'),
      ('minor', 'The bubble keeps a round shape and a bright specular highlight where the source '
                'reflects.',
       'there is no highlight anywhere on a bubble in direct sunlight')),
    note="Their standards ask for 'a clear and smooth gradation of colors' and for colours that "
         "shift with movement and angle. The second is exactly right and is core here. The first is "
         "not quite: thin-film interference produces BANDS -- fringes set by the film thickness -- so "
         "a smooth continuous gradient is less characteristic than the banded, swirling pattern a "
         "real bubble shows. The item here requires bands or swirls rather than a flat tint, which "
         "catches the commonest wrong answer without demanding the wrong structure. Scenario 195 is "
         "the same interference mechanism in an oil film.")

add('prism-dispersion', 191,
    'A prism bends the beam and spreads it into a spectrum, with the colours in order.',
    S(('core', 'A prism is present.'),
      ('core', 'A beam of light passes through it.'),
      ('core', 'A spectrum of colours comes out.'),
      ('minor', 'The incoming beam reads as white rather than already coloured.')),
    P(('fatal', 'The spectrum comes out of the prism, along the path the beam takes through it.',
       'the colours appear on the entry side of the prism, or in the air away from the beam path'),
      ('core', 'The colours come out in spectral order, running from red at one edge to blue and '
               'violet at the other.',
       'the colours come out in a jumbled order, or as a repeating pattern of bands'),
      ('core', 'The outgoing spectrum is bent away from the direction the beam came in on.',
       'the spectrum carries straight on in line with the incoming beam'),
      ('major', 'The spectrum fans out: it spreads wider the further from the prism it travels.',
       'the coloured band keeps exactly one width all the way from the prism to where it lands'),
      ('major', 'The beam stays a single beam up to the prism and only splits inside or on leaving '
                'it.',
       'the incoming beam is already spread into colours before it reaches the glass'),
      ('minor', 'The prism itself stays clear rather than becoming a glowing coloured object.',
       'the prism glows with colour of its own, brighter than the beam passing through it'),
      fixed('the prism')),
    note="Their sole standard, a visible spectrum with smooth transitions, is used. Everything else "
         "is written from scratch, and the item that matters most is the ORDER: dispersion is "
         "monotonic in wavelength, so red and violet are at opposite edges and the sequence between "
         "them is fixed. A clip showing a jumble of colours coming out of a prism satisfies their "
         "standard. Scenario 199, 'A beam of light passes through a glass prism', is the same "
         "scenario in the Reflection and Refraction subcategory and carries this mechanism.")

add('lens-colour-fringing', 192,
    'The bright lamp picks up faint coloured fringes at its edges, redder on one side and bluer on '
    'the other.',
    S(('core', 'A bright streetlamp is present.'),
      ('core', 'Coloured fringing is visible at its edges.'),
      ('minor', 'The lamp is the brightest thing in the shot.'),
      ('minor', 'The fringes are faint rather than dominating the image.')),
    P(('fatal', 'The fringing sits at the edges of the bright source rather than being a separate '
                'coloured object in the scene.',
       'coloured bands float in the air away from the lamp, or the whole frame is tinted rather '
       'than the lamp edges'),
      ('core', 'The fringes stay attached to the lamp edges and move with the lamp in frame.',
       'the fringes stay put in the frame while the lamp moves, or they drift off the lamp on their '
       'own'),
      ('core', 'The fringing is on opposite sides in opposite colours -- warmer on one edge, cooler '
               'on the other.',
       'the same colour rings the lamp evenly all the way round'),
      ('major', 'The fringes are narrow next to the bright core rather than wide coloured haloes.',
       'the lamp is surrounded by broad rainbow rings out to several times its own width'),
      ('major', 'The lamp core itself stays white or its own colour rather than being replaced by '
                'the fringe colours.',
       'the bright centre of the lamp turns red or blue along with its edges'),
      ('minor', 'The fringing is stronger for lamps further from the middle of the frame.',
       'a lamp dead centre in frame shows as much fringing as one at the corner',
       'more than one bright source is in shot at different positions'),
      fixed('the lamp and its post')),
    note="This scenario asks for a camera artefact rather than an event in the world, so the items "
         "are about where the fringing sits and how it behaves rather than about any physical "
         "process. Their second standard, that the extent of the fringes be 'proportional to the "
         "intensity of the light source', is not how chromatic aberration works: its magnitude is "
         "set by the lens and grows toward the edges of the frame, not by how bright the subject is. "
         "That field-position dependence is the minor item here, behind a precondition since it "
         "needs two sources at different positions. Their 'without exaggerated or artificial "
         "effects' is a rendering phrase; its usable core is that the fringes stay narrow.")

add('raindrop-dispersion', 193,
    'Sunlit raindrops throw colour, with the spectrum appearing as a bow at a fixed angle rather '
    'than inside each drop.',
    S(('core', 'Raindrops are present.'),
      ('core', 'Sunlight falls on them.'),
      ('core', 'Colour from the dispersed light is visible.'),
      ('minor', 'The scene reads as just after rain -- wet surfaces, a clearing sky.')),
    P(('fatal', 'The colour comes from the sunlight passing through the drops rather than the drops '
                'giving out light of their own.',
       'the raindrops glow with colour in their own right, brighter than the sunlight on them can '
       'account for'),
      ('core', 'The colours come in spectral order wherever they appear, red through to violet, '
               'rather than as arbitrary patches of hue.',
       'the colours appear in a jumbled order, or as a random confetti of tints'),
      ('core', 'The colour is faint and partial, as the caption says, rather than a saturated '
               'rainbow filling the scene.',
       'every visible drop carries a full bright spectrum'),
      ('major', 'Any bow lies opposite the sun -- with the sun behind the camera -- rather than '
                'around the sun.',
       'a rainbow arcs around the sun itself'),
      ('major', 'The colour holds its place relative to the sun and the viewpoint as individual '
                'drops fall through it.',
       'the coloured region falls with the drops, or it jumps about the frame from moment to moment',
       'a bow or a coloured region is visible for long enough to see whether it moves'),
      ('major', 'The drops stay clear and colourless in themselves; the colour is in where the light '
                'goes.',
       'each drop is dyed a different colour like a bead'),
      ('minor', 'Wet surfaces in the scene are darker and shinier than dry ones.',
       'the ground reads as bone dry immediately after the storm the caption names')),
    note="Their sole standard asks for 'multiple colors visible in the raindrops', which points at "
         "the wrong place. Dispersion by raindrops is a geometry effect: each drop sends a given "
         "wavelength back at its own angle, so the spectrum is assembled across many drops into a "
         "bow at a fixed angle from the antisolar point, and individual drops do not read as "
         "coloured beads. Taking their standard literally rewards a clip that dyes each drop a "
         "different colour, which is the misconception here. The bow's geometry -- opposite the sun, "
         "fixed relative to the viewer rather than falling with the drops -- is the addition.")

add('bottle-caustic', 194,
    'The water bottle bends the sunlight to a bright concentrated patch on the table, with at most '
    'faint colour at its edges.',
    S(('core', 'A bottle of water is present.'),
      ('core', 'Sunlight passes through it.'),
      ('core', 'A bright patch appears on the table.'),
      ('minor', 'The bottle reads as clear and water-filled rather than coloured or opaque.')),
    P(('fatal', 'The bright patch is on the far side of the bottle from the sun, along the line the '
                'light takes through it.',
       'the bright patch sits between the sun and the bottle, or somewhere unrelated to the light '
       'path'),
      ('core', 'The patch is brighter than the table around it, because the bottle concentrates the '
               'light.',
       'the patch is darker than the surrounding table, or it is no brighter than the rest of the '
       'surface'),
      ('core', 'The patch moves if the bottle or the light moves, and stays put if both are still.',
       'the bright patch wanders across the table while the bottle and the sunlight are plainly '
       'fixed'),
      ('major', 'The patch is a concentrated streak or spot rather than a broad even wash the size '
                'of the bottle.',
       'the light through the bottle simply lands as a bottle-shaped rectangle of ordinary '
       'brightness'),
      ('major', 'Any colour is confined to the fringes of the patch rather than the patch being a '
                'full separated spectrum.',
       'the bright spot is a clean rainbow with the colours laid out in distinct separated bands'),
      ('minor', 'The bottle also casts a shadow around the bright patch, away from the sun.',
       'the bottle concentrates light onto the table while casting no shadow at all'),
      fixed('the bottle and the table')),
    note="Their standards are the wrong way round for this scenario, and both would reward an "
         "invented effect. A water-filled bottle is a crude thick lens: it makes a bright caustic "
         "streak, and the dispersion of water over that short path with that wide an aperture gives "
         "at most faint colour at the fringes, not the 'distinct rainbow pattern' with colours "
         "'separating cleanly' that they ask for. Following them would fail a physically correct "
         "clip of a bright colourless caustic and pass a painted-on rainbow. The concentration is "
         "the core item here and the colour is capped at the fringes.")

add('oil-film-interference', 195,
    'Interference in the spreading oil film shows as swirling coloured bands that shift as it thins.',
    S(('core', 'Water is present with oil on it.'),
      ('core', 'The oil spreads out into a thin layer.'),
      ('core', 'Colours are visible in the film.'),
      ('minor', 'The oil reads as a thin sheen rather than a thick coloured liquid.')),
    P(('fatal', 'The colour is in the oil film on the surface rather than in the water below or in '
                'the air above.',
       'the colour appears in the body of the water, or it floats above the surface'),
      ('core', 'The colours lie in bands and swirls that follow the film rather than the whole slick '
               'being one flat tint.',
       'the oil layer is a single uniform colour all over'),
      ('core', 'The pattern shifts and the bands move as the film spreads and thins.',
       'the coloured pattern is frozen while the oil is plainly still spreading'),
      ('major', 'The colours appear where the film is thin and are absent where the oil is thick or '
                'has not reached.',
       'the thickest part of the slick is the most colourful, or colour appears on bare water'),
      ('major', 'The covered area only grows while oil keeps spreading.',
       'the film shrinks back while oil is plainly still spreading out'),
      ('minor', 'The colours change with the angle the film is viewed or lit from.',
       'a given patch of film keeps exactly one colour as the view or the light shifts'),
      fixed('the vessel or the water body')),
    note="Their sole standard, swirling patterns of colour in the film, is sound and is core here. "
         "The additions come from what interference actually depends on: the colour is set by the "
         "film thickness, so it appears where the film is THIN, it changes as the film spreads and "
         "drains, and it shifts with viewing angle. A clip showing a fixed colourful pattern on a "
         "thick static slick satisfies their standard. Scenario 190 is the same mechanism in a soap "
         "bubble.")

add('icicle-refraction', 196,
    'Sunlight through the hanging icicles is bent and concentrated, throwing bright patches with '
    'coloured fringes.',
    S(('core', 'Icicles hanging from a tree are present.'),
      ('core', 'Sunlight passes through them.'),
      ('minor', 'The icicles read as clear ice rather than as snow or frost.'),
      ('minor', 'The scene reads as cold -- snow, bare branches or frost.')),
    P(('fatal', 'The light comes from the sun through the ice rather than from the icicles '
                'themselves.',
       'the icicles glow in their own right, brighter than the sunlight falling on them'),
      ('core', 'The icicles pass light: bright patches and highlights appear through and beyond '
               'them rather than solid shadow.',
       'the icicles block the sunlight completely, casting shadow as though they were opaque'),
      ('core', 'The bright patches and highlights are fixed relative to the sun and the icicles, '
               'moving only when one of them moves.',
       'the highlights wander over the ice while the icicles hang still in steady sunlight'),
      ('major', 'Any colour appears as narrow fringes at the edges of the bright patches rather '
                'than as broad bands of separated spectrum.',
       'the icicles throw a full clean rainbow with the colours in separated bands'),
      ('major', 'The icicles hang downward and keep their tapered shape.',
       'the icicles point sideways or upward, or they change shape over the shot'),
      ('minor', 'Where an icicle is thick or frosted it passes less light than where it is thin and '
                'clear.',
       'a thick frosted icicle is as bright and as clear as a thin one'),
      fixed('the tree and the branches')),
    note="This record is broken. Its physics_prompt is a copy-paste artefact from scenario 198: it "
         "describes sunlight hitting a mirror in a room and being reflected into it at an equal "
         "angle, and mentions no ice at all. Its sole key standard follows the same wrong scenario, "
         "asking about colour fringing at the edges of 'the reflected light spot'. Neither is usable, "
         "so every item here is written from the caption alone. What sunlight through clear ice "
         "actually does is refract and concentrate -- bright patches and highlights, with colour "
         "confined to narrow fringes rather than a separated spectrum, on the pattern of scenario "
         "194.")

# ---- Reflection and Refraction (197-203) ---------------------------------
add('partial-reflection-refraction', 197,
    'The beam splits at the pond surface: part reflects away at the mirror angle and part carries '
    'on into the water, bent.',
    S(('core', 'A beam of light is present.'),
      ('core', 'It meets the surface of a pond.'),
      ('core', 'The pond surface is calm, as the caption says.'),
      ('minor', 'The beam arrives at a slant rather than straight down.')),
    P(('fatal', 'Both the reflected and the refracted beams start at the point where the incoming '
                'beam meets the water.',
       'a beam leaves the surface from a different place than the one the incoming beam strikes'),
      ('core', 'The reflected beam leaves on the far side of the upright from the incoming beam, at '
               'the same slant.',
       'the reflected beam goes back the way the incoming beam came, or it leaves at a plainly '
       'different slant'),
      ('core', 'The beam inside the water is bent toward the upright compared with the incoming '
               'beam, and carries on downward.',
       'the beam inside the water bends away from the upright, or it carries straight on unbent, or '
       'it turns back upward'),
      ('major', 'Both beams are present at once, with the reflected one weaker than the incoming '
                'beam.',
       'the beam either reflects or enters the water but not both, or the reflected beam is brighter '
       'than the beam that arrived'),
      ('major', 'All three beams stay in the same plane.',
       'the reflected or refracted beam swings off sideways out of the plane of the incoming beam'),
      ('minor', 'The bend happens at the surface only, not gradually through the water.',
       'the beam curves continuously as it goes down through the water'),
      fixed('the pond')),
    note="Their standards -- reflection symmetric about the incident angle, refraction bending at "
         "the surface -- are both correct physics, and their second is unusually specific for this "
         "benchmark. Both are used. The additions are the direction of the bend, which their 'at a "
         "angle' leaves open and which is the thing a clip gets wrong half the time, and the "
         "simultaneity: a calm water surface both reflects and transmits, so a clip that shows only "
         "one of the two is incomplete.")

add('mirror-redirect', 198,
    'The mirror throws the sunlight back into the room at the matching angle, making a bright patch '
    'on the far surface.',
    S(('core', 'A mirror is present.'),
      ('core', 'Sunlight falls on it.'),
      ('core', 'Reflected light lands somewhere in the room.'),
      ('minor', 'The room is otherwise dimmer than the reflected patch.')),
    P(('fatal', 'The reflected light leaves the mirror from where the sunlight lands on it.',
       'the bright patch appears with no light path from the mirror to it, or the mirror throws light '
       'while the sunlight is plainly not on it'),
      ('core', 'The reflected beam leaves the mirror on the far side of the upright from the '
               'incoming sunlight, at the same slant.',
       'the reflected beam goes back along the incoming sunlight, or it leaves at a plainly '
       'different slant'),
      ('core', 'The bright patch moves when the mirror is turned and stays put when everything is '
               'still.',
       'the patch wanders about the room while the mirror and the sunlight are both plainly fixed'),
      ('major', 'The patch is brighter than the surfaces around it.',
       'the patch is no brighter than the rest of the wall, or it is darker'),
      ('major', 'The reflected light does not appear on surfaces the beam cannot reach.',
       'bright patches appear behind obstructions or on surfaces facing away from the mirror'),
      ('minor', 'The mirror shows a reflection of the room as well as throwing the beam.',
       'the mirror surface reads as a blank white panel with nothing reflected in it'),
      fixed('the mirror and the room')),
    note="Their standards -- equal angles about the mirror surface, a noticeable brightness contrast "
         "between the lit patch and the shadow -- are both sound and both used. The additions are "
         "the coupling between mirror and patch (turn the mirror and the patch moves; hold both "
         "still and it stays) and the requirement that the mirror still act as a mirror rather than "
         "a white panel, which is the commonest way these clips cheat.")

add('prism-dispersion', 199,
    'A glass prism bends the beam and splits it into its component colours, in order.',
    S(('core', 'A glass prism is present.'),
      ('core', 'A beam of light passes through it.'),
      ('core', 'The beam comes out split into colours.'),
      ('minor', 'The incoming beam reads as white rather than already coloured.')),
    P(('fatal', 'The colours come out of the prism along the beam path rather than appearing '
                'elsewhere.',
       'the colours appear on the entry side of the glass, or in the air away from the beam'),
      ('core', 'The colours are in spectral order, red at one edge through to violet at the other.',
       'the colours emerge jumbled, or in repeating bands'),
      ('core', 'The whole emerging fan is bent away from the incoming direction, and violet is bent '
               'furthest.',
       'the spectrum carries straight on in line with the incoming beam, or red is bent further than '
       'violet'),
      ('major', 'The colours spread further apart the further from the prism they travel.',
       'the coloured band keeps one fixed width from the prism to where it lands'),
      ('major', 'The prism stays clear glass, passing the beam rather than glowing.',
       'the prism itself lights up with colour brighter than the beam through it'),
      ('minor', 'A faint reflection also comes off the prism faces.',
       'the glass surfaces show no reflection at all in a bright beam',
       'the shot shows the prism faces clearly enough to see a reflection'),
      ('minor', 'The spectrum lands somewhere and stays there while the prism and the beam are '
                'still.',
       'the spectrum drifts across the surface with both the prism and the beam plainly fixed')),
    note="Their standards -- a clearly visible spectrum, and the colours bending relative to the "
         "original beam -- are both used. The addition beyond scenario 191, which is the same "
         "scenario in the Chromatic Aberration subcategory and carries this mechanism, is the "
         "ordering of the bend: dispersion in glass is stronger at shorter wavelengths, so violet is "
         "deviated further than red. A clip that reverses that has the spectrum backwards while "
         "still satisfying both of their standards.")

add('refraction-offset', 200,
    'The spoon looks broken at the water line, with the submerged part shifted from where it should '
    'carry on.',
    S(('core', 'A glass of water is present.'),
      ('core', 'A spoon is in it, going through the water surface.'),
      ('core', 'The spoon looks bent or offset at the surface, as the caption says.'),
      ('minor', 'The glass reads as clear and the water as clear.')),
    P(('fatal', 'The spoon is one continuous object; only how it looks changes at the surface.',
       'the spoon is genuinely in two separate pieces, or the submerged part is missing altogether'),
      ('core', 'The apparent break is at the water line and nowhere else.',
       'the spoon appears to bend in the middle of the water, or above the surface in the air'),
      ('core', 'The submerged part appears offset or bent relative to the part in the air.',
       'the spoon appears perfectly straight and continuous through the surface'),
      ('major', 'The apparent break stays at the water line as the spoon is moved.',
       'the bend travels up and down the spoon as it is moved, away from the surface'),
      ('major', 'The submerged part looks nearer and larger than it would out of water, not smaller '
                'and further.',
       'the submerged part appears shrunken and pushed away'),
      ('minor', 'The offset grows as the spoon is tilted further from upright and vanishes when it '
                'is straight up and down.',
       'a spoon standing vertically in the water still appears broken at the surface',
       'the spoon is tilted or moved during the shot'),
      ('minor', 'The water surface itself stays level and the water stays clear.',
       'the water surface slants in the upright glass, or it clouds over'),
      fixed('the glass')),
    note="Their sole standard, that the spoon appears to split or bend at the water's surface, is "
         "the right core requirement and is used. Everything else is written from scratch. The two "
         "items that matter beyond it are the direction of the effect -- refraction at the surface "
         "makes the submerged part look nearer and larger, not further and smaller -- and that the "
         "break stays locked to the surface rather than travelling with the spoon.")

add('convex-mirror-image', 201,
    'The curved side mirror shows the following car smaller than life, growing as it closes up.',
    S(('core', 'A side mirror is present.'),
      ('core', 'A following car is visible in it.'),
      ('minor', 'The mirror reads as a vehicle side mirror rather than a flat hand mirror.'),
      ('minor', 'The scene reads as being on a road with traffic behind.')),
    P(('fatal', 'What appears in the mirror is behind the car, in the direction the mirror faces.',
       'the mirror shows the road ahead, or it shows something that is plainly in front of the car'),
      ('core', "The following car's image is smaller in the mirror than the same car would look "
               'seen directly at that distance.',
       'the image in the mirror is larger than life, or it matches direct view exactly on a plainly '
       'curved mirror'),
      ('core', 'The image grows as the following car closes up and shrinks as it drops back.',
       'the image keeps exactly one size while the following car plainly changes its distance'),
      ('major', 'The image moves across the mirror in the direction that follows from the cars\' '
                'relative motion, and holds still when they hold station.',
       'the image slides about the mirror while both cars keep the same relative position'),
      ('major', 'The image stays the right way up and the right way round for a mirror.',
       'the reflected car appears upside down in the mirror'),
      ('minor', 'The mirror shows more of the scene than a flat mirror of the same size would, with '
                'the view compressed toward its edges.',
       'the mirror shows a narrow undistorted crop as though it were flat'),
      fixed('the mirror housing')),
    note="Their sole standard asks that the reflection be 'without introducing visual artifacts or "
         "unrealistic distortions', which names no observable and, read literally, asks for the "
         "absence of the very thing a convex mirror does. It is not used. Their physics_prompt has "
         "the real content -- the curved surface reduces the image size -- and that is the core item "
         "here, together with the way the image grows as the follower closes and the wider "
         "compressed field of view that comes with the curvature.")

add('still-water-mirror', 202,
    'The still lake shows the mountains upside down below the shoreline, matching them feature for '
    'feature.',
    S(('core', 'Mountains are present.'),
      ('core', 'A lake is present.'),
      ('core', 'The mountains are reflected in the lake.'),
      ('minor', 'The water reads as still, as the caption says.')),
    P(('fatal', 'The reflection is in the water below the shoreline, not above it or beside it.',
       'the reflected mountains appear in the sky, or off to one side of the real ones'),
      ('core', 'The reflection is upside down, mirrored about the waterline.',
       'the reflection is the right way up, or mirrored left to right instead of top to bottom'),
      ('core', 'Each reflected feature lines up directly below the real one.',
       'peaks and their reflections are offset sideways from each other'),
      ('major', 'The reflection is a little dimmer and less contrasted than the mountains '
                'themselves.',
       'the reflection is brighter or more saturated than the real mountains'),
      ('major', 'The lighting agrees: a slope lit on one side has its reflection lit on the same '
                'side.',
       'the reflected slopes are lit from the opposite side to the real ones'),
      ('minor', 'Any ripple that does appear breaks the reflection up where it passes rather than '
                'leaving it untouched.',
       'the reflection stays perfectly crisp across a patch of visibly disturbed water',
       'the water is disturbed somewhere in the shot'),
      ('minor', 'The reflection changes if the mountains or the light change, and holds still '
                'otherwise.',
       'the reflection shifts about while the mountains and the light are plainly unchanged'),
      fixed('the mountains and the shoreline')),
    note="Their standards -- the reflection matches shape, colour and detail, and the lighting and "
         "shadows are consistent between the two -- are both sound and both used. The additions are "
         "the geometry their wording leaves open: the reflection is inverted about the waterline and "
         "each feature sits directly below its original, which is what catches a clip that pastes a "
         "correct-looking but upright or sideways-shifted copy into the water.")

add('lens-magnification', 203,
    'The magnifier bends the light so what is under it looks enlarged, with the view distorted '
    'toward the rim.',
    S(('core', 'A magnifying glass is present.'),
      ('core', 'Light passes through it and something is seen through it.'),
      ('minor', 'The lens reads as a converging magnifier rather than a flat pane.'),
      ('minor', 'Something is close behind the lens to be looked at.')),
    P(('fatal', 'What is seen through the lens is what is actually behind it.',
       'the lens shows something that is not there, or the view through it is unrelated to what lies '
       'behind it'),
      ('core', 'The view through the lens differs from the view beside it: it is not simply a clear '
               'window.',
       'what is seen through the lens is exactly the same size and shape as the surroundings, as '
       'though the glass were flat'),
      ('core', 'What is seen through the lens is enlarged while the lens is held close to it, and '
               'the two agree at the rim about what is being looked at.',
       'the object appears smaller through a lens held close to it, or the region seen through the '
       'lens shows a different object from the one behind it'),
      ('major', 'The view is distorted and curved toward the rim rather than being uniformly sharp '
                'to the edge.',
       'the whole circle is a perfectly undistorted enlargement right out to the rim'),
      ('major', 'The magnification changes as the lens is moved toward or away from the object.',
       'the enlargement stays at exactly one factor however far the lens is held from what is under '
       'it',
       'the lens is moved toward or away from the object during the shot'),
      ('major', 'If the lens is held well beyond arm\'s length from the object, the image it gives '
                'is small and turned upside down rather than enlarged.',
       'a lens held far from the object still gives a large upright enlargement',
       'the lens is held far from the object at some point in the shot'),
      ('minor', 'The lens may concentrate light into a bright patch, and any such patch is on the '
                'far side from the source.',
       'a bright concentrated patch appears on the source side of the lens',
       'a concentrated bright patch is visible'),
      ('minor', 'The lens itself stays clear glass rather than glowing or colouring the view.',
       'the lens glows in its own right, or it tints everything seen through it')),
    note="Their standards -- edge distortion, a noticeably larger image -- are both used, but the "
         "second needs qualifying and this is the same trap as PhyGenBench ids 65 to 69. A "
         "converging lens only magnifies while it is held inside its focal length; held further off "
         "it gives a small INVERTED image, which is correct physics that a rubric demanding "
         "enlargement would mark wrong. The enlargement item here is therefore conditioned on the "
         "lens being held close, and the far-field behaviour is a separate item behind its own "
         "precondition.")

# ---- Shadow Softness and Penumbra (204-210) ------------------------------
add('low-angle-soft-shadow', 204,
    'Low dusk light through the window throws a long soft-edged shadow of the plant.',
    S(('core', 'A hanging plant is present.'),
      ('core', 'A window is present and light comes through it.'),
      ('core', 'The plant casts a shadow.'),
      ('minor', 'The light reads as low and warm, as at dusk.')),
    P(shadow_away('the plant', 'the window'),
      ('core', 'The shadow edges are soft, fading from dark to light over a visible width rather '
               'than switching at a line.',
       'the shadow has a hard crisp outline with no gradient at its edge at all'),
      ('core', 'The shadow is long and stretched, as a low light source makes it.',
       'the shadow is short and compact directly beneath the plant, as it would be under an overhead '
       'light'),
      ('major', 'The shadow edge is softer the further from the plant it is, and tighter close to '
                'it.',
       'the shadow edge is equally soft along its whole length, or it is softest right at the plant'),
      ('major', 'The shadow keeps the plant\'s outline -- separate leaves and trailing stems -- '
                'loosely rather than being a solid slab.',
       'the shadow is a single hard-edged rectangle with no leaf structure'),
      ('minor', 'The shadow moves if the plant swings and holds still if it does not.',
       'the shadow drifts while the plant hangs still'),
      fixed('the window and the room')),
    note="Their standards -- soft blurred edges, a noticeable gradient from the darkest part to the "
         "lighter part -- are both correct physics of an extended source and are both used. The "
         "additions are the two consequences they leave out: a low source makes a LONG shadow, and "
         "the penumbra widens with distance from the object so the far end of a long shadow is "
         "softer than the near end. Scenario 210 is the deliberate contrast case, where an overhead "
         "sun gives hard edges.")

add('penumbra-with-distance', 205,
    'The lamp throws a shadow of the vase that is crisp where it starts and softer the further out '
    'it goes.',
    S(('core', 'A table lamp is present and lit.'),
      ('core', 'A vase is present.'),
      ('core', 'The vase casts a shadow.'),
      ('minor', 'The lamp reads as the light that matters in the scene.')),
    P(shadow_away('the vase', 'the lamp'),
      ('core', 'The shadow is tighter and darker close to the vase and its edges get softer the '
               'further from the vase it goes.',
       'the shadow edge is equally sharp along its whole length, or it is sharpest at the far end '
       'and blurred at the base'),
      ('core', 'The shadow is joined to the vase where the vase meets the surface.',
       'the shadow is detached, with a lit gap between the vase and the start of its shadow'),
      ('major', 'The shadow keeps the outline of the vase -- its profile and its neck -- rather '
                'than being a plain blob.',
       'the shadow has no relation to the shape of the vase'),
      ('major', 'The surface inside the shadow is darker than the surface outside it, and the vase '
                'itself is lit on the lamp side.',
       'the shadowed surface is as bright as the lit surface, or the vase is brightest on the side '
       'away from the lamp'),
      ('minor', 'The shadow moves if the lamp or the vase moves, and holds still otherwise.',
       'the shadow shifts while both the lamp and the vase are plainly fixed'),
      fixed('the lamp and the table')),
    note="Their three standards are the best-written set in this category: a sharp edge near the "
         "vase, blurring as the shadow extends, and a gradual transition between the two. That is "
         "exactly how the penumbra of an extended source grows with distance, and all three are "
         "used, with the third taken in its physical reading rather than as a rendering "
         "requirement. The additions are only the standard geometry items -- which side the shadow "
         "falls on, and that it stays attached at the base.")

add('small-source-shadow', 206,
    'The candle throws a fairly crisp shadow of the hand, softening only where the hand is further '
    'from the surface.',
    S(('core', 'A lit candle is present.'),
      ('core', 'A hand is present in its light.'),
      ('core', 'The hand casts a shadow.'),
      ('minor', 'The candle reads as the light that matters in the scene.')),
    P(shadow_away('the hand', 'the candle flame'),
      ('core', 'The shadow keeps the shape of the hand, with the fingers separately visible.',
       'the shadow is a featureless patch with no fingers in it'),
      ('core', 'The shadow has a definite edge -- a candle flame is small, so the edge reads as an '
               'edge rather than dissolving into a smooth gradient.',
       'the shadow has no discernible boundary at all, fading away so gradually that its extent '
       'cannot be made out'),
      ('major', 'The shadow is sharper where the hand is close to the surface and softer where it '
                'is further from it.',
       'the shadow keeps exactly one sharpness however far the hand is held from what it falls on'),
      ('major', 'The shadow is large and the hand is strongly lit, because the flame is close.',
       'the hand is only faintly lit by a candle right beside it, or its shadow is smaller than the '
       'hand itself'),
      ('minor', 'The shadow flickers in step with the flame.',
       'the shadow holds perfectly steady while the flame plainly gutters'),
      fixed('the candle')),
    note="Their sole standard asks for 'a soft, gradient edge with no sharp lines', and their "
         "physics_prompt calls the shadow 'soft, blurry'. That is the wrong way round for this "
         "source. Penumbra width goes with the angular size of the source, and a candle flame is "
         "small -- far smaller than a lampshade or an overcast sky -- so a candle actually gives one "
         "of the crisper shadows in this block, softening only as the hand is moved away from the "
         "surface. Requiring no sharp lines at all would fail a correct clip. This rubric requires a "
         "discernible edge and puts the softening where it belongs, on distance. Scenarios 208 and "
         "209 are the genuinely soft cases, where the source really is large.")

add('elongated-soft-shadow', 207,
    'Low sunlight stretches the tree shadow out long, with its far end softer than its base.',
    S(('core', 'A tree is present.'),
      ('core', 'Low-angle sunlight falls on it.'),
      ('core', 'The tree casts a shadow.'),
      ('minor', 'The light reads as low -- long shadows elsewhere, a warm colour, or a low sun in '
                'shot.')),
    P(shadow_away('the tree', 'the sun'),
      ('core', 'The shadow is long and stretched away from the sun rather than compact under the '
               'tree.',
       'the shadow lies short and tight beneath the tree under a plainly low sun'),
      ('core', 'The shadow edges soften with distance from the tree, so the far end of the shadow is '
               'less defined than the base of the trunk.',
       'the whole shadow has one uniform edge sharpness from trunk to tip'),
      ('major', 'The shadow keeps the tree\'s structure -- trunk, branches, a broken canopy -- '
                'rather than being a solid slab.',
       'the shadow is one filled shape with no branch or foliage structure'),
      ('major', 'The trunk shadow is joined to the trunk where it meets the ground.',
       'the shadow starts away from the trunk with lit ground in between'),
      ('minor', 'Gaps in the canopy let light through as bright patches within the shadow.',
       'the canopy shadow is uniformly dark with no light coming through it anywhere'),
      ('minor', 'The shadow moves only if the tree moves or the light moves.',
       'the shadow swings about while the tree stands still in steady sunlight'),
      fixed('the tree and the ground')),
    note="Their sole standard, visibly soft edges with a gradual transition, is used. The additions "
         "are the elongation their physics_prompt mentions but their standard does not, and the way "
         "the softness varies: the sun has a small angular size, so the shadow is reasonably crisp "
         "at the trunk and softens toward the tip, and a uniformly blurred shadow is as wrong as a "
         "uniformly sharp one. The bright patches through canopy gaps are the other addition and are "
         "an easy thing for a clip to omit.")

add('diffused-source-shadow', 208,
    'The cloud spreads the sunlight out, so the shadows below lose their edges and go soft all over.',
    S(('core', 'Sunlight and a cloud are present.'),
      ('core', 'The cloud comes between the sun and the scene, at least partly.'),
      ('core', 'The light or the shadows below change as it does.'),
      ('minor', 'The cloud is thin enough to pass light rather than being a solid dark mass.')),
    P(('fatal', 'The light reaching the ground comes through or past the cloud rather than the cloud '
                'giving out light of its own.',
       'the cloud glows in its own right, brighter than the sunlight behind it can account for'),
      ('core', 'Shadows on the ground get softer and weaker while the cloud is over the sun, and '
               'sharpen again if it clears.',
       'the shadows keep exactly the same hard edges while the cloud plainly covers the sun'),
      ('core', 'The whole scene dims a little rather than parts of it going fully dark.',
       'the ground under the cloud goes to complete darkness while the rest stays in full sun'),
      ('major', 'The shadow softening and the cloud crossing happen together.',
       'the shadows go soft well before the cloud reaches the sun, or long after it has passed'),
      ('major', 'The lit and shadowed regions stay consistent with one sun direction throughout.',
       'the shadow directions change as the cloud passes, as though the sun had moved'),
      ('minor', 'The cloud itself is brighter on the side facing the sun.',
       'the cloud is brightest on the side turned away from the sun'),
      fixed('the ground and whatever casts the shadows')),
    note="Their sole standard, a blurred shadow edge with a gradual transition from light to dark, "
         "is sound and is used. The addition is the coupling in time: this scenario is about the "
         "cloud CAUSING the softening, so the two must happen together, and a clip with permanently "
         "soft shadows and a cloud drifting past irrelevantly satisfies their standard. The other "
         "addition is that diffusion dims and softens rather than blacking out, since a thin cloud "
         "spreads the light rather than removing it.")

add('curtain-diffusion', 209,
    'The curtain scatters the sunlight coming through it, so what lands below is soft and '
    'edgeless.',
    S(('core', 'A translucent curtain is present.'),
      ('core', 'Sunlight passes through it.'),
      ('core', 'Light and shadow fall on the surface below or beyond it.'),
      ('minor', 'The curtain reads as thin and light-passing rather than heavy and opaque.')),
    P(('fatal', 'The light beyond the curtain comes through it from the sunlit side.',
       'the curtain glows in its own right, or light appears beyond it with the sun plainly on the '
       'far side of an opaque wall'),
      ('core', 'The pattern on the surface below has soft edges rather than the crisp outline the '
               'window frame would cast without the curtain.',
       'the curtain passes a hard-edged image of the window and its frame as though it were clear '
       'glass'),
      ('core', 'The curtain is brighter than what is behind it and dims the light that gets past.',
       'the surface beyond the curtain is as brightly lit as it would be with the curtain drawn '
       'aside'),
      ('major', 'Overlapping folds of curtain pass less light than single thicknesses, so the '
                'pattern below follows the folds.',
       'the light below is perfectly even although the curtain plainly hangs in folds'),
      ('major', 'The soft pattern moves with the curtain if it stirs and holds still otherwise.',
       'the pattern below shifts about while the curtain hangs perfectly still'),
      ('minor', 'What is behind the curtain shows through only as a vague shape rather than sharply.',
       'objects behind the curtain are seen through it in sharp detail'),
      fixed('the window and the surface below')),
    note="Their sole standard, soft and gradual shadows with no abrupt transitions, is sound and is "
         "used. The additions are what makes it the curtain doing the work: a translucent sheet is a "
         "large diffuse source, so it replaces the hard window-frame outline with a soft wash, it "
         "dims what gets through, and its folds show up as thickness variation in the pattern below. "
         "Scenario 208 is the same diffusion mechanism with a cloud as the diffuser.")

add('overhead-hard-shadow', 210,
    'Overhead sun through the fence lays down hard-edged shadow bars close under it.',
    S(('core', 'A fence is present.'),
      ('core', 'Sunlight passes through or past it.'),
      ('core', 'The fence casts shadows on the ground.'),
      ('minor', 'The light reads as high and overhead, as at noon.')),
    P(('fatal', 'Shadow falls where the fence blocks the light and light falls through the gaps.',
       'the shadow bars line up with the gaps rather than with the pickets, or the fence casts a '
       'solid unbroken shadow with no gaps at all'),
      ('core', 'The shadow edges are crisp: the change from lit to shadowed happens over a narrow '
               'width rather than fading out.',
       'the shadow bars have wide soft gradients at their edges with no definite boundary'),
      ('core', 'The shadows are short and lie close under the fence, as an overhead sun makes them.',
       'the shadows stretch far out across the ground, as they would under a low sun'),
      ('major', 'The shadow bars keep the spacing and width of the pickets that cast them.',
       'the bars bunch together, spread apart, or differ in number from the pickets'),
      ('major', 'The bars run away from the sun and all lie parallel in the same direction.',
       'the bars fan out in different directions, or they point back toward the sun'),
      ('minor', 'The shadows move only if the fence or the light moves.',
       'the bars slide across the ground while the fence stands still in steady sunlight'),
      fixed('the fence and the ground')),
    note="Their standards -- minimal gradation, very narrow transition regions at the shadow edges "
         "-- are correct for this source and are both used, and this entry is the deliberate "
         "contrast to the six soft-shadow scenarios before it: the sun is a small source, so direct "
         "unfiltered sunlight gives the hardest shadows in the block. The additions are the "
         "shortness that comes with an overhead sun and the correspondence between bar spacing and "
         "picket spacing, which is where a clip most easily drifts.")
