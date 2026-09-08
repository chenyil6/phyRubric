# ============ Gravity: microgravity pours (0-4) ==========================
for i, vessel, liq, extra in [
    (0, 'cup', 'water', None),
    (1, 'cup', 'oil', None),
    (2, 'bottle', 'juice', None),
    (3, 'squeeze bottle or packet', 'honey',
     ('minor', 'Honey, far more viscous, is slow to round up: it trails strands and lumpy '
               'shapes that only gradually pull into blobs.',
      'the honey behaves like a thin liquid, snapping into clean spheres instantly with no '
      'strands or lumps')),
    (4, 'can', 'soda',
     ('minor', 'Gas bubbles stay dispersed through the liquid instead of collecting on one '
               'side of a blob, since there is no buoyancy to sort them.',
      'bubbles rise to one side of a drifting blob and gather there, as they would under '
      'gravity')),
]:
    pc = [
        ('fatal', 'No direction in the scene acts as down: the released liquid does not '
                  'accelerate toward the floor, and nothing pools at the bottom of the frame.',
         f'the {liq} falls and pools at the bottom of the frame as it would on Earth'),
        ('core', f'A freed mass of {liq} rounds up into a blob or sphere instead of falling as '
                 f'a column or breaking into a splashing stream.',
         f'the released {liq} keeps the shape of a falling stream or splashes on a surface'),
        ('core', 'A drifting blob travels in a straight line at roughly constant speed until it '
                 'meets something; its path does not arc downward and it does not slow to a '
                 'halt in open air.',
         'a drifting blob curves downward or coasts to a stop in mid-air with nothing acting '
         'on it'),
        ('major', 'Two blobs that touch merge into one larger blob and stay merged.',
         'blobs pass through each other, or touch and bounce apart without merging'),
        ('major', 'A blob that touches a surface sticks and spreads over it rather than running '
                  'off it or collecting beneath it.',
         'liquid that meets a wall runs down it or gathers underneath it'),
        ('minor', f'{liq.capitalize()} still inside the {vessel} shows no flat horizontal '
                  f'surface; it wets and clings to the container wall instead of lying level.',
         f'the {liq} left in the {vessel} sits with a flat level surface'),
        ('minor', 'Hair, clothing and any loose object in shot also hang free rather than '
                  'falling or settling.',
         'hair, clothing or loose objects hang and fall as they would on the ground'),
    ]
    if extra:
        pc.append(extra)
    add('microgravity', i,
        f'A {vessel} of {liq} is emptied into the open air of a space station.',
        S(('core', 'The setting reads as the interior of a space station or orbiting '
                   'spacecraft, not an ordinary room.'),
          ('core', f'A {vessel} of {liq} is present and its contents are released into the '
                   f'open surroundings rather than into another container.'),
          ('core', 'The release is slow and deliberate, as a pour rather than a throw or a '
                   'sudden shake.'),
          ('minor', f'The {liq} ends up loose and spread through the surrounding space rather '
                    f'than staying with the {vessel}.')),
        P(*pc))

# ============ Buoyancy: dense objects sink (5, 6, 9) =====================
for i, obj, vessel in [(5, 'piece of iron', 'tank'), (6, 'stone', 'pool'),
                       (9, 'glass ball', 'bathtub')]:
    add('buoyancy', i,
        f'A {obj} is set on the water in a {vessel} and sinks.',
        S(('core', f'A {obj} is present and recognisable.'),
          ('core', f'It is placed onto the water surface of a {vessel} of water.'),
          ('core', 'The placing is gentle -- lowered or set down, not thrown, dropped hard or '
                   'flung in.'),
          ('minor', f'The {vessel} reads as the container the caption names and is filled with '
                    f'water.')),
        P(('fatal', f'The {obj} goes under the surface and does not float.',
           f'the {obj} stays floating on the water surface'),
          ('core', 'It goes under as soon as it is released, without resting on the surface or '
                   'hesitating there first.',
           'it sits on the surface for a while before sinking, or is held up by the surface'),
          ('core', 'It settles on the bottom and stays there; it does not rise again on its own.',
           'it rises back toward the surface, or hovers at mid-depth, with nothing lifting it'),
          ('major', 'It descends at a moderate, roughly steady rate -- slower than the same '
                    'object would fall through air.',
           'it drops through the water as fast as it would fall through air, or drifts down '
           'unnaturally slowly'),
          ('major', 'The surface dips and ripples where it enters, and the ripples spread '
                    'outward and die away.',
           'the water surface is unmoved by the entry, or ripples travel inward toward the '
           'entry point'),
          ('minor', 'The water level rises slightly when the object is added and does not fall '
                    'while it stays in.',
           'the water level drops when the object goes in'),
          ('minor', 'The submerged object reads as being under water -- tinted, softened or '
                    'displaced by refraction rather than as crisp as it was in air.',
           'the submerged object looks exactly as it did in air, with no sign of the water '
           'between it and the camera')))

