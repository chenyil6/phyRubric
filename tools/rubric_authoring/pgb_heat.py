# ---- Heat / Solidification (90, 91, 92) --------------------------------
g([90, 91, 92], 'ok',
  "Held below its freezing point, an aqueous liquid crystallises into a rigid solid. It freezes "
  "inward from the coldest boundaries -- the walls and the exposed top -- so a solid shell forms "
  "first and the still-liquid core is the last to go; water expands on freezing, so the level "
  "rises and can dome or crack the vessel.",
  ["The liquid loses its free surface and becomes a rigid solid that no longer sloshes or "
   "flows when the glass is disturbed.",
   "Freezing begins at the glass walls and the exposed surface and advances inward, rather than "
   "the middle solidifying first or the whole volume setting at once.",
   "The frozen region only grows while the temperature keeps falling; it does not retreat and "
   "re-freeze repeatedly.",
   "The surface stops rippling and locks in place before the interior is solid.",
   "The frozen material occupies slightly more volume than the liquid did: the level rises "
   "rather than dropping, and it can dome upward or crack the glass.",
   "The frozen material is cloudy or opaque where dissolved air and solids are pushed ahead of "
   "the freezing front, not perfectly clear throughout.",
   "The vessel does not fill itself or lose material: the amount present is conserved apart "
   "from the volume change.",
   "Frost or condensation appears on the outside of the glass, since its wall is now below the "
   "surrounding dew point."])
o(91, add=["The juice's colour concentrates in the still-liquid core as the ice front pushes "
           "solutes ahead of it, so the frozen shell is paler than the centre."])
o(92, add=["Milk sets to an opaque solid; no clear ice appears, since its fat and protein "
           "scatter light throughout."])
g([93], 'rewrite',
  "Cooking oil has no sharp freezing point. As it cools it clouds, thickens and stops flowing, "
  "ending as an opaque waxy paste or soft solid rather than clear crystalline ice -- and it "
  "contracts rather than expanding.",
  ["The oil clouds progressively: it goes from clear to hazy to opaque as it cools.",
   "It thickens visibly -- it flows more and more sluggishly and finally stops flowing when the "
   "glass is tilted or disturbed.",
   "The final state is an opaque waxy or buttery mass, not transparent ice with facets or "
   "crystal fronts.",
   "The change advances from the coldest boundaries -- the walls and the top -- inward.",
   "The level does not rise: oil contracts on solidifying, so the surface stays put or drops "
   "slightly.",
   "The change is progressive and one-directional while the temperature keeps falling.",
   "Condensation or frost forms on the outside of the cold glass."],
  issue="'Below the freezing point, the oil will freeze' invites a rubric item that demands "
        "water-like freezing. Real oil clouds and thickens to a paste, does not form clear "
        "crystalline ice, and contracts instead of expanding -- so a verbatim rubric would "
        "reward a clip that renders oil as ice and would penalise the correct cloudy-paste "
        "result. The correct answer here is also the sharpest discriminator in the whole "
        "solidification group.")
g([94], 'ok',
  "Beer is mostly water with alcohol and dissolved CO2. Its freezing point is depressed, so it "
  "sets to a slush before a solid; the water freezes preferentially, and the dissolved gas is "
  "driven out as the liquid cools and freezes, so bubbles and foam appear and the can or glass "
  "can overflow.",
  ["The beer thickens into a slush -- part solid, part liquid -- before it becomes a rigid solid.",
   "Freezing begins at the walls and the exposed surface and advances inward.",
   "Dissolved CO2 comes out of solution: bubbles form and foam rises on top as freezing proceeds.",
   "The volume increases: the level rises, the foam can push over the rim, and a sealed "
   "container can bulge or burst.",
   "The frozen mass is cloudy and slushy rather than clear ice.",
   "The frozen region only grows while the temperature keeps falling.",
   "Condensation or frost forms on the outside of the cold vessel.",
   "The final solid no longer sloshes when the vessel is moved."])

