# PhyGenBench `physical_laws` 逐条体检

## 摘要

160 条 prompt 全部过了一遍，判据只有一条：**照抄这条 law 写出来的 rubric，会不会误判一个物理正确的片段，或者放过一个物理错误的片段。**只要会，就归入需改写——哪怕 law 的结论本身是对的。

结果：**可直接用 110**、**需改写 47**、**建议排除 3**（共 160）。每条都给了改正后的 law 和展开的可见观察量，观察量总数 1204 条。

几条要单独说的：

- **id 109（油沸腾）是全库最严重的一条。**law 写「温度到 100°C 油会沸腾、大量气泡涌上表面」——油的沸点在 300°C 以上，100°C 的油只是热。也就是说，一个把油拍成 100°C 剧烈沸腾的片段，会被这条 law 判为**正确**。错的方向朝着奖励幻觉走。而且末句写的是 "the coffee surface"，是从别的 caption 复制粘贴留下的。
- **id 147（苏打水）方向性错误。**苏打水是碳酸水，pH 3–4，蓝色石蕊会变红；law 写「溶液保持蓝色」。照抄的结果是：**什么都不发生的片段得满分**，而这恰好是视频模型最容易生成的东西。
- **id 101（暖车窗）caption 和 law 直接矛盾。**caption 说冷环境里的暖车窗，law 说「窗温远低于雾温」。两者不能同真，且按 caption 的物理，雾碰到暖玻璃是蒸发而不是凝结。这个没法只改 law 修好，所以建议排除。
- **id 110–114（凝华）五条把动词写反了**：气→固是 deposition，sublimation 是反过来。结论没错，但 law 里完全没提真正有用的那条判据——直接长冰晶、没有液滴阶段，而这是它和 100–104（液化）唯一的区分点。
- **id 148（紫甘蓝汁）说会放气体**，实际不放。照抄会奖励一个凭空加气泡的片段。
- **id 123（青+洋红）**减色混合得到的是**蓝**，不是 law 写的 purple。
- **id 77（玻璃弹珠）、78（雾滴）建议排除**：干涉/衍射在这两个体系里根本不发生，实心玻璃球给的是 caustics，雾滴给的是白色 Mie 散射。law 要求「珠子/雾会很多彩」，照抄就是要求模型生成一个不存在的现象。
- **id 116、118 的证据是气味**，视频判不了；换成「固体变小 + 无液相 + 冷面复凝」，也就是 117 已经写对的那套。
- **id 55–59（水面倒影）和 65–69（放大镜）结论对但会误判正确片段**：前者「与原物同大小」只对虚像成立、屏幕上倒影只会等大或更小；后者只写了终态放大，而一个从远处推近的正确片段会先出现**倒立缩小**的实像。

打的标记：`mechanism-mislabelled`×11、`premise-implausible`×5、`outcome-uncertain`×3、`object-mismatch`×2、`duplicate`×2、`non-visual`×2、`caption-law-conflict`×1、`low-visibility`×1。

机器可读版在 `_audit.json`，字段：`verdict` / `law_original` / `law_corrected` / `observables` / `issue` / `flags`。下面是逐条内容。

## 需改写与建议排除清单

| id | main | sub | verdict | flags | 问题一句话 |
|---|---|---|---|---|---|
| 7 | Force | Buoyancy | **需改写** | `object-mismatch` | The law names a wood block; the caption places a tennis ball. The conclusion (floats) is right, the object is not -- copied from id 8. |
| 12 | Force | Stress | **需改写** | -- | 'Shrink' is wrong for a sealed air balloon under hand pressure: air is nearly incompressible at these loads, so the balloon changes shape at roughly constant volume. |
| 17 | Force | Atmospheric Pressure | **需改写** | -- | A curved stiff shell does not shrink uniformly under external pressure; it buckles locally. |
| 19 | Force | Atmosphere Pressure | **需改写** | `mechanism-mislabelled` | Mechanism mislabelled. An inflated balloon's rubber is under tension, so its internal pressure is already above atmospheric; it collapses by elastic recoil when emptie... |
| 24 | Force | Solid Pressure | **需改写** | `outcome-uncertain` | The outcome is not determined by the physics as captioned. A pencil is blunt compared with a needle, and slow pressing on a balloon is the classic case that can go eit... |
| 31 | Force | Friction | **需改写** | `mechanism-mislabelled` | Mechanism mislabelled: the mark is ink deposition (capillary wetting, or ink transferred by a rolling ball), not friction-driven abrasion. |
| 33 | Force | Friction | **需改写** | `mechanism-mislabelled` | Mechanism mislabelled: the mark is ink deposition (capillary wetting, or ink transferred by a rolling ball), not friction-driven abrasion. |
| 34 | Force | Friction | **需改写** | `mechanism-mislabelled` | Mechanism mislabelled: the mark is ink deposition (capillary wetting, or ink transferred by a rolling ball), not friction-driven abrasion. |
| 36 | Force | Surface Tension | **需改写** | -- | Bare glass and glazed ceramic are hydrophilic; water spreads on them. Requiring 'spherical droplets' here would mark a physically correct clip wrong. |
| 38 | Force | Surface Tension | **需改写** | -- | Bare glass and glazed ceramic are hydrophilic; water spreads on them. Requiring 'spherical droplets' here would mark a physically correct clip wrong. |
| 39 | Force | Surface Tension | **需改写** | `premise-implausible` | The caption's premise is physically impossible: water does not slide gracefully across paper, it is absorbed. |
| 42 | Light | Direct Radiation | **需改写** | -- | Glass is transparent. The law's claim that the light path 'will be blocked by the glass bottle' is false, and a verbatim rubric would reward a clip showing a solid dar... |
| 43 | Light | Direct Radiation | **需改写** | -- | A plastic cup is translucent, not opaque. Stating flatly that the beam 'will be blocked' invites a rubric item that requires a full dark shadow and would fail a correc... |
| 55 | Light | Reflection | **需改写** | -- | 'The same size as the original entities' is true of the virtual image in object space, but not of its apparent size on screen: the reflected ray path is longer than th... |
| 56 | Light | Reflection | **需改写** | -- | 'The same size as the original entities' is true of the virtual image in object space, but not of its apparent size on screen: the reflected ray path is longer than th... |
| 57 | Light | Reflection | **需改写** | -- | 'The same size as the original entities' is true of the virtual image in object space, but not of its apparent size on screen: the reflected ray path is longer than th... |
| 58 | Light | Reflection | **需改写** | -- | 'The same size as the original entities' is true of the virtual image in object space, but not of its apparent size on screen: the reflected ray path is longer than th... |
| 59 | Light | Reflection | **需改写** | -- | 'The same size as the original entities' is true of the virtual image in object space, but not of its apparent size on screen: the reflected ray path is longer than th... |
| 62 | Light | Reflection | **需改写** | `outcome-uncertain` | The caption is ambiguous between a glass pane and a drinking glass, and the two give visibly different correct answers. |
| 64 | Light | Reflection | **需改写** | `premise-implausible` | The caption's premise is incoherent -- a floating object is already at the surface, so 'floating closer to a calm water surface' names no motion. |
| 65 | Light | Refraction | **需改写** | -- | The law states only the end state. A physically faithful clip that starts with the lens far from the page shows a small inverted image first, which a verbatim rubric i... |
| 66 | Light | Refraction | **需改写** | -- | The law states only the end state. A physically faithful clip that starts with the lens far from the page shows a small inverted image first, which a verbatim rubric i... |
| 67 | Light | Refraction | **需改写** | -- | The law states only the end state. A physically faithful clip that starts with the lens far from the page shows a small inverted image first, which a verbatim rubric i... |
| 68 | Light | Refraction | **需改写** | -- | The law states only the end state. A physically faithful clip that starts with the lens far from the page shows a small inverted image first, which a verbatim rubric i... |
| 69 | Light | Refraction | **需改写** | -- | The law states only the end state. A physically faithful clip that starts with the lens far from the page shows a small inverted image first, which a verbatim rubric i... |
| 77 | Light | Interference & Diffraction | **建议排除** | -- | The law is false: 'due to interference & diffraction, the marbles will be colorful' names a mechanism that does not operate on solid glass spheres. |
| 78 | Light | Interference & Diffraction | **建议排除** | -- | The law is false: individual mist particles are not coloured by interference or diffraction. |
| 79 | Light | Interference & Diffraction | **需改写** | `mechanism-mislabelled` `duplicate` | Mechanism mislabelled. Prism colour is dispersion (wavelength-dependent refraction), not thin-film interference; a prism has no thin film. |
| 89 | Light | Dispersion | **需改写** | `mechanism-mislabelled` `duplicate` | Mechanism mislabelled: a soap film is a few hundred nanometres thick and its colour comes from interference between reflections at its two surfaces, not from wavelengt... |
| 93 | Heat | Solidification | **需改写** | -- | 'Below the freezing point, the oil will freeze' invites a rubric item that demands water-like freezing. |
| 101 | Heat | Liquefaction | **建议排除** | `caption-law-conflict` | Direct caption/law conflict. The caption says a WARM car window in a COLD environment; the law says 'the temperature of window is much lower than that of fog'. |
| 109 | Heat | Boiling | **需改写** | `premise-implausible` | Two faults. (1) The law is physically false: oil at 100 C is merely hot, so a clip showing oil in a vigorous rolling boil at 100 C would be marked CORRECT by this law... |
| 110 | Heat | deposition | **需改写** | `mechanism-mislabelled` | The verb is exactly backwards: sublimation is solid to gas, and vapour to solid is deposition. Five entries repeat the error. |
| 111 | Heat | deposition | **需改写** | `mechanism-mislabelled` | The verb is exactly backwards: sublimation is solid to gas, and vapour to solid is deposition. Five entries repeat the error. |
| 112 | Heat | deposition | **需改写** | `mechanism-mislabelled` `premise-implausible` | The verb is exactly backwards: sublimation is solid to gas, and vapour to solid is deposition. Five entries repeat the error. |
| 113 | Heat | deposition | **需改写** | `mechanism-mislabelled` | The verb is exactly backwards: sublimation is solid to gas, and vapour to solid is deposition. Five entries repeat the error. |
| 114 | Heat | deposition | **需改写** | `mechanism-mislabelled` | The verb is exactly backwards: sublimation is solid to gas, and vapour to solid is deposition. Five entries repeat the error. |
| 116 | Heat | Sublimation | **需改写** | `non-visual` | The stated evidence is non-visual: 'will emit a distinctive odor' (116) and 'will release its characteristic strong aroma' (118) cannot be checked from a video, so a r... |
| 118 | Heat | Sublimation | **需改写** | `non-visual` | The stated evidence is non-visual: 'will emit a distinctive odor' (116) and 'will release its characteristic strong aroma' (118) cannot be checked from a video, so a r... |
| 123 | Physical Properties | Color | **需改写** | -- | Subtractive mixing of cyan and magenta yields blue. Labelling the target 'purple' is loose enough that a clip producing a red-violet -- which would require a red-absor... |
| 134 | Physical Properties | Hardness | **需改写** | -- | 'The hardness of the wood is very high' is simply false -- wood is far softer than porcelain, and the sibling entries use stone, concrete and metal precisely because t... |
| 136 | Physical Properties | Solubility | **需改写** | -- | 'Due to immiscibility, honey and milk cannot dissolve each other' is false: honey is sugar in water and dissolves fully in an aqueous liquid. |
| 140 | Physical Properties | Combustibility | **需改写** | `object-mismatch` | Object mismatch: the law says 'combustibility of wood, the wood will be ignited' while the caption contains no wood at all -- it is paper into paper, apparently a copy... |
| 143 | Physical Properties | Combustibility | **需改写** | `outcome-uncertain` | Mandating that the grass 'will be ignited' penalises the most likely real outcome -- a thrown candle is extinguished in flight. |
| 147 | Chemical Properties | Acidity and Alkalinity | **需改写** | -- | Factually wrong: 'the solution color remains blue' would only hold for a neutral or basic addition. Carbonated water has a pH around 3-4 and turns blue litmus red. |
| 148 | Chemical Properties | Acidity and Alkalinity | **需改写** | -- | Two errors. 'Acid and base reaction' is wrong -- cabbage juice is an indicator, and mixing it with lemon juice is an indicator colour shift, not neutralisation. |
| 154 | Chemical Properties | Dehydration property | **需改写** | -- | The dehydration/carbonisation claim is material-specific, and 'a sponge' is ambiguous between cellulose and polyurethane. |
| 157 | Chemical Properties | Redox property | **需改写** | -- | The caption says only 'metal' -- a chair, a railing, a bedframe -- and the law asserts that metal rusts. |
| 158 | Chemical Properties | Redox property | **需改写** | -- | The caption says only 'metal' -- a chair, a railing, a bedframe -- and the law asserts that metal rusts. |
| 159 | Chemical Properties | Redox property | **需改写** | -- | The caption says only 'metal' -- a chair, a railing, a bedframe -- and the law asserts that metal rusts. |

## 可直接用但有保留

结论正确、照抄也不会误判，但有一句得删掉或者有个前提得注意。

| id | sub | flags | 保留 |
|---|---|---|---|
| 45 | Tyndall Effect | -- | The law itself is right. The caption is what over-claims: 'casting intricate patterns and subtle hues' is decoration -- Tyndall scattering gives a plain luminous path,... |
| 46 | Tyndall Effect | -- | The law itself is right. The caption is what over-claims: 'casting intricate patterns and subtle hues' is decoration -- Tyndall scattering gives a plain luminous path,... |
| 47 | Tyndall Effect | -- | The law itself is right. The caption is what over-claims: 'casting intricate patterns and subtle hues' is decoration -- Tyndall scattering gives a plain luminous path,... |
| 48 | Tyndall Effect | -- | The law itself is right. The caption is what over-claims: 'casting intricate patterns and subtle hues' is decoration -- Tyndall scattering gives a plain luminous path,... |
| 49 | Tyndall Effect | -- | The law itself is right. The caption is what over-claims: 'casting intricate patterns and subtle hues' is decoration -- Tyndall scattering gives a plain luminous path,... |
| 85 | Dispersion | -- | Only the wording needs care: nothing 'emits' multicoloured light. |
| 86 | Dispersion | -- | Only the wording needs care: nothing 'emits' multicoloured light. |
| 87 | Dispersion | -- | Only the wording needs care: nothing 'emits' multicoloured light. |
| 88 | Dispersion | -- | Only the wording needs care: nothing 'emits' multicoloured light. |
| 119 | Sublimation | -- | Only the wording needs trimming: 'toxic' is not a visible property and must not become a rubric item. |
| 125 | Flame Reaction | `premise-implausible` | The colour claim is right, but the caption's setup cannot happen: a piece of copper will not catch fire. |
| 137 | Solubility | `low-visibility` | The law is correct but nearly unjudgeable on video: clear liquid into clear liquid produces almost no visible evidence either way, so a rubric built on it can be satis... |
| 150 | Dehydration property | -- | Only a wording trim: 'releasing large amounts of acidic gas' has a non-visible clause. |
| 151 | Dehydration property | -- | Only a wording trim: 'releasing large amounts of acidic gas' has a non-visible clause. |
| 152 | Dehydration property | -- | Only a wording trim: 'releasing large amounts of acidic gas' has a non-visible clause. |
| 153 | Dehydration property | -- | Only a wording trim: 'releasing large amounts of acidic gas' has a non-visible clause. |

## 逐条

### Force

#### id 0, 1, 2, 3, 4 — Gravity — **可直接用**

- `0` A cup of water is slowly poured out in the space station, releasing the liquid into the surrounding area
- `1` A cup of oil is slowly poured out in the space station, releasing the liquid into the surrounding area
- `2` A bottle of juice is slowly poured out in the space station, releasing the liquid into the surrounding area
- `3` A squeeze of honey is slowly released in the space station, spreading the liquid into the surrounding area
- `4` A can of soda is slowly poured out in the space station, releasing the liquid into the surrounding area

**Law as given.**

> Lack of gravity

**Corrected.** In the microgravity of an orbiting station there is no downward pull. Released liquid does not fall; it drifts on whatever velocity it was given, and surface tension pulls it into rounded blobs that merge on contact and cling to any surface they touch.

**Observables.**

- No direction in the scene acts as 'down': the released liquid does not accelerate toward the floor, and nothing pools at the bottom of the frame.
- A freed mass of liquid rounds up into a blob or sphere instead of falling as a column or breaking into a splashing stream.
- A drifting blob travels in a straight line at roughly constant speed until it meets something; its path does not arc downward.
- Two blobs that touch merge into one larger blob and stay merged.
- A blob that touches a surface sticks and spreads over it rather than running off it or collecting beneath it.
- Liquid still inside the cup or bottle shows no flat horizontal surface; it wets and clings to the container wall instead of lying level.
- The astronaut's hair, clothing and any loose object in shot also hang free rather than falling.

