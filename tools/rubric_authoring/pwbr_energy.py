# phyworldbench 71-105: Energy Conservation.
# Same authoring flow as the earlier blocks: items come from the caption plus first-principles
# physics, then physics_prompt and key_standards are diffed for coverage; conflicts are followed
# on the side of physics and recorded in `note`. Mechanism names are reused across category
# boundaries wherever the scenario is physically the same as an earlier one, so that duplicates
# between their categories are visible in the rubric set.

def cons(o):
    return ('fatal',
            f'{o[0].upper()}{o[1:]} keeps its own shape and identity for the whole shot, and it '
            f'does not pass through any solid surface.',
            f'{o} turns into a different object, passes through something solid, or disappears '
            f'and re-appears')


def marks(o, mk):
    return ('minor',
            f'{mk[0].upper()}{mk[1:]} stay attached to {o} and move with it.',
            f'{mk} slide across the surface, detach, or change from one moment to the next')


def faster_down(o, place='as it descends'):
    return ('core', f'{o[0].upper()}{o[1:]} gains speed {place}.',
            f'{o} descends at one fixed speed throughout, or slows steadily on the way down with '
            f'nothing in the way')


# ---- Potential to Kinetic Energy (71-77) ---------------------------------
add('impoundment-release', 71,
    'Still water held behind a dam is released and rushes out downhill, gaining speed as it drops.',
    S(('core', 'A dam is present.'),
      ('core', 'Water is held behind it.'),
      ('core', 'The dam is opened -- a gate lifts, a channel opens, or a way through appears.'),
      ('minor', 'The water behind the dam is calm or still before it is opened.')),
    P(('fatal', 'Water flows out through the opening and downhill, away from the reservoir.',
       'water flows uphill out of the opening, or a torrent appears downstream while the dam is '
       'still plainly shut'),
      ('core', 'The water only starts moving fast once the dam is opened.',
       'the reservoir is already surging through a closed dam'),
      ('core', 'The released water speeds up as it drops through and past the opening.',
       'the outflow leaves at one slow rate and never gains any speed, or slows as it falls'),
      ('major', 'The jet breaks up into white water and spray where it lands.',
       'the outflow stays a smooth glassy sheet with no turbulence at all where it plunges'),
      ('major', 'The reservoir surface stays level and settles downward as water leaves.',
       'the stored water stands up in a heap or a hole that gravity would flatten'),
      ('major', 'The dam stays put and water passes only through the opening.',
       'water passes through the solid wall of the dam, or the dam drifts off with the flow'),
      ('minor', 'The water stays one connected body.',
       'lumps of water hang unattached in the air above the flow'),
      ('minor', 'Foam and floating debris are carried along with the flow.',
       'floating debris stays fixed in place while the water races past it',
       'there is foam or floating debris on the water')))

add('slope-acceleration', 72,
    'A rock starts from rest at the top of a hill and accelerates down the slope.',
    S(('core', 'A rock is present.'),
      ('core', 'A hill or slope is present.'),
      ('core', 'The rock starts at rest and then begins to move.'),
      ('minor', 'It starts at or near the top edge of the slope.')),
    P(('fatal', 'The rock moves downhill once it starts.',
       'the rock climbs the hill on its own, or sets off along the level with nothing pushing it'),
      faster_down('the rock'),
      ('core', 'Apart from bounces, the rock stays on the hillside and follows its slope.',
       'the rock passes into the hillside, or drifts away from the surface and travels through open '
       'air'),
      ('major', 'It is at rest until something sets it off.',
       'the rock is already creeping along before anything disturbs it'),
      ('major', 'Its rolling or tumbling agrees with the way it is travelling.',
       'the rock rotates backwards relative to its direction of travel while touching the ground'),
      cons('the rock'),
      ('minor', 'Dust, grass or loose stones are disturbed along its path.',
       'the rock crosses loose ground leaving it perfectly undisturbed'),
      ('minor', 'Stones it knocks loose also travel downhill.',
       'dislodged stones move uphill or hang where they were struck',
       'the rock dislodges other stones')))

add('slope-acceleration', 73,
    'A skier sets off from the top and accelerates down the slope on their skis.',
    S(('core', 'A skier is present.'),
      ('core', 'A slope is present.'),
      ('core', 'The skier starts at the top and skis down it.'),
      ('minor', 'The skier starts stationary or nearly so.')),
    P(('fatal', 'The skier travels downhill.',
       'the skier glides uphill with nothing driving them, or stays put on a steep pitch with '
       'nothing holding them'),
      faster_down('the skier', 'while descending'),
      ('core', 'The skis stay on the snow under the skier.',
       'the skis float clear of the snow or sink through it'),
      ('major', "The skier's path follows the surface of the slope.",
       'the path cuts through the snow surface, or leaves the slope and carries on through open air'),
      ('major', 'Speed is lost only where the skier turns, brakes, or reaches flatter ground.',
       'the skier slows sharply on a steep straight pitch with no turn, no braking and nothing in '
       'the way'),
      ('minor', 'Loose clothing and hair are pushed back as speed builds.',
       'clothing and hair hang dead still at the fastest part of the run'),
      ('minor', 'The skis leave tracks in the snow behind them.',
       'the snow behind the skier stays smooth as though nothing had passed'),
      ('minor', 'Snow is thrown from the skis where they are turned or edged.',
       'a hard turn on loose snow throws up none at all',
       'the skier turns or brakes')))

add('pendulum-swing', 74,
    'A pendulum released from a height is fastest at the bottom and rises to nearly that height '
    'on the far side.',
    S(('core', 'A pendulum is present -- a weight on a cord or a rod.'),
      ('core', 'It starts held up to one side.'),
      ('core', 'It is released and swings.'),
      ('minor', 'A fixed pivot or support is visible.')),
    P(('fatal', 'The weight swings downward when released.',
       'the weight rises on release, hangs where it was let go, or drifts away from the pivot'),
      ('core', 'It gains speed on the way down and is fastest at the lowest point of the swing.',
       'it moves at one speed throughout, or is at its fastest at the top of the swing'),
      ('core', 'It slows as it rises and comes momentarily to rest at the top of the far swing.',
       'it keeps its speed all the way up, or speeds up as it climbs'),
      ('core', 'It rises on the far side to about the height it was released from, and never higher.',
       'it climbs higher than the height it was released from, or reaches only a small fraction of '
       'it as though the cord had gone slack'),
      ('major', 'The cord stays taut and keeps its length; the weight travels on an arc about the '
                'pivot.',
       'the cord stretches, goes slack while the weight is out to the side, or the weight leaves '
       'the arc'),
      ('major', 'The pivot stays fixed.',
       'the support point travels along with the weight'),
      ('minor', 'Successive swings are about equal or a little smaller, and each takes about the '
                'same time.',
       'the swings grow bigger on their own'),
      ('minor', 'The cord runs straight from the pivot to the weight throughout.',
       'the cord bows into a curve, or points somewhere other than at the weight')))

