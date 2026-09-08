# ============ Direct radiation: opaque bodies (40, 41, 44) ==============
for i, obj in [(40, 'wooden block'), (41, 'metal can'), (44, 'cardboard box')]:
    add('shadow-casting', i,
        f'A diagonal beam lights a {obj} in the dark and it casts a shadow.',
        S(('core', f'A {obj} is present in an otherwise dark scene.'),
          ('core', 'A beam of light shines on it diagonally.'),
          ('core', 'A shadow of the object appears on the surface beyond it.'),
          ('minor', 'The scene is dark apart from the beam and what it lights.')),
        P(('fatal', 'A shadow is present on the surface beyond the object while the beam is on.',
           'no shadow appears anywhere although a beam plainly strikes an opaque object'),
          ('core', 'The shadow lies on the opposite side of the object from the light source, '
                   'never between them.',
           'the shadow falls on the source side of the object, between object and light'),
          ('core', "Its outline matches the object's silhouette as seen from the source.",
           "the shadow's outline does not correspond to the object's shape"),
          ('major', 'Because the beam comes in diagonally, the shadow is stretched away from the '
                    'source rather than sitting symmetrically under the object.',
           'the shadow sits directly and symmetrically beneath the object although the beam is '
           'plainly slanted'),
          ('major', 'The lit face of the object is the face turned toward the source, and the '
                    'shadowed face is the one turned away.',
           'the face turned away from the source is the bright one'),
          ('minor', 'The shadow moves consistently with the object and the source: if either '
                    'moves it tracks that movement, and if both are still it is still.',
           'the shadow drifts, stretches or swings while object and source are both stationary'),
          ('minor', 'The shadowed region is darker than the surrounding lit surface, and it '
                    'disappears if the beam is cut.',
           'the shadow is as bright as the lit surface, or it survives the beam being cut')))

# ============ Direct radiation: translucent cup (43) ====================
add('shadow-casting', 43,
    'A diagonal beam lights a translucent plastic cup: light comes through and the shadow is '
    'partial.',
    S(('core', 'A plastic cup is present in an otherwise dark scene.'),
      ('core', 'A beam of light shines on it diagonally.'),
      ('core', 'A shadow of the cup appears on the surface beyond it.'),
      ('minor', 'The scene is dark apart from the beam and what it lights.')),
    P(('fatal', 'A shadow region is present beyond the cup, away from the source, while the '
                'beam is on.',
       'no shadow region appears at all although a beam plainly strikes the cup'),
      ('core', 'Light plainly passes through the cup, so its shadow is partial rather than dark '
               '-- lighter than the shadow an opaque object would cast.',
       'the cup casts a solid dark shadow with no light coming through it'),
      ('core', 'The shadow lies away from the source, and the cup\'s lit face is the one turned '
               'toward the source.',
       'the shadow falls between cup and light, or the face turned away from the source is the '
       'bright one'),
      ('major', "The cup's wall glows where the beam enters it, and the light spreads within "
                "the wall.",
       'the wall stays dark where the beam strikes it, showing no glow at all'),
      ('major', "The shadow's outline follows the cup's silhouette but is soft-edged rather "
                "than razor sharp.",
       "the shadow's outline is unrelated to the cup's shape, or is as hard-edged as an opaque "
       "object's"),
      ('minor', 'Because the beam comes in diagonally, the shadow is stretched away from the '
                'source rather than sitting symmetrically under the cup.',
       'the shadow sits directly and symmetrically beneath the cup although the beam is plainly '
       'slanted'),
      ('minor', 'Shadow and glow both vanish if the beam is cut, and both move consistently if '
                'the cup or the source moves.',
       'the shadow or the glow survives the beam being cut, or drifts while cup and source are '
       'both still')),
    note="The dataset's law says the light path will be blocked. A plastic cup is translucent, "
         "so a rubric that demanded a full dark shadow would fail a correct clip.")

