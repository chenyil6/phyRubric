# phyworldbench 1-35: Object Motion and Kinematics.
# Items are derived from the caption (the bare event prompt) plus first-principles physics;
# SRC[i]['physics_prompt'] and SRC[i]['key_standards'] were then diffed for coverage. Where
# they conflict with physics, the rubric follows physics and says so in `note`.

def cons(o):
    return ('fatal',
            f'{o[0].upper()}{o[1:]} keeps its own shape and identity for the whole shot, and it '
            f'does not pass through any solid surface.',
            f'{o} turns into a different object, passes through something solid, or disappears '
            f'and re-appears')


def nojump(o):
    return ('major',
            f'{o[0].upper()}{o[1:]} moves from each position to the next along a connected path.',
            f'{o} jumps to a different place between frames rather than travelling there')


def marks(o, mk):
    return ('minor',
            f'{mk[0].upper()}{mk[1:]} stay attached to {o} and move with it.',
            f'{mk} slide across the surface, detach, or change from one moment to the next')


# ---- Linear Motion (1-7) -------------------------------------------------
add('powered-ascent', 1,
    'A rocket lifts off under its own thrust and climbs into the sky.',
    S(('core', 'A rocket is present.'),
      ('core', 'The rocket leaves the ground and climbs into the sky.'),
      ('minor', 'The rocket starts at rest on the ground or on a launch structure rather than '
                'already being airborne.'),
      ('minor', 'Open sky is visible as what it climbs into.')),
    P(('core', 'The rocket speeds up as it climbs: it moves slowly just off the pad and fastest '
               'later in the ascent.',
       'it leaves the pad already at full speed and holds it, or it slows down while climbing '
       'with the engine still firing'),
      ('core', 'Exhaust leaves the nozzle downward, opposite to the direction the rocket travels.',
       'the plume points sideways or in the direction of travel, or the rocket climbs with no '
       'exhaust at all while the engine is plainly lit'),
      ('major', 'The rocket holds one heading through the climb rather than veering off and back.',
       'it zig-zags, drifts sideways, or reverses direction in mid-climb with nothing acting on it'),
      ('major', "The rocket's nose stays pointed along its direction of travel.",
       'it climbs sideways or tail-first'),
      ('minor', 'The plume and its smoke spread out and drift after leaving the nozzle.',
       'the plume stays a rigid attached shape that never disperses'),
      ('minor', 'The launch pad and the ground stay put; only the rocket rises.',
       'the pad or the ground rises along with the rocket'),
      cons('the rocket')))

add('rolling-friction-decay', 2,
    'A skateboard rolls along a level sidewalk and gradually slows.',
    S(('core', 'A skateboard is present.'),
      ('core', 'The skateboard rolls along the ground.'),
      ('core', 'The surface it rolls on reads as a paved sidewalk or path.'),
      ('minor', 'The board is already rolling or is set rolling, rather than being carried.')),
    P(('core', 'The board slows as it rolls, since nothing drives it once it is released.',
       'it holds exactly one speed for the whole shot, or it speeds up on its own on level ground'),
      ('core', 'The wheels stay on the ground and the deck stays above them.',
       'the board floats clear of the surface while still rolling forward'),
      ('major', 'The wheels turn in the direction the board travels, and they turn only while it '
                'is moving.',
       'the wheels sit still while the board slides forward, or they turn against the direction '
       'of travel'),
      ('major', 'The board holds one straight heading rather than curving away or reversing with '
                'nothing acting on it.',
       'it swerves or reverses on its own on a straight level path'),
      marks('the board', 'the deck graphics and the wheels'),
      ('minor', "The board's shadow stays under it and tracks it along the ground.",
       'the shadow detaches from the board, lags behind it, or is missing',
       'the scene is lit so that a shadow would be visible'),
      cons('the board')),
    note="The benchmark's own key standard for this scenario demands 'a steady speed without "
         "visible acceleration or deceleration', which is wrong and wrong in the direction that "
         "rewards a bad clip: a released skateboard on a level sidewalk loses speed to rolling "
         "resistance and bearing drag. Their physics_prompt admits as much ('with minimal friction "
         "slowing it down'), so their prompt and their standard contradict each other. This rubric "
         "requires the deceleration. The caption's 'down a flat sidewalk' is also internally odd; "
         "'flat' is taken as the operative word and no downhill slope is required.")

add('driven-constant-velocity', 3,
    'A train runs along a straight track without speeding up or slowing down.',
    S(('core', 'A train is present.'),
      ('core', 'The train moves along a track.'),
      ('core', 'The track runs straight rather than curving.'),
      ('minor', 'The train holds one speed rather than visibly starting, stopping or surging.')),
    P(('core', 'The train stays on the track, with its wheels on the rails throughout.',
       'the train leaves the rails, floats above them, or travels beside the track'),
      ('core', 'The whole train moves as one: the carriages keep their spacing and order and '
               'travel at the same speed as the locomotive.',
       'carriages stretch apart, bunch up, swap places, or move at visibly different speeds on '
       'straight track'),
      ('major', 'The wheels turn in the direction of travel while the train moves, and the amount '
                'they turn goes with the distance covered.',
       'the wheels are motionless while the train advances, or they turn against the direction of '
       'travel'),
      nojump('the train'),
      ('minor', 'The track, sleepers and ballast stay fixed as the train passes over them.',
       'the track slides, bends, or moves along with the train'),
      marks('the train', 'the windows, doors and livery'),
      cons('the train')))

