# phyworldbench 281-315: Human and Animal Motion (Biomechanics).
# Same authoring flow as the earlier blocks. Cross-check against KS[i] -- id 294 is one of the
# eleven dict-wrapped records.
#
# This category collides head-on with _policy.json's not_penalized list, which excludes athletic
# form, technique, physique and skill outright. The benchmark's standards here are saturated with
# exactly that: 'naturally and fluidly', 'smooth and coordinated', 'deliberate and controlled',
# 'without fumbling or needing readjustments', 'minimal swaying', 'no unnecessary pauses or
# jerks'. A person who fumbles a shoelace or wobbles on a curb is being realistic, not violating
# physics, so none of those phrases is used as an item.
#
# What IS judgeable, and what generated video notoriously breaks, is five things, and they carry
# the whole category:
#   1. body-plan integrity -- limbs and digits in the right number, attached, not merging or
#      passing through each other, joints bending at joints and within their range;
#   2. contact mechanics -- a foot bearing weight stays planted (no foot-slip), propulsion needs
#      ground contact, and the body advances in step with the leg cycle (no moonwalking);
#   3. ballistic flight -- once airborne, a body follows its arc and cannot steer or re-accelerate;
#   4. stimulus-response order for the reflex block -- the cause comes first, the response is fast;
#   5. object-interaction causality for the fine-motor block -- things move when and only when the
#      hands or beak act on them, and stay moved.
#
# Where a standard asks for something invisible -- muscle contractions under clothing (284, 298),
# 'noticeable centrifugal force' (306), centre of mass placement (312) -- it is restated as the
# visible consequence or dropped, and the note says which.


def intact(o, parts):
    return ('fatal',
            f'{o[0].upper()}{o[1:]} keeps one connected body with the right parts: {parts} stay '
            f'attached, do not multiply, merge or vanish, and do not pass through each other or '
            f'through anything solid.',
            f'{o} gains or loses {parts} mid-shot, or parts of the body merge, detach or pass '
            f'through each other or through solid objects')


def joints(o):
    return ('core', f'{o[0].upper()}{o[1:]} bends at its joints and within their range.',
            f'a limb of {o} bends in the middle of a bone, or a joint folds the wrong way')


def planted(o, foot='a foot'):
    return ('core', f'While {foot} of {o} is planted and bearing weight, it stays put on the '
                    f'surface.',
            f'a planted weight-bearing foot slides across the surface, or hovers just above it')


def advance(o):
    return ('major', f'{o[0].upper()}{o[1:]} covers ground in step with its leg motion: strides '
                     f'move it, and it does not glide with legs still or run in place while '
                     f'travelling.',
            f'{o} slides along with no leg motion, or strides hard while staying in one place, or '
            f'the ground covered has no relation to the steps taken')


def fixed(o):
    pl = ' and ' in o
    return ('minor',
            f'{o[0].upper()}{o[1:]} stay put and keep their shape throughout.' if pl else
            f'{o[0].upper()}{o[1:]} stays put and keeps its shape throughout.',
            f'{o} shift, flex or change shape on their own' if pl else
            f'{o} shifts, flexes or changes shape on its own')


def surface(o, mk):
    return ('minor', f'{mk[0].upper()}{mk[1:]} stay with {o} and move with it.',
            f'{mk} slide over the body, detach, or change from one moment to the next')


# ---- Anatomical Feasibility (281-287) --------------------------------------
add('ballistic-leap', 281,
    'The frog crouches, drives off with its hind legs, arcs through the air and lands in the pond.',
    S(('core', 'A frog is present on a rock.'),
      ('core', 'It leaps off the rock.'),
      ('core', 'It goes into the pond.'),
      ('minor', 'The leap starts from a crouch rather than the frog already being airborne.')),
    P(intact('the frog', 'its four legs and its body'),
      ('core', 'The push comes from the hind legs extending while the frog is still on the rock.',
       'the frog rises off the rock with its legs still folded, or its legs extend only after it '
       'is already in the air'),
      ('core', 'Once airborne, the frog follows a single arc: up, over and down, without steering, '
               'pausing or gaining speed in mid-air.',
       'the frog changes direction in mid-air, hangs at the top of its leap, or accelerates '
       'forward with nothing to push on'),
      ('major', 'The frog lands where its arc was taking it, in or at the pond, and the water '
                'responds -- a splash and rings.',
       'the frog enters the water and the surface stays glassy, or it lands somewhere its arc was '
       'not going'),
      joints('the frog'),
      ('minor', 'The legs trail or fold during flight and gather for the landing.',
       'the legs stay rigidly extended and motionless from launch to landing'),
      fixed('the rock')),
    note="Their standards ask for full symmetric extension and for the body to move 'naturally and "
         "fluidly' with 'balance and stability' on landing -- form words that _policy.json "
         "excludes. The physics that remains is the launch-flight-landing chain: the impulse must "
         "come from leg extension DURING rock contact, the flight must be a single unpowered arc, "
         "and the water must answer the arrival. Those three carry the scenario; grace does not.")

add('crouch-jump-landing', 282,
    'The cat crouches, springs off the ground, arcs up and lands on the table.',
    S(('core', 'A cat is present.'),
      ('core', 'A table is present.'),
      ('core', 'The cat jumps and ends up on the table.'),
      ('minor', 'The jump starts from the ground or a lower surface, not from mid-air.')),
    P(intact('the cat', 'its four legs, tail and body'),
      ('core', 'The jump is launched from a crouch: the hind legs bend and then extend while still '
               'on the ground.',
       'the cat floats upward from a standing pose with no crouch or extension, or its legs push '
       'off after it has already left the ground'),
      ('core', 'In the air the cat follows one arc and does not steer, stall or re-accelerate.',
       'the cat adjusts its course in mid-air, hovers at the top, or speeds up in flight'),
      ('major', 'The arc actually reaches the table top: the launch is aimed and scaled to the '
                'height it achieves.',
       'the cat leaps feebly and materialises on the table anyway, or overshoots hugely and still '
       'stops dead on it'),
      joints('the cat'),
      ('minor', 'The landing is taken on the paws, front paws touching first, with the body '
                'gathering behind.',
       'the cat lands flat on its belly or on its side from a routine jump'),
      fixed('the table')),
    note="Their first and third standards carry real content -- the coordinated hind-leg push, and "
         "the front-paws-first landing, which is genuine cat landing mechanics -- and both are "
         "kept, the landing as a minor since a clumsy cat is not a physics violation. Their second "
         "('smoothly and naturally ... without any abrupt or unnatural movements') is form and is "
         "not used. The addition is the match between launch and outcome: a jump that visibly "
         "could not reach the table must not end on it.")

add('load-bearing-lift', 283,
    'The person takes the weight of the box and their body shows it: braced, counterbalanced, and '
    'moving with the load.',
    S(('core', 'A person is present.'),
      ('core', 'A box is present, and it reads as heavy.'),
      ('core', 'The person lifts it from the ground.'),
      ('minor', 'The lift starts with the box at rest on the ground.')),
    P(intact('the person', 'their arms, legs and hands'),
      ('core', 'The box moves only while the person is holding and lifting it, and it moves with '
               'their hands.',
       'the box rises before the hands close on it, keeps rising after they let go, or moves '
       'independently of the grip'),
      ('core', 'The load shows in the body: the person braces, straightens under strain, and once '
               'holding the box leans back or staggers slightly to keep the combined weight over '
               'their feet.',
       'the person plucks the heavy box up one-handed at arm\'s length as though it were empty, '
       'standing perfectly casual'),
      ('major', 'The lift is slower than an empty-handed movement of the same arms would be.',
       'the box flies up as fast as the person could swing their empty arms'),
      ('major', 'The person\'s feet stay planted while they take up the load.',
       'the feet slide about under the person during the lift'),
      joints('the person'),
      ('minor', 'The box stays rigid and keeps its shape in the grip.',
       'the box bends and slumps in the hands like a sack')),
    note="Their second standard, that the back stay 'relatively straight, avoiding excessive "
         "bending', is lifting TECHNIQUE -- a person who lifts badly with a rounded back is being "
         "unwise, not unphysical -- and _policy.json excludes form, so it is not used. Their first, "
         "the bend-and-straighten of the legs, survives inside the bracing item. What replaces the "
         "form words is the signature of mass: the lift is slow, the body counterbalances by "
         "leaning back, and the box moves only with the hands.")

