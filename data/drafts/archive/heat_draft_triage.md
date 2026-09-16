# Heat draft triage

标准：**人体**（无人，除非身体就是物理）· **时间尺度**（5–10 s 内看得到关键变化）· **可判断**（画面上能判对错）· **变体**（每现象 3–5 个，不要近重复）

| 判定 | 数量 | 说明 |
|---|---|---|
| keep | 154 | 符合 |
| modify | 17 | 可修改，下面给了新 caption/expectation |
| user_delete | 6 | 用户已删 |
| drop_must | 25 | 必须丢：时间尺度/物理/可判性有硬伤 |
| drop_redundant (P) | 19 | 近重复，优先丢，丢完正好 200 条 |
| drop_redundant_optional | 29 | 近重复但可保留；全丢则剩 171 条 |

必删后剩 **219**；再丢 P 级冗余后剩 **200**。

## 现象覆盖（必删 + P 级丢弃之后）

| subcategory | 现象 | 保留数 | 保留 id |
|---|---|---|---|
| melt_freeze | 冰品融化 | 2 | 0001 0008 |
| melt_freeze | 冰/雪融化 | 10 | 0002 0006 0009 0010 0014 0016 0017 0021 0025 0044 |
| melt_freeze | 黄油/油脂融化 | 4 | 0003 0004 0019 0045 |
| melt_freeze | 巧克力融化 | 1 | 0005 |
| melt_freeze | 蜡/蜡笔融化 | 4 | 0011 0012 0032 0043 |
| melt_freeze | 芝士融化 | 2 | 0018 0047 |
| melt_freeze | 凝固/定型 | 14 | 0026 0027 0028 0029 0030 0031 0033 0034 0035 0037 0038 0039 0040 0050 |
| melt_freeze | 解冻/去霜 | 3 | 0041 0042 0049 |
| boil_steam | 壶/阀喷汽 | 3 | 0051 0057 0060 |
| boil_steam | 沸溢/奶泡 | 3 | 0052 0055 0098 |
| boil_steam | 锅内沸腾 | 7 | 0053 0058 0059 0065 0066 0067* 0084 |
| boil_steam | 开盖出汽 | 4 | 0054 0068 0071 0082 |
| boil_steam | 静态汽羽 | 10 | 0056 0061 0063 0076 0077 0080 0088 0089* 0095 0099 |
| boil_steam | 熨/蒸软化 | 2 | 0062 0086 |
| boil_steam | 倒热液出汽 | 3 | 0064 0075 0094 |
| boil_steam | 水碰热面闪蒸 | 6 | 0069 0079 0081 0090 0091 0100 |
| boil_steam | 关火停沸 | 1 | 0074 |
| condensation | 冷容器外壁结露 | 12 | 0101 0105 0113 0114* 0121* 0122 0125* 0132 0134* 0141* 0144* 0149 |
| condensation | 呼气起雾 | 5 | 0102 0106 0111 0118 0133 |
| condensation | 热湿气碰冷面 | 8 | 0103 0107 0115 0119* 0124* 0126* 0145 0146 |
| condensation | 眼镜进暖室起雾 | 4 | 0104 0117 0140* 0143 |
| condensation | 车内起雾 | 1 | 0108 |
| condensation | 冷雾下沉 | 2 | 0109 0120 |
| condensation | 盖子内侧起雾 | 3 | 0110 0116 0129 |
| condensation | 冷冻品出柜结霜 | 3 | 0112 0128 0150 |
| burn_smoke | 燃料被消耗 | 9 | 0151 0155 0164 0167 0168 0187 0189* 0190 0193 |
| burn_smoke | 熄灭 | 9 | 0152 0158* 0162 0163 0165* 0173 0179 0181 0195 |
| burn_smoke | 点燃 | 9 | 0153 0161 0166 0178* 0184 0191* 0194* 0197 0199 |
| burn_smoke | 火焰随气流 | 7 | 0156 0160 0172 0175* 0188* 0192 0198 |
| burn_smoke | 烟的走向 | 5 | 0157 0174 0176 0182 0196* |
| burn_smoke | 闪燃/喷焰 | 3 | 0171 0177 0186 |
| heat_response | 烹煮质变/浮起 | 7 | 0201 0216* 0229 0231 0238 0244 0250* |
| heat_response | 受热膨胀/爆开 | 11 | 0202 0203 0204* 0212 0217 0218* 0219 0225 0232 0247 0249 |
| heat_response | 塑料/蜡受热变形 | 6 | 0205 0215 0222 0230 0237 0243 |
| heat_response | 热空气上升 | 7 | 0207 0208 0214 0220 0226 0234* 0245 |
| heat_response | 水碰热面(与 boil_steam 重叠) | 8 | 0209 0211 0223 0227 0233* 0236* 0241* 0248 |
| heat_response | 烘干 | 1 | 0235 |
| heat_response | 黄油/油脂融化 | 1 | 0246 |

`*` = drop_redundant_optional（可丢可留）。


## melt_freeze

### HEAT-0001  ✅ keep  · 冰品融化
- 滴落本身是秒级事件；建议把 expectation 里 'the visible change may be small' 删掉，它削弱可判性
- draft: An ice cream cone stands in a holder on a sunny picnic table, and the ice cream is melting and dripping down the side of the cone.

### HEAT-0002  ✅ keep  · 冰/雪融化
- 热水浇冰块：快、无人、可判
- draft: Hot water is poured from a kettle over a large block of ice on the ground, and the ice melts where the water hits it.

### HEAT-0003  ✅ keep  · 黄油/油脂融化
- draft: A pat of cold butter is dropped into a hot frying pan, and it melts into a spreading pool of liquid.

### HEAT-0004  ✅ keep  · 黄油/油脂融化
- 微波炉内景要透过门窗看，生成器可能只画外壳；用户已选，接受
- draft: A pat of butter on a small plate is heated in a microwave and slowly melts.

### HEAT-0005  ✏️ modify  · 巧克力融化
- 隔水融化整碗巧克力要几分钟；从'半融'中段开始，5 秒内有可见变化，且只要求方向
- draft: A bowl full of chocolate pieces sits in a pan of steaming hot water and is stirred with a spatula, and the chocolate slowly melts.
- **new caption:** A bowl of half-melted chocolate sits in a pan of steaming water and is stirred with a spatula, and the remaining pieces melt into the liquid.
- **new expectation:** The remaining pieces soften and lose their edges from the outside in and are smeared into the glossy liquid by the spatula; the melted part does not re-harden or break back into separate pieces while the water steams.

### HEAT-0006  ✅ keep  · 冰/雪融化
- 红热铁球放冰上：快、无人、可判
- draft: A glowing red-hot metal ball is set on top of a large block of ice, and the ice melts around it.

### HEAT-0007  ❌ drop (must)  · 冰/雪融化
- 太阳下柠檬水里的冰块 5 秒内看不出任何变化；expectation '比新冰更小更圆' 从画面上判不出来
- draft: A glass of lemonade with ice cubes sits on a table in the sun, and the ice is melting.

### HEAT-0008  ✏️ modify  · 冰品融化
- 去掉手：手只是接滴的地方，用杯子代替
- draft: A fruit popsicle is held upright on its stick in the summer heat, and it drips down the stick onto the hand.
- **new caption:** A fruit popsicle stands upright on its stick in a cup on a sunny table, and it drips down the stick.
- **new expectation:** Drips run downward along the stick and collect in the cup; the popsicle looks glossy and soft and may slide on the stick; it does not refreeze, grow, or drip upward.

### HEAT-0009  ✅ keep  · 冰/雪融化
- 冰柱滴水：滴落是秒级事件
- draft: Icicles hanging from a roof gutter drip steadily in the afternoon sun.