**Additionally for 3.**

- The honey, far more viscous, is slow to round up: it trails strands and lumpy shapes that only gradually pull into blobs.

**Additionally for 4.**

- Gas bubbles in the soda do not collect on one side of the blob; they stay dispersed through it, since there is no buoyancy to sort them.

#### id 5, 6 — Buoyancy — **可直接用**

- `5` A piece of iron is gently placed on the surface of the water in a tank filled with water.
- `6` A stone is gently placed on the surface of a pool filled with water.

**Law as given.** (templated across the group)

> Due to buoyancy and density of objects, the iron block will sink

> Due to buoyancy and density of objects, the stone will sink

**Corrected.** Iron, stone and solid glass are several times denser than water, so the buoyant force cannot support them: each one goes under at once and descends to the bottom.

**Observables.**

- The object goes under immediately rather than resting on the surface or hesitating there.
- It accelerates briefly, then descends at a roughly steady rate, slower than it would fall through air.
- It stays on the bottom once it arrives and does not rise again on its own.
- The surface dips and ripples where the object enters, and the ripples spread outward and die away rather than persisting or converging.
- The water level rises slightly when the object is added and does not fall while it stays in.
- The submerged object still reads as being under water: it is tinted, blurred or displaced by refraction rather than looking as crisp as it did in air.

#### id 7 — Buoyancy — **需改写**  (`object-mismatch`)

- `7` A tennis ball is gently placed on the surface of a bucket filled with water.

**Law as given.**

> Due to buoyancy and density of objects, the wood block will float on the water

**Corrected.** A sealed, air-filled tennis ball is far less dense than water, so it floats, riding with roughly a third of its body below the surface.

**Observables.**

- The ball stays at the surface and never sinks below it.
- It settles to a definite waterline with most of its body above water.
- It bobs a few times with each swing smaller than the last, then comes to rest.
- The surface dips and ripples where the ball lands, and the ripples spread outward and die away.
- The water level rises slightly when the ball is added and does not fall while it stays in.
- The ball does not drift under on its own, nor lift clear of the water on its own.
- The felt surface wets and darkens where it sits in the water.

**Why it needs changing.** The law names a wood block; the caption places a tennis ball. The conclusion (floats) is right, the object is not -- copied from id 8.

#### id 8 — Buoyancy — **可直接用**

- `8` A piece of wood block is gently placed on the surface of a bowl filled with water.

**Law as given.**

> Due to buoyancy and density of objects, the wood block will float on the water

**Corrected.** Wood is less dense than water, so it floats: it settles at a waterline with part of its body above the surface.

**Observables.**

- The block stays at the surface and never sinks below it.
- It settles to a definite waterline with a visible part above water, rather than sitting entirely on top of the surface or entirely under it.
- It bobs a few times with each swing smaller than the last, then comes to rest.
- The surface dips and ripples where the block lands, and the ripples spread outward and die away.
- The water level rises slightly when the block is added and does not fall while it stays in.
- The block does not drift under on its own, nor lift clear of the water on its own.

#### id 9 — Buoyancy — **可直接用**

- `9` A glass ball is gently placed on the surface of a bathtub filled with water.

**Law as given.**

> Due to buoyancy and density of objects, the glass ball will sink

**Corrected.** Iron, stone and solid glass are several times denser than water, so the buoyant force cannot support them: each one goes under at once and descends to the bottom.

**Observables.**

- The object goes under immediately rather than resting on the surface or hesitating there.
- It accelerates briefly, then descends at a roughly steady rate, slower than it would fall through air.
- It stays on the bottom once it arrives and does not rise again on its own.
- The surface dips and ripples where the object enters, and the ripples spread outward and die away rather than persisting or converging.
- The water level rises slightly when the object is added and does not fall while it stays in.
- The submerged object still reads as being under water: it is tinted, blurred or displaced by refraction rather than looking as crisp as it did in air.

#### id 10, 11 — Stress — **可直接用**

- `10` A timelapse of a water-filled sponge being forcefully squeezed by hand, with the pressure intensifying rapidly over time.
- `11` A timelapse of a water-filled soft towel being forcefully squeezed by hand, with the pressure intensifying rapidly over time.

**Law as given.** (templated across the group)

> Due to stress, the sponge will shrink with the water in the sponge squeezed out

> Due to stress, the towel will shrink with the water in the towel squeezed out

**Corrected.** Squeezing a soaked porous material drives the water out of its pores: the material compresses under the hand while water runs from it, and it springs back only partly when released, still damp.

**Observables.**

- The material compresses only where and while the hand presses it, and it stops compressing when the hand stops.
- Water leaves the material while it is being compressed, running out at the squeezed region and falling away.
- The water that comes out came from inside: the material grows visibly less swollen and darker-wet at the point of squeeze, and the amount of water is bounded by what it held.
- The material springs back partly when the hand releases, not to its original swollen size, and it stays damp rather than dry.
- Water runs downward off the material and pools or falls; it does not climb it or hang in the air.
- No water is drawn back into the material once it has left.

#### id 12 — Stress — **需改写**

- `12` A timelapse of a balloon filled with air being pressed down by hand, with the pressure intensifying rapidly over time.

**Law as given.**

> Due to stress, the balloon will shrink and deformed

**Corrected.** Pressing an inflated, sealed balloon mostly changes its shape rather than its size: it flattens where the hand bears on it and bulges elsewhere, the trapped air being only slightly compressible, and it springs back fully when released.

**Observables.**

- The balloon flattens only where the hand presses, at the moment it presses.
- It bulges outward elsewhere while flattened at the contact, rather than shrinking all over.
- Its overall size stays roughly the same under hand pressure; it does not visibly deflate.
- It springs back to its original shape when the hand lifts, not staying dented.
- The rubber's surface markings stretch and crowd with the local deformation rather than sliding across a still surface.
- It bursts only if the rubber is stretched past its limit, and if it bursts the tearing starts at the loaded region and is irreversible.

**Why it needs changing.** 'Shrink' is wrong for a sealed air balloon under hand pressure: air is nearly incompressible at these loads, so the balloon changes shape at roughly constant volume. The law also omits the elastic recovery, which is the sharpest visible check.

#### id 13 — Stress — **可直接用**

- `13` A timelapse of a open toothpaste tube being squeezed by hand, with the pressure intensifying rapidly over time.

**Law as given.**

> Due to stress, Toothpaste will be squeezed out and the tube will deform with the toothpaste being dispensed

**Corrected.** Squeezing an open tube raises the pressure inside, so paste is forced out of the nozzle while the tube's wall dents and stays creased where it was pressed.

**Observables.**

- Paste comes out only while the tube is squeezed, from the open nozzle, and it stops when the squeeze stops.
- What comes out came from inside: the tube collapses and empties as paste leaves it, and the amount extruded is bounded by what the tube held.
- The tube dents where the fingers press and keeps the crease after they move on; it does not spring back perfectly plump.
- The paste holds the ribbon shape and roughly the cross-section of the nozzle it came from, sagging slowly rather than running like water.
- The extruded paste stays where it lands and is not drawn back into the tube.

#### id 14 — Stress — **可直接用**

- `14` A timelapse of a water-filled soft cloth being forcefully squeezed by hand, with the pressure intensifying rapidly over time.

**Law as given.**

> Due to stress, the cloth will shrink with the water in the cloth squeezed out

**Corrected.** Squeezing a soaked porous material drives the water out of its pores: the material compresses under the hand while water runs from it, and it springs back only partly when released, still damp.

**Observables.**

- The material compresses only where and while the hand presses it, and it stops compressing when the hand stops.
- Water leaves the material while it is being compressed, running out at the squeezed region and falling away.
- The water that comes out came from inside: the material grows visibly less swollen and darker-wet at the point of squeeze, and the amount of water is bounded by what it held.
- The material springs back partly when the hand releases, not to its original swollen size, and it stays damp rather than dry.
- Water runs downward off the material and pools or falls; it does not climb it or hang in the air.
- No water is drawn back into the material once it has left.

#### id 15, 16 — Atmosphere Pressure — **可直接用**

- `15` A timelapse of air being gradually and forcefully extracted from the mouth of an empty, thin, sealed plastic bottle.
- `16` A timelapse of air being gradually and forcefully extracted from a sealed, empty aluminum can.

**Law as given.** (templated across the group)

> Due to atmosphere pressure outside, the plastic bottle will be shrinking

> Due to atmospheric pressure outside, the aluminum can will be shrinking

**Corrected.** Pumping the air out of a sealed thin-walled vessel removes the internal pressure that was balancing the atmosphere outside, so the wall is pushed inward: it buckles and crumples, usually suddenly, and stays creased.

**Observables.**

- The vessel deforms only while air is being drawn out, and the deformation tracks the extraction rather than starting before it.
- The wall moves inward, never outward: no part of it bulges out while air is being removed.
- The collapse is a buckling, not a smooth uniform shrink: flat panels cave, sharp creases and facets appear, and the shape becomes irregular.
- It often gives way suddenly rather than at a constant rate, and it stays crumpled once it has collapsed.
- The vessel does not spring back to its original shape while the air is still out.
- The creases stay where they formed as the collapse continues; they do not migrate across the wall.

**Additionally for 15.**

- The thin plastic bottle crumples progressively and irregularly rather than collapsing all at once.

#### id 17 — Atmospheric Pressure — **需改写**

- `17` A timelapse of air being gradually and forcefully extracted from a sealed, empty plastic ball.

**Law as given.**

> Due to atmospheric pressure outside, the plastic ball will be shrinking

**Corrected.** A sealed hollow plastic ball has a stiff curved shell, so removing the air does not shrink it uniformly: one region dimples and caves inward, and the dent stays.

**Observables.**

- The ball deforms only while air is being drawn out.
- The wall moves inward, never outward.
- The deformation is a local dimple or cave-in on one side, not a uniform reduction in diameter with the ball staying round.
- The dent appears suddenly once the shell buckles, and it stays once formed.
- The ball does not spring back to round while the air is still out.
- The undented parts keep their original curvature and size.

**Why it needs changing.** A curved stiff shell does not shrink uniformly under external pressure; it buckles locally. 'Shrinking' invites a rubric item that would accept a ball smoothly reducing in diameter, which is not what happens.

#### id 18 — Atmosphere Pressure — **可直接用**

- `18` A timelapse of air being gradually and forcefully pulled out of an empty, thin, sealed aluminium can.

**Law as given.**

> Due to atmospheric pressure outside, the aluminium can will be crumpling

**Corrected.** Pumping the air out of a sealed thin-walled vessel removes the internal pressure that was balancing the atmosphere outside, so the wall is pushed inward: it buckles and crumples, usually suddenly, and stays creased.

**Observables.**

- The vessel deforms only while air is being drawn out, and the deformation tracks the extraction rather than starting before it.
- The wall moves inward, never outward: no part of it bulges out while air is being removed.
- The collapse is a buckling, not a smooth uniform shrink: flat panels cave, sharp creases and facets appear, and the shape becomes irregular.
- It often gives way suddenly rather than at a constant rate, and it stays crumpled once it has collapsed.
- The vessel does not spring back to its original shape while the air is still out.
- The creases stay where they formed as the collapse continues; they do not migrate across the wall.

#### id 19 — Atmosphere Pressure — **需改写**  (`mechanism-mislabelled`)

- `19` A timelapse of air being gradually and forcefully extracted from the interior of a thin, sealed balloon.

**Law as given.**

> Due to atmospheric pressure outside, the balloon will collapse inward.

**Corrected.** Drawing the air out of a balloon lets the stretched rubber contract: the balloon shrinks and wrinkles as it empties. The rubber's own elasticity does this, not the outside atmosphere.

**Observables.**

- The balloon shrinks only while air is being drawn out, and it stops when the extraction stops.
- It gets smaller all over as the stretched rubber recovers, rather than buckling with sharp creases like a rigid shell.
- Wrinkles and slack folds appear in the rubber as it deflates, and the surface markings crowd together with it.
- It does not re-inflate on its own while the air is still out.
- The neck stays sealed to whatever is drawing the air; the balloon does not deflate through a hole that is not there.

**Why it needs changing.** Mechanism mislabelled. An inflated balloon's rubber is under tension, so its internal pressure is already above atmospheric; it collapses by elastic recoil when emptied, not because the outside atmosphere crushes it. The visible result (shrinking, wrinkling) is right, and it is visibly different from the rigid-vessel cases (15-18) -- no buckling.

#### id 20 — Solid Pressure — **可直接用**

- `20` A hand slowly presses a needle into the surface of a fully inflated balloon, with the tip gradually penetrating the outer layer.

**Law as given.**

> Due to high pressure of the needle, the balloon will explode

**Corrected.** A needle or pin concentrates a modest force onto a tiny area, so the stress at the tip exceeds what the stretched rubber can take: the balloon fails at the point of contact and the tear runs away from it at once.

**Observables.**

- The balloon fails at the tip's point of contact, not anywhere else on its surface.
- It fails only once the tip has plainly reached and dented the rubber, not before contact.
- The rubber dents and stretches inward around the tip in the moments before it gives.
- Once it starts, the failure runs quickly and completely across the taut rubber rather than leaving a neat small hole in a still-inflated balloon.
- The failure is irreversible: the rubber does not close up and the balloon does not re-inflate.
- The freed rubber snaps away from the burst and then falls slack; it does not hold its inflated shape.
- The escaping air is invisible: nothing should be seen leaving the balloon except the moving rubber itself.

#### id 21, 22 — Solid Pressure — **可直接用**

- `21` A pencil slowly presses into the surface of a tightly stretched rubber sheet, with the tip gradually penetrating the outer layer.
- `22` A fork slowly presses a tensed piece of plastic wrap, with the tines gradually penetrating the outer layer.

**Law as given.** (templated across the group)

> Due to high pressure of the pencil, the rubber sheet will tear

> Due to high pressure of the fork, the plastic wrap will rupture

**Corrected.** A tip pressed into a taut sheet concentrates the load at the contact, so the sheet fails there once the local stress exceeds its strength: it tents inward first, then punctures and tears from that point.

**Observables.**

- The sheet fails at the point of contact, not elsewhere.
- It tents and stretches inward around the tip before it gives, and the tenting deepens as the tip advances.
- The failure happens only after contact, not before the tip arrives.
- The tear starts at the puncture and runs outward from it; it does not appear as a hole away from the tip.
- The failure is irreversible: the sheet does not close up.
- The freed edges relax and slacken as the tension is released.

**Additionally for 22.**

- A fork presses several tines at once, so several punctures appear together, one at each tine that reaches the wrap.

#### id 23 — Solid Pressure — **可直接用**

- `23` A pin slowly presses into the surface of a water-filled balloon, with the tip gradually penetrating the outer layer.

**Law as given.**

> Due to high pressure of the pin, the balloon will burst

**Corrected.** A needle or pin concentrates a modest force onto a tiny area, so the stress at the tip exceeds what the stretched rubber can take: the balloon fails at the point of contact and the tear runs away from it at once.

**Observables.**

- The balloon fails at the tip's point of contact, not anywhere else on its surface.
- It fails only once the tip has plainly reached and dented the rubber, not before contact.
- The rubber dents and stretches inward around the tip in the moments before it gives.
- Once it starts, the failure runs quickly and completely across the taut rubber rather than leaving a neat small hole in a still-inflated balloon.
- The failure is irreversible: the rubber does not close up and the balloon does not re-inflate.
- The freed rubber snaps away from the burst and then falls slack; it does not hold its inflated shape.
- The water inside is released as a coherent mass that then falls and spreads, and the emptied rubber is left limp and wet.
- The water goes downward and stays where it lands; it is not drawn back into the rubber.

#### id 24 — Solid Pressure — **需改写**  (`outcome-uncertain`)

- `24` A pencil slowly presses into the surface of a fully inflated balloon, with the tip gradually penetrating the outer layer.

**Law as given.**

> Due to high pressure of the pencil, the balloon will explode

**Corrected.** A blunt pencil pressed slowly onto an inflated balloon may or may not burst it: if the rubber is highly stretched it fails at the tip, but a rounded tip can also indent the rubber deeply without piercing. Judge whether what is shown is internally consistent, not whether it bursts.

**Observables.**