# ---- Heat / Melting (95-99) --------------------------------------------
g([95, 96, 97, 98, 99], 'ok',
  "Above its melting point the solid turns to liquid, starting at the warmest, most exposed "
  "surfaces and working inward: edges round off, the body slumps under its own weight, and the "
  "liquid runs downhill and pools. Nothing is created -- the solid shrinks by exactly what the "
  "liquid gains -- and the change does not reverse while the temperature stays high.",
  ["The solid visibly shrinks while liquid appears, and the two changes happen together.",
   "Melting starts at the outer and most exposed surfaces and progresses inward, not from the "
   "centre outward.",
   "Sharp edges and corners round off first.",
   "The body slumps, sags or loses its shape as it softens, before it is fully liquid.",
   "The liquid runs downhill and pools at the lowest point rather than staying heaped or "
   "climbing.",
   "The material is conserved: the pool grows only as the solid shrinks, and no extra volume "
   "appears from nowhere.",
   "The change is one-directional while the temperature keeps rising -- the solid does not "
   "re-form or grow back.",
   "The remaining solid keeps its own colour and texture; the liquid is the same substance, not "
   "a different-coloured fluid."])
o(95, add=["The remaining ice sits in and floats in its own meltwater rather than sinking, and "
           "it stays clear or white while the meltwater is clear."])
o(96, add=["Wax softens and sags well before it flows: a pool forms in the top around the wick "
           "while the body below is still solid, and wax that runs down the side re-solidifies "
           "into an opaque ridge as it cools."])
o(99, add=["Wax softens and sags before it flows, and wax that runs away from the heat cools "
           "and re-solidifies into an opaque ridge."])
o(98, add=["Ice cream slumps and loses its scooped shape before liquefying, and it turns from "
           "matte and firm to glossy and runny."])

# ---- Heat / Liquefaction (100, 102, 103, 104) --------------------------
g([100, 102, 103, 104], 'ok',
  "Air holding water vapour cools where it touches a surface below its dew point, so vapour "
  "condenses on that surface: it fogs, then beads into droplets that grow, merge and run down "
  "under gravity. Condensation happens on the cold surface, not in mid-air.",
  ["Droplets form on the cold surface itself, not floating in the air in front of it.",
   "The surface fogs or clouds first, then resolves into discrete droplets.",
   "Droplets grow with time and merge into larger ones; the total wetted area only increases "
   "while the surface stays cold and the air stays humid.",
   "Once large enough, droplets run down under gravity and leave clear streaks behind them.",
   "Droplets form on the face exposed to the humid air, not on the sheltered or dry side.",
   "The droplets are liquid water -- rounded, translucent, mobile -- not frost, crystals or ice.",
   "What is behind the surface becomes harder to see as the condensation builds, and clearer "
   "again along the streaks the running drops clear.",
   "The vapour or mist in the air is depleted or unchanged, never made denser, by condensing "
   "onto the surface."])
o(102, add=["Drops that gather on the underside of the lid hang from it and drip back into the "
            "pot rather than falling off sideways."])
o(103, add=["The plastic sheet sags where the collected water weighs it down, and the drops run "
            "to the low points of the sag."])
g([101], 'exclude',
  "The caption and the law contradict each other, and the caption's own physics does not "
  "produce condensation: fog meeting a WARM window is warmed above its dew point, so the "
  "droplets evaporate and the glass clears -- the opposite of the stated outcome.",
  ["If the window is genuinely warmer than the surrounding fog, the glass stays clear or clears "
   "progressively, and any existing droplets shrink and disappear rather than growing.",
   "Condensation, if shown at all, is on the cold side of the glass, not the warm side.",
   "Fog outside the window drifts and thins with the air, unaffected by the glass except where "
   "it touches it."],
  issue="Direct caption/law conflict. The caption says a WARM car window in a COLD environment; "
        "the law says 'the temperature of window is much lower than that of fog'. Both cannot "
        "hold. Following the law contradicts the prompt; following the caption gives "
        "evaporation, not condensation. This is not repairable by rewriting the law alone -- the "
        "caption has to be changed to a cold window -- so exclude it (ids 100, 102, 103, 104 "
        "already cover the intended physics).",
  flags=['caption-law-conflict'])