### HEAT-0010  ✅ keep  · 冰/雪融化
- draft: An ice cube is dropped into a mug of hot tea, and it melts quickly.

### HEAT-0011  ✅ keep  · 蜡/蜡笔融化
- 溢出是秒级事件
- draft: A candle burns on a dinner table, and melted wax spills over the rim and runs down one side.

### HEAT-0012  ✏️ modify  · 蜡/蜡笔融化
- 可选：用'propped'去掉持棍的人；expectation 沿用 draft
- draft: A marshmallow on a stick is held over a campfire, and it softens and sags.
- **new caption:** A marshmallow on a stick is propped over a campfire, and it puffs, softens and sags.
- **new expectation:** The side facing the fire puffs and goes glossy first, then the marshmallow slumps and droops under its own weight, more on the fire side; the surface may brown, blacken in spots, or even catch if close to the flame, and any such darkening deepens and never fades back to white; it does not firm up again while over the heat.

### HEAT-0013  🗑 user_delete  · 冰/雪融化
- 用户已决定删除
- draft: Snow lies on the hood of a car that has just been driven, and the snow melts into water that runs off the hood.

### HEAT-0014  ✅ keep  · 冰/雪融化
- 弱：小冰雹在晒热的路面上几十秒出湿圈，勉强够；用户保留了 caption
- draft: Hailstones lie on a sunlit pavement after a storm, and they shrink into wet spots.

### HEAT-0015  🗑 user_delete  · 冰品融化
- 用户已决定删除
- draft: A scoop of vanilla ice cream is set on a warm brownie fresh from the oven, and it melts down over the brownie.

### HEAT-0016  ✅ keep  · 冰/雪融化
- 雪花很小，480p 可能看不清，但物理和时间尺度都对
- draft: Snowflakes land on the dark sleeve of a warm coat during a snowfall and melt into tiny drops.

### HEAT-0017  ✅ keep  · 冰/雪融化
- draft: An ice cube is flicked onto a hot skillet, and it skitters around and shrinks as it melts.

### HEAT-0018  ✏️ modify  · 芝士融化
- 披萨在烤箱里：内景难画、芝士化开要 1–2 分钟；改成热锅上的芝士碎，秒级且无人
- draft: A pizza sits in a hot oven, and the shredded cheese on top melts and joins into a smooth bubbling layer.
- **new caption:** A handful of shredded cheese is scattered onto a hot skillet, and the shreds melt and flow together into a bubbling layer.
- **new expectation:** The shreds slump and go glossy where they touch the pan first, then merge into one layer that bubbles at the edges; they do not stay as separate dry strands or pull back apart.

### HEAT-0019  ✅ keep  · 黄油/油脂融化
- draft: A cube of cold butter is dropped into a bowl of hot soup, and the butter melts and spreads across the surface.

### HEAT-0020  ❌ drop (must)  · 巧克力融化
- 手指是主体，太阳下涂层软化是分钟级；巧克力已有 0005/0027/0037/0050
- draft: A chocolate-coated ice cream bar is held in the sun, and the chocolate coating softens and smears on the fingers.

### HEAT-0021  ✏️ modify  · 冰/雪融化
- 室温下毛上的雪要几分钟；放到壁炉前，火侧先化，方向可判
- draft: A dog has just come in from the snow with clumps of snow on its fur, and the snow is melting and dripping onto the floor.
- **new caption:** A dog with clumps of snow in its fur lies in front of a fireplace, and the snow melts and drips onto the floor.
- **new expectation:** The clumps on the side facing the fire turn wet and shrink or slide off first, drops fall downward, and a wet patch forms on the floor; the snow does not stay white and fluffy or grow.

### HEAT-0022  🗑 user_delete  · 冰品融化
- 用户已决定删除
- draft: A carton of ice cream is left out on the kitchen counter, and when it is opened the ice cream inside has gone soft and soupy around the edges.

### HEAT-0023  🗑 user_delete  · 冰品融化
- 用户已决定删除
- draft: A woman holds a spoonful of frozen sorbet over her bowl and it slumps and drips off the spoon.

### HEAT-0024  🗑 user_delete  · 黄油/油脂融化
- 用户已决定删除
- draft: A pat of butter is set on top of a steaming baked potato, and it melts and runs down into the split.

### HEAT-0025  ✏️ modify  · 冰/雪融化
- 盘子上的雪球室温下要十几分钟；改成热铁板，秒级；和 0017（冰块滑动）是不同的错误模式
- draft: A small snowball sits on a plate indoors and is melting into a puddle.
- **new caption:** A small snowball is set on a hot griddle, and it hisses and collapses into water and steam.
- **new expectation:** The snow darkens and slumps from the bottom where it touches the metal, meltwater spreads and sizzles around it and steam rises; the ball does not stay white and firm, grow, or refreeze.

### HEAT-0026  ✅ keep  · 凝固/定型
- draft: A candle tips and a drop of liquid wax falls onto a wooden table, where it hardens into a small white disc.

### HEAT-0027  ✅ keep  · 凝固/定型
- draft: Warm chocolate sauce is poured over a scoop of ice cream, and the sauce firms into a crackly shell on the cold surface.

### HEAT-0028  ✅ keep  · 凝固/定型
- 按按钮需要手，是不可避免的触发，被动语态可接受
- draft: A bead of hot glue is squeezed from a glue gun onto a piece of wood, a button is pressed into it, and the glue sets hard around the button.

### HEAT-0029  ✅ keep  · 凝固/定型
- draft: Boiling sugar syrup is drizzled from a spoon into a bowl of ice water, and the syrup hardens instantly into brittle golden threads.

### HEAT-0030  ✅ keep  · 凝固/定型
- 盖章需要手，不可避免
- draft: Melted sealing wax is dripped onto the flap of an envelope and a stamp is pressed into it, and the wax hardens with the stamp's design.

### HEAT-0031  ✅ keep  · 凝固/定型
- 与 0027 是'脆壳 vs 软糖'两种凝固，保留
- draft: Hot fudge is spooned over a bowl of ice cream, and it thickens and stiffens where it meets the cold ice cream.

### HEAT-0032  ✅ keep  · 蜡/蜡笔融化
- draft: A hairdryer is aimed at crayons taped to the top of a canvas, and the crayons melt and run down the canvas in coloured streaks that harden lower down.

### HEAT-0033  ✅ keep  · 凝固/定型
- draft: Hot caramel is poured onto a cold marble slab, and the caramel spreads, then stiffens into a glassy sheet.

### HEAT-0034  ✅ keep  · 凝固/定型
- draft: Melted butter is poured onto a plate that has just come out of the freezer, and the butter turns cloudy and firm on the plate.

### HEAT-0035  ✅ keep  · 凝固/定型
- draft: On a bitterly cold winter morning a cup of water is splashed onto a frozen car windshield, and the water freezes into a film of ice on the glass.

### HEAT-0036  🗑 user_delete  · 凝固/定型
- 用户已决定删除
- draft: On a bitterly cold winter day a child blows a soap bubble outdoors and catches it on the wand, and the bubble turns frosty and stiff.

### HEAT-0037  ✏️ modify  · 凝固/定型
- 'chilled tray' 上巧克力凝固要 1–2 分钟；改成冷冻托盘（几十秒），expectation 只要求方向
- draft: Melted chocolate is piped in lines onto a sheet of parchment on a chilled tray, and the lines set firm and matte.
- **new caption:** Melted chocolate is piped in lines onto a metal tray straight from the freezer, and the lines set as they cool.
- **new expectation:** The lines hold the shape they were piped in and turn from glossy to dull starting where they touch the cold metal; they do not spread out, run, or turn glossy again.

