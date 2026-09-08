# phyworldbench 211-245: Deformations and Elasticity.
# Same authoring flow as the earlier blocks. Cross-check against KS[i] -- ids 212, 223 and 226 are
# among the eleven records whose standards are wrapped in a dict.
#
# This category is where the benchmark repeats itself most: eleven of the thirty-five scenarios are
# a physical situation already covered in categories 2, 3 or 5, so they carry the earlier mechanism
# name and their notes point at the twin. The elastic/plastic/brittle split that organises the
# category is also the axis the rubrics turn on, and it reduces to one question per scenario -- does
# the deformation come back, stay, or end in fracture -- so the core items are mostly about which of
# the three the clip commits to and whether it stays consistent with that choice.
#
# Two recurring problems in the standards. The rendering vocabulary is at its thickest here:
# 'smoothly', 'without any sudden jerks', 'without abrupt jumps', 'fluidly without any unnatural or
# jerky movements', 'without any delays or unnatural pauses', 'no sudden or abrupt movements'. None
# of it names a physical observable. And two standards in the thermal block contradict their own
# physics_prompt: 243 asks plastic wrap to EXPAND when heated while its prompt has it conforming
# tightly to the surface, which is shrinking; 244 asks for a constant rate of rise where the
# physics gives a decelerating one.


def cons(o):
    return ('fatal',
            f'{o[0].upper()}{o[1:]} keeps its own identity for the whole shot, and it does not pass '
            f'through any solid surface.',
            f'{o} turns into a different object or a different material, passes through something '
            f'solid, or disappears and re-appears')


def recovers(o):
    return ('core', f'{o[0].upper()}{o[1:]} comes back to the shape it started with once the force '
                    f'is off it.',
            f'{o} stays deformed after the force is removed')


def keeps(o, what):
    return ('core', f'{what[0].upper()}{what[1:]} stays once it has been made: {o} does not spring '
                    f'back to how it was.',
            f'{o} returns to its original undeformed shape on its own')


def while_loaded(o):
    return ('major', f'{o[0].upper()}{o[1:]} deforms while the force is on it and not before.',
            f'{o} is already deformed before anything touches it, or it deforms after the force has '
            f'plainly been taken off')


def unmarked(hard, soft):
    return ('major', f'{hard[0].upper()}{hard[1:]} comes through unmarked; it is {soft} that gives '
                     f'way.',
            f'{hard} deforms instead of {soft}')


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


# ---- Material Flexibility (211-217) --------------------------------------
add('stretch-fit-recovery', 211,
    'The silicone case stretches to go over the phone and closes back tight around it.',
    S(('core', 'A silicone phone case is present.'),
      ('core', 'A phone is present.'),
      ('core', 'The case is stretched over the phone.'),
      ('minor', 'The case reads as soft silicone or rubber rather than hard plastic.')),
    P(cons('the case'),
      ('core', 'The case stretches where it is pulled over an edge or a corner and closes back down '
               'once past it.',
       'the case slides on without changing shape anywhere, or it stays stretched open after the '
       'phone is in'),
      ('core', 'The case ends up fitting the phone closely rather than baggy or split.',
       'the case hangs loose on the phone at the end, or it is left torn'),
      ('major', 'It thins where it is stretched most and thickens again as it relaxes.',
       'the case keeps exactly one thickness while being pulled over a corner'),
      while_loaded('the case'),
      ('major', 'The case stays one continuous piece: it does not tear under ordinary fitting force.',
       'the silicone splits or a corner tears off as it is stretched on'),
      marks('the case', 'its texture, colour and cut-outs'),
      ('minor', 'The phone keeps its own shape while the case is worked over it.',
       'the phone bends or squashes as the case is pulled onto it')),
    note="Their third standard, that the material retains its texture throughout, is a real "
         "observable and is used -- it is the item that catches a case that morphs into a different "
         "material as it stretches. Their second, the return to shape, is the core requirement. "
         "Their first is mostly rendering ('smoothly without any sudden jerks'), and the usable "
         "residue is 'without tearing', which is a separate item here. The addition is the local "
         "thinning under stretch, which is what distinguishes silicone being stretched from a case "
         "that simply slides on rigid.")

add('elastic-stretch', 212,
    'The pulled rubber band gets longer and thinner under tension and takes back its length when let '
    'go.',
    S(('core', 'A rubber band is present.'),
      ('core', 'Two fingers pull on it.'),
      ('core', 'The band gets longer as it is pulled.'),
      ('minor', 'The band starts slack or unstretched rather than already taut.')),
    P(cons('the band'),
      ('core', 'The band lengthens while it is being pulled and by more the harder it is pulled.',
       'the band keeps exactly one length while the fingers plainly move further apart'),
      ('core', 'The band thins as it lengthens rather than keeping the same thickness.',
       'the band stays exactly as thick when stretched as when slack'),
      ('major', 'The band stays in contact with both fingers and stays taut between them, in a '
                'straight line.',
       'the band sags between fingers that are plainly pulling it apart, or it comes off a finger and '
       'stays stretched'),
      ('major', 'If it is released it shortens again, and faster than it was stretched.',
       'the band eases back at the same slow rate it was pulled out at, or it stays long after '
       'release',
       'the band is released during the shot'),
      ('major', 'The band stays whole rather than snapping under an ordinary pull.',
       'the band breaks apart while being stretched a modest amount'),
      marks('the band', 'its colour and any printing on it')),
    note="Their sole standard is 'the rubber band smoothly elongates without any abrupt jumps or "
         "breaks', of which only 'without breaks' names anything physical. Everything else is "
         "written from scratch. Scenarios 68, 'A rubber band is pulled from both ends', and 79, 'A "
         "rubber band is stretched and then released', are the same physical situation in categories "
         "3 and 2 and carry this mechanism; 79 is judged for the release and this one for the "
         "stretch, so the release item here sits behind a precondition.")

add('flex-and-recover', 213,
    'The ruler bows under the force and springs flat again when it is let go.',
    S(('core', 'A plastic ruler is present.'),
      ('core', 'A force is applied to it and then taken off.'),
      ('core', 'The ruler bends while the force is on it.'),
      ('minor', 'The ruler reads as thin plastic rather than metal or wood.')),
    P(cons('the ruler'),
      while_loaded('the ruler'),
      recovers('the ruler'),
      ('major', 'The ruler bends into a smooth curve along its length rather than folding at a '
                'point.',
       'the ruler kinks at one spot and stays straight either side of it'),
      ('major', 'The ruler stays whole: it does not snap under a bend it plainly springs back from.',
       'the ruler breaks and the pieces then behave as though it were still one piece'),
      ('minor', 'The ruler keeps its length as it bends rather than getting visibly longer or '
                'shorter.',
       'the ruler stretches out longer as it is bowed'),
      marks('the ruler', 'its scale markings')),
    note="Their standards -- continuous bending under force without breaking, and full return to "
         "shape with no permanent deformation -- are both sound and both used, and this is one of the "
         "cleaner records in the category. The additions are the mode of bending (a smooth curve, "
         "not a hinge) and length conservation, which is the give-away when a clip animates a bend "
         "by stretching the geometry. Scenario 217 is the same mechanism for a credit card.")