- The rubber dents and stretches inward around the pencil tip while it presses, and the dent deepens as the pencil advances.
- If the balloon bursts, it bursts at the tip's point of contact and only after contact.
- If it does not burst, the rubber stays intact and springs back when the pencil withdraws.
- A burst is irreversible: the rubber does not close up and the balloon does not re-inflate.
- The pencil is checked by the rubber's resistance rather than passing through as if nothing were there.
- Whichever happens, it happens once: the balloon does not burst, recover and burst again.

**Why it needs changing.** The outcome is not determined by the physics as captioned. A pencil is blunt compared with a needle, and slow pressing on a balloon is the classic case that can go either way. Mandating 'will explode' would penalise a physically correct clip.

#### id 25, 26, 27, 28, 29 — Elasticity — **可直接用**

- `25` A vibrant, elastic rubber ball is thrown forcefully towards the ground, capturing its dynamic interaction with the surface upon impact.
- `26` A vibrant, elastic basketball is thrown forcefully towards the ground, capturing its dynamic interaction with the surface upon impact.
- `27` A vibrant, elastic tennis ball is thrown forcefully towards the ground, capturing its dynamic interaction with the surface upon impact.
- `28` A vibrant, elastic football is thrown forcefully towards the ground, capturing its dynamic interaction with the surface upon impact.
- `29` A vibrant, elastic beach ball is thrown forcefully towards the ground, capturing its dynamic interaction with the surface upon impact.

**Law as given.** (templated across the group)

> Due to elasticity, the elastic rubber ball will bounce up

> Due to elasticity, the elastic basketball will bounce up

> Due to elasticity, the elastic tennis ball will bounce up

> Due to elasticity, the elastic football will bounce up

> Due to elasticity, the elastic beach ball will bounce up

**Corrected.** A ball thrown at the ground deforms on contact and pushes back off it, so it rebounds -- but always more slowly than it arrived, since some energy is lost in the deformation. Successive bounces are lower and closer together.

**Observables.**

- The ball reverses direction at the ground, at the moment of contact, and not a gap above it.
- It leaves the ground more slowly than it arrived, so the rebound rises less high than the throw came from.
- Each successive bounce is lower than the one before and the intervals between bounces get shorter; the sequence never grows.
- Between bounces the ball follows a single arc, speeding up as it falls and slowing as it rises, with no kink or hover in mid-air.
- The ball flattens against the ground at the contact and recovers its round shape as it leaves; it does not stay dented.
- The rebound direction follows the approach: a ball thrown straight down comes back up, one thrown at an angle comes off on the mirrored line.
- The ball's motion only ever loses energy: it does not speed up in flight or bounce higher than the previous bounce.

**Additionally for 26.**

- The basketball's contact flattening is visible and brief, and it rebounds high -- a substantial fraction of the drop.

**Additionally for 29.**

- Being very light for its size, the beach ball is slowed noticeably by the air: it decelerates between bounces and its rebounds die away quickly.

#### id 30 — Friction — **可直接用**

- `30` A piece of white chalk is used to write on the rough, dark surface of a blackboard,showcasing the interaction between the chalk and the blackboard surface.

**Law as given.**

> Due to friction, there will be chalk mark on the blackboard

**Corrected.** Dragging a soft solid stick across a rough surface abrades material off it and leaves it behind: a mark appears along the path travelled, and the stick itself is worn down.

**Observables.**

- The mark appears only where the tip has passed, at the moment it passes, and it follows the path exactly.
- The leading end of the mark advances with the tip and never runs ahead of it.
- No mark appears where the tip was lifted clear of the surface.
- The mark is permanent unless something wipes it: it does not fade or retract on its own.
- The stick is consumed as it writes -- it shortens or blunts -- and loose dust or crumbs are shed at the contact.
- The mark's colour is the stick's own, laid over the surface's colour rather than replacing the surface.
- Chalk dust falls from the contact and settles below, and the mark reads as a dry powdery deposit that could be smudged.

#### id 31 — Friction — **需改写**  (`mechanism-mislabelled`)

- `31` A blue marker is used to write on the smooth, white surface of a whiteboard, showcasing the interaction between the marker and the whiteboard surface.

**Law as given.**

> Due to friction, there will be a marker mark on the whiteboard

**Corrected.** A pen, marker or highlighter leaves a mark by depositing ink onto the surface, not by friction: the ink wets the surface where the tip has passed. Friction only turns a ballpoint's ball; nothing is abraded off the tip.

**Observables.**

- The mark appears only where the tip has passed, at the moment it passes, and it follows the path exactly.
- The leading end of the mark advances with the tip and never runs ahead of it.
- No mark appears where the tip was lifted clear of the surface.
- The mark is wet ink laid on the surface: its colour is the ink's own and it may spread slightly or soak in, rather than sitting as powder on top.
- The mark is permanent unless something wipes it: it does not fade or retract on its own.
- The pen or marker is not visibly consumed by writing -- no dust or crumbs are shed at the contact.

**Why it needs changing.** Mechanism mislabelled: the mark is ink deposition (capillary wetting, or ink transferred by a rolling ball), not friction-driven abrasion. The visible outcome -- a mark along the path -- is right, but the correct rubric must not require shedding or wear at the tip, which is what a friction claim implies.

#### id 32 — Friction — **可直接用**

- `32` A piece of red crayon is used to draw on the rough, white surface of a paper, showcasing the interaction between the crayon and the paper surface.

**Law as given.**

> Due to friction, there will be a crayon mark on the paper

**Corrected.** Dragging a soft solid stick across a rough surface abrades material off it and leaves it behind: a mark appears along the path travelled, and the stick itself is worn down.

**Observables.**

- The mark appears only where the tip has passed, at the moment it passes, and it follows the path exactly.
- The leading end of the mark advances with the tip and never runs ahead of it.
- No mark appears where the tip was lifted clear of the surface.
- The mark is permanent unless something wipes it: it does not fade or retract on its own.
- The stick is consumed as it writes -- it shortens or blunts -- and loose dust or crumbs are shed at the contact.
- The mark's colour is the stick's own, laid over the surface's colour rather than replacing the surface.
- The wax mark sits on the raised texture of the paper and skips the hollows, so it reads broken rather than solid.

#### id 33, 34 — Friction — **需改写**  (`mechanism-mislabelled`)

- `33` A yellow highlighter is used to mark on the rough, brown surface of a cardboard, showcasing the interaction between the highlighter and the cardboard surface.
- `34` A black pen is used to write on the smooth, white surface of a notebook, showcasing the interaction between the pen and the notebook surface.

**Law as given.** (templated across the group)

> Due to friction, there will be a highlighter mark on the cardboard

> Due to friction, there will be a pen mark on the notebook

**Corrected.** A pen, marker or highlighter leaves a mark by depositing ink onto the surface, not by friction: the ink wets the surface where the tip has passed. Friction only turns a ballpoint's ball; nothing is abraded off the tip.

**Observables.**

- The mark appears only where the tip has passed, at the moment it passes, and it follows the path exactly.
- The leading end of the mark advances with the tip and never runs ahead of it.
- No mark appears where the tip was lifted clear of the surface.
- The mark is wet ink laid on the surface: its colour is the ink's own and it may spread slightly or soak in, rather than sitting as powder on top.
- The mark is permanent unless something wipes it: it does not fade or retract on its own.
- The pen or marker is not visibly consumed by writing -- no dust or crumbs are shed at the contact.

**Additionally for 33.**

- The highlighter's ink is translucent: what is underneath still reads through the mark rather than being covered over.

**Why it needs changing.** Mechanism mislabelled: the mark is ink deposition (capillary wetting, or ink transferred by a rolling ball), not friction-driven abrasion. The visible outcome -- a mark along the path -- is right, but the correct rubric must not require shedding or wear at the tip, which is what a friction claim implies.

#### id 35 — Surface Tension — **可直接用**

- `35` A glistening dewdrop is sliding gracefully across the textured surface of a lotus leaf, accentuating its shape as it moves

**Law as given.**

> Due to surface tension, the dewdrop will form spherical droplets

**Corrected.** On a water-repellent surface the drop's own surface tension wins over its attraction to the surface, so it beads up into a near-sphere, touches over a small area, and rolls freely with almost nothing left behind.

**Observables.**

- The drop holds a rounded, near-spherical shape while it sits and while it moves, rather than flattening into a film.
- It meets the surface over a small contact patch, with a steep edge where liquid meets solid.
- It rolls or slides as one body and keeps its shape while moving; it does not stretch into a streak.
- It leaves the surface behind dry: no wet trail, no darkened path where it has passed.
- It moves downhill or with whatever pushes it, and it does not climb the surface on its own.
- If it meets another drop they merge into one larger drop and the merged drop is rounder than a dumbbell, settling quickly.
- The drop is transparent: it refracts and brightens what is behind it, and carries a small specular highlight that stays put relative to the light while the drop moves.
- On the lotus leaf the drop sits especially high and round, riding on the leaf's microtexture, and it detaches and rolls at the slightest tilt.

#### id 36 — Surface Tension — **需改写**

- `36` A glistening dewdrop is sliding gracefully across the smooth surface of a glass, accentuating its shape as it moves

**Law as given.**

> Due to surface tension, the dewdrop will form spherical droplets

**Corrected.** Bare glass and glazed ceramic are wettable, so water does not stay spherical on them: the drop flattens into a low dome, spreads its contact patch, tends to stick rather than slide, and leaves a wet trail if it does move.

**Observables.**

- The drop reads as a flattened dome, not a sphere: it is plainly wider than it is tall.
- Its edge meets the surface at a shallow angle, spread over a broad contact patch.
- It resists moving, and when it does move it stretches and leaves a wet trail or a darkened, glossy path behind it.
- Some liquid is left behind as it moves: the drop shrinks or breaks into a trail of smaller drops rather than travelling as one intact bead.
- It does not climb the surface on its own.
- The drop is transparent: it refracts what is behind it and carries a specular highlight.

**Why it needs changing.** Bare glass and glazed ceramic are hydrophilic; water spreads on them. Requiring 'spherical droplets' here would mark a physically correct clip wrong. Only the repellent surfaces (lotus leaf, waxed apple) support the spherical claim.

#### id 37 — Surface Tension — **可直接用**

- `37` A glistening dewdrop is sliding gracefully across the smooth surface of a waxed apple, accentuating its shape as it moves

**Law as given.**

> Due to surface tension, the dewdrop will form spherical droplets

**Corrected.** On a water-repellent surface the drop's own surface tension wins over its attraction to the surface, so it beads up into a near-sphere, touches over a small area, and rolls freely with almost nothing left behind.

**Observables.**

- The drop holds a rounded, near-spherical shape while it sits and while it moves, rather than flattening into a film.
- It meets the surface over a small contact patch, with a steep edge where liquid meets solid.
- It rolls or slides as one body and keeps its shape while moving; it does not stretch into a streak.
- It leaves the surface behind dry: no wet trail, no darkened path where it has passed.
- It moves downhill or with whatever pushes it, and it does not climb the surface on its own.
- If it meets another drop they merge into one larger drop and the merged drop is rounder than a dumbbell, settling quickly.
- The drop is transparent: it refracts and brightens what is behind it, and carries a small specular highlight that stays put relative to the light while the drop moves.

#### id 38 — Surface Tension — **需改写**

- `38` A glistening dewdrop is sliding gracefully across the smooth surface of a ceramic vase, accentuating its shape as it moves

**Law as given.**

> Due to surface tension, the drop of water will form spherical droplets

**Corrected.** Bare glass and glazed ceramic are wettable, so water does not stay spherical on them: the drop flattens into a low dome, spreads its contact patch, tends to stick rather than slide, and leaves a wet trail if it does move.

**Observables.**

- The drop reads as a flattened dome, not a sphere: it is plainly wider than it is tall.
- Its edge meets the surface at a shallow angle, spread over a broad contact patch.
- It resists moving, and when it does move it stretches and leaves a wet trail or a darkened, glossy path behind it.
- Some liquid is left behind as it moves: the drop shrinks or breaks into a trail of smaller drops rather than travelling as one intact bead.
- It does not climb the surface on its own.
- The drop is transparent: it refracts what is behind it and carries a specular highlight.

**Why it needs changing.** Bare glass and glazed ceramic are hydrophilic; water spreads on them. Requiring 'spherical droplets' here would mark a physically correct clip wrong. Only the repellent surfaces (lotus leaf, waxed apple) support the spherical claim.

#### id 39 — Surface Tension — **需改写**  (`premise-implausible`)

- `39` A glistening dewdrop is sliding gracefully across the textured surface of a book, accentuating its shape as it moves

**Law as given.**

> Due to surface tension, the dewdrop will form spherical droplets

**Corrected.** Paper absorbs water. A dewdrop placed on a book does not slide across it as a bead: it wicks into the fibres, spreading as a darkened stain that grows and stops growing, and it cannot travel across the surface at all.

**Observables.**

- The drop soaks in where it touches rather than beading up and remaining intact.
- A darkened wet patch spreads outward from the contact and its edge advances, then stops.
- The wet patch never shrinks or retreats on its own; drying is slow and uniform, not a receding edge.
- The drop does not travel across the page as an intact bead, and it leaves no dry surface behind it.
- The paper itself answers the water: the wetted region darkens, and it may cock, wrinkle or buckle as the fibres swell.
- Ink or print under the wet patch may bleed or darken but does not move across the page.

**Why it needs changing.** The caption's premise is physically impossible: water does not slide gracefully across paper, it is absorbed. The rubric must judge absorption, and the fact that no sliding bead appears is a fault of the caption, not of a clip that shows soaking. Semantic adherence and physical plausibility pull in opposite directions here.

### Light

#### id 40, 41 — Direct Radiation — **可直接用**

- `40` A ray of light is shining diagonally on a wooden block in the dark, with the shadow of the wooden block appearing at the bottom.
- `41` A ray of light is shining diagonally on a metal can in the dark, with the shadow of the metal can appearing at the bottom.

**Law as given.** (templated across the group)

> Due to direct radiation of light, the light path will be blocked by the wooden block, thus the shadow of the wooden block will appear at the bottom

> Due to direct radiation of light, the light path will be blocked by the metal can, thus the shadow of the metal can will appear at the bottom.

**Corrected.** An opaque body in a beam blocks the light, so a shadow of its own outline falls on the surface beyond it, on the far side from the source and along the beam's direction.

**Observables.**

- A shadow is present on the surface beyond the object while the beam is on.
- The shadow lies on the opposite side of the object from the light source, never between them.
- Its outline matches the object's silhouette as seen from the source.
- Because the beam comes in diagonally, the shadow is stretched away from the source rather than sitting symmetrically under the object.
- The shadow moves and stretches consistently with the object and the source: if either moves, it tracks that movement; if both are still, it is still.
- The lit face of the object is the face turned toward the source, and the shadowed face is the one turned away.
- The shadowed region is darker than the surrounding lit surface, and it disappears if the beam is cut.

#### id 42 — Direct Radiation — **需改写**

- `42` A ray of light is shining diagonally on a glass bottle in the dark, with the shadow of the glass bottle appearing at the bottom.

**Law as given.**

> Due to direct radiation of light, the light path will be blocked by the glass bottle, thus the shadow of the glass bottle will appear at the bottom.

**Corrected.** A clear glass bottle transmits and refracts the beam rather than blocking it: the region beyond it is not a dark shadow but a faint outline crossed by bright concentrated bands (caustics), because the curved glass focuses the light that passes through.

**Observables.**

- Light plainly passes through the bottle: the region beyond it is not uniformly dark.
- Bright concentrated streaks or bands appear within or beside the bottle's outline on the surface -- brighter than the surrounding lit surface, not darker.
- Only the opaque parts (a label, a cap, thick seams) cast genuinely dark shadow.
- The bright bands and the faint outline lie away from the source along the beam and stretch because it is diagonal.
- The bottle's body lights up internally where the beam crosses it.
- Everything -- outline, caustics, internal glow -- vanishes if the beam is cut, and moves consistently if the bottle or the source moves.

**Why it needs changing.** Glass is transparent. The law's claim that the light path 'will be blocked by the glass bottle' is false, and a verbatim rubric would reward a clip showing a solid dark shadow -- exactly the wrong physics. The distinctive correct signature is a bright caustic, not a shadow.

#### id 43 — Direct Radiation — **需改写**

- `43` A ray of light is shining diagonally on a plastic cup in the dark, with the shadow of the plastic cup appearing at the bottom.

**Law as given.**

> Due to direct radiation of light, the light path will be blocked by the plastic cup, thus the shadow of the plastic cup will appear at the bottom.

**Corrected.** A translucent plastic cup only partly blocks the beam: it casts a soft, incomplete shadow with light coming through it, brighter than the shadow of an opaque body, and the cup itself glows where the beam enters.

**Observables.**