add('sprint-start-drive', 284,
    'The sprinter drives out of the start, pushing back against the ground and gaining speed stride '
    'by stride.',
    S(('core', 'A sprinter is present.'),
      ('core', 'They start and accelerate, as at the start of a race.'),
      ('minor', 'The start begins from rest -- blocks, a crouch or a standing set position.'),
      ('minor', 'The setting reads as a race or a track.')),
    P(intact('the sprinter', 'their arms and legs'),
      planted('the sprinter', 'each driving foot'),
      ('core', 'The sprinter speeds up over the first strides: slowest at the first step, visibly '
               'faster after several.',
       'the sprinter is at full speed from the first frame of movement, or gains no speed at all '
       'over many strides'),
      advance('the sprinter'),
      ('major', 'Acceleration happens only while feet are driving against the ground; nothing '
                'speeds the sprinter up mid-air between strides.',
       'the sprinter gains speed during a stretch when neither foot is in contact with the track'),
      ('major', 'The body leans forward hard at the start and comes more upright as speed builds.',
       'the sprinter accelerates from the gun bolt upright, or stays in the deep start lean at '
       'full speed'),
      ('minor', 'The arms swing opposite to the legs.',
       'both arms swing with the same-side legs, or hang motionless through a hard start')),
    note="Their third standard requires muscle contractions in calves, thighs and glutes to be "
         "'clearly visible and proportionate to the exertion', which is unjudgeable in most "
         "footage -- muscles are under skin and kit, and 'proportionate' has no visible scale -- so "
         "it is not used. Their first, ground contact producing the drive, is the right physics "
         "and is core here. The forward lean coming upright is the visible kinematic signature of "
         "acceleration and stands in for the invisible muscles.")

add('quadruped-run', 285,
    'The dog runs the ball down with a proper four-beat drive, feet gripping and body advancing '
    'with the strides.',
    S(('core', 'A dog is present.'),
      ('core', 'A ball is present.'),
      ('core', 'The dog runs after the ball.'),
      ('minor', 'The ball is moving ahead of the dog rather than lying at its feet.')),
    P(intact('the dog', 'its four legs, tail and body'),
      planted('the dog', 'each foot in stance'),
      advance('the dog'),
      ('core', 'The legs cycle in a coherent running pattern -- front and hind pairs alternating '
               'with the back flexing in rhythm -- rather than moving at random or in unison.',
       'all four legs swing forward together on every stride, or the legs churn without any '
       'repeating pattern'),
      ('major', 'The dog\'s path follows the ball: it turns as the ball turns and closes on it.',
       'the dog runs hard on a line unrelated to the ball, or the ball changes course and the '
       'chase does not'),
      ('major', 'The ball itself moves ballistically -- rolling, bouncing and slowing -- not '
                'steering itself.',
       'the ball swerves, accelerates or dodges on its own with nothing acting on it'),
      joints('the dog'),
      surface('the dog', 'its coat markings')),
    note="Their standards ask for fluid muscle and joint movement 'responding appropriately' --"
         "form words -- and for the alternating gait with the spine flexing in harmony, which is "
         "real and is kept as the gait-pattern item. The additions are the two couplings a chase "
         "has: the dog's path is slaved to the ball, and the ball is slaved to physics. In "
         "generated clips it is usually the ball that cheats.")

add('rotational-swing', 286,
    'The swing unwinds from the ground up: weight shifts, hips turn, shoulders follow, and the bat '
    'whips through in one arc.',
    S(('core', 'A person is present.'),
      ('core', 'They hold and swing a baseball bat.'),
      ('minor', 'The swing is a full one -- wind-up through contact zone to follow-through.'),
      ('minor', 'The stance reads as a batting stance rather than a casual wave.')),
    P(intact('the person', 'their arms and hands'),
      ('core', 'The bat stays in the hands throughout the swing, and its arc is centred on the '
               'body.',
       'the bat leaves the hands mid-swing and continues its arc, or it swings about a point away '
       'from the batter'),
      ('core', 'The swing is a single continuous arc that speeds up into the hitting zone and '
               'carries through into a follow-through.',
       'the bat stops dead at the moment of contact with nothing hit, or the swing runs backward, '
       'or the bat teleports across part of its arc'),
      ('major', 'The body drives the bat: the hips and torso turn with the swing, and the weight '
                'moves from back foot to front.',
       'the bat whips round at full speed while the body stays perfectly square and still'),
      ('major', 'The feet stay grounded through the swing, pivoting rather than sliding away.',
       'both feet leave the ground during an ordinary swing, or they skate across the ground'),
      joints('the person'),
      ('minor', 'The head stays roughly steady while the body rotates around it.',
       'the head whips around faster than the shoulders')),
    note="Their standards are the hip-then-shoulder sequence, the weight transfer, and a fluid "
         "continuous trajectory. The sequence and the transfer are real rotational mechanics and "
         "are kept in the body-drives-bat item; 'smoothly', 'naturally' and 'fluidly' are not "
         "used. The addition is the arm-body coupling failure to catch: a bat moving at full speed "
         "from arms alone with a frozen torso, which is the standard generated-swing artefact.")

add('flapping-takeoff', 287,
    'The bird beats its wings down to climb, rising with the power strokes until it is away.',
    S(('core', 'A bird is present.'),
      ('core', 'It flaps its wings.'),
      ('core', 'It takes off -- leaves its perch or the ground and climbs.'),
      ('minor', 'The take-off starts from rest rather than mid-flight.')),
    P(intact('the bird', 'its two wings, legs and tail'),
      ('core', 'The climb is powered by the wingbeats: the bird rises while and because the wings '
               'are beating, and both wings beat together.',
       'the bird lifts off and climbs with its wings folded or held still, or the wings beat out '
       'of time with each other'),
      ('core', 'The wings sweep through real strokes -- high to low and back -- rather than '
               'fluttering in place at the wingtips.',
       'the wings vibrate in a blur without sweeping, or they rotate like propellers'),
      ('major', 'The body responds to the strokes: it rises on the downstroke and settles slightly '
                'between strokes, climbing overall.',
       'the bird ascends in a perfectly smooth line with no rhythm related to the beats, or it '
       'hangs motionless in the air between beats'),
      ('major', 'A push-off with the legs, if shown, comes first and the wings take over.',
       'the bird is already high above the perch before either the legs or the wings have moved'),
      joints('the bird'),
      ('minor', 'Feathers and wingtips flex under the strokes, bending most at the downstroke.',
       'the wings stay perfectly rigid boards through hard flapping')),
    note="Both of their standards are sound -- full-range downstrokes generating the lift, and the "
         "body rising with the beats while staying balanced -- and both are used; the "
         "body-wingbeat coupling is the best-observed standard in this category. The additions are "
         "the stroke geometry (sweeping, not buzzing in place) and the wing flexing, which is what "
         "distinguishes a driven aerofoil from a rigid animated plane.")

# ---- Balance and Posture (288-294) -----------------------------------------
add('log-rolling-balance', 288,
    'The log rolls under the runner\'s feet, the feet keep stepping against the roll, and the log '
    'and water answer every step.',
    S(('core', 'A person is present.'),
      ('core', 'A log is floating in water.'),
      ('core', 'The person is on the log, balancing as it moves.'),
      ('minor', 'The log actually rotates under them during the shot.')),
    P(intact('the person', 'their arms and legs'),
      ('core', 'The feet counter the roll: they keep stepping against the direction the log turns, '
               'and the log\'s rotation and the stepping belong together.',
       'the person stands frozen on a log that is plainly rolling, or steps rapidly on a log that '
       'never turns'),
      ('core', 'The log behaves like a floating body: it rolls under the feet, sinks slightly '
               'under the person\'s weight, and bobs as the load shifts.',
       'the log is rock-steady like a fixed platform, or it hangs above the waterline with someone '
       'standing on it'),
      ('major', 'The person keeps correcting -- arms out and working, hips shifting -- rather than '
                'holding one rigid pose.',
       'the person balances on a rolling log in a single locked pose with no adjustment at all'),
      ('major', 'The water answers: ripples spread from the log as it works, and splashes follow '
                'big corrections.',
       'the water stays glassy while the log churns and rolls in it'),
      ('major', 'If the person comes off, they fall -- into the water, with a splash.',
       'the person steps off the log onto the water and stands there, or drifts down slower than '
       'a fall',
       'the person leaves the log during the shot'),
      joints('the person'),
      surface('the person', 'their clothing and hair')),
    note="Their standards describe the corrective motion well -- continuous weight adjustment, "
         "rapid footwork, outstretched active arms -- and for once the wobble is required rather "
         "than forbidden; those are kept, stripped of 'smooth' and 'precise'. The additions are "
         "the two couplings their standards miss: the stepping must be against the log's actual "
         "rotation, and the log must behave like a floating body rather than a fixed prop. "
         "Scenarios 148, 149 and 153 carry the same active-balance physics on other supports.")

