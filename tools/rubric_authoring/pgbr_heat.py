# ============ Solidification: aqueous liquids (90, 91, 92) ==============
for i, subj, extra in [
    (90, 'water',
     ('minor', 'The ice is water ice -- clear or white -- and it floats in whatever liquid is '
               'left rather than sinking through it.',
      'the ice that forms sinks to the bottom of the remaining liquid')),
    (91, 'juice',
     ('minor', "The ice front pushes the juice's colour ahead of it, so the still-liquid core "
               "keeps the strongest colour and the frozen shell is paler than it.",
      'the frozen shell is deeper in colour than the unfrozen juice at its centre')),
    (92, 'milk',
     ('minor', 'Milk sets to an opaque solid; no clear transparent ice appears, since its fat '
               'and protein scatter light throughout.',
      'the milk freezes into clear transparent ice')),
]:
    add('freezing', i,
        f'A glass of {subj} is cooled far below freezing and turns solid.',
        S(('core', f'A glass of {subj} is present.'),
          ('core', 'The contents change state over the course of the shot rather than staying as '
                   'they began.'),
          ('core', 'The change is the one cooling produces -- toward freezing, not toward '
                   'boiling or drying out.'),
          ('minor', 'The shot reads as a timelapse: the change runs faster than it would in real '
                    'time.')),
        P(('fatal', 'The liquid ends up as a rigid solid: it no longer sloshes or flows when the '
                    'glass is disturbed.',
           'the contents stay entirely liquid although the temperature plainly drops to very low '
           'levels'),
          ('core', 'Freezing begins at the glass walls and the exposed top surface and advances '
                   'inward, so a solid shell forms before the core does.',
           'the middle solidifies first while the layer against the glass is still liquid'),
          ('core', 'The frozen region only grows while the temperature keeps falling; it does not '
                   'melt back and re-freeze repeatedly.',
           'the ice repeatedly retreats and re-forms although the cooling continues throughout'),
          ('major', 'The frozen material takes up slightly more room than the liquid did: the '
                    'level rises, and it may dome upward or crack the glass.',
           'the level plainly drops as the contents freeze'),
          ('major', 'Material is conserved: the glass does not fill itself further and the '
                    'contents do not disappear.',
           'the amount in the glass grows or vanishes with nothing added or removed'),
          ('minor', 'The surface stops moving as it sets: a solid surface no longer ripples or '
                    'sloshes.',
           'the surface of the frozen contents still ripples and sloshes'),
          ('minor', 'Frost or condensation appears on the outside of the glass, whose wall is now '
                    'below the surrounding dew point.',
           'the outside of the glass stays perfectly dry and clear although the contents froze'),
          extra))

# ============ Solidification: oil (93) ==================================
add('amorphous-solidification', 93,
    'A glass of oil is cooled far below freezing: it clouds and thickens into an opaque paste.',
    S(('core', 'A glass of oil is present.'),
      ('core', 'The contents change over the course of the shot rather than staying as they '
               'began.'),
      ('core', 'The change is the one cooling produces -- toward setting, not toward boiling or '
               'thinning.'),
      ('minor', 'The shot reads as a timelapse: the change runs faster than it would in real '
                'time.')),
    P(('fatal', 'The oil thickens as it cools and finally stops flowing when the glass is tilted '
                'or disturbed.',
       'the oil stays as freely runny at the end as at the start, or gets thinner, although the '
       'temperature plainly drops to very low levels'),
      ('core', 'It clouds progressively -- clear, then hazy, then opaque -- as it cools.',
       'the oil stays perfectly clear and transparent all the way to a solid'),
      ('core', 'The final state is an opaque waxy or buttery mass, not transparent ice with '
               'facets or advancing crystal fronts.',
       'the oil sets into clear faceted crystalline ice, the way water does'),
      ('core', 'The change advances from the coldest boundaries -- the walls and the top -- '
               'inward.',
       'the middle sets first while the layer against the glass is still runny'),
      ('major', 'The level does not rise: oil contracts on solidifying, so the surface stays put '
                'or drops slightly.',
       'the level plainly rises and domes upward as it sets, as freezing water does'),
      ('major', 'Material is conserved: the glass does not fill itself further and the contents '
                'do not disappear.',
       'the amount in the glass grows or vanishes with nothing added or removed'),
      ('minor', 'The change is progressive and one-directional while the temperature keeps '
                'falling.',
       'the oil repeatedly re-liquefies and re-thickens although the cooling continues throughout'),
      ('minor', 'Condensation or frost forms on the outside of the cold glass.',
       'the outside of the glass stays perfectly dry and clear although the contents set solid')),
    note="The dataset's law says the oil will freeze. Cooking oil has no sharp freezing point: it "
         "clouds and thickens to an opaque paste and contracts rather than expanding, so a rubric "
         "demanding water-like ice would reward the wrong clip.")