- A shadow region is present beyond the cup, on the far side from the source.
- The shadow is partial rather than dark: light plainly passes through the cup, so its shadow is lighter than the shadow of an opaque object would be.
- The cup's wall glows where the beam enters it, and the light spreads within the wall.
- The shadow's outline follows the cup's silhouette but is soft-edged rather than sharp.
- The shadow lies away from the source along the beam and stretches because the beam is diagonal.
- Shadow and glow both vanish if the beam is cut.

**Why it needs changing.** A plastic cup is translucent, not opaque. Stating flatly that the beam 'will be blocked' invites a rubric item that requires a full dark shadow and would fail a correct clip showing light passing through.

#### id 44 — Direct Radiation — **可直接用**

- `44` A ray of light is shining diagonally on a cardboard box in the dark, with the shadow of the cardboard box appearing at the bottom.

**Law as given.**

> Due to direct radiation of light, the light path will be blocked by the cardboard box, thus the shadow of the cardboard box will appear at the bottom.

**Corrected.** An opaque body in a beam blocks the light, so a shadow of its own outline falls on the surface beyond it, on the far side from the source and along the beam's direction.

**Observables.**

- A shadow is present on the surface beyond the object while the beam is on.
- The shadow lies on the opposite side of the object from the light source, never between them.
- Its outline matches the object's silhouette as seen from the source.
- Because the beam comes in diagonally, the shadow is stretched away from the source rather than sitting symmetrically under the object.
- The shadow moves and stretches consistently with the object and the source: if either moves, it tracks that movement; if both are still, it is still.
- The lit face of the object is the face turned toward the source, and the shadowed face is the one turned away.
- The shadowed region is darker than the surrounding lit surface, and it disappears if the beam is cut.

#### id 45, 46, 47, 48, 49, 50, 51, 52, 53, 54 — Tyndall Effect — **可直接用**

- `45` A concentrated, bright beam of light generated by a laser pointer is passing through a glass of thick whole milk, creating a mesmerizing display as the light interacts with the milk's particles, casting intricate patterns and subtle hues within the fluid. 
- `46` A concentrated, bright beam of light generated by a flashlight is passing through a bowl of murky water, creating a mesmerizing display as the light interacts with the water's particles, casting intricate patterns and subtle hues within the fluid.
- `47` A focused, bright beam of light generated by a car headlight is passing through a jar of dusty air, creating a mesmerizing display as the light interacts with the dust particles, casting intricate patterns and subtle hues within the air.
- `48` A directed, bright beam of light generated by a phone flashlight is passing through a container of stirred muddy water, creating a mesmerizing display as the light interacts with the mud particles, casting intricate patterns and subtle hues within the fluid.
- `49` A narrow, bright beam of light generated by a reading lamp is passing through a bottle of mixed orange juice, creating a mesmerizing display as the light interacts with the juice particles, casting intricate patterns and subtle hues within the liquid.
- `50` A ray of light generated by headlights is passing through heavy fog
- `51` A ray of light generated by a flashlight is passing through a dusty room.
- `52` A ray of light generated by a laser pointer is passing through smoke.
- `53` A ray of light generated by a flashligh is passing through thick mist.
- `54` A ray of light generated by a projector is passing through a dark room with fine dust particles.

**Law as given.** (templated across the group)

> Due to tyndall effect, there will be a clearly visible light path in the milk

> Due to tyndall effect, there will be a clearly visible light path in the water

> Due to tyndall effect, there will be a clearly visible light path in the air

> Due to tyndall effect, there will be a clearly visible light path in the muddy water

> Due to tyndall effect, there will be a clearly visible light path in the juice

> Due to tyndall effect, there will be a clearly visible light path in the fog

> Due to tyndall effect, there will be a clearly visible light path in the dust

> Due to tyndall effect, there will be a clearly visible light path in the smoke

> Due to tyndall effect, there will be a clearly visible light path in the mist

**Corrected.** A beam crossing a medium full of suspended particles or droplets is scattered sideways along its path, so the beam itself becomes visible as a luminous line or cone from the side.

**Observables.**

- The beam is visible as a line or cone through the medium, not just as a spot where it lands.
- The visible path starts at the source's aperture and runs in a straight line in the direction the source is pointed.
- The path is only visible inside the scattering medium: it is fainter or absent in the clear air or clear liquid before and after it.
- The beam dims and spreads with distance into the medium as light is scattered out of it, rather than staying equally bright all the way through or brightening.
- The path moves with the source: aim the source elsewhere and the visible line follows immediately, keeping its straight geometry.
- The path vanishes when the source is switched off, and nothing glows in the medium without the beam.
- Where the beam meets a wall or the far side it makes a bright spot, and that spot lies on the beam's straight continuation.

**Additionally for 45.**

- Whole milk scatters strongly, so the beam penetrates only a short way into the glass and diffuses into a glow rather than crossing it cleanly.

**Additionally for 47.**

- Individual dust motes drifting through the beam glint as they cross it and go dark as they leave it.

**Additionally for 51.**

- Individual dust motes drifting through the beam glint as they cross it and go dark as they leave it.

**Additionally for 52.**

- Smoke drifting across the beam distorts and thickens the visible path where it passes, and the path recovers when the smoke moves on.

**Additionally for 54.**

- Individual dust motes drifting through the beam glint as they cross it and go dark as they leave it.

**Why it needs changing (id 45).** The law itself is right. The caption is what over-claims: 'casting intricate patterns and subtle hues' is decoration -- Tyndall scattering gives a plain luminous path, not patterns or hues. Treat that phrase as a caption-adherence matter, and do not turn it into a physics requirement, or a correct clip showing a clean beam would be penalised for not inventing colours.

#### id 55, 56, 57, 58, 59 — Reflection — **需改写**

- `55` A bird is flying over a calm and clear lake surface, with the reflection of the bird appearing on the water surface.
- `56` A kite is soaring above a smooth and tranquil pond, with the reflection of the kite appearing on the water surface.
- `57` A plane is gliding over a still and crystal-clear river, with the reflection of the plane appearing on the water surface.
- `58` A drone is hovering above a quiet and glassy swimming pool, with the reflection of the drone appearing on the water surface.
- `59` A balloon is floating over a serene and mirror-like ocean, with the reflection of the balloon appearing on the water surface.

**Law as given.** (templated across the group)

> Due to reflection, the lake will present inverted images of the bird, the sky and the surrounding landscapes, which are the same size as the original entities

> Due to reflection, the pond will present inverted images of the kite, the sky and the surrounding landscapes, which are the same size as the original entities

> Due to reflection, the river will present inverted images of the plane, the sky and the surrounding landscapes, which are the same size as the original entities

> Due to reflection, the swimming pool will present inverted images of the drone, the sky and the surrounding landscapes, which are the same size as the original entities

> Due to reflection, the ocean will present inverted images of the balloon, the sky and the surrounding landscapes, which are the same size as the original entities

**Corrected.** A calm water surface acts as a plane mirror: it shows the object, the sky and the shore mirrored about the water plane -- upside down, moving in step with the original, and dimmer and tinted by the water. The mirror image is the same size as the object itself, but it lies farther from the camera along the light path, so on screen it appears equal or slightly smaller, never larger.

**Observables.**

- A reflection of the object is present in the water while the object is above it.
- The reflection is inverted -- mirrored about the water line, not a second upright copy.
- It moves in step with the object: same horizontal direction, same timing, no lag or independent drift.
- It appears equal in size or slightly smaller on screen, never larger than the object.
- It is dimmer and tinted by the water rather than as bright and crisp as the object itself.
- The sky and the surroundings are mirrored in the same water at the same time, consistently with the object's reflection.
- Ripples or disturbances break the reflection up where they pass and it re-forms as the water settles; a perfectly still reflection on visibly rippled water is wrong.
- The reflection shows the object's underside -- the face turned toward the water -- not the face turned toward the camera.

**Why it needs changing.** 'The same size as the original entities' is true of the virtual image in object space, but not of its apparent size on screen: the reflected ray path is longer than the direct one, so the reflection subtends a smaller angle. Taken verbatim as a rubric item it would fail a correct clip. The stronger, genuinely checkable claims -- inversion, synchronised motion, reduced brightness, break-up by ripples -- are absent from the law.

#### id 60 — Reflection — **可直接用**

- `60` A wooden block is moving closer to an upright mirror, with the reflection in the mirror moving closer synchronously.

**Law as given.**

> Due to reflection, the image in the mirror should be the same size as the original wooden block

**Corrected.** A plane mirror forms an image the same size as the object, as far behind the mirror as the object is in front. As the object approaches, the image approaches from the other side at the same rate, so the gap between them closes at twice the object's speed and they meet at the surface.

**Observables.**

- An image of the object is present in the mirror throughout.
- It is the same size as the object and upright, not inverted.
- It moves toward the mirror as the object does, in step and at the same rate.
- The gap between object and image closes at twice the object's own speed, and they meet at the mirror's surface -- the image does not stop short of it or pass through.
- The image is left-right reversed relative to the object.
- The image's distance behind the mirror always matches the object's distance in front.
- The image is dimmer than the object but otherwise the same shape and colour.

#### id 61 — Reflection — **可直接用**

- `61` A football is rolling towards a vertical window, with the reflection in the window moving closer synchronously.

**Law as given.**

> Due to reflection, the image in the window should be the same size as the original football

**Corrected.** A window pane and a polished metal surface both reflect part of the light that reaches them, so they carry an image of the approaching object -- fainter than a mirror's, and tinted by the surface, but with the same geometry: same size for a flat surface, approaching in step.

**Observables.**

- An image of the object is present in the reflecting surface throughout.
- It moves toward the surface as the object does, in step and at the same rate.
- It is upright and left-right reversed, not inverted.
- It is plainly fainter than the object, and tinted by the surface rather than a perfect copy.
- Its distance behind the surface matches the object's distance in front, so the two meet at the surface.
- If the reflecting surface is flat, the image is the same size as the object; if it is curved, the image is distorted and compressed consistently with that curvature.
- Whatever else faces the surface is reflected in it at the same time, consistently with the object's reflection.
- Because the window is transparent, what is behind it is visible through the reflection at the same time.

#### id 62 — Reflection — **需改写**  (`outcome-uncertain`)

- `62` A toy car is driving towards a standing glass, with the reflection in the glass moving closer synchronously.

**Law as given.**

> Due to reflection, the image in the glass should be the same size as the original toy car

**Corrected.** What 'a standing glass' means decides the answer. A flat glass pane reflects an upright, same-size, left-right reversed image approaching in step. A drinking glass is a curved, part-filled body: its reflection is compressed and distorted, it is smaller than the object, and it is accompanied by refracted views of the car through the glass.

**Observables.**

- An image of the toy car is present in the glass throughout, moving toward it in step with the car.
- The image is upright rather than inverted.
- It is plainly fainter than the car itself, since only part of the light is reflected.
- If the glass is a flat pane, the image is the same size as the car and its distance behind the surface matches the car's distance in front.
- If the glass is a curved vessel, the image is compressed and distorted rather than a faithful same-size copy, and the distortion is consistent across the whole image.
- The car is also visible through the glass, refracted and displaced, at the same time as the reflection.

**Why it needs changing.** The caption is ambiguous between a glass pane and a drinking glass, and the two give visibly different correct answers. The law's 'same size' claim only holds for a flat pane; applied to a drinking glass it would fail a correct clip.

#### id 63 — Reflection — **可直接用**

- `63` A basketball is being moved closer to a shiny metallic surface, with the reflection on the metallic surface moving closer synchronously.

**Law as given.**

> Due to reflection, the image on the metallic surface should be the same size as the original basketball

**Corrected.** A window pane and a polished metal surface both reflect part of the light that reaches them, so they carry an image of the approaching object -- fainter than a mirror's, and tinted by the surface, but with the same geometry: same size for a flat surface, approaching in step.

**Observables.**

- An image of the object is present in the reflecting surface throughout.
- It moves toward the surface as the object does, in step and at the same rate.
- It is upright and left-right reversed, not inverted.
- It is plainly fainter than the object, and tinted by the surface rather than a perfect copy.
- Its distance behind the surface matches the object's distance in front, so the two meet at the surface.
- If the reflecting surface is flat, the image is the same size as the object; if it is curved, the image is distorted and compressed consistently with that curvature.
- Whatever else faces the surface is reflected in it at the same time, consistently with the object's reflection.
- The metal tints the reflection toward its own colour and blurs fine detail.

#### id 64 — Reflection — **需改写**  (`premise-implausible`)

- `64` A rubber duck is floating closer to a calm water surface, with the reflection in the water moving closer synchronously.

**Law as given.**

> Due to reflection, the image in the water should be the same size as the original rubber duck

**Corrected.** A duck already floating on the water cannot move closer to that surface. What is checkable is the reflection of a floating body: it is joined to the duck at the waterline, inverted below it, moves with it, and is broken up by the ripples the duck itself makes.

**Observables.**

- A reflection of the duck is present in the water beneath it.
- The reflection is inverted and joined to the duck at the waterline, with no gap between duck and image.
- It moves with the duck, in step and in the same horizontal direction.
- It is dimmer than the duck and tinted by the water.
- The duck's own ripples break the reflection up as they spread, and it re-forms as the water settles.
- The reflection shows the duck's submerged-facing side, not the face turned to the camera.
- The duck floats at a steady waterline while all this happens; it neither sinks nor lifts clear of the water.

**Why it needs changing.** The caption's premise is incoherent -- a floating object is already at the surface, so 'floating closer to a calm water surface' names no motion. The reflection geometry for a floating body is different from the airborne cases (55-59): image and object touch at the waterline.

#### id 65, 66, 67, 68, 69 — Refraction — **需改写**

- `65` A magnifying glass is gradually moving closer to the pages of an open book, revealing the intricate details and textures of the printed text as it approaches.
- `66` A magnifying glass is gradually moving closer to the face of a wristwatch, revealing the intricate details and textures of the clock hands and numbers as it approaches.
- `67` A magnifying glass is gradually moving closer to a leaf, revealing the intricate details and textures of the veins and surface patterns as it approaches.
- `68` A magnifying glass is gradually moving closer to a coin, revealing the intricate details and textures of the embossed design as it approaches.
- `69` A magnifying glass is gradually moving closer to the petals of a flower, revealing the intricate details and textures of the flower as it approaches.

**Law as given.** (templated across the group)

> Due to refraction, the characters in the magnifying glass should be bigger than those in the book

> Due to refraction, the clock hands and numbers in the magnifying glass should be bigger than those on the wristwatch

> Due to refraction, the veins and surface patterns in the magnifying glass should be bigger than those on the leaf

> Due to refraction, the embossed design in the magnifying glass should be bigger than those on the coin

> Due to refraction, the details in the magnifying glass should be bigger than those on the flower

**Corrected.** A converging lens magnifies only while the object is inside its focal length. Held far from the page it forms a small INVERTED image; as it is brought closer the image grows and blurs through the focal distance, and only inside it does the familiar upright magnified view appear. Both regimes are correct physics.

**Observables.**

- Whatever is seen through the lens differs from what is seen beside it: the lens changes the view rather than acting as a plain window.
- Close in, the view through the lens is upright and larger than the same detail outside the lens rim.
- Held far off, the view through the lens is inverted and small -- this is correct, not a fault.
- The transition between the two is continuous: the image grows, blurs out near the focal distance, and flips; it does not jump between states.
- The magnification changes smoothly as the lens moves, and it changes in one direction while the lens moves in one direction.
- The magnified content matches the actual content underneath -- the same words, marks or patterns, enlarged, not different ones.
- The rim of the lens marks a sharp discontinuity: content jumps in scale across it, and the content just inside the rim connects to the content just outside.
- The lens's own outline and the hand holding it are not magnified.

**Why it needs changing.** The law states only the end state. A physically faithful clip that starts with the lens far from the page shows a small inverted image first, which a verbatim rubric item ('should be bigger') would mark wrong. The focal-length regime change is the sharpest available discriminator and is missing from the law.

#### id 70, 71, 72, 73, 74 — Refraction — **可直接用**

- `70` A clear plastic straw is slowly inserted into a glass of crystal-clear water, revealing the fascinating visual changes and reflections that occur as the straw interacts with the liquid.
- `71` A silver spoon is slowly inserted into a glass of crystal-clear water, revealing the fascinating visual changes and reflections as the spoon interacts with the liquid.
- `72` A wooden pencil is carefully dipped into a glass of crystal-clear water, showing the intriguing visual shifts and reflections caused by the interaction between the pencil and the liquid.
- `73` A metal fork is gently placed into a glass of crystal-clear water, displaying the interesting visual distortions and reflections as the fork meets the liquid.
- `74` A plastic ruler is slowly submerged into a glass of crystal-clear water, highlighting the noticeable visual changes and reflections as the ruler interacts with the liquid.

