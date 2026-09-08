# ============ Litmus turned red by acid (145, 146) ======================
for i, acid, extra in [
    (145, 'colourless vinegar',
     ('minor', 'The level rises by the amount added.',
      'the level does not change when a glassful is poured in')),
    (146, 'hydrochloric acid',
     ('minor', 'More acid deepens the red rather than reversing it, and the colour saturates once '
               'the indicator has fully turned.',
      'adding more acid pushes the colour back toward purple')),
]:
    add('indicator-colour-change', i,
        f'{acid.capitalize()} is poured into purple litmus solution, which turns red.',
        S(('core', 'A glass of purple litmus solution is present.'),
          ('core', f'{acid.capitalize()} is poured into it.'),
          ('core', 'The solution changes over the course of the shot rather than staying as it '
                   'began.'),
          ('minor', 'The added liquid reads as colourless.'),
          ('minor', 'The shot reads as a timelapse: the change runs faster than it would in real '
                    'time.')),
        P(('fatal', 'The solution changes colour from purple to red: the added acid drops the pH '
                    'and the indicator turns.',
           'the solution stays purple, or turns blue, although an acid is plainly poured in'),
          ('core', 'The change begins where the acid enters and spreads outward with the mixing '
                   'flow.',
           'the whole glass switches colour in one frame, or the change starts somewhere the acid '
           'never reached'),
          ('core', 'The end state is uniform, with no purple layer or pocket left.',
           'a purple layer or pocket is still sitting in the glass at the end'),
          ('core', 'The change is irreversible: it does not drift back to purple on its own.',
           'the red drifts back to purple with nothing added'),
          ('major', 'Streaks of purple survive while the mixing is under way and are gradually '
                    'consumed.',
           'no streaked intermediate stage appears between the purple start and the uniform red '
           'end'),
          ('major', 'The added liquid is itself colourless, so the new colour comes from the '
                    'indicator rather than from pouring in something red.',
           'the poured liquid is visibly red as it goes in'),
          ('minor', 'Nothing happens that the chemistry does not call for: no bubbling, no '
                    'precipitate, no heat haze.',
           'the mixture fizzes, throws down a precipitate, or steams'),
          extra))

# ============ Soda water is acidic (147) ================================
add('indicator-colour-change', 147,
    'Colourless soda water is added to blue litmus solution, which turns red or pink.',
    S(('core', 'A glass of blue litmus solution is present.'),
      ('core', 'Colourless soda water is added to it.'),
      ('core', 'The solution changes over the course of the shot rather than staying as it began.'),
      ('minor', 'The added liquid reads as colourless and carbonated.'),
      ('minor', 'The shot reads as a timelapse: the change runs faster than it would in real '
                'time.')),
    P(('fatal', 'The blue litmus turns red or pink: soda water is carbonated water, whose '
                'dissolved carbon dioxide forms carbonic acid, so it is acidic.',
       'the solution stays blue, or deepens in blue, although an acid is plainly added'),
      ('core', 'The change begins where the soda water enters and spreads with the mixing.',
       'the whole glass switches colour in one frame, or the change starts somewhere the soda '
       'water never reached'),
      ('core', 'Bubbles form and rise to the surface as dissolved carbon dioxide comes out of '
               'solution.',
       'no bubbles appear at all although carbonated water is poured in'),
      ('core', 'The fizzing subsides over time as the dissolved gas is used up rather than '
               'continuing undiminished.',
       'the fizzing goes on at full strength indefinitely'),
      ('major', 'Streaks of blue persist while the mixing is under way and are consumed, ending '
                'in a uniform colour.',
       'no streaked intermediate stage appears between the blue start and the uniform end'),
      ('major', 'The added liquid is colourless, so the colour change comes from the indicator '
                'rather than from pouring in something pink.',
       'the poured liquid is visibly red or pink as it goes in'),
      ('minor', 'The colour change holds over the shot; it may pale slightly as gas escapes but it '
                'does not revert to blue.',
       'the colour drifts back to blue with nothing added'),
      ('minor', 'The level rises by the amount added.',
       'the level does not change when a glassful is poured in')),
    note="The dataset's law says the solution remains blue, which is factually wrong: carbonated "
         "water is acidic and turns blue litmus red. Following the law would mark a correct clip "
         "wrong and give full marks to a clip in which nothing happens -- the easiest thing for a "
         "video model to produce, so this error is actively harmful as a benchmark item.")