# ============ Solidification: beer (94) =================================
add('freezing-point-depression', 94,
    'A glass of beer is cooled far below freezing: it slushes, foams and expands.',
    S(('core', 'A glass of beer is present.'),
      ('core', 'The contents change state over the course of the shot rather than staying as they '
               'began.'),
      ('core', 'The change is the one cooling produces -- toward freezing, not toward boiling or '
               'drying out.'),
      ('minor', 'The shot reads as a timelapse: the change runs faster than it would in real '
                'time.')),
    P(('fatal', 'The beer ends up frozen: a slushy or solid mass that no longer pours or sloshes '
                'freely.',
       'the beer stays entirely liquid although the temperature plainly drops to very low levels'),
      ('core', 'A partly frozen slushy stage is visible before the contents are rigid, since the '
               'alcohol and dissolved solids depress the freezing point.',
       'the beer jumps straight from free-flowing liquid to fully rigid solid with no slushy '
       'stage in between'),
      ('core', 'Freezing begins at the glass walls and the exposed top surface and advances '
               'inward.',
       'the middle solidifies first while the layer against the glass is still liquid'),
      ('core', 'The frozen region only grows while the temperature keeps falling.',
       'the ice repeatedly retreats and re-forms although the cooling continues throughout'),
      ('major', 'Dissolved carbon dioxide comes out of solution as the liquid cools and freezes: '
                'bubbles form and foam gathers on top.',
       'no bubbles or foam appear at any point while a carbonated drink freezes'),
      ('major', 'The volume increases: the level rises and the foam can push over the rim.',
       'the level plainly drops as the contents freeze'),
      ('minor', 'The frozen mass is cloudy and slushy rather than clear ice.',
       'the beer freezes into clear transparent ice'),
      ('minor', 'Frost or condensation appears on the outside of the cold glass.',
       'the outside of the glass stays perfectly dry and clear although the contents froze')))

# ============ Melting (95-99) ==========================================
for i, subj, extra in [
    (95, 'a piece of ice',
     ('minor', 'The remaining ice sits in and floats in its own meltwater rather than sinking '
               'through it, and both stay clear or white.',
      'the shrinking ice sinks through its own meltwater')),
    (96, 'a candle',
     ('minor', 'Wax softens and sags well before it flows: a pool forms in the top around the '
               'wick while the body below is still solid, and wax that runs down the side cools '
               'and re-solidifies into an opaque ridge.',
      'the whole candle liquefies at once, or wax that runs down the cool side stays liquid '
      'indefinitely')),
    (97, 'butter',
     ('minor', 'Butter goes from firm and matte to glossy and slumped before it flows, and the '
               'melt is a clear yellow oil rather than an opaque white liquid.',
      'the butter turns straight into an opaque white liquid with no softening or glossing stage')),
    (98, 'ice cream',
     ('minor', 'The ice cream slumps and loses its scooped shape before liquefying, turning from '
               'matte and firm to glossy and runny.',
      'the ice cream keeps its scooped shape intact right up to the moment it is liquid')),
    (99, 'wax',
     ('minor', 'The wax softens and sags before it flows, and wax that runs away from the heat '
               'cools and re-solidifies into an opaque ridge.',
      'the wax turns instantly from rigid solid to free-running liquid with no softening stage')),
]:
    add('melting', i,
        f'{subj.capitalize()} is warmed well past its melting point and turns to liquid.',
        S(('core', f'{subj.capitalize()} is present.'),
          ('core', 'It changes state over the course of the shot rather than staying as it began.'),
          ('core', 'The change is the one warming produces -- toward melting, not toward freezing '
                   'or hardening.'),
          ('minor', 'The shot reads as a timelapse: the change runs faster than it would in real '
                    'time.')),
        P(('fatal', 'The solid turns to liquid: it shrinks while liquid appears, and the two '
                    'happen together.',
           'the solid stays entirely solid and unchanged although the temperature plainly rises '
           'well past its melting point'),
          ('core', 'Melting starts at the outer and most exposed surfaces and works inward.',
           'the interior liquefies first while the outer surface is still solid'),
          ('core', 'The change is one-directional while the temperature keeps rising: the solid '
                   'does not re-form or grow back.',
           'the solid grows back although the warming continues throughout'),
          ('core', 'The liquid runs downhill and pools at the lowest point available to it.',
           'the melt climbs upward, or stays heaped where it formed as though it were still '
           'solid'),
          ('major', 'Sharp edges and corners round off first, and the body slumps or sags as it '
                    'softens, before it is fully liquid.',
           'the solid keeps perfectly sharp edges and its exact shape until the instant it is '
           'gone'),
          ('major', 'Material is conserved: the pool grows only as the solid shrinks, and no '
                    'extra volume appears from nowhere.',
           'the pool of melt is far more than the solid could have supplied, or the solid '
           'disappears leaving nothing behind'),
          ('minor', 'The liquid is the same substance as the solid: it carries the same colour '
                    'rather than being a differently coloured fluid.',
           'the melt is a colour that has nothing to do with the solid it came from'),
          extra))

