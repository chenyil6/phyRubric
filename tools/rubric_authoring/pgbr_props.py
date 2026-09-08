# ============ Colour: subtractive mixing (120, 121, 122, 124) ===========
DULL = ('core', 'The blend is as dark as the parents or darker and duller, never brighter or more '
                'vivid than both of them, since each pigment only takes more light away.',
        'the blend is brighter and more saturated than either paint that went into it')
VOL = ('minor', 'The total amount is the sum of the two and does not shrink or grow during the '
                'stirring.',
       'the amount in the container grows or shrinks with nothing added or removed')
for i, a, b, target, offhue, sat, extra in [
    (120, 'red', 'blue', 'purple', 'green or yellow', DULL,
     ('minor', 'Real red and blue paint give a dark, somewhat muddy purple rather than a vivid '
               'spectral violet, so a dull result is correct here.',
      'the blend is a brilliant saturated violet brighter than either paint')),
    (121, 'yellow', 'red', 'orange', 'green or blue', DULL, VOL),
    (122, 'green', 'blue', 'teal or blue-green', 'red or orange', DULL, VOL),
    (124, 'pink', 'white', 'a paler tint of pink', 'green or blue',
     ('core', 'White only lightens: the blend is a paler tint of the pink, lighter than the pink '
              'but no more vivid than it.',
      'the blend is deeper or more saturated pink than the pink paint that went into it'),
     ('minor', 'The result stays in the same hue family as the pink rather than shifting toward '
               'another colour.',
      'the blend shifts to a hue neither parent has, such as orange or lilac')),
]:
    add('subtractive-mixing', i,
        f'Equal amounts of {a} and {b} paint are stirred to a uniform {target}.',
        S(('core', f'{a.capitalize()} and {b} paint are both present, in roughly equal amounts.'),
          ('core', 'They are combined and stirred.'),
          ('core', 'The mixture ends up fully blended and uniform, as the caption says.'),
          ('minor', 'The combining and stirring read as rapid and vigorous, as the caption '
                    'says.')),
        P(('fatal', 'The two paints combine into one blended colour.',
           'the paints stay as two separate unmixed colours however long they are stirred'),
          ('core', f'The final colour is {target}, lying between the two parent hues.',
           f'the blend is a colour neither parent can give, such as {offhue}'),
          sat,
          ('core', 'The blend appears progressively as the stirring proceeds.',
           'the colour switches to its final value in a single frame with no intermediate stage'),
          ('major', 'Streaks and swirls of the unmixed parent colours are visible while the '
                    'stirring is under way, and they disappear as it homogenises.',
           'no streaks of the parent colours are ever visible during the stirring'),
          ('major', 'The parent colours are consumed as the blend forms: no untouched pool of '
                    'pure parent colour survives once it is fully blended.',
           'a pool of one pure parent colour is still sitting there at the end'),
          ('minor', 'The change is irreversible: the mixture does not un-mix back into two '
                    'colours.',
           'the blend separates back into the two parent colours'),
          extra))

