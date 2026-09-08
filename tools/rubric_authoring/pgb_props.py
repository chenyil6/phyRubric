# ---- Physical Properties / Color (120, 121, 122, 124) ------------------
g([120, 121, 122, 124], 'ok',
  "Paints mix subtractively: each pigment removes part of the spectrum, so the blend takes an "
  "intermediate hue between its parents and is never more saturated or brighter than both of "
  "them. Red+blue gives purple, yellow+red orange, green+blue teal, and adding white lightens "
  "toward a pale tint.",
  ["The final colour is the stated one and lies between the two parent hues, not outside their "
   "range.",
   "The blend appears progressively as stirring proceeds rather than switching to the final "
   "colour in one frame.",
   "Streaks and swirls of the unmixed parent colours are visible during stirring and disappear "
   "as it homogenises.",
   "The parent colours are consumed as the blend forms: no untouched pool of pure parent colour "
   "survives once it is 'fully blended'.",
   "The blend is uniform at the end -- no residual banding or separated layers.",
   "The result is equal to or darker and duller than the parents, never brighter or more vivid "
   "than both of them.",
   "The colour change is irreversible: the mixture does not un-mix back into two colours.",
   "The total volume is the sum of the two, and it does not shrink or grow during stirring."])
o(124, add=["This is the one case where the blend is lighter than one parent: white lightens the "
            "pink toward a pale tint, and the result stays in the same hue family rather than "
            "shifting toward another colour."])
o(120, add=["Real red and blue paint give a dark, somewhat muddy purple rather than a vivid "
            "spectral violet; a dull result is correct here, not a fault."])
g([123], 'rewrite',
  "Cyan and magenta are subtractive primaries: cyan absorbs red, magenta absorbs green, so what "
  "is left is BLUE. The blend is bluer than the magenta and darker than either parent -- not the "
  "red-leaning purple the law names.",
  ["The final colour is blue or blue-violet, clearly bluer than the magenta it came from.",
   "It is not a red-leaning purple or a magenta-dominated violet.",
   "The blend appears progressively as stirring proceeds, with parent streaks visible in "
   "between.",
   "It is darker and duller than either parent, never brighter than both.",
   "Both parent colours are consumed; no pure cyan or pure magenta pool survives at the end.",
   "The end state is uniform, with no banding or layering.",
   "The change is irreversible -- the mixture does not separate back into cyan and magenta."],
  issue="Subtractive mixing of cyan and magenta yields blue. Labelling the target 'purple' is "
        "loose enough that a clip producing a red-violet -- which would require a red-absorbing "
        "failure -- would pass. Since the whole point of this sub-category is the specific hue, "
        "the target has to be stated correctly.")

# ---- Physical Properties / Flame Reaction (125-129) --------------------
g([125, 126, 127, 128, 129], 'ok',
  "Each metal's electrons emit at characteristic wavelengths when excited in a flame, so the "
  "flame takes that element's own colour, independent of the fuel: copper green, magnesium "
  "brilliant white, lithium crimson, sodium yellow-orange, potassium pale lilac.",
  ["The flame's colour is the one characteristic of that metal.",
   "The colour is in the flame itself and around the burning metal, not painted on the solid.",
   "The colour stays the same as long as the metal keeps burning, rather than cycling through "
   "unrelated hues.",
   "The flame casts light of its own colour on nearby surfaces.",
   "The flame rises and flickers upward, and is anchored to the burning metal.",
   "The metal is consumed as it burns -- it darkens, shrinks or leaves a residue -- rather than "
   "staying pristine.",
   "The flame goes out when the metal is used up, and nothing burns before ignition."])
o(125, add=["Bulk copper metal does not actually ignite; flame-test green comes from copper "
            "compounds or fine powder in an existing flame. Judge the flame colour as shown and "
            "treat the implausible ignition as the prompt's own premise."],
  flags=['premise-implausible'],
  issue="The colour claim is right, but the caption's setup cannot happen: a piece of copper "
        "will not catch fire. The other four metals in the group do burn, so only this prompt "
        "needs the caveat.")
o(126, add=["Magnesium burns dazzlingly bright -- bright enough to wash out the exposure -- and "
            "leaves a white powdery ash."])
o(128, add=["Sodium melts into a ball as it burns, and the yellow-orange is intense enough to "
            "dominate the whole scene's colour."])
o(129, add=["Potassium reacts vigorously and the lilac is pale and easily swamped by the yellow "
            "of any sodium contamination."])

