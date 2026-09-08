# phyworldbench 141-175: Rigid Body Dynamics.
# Same authoring flow as the earlier blocks: items come from the caption plus first-principles
# physics, then physics_prompt and key_standards are diffed for coverage; conflicts are followed
# on the side of physics and recorded in `note`. Cross-check against KS[i], not against
# SRC[i]['key_standards'].
#
# Three things recur across this category and account for most of the divergences recorded below.
#
# First, several standards are tautologies -- 'The screw turn clockwise or counterclockwise', 'The
# key is rotating', 'The bolt rotates around this axis', 'The branches is cut into pieces'. Any
# clip showing the named object doing the named thing at all satisfies them, so they carry no
# discriminating power and the items here are written from scratch.
#
# Second, the Balance and Stability block asks repeatedly for an absence of wobble -- 'without any
# noticeable wobbles', 'minimal deviation from vertical alignment', 'no abrupt or jerky actions',
# 'without any falls'. That is backwards for every one of these scenarios. Balancing on a
# unicycle, a beam or a wire is active stabilisation of an unstable equilibrium, so continuous
# corrective motion is the physics and a perfectly rigid upright figure is the wrong answer.
# _policy.json's not_penalized list also excludes skill and form outright. Where a standard
# consists only of that, it is not used.
#
# Third, three standards assert something about the centre of mass (151, 154, 161). The centre of
# mass is not a visible feature, so those are restated as the observable consequence -- which end
# goes down, which legs are in contact, which way the body topples -- rather than being asked for
# directly.


def cons(o):
    return ('fatal',
            f'{o[0].upper()}{o[1:]} keeps its own shape and identity for the whole shot, and it '
            f'does not pass through any solid surface.',
            f'{o} turns into a different object, passes through something solid, or disappears '
            f'and re-appears')


def rigid(o):
    return ('core', f'{o[0].upper()}{o[1:]} stays rigid: it moves as one piece without bending, '
                    f'stretching or sagging.',
            f'{o} bends, stretches or flexes like something soft')


def keeps(o, what):
    return ('core', f'{what[0].upper()}{what[1:]} stays once it has been made: {o} does not spring '
                    f'back to how it was.',
            f'{o} returns to its original undamaged shape on its own')


def unmarked(hard, soft):
    return ('major', f'{hard[0].upper()}{hard[1:]} comes through unmarked; it is {soft} that gives '
                     f'way.',
            f'{hard} dents, buckles or deforms instead of {soft}')


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


# ---- Rotation and Torque (141-147) ---------------------------------------
add('torque-spin-up', 141,
    'A pushed roundabout speeds up while it is being pushed and coasts to a stop afterwards.',
    S(('core', 'A roundabout is present.'),
      ('core', 'A child pushes it.'),
      ('core', 'The roundabout turns.'),
      ('minor', 'The roundabout is still or barely moving before the push.')),
    P(('fatal', 'The roundabout turns about its own central post and stays on it.',
       'the roundabout lifts off its mounting, turns about a point off to one side, or drifts away '
       'across the ground while spinning'),
      ('core', 'It speeds up while the child is pushing.',
       'it is already at full speed at the first touch and holds it, or it slows down while the '
       'child is plainly still pushing'),
      ('core', 'It turns the way the child pushes it.',
       'it turns against the direction of the push'),
      ('major', 'It keeps turning after the child stops pushing, and slows gradually rather than '
                'stopping dead.',
       'it halts the instant contact is lost, or it holds full speed indefinitely with nobody '
       'touching it'),
      ('major', 'The whole platform turns as one, at the same rate all the way round.',
       'parts of the roundabout turn at different rates, or the rim turns while the centre stays '
       'still'),
      ('minor', 'The outer edge covers more ground than the middle in the same time.',
       'the middle sweeps round faster than the rim'),
      ('minor', 'The child stays on the ground, or moves with the platform if they are on it.',
       'the child stands on the turning platform and stays facing one fixed direction as it spins'),
      fixed('the ground and the frame')),
    note="Their standards are sound as far as they go -- angular acceleration, and rotation "
         "direction matching the applied torque. What they omit is what happens after the push "
         "stops, which is where the clips go wrong: a roundabout has real rotational inertia and "
         "coasts for a long time, so a platform that stops the moment the hands come off, or that "
         "spins on for ever at full speed, are both failures their standards do not catch.")

add('spinning-top', 142,
    'A top spins upright on the table and gradually loses speed.',
    S(('core', 'A spinning top is present.'),
      ('core', 'It spins on a table.'),
      ('minor', 'The top stays up on its point rather than lying over for the whole shot.'),
      ('minor', 'The surface reads as a table rather than the floor.')),
    P(cons('the top'),
      ('core', 'The top loses spin over the shot, since friction at the point and against the air '
               'takes energy out of it.',
       'the top holds exactly one rate of spin for the whole shot, or it spins up faster on its own '
       'with nothing driving it'),
      ('core', 'The top stays balanced on its point while it is spinning fast.',
       'the top spins fast while lying on its side, or it hovers with its point clear of the table'),
      ('major', 'It keeps turning the same way throughout.',
       'the direction of spin reverses on its own'),
      ('major', 'As it slows it starts to lean and wander, rather than staying perfectly vertical '
                'to the last.',
       'the top stays exactly upright and in one spot right down to standing still'),
      ('minor', "The top's markings turn with it rather than staying still.",
       'the pattern on the top holds a fixed orientation while the body spins under it'),
      fixed('the table')),
    note="Their sole standard is the gradual slowdown, which is right and is core here. The "
         "addition is the loss of stability as it slows: a fast top is held upright by its own "
         "spin, so it must begin to lean and wobble as that spin goes, and a top that stays "
         "perfectly vertical until it stops dead has the mechanism missing. Scenarios 26 and 87 are "
         "the same physical situation in categories 1 and 3 and carry this mechanism; 87 is judged "
         "for the decay and this one for the balance that goes with it.")

add('wind-driven-rotation', 143,
    'Wind turns the windmill blades, and the rate they turn follows the strength of the wind.',
    S(('core', 'A windmill is present.'),
      ('core', 'Its blades turn.'),
      ('minor', 'There is a sign of wind beyond the blades themselves -- moving grass, cloud or '
                'cloth.'),
      ('minor', 'The structure reads as a windmill rather than a fan or a turbine hall.')),
    P(('fatal', 'The blades turn about their hub and stay attached to it.',
       'a blade comes off and keeps turning, or the assembly turns about a point away from the hub'),
      ('core', 'All the blades turn together, as one assembly, at the same rate.',
       'blades move at different rates, change their spacing, or turn in opposite directions'),
      ('core', 'The blades turn in the plane they are set in, face-on to the wind.',
       'the blades turn edge-on to the airflow, or they swing about like a weather vane rather than '
       'turning in their own plane'),
      ('major', 'The blades keep one direction of rotation while the wind holds its direction.',
       'the rotation reverses while the wind is plainly still coming from the same side'),
      ('major', 'The turning slows if the wind drops and picks up if it strengthens.',
       'the blades hold exactly one rate through a visible lull or gust, or they turn steadily on '
       'in still air'),
      marks('the blades', 'their sails and slats'),
      fixed('the tower and its base')),
    note="Their sole standard, 'the blades rotate in a steady speed', is not usable as written: "
         "real wind is gusty, so a correct clip shows the rate rising and falling with it, and "
         "requiring an exactly constant rate would fail that clip while passing a blade assembly "
         "spinning on in dead air. The item here couples the rate to the visible wind instead. "
         "Scenario 24, 'A steady wind blows at a windmill', is the same physical situation in the "
         "Rotational Motion subcategory of category 1 and carries this mechanism; 24 is the steady "
         "case, where the constant rate their standard asks for is the right answer.")