add('stiff-flex-limit', 214,
    'The wooden stick gives only a little under pressure and springs back, and it snaps if pushed '
    'much further.',
    S(('core', 'A wooden stick is present.'),
      ('core', 'Pressure is applied to it.'),
      ('core', 'The stick bends while the pressure is on it.'),
      ('minor', 'The stick reads as wood rather than plastic or metal.')),
    P(cons('the stick'),
      while_loaded('the stick'),
      ('core', 'The bend is small: the stick gives far less than a plastic ruler or a rubber rod '
               'would under the same handling.',
       'the wooden stick bends round into a deep curve or a loop while staying whole'),
      ('core', 'What the clip commits to holds together: a stick that only bends a little springs '
               'back, and a stick pushed into a deep bend snaps rather than holding the curve.',
       'the stick bends deeply and then springs back unharmed, or it takes on a permanent gentle '
       'curve and stays there like bent wire'),
      ('major', 'The bend is spread along the stick rather than being a fold at one point.',
       'the stick hinges at a single spot with the rest dead straight'),
      ('major', 'If it does break, the break is where the bend was greatest and the pieces separate.',
       'the stick breaks somewhere it was not bent, or the pieces stay joined as though nothing had '
       'happened',
       'the stick breaks during the shot'),
      ('minor', 'The grain and any bark stay with the stick.',
       'the surface texture of the stick changes or slides along it as it bends')),
    note="Their standards ask for a slight but noticeable bend without breaking and for the bend "
         "'not excessive'. The substance is right -- wood has a small strain to failure -- but there "
         "is no number available and none is used, per _policy.json's exclusion of anything needing "
         "measurement. It is restated comparatively: the stick gives visibly less than a plastic or "
         "rubber item would. The added core item is internal consistency, because the two wrong "
         "answers here pull in opposite directions -- a stick that bends into a deep curve and "
         "springs back, and one that takes a permanent bend like wire.")

add('press-load-yield', 215,
    'The press bows the steel rod, and how it ends up follows from how far it was pushed.',
    S(('core', 'A hydraulic press is present.'),
      ('core', 'A steel rod is present.'),
      ('core', 'The press pushes on the rod and the rod deforms.'),
      ('minor', 'The rod reads as steel -- metallic, stiff and unpainted or plain.')),
    P(cons('the rod'),
      while_loaded('the rod'),
      ('core', 'The rod resists visibly: it takes the full force of the press to move it at all, and '
               'it does not fold up like something soft.',
       'the rod squashes and folds under the press the way a plastic tube would'),
      ('core', 'What the clip commits to holds together: a rod that is bowed only slightly springs '
               'back, and a rod bent right over stays bent.',
       'the rod is bent into a deep permanent-looking curve and then springs perfectly straight, or '
       'it holds a barely visible bow after the press has plainly been withdrawn'),
      ('major', 'The rod bends rather than shortening: a slender rod under end load bows sideways '
                'instead of getting visibly shorter.',
       'the rod visibly shortens along its length under the press'),
      ('major', 'The press moves and bears on the rod before the rod deforms.',
       'the rod deforms while the ram is plainly still clear of it'),
      unmarked('the press ram', 'the rod'),
      fixed('the press frame')),
    note="Their standards ask for the rod to bend and then return 'to its original form' with the "
         "bend 'slight'. Those two pull against each other in practice: a hydraulic press applies "
         "far more than the force needed to yield a steel rod, so a visible bend from a press is "
         "usually permanent, and a bend small enough to be fully elastic is barely visible. Rather "
         "than pick one, the core item asks for internal consistency between the size of the bend and "
         "whether it recovers. Scenario 69, 'A steel rod is pushed from both ends', is the axial "
         "version and carries the related point that steel does not visibly shorten.")

add('wind-load-elastic-recovery', 216,
    'The branch bends away under the wind and comes back upright as the wind eases.',
    S(('core', 'A tree branch is present.'),
      ('core', 'Wind pushes on it.'),
      ('core', 'The branch bends while the wind is on it.'),
      ('minor', 'The wind shows elsewhere too -- leaves, grass or other branches moving.')),
    P(cons('the branch'),
      ('core', 'The branch bends away from the wind, in the direction the wind is going.',
       'the branch bends into the wind, or it bends in a direction unrelated to where the wind comes '
       'from'),
      recovers('the branch'),
      ('major', 'The bend follows the wind: it deepens in a gust and eases in a lull.',
       'the branch holds exactly one bend through a visible change in the wind, or it bends and '
       'unbends with the surrounding foliage plainly still'),
      ('major', 'The branch bends as a curve, most at the thin outer end and least at the thick '
                'base.',
       'the branch swings rigidly from its base like a hinged pole, or it bends most at the trunk '
       'and stays straight at the tip'),
      ('major', 'The branch stays attached to the tree and stays whole.',
       'the branch snaps off in ordinary wind and the tree behaves as if it had not'),
      ('minor', 'The leaves and twigs stay on the branch and move with it.',
       'the leaves hang still while the branch they are on sweeps back and forth')),
    note="Their standards are almost entirely rendering -- 'bends fluidly without any unnatural or "
         "jerky movements', 'returns to its original position smoothly'. The usable residue is the "
         "return without permanent deformation, which is the core item. The rest is written from "
         "scratch, and the two items that matter are direction (a wind-loaded branch bends downwind) "
         "and the shape of the bend (a tapered cantilever bends most at the tip). Scenario 78, 'A "
         "palm tree is hit by strong winds', is the same physical situation in category 3 and "
         "carries this mechanism.")

add('flex-and-recover', 217,
    'The credit card bows under pressure and snaps back flat when released.',
    S(('core', 'A credit card is present.'),
      ('core', 'Pressure is applied to it and then released.'),
      ('core', 'The card bends while the pressure is on it.'),
      ('minor', 'The card reads as a thin stiff card rather than paper or metal.')),
    P(cons('the card'),
      while_loaded('the card'),
      recovers('the card'),
      ('major', 'The card returns to flat quickly on release rather than easing back slowly.',
       'the card creeps back to flat over several seconds after being let go'),
      ('major', 'The card bends into a smooth curve rather than creasing at a line.',
       'the card takes a hard fold and then flattens out with the crease gone'),
      ('minor', 'The card keeps its size as it bends.',
       'the card stretches longer or wider as it is bowed'),
      marks('the card', 'its printing, chip and stripe')),
    note="Their two standards -- visible bending under pressure, return to the original flat shape "
         "-- are sound and are used. The additions are the speed of the return, which is what "
         "distinguishes a stiff elastic card from a slowly relaxing plastic one, and the distinction "
         "between a curve and a crease: a card bent past its limit takes a permanent white crease, so "
         "a clip that shows a hard fold flattening out with no trace is having it both ways. "
         "Scenario 213 is the same mechanism for a plastic ruler.")

# ---- Elastic Rebound (218-224) -------------------------------------------
add('bounce-decay', 218,
    'The rubber band ball squashes on the desk, springs back up, and each bounce is lower than the '
    'last.',
    S(('core', 'A rubber band ball is present.'),
      ('core', 'It is dropped onto a desk.'),
      ('core', 'It bounces off the desk.'),
      ('minor', 'The ball reads as wound rubber bands rather than a solid ball.')),
    P(cons('the ball'),
      ('core', 'The ball squashes where it meets the desk and rounds out again as it leaves.',
       'the ball stays perfectly round through the contact, or it stays flattened after it has '
       'left the desk'),
      ('core', 'Each bounce takes it lower than the one before, and it ends up at rest on the desk.',
       'the ball bounces back to the height it fell from every time, or each bounce takes it higher'),
      ('major', 'It speeds up on the way down and slows on the way up.',
       'the ball travels at one unchanging speed through its fall and rise'),
      ('major', 'The squashing happens only while it is touching the desk.',
       'the ball is deformed in mid-air between bounces'),
      unmarked('the desk', 'the ball'),
      ('minor', 'The rubber bands stay wound into the ball rather than coming loose.',
       'bands spring free from the ball on impact and the ball is unchanged')),
    note="Their sole standard, that the ball rebounds 'without any delays or unnatural pauses', is "
         "a rendering phrase and names nothing physical; every item here is written from scratch. "
         "Scenarios 39, 'A basketball hits the ground after being dropped', and 89, 'A bouncy ball "
         "bounces freely', are the same physical situation in categories 2 and 3 and carry this "
         "mechanism, as do scenarios 219 and 224 in this block.")