# ============ Direct radiation: glass bottle (42) =======================
add('shadow-casting', 42,
    'A diagonal beam passes through a glass bottle, casting caustics rather than a dark shadow.',
    S(('core', 'A glass bottle is present in an otherwise dark scene.'),
      ('core', 'A beam of light shines on it diagonally.'),
      ('core', "A shadow region corresponding to the bottle appears on the surface beyond it."),
      ('minor', 'The scene is dark apart from the beam and what it lights.')),
    P(('fatal', 'Light plainly passes through the bottle: the region beyond it is not uniformly '
                'dark.',
       'the glass bottle casts a solid dark shadow, as an opaque object would'),
      ('core', 'Bright concentrated streaks or bands appear within or beside the bottle\'s '
               'outline on the surface -- brighter than the surrounding lit surface, not darker.',
       'no bright concentrated light appears anywhere beyond the bottle'),
      ('core', 'Only the opaque parts -- a label, a cap, thick seams -- cast genuinely dark '
               'shadow.',
       'the clear glass casts as dark a shadow as the label and cap do'),
      ('major', "The bottle's body lights up internally where the beam crosses it.",
       'the glass stays dark where the beam passes through it'),
      ('major', 'The faint outline and the bright bands lie away from the source along the beam '
                'and are stretched because it is diagonal.',
       'the pattern sits symmetrically beneath the bottle, or falls on the source side of it'),
      ('minor', 'Outline, caustics and internal glow all vanish if the beam is cut, and all '
                'move consistently if the bottle or the source moves.',
       'part of the pattern survives the beam being cut, or drifts while bottle and source are '
       'both still'),
      ('minor', 'The surrounding scene stays dark apart from the beam and what it lights.',
       'the whole scene is lit although only a single narrow beam is present')),
    note="The dataset's law says the light path will be blocked by the glass. Glass transmits: "
         "the signature is a faint outline crossed by bright caustics, and a solid dark shadow "
         "is the wrong physics. The caption still asks for a shadow, so S3 assesses that "
         "separately.")

# ============ Tyndall scattering (45-54) ===============================
for i, src, med, place, decorated, extra in [
    (45, 'laser pointer', 'thick whole milk', 'a glass', True,
     ('minor', 'Whole milk scatters strongly, so the beam penetrates only a short way into the '
               'glass and diffuses into a glow rather than crossing it cleanly.',
      'the beam crosses the full width of thick whole milk as a clean undimmed line')),
    (46, 'flashlight', 'murky water', 'a bowl', True, None),
    (47, 'car headlight', 'dusty air', 'a jar', True,
     ('minor', 'Individual dust motes drifting through the beam glint as they cross it and go '
               'dark as they leave it.',
      'motes stay equally bright inside and outside the beam, or none react to it at all')),
    (48, 'phone flashlight', 'stirred muddy water', 'a container', True, None),
    (49, 'reading lamp', 'mixed orange juice', 'a bottle', True, None),
    (50, 'headlights', 'heavy fog', 'the open air', False, None),
    (51, 'flashlight', 'the dust of a dusty room', 'the room', False,
     ('minor', 'Individual dust motes drifting through the beam glint as they cross it and go '
               'dark as they leave it.',
      'motes stay equally bright inside and outside the beam, or none react to it at all')),
    (52, 'laser pointer', 'smoke', 'the open air', False,
     ('minor', 'Smoke drifting across the beam distorts and thickens the visible path where it '
               'passes, and the path recovers when the smoke moves on.',
      'the visible path is unaffected by smoke plainly drifting through it')),
    (53, 'flashlight', 'thick mist', 'the open air', False, None),
    (54, 'projector', 'fine dust', 'a dark room', False,
     ('minor', 'Individual dust motes drifting through the beam glint as they cross it and go '
               'dark as they leave it.',
      'motes stay equally bright inside and outside the beam, or none react to it at all')),
]:
    pc = [
        ('fatal', 'The beam is visible as a line or cone through the medium, not just as a spot '
                  'where it lands.',
         'no beam path is visible in the scattering medium at all'),
        ('core', "The visible path starts at the source's aperture and runs in a straight line "
                 "in the direction the source is pointed.",
         'the visible path starts away from the source, bends, or points somewhere the source '
         'does not'),
        ('core', 'The path is only visible inside the scattering medium: it is fainter or absent '
                 'in the clear air or clear liquid before and after it.',
         'the beam is equally visible in clear air or clear liquid where there is nothing to '
         'scatter it'),
        ('major', 'The beam dims and spreads with distance into the medium as light is scattered '
                  'out of it.',
         'the beam brightens as it goes deeper into the medium, or stays exactly as bright all '
         'the way through'),
        ('major', 'The path moves with the source: aim the source elsewhere and the visible line '
                  'follows immediately, keeping its straight geometry.',
         'the visible path lags behind the source, or stays put while the source turns away'),
        ('minor', 'The path vanishes when the source is switched off, and nothing glows in the '
                  'medium without the beam.',
         'the medium goes on glowing after the source is off'),
        ('minor', 'Where the beam meets a wall or the far side it makes a bright spot, and that '
                  'spot lies on the beam\'s straight continuation.',
         'the bright spot lands off the line the beam was travelling on'),
    ]
    if extra:
        pc.append(extra)
    sa = [('core', f'A {src} is present and switched on.'),
          ('core', f'{med.capitalize()} is present in {place}.'),
          ('core', 'The beam passes through the medium and its path is visible from the side.')]
    sa.append(('minor', 'The interaction reads as the mesmerizing display the caption promises.')
              if decorated else
              ('minor', 'The scene reads as the setting the caption names.'))
    add('tyndall-scattering', i,
        f'A beam from a {src} makes a visible path through {med}.',
        S(*sa), P(*pc),
        note=("The caption's 'intricate patterns and subtle hues' is decoration: Tyndall "
              "scattering gives a plain luminous path, not patterns or colours. It is scored as "
              "caption adherence in S4 and is not a physics requirement." if decorated else None))