add('dive-entry-splash', 75,
    'A diver drops from a platform, accelerating, and enters the water with a splash to match.',
    S(('core', 'A diver is present.'),
      ('core', 'The diver leaves the platform and goes into the pool.'),
      ('minor', 'A raised platform is visible.'),
      ('minor', 'The diver starts standing on the platform.')),
    P(('fatal', 'The diver falls downward from the platform into the water.',
       'the diver rises away from the platform with nothing lifting them, or hangs in the air above '
       'the pool'),
      ('core', 'The fall speeds up, so the diver is moving fastest just before entry.',
       'the descent is at one constant speed, or the diver slows on the way down'),
      ('core', 'The entry throws water up and outward, by an amount that goes with how fast the '
               'diver was travelling.',
       'a fast entry leaves the surface glassy, or a huge eruption of water comes from a slow gentle '
       'entry'),
      ('major', 'The diver carries on into the water and goes under.',
       'the diver lands on top of the water and stays on the surface as though it were solid'),
      ('major', 'Water thrown up falls back into the pool.',
       'thrown-up water hangs in the air or drifts away upward'),
      ('major', 'The flight is a single arc: the diver does not change direction in mid-air.',
       'the diver turns a corner in mid-air, or gains speed sideways with nothing to push against'),
      ('minor', 'Ripples and waves spread outward from the entry point.',
       'the water stays flat around the entry once the diver is under'),
      ('minor', 'The platform or board recoils as the diver pushes off it.',
       'a springboard stays perfectly rigid as the diver drives off it',
       'the take-off is in view')))

add('slope-acceleration', 76,
    'A child slides down a slide, gaining speed on the steep part and slowing at the bottom.',
    S(('core', 'A child is present.'),
      ('core', 'A slide is present.'),
      ('core', 'The child slides down it from the top.'),
      ('minor', 'The child starts at the top, at rest or nearly so.')),
    P(('fatal', 'The child slides downward along the slide.',
       'the child slides up the slide unaided, or hangs still on a steep part with nothing holding '
       'them'),
      faster_down('the child', 'down the steep part'),
      ('core', 'The child stays on the surface of the slide and follows its shape, including any '
               'curve or flattening at the bottom.',
       'the child passes through the slide surface, or travels along above it'),
      ('major', 'The slide itself stays fixed while the child goes down it.',
       'the slide bends, travels along, or reshapes itself as the child descends'),
      ('major', 'The child slows on the flat run-out at the bottom, or leaves the slide there.',
       'the child is still gaining speed on the level end of the slide',
       'the bottom of the slide is in view'),
      ('minor', 'Clothing and hair are pushed back as speed builds.',
       'hair and loose clothes hang perfectly still at the fastest part of the descent'),
      ('minor', 'Anything loose the child is carrying either stays with them or is left behind on '
                'the slide.',
       'a loose item follows the child down through the air without touching anything',
       'the child carries or wears something loose')))

add('coaster-descent', 77,
    'A coaster train crests the hill slowly and accelerates down the drop.',
    S(('core', 'A rollercoaster train is present.'),
      ('core', 'A track is present and the train runs along it.'),
      ('core', 'The train reaches the peak and starts down from it.'),
      ('minor', 'The train is moving slowly at the crest.')),
    P(('fatal', 'The train stays on the track, its wheels on the rails, throughout.',
       'the train leaves the rails, floats above them, or passes through the structure'),
      faster_down('the train', 'as it comes down from the peak'),
      ('core', 'It is at its slowest at the crest and fastest at the bottom of the drop.',
       'the train is at its fastest at the top of the hill'),
      ('major', 'The whole train moves as one: the cars keep their order and spacing and take the '
                'same path.',
       'cars stretch apart, bunch up, or leave the track independently of one another'),
      ('major', 'The train follows the shape of the track, turning where the rails turn.',
       'the train cuts straight across a curve, or takes a line the rails do not follow'),
      ('minor', 'The track and its supports stay fixed as the train passes.',
       'the rails or the supports travel along with the train'),
      ('minor', 'Riders are pressed into their seats and their hair and arms are pushed by the air '
                'at speed.',
       'riders and their hair stay perfectly still through the drop',
       'riders are visible')))

# ---- Elastic Energy (78-84) ---------------------------------------------
add('wind-load-elastic-recovery', 78,
    'Wind bends a palm downwind; trunk and fronds flex and spring back as the wind eases.',
    S(('core', 'A palm tree is present.'),
      ('core', 'Strong wind is plainly acting on it: the tree or its fronds are moved by air.'),
      ('minor', 'The wind keeps up through the shot rather than a single flick.'),
      ('minor', 'The surroundings show the same wind -- other plants, dust or spray.')),
    P(('fatal', 'The tree bends away from the wind, in the direction the air is moving.',
       'the tree leans into the wind, or its fronds stream back toward where the wind is coming '
       'from'),
      ('core', 'The trunk bends in a smooth curve and stays whole and rooted.',
       'the trunk kinks at a sharp hinge, parts without any break appearing, or lifts out of the '
       'ground'),
      ('core', 'The thin fronds bend far more than the thick trunk.',
       'the trunk whips about while the fronds stay stiff and unmoved'),
      ('major', 'All the fronds stream the same way as the wind at any one moment.',
       'neighbouring fronds blow in opposite directions at the same instant'),
      ('major', 'The tree straightens back toward upright as the wind eases.',
       'the tree stays bent over after the wind has plainly dropped',
       'the wind eases within the shot'),
      ('minor', 'The fronds beat and flutter rather than holding a fixed shape.',
       'the bent fronds hold one frozen shape while the wind plainly keeps blowing'),
      ('minor', 'Loose material in the air -- dust, spray, leaves -- moves the same way as the wind.',
       'airborne material drifts against the direction the tree is bent',
       'loose material is carried in the air')))

add('elastic-stretch', 79,
    'A band is pulled longer, then released and snaps back fast to its original length.',
    S(('core', 'A rubber band is present.'),
      ('core', 'It is stretched longer.'),
      ('core', 'It is released.'),
      ('minor', 'It starts relaxed.')),
    P(('fatal', 'The band lengthens as it is pulled and shortens again when released.',
       'the band gets shorter as it is pulled, or stays stretched after release with nothing '
       'holding it'),
      ('core', 'The snap back is far quicker than the pull, taking a fraction of the time.',
       'the band creeps back to its original length as slowly as it was drawn out'),
      ('core', 'It comes back to about its original length.',
       'the released band settles plainly longer or shorter than it started'),
      ('major', 'It thins while stretched and thickens again on release.',
       'the band holds exactly the same thickness at every length'),
      ('major', 'It stretches only while and as far as it is pulled.',
       'the band goes on lengthening after the pull has stopped'),
      ('minor', 'Unless it is pulled to breaking, it stays one loop throughout.',
       'the band parts into a strip, or loses a piece, with no break appearing'),
      ('minor', 'On snapping back it flies, whips or flutters rather than arriving perfectly still.',
       'the band reaches its relaxed shape and is instantly motionless, with no overshoot at all')),
    note="Both of their key standards for this scenario are about rendering rather than physics: "
         "one asks that the elongation be 'smooth and continuous', the other that the release be "
         "'displayed in real-time ... without any visible lag or unnatural motion'. Neither names "
         "a physical observable, so neither is used. The physics that is actually testable here is "
         "the asymmetry between the slow pull and the fast recoil, the thinning under load, and the "
         "return to the original length. Scenario 68 is the same object under tension without the "
         "release, and shares this mechanism.")