add('bounce-decay', 219,
    'The basketball flattens against the ground, springs back up, and each bounce is lower than the '
    'last.',
    S(('core', 'A basketball is present.'),
      ('core', 'It is dropped onto the ground.'),
      ('core', 'It bounces off the ground.'),
      ('minor', 'The ball starts from a drop rather than being thrown down.')),
    P(cons('the ball'),
      ('core', 'The ball flattens where it meets the ground and rounds out again as it leaves.',
       'the ball stays perfectly spherical through the contact, or it stays flattened after leaving '
       'the ground'),
      ('core', 'It rebounds lower than it fell from, and each later bounce is lower again.',
       'the ball returns to the height it was dropped from, or each bounce takes it higher than the '
       'last'),
      ('major', 'It speeds up as it falls and slows as it rises.',
       'the ball moves at one unchanging speed through the fall and the rise'),
      ('major', 'The flattening happens only during contact.',
       'the ball is squashed while in mid-air between bounces'),
      ('major', 'The bounces come closer together as they get lower.',
       'the time between bounces stays the same while the bounces plainly get lower'),
      marks('the ball', 'its seams and its pebbling')),
    note="Their standards -- visible compression on impact, a rebound to some height -- are sound "
         "and are used, though 'to a certain height' fixes nothing on its own; the item that does "
         "the work is that the rebound is LOWER than the drop, since a ball returning to its "
         "starting height satisfies their standard and creates energy. This scenario is a duplicate "
         "of 39, 'A basketball hits the ground after being dropped', in the Collisions subcategory "
         "of category 2, and carries the same mechanism.")

add('trampoline-rebound', 220,
    'The trampoline bed stretches down under the jumper and throws them back up as it snaps flat.',
    S(('core', 'A trampoline is present.'),
      ('core', 'Someone jumps on it.'),
      ('core', 'The bed stretches down when they land on it.'),
      ('minor', 'The jumper leaves the bed again during the shot.')),
    P(('fatal', 'The jumper and the bed stay in contact while the bed is stretched, and the jumper '
                'does not pass through it.',
       'the jumper passes through the bed, or the bed stretches down with the jumper plainly clear '
       'of it'),
      ('core', 'The bed goes down as the jumper lands and comes back up as they leave.',
       'the bed stays flat under the landing, or it stays stretched down after the jumper has gone '
       'up'),
      ('core', 'The jumper is slowed to a stop on the way down and then pushed back up.',
       'the jumper reverses direction the instant they touch the bed with no give at all, or they '
       'sink in and stay down'),
      ('major', 'The bed is deepest where the jumper is and the deformation follows them about.',
       'the bed dips in a place the jumper is not, or the dip stays put as the jumper moves across '
       'it'),
      ('major', 'The bed comes back flat between bounces rather than staying dished.',
       'the bed holds a permanent hollow after the jumper has left it'),
      ('major', 'The jumper goes no higher than the energy they put in: an unaided bounce does not '
                'take them higher than the one before.',
       'each bounce takes the jumper higher than the last with no extra push from them'),
      ('minor', 'The frame and the springs stay in place while the bed stretches.',
       'the frame flexes as much as the bed, or a spring comes free and the bed still works')),
    note="Their standards -- the bed stretching downward on landing, and the return to shape "
         "propelling the jumper up -- are both sound and both used. The additions are the deformation "
         "following the jumper rather than sitting in a fixed place, the bed recovering fully between "
         "bounces, and the energy bound on successive bounces. Scenario 80, 'A child jumps onto a "
         "trampoline', is the same physical situation in category 3 and carries this mechanism; "
         "scenario 223 is the cantilever version with a diving board.")

add('wall-rebound-compression', 221,
    'The rubber ball squashes against the wall, springs back round and comes away slower than it '
    'arrived.',
    S(('core', 'A rubber ball is present.'),
      ('core', 'A wall is present.'),
      ('core', 'The ball bounces off the wall.'),
      ('minor', 'The ball is travelling under its own momentum rather than being held against the '
                'wall.')),
    P(('fatal', 'The ball and the wall meet at their surfaces: the ball rebounds rather than going '
                'into the wall.',
       'the ball passes into or through the wall, or it turns back before reaching it'),
      ('core', 'The ball squashes against the wall at contact and springs back round as it leaves.',
       'the ball stays perfectly round through the contact, or it stays flattened after it has come '
       'away'),
      ('core', 'The ball comes off the wall more slowly than it arrived.',
       'the ball leaves faster than it came in, or at exactly the speed it arrived at'),
      ('major', 'The squashing happens only while the ball touches the wall.',
       'the ball is deformed in mid-flight before contact, or after it has left'),
      ('major', 'The ball comes away from the face of the wall on the side it arrived from.',
       'the ball rebounds along the wall face, or into the wall'),
      unmarked('the wall', 'the ball'),
      marks('the ball', 'its colour and any markings')),
    note="Their standards -- the ball springs back to shape after losing contact, and it rebounds "
         "some distance -- are used, with the same caveat as scenario 219: 'to a certain distance' "
         "fixes nothing, and the item that discriminates is that the rebound is slower than the "
         "approach. Scenario 165, 'A soccer ball hits a wall', is the same physical situation in "
         "category 5 and carries this mechanism.")

add('spring-compression', 222,
    'The spring shortens under the press, its coils closing up, and it springs back to length when '
    'released.',
    S(('core', 'A spring is present.'),
      ('core', 'It is compressed.'),
      ('core', 'It is released and returns during the shot.'),
      ('minor', 'The spring reads as a coiled metal spring rather than a rubber tube.')),
    P(cons('the spring'),
      ('core', 'The spring gets shorter as it is pressed and the gaps between the coils close up.',
       'the spring keeps the same length under a plainly advancing press, or it shortens with the '
       'coil spacing unchanged'),
      recovers('the spring'),
      ('major', 'It takes more force the further it is compressed.',
       'the spring compresses just as easily at the end of its travel as at the start, right down to '
       'closed'),
      ('major', 'On release it returns quickly and may overshoot and oscillate before settling.',
       'the spring eases back to length as slowly as it was compressed'),
      ('major', 'The coils stay a single continuous helix rather than passing through each other.',
       'coils overlap or pass through one another as the spring closes up'),
      ('minor', 'The spring keeps its coil diameter as it shortens.',
       'the spring gets visibly fatter or thinner in diameter as it is compressed')),
    note="Their three standards -- visible compression, return to shape, no permanent deformation -- "
         "are sound and are used. The additions are the stiffening with compression, the quick "
         "return with possible overshoot, and the coils not interpenetrating, which is the "
         "give-away when a clip animates a spring by scaling the geometry. Scenario 66, 'A spring is "
         "pressed from both ends by hand', is the same physical situation in category 3 and carries "
         "this mechanism.")

add('board-recoil-launch', 223,
    'The diving board bows down under the diver and springs back up as they leave it.',
    S(('core', 'A diver is present.'),
      ('core', 'A diving board is present.'),
      ('core', 'The board bends down under the diver.'),
      ('minor', 'The diver leaves the board during the shot.')),
    P(('fatal', 'The diver stands on the board and the board carries them, rather than either '
                'passing through the other.',
       "the diver's feet pass into the board, or the board bends with the diver plainly clear of it"),
      ('core', 'The board bends down while the diver bears on it and springs back once they leave.',
       'the board stays flat under the diver, or it stays bent down after they have gone'),
      ('core', 'The board bends as a cantilever: most at the free tip and least at the fixed end.',
       'the board bends most at its mounting and stays straight at the tip, or it drops as a rigid '
       'plank'),
      ('major', 'The board springs up past flat and then settles, rather than stopping dead at flat.',
       'the board returns to level and stops there instantly with no recoil at all'),
      ('major', 'The diver goes up as the board comes up, and higher than the board alone would '
                'throw a dead weight.',
       'the diver leaves the board downward, or they rise while the board is still going down'),
      ('major', 'The board stays fixed at its mounting.',
       'the board comes loose from its support and still launches the diver'),
      ('minor', 'The board settles back to level and stops rather than flexing on indefinitely.',
       'the board keeps oscillating at the same size for the rest of the shot')),
    note="Their two standards -- the board bending down under the diver's weight, and a recoil once "
         "they leave -- are both sound and both used. The additions are the cantilever shape of the "
         "bend, the overshoot past flat, and the decay of the flexing afterwards. Scenario 220, the "
         "trampoline, is the same energy-storing mechanism with a membrane instead of a beam.")