### HEAT-0038  ✅ keep  · 凝固/定型
- 手指就是冷表面，人体即物理
- draft: A fingertip is dipped into the warm wax pool of a candle and pulled out, and the wax on the finger cools into a thin hard cap.

### HEAT-0039  ✅ keep  · 凝固/定型
- draft: Hot bacon fat is poured into a glass jar straight from the fridge, and the fat begins to set where it touches the cold glass.

### HEAT-0040  ✅ keep  · 凝固/定型
- draft: A hot glue gun is lifted away from a joint, and the thin strand of glue trailing from the nozzle stiffens into a fine fixed thread.

### HEAT-0041  ✅ keep  · 解冻/去霜
- draft: A frozen fish fillet is laid in a hot pan, and the white frost on its surface disappears as the fillet thaws.

### HEAT-0042  ✅ keep  · 解冻/去霜
- draft: A bag of frozen peas is emptied into a pot of hot water, and the frost on them vanishes and the clumps break apart.

### HEAT-0043  ✏️ modify  · 蜡/蜡笔融化
- 结果态（'has softened'）5 秒内没有事发生；改成热锅上的蜡笔。若觉得和 0032 重复也可丢
- draft: A crayon lying on the dashboard of a car parked in the sun has softened and slumped over.
- **new caption:** A wax crayon lies on a hot skillet, and it softens, slumps, and melts into a coloured pool.
- **new expectation:** The crayon sags and loses its shape from the side touching the pan, and a pool of the same colour spreads out from it; it does not stay stiff, straighten, or change colour.

### HEAT-0044  ✏️ modify  · 冰/雪融化
- 冷水+搅拌是分钟级且需要手；改热水，无人，颜色扩散秒级可判
- draft: A block of frozen orange juice is dropped into a jug of water and stirred, and it starts to melt into the water.
- **new caption:** A block of frozen orange juice is dropped into a jug of hot water, and it melts, the orange colour spreading into the water.
- **new expectation:** The block rounds off and shrinks while orange streaks sink and spread from it and the water turns steadily more orange; the block does not grow and the water does not clear again.

### HEAT-0045  ✏️ modify  · 黄油/油脂融化
- 'has turned clear' 是结果态，画面上只是一罐清液，判不出曾是固体；隔水加热又太慢（壁层变清要几十秒到一分钟）；改成热锅，几秒内白→透明，和 0003 黄油的区别是材料响应：不起泡不变黄
- draft: A lump of coconut oil in a jar on a sunny counter has turned from white and solid to clear liquid.
- **new caption:** A spoonful of solid white coconut oil is dropped into a hot frying pan, and it melts into clear liquid.
- **new expectation:** The white lump turns glossy and clear from the bottom where it touches the pan and shrinks as a colourless pool spreads out around it; the pool stays clear with no foam or browning, and the oil does not stay white and solid or turn white again in the hot pan.

### HEAT-0046  ❌ drop (must)  · 巧克力融化
- 结果态 + 需要手拆包装；巧克力变体已够
- draft: Chocolate coins left in a jacket pocket on a warm day have softened, and when unwrapped the foil comes away smeared and the coin bends.

### HEAT-0047  ✏️ modify  · 芝士融化
- 'is held near a grill' 仍需要手；raclette 就是这个现象的无人版
- draft: A block of hard cheese is held near a hot grill, and the near face softens and begins to sag and drip.
- **new caption:** A wedge of cheese sits under the heating element of a raclette grill, and the face nearest the element softens, sags and drips.
- **new expectation:** Only the face toward the heat softens and goes glossy; drips run downward off the lowest point onto the plate below; the far side stays firm and the cheese does not stiffen again under the heat.

### HEAT-0048  ❌ drop (must)  · 冰/雪融化
- 太阳晒热的盘子上冰块要几分钟；与 0017 重复
- draft: An ice cube sits on a sun-warmed metal plate on a balcony and is melting.

### HEAT-0049  ✏️ modify  · 解冻/去霜
- 刮霜是持续手部动作，暖风除霜是分钟级；改温水浇霜，秒级，且与 0035（水在冷玻璃上结冰）构成对照
- draft: Frost is scraped off a car windshield with a card while the heater runs inside, and the remaining frost turns to water and runs down the glass.
- **new caption:** Warm water is poured over a frosted car windshield on a cold morning, and the frost clears where the water runs.
- **new expectation:** The frost turns clear along the path of the water and the water runs downward off the glass; frost does not re-form on the wetted glass while the water is warm, and untouched areas stay frosted.

### HEAT-0050  ✅ keep  · 凝固/定型
- draft: Hot melted chocolate is spooned onto a cold metal bowl turned upside down, and it stiffens where it lands, leaving a fixed drip pattern.


## boil_steam

### HEAT-0051  ✅ keep  · 壶/阀喷汽
- draft: A kettle on a stove is at the boil, steam pours from the spout, and the lid rattles.

### HEAT-0052  ✅ keep  · 沸溢/奶泡
- draft: A pot of pasta water boils over on a stove, and foamy water spills down the outside of the pot onto the burner.

### HEAT-0053  ✅ keep  · 锅内沸腾
- draft: A saucepan of water on high heat is at a rolling boil, with large bubbles bursting at the surface.

### HEAT-0054  ✅ keep  · 开盖出汽
- draft: The lid is lifted off a rice cooker, and a cloud of steam billows up out of it.

### HEAT-0055  ✅ keep  · 沸溢/奶泡
- draft: A steam wand is pushed into a jug of milk, and the milk hisses, swirls, and rises in the jug as foam.

### HEAT-0056  ✅ keep  · 静态汽羽
- draft: A cup of hot tea sits on a table, and thin wisps of steam curl up from its surface.

### HEAT-0057  ✅ keep  · 壶/阀喷汽
- draft: A pressure cooker on a stove starts hissing, and a jet of steam shoots up from the valve on its lid.

### HEAT-0058  ✅ keep  · 锅内沸腾
- draft: A pot of soup simmers on a stove, with small bubbles breaking the surface and steam rising.

### HEAT-0059  ✅ keep  · 锅内沸腾
- draft: Eggs boil in a pot on a stove, rattling against each other as the water bubbles around them.

### HEAT-0060  ✅ keep  · 壶/阀喷汽
- draft: A stovetop kettle begins to whistle, and steam streams from the whistle spout.

### HEAT-0061  ✅ keep  · 静态汽羽
- 弱：静态弥漫，只能判'不下沉'
- draft: A hot shower has just been turned off, and the bathroom is filled with steam drifting up toward the ceiling.

### HEAT-0062  ✅ keep  · 熨/蒸软化
- 熨斗被压下需要手，被动语态可接受
- draft: A steam iron is pressed onto a shirt on an ironing board, and puffs of steam rise from around the iron.

### HEAT-0063  ✅ keep  · 静态汽羽
- draft: Steam rises from a manhole cover on a city street on a cold morning.

### HEAT-0064  ✅ keep  · 倒热液出汽
- draft: Boiling water is poured from a kettle into a mug, and steam rises from the mug as it fills.

### HEAT-0065  ✅ keep  · 锅内沸腾
- draft: Noodles cook in a pot of boiling water, bobbing and swirling with the bubbles.

### HEAT-0066  ✅ keep  · 锅内沸腾
- 玻璃壶里气泡自底上升：最可判的沸腾条目
- draft: Water boils in a glass electric kettle, with streams of bubbles rising from the bottom to the surface.