add('trampoline-rebound', 80,
    'A child lands on a trampoline; the bed stretches down under them and throws them back up.',
    S(('core', 'A child is present.'),
      ('core', 'A trampoline is present.'),
      ('core', 'The child lands on the trampoline bed.'),
      ('minor', 'The child comes down onto it from above.')),
    P(('fatal', 'The bed drives the child back upward after stretching down under them.',
       'the child lands and stays down with the bed still deeply stretched, or passes through the '
       'bed'),
      ('core', 'The bed dips downward where the child lands, deepest under them, and returns to '
               'flat afterwards.',
       'the bed stays flat and rigid under the landing, or the dip appears where the child is not'),
      ('core', 'The bed brings the child to a stop over the depth of the dip rather than at the '
               'surface.',
       'the child stops dead on touching the bed and is then flicked up with no dip at all'),
      ('major', 'The rebound does not carry the child higher than the fall they arrived with, '
                'unless they plainly push and pump.',
       'the child bounces higher and higher with no effort of their own'),
      ('major', 'The frame and legs stay in place and the bed stays attached at its edges.',
       'the frame travels along with the bed, or the bed comes away from its edges while stretched'),
      ('minor', 'The bed is deepest at the moment the child is slowest, at the bottom of the bounce.',
       'the bed is at its deepest while the child is already back near the top'),
      ('minor', 'The springs stretch and the bed surface tightens as the load comes on.',
       'the springs and the bed edge stay exactly as they were under a heavy landing',
       'the springs or the bed edge are in view')))

add('bow-launch', 81,
    'A drawn bow flexes; on release the string drives the arrow forward and the bow returns to shape.',
    S(('core', 'A bow with a string is present.'),
      ('core', 'The string is drawn back.'),
      ('core', 'An arrow is released and flies forward.'),
      ('minor', 'The arrow is on the string before the release.')),
    P(('fatal', 'The arrow flies forward, away from the bow, when the string is released.',
       'the arrow flies back toward the archer, or leaves the bow before the string is let go'),
      ('core', 'The limbs of the bow bend as the string is drawn and straighten as it is released.',
       'the limbs stay perfectly rigid through the draw, or bend the wrong way as the string comes '
       'back'),
      ('core', 'The arrow gains speed only while the string is still driving it, and then flies on.',
       'the arrow keeps gaining speed long after it has left the string'),
      ('major', 'The string stays attached to both limb tips and drives forward past its rest '
                'position.',
       'the string comes off a tip yet still launches the arrow'),
      ('major', 'The arrow flies point first, along the line the bow was aimed.',
       'the arrow travels sideways or tail first while holding a straight course'),
      ('major', 'Over distance the arrow falls below the line it was launched along.',
       'the arrow holds a dead level path to the end of a long flight',
       'the arrow is followed a long way'),
      ('minor', 'The bow and the arms holding it are jolted and settle after the shot.',
       'the bow is perfectly still at the instant the arrow leaves'),
      ('minor', 'The arrow stays straight and rigid, with its fletching on the tail.',
       'the arrow bends like rubber in flight, or its fletching slides along the shaft')))

add('spring-launch', 82,
    'A toy is pressed down to load its spring, springs up when released, and falls back.',
    S(('core', 'A spring-loaded toy is present.'),
      ('core', 'It is pressed down.'),
      ('core', 'It is released and jumps up.'),
      ('minor', 'A spring or a springy mechanism is visible on it.')),
    P(('fatal', 'The toy launches upward, and only after it has been pressed down and released.',
       'the toy launches while it is still being pressed down, or is driven further down when let go'),
      ('core', 'The spring shortens while it is pressed and lengthens as the toy launches.',
       'the spring holds the same length through both the press and the launch'),
      ('core', 'Once airborne the toy slows as it rises, stops climbing, and falls back.',
       'the toy climbs at a steady rate as though driven, or hangs at the top of its climb'),
      ('major', 'The launch happens at the moment of release.',
       'the toy sits still for a while after release and then jumps on its own'),
      ('major', 'It goes up roughly along the direction it was pressed.',
       'the toy shoots off at right angles to the way it was compressed'),
      ('major', 'How high it goes follows how far the spring was pressed.',
       'a barely pressed spring throws it just as high as a fully compressed one',
       'it is launched more than once from different amounts of compression'),
      ('minor', 'The surface it is pressed against stays put.',
       'the table or floor goes down with the toy as it is pressed'),
      marks('the toy', 'the printing and the colours on the toy')))

add('bungee-oscillation', 83,
    'A jumper falls free while the cord is slack, then the stretching cord halts and reverses '
    'the fall.',
    S(('core', 'A jumper is present.'),
      ('core', 'A bridge or other high structure is present.'),
      ('core', 'The jumper leaps off and falls.'),
      ('minor', 'A bungee cord is attached to the jumper.')),
    P(('fatal', 'The jumper falls, and the cord is what stops the fall.',
       'the jumper floats or rises after leaping, or falls all the way to the ground with the cord '
       'plainly attached'),
      ('core', 'While the cord is still slack the jumper falls freely, gaining speed.',
       'the fall is braked from the first instant, with the cord hanging loose'),
      ('core', 'The cord stretches well beyond its length once taut, and the fall turns round at '
               'the point of greatest stretch.',
       'the cord keeps its slack length and jerks the jumper to a halt like a chain, or the reversal '
       'comes while the cord is still loose'),
      ('major', 'The cord stays attached at both ends -- to the structure and to the jumper.',
       'the cord comes free at one end and still holds the jumper'),
      ('major', 'The cord is straight and taut while it is pulling, and loose when it is not.',
       'the cord hangs in a slack curve while plainly hauling the jumper upward'),
      ('major', 'After the first rebound each rise is lower than the one before.',
       'the bounces hold the same height, or grow, until the shot ends',
       'more than one bounce is shown'),
      ('minor', "The jumper's limbs and clothing are pulled about by the airflow and by the jerk.",
       'the jumper holds a rigid pose with clothing perfectly still throughout the fall'),
      ('minor', 'Once the bouncing dies away the jumper hangs from the cord.',
       'the jumper ends up standing in the air, or drifts off sideways at rest',
       'the shot lasts until the bouncing dies down')))

