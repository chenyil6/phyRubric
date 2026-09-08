# ---- Force / Gravity (0-4) ------------------------------------------------
g([0, 1, 2, 3, 4], 'ok',
  "In the microgravity of an orbiting station there is no downward pull. Released liquid "
  "does not fall; it drifts on whatever velocity it was given, and surface tension pulls it "
  "into rounded blobs that merge on contact and cling to any surface they touch.",
  ["No direction in the scene acts as 'down': the released liquid does not accelerate toward "
   "the floor, and nothing pools at the bottom of the frame.",
   "A freed mass of liquid rounds up into a blob or sphere instead of falling as a column or "
   "breaking into a splashing stream.",
   "A drifting blob travels in a straight line at roughly constant speed until it meets "
   "something; its path does not arc downward.",
   "Two blobs that touch merge into one larger blob and stay merged.",
   "A blob that touches a surface sticks and spreads over it rather than running off it or "
   "collecting beneath it.",
   "Liquid still inside the cup or bottle shows no flat horizontal surface; it wets and clings "
   "to the container wall instead of lying level.",
   "The astronaut's hair, clothing and any loose object in shot also hang free rather than "
   "falling."])
o(3, add=["The honey, far more viscous, is slow to round up: it trails strands and lumpy shapes "
          "that only gradually pull into blobs."])
o(4, add=["Gas bubbles in the soda do not collect on one side of the blob; they stay dispersed "
          "through it, since there is no buoyancy to sort them."])

# ---- Force / Buoyancy (5-9) ----------------------------------------------
g([5, 6, 9], 'ok',
  "Iron, stone and solid glass are several times denser than water, so the buoyant force "
  "cannot support them: each one goes under at once and descends to the bottom.",
  ["The object goes under immediately rather than resting on the surface or hesitating there.",
   "It accelerates briefly, then descends at a roughly steady rate, slower than it would fall "
   "through air.",
   "It stays on the bottom once it arrives and does not rise again on its own.",
   "The surface dips and ripples where the object enters, and the ripples spread outward and "
   "die away rather than persisting or converging.",
   "The water level rises slightly when the object is added and does not fall while it stays in.",
   "The submerged object still reads as being under water: it is tinted, blurred or displaced "
   "by refraction rather than looking as crisp as it did in air."])
g([8], 'ok',
  "Wood is less dense than water, so it floats: it settles at a waterline with part of its "
  "body above the surface.",
  ["The block stays at the surface and never sinks below it.",
   "It settles to a definite waterline with a visible part above water, rather than sitting "
   "entirely on top of the surface or entirely under it.",
   "It bobs a few times with each swing smaller than the last, then comes to rest.",
   "The surface dips and ripples where the block lands, and the ripples spread outward and "
   "die away.",
   "The water level rises slightly when the block is added and does not fall while it stays in.",
   "The block does not drift under on its own, nor lift clear of the water on its own."])
g([7], 'rewrite',
  "A sealed, air-filled tennis ball is far less dense than water, so it floats, riding with "
  "roughly a third of its body below the surface.",
  ["The ball stays at the surface and never sinks below it.",
   "It settles to a definite waterline with most of its body above water.",
   "It bobs a few times with each swing smaller than the last, then comes to rest.",
   "The surface dips and ripples where the ball lands, and the ripples spread outward and die "
   "away.",
   "The water level rises slightly when the ball is added and does not fall while it stays in.",
   "The ball does not drift under on its own, nor lift clear of the water on its own.",
   "The felt surface wets and darkens where it sits in the water."],
  issue="The law names a wood block; the caption places a tennis ball. The conclusion (floats) "
        "is right, the object is not -- copied from id 8.",
  flags=['object-mismatch'])