add('helical-advance', 144,
    'A turned screw threads its way down into the wood, going deeper the more it is turned.',
    S(('core', 'A screwdriver and a screw are present.'),
      ('core', 'The screwdriver turns the screw.'),
      ('core', 'The screw goes into the wood.'),
      ('minor', 'The screw starts proud of the surface rather than already being driven home.')),
    P(('fatal', 'The screw goes deeper into the wood, not out of it, while it is being driven.',
       'the screw backs out of the wood while the driver turns it in the driving direction, or it '
       'sinks in with the driver plainly not turning'),
      ('core', 'Turning and depth go together: the screw advances only while it turns, and how far '
               'it goes tracks how much it has been turned.',
       'the screw spins in place without going any deeper, or it slides in without turning at all'),
      ('core', 'The screwdriver tip stays in the screw head and the two turn together.',
       'the driver turns while the screw stays still, or the tip passes through the head'),
      ('major', 'The screw turns about its own long axis, staying in line with the driver.',
       'the screw wobbles about some other axis, or it tips out of line with the shaft while being '
       'driven'),
      ('major', 'The wood stays still while the screw turns in it.',
       'the wood turns along with the screw'),
      ('minor', 'The wood around the hole shows the screw going in -- displaced fibres, a raised '
                'lip or shavings.',
       'the screw enters a surface that stays perfectly smooth and unmarked around it'),
      unmarked('the screw', 'the wood')),
    note="Their first standard, 'The screw turn clockwise or counterclockwise', is a tautology: "
         "every rotation satisfies it. Their second, that the alignment stays consistent, is the "
         "one usable half and is here. Everything else is written from scratch. The item that does "
         "the work is the coupling between rotation and depth -- a screw is a helical constraint, so "
         "turning and advancing are the same motion -- and the commonest wrong answer, a screw "
         "spinning merrily in place or sinking in without turning, satisfies both of their "
         "standards.")

add('free-spin-decay', 145,
    'A pushed pedal spins the wheel up, and the wheel then coasts and slowly loses speed.',
    S(('core', 'A bicycle is present.'),
      ('core', 'A person steps on the pedal.'),
      ('core', 'A wheel turns.'),
      ('minor', 'The wheel is still or nearly still before the pedal is pushed.')),
    P(('fatal', 'The wheel turns about its own hub and stays on it.',
       'the wheel leaves the frame, or it turns about a point off to one side of the hub'),
      ('core', 'The wheel speeds up while the pedal is being driven.',
       'the wheel is already at full speed before the foot lands, or it slows while the pedal is '
       'plainly still being driven'),
      ('core', 'The wheel slows down once the pedal is released, gradually rather than stopping '
               'dead.',
       'the wheel holds full speed for the rest of the shot after the pedal is released, or it '
       'stops the instant the foot lifts'),
      ('major', 'The wheel turns the way the pedal drives it.',
       'the wheel turns against the direction the pedal is pushed'),
      ('major', 'The pedal, the chain and the wheel move together: the pedal turns while the wheel '
                'is being driven and the chain runs with them.',
       'the pedal turns with the wheel and chain motionless, or the chain hangs slack while power '
       'is plainly going through it'),
      ('minor', 'The rim covers more ground than the spokes near the hub in the same time.',
       'the hub region sweeps round faster than the rim'),
      marks('the wheel', 'the tyre lettering and the valve')),
    note="Their three standards -- spin up, slow down, direction consistent with the applied force "
         "-- are all sound and all used here, which is unusual in this block. The addition is the "
         "drivetrain: the pedal, chain and wheel are geared together, so a clip in which the pedal "
         "moves and the chain does not, or vice versa, is broken in a way none of their standards "
         "notices. Scenario 23, 'A bicycle wheel spins while suspended in the air', is the same "
         "wheel judged for the decay alone and carries this mechanism.")

add('threaded-tightening', 146,
    'A turned wrench draws the bolt down into its thread until it comes up tight and stops.',
    S(('core', 'A wrench and a bolt are present.'),
      ('core', 'The wrench turns the bolt.'),
      ('minor', 'The bolt is engaged in something -- a nut, a plate or a threaded hole -- rather '
                'than turning in free air.'),
      ('minor', 'The bolt ends up tight rather than still turning freely, as the caption says.')),
    P(('fatal', 'The bolt draws down into its thread as it is turned, rather than backing out.',
       'the bolt rises out of its thread while the wrench turns it in the tightening direction'),
      ('core', 'The wrench and the bolt turn together, with the jaws staying on the bolt head.',
       'the wrench turns while the bolt stays still, or the jaws pass through the head'),
      ('core', 'The bolt turns only while the wrench turns it, and stops when the wrench stops.',
       'the bolt keeps turning on its own after the wrench is taken off'),
      ('major', 'The turning gets harder and then stops as the bolt comes up tight, rather than '
                'spinning on freely at the same rate.',
       'the bolt keeps turning at the same easy rate for the whole shot although it is plainly '
       'seated'),
      ('major', 'The bolt turns about its own axis and stays in line with the hole.',
       'the bolt tips out of line with its thread, or it wobbles about some other axis while being '
       'turned'),
      ('minor', 'What the bolt is threaded into stays still.',
       'the nut or the plate turns along with the bolt'),
      unmarked('the wrench', 'nothing at all here')),
    note="Their first standard, 'The bolt rotates around this axis', is a tautology with a dangling "
         "reference -- no axis has been named -- and their second repeats the direction match that "
         "the first block already covers. Neither names the thing that makes this scenario "
         "'tightens' rather than merely 'turns': the resistance builds and the motion stops when the "
         "bolt seats. That is the core item here. Scenario 144 is the same helical mechanism driving "
         "a screw into wood.")

add('spring-winding', 147,
    'A turned key winds the spring inside the toy, getting stiffer as it goes, and stays wound.',
    S(('core', 'A wind-up toy is present.'),
      ('core', 'Its key is twisted.'),
      ('minor', 'The key turns rather than the whole toy turning with it.'),
      ('minor', 'The toy reads as a wind-up toy with a key rather than a battery toy.')),
    P(cons('the toy'),
      ('core', 'The key turns only while it is being twisted and stops when the hand stops.',
       'the key keeps turning on its own after the hand lets go, or it turns with nothing touching '
       'it'),
      ('core', 'The key does not unwind back while it is being held.',
       'the key runs backwards under the hand that is winding it'),
      ('major', 'The winding gets stiffer as it goes -- the turns come slower or need more effort '
                'the further in it is wound.',
       'the key turns as freely at the end of the winding as at the start, without limit'),
      ('major', 'The key turns about its own axis, in place on the toy.',
       'the key travels across the body of the toy while turning, or it turns about some other axis'),
      ('minor', 'The toy body stays still while the key is turned.',
       'the whole toy spins round with the key'),
      ('minor', 'The toy starts moving only after the winding, not during it.',
       'the toy runs about at speed while it is still being wound',
       'the toy is released within the shot')),
    note="Their standards are 'The key is rotating' -- a tautology -- and the direction match. "
         "Neither touches the physics the caption names, which is energy being stored: a spring "
         "resists more the more it is wound, so the winding stiffens and eventually stops, and the "
         "wound key holds rather than unwinding under the hand. Those are the items here. That the "
         "toy only runs after release is behind a precondition, since many clips end before it.")

# ---- Balance and Stability (148-154) --------------------------------------
add('active-balance-riding', 148,
    'A clown rides the unicycle, making constant small corrections to stay over the wheel.',
    S(('core', 'A clown is present.'),
      ('core', 'A unicycle is present.'),
      ('core', 'The clown rides it, and it travels.'),
      ('minor', 'The clown reads as a clown -- costume, make-up or props.')),
    P(cons('the unicycle'),
      ('core', 'The wheel turns as the unicycle travels, and the amount it turns goes with the '
               'distance covered.',
       'the unicycle glides along with its wheel still, or the wheel turns against the direction of '
       'travel'),
      ('core', 'The clown keeps making small corrections -- shifting, steering, waving the arms -- '
               'rather than sitting perfectly rigid.',
       'the clown is locked in one fixed pose, upright and motionless, while balanced on a single '
       'wheel'),
      ('major', 'The wheel stays under the clown, and the two lean together rather than separately.',
       'the wheel drifts out from under the rider while they stay upright, or the clown and the '
       'machine lean opposite ways'),
      ('major', 'The wheel keeps contact with the ground.',
       'the unicycle rides along clear of the ground'),
      ('minor', 'A turn is made by leaning into it rather than staying vertical through it.',
       'the clown stays exactly vertical through a sharp turn',
       'the unicycle changes direction during the shot'),
      marks('the unicycle', 'the spokes and the pedals')),
    note="Their standards ask for 'minimal deviation from vertical alignment' and 'no sudden "
         "falls'. Both are the wrong way round. A unicycle is an unstable equilibrium held by "
         "continuous active correction, so visible small adjustment is the physics and a rigidly "
         "upright rider is the answer that cannot be produced by a real body; and whether the rider "
         "falls is skill, which _policy.json's not_penalized list excludes outright. This rubric "
         "requires the corrective motion instead, and asks nothing about success.")

