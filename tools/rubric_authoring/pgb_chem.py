# ---- Chemical / Acidity and Alkalinity (145, 146) ---------------------
g([145, 146], 'ok',
  "Purple litmus is an acid-base indicator: added acid drops the pH and turns it red. The change "
  "starts where the acid enters, spreads with the mixing, and ends with the whole solution red.",
  ["The solution's colour changes from purple to red.",
   "The change begins where the acid enters and spreads outward with the mixing flow, rather "
   "than the whole glass switching colour in one frame.",
   "Streaks of purple survive in between and are gradually consumed, ending with a uniform red.",
   "The final colour is uniform, with no purple layer or pocket left.",
   "The change is irreversible: it does not drift back to purple on its own.",
   "The added liquid is itself colourless, so the new colour comes from the indicator, not from "
   "pouring in something red.",
   "The level rises by the amount added.",
   "Nothing else happens that the chemistry does not call for -- no bubbling, no precipitate, no "
   "heat haze."])
o(146, add=["More acid deepens the red rather than reversing it, and the colour saturates once "
            "the indicator has fully turned."])
g([147], 'rewrite',
  "Soda water is carbonated water -- dissolved CO2 forms carbonic acid, so it is acidic. Blue "
  "litmus therefore turns red or pink, and CO2 bubbles come out of solution as well.",
  ["The blue litmus solution turns red or pink; it does not remain blue.",
   "The change begins where the soda water enters and spreads with the mixing.",
   "Streaks of blue persist during mixing and are consumed, ending in a uniform colour.",
   "Bubbles form and rise to the surface as dissolved CO2 escapes, and the fizzing subsides over "
   "time rather than continuing forever.",
   "The added liquid is colourless, so the colour change comes from the indicator.",
   "The colour change is irreversible over the shot, though it may pale slightly as CO2 escapes.",
   "The level rises by the amount added."],
  issue="Factually wrong: 'the solution color remains blue' would only hold for a neutral or "
        "basic addition. Carbonated water has a pH around 3-4 and turns blue litmus red. A "
        "verbatim rubric would mark a physically correct clip WRONG and reward a clip in which "
        "nothing happens -- the easiest possible thing for a video model to produce, so this "
        "error is actively harmful as a benchmark item.")
g([148], 'rewrite',
  "Red cabbage juice is an anthocyanin indicator, not a base. Lemon juice acidifies it, shifting "
  "it from purple toward pink or red. There is no acid-base neutralisation and NO gas is "
  "released.",
  ["The cabbage juice shifts from purple toward pink or red.",
   "The shift begins where the lemon juice enters and spreads with the mixing.",
   "No bubbles or fizzing appear: nothing gaseous is produced.",
   "No precipitate forms and the liquid stays a liquid throughout.",
   "Streaks of the original colour persist during mixing and are consumed, ending uniform.",
   "The change is irreversible on its own over the shot.",
   "The level rises by the amount added.",
   "The final colour is intermediate and consistent with dilution -- it does not become more "
   "vivid than either starting liquid."],
  issue="Two errors. 'Acid and base reaction' is wrong -- cabbage juice is an indicator, and "
        "mixing it with lemon juice is an indicator colour shift, not neutralisation. 'Release of "
        "gases' is wrong outright: nothing here produces gas. A verbatim rubric would reward a "
        "clip that invents fizzing, which is exactly the sort of plausible-looking hallucination "
        "the benchmark exists to catch.")
g([149], 'ok',
  "Citric acid in the juice reacts with sodium bicarbonate to release carbon dioxide, so the "
  "mixture fizzes: bubbles nucleate on the powder, foam builds and rises, and the reaction dies "
  "away as one reactant is used up.",
  ["Bubbles appear and rise to the surface once the baking soda meets the juice.",
   "Bubbling starts at the powder itself and where it lands, not uniformly throughout the liquid.",
   "Foam builds on the surface and can rise up the cup, potentially overflowing.",
   "The fizzing is most vigorous just after mixing and then subsides as the reactants are "
   "consumed; it does not continue undiminished or start late for no reason.",
   "The powder visibly dissolves and disappears as it reacts.",
   "Bubbles rise upward and burst at the surface; none sink.",
   "The reaction is irreversible -- the foam collapses to liquid and the powder does not "
   "re-form.",
   "The liquid keeps the juice's own colour; the foam is a paler version of it, not a new "
   "colour."])