# ============ Buoyancy: light objects float (7, 8) ======================
for i, obj, vessel, extra in [
    (7, 'tennis ball', 'bucket',
     ('minor', 'The felt wets and darkens where it sits in the water.',
      'the part of the ball below the waterline stays dry-looking after a long soak')),
    (8, 'piece of wood block', 'bowl', None),
]:
    pc = [
        ('fatal', f'The {obj} stays at the surface and never sinks below it.',
         f'the {obj} sinks and goes to the bottom'),
        ('core', 'It settles to a definite waterline, with part of its body above the surface '
                 'and part below.',
         'it perches entirely on top of the surface with nothing submerged, or floats with '
         'nothing showing above the water'),
        ('core', 'It does not drift under on its own, nor lift clear of the water on its own.',
         'it slowly submerges or rises out of the water with nothing acting on it'),
        ('major', 'It bobs a few times, each swing smaller than the last, then comes to rest.',
         'the bobbing grows instead of dying away, or it stops dead the instant it lands'),
        ('major', 'The surface dips and ripples where it lands, and the ripples spread outward '
                  'and die away.',
         'the water surface is unmoved by the landing, or ripples run inward toward it'),
        ('minor', 'The water level rises slightly when it is added and does not fall while it '
                  'stays in.',
         'the water level drops when the object goes in'),
    ]
    if extra:
        pc.append(extra)
    add('buoyancy', i,
        f'A {obj} is set on the water in a {vessel} and floats.',
        S(('core', f'A {obj} is present and recognisable.'),
          ('core', f'It is placed onto the water surface of a {vessel} of water.'),
          ('core', 'The placing is gentle -- lowered or set down, not thrown or dropped hard.'),
          ('minor', f'The {vessel} reads as the container the caption names and is filled with '
                    f'water.')),
        P(*pc),
        note=("The dataset's law for id 7 describes a wood block, copied from id 8; the caption "
              "puts a tennis ball there. Both float, so the outcome is unchanged, but the "
              "rubric follows the caption's object." if i == 7 else None))

# ============ Stress: squeezing a soaked porous body (10, 11, 14) =======
for i, obj in [(10, 'sponge'), (11, 'soft towel'), (14, 'soft cloth')]:
    add('poroelastic-squeeze', i,
        f'A soaked {obj} is squeezed harder and harder by hand and water runs out of it.',
        S(('core', f'A {obj} is present and visibly loaded with water.'),
          ('core', 'A hand squeezes it.'),
          ('core', 'The squeezing builds up over the clip rather than staying level or easing '
                   'off.'),
          ('minor', 'The clip reads as a timelapse: the process advances across it rather than '
                    'showing one held moment.')),
        P(('fatal', f'Water leaves the {obj} while it is being compressed.',
           f'the {obj} is squeezed hard and no water ever comes out of it'),
          ('core', 'It compresses only where and while the hand presses it, and stops '
                   'compressing when the hand stops.',
           'it goes on compressing after the hand stops, or compresses in a region the hand '
           'never touched'),
          ('core', 'The water that comes out came from inside: the material grows visibly less '
                   'swollen at the squeeze, and the amount of water is bounded by what it held.',
           'more water pours out than the material could have held, or it stays as swollen as '
           'before while water streams from it'),
          ('major', 'It springs back only partly when the hand releases -- not to its original '
                    'swollen size -- and it stays damp rather than dry.',
           'it springs back fully to its original swollen size, or comes out dry'),
          ('major', 'Water runs downward off it and pools or falls.',
           'water runs up the material or hangs in the air beside it'),
          ('minor', 'No water is drawn back in once it has left.',
           'spilt water climbs back into the material')))

