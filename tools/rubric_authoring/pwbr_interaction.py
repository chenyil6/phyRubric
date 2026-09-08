# phyworldbench 36-70: Interaction Dynamics.
# Items are derived from the caption (the bare event prompt) plus first-principles physics;
# SRC[i]['physics_prompt'] and SRC[i]['key_standards'] were then diffed for coverage. Where
# they conflict with physics, the rubric follows physics and says so in `note`.
# SA follows basic_standards['Event'] where it is narrower than the outcome, so an outcome the
# caption does not name (bouncing, crumpling, shattering) is judged by PC, not SA.

def cons(o):
    return ('fatal',
            f'{o[0].upper()}{o[1:]} keeps its own shape and identity for the whole shot, and it '
            f'does not pass through any solid surface.',
            f'{o} turns into a different object, passes through something solid, or disappears '
            f'and re-appears')


def soft(o):
    return ('fatal',
            f'{o[0].upper()}{o[1:]} stays one continuous piece of the same material and does not '
            f'pass through any solid surface.',
            f'{o} splits into unrelated pieces, turns into another material, or passes through the '
            f'surface it rests on')


def nointer(pair):
    return ('fatal',
            f'{pair[0].upper()}{pair[1:]} meet surface to surface: they never overlap, merge, or '
            f'pass through each other.',
            f'{pair} overlap, merge into one body, or pass through each other at contact')


def nojump(o):
    return ('major',
            f'{o[0].upper()}{o[1:]} moves from each position to the next along a connected path.',
            f'{o} jumps to a different place between frames rather than travelling there')


def marks(o, mk):
    return ('minor',
            f'{mk[0].upper()}{mk[1:]} stay attached to {o} and move with it.',
            f'{mk} slide across the surface, detach, or change from one moment to the next')


def before(a, b):
    return ('core',
            f'{a[0].upper()}{a[1:]} changes how it is moving only when {b} reaches it, not before.',
            f'{a} is deflected, set moving or thrown back before contact is made')


# ---- Collisions (36-42) --------------------------------------------------
add('body-tackle-collision', 36,
    'Two running players collide body to body; both are deflected and they stay engaged.',
    S(('core', 'Two football players are present.'),
      ('core', 'The two players come together and make body contact with each other.'),
      ('minor', 'At least one of them is moving toward the other before contact.'),
      ('minor', 'The setting reads as a football field or pitch.')),
    P(nointer('the two players'),
      ('core', 'Both players change how they are moving at the moment of contact: at least one is '
               'slowed, deflected or knocked off balance.',
       'they collide and both carry on exactly as before, as if nothing had passed between them'),
      before('a player', 'the other'),
      ('major', 'The pair together carries on in the direction of whichever player was driving '
                'harder, rather than both being thrown back the way they came.',
       'both players rebound backwards along their own approach directions while still locked '
       'together'),
      ('major', 'Both players stay on their legs while running, feet pushing off the ground, '
                'rather than gliding along.',
       'a player slides forward with their legs still or their feet clear of the ground'),
      ('minor', 'Loose kit and hair are jolted at the moment of impact.',
       'helmets, jerseys and hair stay perfectly still through a heavy collision'),
      ('minor', 'The turf is disturbed where they plant their feet or land.',
       'the ground stays untouched where studs plainly dig in',
       'the ground under their feet is in view')))

add('elastic-ball-collision', 37,
    'One ball strikes another; they touch without overlapping and both leave along new directions.',
    S(('core', 'Two billiard balls are present.'),
      ('core', 'The two balls come together and collide.'),
      ('minor', 'At least one ball is moving before the contact.'),
      ('minor', 'The setting reads as a billiard or pool table.')),
    P(nointer('the two balls'),
      ('core', 'The struck ball is set moving by the contact, and it starts moving at the moment of '
               'contact.',
       'the second ball rolls away before the first one reaches it, or stays put after a solid hit'),
      ('core', "The striking ball's motion changes at contact: it slows, stops or is deflected.",
       'the first ball carries straight on at its original speed as though the second were not there'),
      ('major', 'The struck ball leaves along the line joining the two centres at contact, i.e. '
                'away from the side it was struck on.',
       'the struck ball sets off back toward the ball that hit it, or at right angles to the push'),
      ('major', 'Both balls stay down on the cloth throughout.',
       'a ball floats above the table surface or sinks into it'),
      marks('the ball', 'the numbers and stripes on each ball'),
      ('minor', 'The balls lose speed gradually as they roll on across the cloth.',
       'a ball rolls on at exactly its original speed until the shot ends',
       'the balls stay in view for a while after the collision')),
    note="Their physics_prompt and key standard 3 require the balls to 'move in opposite "
         "directions after the collision'. That is only true of a head-on hit, and even then two "
         "equal balls exchange velocities so the striker stops rather than reversing; any cut shot "
         "sends both balls off to the same side at an angle. Scoring a correct angled break as a "
         "failure would be the wrong way round, so this rubric asks instead for the struck ball to "
         "leave along the line of centres, which is what actually holds.")

add('crash-crumple', 38,
    'A car strikes a fixed barrier, crumples at the front and is stopped abruptly.',
    S(('core', 'A car is present.'),
      ('core', 'The car strikes a barrier.'),
      ('core', 'The barrier is a fixed obstacle standing in the car path.'),
      ('minor', 'The car is moving toward the barrier before impact.')),
    P(('fatal', 'The barrier stops the car body: the car does not pass through it.',
       'the car drives through the barrier as though it were not solid'),
      ('core', 'The front of the car deforms at impact -- panels crumple, fold or break up -- '
               'while the rest of the body holds together.',
       'the car strikes hard and stays perfectly undamaged, or the whole car squashes evenly like '
       'a soft block'),
      ('core', 'The car loses its speed abruptly at the barrier instead of carrying on.',
       'the car continues past the barrier at cruising speed'),
      ('major', 'The damage is on the part of the car that met the barrier.',
       'the deformation appears on a panel that never touched the barrier'),
      ('major', 'The crumpling is permanent: the crushed panels stay crushed.',
       'the folded front springs back to its original shape after the impact'),
      ('major', 'The barrier is not flung away as though it weighed nothing.',
       'the barrier is thrown off like a light prop while the car is left untouched'),
      ('minor', 'The car body dips forward on its suspension as it is stopped.',
       'the body stays rigidly level through a violent stop'),
      ('minor', 'Loose debris is thrown forward from the impact and then falls to the ground.',
       'fragments hang in the air or drift upward after the impact',
       'pieces come off the car')))

