#!/usr/bin/env python3
"""Triage of data/drafts/heat_draft.json against four criteria:
  person     - no human unless the body IS the physics
  timescale  - key change visible in 5-10 real seconds
  judgeable  - the judge can tell right from wrong from the frames
  variety    - 3-5 scenarios per phenomenon, no near-duplicates
Verdicts:  keep | modify (new caption/expectation given) | drop_must | drop_redundant (P = priority, to reach 200) |
           drop_redundant_optional (redundant but keepable if the count should stay above 200) | user_delete
Writes data/drafts/heat_draft_triage.json and data/drafts/heat_draft_triage.md.  Does NOT touch heat.json.
"""
import json
from collections import Counter, OrderedDict
from pathlib import Path

SRC = Path("/u/hchen56/phyRubric/data/drafts/heat_draft.json")
OUT_JSON = Path("/u/hchen56/phyRubric/data/drafts/heat_draft_triage.json")
OUT_MD = Path("/u/hchen56/phyRubric/data/drafts/heat_draft_triage.md")

V: "OrderedDict[str, dict]" = OrderedDict()
def keep(i, note="", pheno=""):            V[f"HEAT-{i:04d}"] = dict(verdict="keep", note=note, pheno=pheno)
def mod(i, c, e, note, pheno=""):          V[f"HEAT-{i:04d}"] = dict(verdict="modify", caption=c, expectation=e, note=note, pheno=pheno)
def must(i, note, pheno=""):               V[f"HEAT-{i:04d}"] = dict(verdict="drop_must", note=note, pheno=pheno)
def redP(i, note, pheno=""):               V[f"HEAT-{i:04d}"] = dict(verdict="drop_redundant", note=note, pheno=pheno)
def redO(i, note, pheno=""):               V[f"HEAT-{i:04d}"] = dict(verdict="drop_redundant_optional", note=note, pheno=pheno)
def udel(i, pheno=""):                     V[f"HEAT-{i:04d}"] = dict(verdict="user_delete", note="用户已决定删除", pheno=pheno)

# ================================================================ melt_freeze
ICE, FAT, CHOC, DESSERT, CHEESE, WAX, SET, THAW = "冰/雪融化", "黄油/油脂融化", "巧克力融化", "冰品融化", "芝士融化", "蜡/蜡笔融化", "凝固/定型", "解冻/去霜"
keep(1, "滴落本身是秒级事件；建议把 expectation 里 'the visible change may be small' 删掉，它削弱可判性", DESSERT)
keep(2, "热水浇冰块：快、无人、可判", ICE)
keep(3, "", FAT)
keep(4, "微波炉内景要透过门窗看，生成器可能只画外壳；用户已选，接受", FAT)
mod(5, "A bowl of half-melted chocolate sits in a pan of steaming water and is stirred with a spatula, and the remaining pieces melt into the liquid.",
       "The remaining pieces soften and lose their edges from the outside in and are smeared into the glossy liquid by the spatula; the melted part does not re-harden or break back into separate pieces while the water steams.",
       "隔水融化整碗巧克力要几分钟；从'半融'中段开始，5 秒内有可见变化，且只要求方向", CHOC)
keep(6, "红热铁球放冰上：快、无人、可判", ICE)
must(7, "太阳下柠檬水里的冰块 5 秒内看不出任何变化；expectation '比新冰更小更圆' 从画面上判不出来", ICE)
mod(8, "A fruit popsicle stands upright on its stick in a cup on a sunny table, and it drips down the stick.",
       "Drips run downward along the stick and collect in the cup; the popsicle looks glossy and soft and may slide on the stick; it does not refreeze, grow, or drip upward.",
       "去掉手：手只是接滴的地方，用杯子代替", DESSERT)
keep(9, "冰柱滴水：滴落是秒级事件", ICE)
keep(10, "", ICE)
keep(11, "溢出是秒级事件", WAX)
mod(12, "A marshmallow on a stick is propped over a campfire, and it puffs, softens and sags.",
        None, "可选：用'propped'去掉持棍的人；expectation 沿用 draft", WAX)