### HEAT-0067  ⚠️ redundant (optional)  · 锅内沸腾
- 与 0053 重复（篝火只是换了背景）
- draft: A pot of water hangs over a campfire on a tripod, boiling, with steam rising into the evening air.

### HEAT-0068  ✅ keep  · 开盖出汽
- draft: A bamboo steamer basket is lifted off a wok of boiling water, and steam gushes up from the wok and from the basket.

### HEAT-0069  ✅ keep  · 水碰热面闪蒸
- draft: Water is ladled onto the hot stones of a sauna, and a burst of steam rises off the stones with a hiss.

### HEAT-0070  ⚠️ drop (redundant, P)  · 开盖出汽
- 开盖出汽第 7 条；街头摊位隐含人群
- draft: The lid of a large pot of dumplings is lifted at a street stall, and steam rolls up out of the pot into the cold air.

### HEAT-0071  ✅ keep  · 开盖出汽
- draft: A dishwasher door is opened at the end of its cycle, and a wave of steam rolls up and out of the machine.

### HEAT-0072  ⚠️ drop (redundant, P)  · 锅内沸腾
- 快空的咖啡壶：画面小、弱
- draft: A coffee pot on a warming plate is nearly empty, and the last of the coffee bubbles and steams in the bottom.

### HEAT-0073  ❌ drop (must)  · 静态汽羽
- 超声加湿器出的是冷雾，常常下沉贴桌面；'plume upward' 这个 expectation 本身物理上不可靠
- draft: A humidifier on a bedside table sends a steady plume of mist upward into the room.

### HEAT-0074  ✅ keep  · 关火停沸
- 关火后沸腾停止：很好的因果测试
- draft: A pan of water on a stove is at a boil, and the burner is turned off; the bubbling dies down and only faint steam remains.

### HEAT-0075  ✅ keep  · 倒热液出汽
- draft: Hot water is poured from a thermos into a bowl of instant noodles, and steam rises from the bowl.

### HEAT-0076  ✅ keep  · 静态汽羽
- draft: A geyser in a national park erupts, sending a column of boiling water and steam high into the air before it falls back.

### HEAT-0077  ✅ keep  · 静态汽羽
- draft: Steam rises from the surface of a hot spring on a cold morning.

### HEAT-0078  ❌ drop (must)  · 熨/蒸软化
- 暖气片（~60°C）上的湿毛巾基本看不到蒸汽，5 秒内也看不到变干
- draft: A wet towel is laid over a hot radiator, and steam rises from the towel where it touches the hot metal.

### HEAT-0079  ✅ keep  · 水碰热面闪蒸
- draft: Wet spinach is tossed into a very hot pan, and a burst of steam rises with a loud hiss as the leaves wilt.

### HEAT-0080  ✅ keep  · 静态汽羽
- draft: A locomotive at a heritage railway lets off steam, and a great white cloud rolls up from beside the wheels.

### HEAT-0081  ✅ keep  · 水碰热面闪蒸
- draft: Water is poured onto the hot coals of a barbecue after cooking, and a hissing cloud of steam rises from the grill.

### HEAT-0082  ✅ keep  · 开盖出汽
- draft: The door of a hot oven is opened, and a wave of hot air and steam rushes up and out of the opening.

### HEAT-0083  ❌ drop (must)  · 锅内沸腾
- 活龙虾入锅：内容敏感，且现象是液面抬升不是热
- draft: A live lobster is dropped into a pot of boiling water, and the water surges and steam rises as the level jumps.

### HEAT-0084  ✅ keep  · 锅内沸腾
- 肉片卷曲上浮其实更像 heat_response，可考虑改 subcategory
- draft: A hot pot bubbles in the centre of a dinner table, and thin slices of meat dropped into the broth curl up and rise to the surface.

### HEAT-0085  ❌ drop (must)  · 静态汽羽
- 铺沥青必然有工人在画面里
- draft: Hot tar is spread from a bucket across a roof, and steam and fumes rise off the fresh tar.

### HEAT-0086  ✅ keep  · 熨/蒸软化
- draft: A jet of steam from a wallpaper steamer plate softens old wallpaper, and the paper peels away in wet strips.

### HEAT-0087  ⚠️ drop (redundant, P)  · 开盖出汽
- 与 0054 重复（微波炉版）
- draft: A cup of instant soup is heated in a microwave, and when the door opens steam rises from the cup.

### HEAT-0088  ✅ keep  · 静态汽羽
- keep_person：跑者的身体就是汽源
- draft: Runners at a winter race stand steaming at the finish line, with vapour rising from their heads and shoulders.

### HEAT-0089  ⚠️ redundant (optional)  · 静态汽羽
- 壁炉前的湿狗变干：慢；与 0235 重叠
- draft: A wet dog lies in front of a fireplace, and steam rises gently from its fur as it dries.

### HEAT-0090  ✅ keep  · 水碰热面闪蒸
- draft: Rain falls on a sun-baked road, and steam rises from the hot asphalt as the drops hit.

### HEAT-0091  ✅ keep  · 水碰热面闪蒸
- draft: A glowing piece of metal is plunged into a bucket of water, and a cloud of steam bursts up from the bucket.

### HEAT-0092  ⚠️ drop (redundant, P)  · 倒热液出汽
- 与 0064/0075 重复
- draft: A ladle of hot broth is poured over cold noodles in a bowl, and a puff of steam rises from the bowl.

### HEAT-0093  ⚠️ drop (redundant, P)  · 静态汽羽
- 与 0056 重复（浓缩咖啡版）
- draft: Espresso drips from a machine into a small cup, and steam curls up from the fresh coffee.

### HEAT-0094  ✅ keep  · 倒热液出汽
- 加了颜色扩散，比 0064 多一个可判项
- draft: Boiling water is poured over a tea bag in a glass, and steam rises while the colour spreads from the bag.

### HEAT-0095  ✅ keep  · 静态汽羽
- draft: A car with an overheated engine sits at the roadside with steam pouring out from under the hood.

### HEAT-0096  ⚠️ drop (redundant, P)  · 水碰热面闪蒸
- 与 0223（水珠在热铁板上跳）重复，且'熨斗板朝上滴水'场景别扭
- draft: Water is dripped onto a hot clothes iron plate, and each drop sizzles and vanishes into steam.

### HEAT-0097  ⚠️ drop (redundant, P)  · 开盖出汽
- 开盖出汽第 8 条
- draft: A lid is lifted from a pan of steamed vegetables, and steam rises to fog the range hood above.

### HEAT-0098  ✅ keep  · 沸溢/奶泡
- draft: A saucepan of milk on a stove begins to boil, and the milk foams up rapidly toward the rim.

### HEAT-0099  ✅ keep  · 静态汽羽
- draft: A vent pipe on a factory roof releases a steady plume of white steam into the winter sky.

### HEAT-0100  ✅ keep  · 水碰热面闪蒸
- 与 0211 是'冻霜 vs 表面水'两种变体，保留
- draft: Frozen french fries are dropped into a pot of hot oil, and the oil erupts in bubbles and steam.


## condensation

### HEAT-0101  ✅ keep  · 冷容器外壁结露
- draft: A cold bottle of soda has just been taken out of the fridge on a hot day, and beads of water form on the outside of the bottle.

### HEAT-0102  ✅ keep  · 呼气起雾
- draft: Breath is blown onto a cold window pane, and a patch of fog appears on the glass and then fades.

### HEAT-0103  ✅ keep  · 热湿气碰冷面
- 静态：只能判雾均匀、不瞬间消失
- draft: A hot shower has just run in a closed bathroom, and the mirror is fogged over so that reflections are a blur.