# ============ Reflection in water: airborne objects (55-59) =============
for i, obj, water in [(55, 'bird', 'lake'), (56, 'kite', 'pond'), (57, 'plane', 'river'),
                      (58, 'drone', 'swimming pool'), (59, 'balloon', 'ocean')]:
    add('specular-reflection', i,
        f'A {obj} passes above a calm {water} and is reflected in it.',
        S(('core', f'A {obj} is present above the water.'),
          ('core', f'A calm, clear {water} is present.'),
          ('core', 'A reflection of the object appears on the water surface.'),
          ('minor', 'The water reads as calm and still, as the caption describes.')),
        P(('fatal', f'A reflection of the {obj} is present in the water while it is above it.',
           f'no reflection of the {obj} appears at all on a mirror-calm surface'),
          ('core', 'The reflection is inverted -- mirrored about the water line, not a second '
                   'upright copy.',
           'the reflection is upright, the same way up as the object'),
          ('core', 'It moves in step with the object: same horizontal direction, same timing, no '
                   'lag and no independent drift.',
           'the reflection lags, leads, or moves in a direction of its own'),
          ('core', "It shows the object's underside -- the face turned toward the water -- not "
                   "the face turned toward the camera.",
           'the reflection shows the same face of the object that the camera sees'),
          ('major', 'It appears equal in size or slightly smaller on screen, never larger than '
                    'the object.',
           'the reflection is plainly larger on screen than the object it belongs to'),
          ('major', 'The sky and the surroundings are mirrored in the same water at the same '
                    'time, consistently with the object\'s reflection.',
           'the water reflects the object but shows nothing of the sky or shore around it'),
          ('minor', 'It is dimmer and tinted by the water rather than as bright and crisp as the '
                    'object itself.',
           'the reflection is as bright and sharp as the object, or brighter'),
          ('minor', 'Ripples break the reflection up where they pass, and it re-forms as the '
                    'water settles.',
           'the reflection stays perfectly sharp across visibly rippled water')),
        note="The dataset's law says the reflection is the same size as the original. That holds "
             "for the virtual image, not for its apparent size on screen: the reflected path is "
             "longer, so the reflection subtends an equal or smaller angle. P5 states the "
             "checkable version.")

# ============ Reflection: object approaching a plane mirror (60) ========
add('specular-reflection', 60,
    'A wooden block moves toward an upright mirror and its image approaches from the other side.',
    S(('core', 'A wooden block and an upright mirror are both present.'),
      ('core', 'The block moves closer to the mirror.'),
      ('core', 'A reflection of the block in the mirror moves closer in step with it.'),
      ('minor', 'The mirror reads as upright and flat, as the caption describes.')),
    P(('fatal', 'An image of the block is present in the mirror throughout.',
       'the mirror shows no image although the block is plainly in front of it'),
      ('core', 'The image is the same size as the block and upright, not inverted.',
       'the image is inverted, or plainly a different size from the block'),
      ('core', 'It moves toward the mirror as the block does, in step and at the same rate.',
       'the image lags, leads, moves away as the block approaches, or drifts on its own'),
      ('major', "The gap between block and image closes at twice the block's own speed, and the "
                "two meet at the mirror's surface -- the image does not stop short of it or pass "
                "through it.",
       'the image stops short of the surface, or crosses out of the mirror into the room'),
      ('major', "The image's distance behind the mirror always matches the block's distance in "
                "front of it.",
       'the image sits at a depth unrelated to how far the block is from the mirror'),
      ('minor', 'The image is left-right reversed relative to the block.',
       'the image is not reversed, reading exactly as the block does'),
      ('minor', 'The image is dimmer than the block but otherwise the same shape and colour.',
       'the image is brighter than the block, or a different shape or colour')))