add('glide-descent', 4,
    'A thrown paper airplane glides across a room, losing height as it goes.',
    S(('core', 'A paper airplane is present.'),
      ('core', 'The airplane flies through the air across the room.'),
      ('minor', 'The flight starts from a throw or a release rather than the plane already being '
                'in mid-flight.'),
      ('minor', 'The setting reads as the inside of a room.')),
    P(('core', 'The airplane loses height as it glides forward: an unpowered glider trades '
               'altitude for distance, so its path slopes downward overall and it ends lower than '
               'it started.',
       'it holds exactly the same height across the whole room, or it climbs steadily, with no '
       'thrust and nothing lifting it'),
      ('core', 'The airplane ends up on the floor or against something, rather than staying aloft '
               'indefinitely.',
       'it hovers in place or circles at a fixed height until the shot ends. If the clip simply '
       'ends while it is still legitimately gliding, mark not_shown'),
      ('major', 'The nose stays pointed roughly along the direction of flight.',
       'it flies backwards, sideways or tumbling nose-over-tail while still tracking a smooth path'),
      ('major', 'The airplane keeps its folded rigid form while flying.',
       'the paper flaps like cloth, unfolds in flight, or ripples as if weightless'),
      ('minor', 'Small deviations are consistent with air: it may dip, bank or stall, and any such '
                'wobble carries through into the path it then follows.',
       'the plane wobbles while its path stays perfectly unaffected, or it changes heading with '
       'no corresponding change in attitude'),
      ('minor', 'Landing leaves it lying on the surface rather than standing on its nose or '
                'embedded in the floor.',
       'it comes to rest in a pose no light folded paper would hold',
       'the airplane lands within the clip'),
      cons('the airplane')),
    note="The benchmark's key standard for this scenario -- 'the elevation of the paper airplane "
         "remains unchanged, neither rising nor falling as it travels across the room' -- is "
         "physically impossible and rewards the wrong clip. An unpowered paper airplane has no "
         "thrust, so it must descend along a glide slope; level flight would require lift and "
         "thrust in balance. This rubric requires the descent. The caption's 'straight' is read as "
         "the heading, not the altitude.")

add('rolling-friction-decay', 5,
    'A marble rolls across a level table top and gradually slows.',
    S(('core', 'A marble is present.'),
      ('core', 'The marble rolls across a table top.'),
      ('minor', 'The table surface reads as flat and level.'),
      ('minor', 'The marble is already rolling or is set rolling, rather than being placed down '
                'in motion out of nowhere.')),
    P(('core', 'The marble slows as it rolls, since nothing drives it along the level surface.',
       'it holds exactly one speed for the whole shot, or it speeds up on its own on a level table'),
      ('core', 'The marble stays in contact with the table top while it rolls.',
       'it floats above the surface, sinks into it, or rolls along without touching it'),
      ('major', 'The marble rotates as it advances, turning in the direction it travels.',
       'it slides across the table without rotating at all, or it spins against its direction of '
       'travel'),
      ('major', 'The marble holds one straight heading rather than curving or reversing with '
                'nothing acting on it.',
       'it swerves or turns back on itself on a level empty table'),
      ('minor', 'The marble stops or leaves the table rather than rolling on for ever.',
       'it is still rolling at exactly its starting speed as the shot ends after a long run'),
      marks('the marble', 'the coloured swirl and highlights inside the glass'),
      cons('the marble')),
    note="The benchmark's key standard 'the marble moves at a consistent speed' is wrong for a "
         "marble released on a level table: rolling resistance slows it. Note the benchmark is "
         "inconsistent with itself here -- for the spinning top (id 26) it correctly requires the "
         "motion to decay. This rubric requires the deceleration.")

add('pedalled-travel', 6,
    'A cyclist rides along a straight road.',
    S(('core', 'A cyclist is present, riding a bicycle.'),
      ('core', 'The cyclist travels along a road.'),
      ('core', 'The road runs straight rather than curving.'),
      ('minor', 'The cyclist stays on the bicycle for the whole shot.')),
    P(('core', "The wheels turn in the direction of travel, and they turn only while the bicycle "
               "is moving.",
       'the wheels are still while the bicycle advances, or they turn against the direction of '
       'travel'),
      ('core', 'Both wheels stay on the road surface and the bicycle stays upright under the rider.',
       'the bicycle floats above the road, or it stays upright with no wheel touching the ground'),
      ('major', 'Pedalling and travel go together: the cranks turn while the bicycle gains or '
                'holds speed, and the chain and rear wheel turn with them.',
       'the rider pedals backwards while moving forward, or the cranks spin with the bicycle '
       'standing still'),
      ('major', 'The bicycle holds one heading along the road rather than veering off and back '
                'with no steering input.',
       'it swerves across the road or reverses direction with the rider making no corresponding '
       'move'),
      ('minor', 'The rider leans and steers together: any lean is matched by a turn in the same '
                'direction.',
       'the rider leans hard one way while the bicycle continues dead straight'),
      marks('the bicycle', 'the frame, spokes and the rider'),
      cons('the bicycle and rider')),
    note="The benchmark's physics_prompt and key standards demand constant velocity ('equal "
         "distances in equal time intervals'), but the caption says only that the cyclist rides "
         "along a straight road -- a real cyclist may accelerate, coast or slow, and none of that "
         "is a physics violation. Requiring constant speed here would penalise correct clips, so "
         "this rubric judges the straight heading and the pedal-wheel-ground coupling instead and "
         "leaves the speed profile free.")

add('rolling-friction-decay', 7,
    'A kicked soccer ball rolls along the ground toward the goal.',
    S(('core', 'A soccer ball is present.'),
      ('core', 'The ball travels along the ground toward a goal.'),
      ('core', 'A goal is present as the thing it travels toward.'),
      ('minor', 'A kick or contact starts the ball moving, rather than the ball already being in '
                'motion from the first frame.')),
    P(('core', 'The ball leaves the foot in the direction the foot was travelling, and starts '
               'moving at the instant of contact.',
       'the ball starts moving before the foot reaches it, or it leaves at an angle unrelated to '
       'the kick',
       'the kick itself is shown'),
      ('core', 'The ball slows as it rolls along the ground.',
       'it holds exactly one speed all the way to the goal, or it speeds up on its own after the '
       'kick'),
      ('major', 'The ball rotates as it advances, turning in the direction it travels.',
       'it slides along the grass without rotating, or it spins against its direction of travel'),
      ('major', 'The ball stays on the ground and follows one heading rather than curving away or '
                'lifting off with nothing striking it.',
       'it rises into the air unstruck, or it bends sideways on level ground after the kick'),
      ('minor', 'The ball stays in contact with the surface it rolls over and follows its contour.',
       'it sinks into the turf or rolls a hand-width above it'),
      marks('the ball', 'the panel seams and printing'),
      cons('the ball')))


