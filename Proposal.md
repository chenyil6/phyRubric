# 面向视频生成的物理常识评测：全面的 benchmark、rubric 驱动的构建流程与开源可诊断 judge

## 摘要

中文版

判断一段生成视频"物理上对不对"，靠的不是教科书定律，而是每个人从日常经验中获得的物理常识：东西松手会掉、推一下会滑一段再停、玻璃摔了会碎、镜子里的影像跟着人动。现有评测在两头都出了问题：一头是覆盖面——几乎只有力学，光、热极少，声、电为零，还混进了需要专业知识的现象（丁达尔效应、焰色反应、涡流）；另一头是标签——标注员对着一组泛化的问题凭直觉打 1–5 分，同一个问题套用在所有视频上，judge 学到的也只是一个分数。我们提出三点贡献：(1) 一个以**物理常识**为边界、按力、热、光、电、声五个分支 × 十类违规组织、力 315、热 250、光 277、电 252、声 96、共 1,190 条 caption、每条配多个生成模型的视频、从零生成并经人工校验的全面 benchmark 与训练集；(2) 一套 **rubric 驱动的构建流程**——为每条 caption 写定制 rubric，每个物理项是"应看到什么 / 看到什么算违反"的可证伪对，按 fatal / core / major / minor 分级且分级对应直觉物理的层次，再由大 VLM 依 rubric 逐项判定、写出理由，人工复核；(3) 一个在该数据上训练的**开源 VLM judge**，比较 LoRA-SFT 直接输出分数与理由、以及 cold-start SFT + GRPO 输出思维链两种路线，输出的诊断可直接反馈给生成模型。

英文版

Whether a generated video "looks physically right" is judged not by textbook laws but by the physical commonsense everyone acquires from everyday experience: released objects fall, a pushed object coasts then stops, dropped glass shatters, a mirror image moves with its subject. Existing evaluations fail at both ends. Coverage: almost exclusively mechanics, little optics or heat, no acoustics or electricity, and a fair share of phenomena that require expert knowledge (Tyndall scattering, flame colours, eddy currents). Labels: annotators answer a fixed set of generic 1–5 questions by intuition, the same questions for every video, and the resulting judges learn nothing but a number. We contribute (1) a comprehensive benchmark and training set scoped to physical commonsense, organised as five branches (mechanics, heat, light, electricity, sound) × ten violation types, with 315 captions for mechanics, 250 for heat, 277 for light, 252 for electricity and 96 for sound (1,190 in total: 945 train, 245 eval), each rendered by several video generators, generated from scratch and human-verified; (2) a rubric-driven construction pipeline in which every caption receives a bespoke rubric of falsifiable expect/fail items graded fatal / core / major / minor, with grades anchored to levels of intuitive physics, and a large VLM decides each item and writes the rationale under human review; (3) an open VLM judge trained on this data, comparing LoRA-SFT that emits score and reason against cold-start SFT + GRPO that emits a chain of thought, whose diagnosis can be fed back to the generator.

## 1. 什么是物理常识

认知科学里对应的概念是 **intuitive physics**：

> "the knowledge underlying the human ability to understand the physical environment and interact with objects and substances that undergo dynamic state changes, making at least approximate predictions about how observed events will unfold." — Kubricht, Holyoak & Lu, *Trends in Cognitive Sciences* 2017

三个关键词：**objects and substances**（不只刚体，也包括液体、颗粒、气体）、**approximate**（是近似预期，不是数值）、**how events unfold**（关于过程，不是静态事实）。NLP 里 PIQA 对 physical commonsense 的界定与之一致——"knowledge about everyday objects: their physical properties, affordances, and how they can be manipulated"——并在标注时**明确删除了需要专业知识的条目**，"which should not fall under the umbrella of commonsense"。

我们采用的工作定义：

> **物理常识**：一个没有仪器、不知道任何定律名称的人，仅凭日常经验，在观看一段几秒钟的视频时会隐式形成、并在被违反时能够察觉的预期。

发展心理学给出了这些预期的层次，我们用它校准 rubric 的严重度（§4.2）：