add('bounce-decay', 39,
    'A dropped ball hits the ground and bounces, each bounce lower than the last.',
    S(('core', 'A basketball is present.'),
      ('core', 'The ball falls and reaches the ground.'),
      ('minor', 'The ball starts from a drop or a release rather than a throw or a kick.'),
      ('minor', 'The ground or court surface it lands on is visible.')),
    P(cons('the ball'),
      ('core', 'The ball rebounds off the ground, and each bounce reaches a lower peak than the '
               'one before.',
       'the ball lands and stays put with no rebound at all, or every bounce reaches the same '
       'height, or each rebound goes higher than the last'),
      ('core', 'The ball speeds up while falling and slows while rising between bounces.',
       'the ball travels up and down at one unchanging speed'),
      ('major', 'The ball reverses direction at the ground and nowhere else.',
       'the ball turns round in mid-air before reaching the ground'),
      ('major', 'The intervals between successive bounces get shorter as the bounces get lower.',
       'the ball spends just as long in the air on the small late bounces as on the first big one'),
      marks('the ball', 'the seams and lettering on the ball'),
      ('minor', 'The ball flattens slightly where it presses on the ground and springs back out.',
       'the ball stays a perfect rigid sphere at the moment it is pressed against the floor',
       'the contact is close enough to see the ball outline clearly')))

add('off-centre-collision-spin', 40,
    'Two toy cars meet on a track; one is set spinning and the other goes off in a new direction.',
    S(('core', 'Two toy cars are present.'),
      ('core', 'The two cars collide with each other.'),
      ('core', 'A track is present and the cars run along it.'),
      ('minor', 'At least one car is moving before the collision.')),
    P(nointer('the two cars'),
      ('core', "Each car's motion changes at the collision: their speeds or directions are not the "
               'same after contact as before.',
       'the cars touch and both carry on along their original lines at their original speeds'),
      before('a car', 'the other'),
      ('core', 'Any spin starts at the collision, from the cars meeting off-centre.',
       'a car is already spinning before the impact, or starts to spin with nothing touching it'),
      ('major', 'Each car is pushed away from the side it was struck on.',
       'a car is driven back toward the car that hit it'),
      ('major', 'The cars stay on their wheels and on the track surface unless the impact plainly '
                'flips them.',
       'a car floats above the track or sinks into it'),
      ('minor', 'The wheels of a rolling car turn in the direction it travels.',
       'the wheels stay locked while a car rolls along the track'),
      ('minor', 'A car left spinning slows its spin as it goes.',
       'a car spins on at exactly the same rate until the shot ends',
       'a car is left spinning in view')))

add('impact-dent', 41,
    'A block falls onto a metal plate, lands hard, barely rebounds and marks the surface.',
    S(('core', 'A metal block is present.'),
      ('core', 'The block falls and strikes a metal plate.'),
      ('core', 'A flat metal plate is present as the surface it lands on.'),
      ('minor', 'The block starts above the plate and falls, rather than being placed on it.')),
    P(cons('the block'),
      ('core', 'The block speeds up as it falls.',
       'it descends at one steady speed like a lift, or slows on the way down'),
      ('core', 'The block stops at the surface of the plate rather than continuing into it.',
       'the block sinks into the plate or passes through it'),
      ('major', 'Both pieces read as stiff metal: the block keeps its shape and the plate does not '
                'fold like cloth.',
       'the block squashes like clay, or the plate ripples like fabric at impact'),
      ('major', 'Any rebound is small: the block hops a little at most and settles quickly.',
       'the block bounces back up toward the height it was dropped from'),
      ('major', 'A mark or dent left on the plate is at the spot the block struck, and it stays '
                'there.',
       'the mark appears away from the point of contact, or fades back to a pristine surface',
       'a mark or dent appears on the plate'),
      ('minor', 'The plate is jolted, rings or shivers at the moment of impact.',
       'the plate shows no reaction whatever at the instant of contact'),
      ('minor', 'The block ends up resting in contact with the plate.',
       'the block comes to rest hovering just above the plate')))

add('kick-then-ball-collision', 42,
    'A kick sends one ball into a second rolling ball; both leave along new directions.',
    S(('core', 'A child is present.'),
      ('core', 'The child kicks a soccer ball.'),
      ('core', 'The kicked ball reaches a second ball and collides with it.'),
      ('minor', 'The second ball is already rolling before the collision.')),
    P(nointer('the two balls'),
      ('core', 'The ball starts moving when the foot meets it, and it moves off in the direction '
               'the foot swings.',
       'the ball sets off before the foot arrives, or leaves in a direction unrelated to the kick'),
      ('core', 'Both balls change direction or speed at the moment they touch each other.',
       'the two balls meet and each carries on exactly as it was'),
      ('major', 'Each ball leaves the contact on the far side from where the other struck it.',
       'a ball is pushed back toward the side its partner came from'),
      ('major', 'The kicking leg swings through the ball while the child stays balanced on the '
                'other foot.',
       'the ball flies off while the leg never moves, or the legs pass through each other'),
      ('minor', 'Both balls roll along the ground rather than skidding without turning.',
       'a ball slides across the ground with its markings never coming round'),
      ('minor', 'The balls lose speed as they roll on after the collision.',
       'a ball rolls on at exactly the same speed until the shot ends',
       'the balls stay in view after the collision')))

# ---- Friction and Sliding (43-49) ---------------------------------------
add('loss-of-traction-skid', 43,
    'A car on ice loses grip: it slides off its heading instead of tracking where the wheels point.',
    S(('core', 'A car is present.'),
      ('core', 'The car drives along a road.'),
      ('core', 'The road surface reads as icy or snow-covered.'),
      ('minor', 'The surroundings read as cold -- snow, frost or bare winter ground.')),
    P(cons('the car'),
      ('core', 'The ice costs the car grip: at some point it slides, its direction of travel '
               'parting from where the wheels point, or it keeps sliding where a dry road would '
               'have held it.',
       'the car tracks the icy surface with exactly the grip of dry tarmac for the whole shot'),
      ('core', 'The car stays on the road surface with its wheels down on it.',
       'the car floats above the ice or sinks into it'),
      ('major', 'While sliding the car keeps going the way it was already travelling rather than '
                'instantly following its nose.',
       'the direction of travel snaps round to wherever the car is pointed, even mid-slide'),
      ('major', 'A wheel may lock and skid, but no wheel turns backwards while the car moves '
                'forward.',
       'the wheels rotate backwards while the car travels forward'),
      ('minor', 'The body leans and rocks on its suspension as it slides and turns.',
       'the body stays rigidly level throughout a slide'),
      ('minor', 'Loose snow or slush is thrown up where the tyres meet the surface.',
       'the tyres pass through deep loose snow without disturbing any of it',
       'there is loose snow or slush on the road')))