# ---- Parabolic Motion (8-14) --------------------------------------------
def arc(o):
    """The four observables every unpowered flight shares, plus the gravity fatal."""
    O = o[0].upper() + o[1:]
    return [
        ('fatal', f'{O} is pulled back down: it does not hang motionless in the air or keep '
                  f'drifting upward once released.',
         f'{o} stops in mid-air and stays there, or carries on rising with nothing driving it. If '
         f'the clip ends while it is still legitimately climbing, mark not_shown'),
        ('core', f'{O} rises to a highest point and then descends.',
         f'{o} climbs out of shot without ever topping out, or drops from the instant of release '
         f'with no rise at all'),
        ('core', f'{O} is slowest near the top of the flight and speeds up on the way down.',
         f'{o} covers equal distances at every stage of the arc, or it moves fastest at the top'),
        ('major', f'{O} keeps making sideways progress right through the flight, including at the '
                  f'top.',
         f'{o} stops dead in mid-air, hovers at the apex, or drops vertically from the top'),
        ('major', 'The path is one arc bending the same way throughout, curving over and down.',
         'the path kinks, loops, or bends upward again after the top with nothing striking it'),
    ]


add('projectile-arc', 8,
    'An athlete throws a javelin, which arcs up and comes down.',
    S(('core', 'A javelin is present.'),
      ('core', 'An athlete throws the javelin and it flies away from them.'),
      ('minor', 'The setting reads as an athletics competition or training ground.'),
      ('minor', 'The javelin starts in the hand rather than already being in flight.')),
    P(*arc('the javelin'),
      ('minor', "The throwing motion runs ahead of the release and sends the javelin the way the "
                "arm was travelling.",
       'the javelin leaves at an angle unrelated to the arm, or it departs before the arm reaches '
       'the release'),
      ('minor', 'The javelin stays roughly aligned with its own flight path, nose leading, and '
                'comes down point-first.',
       'it flies broadside or tail-first, or it lands flat while tracking a clean arc')))

add('projectile-arc', 9,
    'A juggler throws a ball up; it peaks and falls back to the hand.',
    S(('core', 'A ball is present.'),
      ('core', 'A person throws the ball up into the air.'),
      ('minor', 'The ball starts in the hand rather than already being aloft.'),
      ('minor', 'The person reads as juggling rather than merely holding the ball.')),
    P(*arc('the ball'),
      ('minor', 'The ball comes back down to about the height it was released from, and the hand '
                'moves to meet it.',
       'the ball returns to a completely different height, or the hand stays still while the ball '
       'lands in it anyway',
       'the catch is shown'),
      ('minor', 'The ball turns at a steady rate in flight, or not at all, rather than changing '
                'its spin in mid-air.',
       'the ball starts and stops spinning in mid-air with nothing touching it')))

add('projectile-arc', 10,
    'A basketball is shot from a distance and drops toward the hoop.',
    S(('core', 'A basketball is present.'),
      ('core', 'The ball is shot and travels through the air toward a hoop.'),
      ('core', 'A hoop is present as the target.'),
      ('minor', 'The shot is taken from well back rather than at the rim.')),
    P(*arc('the ball'),
      ('minor', 'The ball is descending, not rising, by the time it reaches the hoop.',
       'it arrives at the hoop still climbing, or it rises into the hoop from below'),
      ('minor', 'The net and rim move only where the ball touches them, and settle afterwards.',
       'the net swings before contact, or the rim bends and stays bent',
       'the ball reaches the hoop')))

add('projectile-arc', 11,
    'A stone is thrown across a river and lands in the water or on the far side.',
    S(('core', 'A stone is present.'),
      ('core', 'The stone is thrown and flies out over a river.'),
      ('core', 'A river or comparable body of moving water is present.'),
      ('minor', 'The throw starts from one bank rather than from over the water.')),
    P(*arc('the stone'),
      ('minor', 'The stone ends its flight by reaching the water or the far bank.',
       'it comes to rest in mid-air over the river, or fades out before reaching anything. If the '
       'clip ends while it is still in flight, mark not_shown'),
      ('minor', 'If it lands in the water, the splash appears where and when the stone meets the '
                'surface, and rings spread outward from that point.',
       'the splash appears away from the entry point, or before the stone arrives',
       'the stone lands in the water')))

add('firework-burst', 12,
    'A firework shell climbs, slows near the top, and bursts.',
    S(('core', 'A firework is present.'),
      ('core', 'The firework climbs into the sky.'),
      ('core', 'The firework bursts.'),
      ('minor', 'The launch starts from the ground rather than the shell already being high up.')),
    P(('fatal', 'The burst happens after the climb, not before it.',
       'the shell explodes on the ground or at the start of the ascent and then flies up'),
      ('core', 'The shell slows as it climbs, and it bursts near the top of its rise where it is '
               'moving slowest.',
       'it accelerates all the way up, or it bursts at full speed low in the climb'),
      ('core', 'The burst throws sparks outward from one point, roughly evenly in all directions.',
       'the sparks appear as a flat sheet, spread from somewhere other than the shell, or expand '
       'in one direction only'),
      ('major', 'Each spark then follows its own arc: it slows, curves over and falls.',
       'the sparks travel out in straight lines to the edge of frame, or hang in place where they '
       'stopped'),
      ('major', 'The sparks fade and thin out as they fall rather than staying equally bright to '
                'the end.',
       'the sparks keep full brightness indefinitely, or brighten as they fall'),
      ('minor', 'A trail of light or smoke marks the climb, and it lags behind the shell.',
       'the trail runs ahead of the shell, or the shell climbs leaving nothing behind'),
      ('minor', 'The burst lights the surrounding sky and smoke while it lasts, and that glow '
                'fades with it.',
       'the burst throws no light on anything around it although it is plainly bright')))