# ---- Force / Stress (10-14) ---------------------------------------------
g([10, 11, 14], 'ok',
  "Squeezing a soaked porous material drives the water out of its pores: the material "
  "compresses under the hand while water runs from it, and it springs back only partly when "
  "released, still damp.",
  ["The material compresses only where and while the hand presses it, and it stops compressing "
   "when the hand stops.",
   "Water leaves the material while it is being compressed, running out at the squeezed region "
   "and falling away.",
   "The water that comes out came from inside: the material grows visibly less swollen and "
   "darker-wet at the point of squeeze, and the amount of water is bounded by what it held.",
   "The material springs back partly when the hand releases, not to its original swollen size, "
   "and it stays damp rather than dry.",
   "Water runs downward off the material and pools or falls; it does not climb it or hang in "
   "the air.",
   "No water is drawn back into the material once it has left."])
g([13], 'ok',
  "Squeezing an open tube raises the pressure inside, so paste is forced out of the nozzle "
  "while the tube's wall dents and stays creased where it was pressed.",
  ["Paste comes out only while the tube is squeezed, from the open nozzle, and it stops when "
   "the squeeze stops.",
   "What comes out came from inside: the tube collapses and empties as paste leaves it, and "
   "the amount extruded is bounded by what the tube held.",
   "The tube dents where the fingers press and keeps the crease after they move on; it does "
   "not spring back perfectly plump.",
   "The paste holds the ribbon shape and roughly the cross-section of the nozzle it came from, "
   "sagging slowly rather than running like water.",
   "The extruded paste stays where it lands and is not drawn back into the tube."])
g([12], 'rewrite',
  "Pressing an inflated, sealed balloon mostly changes its shape rather than its size: it "
  "flattens where the hand bears on it and bulges elsewhere, the trapped air being only "
  "slightly compressible, and it springs back fully when released.",
  ["The balloon flattens only where the hand presses, at the moment it presses.",
   "It bulges outward elsewhere while flattened at the contact, rather than shrinking all over.",
   "Its overall size stays roughly the same under hand pressure; it does not visibly deflate.",
   "It springs back to its original shape when the hand lifts, not staying dented.",
   "The rubber's surface markings stretch and crowd with the local deformation rather than "
   "sliding across a still surface.",
   "It bursts only if the rubber is stretched past its limit, and if it bursts the tearing "
   "starts at the loaded region and is irreversible."],
  issue="'Shrink' is wrong for a sealed air balloon under hand pressure: air is nearly "
        "incompressible at these loads, so the balloon changes shape at roughly constant volume. "
        "The law also omits the elastic recovery, which is the sharpest visible check.")

# ---- Force / Atmospheric Pressure (15-19) -------------------------------
g([15, 16, 18], 'ok',
  "Pumping the air out of a sealed thin-walled vessel removes the internal pressure that was "
  "balancing the atmosphere outside, so the wall is pushed inward: it buckles and crumples, "
  "usually suddenly, and stays creased.",
  ["The vessel deforms only while air is being drawn out, and the deformation tracks the "
   "extraction rather than starting before it.",
   "The wall moves inward, never outward: no part of it bulges out while air is being removed.",
   "The collapse is a buckling, not a smooth uniform shrink: flat panels cave, sharp creases "
   "and facets appear, and the shape becomes irregular.",
   "It often gives way suddenly rather than at a constant rate, and it stays crumpled once it "
   "has collapsed.",
   "The vessel does not spring back to its original shape while the air is still out.",
   "The creases stay where they formed as the collapse continues; they do not migrate across "
   "the wall."])
o(15, add=["The thin plastic bottle crumples progressively and irregularly rather than "
           "collapsing all at once."])
g([17], 'rewrite',
  "A sealed hollow plastic ball has a stiff curved shell, so removing the air does not shrink "
  "it uniformly: one region dimples and caves inward, and the dent stays.",
  ["The ball deforms only while air is being drawn out.",
   "The wall moves inward, never outward.",
   "The deformation is a local dimple or cave-in on one side, not a uniform reduction in "
   "diameter with the ball staying round.",
   "The dent appears suddenly once the shell buckles, and it stays once formed.",
   "The ball does not spring back to round while the air is still out.",
   "The undented parts keep their original curvature and size."],
  issue="A curved stiff shell does not shrink uniformly under external pressure; it buckles "
        "locally. 'Shrinking' invites a rubric item that would accept a ball smoothly reducing "
        "in diameter, which is not what happens.")