add('beam-balance-attempt', 149,
    'A gymnast works to stay over the narrow beam, correcting continuously as she shifts.',
    S(('core', 'A gymnast is present.'),
      ('core', 'A beam is present.'),
      ('core', 'The gymnast is on the beam and working to stay balanced.'),
      ('minor', 'The beam reads as a narrow gymnastics beam rather than a wide bench or the floor.')),
    P(cons('the beam'),
      ('core', 'The gymnast keeps her weight over the beam: her supporting foot or hand is on it '
               'whenever she is up.',
       'she stays up with her supporting foot out in the air beside the beam, or she hovers above it'),
      ('core', 'She makes continuous corrections -- arms out, small shifts, ankle and hip '
               'adjustments -- rather than holding one rigid pose.',
       'she stands perfectly still and rigid on the narrow beam with no adjustment at all'),
      ('major', 'When she leans one way she corrects back the other way rather than leaning further '
                'and further and still staying up.',
       'she tips well past vertical and holds there, balanced on the beam with nothing supporting '
       'the lean'),
      ('major', 'If she does come off, she goes down under gravity rather than stepping off into '
                'the air.',
       'she leaves the beam and stays at that height, or she drifts down slower than a fall',
       'she loses the beam during the shot'),
      ('major', 'Her contact with the beam is at the beam surface: her feet rest on it rather than '
                'sinking into it.',
       'her feet pass into or through the beam'),
      ('minor', 'The beam and its supports stay still under her.',
       'the beam sways, bends or shifts as she moves on it'),
      marks('the gymnast', 'her leotard and her hair')),
    note="Their three standards ask for controlled movement 'without any noticeable wobbles', the "
         "centre of mass over the beam, and no falls. The first and third are unusable: the caption "
         "says the gymnast TRIES to balance, so a fall is a legitimate outcome and not a physics "
         "error, and wobble is the correcting motion that balancing consists of -- form and skill "
         "are excluded by _policy.json. The centre of mass is not visible, so it is restated here as "
         "the supporting foot being on the beam and the lean being corrected rather than held.")

add('teetering-stack', 150,
    'A leaning stack of books rocks slightly on the table without going over.',
    S(('core', 'A stack of books is present.'),
      ('core', 'It rests on a table.'),
      ('core', 'The stack leans or teeters rather than sitting square, as the caption says.'),
      ('minor', 'The stack is tall enough to look precarious rather than being two or three books.')),
    P(('fatal', 'The books rest on each other and on the table, with each one supported by what is '
                'under it.',
       'a book hangs in the air unsupported, or books pass through each other'),
      ('core', 'Each book stays flat and rigid; the lean comes from how they sit on each other.',
       'the books bend or curve to make the lean, or they stretch to keep the stack together'),
      ('core', 'The teetering stays small and returns toward where it was, rather than growing.',
       'the lean grows steadily further with nothing pushing it and the stack still stands, or the '
       'stack rocks harder and harder on its own'),
      ('major', 'The stack rocks about its bottom edge, pivoting on the table, rather than sliding '
                'about or flexing in the middle.',
       'the stack slides across the table as it rocks, or the middle of the stack sways while the '
       'top and bottom stay put'),
      ('major', 'The books keep their order and their spacing as the stack moves.',
       'books swap places, or gaps open and close between them while the stack merely teeters'),
      ('minor', 'The rocking dies down rather than continuing at the same size indefinitely.',
       'the stack teeters at exactly the same amplitude for the whole shot'),
      fixed('the table')),
    note="Their standards -- the stack stays up, the teetering angle varies within a small range -- "
         "are sound and are used. The additions are what makes it a rigid-body scenario rather than "
         "a soft one: the books do not bend to accommodate the lean, the stack pivots on an edge "
         "rather than sliding or flexing, and the rocking decays. A clip in which a curving stack "
         "sways in the middle satisfies both of their standards.")

add('leaning-ladder', 151,
    'A ladder rests against the wall, held by contact at its foot and its top, and stays there.',
    S(('core', 'A ladder is present.'),
      ('core', 'It leans against a wall.'),
      ('minor', 'The ladder stands at a slant rather than flat against the wall or upright on its '
                'own.'),
      ('minor', 'The foot of the ladder is on the ground within the shot.')),
    P(cons('the ladder'),
      rigid('the ladder'),
      ('core', 'The ladder touches the wall near its top and the ground at its foot, and keeps both '
               'contacts.',
       'the ladder leans with a gap at the wall or with its feet clear of the ground, or an end '
       'passes into the wall or the floor'),
      ('major', 'The foot of the ladder stays where it is rather than creeping outward.',
       'the foot slides steadily out from the wall while the ladder stays at the same angle'),
      ('major', 'The ladder stays at one angle, and any small settling stops rather than carrying '
                'on.',
       'the ladder leans progressively further with nothing acting on it and does not fall'),
      ('major', 'If the foot does slip, the top comes down the wall with it.',
       'the foot slides out while the top stays at the same height on the wall',
       'the foot moves during the shot'),
      ('minor', 'The rungs stay evenly spaced and square to the stiles.',
       'the rungs shift along the ladder or splay as it leans'),
      fixed('the wall and the floor')),
    note="Their second standard asks that the centre of mass stay between the base and the wall "
         "contact. That is the correct physics of why the ladder stands, but the centre of mass is "
         "not a visible feature of a clip, so an annotator can only guess at it. It is restated "
         "here as the observable consequences: both contacts are kept, the foot does not creep, and "
         "if the foot does go then the top must come down with it. Their first standard, that the "
         "ladder stays up, is used as written.")

add('edge-of-table-stability', 152,
    'A glass of water sits near the table edge, resting square on its base and staying put.',
    S(('core', 'A glass of water is present.'),
      ('core', 'It stands on a table.'),
      ('core', 'It sits near the edge rather than in the middle, as the caption says.'),
      ('minor', 'The glass holds visible water rather than being empty.')),
    P(cons('the glass'),
      ('core', 'The glass stays where it was put: it does not creep toward the edge or slide about '
               'on a level table.',
       'the glass slides across the table with nothing touching it'),
      ('core', 'The glass rests on its base with the base on the table, rather than tipping or '
               'overhanging into thin air.',
       'the glass stands tilted and stays tilted, or it balances with its base entirely off the '
       'table edge'),
      ('major', 'The water surface stays level and stays put.',
       'the water sits at a slant in an upright glass, or it sloshes about with nothing disturbing '
       'the glass'),
      ('major', 'If the glass does go over the edge, it falls.',
       'the glass leaves the table and hangs in the air, or it drifts down slower than a fall',
       'the glass leaves the table during the shot'),
      ('major', 'The water stays in the glass while the glass is upright and still.',
       'the level drops with nothing pouring out, or water rises over the rim on its own'),
      ('minor', 'The glass keeps its reflections and highlights as the light stays put.',
       'the highlights on the glass slide about or vanish while nothing in the scene moves'),
      fixed('the table')),
    note="Their standards are sound in substance, but the second asks that the centre of the glass "
         "be 'visually aligned vertically above the table surface', which is a centre-of-mass "
         "statement dressed as an observable. It is restated here as the base resting on the table "
         "and the glass not standing at a lasting tilt. The water items are additions: a glass of "
         "water is also a free surface, and a slanted or self-sloshing surface in a still upright "
         "glass is a violation their standards do not reach.")