add('bounce-decay', 224,
    'The tyre squashes where it lands, bounces back up, and each bounce is lower than the last.',
    S(('core', 'A rubber tyre is present.'),
      ('core', 'It is dropped and lands on the ground.'),
      ('core', 'It bounces off the ground.'),
      ('minor', 'The tyre reads as a rubber tyre rather than a solid wheel.')),
    P(cons('the tyre'),
      ('core', 'The tyre squashes flat where it meets the ground and rounds out again as it leaves.',
       'the tyre keeps its exact round section through the contact, or it stays squashed after it '
       'has left the ground'),
      ('core', 'It rebounds lower than it fell from and settles to rest.',
       'the tyre bounces back to the height it was dropped from, or it bounces higher each time'),
      ('major', 'The squashing is at the part touching the ground and nowhere else.',
       'the tyre deforms on the side away from the ground, or all round at once'),
      ('major', 'It speeds up as it falls and slows as it rises.',
       'the tyre travels at one unchanging speed through the fall and the rise'),
      ('major', 'The tyre may topple or roll after landing rather than balancing on its edge.',
       'the tyre stands perfectly upright on its tread and stays there through several bounces'),
      marks('the tyre', 'its tread pattern and sidewall lettering')),
    note="Their standards -- deformation at the point of contact, and a quick return to shape after "
         "impact -- are both sound and both used. The addition is the decay, which neither standard "
         "mentions and which is the commonest wrong answer for any bouncing body. Scenarios 39, 89, "
         "218 and 219 are the same mechanism with other objects.")

# ---- Plastic Deformation (225-231) ---------------------------------------
add('plastic-bend-retention', 225,
    'The wire takes the coiled shape it is bent into and holds it.',
    S(('core', 'A metal wire is present.'),
      ('core', 'It is bent into a spiral or coil.'),
      ('core', 'The wire holds the new shape rather than springing straight.'),
      ('minor', 'The wire starts straight or in some other shape before being bent.')),
    P(cons('the wire'),
      keeps('the wire', 'the coiled shape'),
      ('core', 'The wire takes its new shape only where it is actually bent, as the hands work along '
               'it.',
       'the whole wire coils up at once ahead of the hands, or it changes shape in places nothing '
       'has touched'),
      ('major', 'The wire keeps its length: bending it into a coil does not make it longer or '
                'shorter.',
       'the wire grows visibly longer as it is coiled up'),
      ('major', 'The wire keeps its thickness and stays one continuous piece.',
       'the wire thins away to nothing at the bends, or it parts and the pieces still coil together'),
      ('major', 'It resists: the wire needs real force at each bend rather than falling into shape.',
       'the wire coils itself up under no more than its own weight'),
      ('minor', 'The bends are rounded rather than sharp corners, since a wire has a smallest radius '
                'it will take.',
       'the wire turns square corners with no radius at all')),
    note="Their standards -- a permanent change of shape, and the surface and structure staying "
         "intact -- are both sound and both used. The additions are the progression (the wire takes "
         "shape where the hands work, not all at once), length conservation, and the finite bend "
         "radius. Scenario 226 is the same mechanism applied to a spoon.")

add('plastic-bend-retention', 226,
    'The spoon bends where it is worked and stays bent when the hands come off.',
    S(('core', 'A metal spoon is present.'),
      ('core', 'It is bent by hand.'),
      ('core', 'The spoon stays bent after the hands stop, as the caption says.'),
      ('minor', 'The spoon starts straight and undamaged.')),
    P(cons('the spoon'),
      keeps('the spoon', 'the bend'),
      ('core', 'The spoon bends where the hands act on it -- usually the neck between bowl and '
               'handle -- and not elsewhere.',
       'the spoon bends in a place no hand is near, or it curves evenly along its whole length'),
      ('major', 'It resists: the spoon moves only while real force is on it and stops when the hands '
                'stop.',
       'the spoon keeps bending further on its own after the hands stop, or it folds up under a light '
       'touch'),
      ('major', 'The spoon stays one piece rather than snapping under an ordinary bend.',
       'the spoon breaks in two and the pieces then behave as if still joined'),
      ('major', 'The metal stays metal: it keeps its thickness and its shine at the bend.',
       'the spoon stretches thin like putty at the bend, or it changes material as it deforms'),
      ('minor', 'The bowl of the spoon keeps its own shape while the neck bends.',
       'the bowl squashes or reshapes itself as the neck is bent')),
    note="This is one of the eleven records whose key_standards are wrapped in a dict. The real "
         "standards -- the bending is shown, and the distorted spoon retains its shape 'without "
         "noticeable recovery' -- are used; the second is the core of the scenario. The additions "
         "are where the bend goes (metal yields at the thinnest section) and that the metal stays "
         "metal rather than stretching like putty, which is the commonest way a clip renders a bend.")

add('crash-crumple', 227,
    'The fender folds and wrinkles in the collision and stays deformed afterwards.',
    S(('core', 'A car is present.'),
      ('core', 'A collision happens.'),
      ('core', 'The fender crumples.'),
      ('minor', 'The fender is intact before the impact.')),
    P(('fatal', 'The fender deforms where the impact acts on it and only from the moment of contact.',
       'the fender crumples before anything reaches it, or the impacting object passes through it '
       'without deforming it'),
      ('core', 'The fender folds and wrinkles rather than shrinking evenly or bouncing back.',
       'the fender dents smoothly and pops back out, or the whole panel scales down in size'),
      keeps('the fender', 'the crumpling'),
      ('major', 'The damage is worst at the impact and lessens away from it.',
       'the far side of the car is more damaged than the point of contact'),
      ('major', 'The metal folds rather than fragmenting: sheet steel is ductile.',
       'the fender shatters into separate pieces like glass'),
      ('major', 'The rest of the car moves as one with the fender rather than being unaffected.',
       'the car body carries on undisturbed while the fender crumples, or the two separate'),
      ('minor', 'Paint on the crumpled region creases and flakes rather than staying perfectly '
                'smooth.',
       'the paint stays glossy and unbroken over deep folds')),
    note="Their standards -- visible crumpling with bends, wrinkles or folds, and no reversion "
         "afterwards -- are both sound and both used, and this record is one of the better ones in "
         "the category. The additions are the damage gradient away from the impact, the ductile mode "
         "of failure, and the paint following the metal. Scenario 38, 'A car crashes into a "
         "stationary barrier', is the same physical situation in category 2 and carries this "
         "mechanism.")

add('mouldable-reshaping', 228,
    'The clay takes each new form as it is worked and holds whatever shape it is left in.',
    S(('core', 'A clay sculpture is present.'),
      ('core', 'It is reshaped during the shot.'),
      ('core', 'The clay holds its new form rather than springing back.'),
      ('minor', 'The clay reads as soft workable clay rather than fired ceramic.')),
    P(cons('the clay'),
      keeps('the clay', 'the new shape'),
      ('core', 'The clay changes only where it is worked, and the change follows the hands or the '
               'tool.',
       'the sculpture reshapes itself in places nothing is touching, or it jumps from one form to '
       'another between frames'),
      ('major', 'The amount of clay stays about the same: it is moved about rather than created or '
                'destroyed.',
       'the sculpture grows much bigger with no clay added, or material simply vanishes as it is '
       'worked'),
      ('major', 'The clay stays one connected mass unless it is plainly cut or pulled apart.',
       'parts of the sculpture separate on their own and then merge back'),
      ('major', 'The clay holds still between touches rather than creeping on its own.',
       'the shape goes on changing after the hands have come away'),
      ('minor', 'Marks left by the hands or the tool stay in the surface.',
       'fingerprints and tool marks smooth themselves away on their own')),
    note="Their two standards -- the clay retains its new shape without returning to the original, "
         "and the transition is continuous -- are both sound and both used, with the second read as "
         "physical continuity rather than as a rendering requirement: a sculpture that jumps between "
         "forms is the artefact this catches. The additions are conservation of material, which is "
         "the easiest thing for a clip to break, and the persistence of tool marks.")