add('slope-slide-with-friction', 44,
    'A sled slides down a snowy slope, gaining speed on the slope and losing it on the flat.',
    S(('core', 'A sled is present.'),
      ('core', 'The sled slides down a slope.'),
      ('core', 'The slope is snow-covered.'),
      ('minor', 'The sled starts higher up and ends lower down.')),
    P(cons('the sled'),
      ('core', 'The sled picks up speed while it is on the slope: gravity along a snowy slope '
               'beats the friction of the runners.',
       'the sled slows down steadily all the way down the slope, or descends at one fixed speed as '
       'though being lowered'),
      ('core', 'The sled stays on the snow surface, sliding on its runners or its base.',
       'the sled floats above the snow or sinks through it'),
      ('major', 'The sled travels downhill and its path follows the surface it is on.',
       'the sled drifts uphill, or cuts through open air away from the slope surface'),
      ('major', 'The sled slows and stops where the ground levels out or the snow deepens.',
       'the sled stops dead in the middle of the steep part with nothing in its way',
       'the sled reaches level ground or an obstacle within the shot'),
      ('minor', 'Snow is disturbed along the track -- spray at the runners or a trail behind.',
       'the sled slides over loose snow leaving it perfectly undisturbed'),
      ('minor', 'A rider moves with the sled and is pressed back as it gains speed.',
       'the rider stays bolt upright and detached from the sled motion',
       'someone is riding the sled')),
    note="Their physics_prompt and key standard 1 require the sled to decelerate as it goes down "
         "the hill ('gradually slowing as friction increases'). That is backwards: on a snowy "
         "slope the along-slope component of gravity exceeds runner friction, which is the whole "
         "reason sledding works, so the sled accelerates while descending and only decelerates on "
         "the runout. Following their standard would score a correct clip as a failure, so this "
         "rubric requires acceleration on the slope and puts the deceleration where it belongs.")

add('push-then-friction-stop', 45,
    'A pushed box slides across a floor and stops soon after the push ends.',
    S(('core', 'A box is present.'),
      ('core', 'The box slides across the floor.'),
      ('core', 'Something pushes it -- a hand, a foot or a person.'),
      ('minor', 'The floor reads as wooden boards.')),
    P(cons('the box'),
      ('core', 'The box moves while it is being pushed and slows to a stop once the push stops.',
       'the box keeps sliding at the same speed long after contact ends, or sets off before '
       'anything touches it'),
      ('core', 'The box stays flat on the floor, in contact with it.',
       'the box slides along above the floor or sinks into it'),
      ('major', 'The box moves in the direction it is pushed.',
       'the box slides off sideways or back toward the pusher'),
      ('major', 'The pusher and the box stay in contact while the box is being driven, and the '
                'pusher does not pass into it.',
       'the hand or foot passes through the box, or keeps shoving with the box no longer moving '
       'with it'),
      ('minor', 'The floorboards stay fixed as the box passes over them.',
       'the floor slides, bends or travels along with the box'),
      marks('the box', 'the labels, tape and printing on the box')),
    note="Their standard's 'slows down quickly' has no visible scale -- how fast a box stops "
         "depends on its weight and the floor, and the rubric policy excludes anything needing "
         "measurement -- so 'quickly' is not used. That the box slows and stops once the push ends "
         "is P2.")

add('low-friction-glide', 46,
    'A puck glides across ice, losing speed only slowly, and eventually stops.',
    S(('core', 'A puck is present.'),
      ('core', 'The puck slides across the surface.'),
      ('core', 'The surface reads as ice.'),
      ('minor', 'The puck lies flat on the ice rather than being carried or rolling on its edge.')),
    P(cons('the puck'),
      ('core', 'The puck loses speed only slowly: over the shot it decelerates far less than '
               'something sliding on a rough floor would.',
       'the puck pulls up short in a stride or two as though sliding on carpet, or speeds up on '
       'its own on level ice'),
      ('core', 'The puck stays flat on the ice surface and does not sink into it.',
       'the puck slides along above the ice or through it'),
      ('major', 'The puck holds one straight line unless something touches it.',
       'the puck curves or reverses on level ice with nothing acting on it'),
      nojump('the puck'),
      ('minor', 'Face markings turn with the puck if it is spinning and stay put if it is not.',
       'the markings rotate while the puck outline plainly does not, or slide across its face'),
      ('minor', 'The puck comes to rest on the ice and stays there.',
       'the puck settles and then drifts off again on its own',
       'the puck stops within the shot')))

add('slide-off-edge-tip-fall', 47,
    'A book slides across a table, tips over the edge and falls to the floor.',
    S(('core', 'A book is present.'),
      ('core', 'The book slides across the table surface.'),
      ('core', 'The book leaves the table edge.'),
      ('minor', 'A table is present as the surface it slides on.')),
    P(cons('the book'),
      ('core', 'Past the edge the book falls, speeding up as it goes down.',
       'the book carries on horizontally beyond the edge, or hangs in the air off the table'),
      ('core', 'While still on the table the book stays in contact with the table top.',
       'the book slides along above the table top'),
      ('major', 'The book tips as it goes over: the unsupported part drops first and it rotates '
                'nose-down.',
       'the book stays perfectly level as it leaves the edge and sinks flat like a lift platform'),
      ('major', 'The book slows while sliding on the level table rather than gaining speed.',
       'the book speeds up on its own while sliding across the level table'),
      ('major', 'The book lands on the floor and stays down.',
       'the book comes to rest in mid-air below the table, or bounces back up onto the table',
       'the floor is in view'),
      ('minor', 'The book flops or its pages splay as it falls and lands.',
       'the book stays perfectly rigid like a solid brick through the fall and the landing'),
      marks('the book', 'the cover art and the title on the book')))

add('sliding-friction-stop', 48,
    'A coin slides along a surface, loses speed steadily and comes to rest.',
    S(('core', 'A coin is present.'),
      ('core', 'The coin slides along a surface.'),
      ('core', 'The coin comes to a stop within the shot.'),
      ('minor', 'The coin is already moving at the start rather than being set down at rest.')),
    P(cons('the coin'),
      ('core', 'The coin loses speed all the way to the stop, and once stopped it stays stopped.',
       'the coin holds one speed and then halts instantly, or sets off again on its own after '
       'coming to rest'),
      ('core', 'The coin stays flat on the surface while sliding and does not sink into it.',
       'the coin slides along above the surface or through it'),
      ('major', 'The coin holds one straight line unless something deflects it.',
       'the coin curves or reverses on a level surface with nothing acting on it'),
      nojump('the coin'),
      ('minor', 'The face design stays part of the coin: if the coin turns, the design comes round '
                'with it.',
       'the design slides across the coin, or stays squarely facing the camera while the coin '
       'plainly turns'),
      ('minor', 'A coin that is spinning as it slides also slows its spin, and settles flat.',
       'the spin continues at full rate after the coin has stopped travelling',
       'the coin is spinning as well as sliding')),
    note="Their first key standard for this scenario is 'the coin slides smoothly at the start', "
         "which names no physical observable -- smoothness is a rendering property, not a "
         "consequence of any law -- so it is not used. Their second standard, the gradual "
         "deceleration, is the whole physical content of the scenario and is item P2 here.")

