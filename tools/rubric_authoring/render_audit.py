"""Render audit/phygenbench/AUDIT.md from _audit.json."""
import json, os, collections

ROOT = '/home/jovyan/chy/physical_judge'
A = json.load(open(os.path.join(ROOT, 'audit', 'phygenbench', '_audit.json')))
OUT = os.path.join(ROOT, 'audit', 'phygenbench', 'AUDIT.md')
MARK = {'ok': '可直接用', 'rewrite': '需改写', 'exclude': '建议排除'}
L = []
w = L.append

def groups():
    """Consecutive records sharing one law_corrected form one analysis group."""
    out, cur = [], []
    for r in A:
        if cur and r['law_corrected'] == cur[-1]['law_corrected']:
            cur.append(r)
        else:
            if cur: out.append(cur)
            cur = [r]
    out.append(cur)
    return out

G = groups()
cnt = collections.Counter(r['verdict'] for r in A)
flags = collections.Counter(f for r in A for f in r.get('flags', ()))
bad = [r for r in A if r['verdict'] != 'ok']

w('# PhyGenBench `physical_laws` 逐条体检')
w('')
w('## 摘要')
w('')
w(f"160 条 prompt 全部过了一遍，判据只有一条：**照抄这条 law 写出来的 rubric，会不会误判一个"
  f"物理正确的片段，或者放过一个物理错误的片段。**只要会，就归入需改写——哪怕 law 的结论本身"
  f"是对的。")
w('')
w(f"结果：**可直接用 {cnt['ok']}**、**需改写 {cnt['rewrite']}**、**建议排除 {cnt['exclude']}**"
  f"（共 {len(A)}）。每条都给了改正后的 law 和展开的可见观察量，观察量总数 "
  f"{sum(len(r['observables']) for r in A)} 条。")
w('')
w('几条要单独说的：')
w('')
w('- **id 109（油沸腾）是全库最严重的一条。**law 写「温度到 100°C 油会沸腾、大量气泡涌上'
  '表面」——油的沸点在 300°C 以上，100°C 的油只是热。也就是说，一个把油拍成 100°C 剧烈'
  '沸腾的片段，会被这条 law 判为**正确**。错的方向朝着奖励幻觉走。而且末句写的是 "the '
  'coffee surface"，是从别的 caption 复制粘贴留下的。')
w('- **id 147（苏打水）方向性错误。**苏打水是碳酸水，pH 3–4，蓝色石蕊会变红；law 写「溶液'
  '保持蓝色」。照抄的结果是：**什么都不发生的片段得满分**，而这恰好是视频模型最容易生成的东西。')
w('- **id 101（暖车窗）caption 和 law 直接矛盾。**caption 说冷环境里的暖车窗，law 说'
  '「窗温远低于雾温」。两者不能同真，且按 caption 的物理，雾碰到暖玻璃是蒸发而不是凝结。'
  '这个没法只改 law 修好，所以建议排除。')
w('- **id 110–114（凝华）五条把动词写反了**：气→固是 deposition，sublimation 是反过来。'
  '结论没错，但 law 里完全没提真正有用的那条判据——直接长冰晶、没有液滴阶段，'
  '而这是它和 100–104（液化）唯一的区分点。')
w('- **id 148（紫甘蓝汁）说会放气体**，实际不放。照抄会奖励一个凭空加气泡的片段。')
w('- **id 123（青+洋红）**减色混合得到的是**蓝**，不是 law 写的 purple。')
w('- **id 77（玻璃弹珠）、78（雾滴）建议排除**：干涉/衍射在这两个体系里根本不发生，'
  '实心玻璃球给的是 caustics，雾滴给的是白色 Mie 散射。law 要求「珠子/雾会很多彩」，'
  '照抄就是要求模型生成一个不存在的现象。')
w('- **id 116、118 的证据是气味**，视频判不了；换成「固体变小 + 无液相 + 冷面复凝」，'
  '也就是 117 已经写对的那套。')