# ============ Cabbage-juice indicator, no gas (148) ====================
add('indicator-colour-change', 148,
    'Lemon juice is poured into red cabbage juice, shifting it from purple toward pink.',
    S(('core', 'A glass of red cabbage juice is present.'),
      ('core', 'Lemon juice is poured into it.'),
      ('core', 'The mixture changes over the course of the shot rather than staying as it began.'),
      ('minor', 'The shot reads as a timelapse: the change runs faster than it would in real '
                'time.')),
    P(('fatal', 'The cabbage juice shifts from purple toward pink or red: its anthocyanin is an '
                'indicator and the lemon juice acidifies it.',
       'the colour does not change at all, or it shifts toward blue or green'),
      ('core', 'No bubbles or fizzing appear: nothing here produces a gas.',
       'the mixture fizzes and gives off bubbles'),
      ('core', 'The shift begins where the lemon juice enters and spreads with the mixing.',
       'the whole glass switches colour in one frame, or the change starts somewhere the lemon '
       'juice never reached'),
      ('core', 'No precipitate forms and the contents stay liquid throughout.',
       'a solid precipitate settles out, or the mixture sets'),
      ('major', 'Streaks of the original colour persist while the mixing is under way and are '
                'consumed, ending uniform.',
       'no streaked intermediate stage appears between the purple start and the uniform end'),
      ('major', 'The final colour is intermediate and consistent with dilution: it does not become '
                'more vivid than either starting liquid.',
       'the mixture ends up more vivid and saturated than either liquid that went into it'),
      ('minor', 'The change is irreversible on its own over the shot.',
       'the colour drifts back to its starting purple with nothing added'),
      ('minor', 'The level rises by the amount added.',
       'the level does not change when a glassful is poured in')),
    note="Two errors in the dataset's law. It calls this an acid-base reaction, but cabbage juice "
         "is an indicator and this is a colour shift, not neutralisation; and it claims a release "
         "of gases, when nothing here produces gas. A verbatim rubric would reward a clip that "
         "invents fizzing -- exactly the plausible-looking hallucination the benchmark exists to "
         "catch.")

# ============ Acid + carbonate fizz (149) ==============================
add('acid-carbonate-reaction', 149,
    'Baking soda is mixed into orange juice in a clear cup and the mixture fizzes.',
    S(('core', 'Orange juice is present in a clear cup.'),
      ('core', 'Baking soda is added to it and mixed.'),
      ('core', 'The mixture changes over the course of the shot rather than staying as it began.'),
      ('minor', 'The cup reads as clear, as the caption says.'),
      ('minor', 'The shot reads as a timelapse: the change runs faster than it would in real '
                'time.')),
    P(('fatal', 'The mixture fizzes: bubbles appear and rise once the baking soda meets the juice, '
                'as the citric acid and the bicarbonate release carbon dioxide.',
       'nothing at all happens when baking soda is mixed into acidic juice'),
      ('core', 'The bubbling starts at the powder itself and where it lands, not uniformly '
               'throughout the liquid.',
       'bubbles appear evenly throughout the liquid with none at the powder'),
      ('core', 'The fizzing is most vigorous just after the mixing and then subsides as the '
               'reactants are consumed.',
       'the fizzing continues undiminished indefinitely, or starts long afterwards for no reason'),
      ('core', 'Bubbles rise upward and burst at the surface; none sink.',
       'bubbles sink through the liquid toward the bottom of the cup'),
      ('major', 'Foam builds on the surface and can rise up the cup, possibly over the rim.',
       'no foam gathers on the surface of a vigorously fizzing mixture'),
      ('major', 'The powder visibly dissolves and disappears as it reacts.',
       'the powder is still sitting there unchanged after the fizzing has finished'),
      ('minor', 'The reaction is irreversible: the foam collapses back to liquid and the powder '
                'does not re-form.',
       'the powder re-forms out of the liquid'),
      ('minor', "The liquid keeps the juice's own colour, and the foam is a paler version of it "
                "rather than a new colour.",
       'the mixture turns a colour that has nothing to do with the juice')))