# ============ Stress: extruding an open tube (13) =======================
add('extrusion', 13,
    'An open toothpaste tube is squeezed harder and harder and paste comes out of the nozzle.',
    S(('core', 'An open toothpaste tube is present, with its cap off or its nozzle clear.'),
      ('core', 'A hand squeezes the tube.'),
      ('core', 'The squeezing builds up over the clip rather than staying level.'),
      ('minor', 'The clip reads as a timelapse: the process advances across it.')),
    P(('fatal', 'Paste comes out of the tube while it is squeezed.',
       'the tube is squeezed hard and nothing ever comes out of it'),
      ('core', 'The paste emerges from the open nozzle only, only while the tube is squeezed, '
               'and stops when the squeeze stops.',
       'paste appears from a closed end or through the tube wall, or keeps flowing after the '
       'squeezing stops'),
      ('core', 'What comes out came from inside: the tube collapses and empties as paste leaves '
               'it, and the amount extruded is bounded by what the tube held.',
       'the tube stays plump and full while paste streams out of it, or yields far more paste '
       'than it could have contained'),
      ('major', 'The tube dents where the fingers press and keeps the crease after they move '
                'on; it does not spring back perfectly plump.',
       'the tube springs back to its original round shape as each finger lifts'),
      ('major', 'The paste holds a ribbon shape roughly the cross-section of the nozzle it came '
                'from, sagging slowly rather than running like water.',
       'the extruded paste runs and spreads like a thin liquid, or emerges far wider than the '
       'nozzle'),
      ('minor', 'The extruded paste stays where it lands and is not drawn back into the tube.',
       'paste that has come out is sucked back in')))

# ============ Stress: pressing a sealed air balloon (12) ================
add('elastic-deformation', 12,
    'An inflated balloon is pressed down harder and harder by hand.',
    S(('core', 'An air-filled, inflated balloon is present.'),
      ('core', 'A hand presses down on it.'),
      ('core', 'The pressure builds up over the clip rather than staying level.'),
      ('minor', 'The clip reads as a timelapse: the process advances across it.')),
    P(('fatal', 'The balloon holds roughly its overall size under hand pressure: the trapped '
                'air has nowhere to go and is barely compressible.',
       'the balloon shrinks all over as it is pressed, as if the air inside had gone somewhere'),
      ('core', 'It flattens only where the hand bears on it, at the moment the hand bears on '
               'it.',
       'it flattens in a region the hand never touches, or flattens before the hand reaches it'),
      ('core', 'It bulges outward elsewhere while it is flattened at the contact.',
       'the pressed balloon stays the same shape everywhere except the dent, with no bulge '
       'anywhere'),
      ('major', 'It springs back to its original shape when the hand lifts.',
       'the dent stays after the hand is gone, as if the rubber were putty'),
      ('minor', "The rubber's surface markings stretch and crowd with the local deformation "
                "rather than sliding across a still surface.",
       'printed markings slide over the rubber while the rubber itself deforms under them'),
      ('major', 'The tearing starts at the loaded region and the burst is irreversible.',
       'the balloon splits somewhere the hand never loaded, or the rubber closes back up',
       'the balloon bursts')),
    note="The dataset's law says the balloon will shrink. Air is nearly incompressible at hand "
         "loads, so a sealed balloon changes shape at roughly constant volume and springs back; "
         "the rubric judges that instead.")

# ============ Atmospheric pressure: thin vessel buckles (15, 16, 18) ====
for i, obj, extra in [
    (15, 'thin sealed plastic bottle',
     ('minor', 'The thin plastic crumples progressively and irregularly rather than collapsing '
               'all at once into a neat shape.',
      'the bottle collapses into a tidy symmetrical form with no irregular crumpling')),
    (16, 'sealed empty aluminium can', None),
    (18, 'thin sealed aluminium can', None),
]:
    pc = [
        ('fatal', 'The wall moves inward, never outward: no part of it bulges out while air is '
                  'being removed.',
         'the vessel swells or bulges outward as air is drawn out of it'),
        ('core', 'It deforms only while air is being drawn out, and the deformation tracks the '
                 'extraction rather than starting before it.',
         'it starts collapsing before any air is drawn out, or goes on collapsing after the '
         'extraction stops'),
        ('core', 'The collapse is a buckling, not a smooth uniform shrink: panels cave in, '
                 'sharp creases and facets appear, and the shape becomes irregular.',
         'the vessel shrinks smoothly and uniformly, keeping its original proportions like a '
         'scaled-down copy'),
        ('major', 'It stays crumpled and does not spring back to its original shape while the '
                  'air is still out.',
         'the crumpled vessel pops back to its original shape with the air still removed'),
        ('major', 'It stays the same object: it dents and creases but does not tear open, melt '
                  'or turn into another material.',
         'the wall tears open, melts or changes material as it collapses'),
        ('minor', 'The creases stay where they formed as the collapse continues; they do not '
                  'migrate across the wall.',
         'creases slide around the wall while the vessel keeps collapsing'),
    ]
    if extra:
        pc.append(extra)
    add('atmospheric-pressure', i,
        f'Air is pumped out of a {obj} and the wall is crushed inward.',
        S(('core', f'A sealed, empty {obj} is present.'),
          ('core', 'Air is being drawn or pumped out of it, and something in shot does the '
                   'drawing.'),
          ('core', 'The extraction is gradual and forceful, building over the clip rather than '
                   'happening in one instant.'),
          ('minor', 'The clip reads as a timelapse: the process advances across it.')),
        P(*pc))