add('plastic-elongation', 230,
    'The dough stretches out and thins as it is pulled, necking where it thins most, and stays '
    'stretched.',
    S(('core', 'A lump of dough is present.'),
      ('core', 'It is stretched out.'),
      ('core', 'The dough gets longer as it is pulled.'),
      ('minor', 'The dough reads as soft dough rather than a rubber or plastic sheet.')),
    P(cons('the dough'),
      keeps('the dough', 'the stretched shape'),
      ('core', 'The dough thins as it lengthens, and thins most where it is stretched hardest.',
       'the dough keeps exactly its original thickness as it is drawn out, or it thickens as it '
       'lengthens'),
      ('major', 'The amount of dough stays about the same: length is gained by thinning, not by '
                'material appearing.',
       'the dough gets longer with no thinning anywhere and no dough added'),
      ('major', 'The dough gives way slowly and clings rather than snapping back like rubber.',
       'the dough springs back to a lump the moment it is let go'),
      ('major', 'If it is pulled far enough it necks down and parts, and the parted ends stay '
                'thinned.',
       'the dough separates cleanly with square blunt ends and no thinning at the break',
       'the dough is pulled until it separates'),
      ('minor', 'The dough sags under its own weight while held up.',
       'a long thin length of dough holds itself out perfectly straight and level'),
      ('minor', 'Flour, texture and any inclusions stay with the dough as it stretches.',
       'the surface texture of the dough slides across it or vanishes as it is drawn out')),
    note="Their second standard, that the dough keeps its elongated shape, is the core requirement "
         "and is used. Their first asks that it 'elongate and thin out uniformly', and uniformly is "
         "wrong: a soft plastic material under tension necks -- it thins fastest where it is already "
         "thinnest -- and that localisation is the signature of the mechanism. Requiring uniform "
         "thinning would fail a correct clip of dough necking down before it parts, so this rubric "
         "asks for the thinning to be greatest where the pull is greatest instead.")

add('ductile-crumple', 229,
    'The can collapses under the foot into creases and folds and stays crushed.',
    S(('core', 'An aluminium can is present.'),
      ('core', 'A foot crushes it.'),
      ('core', 'The can collapses.'),
      ('minor', 'The can is intact and full-sized before the foot comes down.')),
    P(('fatal', 'The foot and the can meet at their surfaces, and the can gives way under it.',
       'the foot passes through the can, or the can collapses before the foot reaches it'),
      ('core', 'The can crumples where the foot bears on it and gets visibly shorter or flatter.',
       'the can keeps its full shape under a foot plainly bearing down on it'),
      keeps('the can', 'the crushing'),
      ('major', 'The can buckles into creases and folds rather than shrinking evenly.',
       'the can scales down smoothly into a smaller can of the same shape'),
      ('major', 'The metal folds rather than fragmenting.',
       'the can breaks into separate shards'),
      unmarked('the foot and shoe', 'the can'),
      marks('the can', 'its printing and its label')),
    note="Their standards -- irreversible change of shape and structure, and stress marks or "
         "wrinkles where it deformed -- are both sound and both used; the second is a good "
         "observable and is unusual for this benchmark in naming the mode rather than just the fact. "
         "Scenario 164, 'A hammer strikes an aluminum can', is the same object and mechanism in "
         "category 5 and carries this mechanism; scenario 167, the plastic bottle stepped on, is the "
         "same loading on a different material.")

add('foil-crumple', 231,
    'The foil folds up into sharp creases under light pressure and stays crumpled.',
    S(('core', 'A piece of tin foil is present.'),
      ('core', 'It is crumpled.'),
      ('core', 'The foil holds its crumpled form rather than springing flat.'),
      ('minor', 'The foil starts flat and smooth.')),
    P(cons('the foil'),
      keeps('the foil', 'the creases'),
      ('core', 'The foil folds into sharp creases rather than curving into smooth bulges.',
       'the foil deforms into rounded smooth shapes with no creases anywhere'),
      ('major', 'It gives way under light pressure rather than resisting like sheet metal.',
       'the foil needs heavy force to crumple at all, or it springs back like a stiff sheet'),
      ('major', 'The crumpled ball takes up less room than the flat sheet, and the material goes '
                'into the folds.',
       'the crumpled foil covers the same area as the flat sheet, or foil disappears as it is '
       'balled up'),
      ('major', 'The foil stays one piece rather than tearing into separate scraps under ordinary '
                'crumpling.',
       'the sheet breaks into pieces as it is crushed and then behaves as one piece'),
      ('minor', 'The crumpled surface catches the light unevenly, with bright facets and dark folds.',
       'the crumpled foil reads as an evenly matt surface with no facets in it')),
    note="Their standards -- crumpling into folds without returning to shape, and a visible change "
         "of texture -- are both sound and both used, the second being unusually well chosen: "
         "crumpled foil looks different because it is now a field of small specular facets, and that "
         "is a real observable. The addition is the mode -- foil creases sharply rather than bulging "
         "smoothly -- and that it yields under light pressure, which is what the caption's 'light "
         "pressure' is about.")

# ---- Brittle Fracture (232-238) ------------------------------------------
add('brittle-shatter-on-impact', 232,
    'The mug hits the concrete and breaks apart at once, with no bending first.',
    S(('core', 'A ceramic mug is present.'),
      ('core', 'It is dropped and hits concrete.'),
      ('core', 'The mug breaks.'),
      ('minor', 'The mug is whole before the impact.')),
    P(('fatal', 'The mug breaks at the impact, when and where it hits the concrete.',
       'the mug breaks in mid-air before landing, or it lands intact and falls apart moments later '
       'with nothing touching it'),
      ('core', 'The mug does not bend, flex or squash before it breaks.',
       'the mug visibly deforms or flattens on impact and then breaks'),
      ('core', 'The break gives separate hard-edged fragments, and they stay separate.',
       'the pieces merge back into a whole mug, or the mug simply vanishes with no fragments'),
      ('major', 'The pieces fly outward from the impact and then fall and come to rest.',
       'the fragments hang in the air, or they gather back toward the impact point'),
      ('major', 'The fragments keep the wall thickness and the glaze of the mug.',
       'the pieces are thin flakes or dust unrelated to the wall of the mug'),
      unmarked('the concrete', 'the mug'),
      ('minor', 'The cracks that separate the pieces are irregular rather than a neat pattern.',
       'the mug parts along a regular geometric grid')),
    note="Their standards -- instant shattering into multiple irregular fragments, and no flexing, "
         "bending or delayed fracture -- are both sound and are used almost as written. This "
         "subcategory has the best-written standards in the benchmark, because they name the "
         "mechanism negatively (no deformation) rather than just the outcome. The additions are "
         "where the pieces go afterwards and that they keep the wall thickness. Scenarios 53, 233 "
         "and 238 are the same mechanism with other objects.")