# ============ Colour: cyan + magenta (123) ==============================
add('subtractive-mixing', 123,
    'Equal amounts of cyan and magenta paint are stirred to a uniform blue.',
    S(('core', 'Cyan and magenta paint are both present, in roughly equal amounts.'),
      ('core', 'They are combined and stirred.'),
      ('core', 'The mixture ends up fully blended and uniform, as the caption says.'),
      ('minor', 'The combining and stirring read as rapid and vigorous, as the caption says.')),
    P(('fatal', 'The two paints combine into one blended colour.',
       'the paints stay as two separate unmixed colours however long they are stirred'),
      ('core', 'The final colour is blue or blue-violet -- cyan absorbs red and magenta absorbs '
               'green, so what is left is blue -- and it is clearly bluer than the magenta it '
               'came from.',
       'the blend is a red-leaning purple or a magenta-dominated violet rather than blue'),
      ('core', 'The blend is as dark as the parents or darker and duller, never brighter or more '
               'vivid than both of them.',
       'the blend is brighter and more saturated than either paint that went into it'),
      ('core', 'The blend appears progressively as the stirring proceeds.',
       'the colour switches to its final value in a single frame with no intermediate stage'),
      ('major', 'Streaks and swirls of the unmixed cyan and magenta are visible while the '
                'stirring is under way, and they disappear as it homogenises.',
       'no streaks of the parent colours are ever visible during the stirring'),
      ('major', 'Both parent colours are consumed: no pool of pure cyan or pure magenta survives '
                'at the end.',
       'a pool of one pure parent colour is still sitting there at the end'),
      ('minor', 'The change is irreversible: the mixture does not separate back into cyan and '
                'magenta.',
       'the blend separates back into the two parent colours'),
      ('minor', 'The total amount is the sum of the two and does not shrink or grow during the '
                'stirring.',
       'the amount in the container grows or shrinks with nothing added or removed')),
    note="The dataset's law names purple. Subtractive mixing of cyan and magenta gives blue, and "
         "'purple' is loose enough that a red-leaning violet -- which would require a "
         "red-absorbing failure -- would pass, in a sub-category whose whole point is the specific "
         "hue.")

# ============ Flame reaction (125-129) ==================================
for i, metal, colour, badcolour, extra, note in [
    (125, 'copper', 'green or blue-green', 'an ordinary yellow-orange with no green in it',
     ('minor', 'The flame is anchored at the metal and the green is brightest close to it, '
               'fading outward.',
      'the green is brightest far from the metal and absent close to it'),
     "Bulk copper metal will not actually catch fire; flame-test green comes from copper compounds "
     "or fine powder held in an existing flame. The implausible ignition is the prompt's own "
     "premise and is scored as caption adherence, not as a physics violation."),
    (126, 'magnesium', 'a brilliant dazzling white', 'a dim yellow-orange rather than white',
     ('minor', 'Magnesium burns bright enough to wash out the exposure, and it leaves a white '
               'powdery ash.',
      'the magnesium burns dimly, or leaves a black sooty residue instead of white ash'), None),
    (127, 'lithium', 'crimson red', 'green, blue or white rather than crimson',
     ('minor', 'The lithium reacts with the air as it burns, dulling and coating with a whitish '
               'product rather than staying silvery.',
      'the lithium stays bright silvery metal throughout the burn'), None),
    (128, 'sodium', 'an intense yellow-orange', 'green, blue or violet rather than yellow-orange',
     ('minor', 'The sodium melts into a ball as it burns, and its yellow-orange is intense enough '
               'to dominate the colour of the whole scene.',
      'the sodium stays a rigid unmelted lump, or the intense flame leaves the rest of the '
      "scene's colours untouched"), None),
    (129, 'potassium', 'a pale lilac', 'green or deep blue rather than lilac',
     ('minor', 'The lilac is pale and easily swamped -- a faint tint on the flame rather than a '
               'deep saturated purple.',
      'the flame is a deep saturated purple far more vivid than a pale lilac'), None),
]:
    add('flame-emission', i,
        f'A piece of {metal} burns with its characteristic {colour} flame.',
        S(('core', f'A piece of {metal} is present.'),
          ('core', 'It is ignited and burns with a visible flame.'),
          ('core', 'The burning continues over a stretch of the shot rather than a single frame, '
                   'as the caption says.'),
          ('minor', 'The flame reads as vivid and distinctive, as the caption says.')),
        P(('fatal', f"The flame takes {metal}'s characteristic colour: {colour}.",
           f'the flame is {badcolour}'),
          ('core', 'The colour is in the flame itself and in the hot gas around the burning '
                   'metal, not a tint painted on the solid.',
           'the colour sits on the surface of the solid while the flame above it is an ordinary '
           'fire colour'),
          ('core', 'The colour stays the same for as long as the metal keeps burning.',
           'the flame cycles through unrelated colours while the same metal burns'),
          ('core', 'The flame rises and flickers upward and stays anchored to the burning metal.',
           'the flame hangs detached from the metal, or points downward with no draught to '
           'explain it'),
          ('major', 'The flame casts light of its own colour on the surfaces near it.',
           'the surroundings are lit a colour quite different from the flame, or a bright flame '
           'lights nothing at all'),
          ('major', 'The metal is consumed as it burns: it darkens, shrinks or leaves a residue.',
           'the metal is still pristine and full size after burning steadily'),
          ('minor', 'The flame goes out when the metal is used up, and nothing is burning before '
                    'the ignition.',
           'the flame is already burning in the first frame, before the ignition'),
          extra),
        note=note)