add('wet-drag-high-friction', 49,
    'A wet cloth is dragged over a counter: it clings and bunches, and leaves the surface wet.',
    S(('core', 'A cloth is present.'),
      ('core', 'The cloth is dragged along a counter surface.'),
      ('core', 'The cloth reads as wet -- darkened, heavy or dripping.'),
      ('minor', 'Something is pulling it -- a hand or a held edge -- rather than it moving alone.')),
    P(soft('the cloth'),
      ('core', 'The cloth resists as it is pulled: it bunches, folds or stretches where the pull is '
               'applied before the rest follows.',
       'the cloth stays a flat stiff rectangle and glides along as if it were a tile'),
      ('core', 'The cloth stays down on the counter as it is dragged.',
       'the cloth floats clear of the counter while being dragged along it'),
      ('major', 'The cloth moves only where and when it is pulled, and it follows the direction of '
                'the pull.',
       'the cloth travels with nothing holding it, or moves against the direction of the pull'),
      ('major', 'The counter is left wet where the cloth has passed -- a film, a streak or a '
                'darkened band.',
       'a plainly soaked cloth leaves the counter completely dry behind it'),
      ('minor', 'The cloth sags under its own weight where nothing supports it.',
       'the cloth sticks out stiffly into the air like a sheet of card'),
      marks('the cloth', 'the pattern and the hem of the cloth'),
      ('minor', 'Water squeezed out of the cloth spreads on the counter and runs downhill.',
       'pooled water climbs away from the cloth or beads uphill',
       'liquid pools on the counter')))

# ---- Gravity and Free Fall (50-56) --------------------------------------
add('exit-into-freefall', 50,
    'A skydiver leaves an aircraft and falls away from it, speeding up downward in a hard airflow.',
    S(('core', 'A skydiver is present.'),
      ('core', 'An airplane is present.'),
      ('core', 'The skydiver leaves the airplane and is in the air.'),
      ('minor', 'The skydiver starts in or on the aircraft rather than already falling in open '
                'sky.')),
    P(('fatal', 'Once clear of the aircraft the skydiver falls away downward.',
       'the skydiver rises away from the plane with nothing lifting them, or hangs level alongside '
       'it in the air'),
      ('core', 'The fall speeds up at first rather than starting at its final rate.',
       'the descent begins at one fixed speed and never changes from the instant they let go'),
      ('core', 'The skydiver drops below and behind the aircraft, which flies on.',
       'the plane hovers beside the falling skydiver, or keeps station with them all the way down'),
      ('major', 'The airflow acts on the skydiver: clothing and straps are pressed back and beat '
                'about hard.',
       'the jumpsuit, straps and hair hang as still as in a calm room during free fall'),
      ('major', 'Anything worn or carried falls with the skydiver and stays with them.',
       'a helmet, goggles or pack drifts upward away from the falling skydiver'),
      ('minor', 'The fall continues to the end of the shot or until a canopy opens.',
       'the skydiver comes to a halt in mid-air with no canopy out'),
      ('minor', 'A deployed canopy fills with air and the fall slows sharply.',
       'the canopy opens and the descent rate is unchanged, or it stays a limp rag while braking '
       'the fall',
       'a parachute opens within the shot')))

add('free-fall-from-rest', 51,
    'An apple leaves the branch and falls straight down under gravity, speeding up as it goes.',
    S(('core', 'An apple is present.'),
      ('core', 'The apple leaves the branch and falls.'),
      ('core', 'A tree branch is present.'),
      ('minor', 'The apple starts attached to or resting on the branch.')),
    P(('fatal', 'The apple falls downward once it leaves the branch.',
       'the apple rises, drifts off sideways, or hangs in the air after detaching'),
      ('core', 'The apple speeds up as it falls: it covers more ground late in the fall than at the '
               'start.',
       'it descends at one steady speed for the whole drop, or slows as it goes down'),
      ('core', 'The fall is essentially straight down, with no sideways swerve that nothing caused.',
       'the apple curves or arcs across the frame in still air'),
      ('major', 'The apple keeps falling until it meets something.',
       'the apple halts in mid-air, or eases to a gentle stop before touching anything'),
      ('major', 'The branch springs back or shakes when the apple weight leaves it.',
       'the branch stays exactly as loaded after the apple has gone',
       'the branch is in view as the apple detaches'),
      ('minor', 'The stalk and any leaf that comes away with the apple stay attached and fall with '
                'it.',
       'a leaf carried off with the apple drifts upward or hangs where the apple was'),
      ('minor', 'On landing the apple bumps, rolls a little and settles on the ground.',
       'the apple sinks into the ground, or stops dead where it lands as though glued',
       'the apple reaches the ground within the shot')))

add('cliff-drop-impact', 52,
    'A rock falls from a cliff, accelerating like a dense body, and strikes the ground below.',
    S(('core', 'A rock is present.'),
      ('core', 'The rock falls from the cliff down through the air.'),
      ('core', 'A cliff or a high drop is present.'),
      ('minor', 'The rock starts at rest at the top rather than being hurled.')),
    P(('fatal', 'The rock falls downward.',
       'the rock rises, hovers, or drifts along instead of falling'),
      ('core', 'The rock speeds up as it descends.',
       'the rock falls at one constant speed all the way down, or slows during the fall'),
      ('core', 'The rock falls like a dense body: it drops fast and holds its attitude rather than '
               'fluttering or drifting the way something light would.',
       'the rock floats down slowly like a feather, or sways from side to side as it falls'),
      ('major', 'Its path stays essentially vertical; any sideways speed it left the edge with '
                'stays as it was.',
       'the rock swerves back and forth, or gains sideways speed in still air'),
      ('major', 'The rock reaches the surface below and the fall ends there.',
       'the rock fades out in mid-air, or stops just short of the ground',
       'the bottom of the drop is in view'),
      ('minor', 'The rock tumbles as one rigid piece: its faces come round with it.',
       'the rock surface markings slide over its faces while it turns'),
      ('minor', 'At impact the rock bounces, breaks or beds in and then stops.',
       'the rock settles onto the ground as gently as if it had been placed there',
       'the impact is in view')))