# ============ Reflection: partial reflectors (61, 63) ==================
for i, obj, surf, extra in [
    (61, 'football', 'vertical window',
     ('minor', 'Because the window is transparent, what is behind it is visible through the '
               'reflection at the same time.',
      'the window is completely opaque, showing only the reflection')),
    (63, 'basketball', 'shiny metallic surface',
     ('minor', 'The metal tints the reflection toward its own colour and blurs fine detail.',
      'the metal returns a perfect untinted image, as a clean mirror would')),
]:
    add('specular-reflection', i,
        f'A {obj} approaches a {surf} and its reflection approaches in step.',
        S(('core', f'A {obj} and a {surf} are both present.'),
          ('core', f'The {obj} moves closer to the surface.'),
          ('core', 'A reflection of it in the surface moves closer in step with it.'),
          ('minor', f'The surface reads as a {surf}.')),
        P(('fatal', f'An image of the {obj} is present in the reflecting surface throughout.',
           'the surface shows no image although the object is plainly in front of it'),
          ('core', 'It moves toward the surface as the object does, in step and at the same '
                   'rate.',
           'the image lags, leads, retreats as the object approaches, or drifts on its own'),
          ('core', 'It is upright and left-right reversed, not inverted.',
           'the image is upside down'),
          ('major', 'It is plainly fainter than the object, and tinted by the surface rather '
                    'than a perfect copy.',
           'the reflection is as bright and clean as the object itself, or brighter'),
          ('major', "Its distance behind the surface matches the object's distance in front, so "
                    "the two meet at the surface.",
           'the image sits at a depth unrelated to the object, or the two never meet at the '
           'surface'),
          ('minor', 'Whatever else faces the surface is reflected in it at the same time, '
                    'consistently with the object\'s reflection.',
           'the surface reflects the object alone and nothing else in front of it'),
          extra))

# ============ Reflection: ambiguous 'standing glass' (62) ==============
add('specular-reflection', 62,
    'A toy car drives toward a glass and its reflection approaches in step.',
    S(('core', 'A toy car and a standing glass are both present.'),
      ('core', 'The car moves closer to the glass.'),
      ('core', 'A reflection of the car in the glass moves closer in step with it.'),
      ('minor', 'The glass reads as standing upright, as the caption describes.')),
    P(('fatal', 'An image of the toy car is present in the glass throughout, moving toward it in '
                'step with the car.',
       'the glass shows no image although the car is plainly in front of it'),
      ('core', 'The image is upright rather than inverted.',
       'the image is upside down'),
      ('core', 'The image matches the shape of the glass it is in: same size for a flat pane, '
               'compressed and distorted for a curved vessel, with the distortion consistent '
               'across the whole image.',
       'a curved glass returns a flat undistorted same-size image, or a flat pane distorts one'),
      ('major', 'It is plainly fainter than the car, since only part of the light is reflected.',
       'the reflection is as bright and solid as the car itself'),
      ('major', 'The car is also visible through the glass, refracted and displaced, at the same '
                'time as the reflection.',
       'the glass is completely opaque, showing only the reflection'),
      ('minor', 'Whatever else faces the glass is reflected in it at the same time.',
       'the glass reflects the car alone and nothing else in front of it'),
      ('minor', "The image's distance behind the pane matches the car's distance in front of it.",
       'the image sits at a depth unrelated to how far the car is from the pane',
       'the glass is a flat pane')),
    note="'A standing glass' is ambiguous between a glass pane and a drinking glass, and the two "
         "give visibly different correct images. The dataset's same-size claim only holds for a "
         "flat pane, so P3 judges consistency with whichever is shown.")

# ============ Reflection: floating duck (64) ===========================
add('specular-reflection', 64,
    'A rubber duck floats on calm water with its reflection joined to it at the waterline.',
    S(('core', 'A rubber duck is floating on a calm water surface.'),
      ('core', 'The duck moves closer to the water surface and its reflection moves closer in '
               'step, as the caption describes.'),
      ('minor', 'A reflection of the duck is visible in the water.'),
      ('minor', 'The water reads as calm, as the caption describes.')),
    P(('fatal', 'A reflection of the duck is present in the water beneath it.',
       'no reflection appears beneath the duck on calm water'),
      ('core', 'The reflection is inverted and joined to the duck at the waterline, with no gap '
               'between duck and image.',
       'the reflection is upright, or sits separated from the duck by a stretch of open water'),
      ('core', 'The duck floats at a steady waterline: it neither sinks nor lifts clear of the '
               'water.',
       'the duck sinks, or rises off the surface, with nothing acting on it'),
      ('major', 'The reflection moves with the duck, in step and in the same horizontal '
                'direction.',
       'the reflection lags, leads, or moves in a direction of its own'),
      ('major', "The duck's own ripples break the reflection up as they spread, and it re-forms "
                "as the water settles.",
       'the reflection stays perfectly sharp while the duck plainly disturbs the water'),
      ('minor', 'It is dimmer than the duck and tinted by the water.',
       'the reflection is as bright and crisp as the duck, or brighter'),
      ('minor', "It shows the duck's water-facing side, not the face turned toward the camera.",
       'the reflection shows the same face of the duck that the camera sees')),
    note="The caption's premise is incoherent: a floating duck is already at the surface, so it "
         "cannot move closer to it. S2 asserts the caption anyway; PC judges the reflection "
         "geometry of a floating body, where image and object touch at the waterline.")