# ============ Atmospheric pressure: stiff shell dimples (17) ============
add('atmospheric-pressure', 17,
    'Air is pumped out of a sealed hollow plastic ball and one side caves in.',
    S(('core', 'A sealed, empty plastic ball is present.'),
      ('core', 'Air is being drawn out of it, and something in shot does the drawing.'),
      ('core', 'The extraction is gradual and forceful, building over the clip.'),
      ('minor', 'The clip reads as a timelapse: the process advances across it.')),
    P(('fatal', 'The wall moves inward, never outward.',
       'the ball swells or bulges outward as air is drawn out of it'),
      ('core', 'It deforms only while air is being drawn out.',
       'it starts deforming before any air is drawn out, or keeps deforming after the '
       'extraction stops'),
      ('core', 'The deformation is a local dimple or cave-in on one side, not a uniform '
               'reduction in diameter with the ball staying round.',
       'the ball shrinks smoothly and stays spherical, like a scaled-down copy of itself'),
      ('major', 'The dent stays once formed and the ball does not spring back to round while '
                'the air is still out.',
       'the dent pops back out with the air still removed'),
      ('major', 'The parts of the shell that have not caved keep their original curvature and '
                'size.',
       'the undented parts shrink or flatten along with the dent'),
      ('minor', 'The dent appears suddenly, once the shell buckles, rather than creeping in at '
                'a perfectly even rate.',
       'the surface sinks in at a perfectly smooth constant rate with no buckling moment')),
    note="The dataset's law says the ball will shrink. A stiff curved shell under external "
         "pressure buckles locally instead, so the rubric asks for a dimple rather than a "
         "uniform reduction.")

# ============ Elastic recoil: emptying a balloon (19) ==================
add('elastic-recoil', 19,
    'Air is drawn out of a sealed balloon and the stretched rubber contracts and wrinkles.',
    S(('core', 'A thin, sealed, inflated balloon is present.'),
      ('core', 'Air is being drawn out of it, and something in shot does the drawing.'),
      ('core', 'The extraction is gradual and forceful, building over the clip.'),
      ('minor', 'The clip reads as a timelapse: the process advances across it.')),
    P(('fatal', 'The balloon shrinks as the air leaves, and only while the air is being drawn '
                'out.',
       'the balloon stays fully inflated while air is drawn out of it, or re-inflates during '
       'the extraction'),
      ('core', 'It gets smaller all over as the stretched rubber recovers, rather than buckling '
               'with sharp creases like a rigid shell.',
       'the balloon caves in with sharp panels and facets as if it had a stiff wall'),
      ('core', 'Wrinkles and slack folds appear in the rubber as it deflates, and the surface '
               'markings crowd together with it.',
       'the rubber stays taut and smooth all the way down to a much smaller balloon'),
      ('major', 'It does not re-inflate on its own while the air is still out.',
       'the deflated balloon fills out again with nothing supplying air'),
      ('major', 'The neck stays sealed to whatever is drawing the air out; the balloon does not '
                'empty through an opening that is not there.',
       'air leaves through the rubber or through a hole that never appears'),
      ('minor', 'The shrinking tracks the extraction rather than proceeding in jumps unrelated '
                'to it.',
       'the balloon changes size in steps that have nothing to do with the extraction')),
    note="The dataset's law credits atmospheric pressure. An inflated balloon is already above "
         "atmospheric inside, so it collapses by elastic recoil of the stretched rubber -- "
         "shrinking and wrinkling all over, with none of the buckling seen in the rigid vessels "
         "of ids 15, 16 and 18.")