add('brittle-shatter-on-impact', 53,
    'A glass falls from a table and, on a hard floor, breaks at the moment of impact.',
    S(('core', 'A glass cup is present.'),
      ('core', 'The cup falls from the table.'),
      ('minor', 'A table is present as what it falls from.'),
      ('minor', 'The cup starts standing on the table.')),
    P(('fatal', 'The cup falls downward and reaches the floor.',
       'the cup floats, rises, or stops in mid-air before reaching the floor'),
      ('core', 'The cup speeds up as it falls.',
       'the cup descends at one steady speed for the whole fall'),
      ('core', 'The cup stops at the floor surface rather than continuing into it.',
       'the cup sinks into the floor or passes through it'),
      ('core', 'If the cup breaks, it breaks at the moment of impact and not before.',
       'the cup is already cracking or shedding fragments while still in the air',
       'the cup breaks within the shot'),
      ('major', 'The cup falls as one rigid object while in the air, holding its shape.',
       'the cup deforms, sags or wobbles like rubber during the fall'),
      ('major', 'Fragments fly outward from the point of impact, then fall and settle on the floor.',
       'fragments drift upward and stay up, or hang in the air where they appeared',
       'the cup breaks and the floor around it is in view'),
      ('minor', 'What lands stays landed: the pieces do not reassemble and the cup does not return '
                'to the table.',
       'the broken pieces gather back into a whole cup, or the cup rises back onto the table'),
      ('minor', 'Liquid in the cup spills out and spreads on impact.',
       'the liquid stays in a cup-shaped blob after the cup has broken, or vanishes at impact',
       'the cup has liquid in it')))

add('air-resistance-descent', 54,
    'A feather drifts down slowly, air resistance dominating its weight, and settles on the ground.',
    S(('core', 'A feather is present.'),
      ('core', 'The feather falls through the air.'),
      ('minor', 'The feather starts higher up and ends lower down.'),
      ('minor', 'The ground it descends toward is visible.')),
    P(('fatal', 'The feather descends overall rather than rising away.',
       'the feather climbs steadily out of frame in still air, or hangs motionless in mid-air for '
       'the whole shot'),
      ('core', 'The feather falls slowly -- far slower than a stone would over the same drop, so '
               'the descent is drawn out.',
       'the feather drops fast and straight down like a pebble'),
      ('core', 'Its descent is not a plain vertical line: it rocks, flutters, sideslips or spirals '
               'as the air pushes on its face.',
       'the feather tracks a perfectly straight vertical line with no rocking at all'),
      ('core', 'It does not keep gaining speed: after the first moment its rate of descent stays '
               'about the same rather than building the way a dense body does.',
       'the feather accelerates all the way down so that it is moving fastest just before it lands'),
      ('major', 'The feather turns as it goes, showing edge and face to the air in turn.',
       'the feather holds exactly one orientation the whole way down while plainly drifting'),
      ('major', 'It lands lightly and stays on the ground.',
       'the feather strikes the ground hard and bounces, or drives into it',
       'the feather reaches the ground within the shot'),
      ('minor', 'The barbs flex as air moves past them.',
       'the feather behaves as a perfectly rigid plate throughout'),
      marks('the feather', 'the colour pattern and the markings on the feather')))

add('through-hoop-then-bounce', 55,
    'A ball drops through the hoop, keeps falling, and rebounds off the court below.',
    S(('core', 'A basketball is present.'),
      ('core', 'A hoop is present.'),
      ('core', 'The ball passes downward through the hoop.'),
      ('minor', 'The ball arrives from above the rim rather than being pushed up through it.')),
    P(('fatal', 'The ball passes through the opening of the hoop, not through solid parts of it.',
       'the ball passes through the rim itself or through the backboard'),
      ('core', 'The ball speeds up as it falls.',
       'the ball descends at one steady speed throughout'),
      ('core', 'Below the hoop the ball continues down to the court and rebounds off it.',
       'the ball halts under the hoop, or reaches the floor with no rebound at all'),
      ('major', 'Each rebound is lower than the fall that produced it.',
       'the ball bounces back up higher than the point it fell from'),
      ('major', 'The hoop and backboard stay on their mounting, shaking at most if the ball strikes '
                'the rim.',
       'the hoop travels along with the ball or drifts away from its mounting'),
      ('major', 'The net is pushed out and down as the ball passes and then falls back.',
       'the net hangs undisturbed as the ball passes through it, or the ball passes through the net '
       'mesh sideways',
       'the hoop has a net'),
      marks('the ball', 'the seams and lettering on the ball'),
      ('minor', 'The ball ends up rolling or resting on the court.',
       'the ball is left bouncing to the same height when the shot ends',
       'the ball stays in view after the first bounces')))

add('droplet-detach-and-merge', 56,
    'A drop hangs at a leaf tip, necks off, falls, and merges with the water it lands in.',
    S(('core', 'A water drop is present at a leaf.'),
      ('core', 'The drop leaves the leaf and falls.'),
      ('core', 'A leaf is present.'),
      ('minor', 'The drop starts hanging on the leaf rather than appearing already in mid-air.')),
    P(('fatal', 'The drop falls downward once it detaches.',
       'the drop rises off the leaf or hangs in the air below it'),
      ('core', 'The drop speeds up as it falls.',
       'the drop descends at one fixed speed all the way down'),
      ('core', 'The drop stays a compact rounded blob held together as it falls.',
       'the drop spreads into a sheet, breaks into a spray, or flattens out while falling in still '
       'air'),
      ('major', 'The drop hangs, stretches and necks down at the tip before it separates.',
       'the drop parts from the leaf with no stretching at all, as though cut off'),
      ('major', 'Where it lands the drop joins the water there -- it spreads, is absorbed, or '
                'merges in.',
       'the drop sits on the water as a separate bead, or bounces away off the surface',
       'the drop reaches a wet surface within the shot'),
      ('minor', 'It stays a single drop: no companions appear in mid-air.',
       'extra drops appear out of nothing alongside it as it falls'),
      ('minor', 'The leaf springs up slightly as the weight of the drop leaves it.',
       'the leaf stays bent exactly as loaded after the drop has gone',
       'the leaf tip is in view as the drop leaves'),
      ('minor', 'Ripples spread outward from where the drop lands.',
       'the water it lands in stays glassy and unmarked',
       'the drop lands in standing water in view')))

# ---- Electromagnetic Interactions (57-63) --------------------------------
add('eddy-current-braking', 57,
    'A magnet falls slowly down a copper tube, much slower than free fall, then falls normally out.',
    S(('core', 'A magnet is present.'),
      ('core', 'A copper or metal tube is present.'),
      ('core', 'The magnet is dropped into the tube and travels down through it.'),
      ('minor', 'The magnet is released rather than pushed or driven through.')),
    P(('fatal', 'The magnet takes much longer to pass down the tube than a free fall over the same '
                'height would.',
       'the magnet drops through the tube as fast as it would through open air'),
      ('core', 'Inside the tube it settles to a slow near-steady descent rather than continuing to '
               'gain speed.',
       'the magnet accelerates all the way down inside the tube'),
      ('core', 'The magnet travels downward and comes out of the lower end.',
       'the magnet climbs back up the tube on its own, or stays inside it for good'),
      ('major', 'Outside the tube the magnet falls normally -- fast and accelerating -- before '
                'entering and after leaving.',
       'the magnet drifts down slowly in open air outside the tube as well'),
      ('major', 'The tube is not magnetic: nothing clamps to its wall and the tube is not dragged '
                'along.',
       'the magnet sticks to the copper wall and stops, or the tube is towed along by the magnet'),
      cons('the magnet'),
      ('minor', 'The tube stays a rigid straight tube as the magnet goes down it.',
       'the tube bulges, bends or ripples where the magnet is inside it'),
      ('minor', 'Out of the bottom the magnet falls away and reaches whatever is below.',
       'the magnet leaves the tube and hangs in the air beneath it',
       'the space below the tube is in view')),
    note="Their key standard 2 asks that the magnet 'travels through the copper tube without "
         "visibly contacting the inner walls'. That is not judgeable: a copper tube is opaque, so "
         "nothing inside it is visible at all, and a real magnet dropped down a tube does rattle "
         "against the wall. Their key standard 1 likewise compares the speed inside the tube with "
         "free fall, which can only be read from how long the magnet takes between the two open "
         "ends. This rubric judges the observable version -- the transit time and the normal fall "
         "outside -- and drops the no-contact requirement.")