add('projectile-arc', 13,
    'A soccer player lofts the ball high; it climbs, peaks and drops.',
    S(('core', 'A soccer ball is present.'),
      ('core', 'A player kicks the ball and it flies up into the air.'),
      ('core', 'The ball goes high rather than staying along the ground.'),
      ('minor', 'The ball starts on or near the ground rather than already being aloft.')),
    P(*arc('the ball'),
      ('minor', 'The ball leaves the foot at the moment of contact and in the direction the foot '
                'was swinging.',
       'the ball leaves before the foot arrives, or it departs at an angle unrelated to the swing',
       'the contact is shown'),
      ('minor', 'The ball comes down onto the pitch or to a player rather than fading out aloft.',
       'it dissolves in mid-air or settles to a stop above the ground. If the clip ends while it '
       'is still in flight, mark not_shown')))

add('fountain-spray', 14,
    'A fountain throws water up in arcs that fall back down.',
    S(('core', 'A fountain is present.'),
      ('core', 'Water is thrown up into the air from it.'),
      ('core', 'The water follows a visible arc rather than only welling up or spilling over.'),
      ('minor', 'The water falls back into a basin, pool or surface below.')),
    P(*arc('the water'),
      ('minor', 'The jet is continuous from the nozzle and breaks into separate droplets only '
                'further along, mostly near and past the top.',
       'the water leaves the nozzle already as separated droplets, or it stays a solid rod all the '
       'way down'),
      ('minor', 'Droplets landing in the pool disturb it where they hit, and the disturbance '
                'spreads and dies away.',
       'the returning water leaves the pool surface completely undisturbed')))


# ---- Circular Motion (15-21) --------------------------------------------
def circ(o, ctr):
    """Continuous change of heading, and one direction of travel round the centre."""
    O = o[0].upper() + o[1:]
    return [
        ('core', f'{O} changes its direction of travel continuously, coming round {ctr} instead of '
                 f'running straight.',
         f'{o} travels in straight segments and snaps to a new heading at corners, or stops turning '
         f'part way round and carries on straight'),
        ('major', f'{O} keeps going round {ctr} the same way for the whole shot.',
         f'{o} reverses to the other way round with nothing acting on it'),
    ]


add('drift-oversteer', 15,
    'A car slides through a sharp turn with its rear stepped out.',
    S(('core', 'A car is present.'),
      ('core', 'The car goes round a sharp turn.'),
      ('core', 'The car slides rather than tracking the corner cleanly.'),
      ('minor', 'The car is moving under its own power rather than being pushed or towed.')),
    P(*circ('the car', 'the corner'),
      ('core', 'The car points somewhere other than where it is going: the body is turned into the '
               'corner while it travels along the arc, so the rear runs wide.',
       'the car stays exactly aligned with its path all the way round, which is cornering rather '
       'than drifting'),
      ('major', 'All four wheels stay on the road and the car stays the right way up.',
       'the car floats off the surface, or holds the slide with wheels off the ground'),
      ('minor', 'The sliding rear tyres make smoke or dust, and it comes off the tyres and trails '
                'behind them.',
       'smoke appears away from the tyres, or pours from stationary tyres before the slide starts'),
      ('minor', 'The front wheels are turned to catch the slide rather than pointing straight into '
                'the corner.',
       'the steering stays dead ahead through a full drift'),
      cons('the car')),
    note="The benchmark's key standards for this scenario ask only that 'the car follows a circular "
         "path' and 'the direction changes continuously' -- true of any cornering car and blind to "
         "what makes it a drift. The defining observable is the yaw: the body points into the "
         "corner while the car travels along the arc, with the rear tyres sliding. This rubric adds "
         "it as a core item.")

add('tethered-circular-motion', 16,
    'A struck tetherball circles the pole on a taut rope.',
    S(('core', 'A tetherball is present.'),
      ('core', 'A pole is present with the ball attached to it by a rope.'),
      ('core', 'The ball travels round the pole.'),
      ('minor', 'A hit sets the ball going rather than it already circling from the first frame.')),
    P(*circ('the ball', 'the pole'),
      ('core', 'The rope stays taut and straight from its anchor to the ball for as long as the '
               'ball is circling.',
       'the rope goes slack, sags, or stretches and shortens while the ball keeps circling at the '
       'same distance'),
      ('major', 'The rope stays attached at both ends: to the pole and to the ball.',
       'the rope detaches, passes through the pole, or joins the ball at a point that shifts around it'),
      ('minor', 'As the rope wraps onto the pole the ball comes in closer and goes round quicker; '
                'the loose length only ever decreases while it wraps.',
       'the wrapped rope pays back out on its own, or the ball circles at a fixed distance while '
       'the rope visibly wraps up'),
      ('minor', 'The pole stays planted and upright; it may flex, but it does not travel.',
       'the pole moves along with the ball or leans further each turn without springing back'),
      cons('the ball')))

add('bowl-oscillation-decay', 17,
    'A ball circles the inside of a bowl, dropping lower until it settles.',
    S(('core', 'A ball is present.'),
      ('core', 'A bowl or comparable curved container is present.'),
      ('core', 'The ball runs round the inside of the bowl.'),
      ('minor', 'The ball stays inside the bowl rather than leaving it.')),
    P(*circ('the ball', 'the inside of the bowl'),
      ('core', 'The ball works its way lower over time and ends up resting at the bottom, since '
               'friction takes energy out of it on every lap.',
       'it circles at exactly the same height indefinitely, or it climbs higher up the wall on its '
       'own. If the clip ends while it is still legitimately descending, mark not_shown'),
      ('major', 'The ball stays in contact with the bowl and follows its curve, riding higher where '
                'it is moving faster and lower where it is slower.',
       'the ball floats clear of the inner surface, cuts across the middle of the bowl in mid-air, '
       'or passes through the wall'),
      ('minor', 'The ball rolls rather than sliding: it turns as it travels round the wall.',
       'it slides round the bowl without ever rotating'),
      ('minor', 'The bowl itself stays put while the ball moves inside it.',
       'the bowl rocks, slides or spins along with the ball with nothing driving it'),
      cons('the ball')),
    note="The benchmark's key standards ask only that the ball 'moves in a circular path' and that "
         "the path 'aligns with the shape of the bowl'. Both are satisfied by a ball orbiting for "
         "ever at one height, which is the commonest wrong answer. The discriminating observable is "
         "the decay -- the ball loses height lap by lap and finishes at the bottom -- so this "
         "rubric makes it core.")