g([19], 'rewrite',
  "Drawing the air out of a balloon lets the stretched rubber contract: the balloon shrinks "
  "and wrinkles as it empties. The rubber's own elasticity does this, not the outside "
  "atmosphere.",
  ["The balloon shrinks only while air is being drawn out, and it stops when the extraction "
   "stops.",
   "It gets smaller all over as the stretched rubber recovers, rather than buckling with sharp "
   "creases like a rigid shell.",
   "Wrinkles and slack folds appear in the rubber as it deflates, and the surface markings "
   "crowd together with it.",
   "It does not re-inflate on its own while the air is still out.",
   "The neck stays sealed to whatever is drawing the air; the balloon does not deflate through "
   "a hole that is not there."],
  issue="Mechanism mislabelled. An inflated balloon's rubber is under tension, so its internal "
        "pressure is already above atmospheric; it collapses by elastic recoil when emptied, not "
        "because the outside atmosphere crushes it. The visible result (shrinking, wrinkling) is "
        "right, and it is visibly different from the rigid-vessel cases (15-18) -- no buckling.",
  flags=['mechanism-mislabelled'])

# ---- Force / Solid Pressure (20-23) -------------------------------------
g([20, 23], 'ok',
  "A needle or pin concentrates a modest force onto a tiny area, so the stress at the tip "
  "exceeds what the stretched rubber can take: the balloon fails at the point of contact and "
  "the tear runs away from it at once.",
  ["The balloon fails at the tip's point of contact, not anywhere else on its surface.",
   "It fails only once the tip has plainly reached and dented the rubber, not before contact.",
   "The rubber dents and stretches inward around the tip in the moments before it gives.",
   "Once it starts, the failure runs quickly and completely across the taut rubber rather than "
   "leaving a neat small hole in a still-inflated balloon.",
   "The failure is irreversible: the rubber does not close up and the balloon does not "
   "re-inflate.",
   "The freed rubber snaps away from the burst and then falls slack; it does not hold its "
   "inflated shape."])
o(23, add=["The water inside is released as a coherent mass that then falls and spreads, and "
           "the emptied rubber is left limp and wet.",
           "The water goes downward and stays where it lands; it is not drawn back into the "
           "rubber."])
o(20, add=["The escaping air is invisible: nothing should be seen leaving the balloon except "
           "the moving rubber itself."])
g([21, 22], 'ok',
  "A tip pressed into a taut sheet concentrates the load at the contact, so the sheet fails "
  "there once the local stress exceeds its strength: it tents inward first, then punctures and "
  "tears from that point.",
  ["The sheet fails at the point of contact, not elsewhere.",
   "It tents and stretches inward around the tip before it gives, and the tenting deepens as "
   "the tip advances.",
   "The failure happens only after contact, not before the tip arrives.",
   "The tear starts at the puncture and runs outward from it; it does not appear as a hole "
   "away from the tip.",
   "The failure is irreversible: the sheet does not close up.",
   "The freed edges relax and slacken as the tension is released."])
o(22, add=["A fork presses several tines at once, so several punctures appear together, one at "
           "each tine that reaches the wrap."])