| 层 | 内容 | 来源 |
|---|---|---|
| **L1 核心物体原则** | 恒存（不凭空出现/消失）、实体性（不互相穿透）、时空连续（不瞬移）、内聚与不变性（不自行分裂、合并、变形、换身）、接触（不隔空作用） | Spelke & Kinzler 2007；Baillargeon（persistence）；Piloto et al. 2022 (PLATO)；IntPhys 2 |
| **L2 日常动力学** | 重力与支撑、惯性（惰性物体不自发启动、不自发反向、被推则动）、碰撞与反弹、材料类别各有的响应（刚体、软体、液体、颗粒、气体）、容纳/遮挡/覆盖等事件类别；**自驱动主体（人、动物、机动车）免除"无因运动"约束** | Lin, Stavans & Baillargeon 2022；Lake et al. 2017 |
| **L3 日常现象经验** | 知道结果、不需要机制：冰会融、水会沸、油浮在水上、影子背着光、镜像是反的、磁铁吸铁、开关一按灯就亮、敲鼓鼓面会振 | PIQA；Kubricht "approximate" |
| **排除** | 需要定律名称、数值比较或实验室条件才有预期的现象；技能与姿态；无事件的静态场景 | PIQA 的删除规则 |

## 2. 前人的不足

### 2.1 覆盖不全，且混入了不属于常识的内容

对四个主要 benchmark 逐条统计（本项目实测）：

| Benchmark | 规模 | 实际覆盖 | 不属于常识 |
|---|---|---|---|
| VideoPhy-1 | 344 caption | 全部为**力**：solid_solid 143 / solid_fluid 146 / fluid_fluid 55 | 0，但 13 条静态无事件 |
| VideoPhy-2 | 600 caption | 定律域 **力学 90.1%** / 流体 3.1% / 光 2.7% / 热 1.0%；422/600 是 Sports | 0，但大量"动作难看"被当成物理违规 |
| PhyGenBench | 160 caption | Force 40 / Light 50 / Heat 30 / Properties 25 / Chemical 15 | **35 条明确不是**（Tyndall 10、干涉衍射 10、焰色 5、石蕊 5、浓硫酸 5），30 条边界；**47/160 条定律本身有错**、3 条与 caption 矛盾 |
| PhyWorldBench | 315 场景 | 9 类：力学 5 类、光影 1、变形 1、尺度 1、生物力学 1 | **56 条不是**（电磁 7、色差 7、半影 7、跨尺度定量比较 35）、14 条非物理（反射行为、精细技能） |

四个 benchmark **合起来**，力学是唯一被充分覆盖的分支；热与光只有几十条；电、声为零；约 15–20% 的条目需要中学以上的物理/化学知识才能形成预期。更近的 PhyGround（2026）以 13 条教科书定律组织（固体 6、流体 5、光学 2），自称评的是 physical reasoning，同样不涉及热、电、声。

另一个共同缺陷是**分类轴错位**：所有 benchmark 都按定律命名类别（"Conservation of Momentum"、"Newton's First Law"），而生成视频实际的错法是另一套东西。我们把 VideoPhy-2 中 3631 条人类手写违规按错法归类：形变/形状漂移 674、人体解剖异常 572、轨迹/速度 440、悬浮/坠落 372、无因运动 352、数量变化 148、凭空出现消失 124、穿模 107——其中超过 1600 条属于 L1 核心物体原则，却没有任何 benchmark 把它作为类别。

### 2.2 标签泛化、凭直觉，judge 只学到一个数

VideoPhy-1/2 对整段视频给一个 SA 分和一个 PC 分，没有定义"扣分扣在哪"。PhyGround 前进了一步——把 PC 拆成 3 个通用维度（外观/形状/存在一致性、事件时序、prompt 对齐）加 2–4 个按定律预设的子问题，每个 1–5 分并让标注员写一句理由——但每个子问题是**同一条律套所有视频的通用措辞**（"To what extent does liquid flow along surfaces, spread, and drain in a physically plausible manner?"），预期是什么、看到什么算违反，全靠标注员当场发挥，不同标注员、不同视频之间没有共同的可证伪基准。用这样的标签训出来的 judge（VideoCon-Physics、AutoEval、PhyJudge-9B）自然只能输出分数，没有解释、没有定位、没有可回溯的依据。