udel(13, ICE)
keep(14, "弱：小冰雹在晒热的路面上几十秒出湿圈，勉强够；用户保留了 caption", ICE)
udel(15, DESSERT)
keep(16, "雪花很小，480p 可能看不清，但物理和时间尺度都对", ICE)
keep(17, "", ICE)
mod(18, "A handful of shredded cheese is scattered onto a hot skillet, and the shreds melt and flow together into a bubbling layer.",
        "The shreds slump and go glossy where they touch the pan first, then merge into one layer that bubbles at the edges; they do not stay as separate dry strands or pull back apart.",
        "披萨在烤箱里：内景难画、芝士化开要 1–2 分钟；改成热锅上的芝士碎，秒级且无人", CHEESE)
keep(19, "", FAT)
must(20, "手指是主体，太阳下涂层软化是分钟级；巧克力已有 0005/0027/0037/0050", CHOC)
mod(21, "A dog with clumps of snow in its fur lies in front of a fireplace, and the snow melts and drips onto the floor.",
        "The clumps on the side facing the fire turn wet and shrink or slide off first, drops fall downward, and a wet patch forms on the floor; the snow does not stay white and fluffy or grow.",
        "室温下毛上的雪要几分钟；放到壁炉前，火侧先化，方向可判", ICE)
udel(22, DESSERT); udel(23, DESSERT); udel(24, FAT)
mod(25, "A small snowball is set on a hot griddle, and it hisses and collapses into water and steam.",
        "The snow darkens and slumps from the bottom where it touches the metal, meltwater spreads and sizzles around it and steam rises; the ball does not stay white and firm, grow, or refreeze.",
        "盘子上的雪球室温下要十几分钟；改成热铁板，秒级；和 0017（冰块滑动）是不同的错误模式", ICE)
keep(26, "", SET); keep(27, "", SET)
keep(28, "按按钮需要手，是不可避免的触发，被动语态可接受", SET)
keep(29, "", SET); keep(30, "盖章需要手，不可避免", SET); keep(31, "与 0027 是'脆壳 vs 软糖'两种凝固，保留", SET)
keep(32, "", WAX); keep(33, "", SET); keep(34, "", SET); keep(35, "", SET)
udel(36, SET)
mod(37, "Melted chocolate is piped in lines onto a metal tray straight from the freezer, and the lines set as they cool.",
        "The lines hold the shape they were piped in and turn from glossy to dull starting where they touch the cold metal; they do not spread out, run, or turn glossy again.",
        "'chilled tray' 上巧克力凝固要 1–2 分钟；改成冷冻托盘（几十秒），expectation 只要求方向", SET)
keep(38, "手指就是冷表面，人体即物理", SET)
keep(39, "", SET); keep(40, "", SET); keep(41, "", THAW); keep(42, "", THAW)
mod(43, "A wax crayon lies on a hot skillet, and it softens, slumps, and melts into a coloured pool.",
        "The crayon sags and loses its shape from the side touching the pan, and a pool of the same colour spreads out from it; it does not stay stiff, straighten, or change colour.",
        "结果态（'has softened'）5 秒内没有事发生；改成热锅上的蜡笔。若觉得和 0032 重复也可丢", WAX)
mod(44, "A block of frozen orange juice is dropped into a jug of hot water, and it melts, the orange colour spreading into the water.",
        "The block rounds off and shrinks while orange streaks sink and spread from it and the water turns steadily more orange; the block does not grow and the water does not clear again.",
        "冷水+搅拌是分钟级且需要手；改热水，无人，颜色扩散秒级可判", ICE)
mod(45, "A spoonful of solid white coconut oil is dropped into a hot frying pan, and it melts into clear liquid.",
        "The white lump turns glossy and clear from the bottom where it touches the pan and shrinks as a colourless pool spreads out around it; the pool stays clear with no foam or browning, and the oil does not stay white and solid or turn white again in the hot pan.",
        "'has turned clear' 是结果态，画面上只是一罐清液，判不出曾是固体；隔水加热又太慢（壁层变清要几十秒到一分钟）；改成热锅，几秒内白→透明，和 0003 黄油的区别是材料响应：不起泡不变黄", FAT)
must(46, "结果态 + 需要手拆包装；巧克力变体已够", CHOC)
mod(47, "A wedge of cheese sits under the heating element of a raclette grill, and the face nearest the element softens, sags and drips.",
        "Only the face toward the heat softens and goes glossy; drips run downward off the lowest point onto the plate below; the far side stays firm and the cheese does not stiffen again under the heat.",
        "'is held near a grill' 仍需要手；raclette 就是这个现象的无人版", CHEESE)