add('driven-dribble', 84,
    'A hand drives a ball down; it deforms at the floor, rebounds to the hand, and is driven again.',
    S(('core', 'A basketball is present.'),
      ('core', 'The ball is driven down onto the floor and comes back up, more than once.'),
      ('minor', 'A hand is doing the driving.'),
      ('minor', 'The floor it bounces off is visible.')),
    P(('fatal', 'The ball rebounds upward off the floor each time it strikes.',
       'the ball passes into the floor, or lands and stays down while the dribbling goes on'),
      ('core', 'The hand pushes the ball down, so the ball starts down when the hand does and not '
               'before.',
       'the ball sets off downward before the hand touches it, or is driven down while the hand is '
       'moving up'),
      ('core', 'The ball gains speed on the way down and loses it on the way up.',
       'the ball travels up and down at one unchanging speed'),
      ('major', 'The bounce height is kept up by the hand: with no push the next bounce is lower.',
       'the ball keeps returning to the same height with the hand never touching it'),
      ('major', 'The ball stays under the hand rather than wandering off on its own.',
       'the ball bounces away sideways and returns to the hand with nothing redirecting it'),
      marks('the ball', 'the seams and the lettering on the ball'),
      ('minor', 'The ball flattens where it presses on the floor and springs back out.',
       'the ball stays a perfect rigid sphere at the moment it is pressed against the floor',
       'the contact is close enough to see the ball outline clearly')))

# ---- Energy Loss / Damping (85-91) --------------------------------------
add('free-spin-decay', 85,
    'A fan keeps turning after the power is cut, slows steadily, and stops.',
    S(('core', 'A ceiling fan is present.'),
      ('core', 'The fan is turning at the start.'),
      ('core', 'The fan stops turning, or is plainly slowing, by the end.'),
      ('minor', 'The fan is mounted overhead rather than free-floating.')),
    P(('fatal', 'The fan keeps turning after the power is cut and slows to a stop.',
       'the blades stop dead in the same moment the fan is switched off'),
      ('core', 'The rate of turn falls off steadily until it stops.',
       'the fan runs at full rate and then halts abruptly, or slows and then speeds up again on '
       'its own'),
      ('core', 'The blades keep turning the same way round as they slow.',
       'the rotation reverses direction as it dies away'),
      ('major', 'The blades stay attached to the hub and keep their spacing.',
       'a blade detaches, or the blades change their spacing as the fan slows'),
      ('major', 'The fan turns as one about its own axis, and that axis stays fixed.',
       'the fan drifts across the ceiling, or its axis wanders about'),
      marks('the fan', 'the blade faces and any markings on them'),
      ('minor', 'Things being blown about by the fan settle as the airflow dies.',
       'papers or hanging cords go on being blown just as hard after the blades have stopped',
       'something light is in the airflow')))

add('damped-oscillation', 86,
    'A pendulum swings with shrinking swings at an unchanging tempo, and finally hangs still.',
    S(('core', 'A pendulum is present.'),
      ('core', 'It swings back and forth more than once.'),
      ('minor', 'A fixed pivot or support is visible.'),
      ('minor', 'It is left to swing on its own rather than being pushed each pass.')),
    P(('fatal', 'The swings get smaller as time goes on.',
       'the swings hold exactly the same size for the whole shot, or grow bigger with nothing '
       'pushing the pendulum'),
      ('core', 'Each swing takes about the same time as the swings shrink: the tempo does not slow '
               'with the amplitude.',
       'each pass takes plainly longer than the last as the pendulum dies down'),
      ('core', 'It is fastest at the bottom of each pass and momentarily still at each end.',
       'the weight moves at one speed all the way through a pass'),
      ('core', 'It ends up hanging still at the lowest point.',
       'the pendulum comes to rest out to one side of the pivot',
       'the swinging dies out within the shot'),
      ('major', 'The cord stays taut and keeps its length, with the pivot fixed.',
       'the cord stretches or goes slack, or the support point travels about'),
      ('major', 'Each pass peaks a little lower than the last rather than collapsing all at once.',
       'the swing goes from full size to nothing between one pass and the next'),
      ('minor', 'The lowest point of the path is the same on every pass.',
       'the bottom of the swing wanders from pass to pass'),
      ('minor', 'The cord runs straight from the pivot to the weight.',
       'the cord bows into a curve, or points somewhere other than at the weight')))

add('spinning-top', 87,
    'A top spins, slows, wobbles more widely as it slows, and topples at the end.',
    S(('core', 'A spinning top is present.'),
      ('core', 'It is spinning.'),
      ('core', 'Its spin slows, or it topples, within the shot.'),
      ('minor', 'It spins on a surface rather than in mid-air.')),
    P(('fatal', 'The top spins about its own axis while standing on its tip on the surface.',
       'the top spins while floating clear of the surface, or its axis passes down through the '
       'ground'),
      ('core', 'Its rate of spin falls off as it goes.',
       'the top spins at exactly the same rate until it suddenly falls over, or speeds up on its own'),
      ('core', 'It topples only after it has slowed, not while spinning fast.',
       'the top falls over while still spinning at full rate'),
      ('major', 'The wobble of its axis grows as it slows.',
       'the axis stays perfectly upright right up to the instant it falls'),
      ('major', 'It keeps turning the same way round throughout.',
       'the direction of spin reverses on its own'),
      marks('the top', 'the painted rings and markings on the top'),
      ('minor', 'Once it has toppled it lies on the surface and stops.',
       'the fallen top goes on spinning flat on the floor at its old rate',
       'the top topples within the shot')),
    note="Scenario 26, 'A child uses a top on the floor', is the same physical situation in the "
         "Rotational Motion subcategory of category 1 and carries the same mechanism here.")

add('rolling-friction-decay', 88,
    'A board rolls on level ground; its speed and its wheel rotation die away together until it '
    'stops.',
    S(('core', 'A skateboard is present.'),
      ('core', 'It rolls along the ground.'),
      ('core', 'It slows down or stops within the shot.'),
      ('minor', 'It is rolling on its own rather than being pushed along.')),
    P(cons('the board'),
      ('core', 'The board loses speed as it rolls, with nothing driving it.',
       'the board holds exactly one speed for the whole shot, or speeds up on its own on level '
       'ground'),
      ('core', 'The wheels slow in step with the board: their rate of turn falls as its speed '
               'falls, and they are still when it is still.',
       'the wheels go on spinning at full rate after the board has stopped, or stay still while it '
       'rolls'),
      ('major', 'The wheels turn the way the board is travelling.',
       'the wheels turn against the direction of travel'),
      ('major', 'The board holds one straight heading, with nothing acting on it.',
       'it swerves or reverses on its own on level ground'),
      marks('the board', 'the deck graphics and the wheels'),
      ('minor', 'Once stopped it stays stopped.',
       'the board sets off again on its own after coming to rest',
       'the board stops within the shot')),
    note="Their third key standard, that the board 'comes to a complete stop after a realistic "
         "period of time', cannot be judged: nothing in the clip fixes what period is realistic, "
         "since it depends on the unknown starting speed and surface. It is not used. Scenario 2, "
         "'A skateboard rolls down a flat sidewalk', is the same physical situation in category 1 "
         "and carries the same mechanism.")