add('brittle-shatter-on-impact', 233,
    'The glass cup hits the tile and breaks apart at once, with no bending first.',
    S(('core', 'A glass cup is present.'),
      ('core', 'It is dropped onto a tile floor.'),
      ('core', 'The cup shatters.'),
      ('minor', 'The cup is whole before the impact.')),
    P(('fatal', 'The cup breaks at the impact, when and where it hits the floor.',
       'the cup breaks in mid-air before landing, or it lands intact and falls apart later with '
       'nothing touching it'),
      ('core', 'The cup does not bend or squash before it breaks.',
       'the cup visibly deforms on impact and then shatters'),
      ('core', 'The break gives separate glass fragments and they stay separate.',
       'the pieces merge back into a whole cup, or the cup vanishes with no fragments'),
      ('major', 'The breaking spreads from the point of contact rather than starting all over at '
                'once.',
       'the whole cup turns to fragments simultaneously including the rim furthest from the floor'),
      ('major', 'The fragments scatter outward and settle rather than staying put or hovering.',
       'the shards hang in the air after the break'),
      unmarked('the tile floor', 'the cup'),
      ('minor', 'The fragments stay clear and glassy rather than turning opaque or powdery.',
       'the glass becomes an opaque white powder as it breaks')),
    note="Their standards -- shattering without prior bending or deformation, and fragmentation "
         "spreading quickly from the point of impact -- are both sound and both used. This scenario "
         "is a duplicate of 53, 'A glass cup falls from a table', in the Elastic and Inelastic "
         "Collisions subcategory of category 2 and carries the same mechanism.")

add('brittle-shatter-on-strike', 234,
    'The hammer blow breaks the plate into jagged pieces at once, with no bending first.',
    S(('core', 'A ceramic plate is present.'),
      ('core', 'A hammer strikes it.'),
      ('core', 'The plate breaks.'),
      ('minor', 'The plate is whole before the blow.')),
    P(('fatal', 'The plate breaks where and when the hammer strikes it.',
       'the plate breaks before the hammer arrives, or the hammer passes through it without breaking '
       'it'),
      ('core', 'The plate does not bend or dish before it breaks.',
       'the plate visibly flexes under the hammer and then breaks'),
      ('core', 'The break gives separate hard-edged pieces that stay separate.',
       'the pieces merge back into a whole plate, or the plate vanishes with no fragments'),
      ('major', 'The cracks run out from the point of impact.',
       'the cracks start at the rim and run inward, or they appear in a place the hammer never '
       'touched'),
      ('major', 'The pieces are large and jagged rather than uniform, and they keep the plate '
                'thickness.',
       'the plate breaks into a fine even powder, or into identical regular tiles'),
      unmarked('the hammer', 'the plate'),
      ('minor', 'The pieces are thrown outward and then settle.',
       'the fragments hang where they were made')),
    note="Their sole standard, instant fracture with no noticeable deformation, is the core of the "
         "mechanism and is used. The additions are the crack geometry -- radiating from the point of "
         "impact, which is what makes a struck plate different from a dropped one -- and the "
         "fragment character. Scenarios 232, 233 and 238 are the dropped versions.")

add('brittle-snap', 235,
    'The icicle gives barely at all and then snaps clean through rather than holding a bend.',
    S(('core', 'An icicle is present.'),
      ('core', 'It is bent, as the caption says.'),
      ('minor', 'The icicle reads as clear or milky ice rather than glass or plastic.'),
      ('minor', 'The icicle starts whole and attached or held.')),
    P(cons('the icicle'),
      ('core', 'The icicle gives very little before it fails: it does not bow into a curve the way a '
               'flexible rod would.',
       'the icicle bends round into a visible curve and stays whole'),
      ('core', 'What the clip commits to holds together: an icicle that is bent past its limit snaps '
               'through, and it does not keep a permanent bend.',
       'the icicle takes a lasting curved shape like bent wire, or it bends far and then springs '
       'straight again'),
      ('major', 'The break is a clean separation across the icicle with a definite fracture face.',
       'the icicle tears apart in a stringy, drawn-out way, or it crumbles into slush at the break'),
      ('major', 'The break is where the bending was greatest.',
       'the icicle breaks at a place it was not being bent'),
      ('major', 'The pieces separate and fall.',
       'the broken pieces stay in place as though still joined, or they drift rather than falling'),
      ('minor', 'The ice stays ice through the shot rather than melting away in a few seconds.',
       'the icicle melts to nothing over the course of the shot')),
    note="Caption and physics pull apart here, as they did at PhyGenBench id 39. The caption says "
         "the icicle BENDS; the physics_prompt and their key standard say it snaps with 'no visible "
         "bending' at all. Ice is brittle in fast loading but a thin icicle does give slightly "
         "before it goes, so requiring exactly zero bending would fail a correct clip while the "
         "caption asserts bending outright. SA carries the caption's bending; the PC items ask for "
         "the give to be small and for the outcome to be a clean snap rather than a held curve, so "
         "either reading can pass without the clip having it both ways.")

add('brittle-snap', 236,
    'The twig gives almost nothing and then snaps through under the foot.',
    S(('core', 'A dry twig is present.'),
      ('core', 'It is stepped on.'),
      ('core', 'The twig breaks.'),
      ('minor', 'The twig reads as dry and dead rather than green and springy.')),
    P(('fatal', 'The twig breaks where and when the foot bears on it.',
       'the twig breaks before the foot reaches it, or the foot passes through it'),
      ('core', 'The twig gives very little before it goes: it does not bow into a curve first.',
       'the twig bends round into a deep curve under the foot and stays whole'),
      ('core', 'The break is a sharp separation into pieces rather than a gradual tearing or '
               'stretching.',
       'the twig draws out and thins before parting, or it tears apart in fibrous strands over '
       'several moments'),
      ('major', 'The break is under or beside the foot, where the load is.',
       'the twig breaks at a point well away from the foot'),
      ('major', 'The pieces separate and stay separate.',
       'the broken ends rejoin, or the twig is whole again later in the shot'),
      unmarked('the foot and shoe', 'the twig'),
      ('minor', 'The break leaves rough splintered ends rather than a smooth cut face.',
       'the twig parts with clean square ends as though sawn')),
    note="Their standards -- a clean sharp snap with no visible bending, and immediate separation "
         "without gradual tearing or elongation -- are both sound and both used. The additions are "
         "the location of the break and the splintered ends, which is the one respect in which dry "
         "wood differs from the ceramics and glass in this block: it is brittle but fibrous, so the "
         "fracture face is rough rather than sharp-edged. Scenario 235 is the same mechanism in ice.")

add('crack-propagation', 237,
    'Cracks run out through the glass sheet under the pressure, growing and never closing, with no '
    'bending.',
    S(('core', 'A sheet of glass is present.'),
      ('core', 'Pressure is applied to it.'),
      ('core', 'The glass cracks.'),
      ('minor', 'The sheet is clear and unbroken before the pressure is applied.')),
    P(cons('the sheet'),
      ('core', 'The cracks only ever grow; none of them closes up or disappears.',
       'a crack heals over, or the sheet is unbroken again later in the shot'),
      ('core', 'The glass does not bend, dish or stretch before it cracks.',
       'the sheet visibly bows or stretches under the pressure before cracking'),
      ('major', 'The cracks start where the pressure is applied and run out from there.',
       'the cracks start at the far edge of the sheet and run toward the pressure point'),
      ('major', 'The cracks run out quickly and in irregular branching lines.',
       'the cracks creep out slowly over several seconds, or they form a neat regular pattern'),
      ('major', 'The sheet stays in one plane: cracked regions do not lift, curl or separate unless '
                'a piece plainly comes free.',
       'the cracked glass ripples or curls like paper'),
      ('minor', 'The cracks show as bright lines catching the light rather than as drawn-on dark '
                'marks.',
       'the cracks read as flat dark lines with no glint at all in a lit scene')),
    note="All three of their standards -- clean sharp fracture, rapid jagged crack propagation, and "
         "no noticeable deformation or stretching -- are sound and are used. The additions are the "
         "irreversibility, which is the failure mode a looped or reversed clip produces, and the "
         "starting point of the cracks. This is one of the few records in the benchmark where the "
         "supplied standards would have made a workable rubric on their own.")