这些 judge 还有一个从未被检验的盲区：**它们的训练分布决定了它们只是力学 judge**。judge 的物理知识住在权重里，训练数据偏什么它就只会什么——VideoCon-Physics 的训练 caption 100% 是力学与流体，AutoEval 的训练集 90% 力学（热 1%、光 2.7%、电 0），PhyJudge-9B 的 13 条律不含热与电。它们在热、光、电上的能力从未被测量过，因为没有 benchmark 能测（§6 实验 3）。

### 2.3 评判与生成脱耦

分数下降到 2 分，是因为物体消失了、液体倒流了、还是人多了一只手？现有 judge 不回答这个问题，因此评判结果无法用于改进生成。

## 3. 贡献一：全面的物理常识 benchmark 与训练集

**出发点。** §2.1 的统计表明，现有 benchmark 绝大多数样本落在力学一个维度：VideoPhy-1 100%、VideoPhy-2 约 90%、PhyWorldBench 九类中五类为力学，PhyGenBench 是唯一在光、热上有几十条样本的，电、声在所有 benchmark 里为零。用这样的数据评一个生成模型，得到的只是"它的力学常识如何"，对它是否知道冰会融、影子背光、开关一按灯就亮、敲鼓鼓面会振，几乎没有任何测量——**对模型物理知识的评测是不全面的**。我们的 benchmark 共 **1,190 条 caption：力 315、热 250、光 277、电 252、声 96**，每条 caption 用多个生成模型出视频。四个主分支数量相近（250–315 条），使每个分支都能单独报告一个有统计意义的分支分数，模型的物理常识画像因此是多维的而不是一维的；声学分支较小，因为无音轨视频里只能评声音的可见效果（见 §3.1）。分支近似等量而非按"生活中出现的频率"分配，是有意的：分支分数的可靠性取决于该分支的样本数，而频率本身没有客观定义——VideoPhy-2 的 90% 力学并非测得的频率，只是它从动作数据集抽 caption 带来的偏差。频率信息放在汇总层：报告分支分数的等权平均，也可以报告任意加权的总分。

### 3.1 两轴组织

- **场景轴（五分支）**——要检验什么，每个分支只收肉眼可判的常识层内容：
  - **力**：重力/下落/支撑、惯性与滑行停止、碰撞与反弹、摩擦与滚动、抛体弧线、平衡与倾倒、绳与布的张力、弹性/塑性/脆性变形、切割与撕裂；流体（倾倒、飞溅、浮沉、流动、黏度）、颗粒（沙、盐）、气体（风、烟）；人与动物的肢体可行性与步态。
  - **热**：融化与快速凝固（冰淇淋化掉、蜡滴变硬）、沸腾与蒸汽、玻璃起雾、火焰与烟的行为（火苗向上、纸卷曲成灰）、受热的物理响应（塑料勺软塌、爆米花爆开、饺子煮熟浮起）；核心判据是**过程方向不可逆**。变色类变化（蛋清变白、褐变、焦糖化）是化学，不收。
  - **光**：影子（方向一致、贴着物体、随物体动）、镜面与水面倒影（左右反、随主体动）、透过玻璃与水看东西、光源一致性、遮挡、棱镜/彩虹、颜料混色。
  - **电**：开关与灯、插头、闪电闪光、焊接火花、磁铁吸铁与贴冰箱、静电吸附、电动玩具启停。排除涡流、静电斥力等需要机制的现象。
  - **声**：定义为**声音的可见后果**。无音轨视频里声音本身不可观测，本分支不评听觉，只评三类肉眼可见的力学后果：(a) 被敲击/拨动的物体自身的大幅低频运动（鼓面下陷回弹、低音提琴弦左右摆、镲片晃动、钢尺上下抖）；(b) 声源让别的东西动（低音炮旁杯中水起波纹、桌上米粒跳动、重卡驶过碗碟哐哐响、蜡烛火苗随低音抖）；(c) 发声装置自身的往复运动随开关起停（音箱纸盆、桌上震动挪位的手机、甩干中的洗衣机）。高频小幅振动本身在视频分辨率下不可见（音叉叉股、酒杯口、锣面、口琴簧片的"发糊"），这类现象只有放大成可见的次级效果才收——沿用课堂演示的做法：音叉插水溅起水花、吊着的乒乒球被锣弹开、琴弦上的纸片被弹飞、木琴条上的盐粒跳起、弓拉镲片上的沙子聚成线、贴在震动玻璃上的纸条抖动。人或动物对声音的反应属于行为而非物理，不收。因可判现象有限，本分支样本较少：2026-09-14 按可见性清理后训练集 76 条、评测集 20 条，音视频联合评测留作未来工作。