add('wire-balance-walking', 153,
    'A tightrope walker crosses the wire, correcting continuously to stay over it.',
    S(('core', 'A tightrope walker is present.'),
      ('core', 'A wire is present.'),
      ('core', 'The walker moves along the wire.'),
      ('minor', 'The support reads as a thin wire or rope rather than a plank or a beam.')),
    P(('fatal', 'The walker is supported by the wire: their feet are on it and it takes their '
                'weight.',
       'the walker treads on air beside the wire, or their feet pass through it'),
      ('core', 'The walker keeps correcting -- arms out and adjusting, small shifts of hip and '
               'ankle, a balance pole moving -- rather than holding one rigid pose.',
       'the walker crosses in a single fixed pose with no adjustment at all'),
      ('core', 'The walker stays over the wire: a lean one way is answered by a correction back.',
       'the walker leans far off to one side and stays there, upright on the wire with nothing '
       'holding the lean'),
      ('major', 'The wire sags under the walker, and the lowest point moves along with them.',
       'the wire stays perfectly straight and taut under their weight, or the sag stays at one place '
       'as the walker moves past it'),
      ('major', 'The wire stays anchored at its ends and does not stretch out longer as they cross.',
       'the wire lengthens as the walker advances, or an end comes free and the walker stays up'),
      ('minor', 'The walker advances along the wire rather than being carried along it while '
                'stepping in place.',
       'the walker strides while staying at the same point on the wire, or slides along without '
       'stepping'),
      marks('the walker', 'their costume and their pole')),
    note="Both of their standards are unusable as written: 'no abrupt or jerky actions' and "
         "'without excessive swaying or tilting' ask for the absence of the corrective motion that "
         "the balancing consists of, and they are about poise and skill, which _policy.json "
         "excludes. The physics that is actually testable here is the correction loop and the wire's "
         "response -- it sags under the load and the sag travels with the walker -- and that is what "
         "this rubric asks for. Scenarios 148 and 149 are the same active-balance problem on a "
         "unicycle and a beam.")

add('three-point-rocking', 154,
    'A chair on an uneven floor rests on three legs and rocks onto the fourth when disturbed.',
    S(('core', 'A chair is present.'),
      ('core', 'It stands on a floor that is uneven.'),
      ('core', 'The chair wobbles or rocks rather than standing solid, as the caption says.'),
      ('minor', 'The unevenness is visible in the floor itself, not only in the chair.')),
    P(cons('the chair'),
      ('core', 'At any moment the chair rests on the legs that reach the floor, with the others '
               'clear of it.',
       'all four legs sit flat on a plainly uneven floor at once, or a leg holds the chair up with '
       'a visible gap beneath it'),
      ('core', 'The rocking moves the contact from one set of legs to another rather than bending '
               'the chair.',
       'the chair frame flexes to take up the unevenness while all the legs stay down'),
      ('major', 'The legs stay on the floor surface and do not pass into it.',
       'a leg sinks into the solid floor or passes through it'),
      ('major', 'The rocking dies down to rest on one set of legs rather than continuing '
                'indefinitely.',
       'the chair rocks at the same size for the whole shot with nothing pushing it'),
      ('major', 'The chair rocks about the legs that are down, staying in roughly one place, rather '
                'than sliding across the floor.',
       'the chair travels across the floor as it rocks'),
      ('minor', 'The chair rocks only when something disturbs it.',
       'the chair starts rocking on its own with nothing touching it and no visible cause'),
      fixed('the floor')),
    note="Their first standard asks that the chair's centre of mass 'shift to reflect the "
         "imbalance', which is not a visible feature and in any case the centre of mass of a rigid "
         "chair does not move relative to the chair. It is restated as the observable version: "
         "which legs are carrying the load, and the contact set changing as it rocks. Their second "
         "standard, intermittent leg contact without sliding, is sound and is used. The addition is "
         "the decay, since a rocking chair on an uneven floor settles onto three legs.")

# ---- Center of Mass (155-161) --------------------------------------------
add('load-shift-tilt', 155,
    'An elephant walking along the boat tips it toward whichever end the elephant is on.',
    S(('core', 'An elephant is present.'),
      ('core', 'A boat is present.'),
      ('core', 'The elephant walks along or across the boat.'),
      ('minor', 'The boat is in water rather than ashore or on a trailer.')),
    P(cons('the boat'),
      ('core', 'The boat tips toward the part the elephant is standing on, and the tilt follows the '
               'elephant as it moves.',
       'the boat tips away from the elephant, or the tilt stays fixed while the elephant walks from '
       'one end to the other'),
      ('core', 'The boat sits lower in the water with the elephant aboard than it would empty.',
       'the boat rides at the same height carrying an elephant as it does empty, or it rises in the '
       'water as the elephant steps on'),
      ('major', 'The elephant stays on the boat surface, and its feet rest on the deck.',
       "the elephant's feet pass into the deck, or it walks along above the boat without touching it"),
      ('major', 'The boat and the elephant tilt together; the elephant does not stay level on a '
                'tilting deck.',
       'the elephant stands exactly upright while the deck under it leans'),
      ('minor', 'The water responds to the tilting -- the waterline shifts and ripples go out.',
       'the water surface stays glassy and unchanged as the boat rolls about in it'),
      rigid('the boat')),
    note="Their sole standard, that the elephant's position visibly shifts the boat's tilt, is the "
         "central item and is used. The additions are the two things it leaves out: the boat also "
         "sits lower overall under the load, which a clip can easily get wrong by keeping the "
         "waterline fixed, and the elephant must lean with the deck rather than staying upright on a "
         "tilting floor.")

add('seesaw-weight-shift', 156,
    'A person sitting on one end of an empty seesaw takes that end all the way down to the ground.',
    S(('core', 'A seesaw is present.'),
      ('core', 'A person sits down on one end of it.'),
      ('core', 'The other end is empty, as the caption says.'),
      ('minor', 'The seesaw is level or near level before the person sits.')),
    P(cons('the seesaw'),
      rigid('the seesaw'),
      ('core', 'The end the person sits on goes down and the far end goes up.',
       'the end being sat on rises, or both ends go the same way'),
      ('core', 'The loaded end continues down until it reaches the ground or its stop, since there '
               'is nothing on the other end to hold it.',
       'the seesaw settles at a slant and holds there with one end loaded and the other empty and '
       'clear of the ground'),
      ('major', 'The seesaw turns about its pivot, which stays where it is.',
       'the whole seesaw drops or shifts sideways, or it turns about a point away from the pivot'),
      ('major', 'The person stays on the end they sat on and moves down with it.',
       'the person slides along the plank, or they stay at one height while the end under them '
       'descends'),
      ('minor', 'The far end rises by as much as the near end drops.',
       'one end moves far more than the other about the same central pivot'),
      fixed('the pivot post and the ground')),
    note="Their second standard, that the seesaw 'clearly balances at the new angle after the "
         "person sits down', is wrong and rewards the wrong clip. With one end loaded and the other "
         "empty there is no balancing angle: the loaded end goes all the way down to its stop. A "
         "clip in which the seesaw settles half-tilted and hangs there satisfies their standard "
         "while showing a torque appearing from nowhere. This rubric requires it to go down to the "
         "stop. Their first standard, on which end goes which way, is sound and is used.")

add('off-centre-load-tip', 157,
    'An unevenly loaded backpack tips over toward the loaded side and comes to rest there.',
    S(('core', 'A backpack is present.'),
      ('core', 'It is loaded unevenly, as the caption says.'),
      ('core', 'It tips over during the shot.'),
      ('minor', 'The load or the bulge is visible on one side rather than being invisible.')),
    P(cons('the backpack'),
      ('core', 'The backpack tips toward the side the weight is on.',
       'it tips toward its empty side, or it tips in a direction unrelated to where the load sits'),
      ('core', 'The tipping speeds up once it is past the point of balance rather than easing over '
               'at a constant rate.',
       'the backpack goes over at one steady rate throughout, or it slows as it falls'),
      ('major', 'The backpack pivots about the edge of its base rather than sliding or floating '
                'over.',
       'the backpack slides sideways as it goes over, or it topples about a point in mid-air'),
      ('major', 'It comes to rest once it is down and stays there.',
       'it rocks back upright on its own after landing, or it keeps rolling with nothing pushing it'),
      ('major', 'The load stays inside and moves with the bag.',
       'the contents stay put while the bag tips away from them'),
      ('minor', 'The bag keeps its overall shape as it goes over, sagging at most.',
       'the backpack flattens or folds up as it tips'),
      fixed('the surface it stands on')),
    note="Their standards are sound. The one correction is direction: their physics_prompt says the "
         "backpack tips 'forward', but the caption says only that it is loaded off centre, and an "
         "off-centre load tips toward the load, whichever way that is. Requiring forward would fail "
         "a correct clip of a side-loaded bag. The addition is the acceleration past the balance "
         "point, which is what separates a real topple from an eased-over one.")