# ============ Liquefaction: condensation (100, 102, 103, 104) ==========
for i, vapour, surf, setting, extra in [
    (100, 'water vapour', 'cool glass surface', 'a humid environment',
     ('minor', 'The droplets gather on the face exposed to the humid air, not on the sheltered '
               'dry side.',
      'condensation builds on the sheltered dry side while the face in the humid air stays '
      'clear')),
    (102, 'steam', 'cool metal pot lid', 'a kitchen',
     ('minor', 'Drops that gather on the underside of the lid hang from it and drip back down '
               'into the pot.',
      'drops on the underside of the lid fall upward, or sit there without ever dripping while '
      'they keep growing')),
    (103, 'mist', 'cool plastic sheet', 'a greenhouse',
     ('minor', 'The plastic sheet sags where the collected water weighs it down, and the drops '
               'run to the low points of the sag.',
      'the sheet holds a heavy load of water without deflecting at all')),
    (104, 'water vapour', 'cool plastic sheet', 'a greenhouse',
     ('minor', 'The plastic sheet sags where the collected water weighs it down, and the drops '
               'run to the low points of the sag.',
      'the sheet holds a heavy load of water without deflecting at all')),
]:
    add('condensation', i,
        f'{vapour.capitalize()} in {setting} condenses into droplets on a {surf}.',
        S(('core', f'A {surf} is present.'),
          ('core', f'{vapour.capitalize()} or humid air is present around it.'),
          ('core', 'Condensation appears on the surface over the course of the shot rather than '
                   'being there from the start.'),
          ('minor', f'The setting reads as {setting}, as the caption says.'),
          ('minor', 'The shot reads as a timelapse: the change runs faster than it would in real '
                    'time.')),
        P(('fatal', 'Water collects on the cool surface: it fogs and then beads into droplets.',
           'nothing collects on the surface at all although humid air plainly meets a cool solid'),
          ('core', 'The water forms on the surface itself, not floating in the air in front of '
                   'it.',
           'droplets hang in mid-air in front of the surface instead of sitting on it'),
          ('core', 'What forms is liquid water -- rounded, translucent, mobile -- not frost, '
                   'crystals or ice.',
           'crystalline frost forms instead of liquid droplets, although the surface is only cool '
           'rather than freezing'),
          ('core', 'Droplets grow and merge into larger ones as time passes, and the wetted area '
                   'only increases while the surface stays cool and the air stays humid.',
           'the droplets shrink and disappear although the surface is still cool and the air '
           'still humid'),
          ('major', 'The surface fogs or clouds over first, and only then resolves into discrete '
                    'droplets.',
           'fully formed large droplets appear all at once with no misting stage before them'),
          ('major', 'Once heavy enough, droplets run down under gravity and leave clear streaks '
                    'behind them.',
           'droplets slide upward or sideways against gravity'),
          ('minor', 'What is behind the surface becomes harder to see as the condensation builds, '
                    'and clearer again along the streaks the running drops have cleared.',
           'the view through the surface is unaffected by heavy condensation on it'),
          extra))