- **违规轴（十类）**——会怎么错：恒存与数量 / 形状与同一性 / 实体性（穿模）/ 无因运动与启停 / 重力方向 / 轨迹与动量 / 过程方向与顺序 / 缺失后果 / 材料响应错误 / 属性漂移。

每条 caption 在场景轴上有一个主标签；caption 的设计使某几类预期处于"风险中"（有遮挡则考恒存，有抛掷则考惯性与轨迹，有相变则考过程方向），rubric 的每个 PC 项在违规轴上有一个标签。评测报告在两个轴上分别汇总，既能回答"模型在热学上多差"，也能回答"模型最常犯的是穿模还是无因运动"。

### 3.2 规模与来源

**从零生成，不复用现有 benchmark 的 caption。** 以五分支的常识清单和十类违规为条件，生成并经三轮 review 后保留 **1,190 条 caption：力 315、热 250、光 277、电 252、声 96**，要求：日常场景、有明确的动态事件与可见结果、单句可拍摄、不含定律名词与数值、不含装饰性形容。分支内部按违规类型分格，每个格子设最小样本数，保证违规轴上的汇总同样有意义。生成的 caption 全部经人工 **review、矫正、verification**（§4.1）。

**划分**：力 **240 条训练、75 条评测**，热 **200 / 50**，光 **227 / 50**，电 **202 / 50**，声 **76 / 20**，即训练集 945、评测集 245；力学评测集较大是为了让 15 个子类各有 5 条，可以按子类出数。评测 id 固定从 0251（声 0101）起编，训练 id 与之之间的空档是有意保留的，训练集增删不重编评测集；划分按 caption 进行，两边在分支与违规类型上分布一致，评测 caption 不与任何训练 caption 共享场景模板。

现有四个 benchmark 经 §1 边界筛选后作为**外部测试集**，用于检验 judge 是否过拟合于自家的 caption 分布。

**视频：prompt 少、模型多。** 成本落在 caption 上（写作、rubric、人工 review 都按 caption 计），而一份 rubric 可复用于该 caption 下所有模型的视频，所以用较少的 caption 配较多的生成模型最划算，同一 caption 下不同模型的视频也天然给出质量分布。训练集每条 caption 用 3 个开源文生视频模型（CogVideoX1.5-5B、Wan2.2-T2V-A14B、LTX-Video-2B）生成，约 2,835 个视频，与 VideoPhy-2 训练集（3,343 个视频、每条 prompt 仅 1 个视频）同量级，但每条 caption 有 3 个模型的视频；评测集每条用 7–8 个模型——上述 3 个训练用模型，加上只在评测集出现的 HunyuanVideo-1.5、Wan2.2-TI2V-5B、Cosmos-Predict2.5-2B 与 1–2 个闭源模型——约 1,700–1,960 个视频。只在评测集出现的模型用来衡量 judge 对未见过的生成器的泛化。