# ============ Sulfuric acid dehydration (150-153) ======================
for i, subj, extra in [
    (150, 'a piece of bread',
     ('minor', "The porous crumb soaks the acid up, so the blackening runs deeper than the "
               "surface and follows the acid into the structure.",
      'the charring stays a flat surface stain on porous bread')),
    (151, 'a slice of apple',
     ('minor', "The apple's water content makes the reaction wetter: liquid is released, the "
               "surface bubbles, and the flesh collapses as it blackens.",
      'the apple stays dry and firm while it blackens')),
    (152, 'a sheet of paper',
     ('minor', 'The acid runs and pools under gravity, and the charring follows where it flows '
               'across the sheet.',
      'the acid runs uphill, or the charring appears where no acid ever flowed')),
    (153, 'a cotton ball',
     ('minor', 'The fibres blacken and the ball collapses from a fluffy mass to a small dark '
               'clump.',
      'the cotton ball keeps its full fluffy volume after charring')),
]:
    add('acid-dehydration', i,
        f'Concentrated sulfuric acid is poured onto {subj}, which chars black.',
        S(('core', f'{subj.capitalize()} is present.'),
          ('core', 'Concentrated sulfuric acid is poured onto it.'),
          ('core', 'A reaction is shown over the course of the shot rather than a static scene.'),
          ('minor', 'The shot reads as a timelapse: the change runs faster than it would in real '
                    'time.')),
        P(('fatal', 'The wetted material darkens and chars: the acid strips water out of the '
                    'carbohydrate and leaves carbon behind.',
           'the acid lands and nothing at all happens to the material'),
          ('core', 'The darkening starts exactly where the acid landed and spreads outward from '
                   'there as it soaks in.',
           'the whole object darkens at once, or the darkening starts where the acid never '
           'reached'),
          ('core', 'The colour progresses through yellowing and browning to black rather than '
                   'jumping straight to black.',
           'the material goes from untouched to fully black in a single step'),
          ('core', 'Parts of the object the acid never reached stay unchanged in colour and '
                   'shape.',
           'the whole object is consumed although only part of it was wetted'),
          ('major', 'The wetted material shrinks, wrinkles and slumps as it chars.',
           'the blackened region keeps its exact original shape and volume'),
          ('major', 'The change is irreversible: the charred region does not lighten or recover.',
           'the blackened region lightens back toward its original colour'),
          ('minor', 'Fumes or vapour rise from the reacting area, driven by the heat released.',
           'no fume or vapour at all rises from a vigorously reacting area'),
          extra),
        note="Only a wording trim from the dataset's law: 'releasing large amounts of acidic gas' "
             "has a clause a video cannot show, so the rubric keeps the visible fume and drops the "
             "chemical identification.")

# ============ Sulfuric acid on a sponge (154) ==========================
add('acid-dehydration', 154,
    'Concentrated sulfuric acid is poured onto a sponge, which is attacked where it lands.',
    S(('core', 'A sponge is present.'),
      ('core', 'Concentrated sulfuric acid is poured onto it.'),
      ('core', 'A reaction is shown over the course of the shot rather than a static scene.'),
      ('minor', 'The shot reads as a timelapse: the change runs faster than it would in real '
                'time.')),
    P(('fatal', 'The sponge is visibly attacked where the acid landed.',
       'the acid lands and nothing at all happens to the sponge'),
      ('core', 'The change starts exactly where the acid landed and spreads outward from there.',
       'the whole sponge changes at once, or the change starts where the acid never reached'),
      ('core', 'Whichever path the material takes is shown consistently: charring to black for a '
               'cellulose sponge, or yellowing, softening and dissolving for a synthetic one.',
       'the sponge carbonises to black like cellulose and melts and dissolves like plastic at the '
       'same time'),
      ('core', 'Untouched parts of the sponge stay unchanged in colour and shape.',
       'the whole sponge is destroyed although only part of it was wetted'),
      ('major', 'The wetted region shrinks and collapses as it is attacked.',
       'the damaged region keeps its exact original shape and volume'),
      ('major', 'The damage is irreversible and does not recover.',
       'the damaged region springs back to its original state'),
      ('minor', 'Fumes or vapour rise from the reacting area.',
       'no fume or vapour at all rises from a vigorously reacting area'),
      ('minor', 'The acid runs and pools under gravity, and the damage follows where it flows.',
       'the acid runs uphill, or the damage appears where no acid ever flowed')),
    note="The dataset's law asserts dehydration and carbonisation, which is material-specific, and "
         "'a sponge' is ambiguous between cellulose and polyurethane. A rubric demanding black "
         "carbonisation would fail a correct clip of a plastic sponge, so P3 judges internal "
         "consistency with whichever material is shown.")