add('bounce-decay', 89,
    'A ball bounces on its own, each bounce lower and quicker than the last, until it stops.',
    S(('core', 'A bouncy ball is present.'),
      ('core', 'It bounces off a surface more than once.'),
      ('minor', 'It bounces on its own, with nothing striking it after the first release.'),
      ('minor', 'The surface it bounces on is visible.')),
    P(cons('the ball'),
      ('core', 'Each bounce reaches a lower peak than the one before.',
       'the bounces all reach the same height, or each one goes higher than the last with nothing '
       'driving the ball'),
      ('core', 'The intervals between bounces get shorter as the bounces get lower.',
       'the ball spends as long in the air between the small late bounces as between the first big '
       'ones'),
      ('core', 'It gains speed while falling and loses it while rising.',
       'the ball travels up and down at one unchanging speed'),
      ('major', 'It reverses direction at the surface and nowhere else.',
       'the ball turns round in mid-air before reaching the surface'),
      ('major', 'It ends up at rest on the surface, or rolling along it.',
       'the ball is still bouncing to its original height when the shot ends',
       'the shot lasts until the bouncing dies away'),
      marks('the ball', 'the colours and markings on the ball'),
      ('minor', 'The ball flattens where it presses on the surface and springs back out.',
       'the ball stays a perfect rigid sphere at the moment it is pressed against the floor',
       'the contact is close enough to see the ball outline clearly')),
    note="Scenario 39, 'A basketball hits the ground after being dropped', is the same physical "
         "situation in the Collisions subcategory of category 2 and carries the same mechanism.")

add('damped-oscillation', 90,
    'A swing left to itself rises less on each pass while the time per pass stays the same.',
    S(('core', 'A child on a swing is present.'),
      ('core', 'The swing goes back and forth more than once.'),
      ('minor', 'The swing hangs from a fixed frame, beam or branch.'),
      ('minor', 'Nobody is pushing the swing.')),
    P(('fatal', 'Each pass rises no higher than the one before, unless the child is plainly pumping.',
       'the swing climbs higher and higher with the child sitting still and nobody pushing'),
      ('core', 'The height falls off gradually, pass by pass.',
       'the swing holds exactly the same height for the whole shot with nothing driving it'),
      ('core', 'Each pass takes about the same time as the swing dies down.',
       'the passes take plainly longer and longer as the swing shrinks'),
      ('core', 'The child is fastest at the bottom and momentarily still at each end.',
       'the swing moves at one speed all the way through its arc'),
      ('major', 'The ropes or chains stay taut and the same length, and the top stays fixed.',
       'the ropes stretch, go slack at the top of a pass, or the frame travels with the swing'),
      ('major', 'The child moves with the seat and stays on it.',
       'the child stays upright and still while the seat swings away beneath them'),
      ('minor', "The child's hair and clothes are pushed about as they swing.",
       'hair and clothes hang dead still through a fast swing'),
      ('minor', 'The swing settles hanging straight down.',
       'the swing comes to rest out to one side',
       'the swinging dies out within the shot')))

add('string-vibration-decay', 91,
    'A plucked string vibrates in a narrowing band at a fixed tempo and comes to rest straight.',
    S(('core', 'A guitar with strings is present.'),
      ('core', 'A string is vibrating.'),
      ('core', 'The vibration dies away and the string becomes still.'),
      ('minor', 'The string is plucked or struck rather than already still.')),
    P(('fatal', 'The vibration dies away by itself.',
       'the string vibrates just as widely at the end of the shot as at the start, or its vibration '
       'grows with nothing touching it'),
      ('core', 'The width of the vibration shrinks steadily.',
       'the string vibrates at full width and then stops within a single frame'),
      ('core', 'The string stays fixed at both ends and vibrates only in between.',
       'the vibration carries on past the bridge or the nut, or an end of the string moves about'),
      ('core', 'It comes to rest straight along its own line.',
       'the string settles into a bent or wavy shape'),
      ('major', 'Only the width shrinks: the string does not flap more and more slowly as it fades.',
       'the vibration visibly slows its tempo as it dies away'),
      ('major', 'The string that was plucked is the one vibrating widely; the others stay near still.',
       'every string on the guitar swings wide when one is plucked'),
      ('minor', 'The body of the guitar stays still apart from small shivers.',
       'the whole guitar body swings back and forth along with the string'),
      ('minor', 'The vibrating string is a blurred band at its widest and a sharp line once still.',
       'the string is a sharp still line while it is plainly at full vibration')))

# ---- Conservation of Mechanical Energy (92-98) --------------------------
add('gravity-speed-exchange', 92,
    'A rider gains speed down each dip and loses it up each rise, following the track surface.',
    S(('core', 'A bicyclist is present.'),
      ('core', 'A pump track with rises and dips is present.'),
      ('core', 'The rider rides over its rises and dips.'),
      ('minor', 'The rider stays on the bike and moving throughout.')),
    P(('fatal', 'The bike stays on the track surface, wheels on the ground apart from deliberate '
                'jumps.',
       'the bike travels through the track surface, or floats above it while plainly rolling'),
      ('core', 'The rider speeds up going down each descent.',
       'the rider travels at one unchanging speed over the whole track'),
      ('core', 'The rider slows going up each rise.',
       'the rider speeds up while climbing a rise without pedalling'),
      ('major', 'Speed builds and falls with the slope rather than changing in jumps.',
       'the speed changes from one value to another between frames with no slope to account for it'),
      ('major', 'The wheels turn in the direction of travel and at a rate that goes with the ground '
                'speed.',
       'the wheels stay still while the bike rolls, or turn backwards while it moves forward'),
      ('major', 'Speed can be gained by pumping the dips, but not from nothing on level ground.',
       'the rider accelerates hard along a level straight without pedalling or pumping'),
      ('minor', 'The rider moves relative to the bike, pushing down and taking up the rollers.',
       'the rider stays a rigid statue over every roller'),
      ('minor', 'The bike leans into the turns of the track.',
       'the bike stays bolt upright through a hard turn',
       'the track turns')))

