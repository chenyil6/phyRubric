# ---- Light / Direct Radiation (40, 41, 44) ------------------------------
g([40, 41, 44], 'ok',
  "An opaque body in a beam blocks the light, so a shadow of its own outline falls on the "
  "surface beyond it, on the far side from the source and along the beam's direction.",
  ["A shadow is present on the surface beyond the object while the beam is on.",
   "The shadow lies on the opposite side of the object from the light source, never between "
   "them.",
   "Its outline matches the object's silhouette as seen from the source.",
   "Because the beam comes in diagonally, the shadow is stretched away from the source rather "
   "than sitting symmetrically under the object.",
   "The shadow moves and stretches consistently with the object and the source: if either "
   "moves, it tracks that movement; if both are still, it is still.",
   "The lit face of the object is the face turned toward the source, and the shadowed face is "
   "the one turned away.",
   "The shadowed region is darker than the surrounding lit surface, and it disappears if the "
   "beam is cut."])
g([43], 'rewrite',
  "A translucent plastic cup only partly blocks the beam: it casts a soft, incomplete shadow "
  "with light coming through it, brighter than the shadow of an opaque body, and the cup itself "
  "glows where the beam enters.",
  ["A shadow region is present beyond the cup, on the far side from the source.",
   "The shadow is partial rather than dark: light plainly passes through the cup, so its "
   "shadow is lighter than the shadow of an opaque object would be.",
   "The cup's wall glows where the beam enters it, and the light spreads within the wall.",
   "The shadow's outline follows the cup's silhouette but is soft-edged rather than sharp.",
   "The shadow lies away from the source along the beam and stretches because the beam is "
   "diagonal.",
   "Shadow and glow both vanish if the beam is cut."],
  issue="A plastic cup is translucent, not opaque. Stating flatly that the beam 'will be "
        "blocked' invites a rubric item that requires a full dark shadow and would fail a "
        "correct clip showing light passing through.")
g([42], 'rewrite',
  "A clear glass bottle transmits and refracts the beam rather than blocking it: the region "
  "beyond it is not a dark shadow but a faint outline crossed by bright concentrated bands "
  "(caustics), because the curved glass focuses the light that passes through.",
  ["Light plainly passes through the bottle: the region beyond it is not uniformly dark.",
   "Bright concentrated streaks or bands appear within or beside the bottle's outline on the "
   "surface -- brighter than the surrounding lit surface, not darker.",
   "Only the opaque parts (a label, a cap, thick seams) cast genuinely dark shadow.",
   "The bright bands and the faint outline lie away from the source along the beam and stretch "
   "because it is diagonal.",
   "The bottle's body lights up internally where the beam crosses it.",
   "Everything -- outline, caustics, internal glow -- vanishes if the beam is cut, and moves "
   "consistently if the bottle or the source moves."],
  issue="Glass is transparent. The law's claim that the light path 'will be blocked by the "
        "glass bottle' is false, and a verbatim rubric would reward a clip showing a solid dark "
        "shadow -- exactly the wrong physics. The distinctive correct signature is a bright "
        "caustic, not a shadow.")

# ---- Light / Tyndall Effect (45-54) ------------------------------------
g([45, 46, 47, 48, 49, 50, 51, 52, 53, 54], 'ok',
  "A beam crossing a medium full of suspended particles or droplets is scattered sideways along "
  "its path, so the beam itself becomes visible as a luminous line or cone from the side.",
  ["The beam is visible as a line or cone through the medium, not just as a spot where it "
   "lands.",
   "The visible path starts at the source's aperture and runs in a straight line in the "
   "direction the source is pointed.",
   "The path is only visible inside the scattering medium: it is fainter or absent in the clear "
   "air or clear liquid before and after it.",
   "The beam dims and spreads with distance into the medium as light is scattered out of it, "
   "rather than staying equally bright all the way through or brightening.",
   "The path moves with the source: aim the source elsewhere and the visible line follows "
   "immediately, keeping its straight geometry.",
   "The path vanishes when the source is switched off, and nothing glows in the medium without "
   "the beam.",
   "Where the beam meets a wall or the far side it makes a bright spot, and that spot lies on "
   "the beam's straight continuation."])
o(45, add=["Whole milk scatters strongly, so the beam penetrates only a short way into the "
           "glass and diffuses into a glow rather than crossing it cleanly."])
o(47, add=["Individual dust motes drifting through the beam glint as they cross it and go dark "
           "as they leave it."])