# ============ Rusting of iron and steel (155, 156) =====================
for i, metal in [(155, 'iron'), (156, 'steel')]:
    add('rusting', i,
        f'A clean, smooth piece of {metal} rusts over decades in a humid environment.',
        S(('core', f'A clean, smooth piece of {metal} is present at the start.'),
          ('core', 'It changes over the course of the shot rather than staying as it began.'),
          ('minor', 'The environment reads as humid, as the caption says.'),
          ('minor', 'The shot reads as a timelapse covering a very long span, as the caption '
                    'says.')),
        P(('fatal', 'Orange-brown rust appears on the metal and grows over the timelapse, since '
                    'water and oxygen are both present.',
           'the metal stays clean and bright throughout although it sits in a humid environment '
           'for decades'),
          ('core', 'It starts at edges, corners, scratches and places where water sits, then '
                   'spreads over the flat surface.',
           'rust appears uniformly all over at once, or the flat middle rusts while the edges stay '
           'bright'),
          ('core', 'The rusted area only ever grows: it never shrinks or reverts to bare metal.',
           'rusted areas return to bright bare metal as the timelapse runs on'),
          ('core', 'The colour progression runs through dull grey and light brown before deep '
                   'orange-brown.',
           'the metal goes from bright to fully rusted in a single step'),
          ('major', 'The surface loses its shine progressively, becoming dull and then rough.',
           'the metal keeps a mirror shine under heavy rust'),
          ('major', 'The rust roughens, blisters and flakes, so the texture changes and not just '
                    'the colour.',
           'the rust is a flat painted-on colour change with no change of texture at all'),
          ('minor', 'The object keeps its overall shape and position: rust corrodes and pits it '
                    'but does not make it move, grow or change form.',
           'the object moves, grows or changes shape as it rusts'),
          ('minor', 'Rust stains run downward from the corroded areas, following where water '
                    'drains.',
           'the stains run upward from the rusted patches')))

# ============ Corrosion of unspecified metal (157, 158, 159) ===========
for i, obj, setting in [
    (157, 'metal chair', 'left outdoors in the rain over a long period'),
    (158, 'polished metal railing', 'exposed to the elements over years'),
    (159, 'metal bedframe', 'kept in a damp location over several years'),
]:
    add('corrosion', i,
        f'A bright, new {obj} {setting} corrodes progressively.',
        S(('core', f'A bright, new {obj} is present at the start.'),
          ('core', 'It changes over the course of the shot rather than staying as it began.'),
          ('minor', f'The setting reads as {setting}, as the caption says.'),
          ('minor', 'The shot reads as a timelapse covering a long span, as the caption says.')),
        P(('fatal', 'The metal surface corrodes progressively rather than staying pristine.',
           'the metal is still bright and new after years of exposure to water'),
          ('core', 'The corrosion product matches the metal shown: orange-brown flaking rust for '
                   'iron or steel, dull grey or white oxide for aluminium and zinc, green patina '
                   'for copper or brass.',
           'bright orange rust appears on a metal that cannot rust, such as aluminium, copper or '
           'brass'),
          ('core', 'It starts at edges, joints, scratches and places where water lingers, then '
                   'spreads.',
           'the corrosion appears uniformly all over at once, or sheltered parts corrode while the '
           'wet edges and joints stay bright'),
          ('core', 'The corroded area only ever grows: it never reverts to bright metal.',
           'corroded areas return to bright metal as the timelapse runs on'),
          ('major', 'The shine is lost progressively, and the surface roughens, pits or flakes.',
           'the metal keeps a mirror shine under heavy corrosion'),
          ('major', 'The colour progression is gradual rather than a single jump to a fully '
                    'corroded state.',
           'the metal goes from bright to fully corroded in a single step'),
          ('minor', 'The object keeps its shape and position, corroding in place.',
           'the object moves, grows or changes shape as it corrodes'),
          ('minor', 'Stains run downward from the corroded areas, following how the water drains.',
           'the stains run upward from the corroded patches')),
        note="The dataset's law says the metal will rust, which is over-general: rust is iron "
             "oxide, and the caption names only 'metal'. A correct clip of an aluminium railing "
             "going dull grey would be marked wrong, and bright orange rust on anodised aluminium "
             "would be marked right. Ids 155 and 156 cover the ferrous case properly, so P2 here "
             "asks for the product appropriate to whatever metal is shown.")