must(48, "太阳晒热的盘子上冰块要几分钟；与 0017 重复", ICE)
mod(49, "Warm water is poured over a frosted car windshield on a cold morning, and the frost clears where the water runs.",
        "The frost turns clear along the path of the water and the water runs downward off the glass; frost does not re-form on the wetted glass while the water is warm, and untouched areas stay frosted.",
        "刮霜是持续手部动作，暖风除霜是分钟级；改温水浇霜，秒级，且与 0035（水在冷玻璃上结冰）构成对照", THAW)
keep(50, "", SET)

# ================================================================ boil_steam
BOIL, OVER, KETTLE, LID, POUR, FLASH, PLUME, OFF, IRON = "锅内沸腾", "沸溢/奶泡", "壶/阀喷汽", "开盖出汽", "倒热液出汽", "水碰热面闪蒸", "静态汽羽", "关火停沸", "熨/蒸软化"
keep(51, "", KETTLE); keep(52, "", OVER); keep(53, "", BOIL); keep(54, "", LID); keep(55, "", OVER); keep(56, "", PLUME); keep(57, "", KETTLE)
keep(58, "", BOIL); keep(59, "", BOIL); keep(60, "", KETTLE)
keep(61, "弱：静态弥漫，只能判'不下沉'", PLUME)
keep(62, "熨斗被压下需要手，被动语态可接受", IRON)
keep(63, "", PLUME); keep(64, "", POUR); keep(65, "", BOIL); keep(66, "玻璃壶里气泡自底上升：最可判的沸腾条目", BOIL)
redO(67, "与 0053 重复（篝火只是换了背景）", BOIL)
keep(68, "", LID); keep(69, "", FLASH)
redP(70, "开盖出汽第 7 条；街头摊位隐含人群", LID)
keep(71, "", LID)
redP(72, "快空的咖啡壶：画面小、弱", BOIL)
must(73, "超声加湿器出的是冷雾，常常下沉贴桌面；'plume upward' 这个 expectation 本身物理上不可靠", PLUME)
keep(74, "关火后沸腾停止：很好的因果测试", OFF)
keep(75, "", POUR); keep(76, "", PLUME); keep(77, "", PLUME)
must(78, "暖气片（~60°C）上的湿毛巾基本看不到蒸汽，5 秒内也看不到变干", IRON)
keep(79, "", FLASH); keep(80, "", PLUME); keep(81, "", FLASH); keep(82, "", LID)
must(83, "活龙虾入锅：内容敏感，且现象是液面抬升不是热", BOIL)
keep(84, "肉片卷曲上浮其实更像 heat_response，可考虑改 subcategory", BOIL)
must(85, "铺沥青必然有工人在画面里", PLUME)
keep(86, "", IRON)
redP(87, "与 0054 重复（微波炉版）", LID)
keep(88, "keep_person：跑者的身体就是汽源", PLUME)
redO(89, "壁炉前的湿狗变干：慢；与 0235 重叠", PLUME)
keep(90, "", FLASH); keep(91, "", FLASH)
redP(92, "与 0064/0075 重复", POUR)
redP(93, "与 0056 重复（浓缩咖啡版）", PLUME)
keep(94, "加了颜色扩散，比 0064 多一个可判项", POUR); keep(95, "", PLUME)
redP(96, "与 0223（水珠在热铁板上跳）重复，且'熨斗板朝上滴水'场景别扭", FLASH)
redP(97, "开盖出汽第 8 条", LID)
keep(98, "", OVER); keep(99, "", PLUME); keep(100, "与 0211 是'冻霜 vs 表面水'两种变体，保留", FLASH)