**Law as given.**

> Due to refraction, the part above water and the part in water will have a tiny offset at the water surface

**Corrected.** Light from the submerged part of the object bends as it leaves the water, so that part appears displaced and raised relative to the part above: the object looks broken or kinked exactly at the water line, and the submerged part looks shallower and wider.

**Observables.**

- The object appears to change direction exactly at the water surface, not above or below it.
- The break appears only once the object is partly in the water, and it grows as more of the object goes in.
- The submerged part appears displaced sideways from the straight continuation of the part above, and appears shorter or raised rather than reaching as deep as it really does.
- The submerged part appears wider or magnified compared with the part in air.
- The apparent kink tracks the object: tilt or move it and the offset changes with it, vanishing when the object is vertical to the line of sight.
- The part above water is undistorted and continues in a straight line.
- The water surface also reflects: a partial mirror image of the object appears at the surface alongside the refracted view.
- Insertion disturbs the water -- ripples spread from the entry and the surface line wobbles, which makes the apparent break wobble with it.

**Additionally for 71.**

- The polished spoon also reflects its surroundings, so the refracted submerged bowl and the reflected room are both visible at once.

**Additionally for 73.**

- Each tine of the fork breaks at the same water line, all by the same offset and in the same direction.

**Additionally for 74.**

- The ruler's printed graduations let the offset be seen directly: the marks above and below the surface no longer line up.

#### id 75, 76 — Interference & Diffraction — **可直接用**

- `75` A large number of soap bubbles are floating in the air under the sunlight.
- `76` A group of oil droplets is floating on the surface of water in the sunlight.

**Law as given.** (templated across the group)

> Due to interference & diffraction, the bubbles will be colorful

> Due to interference & diffraction, the droplets will be colorful

**Corrected.** A film only a few wavelengths thick makes light reflected from its front and back surfaces interfere, so the colour seen depends on the local thickness and the viewing angle: swirling iridescent bands that shift as the film drains or as the view changes.

**Observables.**

- The colours appear as bands or swirls that vary across the film, not as one uniform tint.
- The colours shift when the film moves, drains or is seen from a different angle, rather than being painted on and fixed to the surface.
- The bands follow the film's thickness pattern and move with the film's flow, staying attached to the fluid rather than sliding across it.
- The palette is the iridescent sequence -- magenta, gold, cyan, green -- rather than arbitrary saturated colours.
- The colours are only present where the film is thin: thicker regions and the surrounding bulk liquid are colourless.
- The colours are a surface effect: what lies behind or under the film still reads through it.
- The effect requires light: it dims with the light and vanishes in shadow.

**Additionally for 75.**

- Each bubble carries its own independent pattern, and the pattern moves and rotates with that bubble.
- A bubble that bursts disappears entirely and does not re-form.

**Additionally for 76.**

- The coloured patches spread and are carried by the water's surface flow, changing shape as they go.

#### id 77 — Interference & Diffraction — **建议排除**

- `77` Several glass marbles are placed on a floor under the sunlight.

**Law as given.**

> Due to interference & diffraction, the marbles will be colorful

**Corrected.** Solid glass marbles have no thin film, so interference and diffraction produce nothing here. What sunlight on glass marbles actually gives is bright focused caustics on the floor around them, specular sparkle, plus whatever colour the glass itself is dyed.

**Observables.**

- Bright concentrated caustic patches appear on the floor near each marble, on the far side from the sun.
- The marbles carry small sharp specular highlights positioned consistently with the sun.
- Any colour in a marble is its own dye, fixed to the marble and unchanged by the viewing angle -- not a shifting iridescence.
- Caustics and highlights move consistently if the marbles or the light move, and vanish in shadow.

**Why it needs changing.** The law is false: 'due to interference & diffraction, the marbles will be colorful' names a mechanism that does not operate on solid glass spheres. A verbatim rubric item would demand iridescent marbles and reward a clip that invents them. If this prompt is kept it must be relabelled as caustics/specular reflection with the 'colorful' claim dropped; we recommend excluding it instead, since the caption asks for nothing else.

#### id 78 — Interference & Diffraction — **建议排除**

- `78` A bunch of mist particles are suspended in the air under the sunlight.

**Law as given.**

> Due to interference & diffraction, the particles will be colorful

**Corrected.** Mist droplets are far larger than the wavelength of light, so they scatter it almost independently of wavelength: mist looks white or grey, not colourful. Colour appears only in specific geometries (a rainbow with the sun behind the viewer, a corona around the sun), which the caption does not set up.

**Observables.**

- The suspended mist reads white or grey and bright where the sun strikes it, without intrinsic colour.
- Sunlight through the mist makes visible beams and shafts rather than coloured particles.
- Any coloured arc, if present, is a single ordered bow positioned opposite the sun -- not colour spread over the particles themselves.
- The brightness follows the sun's direction and vanishes in shadow.

**Why it needs changing.** The law is false: individual mist particles are not coloured by interference or diffraction. A verbatim rubric would require rainbow-coloured mist and reward a clip that renders it. There is no way to keep the law's claim; the honest options are to exclude the prompt or to rewrite the prompt itself as a rainbow scene with the sun behind the camera.

#### id 79 — Interference & Diffraction — **需改写**  (`duplicate`, `mechanism-mislabelled`)

- `79` A collection of prisms is arranged in a pattern with sunlight shining through them.

**Law as given.**

> Due to interference & diffraction, the prisms will be colorful

**Corrected.** This is dispersion, not interference: a prism splits white light by wavelength, throwing an ordered spectrum -- red through violet in sequence -- onto whatever the light lands on. The prism's own glass is not itself coloured.

**Observables.**

- A spectrum appears where the transmitted light lands, not on the prisms themselves.
- The colours are in the ordered sequence red-orange-yellow-green-blue-violet, adjacent and in that order, rather than a random scatter of hues.
- The spectrum lies on the far side of the prism from the source, along the deviated beam.
- Each spectrum tracks the prism that made it: rotate or move a prism and its spectrum sweeps accordingly.
- The spectra vanish when the light is cut, and no colour is emitted in the dark.
- The light entering the prism is white and the light leaving it is dispersed; the prism does not brighten or add light.

**Why it needs changing.** Mechanism mislabelled. Prism colour is dispersion (wavelength-dependent refraction), not thin-film interference; a prism has no thin film. As written this entry also duplicates the Dispersion group (id 85). The observable signature differs sharply: dispersion gives an ordered spectrum cast onto a surface, interference gives swirling bands on the film itself.

#### id 80, 81, 82, 83, 84 — Interference & Diffraction — **可直接用**

- `80` A puddle of oil on the road under the sunlight.
- `81` A soap bubble floating in the air under the sunlight.
- `82` A film of soap on a wand under the sunlight.
- `83` A thin layer of gasoline on water under the sunlight.
- `84` A layer of detergent on a wet surface under the sunlight.

**Law as given.** (templated across the group)

> Due to interference & diffraction, the oil will be colorful

> Due to interference and diffraction, the bubble will be colorful

> Due to interference and diffraction, the film will be colorful

> Due to interference and diffraction, the layer will be colorful

**Corrected.** A film only a few wavelengths thick makes light reflected from its front and back surfaces interfere, so the colour seen depends on the local thickness and the viewing angle: swirling iridescent bands that shift as the film drains or as the view changes.

**Observables.**

- The colours appear as bands or swirls that vary across the film, not as one uniform tint.
- The colours shift when the film moves, drains or is seen from a different angle, rather than being painted on and fixed to the surface.
- The bands follow the film's thickness pattern and move with the film's flow, staying attached to the fluid rather than sliding across it.
- The palette is the iridescent sequence -- magenta, gold, cyan, green -- rather than arbitrary saturated colours.
- The colours are only present where the film is thin: thicker regions and the surrounding bulk liquid are colourless.
- The colours are a surface effect: what lies behind or under the film still reads through it.
- The effect requires light: it dims with the light and vanishes in shadow.

**Additionally for 80.**

- The coloured bands lie on the puddle's surface and are broken up by ripples, re-forming as the surface settles.

**Additionally for 82.**

- As the soap film on the wand drains, it thins at the top, so the bands migrate downward and the top eventually goes colourless or black before the film breaks.
- The film bursts irreversibly: it does not re-form once broken.

#### id 85, 86, 87, 88 — Dispersion — **可直接用**

- `85` A beam of light passes through a prism.
- `86` A beam of light passes through a crystal chandelier.
- `87` A beam of light passes through a droplet of water.
- `88` A beam of light passes through a glass diamond.

**Law as given.**

> Due to the dispersion of light, it emits multicolored light.

**Corrected.** A transparent body with flat or curved faces refracts short wavelengths more than long ones, so white light entering it leaves separated by colour: an ordered spectrum, red through violet, cast wherever the emerging light lands.

**Observables.**

- An ordered spectrum appears -- red, orange, yellow, green, blue, violet, adjacent and in that sequence, not a random scatter of hues.
- The spectrum appears on the far side of the body from the source, along the path of the deviated light.
- The light entering is white and only the light leaving is separated; the body does not emit light of its own.
- The spectrum tracks the geometry: move or turn the body, or the source, and the spectrum sweeps accordingly and keeps its colour order.
- The spectrum vanishes when the source is cut, and nothing glows in the dark.
- The body's own material stays its own colour and is not itself rainbow-tinted.
- The spectrum's colours stay in fixed order relative to one another; they do not shuffle between frames.

**Additionally for 86.**

- A chandelier's many facets throw many separate spectral flecks around the room, each one an ordered little spectrum, and they sweep together if the chandelier turns.

**Additionally for 87.**

- A single droplet both disperses and refocuses the light, so the colours appear as a small bright fan or arc rather than a long spread band.

**Additionally for 88.**

- Glass has weaker dispersion than real diamond, so the spectral flecks are present but less vivid than a diamond's fire; strong ordered spectra are still expected.

**Why it needs changing.** Only the wording needs care: nothing 'emits' multicoloured light. The incoming white light is separated by wavelength and the spectrum lands on a surface beyond the body. An item phrased as emission would accept a prism glowing with colour of its own, which is the usual failure mode here, and would not ask for the ordered red-to-violet sequence that is the real signature.

#### id 89 — Dispersion — **需改写**  (`duplicate`, `mechanism-mislabelled`)

- `89` A beam of light passes through a soap bubble.

**Law as given.**

> Due to the dispersion of light, it emits multicolored light.

**Corrected.** Soap-bubble colour is thin-film interference, not dispersion: the film's own surface carries swirling iridescent bands whose colours depend on local thickness and viewing angle. No spectrum is cast anywhere.

**Observables.**

- The colours appear on the bubble's own surface, as bands or swirls, not as a spectrum cast onto a surface beyond it.
- The colours vary across the bubble and shift as it moves, rotates or drains.
- The palette is iridescent -- magenta, gold, cyan, green -- rather than an ordered red-to-violet sequence in a line.
- The pattern is attached to the film and travels with it rather than sliding across a still surface.
- What is behind the bubble still reads through it.
- The bubble bursts irreversibly and does not re-form.

**Why it needs changing.** Mechanism mislabelled: a soap film is a few hundred nanometres thick and its colour comes from interference between reflections at its two surfaces, not from wavelength separation in a bulk medium. The two mechanisms have visibly different signatures -- an ordered cast spectrum versus swirling bands on the object -- so a verbatim dispersion rubric would look for the wrong thing. This entry also duplicates the interference group (ids 75, 81).

### Heat

#### id 90, 91, 92 — Solidification — **可直接用**

- `90` A timelapse captures the transformation of a glass of water as the temperature significantly drops to very low levels.
- `91` A timelapse captures the transformation of a glass of juice as the temperature significantly drops to very low levels.
- `92` A timelapse captures the transformation of a glass of milk as the temperature significantly drops to very low levels.

**Law as given.** (templated across the group)

> Because the temperature drops below the freezing point, the water will freeze

> Because the temperature drops below the freezing point, the juice will freeze

> Because the temperature drops below the freezing point, the milk will freeze

**Corrected.** Held below its freezing point, an aqueous liquid crystallises into a rigid solid. It freezes inward from the coldest boundaries -- the walls and the exposed top -- so a solid shell forms first and the still-liquid core is the last to go; water expands on freezing, so the level rises and can dome or crack the vessel.

**Observables.**

- The liquid loses its free surface and becomes a rigid solid that no longer sloshes or flows when the glass is disturbed.
- Freezing begins at the glass walls and the exposed surface and advances inward, rather than the middle solidifying first or the whole volume setting at once.
- The frozen region only grows while the temperature keeps falling; it does not retreat and re-freeze repeatedly.
- The surface stops rippling and locks in place before the interior is solid.
- The frozen material occupies slightly more volume than the liquid did: the level rises rather than dropping, and it can dome upward or crack the glass.
- The frozen material is cloudy or opaque where dissolved air and solids are pushed ahead of the freezing front, not perfectly clear throughout.
- The vessel does not fill itself or lose material: the amount present is conserved apart from the volume change.
- Frost or condensation appears on the outside of the glass, since its wall is now below the surrounding dew point.

**Additionally for 91.**

- The juice's colour concentrates in the still-liquid core as the ice front pushes solutes ahead of it, so the frozen shell is paler than the centre.

**Additionally for 92.**

- Milk sets to an opaque solid; no clear ice appears, since its fat and protein scatter light throughout.

#### id 93 — Solidification — **需改写**

- `93` A timelapse captures the transformation of a glass of oil as the temperature significantly drops to very low levels.

**Law as given.**

> Because the temperature drops below the freezing point, the oil will freeze

**Corrected.** Cooking oil has no sharp freezing point. As it cools it clouds, thickens and stops flowing, ending as an opaque waxy paste or soft solid rather than clear crystalline ice -- and it contracts rather than expanding.

**Observables.**

- The oil clouds progressively: it goes from clear to hazy to opaque as it cools.
- It thickens visibly -- it flows more and more sluggishly and finally stops flowing when the glass is tilted or disturbed.
- The final state is an opaque waxy or buttery mass, not transparent ice with facets or crystal fronts.
- The change advances from the coldest boundaries -- the walls and the top -- inward.
- The level does not rise: oil contracts on solidifying, so the surface stays put or drops slightly.
- The change is progressive and one-directional while the temperature keeps falling.
- Condensation or frost forms on the outside of the cold glass.

**Why it needs changing.** 'Below the freezing point, the oil will freeze' invites a rubric item that demands water-like freezing. Real oil clouds and thickens to a paste, does not form clear crystalline ice, and contracts instead of expanding -- so a verbatim rubric would reward a clip that renders oil as ice and would penalise the correct cloudy-paste result. The correct answer here is also the sharpest discriminator in the whole solidification group.

#### id 94 — Solidification — **可直接用**

- `94` A timelapse captures the transformation of a glass of beer as the temperature significantly drops to very low levels.

**Law as given.**

> Because the temperature drops below the freezing point, the beer will freeze

**Corrected.** Beer is mostly water with alcohol and dissolved CO2. Its freezing point is depressed, so it sets to a slush before a solid; the water freezes preferentially, and the dissolved gas is driven out as the liquid cools and freezes, so bubbles and foam appear and the can or glass can overflow.

**Observables.**

- The beer thickens into a slush -- part solid, part liquid -- before it becomes a rigid solid.
- Freezing begins at the walls and the exposed surface and advances inward.
- Dissolved CO2 comes out of solution: bubbles form and foam rises on top as freezing proceeds.
- The volume increases: the level rises, the foam can push over the rim, and a sealed container can bulge or burst.
- The frozen mass is cloudy and slushy rather than clear ice.
- The frozen region only grows while the temperature keeps falling.
- Condensation or frost forms on the outside of the cold vessel.
- The final solid no longer sloshes when the vessel is moved.

#### id 95, 96, 97, 98, 99 — Melting — **可直接用**

- `95` A timelapse captures the gradual transformation of a piece of ice as the temperature rises significantly.
- `96` A timelapse captures the gradual transformation of a candle as the temperature rises significantly.
- `97` A timelapse captures the gradual transformation of butter as the temperature rises significantly.
- `98` A timelapse captures the gradual transformation of ice cream as the temperature rises significantly.
- `99` A timelapse captures the gradual transformation of wax as the temperature rises significantly.

**Law as given.** (templated across the group)

> Because the temperature rises above the melting point, the ice will melt

> Because the temperature rises above the melting point, the candle will melt

> Because the temperature rises above the melting point, the butter will melt

> Because the temperature rises above the melting point, the ice cream will melt

> Because the temperature rises above the melting point, the wax will melt