# ============ Solid pressure: needle or pin bursts a balloon (20, 23) ===
for i, tool, kind, extra in [
    (20, 'needle', 'fully inflated', [
        ('minor', 'The escaping air is invisible: nothing is seen leaving the balloon except '
                  'the moving rubber itself.',
         'a visible jet, cloud or puff of air is seen streaming out of the burst')]),
    (23, 'pin', 'water-filled', [
        ('major', 'The water is released as a coherent mass that then falls and spreads, and '
                  'the emptied rubber is left limp and wet.',
         'the water vanishes with the burst, or the rubber is left dry'),
        ('minor', 'The water goes downward and stays where it lands; it is not drawn back into '
                  'the rubber.',
         'spilt water climbs back into the rubber or moves upward on its own')]),
]:
    add('stress-concentration', i,
        f'A {tool} is pressed slowly into a {kind} balloon until it bursts.',
        S(('core', f'A {tool} and a {kind} balloon are both present.'),
          ('core', f'A hand presses the {tool} into the balloon\'s surface.'),
          ('core', 'The press is slow and gradual, and the tip reaches the rubber and goes into '
                   'it.'),
          ('minor', 'The shot stays on the contact region long enough to show the tip meeting '
                    'the rubber.')),
        P(*([('fatal', "The balloon fails at the tip's point of contact, not anywhere else on "
                       "its surface.",
              'the balloon bursts or splits somewhere away from the tip'),
             ('core', 'It fails only once the tip has plainly reached and dented the rubber, '
                      'not before contact.',
              'the balloon bursts before the tip touches it'),
             ('core', 'Once it starts, the failure runs quickly and completely across the taut '
                      'rubber rather than leaving a neat small hole in a still-inflated '
                      'balloon.',
              'a tidy round hole appears and the balloon stays inflated around it'),
             ('major', 'The rubber dents and stretches inward around the tip in the moments '
                       'before it gives.',
              'the rubber stays undisturbed right up to the instant it bursts'),
             ('major', 'The failure is irreversible: the rubber does not close up and the '
                       'balloon does not re-inflate.',
              'the burst rubber knits back together or the balloon fills out again'),
             ('minor', 'The freed rubber snaps away from the burst and then falls slack; it '
                       'does not hold its inflated shape.',
              'the shredded rubber keeps the balloon\'s round shape after the burst')] + extra)))

# ============ Solid pressure: tip into a taut sheet (21, 22) ============
for i, tool, sheet, extra in [
    (21, 'pencil', 'tightly stretched rubber sheet', None),
    (22, 'fork', 'tensed piece of plastic wrap',
     ('minor', 'A fork presses several tines at once, so several punctures appear together, one '
               'at each tine that reaches the wrap.',
      'a single puncture appears although several tines plainly reach the wrap')),
]:
    pc = [
        ('fatal', 'The sheet fails at the point of contact, not elsewhere.',
         'a hole or tear appears in the sheet away from the tip'),
        ('core', 'It tents and stretches inward around the tip before it gives, and the tenting '
                 'deepens as the tip advances.',
         'the sheet stays flat right up to the instant it punctures'),
        ('core', 'The failure happens only after contact, not before the tip arrives.',
         'the sheet punctures before the tip touches it'),
        ('major', 'The tear starts at the puncture and runs outward from it.',
         'the tear grows inward toward the puncture from somewhere else'),
        ('major', 'The failure is irreversible: the sheet does not close up.',
         'the punctured sheet seals itself back up'),
        ('minor', 'The freed edges relax and slacken as the tension is released.',
         'the punctured sheet stays as taut as before all around the hole'),
    ]
    if extra:
        pc.append(extra)
    add('stress-concentration', i,
        f'A {tool} is pressed slowly into a {sheet} until it punctures.',
        S(('core', f'A {tool} and a {sheet} are both present.'),
          ('core', f'The {tool} is pressed into the sheet and its tip goes through.'),
          ('core', 'The press is slow and gradual rather than a stab.'),
          ('minor', 'The shot stays on the contact region long enough to show the tip meeting '
                    'the sheet.')),
        P(*pc))

# ============ Solid pressure: blunt pencil on a balloon (24) ============
add('stress-concentration', 24,
    'A pencil is pressed slowly into an inflated balloon; it may or may not burst.',
    S(('core', 'A pencil and a fully inflated balloon are both present.'),
      ('core', "A hand presses the pencil into the balloon's surface."),
      ('core', 'The press is slow and gradual, and the tip reaches the rubber and indents it.'),
      ('minor', 'The shot stays on the contact region long enough to show the tip meeting the '
                'rubber.')),
    P(('fatal', "The pencil is checked by the rubber's resistance rather than passing through "
                "it as if nothing were there.",
       'the pencil slides through the intact rubber without piercing it'),
      ('core', 'The rubber dents and stretches inward around the tip while the pencil presses, '
               'and the dent deepens as it advances.',
       'the rubber stays undisturbed while the pencil pushes into it'),
      ('core', 'Whichever outcome the clip commits to happens once and stays: the balloon does '
               'not burst, recover and burst again.',
       'the balloon bursts and then is whole again later in the clip'),
      ('major', 'The balloon holds its overall inflation while it is only being indented; it '
                'does not visibly shrink or swell under the press.',
       'the balloon deflates or inflates as the pencil presses on it, with nothing moving air'),
      ('minor', 'The balloon is pushed back, or held by something, as the pencil advances '
                'rather than staying pinned in place with nothing supporting it.',
       'the balloon stays fixed in mid-air under the push with nothing holding it'),
      ('major', 'It bursts at the point of contact, only after contact, and the burst is '
                'irreversible.',
       'the burst starts away from the tip, or the rubber closes back up afterwards',
       'the balloon bursts'),
      ('minor', 'The rubber springs back to its original shape when the pencil withdraws.',
       'the dent stays in the rubber after the pencil is gone',
       'the balloon does not burst and the pencil is withdrawn')),
    note="The dataset's law demands an explosion. A blunt tip pressed slowly can dent an "
         "inflated balloon deeply without piercing it, so the outcome is genuinely undetermined "
         "and the rubric judges internal consistency instead.")