add('static-stance-balance', 289,
    'The yogi stands on one leg, weight over the standing foot, holding the pose with small '
    'corrections.',
    S(('core', 'A person is present.'),
      ('core', 'They stand on one leg, in a yoga pose.'),
      ('minor', 'The other leg is visibly lifted -- raised, folded or extended.'),
      ('minor', 'The setting reads as a yoga practice -- mat, studio or deliberate stance.')),
    P(intact('the person', 'their two legs and arms'),
      planted('the person', 'the standing foot'),
      ('core', 'The body is arranged over the standing foot: the visible masses -- trunk, lifted '
               'leg, arms -- balance out around it rather than all hanging off one side.',
       'the person holds a deep sideways lean with everything off to one side of the standing foot '
       'and stays up anyway'),
      ('major', 'Small corrections are visible somewhere -- the ankle working, toes gripping, '
                'arms trimming -- rather than statue stillness.',
       'the person is perfectly frozen on one leg for the whole shot, with not even the ankle '
       'working'),
      ('major', 'If the pose is lost, the lifted foot comes down or a step is taken; the person '
                'does not hang tipped in mid-air.',
       'the person tips well past recovery and hovers there without stepping',
       'the person loses the pose during the shot'),
      joints('the person'),
      ('minor', 'The lifted foot stays off the ground for the held pose.',
       'the lifted foot rests on the ground throughout while the pose is presented as one-legged')),
    note="Their standards ask for a straight vertical line, no excessive wobbling, and a lifted "
         "leg that 'does not sway' -- form and skill, which _policy.json excludes, and partly "
         "wrong besides: many one-legged poses are deliberately not vertical, and micro-sway is "
         "how standing balance works. What is kept is the physics under the pose: the weight must "
         "be organised over the planted foot, the ankle must be alive, and a lost pose must end in "
         "a step or a descent rather than a suspended lean.")

add('beam-balance-attempt', 290,
    'The gymnast tips, fights it with arms and hips, and pulls back over the beam.',
    S(('core', 'A gymnast is present on a narrow beam.'),
      ('core', 'They wobble -- a visible loss of balance happens.'),
      ('core', 'They regain balance rather than falling, as the caption says.'),
      ('minor', 'The beam reads as a narrow gymnastics beam.')),
    P(intact('the gymnast', 'their arms and legs'),
      ('core', 'The recovery is worked for: the wobble is answered by visible counter-motion -- '
               'arms swinging, hips shifting, a knee dropping -- before the body comes back over '
               'the beam.',
       'the gymnast tips well off vertical and simply glides back upright with no counter-motion '
       'anywhere'),
      ('core', 'The supporting foot stays on the beam through the wobble and the recovery.',
       'the gymnast stays up while the supporting foot leaves the beam or slides along it '
       'unweighted'),
      ('major', 'The counter-motion is in the correct sense: arms and free leg swing toward the '
                'falling side to drive the body back the other way.',
       'the arms swing away from the fall and the gymnast recovers anyway'),
      ('major', 'The wobble and recovery are one connected episode -- tip, fight, settle -- not a '
                'jump cut from tipped to upright.',
       'the gymnast is tipped in one moment and serenely upright the next with nothing between'),
      joints('the gymnast'),
      fixed('the beam and its supports')),
    note="This scenario is the useful inverse of the benchmark's usual balance standards: the "
         "caption REQUIRES the wobble, so it goes in SA, and what PC judges is the mechanics of "
         "the recovery -- counter-rotation of arms and free leg toward the fall, which is how "
         "angular momentum is actually traded to bring the trunk back. Their sole standard says "
         "much this, minus the direction, and is used. Scenario 149, 'A gymnast tries to balance "
         "on a beam', is the same situation in category 5 and carries this mechanism; scenario "
         "291 is the routine without the named wobble.")

add('beam-balance-attempt', 291,
    'The gymnast works along the beam, every pose held over it with live, continuous adjustment.',
    S(('core', 'A gymnast is present.'),
      ('core', 'A balance beam is present.'),
      ('core', 'The gymnast performs on it -- moves, poses or turns.'),
      ('minor', 'The performance includes more than standing -- steps, a turn or a pose change.')),
    P(intact('the gymnast', 'their arms and legs'),
      ('core', 'Whatever the pose, the support is on the beam: feet or hands bear on the beam '
               'surface whenever the gymnast is up.',
       'the gymnast holds a position with no support on the beam at all, or supported on empty air '
       'beside it'),
      ('core', 'Balance is continuously worked: arms, hips and ankles keep trimming through moves '
               'and holds.',
       'the gymnast moves through the routine as a rigid figurine with no adjustment anywhere'),
      ('major', 'Feet placed on the beam land on it and stay put while weighted.',
       'a weighted foot lands half off the beam and holds, or slides along the beam under load'),
      ('major', 'Transitions carry momentum believably: a turn or leap is prepared, executed and '
                'caught, not entered from nothing.',
       'the gymnast rotates or leaps from a dead stand with no wind-up and lands with no catch'),
      joints('the gymnast'),
      fixed('the beam and its supports')),
    note="Their standards ask for a steady centred posture 'minimizing wobbling or unnecessary "
         "movements' and smooth controlled transitions -- which, beyond being form, sits oddly "
         "beside their own scenario 290, where the wobble is the event. Balancing on a beam IS "
         "continuous adjustment, so this rubric requires the adjustment and refuses to penalise "
         "wobble. Same mechanism and situation as 149 and 290; what differs is that here the whole "
         "routine, not one recovery, is under judgement.")

add('narrow-path-balance', 292,
    'The cat walks the fence top, paws landing on the rail one after another, tail swinging '
    'against every lean.',
    S(('core', 'A cat is present.'),
      ('core', 'A fence is present.'),
      ('core', 'The cat walks along the top of it.'),
      ('minor', 'The fence top reads as narrow -- a rail or board, not a wide wall.')),
    P(intact('the cat', 'its four legs and tail'),
      planted('the cat', 'each paw in stance'),
      ('core', 'The paws land on the fence top itself, one supporting set at a time, along the '
               'line of the rail.',
       'paws land on empty air beside the rail, or the cat stands with no paw on the fence at all'),
      advance('the cat'),
      ('major', 'The tail is alive: it moves during the walk and swings opposite to leans of the '
                'body.',
       'the tail hangs perfectly rigid and still through the whole traverse'),
      ('major', 'If the cat overbalances, it either drops to the ground or catches the rail; it '
                'does not hang tipped in space.',
       'the cat tips far past the rail and stays there unsupported',
       'the cat overbalances during the shot'),
      joints('the cat'),
      surface('the cat', 'its coat markings')),
    note="Their standards -- precise deliberate paw placement 'without slipping', the tail "
         "actively counterbalancing, and 'no significant wobbles' -- split cleanly: the tail item "
         "is real physics (a cat trades angular momentum with its tail) and is kept with its "
         "direction made explicit; the no-slip and no-wobble clauses are form and are replaced by "
         "the planted-paw and recovery items. Scenario 293 is the same mechanism for a child on a "
         "curb, with arms doing the tail's job.")