**评测集标注：人是最终标签，但人核对 VLM 而不是从零标。** 训练集的标签来自教师 VLM（§4.3），评测集若也全靠同一个 VLM，会出现两个问题：judge 在评测集上的分数量的只是"学生与老师多像"而非"判得对不对"；生成模型的排名也只是这个 VLM 的偏好，没有人背书。所以 245 条 caption 的全部视频（约 1,700–1,960 个）由人给出最终的 rubric 逐项判定，SA/PC 分由判定算出。具体做法是教师 VLM 先逐项判并写出依据画面的理由，标注员看视频与理由后对每项点"同意 / 推翻"，推翻的改写答案——rubric 把人的工作从"凭直觉打 1–5 分"变成"核对几条可判真假的陈述"，每个视频只需几十秒到一两分钟，全量核对约 40–60 人时，不同标注员的答案也可复核一致；若人力不够则分层抽样（按分支 × 生成模型），抽样部分给出人工标签，其余沿用 VLM 标签并报告抽样测得的误差。这套核对同时直接产出教师 VLM 与人的逐项一致率，是 §4.3 标注 pipeline 可信度的核心报告指标。标注量与 PhyGround（1,831 个视频）同量级；标注员不要求物理专业背景——这与"常识"的定义一致，也与 VideoPhy-2 用 STEM 标注员的做法形成对照。

### 3.3 与既有工作的区别

| | VideoPhy-2 | PhyGenBench | PhyWorldBench | PhyGround | 本工作 |
|---|---|---|---|---|---|
| 边界 | 无定义 | 定律列表 | 定律列表 | 13 条教科书定律 | 认知科学定义的物理常识，显式排除专业知识 |
| 分支 | 力 | 力/光/热/化 | 力/光 | 力/流/光 | 力/热/光/电/声 |
| 违规轴 | 无 | 无 | 无 | 3 个通用维度 | 10 类，对应 L1–L3 |
| caption 数 | 600 | 160 | 350 | 250 | 1,190（力 315、热 250、光 277、电 252、声 96；训练 945 / 评测 245） |
| 视频数 | 3,397 test / 3,343 train | 1,280 | — | 2,000 | ≈2,835 train / ≈1,700–1,960 eval |
| 力学以外的样本占比 | ~10% | ~50%（含非常识） | ~22% | ~15% | 77% |
| 电学样本 | 0 | 0 | 7（非常识） | 0 | 300 |
| 标签粒度 | 整段 1–5 | 三阶段 0–3 | 通用 key_standards | 每律 1–5 + 一句理由 | 逐项 pass/fail/not_shown + 解释 + 严重度 |
| 预期是否可证伪 | 否 | 部分 | 部分 | 否（通用措辞） | 每项 expect/fail 对 |

## 4. 贡献二：rubric 驱动的构建流程

流程对训练集与评测集的每条 caption 同样执行，人类在三个节点介入。

### 4.1 caption 生成与校验

LLM 按格子生成候选 caption → 自动过滤（重复、含定律名词/数值、无动态事件、不在常识层清单内）→ 人工 review：矫正措辞、确认所属格子、剔除需要专业知识或结果不确定的条目（"结果不确定"是 PhyGenBench 审计里的一类典型问题，如针刺气球是否一定爆）。

**caption 写作原则（各分支 review 后补充）。**