# ============ Refraction: magnifying glass (65-69) =====================
for i, subj, detail in [
    (65, 'the pages of an open book', 'the printed text'),
    (66, 'the face of a wristwatch', 'the hands and numbers'),
    (67, 'a leaf', 'the veins and surface patterns'),
    (68, 'a coin', 'the embossed design'),
    (69, 'the petals of a flower', 'the petal detail'),
]:
    add('lens-refraction', i,
        f'A magnifying glass moves closer to {subj}, enlarging {detail}.',
        S(('core', f'A magnifying glass and {subj} are both present.'),
          ('core', 'The glass moves gradually closer to the subject.'),
          ('core', f'The view through the glass shows {detail} enlarged as it approaches.'),
          ('minor', 'The subject reads as the one the caption names, with the detail it '
                    'mentions.')),
        P(('fatal', 'What is seen through the lens differs from what is seen beside it: the lens '
                    'changes the view rather than acting as a plain window.',
           'the view through the lens is identical to the view around it, as if the glass were '
           'flat'),
          ('core', 'Close in, the view through the lens is upright and larger than the same '
                   'detail outside the rim.',
           'with the lens close to the subject the view through it is not enlarged'),
          ('core', 'The magnification changes smoothly as the lens moves, and it changes in one '
                   'direction while the lens moves in one direction.',
           'the magnification jumps about, or grows and shrinks while the lens moves steadily '
           'one way'),
          ('core', 'The magnified content matches the actual content underneath -- the same '
                   'words, marks or patterns, enlarged, not different ones.',
           'the lens shows content that is not there underneath it'),
          ('major', 'The rim marks a sharp discontinuity: content jumps in scale across it, and '
                    'the content just inside the rim connects to the content just outside.',
           'the view fades smoothly across the rim with no jump, or the two views show '
           'unrelated regions'),
          ('major', 'Held far from the subject the view through the lens is inverted and small, '
                    'and any transition to the upright magnified view is continuous rather than '
                    'an abrupt swap.',
           'the view flips between states in a single cut, or stays upright and magnified with '
           'the lens held far off'),
          ('minor', "The lens's own outline and the hand holding it are not magnified.",
           'the rim or the fingers holding the lens are enlarged along with the subject'),
          ('minor', 'The lens does not add light of its own; the view through it is lit '
                    'consistently with the rest of the scene.',
           'the region seen through the lens glows brighter than the scene can account for')),
        note="The dataset's law states only the end result. A converging lens magnifies only "
             "inside its focal length: held far off it gives a small inverted image, which is "
             "correct physics and which a rubric demanding constant magnification would mark "
             "wrong. P6 covers that regime.")

# ============ Refraction: partly submerged objects (70-74) =============
for i, obj, extra in [
    (70, 'clear plastic straw', None),
    (71, 'silver spoon',
     ('minor', 'The polished spoon also reflects its surroundings, so the refracted submerged '
               'bowl and the reflected room are visible at once.',
      'the polished spoon reflects nothing at all')),
    (72, 'wooden pencil', None),
    (73, 'metal fork',
     ('minor', 'Every tine breaks at the same water line, all by the same offset and in the '
               'same direction.',
      'the tines break at different levels or offset in different directions')),
    (74, 'plastic ruler',
     ('minor', "The ruler's printed graduations make the offset directly visible: the marks "
               "above and below the surface no longer line up.",
      'the graduations run straight across the water line with no offset')),
]:
    pc = [
        ('fatal', 'The object appears to change direction exactly at the water surface, not '
                  'above it and not below it.',
         'the object stays perfectly straight through the surface, or bends at a level away '
         'from it'),
        ('core', 'The break appears only once the object is partly in the water, and it grows as '
                 'more of the object goes in.',
         'the break is there before the object touches the water, or does not change as it goes '
         'deeper'),
        ('core', 'The submerged part appears displaced sideways from the straight continuation '
                 'of the part above.',
         'the submerged part continues on exactly the line of the part above'),
        ('core', 'The part above water is undistorted and continues in a straight line.',
         'the part still in air is bent or distorted'),
        ('major', 'The submerged part appears shorter or raised rather than reaching as deep as '
                  'it really does, and appears wider or magnified compared with the part in air.',
         'the submerged part appears longer and thinner than the part in air'),
        ('major', 'The apparent kink tracks the object: tilt or move it and the offset changes '
                  'with it, vanishing when the object is straight along the line of sight.',
         'the kink stays fixed in place or in size while the object is tilted and moved'),
        ('minor', 'The water answers the insertion: ripples spread from the entry, the surface '
                  'line wobbles, and a partial mirror image of the object appears at the surface '
                  'alongside the refracted view.',
         'the water surface is completely unmoved by the insertion and reflects nothing'),
    ]
    if extra:
        pc.append(extra)
    add('refraction-at-interface', i,
        f'A {obj} is lowered into clear water and appears broken at the surface.',
        S(('core', f'A {obj} and a glass of clear water are both present.'),
          ('core', 'The object is put into the water and ends up partly submerged.'),
          ('core', 'The insertion is slow and gradual, as the caption describes.'),
          ('minor', 'Visible distortion and reflection at the surface are shown, as the caption '
                    'promises.')),
        P(*pc))