add('narrow-path-balance', 293,
    'The child walks the curb line arms out, wobbling and correcting, feet landing one in front of '
    'the other.',
    S(('core', 'A child is present.'),
      ('core', 'They walk along a curb.'),
      ('core', 'They are balancing -- arms out or visibly steadying themselves.'),
      ('minor', 'The curb reads as a raised edge with a drop of at least a step to one side.')),
    P(intact('the child', 'their arms and legs'),
      planted('the child', 'each foot in stance'),
      ('core', 'The feet land on the curb itself, roughly in line, one supporting the body at a '
               'time.',
       'the feet land beside the curb in the road while the child stays up on the line, or both '
       'feet leave the curb mid-walk with the child still supported'),
      advance('the child'),
      ('major', 'The arms work: held out and moving against the body\'s leans rather than pinned '
                'to the sides.',
       'the arms hang motionless at the sides while the body visibly teeters'),
      ('major', 'A lost balance ends on the ground: a step down or a hop off, not a hover.',
       'the child tips beyond recovery and remains suspended over the drop',
       'the child loses the line during the shot'),
      joints('the child'),
      surface('the child', 'their clothing and hair')),
    note="Their standards want a consistently steady arm position, an upright body with 'minimal "
         "swaying or tilting', and careful deliberate steps -- but a child on a curb wobbles, and "
         "the wobble is the game; _policy.json excludes the form reading wholesale. The physics "
         "kept is the arms as a working counterbalance (moving, not just extended -- their 'steady "
         "arm position' actually has it backwards), the feet supporting on the curb line, and the "
         "step-down when balance is lost. Scenario 292 is the same mechanism with a cat's tail.")

add('wire-balance-walking', 294,
    'The walker crosses the rope with continuous correction, the rope sagging and swaying under '
    'every step.',
    S(('core', 'A tightrope walker is present.'),
      ('core', 'A rope is rigged between anchor points.'),
      ('core', 'The walker crosses along it.'),
      ('minor', 'The rope is off the ground with visible slack span between supports.')),
    P(('fatal', 'The walker is supported by the rope: their feet are on it and it takes their '
                'weight.',
       'the walker treads on air beside the rope, or their feet pass through it'),
      ('core', 'The walker keeps correcting -- arms or pole working, hips trimming -- rather than '
               'holding one rigid pose across.',
       'the walker crosses in a single locked pose with no adjustment anywhere'),
      ('core', 'The rope answers the walker: it sags under them, the sag travels with them, and it '
               'sways when they wobble.',
       'the rope stays a rigid straight line under a walker mid-span, or its sag stays put as the '
       'walker moves past it'),
      ('major', 'A lean to one side is answered by a correction back; a lean that just holds is '
                'not survival.',
       'the walker hangs far off to one side of the rope, upright and supported, with nothing '
       'holding the lean'),
      ('major', 'The feet advance along the rope, each placed ahead of the other on the line.',
       'the walker slides along the rope without stepping, or strides while staying at the same '
       'point on it'),
      joints('the walker'),
      ('minor', 'The anchor points hold: the rope stays attached and does not lengthen as the '
                'walker crosses.',
       'an anchor lets go and the walker continues undisturbed, or the rope visibly stretches '
       'longer with every step')),
    note="This is one of the eleven dict-wrapped records; its real standards ask for an upright "
         "spine 'perpendicular to the rope', dynamically adjusting arms, and careful deliberate "
         "foot placement. The arms item is kept as the correction loop; the posture and care items "
         "are form. This scenario duplicates 153, 'A tightrope walker moves across a wire', in "
         "category 5 and carries its mechanism; as there, the rope's own response -- travelling "
         "sag, sway under wobbles -- does the discriminating work, since a rigid rope is the "
         "commonest giveaway.")

# ---- Locomotion Across Terrains (295-301) -----------------------------------
add('soft-ground-gait', 295,
    'The camel strides across the sand on its broad feet, prints appearing behind it, barely '
    'sinking.',
    S(('core', 'A camel is present.'),
      ('core', 'It walks across sandy desert.'),
      ('minor', 'The ground reads as loose sand rather than packed earth.'),
      ('minor', 'The camel travels rather than standing.')),
    P(intact('the camel', 'its four legs, neck and hump'),
      planted('the camel', 'each foot in stance'),
      advance('the camel'),
      ('core', 'The feet interact with the sand: prints or disturbed sand appear where it has '
               'stepped, and only there.',
       'the camel crosses loose sand leaving it perfectly undisturbed, or prints appear where no '
       'foot fell'),
      ('major', 'The camel rides on the surface: its wide feet settle slightly into the sand but '
                'do not punch in deep.',
       'the legs sink shin-deep into the sand at every stride, or the feet hover clear of the '
       'surface'),
      ('major', 'The walk is an orderly repeating gait; camels swing both legs of a side nearly '
                'together, giving the rolling walk.',
       'the legs move in no repeating order, or all four move at once'),
      joints('the camel'),
      surface('the camel', 'its coat and any harness')),
    note="Their sole standard is a smooth consistent gait with appropriate adjustments -- form "
         "words with nothing to fail. The physics_prompt has the real content: weight spread over "
         "wide padded feet to avoid sinking, which becomes the shallow-settling item, paired with "
         "the requirement that the sand nonetheless records the passage. The pacing gait -- "
         "same-side legs swinging near-together, which gives camels their roll -- is the one "
         "species-specific observable and is kept as a major item.")

add('soft-ground-gait', 296,
    'The runner labours across the sand, feet sinking and slipping a little, kicked sand and '
    'prints trailing behind.',
    S(('core', 'A person is present.'),
      ('core', 'They run across a sandy beach.'),
      ('minor', 'The sand reads as soft and dry rather than wet-packed.'),
      ('minor', 'The run covers ground rather than being on the spot.')),
    P(intact('the runner', 'their arms and legs'),
      advance('the runner'),
      ('core', 'Every footfall marks the sand: prints appear at each step, stay behind, and sand '
               'is kicked back with the push-off.',
       'the runner crosses soft sand leaving no prints and disturbing nothing'),
      ('core', 'The feet sink and shift slightly in the soft surface at each step, and the '
               'push-off gives a little.',
       'the feet strike soft dry sand exactly as they would a running track, rigid and clean'),
      ('major', 'The gait shows the cost: shorter or heavier strides and more body work than the '
                'same runner would need on firm ground.',
       'the runner floats across deep soft sand with the effortless stride of a track sprinter'),
      ('major', 'Kicked sand flies backward, opposite the push, and falls.',
       'sand sprays forward ahead of the runner\'s push, or hangs in the air'),
      joints('the runner'),
      surface('the runner', 'their clothing and hair')),
    note="Both of their standards are unusually physical for this category -- effortful mechanics "
         "reflecting the unstable surface, and sand interaction varying with the stride -- and "
         "both are used, stripped of 'naturally'. The sand is the truth-teller here: prints that "
         "persist, grains kicked opposite the push, and the slight give under each foot. Scenario "
         "120 carries the pure sand-transport physics; this rubric shares its mechanism with 295, "
         "the camel on the same footing.")

add('galloping-gait', 297,
    'The horse gallops in repeating strides, hooves striking and leaving together in the gallop '
    'rhythm, grass marking the passage.',
    S(('core', 'A horse is present.'),
      ('core', 'A grassy field is present.'),
      ('core', 'The horse gallops across it.'),
      ('minor', 'The pace reads as a gallop -- airborne phases between strides -- rather than a '
                'walk.')),
    P(intact('the horse', 'its four legs, mane and tail'),
      planted('the horse', 'each hoof in stance'),
      advance('the horse'),
      ('core', 'The gallop has its rhythm: strides repeat, the legs gather and extend together, '
               'and there is a moment with all hooves off the ground within each stride.',
       'the legs churn with no repeating stride, or the horse is always supported with never an '
       'airborne beat at a flat-out gallop'),
      ('major', 'In the airborne beat the horse travels ballistically -- it neither lifts higher '
                'nor speeds up while no hoof touches the ground.',
       'the horse rises or accelerates during the airborne phase of the stride'),
      ('major', 'The grass answers the hooves: it flattens or scatters where they strike, and '
                'only there.',
       'the field is untouched behind a galloping horse, or grass flattens where no hoof fell'),
      joints('the horse'),
      surface('the horse', 'its coat markings')),
    note="Their standards ask for consistent hoof contact visibly compressing the grass -- kept -- "
         "and for leg muscles 'visibly contracting and extending in a fluid and powerful manner', "
         "which on a horse is half-visible at best and is folded into the gait item rather than "
         "asked for directly. The addition is the suspension phase: a gallop contains an airborne "
         "beat, and that beat is ballistic, which is where generated horses most often cheat by "
         "accelerating in mid-air.")