# ============ Hardness: brittle fracture (130-133) =====================
for i, obj, target, extra in [
    (130, 'egg', 'rugged rock surface',
     ('minor', "The shell fragments and the yolk and white splatter, then run downward under "
               "gravity and cling to the rock in streaks.",
      'the egg contents stay as a compact ball, or run upward across the rock')),
    (131, 'lightweight vase', 'sturdy concrete wall',
     ('minor', 'A hard throw gives many pieces thrown wide rather than a single neat crack.',
      'a violent impact leaves the object in one piece with a single hairline crack')),
    (132, 'glass bottle', 'rugged rock surface',
     ('minor', 'Glass shatters into many small shards that scatter widely and catch the light.',
      'the bottle splits into two large clean halves with no shards at all')),
    (133, 'brittle glass cup', 'solid metallic surface',
     ('minor', 'A hard throw gives many pieces thrown wide rather than a single neat crack.',
      'a violent impact leaves the object in one piece with a single hairline crack')),
]:
    add('brittle-fracture', i,
        f'A {obj} is thrown hard at a {target} and shatters on impact.',
        S(('core', f'A {obj} and a {target} are both present.'),
          ('core', f'The {obj} is thrown at the surface and reaches it.'),
          ('minor', 'The throw reads as forceful and fast, as the caption says.'),
          ('minor', f'The target reads as the {target} the caption names.')),
        P(('fatal', 'The thrown object breaks on impact: it cannot absorb the impact by deforming, '
                    'so it fractures.',
           'the object bounces off intact, or sticks to the surface undamaged'),
          ('core', 'It breaks at the moment and the place of contact.',
           'it comes apart in mid-air before it lands, or survives the impact whole and falls '
           'apart later with nothing touching it'),
          ('core', 'Fragments and contents fly outward from the impact point, away from the '
                   'surface, and then fall under gravity.',
           'the fragments hang in the air or drift off with no regard to gravity'),
          ('core', 'The breakage is irreversible: fragments do not reassemble and the object does '
                   'not re-form.',
           'the fragments come back together into the intact object'),
          ('major', f'The {target} is left essentially undamaged: the projectile takes all the '
                    f'destruction.',
           'the target surface shatters or is punched through by the thrown object'),
          ('major', 'The object follows a ballistic path before impact: it does not hover, slow '
                    'in mid-air, or change direction on its own.',
           'the object hovers, stops in flight, or changes direction with nothing acting on it'),
          ('minor', 'The debris comes to rest on the ground or on the surface and stays there.',
           'the debris goes on sliding or twitching after everything else has settled'),
          extra))