**Corrected.** Above its melting point the solid turns to liquid, starting at the warmest, most exposed surfaces and working inward: edges round off, the body slumps under its own weight, and the liquid runs downhill and pools. Nothing is created -- the solid shrinks by exactly what the liquid gains -- and the change does not reverse while the temperature stays high.

**Observables.**

- The solid visibly shrinks while liquid appears, and the two changes happen together.
- Melting starts at the outer and most exposed surfaces and progresses inward, not from the centre outward.
- Sharp edges and corners round off first.
- The body slumps, sags or loses its shape as it softens, before it is fully liquid.
- The liquid runs downhill and pools at the lowest point rather than staying heaped or climbing.
- The material is conserved: the pool grows only as the solid shrinks, and no extra volume appears from nowhere.
- The change is one-directional while the temperature keeps rising -- the solid does not re-form or grow back.
- The remaining solid keeps its own colour and texture; the liquid is the same substance, not a different-coloured fluid.

**Additionally for 95.**

- The remaining ice sits in and floats in its own meltwater rather than sinking, and it stays clear or white while the meltwater is clear.

**Additionally for 96.**

- Wax softens and sags well before it flows: a pool forms in the top around the wick while the body below is still solid, and wax that runs down the side re-solidifies into an opaque ridge as it cools.

**Additionally for 98.**

- Ice cream slumps and loses its scooped shape before liquefying, and it turns from matte and firm to glossy and runny.

**Additionally for 99.**

- Wax softens and sags before it flows, and wax that runs away from the heat cools and re-solidifies into an opaque ridge.

#### id 100 — Liquefaction — **可直接用**

- `100` A timelapse captures the transformation as water vapor in a humid environment comes into contact with a cool glass surface.

**Law as given.**

> Because temperature of glass is much lower than that of water vapor, water vapor will liquefy into water droplets

**Corrected.** Air holding water vapour cools where it touches a surface below its dew point, so vapour condenses on that surface: it fogs, then beads into droplets that grow, merge and run down under gravity. Condensation happens on the cold surface, not in mid-air.

**Observables.**

- Droplets form on the cold surface itself, not floating in the air in front of it.
- The surface fogs or clouds first, then resolves into discrete droplets.
- Droplets grow with time and merge into larger ones; the total wetted area only increases while the surface stays cold and the air stays humid.
- Once large enough, droplets run down under gravity and leave clear streaks behind them.
- Droplets form on the face exposed to the humid air, not on the sheltered or dry side.
- The droplets are liquid water -- rounded, translucent, mobile -- not frost, crystals or ice.
- What is behind the surface becomes harder to see as the condensation builds, and clearer again along the streaks the running drops clear.
- The vapour or mist in the air is depleted or unchanged, never made denser, by condensing onto the surface.

#### id 101 — Liquefaction — **建议排除**  (`caption-law-conflict`)

- `101` A timelapse captures the transformation as fog in a cold environment comes into contact with a warm car window.

**Law as given.**

> Because temperature of window is much lower than that of fog, fog will condense into water droplets

**Corrected.** The caption and the law contradict each other, and the caption's own physics does not produce condensation: fog meeting a WARM window is warmed above its dew point, so the droplets evaporate and the glass clears -- the opposite of the stated outcome.

**Observables.**

- If the window is genuinely warmer than the surrounding fog, the glass stays clear or clears progressively, and any existing droplets shrink and disappear rather than growing.
- Condensation, if shown at all, is on the cold side of the glass, not the warm side.
- Fog outside the window drifts and thins with the air, unaffected by the glass except where it touches it.

**Why it needs changing.** Direct caption/law conflict. The caption says a WARM car window in a COLD environment; the law says 'the temperature of window is much lower than that of fog'. Both cannot hold. Following the law contradicts the prompt; following the caption gives evaporation, not condensation. This is not repairable by rewriting the law alone -- the caption has to be changed to a cold window -- so exclude it (ids 100, 102, 103, 104 already cover the intended physics).

#### id 102, 103, 104 — Liquefaction — **可直接用**

- `102` A timelapse captures the transformation as steam in a kitchen environment comes into contact with a cool metal pot lid.
- `103` A timelapse captures the transformation as mist in a greenhouse environment comes into contact with a cool plastic sheet.
- `104` A timelapse captures the transformation as water vapor in a greenhouse environment comes into contact with a cool plastic sheet.

**Law as given.** (templated across the group)

> Because temperature of pot lid is much lower than that of steam, steam will condense into water droplets

> Because temperature of plastic sheet is much lower than that of mist, mist will condense into water droplets

> Because temperature of plastic sheet is much lower than that of water vapor, water vapor will condense into water droplets

**Corrected.** Air holding water vapour cools where it touches a surface below its dew point, so vapour condenses on that surface: it fogs, then beads into droplets that grow, merge and run down under gravity. Condensation happens on the cold surface, not in mid-air.

**Observables.**

- Droplets form on the cold surface itself, not floating in the air in front of it.
- The surface fogs or clouds first, then resolves into discrete droplets.
- Droplets grow with time and merge into larger ones; the total wetted area only increases while the surface stays cold and the air stays humid.
- Once large enough, droplets run down under gravity and leave clear streaks behind them.
- Droplets form on the face exposed to the humid air, not on the sheltered or dry side.
- The droplets are liquid water -- rounded, translucent, mobile -- not frost, crystals or ice.
- What is behind the surface becomes harder to see as the condensation builds, and clearer again along the streaks the running drops clear.
- The vapour or mist in the air is depleted or unchanged, never made denser, by condensing onto the surface.

**Additionally for 102.**

- Drops that gather on the underside of the lid hang from it and drip back into the pot rather than falling off sideways.

**Additionally for 103.**

- The plastic sheet sags where the collected water weighs it down, and the drops run to the low points of the sag.

#### id 105, 106, 107, 108 — Boiling — **可直接用**

- `105` A timelapse captures the transformation of water in a pot as the temperature rapidly rises above 100°C.
- `106` A timelapse captures the transformation of milk in a kettle as the temperature rapidly rises above 100°C.
- `107` A timelapse captures the transformation of soup in a saucepan as the temperature rapidly rises above 100°C.
- `108` A timelapse captures the transformation of tea in a teapot as the temperature rapidly rises above 100°C.

**Law as given.** (templated across the group)

> Because the temperature reaches boiling point, the water will boil and a large number of bubbles will surge to the water surface

> Because the temperature reaches boiling point, the milk will boil and a large number of bubbles will surge to the milk surface

> Because the temperature reaches boiling point, the soup will boil and a large number of bubbles will surge to the soup surface

> Because the temperature reaches boiling point, the tea will boil and a large number of bubbles will surge to the tea surface

**Corrected.** At the boiling point vapour bubbles nucleate on the hottest surfaces -- the bottom and walls of the vessel -- then grow, detach, expand as they rise, and burst at the surface. The surface goes into continuous agitation, visible steam rises above it, and the level slowly drops as liquid leaves as vapour.

**Observables.**

- Bubbles form at the bottom and the heated walls, not in mid-liquid or at the surface.
- Bubbles rise upward, growing as they go, and burst at the surface.
- Bubble production ramps up as heating continues rather than starting at full intensity or dying away.
- The surface is in continuous agitation once boiling is established -- it does not stay flat and mirror-like while bubbles pour through it.
- Visible steam or vapour rises above the surface and disperses upward.
- The liquid level slowly drops as boiling continues; it does not rise or stay exactly fixed over a long boil.
- Bubbles do not appear before the vessel is heated, and they subside if the heat is removed.
- The liquid keeps its own colour and identity throughout; boiling agitates it but does not change what it is.

**Additionally for 106.**

- Milk's protein and fat skin traps the bubbles, so foam builds and climbs the wall as a rising head rather than bursting freely -- and it can boil over the rim, which plain water in the same vessel would not do.

#### id 109 — Boiling — **需改写**  (`premise-implausible`)

- `109` A timelapse captures the transformation of oil in a cauldron as the temperature rapidly rises above 100°C.

**Law as given.**

> Because the temperature reaches boiling point, the oil will boil and a large number of bubbles will surge to the coffee surface

**Corrected.** Cooking oil does not boil anywhere near 100 C -- its boiling point is several hundred degrees, well above its smoke point. Heated hot oil shimmers with convection and gives off a faint haze or smoke; it does not fill with rising bubbles. Bubbling and spitting in hot oil come from water contamination flashing to steam, not from the oil boiling.

**Observables.**

- The hot oil does not fill with a mass of rising vapour bubbles of its own.
- Convection is visible instead: the surface shimmers and streams, and suspended specks circulate.
- As it gets hotter a faint haze or wisps of smoke rise from the surface.
- Any bubbling is localised and violent -- spitting and popping where water has entered -- rather than a uniform rolling boil across the whole vessel.
- The oil darkens with prolonged heating rather than staying visually unchanged.
- The level does not drop the way a boiling aqueous liquid's does.
- Nothing happens before the vessel is heated, and the shimmer subsides when the heat is removed.

**Why it needs changing.** Two faults. (1) The law is physically false: oil at 100 C is merely hot, so a clip showing oil in a vigorous rolling boil at 100 C would be marked CORRECT by this law and is in fact wrong -- the error runs in the dangerous direction. (2) The law's last clause says 'the coffee surface', a copy-paste artefact from a different caption. This is the single most consequential error we found in PhyGenBench; the caption's stated temperature also has to change, or the expected outcome has to become shimmer-and-smoke rather than boiling.

#### id 110, 111, 112, 113, 114 — deposition — **需改写**  (`mechanism-mislabelled`, `premise-implausible`)

- `110` A timelapse captures the transformation as water vapor in a humid environment comes into contact with a cold glass surface.
- `111` A timelapse captures the transformation as steam in a kitchen comes into contact with a cold window.
- `112` A timelapse captures the transformation as mist in a rainforest comes into contact with a cold metal surface.
- `113` A timelapse captures the transformation as fog in a mountainous region comes into contact with a cold car windshield.
- `114` A timelapse captures the transformation as moisture in the air of a refrigerated room comes into contact with a cold plastic bottle.

**Law as given.** (templated across the group)

> Because the temperature of the glass is much lower than that of the water vapor and below the freezing point, the water vapor will sublimate into frost.

> Because the temperature of the window is much lower than that of the steam and below the freezing point, the steam will sublimate into frost.

> Because the temperature of the metal surface is much lower than that of the mist and below the freezing point, the mist will sublimate into frost.

> Because the temperature of the windshield is much lower than that of the fog and below the freezing point, the fog will sublimate into frost.

> Because the temperature of the bottle is much lower than that of the moisture and below the freezing point, the moisture will sublimate into frost.

**Corrected.** Water vapour meeting a surface below freezing goes straight to solid ice: DEPOSITION, not sublimation (which is the reverse). Feathery, needle-like or dendritic frost crystals grow directly on the surface and spread from their nucleation points, with no liquid-droplet stage.

**Observables.**

- Frost forms on the cold surface itself, not in the air in front of it.
- The deposit is crystalline -- feathery, needle-like or branching -- not rounded liquid droplets.
- It grows outward from nucleation points and spreads across the surface, and the frosted area only increases while the surface stays below freezing.
- No liquid stage appears: there are no beads that later freeze, and nothing runs down under gravity.
- The frost sticks in place -- it does not slide, drip or flow.
- It forms on the face exposed to the humid air and follows that surface's shape, including vertical and overhanging parts, since it is not held on by gravity.
- It is opaque white and progressively obscures whatever is behind the surface.
- Nothing forms before the surface is cold, and the growth is one-directional while it stays cold.

**Additionally for 112.**

- A rainforest scene held below freezing is implausible on its own terms; judge the frost physics as shown, and treat the setting as the caption's business rather than a physics violation.

**Why it needs changing.** The verb is exactly backwards: sublimation is solid to gas, and vapour to solid is deposition. Five entries repeat the error. The physics of the outcome is right, and the genuinely valuable content -- crystalline frost with no droplet stage, which is the one discriminator against the Liquefaction group (ids 100-104) -- is not stated in the law at all.

#### id 115 — Sublimation — **可直接用**

- `115` A timelapse captures the transformation of dry ice as it is exposed to a gradually increasing temperature at room temperature

**Law as given.**

> Dry ice (solid carbon dioxide) in the sublimation process due to the rapid decrease in temperature will make the water vapor in the surrounding air condense into small water droplets forming visible fog

**Corrected.** Dry ice sublimes straight from solid to gas. The CO2 itself is invisible; what is seen is the white fog of ambient water vapour condensing in the cold gas. The block shrinks and leaves NO puddle, and the cold dense gas sinks and spreads along the ground.

**Observables.**

- The block visibly shrinks and its edges round off as it sublimes.
- White fog appears around and above the block while it shrinks.
- No liquid puddle forms: the surface under the block stays dry apart from condensation from the air, and no melt runs off the block.
- The fog is dense and cold, so it sinks and flows along the ground and over edges rather than rising like steam.
- The fog forms in the air near the block, not on the block's own surface as a coating.
- The fog disperses and thins away from the block as it warms and mixes.
- Frost or condensation appears on surfaces the block touches, since they are chilled below the dew point.
- The shrinking is one-directional -- the block never grows back.

#### id 116 — Sublimation — **需改写**  (`non-visual`)

- `116` A timelapse captures the transformation of naphthalene as it is exposed to gradually increasing temperature at room temperature

**Law as given.**

> Naphthalene in the sublimation process due to the release of volatile organic compounds will emit a distinctive odor and can form vapor under mild heating conditions.

**Corrected.** Both substances do sublime, but the law's evidence is an odour, which no video can show. The judgeable content is the solid shrinking and thinning with no liquid stage, no puddle, and faint vapour or haze near it, plus a white deposit re-forming on cooler surfaces.

**Observables.**

- The solid shrinks and its edges round and thin as it is warmed.
- No liquid appears at any point: no droplets on the solid, no pool beneath it, nothing runs.
- Faint vapour, shimmer or haze appears immediately above the solid rather than a dense plume.
- A thin white deposit builds up on nearby cooler surfaces.
- The shrinking is one-directional and gradual while warming continues.
- The solid keeps its own white waxy appearance and does not darken, char or slump.
- Nothing happens before warming begins.

**Why it needs changing.** The stated evidence is non-visual: 'will emit a distinctive odor' (116) and 'will release its characteristic strong aroma' (118) cannot be checked from a video, so a rubric item derived from them is unjudgeable and would either be skipped or answered by guessing. Replace it with the shrinking-solid / no-liquid / re-deposition observables, which is what id 117 already does correctly.

#### id 117 — Sublimation — **可直接用**

- `117` A timelapse captures the transformation of iodine crystals as they are exposed to gradually increasing temperature at room temperature

**Law as given.**

> Iodine crystals in the sublimation process will turn directly into purple vapor without passing through a liquid phase, which can be seen as the temperature rises.

**Corrected.** Iodine sublimes directly from crystals to a violet vapour with no liquid phase, and the vapour re-deposits as crystals on cooler surfaces above it.

**Observables.**

- Violet or purple vapour appears above the crystals as they are warmed.
- The crystals shrink as the vapour appears, and the two happen together.
- No liquid forms: no droplets, no pool, no wet residue under the crystals.
- The vapour is denser than air near the source, so it fills the vessel from the bottom upward rather than shooting away.
- The vapour thins and pales as it disperses, and it is darkest right above the crystals.
- Fresh crystals appear on the cooler upper surfaces where the vapour re-deposits.
- The crystals themselves keep their dark grey-violet metallic look; they do not turn liquid or change colour before vaporising.
- Nothing happens before warming begins.

#### id 118 — Sublimation — **需改写**  (`non-visual`)

- `118` A timelapse captures the transformation of camphor as it is exposed to gradually increasing temperature at room temperature

**Law as given.**

> Camphor in the sublimation process will release its characteristic strong aroma as it transforms from a solid directly into a gas under mild heating.

**Corrected.** Both substances do sublime, but the law's evidence is an odour, which no video can show. The judgeable content is the solid shrinking and thinning with no liquid stage, no puddle, and faint vapour or haze near it, plus a white deposit re-forming on cooler surfaces.

**Observables.**

- The solid shrinks and its edges round and thin as it is warmed.
- No liquid appears at any point: no droplets on the solid, no pool beneath it, nothing runs.
- Faint vapour, shimmer or haze appears immediately above the solid rather than a dense plume.
- A thin white deposit builds up on nearby cooler surfaces.
- The shrinking is one-directional and gradual while warming continues.
- The solid keeps its own white waxy appearance and does not darken, char or slump.
- Nothing happens before warming begins.