add('gravity-speed-exchange', 93,
    'A skier loses speed climbing each mound and gains it on the far side, staying with the surface.',
    S(('core', 'A skier is present.'),
      ('core', 'Small mounds are present on the slope.'),
      ('core', 'The skier crosses the mounds.'),
      ('minor', 'The skier moves down the slope overall.')),
    P(('fatal', 'The skier moves down the slope overall.',
       'the skier climbs the slope with nothing driving them'),
      ('core', 'They slow as they come up each mound.',
       'the skier gains speed while climbing the near side of a mound'),
      ('core', 'They speed up going down the far side of each mound.',
       'the skier slows on the descents as well as the climbs'),
      ('major', 'The skier rises and falls with the shape of the surface.',
       'the skier holds a straight line through the mounds, cutting through the snow'),
      ('major', 'The skis stay on the snow under the skier except while airborne off a crest.',
       'the skis sink into the snow, or hang clear of it while the skier is plainly gliding'),
      ('major', 'Leaving the snow at a crest, the skier follows a free arc and comes back down.',
       'the skier floats along above the snow for a long stretch after a crest',
       'the skier leaves the snow at a crest'),
      ('minor', 'The knees and body flex to take up each mound.',
       'the skier stays rigid as a plank over every mound'),
      ('minor', 'Snow is disturbed where the skis pass.',
       'the snow is left smooth where the skis have plainly crossed it')),
    note="Their second standard, that the skier's motion 'remains smooth over the mounds', is a "
         "rendering property and is not used. The physical content -- slower over each crest, "
         "faster down each far side -- is P2 and P3.")

add('gravity-speed-exchange', 94,
    'A coaster train gains speed downhill and loses it uphill, and cannot crest a hill higher '
    'than the one it came from.',
    S(('core', 'A rollercoaster train is present.'),
      ('core', 'Several hills of different heights are present on the track.'),
      ('core', 'The train travels over them.'),
      ('minor', 'Nothing visibly drives the train between the hills.')),
    P(('fatal', 'The train stays on the track throughout.',
       'the train leaves the rails, floats above them, or passes through the structure'),
      ('core', 'It speeds up going downhill.',
       'the train travels at one unchanging speed over hills and dips alike'),
      ('core', 'It slows going uphill and is at its slowest at each crest.',
       'the train speeds up as it climbs, or is at its fastest at the top of a hill'),
      ('core', 'With nothing driving it between hills, it does not crest a hill higher than the one '
               'it came down from.',
       'the train climbs over a hill plainly taller than the one it descended, with nothing driving '
       'it'),
      ('major', 'The train stays coupled, keeping the order and spacing of its cars.',
       'cars stretch apart, bunch up, or come off from one another on the hills'),
      ('major', 'The train follows the shape of the track.',
       'the train cuts across a dip or a curve the rails do not follow'),
      ('minor', 'The track and its supports stay fixed as the train passes.',
       'the rails or the supports travel along with the train'),
      ('minor', 'Riders are pushed into their seats on the drops and lifted at the crests.',
       'riders sit perfectly undisturbed through the drops',
       'riders are visible')))

add('pendulum-swing', 95,
    'A pendulum swings between two turning points of about equal height, fastest at the bottom.',
    S(('core', 'A pendulum is present.'),
      ('core', 'It swings back and forth between two turning points.'),
      ('minor', 'A fixed pivot or support is visible.'),
      ('minor', 'It is left to swing rather than being pushed on each pass.')),
    P(('fatal', 'The weight swings back and forth about the pivot above it.',
       'the weight circles the pivot on a slack cord, or swings about some point that is not the '
       'pivot'),
      ('core', 'It is fastest at the lowest point and slowest at the two turning points.',
       'the weight is at its fastest at the ends of the swing, or moves at one speed throughout'),
      ('core', 'The two turning points are at about the same height, and neither is above the '
               'height it started from.',
       'one side of the swing rises plainly higher than the other, or the swing climbs above where '
       'it started'),
      ('major', 'Successive swings are about equal or a little lower, never higher.',
       'the swings grow with nothing pushing the pendulum'),
      ('major', 'The cord stays taut and keeps its length, with the pivot fixed.',
       'the cord stretches or goes slack, or the support point travels'),
      ('minor', 'The lowest point of the path is the same on every pass.',
       'the bottom of the swing wanders from pass to pass'),
      ('minor', 'Each pass takes about the same time.',
       'the passes take plainly different times from one to the next')),
    note="Three scenarios are pendulums judged for different things: 74 for the release "
         "and the conversion on the way down, 86 for the decay of the swings, and this one for the "
         "equality of the two turning points. They are not consistent with one another if read as "
         "absolutes -- 86 requires the height to fall, this one requires it to be kept -- so the "
         "items here ask only that the swing never rises higher than it started and that any loss "
         "is gradual, which holds in both readings.")

add('bowl-oscillation-decay', 96,
    'A marble released at the rim runs down, up the far side to nearly the same height, and '
    'oscillates.',
    S(('core', 'A marble is present.'),
      ('core', 'A half-pipe or curved channel is present.'),
      ('core', 'The marble is released near the top and runs down.'),
      ('minor', 'The marble starts at rest.')),
    P(('fatal', 'The marble runs down into the pipe and up the far side.',
       'the marble stays put at the rim, climbs out of the pipe on its own, or passes through the '
       'pipe surface'),
      ('core', 'It is fastest at the lowest point and slowest at the top of each side.',
       'the marble moves at one speed throughout, or is at its fastest at the top of a side'),
      ('core', 'It rises on the far side to about the height it was released from, and never higher.',
       'the marble climbs higher than its release height, or leaves over the rim with nothing added'),
      ('major', 'Each rise is the same or a little lower than the last.',
       'the rises grow pass by pass with nothing driving the marble'),
      ('major', 'The marble stays on the inside surface and follows its curve.',
       'the marble cuts across the pipe through open air, or sinks into the surface'),
      ('minor', 'The marble rolls, its pattern coming round with it.',
       'the marble slides up and down with its markings fixed toward the camera'),
      ('minor', 'It settles at the lowest point of the pipe.',
       'the marble comes to rest part-way up one side',
       'the oscillation dies out within the shot')))

add('yoyo-cycle', 97,
    'A yo-yo runs down its unwinding string, slows and reverses, and climbs back as it winds on.',
    S(('core', 'A yo-yo is present.'),
      ('core', 'A string is attached to it and held.'),
      ('core', 'The yo-yo travels down and back up.'),
      ('minor', 'The string is looped on a hand or finger.')),
    P(('fatal', 'The yo-yo descends as the string unwinds and climbs as it winds back on.',
       'the yo-yo descends while its string is winding on, or rises while the string pays out'),
      ('core', 'It speeds up going down and slows going up.',
       'the yo-yo travels up and down at one unchanging speed'),
      ('core', 'It spins as it runs, and the length of string paid out goes with how far down it is.',
       'the yo-yo hangs still on a fixed length of string while plainly travelling up and down'),
      ('major', 'The string stays attached to the hand at one end and to the yo-yo at the other, '
                'and its total length does not change.',
       'the string comes free at one end, or grows and shrinks by itself'),
      ('major', 'It does not rise above the hand, and it climbs only on the spin it has left or on '
                'a pull from the hand.',
       'the yo-yo rises above the hand holding it, or climbs back up with no spin left and no pull'),
      ('minor', 'The string is taut and straight between hand and yo-yo while the yo-yo hangs below.',
       'the string bows out slackly while the yo-yo hangs at the bottom of it'),
      ('minor', 'The spin is fastest at the bottom and dies away if the yo-yo is left there.',
       'a yo-yo left hanging at the bottom spins on at full rate to the end of the shot',
       'the yo-yo is left spinning at the bottom')))