# ============ Elasticity: bouncing balls (25-29) ========================
for i, ball, extra in [
    (25, 'rubber ball', None),
    (26, 'basketball',
     ('minor', "The basketball's flattening at the contact is visible and brief, and it rebounds "
               "high -- a substantial fraction of the height it came from.",
      'the basketball barely rebounds at all, or shows no contact deformation at any point')),
    (27, 'tennis ball', None),
    (28, 'football', None),
    (29, 'beach ball',
     ('minor', 'Being very light for its size, the beach ball is noticeably slowed by the air: '
               'it loses speed between bounces and its rebounds die away quickly.',
      'the beach ball keeps its speed through the air like a dense ball and bounces on and on')),
]:
    pc = [
        ('fatal', f'The {ball} reverses direction at the ground, at the moment of contact, not '
                  f'at a gap above it.',
         f'the {ball} turns around in empty air above the ground, or sinks into or through it'),
        ('core', 'It leaves the ground more slowly than it arrived, so the rebound does not '
                 'reach the height the throw came from.',
         'it comes off the ground faster than it hit, or rebounds higher than it was thrown '
         'from'),
        ('core', 'Each successive bounce is lower than the one before and the intervals between '
                 'bounces get shorter; the sequence never grows.',
         'a later bounce goes higher than an earlier one, or the bounces settle into an endless '
         'identical rhythm'),
        ('major', 'Between bounces it follows a single smooth arc, speeding up as it falls and '
                  'slowing as it rises, with no kink or hover in mid-air.',
         'the flight path kinks, hangs or changes direction in mid-air with nothing touching it'),
        ('major', 'The rebound direction follows the approach: thrown straight down it comes '
                  'back up, thrown at an angle it comes off on the mirrored line.',
         'the ball comes off the ground on a line unrelated to how it arrived'),
        ('minor', 'It flattens against the ground at the contact and recovers its round shape '
                  'as it leaves, rather than staying dented.',
         'the ball stays deformed after leaving the ground'),
        ('minor', 'Its motion only ever loses energy: it does not speed up in flight.',
         'the ball gains speed while in the air with nothing driving it'),
    ]
    if extra:
        pc.append(extra)
    add('elasticity', i,
        f'A {ball} is thrown hard at the ground and bounces.',
        S(('core', f'A {ball} is present and recognisable.'),
          ('core', 'It is thrown toward the ground and reaches it.'),
          ('core', 'The throw is forceful rather than a gentle release or a drop.'),
          ('minor', 'The clip stays with the ball through the impact and its aftermath rather '
                    'than cutting away at contact.')),
        P(*pc))

# ============ Friction: abrasive marking (30, 32) =======================
for i, tool, surf, extra in [
    (30, 'piece of white chalk', 'rough, dark blackboard',
     ('minor', 'Chalk dust falls from the contact and settles below, and the mark reads as a '
               'dry powdery deposit that could be smudged.',
      'no dust is produced anywhere and the mark reads as wet ink or paint')),
    (32, 'piece of red crayon', 'rough, white paper',
     ('minor', 'The wax mark sits on the raised texture of the paper and skips the hollows, so '
               'it reads broken rather than perfectly solid.',
      'the crayon mark is a flat, even, fully solid block on plainly rough paper')),
]:
    add('abrasion', i,
        f'A {tool} is drawn across a {surf} and leaves a mark.',
        S(('core', f'A {tool} is present and is drawn across a {surf}.'),
          ('core', 'A mark appears on the surface as a result.'),
          ('core', 'The surface reads as the one the caption describes, in texture and colour.'),
          ('minor', 'The shot stays close enough on the contact to show the tip meeting the '
                    'surface.')),
        P(('fatal', 'Nothing is marked that the tip never touched: no stroke appears in a '
                    'region the tip never visited.',
           'marks appear where the tip never went, or a finished stroke materialises on its own'),
          ('core', 'The mark grows from the tip as it moves and its leading end never runs '
                   'ahead of the tip.',
           'the line draws itself ahead of the tip'),
          ('core', 'The mark is permanent unless something wipes it: it does not fade or '
                   'retract on its own.',
           'the mark fades away or retracts back into the tip with nothing erasing it'),
          ('major', 'No mark appears where the tip was lifted clear of the surface.',
           'the line continues while the tip is plainly off the surface'),
          ('major', 'The stick is consumed as it writes -- it shortens or blunts -- and loose '
                    'dust or crumbs are shed at the contact.',
           'the stick is as long and sharp after a great deal of writing as it was at the start'),
          ("minor", "The mark's colour is the stick's own, laid over the surface's colour "
                    "rather than replacing the surface.",
           'the mark comes out in a colour the stick does not have, or the surface changes '
           'colour underneath it'),
          extra))