- **人是噪声源，只在必要时出场。** T2V 模型对人物的渲染质量参差——多指、手部穿模、面部畸变——这类失败与被测的物理过程无关，却会进入 PC 分，干扰对物理一致性本身的判读，也让 SA 项多出一串与物理无关的"人物是否出现、动作是否正确"。因此 caption 只在两种情况下写人：(a) 人体本身是物理过程的参与方——手掌是融化冰块的热源、呼气是雾的水源、乘客的呼吸使车窗起雾；(b) 人是过程的必要施力者——扣动打火机、把黄油放进热锅。前者压缩到最小的身体部位（"a bare hand"、"breath"），不写身份与表情；后者优先用被动式或状态描述（"A pat of butter is dropped into a hot pan"、"An ice cream cone stands on a sunny table, already softening"），让触发动作只占片头，被评估的物理过程发生在人退出之后。纯旁观者、叙事道具（"a child leaves… and walks away"）一律删除。落地规则：**除力学的 biomechanics 这一个子类外，其余所有分支、所有子类一律尽量去人。** biomechanics 评的就是人和动物身体运动是否合理（步态、起跳与落地、屈膝坐下、失足摔倒），人是现象本身，这个子类整体保留人物，也由它保证 judge 的训练分布里仍有带人的视频。其他子类只允许上述 (a)(b) 两种例外，且例外要缩到最小——乘客随刹车前倾、脚踏冰面打滑写成 "a passenger"、"a foot"，不写身份、表情和多余动作；凡是能用物体代替人的（小孩跳上床 → 重物落到床上，两人走廊撞肩 → 两辆购物车相撞）一律换成物体。热、光、电、声四支的现象几乎都只涉及物体与环境，review 后应做到无人，只剩把身体当热源、水源或必要施力者的个别条目（呼气使镜面起雾、头发被气球吸起）。
- **过程要能在 5 秒内看见。** 生成视频约 5 秒，caption 描述的可见变化必须落在这个窗口内。分钟到小时级的过程（冰块化尽、蜡烛烧短、蜂蜜化开）不能写成一个完成的动作，而要写成进行中的状态（"the cubes are rounded and shrinking"）、前后对比的结果态（"when the hand opens, the chocolate has gone soft"），或换成同一现象的快速变体（黄油入热锅、雪落在热引擎盖上）。相应地，rubric 的 expect/fail 只要求变化的**方向与顺序**（更湿、更软、先底后顶、不可逆），不要求完成度或速率——这正是 process_direction 这一类的定义；否则一段物理上正确、变化幅度很小的 5 秒视频会被误判为违反。
- **caption 只说发生了什么，不说该长什么样。** "the chocolate slowly melts" 到此为止；边缘先软、表面发亮、滴液向下这些属于 expect/fail，是 judge 要去看的东西。把它们写进 caption 既是把答案喂给生成器，也会让 SA 项凭空膨胀。
- **结果必须能从画面判对错。** 每条 caption 至少要有一个 judge 能在帧里核对的定向变化：方向（向下、向外、顺风）、先后（先底后顶、先绷紧再拽停）、有无（灯亮前地面不亮、开关前风扇不转）。只能靠"没有出错"来判的条目——一杯茶冒着热气、一个人在走路、雾已经蒙在镜子上——不收：它们测的是生成模型的渲染质量，不是物理常识，而且几乎任何视频都能通过。纯结果态（"has softened"）是最弱的写法，因为屏幕上什么都没发生。
- **每个现象 3–5 个变体，不收近重复。** 同一现象换不同的物体和场景写 3–5 条（冰放在热锅上、冰扔进热茶、热水浇在冰块上），因为生成模型在不同场景下失败的方式不同，只写一条会把"这个现象"和"这个场景"混在一起；超过 5 条就是重复，只会拉低该分支分数的有效样本量。近重复的判定看被评估的物理事件而不是物体名：掀开电饭锅盖冒汽和掀开蒸笼冒汽是同一条，眼镜从冷处进咖啡馆起雾和进办公室起雾也是同一条。review 时按"物理事件"聚簇，每簇保留物体和场景差异最大的几条。
- **一个现象只归一个分支。** 分支边界上的事件按被评估的物理内容归属，不重复收："开关一按灯亮"是电学的因果链，光学 illumination 只评光出现之后往哪去（随距离衰减、光束跟着光源走、阴影背光），所以光学里"墙壁开关一按吊灯亮、房间变亮"这类条目全部删除；烟从烟囱升起、吹灭蜡烛冒烟归热学 burn_smoke，力学 gas_wind 不再写；冷冻食品下热锅嘶响归热学，不进力学 fluid。这样每条 caption 只贡献给一个分支分数，分支之间的比较才有意义。

### 4.2 rubric 撰写与分级

每条 caption 一份 rubric：

- **SA 项**：caption 要求的每个可见事实一项，core / minor 两级；多子动作时每个子动作一项，再加一项顺序。
- **PC 项**：每项一对可证伪陈述——`expect`（正确时应看到什么）/ `fail`（看到什么即算违反）；带 `precondition` 的项在前提未出现时判 `not_shown`，不影响分数。