g([24], 'rewrite',
  "A blunt pencil pressed slowly onto an inflated balloon may or may not burst it: if the "
  "rubber is highly stretched it fails at the tip, but a rounded tip can also indent the "
  "rubber deeply without piercing. Judge whether what is shown is internally consistent, not "
  "whether it bursts.",
  ["The rubber dents and stretches inward around the pencil tip while it presses, and the dent "
   "deepens as the pencil advances.",
   "If the balloon bursts, it bursts at the tip's point of contact and only after contact.",
   "If it does not burst, the rubber stays intact and springs back when the pencil withdraws.",
   "A burst is irreversible: the rubber does not close up and the balloon does not re-inflate.",
   "The pencil is checked by the rubber's resistance rather than passing through as if nothing "
   "were there.",
   "Whichever happens, it happens once: the balloon does not burst, recover and burst again."],
  issue="The outcome is not determined by the physics as captioned. A pencil is blunt compared "
        "with a needle, and slow pressing on a balloon is the classic case that can go either "
        "way. Mandating 'will explode' would penalise a physically correct clip.",
  flags=['outcome-uncertain'])

# ---- Force / Elasticity (25-29) -----------------------------------------
g([25, 26, 27, 28, 29], 'ok',
  "A ball thrown at the ground deforms on contact and pushes back off it, so it rebounds -- "
  "but always more slowly than it arrived, since some energy is lost in the deformation. "
  "Successive bounces are lower and closer together.",
  ["The ball reverses direction at the ground, at the moment of contact, and not a gap above it.",
   "It leaves the ground more slowly than it arrived, so the rebound rises less high than the "
   "throw came from.",
   "Each successive bounce is lower than the one before and the intervals between bounces get "
   "shorter; the sequence never grows.",
   "Between bounces the ball follows a single arc, speeding up as it falls and slowing as it "
   "rises, with no kink or hover in mid-air.",
   "The ball flattens against the ground at the contact and recovers its round shape as it "
   "leaves; it does not stay dented.",
   "The rebound direction follows the approach: a ball thrown straight down comes back up, one "
   "thrown at an angle comes off on the mirrored line.",
   "The ball's motion only ever loses energy: it does not speed up in flight or bounce higher "
   "than the previous bounce."])
o(29, add=["Being very light for its size, the beach ball is slowed noticeably by the air: it "
           "decelerates between bounces and its rebounds die away quickly."])
o(26, add=["The basketball's contact flattening is visible and brief, and it rebounds high -- "
           "a substantial fraction of the drop."])

# ---- Force / Friction (30, 32) ------------------------------------------
g([30, 32], 'ok',
  "Dragging a soft solid stick across a rough surface abrades material off it and leaves it "
  "behind: a mark appears along the path travelled, and the stick itself is worn down.",
  ["The mark appears only where the tip has passed, at the moment it passes, and it follows "
   "the path exactly.",
   "The leading end of the mark advances with the tip and never runs ahead of it.",
   "No mark appears where the tip was lifted clear of the surface.",
   "The mark is permanent unless something wipes it: it does not fade or retract on its own.",
   "The stick is consumed as it writes -- it shortens or blunts -- and loose dust or crumbs "
   "are shed at the contact.",
   "The mark's colour is the stick's own, laid over the surface's colour rather than replacing "
   "the surface."])
o(30, add=["Chalk dust falls from the contact and settles below, and the mark reads as a dry "
           "powdery deposit that could be smudged."])
o(32, add=["The wax mark sits on the raised texture of the paper and skips the hollows, so it "
           "reads broken rather than solid."])
g([31, 33, 34], 'rewrite',
  "A pen, marker or highlighter leaves a mark by depositing ink onto the surface, not by "
  "friction: the ink wets the surface where the tip has passed. Friction only turns a "
  "ballpoint's ball; nothing is abraded off the tip.",
  ["The mark appears only where the tip has passed, at the moment it passes, and it follows "
   "the path exactly.",
   "The leading end of the mark advances with the tip and never runs ahead of it.",
   "No mark appears where the tip was lifted clear of the surface.",
   "The mark is wet ink laid on the surface: its colour is the ink's own and it may spread "
   "slightly or soak in, rather than sitting as powder on top.",
   "The mark is permanent unless something wipes it: it does not fade or retract on its own.",
   "The pen or marker is not visibly consumed by writing -- no dust or crumbs are shed at the "
   "contact."],
  issue="Mechanism mislabelled: the mark is ink deposition (capillary wetting, or ink "
        "transferred by a rolling ball), not friction-driven abrasion. The visible outcome -- a "
        "mark along the path -- is right, but the correct rubric must not require shedding or "
        "wear at the tip, which is what a friction claim implies.",
  flags=['mechanism-mislabelled'])