add('bowl-oscillation-decay', 98,
    'A ball released at the rim rolls down, up the far side to nearly the same height, and '
    'oscillates lower each pass.',
    S(('core', 'A ball is present.'),
      ('core', 'A bowl is present.'),
      ('core', 'The ball is released on one side and rolls down into it.'),
      ('minor', 'The ball starts at rest.')),
    P(('fatal', 'The ball rolls down into the bowl and up the far side.',
       'the ball stays put on the side of the bowl, climbs out of it on its own, or passes through '
       'the bowl wall'),
      ('core', 'It is fastest at the bottom of the bowl and slowest at the top of each rise.',
       'the ball moves at one speed throughout, or is at its fastest at the top of a rise'),
      ('core', 'It rises on the far side to about the height it started from, and never higher.',
       'the ball climbs higher than the point it was released from, or leaves over the rim with '
       'nothing added'),
      ('major', 'Each pass rises the same or a little lower than the last.',
       'the rises grow pass by pass with nothing driving the ball'),
      ('major', 'The ball stays on the inside surface of the bowl and follows its curve.',
       'the ball cuts across the bowl through open air, or sinks into the surface'),
      ('minor', 'The ball rolls rather than sliding: its markings come round with it.',
       'the ball slides up and down the bowl with its markings fixed toward the camera'),
      ('minor', 'It settles at the lowest point of the bowl.',
       'the ball comes to rest part-way up one side',
       'the oscillation dies out within the shot')),
    note="Scenario 17, 'A ball rolls around in a bowl', is the same physical situation in the "
         "Circular Motion subcategory of category 1, and scenario 96 is the same again in a "
         "half-pipe; all three carry this mechanism. Their standards for 17 can be satisfied by a "
         "ball circling for ever at one height, which is the commonest wrong answer, so the "
         "height-per-pass items are the ones that do the work in all three.")

# ---- Heat Transfer and Phase Changes (99-105) ---------------------------
add('condensation-on-cold-surface', 99,
    'Droplets gather on the outside of a cold glass, grow, merge and run down, wetting the table.',
    S(('core', 'A cold drink in a glass or bottle is present.'),
      ('core', 'It sits on a tabletop.'),
      ('core', 'Water appears on the outside of the container.'),
      ('minor', 'The drink reads as cold -- ice, frost, or a chilled bottle.')),
    P(('fatal', 'The water gathers on the outside of the container.',
       'the beads of water appear on the inside of the glass, or down in the drink itself'),
      ('core', 'The wetting develops over the shot: droplets appear and grow.',
       'the outside of the glass goes from dry to fully beaded between two frames, or the droplets '
       'dry off while the drink is plainly still cold'),
      ('core', 'Droplets run downward once they are big enough, leaving trails.',
       'droplets slide upward or sideways across the glass'),
      ('major', 'Droplets merge into larger ones when they touch.',
       'droplets pass through one another, or stay separate where they plainly overlap'),
      ('major', 'Only the chilled surface beads up: the table and the room-temperature things around '
                'it stay dry apart from water that runs off the glass.',
       'the tabletop and the objects around it bead up as heavily as the cold glass'),
      ('minor', 'The droplets stay put on the glass rather than drifting about on it.',
       'beads wander around the surface of the glass as though blown along'),
      ('minor', 'A ring or pool of water gathers where the glass meets the table.',
       'water runs down the glass for a long time and the tabletop under it stays perfectly dry',
       'the base of the glass is in view')))

add('ice-melting', 100,
    'Ice cubes in hot water float mostly submerged, shrink from the outside in, and melt away.',
    S(('core', 'Ice cubes are present.'),
      ('core', 'A glass of water is present.'),
      ('core', 'The cubes go into the water.'),
      ('minor', 'The water reads as hot -- steam, or a hot vessel.')),
    P(('fatal', 'The cubes get smaller and melt away in the hot water.',
       'the cubes hold exactly their starting size in plainly hot water for the whole shot, or grow '
       'bigger'),
      ('core', 'They melt from the outside in, losing their corners and edges first.',
       'a cube keeps sharp square edges and then vanishes all at once'),
      ('core', 'The cubes float, with most of their bulk below the surface and a little above.',
       'the cubes sink to the bottom of the glass, or sit up on top of the water'),
      ('major', 'The water level rises when the cubes go in and does not fall as they melt.',
       'the level drops sharply as the ice disappears, or does not move at all when the cubes go in'),
      ('major', 'The cubes stay in the water and move with it.',
       'a cube hovers above the surface, or holds still while the water swirls around it'),
      ('minor', 'The melting is gradual and continuous.',
       'a cube goes from full size to gone between two frames'),
      ('minor', 'Steam above the water thins as the drink cools.',
       'the water steams just as hard after the ice has melted into it',
       'steam is visible at the start')))

add('conduction-into-spoon', 101,
    'A spoon is lowered into hot tea; it displaces liquid, disturbs the surface, and the tea steams.',
    S(('core', 'A metal spoon is present.'),
      ('core', 'A cup of hot tea is present.'),
      ('core', 'The spoon goes into the tea.'),
      ('minor', 'The tea reads as hot -- steam, or a hot mug.')),
    P(('fatal', 'The spoon enters the liquid and stays in it, resting against the cup.',
       'the spoon floats unsupported in the middle of the tea, or passes through the wall or the '
       'base of the cup'),
      ('core', 'The tea level rises as the spoon goes in, by about the bulk of the submerged part.',
       'the level does not move at all as the spoon is pushed in, or drops as it enters'),
      ('core', 'The spoon keeps its shape and stays solid in the hot tea.',
       'the spoon bends, softens or melts in the tea'),
      ('major', 'Putting the spoon in disturbs the surface: ripples spread out and settle.',
       'the surface stays glassy as the spoon is pushed into it'),
      ('major', 'Steam rises from the tea and drifts upward.',
       'steam sinks downward out of the cup, or hangs in one fixed shape'),
      ('minor', 'The handle stays above the surface and dry, with the tea no higher on it than its '
                'own level.',
       'the tea climbs the handle above the level of its own surface'),
      ('minor', 'Seen through the liquid from the side, the submerged part of the spoon looks '
                'offset from the part above the surface.',
       'the spoon is a single unbroken straight line through the waterline when seen through the '
       'side of a clear glass',
       'the spoon is seen through the side of a transparent vessel'),
      ('minor', 'Lifted out, the wetted part drips back into the cup.',
       'the spoon comes out of the tea perfectly dry',
       'the spoon is lifted out within the shot')),
    note="Their first key standard is 'steam forming on the spoon as it absorbs heat', which is "
         "muddled: steam does not form on a spoon put into hot tea, and the conduction their "
         "physics_prompt is about -- the handle warming -- has no signature a camera can see. This "
         "rubric judges what is visible instead: displacement, ripples, the steam over the tea, and "
         "the spoon staying solid.")