# ============ Thin-film interference (75, 76, 80-84) ===================
for i, subj, place, count, extra in [
    (75, 'soap bubbles', 'floating in the air under sunlight', 'a large number', [
        ('minor', 'Each bubble carries its own independent pattern, and that pattern moves and '
                  'rotates with the bubble it belongs to.',
         'all the bubbles share one identical pattern, or a pattern stays put while its bubble '
         'moves')]),
    (76, 'oil droplets', 'floating on the surface of water in sunlight', 'a group', [
        ('minor', "The coloured patches are carried by the water's surface flow and change "
                  "shape as they go.",
         'the coloured patches sit fixed in place while the water beneath them plainly flows')]),
    (80, 'a puddle of oil', 'on the road under sunlight', 'a single puddle', [
        ('minor', 'The coloured bands lie on the puddle surface and are broken up by ripples, '
                  're-forming as the surface settles.',
         'the bands stay perfectly still across a visibly rippled puddle')]),
    (81, 'a soap bubble', 'floating in the air under sunlight', 'a single bubble', []),
    (82, 'a film of soap on a wand', 'under sunlight', 'a single film', [
        ('minor', 'As the film drains it thins at the top, so the bands migrate downward and the '
                  'top goes colourless or black before the film breaks.',
         'the bands migrate upward, or the film stays uniformly coloured until it breaks')]),
    (83, 'a thin layer of gasoline on water', 'under sunlight', 'a single layer', []),
    (84, 'a layer of detergent on a wet surface', 'under sunlight', 'a single layer', []),
]:
    pc = [
        ('fatal', 'Iridescent colour appears on the film.',
         'the film is entirely colourless in full sunlight'),
        ('core', 'The colours appear as bands or swirls that vary across the film, not as one '
                 'uniform tint.',
         'the film is tinted one flat uniform colour all over'),
        ('core', 'The colours shift as the film moves, drains or is seen from a different angle, '
                 'rather than being painted on and fixed to the surface.',
         'the pattern is fixed like paint and does not change as the film moves or turns'),
        ('major', "The bands follow the film's thickness pattern and travel with the fluid "
                  "rather than sliding across it.",
         'the pattern slides across the film while the film itself stays still'),
        ('major', 'The colours are only present where the film is thin: thicker regions and the '
                  'surrounding bulk liquid are colourless.',
         'the bulk liquid or a thick region is iridescent too'),
        ('minor', 'The palette is the iridescent sequence -- magenta, gold, cyan, green -- '
                  'rather than arbitrary saturated colours.',
         'the colours are flat saturated primaries unlike any iridescence'),
        ('minor', 'The effect needs light and is a surface effect: what lies behind or under the '
                  'film still reads through it, and the colour dims and vanishes in shadow.',
         'the film is opaque, or goes on glowing with colour in shadow'),
    ]
    pc += extra
    if i in (75, 82):
        pc.append(('minor', 'A film that bursts is gone irreversibly: it does not re-form.',
                   'a burst film knits back together'))
    add('thin-film-interference', i,
        f'Iridescent colour appears on {subj} {place}.',
        S(('core', f'{subj.capitalize()} is present as described.'),
          ('core', 'The scene is lit by sunlight coming from a consistent direction.'),
          ('core', f'The subject is where the caption puts it: {place}.'),
          ('minor', f'The quantity roughly matches the caption -- {count}.')),
        P(*pc[:8]))