# ================================================================ condensation
COLD, BREATH, GLASSES, WARMAIR, LIDIN, FROST, COLDAIR, CAR = "冷容器外壁结露", "呼气起雾", "眼镜进暖室起雾", "热湿气碰冷面", "盖子内侧起雾", "冷冻品出柜结霜", "冷雾下沉", "车内起雾"
keep(101, "", COLD); keep(102, "", BREATH); keep(103, "静态：只能判雾均匀、不瞬间消失", WARMAIR); keep(104, "", GLASSES); keep(105, "", COLD); keep(106, "", BREATH)
keep(107, "", WARMAIR); keep(108, "keep_person：乘客的呼吸就是水源", CAR)
keep(109, "冷雾下沉，是'蒸汽上升'的反例，很有价值", COLDAIR); keep(110, "", LIDIN); keep(111, "keep_person", BREATH)
keep(112, "", FROST); keep(113, "结霜杯→水珠，秒级", COLD)
redO(114, "冷容器结露第 n 条", COLD)
keep(115, "", WARMAIR); keep(116, "", LIDIN); keep(117, "", GLASSES); keep(118, "keep_person：头盔面罩随呼吸起雾，人体即物理", BREATH)
redO(119, "温室玻璃早晨变干：慢", WARMAIR)
keep(120, "", COLDAIR)
redO(121, "与 0101/0113 重复", COLD)
keep(122, "水管滴水是事件，可判", COLD)
redP(123, "与 0104 重复", GLASSES)
redO(124, "与 0107/0115 重复", WARMAIR); redO(125, "与 0105 重复", COLD); redO(126, "与 0115 重复", WARMAIR)
redP(127, "与 0104 重复", GLASSES)
keep(128, "", FROST); keep(129, "", LIDIN)
must(130, "冷手压在暖窗上留下雾手印：物理不明确（常见的是暖手在冷玻璃上），判定标准不可靠", BREATH)
must(131, "围巾结霜需要零下且是分钟级累积", BREATH)
keep(132, "雾只到奶线以下：最有判别力的结露条目", COLD); keep(133, "", BREATH)
redO(134, "'罐口内侧结露'场景别扭；与 0101 重复", COLD)
redP(135, "与 0129 重复", LIDIN)
must(136, "一杯可可的蒸汽基本不会让旁边的窗起雾；期望本身站不住", WARMAIR)
must(137, "泳镜内起雾在游泳画面里看不见；慢", GLASSES)
redP(138, "与 0112/0150 重复", FROST)
must(139, "需要'一分钟后重新打开'的跳切，5 秒单镜头做不到", LIDIN)
redO(140, "需要人凑近烤箱；与 0143 重复", GLASSES)
redO(141, "大理石台面出汗：渲染和判定都很难", COLD)
redP(142, "与 0101 重复", COLD)
keep(143, "", GLASSES)
redO(144, "与 0122 重复（滴落）", COLD)
keep(145, "", WARMAIR); keep(146, "", WARMAIR)
redP(147, "与 0101 重复", COLD)
redP(148, "与 0102/0106 重复", BREATH)
keep(149, "手指只是划一下的工具，已最小化；划痕保留可判", COLD)
keep(150, "", FROST)

# ================================================================ burn_smoke
IGN, EXT, AIR, SMOKE, CONSUME, FLARE = "点燃", "熄灭", "火焰随气流", "烟的走向", "燃料被消耗", "闪燃/喷焰"
mod(151, "A sheet of newspaper is laid over a campfire, and the paper catches, curls, blackens, and falls apart into ash.",
         "The flame spreads across the paper from where it touched the fire, the paper curls and shrinks as it burns, and grey flakes drift down; the paper does not return or burn from a spot the flame never reached.",
         "'is held to' 仍需要手；放到火上即可", CONSUME)
keep(152, "", EXT); keep(153, "", IGN)
redP(154, "与 0184 重复", IGN)
keep(155, "", CONSUME); keep(156, "", AIR); keep(157, "", SMOKE)
redO(158, "与 0152 重复（多支蜡烛版）", EXT)
redP(159, "与 0153/0161 重复", IGN)
keep(160, "", AIR); keep(161, "", IGN); keep(162, "", EXT); keep(163, "", EXT)
mod(164, "A lit sparkler stands upright in a cake, throwing off a spray of bright sparks that fade as they fall.",
         "Sparks fly outward and downward from the burning point and go dark within a short distance; the burning point moves down the wire, never back up, and the spent wire above it is dark.",
         "去掉持烟花的手", CONSUME)