add('suspended-load', 158,
    'A crane raises the load on a taut cable, and the load hangs directly below the hook.',
    S(('core', 'A crane is present.'),
      ('core', 'A large object hangs from it.'),
      ('core', 'The load is lifted -- it goes up during the shot.'),
      ('minor', 'The load reads as heavy and large rather than light and small.')),
    P(cons('the load'),
      ('core', 'The load hangs directly below the hook while it is still.',
       'the load hangs off to one side of the hook with the cable slanting and nothing pushing it'),
      ('core', 'The cable is straight and taut while it carries the load.',
       'the cable hangs slack or curls while the load is plainly hanging on it'),
      ('major', 'The load rises only while the cable is being hauled in, and stops when it stops.',
       'the load keeps rising with the cable stationary, or it hangs still while cable is plainly '
       'being wound in'),
      ('major', 'The cable keeps its length rather than stretching under the load.',
       'the cable visibly lengthens as the load is picked up'),
      ('major', 'If the crane moves, the load swings behind it and the swing then dies down.',
       'the load tracks the crane exactly with no swing at all, or it swings on at the same size '
       'for the rest of the shot',
       'the crane or its jib moves during the lift'),
      ('minor', 'The load hangs the same way up throughout rather than turning over.',
       'the load rotates about a horizontal axis while hanging on a single cable'),
      fixed('the crane body and its base')),
    note="Their sole standard -- hook and load aligned vertically with no horizontal offset when "
         "stable -- is good physics and is core here. Everything else is written from scratch. The "
         "items that matter most beyond it are the cable being taut and inextensible, and the "
         "pendulum swing when the crane moves, which is where these clips most often show a load "
         "glued rigidly under a moving hook.")

add('uneven-pack-topple', 159,
    'An unevenly packed suitcase goes over toward its heavy side and stays down.',
    S(('core', 'A suitcase is present.'),
      ('core', 'It tips over during the shot.'),
      ('minor', 'The suitcase stands upright before it tips.'),
      ('minor', 'Something suggests the uneven packing -- a bulge, an open lid or a visible load.')),
    P(cons('the suitcase'),
      rigid('the suitcase'),
      ('core', 'The suitcase goes over toward its heavy side.',
       'it tips toward its light side, or it tips in a direction with nothing to account for it'),
      ('core', 'The tipping speeds up once it is past the point of balance.',
       'the suitcase goes over at one unchanging rate, or it slows down as it falls'),
      ('major', 'It pivots about the bottom edge it goes over, keeping that edge on the ground.',
       'the suitcase slides away as it tips, or it turns about a point off the ground'),
      ('major', 'It lands and stays down.',
       'it rights itself again on its own after landing'),
      ('minor', 'The wheels and handle stay on the case and move with it.',
       'the wheels or the handle stay behind as the case goes over'),
      fixed('the floor')),
    note="Their sole standard is 'The suitcase visibly tips over', which any tipping satisfies -- "
         "including a case that tips the wrong way, slides over, or eases down at a constant rate. "
         "Every item here beyond the fact of tipping is written from scratch: the direction is set "
         "by where the weight is, the motion accelerates past the balance point, and the case "
         "pivots on an edge. Scenario 157 is the same mechanism for a backpack.")

add('base-of-support-recovery', 160,
    'A pushed table leans and then settles back on all its legs without going over.',
    S(('core', 'A table is present.'),
      ('core', 'It is pushed.'),
      ('core', 'It stays upright rather than toppling, as the caption says.'),
      ('minor', 'The push is visible -- a hand, a body or an object making contact.')),
    P(cons('the table'),
      rigid('the table'),
      ('core', 'The table responds while it is being pushed and stops responding when the push '
               'stops.',
       'the table keeps tilting or sliding after the push has plainly ended, or it moves before '
       'anything touches it'),
      ('core', 'The table comes back down onto all its legs once the push ends.',
       'it stays leaning on two legs after the push, balanced there with nothing holding it'),
      ('major', 'Whichever legs are down stay in contact with the floor and do not pass into it.',
       'a leg sinks into the floor, or the table stays up with every leg clear of the ground'),
      ('major', 'The table either tilts about a bottom edge or slides along the floor, and does so '
                'as one piece.',
       'the top slides while the legs stay put, or the legs splay outward under the push'),
      ('minor', 'Any rocking after the push dies down.',
       'the table rocks on at the same size for the rest of the shot'),
      fixed('the floor')),
    note="Their sole standard, that the table 'resists tipping and returns to an upright position "
         "when nudged', is the core of the scenario and is used. The additions are what makes it "
         "rigid-body: the table moves as one piece, its legs stay on the floor rather than splaying "
         "or sinking, and the response is tied to the push in time. Sliding instead of tipping is "
         "also allowed here -- a pushed table often does -- and their standard does not say so.")

add('strike-then-topple', 161,
    'A struck pin tips away from the ball, goes over past its balance point and falls.',
    S(('core', 'A bowling ball and a pin are present.'),
      ('core', 'The ball strikes the pin.'),
      ('core', 'The pin falls.'),
      ('minor', 'The pin stands upright before it is struck.')),
    P(('fatal', 'The ball and the pin meet at their surfaces, and the pin moves only after the '
                'contact.',
       'the pin starts falling before the ball reaches it, or the ball passes through the pin'),
      ('core', 'The pin goes over away from the ball, in the direction the ball was travelling.',
       'the pin topples back toward where the ball came from, or sideways with nothing to account '
       'for it'),
      ('core', 'The pin tips about its base and then falls once it is past its balance point, '
               'rather than sliding away flat or lifting off.',
       'the pin slides upright across the lane without tipping, or it rises off the lane and falls '
       'from mid-air'),
      ('major', 'The ball carries on after the hit rather than stopping dead.',
       'the ball halts at the point of contact with nothing blocking it'),
      ('major', 'The pin speeds up as it goes over.',
       'the pin falls at one unchanging rate, or it slows as it goes down'),
      ('minor', 'The pin lands and stays down.',
       'the pin rights itself again after landing'),
      cons('the pin')),
    note="Their first standard asks that the pin's centre of mass move horizontally beyond its "
         "base. That is the correct account of why the pin goes over, but the centre of mass is not "
         "visible, so it is restated here as the observable version: the pin tips about its base and "
         "then accelerates over once past the balance point. Their second standard, that the pin "
         "falls, is a bare outcome. The additions are the direction -- away from the ball -- and the "
         "ball continuing on afterwards, which is where a clip most often stops the ball dead.")

# ---- Impact and Deformation (162-168) ------------------------------------
add('soft-target-absorption', 162,
    'A baseball sinks into the pillow, which dents under it, and the ball drops rather than '
    'springing away.',
    S(('core', 'A baseball is present.'),
      ('core', 'A pillow is present.'),
      ('core', 'The ball strikes the pillow.'),
      ('minor', 'The pillow reads as soft and yielding rather than firm.')),
    P(('fatal', 'The ball and the pillow meet at their surfaces: the ball presses into the pillow '
                'rather than passing through it.',
       'the ball passes through the pillow and out the other side, or it stops short of it with a '
       'visible gap'),
      ('core', 'The pillow dents where the ball hits, and the dent is deepest at the contact.',
       'the pillow stays perfectly smooth through the impact, or it dents somewhere the ball never '
       'touched'),
      ('core', 'The ball loses most of its speed in the impact and does not spring away fast.',
       'the ball rebounds off the pillow as briskly as it arrived'),
      ('major', 'The pillow springs most of the way back after the ball leaves or settles.',
       'the dent stays as a permanent hole in the pillow'),
      unmarked('the ball', 'the pillow'),
      ('minor', 'The pillow moves or shifts under the blow rather than being perfectly anchored.',
       'the pillow takes a hard impact without shifting at all',
       'the pillow is resting free rather than being held or fixed'),
      ('minor', 'The ball ends up resting on or against the pillow, or on the ground below it.',
       'the ball hangs in the air beside the pillow after the impact')),
    note="Their sole standard, that the pillow compresses where the ball hits, is used. Their "
         "physics_prompt goes wrong twice, and both errors reward the wrong clip. It says the BALL "
         "deforms on contact: a baseball is a hard wound sphere and does not visibly deform against "
         "a pillow, so a clip showing a squashing baseball would be scored correct. It also says "
         "the ball bounces away: a pillow is close to fully absorbing, so the ball drops rather "
         "than rebounding, and requiring a bounce penalises the correct outcome. This rubric asks "
         "for the absorption and for the ball to come through unmarked.")