### HEAT-0104  ✅ keep  · 眼镜进暖室起雾
- draft: A pair of glasses is brought in from the cold street into a warm café, and the lenses fog over.

### HEAT-0105  ✅ keep  · 冷容器外壁结露
- draft: A glass of ice water sits on a wooden table in a warm room, and condensation runs down the outside of the glass onto the table.

### HEAT-0106  ✅ keep  · 呼气起雾
- draft: Breath is blown onto the shiny back of a cold metal spoon, and the spoon fogs and then clears.

### HEAT-0107  ✅ keep  · 热湿气碰冷面
- draft: A hot shower runs with the bathroom door closed, and the bathroom window is misting over from the bottom up.

### HEAT-0108  ✅ keep  · 车内起雾
- keep_person：乘客的呼吸就是水源
- draft: Four people sit in a parked car on a cold evening, and the inside of the windows fogs up.

### HEAT-0109  ✅ keep  · 冷雾下沉
- 冷雾下沉，是'蒸汽上升'的反例，很有价值
- draft: A chest freezer is opened, and a low mist rolls out over the rim and sinks toward the floor.

### HEAT-0110  ✅ keep  · 盖子内侧起雾
- draft: The lid of a pot that has been simmering is lifted and turned over, and its underside is covered in drops that run and drip off.

### HEAT-0111  ✅ keep  · 呼气起雾
- keep_person
- draft: A man exhales on a frosty morning, and his breath appears as a white cloud that drifts away and fades.

### HEAT-0112  ✅ keep  · 冷冻品出柜结霜
- draft: A tub of ice cream is taken from the freezer, and a white frost forms on its lid as it sits on the counter.

### HEAT-0113  ✅ keep  · 冷容器外壁结露
- 结霜杯→水珠，秒级
- draft: A frosted beer mug is filled from a tap on a warm terrace, and the outside of the mug beads with water.

### HEAT-0114  ⚠️ redundant (optional)  · 冷容器外壁结露
- 冷容器结露第 n 条
- draft: A cold can of drink is set on a picnic table in the sun, and within a short time it is wet with condensation.

### HEAT-0115  ✅ keep  · 热湿气碰冷面
- draft: Steam from a kettle rises against a kitchen cabinet door, and the door beads with water that runs down.

### HEAT-0116  ✅ keep  · 盖子内侧起雾
- draft: A lid is snapped onto a container of hot food, and the inside of the clear lid fogs over.

### HEAT-0117  ✅ keep  · 眼镜进暖室起雾
- draft: A camera is carried from an air-conditioned lobby out into humid summer heat, and its lens fogs up.

### HEAT-0118  ✅ keep  · 呼气起雾
- keep_person：头盔面罩随呼吸起雾，人体即物理
- draft: A motorcyclist stops at a light on a cold day, and the inside of the helmet visor fogs with each breath.

### HEAT-0119  ⚠️ redundant (optional)  · 热湿气碰冷面
- 温室玻璃早晨变干：慢
- draft: Sunlight warms a greenhouse in the morning, and the inside of its glass panes is covered in drops that begin to run down.

### HEAT-0120  ✅ keep  · 冷雾下沉
- draft: A car's air conditioning is turned to full blast on a humid day, and faint mist drifts out of the dashboard vents.

### HEAT-0121  ⚠️ redundant (optional)  · 冷容器外壁结露
- 与 0101/0113 重复
- draft: A cold bottle of white wine stands in a bucket of ice on a restaurant table, and the bottle neck above the ice is beaded with water.

### HEAT-0122  ✅ keep  · 冷容器外壁结露
- 水管滴水是事件，可判
- draft: A cold metal water pipe runs along a basement wall on a humid day, and it sweats droplets that drip onto the floor.

### HEAT-0123  ⚠️ drop (redundant, P)  · 眼镜进暖室起雾
- 与 0104 重复
- draft: A pair of sunglasses left in a cold car is carried into a warm shop, and the lenses cloud over.

### HEAT-0124  ⚠️ redundant (optional)  · 热湿气碰冷面
- 与 0107/0115 重复
- draft: Steam from a hot shower drifts against the cool tiled wall, and the tiles bead with water that runs in streaks.

### HEAT-0125  ⚠️ redundant (optional)  · 冷容器外壁结露
- 与 0105 重复
- draft: A cold pitcher of lemonade is set on a paper napkin, and the napkin darkens with damp around the base as drops run down the pitcher.

### HEAT-0126  ⚠️ redundant (optional)  · 热湿气碰冷面
- 与 0115 重复
- draft: A hot dishwasher is opened and the steam that escapes fogs the cool kitchen window above the sink.

### HEAT-0127  ⚠️ drop (redundant, P)  · 眼镜进暖室起雾
- 与 0104 重复
- draft: A pair of glasses is brought in from a cold morning ride, and the lenses fog over in the warm office.

### HEAT-0128  ✅ keep  · 冷冻品出柜结霜
- draft: A cold glass baking dish is taken out of the fridge into a steamy kitchen, and it fogs over.

### HEAT-0129  ✅ keep  · 盖子内侧起雾
- draft: A pot of soup is covered with a glass lid, and the lid quickly fogs and drips on the inside.

### HEAT-0130  ❌ drop (must)  · 呼气起雾
- 冷手压在暖窗上留下雾手印：物理不明确（常见的是暖手在冷玻璃上），判定标准不可靠
- draft: A cold hand presses against a warm window from inside, and when it lifts away a foggy handprint is left on the glass.

### HEAT-0131  ❌ drop (must)  · 呼气起雾
- 围巾结霜需要零下且是分钟级累积
- draft: A jogger's breath fogs the inside of her scarf on a freezing morning, and frost forms on the fabric in front of her mouth.

### HEAT-0132  ✅ keep  · 冷容器外壁结露
- 雾只到奶线以下：最有判别力的结露条目
- draft: A cold bottle of milk is poured into a glass on a hot patio, and the outside of the glass mists over.

### HEAT-0133  ✅ keep  · 呼气起雾
- draft: Warm breath from a dog panting near a cold car window leaves a spreading fog patch on the glass.

### HEAT-0134  ⚠️ redundant (optional)  · 冷容器外壁结露
- '罐口内侧结露'场景别扭；与 0101 重复
- draft: A cold soda can is opened, and the inside of the rim and the top of the can bead with moisture as it sits in the sun.

### HEAT-0135  ⚠️ drop (redundant, P)  · 盖子内侧起雾
- 与 0129 重复
- draft: Hot tea is poured into a glass teapot, and the inside of the lid and upper glass fog with steam.

### HEAT-0136  ❌ drop (must)  · 热湿气碰冷面
- 一杯可可的蒸汽基本不会让旁边的窗起雾；期望本身站不住
- draft: A hot mug of cocoa steams on a windowsill on a cold day, and the steam fogs the window beside it.

### HEAT-0137  ❌ drop (must)  · 眼镜进暖室起雾
- 泳镜内起雾在游泳画面里看不见；慢
- draft: A swimmer's goggles fog up inside as she swims laps in a heated pool.

### HEAT-0138  ⚠️ drop (redundant, P)  · 冷冻品出柜结霜
- 与 0112/0150 重复
- draft: A frozen chocolate bar is taken out of the freezer, and a white frost forms on the wrapper within moments.

### HEAT-0139  ❌ drop (must)  · 盖子内侧起雾
- 需要'一分钟后重新打开'的跳切，5 秒单镜头做不到
- draft: A hot pizza is slid into a cardboard box and the lid is closed; when it is reopened a minute later the inside of the lid is damp and steaming.