add('incline-climbing-gait', 298,
    'The hiker works up the steep trail leaning into the slope, each step planted and pushed '
    'through.',
    S(('core', 'A person is present.'),
      ('core', 'A steep trail on a mountainside is present.'),
      ('core', 'The person hikes up it.'),
      ('minor', 'Gear or setting reads as hiking -- boots, pack, marked trail or open mountain.')),
    P(intact('the hiker', 'their arms and legs'),
      planted('the hiker', 'each foot in stance'),
      advance('the hiker'),
      ('core', 'The body leans up the slope: on a steep climb the hiker inclines forward relative '
               'to the trail, never backward.',
       'the hiker climbs a steep grade leaning back away from the slope, or stands bolt upright '
       'perpendicular to steep ground'),
      ('major', 'Progress is slower and more worked than on the flat: steps are shorter, the body '
                'rises with each one, and pauses read as effort.',
       'the hiker glides up the steep grade at an easy flat-ground walking pace'),
      ('major', 'Steps adapt to the ground: foot placements follow the rocks and ruts of the '
                'trail rather than ignoring them.',
       'the feet land through rocks and roots as though the trail were smooth pavement'),
      joints('the hiker'),
      surface('the hiker', 'their clothing and pack')),
    note="Their second and third standards -- the forward lean against the incline, and footsteps "
         "adjusting to the terrain -- are real mechanics and are used. Their first wants visibly "
         "contracting leg muscles with 'realistic engagement', unjudgeable through clothing, and "
         "its work is done instead by the pace-and-effort item: climbing costs, and the visible "
         "cost is shorter, slower, higher-stepping strides.")

add('burst-and-pause-scurry', 299,
    'The lizard crosses the rocks in darts and freezes, its body and feet following the ground it '
    'crosses.',
    S(('core', 'A lizard is present.'),
      ('core', 'Rocky ground reads as desert.'),
      ('core', 'The lizard scurries across it.'),
      ('minor', 'The ground is uneven -- rocks and gaps rather than flat pavement.')),
    P(intact('the lizard', 'its four legs and tail'),
      advance('the lizard'),
      ('core', 'The movement comes in bursts: quick darts separated by dead stops, rather than one '
               'continuous glide.',
       'the lizard cruises across the rocks at a single unbroken speed like a toy on wheels'),
      ('core', 'The body works side to side as it runs, the legs sprawling out and the trunk '
               'flexing with the strides.',
       'the lizard slides forward with a rigid straight body and no lateral flexion at speed'),
      ('major', 'The path and posture follow the terrain: it goes over or around rocks, tilting '
                'with the surface.',
       'the lizard runs a level straight line through boulders, or its body stays horizontal on '
       'plainly tilted rock'),
      ('major', 'Feet land on rock surfaces and push from them.',
       'the feet paddle through thin air above the ground while the lizard advances'),
      joints('the lizard'),
      surface('the lizard', 'its skin markings')),
    note="Their standards -- footing and limb positioning adjusting to the terrain, the body "
         "tilting and swaying to keep balance -- are used, with the centre-of-mass phrasing "
         "replaced by its visible form. The additions are the two signatures of lizard locomotion "
         "that generated clips flatten out: motion in bursts with hard stops, and the lateral "
         "undulation of a sprawling gait. A lizard that glides smoothly and steadily is a wheeled "
         "toy with legs painted on.")

add('waddling-gait', 300,
    'The penguin crosses the ice in short quick steps, rocking side to side, flippers out for '
    'trim.',
    S(('core', 'A penguin is present.'),
      ('core', 'Ice or packed snow is underfoot.'),
      ('core', 'The penguin waddles across it.'),
      ('minor', 'The gait reads as a waddle -- upright body, short steps, side-to-side rock.')),
    P(intact('the penguin', 'its two legs and flippers'),
      advance('the penguin'),
      ('core', 'The waddle is the mechanism: short steps with the body rocking onto the support '
               'side at each one, in time with the feet.',
       'the penguin strides long and level like a walking person, or its body rocks out of time '
       'with its steps'),
      ('core', 'The feet respect the ice: steps are short and flat-footed, and any slip reads as '
               'a slip -- caught with flippers and a stagger, or ending on the belly.',
       'the penguin strides across bare ice with confident grippy strides no surface like ice '
       'allows, or it glides standing still across level ice with no push'),
      ('major', 'The flippers are out and working, trimming against the rocking.',
       'the flippers stay clamped to the body through the whole traverse'),
      ('major', 'A fall or slide, if it happens, obeys the slope: the penguin slides down or along '
                'level ice only while momentum lasts.',
       'the penguin toboggans uphill or accelerates along level ice with nothing driving it',
       'the penguin falls or toboggans during the shot'),
      joints('the penguin'),
      surface('the penguin', 'its plumage markings')),
    note="Their standards -- small careful steps with minimal slippage, the sway, the flippers for "
         "balance -- are kept, with one correction of sense: penguins DO slip, and a slip caught "
         "with a stagger or ending in tobogganing is correct behaviour, so what is penalised is "
         "not slipping but impossible grip -- long confident strides on bare ice -- and its "
         "opposite, frictionless standing glide. The rock-in-time-with-steps item is the waddle "
         "itself: the body vaults side to side over each short support.")

add('cliff-climbing-gait', 301,
    'The goat moves up the cliff hold by hold, each hoof set on real rock before the next moves.',
    S(('core', 'A mountain goat is present.'),
      ('core', 'A steep cliff or rock face is present.'),
      ('core', 'The goat climbs it.'),
      ('minor', 'The face reads as genuinely steep -- ledges and holds rather than a walkable '
                'slope.')),
    P(intact('the goat', 'its four legs and body'),
      ('core', 'Every hoof that bears weight is set on rock -- a ledge, knob or crack -- and stays '
               'set while loaded.',
       'a weighted hoof rests on smooth blank face or on air, or slides down the rock while the '
       'goat stands on it'),
      ('core', 'The climb advances hold by hold: one or two hooves move while the others carry, '
               'and the body rises with the placements.',
       'the goat surges up the face with all four hooves moving at once, or ascends while its '
       'hooves stay planted'),
      ('major', 'The body stays close over the rock, hugging the face on steep ground.',
       'the goat leans far out from a near-vertical face and holds there, or stands broadside and '
       'level on it'),
      ('major', 'Dislodged debris, if any, falls down the face.',
       'kicked stones drift upward or hang beside the goat',
       'debris comes loose during the climb'),
      ('major', 'Upward progress happens through the legs pushing on holds, not between contacts.',
       'the goat gains height during a moment when no hoof is set on anything'),
      joints('the goat'),
      surface('the goat', 'its coat markings')),
    note="Their standards -- natural limb flexion, hooves clearly gripping small ledges, the "
         "centre of gravity adjusted for stability -- reduce to the hold-by-hold mechanics once "
         "the form words and the invisible centre of gravity are removed: weighted hooves on real "
         "features, staying put under load, with height gained only through contact. The "
         "close-to-the-face posture is the visible form of their gravity item, and the falling "
         "debris ties the scene to the gravity the climb is defying.")

# ---- Reflexive and Involuntary Motion (302-308) -----------------------------
add('reflex-sneeze', 302,
    'The pepper goes in, the build-up crumples the face, and the sneeze snaps the head and chest '
    'forward in a burst.',
    S(('core', 'A person is present.'),
      ('core', 'They inhale pepper or react to it, as the caption says.'),
      ('core', 'A sneeze or a strong reaction follows.'),
      ('minor', 'The pepper or its source is visible -- a shaker, a cloud, a jar.')),
    P(intact('the person', 'their head, arms and torso'),
      ('core', 'The order is right: exposure first, build-up next, sneeze last.',
       'the sneeze comes before the pepper is anywhere near them, or the build-up follows the '
       'sneeze'),
      ('core', 'The sneeze itself is a burst: a fast convulsive forward snap of head and chest '
               'over a fraction of a second, not a slow bow.',
       'the "sneeze" is a gentle, slow nod stretched over seconds'),
      ('major', 'The eyes close at the moment of the sneeze.',
       'the eyes stay wide open and fixed through the convulsion'),
      ('major', 'The body recovers after: the head comes back up and the posture resettles.',
       'the person stays frozen mid-sneeze for the rest of the shot'),
      joints('the person'),
      ('minor', 'The face works before the sneeze -- crumpling, nostrils flaring, breath catching.',
       'the face is perfectly serene until the instant of the convulsion')),
    note="Their standards -- rapid chest and diaphragm contraction, the sudden uncontrollable "
         "forward motion, the involuntary facial sequence -- are essentially right and are used, "
         "recast onto what is visible: the diaphragm itself cannot be seen, but its burst can. The "
         "items that discriminate are order and tempo, because generated reflexes fail by being "
         "leisurely: a sneeze is one of the fastest whole-body movements a person makes, and a "
         "slow graceful version is wrong even when every pose along the way is plausible.")

