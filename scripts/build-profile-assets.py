"""Build original, self-contained SVG artwork for the bilingual profile."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
PAPER, INK, RUST, MUTED, LINE = '#f6f1e8', '#332b27', '#b75d40', '#77665a', '#d9cbb9'

def text(x, y, value, size=18, fill=INK, family='sans', extra=''):
    fonts = {'sans': 'Segoe UI,Microsoft YaHei,Arial,sans-serif', 'serif': 'Georgia,Times New Roman,serif', 'mono': 'Consolas,monospace'}
    return f'<text x="{x}" y="{y}" fill="{fill}" font-family="{fonts[family]}" font-size="{size}" {extra}>{escape(value)}</text>'

def svg(name, w, h, content, title):
    (ROOT/'assets'/name).write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title">
<title id="title">{escape(title)}</title>
<rect width="{w}" height="{h}" rx="8" fill="{PAPER}"/>
{content}
</svg>\n''', encoding='utf-8')

# The citrus is an original mark derived from the account name, not a logo from a reference.
orange = '''<g stroke="#b75d40" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
<path d="M743 148 C697 115 621 146 608 217 C590 311 651 354 719 346 C789 343 826 285 811 218 C801 169 771 149 743 148Z" fill="#e4a17e"/>
<path d="M719 156 C724 130 741 117 753 112" fill="none"/>
<path d="M729 135 C723 100 678 91 660 102 C680 130 704 143 729 135Z" fill="#d9c9ad" stroke="#857057"/>
<path d="M672 108 Q708 114 729 135" fill="none" stroke="#857057"/>
<path d="M631 192 Q614 231 626 265 M637 283 l3 7 M775 191 l4 6 M784 207 l3 7" fill="none" opacity=".65"/>
<path d="M697 163 q16 -11 28 -3" fill="none"/>
</g>'''
# A cut citrus segment doubles as a radial map of evidence.
slice_art = '''<g transform="translate(804 315) rotate(-18)">
<path d="M-83 0 A83 83 0 0 0 83 0Z" fill="#b75d40"/>
<path d="M-74 4 A74 70 0 0 0 74 4Z" fill="#f6e4ca"/>
<g fill="#d88761" stroke="#f6e4ca" stroke-width="4">
<path d="M-65 10 L-12 10 L-49 48 Q-64 30 -65 10Z"/>
<path d="M-4 14 L-43 54 Q-24 69 -5 69Z"/>
<path d="M5 14 L5 69 Q28 68 45 53Z"/>
<path d="M14 10 L65 10 Q64 32 51 47Z"/>
</g></g>'''
for lang in ('zh','en'):
    zh = lang == 'zh'
    b = text(42,48,'JUZIKUWEI  /  PERSONAL WORKSHOP',15,MUTED,'mono',extra='letter-spacing="1.5"')
    b += text(958,48,'中文 / EN' if zh else 'EN / 中文',14,MUTED,'mono',extra='text-anchor="end"')
    b += f'<path d="M42 69H958" stroke="{LINE}"/>'
    b += text(40,154,'A little curiosity.',48,INK,'serif')
    b += text(40,215,'A working idea.',48,RUST,'serif',extra='font-style="italic"')
    b += text(43,265,'把好奇心，做成可以运行的东西。' if zh else 'Turning curiosity into things that work.',22)
    b += text(43,306,'我是 juzikuwei，和 AI 一起构建应用。' if zh else 'I’m juzikuwei. I build applications with AI.',17,MUTED)
    b += text(43,334,'关注检索、Agent，以及答案背后的证据。' if zh else 'Retrieval, agents, and the evidence behind answers.',17,MUTED)
    b += orange + slice_art
    b += '<g fill="none" stroke="#857057" stroke-width="1.4"><path d="M789 127 Q851 104 864 142"/><path d="m858 135 6 9 4-12"/><path d="M596 281 Q564 299 577 351"/><path d="m570 342 7 11 5-12"/></g>'
    b += text(809,93,'stay curious',18,MUTED,'serif',extra='font-style="italic" transform="rotate(7 809 93)"')
    b += text(590,392,'ideas need roots.',20,MUTED,'serif',extra='font-style="italic" transform="rotate(-4 590 392)"')
    b += '<g transform="translate(864 207) rotate(8)"><rect width="91" height="66" fill="#ede2cf"/><path d="M14 19H74M14 31H60M14 43H68" stroke="#bda98e"/><path d="m62 44 6 6 12-17" stroke="#b75d40" stroke-width="2" fill="none"/></g>'
    b += f'<path d="M42 427H958" stroke="{LINE}"/>'
    b += text(43,464,'AI WRITES. I QUESTION, SHAPE & VERIFY.',15,INK,'mono')
    b += text(958,464,'RAG · AGENTS · EVALS',14,MUTED,'mono',extra='text-anchor="end"')
    svg(f'profile-header{"" if zh else "-en"}.svg',1000,494,b,'橘子的 AI 工作台：把好奇心做成可以运行的东西' if zh else 'Juzikuwei’s AI workshop: turning curiosity into things that work')

    for project in ('radar','focus'):
        radar = project == 'radar'
        b = text(34,41,'RESEARCH TOOL' if radar else 'PRODUCT EXPLORATION',13,RUST,'mono',extra='letter-spacing="2"')
        b += text(33,93,'Tech Radar' if radar else 'Focus Lab',43,INK,'serif')
        desc = ('让回答，带着证据回来。' if radar else '让一个想法，遇见不同的声音。') if zh else ('Answers that bring their sources.' if radar else 'One idea. Different perspectives.')
        b += text(35,133,desc,21)
        info = ('混合检索 / 有界工具调用 / 引用校验' if radar else '虚拟受访者 / 多轮访谈 / 洞察报告') if zh else ('Hybrid retrieval / bounded agents / citations' if radar else 'Virtual participants / interviews / insights')
        b += text(35,167,info,16,MUTED)
        b += text(35,226,'PYTHON · FASTAPI · REACT · MCP' if radar else 'JAVASCRIPT · FASTAPI · LANGCHAIN',13,MUTED,'mono')
        b += f'<path d="M574 35V229" stroke="{LINE}"/>'
        if radar:
            b += '<g stroke="#b75d40" fill="none"><circle cx="747" cy="128" r="79" opacity=".25"/><circle cx="747" cy="128" r="53" opacity=".4"/><circle cx="747" cy="128" r="25" opacity=".6"/><path d="M747 49V207M668 128H826" opacity=".25"/><path d="M747 128 801 71 A79 79 0 0 1 826 128Z" fill="#e9c9b5" stroke="none"/><path d="m747 128 54-57" stroke-width="2"/></g>'
            b += '<g fill="#b75d40"><circle cx="779" cy="99" r="5"/><circle cx="710" cy="150" r="4"/><circle cx="760" cy="182" r="4"/></g><path d="M779 99H840V72" fill="none" stroke="#b75d40"/>'
            b += text(843,65,'[source]',13,RUST,'mono')
            b += text(842,182,'evidence',16,MUTED,'serif',extra='font-style="italic"')
            b += text(842,202,'over guesswork.',16,MUTED,'serif',extra='font-style="italic"')
        else:
            b += '<g stroke="#b75d40" stroke-width="1.5"><path d="M696 91 766 141 849 91M766 141V195" fill="none"/><rect x="628" y="55" width="121" height="56" rx="17" fill="#eee0cd"/><rect x="791" y="55" width="121" height="56" rx="17" fill="#e9c1aa"/><rect x="705" y="148" width="121" height="56" rx="17" fill="#f9f5ed"/></g>'
            b += text(688,90,'what if?',21,INK,'serif',extra='text-anchor="middle" font-style="italic"')
            b += text(851,90,'why not?',21,INK,'serif',extra='text-anchor="middle" font-style="italic"')
            b += text(765,184,'tell me more.',18,INK,'serif',extra='text-anchor="middle" font-style="italic"')
        svg(f'project-{project}-{lang}.svg',1000,260,b,('Tech Radar' if radar else 'Focus Lab')+' — '+desc)

    b = text(36,44,'THE HUMAN IN THE LOOP',13,RUST,'mono',extra='letter-spacing="2"')
    b += text(35,94,'AI writes. I verify.',39,INK,'serif',extra='font-style="italic"')
    labels = [('定义问题','目标、范围与边界'),('设计工作流','数据、工具与失败路径'),('验证结果','测试、评测与 Trace')] if zh else [('Define','Goals, scope, boundaries'),('Design','Data, tools, failure paths'),('Verify','Tests, evaluations, traces')]
    for i,(label,caption) in enumerate(labels):
        x=38+i*326
        b+=text(x,153,f'0{i+1}',14,RUST,'mono')+text(x+40,154,label,22)+text(x,190,caption,17,MUTED)
        if i<2: b+=f'<path d="M{x+245} 147h38m-7-5 7 5-7 5" stroke="{RUST}" fill="none"/>'
    svg(f'build-process-{lang}.svg',1000,224,b,'AI 编写，我定义、设计并验证' if zh else 'AI writes; I define, design, and verify')