### HEAT-0140  ⚠️ redundant (optional)  · 眼镜进暖室起雾
- 需要人凑近烤箱；与 0143 重复
- draft: A warm oven door is opened to check bread, and the glasses of the cook leaning in fog over from the escaping steam.

### HEAT-0141  ⚠️ redundant (optional)  · 冷容器外壁结露
- 大理石台面出汗：渲染和判定都很难
- draft: A cold marble countertop in a humid kitchen sweats a film of moisture that leaves damp patches under bowls set on it.

### HEAT-0142  ⚠️ drop (redundant, P)  · 冷容器外壁结露
- 与 0101 重复
- draft: A plastic water bottle taken from an ice chest at the beach fogs and beads with water as it sits in the sand.

### HEAT-0143  ✅ keep  · 眼镜进暖室起雾
- draft: A pair of glasses is carried into a steam room, and the lenses cloud over completely within seconds.

### HEAT-0144  ⚠️ redundant (optional)  · 冷容器外壁结露
- 与 0122 重复（滴落）
- draft: A cold glass of iced coffee stands on a humid balcony railing, and water drips from its base onto the railing.

### HEAT-0145  ✅ keep  · 热湿气碰冷面
- draft: A proofing cabinet full of warm moist air is opened, and the cool glass of the door immediately fogs on the inside.

### HEAT-0146  ✅ keep  · 热湿气碰冷面
- draft: A cold pane of glass is held over a steaming kettle, and it fogs and then drips from its lower edge.

### HEAT-0147  ⚠️ drop (redundant, P)  · 冷容器外壁结露
- 与 0101 重复
- draft: A cold gallon jug of milk is set on a shelf in a warm shop, and the jug turns cloudy with condensation on the outside.

### HEAT-0148  ⚠️ drop (redundant, P)  · 呼气起雾
- 与 0102/0106 重复
- draft: Breath is blown onto a cold hand mirror, and the fog on the glass hides the reflection for a moment before it clears.

### HEAT-0149  ✅ keep  · 冷容器外壁结露
- 手指只是划一下的工具，已最小化；划痕保留可判
- draft: A cold metal railing on a humid summer morning is covered in fine droplets, and a finger drags through them leaving a clear line.

### HEAT-0150  ✅ keep  · 冷冻品出柜结霜
- draft: A tray of ice cubes is taken from the freezer, and the cubes and tray frost over white.


## burn_smoke

### HEAT-0151  ✏️ modify  · 燃料被消耗
- 'is held to' 仍需要手；放到火上即可
- draft: A sheet of newspaper is held to a campfire flame, and the paper catches, curls, blackens, and falls apart into ash.
- **new caption:** A sheet of newspaper is laid over a campfire, and the paper catches, curls, blackens, and falls apart into ash.
- **new expectation:** The flame spreads across the paper from where it touched the fire, the paper curls and shrinks as it burns, and grey flakes drift down; the paper does not return or burn from a spot the flame never reached.

### HEAT-0152  ✅ keep  · 熄灭
- draft: A candle on a table is blown out, and a thin trail of smoke rises from the wick.

### HEAT-0153  ✅ keep  · 点燃
- draft: A match is struck against the side of its box, and it flares into a flame that settles to a steady burn.

### HEAT-0154  ⚠️ drop (redundant, P)  · 点燃
- 与 0184 重复
- draft: A lit match is touched to a candle wick, and the wick catches and holds a small flame.

### HEAT-0155  ✅ keep  · 燃料被消耗
- draft: A dry log is tossed onto a campfire, and a burst of sparks flies up into the night.

### HEAT-0156  ✅ keep  · 火焰随气流
- draft: Wind gusts across a campfire, and the flames lean over and stretch out sideways before standing up again.

### HEAT-0157  ✅ keep  · 烟的走向
- draft: A stick of incense is lit in a quiet room, and a thin ribbon of smoke rises from its tip and curls in the still air.

### HEAT-0158  ⚠️ redundant (optional)  · 熄灭
- 与 0152 重复（多支蜡烛版）
- draft: The candles on a birthday cake are blown out, and all the little flames go out and leave rising wisps of smoke.

### HEAT-0159  ⚠️ drop (redundant, P)  · 点燃
- 与 0153/0161 重复
- draft: A long barbecue lighter is clicked, and a small flame appears at its tip and burns steadily.

### HEAT-0160  ✅ keep  · 火焰随气流
- draft: The glowing embers in a fireplace are poked with a poker, and they brighten and send up a swirl of sparks.

### HEAT-0161  ✅ keep  · 点燃
- draft: The knob on a gas stove is turned, and a ring of blue flames lights around the burner.

### HEAT-0162  ✅ keep  · 熄灭
- draft: A metal snuffer is lowered over a candle flame, and the flame dies and smoke curls out from under the snuffer.

### HEAT-0163  ✅ keep  · 熄灭
- draft: A bucket of water is poured over a dying campfire, and the fire goes out with a hiss in a cloud of steam and smoke.

### HEAT-0164  ✏️ modify  · 燃料被消耗
- 去掉持烟花的手
- draft: A lit sparkler is held at arm's length, and it throws off a spray of bright sparks that fade as they fall.
- **new caption:** A lit sparkler stands upright in a cake, throwing off a spray of bright sparks that fade as they fall.
- **new expectation:** Sparks fly outward and downward from the burning point and go dark within a short distance; the burning point moves down the wire, never back up, and the spent wire above it is dark.

### HEAT-0165  ⚠️ redundant (optional)  · 熄灭
- 与 0012/0152 重复
- draft: A marshmallow on a stick catches fire over a campfire and is blown out, leaving it blackened.

### HEAT-0166  ✅ keep  · 点燃
- draft: A kerosene lamp is lit with a match, and the wick catches and the flame steadies inside the glass chimney.

### HEAT-0167  ✅ keep  · 燃料被消耗
- draft: A match is set to a pile of dry leaves, and the fire spreads across the pile with smoke rising from it.

### HEAT-0168  ✅ keep  · 燃料被消耗
- draft: A charcoal chimney starter is lit, and flames and smoke rise up through the coals from the paper burning below.

### HEAT-0169  ❌ drop (must)  · 烟的走向
- 余烬慢慢熄灭：5 秒内没有事发生，只能判'不变亮'
- draft: The last embers of a campfire are dying down under grey ash.

### HEAT-0170  ❌ drop (must)  · 火焰随气流
- 手是唯一动因；与 0152 重复
- draft: A hand waves over a candle that has just been blown out, and the rising smoke swirls and scatters.

### HEAT-0171  ✅ keep  · 闪燃/喷焰
- draft: A fatty burger is flipped on a grill, and fat drips onto the coals and a flame flares up under the patty.

### HEAT-0172  ✅ keep  · 火焰随气流
- draft: Air is blown gently onto the embers of a fire, and they glow brighter and a small flame springs up.

### HEAT-0173  ✅ keep  · 熄灭
- draft: A lid is slid over a small grease fire in a pan, and the flames go out.

### HEAT-0174  ✅ keep  · 烟的走向
- draft: Smoke drifts from a chimney on a windy day and is blown sideways as it leaves the stack.

### HEAT-0175  ⚠️ redundant (optional)  · 火焰随气流
- 与 0198 重复
- draft: A candle flame flickers as a draft passes the table, then steadies again.

### HEAT-0176  ✅ keep  · 烟的走向
- draft: A bonfire on a beach burns high, and sparks and embers rise into the dark sky and wink out.

### HEAT-0177  ✅ keep  · 闪燃/喷焰
- 可选：'clamped in a stand' 去掉持喷枪的手
- draft: A blowtorch heats a copper pipe, and the flame roars out of the nozzle in a blue cone.