# ---- Physical Properties / Hardness (130-133) --------------------------
g([130, 131, 132, 133], 'ok',
  "A brittle body thrown hard at a rigid surface cannot absorb the impact by deforming, so it "
  "fractures at the point of contact. What matters is brittleness plus the target's rigidity and "
  "the impact speed, not 'hardness' as such -- the target survives essentially undamaged while "
  "the projectile does not.",
  ["The thrown object breaks on impact rather than bouncing off intact or sticking to the "
   "surface.",
   "It breaks at the moment and place of contact, not before it lands or well afterwards.",
   "Fragments and contents fly outward from the impact point, away from the surface, and then "
   "fall under gravity.",
   "The target surface is left essentially undamaged; the projectile takes all the destruction.",
   "The breakage is irreversible: fragments do not reassemble, and the object does not re-form.",
   "The object travels along a ballistic path before impact -- it does not hover, slow in "
   "mid-air, or change direction on its own.",
   "The debris comes to rest on the ground or on the surface and stays there.",
   "The number and spread of fragments is consistent with the impact: a hard throw gives many "
   "fragments thrown wide, not a single neat crack."])
o(130, add=["An egg's shell fragments and the yolk and white splatter, then run downward under "
            "gravity and cling to the rock in streaks."])
o(132, add=["Glass shatters into many small shards that scatter widely and catch the light."])
g([134], 'rewrite',
  "Wood is not hard -- it is softer than porcelain. The plate still shatters, but because it is "
  "brittle and the impact is fast and the table is rigid enough not to give way, not because the "
  "wood out-ranks it in hardness. The wooden table may well be dented or scratched, unlike stone "
  "or concrete.",
  ["The porcelain plate breaks on impact rather than bouncing off intact.",
   "It breaks at the moment and place of contact.",
   "Fragments fly outward from the impact point and then fall under gravity.",
   "The table survives as a table: it may be scuffed, dented or scratched, but it does not "
   "shatter or break through.",
   "The breakage is irreversible; fragments do not reassemble.",
   "The plate follows a ballistic path before impact.",
   "The debris comes to rest and stays put."],
  issue="'The hardness of the wood is very high' is simply false -- wood is far softer than "
        "porcelain, and the sibling entries use stone, concrete and metal precisely because they "
        "are rigid. The outcome (the plate breaks) is still right, so the fix is to the stated "
        "mechanism and to what the target is allowed to look like afterwards.")

# ---- Physical Properties / Solubility (135, 139) -----------------------
g([135, 139], 'ok',
  "Oil and water-based liquids do not mix, so they separate into layers ordered by density with "
  "a visible interface: oil (lighter) on top, the aqueous liquid (heavier) underneath, whichever "
  "one is poured in.",
  ["The two liquids end up as two distinct layers with a visible boundary between them.",
   "The oil is the upper layer and the aqueous liquid the lower one, regardless of which was "
   "poured into which.",
   "The poured liquid travels to its own layer: it does not stay where it landed if that is the "
   "wrong side of the interface.",
   "Pouring disturbs the mixture and drives droplets across the interface, and those droplets "
   "then rise or sink to rejoin their own layer.",
   "Droplets of one liquid inside the other stay as rounded blobs with sharp edges rather than "
   "diffusing into a gradient.",
   "The interface settles to a flat, level line once the disturbance dies down.",
   "Neither liquid loses its own colour or clarity to the other -- no uniform blend appears.",
   "The total level rises by the amount added, and each layer's thickness matches how much of "
   "that liquid is present."])
o(135, add=["Oil poured into water sinks momentarily as a stream, then breaks into globules that "
            "rise and coalesce into a film on top."])
o(139, add=["Vinegar is denser than oil, so it sinks through the oil in droplets that gather "
            "into a layer at the bottom -- the poured liquid ends up underneath, which is the "
            "opposite of the intuitive 'poured-in liquid floats' reading."])
g([137, 138], 'ok',
  "Both poured liquids are water-based and fully miscible, so they mix: streaks and plumes spread "
  "from the point of entry, then diffuse and stir into one uniform liquid with no interface and "
  "no layers.",
  ["The two liquids end up as one uniform liquid with no visible boundary or layers.",
   "Mixing starts at the point of entry and spreads outward as plumes and streaks.",
   "The streaks fade progressively into uniformity rather than snapping to a finished state or "
   "persisting indefinitely once disturbed.",
   "No rounded droplets with sharp edges persist -- anything poured in dissipates instead of "
   "holding its shape.",
   "The final liquid's appearance is intermediate between the two, not identical to just one of "
   "them.",
   "The level rises by the amount added.",
   "The mixing is irreversible: the uniform liquid does not separate back into two components.",
   "The flow follows gravity and the pour -- it enters from above and sinks or spreads, and "
   "circulation dies down as the liquid comes to rest."])
o(138, add=["The juice's colour makes the mixing directly visible: coloured plumes sink and "
            "spread, then the whole glass takes an intermediate, weaker colour."])
o(137, add=["Vinegar and water are both clear, so the only visible sign of mixing is faint "
            "refractive shimmer and the flow it induces; there is no colour change to watch."],
  flags=['low-visibility'],
  issue="The law is correct but nearly unjudgeable on video: clear liquid into clear liquid "
        "produces almost no visible evidence either way, so a rubric built on it can be "
        "satisfied by a static shot. Worth keeping only as a weak item, or dropping in favour of "
        "id 138.")