add('withdrawal-reflex', 303,
    'The hand touches the hot surface and snatches back at once -- faster than any deliberate '
    'move in the scene.',
    S(('core', 'A person is present.'),
      ('core', 'A surface that reads as hot is present -- a stove, pan, kettle or flame-heated '
               'metal.'),
      ('core', 'The person touches it and reacts.'),
      ('minor', 'The touch is inadvertent or exploratory rather than a deliberate press.')),
    P(intact('the person', 'their arms and hands'),
      ('core', 'The withdrawal follows the contact, and follows it almost instantly.',
       'the hand pulls back before anything is touched, or it rests on the hot surface for long '
       'seconds before reacting'),
      ('core', 'The snatch is away from the surface, and it is the fastest thing the person does '
               'in the shot.',
       'the hand withdraws toward or along the hot surface, or it leaves as slowly as it '
       'approached'),
      ('major', 'The rest of the body follows the reflex: a flinch, a step back, the other hand '
                'coming over.',
       'the arm snaps back while the face and body carry on perfectly serene, as though the arm '
       'belonged to someone else'),
      ('major', 'The hand does not return casually to the same hot spot moments later.',
       'having snatched back, the person lays the hand flat on the same surface again at once'),
      joints('the person'),
      ('minor', 'The hot surface stays hot-looking and consistent -- steam, glow or heat shimmer '
                'do not switch off when touched.',
       'the visible signs of heat vanish the moment the hand arrives')),
    note="Both of their standards -- near-instantaneous retraction, and a coordinated fast "
         "withdrawal sequence -- are right and are used. The additions give the reflex its "
         "signature against ordinary movement: it is the fastest motion in the shot and it is "
         "directed away, and the body is not indifferent to it. The no-return item catches the "
         "looped or context-blind clip in which the burned hand goes straight back.")

add('startle-response', 304,
    'Something startles the cat and the whole posture fires at once -- back arched, tail flicked, '
    'eyes wide.',
    S(('core', 'A cat is present.'),
      ('core', 'It reacts suddenly, as the caption says.'),
      ('minor', 'The startling cause is visible or audible in the scene -- a movement, an object, '
                'another animal.'),
      ('minor', 'The cat is calm before the startle.')),
    P(intact('the cat', 'its four legs, tail and ears'),
      ('core', 'The reaction follows the disturbance and comes at once, not seconds later.',
       'the cat startles before anything happens, or long after the disturbance has passed'),
      ('core', 'The onset is sudden: the posture changes in a fraction of a second, then holds or '
               'decays.',
       'the cat eases into its startled posture as slowly as a stretch'),
      ('major', 'The startle elements come together as one event -- arch, tail, eyes and ears in '
                'the same instant -- rather than as a leisurely sequence.',
       'the cat arches, then some moments later flicks its tail, then later still widens its eyes, '
       'as separate acts'),
      ('major', 'The reaction is oriented: the cat faces, jumps away from, or fixes on the '
                'disturbance.',
       'the cat startles in a direction that has nothing to do with where the disturbance is'),
      joints('the cat'),
      ('minor', 'The startle decays: the cat settles, relaxes or flees, rather than holding the '
                'peak pose indefinitely.',
       'the cat stands frozen at maximum arch for the rest of the shot')),
    note="Their standards list the right elements -- the sharp tail flick, the rapid arch, the "
         "widened eyes held briefly -- and are used with their tempo made explicit: a startle is "
         "involuntary and therefore simultaneous and fast, so the elements must fire together, "
         "at the disturbance, and then decay. Generated startles fail as slow sequences of "
         "poses; the simultaneity item is aimed exactly there.")

add('protective-reflex', 305,
    'The ball comes in and the guard goes up before it arrives -- arms raised, head away, body '
    'leaning back.',
    S(('core', 'A person is present.'),
      ('core', 'A ball is thrown at them.'),
      ('core', 'They shield their face -- arms up, head turning away.'),
      ('minor', 'The thrower or the throw is visible, not just a ball from nowhere.')),
    P(intact('the person', 'their arms, hands and head'),
      ('core', 'The shielding is timed to the throw: it starts after the threat is visible and is '
               'up before or as the ball arrives.',
       'the guard goes up before any throw exists, or only after the ball has already struck or '
       'passed'),
      ('core', 'The ball flies a real path: a fast, slightly dropping line from the thrower toward '
               'the person.',
       'the ball floats over slowly, swerves in flight, or hangs in the air in front of the guard'),
      ('major', 'The protective set is coherent: arms rise toward the line of flight, the head '
                'turns or tucks away from it, the body gives backward.',
       'the arms rise away from the ball\'s line while the face stays presented to it'),
      ('major', 'What happens at arrival follows through: a blocked ball rebounds off the arms, a '
                'dodged ball passes and lands beyond.',
       'the ball reaches the raised arms and simply vanishes, or stops dead in the air at the '
       'guard'),
      joints('the person'),
      ('minor', 'The guard relaxes after the ball is dealt with.',
       'the person holds the full flinch long after the ball is gone')),
    note="Their standards describe the composite well -- simultaneous arm raise, head tilt, "
         "finger spread, lean back, synchronised to the stimulus -- and the synchronisation is "
         "the physics: a protective reflex is anticipatory, launched off the sight of the throw, "
         "so it must land between the release and the arrival. The finger spread is form-level "
         "detail and is not required. The ball's own flight and its arrival consequences are the "
         "additions, since the object half of the event is what generated clips most often fudge.")

add('shake-dry', 306,
    'The shake runs down the wet dog from head to tail, and the water leaves it in flung arcs.',
    S(('core', 'A dog is present and it is wet.'),
      ('core', 'It shakes its body.'),
      ('minor', 'Water is visible on or around the dog -- soaked coat, drips, a puddle or shore.'),
      ('minor', 'The shake is the vigorous whole-body kind, not a shiver.')),
    P(intact('the dog', 'its four legs, tail and body'),
      ('core', 'The shake is a rapid alternating twist of the body about its length, fast enough '
               'to blur the fur.',
       'the dog sways gently side to side at walking tempo and is somehow dry'),
      ('core', 'Water leaves the dog because of the shake: droplets come off during it, flung '
               'outward from the twisting body, and travel away before falling.',
       'the coat goes from soaked to dry with no water seen leaving, or droplets rise straight up '
       'and hover, or water sprays while the dog is still'),
      ('major', 'The shake travels: it starts at the head and runs back down the body toward the '
                'tail.',
       'the whole dog twists as one rigid piece from the first instant'),
      ('major', 'The dog ends visibly drier -- coat spiked and lifted -- and the water has gone '
                'somewhere: mist, spray marks, drops around it.',
       'the dog is exactly as soaked after a hard shake as before, with dry ground all round'),
      joints('the dog'),
      ('minor', 'The paws stay planted while the trunk does the twisting.',
       'the dog\'s feet skate around beneath it as it shakes')),
    note="Their second standard asks for 'noticeable centrifugal force', which is not a thing a "
         "clip can show -- what is visible is its consequence, droplets leaving tangentially and "
         "outward, and that is what the water item requires. Their 'spontaneous and natural' is "
         "form. The travelling wave -- head first, rippling back to the tail -- is the "
         "signature of a real dog shake and is the item generated clips fail, twisting the whole "
         "dog as one piece.")