o(51, add=["Individual dust motes drifting through the beam glint as they cross it and go dark "
           "as they leave it."])
o(54, add=["Individual dust motes drifting through the beam glint as they cross it and go dark "
           "as they leave it."])
for _i in (45, 46, 47, 48, 49):
    o(_i, issue="The law itself is right. The caption is what over-claims: 'casting intricate "
                "patterns and subtle hues' is decoration -- Tyndall scattering gives a plain "
                "luminous path, not patterns or hues. Treat that phrase as a caption-adherence "
                "matter, and do not turn it into a physics requirement, or a correct clip showing "
                "a clean beam would be penalised for not inventing colours.")
o(52, add=["Smoke drifting across the beam distorts and thickens the visible path where it "
           "passes, and the path recovers when the smoke moves on."])

# ---- Light / Reflection (55-59) ----------------------------------------
g([55, 56, 57, 58, 59], 'rewrite',
  "A calm water surface acts as a plane mirror: it shows the object, the sky and the shore "
  "mirrored about the water plane -- upside down, moving in step with the original, and dimmer "
  "and tinted by the water. The mirror image is the same size as the object itself, but it lies "
  "farther from the camera along the light path, so on screen it appears equal or slightly "
  "smaller, never larger.",
  ["A reflection of the object is present in the water while the object is above it.",
   "The reflection is inverted -- mirrored about the water line, not a second upright copy.",
   "It moves in step with the object: same horizontal direction, same timing, no lag or "
   "independent drift.",
   "It appears equal in size or slightly smaller on screen, never larger than the object.",
   "It is dimmer and tinted by the water rather than as bright and crisp as the object itself.",
   "The sky and the surroundings are mirrored in the same water at the same time, consistently "
   "with the object's reflection.",
   "Ripples or disturbances break the reflection up where they pass and it re-forms as the "
   "water settles; a perfectly still reflection on visibly rippled water is wrong.",
   "The reflection shows the object's underside -- the face turned toward the water -- not the "
   "face turned toward the camera."],
  issue="'The same size as the original entities' is true of the virtual image in object space, "
        "but not of its apparent size on screen: the reflected ray path is longer than the "
        "direct one, so the reflection subtends a smaller angle. Taken verbatim as a rubric "
        "item it would fail a correct clip. The stronger, genuinely checkable claims -- "
        "inversion, synchronised motion, reduced brightness, break-up by ripples -- are absent "
        "from the law.")
g([60], 'ok',
  "A plane mirror forms an image the same size as the object, as far behind the mirror as the "
  "object is in front. As the object approaches, the image approaches from the other side at "
  "the same rate, so the gap between them closes at twice the object's speed and they meet at "
  "the surface.",
  ["An image of the object is present in the mirror throughout.",
   "It is the same size as the object and upright, not inverted.",
   "It moves toward the mirror as the object does, in step and at the same rate.",
   "The gap between object and image closes at twice the object's own speed, and they meet at "
   "the mirror's surface -- the image does not stop short of it or pass through.",
   "The image is left-right reversed relative to the object.",
   "The image's distance behind the mirror always matches the object's distance in front.",
   "The image is dimmer than the object but otherwise the same shape and colour."])
g([61, 63], 'ok',
  "A window pane and a polished metal surface both reflect part of the light that reaches them, "
  "so they carry an image of the approaching object -- fainter than a mirror's, and tinted by "
  "the surface, but with the same geometry: same size for a flat surface, approaching in step.",
  ["An image of the object is present in the reflecting surface throughout.",
   "It moves toward the surface as the object does, in step and at the same rate.",
   "It is upright and left-right reversed, not inverted.",
   "It is plainly fainter than the object, and tinted by the surface rather than a perfect copy.",
   "Its distance behind the surface matches the object's distance in front, so the two meet at "
   "the surface.",
   "If the reflecting surface is flat, the image is the same size as the object; if it is "
   "curved, the image is distorted and compressed consistently with that curvature.",
   "Whatever else faces the surface is reflected in it at the same time, consistently with the "
   "object's reflection."])
o(61, add=["Because the window is transparent, what is behind it is visible through the "
           "reflection at the same time."])