add('plastic-indentation', 163,
    'A dropped steel ball leaves a crater in the clay and stays in it rather than bouncing off.',
    S(('core', 'A steel ball is present.'),
      ('core', 'A clay block is present.'),
      ('core', 'The ball falls onto the clay and reaches it.'),
      ('minor', 'The clay reads as soft and matt rather than hard or glazed.')),
    P(('fatal', 'The ball and the clay meet at their surfaces, and the clay gives way under the '
                'ball.',
       'the ball passes through the clay block, or it stops on a clay surface that does not respond '
       'at all'),
      ('core', 'An indentation forms in the clay where the ball lands.',
       'the clay stays unmarked after the impact, or a mark appears where the ball never touched'),
      keeps('the clay', 'the indentation'),
      ('major', 'The ball barely rebounds: it stays in or on the crater rather than bouncing back '
                'up high.',
       'the ball bounces off the clay to near the height it fell from'),
      ('major', 'The ball speeds up as it falls.',
       'the ball descends at one unchanging rate, or it slows on the way down'),
      unmarked('the steel ball', 'the clay'),
      ('minor', 'The clay pushed aside goes somewhere -- a raised rim or a bulge around the crater.',
       'clay simply vanishes where the crater forms, with nothing displaced around it')),
    note="Their sole standard, that the clay visibly deforms, is used, but on its own it is "
         "satisfied by clay that dents and then springs smoothly back -- which is the opposite of "
         "what soft clay does. The item that carries the physics is the permanence: the deformation "
         "is plastic, so the crater stays, the energy went into making it, and the ball therefore "
         "does not bounce. Scenario 41, 'A falling metal block strikes a metal plate', is the "
         "harder-target version of the same mechanism.")

add('ductile-crumple', 164,
    'A hammer blow crushes the can inward, and the crumpled shape stays.',
    S(('core', 'A hammer is present.'),
      ('core', 'An aluminium can is present.'),
      ('core', 'The hammer strikes the can.'),
      ('minor', 'The can starts intact and uncrushed.')),
    P(('fatal', 'The hammer and the can meet at their surfaces, and the can gives way under the '
                'hammer.',
       'the hammer passes through the can, or the can crushes before the hammer reaches it'),
      ('core', 'The can crumples where it is struck, and the damage is worst at the point of '
               'contact.',
       'the can shrinks evenly all over, or it crumples on a side the hammer never touched'),
      keeps('the can', 'the crumpling'),
      ('major', 'The can folds and creases rather than shattering into pieces: thin aluminium is '
                'ductile.',
       'the can breaks into separate fragments like glass'),
      ('major', 'The crumpled can takes up less room than it did, and the metal goes into the folds '
                'rather than disappearing.',
       'the can keeps exactly its original size and volume while plainly being crushed'),
      unmarked('the hammer', 'the can'),
      marks('the can', 'its printing and its label'),
      ('minor', 'The can jumps or shifts under the blow rather than staying perfectly still.',
       'the can takes a hard hammer blow without moving at all',
       'the can is resting free rather than being held or clamped')),
    note="Their sole standard, deformation with noticeable changes in shape and volume, is sound "
         "and is used. The additions are the mode and the permanence: aluminium is ductile, so it "
         "folds and creases rather than fragmenting, and the crumpling is plastic, so it stays. A "
         "can that springs back to a perfect cylinder satisfies their standard and is the "
         "commonest wrong answer here. Scenario 38, 'A car crashes into a stationary barrier', is "
         "the same crumpling mechanism at a different scale.")

add('wall-rebound-compression', 165,
    'A soccer ball flattens against the wall at contact, springs back and comes away slower.',
    S(('core', 'A soccer ball is present.'),
      ('core', 'A wall is present.'),
      ('core', 'The ball strikes the wall and comes away from it.'),
      ('minor', 'The ball is travelling under its own momentum rather than being carried.')),
    P(('fatal', 'The ball and the wall meet at their surfaces: the ball rebounds rather than '
                'passing into the wall.',
       'the ball goes into or through the wall, or it reverses direction before reaching it'),
      ('core', 'The ball flattens against the wall at the moment of contact and rounds out again as '
               'it leaves.',
       'the ball stays perfectly spherical through the contact, or it stays flattened after it has '
       'come away'),
      ('core', 'The ball comes off the wall more slowly than it arrived.',
       'the ball leaves the wall faster than it came in, or it returns at exactly the speed it '
       'arrived at'),
      ('major', 'The ball comes away from the face of the wall, on the same side it arrived from.',
       'the ball rebounds along the wall face, or it comes off into the wall'),
      ('major', 'The flattening happens only while the ball is touching the wall.',
       'the ball is squashed while still in mid-air before contact, or after it has left'),
      unmarked('the wall', 'the ball'),
      marks('the ball', 'its panel markings')),
    note="Their standards -- the ball compresses at the point of impact, the wall is unaffected -- "
         "are both sound and both used. The addition is the speed: a real bounce loses energy in "
         "the compression, so the ball must come away slower than it arrived, and their standards "
         "would pass a ball that rebounds faster than it came in. Scenario 37 is the ball-to-ball "
         "version of the same contact mechanics.")

add('impact-flexure-rebound', 166,
    'A struck wooden board bows under the blow, springs back and its flexing dies away.',
    S(('core', 'A wooden board is present.'),
      ('core', 'An object falls onto it and hits it.'),
      ('core', 'The board bends when struck, as the caption says.'),
      ('minor', 'The board reads as thin and flexible rather than a thick block.')),
    P(('fatal', 'The falling object and the board meet at their surfaces, and the board gives '
                'under it.',
       'the object passes through the board, or the board bends before the object reaches it'),
      ('core', 'The board bends most where it is struck and comes back to straight afterwards.',
       'the board keeps its bent shape permanently, or it bends most somewhere the object did not '
       'land'),
      ('core', 'The bend appears at the moment of impact rather than before or long after.',
       'the board is already bowed while the object is still in the air'),
      ('major', 'The board flexes back and forth after the impact and the flexing gets smaller each '
                'time.',
       'the board keeps flexing at the same size for the rest of the shot, or its flexing grows'),
      ('major', 'The board stays whole and stays supported where it was.',
       'the board snaps in two under an ordinary blow, or it comes off its supports and stays up'),
      ('minor', 'The struck object rebounds or comes to rest on the board rather than hanging in '
                'the air.',
       'the object stops in mid-air above the board after the impact'),
      unmarked('the falling object', 'the board')),
    note="Their sole standard, a noticeable curve on impact, is used. It says nothing about what "
         "happens next, and that is the whole distinction the caption draws by calling the board "
         "flexible: the bending is elastic, so the board springs back and rings down rather than "
         "staying bent. A board that takes a permanent bow satisfies their standard and belongs to "
         "the plastic scenarios instead. Scenario 67, 'A wooden plank has a weight on top of it', "
         "is the same board under a static load.")