redO(165, "与 0012/0152 重复", EXT)
keep(166, "", IGN); keep(167, "", CONSUME); keep(168, "", CONSUME)
must(169, "余烬慢慢熄灭：5 秒内没有事发生，只能判'不变亮'", SMOKE)
must(170, "手是唯一动因；与 0152 重复", AIR)
keep(171, "", FLARE); keep(172, "", AIR); keep(173, "", EXT); keep(174, "", SMOKE)
redO(175, "与 0198 重复", AIR)
keep(176, "", SMOKE); keep(177, "可选：'clamped in a stand' 去掉持喷枪的手", FLARE)
redO(178, "与 0161 重复", IGN)
keep(179, "", EXT)
redP(180, "打火机盖合上：太小、太平凡", EXT)
keep(181, "", EXT); keep(182, "", SMOKE)
redP(183, "与 0189 重复，且手是目标", CONSUME)
keep(184, "", IGN)
must(185, "人踩火 + 烟头", CONSUME)
keep(186, "", FLARE); keep(187, "可选：'on a stand' 去掉持放大镜的手；起烟要十几秒，写成 in progress 可接受", CONSUME)
redO(188, "与 0156/0192 重复", AIR); redO(189, "与 0183 重复，手指在画面里", CONSUME)
keep(190, "", CONSUME)
redO(191, "纸灯笼：与 0166 重复且画面弱", IGN)
keep(192, "", AIR); keep(193, "", CONSUME)
redO(194, "热水器引火：与 0161 重复，场景冷僻", IGN)
keep(195, "火焰熄灭是秒级事件，可判", EXT)
redO(196, "与 0174 重复", SMOKE)
keep(197, "", IGN); keep(198, "", AIR); keep(199, "", IGN)
redP(200, "手指捏灭：与 0162 重复", EXT)

# ================================================================ heat_response
SOFT, PUFF, CONV, COOK, HFLASH, DRY = "塑料/蜡受热变形", "受热膨胀/爆开", "热空气上升", "烹煮质变/浮起", "水碰热面(与 boil_steam 重叠)", "烘干"
keep(201, "", COOK); keep(202, "", PUFF); keep(203, "", PUFF)
redO(204, "与 0249/0225 重复", PUFF)
keep(205, "", SOFT)
must(206, "结果态：蜡烛已经弯了，5 秒内没有事发生", SOFT)
keep(207, "可选：'on a stand' 去掉手", CONV); keep(208, "", CONV); keep(209, "", HFLASH)
must(210, "结果态；'as it is lifted' 又需要手", SOFT)
keep(211, "", HFLASH); keep(212, "", PUFF)
must(213, "结果态，且一张弯了的唱片从画面上判不出是热造成的", SOFT)
keep(214, "可选：'on a stand' 去掉手", CONV); keep(215, "", SOFT)
redO(216, "与 0201 重复", COOK)
keep(217, "", PUFF)
redO(218, "需要手按；与 0217/0203 重复", PUFF)
keep(219, "", PUFF); keep(220, "", CONV)
must(221, "暖气片旁的湿伞看不到蒸汽", DRY)
keep(222, "", SOFT); keep(223, "", HFLASH)
must(224, "尘埃太细，生成器画不出，判官也看不见", CONV)
keep(225, "", PUFF); keep(226, "", CONV); keep(227, "", HFLASH)
must(228, "结果态；巧克力融化已有多条", SOFT)
keep(229, "", COOK); keep(230, "", SOFT); keep(231, "", COOK)
mod(232, "A flour tortilla lies on a wire rack over a gas flame, and pockets of the tortilla puff up into bubbles.",
         "The bubbles rise on the upper side while the tortilla is over the flame and the underside browns in spots; the puffed pockets do not appear before heating and the browning does not fade.",
         "去掉夹子和手，架在网架上", PUFF)
redO(233, "与 0209/0041 重复", HFLASH); redO(234, "与 0214 重复", CONV)
mod(235, "A damp sock hangs from a stick propped beside a campfire, and steam rises from it.",
         "Steam rises from the side of the sock facing the fire and drifts upward with the heat; the sock does not become wetter and the vapour does not sink.",
         "去掉持棍的手；篝火旁的湿袜确实能看到蒸汽", DRY)
redO(236, "与 0100/0211 重复", HFLASH)
mod(237, "A plastic ruler rests across two cans with a candle flame under its middle, and the ruler softens and sags.",
         "Only the part above the flame softens and droops downward under its own weight; the ends stay straight on the cans; the bend does not straighten while the flame is under it.",
         "去掉持尺的手", SOFT)