add('cornering-lean', 18,
    'A cyclist rides round a curve, leaning into it.',
    S(('core', 'A cyclist is present, riding a bicycle.'),
      ('core', 'The cyclist goes round a curve.'),
      ('core', 'A track or road provides the curve being followed.'),
      ('minor', 'The cyclist stays on the bicycle throughout.')),
    P(*circ('the cyclist', 'the curve'),
      ('core', 'The bicycle and rider lean toward the inside of the curve while turning, and come '
               'back upright as the curve ends.',
       'they stay bolt upright through a hard turn, or lean away from the inside of the curve'),
      ('major', 'Both wheels stay on the track surface and the front wheel is steered into the turn.',
       'the bicycle floats above the track, or the front wheel points out of the turn all the way '
       'round'),
      ('minor', 'The wheels turn in the direction of travel, and keep turning as long as the '
                'bicycle moves.',
       'the wheels sit still while the bicycle sweeps round the curve'),
      ('minor', 'The track surface and its markings stay fixed as the cyclist passes over them.',
       'the track slides or rotates along with the cyclist'),
      cons('the cyclist and bicycle')))

add('orbital-motion', 19,
    'A moon travels round a planet on a closed near-circular orbit.',
    S(('core', 'A moon is present.'),
      ('core', 'A planet is present, larger than the moon.'),
      ('core', 'The moon travels round the planet.'),
      ('minor', 'The setting reads as space rather than a sky seen from the ground.')),
    P(*circ('the moon', 'the planet'),
      ('core', 'The orbit closes on itself: the moon comes back round to where it began instead of '
               'spiralling inward or drifting away.',
       'the moon spirals into the planet, drifts off out of frame, or stops and hangs beside it'),
      ('major', 'The planet stays put at the middle of the motion rather than chasing the moon '
                'round.',
       'the planet swings round the moon, or wanders off while the moon holds station'),
      ('minor', 'The sunlit side of both bodies faces the same direction, and the moon can pass '
                'into the planet shadow rather than staying evenly lit all the way round.',
       'the moon and the planet are lit from opposite sides, or a fully lit face is turned away '
       'from the light'),
      ('minor', 'Both bodies keep their surface markings, which turn with them rather than sliding '
                'across them.',
       'the surface pattern drifts over the body or is repainted between moments'),
      cons('the moon')))

add('carousel-rotation', 20,
    'A child rides round on a turning merry-go-round.',
    S(('core', 'A child is present.'),
      ('core', 'A merry-go-round or comparable turning platform is present.'),
      ('core', 'The child is carried round by the platform.'),
      ('minor', 'The child stays on or holds onto the platform throughout.')),
    P(*circ('the child', 'the middle of the platform'),
      ('core', 'The child turns with the platform as one: their distance from the middle and their '
               'place on it stay the same, so they do not slide across it.',
       'the child slips backwards or forwards relative to the platform, or drifts toward or away '
       'from the middle while holding on'),
      ('major', 'Everything on the platform goes round together at the same rate, so parts further '
                'out sweep through more ground in the same time.',
       'different parts of one rigid platform complete their laps at different times, or the rim '
       'and the middle turn opposite ways'),
      ('minor', 'The child leans or is pulled outward while turning, and hair or loose clothing '
                'trails behind the direction of travel.',
       'hair and clothing hang straight down as if nothing were moving, or stream ahead of the '
       'direction of travel'),
      ('minor', 'The ground and surroundings stay fixed; only the platform and its riders turn.',
       'the ground turns with the platform, or the surroundings spin the other way'),
      cons('the child')))

add('orbital-motion', 21,
    'A satellite circles Earth on a closed orbit.',
    S(('core', 'A satellite is present.'),
      ('core', 'Earth is present.'),
      ('core', 'The satellite travels round Earth.'),
      ('minor', 'The satellite is above the atmosphere rather than flying within a visible sky.')),
    P(*circ('the satellite', 'Earth'),
      ('core', 'The orbit closes and holds: the satellite neither spirals down toward Earth nor '
               'drifts away, and it does not come to a stop.',
       'the satellite falls in toward the surface, wanders off out of frame, or halts and hovers '
       'over one spot while plainly in motion beforehand'),
      ('major', 'Nothing holds the satellite up: there is no plume, support or cable, and it coasts.',
       'the satellite is shown thrusting continuously to stay in orbit, or rests on something'),
      ('minor', 'The satellite keeps one attitude relative to its path or turns steadily; solar '
                'panels and antennas stay attached and move with the body.',
       'the panels flap free of the body, or the satellite tumbles and then abruptly holds still '
       'with nothing acting on it'),
      ('minor', 'Earth is lit from one side, and the satellite is lit from that same side; it can '
                'pass into darkness behind the planet.',
       'the satellite is lit from the opposite side to Earth, or stays evenly bright while crossing '
       'the night side'),
      cons('the satellite')))


# ---- Rotational Motion (22-28) ------------------------------------------
def rot(o, ax):
    """Fixed axis, rigid body, one direction of rotation."""
    O = o[0].upper() + o[1:]
    return [
        ('core', f'{O} turns about {ax}, and that axis stays where it is.',
         f'the axis wanders across the scene, or {o} turns about a different point from one moment '
         f'to the next'),
        ('major', f'{O} turns as one rigid piece: its parts keep their spacing and their shape as '
                  f'they come round.',
         'parts stretch, lag behind one another, or change their spacing as they turn'),
        ('major', f'{O} keeps turning the same way for as long as it turns.',
         'the rotation reverses with nothing acting on it'),
    ]