PC 项分四级，级别对应 §1 的层次，因此不同场景下同一级别落到不同的具体现象上——这就是 rubric 必须 caption 级定制的原因：

| 级别 | 定义 | 对应层次 | 典型 fail 文本 |
|---|---|---|---|
| **fatal** | 场景作为整体不可能：穿透、凭空出现/消失/瞬移、分裂合并、刚体融化变形、重力方向错 | **L1 核心物体原则** | "A stem merges, multiplies or vanishes; or passes through the trellis's timber" |
| **core** | 这段视频**所讲的那个交互**没有发生，或该场景的中心机制被破坏 | **L2 的中心事件**（caption 描述的因果） | "The shears close right through and the stem is untouched; or a cut stem rejoins" |
| **major** | 一处清楚的违反，但不是中心交互：次级后果缺失或反了 | **L2 的伴随预期**：重力、惯性、材料响应 | "A cut piece hangs in the air; or it drifts down slowly; or it rises" |
| **minor** | 真实存在的瑕疵，但不改变事件如何展开 | **L3 属性经验**：颜色、纹理、位置的小漂移 | "A flower changes colour between frames; or a leaf disappears from an untouched stem" |

配套的 policy 规定评判纪律：PC 评的是**实际画面**的物理而非 caption 要求的内容（画了别的东西扣 SA 不扣 PC）；看不见的原因不算违规；成像质量、风格、技能与姿态、需要数值才能判定的东西不评；自驱动主体的自发启停不算违规。

分数由判定确定性推出：SA 按 core/minor 失败数落档；PC 取最严重失败项的上限（fatal→1、core→2、major→3、minor→4），再按额外重项递减，无失败为 5。每份 rubric 在写作时验证 1–5 每一档都可达。

rubric 起草由 LLM 以同分支、同机制的手写 rubric 为 few-shot 完成，经自动形式校验（id 顺序、档位可达性、无数值阈值、fail 文本不重复）后进入人工 review。现有 1,410 份手写 rubric 是 few-shot 库；PhyGenBench 的 160 条定律审计（110 可用 / 47 改写 / 3 排除）说明物理方向的人工核对不可省。

### 4.3 大 VLM 逐项判定与理由

对每条（caption, rubric, 视频），以 Qwen3-VL-235B-A22B 一类的强开源 VLM 作为教师，按 rubric 逐项给出 pass / fail / not_shown 与一句依据画面的解释；SA/PC 分由 §4.2 的函数从判定算出；再由教师将失败项按严重度综合为一段 **reason**（即诊断报告）。教师可用现有的双 agent 主动取证方式运行（overview / inspect_clip / inspect_region / compare_frames / presence_check 迭代取证，第二个 agent 审计证据链），以提高小区域、短时窗违规的召回。

人工 **review 与 verification**。rubric 的意义不是把人去掉，而是让人的判断变得便宜、一致、可审计：教师 VLM 是可规模化的执行者，它的可靠性必须在某处对人校准。评测集：全量人工核对（同意 / 推翻教师的每一项判定，见 §3 评测集标注），人工结果是评测集唯一的 ground truth，judge 在评测集上的所有指标都对人工标签计算。训练集：以教师判定为标签，人工抽样 5–10% 逐项核对，统计教师与人的一致率和推翻方向（教师偏宽还是偏严），作为标签噪声率写入论文；一致率明显偏低的分支或违规类型回到 rubric 撰写环节修正后重判。汇报时把评测集拆成"训练用过的 3 个生成模型"与"只在评测集出现的模型"两列，前者衡量 judge 对新场景的泛化，后者衡量对新生成器的泛化。

### 4.4 产出的数据格式

每个训练样本包含：caption、rubric、视频、教师逐项判定、`sa_score`、`pc_score`、`reason`。这份数据同时支撑 §5 的两种训练格式。

## 5. 贡献三：开源的可诊断 judge