# ============ Ink deposition: pens and markers (31, 33, 34) =============
for i, tool, surf, extra in [
    (31, 'blue marker', 'smooth, white whiteboard', None),
    (33, 'yellow highlighter', 'rough, brown cardboard',
     ('minor', "The highlighter's ink is translucent: what is underneath still reads through "
               "the mark rather than being covered over.",
      'the highlighter mark is opaque and hides whatever was under it')),
    (34, 'black pen', 'smooth, white notebook', None),
]:
    pc = [
        ('fatal', 'Nothing is marked that the tip never touched: no stroke appears in a region '
                  'the tip never visited.',
         'marks appear where the tip never went, or a finished stroke materialises on its own'),
        ('core', 'The mark grows from the tip as it moves and its leading end never runs ahead '
                 'of the tip.',
         'the line draws itself ahead of the tip'),
        ('core', 'The mark is ink laid onto the surface: its colour is the ink\'s own, and it '
                 'may spread slightly or soak in rather than sitting as loose powder on top.',
         'the mark reads as dry powder heaped on the surface, or comes out in a colour the ink '
         'does not have'),
        ('major', 'No mark appears where the tip was lifted clear of the surface.',
         'the line continues while the tip is plainly off the surface'),
        ('major', 'The mark is permanent unless something wipes it: it does not fade or retract '
                  'on its own.',
         'the mark fades away or retracts back into the tip with nothing erasing it'),
        ('minor', 'The pen is not visibly consumed by writing: it does not shorten, and no dust '
                  'or crumbs are shed at the contact.',
         'the tip visibly wears down, or sheds dust and crumbs as it writes'),
    ]
    if extra:
        pc.append(extra)
    add('ink-deposition', i,
        f'A {tool} is drawn across a {surf} and leaves a mark.',
        S(('core', f'A {tool} is present and is drawn across a {surf}.'),
          ('core', 'A mark appears on the surface as a result.'),
          ('core', 'The surface reads as the one the caption describes, in texture and colour.'),
          ('minor', 'The shot stays close enough on the contact to show the tip meeting the '
                    'surface.')),
        P(*pc),
        note="The dataset's law credits friction. A pen, marker or highlighter marks by "
             "depositing ink, and nothing is abraded off the tip, so this rubric must not "
             "require the wear and shedding that the chalk and crayon prompts (ids 30, 32) do.")

# ============ Wetting: repellent surfaces (35, 37) ======================
for i, surf, extra in [
    (35, 'lotus leaf',
     ('minor', 'On the lotus leaf the drop sits especially high and round, riding on the '
               'microtexture, and it detaches and rolls at the slightest tilt.',
      'the drop clings to the tilting leaf and has to be shaken loose')),
    (37, 'waxed apple', None),
]:
    pc = [
        ('fatal', f'The drop stays a body of liquid on top of the {surf}: it does not soak into '
                  f'the solid or pass through it.',
         f'the drop sinks into the {surf} or passes through its surface'),
        ('core', 'It holds a rounded, near-spherical shape while it sits and while it moves, '
                 'rather than flattening into a film.',
         'the drop spreads into a flat film or a wide shallow puddle'),
        ('core', 'It meets the surface over a small contact patch, with a steep edge where '
                 'liquid meets solid.',
         'the drop meets the surface over a broad patch with a shallow feathered edge'),
        ('core', 'It leaves the surface behind dry: no wet trail and no darkened path where it '
                 'has passed.',
         'a wet or darkened trail is left along the path the drop took'),
        ('major', 'It moves as one body and keeps its shape while moving; it does not stretch '
                  'into a streak or shed smaller drops.',
         'the drop stretches into a streak or breaks up into a train of smaller drops as it '
         'moves'),
        ('major', 'It moves downhill or with whatever pushes it, and it does not climb the '
                  'surface on its own.',
         'the drop runs uphill or against the slope with nothing driving it'),
        ('minor', 'The drop is transparent: it refracts and brightens what is behind it, and '
                  'carries a small specular highlight that stays put relative to the light '
                  'while the drop moves.',
         'the drop is opaque, or its highlight travels with the drop instead of staying with '
         'the light'),
    ]
    if extra:
        pc.append(extra)
    add('wetting', i,
        f'A water drop beads up and rolls across a {surf}.',
        S(('core', f'A single water drop is on a {surf}.'),
          ('core', 'The drop moves across the surface during the clip.'),
          ('core', f'The surface reads as a {surf}.'),
          ('minor', 'The drop glistens -- it catches the light as the caption describes.')),
        P(*pc))