# ---- Heat / Boiling (105, 106, 107, 108) ------------------------------
g([105, 106, 107, 108], 'ok',
  "At the boiling point vapour bubbles nucleate on the hottest surfaces -- the bottom and walls "
  "of the vessel -- then grow, detach, expand as they rise, and burst at the surface. The "
  "surface goes into continuous agitation, visible steam rises above it, and the level slowly "
  "drops as liquid leaves as vapour.",
  ["Bubbles form at the bottom and the heated walls, not in mid-liquid or at the surface.",
   "Bubbles rise upward, growing as they go, and burst at the surface.",
   "Bubble production ramps up as heating continues rather than starting at full intensity or "
   "dying away.",
   "The surface is in continuous agitation once boiling is established -- it does not stay flat "
   "and mirror-like while bubbles pour through it.",
   "Visible steam or vapour rises above the surface and disperses upward.",
   "The liquid level slowly drops as boiling continues; it does not rise or stay exactly fixed "
   "over a long boil.",
   "Bubbles do not appear before the vessel is heated, and they subside if the heat is removed.",
   "The liquid keeps its own colour and identity throughout; boiling agitates it but does not "
   "change what it is."])
o(106, add=["Milk's protein and fat skin traps the bubbles, so foam builds and climbs the wall "
            "as a rising head rather than bursting freely -- and it can boil over the rim, "
            "which plain water in the same vessel would not do."])
g([109], 'rewrite',
  "Cooking oil does not boil anywhere near 100 C -- its boiling point is several hundred degrees, "
  "well above its smoke point. Heated hot oil shimmers with convection and gives off a faint "
  "haze or smoke; it does not fill with rising bubbles. Bubbling and spitting in hot oil come "
  "from water contamination flashing to steam, not from the oil boiling.",
  ["The hot oil does not fill with a mass of rising vapour bubbles of its own.",
   "Convection is visible instead: the surface shimmers and streams, and suspended specks "
   "circulate.",
   "As it gets hotter a faint haze or wisps of smoke rise from the surface.",
   "Any bubbling is localised and violent -- spitting and popping where water has entered -- "
   "rather than a uniform rolling boil across the whole vessel.",
   "The oil darkens with prolonged heating rather than staying visually unchanged.",
   "The level does not drop the way a boiling aqueous liquid's does.",
   "Nothing happens before the vessel is heated, and the shimmer subsides when the heat is "
   "removed."],
  issue="Two faults. (1) The law is physically false: oil at 100 C is merely hot, so a clip "
        "showing oil in a vigorous rolling boil at 100 C would be marked CORRECT by this law "
        "and is in fact wrong -- the error runs in the dangerous direction. (2) The law's last "
        "clause says 'the coffee surface', a copy-paste artefact from a different caption. This "
        "is the single most consequential error we found in PhyGenBench; the caption's stated "
        "temperature also has to change, or the expected outcome has to become shimmer-and-smoke "
        "rather than boiling.",
  flags=['premise-implausible'])

# ---- Heat / deposition (110-114) --------------------------------------
g([110, 111, 112, 113, 114], 'rewrite',
  "Water vapour meeting a surface below freezing goes straight to solid ice: DEPOSITION, not "
  "sublimation (which is the reverse). Feathery, needle-like or dendritic frost crystals grow "
  "directly on the surface and spread from their nucleation points, with no liquid-droplet stage.",
  ["Frost forms on the cold surface itself, not in the air in front of it.",
   "The deposit is crystalline -- feathery, needle-like or branching -- not rounded liquid "
   "droplets.",
   "It grows outward from nucleation points and spreads across the surface, and the frosted "
   "area only increases while the surface stays below freezing.",
   "No liquid stage appears: there are no beads that later freeze, and nothing runs down under "
   "gravity.",
   "The frost sticks in place -- it does not slide, drip or flow.",
   "It forms on the face exposed to the humid air and follows that surface's shape, including "
   "vertical and overhanging parts, since it is not held on by gravity.",
   "It is opaque white and progressively obscures whatever is behind the surface.",
   "Nothing forms before the surface is cold, and the growth is one-directional while it stays "
   "cold."],
  issue="The verb is exactly backwards: sublimation is solid to gas, and vapour to solid is "
        "deposition. Five entries repeat the error. The physics of the outcome is right, and the "
        "genuinely valuable content -- crystalline frost with no droplet stage, which is the one "
        "discriminator against the Liquefaction group (ids 100-104) -- is not stated in the law "
        "at all.",
  flags=['mechanism-mislabelled'])