# ============ Glass marbles: caustics, not interference (77) ===========
add('caustics', 77,
    'Sunlit glass marbles on a floor throw bright caustics rather than iridescent colour.',
    S(('core', 'Several glass marbles are present on a floor.'),
      ('core', 'The scene is lit by sunlight coming from a consistent direction.'),
      ('minor', 'There are several marbles rather than one.'),
      ('minor', 'The surface they rest on reads as a floor.')),
    P(('fatal', 'Bright concentrated caustic patches appear on the floor near the marbles, on '
                'the far side from the sun.',
       'each marble casts a solid dark shadow with no bright patch, as an opaque ball would'),
      ('core', 'Each marble carries small sharp specular highlights positioned consistently '
               'with the sun.',
       'the highlights sit on the side away from the sun, or move independently of it'),
      ('core', 'Any colour in a marble is its own dye, fixed to it and unchanged by the viewing '
               'angle -- not a shifting iridescence.',
       'the marbles shimmer with shifting rainbow colour as the view changes'),
      ('major', 'Light passes through the marbles: what is behind a marble reads through it, '
                'displaced and inverted by its curvature.',
       'the marbles are opaque, showing nothing of what is behind them'),
      ('major', 'Caustics and highlights move consistently if the marbles or the light move.',
       'the caustics stay fixed on the floor while the marbles roll'),
      ('minor', 'Caustics and highlights need the sun: they vanish in shadow.',
       'the marbles keep throwing bright patches in shadow')),
    note="Recommended for exclusion. The dataset's law says interference and diffraction make "
         "the marbles colourful; neither mechanism operates on solid glass spheres. This rubric "
         "judges what a sunlit glass marble actually does.")

# ============ Mist: achromatic scattering (78) ========================
add('mie-scattering', 78,
    'Sunlit mist scatters light white, not into colour.',
    S(('core', 'Mist or suspended droplets are present in the air.'),
      ('core', 'The scene is lit by sunlight coming from a consistent direction.'),
      ('minor', 'The mist reads as suspended in the air rather than lying on a surface.')),
    P(('fatal', 'The suspended mist reads white or grey, bright where the sun strikes it, '
                'without intrinsic colour.',
       'the mist particles are rainbow-coloured'),
      ('core', 'Sunlight through the mist makes visible beams and shafts rather than coloured '
               'particles.',
       'the mist shows no beams or shafts although a directional sun plainly reaches it'),
      ('core', 'The brightness follows the sun: the mist is brightest toward the sun and dimmer '
               'away from it.',
       "the mist is brightest on the side away from the sun, or its brightness ignores the sun's "
       "position"),
      ('major', 'Any coloured arc present is a single ordered bow positioned opposite the sun, '
                'not colour spread over the particles themselves.',
       'colour appears scattered over the droplets with no ordered bow anywhere'),
      ('major', 'The mist drifts and thins with the air as one body, and it is the mist that '
                'carries the visible light rather than a separate glowing layer.',
       'the glow sits as its own layer, unattached to the drifting mist'),
      ('minor', 'The effect needs the sun and fades in shadow.',
       'the mist goes on glowing where the sun does not reach')),
    note="Recommended for exclusion. Mist droplets are far larger than the wavelength of light, "
         "so they scatter it achromatically; the dataset's colourful-mist claim cannot be "
         "satisfied correctly.")

# ============ Prisms: dispersion, not interference (79) ================
add('dispersion', 79,
    'Sunlight through an arrangement of prisms is split into cast spectra.',
    S(('core', 'Several prisms are present, arranged in a pattern.'),
      ('core', 'Sunlight shines through them.'),
      ('core', 'What the light does after passing through is visible in the shot.'),
      ('minor', 'The arrangement reads as the deliberate pattern the caption describes.')),
    P(('fatal', 'A spectrum appears where the transmitted light lands, not on the prisms '
                'themselves.',
       'the prisms glow rainbow-coloured and no spectrum is cast anywhere'),
      ('core', 'The colours run in the ordered sequence red, orange, yellow, green, blue, '
               'violet, adjacent and in that order.',
       'the colours appear in a random scatter of hues with no order'),
      ('core', 'Each spectrum lies on the far side of its prism from the sun, along the deviated '
               'beam.',
       'a spectrum falls on the sunward side of the prism that made it'),
      ('major', 'Each spectrum tracks the prism that made it: rotate or move a prism and its '
                'spectrum sweeps accordingly.',
       'a spectrum stays fixed while the prism that made it is moved or turned'),
      ('major', 'The light entering is white and the light leaving is dispersed; the prisms do '
                'not brighten the light or add any of their own.',
       'more light leaves the arrangement than enters it'),
      ('minor', 'The spectra vanish when the light is cut, and no colour is emitted in the dark.',
       'the prisms go on showing colour with the light cut off')),
    note="The dataset's law names interference and diffraction. Prism colour is dispersion -- "
         "wavelength-dependent refraction -- and its signature is an ordered spectrum cast onto "
         "a surface, not swirling colour on the glass. This prompt duplicates id 85.")