o(63, add=["The metal tints the reflection toward its own colour and blurs fine detail."])
g([62], 'rewrite',
  "What 'a standing glass' means decides the answer. A flat glass pane reflects an upright, "
  "same-size, left-right reversed image approaching in step. A drinking glass is a curved, "
  "part-filled body: its reflection is compressed and distorted, it is smaller than the object, "
  "and it is accompanied by refracted views of the car through the glass.",
  ["An image of the toy car is present in the glass throughout, moving toward it in step with "
   "the car.",
   "The image is upright rather than inverted.",
   "It is plainly fainter than the car itself, since only part of the light is reflected.",
   "If the glass is a flat pane, the image is the same size as the car and its distance behind "
   "the surface matches the car's distance in front.",
   "If the glass is a curved vessel, the image is compressed and distorted rather than a "
   "faithful same-size copy, and the distortion is consistent across the whole image.",
   "The car is also visible through the glass, refracted and displaced, at the same time as "
   "the reflection."],
  issue="The caption is ambiguous between a glass pane and a drinking glass, and the two give "
        "visibly different correct answers. The law's 'same size' claim only holds for a flat "
        "pane; applied to a drinking glass it would fail a correct clip.",
  flags=['outcome-uncertain'])
g([64], 'rewrite',
  "A duck already floating on the water cannot move closer to that surface. What is checkable "
  "is the reflection of a floating body: it is joined to the duck at the waterline, inverted "
  "below it, moves with it, and is broken up by the ripples the duck itself makes.",
  ["A reflection of the duck is present in the water beneath it.",
   "The reflection is inverted and joined to the duck at the waterline, with no gap between "
   "duck and image.",
   "It moves with the duck, in step and in the same horizontal direction.",
   "It is dimmer than the duck and tinted by the water.",
   "The duck's own ripples break the reflection up as they spread, and it re-forms as the water "
   "settles.",
   "The reflection shows the duck's submerged-facing side, not the face turned to the camera.",
   "The duck floats at a steady waterline while all this happens; it neither sinks nor lifts "
   "clear of the water."],
  issue="The caption's premise is incoherent -- a floating object is already at the surface, so "
        "'floating closer to a calm water surface' names no motion. The reflection geometry for "
        "a floating body is different from the airborne cases (55-59): image and object touch "
        "at the waterline.",
  flags=['premise-implausible'])

# ---- Light / Refraction (65-69) ----------------------------------------
g([65, 66, 67, 68, 69], 'rewrite',
  "A converging lens magnifies only while the object is inside its focal length. Held far from "
  "the page it forms a small INVERTED image; as it is brought closer the image grows and blurs "
  "through the focal distance, and only inside it does the familiar upright magnified view "
  "appear. Both regimes are correct physics.",
  ["Whatever is seen through the lens differs from what is seen beside it: the lens changes the "
   "view rather than acting as a plain window.",
   "Close in, the view through the lens is upright and larger than the same detail outside the "
   "lens rim.",
   "Held far off, the view through the lens is inverted and small -- this is correct, not a "
   "fault.",
   "The transition between the two is continuous: the image grows, blurs out near the focal "
   "distance, and flips; it does not jump between states.",
   "The magnification changes smoothly as the lens moves, and it changes in one direction while "
   "the lens moves in one direction.",
   "The magnified content matches the actual content underneath -- the same words, marks or "
   "patterns, enlarged, not different ones.",
   "The rim of the lens marks a sharp discontinuity: content jumps in scale across it, and the "
   "content just inside the rim connects to the content just outside.",
   "The lens's own outline and the hand holding it are not magnified."],
  issue="The law states only the end state. A physically faithful clip that starts with the "
        "lens far from the page shows a small inverted image first, which a verbatim rubric "
        "item ('should be bigger') would mark wrong. The focal-length regime change is the "
        "sharpest available discriminator and is missing from the law.")

# ---- Light / Refraction, submerged objects (70-74) ---------------------
g([70, 71, 72, 73, 74], 'ok',
  "Light from the submerged part of the object bends as it leaves the water, so that part "
  "appears displaced and raised relative to the part above: the object looks broken or kinked "
  "exactly at the water line, and the submerged part looks shallower and wider.",
  ["The object appears to change direction exactly at the water surface, not above or below it.",
   "The break appears only once the object is partly in the water, and it grows as more of the "
   "object goes in.",
   "The submerged part appears displaced sideways from the straight continuation of the part "
   "above, and appears shorter or raised rather than reaching as deep as it really does.",
   "The submerged part appears wider or magnified compared with the part in air.",
   "The apparent kink tracks the object: tilt or move it and the offset changes with it, "
   "vanishing when the object is vertical to the line of sight.",
   "The part above water is undistorted and continues in a straight line.",
   "The water surface also reflects: a partial mirror image of the object appears at the "
   "surface alongside the refracted view.",
   "Insertion disturbs the water -- ripples spread from the entry and the surface line "
   "wobbles, which makes the apparent break wobble with it."])