add('crush-and-stay', 167,
    'A stepped-on bottle buckles and flattens, and it stays crushed after the foot lifts.',
    S(('core', 'A plastic bottle is present.'),
      ('core', 'It is stepped on.'),
      ('core', 'The bottle crumples or flattens, as the caption says.'),
      ('minor', 'The bottle starts intact and full-sized.')),
    P(('fatal', 'The foot and the bottle meet at their surfaces, and the bottle gives way under it.',
       'the foot passes through the bottle, or the bottle collapses before the foot reaches it'),
      ('core', 'The bottle crumples where it is trodden on and gets shorter or flatter overall.',
       'the bottle keeps its full size and shape under a foot that is plainly bearing down on it'),
      keeps('the bottle', 'the crushing'),
      ('major', 'The bottle buckles into creases and folds rather than shrinking evenly like '
                'something soft.',
       'the bottle deflates smoothly to a smaller bottle of the same shape'),
      ('major', 'The bottle stays one piece rather than bursting into fragments.',
       'the bottle shatters into separate shards'),
      ('minor', 'Air comes out if there is a way out -- the cap off, or the neck open.',
       'the bottle collapses while sealed and its walls fold inward with the air simply gone',
       'the bottle is plainly open or uncapped'),
      marks('the bottle', 'its label and its cap'),
      unmarked('the foot and shoe', 'the bottle')),
    note="Their sole standard, that the bottle compresses and crumples, is used. What it does not "
         "say is that the crushing is permanent, and that is the point of the scenario: the plastic "
         "yields, so a bottle that pops back to its original shape as the foot lifts satisfies "
         "their standard and shows the wrong material. Their physics_prompt's escaping air needs an "
         "opening, so that item carries a precondition. Scenario 164 is the same permanent-crumple "
         "mechanism in metal.")

add('overload-flatten', 168,
    'A tennis ball is squashed flat under the tyre, and what happens after depends on whether it '
    'survives.',
    S(('core', 'A tennis ball is present.'),
      ('core', 'A car tyre runs over it.'),
      ('core', 'The ball flattens under the tyre, as the caption says.'),
      ('minor', 'The ball is round and intact before the tyre reaches it.')),
    P(('fatal', 'The tyre and the ball meet at their surfaces, and the ball gives way under the '
                'tyre.',
       'the tyre passes through the ball, or the ball flattens before the tyre reaches it'),
      ('core', 'The ball is squashed while the tyre is on it and is most deformed at that moment.',
       'the ball keeps its round shape under a tyre that is plainly on top of it'),
      ('core', 'What happens afterwards follows from what the clip commits to: if the ball stays '
               'whole it springs back toward round, and if it splits or bursts it stays flat.',
       'the ball splits open and then returns to a perfect sphere, or it stays flat as a disc with '
       'no split, tear or opening anywhere'),
      ('major', 'The flattening and the recovery happen in the right order -- squashed under the '
                'tyre, then whatever follows once the tyre has passed.',
       'the ball springs back while the tyre is still on it'),
      ('major', 'The ball stays where the tyre leaves it or is thrown along the tyre\'s direction '
                'of travel.',
       'the ball is flung back toward where the car came from'),
      unmarked('the tyre', 'the ball'),
      ('minor', 'The ball keeps its markings and its colour through the impact.',
       'the seam and the nap change or vanish as the ball is crushed')),
    note="Their sole standard, that the ball visibly flattens, is used. Their physics_prompt adds "
         "that the ball loses its bounce 'with the air rapidly escaping', and that is not the "
         "expected outcome: a pressurised tennis ball run over by a tyre deforms enormously and "
         "then springs back, and requiring it to burst would fail the correct clip. Since either "
         "outcome is physically possible depending on the load, the core item asks for internal "
         "consistency instead -- a ball that bursts stays flat, a ball that stays whole recovers, "
         "and a clip must not have it both ways.")

# ---- Shear and Cutting (169-175) -----------------------------------------
add('tear-propagation', 169,
    'A pulled tear runs along the fabric from where it started, only ever getting longer, with '
    'frayed edges.',
    S(('core', 'A person and a piece of fabric are present.'),
      ('core', 'The person pulls at the fabric and it tears.'),
      ('minor', 'The fabric reads as woven cloth rather than paper or plastic sheet.'),
      ('minor', 'The tear starts at an edge or at a small nick rather than in the middle of an '
                'unbroken sheet.')),
    P(('fatal', 'The fabric is torn by the hands that pull it, at the place they act on.',
       'the fabric splits somewhere the hands are not, or it comes apart with the hands plainly '
       'still'),
      ('core', 'The tear only ever gets longer.',
       'the tear closes back up, or the fabric is whole again later in the shot'),
      ('core', 'The tear grows from one end and runs along a line rather than the whole seam '
               'parting at once.',
       'the fabric separates all along its length in a single frame'),
      ('major', 'The fabric stretches and puckers around the tear before and as it gives.',
       'the cloth parts with no distortion at all in the fabric on either side'),
      ('major', 'The torn edges are ragged with loose threads rather than cut clean.',
       'the tear leaves two perfectly straight, smooth edges as though scissored'),
      ('minor', 'The tear runs roughly with the pull, along the weave.',
       'the tear turns and wanders across the cloth against the direction being pulled'),
      ('minor', 'The two halves stay attached wherever the tear has not yet reached.',
       'the pieces come apart ahead of the tear')),
    note="Their standards -- visible deformation leading to fibre separation, and a gradual "
         "increase in damage -- are both sound and both used. The addition is the irreversibility: "
         "a tear cannot heal, so a clip in which the fabric is whole again later is a violation, and "
         "'gradual increase in damage' does not quite exclude it. The frayed edge is the other "
         "addition, and it is what distinguishes tearing from the cutting scenarios that follow.")

add('progressive-shear-cut', 170,
    'The scissors cut the paper progressively as the blades close, the cut running outward from the '
    'pivot.',
    S(('core', 'Scissors are present.'),
      ('core', 'Paper is present.'),
      ('core', 'The scissors cut the paper.'),
      ('minor', 'The paper is whole before the blades close on it.')),
    P(('fatal', 'The paper is cut where the blades act on it.',
       'the paper separates along a line the blades never touched, or it parts with the scissors '
       'plainly open and away from it'),
      ('core', 'The cut advances as the blades close, running along the paper rather than appearing '
               'all at once.',
       'the paper is cut along its whole length in a single frame while the blades are barely closed'),
      ('core', 'The cut only ever gets longer.',
       'the cut closes back up, or the paper is whole again later in the shot'),
      ('major', 'The paper is cut only where the blades have passed, and is still joined ahead of '
                'them.',
       'the paper is already separated ahead of the blades'),
      ('major', 'The cut edges are straight and clean, and the two pieces stay flat.',
       'the cut leaves ragged frayed edges as though the paper had been torn'),
      ('minor', 'The two pieces move apart or fall away once the cut is through.',
       'the cut pieces stay perfectly aligned as if still joined'),
      unmarked('the scissors', 'the paper')),
    note="Their first standard, a clean cut along the line of contact, is sound. Their second, that "
         "the paper 'clearly separates into two distinct pieces immediately', is wrong and rewards "
         "the wrong clip: a shear cut progresses as the blades close, travelling outward from the "
         "pivot, so an instantaneous full-length separation is exactly the artefact to catch. This "
         "rubric requires the cut to advance with the blades. Scenarios 171 to 174 share this "
         "progressive-cut structure with different tools.")

add('slicing-cut', 171,
    'The knife works down through the loaf, the cut deepening as the blade goes, until a slice '
    'comes free.',
    S(('core', 'A knife is present.'),
      ('core', 'A loaf of bread is present.'),
      ('core', 'The knife cuts into the bread.'),
      ('minor', 'The loaf is whole before the knife goes in.')),
    P(('fatal', 'The bread is cut where the blade passes through it.',
       'the loaf separates somewhere the blade never reached, or it falls apart with the knife '
       'plainly clear of it'),
      ('core', 'The cut deepens as the blade moves, rather than the loaf parting in one go.',
       'the loaf is cut clean through in a single frame as the knife touches it'),
      ('core', 'The cut only ever gets deeper.',
       'the cut closes up again, or the loaf is whole later in the shot'),
      ('major', 'The slice stays attached until the blade is through, then comes free.',
       'the slice falls away while the blade is still part-way through the loaf'),
      ('major', 'The bread compresses slightly under the blade and springs back once it has passed.',
       'the loaf stays perfectly rigid under the blade, or it stays squashed flat where the knife '
       'went through'),
      ('minor', 'The cut face shows the crumb -- an open, uneven interior rather than a solid '
                'featureless surface.',
       'the cut reveals a smooth blank face with no crumb structure at all'),
      ('minor', 'Crumbs come off at the cut.',
       'the loaf is cut with nothing at all shed from it',
       'the shot is close enough to the cut to show crumbs'),
      unmarked('the knife', 'the bread')),
    note="Their sole standard is that the bread ends up in two pieces, which any separation "
         "satisfies. Every item here is written from scratch on the pattern of scenario 170: the cut "
         "advances with the blade, it only deepens, and the slice stays attached until the blade is "
         "through. The bread-specific additions are the slight compression under the blade and the "
         "crumb on the cut face, which are what distinguish bread from a rigid block.")