add('spin-up-from-rest', 22,
    'A helicopter spins up its rotor and lifts off the ground.',
    S(('core', 'A helicopter is present.'),
      ('core', 'The helicopter leaves the ground.'),
      ('minor', 'It starts on the ground rather than already being airborne.'),
      ('minor', 'The rotor is visible rather than out of frame.')),
    P(*rot('the rotor', 'the mast above the cabin'),
      ('core', 'The rotor turns faster and faster before the helicopter leaves the ground, and it '
               'is still turning while the machine is in the air.',
       'the helicopter rises with the rotor stationary or barely moving, or the rotor reaches full '
       'speed only after lift-off'),
      ('major', 'Lift-off is gradual and roughly vertical at first: the machine unsticks, rises, '
                'and does not shoot up instantly from rest.',
       'the helicopter is launched upward at full speed from the first frame, or slides off '
       'sideways along the ground as it rises'),
      ('minor', 'Downwash shows below the rotor: grass, dust or water beneath is pushed outward and '
                'down while it hovers, and settles when it climbs away.',
       'the ground beneath is completely undisturbed under a running rotor'),
      ('minor', 'The tail rotor turns as well while the main rotor runs, and the fuselage does not '
                'spin round under the mast.',
       'the fuselage rotates steadily about the mast the opposite way to the rotor')))

add('free-spin-decay', 23,
    'A bicycle wheel hangs in the air and spins on its axle, slowing.',
    S(('core', 'A bicycle wheel is present.'),
      ('core', 'The wheel spins.'),
      ('core', 'The wheel is held clear of the ground rather than rolling on a surface.'),
      ('minor', 'The wheel stays in the same place while it spins.')),
    P(*rot('the wheel', 'its own axle'),
      ('core', 'The wheel stays where it is: it spins without travelling anywhere.',
       'the wheel rolls away, drifts across the frame, or falls while continuing to spin evenly'),
      ('major', 'The spin gradually slows, since only the bearing and the air act on it and nothing '
                'drives it.',
       'the wheel spins at exactly one rate indefinitely with nothing driving it, or it speeds up on '
       'its own'),
      ('minor', 'The spokes stay straight and evenly spaced and blur or strobe together rather than '
                'individually.',
       'spokes bend, cross, vanish, or change in number as the wheel turns'),
      ('minor', 'Marks on the wheel -- the valve, a label, a scuff on the tyre -- come round with it '
                'once per turn.',
       'such marks stay fixed in place while the wheel turns past them, or slide around the rim')))

add('wind-driven-rotation', 24,
    'A steady wind turns the blades of a windmill about its axis.',
    S(('core', 'A windmill is present.'),
      ('core', 'Its blades turn.'),
      ('minor', 'Wind is evident in the scene, for instance in grass, trees or cloth.'),
      ('minor', 'The windmill stands on the ground rather than floating.')),
    P(*rot('the blade assembly', 'the hub at the front of the mill'),
      ('core', 'The blades turn only while wind is acting: they are still or slow before the wind '
               'shows and turn once it does.',
       'the blades spin at full speed in air that is plainly dead still, or stop dead while the wind '
       'keeps blowing'),
      ('major', 'All the blades sweep round together at the same rate and keep their angle to the '
                'hub.',
       'one blade lags, overtakes or turns the other way, or the blades change their pitch each '
       'revolution'),
      ('minor', 'Other things in the scene respond to the same wind and lean the same way as it: '
                'grass, leaves or cloth move consistently with the direction driving the blades.',
       'the surroundings show wind from one direction while the mill is driven from another'),
      ('minor', 'The tower and the ground stay still; only the blade assembly turns.',
       'the tower twists round with the blades or sways in step with them')))

add('spin-up-from-rest', 25,
    'A ceiling fan is switched on and its blades spin up from rest.',
    S(('core', 'A ceiling fan is present.'),
      ('core', 'The blades begin to turn.'),
      ('minor', 'The blades are at rest at the start rather than already spinning.'),
      ('minor', 'The fan is mounted to a ceiling rather than standing free.')),
    P(*rot('the blade assembly', 'the central hub of the fan'),
      ('core', 'The blades start from rest and build up speed, rather than jumping straight to full '
               'speed.',
       'the blades are already at full speed in the frame after being still, with no build-up'),
      ('major', 'The blades keep their spacing and stay level as they come round; the fan stays '
                'attached to the ceiling.',
       'blades bend upward, drift apart, or the fan detaches while still running'),
      ('minor', 'Air moves below the fan once it is running: light things in the room stir, and '
                'they do not stir before it starts.',
       'hanging or loose objects blow strongly before the blades move at all'),
      ('minor', 'The blades stay opaque and hold their shape as they speed up, blurring together '
                'rather than disappearing or multiplying.',
       'the blade count changes, or blades pass through one another as the fan speeds up')))

add('spinning-top', 26,
    'A top spins upright on the floor, wobbles as it slows, and falls over.',
    S(('core', 'A spinning top is present.'),
      ('core', 'The top spins on the floor.'),
      ('core', 'A person sets it spinning.'),
      ('minor', 'The top starts at rest in the hand rather than already spinning.')),
    P(*rot('the top', 'its own upright axis'),
      ('core', 'The spin slows over time, since friction at the tip and the air take energy out of '
               'it.',
       'the top spins at exactly one rate for the whole shot with nothing driving it, or it speeds '
       'up on its own'),
      ('major', 'It stands nearly upright while spinning fast, then leans and wobbles more as it '
                'slows, and finally topples and comes to rest.',
       'it topples at full speed, or it stays perfectly upright and then simply stops standing. If '
       'the clip ends while it is still spinning fast, mark not_shown'),
      ('minor', 'The tip stays on the floor throughout; the top may wander a little across the '
                'surface but it does not lift off.',
       'the top hovers above the floor, or sinks into it'),
      ('minor', 'Painted bands or patterns on the top come round with it and blur into rings while '
                'it is fast.',
       'the pattern stays fixed in place while the body turns beneath it')))