# ============ Hardness: porcelain on wood (134) ========================
add('brittle-fracture', 134,
    'A porcelain plate is flung hard at a wooden table and shatters, marking the table.',
    S(('core', 'A porcelain plate and a wooden table are both present.'),
      ('core', 'The plate is flung at the table and reaches it.'),
      ('minor', 'The throw reads as fast and forceful, as the caption says.'),
      ('minor', 'The table reads as the robust wooden table the caption names.')),
    P(('fatal', 'The plate breaks on impact: it is brittle, the impact is fast, and the table is '
                'rigid enough not to give way.',
       'the plate bounces off intact, or sticks to the table undamaged'),
      ('core', 'It breaks at the moment and the place of contact.',
       'it comes apart in mid-air before it lands, or survives the impact whole and falls apart '
       'later with nothing touching it'),
      ('core', 'Fragments fly outward from the impact point and then fall under gravity.',
       'the fragments hang in the air or drift off with no regard to gravity'),
      ('core', 'The breakage is irreversible: fragments do not reassemble.',
       'the fragments come back together into the intact plate'),
      ('major', 'The table survives as a table: it may be scuffed, dented or scratched -- wood is '
                'softer than porcelain -- but it does not shatter or get punched through.',
       'the wooden table shatters or is punched through by the plate'),
      ('major', 'The plate follows a ballistic path before impact: it does not hover, slow in '
                'mid-air, or change direction on its own.',
       'the plate hovers, stops in flight, or changes direction with nothing acting on it'),
      ('minor', 'The debris comes to rest and stays put.',
       'the debris goes on sliding or twitching after everything else has settled'),
      ('minor', 'A hard throw gives many pieces thrown wide rather than a single neat crack.',
       'a violent impact leaves the plate in one piece with a single hairline crack')),
    note="The dataset's law says the hardness of the wood is very high, which is false -- wood is "
         "far softer than porcelain, and the sibling entries use stone, concrete and metal "
         "precisely because those are rigid. The plate still shatters, but the target is allowed "
         "to be dented or scratched here.")

# ============ Solubility: immiscible pairs (135, 139) ==================
for i, poured, into, extra in [
    (135, 'oil', 'water',
     ('minor', 'Oil poured into water sinks momentarily as a stream, then breaks into globules '
               'that rise and coalesce into a film on top.',
      'the oil stays at the bottom as a coherent stream and never rises')),
    (139, 'vinegar', 'oil',
     ('minor', 'Neither liquid takes the other\'s colour or clarity: no band of '
               'intermediate-coloured blend forms at the interface.',
      'a band of intermediate-coloured blend forms at the interface and stays there')),
]:
    add('immiscibility', i,
        f'A glass of {poured} is poured gently into a glass of {into}; they separate into layers.',
        S(('core', f'{poured.capitalize()} and {into} are both present.'),
          ('core', f'The {poured} is poured into the {into}, in the direction the caption gives.'),
          ('minor', 'The pour reads as gentle and steady, as the caption says.'),
          ('minor', 'The vessels read as glasses, as the caption says.')),
        P(('fatal', 'The two liquids end up as two distinct layers with a visible boundary between '
                    'them.',
           'they blend into one uniform liquid with no boundary anywhere'),
          ('core', 'The oil is the upper layer and the water-based liquid the lower one, whichever '
                   'was poured into which, since the oil is the lighter of the two.',
           'the oil settles beneath the water-based liquid'),
          ('core', 'The poured liquid travels to its own layer rather than staying where it '
                   'landed.',
           'the poured liquid stays as a blob on the wrong side of the interface indefinitely'),
          ('core', 'Droplets of one liquid inside the other stay rounded with sharp edges rather '
                   'than diffusing into a gradient.',
           'droplets blur out into a gradient and vanish into the surrounding liquid'),
          ('major', 'The interface settles to a flat, level line once the disturbance dies down.',
           'the interface stays permanently domed, tilted or ragged after everything is still'),
          ('major', "The total level rises by the amount added, and each layer's thickness "
                    "matches how much of that liquid is present.",
           'the level does not change when a glassful is poured in, or one layer is far thicker '
           'than the amount of that liquid could account for'),
          ('minor', 'The pour disturbs the liquids and the disturbance dies down as they come to '
                    'rest.',
           'the liquids go on churning indefinitely after the pour has stopped'),
          extra))