add('brittle-shatter-on-impact', 238,
    'The vase hits the floor and breaks into large angular pieces at once, with no bending first.',
    S(('core', 'A porcelain vase is present.'),
      ('core', 'It drops onto the floor.'),
      ('core', 'The vase breaks.'),
      ('minor', 'The vase is whole before the impact.')),
    P(('fatal', 'The vase breaks at the impact, when and where it hits the floor.',
       'the vase breaks in mid-air before landing, or it lands intact and comes apart later with '
       'nothing touching it'),
      ('core', 'The vase does not bend, squash or dent before it breaks.',
       'the vase visibly deforms on impact and then breaks'),
      ('core', 'The break gives separate pieces with sharp angular edges, and they stay separate.',
       'the pieces merge back into a whole vase, or the vase crumbles into rounded pebbles'),
      ('major', 'The pieces are large and irregular rather than uniform, and they keep the wall '
                'thickness and glaze of the vase.',
       'the vase breaks into fine even dust, or into identical regular pieces'),
      ('major', 'The pieces scatter outward from the impact and then settle.',
       'the fragments hang in the air, or they draw back toward the impact point'),
      unmarked('the floor', 'the vase'),
      ('minor', 'The break faces show the unglazed body of the porcelain, different from the glazed '
                'outside.',
       'every face of every fragment is glazed, including the fresh breaks')),
    note="Their standards -- immediate rupture with no noticeable deformation, and fracture into "
         "irregular pieces with sharp angular edges -- are both sound and both used. The addition "
         "worth naming is the unglazed break face: porcelain is glazed on the outside only, so fresh "
         "fractures expose a different-looking material, and a clip whose fragments are glazed all "
         "over has generated them rather than broken the vase. Scenarios 53, 232 and 233 are the "
         "same mechanism.")

# ---- Thermal Expansion and Contraction (239-245) -------------------------
add('gas-cooling-contraction', 239,
    'The air in the sealed balloon contracts as it chills, so the balloon shrinks while staying '
    'closed.',
    S(('core', 'A balloon is present.'),
      ('core', 'It is in a freezer or a plainly cold place.'),
      ('core', 'The balloon gets smaller over the shot.'),
      ('minor', 'The balloon starts inflated and taut.')),
    P(('fatal', 'The balloon stays sealed: it shrinks because the air inside contracts, not because '
                'air escapes.',
       'the balloon shrinks with air visibly jetting out of a hole or an open neck'),
      ('core', 'The balloon only gets smaller while it is cold, and does not swell back on its own.',
       'the balloon grows again while it is plainly still in the cold'),
      ('core', 'The shrinking is gradual, spread over the shot, rather than happening between one '
               'frame and the next.',
       'the balloon jumps from full size to shrunken in a single step'),
      ('major', 'The balloon stays roughly its own shape as it shrinks rather than collapsing into '
                'creases.',
       'the balloon crumples up into folds like a punctured one'),
      ('major', 'The balloon stays whole rather than bursting.',
       'the balloon bursts as it is chilled'),
      ('minor', 'Frost or condensation appears on the balloon or the freezer surfaces.',
       'the balloon and everything around it stay perfectly dry and clear in a working freezer'),
      marks('the balloon', 'its printing and its colour')),
    note="Their standards -- visible shrinking over time, continuous rather than jumping -- are "
         "sound and are used, the second read as physical continuity rather than as a rendering "
         "requirement. The addition that matters is the seal: this scenario looks identical to a "
         "slow leak, and the difference is that the gas contracts inside a closed balloon, so the "
         "envelope stays roughly its own shape rather than crumpling. Scenario 116, 'A balloon has a "
         "small hole', is the leaking case and requires the opposite.")

add('vacuum-collapse', 240,
    'The sealed bottle is crushed inward by outside air as the hot contents cool.',
    S(('core', 'A plastic bottle is present.'),
      ('core', 'It is filled with hot water and then cools, as the caption says.'),
      ('core', 'The bottle deforms over the shot.'),
      ('minor', 'The bottle is capped or sealed rather than open.')),
    P(('fatal', 'The bottle deforms inward, not outward.',
       'the bottle swells outward as it cools'),
      ('core', 'The bottle buckles inward into dents and creases rather than shrinking evenly like a '
               'scale model.',
       'the whole bottle scales down smoothly into a smaller bottle of the same shape'),
      ('core', 'The collapse happens as it cools and not before: the bottle is still full-shaped '
               'while it is hot.',
       'the bottle is already crushed while the water in it is plainly still steaming'),
      ('major', 'The bottle stays sealed while it collapses.',
       'the bottle caves in with the cap plainly off, or with air rushing in through an opening'),
      ('major', 'The collapse stops rather than continuing indefinitely, and the bottle stays '
                'collapsed until it is opened or warmed.',
       'the bottle springs back to full shape on its own while still sealed and cool'),
      ('major', 'The water level and the water stay inside the bottle as it deforms.',
       'water disappears from the bottle as it collapses, or it is forced out through the sealed cap'),
      ('minor', 'Condensation shows on the inside of the bottle as it cools.',
       'the inside of the bottle stays perfectly clear and dry throughout the cooling')),
    note="Their sole standard asks for 'a clear visual contraction process of the plastic', which "
         "misattributes the mechanism. The plastic's own thermal contraction over this range is far "
         "too small to see; the bottle caves in because the cooling air inside drops below "
         "atmospheric pressure and the outside air crushes it, which their physics_prompt gets "
         "right. The observable difference matters: pressure collapse gives sudden inward BUCKLING "
         "with creases, not an even shrink, so a clip that scales the whole bottle down satisfies "
         "their standard and has the wrong physics.")

add('cold-bottle-response', 241,
    'A sealed bottle left out in the freezing cold dishes inward as its air cools, unless the water '
    'in it freezes and pushes back out.',
    S(('core', 'A plastic water bottle is present.'),
      ('core', 'It sits outside in freezing conditions.'),
      ('core', 'The bottle changes over the shot rather than staying as it began.'),
      ('minor', 'The setting reads as freezing -- snow, frost or ice around it.')),
    P(cons('the bottle'),
      ('core', 'What the clip commits to holds together: a bottle whose air is cooling dishes '
               'inward, and a bottle whose water is freezing bulges outward, but not both.',
       'the bottle caves inward while ice plainly forms and grows inside it, or it swells outward '
       'with no ice anywhere in it'),
      ('core', 'Any change is gradual and one-way while it stays cold.',
       'the bottle deforms and then recovers repeatedly while the cold is plainly unbroken'),
      ('major', 'The bottle deforms by denting and creasing rather than shrinking evenly all over '
                'like a scale model.',
       'the whole bottle scales down smoothly into a smaller bottle of the same shape'),
      ('major', 'If ice forms it grows from the walls and the surface inward and takes up more room '
                'than the water it replaces.',
       'ice appears in the middle of the water with liquid all round it, or the contents shrink as '
       'they freeze',
       'the water in the bottle freezes during the shot'),
      ('major', 'The bottle stays sealed and its contents stay in it.',
       'water leaves the sealed bottle, or air is seen rushing into it'),
      ('minor', 'Frost or condensation forms on the outside of the bottle.',
       'the bottle stays perfectly clear and dry in plainly freezing conditions')),
    note="Their sole standard, that the bottle visibly shrink and contract over time, is not usable "
         "as written. The plastic's own thermal contraction is invisible at this scale, and the two "
         "things that ARE visible pull in opposite directions: cooling air makes a sealed bottle "
         "dish inward, while water freezing expands and makes it bulge. Requiring shrinkage would "
         "fail a correct clip of a bottle bulging as its contents freeze. The core item asks for "
         "internal consistency between which of the two the clip shows. Scenario 240 is the "
         "deliberate inward case with a hot start.")