add('driven-constant-rotation', 27,
    'A Ferris wheel turns steadily about its hub with cabins hanging from the rim.',
    S(('core', 'A Ferris wheel is present.'),
      ('core', 'The wheel turns.'),
      ('core', 'Cabins or seats are carried on the wheel.'),
      ('minor', 'The setting reads as a fairground or amusement park.')),
    P(*rot('the wheel', 'its central hub'),
      ('core', 'The cabins hang from their mountings and stay upright all the way round, rather '
               'than turning over with the rim.',
       'the cabins rotate with the wheel and are upside down at the top'),
      ('major', 'The wheel turns steadily and slowly at one rate, and every cabin goes round in the '
                'same time.',
       'the wheel surges and stalls with nothing changing, or cabins on the same rim complete their '
       'laps at different rates'),
      ('minor', 'The wheel stays on its supports and the supports stay planted; only the wheel '
                'turns.',
       'the frame rotates with the wheel, or the whole structure drifts across the ground'),
      ('minor', 'Lights and paintwork on the rim travel round with the structure they are fixed to.',
       'lit patterns slide across the rim independently of the metalwork carrying them')))

add('driven-constant-rotation', 28,
    'A record turns at a steady rate on a turntable while it plays.',
    S(('core', 'A record is present.'),
      ('core', 'The record turns on a turntable.'),
      ('core', 'The turntable is set up for playing, with an arm or stylus present.'),
      ('minor', 'The record lies flat on the platter rather than floating above it.')),
    P(*rot('the record', 'the spindle at its centre'),
      ('core', 'The record turns at one steady rate while it plays, since a driven platter holds '
               'its speed.',
       'the record speeds up and slows repeatedly, or stops and restarts, with nothing touching it'),
      ('major', 'The label and the grooves turn with the disc as one, so the label spins with it '
                'rather than staying readable.',
       'the label stays upright and still while the disc turns under it, or the groove pattern slides '
       'across the surface'),
      ('minor', 'The arm rests on the record and creeps slowly inward as it plays; it does not go '
                'round with the disc.',
       'the arm sweeps round with the record, hovers clear of the surface, or tracks outward toward '
       'the rim'),
      ('minor', 'The record stays centred on the spindle and flat on the platter.',
       'the disc drifts off centre, rocks, or lifts while continuing to turn evenly')))


# ---- Combined Translational and Rotational Motion (29-35) ---------------
def selfroll(o):
    """A body that is itself the roller: rotation tied to its own travel."""
    O = o[0].upper() + o[1:]
    return [
        ('core', f'{O} rotates as it advances, turning the way that carries it forward.',
         f'{o} slides along without rotating at all, or rotates against its direction of travel'),
        ('core', 'The amount of turning goes with the ground covered: it neither spins on the spot '
                 'while sliding along nor covers a long distance with barely any rotation.',
         'the rotation bears no relation to the distance covered, for instance spinning quickly '
         'while creeping forward'),
        ('major', f'{O} stays in contact with the surface it rolls on and follows its contour.',
         f'{o} floats above the surface or sinks into it while rolling'),
    ]


def roll(o, w, pl=True):
    """A body carried on wheels: wheel rotation tied to the body's travel."""
    O, W = o[0].upper() + o[1:], w[0].upper() + w[1:]
    turn, stay = ('turn', 'stay') if pl else ('turns', 'stays')
    return [
        ('core', f'{W} {turn} while {o} advances and {stay} still once it stops.',
         f'{w} {stay} motionless while {o} slides forward, or {turn} on after it has come to a stop'),
        ('core', f'{W} {turn} the way that carries {o} in the direction it is actually going.',
         f'{w} {turn} backwards relative to the direction of travel'),
        ('major', f'The amount {w} {turn} goes with the ground covered: {o} neither spins them many '
                  f'times almost on the spot nor travels a long way with barely any turning.',
         f'the turning of {w} bears no relation to the distance {o} covers'),
        ('major', f'{W} {stay} in contact with the ground and carry {o} along.',
         f'{o} floats clear of the surface, or {w} sink into the ground while it moves'),
    ]


add('wind-driven-tumbling', 29,
    'A tumbleweed is blown across the desert, rolling and bouncing as it goes.',
    S(('core', 'A tumbleweed is present.'),
      ('core', 'It travels across the ground.'),
      ('core', 'The setting reads as desert or comparable dry open ground.'),
      ('minor', 'Wind is evident in the scene, for instance in dust, grass or the tumbleweed itself.')),
    P(('core', 'It rotates as it travels, turning the way it is going rather than sliding along '
               'rigidly.',
       'it slides across the ground without turning, or turns against its direction of travel'),
      ('core', 'It travels downwind, consistent with whatever else in the scene shows the wind.',
       'it travels against the direction the dust and plants show the wind going, or it moves in '
       'plainly dead-still air'),
      ('major', 'Being light and open, it skitters: it hops off the ground, changes speed as it '
                'catches and releases, and its course is irregular.',
       'it tracks a perfectly even straight line at one unchanging speed like a rigid wheel'),
      ('major', 'It keeps returning to the ground between hops rather than sailing steadily through '
                'the air.',
       'it flies on at a constant height without touching down'),
      ('minor', 'It kicks up dust or disturbs loose material where it strikes the ground.',
       'it leaves the sand completely untouched at every bounce'),
      ('minor', 'Its tangled branches keep their arrangement as it turns rather than being redrawn.',
       'the branch pattern changes shape from one moment to the next'),
      cons('the tumbleweed')))

add('rolling-without-slipping', 30,
    'A tyre rolls along the street on its own.',
    S(('core', 'A tyre is present.'),
      ('core', 'The tyre rolls along the ground.'),
      ('core', 'It rolls on its own rather than being carried on a vehicle.'),
      ('minor', 'The setting reads as a street or road.')),
    P(*selfroll('the tyre'),
      ('core', 'The tyre stands up on its tread while rolling quickly, and leans and falls over as '
               'it slows.',
       'it rolls along lying flat on its side, or it topples while still rolling fast. If the clip '
       'ends while it is still rolling quickly, mark not_shown'),
      ('major', 'It slows as it rolls, since nothing drives it.',
       'it holds exactly one speed for the whole shot, or speeds up on its own on level ground'),
      ('minor', 'The tread pattern and any lettering on the sidewall come round with the tyre.',
       'the tread or lettering stays fixed in place while the tyre rolls past'),
      cons('the tyre')))