add('magnetic-attraction-accelerating', 58,
    'A ball is drawn across a table to a magnet, speeding up as the gap closes, and sticks to it.',
    S(('core', 'A magnet is present.'),
      ('core', 'A metal ball is present.'),
      ('core', 'The ball moves across the table toward the magnet.'),
      ('minor', 'A table is present as the surface it moves on.')),
    P(('fatal', 'The ball moves toward the magnet.',
       'the ball is driven away from the magnet, or moves with no relation to where the magnet is'),
      ('core', 'The ball speeds up as the gap closes: slow while far off, fastest just before it '
               'arrives.',
       'the ball travels at one constant speed the whole way, or slows as it nears the magnet'),
      ('core', 'The ball stays on the table surface as it travels.',
       'the ball lifts off the table or sinks into it'),
      ('core', 'The ball ends up touching the magnet and stays held to it.',
       'the ball stops short and rests in open space, or rebounds and settles away as if it were '
       'not attracted at all',
       'the ball reaches the magnet within the shot'),
      ('major', 'The ball travels essentially straight along the line toward the magnet.',
       'the ball wanders in loops, or curves away before coming back'),
      ('major', 'The magnet stays where it is held; if it is loose, ball and magnet close on each '
                'other.',
       'the magnet is dragged backwards away from the ball with nothing pulling it'),
      ('minor', 'The ball starts moving only once the magnet is near, not before.',
       'the ball is already rolling toward the spot before the magnet is anywhere close'),
      ('minor', 'Other loose steel objects nearby are pulled or shift as well.',
       'a loose steel object right beside the magnet is wholly unaffected',
       'other loose steel objects are within reach of the magnet')))

add('electrostatic-repulsion', 59,
    'Two like-charged balloons push apart, hardest when closest and more weakly as the gap grows.',
    S(('core', 'Two balloons are present.'),
      ('core', 'The two balloons are brought close together.'),
      ('minor', 'Each balloon is free to move -- hanging, on a thread, or loosely held.'),
      ('minor', 'They come near enough to almost touch.')),
    P(('fatal', 'The balloons move apart from each other rather than together.',
       'the balloons pull toward each other and touch, or stay pressed together with nothing '
       'holding them'),
      ('core', 'The push is strongest when they are closest: they part briskly at first and the '
               'parting slows as the gap widens.',
       'they drift apart at one steady rate, or gain speed as they get further apart'),
      ('core', 'Both balloons are pushed, each away from the other.',
       'one balloon is driven off while the other stays exactly where it was',
       'both balloons are free to move'),
      ('major', 'They move only once they are brought close, not before.',
       'the balloons start flying apart while they are still well separated'),
      ('major', 'They separate along the line joining them rather than off to the side.',
       'the balloons shoot off at right angles to the line between them'),
      ('minor', 'They stay inflated and taut as they separate.',
       'a balloon shrinks or goes limp as it moves away'),
      ('minor', 'Hair, dust or loose fibres near the balloons are drawn to them or stand up.',
       'loose hair right against a charged balloon lies completely flat',
       'hair or light fibres are close by')))

add('compass-needle-settling', 60,
    'A needle swings on its pivot, its swing dies away, and it settles pointing one fixed way.',
    S(('core', 'A compass needle is present.'),
      ('core', 'The needle turns on its pivot.'),
      ('core', 'The needle comes to rest pointing in one direction.'),
      ('minor', 'The needle sits in a compass body or on a visible pivot.')),
    P(('fatal', 'The needle turns about its pivot and stays on it.',
       'the needle leaves its pivot, floats free, or swings about a point that is not where it is '
       'mounted'),
      ('core', 'The needle ends up steady on one direction rather than turning on and on.',
       'the needle keeps rotating to the end of the shot without ever settling'),
      ('core', 'Its motion dies away: either the swings past the final direction get smaller each '
               'time, or it comes to rest without overshooting.',
       'the needle swings back and forth by the same amount until the shot ends'),
      ('major', 'Once settled it holds its direction in the world and does not wander off to a new '
                'heading on its own.',
       'the resting needle drifts to a different heading with nothing changing around it'),
      ('major', 'Turning the compass body does not carry the needle with it: the needle keeps '
                'pointing the same way while the dial turns underneath.',
       'the needle turns with the body, staying frozen against the dial markings',
       'the compass body is turned or carried while the needle is settled'),
      ('minor', 'The needle stays rigid: its two ends move together as one piece about the centre.',
       'the needle bends, or its ends move independently of each other'),
      ('minor', 'The dial markings stay fixed in the compass body.',
       'the printed dial slides round under the needle on its own')),
    note="Their first key standard is about smoothness and jitter, which is a rendering property "
         "rather than a physical one, so it is not used. The caption for this scenario is only 'A "
         "compass needle is used', but their own basic_standards Event is 'compass needle rotates "
         "and aligns in one direction', so the rotation and the settling are treated as the named "
         "event and sit in SA.")

add('electromagnet-pickup', 61,
    'A coil wired to a battery becomes a magnet and draws nearby paper clips onto it.',
    S(('core', 'A coil of wire is present.'),
      ('core', 'A battery is present and the coil is connected to it.'),
      ('core', 'Paper clips are present near the coil.'),
      ('minor', 'The clips start loose on the surface rather than already attached to the coil.')),
    P(('fatal', 'The clips move toward the coil and come into contact with it.',
       'the clips are pushed away from the coil, or none of them moves at all while the circuit is '
       'plainly made'),
      ('core', 'The clips move only once the circuit is made: nothing happens before the '
               'connection.',
       'the clips leap to the coil before the battery is connected'),
      ('core', 'The clips stay held to the coil for as long as the connection lasts.',
       'the clips drop off while the circuit is still plainly connected'),
      ('major', 'The nearest clips are pulled first and hardest; far-off ones move little or not at '
                'all.',
       'clips right across the table are yanked in as hard as those beside the coil'),
      ('major', 'The wire stays a connected loop from one battery terminal to the other while the '
                'clips are held.',
       'the coil holds the clips with its leads hanging plainly disconnected'),
      ('minor', 'The clips stay separate pieces of wire and keep their shape as they are picked up.',
       'clips merge into a single blob, or change into other objects on the coil'),
      ('minor', 'The clips fall when the connection is broken.',
       'the clips stay stuck to the coil after the battery is plainly disconnected',
       'the circuit is broken within the shot')))