add('guillotine-shear', 172,
    'The descending blade shears the stack progressively, cutting only where it has already passed.',
    S(('core', 'A guillotine paper cutter is present.'),
      ('core', 'A stack of paper is on it.'),
      ('core', 'The blade comes down and cuts the paper.'),
      ('minor', 'The stack is whole and square before the blade comes down.')),
    P(('fatal', 'The paper is cut where the blade passes through it.',
       'the stack separates along a line the blade never crossed, or it parts with the blade still '
       'plainly raised'),
      ('core', 'The cut advances with the blade as it comes down, from one side across.',
       'the whole stack is cut through in a single frame as the blade begins to move'),
      ('core', 'The blade turns about its hinge and stays attached to it.',
       'the blade comes down flat and unhinged, or it separates from the cutter and keeps cutting'),
      ('major', 'Sheets are cut where the blade has passed and still joined where it has not.',
       'sheets ahead of the blade are already separated'),
      ('major', 'All the sheets under the blade are cut, not just the top ones.',
       'the top sheets are cut while the ones below stay whole under a blade that has plainly gone '
       'right through'),
      ('minor', 'The cut edge is straight and square across the stack.',
       'the cut edge is ragged or wanders across the sheets'),
      ('minor', 'The trimmed offcut comes away and the rest of the stack stays in place.',
       'the whole stack scatters, or the offcut stays perfectly in line as if still attached'),
      unmarked('the blade', 'the paper')),
    note="Their sole standard is that the papers are cut as the blade descends, which is the right "
         "shape of requirement but is satisfied by any cut that happens during the descent, "
         "including one that appears all at once. The items here make it progressive and add the "
         "two things specific to a guillotine: the blade pivots about its hinge, and every sheet in "
         "the stack under the blade is cut, not only the visible top ones.")

add('sawing-kerf', 173,
    'The saw works a groove into the beam, deepening it stroke by stroke and shedding sawdust, '
    'until the beam parts.',
    S(('core', 'A saw is present.'),
      ('core', 'A wooden beam is present.'),
      ('core', 'The saw cuts into the beam.'),
      ('minor', 'The beam is whole before the saw goes into it.')),
    P(('fatal', 'The beam is cut where the saw teeth act on it.',
       'the beam separates somewhere the saw never touched, or it comes apart with the saw plainly '
       'lifted clear'),
      ('core', 'The groove only ever gets deeper, and it deepens only while the saw is working.',
       'the groove closes up again, or it keeps deepening with the saw held still'),
      ('core', 'The saw moves back and forth along the cut rather than sinking straight in.',
       'the saw is pressed straight down through the beam without any stroking motion'),
      ('major', 'The beam stays joined until the cut goes right through, then the pieces separate.',
       'the beam falls into two pieces while the groove is plainly only part-way down'),
      ('major', 'The saw stays in the groove it has made rather than wandering to a fresh line.',
       'the saw jumps to a different place on the beam and the old groove is gone'),
      ('minor', 'Sawdust is produced at the cut and falls away.',
       'the beam is cut with nothing at all shed from the groove'),
      ('minor', 'The cut faces show the wood grain running through them.',
       'the cut reveals a blank featureless surface with no grain'),
      unmarked('the saw', 'the beam')),
    note="Their sole standard, that the teeth produce fibre separation along the cutting path, is "
         "sound but does not constrain the progression. The items here add it: the kerf only "
         "deepens, it deepens only while the saw strokes, and the beam holds together until the cut "
         "is through. The reciprocating motion is the other addition -- a saw that is simply pressed "
         "down through the wood satisfies their standard and is not sawing.")

add('reciprocating-trim', 174,
    'The trimmer blades sever branches where they close on them, and the cut pieces fall away.',
    S(('core', 'A hedge trimmer is present.'),
      ('core', 'Branches are present.'),
      ('core', 'The trimmer cuts branches.'),
      ('minor', 'The branches are whole before the trimmer reaches them.')),
    P(('fatal', 'A branch is cut where the blades close on it.',
       'branches fall apart away from the blades, or they are severed with the trimmer plainly not '
       'touching them'),
      ('core', 'Each branch is severed only once the blades reach it, and branches the blades have '
               'not reached stay whole.',
       'branches ahead of the trimmer are already cut, or the whole hedge parts at once as the '
       'trimmer starts'),
      ('core', 'The blades work back and forth against each other rather than spinning round.',
       'the cutting bar rotates like a circular blade or a rotor'),
      ('major', 'Cut pieces fall away under gravity and land.',
       'severed branches hang in the air where they were cut, or they drift upward'),
      ('major', 'The branch still attached to the plant stays attached and stays put.',
       'the uncut part of the branch disappears, or it detaches along with the cut piece'),
      ('minor', 'The cut ends are severed across rather than being torn or splintered along their '
                'length.',
       'the branches split lengthwise into ragged strips instead of being cut across'),
      ('minor', 'Leaves and twigs on the cut pieces go with them.',
       'the leaves stay hanging in place while the branch they are on falls away'),
      unmarked('the trimmer blades', 'the branches')),
    note="Their sole standard, 'The branches is cut into pieces', is a bare outcome that any "
         "separation satisfies. Their physics_prompt is also wrong about the tool: it says "
         "'rotating blades', but a hedge trimmer has a reciprocating bar -- two toothed blades "
         "shearing back and forth against each other -- so a clip showing a spinning rotor would be "
         "scored correct against their description. This rubric requires the reciprocating action "
         "and, following scenario 170, that the cut only reach where the blades have been.")

add('scoring-without-fracture', 175,
    'The cutter draws a score line across the glass, and the pane stays in one piece unless it is '
    'then flexed.',
    S(('core', 'A glass cutter is present.'),
      ('core', 'A pane of glass is present.'),
      ('core', 'The cutter is drawn across the glass, scoring it.'),
      ('minor', 'The pane is whole and unmarked before the cutter is drawn across it.')),
    P(('fatal', 'The score appears only where the cutter has passed.',
       'a line appears across glass the cutter never crossed, or the score runs ahead of the tool'),
      ('core', 'The pane stays in one piece through the scoring itself.',
       'the glass falls apart into separate pieces as the cutter is drawn across it, with nothing '
       'else acting on it'),
      ('core', 'The score line advances with the cutter and only ever gets longer.',
       'the whole line appears in a single frame, or the score fades out again behind the tool'),
      ('major', 'If the pane does separate, something does it: it is flexed, tapped or pressed '
                'after the scoring.',
       'the glass parts on its own some moments after the scoring, with nothing touching it',
       'the pane separates during the shot'),
      ('major', 'Any break follows the scored line.',
       'the glass breaks along a path unrelated to the score',
       'the pane separates during the shot'),
      ('major', 'The glass stays clear and flat where it has not been scored.',
       'the pane clouds over, bends or crazes all across its surface as the cutter passes'),
      ('minor', 'The score is a fine line, and any chips it throws off are small and stay near it.',
       'the cutter leaves a wide gouge or a trail of large fragments'),
      unmarked('the cutter', 'the glass')),
    note="Their sole standard, 'The pane of glass breaks cleanly along the scored line', asks for "
         "the wrong event. A glass cutter does not cut or break glass: it scores a shallow line "
         "that concentrates stress, and the pane then has to be flexed or tapped to snap along it. "
         "The caption says only that the cutter scores the pane. Following their standard would "
         "reward a clip in which the glass falls apart under the wheel, which is the misconception "
         "this scenario is best placed to catch, and would fail a correct clip that scores and "
         "stops. This rubric makes staying whole through the scoring a core item and puts the break "
         "behind a precondition.")