# ============ Liquefaction: warm window (101) ==========================
add('condensation', 101,
    'Fog in a cold environment meets a warm car window, which stays clear.',
    S(('core', 'A car window is present with fog or mist in the air around it.'),
      ('core', 'A change at the window is shown over the course of the shot rather than a static '
               'scene.'),
      ('minor', 'The environment reads as cold, as the caption says.'),
      ('minor', 'The window reads as warm relative to its surroundings, as the caption says.'),
      ('minor', 'The shot reads as a timelapse: the change runs faster than it would in real '
                'time.')),
    P(('fatal', 'The warm glass does not accumulate condensation: it stays clear, or clears '
                'progressively, because the fog touching it is warmed above its dew point.',
       'droplets form and build up on the warm side of the glass as though it were the cold '
       'surface'),
      ('core', 'Any droplets already on the warm glass shrink and disappear rather than growing.',
       'existing droplets on the warm glass grow and merge'),
      ('core', 'Condensation, if it is shown anywhere, is on the cold side of the glass, not the '
               'warm side.',
       'condensation builds on the warm side while the cold side stays clear'),
      ('major', 'No frost or ice forms on a surface that is above freezing.',
       'frost crystals grow on the warm glass'),
      ('major', 'The fog outside drifts and thins with the air as one body, unaffected by the '
                'glass except right where it touches it.',
       'the fog is pinned motionless against the glass, or parts around it as though the air '
       'itself were solid'),
      ('minor', 'The view through the glass stays clear or gets clearer, so what is behind it '
                'remains visible.',
       'the view through the warm glass becomes steadily more obscured'),
      ('minor', 'No water appears from nowhere: nothing pours down the warm glass or pools '
                'beneath it without a source.',
       'water runs down the warm glass in quantity with nothing to supply it')),
    note="Recommended for exclusion. The caption (warm window, cold fog) and the dataset's law "
         "('the temperature of window is much lower than that of fog') contradict each other, and "
         "the caption's own physics gives evaporation rather than condensation. Ids 100, 102, 103 "
         "and 104 already cover the intended physics.")

# ============ Boiling (105-108) ========================================
for i, liq, vessel, extra in [
    (105, 'water', 'a pot',
     ('minor', 'The water stays clear and colourless: boiling agitates it but does not turn it '
               'into something else.',
      'the water changes colour or turns into a different substance as it boils')),
    (106, 'milk', 'a kettle',
     ('minor', "Milk's protein and fat skin traps the bubbles, so foam builds and climbs the "
               "wall as a rising head and can push over the rim -- which plain water in the same "
               "vessel would not do.",
      'the milk bubbles burst freely at a flat surface with no foam head building at all')),
    (107, 'soup', 'a saucepan',
     ('minor', 'Solid pieces in the soup are lifted and tumbled by the convection and the rising '
               'bubbles.',
      'solid pieces sit perfectly still while the soup around them boils vigorously')),
    (108, 'tea', 'a teapot',
     ('minor', 'Steam escapes from the spout and around the lid, the openings the vessel '
               'actually has.',
      'steam pours out through the solid walls of the teapot')),
]:
    add('boiling', i,
        f'{liq.capitalize()} in {vessel} is heated past boiling.',
        S(('core', f'{liq.capitalize()} is present in {vessel}.'),
          ('core', 'It is heated and reaches a boil over the course of the shot rather than '
                   'staying as it began.'),
          ('minor', f'The vessel reads as {vessel}, as the caption says.'),
          ('minor', 'The shot reads as a timelapse: the change runs faster than it would in real '
                    'time.')),
        P(('fatal', 'The liquid comes to a boil: vapour bubbles form in it and it goes into '
                    'continuous agitation.',
           'nothing happens at all although the liquid is plainly heated well past its boiling '
           'point'),
          ('core', 'Bubbles nucleate at the bottom and the heated walls, the hottest surfaces, '
                   'rather than in mid-liquid or only at the surface.',
           'bubbles appear in mid-liquid or only at the surface, with none forming on the '
           "vessel's hot surfaces"),
          ('core', 'Bubbles rise upward, growing as they go, and burst at the surface.',
           'bubbles sink, shrink as they rise, or hang motionless in the liquid'),
          ('core', 'The surface is in continuous agitation once boiling is established.',
           'the surface stays flat and mirror-like while bubbles pour through it'),
          ('major', 'Visible steam or vapour rises above the surface and disperses upward.',
           'no steam appears above a vigorously boiling liquid, or the vapour sinks to the floor'),
          ('major', 'The level slowly drops as liquid leaves as vapour.',
           'the level rises over a long boil with nothing added'),
          ('minor', 'Bubble production ramps up as the heating continues, rather than being at '
                    'full intensity before the vessel is heated, and it subsides if the heat is '
                    'taken away.',
           'a full rolling boil is present from the first frame, before any heating'),
          extra))