add('motor-rod-rotation', 62,
    'A rod turns steadily on its axis between two magnets, sparking at its sliding contacts.',
    S(('core', 'A metal rod is present.'),
      ('core', 'Two magnets are present with the rod between them.'),
      ('core', 'The rod spins.'),
      ('minor', 'The rod turns in place between the magnets rather than flying off.')),
    P(('fatal', 'The rod turns about a fixed axis and stays between the magnets.',
       'the rod drifts out from between the magnets, or passes through a magnet as it turns'),
      ('core', 'The rod turns one way rather than reversing on its own.',
       'the rotation flips direction with nothing in the setup changing'),
      ('core', 'It keeps turning at a roughly steady rate while the setup is unchanged.',
       'the rod stops and restarts, or its rate lurches about with nothing changing'),
      ('major', 'The rod stays rigid and straight as it spins.',
       'the rod bends, stretches or whips like a rope while turning'),
      ('major', 'The magnets stay put; they do not turn with the rod.',
       'the magnets rotate along with the rod as one assembly'),
      marks('the rod', 'the markings and the machined features on the rod'),
      ('minor', 'Sparks come from the sliding contact points, fly outward and fade.',
       'sparks appear away from any contact, or hang in the air without dying out',
       'sparks appear in the shot')))

add('electrostatic-attraction-pickup', 63,
    'Paper scraps are lifted from a table against gravity and cling to a charged balloon.',
    S(('core', 'A balloon is present.'),
      ('core', 'Small pieces of paper are present on a table.'),
      ('core', 'The balloon is brought near the paper pieces.'),
      ('minor', 'The pieces start lying on the table rather than already on the balloon.')),
    P(('fatal', 'Paper pieces leave the table and travel up to the balloon.',
       'the pieces are blown away from the balloon, or lie flat on the table while it is held right '
       'over them'),
      ('core', 'They respond to nearness: the closer the balloon comes, the more of them lift.',
       'the pieces leap up while the balloon is still far away'),
      ('core', 'Once on the balloon the pieces stay stuck to its surface while it is held near.',
       'the pieces slide straight off the balloon as though nothing held them'),
      ('major', 'Only light things respond: the small scraps lift while heavy objects on the table '
                'stay put.',
       'a cup, a coin or the tablecloth is lifted along with the paper'),
      ('major', 'The pieces travel to the balloon and land on the side facing them.',
       'the pieces fly round to the far side of the balloon, or veer away before returning'),
      ('minor', 'The pieces keep their shapes and their number: none appears from nothing.',
       'extra scraps appear out of nowhere on the balloon'),
      ('minor', 'A piece that comes loose falls back down to the table.',
       'a piece that leaves the balloon floats off upward or hangs in the air',
       'a piece comes off the balloon')))

# ---- Tension and Compression (64-70) ------------------------------------
add('slack-then-taut-tension', 64,
    'A rope hanging slack is drawn straight, and only once it is taut does the box begin to move.',
    S(('core', 'A rope is present, slack at the start.'),
      ('core', 'A box is present, attached to or held by the rope.'),
      ('core', 'The rope is pulled and the box moves.'),
      ('minor', 'The pull comes from a person or a machine at the far end.')),
    P(('fatal', 'The box moves only through the rope: it starts moving when the taut rope pulls it.',
       'the box slides forward while the rope is still hanging slack'),
      ('core', 'The rope goes from sagging to straight before the box moves.',
       'the rope stays slack for the whole shot while the box is dragged along'),
      ('core', 'The box follows the direction the taut rope pulls it.',
       'the box moves sideways or away from the line of the rope'),
      ('major', 'The rope stays fixed where it is attached to the box.',
       'the rope end comes free and still drags the box, or passes through the box body'),
      ('major', 'While the box is being dragged the rope stays essentially straight and under load.',
       'the rope goes slack again while the box is still being pulled along'),
      ('minor', 'The rope keeps about the same length: it does not grow or shrink to suit the gap.',
       'the rope lengthens or shortens on its own between its two ends'),
      ('minor', 'While slack the rope hangs in a curve under its own weight.',
       'the slack rope holds a rigid zig-zag or a shape gravity would not give it')))

add('rope-under-tension', 65,
    'A rope pulled at both ends takes up its slack, straightens, and stretches almost none.',
    S(('core', 'A rope is present.'),
      ('core', 'The rope is pulled at both ends.'),
      ('minor', 'The rope starts with some slack in it.'),
      ('minor', 'Both ends are held -- by hands, by people or by fixings.')),
    P(('fatal', 'The rope stays one continuous piece between the two ends, held at both.',
       'the rope parts in the middle with no break or fraying, or an end is no longer held yet the '
       'rope stays stretched straight'),
      ('core', 'Pulling straightens the rope: the sag goes out of it as the ends draw apart.',
       'the rope keeps a loose sag while its ends are plainly being hauled apart'),
      ('core', 'The rope barely stretches: its length between the grips grows very little, unlike '
               'elastic.',
       'the rope stretches out like a rubber band, growing much longer as it is pulled'),
      ('major', 'The ends draw apart, or the pullers lean back, as the load comes on.',
       'the ends move toward each other while the rope becomes tighter'),
      ('major', 'The taut rope is straight between the grips.',
       'the loaded rope holds an S-curve or a bend with nothing pushing on it'),
      ('minor', 'The rope keeps its thickness along its length.',
       'the rope thins to a thread in the middle as it is pulled'),
      ('minor', 'When the pull is released the rope sags again.',
       'the rope stays rigidly straight in the air after the pull stops',
       'the pull is released within the shot')))

add('spring-compression', 66,
    'Hands press a spring shorter: its coils close up and it pushes back when they ease off.',
    S(('core', 'A spring is present.'),
      ('core', 'Two hands press on its two ends.'),
      ('minor', 'The spring starts at its relaxed length.'),
      ('minor', 'The hands stay on the ends of the spring while pressing.')),
    P(('fatal', 'The spring gets shorter between the hands as they press inward.',
       'the spring gets longer as the hands press toward each other, or the hands pass through its '
       'ends'),
      ('core', 'The gaps between the coils close up as it shortens, and no coil passes through '
               'another.',
       'the spring shrinks as a whole with its coil spacing unchanged, or coils cut through one '
       'another'),
      ('core', 'It shortens only while and where the hands press.',
       'the spring compresses before the hands reach it, or keeps shortening after they stop moving'),
      ('major', 'It stops shortening once the coils have closed on each other.',
       'the spring keeps shrinking away to nothing after its coils have already met'),
      ('major', 'It springs back toward its original length when the hands ease off.',
       'the spring stays fully compressed after the hands are taken away',
       'the hands ease off or release within the shot'),
      ('minor', 'The coil diameter stays about the same as the spring shortens.',
       'the spring grows fatter or thinner in proportion as it is compressed'),
      ('minor', 'The fingers press against the ends and stay in contact with them.',
       'the hands stay clear of the spring while it compresses')))