### HEAT-0178  ⚠️ redundant (optional)  · 点燃
- 与 0161 重复
- draft: A stove-top burner is lit under a wok, and the flames spread around the burner ring and lick up its sides.

### HEAT-0179  ✅ keep  · 熄灭
- draft: A hose sprays water onto a burning shed, and the flames shrink and the smoke turns from black to white steam.

### HEAT-0180  ⚠️ drop (redundant, P)  · 熄灭
- 打火机盖合上：太小、太平凡
- draft: A cigarette lighter is snapped shut, and its flame vanishes at once.

### HEAT-0181  ✅ keep  · 熄灭
- draft: A lit sparkler is dropped into a bucket of water, and it goes out with a hiss and a puff of steam.

### HEAT-0182  ✅ keep  · 烟的走向
- draft: A campfire is fed with damp wood, and thick white smoke pours off the logs while the flames struggle.

### HEAT-0183  ⚠️ drop (redundant, P)  · 燃料被消耗
- 与 0189 重复，且手是目标
- draft: A burning twig is held upright, and the flame climbs along it toward the hand until it is dropped.

### HEAT-0184  ✅ keep  · 点燃
- draft: A row of tea-light candles is lit one after another with a long match, and each flame stands upright after it catches.

### HEAT-0185  ❌ drop (must)  · 燃料被消耗
- 人踩火 + 烟头
- draft: Dry grass beside a footpath catches from a dropped cigarette, and the small fire is stamped out with a boot.

### HEAT-0186  ✅ keep  · 闪燃/喷焰
- draft: Brandy is ignited in a pan, and a sheet of flame rises above the pan and then dies down.

### HEAT-0187  ✅ keep  · 燃料被消耗
- 可选：'on a stand' 去掉持放大镜的手；起烟要十几秒，写成 in progress 可接受
- draft: A magnifying glass focuses sunlight onto a dry leaf until a wisp of smoke appears and a small glowing spot begins to spread.

### HEAT-0188  ⚠️ redundant (optional)  · 火焰随气流
- 与 0156/0192 重复
- draft: A hearth fire roars up when a door opens and a draft sweeps through the room.

### HEAT-0189  ⚠️ redundant (optional)  · 燃料被消耗
- 与 0183 重复，手指在画面里
- draft: A wooden match burns down toward the fingers holding it and is dropped into an ashtray just before it reaches them.

### HEAT-0190  ✅ keep  · 燃料被消耗
- draft: A wooden skewer is dropped into the grill's coals and catches fire.

### HEAT-0191  ⚠️ redundant (optional)  · 点燃
- 纸灯笼：与 0166 重复且画面弱
- draft: A paper lantern's candle is lit, and the lantern glows from inside as the flame steadies.

### HEAT-0192  ✅ keep  · 火焰随气流
- draft: A gust blows across a row of candles on a windowsill, and the flames bend sideways and two of them go out, leaving smoke trails.

### HEAT-0193  ✅ keep  · 燃料被消耗
- draft: A handful of dry pine needles is fed to a small fire, and they crackle and flare up brightly before the flames settle.

### HEAT-0194  ⚠️ redundant (optional)  · 点燃
- 热水器引火：与 0161 重复，场景冷僻
- draft: The pilot on a water heater is lit with a long lighter, and a small steady blue flame appears and stays lit.

### HEAT-0195  ✅ keep  · 熄灭
- 火焰熄灭是秒级事件，可判
- draft: A candle inside a glass jar has burned down to its last pool of wax, and the flame goes out.

### HEAT-0196  ⚠️ redundant (optional)  · 烟的走向
- 与 0174 重复
- draft: Smoke from a neighbour's barbecue drifts over a garden fence and rises over the trees.

### HEAT-0197  ✅ keep  · 点燃
- draft: A lit match is dropped into a fire pit filled with kindling, and the fire catches and grows from the bottom up.

### HEAT-0198  ✅ keep  · 火焰随气流
- draft: A candle is set beside an open window on a windy night, and its flame streams sideways and flickers wildly.

### HEAT-0199  ✅ keep  · 点燃
- draft: A fire steel is scraped with a knife, and sparks shower onto a nest of dry tinder that begins to smoke and then flame.

### HEAT-0200  ⚠️ drop (redundant, P)  · 熄灭
- 手指捏灭：与 0162 重复
- draft: A candle is snuffed by pinching the wick between wet fingers, and the flame goes out with a faint hiss and a wisp of smoke.


## heat_response

### HEAT-0201  ✅ keep  · 烹煮质变/浮起
- draft: Frozen dumplings are dropped into a pot of boiling water; they sink at first, and the ones that have cooked bob back up to the surface.

### HEAT-0202  ✅ keep  · 受热膨胀/爆开
- draft: Popcorn kernels in a covered pot with hot oil begin to pop, jumping and turning into fluffy white pieces that fill the pot.

### HEAT-0203  ✅ keep  · 受热膨胀/爆开
- draft: Chestnuts roast in a pan over a fire, and their shells split open with a crack.

### HEAT-0204  ⚠️ redundant (optional)  · 受热膨胀/爆开
- 与 0249/0225 重复
- draft: A sealed bag of microwave popcorn inflates in the microwave, swelling into a puffed pillow.

### HEAT-0205  ✅ keep  · 塑料/蜡受热变形
- draft: A plastic spoon left resting on the rim of a hot frying pan droops and bends over the edge.

### HEAT-0206  ❌ drop (must)  · 塑料/蜡受热变形
- 结果态：蜡烛已经弯了，5 秒内没有事发生
- draft: A tall candle standing on the dashboard of a car parked in the sun has softened and bent over.

### HEAT-0207  ✅ keep  · 热空气上升
- 可选：'on a stand' 去掉手
- draft: A strip of tissue paper is held above a hot radiator, and it lifts and flutters upward in the warm air.

### HEAT-0208  ✅ keep  · 热空气上升
- draft: A hot oven door is opened, and the air above the opening shimmers and wavers.

### HEAT-0209  ✅ keep  · 水碰热面(与 boil_steam 重叠)
- draft: A bag of frozen vegetables is tipped into a hot wok, and the frost on them disappears with a hiss as they hit the pan.

### HEAT-0210  ❌ drop (must)  · 塑料/蜡受热变形
- 结果态；'as it is lifted' 又需要手
- draft: A gel ice pack left in the sun on a picnic blanket has gone soft and floppy.

### HEAT-0211  ✅ keep  · 水碰热面(与 boil_steam 重叠)
- draft: Wet chicken pieces are dropped into a pan of hot oil, and the oil spits and crackles violently for a moment.

### HEAT-0212  ✅ keep  · 受热膨胀/爆开
- draft: A marshmallow in a microwave swells to several times its size and then collapses when the door opens.

### HEAT-0213  ❌ drop (must)  · 塑料/蜡受热变形
- 结果态，且一张弯了的唱片从画面上判不出是热造成的
- draft: A vinyl record left on the back seat of a car in the sun has warped into a wavy shape.

### HEAT-0214  ✅ keep  · 热空气上升
- 可选：'on a stand' 去掉手
- draft: A paper pinwheel is held above a lit candle, and it begins to spin in the rising warm air.

### HEAT-0215  ✅ keep  · 塑料/蜡受热变形
- draft: A heat gun is aimed at the loose plastic wrap around a gift basket, and the wrap tightens and shrinks snugly around the basket.

### HEAT-0216  ⚠️ redundant (optional)  · 烹煮质变/浮起
- 与 0201 重复
- draft: A spoonful of gnocchi is dropped into boiling water, and the cooked ones rise to the surface one by one.