# ============ Boiling: oil (109) =======================================
add('convective-heating', 109,
    'Oil in a cauldron is heated hard: it shimmers and smokes rather than boiling.',
    S(('core', 'Oil is present in a cauldron.'),
      ('core', 'It is heated and changes over the course of the shot rather than staying as it '
               'began.'),
      ('minor', 'The vessel reads as a cauldron, as the caption says.'),
      ('minor', 'The shot reads as a timelapse: the change runs faster than it would in real '
                'time.')),
    P(('fatal', "Hot oil does not fill with a mass of its own rising vapour bubbles: its boiling "
                "point is hundreds of degrees above water's, so at this temperature it is merely "
                "hot.",
       'the oil goes into a uniform rolling boil with bubbles rising throughout, the way water '
       'does'),
      ('core', 'Convection is visible instead: the surface shimmers and streams, and suspended '
               'specks circulate through the body of the oil.',
       'the hot oil is perfectly still, with no shimmer and no circulation at all'),
      ('core', 'As it gets hotter, a faint haze or wisps of smoke rise from the surface.',
       'no haze or smoke ever appears however long and hard the oil is heated'),
      ('core', 'The oil is not consumed into vapour: the level does not fall the way a boiling '
               'aqueous liquid\'s does.',
       'the oil level falls steadily as though the oil were boiling away'),
      ('major', 'What rises off the oil is thin haze or smoke, not the dense white plume a '
                'boiling aqueous liquid gives.',
       'dense white steam billows off the oil as it would off boiling water'),
      ('major', 'Any bubbling is localised and violent -- spitting and popping where water has '
                'got into the oil -- rather than uniform across the vessel.',
       'gentle bubbles rise evenly from the whole base as in a steady simmer'),
      ('minor', 'The shimmer and haze subside when the heat is taken away, and nothing is '
                'happening before the vessel is heated.',
       'shimmer and smoke are at full strength from the first frame, before any heating'),
      ('minor', 'The oil darkens somewhat under prolonged strong heating rather than looking '
                'untouched.',
       'the oil visibly lightens in colour as it is heated hard')),
    note="The dataset's law -- that oil boils and bubbles here -- is false, and false in the "
         "direction that scores a wrong clip as correct: cooking oil boils several hundred degrees "
         "above this temperature, well past its smoke point. Bubbling in hot oil comes from water "
         "contamination flashing to steam. The law also refers to 'the coffee surface', a "
         "copy-paste artefact.")

# ============ Deposition (110-114) =====================================
for i, vapour, surf, setting, note in [
    (110, 'water vapour', 'cold glass surface', 'a humid environment', None),
    (111, 'steam', 'cold window', 'a kitchen', None),
    (112, 'mist', 'cold metal surface', 'a rainforest',
     "A rainforest held below freezing is implausible on its own terms; the setting is scored as "
     "caption adherence and the frost physics is judged as shown."),
    (113, 'fog', 'cold car windshield', 'a mountainous region', None),
    (114, 'moisture in the air', 'cold plastic bottle', 'a refrigerated room', None),
]:
    add('deposition', i,
        f'{vapour.capitalize()} in {setting} deposits directly as frost crystals on a {surf}.',
        S(('core', f'A {surf} is present.'),
          ('core', f'{vapour.capitalize()} or humid air is present around it.'),
          ('core', 'A deposit forms on the surface over the course of the shot rather than being '
                   'there from the start.'),
          ('minor', f'The setting reads as {setting}, as the caption says.'),
          ('minor', 'The shot reads as a timelapse: the change runs faster than it would in real '
                    'time.')),
        P(('fatal', 'Frost forms on the below-freezing surface.',
           'nothing forms on the surface at all although humid air plainly meets a below-freezing '
           'solid'),
          ('core', 'The deposit is crystalline -- feathery, needle-like or branching -- not '
                   'rounded liquid droplets.',
           'rounded liquid droplets form instead of crystals, on a surface that is plainly below '
           'freezing'),
          ('core', 'There is no liquid stage: no beads form and later freeze, and nothing runs '
                   'down under gravity.',
           'droplets gather first and then freeze in place'),
          ('core', 'The frost grows outward from nucleation points and spreads across the '
                   'surface, and the frosted area only increases while the surface stays below '
                   'freezing.',
           'the frost retreats and shrinks although the surface stays below freezing throughout'),
          ('major', 'The frost forms on the surface itself, not in the air in front of it.',
           'crystals hang in mid-air in front of the surface instead of growing on it'),
          ('major', 'It sticks where it grows -- it does not slide, drip or flow -- and it '
                    'follows the shape of the surface including vertical and overhanging parts, '
                    'since gravity is not what holds it on.',
           'the deposit slides, drips or runs off the surface'),
          ('minor', 'It is opaque white and progressively hides whatever is behind the surface.',
           'the frosted region stays perfectly clear and transparent as the deposit thickens'),
          ('minor', 'The frost stays dry: no puddle of meltwater collects beneath it while the '
                    'surface stays below freezing.',
           'water pools beneath the frost although the surface never warms')),
        note=(note or '') + (' ' if note else '') +
             "The dataset's law calls this sublimation; sublimation is the reverse (solid to gas) "
             "and vapour going straight to solid is deposition. The law also omits the one "
             "discriminator against the Liquefaction group (ids 100-104): crystalline frost with "
             "no droplet stage, which P2 and P3 carry.")