add('butter-melting', 102,
    'A pat of butter on a hot pan slumps, melts from the contact face and edges, and spreads as a '
    'liquid film.',
    S(('core', 'Butter is present.'),
      ('core', 'A pan is present and reads as hot.'),
      ('core', 'The butter is put on the pan and melts.'),
      ('minor', 'The butter starts as a solid piece.')),
    P(('fatal', 'The butter goes from solid to liquid on the hot pan.',
       'the butter stays a firm block on a plainly hot pan for the whole shot, or stiffens further'),
      ('core', 'It melts progressively: the solid piece shrinks and slumps while the pool grows.',
       'the piece jumps from a solid pat to a full pool between two frames'),
      ('core', 'The melting starts where the butter touches the pan and at its thin edges.',
       'a pool of liquid opens in the middle of the top face while the base is still solid'),
      ('major', 'The melted butter spreads as a thin film and runs to the lowest part of the pan.',
       'the melted butter holds a tall dome, or runs uphill across the pan'),
      ('major', 'The butter stays on the surface of the pan.',
       'the butter soaks into or passes through the pan'),
      ('major', 'It does not set again while the pan stays hot.',
       'the pool gathers itself back into a solid pat on the hot pan'),
      ('minor', 'The melting butter bubbles, foams or sizzles.',
       'butter melts on a plainly hot pan with no bubbling or movement in it at all'),
      ('minor', 'The film slides across the pan as the pan is tilted or moved.',
       'the melted butter stays in a fixed patch while the pan is tilted',
       'the pan is tilted or moved')))

add('boiling-and-steam', 103,
    'Water in a kettle on a flame comes to the boil after a while and vents steam from the spout.',
    S(('core', 'A kettle is present.'),
      ('core', 'A lit stove or flame is present.'),
      ('core', 'The kettle stands on the stove over the flame.'),
      ('minor', 'The kettle reads as holding water.')),
    P(('fatal', 'Steam leaves the kettle by the spout or the lid, not through its walls.',
       'vapour passes out through the solid metal of the kettle'),
      ('core', 'The boiling comes on after a spell on the flame, not at once.',
       'the kettle is already at a full boil the instant it is set on the stove'),
      ('core', 'The steam rises from the spout and disperses.',
       'the steam falls downward out of the spout, or holds one rigid unchanging shape'),
      ('core', 'Once boiling, it keeps steaming while the flame stays lit.',
       'the boil dies away on its own with the flame still burning under the kettle'),
      ('major', 'The flame stays under the kettle, touching and spreading around its base.',
       'the flame burns beside or above the kettle while heating it'),
      ('major', 'The kettle stays on the stove and keeps its shape.',
       'the kettle floats above the burner, or slumps and deforms on the flame'),
      ('minor', 'The plume is densest at the spout and thins as it rises.',
       'the plume is a solid unchanging shape far away from the spout'),
      ('minor', 'Bubbles form at the bottom, grow, and rise to the surface.',
       'the water boils with no bubbles rising through it',
       'the water inside is visible')),
    note="Their second key standard asks for bubbles at the bottom of the kettle. A kettle is "
         "opaque, so on almost every clip this is not judgeable at all -- the same problem as the "
         "copper tube in scenario 57. It is kept here behind a precondition on a transparent vessel, "
         "and the work is done by the delay, the vent path, and the plume.")

add('candle-wax-melting', 104,
    'A flame at the wick melts wax into a pool in the top of the candle, which shortens as it burns.',
    S(('core', 'A candle is present.'),
      ('core', 'It is lit and burning.'),
      ('minor', 'A wick is visible at the flame.'),
      ('minor', 'The flame lasts through the shot.')),
    P(('fatal', 'The flame sits at the wick and stays with it.',
       'the flame floats away from the wick, or burns at a place on the candle where there is no wick'),
      ('core', 'Wax melts where the flame heats it, so liquid gathers in the top of the candle '
               'around the wick.',
       'the wax stays entirely solid right up to the flame for the whole shot'),
      ('core', 'The flame points upward and its shape wavers.',
       'the flame points sideways or downward in still air, or holds one frozen shape'),
      ('major', 'The candle gets shorter, or its pool deepens, as it burns.',
       'the candle grows taller as it burns, or is untouched after a long burn'),
      ('major', 'The molten wax goes where gravity puts it: it fills the hollow at the top, and any '
                'runs go down the outside.',
       'liquid wax climbs up the candle, or hangs on the side in beads that never run down'),
      ('major', 'Wax that runs well down the cool side sets again.',
       'wax that has run right to the base stays liquid and keeps flowing to the end of the shot',
       'wax runs down the outside'),
      ('minor', 'Runs down the side start only where the pool overflows or the rim is breached.',
       'wax streams down a side while the pool at the top is plainly well below the rim'),
      ('minor', 'The wick darkens and shortens as it burns.',
       'the wick stays a clean pale thread through a long burn')),
    note="Their second key standard requires the wax to drip down the sides. An evenly burning "
         "candle in still air keeps its melt in the crater at the top and does not drip at all, so "
         "taking that standard literally would fail a correct clip. Here the pool is the core item "
         "and the dripping is only judged once runs have started.")

add('chocolate-softening', 105,
    'Chocolate in a warm hand softens and sags where it is held, and smears the fingers.',
    S(('core', 'A person is present, holding chocolate.'),
      ('core', 'The chocolate is held in a hand.'),
      ('core', 'The chocolate softens or loses its shape over the shot.'),
      ('minor', 'The chocolate starts as a firm solid piece.')),
    P(('fatal', 'The chocolate softens rather than stiffening.',
       'the chocolate becomes harder, or frosts over, in a warm hand'),
      ('core', 'The softening builds over the shot rather than happening in one jump.',
       'the piece goes from firm to a puddle between two frames'),
      ('core', 'It softens first where the hand is touching it.',
       'the exposed top face melts away while the part gripped between the fingers stays firm'),
      ('major', 'The softened piece sags, bends or takes the shape of the grip.',
       'the chocolate keeps perfectly sharp moulded edges while plainly melting'),
      ('major', 'Melted chocolate stays on the hand and the piece: it smears the fingers, and any '
                'that runs goes downward.',
       'melted chocolate runs upward along the fingers, or disappears as it melts'),
      ('major', 'It does not set firm again while it is still held in the warm hand.',
       'the softened chocolate hardens back into a crisp piece in the same warm grip'),
      ('minor', 'The surface loses its crisp moulded pattern where it is handled.',
       'the moulded pattern stays sharp after the piece has plainly been worked in a warm hand'),
      ('minor', 'A wrapper or foil stays put and does not melt.',
       'the wrapper melts along with the chocolate',
       'a wrapper or foil is present')))