o(112, add=["A rainforest scene held below freezing is implausible on its own terms; judge the "
            "frost physics as shown, and treat the setting as the caption's business rather "
            "than a physics violation."],
  flags=['mechanism-mislabelled', 'premise-implausible'])

# ---- Heat / Sublimation (115, 117, 119) --------------------------------
g([115], 'ok',
  "Dry ice sublimes straight from solid to gas. The CO2 itself is invisible; what is seen is the "
  "white fog of ambient water vapour condensing in the cold gas. The block shrinks and leaves "
  "NO puddle, and the cold dense gas sinks and spreads along the ground.",
  ["The block visibly shrinks and its edges round off as it sublimes.",
   "White fog appears around and above the block while it shrinks.",
   "No liquid puddle forms: the surface under the block stays dry apart from condensation from "
   "the air, and no melt runs off the block.",
   "The fog is dense and cold, so it sinks and flows along the ground and over edges rather "
   "than rising like steam.",
   "The fog forms in the air near the block, not on the block's own surface as a coating.",
   "The fog disperses and thins away from the block as it warms and mixes.",
   "Frost or condensation appears on surfaces the block touches, since they are chilled below "
   "the dew point.",
   "The shrinking is one-directional -- the block never grows back."])
g([117], 'ok',
  "Iodine sublimes directly from crystals to a violet vapour with no liquid phase, and the "
  "vapour re-deposits as crystals on cooler surfaces above it.",
  ["Violet or purple vapour appears above the crystals as they are warmed.",
   "The crystals shrink as the vapour appears, and the two happen together.",
   "No liquid forms: no droplets, no pool, no wet residue under the crystals.",
   "The vapour is denser than air near the source, so it fills the vessel from the bottom "
   "upward rather than shooting away.",
   "The vapour thins and pales as it disperses, and it is darkest right above the crystals.",
   "Fresh crystals appear on the cooler upper surfaces where the vapour re-deposits.",
   "The crystals themselves keep their dark grey-violet metallic look; they do not turn liquid "
   "or change colour before vaporising.",
   "Nothing happens before warming begins."])
g([119], 'ok',
  "Arsenic trioxide sublimes on moderate heating, going from a white solid directly to a vapour "
  "with no liquid stage; the vapour is white and re-deposits as a white crust on cooler surfaces.",
  ["White vapour or fume rises from the solid as it is warmed.",
   "The solid shrinks as the vapour appears.",
   "No liquid forms: nothing melts, pools or runs.",
   "The vapour disperses and thins with distance from the source.",
   "A white deposit builds up on cooler surfaces above and around the solid.",
   "The solid stays white and powdery or crystalline throughout rather than darkening or "
   "changing texture.",
   "Nothing happens before heating begins, and the solid never grows back."],
  issue="Only the wording needs trimming: 'toxic' is not a visible property and must not become "
        "a rubric item. The visible physics -- white fume, shrinking solid, no liquid, "
        "re-deposition -- is correct as stated.")
g([116, 118], 'rewrite',
  "Both substances do sublime, but the law's evidence is an odour, which no video can show. The "
  "judgeable content is the solid shrinking and thinning with no liquid stage, no puddle, and "
  "faint vapour or haze near it, plus a white deposit re-forming on cooler surfaces.",
  ["The solid shrinks and its edges round and thin as it is warmed.",
   "No liquid appears at any point: no droplets on the solid, no pool beneath it, nothing runs.",
   "Faint vapour, shimmer or haze appears immediately above the solid rather than a dense plume.",
   "A thin white deposit builds up on nearby cooler surfaces.",
   "The shrinking is one-directional and gradual while warming continues.",
   "The solid keeps its own white waxy appearance and does not darken, char or slump.",
   "Nothing happens before warming begins."],
  issue="The stated evidence is non-visual: 'will emit a distinctive odor' (116) and 'will "
        "release its characteristic strong aroma' (118) cannot be checked from a video, so a "
        "rubric item derived from them is unjudgeable and would either be skipped or answered by "
        "guessing. Replace it with the shrinking-solid / no-liquid / re-deposition observables, "
        "which is what id 117 already does correctly.",
  flags=['non-visual'])