# ============ Sublimation: dry ice (115) ===============================
add('sublimation', 115,
    'A block of dry ice sublimes at room temperature, shedding cold fog and leaving no puddle.',
    S(('core', 'A block of dry ice is present.'),
      ('core', 'It changes over the course of the shot rather than staying as it began.'),
      ('minor', 'The surroundings read as room temperature with the temperature gradually '
                'rising, as the caption says.'),
      ('minor', 'The shot reads as a timelapse: the change runs faster than it would in real '
                'time.')),
    P(('fatal', 'The block visibly shrinks as it turns to gas.',
       'the dry ice stays exactly the same size throughout, sitting at room temperature'),
      ('core', 'No liquid puddle forms: the block does not melt, nothing runs off it, and the '
               'ground under it stays dry apart from water condensed out of the air.',
       'the block melts into a puddle of liquid'),
      ('core', 'White fog appears around and above the block while it shrinks -- the ambient '
               'water vapour condensing in the cold gas, since the carbon dioxide itself is '
               'invisible.',
       'nothing visible comes off the block as it shrinks away'),
      ('core', 'The fog is cold and dense, so it sinks and flows along the ground and over edges '
               'rather than rising.',
       'the fog rises and climbs away like steam from a kettle'),
      ('major', 'The fog thins and disperses away from the block as it warms and mixes with the '
                'room air.',
       'the fog stays a sharp-edged cloud at full density far from the block'),
      ('major', 'The shrinking is one-directional: the block never grows back at room '
                'temperature.',
       'the block grows back although it stays at room temperature'),
      ('minor', 'Frost or condensation appears on the surfaces the block is in contact with, '
                'chilled below the dew point.',
       'the surface under the block stays perfectly dry and unchilled'),
      ('minor', "The block's edges and corners round off as it sublimes.",
       'the block keeps perfectly sharp edges and corners while shrinking away')))

# ============ Sublimation: iodine (117) ================================
add('sublimation', 117,
    'Iodine crystals sublime to a violet vapour with no liquid stage.',
    S(('core', 'Iodine crystals are present.'),
      ('core', 'They change over the course of the shot rather than staying as they began.'),
      ('minor', 'The surroundings read as room temperature with the temperature gradually '
                'rising, as the caption says.'),
      ('minor', 'The shot reads as a timelapse: the change runs faster than it would in real '
                'time.')),
    P(('fatal', 'The crystals shrink and vapour appears above them as they are warmed.',
       'nothing comes off the crystals and they stay exactly the same size however long they are '
       'warmed'),
      ('core', 'No liquid forms at any point: no droplets on the crystals, no pool beneath them, '
               'no wet residue.',
       'the crystals melt to a liquid before any vapour appears'),
      ('core', 'The vapour is violet or purple.',
       'the vapour is white or colourless'),
      ('core', 'The crystals shrink as the vapour appears, and the two happen together.',
       'dense vapour pours off while the crystals stay exactly the same size'),
      ('major', 'The vapour is denser than air near its source, so it fills the vessel from the '
                'bottom upward rather than shooting away.',
       'the vapour jets straight upward and away as though it were far lighter than air'),
      ('major', 'Fresh crystals appear on the cooler surfaces above, where the vapour '
                're-deposits.',
       'no deposit appears anywhere although dense vapour fills the vessel'),
      ('minor', 'The vapour is darkest immediately above the crystals and thins and pales as it '
                'disperses.',
       'the vapour is palest at its source and darkest far away from it'),
      ('minor', 'The crystals keep their dark grey-violet metallic look and do not change colour '
                'before vaporising.',
       'the crystals turn a different colour as they sublime')))