# ============ Solubility: miscible pairs (137, 138) ====================
for i, poured, into, sign, note in [
    (137, 'vinegar', 'water',
     ('major', 'Both liquids are clear, so the visible sign of mixing is refractive shimmer and '
               'the flow it drives rather than any change of colour.',
      'a strong colour appears where two clear liquids are combined'),
     "The law is correct but nearly unjudgeable on video: clear liquid into clear liquid leaves "
     "almost no visible evidence either way, so this entry carries little weight next to id 138."),
    (138, 'juice', 'water',
     ('major', "The juice's colour makes the mixing directly visible: coloured plumes sink and "
               "spread, and the whole glass ends up an intermediate, weaker colour than the "
               "undiluted juice.",
      'the whole glass ends up as strongly coloured as the undiluted juice, or the colour '
      'disappears entirely'),
     None),
]:
    add('miscibility', i,
        f'A glass of {poured} is poured gently into a glass of {into} and mixes completely.',
        S(('core', f'{poured.capitalize()} and {into} are both present.'),
          ('core', f'The {poured} is poured into the {into}.'),
          ('minor', 'The pour reads as gentle and steady, as the caption says.'),
          ('minor', 'The vessels read as glasses, as the caption says.')),
        P(('fatal', 'The two liquids end up as one uniform liquid with no visible boundary or '
                    'layers, since both are water-based and fully miscible.',
           'they settle into two distinct layers with a lasting interface between them'),
          ('core', 'Mixing starts at the point of entry and spreads outward from there as plumes '
                   'and streaks.',
           'the mixing starts somewhere the poured liquid never reached, or the whole glass '
           'changes at once'),
          ('core', 'The streaks fade progressively into uniformity rather than snapping to the '
                   'finished state.',
           'the mixture jumps to its uniform end state in a single frame'),
          ('core', 'Nothing poured in holds its shape: no rounded sharp-edged droplets persist.',
           'the poured liquid holds together as sharp-edged blobs that never dissipate'),
          sign,
          ('major', 'The level rises by the amount added.',
           'the level does not change when a glassful is poured in'),
          ('minor', 'The flow follows gravity and the pour: it enters from above and sinks or '
                    'spreads, and the circulation dies down as the liquid comes to rest.',
           'the poured liquid rises up out of the glass, or the circulation goes on indefinitely '
           'after the pour has stopped'),
          ('minor', 'The mixing is irreversible: the uniform liquid does not separate back into '
                    'its two components.',
           'the blended liquid separates back into the two liquids it was made from')),
        note=note)

# ============ Solubility: honey into milk (136) ========================
add('density-layering', 136,
    'A glass of honey is poured gently into milk: it sinks as ropes, layers at the bottom, then '
    'dissolves.',
    S(('core', 'Honey and milk are both present.'),
      ('core', 'The honey is poured into the milk.'),
      ('minor', 'The pour reads as gentle and steady, as the caption says.'),
      ('minor', 'The vessels read as glasses, as the caption says.')),
    P(('fatal', 'The honey sinks through the milk, being much the denser of the two.',
       'the honey rises through the milk, or hangs motionless where it was poured'),
      ('core', 'It falls as a thick coherent rope or column that briefly keeps its shape, since '
               'it is far more viscous than the milk.',
       'the honey disperses instantly on entry as a thin watery liquid would'),
      ('core', 'It gathers into a distinct layer at the bottom of the glass.',
       'it gathers into a layer floating on top of the milk'),
      ('core', 'That layer is temporary: honey is a concentrated sugar solution and does dissolve '
               'in an aqueous liquid, so its edges blur and it thins into the milk over time, '
               'faster with stirring.',
       'the honey stays a permanent sharp-edged layer that never dissolves, the way an immiscible '
       'liquid would'),
      ('major', "The milk next to the honey takes on the honey's tint as it dissolves.",
       'the milk right against the dissolving honey is completely unaffected in colour'),
      ('major', 'The level rises by the amount poured.',
       'the level does not change when a glassful is poured in'),
      ('minor', 'The dissolution is irreversible: once mixed, the honey does not re-gather into a '
                'layer.',
       'the dissolved honey re-gathers into a layer at the bottom'),
      ('minor', 'The honey moves sluggishly throughout -- it pours, falls and spreads far more '
                'slowly than a thin liquid would.',
       'the honey pours and falls as fast and freely as water')),
    note="The dataset's law says honey and milk cannot dissolve each other because they are "
         "immiscible. Honey is sugar in water and dissolves fully in an aqueous liquid: a rubric "
         "demanding a permanent interface would penalise the correct behaviour. The layering is "
         "real but it is a density-and-viscosity effect and it is transient.")