o(33, add=["The highlighter's ink is translucent: what is underneath still reads through the "
           "mark rather than being covered over."])

# ---- Force / Surface Tension (35, 37) -----------------------------------
g([35, 37], 'ok',
  "On a water-repellent surface the drop's own surface tension wins over its attraction to "
  "the surface, so it beads up into a near-sphere, touches over a small area, and rolls "
  "freely with almost nothing left behind.",
  ["The drop holds a rounded, near-spherical shape while it sits and while it moves, rather "
   "than flattening into a film.",
   "It meets the surface over a small contact patch, with a steep edge where liquid meets "
   "solid.",
   "It rolls or slides as one body and keeps its shape while moving; it does not stretch into "
   "a streak.",
   "It leaves the surface behind dry: no wet trail, no darkened path where it has passed.",
   "It moves downhill or with whatever pushes it, and it does not climb the surface on its own.",
   "If it meets another drop they merge into one larger drop and the merged drop is rounder "
   "than a dumbbell, settling quickly.",
   "The drop is transparent: it refracts and brightens what is behind it, and carries a small "
   "specular highlight that stays put relative to the light while the drop moves."])
o(35, add=["On the lotus leaf the drop sits especially high and round, riding on the leaf's "
           "microtexture, and it detaches and rolls at the slightest tilt."])
g([36, 38], 'rewrite',
  "Bare glass and glazed ceramic are wettable, so water does not stay spherical on them: the "
  "drop flattens into a low dome, spreads its contact patch, tends to stick rather than slide, "
  "and leaves a wet trail if it does move.",
  ["The drop reads as a flattened dome, not a sphere: it is plainly wider than it is tall.",
   "Its edge meets the surface at a shallow angle, spread over a broad contact patch.",
   "It resists moving, and when it does move it stretches and leaves a wet trail or a "
   "darkened, glossy path behind it.",
   "Some liquid is left behind as it moves: the drop shrinks or breaks into a trail of smaller "
   "drops rather than travelling as one intact bead.",
   "It does not climb the surface on its own.",
   "The drop is transparent: it refracts what is behind it and carries a specular highlight."],
  issue="Bare glass and glazed ceramic are hydrophilic; water spreads on them. Requiring "
        "'spherical droplets' here would mark a physically correct clip wrong. Only the "
        "repellent surfaces (lotus leaf, waxed apple) support the spherical claim.")
g([39], 'rewrite',
  "Paper absorbs water. A dewdrop placed on a book does not slide across it as a bead: it "
  "wicks into the fibres, spreading as a darkened stain that grows and stops growing, and it "
  "cannot travel across the surface at all.",
  ["The drop soaks in where it touches rather than beading up and remaining intact.",
   "A darkened wet patch spreads outward from the contact and its edge advances, then stops.",
   "The wet patch never shrinks or retreats on its own; drying is slow and uniform, not a "
   "receding edge.",
   "The drop does not travel across the page as an intact bead, and it leaves no dry surface "
   "behind it.",
   "The paper itself answers the water: the wetted region darkens, and it may cock, wrinkle or "
   "buckle as the fibres swell.",
   "Ink or print under the wet patch may bleed or darken but does not move across the page."],
  issue="The caption's premise is physically impossible: water does not slide gracefully across "
        "paper, it is absorbed. The rubric must judge absorption, and the fact that no sliding "
        "bead appears is a fault of the caption, not of a clip that shows soaking. Semantic "
        "adherence and physical plausibility pull in opposite directions here.",
  flags=['premise-implausible'])