g([136], 'rewrite',
  "Honey is a concentrated sugar solution and IS water-soluble, so it does not stay immiscible "
  "with milk. Because it is much denser and far more viscous, it sinks as thick ropes and forms "
  "a temporary bottom layer, then dissolves into the milk given time or stirring -- density "
  "layering, not immiscibility.",
  ["The honey sinks through the milk rather than floating or staying where it was poured.",
   "It falls as a thick, coherent rope or column that keeps its shape briefly, reflecting its "
   "high viscosity, instead of dispersing at once.",
   "It gathers into a distinct layer at the BOTTOM of the glass.",
   "That layer is temporary: its edges blur and it thins and dissolves into the milk over time, "
   "faster with stirring -- it does not stay a permanent sharp-edged layer.",
   "There is no clean flat oil-and-water style interface that persists indefinitely.",
   "The milk near the honey takes on the honey's tint as it dissolves.",
   "The level rises by the amount poured.",
   "The dissolution is irreversible: once mixed, the honey does not re-separate into a layer."],
  issue="'Due to immiscibility, honey and milk cannot dissolve each other' is false: honey is "
        "sugar in water and dissolves fully in an aqueous liquid. A verbatim rubric would demand "
        "a permanent interface and would penalise the correct behaviour (sinking rope, temporary "
        "bottom layer, eventual dissolution). The layering is real but it is a density and "
        "viscosity effect, and it is transient.")

# ---- Physical Properties / Combustibility (141, 142, 144) -------------
g([141, 142, 144], 'ok',
  "A burning object landing on dry, finely divided fuel ignites it where it touches. The flame "
  "front then spreads outward from that point and grows as it recruits more fuel, consuming it "
  "to ash irreversibly while smoke rises.",
  ["Ignition starts where the burning object lands and touches the pile, not elsewhere or all "
   "over at once.",
   "The flame front spreads outward from the ignition point across the pile.",
   "The fire grows over time as it recruits more fuel, rather than staying the same size as the "
   "small burning object or shrinking straight away.",
   "Smoke is produced and rises upward, drifting with the air.",
   "The fuel is consumed: it blackens, curls, shrinks and is left as ash and char.",
   "Burnt fuel stays burnt -- consumed material does not return, and the fire does not run "
   "backwards.",
   "Flames point upward regardless of how the pile is oriented, and lean with any draught.",
   "Unburnt fuel outside the flame front stays unchanged until the front reaches it."])
o(141, add=["Leaves curl and darken just ahead of the flame front, before the flame itself "
            "arrives."])
g([140], 'rewrite',
  "The caption's fuel is paper, not wood: a burning ball of paper thrown into a pile of dry paper "
  "ignites the paper, and paper's thin sheets catch and spread fast, curling and blackening ahead "
  "of the flame front and collapsing into light ash.",
  ["Ignition starts where the burning ball lands in the pile.",
   "The flame front spreads outward from there across the paper and grows.",
   "Individual sheets curl, darken and blacken just ahead of the flame, then flare and collapse.",
   "The fire spreads quickly, as thin paper does, rather than smouldering like a solid log.",
   "Smoke rises upward, and light ash can be carried up by the hot draught.",
   "The paper is consumed to fragile ash that keeps the sheets' shapes until disturbed.",
   "The burning is irreversible: consumed paper does not return.",
   "Unburnt sheets away from the front stay unchanged until it reaches them."],
  issue="Object mismatch: the law says 'combustibility of wood, the wood will be ignited' while "
        "the caption contains no wood at all -- it is paper into paper, apparently a copy-paste "
        "from a different prompt. Wood and paper also burn visibly differently (slow charring "
        "and embers versus fast flare and light ash), so the substitution is not harmless.",
  flags=['object-mismatch'])
g([143], 'rewrite',
  "A lit candle thrown through the air will usually be blown out by its own motion, so the "
  "expected outcome is not a certainty. What can be judged is internal consistency: if the flame "
  "survives the throw, the dry grass ignites where it lands and the fire spreads and grows; if "
  "the flame goes out in flight, nothing ignites -- and either is correct, but not both at once.",
  ["Whether the candle is still lit when it lands is shown consistently, and the outcome follows "
   "from it: a lit candle ignites the grass, an extinguished one does not.",
   "The candle follows a ballistic path, and the flame -- if it survives -- is deflected "
   "backwards by the motion rather than standing straight up.",
   "If ignition occurs, it starts where the candle lands and the flame front spreads outward "
   "from there and grows.",
   "Smoke is produced and rises upward.",
   "Burning grass blackens, curls and is consumed to ash, irreversibly.",
   "A flame that has visibly gone out does not re-light on its own.",
   "Unburnt grass away from the front stays unchanged until it reaches it."],
  issue="Mandating that the grass 'will be ignited' penalises the most likely real outcome -- a "
        "thrown candle is extinguished in flight. Rewriting the target as internal consistency "
        "keeps the entry usable and, unlike the original, cannot be satisfied by a clip that "
        "shows an obviously extinguished candle setting a field alight.",
  flags=['outcome-uncertain'])