# ============ Wetting: wettable surfaces (36, 38) ======================
for i, surf in [(36, 'smooth glass surface'), (38, 'glazed ceramic vase')]:
    add('wetting', i,
        f'A water drop wets and spreads on a {surf} instead of beading.',
        S(('core', f'A single water drop is on a {surf}.'),
          ('core', 'The drop moves across the surface during the clip.'),
          ('core', f'The surface reads as a {surf}.'),
          ('minor', 'The drop glistens -- it catches the light as the caption describes.')),
        P(('fatal', f'The drop stays on the outside of the {surf}: it does not soak into the '
                    f'solid or pass through it.',
           'the drop sinks into the glass or ceramic, or passes through it'),
          ('core', 'It reads as a flattened dome rather than a sphere: plainly wider than it is '
                   'tall.',
           'the drop stands up as a near-perfect bead on the bare wettable surface'),
          ('core', 'Its edge meets the surface at a shallow angle, spread over a broad contact '
                   'patch.',
           'the drop meets the surface over a tiny patch with a steep edge, as it would on wax'),
          ('major', 'When it moves it stretches and leaves a wet trail or a darkened, glossy '
                    'path behind it.',
           'the drop travels and leaves the surface behind completely dry'),
          ('major', 'Some liquid is left behind as it moves: the drop shrinks or breaks into '
                    'smaller drops rather than travelling as one intact bead the whole way.',
           'the drop rolls the length of the surface without losing any liquid at all'),
          ('minor', 'It does not climb the surface on its own.',
           'the drop runs uphill with nothing driving it'),
          ('minor', 'The drop is transparent: it refracts what is behind it and carries a '
                    'specular highlight.',
           'the drop is opaque and shows no refraction or highlight')),
        note="The dataset's law asks for spherical droplets. Bare glass and glazed ceramic are "
             "wettable, so water flattens, sticks and leaves a trail on them; only the "
             "repellent surfaces of ids 35 and 37 support the spherical claim.")

# ============ Absorption: a drop on paper (39) =========================
add('absorption', 39,
    'A water drop meets the textured paper of a book and soaks in instead of sliding.',
    S(('core', 'A single water drop is on the surface of a book.'),
      ('core', 'The drop slides gracefully across the surface as the caption describes.'),
      ('minor', 'The surface reads as textured paper.'),
      ('minor', 'The drop glistens -- it catches the light as the caption describes.')),
    P(('fatal', 'Water on paper soaks in rather than staying an intact bead that travels across '
                'the page.',
       'the drop rolls across the paper like a bead on wax, leaving the page dry behind it'),
      ('core', 'A darkened wet patch spreads outward from the contact, its edge advancing and '
               'then stopping.',
       'the paper stays unchanged where the water sits, with no darkened patch'),
      ('core', 'The wet patch never shrinks or retreats on its own; any drying is slow and '
               'uniform rather than a receding edge.',
       'the wet patch pulls back into a drop or races away as a retreating edge'),
      ('major', 'The paper itself answers the water: the wetted region darkens, and it may '
                'cockle, wrinkle or buckle as the fibres swell.',
       'the paper stays perfectly flat and stiff while visibly soaked'),
      ('major', 'The water is conserved: the stain is bounded by the drop that made it and no '
                'new water appears.',
       'the stain keeps growing far beyond what the drop could wet, or new drops appear from '
       'nowhere'),
      ('minor', 'Ink or print under the wet patch may bleed or darken but does not slide across '
                'the page.',
       'printed text moves or floats away on the water')),
    note="Caption and physics pull apart here: a dewdrop cannot slide gracefully across paper, "
         "it is absorbed. SA asserts the caption's sliding, so a physically correct clip will "
         "fail S2; PC judges the absorption that actually happens. Both can be right at once.")