add('stretch-and-yawn', 307,
    'The stretch reaches up, the yawn opens wide, and the whole body lets down into ease '
    'afterwards.',
    S(('core', 'A person is present.'),
      ('core', 'They yawn.'),
      ('core', 'They stretch -- arms up or out, back arching.'),
      ('minor', 'The setting reads as morning or waking -- bed, bedroom, dressing gown, low light.')),
    P(intact('the person', 'their arms and torso'),
      ('core', 'The stretch is one connected act: the arms rise, the back extends with them, they '
               'hold briefly at the top and come down together.',
       'the arms pump up and down disconnected from the torso, or the body arches with the arms '
       'hanging dead'),
      ('core', 'The yawn opens and closes as a single slow cycle -- wide open, held, released -- '
               'with the face going with it.',
       'the mouth snaps open and shut like speech, or gapes open frozen for the whole shot'),
      ('major', 'The afterphase reads: after stretch and yawn the posture settles somewhere '
                'looser than before.',
       'the person remains at full rigid extension after the stretch is plainly over'),
      ('major', 'Stretch and yawn share the episode plausibly -- overlapping or in sequence -- '
                'rather than machine-gunning in repetition.',
       'the person yawns and re-stretches identically over and over in a visible loop'),
      joints('the person'),
      ('minor', 'The eyes narrow or close during the yawn.',
       'the eyes stay fixed wide open through a full yawn')),
    note="Their standards -- shoulder and chest motion synchronised with the stretch, the wide "
         "yawn with facial relaxation after, the posture shift from arched to relaxed -- are all "
         "used; this record's standards are genuinely about the event rather than its polish. The "
         "one addition is the anti-loop item: an involuntary morning stretch is a one-off "
         "episode with an afterphase, and a clip that cycles it identically betrays itself.")

add('escape-response', 308,
    'The disturbance lands and the fish is gone in a flick -- a sharp body-bend and a dart away.',
    S(('core', 'A fish is present, in water.'),
      ('core', 'A sudden disturbance happens -- a splash, a tap, a shadow, a lunge.'),
      ('core', 'The fish reacts.'),
      ('minor', 'The fish is calm or idling before the disturbance.')),
    P(intact('the fish', 'its fins, tail and body'),
      ('core', 'The reaction follows the disturbance immediately: within the moment, not after a '
               'thoughtful pause.',
       'the fish darts away before anything disturbs it, or ponders for seconds first'),
      ('core', 'The escape starts with a sharp body-bend -- the fish snaps into a curve and '
               'straightens into the dart.',
       'the fish accelerates away perfectly straight and rigid, like a pulled toy'),
      ('core', 'The dart is directed away from the disturbance.',
       'the fish darts straight at the thing that startled it, or in a random unrelated direction '
       'while plainly fleeing'),
      ('major', 'The burst is brief and decays: a fast start, then coasting or normal swimming '
                'further away.',
       'the fish holds the same explosive speed indefinitely across the whole tank or pool'),
      ('major', 'The water shows the burst: a swirl or puff of disturbed water where the fish '
                'fired off.',
       'the fish vanishes from its spot leaving the water perfectly undisturbed'),
      joints('the fish'),
      surface('the fish', 'its markings')),
    note="Their standards -- instant reaction with rapid body contraction, a swift dart clearly "
         "directed away -- are right and are used. The contraction is made specific: the "
         "startle response of a fish is the C-start, a sharp bend and unbend, and its visible "
         "signature (curved body at onset, swirl left in the water) separates a real escape from "
         "a fish that is simply translated away at speed, which is how generated clips do it.")

# ---- Coordination and Fine Motor Skills (309-315) ---------------------------
add('manipulation-causality', 309,
    'The fingers work the laces and the laces answer: loops form where they are made, and a knot '
    'is left behind.',
    S(('core', 'A person is present.'),
      ('core', 'Shoelaces on a shoe are present.'),
      ('core', 'The person ties them.'),
      ('minor', 'The tying runs from loose laces toward a finished knot within the shot.')),
    P(intact('the person', 'their hands and fingers'),
      ('core', 'The laces move only when and where the fingers act on them, and follow the pulls '
               'they are given.',
       'laces loop and thread themselves while the hands hover, or move against the pull applied '
       'to them'),
      ('core', 'The laces persist: two laces stay two laces, keep their length and colour, and do '
               'not merge, vanish or sprout new ends.',
       'the laces fuse into one strand, change count between shots, or pass through each other'),
      ('major', 'The state advances: crossings and loops, once made, stay made until deliberately '
                'changed, and the lace ends shorten as the knot takes them up.',
       'a formed loop silently dissolves and the tying starts over, or the knot grows while the '
       'free ends stay the same length'),
      ('major', 'The end state follows from the actions: after the pulls, a knot or bow is there, '
                'holding.',
       'the hands finish and withdraw and the laces lie loose with no knot, or a bow appears that '
       'the shown moves never constructed'),
      joints('the person'),
      ('minor', 'The shoe stays on the foot or in place while it is worked on.',
       'the shoe drifts about under the busy hands')),
    note="Their standards -- fluid well-timed movements 'free from unnecessary pauses or jerks', "
         "precise gripping 'without fumbling or needing readjustments' -- are dexterity, and a "
         "person who fumbles a lace is perfectly physical; _policy.json excludes all of it. What "
         "the rubric asks instead is causality and object permanence: laces move only under the "
         "fingers, stay two laces, hold their made state, and end in the knot the moves actually "
         "constructed. Those are the terms on which generated hands actually fail.")

add('manipulation-causality', 310,
    'The thread meets the needle eye and either goes through or misses -- what shows is contact, '
    'not magic.',
    S(('core', 'A person is present.'),
      ('core', 'A needle and thread are present.'),
      ('core', 'The person works at threading the needle.'),
      ('minor', 'The eye of the needle and the thread end are visible closely enough to follow.')),
    P(intact('the person', 'their hands and fingers'),
      ('core', 'The thread is moved by the fingers that hold it, toward the eye, and passes '
               'through the eye or misses it -- never through the needle\'s metal.',
       'the thread penetrates the side of the needle, or arrives threaded with no approach shown'),
      ('core', 'Thread and needle persist: one thread of constant thickness and colour, one '
               'needle, neither morphing or duplicating.',
       'the thread changes thickness or colour at the eye, splits into two, or a second needle '
       'appears'),
      ('major', 'Success has its state: once through, the thread hangs in the eye and follows the '
                'needle when it moves.',
       'the thread is through in one frame and unthreaded in the next with no hand near it, or '
       'the needle moves away and leaves the threaded thread hanging in air'),
      ('major', 'The thread end behaves like thread: floppy, drooping under gravity, steadied '
                'between fingers -- not a self-guiding rigid wire.',
       'the free thread end stands out rigid and steers itself into the eye'),
      joints('the person'),
      ('minor', 'Misses are allowed and look like misses: the thread buckles or slides off the '
                'needle, and the person re-tries.',
       'every approach snaps into the eye as though magnetised, however wide of it the thread '
       'starts')),
    note="Their standards want success 'without excessive retries or fumbling' with subtle steady "
         "adjustments -- but retries are what threading a needle looks like, and penalising them "
         "penalises realism; _policy.json excludes the skill reading. The physics is in the "
         "micro-scale object behaviour: limp thread that droops and buckles, passage through the "
         "eye and not the metal, and a threaded state that persists and travels with the needle. "
         "The magnetised-thread failure named in the last item is the characteristic generated "
         "artefact.")

add('keyboard-causality', 311,
    'The hands range over the keyboard fast, and the keys go down under the fingers that strike '
    'them.',
    S(('core', 'A pianist is present.'),
      ('core', 'A piano or keyboard is present.'),
      ('core', 'They play, fast -- rapid passages rather than single slow notes.'),
      ('minor', 'The hands and keys are visible together somewhere in the shot.')),
    P(intact('the pianist', 'their hands and ten fingers'),
      ('core', 'Keys move when and where fingers strike them: pressed keys go down under contact '
               'and come back up on release.',
       'keys ripple down with no finger near them, or fingers strike and the keys never move'),
      ('core', 'The hands travel to reach what they play: passages up or down the keyboard carry '
               'the hands and arms along.',
       'notes sound from ends of the keyboard the hands never approach, or the hands teleport '
       'between positions'),
      ('major', 'Fingers strike keys, not gaps, and neighbouring keys stay up when not struck.',
       'fingers press the cracks between keys to full effect, or whole clusters of keys sink '
       'under one finger'),
      ('major', 'The two hands are independent but coordinated bodies: they cross or share the '
                'keyboard without merging.',
       'the hands pass through each other at a crossing, or fuse where they meet'),
      joints('the pianist'),
      ('minor', 'The pianist\'s body works with the playing: weight shifts and the arms carry the '
                'hands, rather than hands fluttering off a frozen statue.',
       'the torso and arms are rigidly still while the fingers alone blur at speed')),
    note="Their standards -- finger movements matching the piece's speed and rhythm, stable "
         "posture -- lean on sound, which video judging cannot use, and on form. What is "
         "judgeable is the contact causality between finger and key, the travel of hands to the "
         "registers being played, and the integrity of two fast-moving hands sharing a keyboard "
         "-- the standard failure sites of generated piano footage. Posture appears only "
         "inverted: a statue with blurred fingers fails, not an expressive sway.")