add('beam-bending-under-load', 67,
    'A loaded plank bows downward, most under the load, and holds the bend while the weight sits.',
    S(('core', 'A wooden plank is present.'),
      ('core', 'A weight rests on top of the plank.'),
      ('core', 'The plank is supported so that it can bend -- across supports or over a gap.'),
      ('minor', 'The weight is plainly resting on the plank rather than hovering over it.')),
    P(('fatal', 'The plank bends downward under the weight.',
       'the plank bows upward against the load, or the weight sinks through the plank'),
      ('core', 'The bend is greatest where the load sits, and the plank stays continuous through '
               'the bend unless it actually breaks.',
       'the plank sags most at a place far from the weight, or kinks at a sharp hinge while still '
       'in one piece'),
      ('core', 'It bends once the weight is on it and stays bent while the weight remains.',
       'the plank is already bowed before the weight arrives, or springs straight again while the '
       'weight still sits on it'),
      ('major', 'The ends stay on their supports as the plank bends.',
       'an end lifts off or slides off its support while the plank stays bent'),
      ('major', 'The weight stays on the plank and goes down with it as it deflects.',
       'the weight hangs at its original height while the plank sags away beneath it'),
      ('minor', 'The plank keeps its length as it bends: it does not stretch like rubber.',
       'the plank grows noticeably longer as it bows'),
      ('minor', 'A heavier or larger load gives a deeper sag.',
       'adding more load leaves the sag exactly as it was',
       'the load changes during the shot')))

add('elastic-stretch', 68,
    'A rubber band lengthens and thins as it is pulled, and shortens back when released.',
    S(('core', 'A rubber band is present.'),
      ('core', 'It is pulled at two points.'),
      ('minor', 'The band starts relaxed.'),
      ('minor', 'Both pulling points are visible -- fingers, hooks or hands.')),
    P(('fatal', 'The band lengthens along the direction it is pulled.',
       'the band gets shorter as the pulling points move apart, or the fingers pass through it'),
      ('core', 'It thins as it lengthens: the rubber narrows while it is stretched.',
       'the band holds exactly its original thickness while stretching to several times its length'),
      ('core', 'It stays one closed loop attached to both pulling points.',
       'the band comes off a finger yet stays stretched, or turns into a strip with loose ends'),
      ('core', 'It shortens back toward its original size when the pull eases.',
       'the band stays fully stretched after the pull is taken off',
       'the pull is eased or released within the shot'),
      ('major', 'It stretches only while and as far as the pulling points move.',
       'the band goes on lengthening after the hands have stopped moving apart'),
      ('major', 'Under tension the band is straight between the two pulling points.',
       'the stretched band hangs in a slack curve between the fingers'),
      ('minor', 'A printed mark on the band spreads with the rubber rather than keeping its size.',
       'a printed mark keeps exactly its original size while the rubber around it doubles in length'),
      ('minor', 'If it snaps, the pieces fly apart and whip back.',
       'a broken band hangs where it parted with no recoil at all',
       'the band breaks within the shot')))

add('stiff-rod-compression', 69,
    'A steel rod pressed end to end does not visibly shorten; a slender one bows sideways instead.',
    S(('core', 'A steel or metal rod is present.'),
      ('core', 'Something presses on both ends of the rod -- hands, a vice or a press.'),
      ('minor', 'The rod is held between the two pressing points rather than lying free.'),
      ('minor', 'The pressing is sustained rather than a single tap.')),
    P(('fatal', 'The rod does not visibly shorten: steel squeezed like this changes length by far '
                'too little to see.',
       'the rod visibly squashes shorter, concertinas, or compresses like a soft bar'),
      ('core', 'The rod stays a rigid straight bar, unless the push is hard enough to buckle it, in '
               'which case it bows sideways in a smooth curve.',
       'the rod folds, kinks or crumples like a drinking straw under a hand press'),
      ('core', 'The pressing faces stay against the ends of the rod and do not sink into it.',
       'a hand or a press face sinks into the end of the rod'),
      ('major', 'The rod keeps its diameter: it does not fatten where it is squeezed.',
       'the rod bulges fatter in the middle while being pressed'),
      ('major', 'A rod that bows under load springs back straight when the push is taken off.',
       'the rod stays bent after the press is released, with no sign of it having yielded',
       'the push is released within the shot'),
      marks('the rod', 'the surface markings and the machined ends of the rod'),
      ('minor', 'The rod is the same length after the push as before it.',
       'the rod ends up shorter than it started')),
    note="Their only key standard for this scenario is that 'the steel rod visibly shortens in "
         "length as it is pushed from both ends, showing compression'. That rewards a physics "
         "violation: steel is stiff enough that any force a hand or a bench press applies changes "
         "its length by an amount thousands of times too small to see, so a clip in which the rod "
         "visibly squashes is exactly the hallucination that should be penalised. The real "
         "observables are that the rod does not change length and that a slender rod buckles "
         "sideways rather than shortening, and that is what this rubric asks for.")

add('porous-compression', 70,
    'A hand squeezes a sponge; it compresses and bunches where gripped and springs back on release.',
    S(('core', 'A sponge is present.'),
      ('core', 'The sponge is squeezed by a hand or hands.'),
      ('minor', 'The sponge starts at its full uncompressed shape.'),
      ('minor', 'The gripping hand is visible on the sponge.')),
    P(('fatal', 'The sponge gets smaller where it is gripped rather than swelling there.',
       'the sponge bulges out under the fingers, or grows larger overall as it is squeezed'),
      ('core', 'It compresses where the fingers press and the material bunches and wrinkles there, '
               'while parts away from the grip keep more of their shape.',
       'the sponge shrinks evenly like a scaled-down copy of itself'),
      ('core', 'It deforms only while and where it is squeezed.',
       'the sponge goes on deforming after the hand has stopped moving, or changes shape before the '
       'hand reaches it'),
      ('major', 'The fingers stay on the outside of the sponge.',
       'fingers sink through the sponge and out the other side'),
      ('major', 'It springs back toward its original shape when the grip opens.',
       'the sponge stays crushed after the hand has let go',
       'the grip is opened within the shot'),
      marks('the sponge', 'the pores and surface texture of the sponge'),
      ('minor', 'Water is forced out of a wet sponge and runs downward.',
       'a plainly soaked sponge gives up no water at all under a hard squeeze',
       'the sponge is wet')))