### HEAT-0217  ✅ keep  · 受热膨胀/爆开
- draft: Sausages sizzle in a hot pan, and one of them splits open along its side with a pop.

### HEAT-0218  ⚠️ redundant (optional)  · 受热膨胀/爆开
- 需要手按；与 0217/0203 重复
- draft: A baked potato is pulled from the oven, and when it is pressed its skin splits and a puff of steam escapes from the crack.

### HEAT-0219  ✅ keep  · 受热膨胀/爆开
- draft: A dented ping-pong ball is dropped into a bowl of very hot water, and the dent pops back out.

### HEAT-0220  ✅ keep  · 热空气上升
- draft: A hot air balloon's burner is fired, and the balloon lifts off the field.

### HEAT-0221  ❌ drop (must)  · 烘干
- 暖气片旁的湿伞看不到蒸汽
- draft: A wet umbrella is propped near a hot radiator, and steam rises off the fabric as it dries.

### HEAT-0222  ✅ keep  · 塑料/蜡受热变形
- draft: A plastic soda bottle is left too close to a campfire, and the near side shrivels and caves in.

### HEAT-0223  ✅ keep  · 水碰热面(与 boil_steam 重叠)
- draft: A few drops of water are flicked onto a hot griddle, and the drops skitter around and vanish.

### HEAT-0224  ❌ drop (must)  · 热空气上升
- 尘埃太细，生成器画不出，判官也看不见
- draft: Dust motes drift above a hot radiator in a sunlit room, rising and swirling in the warm air.

### HEAT-0225  ✅ keep  · 受热膨胀/爆开
- draft: A lidded plastic container of leftovers is heated in a microwave, and the lid domes upward and pops loose.

### HEAT-0226  ✅ keep  · 热空气上升
- draft: Heat rises from a barbecue grill on a summer afternoon, and the view of the fence behind it wavers in the shimmering air.

### HEAT-0227  ✅ keep  · 水碰热面(与 boil_steam 重叠)
- draft: Cooking oil is poured into a pan over high heat, and the oil begins to shimmer and ripple across its surface.

### HEAT-0228  ❌ drop (must)  · 塑料/蜡受热变形
- 结果态；巧克力融化已有多条
- draft: A chocolate bar left on a sunny windowsill has gone soft and bends over the edge of the sill.

### HEAT-0229  ✅ keep  · 烹煮质变/浮起
- draft: A handful of dry rice noodles is dropped into hot water, and they go from stiff and brittle to limp and floppy.

### HEAT-0230  ✅ keep  · 塑料/蜡受热变形
- draft: A plastic rain poncho hanging close to a patio heater crinkles and shrinks where the heat hits it.

### HEAT-0231  ✅ keep  · 烹煮质变/浮起
- draft: Hot water is poured over a pot of dried seaweed, and the crisp sheets swell and soften into flowing strands.

### HEAT-0232  ✏️ modify  · 受热膨胀/爆开
- 去掉夹子和手，架在网架上
- draft: A flour tortilla is held over a gas flame with tongs, and pockets of the tortilla puff up into bubbles.
- **new caption:** A flour tortilla lies on a wire rack over a gas flame, and pockets of the tortilla puff up into bubbles.
- **new expectation:** The bubbles rise on the upper side while the tortilla is over the flame and the underside browns in spots; the puffed pockets do not appear before heating and the browning does not fade.

### HEAT-0233  ⚠️ redundant (optional)  · 水碰热面(与 boil_steam 重叠)
- 与 0209/0041 重复
- draft: A frozen burger patty is dropped into a hot pan, and the ice on its surface crackles away in a burst of steam.

### HEAT-0234  ⚠️ redundant (optional)  · 热空气上升
- 与 0214 重复
- draft: A lit candle is placed beneath a hanging paper mobile, and the mobile's shapes begin to turn slowly.

### HEAT-0235  ✏️ modify  · 烘干
- 去掉持棍的手；篝火旁的湿袜确实能看到蒸汽
- draft: A damp sock is held over a campfire on a stick, and steam rises from it as it dries.
- **new caption:** A damp sock hangs from a stick propped beside a campfire, and steam rises from it.
- **new expectation:** Steam rises from the side of the sock facing the fire and drifts upward with the heat; the sock does not become wetter and the vapour does not sink.

### HEAT-0236  ⚠️ redundant (optional)  · 水碰热面(与 boil_steam 重叠)
- 与 0100/0211 重复
- draft: A basket of frozen spring rolls is lowered into hot oil, and the oil boils up around them in a rush of bubbles.

### HEAT-0237  ✏️ modify  · 塑料/蜡受热变形
- 去掉持尺的手
- draft: A plastic ruler is held over a candle flame, and the ruler softens and sags in the middle.
- **new caption:** A plastic ruler rests across two cans with a candle flame under its middle, and the ruler softens and sags.
- **new expectation:** Only the part above the flame softens and droops downward under its own weight; the ends stay straight on the cans; the bend does not straighten while the flame is under it.

### HEAT-0238  ✅ keep  · 烹煮质变/浮起
- draft: Bacon strips laid in a hot pan begin to sizzle, and the strips shrink and curl at the edges.

### HEAT-0239  ❌ drop (must)  · 烹煮质变/浮起
- 蜂蜜隔水变清要十几分钟，5 秒看不出
- draft: A jar of thick cloudy honey stands in a bowl of hot water, and the honey is turning clear and runny.

### HEAT-0240  ❌ drop (must)  · 烹煮质变/浮起
- 结果态
- draft: An ice cream truck's freezer door has been left open in the sun, and the ice cream sandwiches inside have sagged and softened in their wrappers.

### HEAT-0241  ⚠️ redundant (optional)  · 水碰热面(与 boil_steam 重叠)
- 与 0223 重复
- draft: A wet pasta strainer is dropped onto a hot burner, and water sizzles off the metal in a burst of steam.

### HEAT-0242  ❌ drop (must)  · 受热膨胀/爆开
- 结果态，且'比刚吹的更大'从画面上判不出来
- draft: A birthday balloon left in a car parked in the sun has swelled up.

### HEAT-0243  ✅ keep  · 塑料/蜡受热变形
- 手是触发（要用手扳直），不可避免
- draft: A hairdryer is aimed at a bent plastic pipe, and the pipe softens enough to be straightened by hand and holds its new shape when cool.

### HEAT-0244  ✅ keep  · 烹煮质变/浮起
- draft: A frozen block of soup sits in a pan over heat, sliding around on a thin layer of melt and shrinking as the liquid pools around it.

### HEAT-0245  ✅ keep  · 热空气上升
- draft: A lava lamp that has warmed up glows on a table, and the blobs of wax inside rise and sink.

### HEAT-0246  ✅ keep  · 黄油/油脂融化
- draft: A pat of cold butter is placed in the centre of a hot pancake on the griddle, and it slides and glides across the surface as it melts.

### HEAT-0247  ✅ keep  · 受热膨胀/爆开
- draft: Boiling water is poured into a collapsed vacuum-packed camping meal pouch, and the pouch swells and stands up.

### HEAT-0248  ✅ keep  · 水碰热面(与 boil_steam 重叠)
- draft: A cold egg is dropped into a pot of boiling water, and the water briefly stops boiling around it before the bubbling returns.

### HEAT-0249  ✅ keep  · 受热膨胀/爆开
- draft: A sheet of plastic wrap covers a bowl of leftovers heated in a microwave, and the wrap puffs up into a dome.

### HEAT-0250  ⚠️ redundant (optional)  · 烹煮质变/浮起
- 慢；与融化重复
- draft: A tub of frozen yogurt is left beside a stove, and the surface goes glossy and soft while the centre stays firm.