o(71, add=["The polished spoon also reflects its surroundings, so the refracted submerged bowl "
           "and the reflected room are both visible at once."])
o(73, add=["Each tine of the fork breaks at the same water line, all by the same offset and in "
           "the same direction."])
o(74, add=["The ruler's printed graduations let the offset be seen directly: the marks above "
           "and below the surface no longer line up."])

# ---- Light / Interference & Diffraction (75, 76, 80-84) ---------------
g([75, 76, 80, 81, 82, 83, 84], 'ok',
  "A film only a few wavelengths thick makes light reflected from its front and back surfaces "
  "interfere, so the colour seen depends on the local thickness and the viewing angle: swirling "
  "iridescent bands that shift as the film drains or as the view changes.",
  ["The colours appear as bands or swirls that vary across the film, not as one uniform tint.",
   "The colours shift when the film moves, drains or is seen from a different angle, rather "
   "than being painted on and fixed to the surface.",
   "The bands follow the film's thickness pattern and move with the film's flow, staying "
   "attached to the fluid rather than sliding across it.",
   "The palette is the iridescent sequence -- magenta, gold, cyan, green -- rather than "
   "arbitrary saturated colours.",
   "The colours are only present where the film is thin: thicker regions and the surrounding "
   "bulk liquid are colourless.",
   "The colours are a surface effect: what lies behind or under the film still reads through "
   "it.",
   "The effect requires light: it dims with the light and vanishes in shadow."])
o(82, add=["As the soap film on the wand drains, it thins at the top, so the bands migrate "
           "downward and the top eventually goes colourless or black before the film breaks.",
           "The film bursts irreversibly: it does not re-form once broken."])
o(75, add=["Each bubble carries its own independent pattern, and the pattern moves and rotates "
           "with that bubble.",
           "A bubble that bursts disappears entirely and does not re-form."])
o(76, add=["The coloured patches spread and are carried by the water's surface flow, changing "
           "shape as they go."])
o(80, add=["The coloured bands lie on the puddle's surface and are broken up by ripples, "
           "re-forming as the surface settles."])
g([79], 'rewrite',
  "This is dispersion, not interference: a prism splits white light by wavelength, throwing an "
  "ordered spectrum -- red through violet in sequence -- onto whatever the light lands on. The "
  "prism's own glass is not itself coloured.",
  ["A spectrum appears where the transmitted light lands, not on the prisms themselves.",
   "The colours are in the ordered sequence red-orange-yellow-green-blue-violet, adjacent and "
   "in that order, rather than a random scatter of hues.",
   "The spectrum lies on the far side of the prism from the source, along the deviated beam.",
   "Each spectrum tracks the prism that made it: rotate or move a prism and its spectrum "
   "sweeps accordingly.",
   "The spectra vanish when the light is cut, and no colour is emitted in the dark.",
   "The light entering the prism is white and the light leaving it is dispersed; the prism does "
   "not brighten or add light."],
  issue="Mechanism mislabelled. Prism colour is dispersion (wavelength-dependent refraction), "
        "not thin-film interference; a prism has no thin film. As written this entry also "
        "duplicates the Dispersion group (id 85). The observable signature differs sharply: "
        "dispersion gives an ordered spectrum cast onto a surface, interference gives swirling "
        "bands on the film itself.",
  flags=['mechanism-mislabelled', 'duplicate'])
g([77], 'exclude',
  "Solid glass marbles have no thin film, so interference and diffraction produce nothing here. "
  "What sunlight on glass marbles actually gives is bright focused caustics on the floor around "
  "them, specular sparkle, plus whatever colour the glass itself is dyed.",
  ["Bright concentrated caustic patches appear on the floor near each marble, on the far side "
   "from the sun.",
   "The marbles carry small sharp specular highlights positioned consistently with the sun.",
   "Any colour in a marble is its own dye, fixed to the marble and unchanged by the viewing "
   "angle -- not a shifting iridescence.",
   "Caustics and highlights move consistently if the marbles or the light move, and vanish in "
   "shadow."],
  issue="The law is false: 'due to interference & diffraction, the marbles will be colorful' "
        "names a mechanism that does not operate on solid glass spheres. A verbatim rubric item "
        "would demand iridescent marbles and reward a clip that invents them. If this prompt is "
        "kept it must be relabelled as caustics/specular reflection with the 'colorful' claim "
        "dropped; we recommend excluding it instead, since the caption asks for nothing else.")