# ============ Combustibility (141, 142, 144) ===========================
for i, igniter, pile, extra in [
    (141, 'burning match', 'pile of dry leaves',
     ('minor', 'Leaves curl and darken just ahead of the flame front, before the flame itself '
               'arrives.',
      'leaves stay flat and unmarked right up to the instant the flame touches them')),
    (142, 'burning stick', 'pile of hay',
     ('minor', 'Hay burns fast and bright with a lot of light ash, and the pile collapses inward '
               'as it is consumed.',
      'the hay pile keeps its full shape and height after being burnt through')),
    (144, 'burning piece of cloth', 'pile of old newspapers',
     ('minor', 'Sheets curl and blacken, then flare and collapse, and light ash can be carried up '
               'by the hot draught.',
      'the newspaper stays flat and unmarked while flames pass over it')),
]:
    add('combustion-spread', i,
        f'A small {igniter} is thrown into a {pile} and sets it alight.',
        S(('core', f'A small {igniter} is present and alight.'),
          ('core', f'It is thrown into a {pile}.'),
          ('core', f'The fuel reads as the dry{pile.split("of")[-1]} the caption names.'),
          ('minor', 'The burning object reads as small next to the pile, as the caption says.')),
        P(('fatal', 'The pile catches fire from the burning object.',
           'the pile does not ignite at all although a flame is plainly in contact with dry fuel'),
          ('core', 'Ignition starts where the burning object lands and touches the pile, not '
                   'elsewhere and not all over at once.',
           'the whole pile ignites at once, or the fire starts away from where the object landed'),
          ('core', 'The flame front spreads outward from the ignition point across the pile, and '
                   'the fire grows as it recruits more fuel.',
           'the flame stays a single spot and never spreads, or it stays exactly the size of the '
           'small burning object throughout'),
          ('core', 'The fuel is consumed: it blackens, curls, shrinks and is left as ash and '
                   'char, and burnt fuel stays burnt.',
           'the fuel is untouched and unmarked after the flames have passed over it, or burnt '
           'material returns to its unburnt state'),
          ('major', 'Smoke is produced and rises upward, drifting with the air.',
           'a spreading fire gives off no smoke at all, or the smoke sinks to the ground'),
          ('major', 'Unburnt fuel outside the flame front stays unchanged until the front reaches '
                    'it.',
           'fuel far from the flames blackens and collapses before the front gets anywhere near '
           'it'),
          ('minor', 'Flames point upward however the pile is oriented, leaning only with a '
                    'draught.',
           'the flames point downward or sideways with no draught to explain it'),
          extra))