**Why it needs changing.** The stated evidence is non-visual: 'will emit a distinctive odor' (116) and 'will release its characteristic strong aroma' (118) cannot be checked from a video, so a rubric item derived from them is unjudgeable and would either be skipped or answered by guessing. Replace it with the shrinking-solid / no-liquid / re-deposition observables, which is what id 117 already does correctly.

#### id 119 — Sublimation — **可直接用**

- `119` A timelapse captures the transformation of arsenic trioxide as it is exposed to gradually increasing temperature at room temperature

**Law as given.**

> Arsenic trioxide in the sublimation process will produce a toxic white vapor without liquefying, which occurs at moderately elevated temperatures.

**Corrected.** Arsenic trioxide sublimes on moderate heating, going from a white solid directly to a vapour with no liquid stage; the vapour is white and re-deposits as a white crust on cooler surfaces.

**Observables.**

- White vapour or fume rises from the solid as it is warmed.
- The solid shrinks as the vapour appears.
- No liquid forms: nothing melts, pools or runs.
- The vapour disperses and thins with distance from the source.
- A white deposit builds up on cooler surfaces above and around the solid.
- The solid stays white and powdery or crystalline throughout rather than darkening or changing texture.
- Nothing happens before heating begins, and the solid never grows back.

**Why it needs changing.** Only the wording needs trimming: 'toxic' is not a visible property and must not become a rubric item. The visible physics -- white fume, shrinking solid, no liquid, re-deposition -- is correct as stated.

### Physical Properties

#### id 120, 121, 122 — Color — **可直接用**

- `120` Equal amounts of red and blue paint are rapidly combined, with the mixture being vigorously stirred until fully blended.
- `121` Equal amounts of yellow and red paint are rapidly combined, with the mixture being vigorously stirred until fully blended.
- `122` Equal amounts of green and blue paint are rapidly combined, with the mixture being vigorously stirred until fully blended.

**Law as given.** (templated across the group)

> The color mixed should be purple

> The color mixed should be orange

> The color mixed should be teal

**Corrected.** Paints mix subtractively: each pigment removes part of the spectrum, so the blend takes an intermediate hue between its parents and is never more saturated or brighter than both of them. Red+blue gives purple, yellow+red orange, green+blue teal, and adding white lightens toward a pale tint.

**Observables.**

- The final colour is the stated one and lies between the two parent hues, not outside their range.
- The blend appears progressively as stirring proceeds rather than switching to the final colour in one frame.
- Streaks and swirls of the unmixed parent colours are visible during stirring and disappear as it homogenises.
- The parent colours are consumed as the blend forms: no untouched pool of pure parent colour survives once it is 'fully blended'.
- The blend is uniform at the end -- no residual banding or separated layers.
- The result is equal to or darker and duller than the parents, never brighter or more vivid than both of them.
- The colour change is irreversible: the mixture does not un-mix back into two colours.
- The total volume is the sum of the two, and it does not shrink or grow during stirring.

**Additionally for 120.**

- Real red and blue paint give a dark, somewhat muddy purple rather than a vivid spectral violet; a dull result is correct here, not a fault.

#### id 123 — Color — **需改写**

- `123` Equal amounts of cyan and magenta paint are rapidly combined, with the mixture being vigorously stirred until fully blended.

**Law as given.**

> The color mixed should be purple

**Corrected.** Cyan and magenta are subtractive primaries: cyan absorbs red, magenta absorbs green, so what is left is BLUE. The blend is bluer than the magenta and darker than either parent -- not the red-leaning purple the law names.

**Observables.**

- The final colour is blue or blue-violet, clearly bluer than the magenta it came from.
- It is not a red-leaning purple or a magenta-dominated violet.
- The blend appears progressively as stirring proceeds, with parent streaks visible in between.
- It is darker and duller than either parent, never brighter than both.
- Both parent colours are consumed; no pure cyan or pure magenta pool survives at the end.
- The end state is uniform, with no banding or layering.
- The change is irreversible -- the mixture does not separate back into cyan and magenta.

**Why it needs changing.** Subtractive mixing of cyan and magenta yields blue. Labelling the target 'purple' is loose enough that a clip producing a red-violet -- which would require a red-absorbing failure -- would pass. Since the whole point of this sub-category is the specific hue, the target has to be stated correctly.

#### id 124 — Color — **可直接用**

- `124` Equal amounts of pink and white paint are rapidly combined, with the mixture being vigorously stirred until fully blended.

**Law as given.**

> The color mixed should be light pink

**Corrected.** Paints mix subtractively: each pigment removes part of the spectrum, so the blend takes an intermediate hue between its parents and is never more saturated or brighter than both of them. Red+blue gives purple, yellow+red orange, green+blue teal, and adding white lightens toward a pale tint.

**Observables.**

- The final colour is the stated one and lies between the two parent hues, not outside their range.
- The blend appears progressively as stirring proceeds rather than switching to the final colour in one frame.
- Streaks and swirls of the unmixed parent colours are visible during stirring and disappear as it homogenises.
- The parent colours are consumed as the blend forms: no untouched pool of pure parent colour survives once it is 'fully blended'.
- The blend is uniform at the end -- no residual banding or separated layers.
- The result is equal to or darker and duller than the parents, never brighter or more vivid than both of them.
- The colour change is irreversible: the mixture does not un-mix back into two colours.
- The total volume is the sum of the two, and it does not shrink or grow during stirring.
- This is the one case where the blend is lighter than one parent: white lightens the pink toward a pale tint, and the result stays in the same hue family rather than shifting toward another colour.

#### id 125, 126, 127, 128, 129 — Flame Reaction — **可直接用**  (`premise-implausible`)

- `125` A piece of copper is ignited, emitting a vivid and unique flame as it burns steadily.
- `126` A piece of magnesium is ignited, emitting a vivid and unique flame as it burns steadily.
- `127` A piece of lithium is ignited, emitting a vivid and unique flame as it burns steadily.
- `128` A piece of sodium is ignited, emitting a vivid and unique flame as it burns steadily.
- `129` A piece of potassium is ignited, emitting a vivid and unique flame as it burns steadily.

**Law as given.** (templated across the group)

> Due to flame reaction, the color of the flame should be green

> Due to flame reaction, the color of the flame should be white

> Due to flame reaction, the color of the flame should be red

> Due to flame reaction, the color of the flame should be yellow

> Due to flame reaction, the color of the flame should be lilac

**Corrected.** Each metal's electrons emit at characteristic wavelengths when excited in a flame, so the flame takes that element's own colour, independent of the fuel: copper green, magnesium brilliant white, lithium crimson, sodium yellow-orange, potassium pale lilac.

**Observables.**

- The flame's colour is the one characteristic of that metal.
- The colour is in the flame itself and around the burning metal, not painted on the solid.
- The colour stays the same as long as the metal keeps burning, rather than cycling through unrelated hues.
- The flame casts light of its own colour on nearby surfaces.
- The flame rises and flickers upward, and is anchored to the burning metal.
- The metal is consumed as it burns -- it darkens, shrinks or leaves a residue -- rather than staying pristine.
- The flame goes out when the metal is used up, and nothing burns before ignition.

**Additionally for 125.**

- Bulk copper metal does not actually ignite; flame-test green comes from copper compounds or fine powder in an existing flame. Judge the flame colour as shown and treat the implausible ignition as the prompt's own premise.

**Additionally for 126.**

- Magnesium burns dazzlingly bright -- bright enough to wash out the exposure -- and leaves a white powdery ash.

**Additionally for 128.**

- Sodium melts into a ball as it burns, and the yellow-orange is intense enough to dominate the whole scene's colour.

**Additionally for 129.**

- Potassium reacts vigorously and the lilac is pale and easily swamped by the yellow of any sodium contamination.

**Why it needs changing (id 125).** The colour claim is right, but the caption's setup cannot happen: a piece of copper will not catch fire. The other four metals in the group do burn, so only this prompt needs the caveat.

#### id 130, 131, 132, 133 — Hardness — **可直接用**

- `130` A delicate, fragile egg is hurled with significant force towards a rugged, solid rock surface, where it collides upon impact
- `131` A lightweight, fragile vase is thrown with great force against a sturdy, concrete wall, where it collides upon impact
- `132` A delicate, fragile glass bottle is hurled with significant force towards a rugged, solid rock surface, where it collides upon impact
- `133` A flimsy, brittle glass cup is propelled with force towards a solid, metallic surface, where it collides upon impact

**Law as given.** (templated across the group)

> The hardness of the stone is very high and the hardness of the raw egg is very low, so the egg will break when it hits the stone

> The hardness of the concrete is very high and the hardness of the vase is very low, so the vase will break when it hits the concrete

> The hardness of the stone is very high and the hardness of the glass bottle is low, so the bottle will shatter when it hits the stone

> The hardness of the metal is very high and the hardness of the glass cup is very low, so the glass cup will break when it hits the metal

**Corrected.** A brittle body thrown hard at a rigid surface cannot absorb the impact by deforming, so it fractures at the point of contact. What matters is brittleness plus the target's rigidity and the impact speed, not 'hardness' as such -- the target survives essentially undamaged while the projectile does not.

**Observables.**

- The thrown object breaks on impact rather than bouncing off intact or sticking to the surface.
- It breaks at the moment and place of contact, not before it lands or well afterwards.
- Fragments and contents fly outward from the impact point, away from the surface, and then fall under gravity.
- The target surface is left essentially undamaged; the projectile takes all the destruction.
- The breakage is irreversible: fragments do not reassemble, and the object does not re-form.
- The object travels along a ballistic path before impact -- it does not hover, slow in mid-air, or change direction on its own.
- The debris comes to rest on the ground or on the surface and stays there.
- The number and spread of fragments is consistent with the impact: a hard throw gives many fragments thrown wide, not a single neat crack.

**Additionally for 130.**

- An egg's shell fragments and the yolk and white splatter, then run downward under gravity and cling to the rock in streaks.

**Additionally for 132.**

- Glass shatters into many small shards that scatter widely and catch the light.

#### id 134 — Hardness — **需改写**

- `134` A weak, frail porcelain plate is flung with significant speed at a robust, wooden table, where it collides upon impact

**Law as given.**

> The hardness of the wood is very high and the hardness of the porcelain plate is very low, so the porcelain plate will break when it hits the wood

**Corrected.** Wood is not hard -- it is softer than porcelain. The plate still shatters, but because it is brittle and the impact is fast and the table is rigid enough not to give way, not because the wood out-ranks it in hardness. The wooden table may well be dented or scratched, unlike stone or concrete.

**Observables.**

- The porcelain plate breaks on impact rather than bouncing off intact.
- It breaks at the moment and place of contact.
- Fragments fly outward from the impact point and then fall under gravity.
- The table survives as a table: it may be scuffed, dented or scratched, but it does not shatter or break through.
- The breakage is irreversible; fragments do not reassemble.
- The plate follows a ballistic path before impact.
- The debris comes to rest and stays put.

**Why it needs changing.** 'The hardness of the wood is very high' is simply false -- wood is far softer than porcelain, and the sibling entries use stone, concrete and metal precisely because they are rigid. The outcome (the plate breaks) is still right, so the fix is to the stated mechanism and to what the target is allowed to look like afterwards.

#### id 135 — Solubility — **可直接用**

- `135` A clear glass of oil is gently poured into a glass of water.

**Law as given.**

> Due to immiscibility, oil and water cannot dissolve each other, there is a stratification of the liquid surface

**Corrected.** Oil and water-based liquids do not mix, so they separate into layers ordered by density with a visible interface: oil (lighter) on top, the aqueous liquid (heavier) underneath, whichever one is poured in.

**Observables.**

- The two liquids end up as two distinct layers with a visible boundary between them.
- The oil is the upper layer and the aqueous liquid the lower one, regardless of which was poured into which.
- The poured liquid travels to its own layer: it does not stay where it landed if that is the wrong side of the interface.
- Pouring disturbs the mixture and drives droplets across the interface, and those droplets then rise or sink to rejoin their own layer.
- Droplets of one liquid inside the other stay as rounded blobs with sharp edges rather than diffusing into a gradient.
- The interface settles to a flat, level line once the disturbance dies down.
- Neither liquid loses its own colour or clarity to the other -- no uniform blend appears.
- The total level rises by the amount added, and each layer's thickness matches how much of that liquid is present.
- Oil poured into water sinks momentarily as a stream, then breaks into globules that rise and coalesce into a film on top.

#### id 136 — Solubility — **需改写**

- `136` A clear glass of honey is gently poured into a glass of milk.

**Law as given.**

> Due to immiscibility, honey and milk cannot dissolve each other, there is a stratification of the liquid surface.

**Corrected.** Honey is a concentrated sugar solution and IS water-soluble, so it does not stay immiscible with milk. Because it is much denser and far more viscous, it sinks as thick ropes and forms a temporary bottom layer, then dissolves into the milk given time or stirring -- density layering, not immiscibility.

**Observables.**

- The honey sinks through the milk rather than floating or staying where it was poured.
- It falls as a thick, coherent rope or column that keeps its shape briefly, reflecting its high viscosity, instead of dispersing at once.
- It gathers into a distinct layer at the BOTTOM of the glass.
- That layer is temporary: its edges blur and it thins and dissolves into the milk over time, faster with stirring -- it does not stay a permanent sharp-edged layer.
- There is no clean flat oil-and-water style interface that persists indefinitely.
- The milk near the honey takes on the honey's tint as it dissolves.
- The level rises by the amount poured.
- The dissolution is irreversible: once mixed, the honey does not re-separate into a layer.

**Why it needs changing.** 'Due to immiscibility, honey and milk cannot dissolve each other' is false: honey is sugar in water and dissolves fully in an aqueous liquid. A verbatim rubric would demand a permanent interface and would penalise the correct behaviour (sinking rope, temporary bottom layer, eventual dissolution). The layering is real but it is a density and viscosity effect, and it is transient.

#### id 137, 138 — Solubility — **可直接用**  (`low-visibility`)

- `137` A clear glass of vinegar is gently poured into a glass of water.
- `138` A clear glass of juice is gently poured into a glass of water.

**Law as given.** (templated across the group)

> Due to solubility, vinegar will mix with water.

> Due to solubility, juice will mix with water.

**Corrected.** Both poured liquids are water-based and fully miscible, so they mix: streaks and plumes spread from the point of entry, then diffuse and stir into one uniform liquid with no interface and no layers.

**Observables.**

- The two liquids end up as one uniform liquid with no visible boundary or layers.
- Mixing starts at the point of entry and spreads outward as plumes and streaks.
- The streaks fade progressively into uniformity rather than snapping to a finished state or persisting indefinitely once disturbed.
- No rounded droplets with sharp edges persist -- anything poured in dissipates instead of holding its shape.
- The final liquid's appearance is intermediate between the two, not identical to just one of them.
- The level rises by the amount added.
- The mixing is irreversible: the uniform liquid does not separate back into two components.
- The flow follows gravity and the pour -- it enters from above and sinks or spreads, and circulation dies down as the liquid comes to rest.

**Additionally for 137.**

- Vinegar and water are both clear, so the only visible sign of mixing is faint refractive shimmer and the flow it induces; there is no colour change to watch.

**Additionally for 138.**

- The juice's colour makes the mixing directly visible: coloured plumes sink and spread, then the whole glass takes an intermediate, weaker colour.

**Why it needs changing (id 137).** The law is correct but nearly unjudgeable on video: clear liquid into clear liquid produces almost no visible evidence either way, so a rubric built on it can be satisfied by a static shot. Worth keeping only as a weak item, or dropping in favour of id 138.

#### id 139 — Solubility — **可直接用**

- `139` A bottle of vinegar is gently poured into a glass of oil.

**Law as given.**

> Due to immiscibility, vinegar and oil cannot dissolve each other, there is a stratification of the liquid surface.

**Corrected.** Oil and water-based liquids do not mix, so they separate into layers ordered by density with a visible interface: oil (lighter) on top, the aqueous liquid (heavier) underneath, whichever one is poured in.

**Observables.**

- The two liquids end up as two distinct layers with a visible boundary between them.
- The oil is the upper layer and the aqueous liquid the lower one, regardless of which was poured into which.
- The poured liquid travels to its own layer: it does not stay where it landed if that is the wrong side of the interface.
- Pouring disturbs the mixture and drives droplets across the interface, and those droplets then rise or sink to rejoin their own layer.
- Droplets of one liquid inside the other stay as rounded blobs with sharp edges rather than diffusing into a gradient.
- The interface settles to a flat, level line once the disturbance dies down.
- Neither liquid loses its own colour or clarity to the other -- no uniform blend appears.
- The total level rises by the amount added, and each layer's thickness matches how much of that liquid is present.
- Vinegar is denser than oil, so it sinks through the oil in droplets that gather into a layer at the bottom -- the poured liquid ends up underneath, which is the opposite of the intuitive 'poured-in liquid floats' reading.