add('stack-building', 312,
    'The child sets block on block; each one rests where it is put, and the tower stands or '
    'topples honestly.',
    S(('core', 'A child is present.'),
      ('core', 'Small blocks are present.'),
      ('core', 'The child stacks them into a tower.'),
      ('minor', 'The tower grows over the shot -- more blocks at the end than the start.')),
    P(('fatal', 'Blocks are solid and separate: they rest on each other without merging, '
                'overlapping or hanging in air.',
       'a block floats unsupported, sinks into the one beneath, or two blocks fuse into one'),
      ('core', 'Each block moves only in the child\'s grasp, and once placed it stays where it was '
               'put unless disturbed.',
       'blocks glide into position on their own, or placed blocks drift and straighten themselves '
       'after the hand leaves'),
      ('core', 'Support is honest: each block rests substantially on what is under it, and a '
               'block set far off the edge falls.',
       'a block balances on a corner overlap of almost nothing, or a stack stands with a large '
       'sideways offset no base could carry'),
      ('major', 'If the tower topples it topples as physics: tipping past its base, blocks '
                'separating and falling down and outward, and staying fallen.',
       'the tower collapses upward or sideways into the air, or the fallen blocks reassemble',
       'the tower topples during the shot'),
      ('major', 'The count is conserved: blocks appear in the tower only from the child\'s hand '
                'and the pile.',
       'the tower gains storeys with no block placed, or blocks vanish from mid-tower while the '
       'stack stands'),
      joints('the child'),
      ('minor', 'The blocks keep their colours and printed faces as they are handled.',
       'blocks change colour or pattern between pick-up and placement')),
    note="Their standards -- each block placed with its centre of mass over the base, the "
         "structure stable with minimum chance of toppling -- name an invisible quantity and a "
         "probability, so both are recast into their visible halves: substantial resting overlap, "
         "and honest consequences when the overlap is not there. A wobbly tower or a toppling one "
         "is not a failure; a tower that cheats -- floating blocks, self-straightening rows, "
         "impossible overhangs -- is. The count-conservation item is the fine-motor version of "
         "the material-conservation items in the clay and dough rubrics (228, 230).")

add('cutting-causality', 313,
    'The knife rises and falls along the vegetable, and slices exist exactly where the blade has '
    'been.',
    S(('core', 'A chef is present.'),
      ('core', 'Vegetables and a knife are present.'),
      ('core', 'The chef slices the vegetables.'),
      ('minor', 'The slicing is quick and repeated, as the caption says.')),
    P(intact('the chef', 'their hands and fingers'),
      ('core', 'Cuts happen only where and when the blade passes through: each downstroke through '
               'the vegetable makes one new slice, and no cut appears elsewhere.',
       'the vegetable falls into slices ahead of the knife, or a stroke passes through and leaves '
       'it whole'),
      ('core', 'The vegetable is consumed as it is cut: the uncut part shortens as the slices '
               'accumulate, and the slices stay cut.',
       'slices pile up while the vegetable stays full length, or cut slices heal back onto it'),
      ('major', 'The knife advances along the vegetable between strokes, matching where the next '
                'slice falls.',
       'the blade chops repeatedly in one place while even slices appear along the whole length'),
      ('major', 'The guiding hand holds the vegetable and retreats ahead of the blade.',
       'the blade strokes pass through the guiding fingers, which are unharmed and unmoved'),
      ('major', 'The slices behave as loose pieces: they lean, topple and slide as they come off '
                'the knife.',
       'the cut slices stand rigidly in formation as though still one body, glued upright'),
      joints('the chef'),
      ('minor', "The cut faces of the slices show the vegetable's interior, distinct from its "
                'skin.',
       'every face of every slice shows outer skin, including the fresh cuts')),
    note="Their standards -- smooth consistent motion with no sudden jerks or pauses, "
         "synchronised wrist and fingers -- are entirely form and are not used; a hesitant cook "
         "slicing raggedly breaks no physics. What carries the scenario is cut-causality: one "
         "stroke, one slice, at the blade's position; conservation between the shrinking "
         "vegetable and the growing pile; and the guiding hand staying out of the blade's path, "
         "which generated kitchens routinely violate by passing steel through fingers.")

add('manipulation-causality', 314,
    'The brush touches down and leaves paint exactly where it moved, stroke by stroke, and the '
    'strokes stay.',
    S(('core', 'A person is present.'),
      ('core', 'A canvas, a brush and paint are present.'),
      ('core', 'The person paints fine details on the canvas.'),
      ('minor', 'The work is close and small -- detail work rather than broad washes.')),
    P(intact('the person', 'their hands and fingers'),
      ('core', 'Marks appear only where the loaded brush touches, while it touches, and follow '
               'its path.',
       'strokes draw themselves ahead of or away from the brush, or the brush moves on the canvas '
       'and leaves nothing'),
      ('core', 'The work accumulates: strokes persist, and later strokes add to or cover earlier '
               'ones rather than earlier ones vanishing.',
       'finished detail dissolves off the canvas, or the painting jumps to a more complete state '
       'no strokes produced'),
      ('major', 'Paint is carried: the brush is loaded from palette or pot, thins as it paints, '
                'and marks come only from a loaded brush.',
       'the brush paints on endlessly without ever taking up paint, in colours it was never '
       'dipped in'),
      ('major', 'The line follows the tool: broad presses give broader marks, the lifted brush '
                'gives none.',
       'a hovering brush lays down lines, or heavy and light touches leave identical hairlines'),
      joints('the person'),
      ('minor', 'The canvas holds still against the working brush.',
       'the canvas slides around under each stroke with nothing steadying it')),
    note="Their standards -- fluid transitions, uniform pressure and direction, steady precision "
         "-- are craft, and an unsteady painter is physically unremarkable; none is used. The "
         "physics is deposition: pigment transfers at contact, along the path, from a brush that "
         "must be loaded and empties as it works, onto a surface where marks persist. The "
         "loaded-brush conservation item plays the role the paint-spread items played in scenario "
         "140, and the appearing-artwork failure named in the second core item is the "
         "characteristic generated-painting artefact.")

add('manipulation-causality', 315,
    'The bird works twig by twig: pick up, carry, place, and the nest keeps every placement.',
    S(('core', 'A bird is present.'),
      ('core', 'A nest and twigs are present.'),
      ('core', 'The bird arranges twigs in the nest.'),
      ('minor', 'At least one full cycle shows -- a twig taken up, carried and placed.')),
    P(intact('the bird', 'its beak, wings and legs'),
      ('core', 'Twigs move only in the bird\'s beak (or feet), and go where the bird puts them.',
       'twigs fly to the nest or weave themselves in while the bird watches, or a carried twig '
       'travels independently of the beak holding it'),
      ('core', 'Placements persist: a twig worked into the nest stays as placed, and the nest '
               'grows only by what is brought.',
       'placed twigs vanish or rearrange themselves between moments, or the nest visibly grows '
       'while the bird brings nothing'),
      ('major', 'A carried twig behaves like a rigid stick: it swings with the head as one piece '
                'and pokes against things it meets.',
       'the carried twig bends like rubber around obstacles, or passes through the nest rim'),
      ('major', 'Loose twigs obey gravity: one dropped or dislodged falls out and down.',
       'a dropped twig hovers beside the nest, or settles upward into place'),
      joints('the bird'),
      ('minor', 'The nest and its supporting branch move only as the bird\'s weight and work '
                'disturb them.',
       'the nest rocks and swings with no bird touching it, or stays rigid as stone while the '
       'bird lands and works')),
    note="Their standards -- precise deliberate beak movements with clear coordination, twigs "
         "positioned securely 'without unnecessary adjustments' -- read fussiness as failure, but "
         "a bird fidgeting a twig into place five times is exactly what nest-building looks like; "
         "the skill reading is excluded. The rubric keeps the causal chain instead: twigs move "
         "only by beak, behave as rigid sticks, fall when dropped, and stay where worked in. It "
         "closes the block the way 309 opened it, with object permanence doing the judging.")