# ============ Combustibility: paper into paper (140) ===================
add('combustion-spread', 140,
    'A small burning ball of paper is thrown into a pile of dry paper and sets it alight.',
    S(('core', 'A small burning ball of paper is present and alight.'),
      ('core', 'It is thrown into a pile of dry paper.'),
      ('core', 'The fuel reads as dry paper, as the caption names.'),
      ('minor', 'The burning ball reads as small next to the pile, as the caption says.')),
    P(('fatal', 'The paper pile catches fire from the burning ball.',
       'the pile does not ignite at all although a flame is plainly in contact with dry paper'),
      ('core', 'Ignition starts where the burning ball lands in the pile, not elsewhere and not '
               'all over at once.',
       'the whole pile ignites at once, or the fire starts away from where the ball landed'),
      ('core', 'The flame front spreads outward from there across the paper and grows, and it '
               'spreads quickly, as thin sheets do, rather than smouldering like a solid log.',
       'the paper chars slowly with glowing embers and no flare, or the flame never spreads from '
       'where it landed'),
      ('core', 'Individual sheets curl, darken and blacken just ahead of the flame, then flare '
               'and collapse into fragile ash that keeps the sheets\' shapes until disturbed.',
       'the sheets stay flat and unmarked while flames pass over them'),
      ('major', 'Smoke rises upward, and light ash can be carried up by the hot draught.',
       'a spreading paper fire gives off no smoke at all, or the smoke sinks to the ground'),
      ('major', 'Unburnt sheets away from the front stay unchanged until it reaches them.',
       'paper far from the flames blackens and collapses before the front gets anywhere near it'),
      ('minor', 'The burning is irreversible: consumed paper does not return.',
       'burnt paper returns to its unburnt state'),
      ('minor', 'Flames point upward however the pile is oriented, leaning only with a draught.',
       'the flames point downward or sideways with no draught to explain it')),
    note="The dataset's law refers to 'combustibility of wood, the wood will be ignited', but the "
         "caption has no wood in it -- it is paper into paper. Wood and paper also burn visibly "
         "differently (slow charring and embers versus fast flare and light ash), so the "
         "substitution is not harmless.")

# ============ Combustibility: thrown candle (143) ======================
add('combustion-spread', 143,
    'A small burning candle is thrown into dry grass; whether it is still lit on landing decides '
    'the outcome.',
    S(('core', 'A small candle is present and alight at the start.'),
      ('core', 'It is thrown into a pile of dry grass.'),
      ('minor', 'The grass reads as the dry grass the caption names.'),
      ('minor', 'The candle reads as small, as the caption says.')),
    P(('fatal', 'Whether the candle is still lit when it lands is shown, and the outcome follows '
                'from it: a still-burning flame in dry grass starts a fire, and an extinguished '
                'candle does not.',
       'an obviously extinguished candle sets the grass alight, or a plainly still-burning flame '
       'lands in dry grass and nothing at all happens'),
      ('core', 'The candle follows a ballistic path through the air.',
       'the candle hovers, stops in flight, or changes direction with nothing acting on it'),
      ('core', 'A flame that survives the throw is deflected backwards by the motion rather than '
               'standing straight up.',
       'the flame stands perfectly upright and undisturbed while the candle flies through the air'),
      ('major', 'A flame that has visibly gone out does not re-light on its own.',
       'an extinguished wick re-lights with nothing to light it'),
      ('major', 'The candle is a solid object: it lands in the grass and stays there.',
       'the candle disappears on landing, or sinks through the ground'),
      ('minor', 'Whatever is burning gives off smoke that rises upward and drifts with the air.',
       'the smoke sinks to the ground or hangs motionless while the air is plainly moving'),
      ('core', 'The fire starts where the candle lands and the flame front spreads outward from '
               'there and grows.',
       'the fire starts away from where the candle landed, or never spreads from that spot',
       'the grass catches fire'),
      ('major', 'The burning grass blackens, curls and is consumed to ash, irreversibly.',
       'burnt grass returns to its unburnt state, or the flames leave the grass unmarked',
       'the grass catches fire')),
    note="The dataset's law mandates that the grass will be ignited, which penalises the most "
         "likely real outcome: a candle thrown through the air is usually blown out by its own "
         "motion. The target here is internal consistency instead -- either outcome is correct, "
         "but not both at once.")