w('- **id 55–59（水面倒影）和 65–69（放大镜）结论对但会误判正确片段**：前者「与原物同'
  '大小」只对虚像成立、屏幕上倒影只会等大或更小；后者只写了终态放大，而一个从远处'
  '推近的正确片段会先出现**倒立缩小**的实像。')
w('')
w(f"打的标记：" + '、'.join(f'`{k}`×{v}' for k, v in flags.most_common()) + '。')
w('')
w('机器可读版在 `_audit.json`，字段：`verdict` / `law_original` / `law_corrected` / '
  '`observables` / `issue` / `flags`。下面是逐条内容。')
w('')

w('## 需改写与建议排除清单')
w('')
w('| id | main | sub | verdict | flags | 问题一句话 |')
w('|---|---|---|---|---|---|')
def gist(r, lim=170):
    t = ' '.join((r.get('issue') or '').split())
    if len(t) <= lim: return t
    cut = t.rfind('. ', 60, lim)
    return (t[:cut + 1] if cut > 0 else t[:lim - 3].rstrip() + '...')

for r in bad:
    one = gist(r)
    w(f"| {r['id']} | {r['main_category']} | {r['sub_category']} | **{MARK[r['verdict']]}** | "
      f"{' '.join('`%s`' % f for f in r.get('flags', ())) or '--'} | {one} |")
w('')

caveat = [r for r in A if r['verdict'] == 'ok' and r.get('issue')]
if caveat:
    w('## 可直接用但有保留')
    w('')
    w('结论正确、照抄也不会误判，但有'
      '一句得删掉或者有个前提得注意。')
    w('')
    w('| id | sub | flags | 保留 |')
    w('|---|---|---|---|')
    for r in caveat:
        w(f"| {r['id']} | {r['sub_category']} | "
          f"{' '.join('`%s`' % f for f in r.get('flags', ())) or '--'} | {gist(r)} |")
    w('')

w('## 逐条')
w('')
last_main = None
for grp in G:
    r0 = grp[0]
    if r0['main_category'] != last_main:
        last_main = r0['main_category']
        w(f'### {last_main}')
        w('')
    ids = [r['id'] for r in grp]
    tag = f"id {ids[0]}" if len(ids) == 1 else 'id ' + ', '.join(map(str, ids))
    fl = sorted({f for r in grp for f in r.get('flags', ())})
    w(f"#### {tag} — {r0['sub_category']} — **{MARK[r0['verdict']]}**"
      + (f"  ({', '.join('`%s`' % f for f in fl)})" if fl else ''))
    w('')
    for r in grp:
        w(f"- `{r['id']}` {r['caption']}")
    w('')
    laws = []
    for r in grp:
        if r['law_original'] not in laws: laws.append(r['law_original'])
    w('**Law as given.**' + ('' if len(laws) == 1 else ' (templated across the group)'))
    w('')
    for t in laws:
        w(f'> {t}')
        w('')
    w(f"**Corrected.** {r0['law_corrected']}")
    w('')
    shared = [o for o in grp[0]['observables'] if all(o in r['observables'] for r in grp)]
    w('**Observables.**')
    w('')
    for o in shared:
        w(f'- {o}')
    w('')
    for r in grp:
        extra = [o for o in r['observables'] if o not in shared]
        if extra:
            w(f"**Additionally for {r['id']}.**")
            w('')
            for o in extra:
                w(f'- {o}')
            w('')
    seen = []
    for r in grp:
        if r.get('issue') and r['issue'] not in seen:
            seen.append(r['issue'])
            who = '' if len(grp) == 1 or len(seen) == 1 and all(
                x.get('issue') == r['issue'] for x in grp) else f" (id {r['id']})"
            w(f"**Why it needs changing{who}.** {r['issue']}")
            w('')

open(OUT, 'w').write('\n'.join(L) + '\n')
print(f'{OUT}  {len(G)} groups, {len(L)} lines')