keep(238, "", COOK)
must(239, "蜂蜜隔水变清要十几分钟，5 秒看不出", COOK)
must(240, "结果态", COOK)
redO(241, "与 0223 重复", HFLASH)
must(242, "结果态，且'比刚吹的更大'从画面上判不出来", PUFF)
keep(243, "手是触发（要用手扳直），不可避免", SOFT); keep(244, "", COOK); keep(245, "", CONV)
keep(246, "", FAT); keep(247, "", PUFF); keep(248, "", HFLASH); keep(249, "", PUFF)
redO(250, "慢；与融化重复", COOK)

# ---------------------------------------------------------------- build
recs = json.loads(SRC.read_text())
assert len(V) == len(recs) == 250, (len(V), len(recs))
out = []
for r in recs:
    v = V[r["id"]]
    row = {"id": r["id"], "subcategory": r["subcategory"], "pheno": v["pheno"], "verdict": v["verdict"], "note": v["note"],
           "draft_caption": r["caption"], "draft_expectation": r["expectation"]}
    if v["verdict"] == "modify":
        row["new_caption"] = v["caption"]
        row["new_expectation"] = v["expectation"] or r["expectation"]
    out.append(row)
OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")

cnt = Counter(o["verdict"] for o in out)
kept_after_must = 250 - cnt["drop_must"] - cnt["user_delete"]
kept_after_P = kept_after_must - cnt["drop_redundant"]
kept_after_all = kept_after_P - cnt["drop_redundant_optional"]

L = []
L.append("# Heat draft triage\n")
L.append("标准：**人体**（无人，除非身体就是物理）· **时间尺度**（5–10 s 内看得到关键变化）· **可判断**（画面上能判对错）· **变体**（每现象 3–5 个，不要近重复）\n")
L.append("| 判定 | 数量 | 说明 |\n|---|---|---|")
L.append(f"| keep | {cnt['keep']} | 符合 |")
L.append(f"| modify | {cnt['modify']} | 可修改，下面给了新 caption/expectation |")
L.append(f"| user_delete | {cnt['user_delete']} | 用户已删 |")
L.append(f"| drop_must | {cnt['drop_must']} | 必须丢：时间尺度/物理/可判性有硬伤 |")
L.append(f"| drop_redundant (P) | {cnt['drop_redundant']} | 近重复，优先丢，丢完正好 {kept_after_P} 条 |")
L.append(f"| drop_redundant_optional | {cnt['drop_redundant_optional']} | 近重复但可保留；全丢则剩 {kept_after_all} 条 |")
L.append(f"\n必删后剩 **{kept_after_must}**；再丢 P 级冗余后剩 **{kept_after_P}**。\n")

L.append("## 现象覆盖（必删 + P 级丢弃之后）\n")
L.append("| subcategory | 现象 | 保留数 | 保留 id |\n|---|---|---|---|")
alive = [o for o in out if o["verdict"] in ("keep", "modify", "drop_redundant_optional")]
by = OrderedDict()
for o in alive:
    by.setdefault((o["subcategory"], o["pheno"]), []).append(o["id"].split("-")[1] + ("*" if o["verdict"] == "drop_redundant_optional" else ""))
for (sc, ph), ids in by.items():
    L.append(f"| {sc} | {ph} | {len(ids)} | {' '.join(ids)} |")
L.append("\n`*` = drop_redundant_optional（可丢可留）。\n")

for sc in ("melt_freeze", "boil_steam", "condensation", "burn_smoke", "heat_response"):
    L.append(f"\n## {sc}\n")
    for o in out:
        if o["subcategory"] != sc: continue
        tag = {"keep": "✅ keep", "modify": "✏️ modify", "drop_must": "❌ drop (must)", "drop_redundant": "⚠️ drop (redundant, P)",
               "drop_redundant_optional": "⚠️ redundant (optional)", "user_delete": "🗑 user_delete"}[o["verdict"]]
        L.append(f"### {o['id']}  {tag}  · {o['pheno']}")
        if o["note"]: L.append(f"- {o['note']}")
        L.append(f"- draft: {o['draft_caption']}")
        if o["verdict"] == "modify":
            L.append(f"- **new caption:** {o['new_caption']}")
            L.append(f"- **new expectation:** {o['new_expectation']}")
        L.append("")
OUT_MD.write_text("\n".join(L) + "\n")
print(dict(cnt), "after_must", kept_after_must, "after_P", kept_after_P, "after_all", kept_after_all)