add('rolling-without-slipping', 31,
    'A bowling ball rolls down the lane toward the pins.',
    S(('core', 'A bowling ball is present.'),
      ('core', 'The ball rolls along a lane.'),
      ('core', 'Pins are present ahead of it.'),
      ('minor', 'The ball is released by a person or is already travelling down the lane, rather '
                'than appearing in mid-lane.')),
    P(*selfroll('the ball'),
      ('core', 'The ball keeps travelling toward the pins and reaches them.',
       'it stops in the middle of the lane, backs up, or fades out before arriving. If the clip ends '
       'while it is still legitimately travelling, mark not_shown'),
      ('major', 'The ball holds one heading, or curves smoothly and consistently in one direction; '
                'any curve matches the way it is spinning.',
       'it swings back and forth across the lane, or bends one way while spinning the other'),
      ('minor', 'The finger holes and any marbling in the ball come round with it as it rolls.',
       'the holes stay fixed on the face toward the camera while the ball plainly rolls forward'),
      ('minor', 'The pins are knocked away from the point of impact and fall outward from there; '
                'unhit pins nearby may be struck in turn.',
       'the pins fall before the ball arrives, fall toward the ball, or stand untouched through a '
       'direct strike',
       'the ball reaches the pins'),
      cons('the ball')))

add('rolling-without-slipping', 32,
    'A soccer ball rolls across the field, spinning as it goes.',
    S(('core', 'A soccer ball is present.'),
      ('core', 'The ball rolls along the ground.'),
      ('core', 'The setting reads as a pitch or field.'),
      ('minor', 'The ball travels a fair distance rather than only shifting in place.')),
    P(*selfroll('the ball'),
      ('core', 'The ball slows as it rolls across the grass, since nothing drives it.',
       'it holds exactly one speed the whole way, or it speeds up on its own on level ground'),
      ('major', 'It holds one heading on level ground rather than swerving or turning back with '
                'nothing touching it.',
       'it changes direction unstruck, or rises off the ground while rolling'),
      ('minor', 'The panel seams and printing come round with the ball once per turn.',
       'the markings stay fixed on the visible face while the ball rolls forward'),
      cons('the ball')))

add('rolling-without-slipping', 33,
    'A wheelbarrow is pushed along a path, its wheel turning as it goes.',
    S(('core', 'A wheelbarrow is present.'),
      ('core', 'The wheelbarrow moves along a path.'),
      ('core', 'A person pushes it.'),
      ('minor', 'The setting reads as a garden or comparable planted ground.')),
    P(*roll('the wheelbarrow', 'the wheel', pl=False),
      ('core', 'The person is behind it holding the handles, and it moves only while they push; the '
               'barrow goes where they steer it.',
       'the barrow travels on its own with nobody in contact, or moves while the person stands still '
       'holding it'),
      ('major', 'While moving it is tipped back onto its wheel, with the legs clear of the ground, '
                'and it settles onto them when it is set down.',
       'it slides along on its legs while the wheel turns freely in the air'),
      ('minor', 'Anything in the tray stays in it and shifts only when the barrow tips or jolts.',
       'the load floats above the tray, or spills without the barrow tilting or striking anything'),
      cons('the wheelbarrow')))

add('rolling-without-slipping', 34,
    'A car drives forward, its wheels turning with its travel.',
    S(('core', 'A car is present.'),
      ('core', 'The car moves forward.'),
      ('minor', 'The wheels are visible rather than hidden from view.'),
      ('minor', 'The car travels on a surface rather than through the air.')),
    P(*roll('the car', 'the wheels'),
      ('core', 'All the wheels turn together at rates consistent with one another while the car '
               'travels straight.',
       'wheels on the same car turn at plainly different rates, or some turn while others are still, '
       'on straight level ground'),
      ('major', 'The body stays level above the wheels and follows where the front wheels point.',
       'the body drifts sideways with the wheels pointing straight, or floats up and down '
       'independently of the wheels'),
      ('minor', 'The tread and the wheel trim come round with the wheel rather than staying put.',
       'the wheel pattern stays fixed while the wheel plainly rotates'),
      cons('the car')),
    note="The benchmark's second key standard here asks that 'the point of contact between each "
         "wheel and the ground should momentarily appear stationary relative to the ground'. That is "
         "the correct physics of rolling without slipping, but it is not judgeable from a generated "
         "clip -- resolving an instantaneously stationary contact patch needs frame rates and "
         "sharpness these videos do not have, so an annotator can only guess. This rubric keeps the "
         "same physics in a form that is visible: rotation direction matched to travel, rotation "
         "amount commensurate with distance covered, and wheels never spinning backwards while the "
         "car goes forward.")

add('rolling-without-slipping', 35,
    'A rolling suitcase is wheeled along, its wheels turning as it travels.',
    S(('core', 'A wheeled suitcase is present.'),
      ('core', 'The suitcase travels across the floor.'),
      ('core', 'A person pulls or pushes it.'),
      ('minor', 'The setting reads as an airport or comparable terminal.')),
    P(*roll('the suitcase', 'the wheels'),
      ('core', 'The suitcase follows the person holding the handle and keeps pace with them.',
       'it moves off on its own with nobody holding it, or lags and catches up while the handle stays '
       'rigid in the hand'),
      ('major', 'It is tilted back on its wheels while being pulled, or stays upright on all its '
                'wheels while pushed, and it stays that way rather than switching about.',
       'it is dragged flat on its side while the wheels turn, or stands vertically with no wheel '
       'touching the floor'),
      ('minor', 'The handle stays at a fixed length while in use and the case body keeps its shape.',
       'the handle telescopes in and out on its own, or the case squashes and springs back as it '
       'rolls'),
      cons('the suitcase')))