# ============ Sublimation: arsenic trioxide (119) ======================
add('sublimation', 119,
    'Arsenic trioxide sublimes to a white fume and re-deposits as a white crust.',
    S(('core', 'A white solid identified as arsenic trioxide is present.'),
      ('core', 'It changes over the course of the shot rather than staying as it began.'),
      ('minor', 'The surroundings read as room temperature with the temperature gradually '
                'rising, as the caption says.'),
      ('minor', 'The shot reads as a timelapse: the change runs faster than it would in real '
                'time.')),
    P(('fatal', 'The solid shrinks while white vapour or fume rises from it.',
       'the solid stays exactly the same size and nothing comes off it however long it is warmed'),
      ('core', 'No liquid forms: nothing melts, pools or runs.',
       'the solid melts to a liquid before any vapour appears'),
      ('core', 'The solid shrinks as the fume appears, and the two happen together.',
       'dense fume pours off while the solid stays exactly the same size'),
      ('core', 'The solid stays white and powdery or crystalline rather than darkening, charring '
               'or slumping.',
       'the solid darkens, chars or slumps as it is warmed'),
      ('major', 'A white deposit builds up on the cooler surfaces above and around the solid, '
                'where the vapour re-deposits.',
       'no deposit appears anywhere although dense fume is plainly given off'),
      ('major', 'The shrinking is one-directional: the solid never grows back.',
       'the solid grows back while the warming continues'),
      ('minor', 'The fume disperses and thins with distance from the source.',
       'the fume stays a sharp-edged cloud at full density far from the solid'),
      ('minor', 'Nothing is happening before the warming begins.',
       'the solid is already fuming at full rate in the first frame, before any warming')),
    note="Only the wording of the dataset's law needed trimming: 'toxic' is not a visible "
         "property and is not a rubric item here.")

# ============ Sublimation: naphthalene, camphor (116, 118) =============
for i, subj in [(116, 'naphthalene'), (118, 'camphor')]:
    add('sublimation', i,
        f'A piece of {subj} sublimes away at room temperature with no liquid stage.',
        S(('core', f'A piece or pile of {subj} is present.'),
          ('core', 'It changes over the course of the shot rather than staying as it began.'),
          ('minor', 'The surroundings read as room temperature with the temperature gradually '
                    'rising, as the caption says.'),
          ('minor', 'The shot reads as a timelapse: the change runs faster than it would in real '
                    'time.')),
        P(('fatal', 'The solid shrinks as it turns to gas.',
           'the solid stays exactly the same size throughout, sitting at room temperature'),
          ('core', 'No liquid appears at any point: no droplets on the solid, no pool beneath it, '
                   'nothing runs off it.',
           'the solid melts into a liquid'),
          ('core', 'The solid keeps its own white waxy appearance and does not darken, char or '
                   'slump.',
           'the solid darkens, chars or slumps as it is warmed'),
          ('core', 'The shrinking is gradual and one-directional while the warming continues.',
           'the solid grows back although the warming continues throughout'),
          ('major', 'Its edges and corners round off and it thins as it goes.',
           'the solid keeps perfectly sharp edges and corners while shrinking away'),
          ('major', 'A thin white deposit builds up on nearby cooler surfaces where the vapour '
                    're-deposits.',
           'the solid disappears entirely with no deposit anywhere around it'),
          ('minor', 'Only faint vapour, shimmer or haze appears immediately above the solid, not '
                    'a dense plume: it sublimes slowly at room temperature.',
           'a thick billowing plume pours off the solid at room temperature'),
          ('minor', 'Nothing is happening before the warming begins.',
           'the solid is already visibly wasting away at full rate in the first frame, before '
           'any warming')),
        note="The dataset's law offers an odour as the evidence, which no video can show, so the "
             "rubric uses the judgeable signature instead: a shrinking solid with no liquid stage "
             "and a white re-deposit, as id 117 already does.")