g([78], 'exclude',
  "Mist droplets are far larger than the wavelength of light, so they scatter it almost "
  "independently of wavelength: mist looks white or grey, not colourful. Colour appears only "
  "in specific geometries (a rainbow with the sun behind the viewer, a corona around the sun), "
  "which the caption does not set up.",
  ["The suspended mist reads white or grey and bright where the sun strikes it, without "
   "intrinsic colour.",
   "Sunlight through the mist makes visible beams and shafts rather than coloured particles.",
   "Any coloured arc, if present, is a single ordered bow positioned opposite the sun -- not "
   "colour spread over the particles themselves.",
   "The brightness follows the sun's direction and vanishes in shadow."],
  issue="The law is false: individual mist particles are not coloured by interference or "
        "diffraction. A verbatim rubric would require rainbow-coloured mist and reward a clip "
        "that renders it. There is no way to keep the law's claim; the honest options are to "
        "exclude the prompt or to rewrite the prompt itself as a rainbow scene with the sun "
        "behind the camera.")

# ---- Light / Dispersion (85-88) ----------------------------------------
g([85, 86, 87, 88], 'ok',
  "A transparent body with flat or curved faces refracts short wavelengths more than long ones, "
  "so white light entering it leaves separated by colour: an ordered spectrum, red through "
  "violet, cast wherever the emerging light lands.",
  ["An ordered spectrum appears -- red, orange, yellow, green, blue, violet, adjacent and in "
   "that sequence, not a random scatter of hues.",
   "The spectrum appears on the far side of the body from the source, along the path of the "
   "deviated light.",
   "The light entering is white and only the light leaving is separated; the body does not emit "
   "light of its own.",
   "The spectrum tracks the geometry: move or turn the body, or the source, and the spectrum "
   "sweeps accordingly and keeps its colour order.",
   "The spectrum vanishes when the source is cut, and nothing glows in the dark.",
   "The body's own material stays its own colour and is not itself rainbow-tinted.",
   "The spectrum's colours stay in fixed order relative to one another; they do not shuffle "
   "between frames."],
  issue="Only the wording needs care: nothing 'emits' multicoloured light. The incoming white "
        "light is separated by wavelength and the spectrum lands on a surface beyond the body. An "
        "item phrased as emission would accept a prism glowing with colour of its own, which is "
        "the usual failure mode here, and would not ask for the ordered red-to-violet sequence "
        "that is the real signature.")
o(86, add=["A chandelier's many facets throw many separate spectral flecks around the room, "
           "each one an ordered little spectrum, and they sweep together if the chandelier "
           "turns."])
o(87, add=["A single droplet both disperses and refocuses the light, so the colours appear as a "
           "small bright fan or arc rather than a long spread band."])
o(88, add=["Glass has weaker dispersion than real diamond, so the spectral flecks are present "
           "but less vivid than a diamond's fire; strong ordered spectra are still expected."])
g([89], 'rewrite',
  "Soap-bubble colour is thin-film interference, not dispersion: the film's own surface carries "
  "swirling iridescent bands whose colours depend on local thickness and viewing angle. No "
  "spectrum is cast anywhere.",
  ["The colours appear on the bubble's own surface, as bands or swirls, not as a spectrum cast "
   "onto a surface beyond it.",
   "The colours vary across the bubble and shift as it moves, rotates or drains.",
   "The palette is iridescent -- magenta, gold, cyan, green -- rather than an ordered "
   "red-to-violet sequence in a line.",
   "The pattern is attached to the film and travels with it rather than sliding across a still "
   "surface.",
   "What is behind the bubble still reads through it.",
   "The bubble bursts irreversibly and does not re-form."],
  issue="Mechanism mislabelled: a soap film is a few hundred nanometres thick and its colour "
        "comes from interference between reflections at its two surfaces, not from wavelength "
        "separation in a bulk medium. The two mechanisms have visibly different signatures -- "
        "an ordered cast spectrum versus swirling bands on the object -- so a verbatim "
        "dispersion rubric would look for the wrong thing. This entry also duplicates the "
        "interference group (ids 75, 81).",
  flags=['mechanism-mislabelled', 'duplicate'])