#### id 140 — Combustibility — **需改写**  (`object-mismatch`)

- `140` A small burning ball of paper was thrown into a pile of dry paper.

**Law as given.**

> Due to combustibility of wood, the wood will be ignited And it burns more and more vigorously

**Corrected.** The caption's fuel is paper, not wood: a burning ball of paper thrown into a pile of dry paper ignites the paper, and paper's thin sheets catch and spread fast, curling and blackening ahead of the flame front and collapsing into light ash.

**Observables.**

- Ignition starts where the burning ball lands in the pile.
- The flame front spreads outward from there across the paper and grows.
- Individual sheets curl, darken and blacken just ahead of the flame, then flare and collapse.
- The fire spreads quickly, as thin paper does, rather than smouldering like a solid log.
- Smoke rises upward, and light ash can be carried up by the hot draught.
- The paper is consumed to fragile ash that keeps the sheets' shapes until disturbed.
- The burning is irreversible: consumed paper does not return.
- Unburnt sheets away from the front stay unchanged until it reaches them.

**Why it needs changing.** Object mismatch: the law says 'combustibility of wood, the wood will be ignited' while the caption contains no wood at all -- it is paper into paper, apparently a copy-paste from a different prompt. Wood and paper also burn visibly differently (slow charring and embers versus fast flare and light ash), so the substitution is not harmless.

#### id 141, 142 — Combustibility — **可直接用**

- `141` A small burning match was thrown into a pile of dry leaves.
- `142` A small burning stick was thrown into a pile of hay.

**Law as given.** (templated across the group)

> Due to combustibility of leaves, the leaves will be ignited And it burns more and more vigorously

> Due to combustibility of hay, the hay will be ignited And it burns more and more vigorously

**Corrected.** A burning object landing on dry, finely divided fuel ignites it where it touches. The flame front then spreads outward from that point and grows as it recruits more fuel, consuming it to ash irreversibly while smoke rises.

**Observables.**

- Ignition starts where the burning object lands and touches the pile, not elsewhere or all over at once.
- The flame front spreads outward from the ignition point across the pile.
- The fire grows over time as it recruits more fuel, rather than staying the same size as the small burning object or shrinking straight away.
- Smoke is produced and rises upward, drifting with the air.
- The fuel is consumed: it blackens, curls, shrinks and is left as ash and char.
- Burnt fuel stays burnt -- consumed material does not return, and the fire does not run backwards.
- Flames point upward regardless of how the pile is oriented, and lean with any draught.
- Unburnt fuel outside the flame front stays unchanged until the front reaches it.

**Additionally for 141.**

- Leaves curl and darken just ahead of the flame front, before the flame itself arrives.

#### id 143 — Combustibility — **需改写**  (`outcome-uncertain`)

- `143` A small burning candle was thrown into a pile of dry grass.

**Law as given.**

> Due to combustibility of grass, the grass will be ignited And it burns more and more vigorously

**Corrected.** A lit candle thrown through the air will usually be blown out by its own motion, so the expected outcome is not a certainty. What can be judged is internal consistency: if the flame survives the throw, the dry grass ignites where it lands and the fire spreads and grows; if the flame goes out in flight, nothing ignites -- and either is correct, but not both at once.

**Observables.**

- Whether the candle is still lit when it lands is shown consistently, and the outcome follows from it: a lit candle ignites the grass, an extinguished one does not.
- The candle follows a ballistic path, and the flame -- if it survives -- is deflected backwards by the motion rather than standing straight up.
- If ignition occurs, it starts where the candle lands and the flame front spreads outward from there and grows.
- Smoke is produced and rises upward.
- Burning grass blackens, curls and is consumed to ash, irreversibly.
- A flame that has visibly gone out does not re-light on its own.
- Unburnt grass away from the front stays unchanged until it reaches it.

**Why it needs changing.** Mandating that the grass 'will be ignited' penalises the most likely real outcome -- a thrown candle is extinguished in flight. Rewriting the target as internal consistency keeps the entry usable and, unlike the original, cannot be satisfied by a clip that shows an obviously extinguished candle setting a field alight.

#### id 144 — Combustibility — **可直接用**

- `144` A small burning piece of cloth was thrown into a pile of old newspapers.

**Law as given.**

> Due to combustibility of paper, the paper will be ignited And it burns more and more vigorously

**Corrected.** A burning object landing on dry, finely divided fuel ignites it where it touches. The flame front then spreads outward from that point and grows as it recruits more fuel, consuming it to ash irreversibly while smoke rises.

**Observables.**

- Ignition starts where the burning object lands and touches the pile, not elsewhere or all over at once.
- The flame front spreads outward from the ignition point across the pile.
- The fire grows over time as it recruits more fuel, rather than staying the same size as the small burning object or shrinking straight away.
- Smoke is produced and rises upward, drifting with the air.
- The fuel is consumed: it blackens, curls, shrinks and is left as ash and char.
- Burnt fuel stays burnt -- consumed material does not return, and the fire does not run backwards.
- Flames point upward regardless of how the pile is oriented, and lean with any draught.
- Unburnt fuel outside the flame front stays unchanged until the front reaches it.

### Chemical Properties

#### id 145, 146 — Acidity and Alkalinity — **可直接用**

- `145` A timelapse captures the transformation as colorless vinegar is poured into a glass of purple litmus solution.
- `146` A timelapse captures the transformation as hydrochloric acid is poured into a glass of purple litmus solution.

**Law as given.**

> The color of the litmus solution will change from purple to red

**Corrected.** Purple litmus is an acid-base indicator: added acid drops the pH and turns it red. The change starts where the acid enters, spreads with the mixing, and ends with the whole solution red.

**Observables.**

- The solution's colour changes from purple to red.
- The change begins where the acid enters and spreads outward with the mixing flow, rather than the whole glass switching colour in one frame.
- Streaks of purple survive in between and are gradually consumed, ending with a uniform red.
- The final colour is uniform, with no purple layer or pocket left.
- The change is irreversible: it does not drift back to purple on its own.
- The added liquid is itself colourless, so the new colour comes from the indicator, not from pouring in something red.
- The level rises by the amount added.
- Nothing else happens that the chemistry does not call for -- no bubbling, no precipitate, no heat haze.

**Additionally for 146.**

- More acid deepens the red rather than reversing it, and the colour saturates once the indicator has fully turned.

#### id 147 — Acidity and Alkalinity — **需改写**

- `147` A timelapse captures the transformation as colorless soda water is added to a glass of blue litmus solution.

**Law as given.**

> The solution color remains blue

**Corrected.** Soda water is carbonated water -- dissolved CO2 forms carbonic acid, so it is acidic. Blue litmus therefore turns red or pink, and CO2 bubbles come out of solution as well.

**Observables.**

- The blue litmus solution turns red or pink; it does not remain blue.
- The change begins where the soda water enters and spreads with the mixing.
- Streaks of blue persist during mixing and are consumed, ending in a uniform colour.
- Bubbles form and rise to the surface as dissolved CO2 escapes, and the fizzing subsides over time rather than continuing forever.
- The added liquid is colourless, so the colour change comes from the indicator.
- The colour change is irreversible over the shot, though it may pale slightly as CO2 escapes.
- The level rises by the amount added.

**Why it needs changing.** Factually wrong: 'the solution color remains blue' would only hold for a neutral or basic addition. Carbonated water has a pH around 3-4 and turns blue litmus red. A verbatim rubric would mark a physically correct clip WRONG and reward a clip in which nothing happens -- the easiest possible thing for a video model to produce, so this error is actively harmful as a benchmark item.

#### id 148 — Acidity and Alkalinity — **需改写**

- `148` A timelapse captures the transformation as lemon juice is poured into a glass of red cabbage juice.

**Law as given.**

> Acid and base reaction resulting in color change and the release of gases.

**Corrected.** Red cabbage juice is an anthocyanin indicator, not a base. Lemon juice acidifies it, shifting it from purple toward pink or red. There is no acid-base neutralisation and NO gas is released.

**Observables.**

- The cabbage juice shifts from purple toward pink or red.
- The shift begins where the lemon juice enters and spreads with the mixing.
- No bubbles or fizzing appear: nothing gaseous is produced.
- No precipitate forms and the liquid stays a liquid throughout.
- Streaks of the original colour persist during mixing and are consumed, ending uniform.
- The change is irreversible on its own over the shot.
- The level rises by the amount added.
- The final colour is intermediate and consistent with dilution -- it does not become more vivid than either starting liquid.

**Why it needs changing.** Two errors. 'Acid and base reaction' is wrong -- cabbage juice is an indicator, and mixing it with lemon juice is an indicator colour shift, not neutralisation. 'Release of gases' is wrong outright: nothing here produces gas. A verbatim rubric would reward a clip that invents fizzing, which is exactly the sort of plausible-looking hallucination the benchmark exists to catch.

#### id 149 — Acidity and Alkalinity — **可直接用**

- `149` A timelapse captures the transformation as orange juice is mixed with baking soda in a clear cup.

**Law as given.**

> Citric acid and baking soda react, producing carbon dioxide bubbles.

**Corrected.** Citric acid in the juice reacts with sodium bicarbonate to release carbon dioxide, so the mixture fizzes: bubbles nucleate on the powder, foam builds and rises, and the reaction dies away as one reactant is used up.

**Observables.**

- Bubbles appear and rise to the surface once the baking soda meets the juice.
- Bubbling starts at the powder itself and where it lands, not uniformly throughout the liquid.
- Foam builds on the surface and can rise up the cup, potentially overflowing.
- The fizzing is most vigorous just after mixing and then subsides as the reactants are consumed; it does not continue undiminished or start late for no reason.
- The powder visibly dissolves and disappears as it reacts.
- Bubbles rise upward and burst at the surface; none sink.
- The reaction is irreversible -- the foam collapses to liquid and the powder does not re-form.
- The liquid keeps the juice's own colour; the foam is a paler version of it, not a new colour.

#### id 150, 151, 152, 153 — Dehydration property — **可直接用**

- `150` A timelapse captures the reaction as concentrated sulfuric acid is poured onto a piece of bread.
- `151` A timelapse captures the reaction as concentrated sulfuric acid is poured onto a slice of apple.
- `152` A timelapse captures the reaction as concentrated sulfuric acid is poured onto a sheet of paper.
- `153` A timelapse captures the reaction as concentrated sulfuric acid is poured onto a cotton ball.

**Law as given.** (templated across the group)

> Due to dehydration property of sulfuric acid, the bread will shrink, carbonize and turn black, releasing large amounts of acidic gas

> Due to dehydration property of sulfuric acid, the apple will shrink, carbonize and turn black, releasing large amounts of acidic gas

> Due to dehydration property of sulfuric acid, the paper will shrink, carbonize and turn black, releasing large amounts of acidic gas

> Due to dehydration property of sulfuric acid, the cotton ball will shrink, carbonize and turn black, releasing large amounts of acidic gas

**Corrected.** Concentrated sulfuric acid strips water out of a carbohydrate and leaves carbon behind, so the material darkens, blackens, chars and shrinks exactly where the acid wetted it, with heat and fumes -- and the change is irreversible.

**Observables.**

- Darkening starts exactly where the acid landed and spreads outward from there as it soaks in.
- The colour progresses through yellowing and browning to black rather than jumping straight to black.
- The wetted material shrinks, wrinkles and slumps as it chars.
- Fumes or vapour rise from the reacting area, driven by the heat released.
- Parts of the object the acid never reached stay unchanged in colour and shape.
- The change is irreversible: the charred region does not lighten or recover.
- The reaction stays localised to the wetted region and its spreading edge -- it does not consume the whole object instantly.
- The acid runs and pools under gravity, and the charring follows where it flows.

**Additionally for 150.**

- Bread's porous crumb soaks the acid up and spreads the charring through the structure, so the blackening runs deeper than the surface.

**Additionally for 151.**

- The apple's water content makes the reaction wetter: it releases liquid, bubbles at the surface, and the flesh collapses as it blackens.

**Additionally for 153.**

- Cotton fibres blacken and the ball collapses from a fluffy mass to a small dark clump.

**Why it needs changing.** Only a wording trim: 'releasing large amounts of acidic gas' has a non-visible clause. Keep the visible fume/vapour and drop the chemical identification, which a video cannot show.

#### id 154 — Dehydration property — **需改写**

- `154` A timelapse captures the reaction as concentrated sulfuric acid is poured onto a sponge.

**Law as given.**

> Due to dehydration property of sulfuric acid, the sponge will shrink, carbonize and turn black, releasing large amounts of acidic gas

**Corrected.** The outcome depends on what the sponge is made of, and the law does not say. A cellulose sponge dehydrates and chars black like the other four; a synthetic polyurethane sponge -- the common kitchen kind -- is attacked, discoloured, softened and dissolved instead, without the clean carbonisation.

**Observables.**

- Change starts exactly where the acid landed and spreads outward from there.
- The wetted region shrinks and collapses as it is attacked.
- Whichever path is shown is shown consistently: charring to black for a cellulose sponge, or yellowing, softening and dissolving for a synthetic one -- not a mixture of the two.
- Fumes or vapour rise from the reacting area.
- Untouched parts of the sponge stay unchanged.
- The damage is irreversible and does not recover.
- The acid runs and pools under gravity, and the damage follows where it flows.

**Why it needs changing.** The dehydration/carbonisation claim is material-specific, and 'a sponge' is ambiguous between cellulose and polyurethane. A verbatim rubric demanding black carbonisation would fail a correct clip of a plastic sponge. Either pin the material in the caption or judge internal consistency, as above.

#### id 155, 156 — Redox property — **可直接用**

- `155` A timelapse captures the transformation of a clean and smooth piece of iron in a humid environment over decades.
- `156` A timelapse captures the transformation of a clean and smooth piece of steel in a humid environment over decades.

**Law as given.** (templated across the group)

> Due to its redox property, iron will rust

> Due to its redox property, steel will rust

**Corrected.** Iron and steel oxidise in the presence of water and oxygen, so rust forms: orange-brown patches appear at edges, scratches and low points where water lingers, spread outward, and roughen and flake the surface. The process only ever advances.

**Observables.**

- Orange-brown rust appears on the metal and grows over the timelapse.
- It starts at edges, corners, scratches and places where water sits, then spreads over the flat surface.
- The rusted area only ever grows -- it never shrinks or reverts to bare metal.
- The surface loses its shine progressively, becoming dull and then rough.
- The rust roughens, blisters and flakes, so the surface texture changes rather than just its colour.
- The colour progression runs through dull grey and light brown before deep orange-brown; it does not jump straight to heavy rust in one frame.
- The object keeps its overall shape and position: rust corrodes and pits it but does not make it move, grow or change form.
- Rust stains run downward from the corroded areas, following where water drains.

#### id 157, 158, 159 — Redox property — **需改写**

- `157` A timelapse shows the changes in a shiny and new metal chair left outdoors in the rain over a long period.
- `158` A timelapse video documents the gradual decay of a polished metal railing exposed to the elements over years.
- `159` A timelapse records the oxidation process of a bright and new metal bedframe kept in a damp location over several years.

**Law as given.**

> Due to its redox property, metal will rust

**Corrected.** 'Metal will rust' is over-general: rusting is specific to iron and steel. Aluminium, copper, brass, zinc and stainless steel corrode differently -- dull grey oxide, green patina, white powder -- or barely at all. The law should either name a ferrous object or accept the corrosion product appropriate to whatever metal is shown.

**Observables.**

- The metal surface corrodes progressively over the timelapse rather than staying pristine.
- The corrosion product matches the metal shown: orange-brown flaking rust for iron or steel, grey or white dull oxide for aluminium and zinc, green patina for copper or brass.
- It starts at edges, joints, scratches and places where water lingers, then spreads.
- The corroded area only ever grows; it never reverts to bright metal.
- The shine is lost progressively, and the surface roughens, pits or flakes.
- The colour progression is gradual, not a single jump to a fully corroded state.
- The object keeps its shape and position, corroding in place.
- Stains run downward from the corroded areas, following how the rain drains.

**Why it needs changing.** The caption says only 'metal' -- a chair, a railing, a bedframe -- and the law asserts that metal rusts. Rust is iron oxide; a correct clip showing an aluminium railing developing dull grey oxide would be marked wrong, and a clip showing bright orange rust on obviously anodised aluminium would be marked right. Ids 155 and 156 already cover the ferrous case properly, so the value of these three is exactly the generality that makes them wrong.