add('heat-warping', 242,
    'The bottle softens in the hot water and distorts out of shape rather than growing evenly.',
    S(('core', 'A plastic soda bottle is present.'),
      ('core', 'It is placed in hot water.'),
      ('core', 'The bottle changes shape over the shot.'),
      ('minor', 'The water reads as hot -- steaming, or plainly just boiled.')),
    P(cons('the bottle'),
      ('core', 'The bottle distorts unevenly -- warping, sagging or puckering -- rather than growing '
               'or shrinking as a neat scaled copy of itself.',
       'the whole bottle scales up or down smoothly with its shape preserved'),
      ('core', 'The change starts once it is in the hot water and not before.',
       'the bottle is already distorted before it goes into the water'),
      ('major', 'The distortion is worst where the bottle is hottest -- the part in the water, and '
                'the thin walls before the thick base and neck.',
       'the thick base deforms while the thin walls stay perfectly true, or the part out of the '
       'water distorts more than the part in it'),
      ('major', 'The bottle stays soft-deformed rather than springing back once out of the water.',
       'the warped bottle returns to its original shape on its own while still hot'),
      ('major', 'The bottle stays one piece and holds its contents.',
       'the bottle splits open under nothing more than hot water'),
      ('minor', 'Condensation or steam shows around the bottle and the water.',
       'the bottle sits in plainly boiling water with no steam or condensation anywhere')),
    note="Their first standard, that 'the plastic bottle visibly expands', is doubtful and their "
         "second is a rendering phrase. A drawn PET bottle put in hot water does not grow evenly: "
         "the oriented plastic relaxes toward its unblown state, so it warps, sags and often "
         "shrinks, which is what their own physics_prompt describes when it says the plastic "
         "'expands unevenly ... visibly warping its shape'. Requiring clean expansion would fail the "
         "correct clip. This rubric asks for uneven distortion, worst where the plastic is hottest "
         "and thinnest, and for it to persist.")

add('heat-shrink', 243,
    'The heated wrap tightens and pulls down onto what is under it rather than growing.',
    S(('core', 'Plastic wrap is present.'),
      ('core', 'It is heated.'),
      ('core', 'The wrap changes over the shot rather than staying as it began.'),
      ('minor', 'There is a surface or an object under the wrap for it to pull onto.')),
    P(cons('the wrap'),
      ('core', 'The wrap draws tighter as it heats -- wrinkles pull out and it closes down onto what '
               'is beneath it.',
       'the wrap grows slacker and baggier as it is heated, or it billows away from the surface '
       'beneath'),
      ('core', 'The tightening only happens while heat is on it and does not undo itself when the '
               'heat comes off.',
       'the wrap loosens back to its original slackness once the heat is removed'),
      ('major', 'The tightening is worst where the heat is strongest.',
       'the wrap tightens uniformly all over while the heat is plainly applied to one area'),
      ('major', 'The wrap takes on the shape of what is under it, showing its contours.',
       'the wrap stays a flat featureless sheet while pulled tight over a shaped object'),
      ('major', 'The wrap stays one piece unless it is plainly overheated, and if it does give way '
                'it holes and shrinks back from the hole rather than tearing straight.',
       'the wrap parts along a clean straight line as though cut'),
      ('minor', 'The wrap stays see-through and glossy rather than clouding over.',
       'the wrap turns opaque white as it is warmed')),
    note="Their sole standard, that 'the plastic wrap visibly expands when heated', contradicts "
         "their own physics_prompt in the same record, which has the wrap 'conforming tightly to the "
         "surface beneath' -- and conforming tightly is shrinking, not expanding. Shrinking is also "
         "the right physics: stretched film relaxes toward its unstretched state when warmed, which "
         "is the whole principle of shrink wrap. Following their standard would score an expanding, "
         "billowing wrap as correct and fail the correct clip, so the core item here requires the "
         "tightening.")

add('thermal-expansion-rise', 244,
    'The liquid climbs the thermometer tube, fast at first and slowing as it catches up with the '
    'water.',
    S(('core', 'A liquid thermometer is present.'),
      ('core', 'It is placed in hot water.'),
      ('core', 'The liquid level in the tube rises.'),
      ('minor', 'The liquid column is visible against the scale rather than hidden.')),
    P(('fatal', 'The level rises after the thermometer goes into the hot water, not before.',
       'the level is already high before the thermometer reaches the water, or it rises with the '
       'thermometer plainly in cold water'),
      ('core', 'The rise slows as it goes: fastest just after immersion and easing off as the '
               'reading approaches the water temperature.',
       'the level climbs at one unchanging rate right up to where it stops, or it speeds up as it '
       'rises'),
      ('core', 'The level settles and holds rather than climbing indefinitely.',
       'the liquid keeps rising to the top of the tube and out of it while the water is plainly not '
       'getting hotter'),
      ('major', 'The column stays a single connected thread of liquid from the bulb upward.',
       'the column breaks into separate segments with gaps, or liquid appears part-way up the tube '
       'with a gap below it'),
      ('major', 'The level only rises while the water is hotter than the thermometer, and falls if '
                'it is taken out into cooler air.',
       'the level goes on rising after the thermometer is taken out into cool air',
       'the thermometer is removed from the water during the shot'),
      ('major', 'The tube, the bulb and the scale keep their own size while the liquid moves.',
       'the tube or the scale stretches along with the rising column'),
      ('minor', 'The liquid keeps its colour and its meniscus as it rises.',
       'the column changes colour or loses its top edge as it climbs')),
    note="Their sole standard asks that the level rise 'at a consistent rate', and that is wrong in "
         "a way that rewards the wrong clip. A thermometer approaches the surrounding temperature "
         "asymptotically, so the column moves fastest immediately after immersion and slower as it "
         "closes the gap; a constant-rate rise is the linear animation this scenario is best placed "
         "to catch, and it also has nowhere to stop. This rubric requires the deceleration and the "
         "settling.")

add('steam-pressure-lift', 245,
    'Steam building under the kettle lid lifts and rattles it, and only once the water is boiling.',
    S(('core', 'A kettle with a lid is present.'),
      ('core', 'It heats up during the shot.'),
      ('core', 'The lid moves -- jiggling, lifting or rattling.'),
      ('minor', 'Steam or vapour is visible at the lid or the spout.')),
    P(cons('the lid'),
      ('core', 'The lid starts moving only after the kettle has heated and steam is being produced, '
               'not from the start.',
       'the lid rattles from the first frame while the kettle is plainly still cold'),
      ('core', 'The lid movement is small: it lifts and drops back rather than being thrown off.',
       'the lid is blown clear of the kettle and lands away from it'),
      ('major', 'The lid comes back down onto its seat each time rather than resting lifted.',
       'the lid hovers above the kettle rim while steam escapes'),
      ('major', 'Steam escapes at the lid while it is lifted and less so while it is seated.',
       'steam pours out around a lid that is plainly sitting tight, or the lid lifts with no steam '
       'anywhere'),
      ('major', 'The lid stays on top of the kettle, over the opening.',
       'the lid drifts off to the side and keeps jiggling clear of the kettle'),
      ('minor', 'The kettle body stays still while the lid moves.',
       'the whole kettle jumps about along with its lid'),
      ('minor', 'Condensation runs on the underside of the lid or down the kettle.',
       'the lid and the kettle stay perfectly dry while steam is plainly escaping')),
    note="This record is filed under Thermal Expansion and Contraction but the mechanism its own "
         "physics_prompt describes is steam pressure lifting the lid, which is not thermal "
         "expansion of a solid at all; the items follow the mechanism actually named. Their sole "
         "standard, a slight jiggle with noticeable but minor movement, is used. Their physics_prompt "
         "also rests on a 'faint rattling sound', which no clip can be judged on, so the audible "
         "part is replaced by its visible counterpart: the lid lifts and reseats, and steam escapes "
         "while it is lifted.")