# ============ Dispersion (85-88) ======================================
for i, body, extra in [
    (85, 'prism', None),
    (86, 'crystal chandelier',
     ('minor', "The chandelier's many facets throw many separate spectral flecks around the "
               "room, each an ordered little spectrum, sweeping together if it turns.",
      'the chandelier throws one single spectrum, or flecks of flat uniform colour')),
    (87, 'droplet of water',
     ('minor', 'A single droplet both disperses and refocuses the light, so the colours appear '
               'as a small bright fan or arc rather than a long spread band.',
      'a single droplet casts a long broad spectral band as a prism would')),
    (88, 'glass diamond',
     ('minor', 'Glass disperses less than real diamond, so the spectral flecks are present but '
               'less vivid than a diamond\'s fire.',
      'the glass shows no spectral colour at all')),
]:
    pc = [
        ('fatal', 'An ordered spectrum appears -- red, orange, yellow, green, blue, violet, '
                  'adjacent and in that sequence.',
         'the light comes out white and unchanged, or in a random scatter of hues with no order'),
        ('core', 'It appears on the far side of the body from the source, along the path of the '
                 'deviated light.',
         'the spectrum falls on the source side of the body, or away from the light path '
         'entirely'),
        ('core', 'The light entering is white and only the light leaving is separated; the body '
                 'does not emit light of its own.',
         'the body glows with colour of its own accord, or emits more light than reaches it'),
        ('major', 'The spectrum tracks the geometry: move or turn the body, or the source, and '
                  'it sweeps accordingly and keeps its colour order.',
         'the spectrum stays fixed while the body or the source is moved'),
        ('major', "The body's own material stays its own colour and is not itself rainbow-"
                  "tinted.",
         'the body itself turns rainbow-coloured'),
        ('minor', 'The spectrum vanishes when the source is cut, and nothing glows in the dark.',
         'the spectrum survives the light being cut off'),
        ('minor', 'The spectrum keeps its colours in fixed order relative to one another; they '
                  'do not shuffle between frames.',
         'the order of the colours changes from frame to frame'),
    ]
    if extra:
        pc.append(extra)
    add('dispersion', i,
        f'A beam through a {body} is split into an ordered spectrum.',
        S(('core', f'A {body} is present.'),
          ('core', 'A beam of light passes through it.'),
          ('core', 'What happens to the light after it passes through is visible in the shot.'),
          ('minor', 'The light reads as a directed beam rather than ambient illumination.')),
        P(*pc),
        note="The dataset's law says the body 'emits multicolored light'. Nothing emits: the "
             "incoming white light is separated by wavelength and the spectrum lands beyond the "
             "body, so P1 and P3 ask for that instead.")

# ============ Soap bubble: thin film, not dispersion (89) =============
add('thin-film-interference', 89,
    'A beam on a soap bubble gives iridescent bands on the film, not a cast spectrum.',
    S(('core', 'A soap bubble is present.'),
      ('core', 'A beam of light reaches it.'),
      ('core', 'What happens to the light at the bubble is visible in the shot.'),
      ('minor', 'The light reads as a directed beam rather than ambient illumination.')),
    P(('fatal', "Iridescent colour appears on the bubble's own surface.",
       'the bubble surface is entirely colourless in the beam'),
      ('core', 'The colours are bands or swirls on the film, not a spectrum cast onto a surface '
               'beyond it.',
       'an ordered red-to-violet band is cast on a surface behind the bubble as a prism would '
       'cast it'),
      ('core', 'The colours vary across the bubble and shift as it moves, rotates or drains.',
       'the bubble carries one flat uniform tint, or a pattern fixed like paint'),
      ('major', 'The palette is iridescent -- magenta, gold, cyan, green -- rather than an '
                'ordered spectral sequence laid out in a line.',
       'the colours run in a strict red-to-violet line across the bubble'),
      ('major', 'The pattern is attached to the film and travels with it rather than sliding '
                'across a still surface.',
       'the pattern slides over the bubble while the bubble itself stays still'),
      ('minor', 'What is behind the bubble still reads through it.',
       'the bubble is opaque'),
      ('minor', 'The bubble bursts irreversibly and does not re-form.',
       'a burst bubble knits back together')),
    note="The dataset's law calls this dispersion. A soap film's colour is thin-film "
         "interference, whose signature is swirling bands on the film rather than an ordered "
         "spectrum cast beyond it; this prompt duplicates ids 75 and 81.")