# ---- Chemical / Dehydration property (150-153) ------------------------
g([150, 151, 152, 153], 'ok',
  "Concentrated sulfuric acid strips water out of a carbohydrate and leaves carbon behind, so "
  "the material darkens, blackens, chars and shrinks exactly where the acid wetted it, with heat "
  "and fumes -- and the change is irreversible.",
  ["Darkening starts exactly where the acid landed and spreads outward from there as it soaks in.",
   "The colour progresses through yellowing and browning to black rather than jumping straight "
   "to black.",
   "The wetted material shrinks, wrinkles and slumps as it chars.",
   "Fumes or vapour rise from the reacting area, driven by the heat released.",
   "Parts of the object the acid never reached stay unchanged in colour and shape.",
   "The change is irreversible: the charred region does not lighten or recover.",
   "The reaction stays localised to the wetted region and its spreading edge -- it does not "
   "consume the whole object instantly.",
   "The acid runs and pools under gravity, and the charring follows where it flows."],
  issue="Only a wording trim: 'releasing large amounts of acidic gas' has a non-visible clause. "
        "Keep the visible fume/vapour and drop the chemical identification, which a video cannot "
        "show.")
o(150, add=["Bread's porous crumb soaks the acid up and spreads the charring through the "
            "structure, so the blackening runs deeper than the surface."])
o(151, add=["The apple's water content makes the reaction wetter: it releases liquid, bubbles at "
            "the surface, and the flesh collapses as it blackens."])
o(153, add=["Cotton fibres blacken and the ball collapses from a fluffy mass to a small dark "
            "clump."])
g([154], 'rewrite',
  "The outcome depends on what the sponge is made of, and the law does not say. A cellulose "
  "sponge dehydrates and chars black like the other four; a synthetic polyurethane sponge -- the "
  "common kitchen kind -- is attacked, discoloured, softened and dissolved instead, without the "
  "clean carbonisation.",
  ["Change starts exactly where the acid landed and spreads outward from there.",
   "The wetted region shrinks and collapses as it is attacked.",
   "Whichever path is shown is shown consistently: charring to black for a cellulose sponge, or "
   "yellowing, softening and dissolving for a synthetic one -- not a mixture of the two.",
   "Fumes or vapour rise from the reacting area.",
   "Untouched parts of the sponge stay unchanged.",
   "The damage is irreversible and does not recover.",
   "The acid runs and pools under gravity, and the damage follows where it flows."],
  issue="The dehydration/carbonisation claim is material-specific, and 'a sponge' is ambiguous "
        "between cellulose and polyurethane. A verbatim rubric demanding black carbonisation "
        "would fail a correct clip of a plastic sponge. Either pin the material in the caption or "
        "judge internal consistency, as above.")

# ---- Chemical / Redox property (155, 156) -----------------------------
g([155, 156], 'ok',
  "Iron and steel oxidise in the presence of water and oxygen, so rust forms: orange-brown "
  "patches appear at edges, scratches and low points where water lingers, spread outward, and "
  "roughen and flake the surface. The process only ever advances.",
  ["Orange-brown rust appears on the metal and grows over the timelapse.",
   "It starts at edges, corners, scratches and places where water sits, then spreads over the "
   "flat surface.",
   "The rusted area only ever grows -- it never shrinks or reverts to bare metal.",
   "The surface loses its shine progressively, becoming dull and then rough.",
   "The rust roughens, blisters and flakes, so the surface texture changes rather than just its "
   "colour.",
   "The colour progression runs through dull grey and light brown before deep orange-brown; it "
   "does not jump straight to heavy rust in one frame.",
   "The object keeps its overall shape and position: rust corrodes and pits it but does not make "
   "it move, grow or change form.",
   "Rust stains run downward from the corroded areas, following where water drains."])
g([157, 158, 159], 'rewrite',
  "'Metal will rust' is over-general: rusting is specific to iron and steel. Aluminium, copper, "
  "brass, zinc and stainless steel corrode differently -- dull grey oxide, green patina, white "
  "powder -- or barely at all. The law should either name a ferrous object or accept the "
  "corrosion product appropriate to whatever metal is shown.",
  ["The metal surface corrodes progressively over the timelapse rather than staying pristine.",
   "The corrosion product matches the metal shown: orange-brown flaking rust for iron or steel, "
   "grey or white dull oxide for aluminium and zinc, green patina for copper or brass.",
   "It starts at edges, joints, scratches and places where water lingers, then spreads.",
   "The corroded area only ever grows; it never reverts to bright metal.",
   "The shine is lost progressively, and the surface roughens, pits or flakes.",
   "The colour progression is gradual, not a single jump to a fully corroded state.",
   "The object keeps its shape and position, corroding in place.",
   "Stains run downward from the corroded areas, following how the rain drains."],
  issue="The caption says only 'metal' -- a chair, a railing, a bedframe -- and the law asserts "
        "that metal rusts. Rust is iron oxide; a correct clip showing an aluminium railing "
        "developing dull grey oxide would be marked wrong, and a clip showing bright orange rust "
        "on obviously anodised aluminium would be marked right. Ids 155 and 156 already cover "
        "the ferrous case properly, so the value of these three is exactly the generality that "
        "makes them wrong.")