基座为 Qwen3-VL-4B / 8B（Qwen3-VL 无 3B/7B 档；若用 Qwen2.5-VL 则为 3B/7B）。**输入只有 caption + 均匀采样的视频帧，不含 rubric**——rubric 只属于 §4 的构建阶段：它让 235B 教师的每个分数都能追溯到"哪一项、为什么 fail"，从而保证训练标签是有依据的；小 judge 学的是由此得到的分数与 reason，用起来与 AutoEval、PhyJudge 一样，任何 caption + 视频直接评。围绕输出格式与训练方式做两条路线的探究实验。

### 5.1 路线 A：LoRA SFT，直接输出分数与理由

目标格式 `{"sa_score": 2, "pc_score": 2,"reason": "..."}`（SA、PC 各一份或合并），reason 即教师依 rubric 综合出的诊断。训练目标是 JSON 的 token 级 NLL。这是与 PhyJudge-9B 最接近的设定，区别在于 reason 来自可证伪的逐项判定而非标注员的自由发挥。

### 5.2 路线 B：Cold-start SFT + GRPO，输出思维链

目标格式 `<think>…</think><answer>2</answer>`。think 由一个 Qwen 语言模型把教师的逐项判定与 reason 改写成第一人称的核对过程（"先看是否有物体消失……再看剪刀闭合处茎是否断开……"），cold-start SFT 后用 GRPO 对齐，奖励 = 答案与标签分数一致（精确命中满分、差 1 部分分）+ 格式合法。标签分数在训练集上来自教师（经人工抽检），因此奖励是可验证的。

两条路线得到两个 judge，在评测集与外部测试集上比较，并分析差异来源。

### 5.3 诊断驱动生成

judge 的 reason（或 think）中列出的失败项直接映射为对 prompt 的定向修正（"玻璃瓶应在轮胎压过后才破裂"），重新生成后再评。若修正后的视频在对应项上由 fail 转 pass、分数上升，则同时验证了诊断的有效性与评判-生成闭环。

## 6. 实验

1. **benchmark 统计**：五分支 × 十类违规上的样本分布；人工 review 对 LLM 生成 caption 与 rubric 的修改率；教师与人类的逐项一致率。
2. **judge 与人类的一致性**：SA/PC 分的 Pearson/Spearman/MAE；与 AutoEval、PhyJudge-9B、闭源 VLM 直接打分的比较；在四个外部 benchmark 常识子集上的迁移。
3. **前人 judge 的分支画像**：AutoEval、PhyJudge-9B 在力、热、光、电、声五个分支评测集上分别与人类的相关性，对照我们的 judge。预期前者在力学上尚可、在热/光/电上明显下降，从而同时说明前人 judge 不 comprehensive、以及训练数据按分支等量的必要性。
4. **路线 A vs 路线 B**：分数一致性、reason/think 与画面的贴合度（人工评 grounding）、对 1 分与 5 分两端的区分能力；分析 GRPO 是否带来超出 SFT 的增益，以及增益来自哪些分支或违规类型。
5. **跨分支泛化**：仅在力学上训练、在热/光/电/声上测试，量化小 judge 权重中的物理知识缺口；与全分支训练对照。
6. **诊断质量**：reason 中的失败项与人类逐项标注的召回/精度；按违规轴统计各生成模型的错法分布。
7. **闭环**：诊断驱动的 prompt 修正带来的 PC 提升，对照随机改写与通用"更真实"提示。
8. **消融**：严重度分级 vs 平权；定制 rubric vs PhyGround 式通用问题；教师是否使用主动取证。

## 7. 待定事项

- 电、声两个分支的可判样本量，需在 caption 生成后用文生视频模型试产一批再定格子的最小样本数；
- 视频的生成模型清单与预算（945 训练 caption × 3 模型，245 评测 caption × 7–8 模型）；
- （已解决 2026-09-15）电、声按"肉眼可判的常识"边界写满、去掉近重复后分别停在 252 与 96 条，接受五分支不等量；分支分数等权平均不受影响；
- 评测集人工标注：245 caption × 7–8 模型 ≈ 1,700–1,960 个视频的全量逐项标注是否可承受，或改为分层抽样；
- GRPO 的奖励是否加入 reason 与人类失败项的匹配项（需要训练集也有人类逐项标注，成本高）。
