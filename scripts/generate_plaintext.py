from __future__ import annotations

from pathlib import Path
import re

CHAPTER_DIRS = [Path('source/chapters'), Path('source/interpretive')]

command_replacements = [
    (re.compile(r"\\section\*\{([^}]*)\}"), lambda m: f"{m.group(1)}\n"),
    (re.compile(r"\\subsection\*\{([^}]*)\}"), lambda m: f"{m.group(1)}\n"),
    (re.compile(r"\\textbf\{([^}]*)\}"), lambda m: m.group(1)),
    (re.compile(r"\\texttt\{([^}]*)\}"), lambda m: m.group(1)),
]

simple_replacements = {
    '\\begin{itemize}': '\n',
    '\\end{itemize}': '\n',
    '\\item': '\n-',
    '\\narrative{': '',
    '\\normative{': '',
    '\\clearpage': '\n',
}

comment_line = re.compile(r"^%.*$", re.MULTILINE)
extra_command = re.compile(r"\\[a-zA-Z]+\*?")
whitespace_cleanup = re.compile(r"\n{3,}")
brace_cleanup = re.compile(r"[{}]")


def natural_key(path: Path) -> list[object]:
    stem = path.stem
    match = re.match(r"chapter-([0-9a-zA-Z]+)", stem)
    token = match.group(1).upper() if match else stem
    parts = re.findall(r"\d+|\D+", token)
    key: list[object] = []
    for part in parts:
        if part.isdigit():
            key.append(int(part))
        else:
            key.append(part)
    return key


texts: list[str] = []
for directory in CHAPTER_DIRS:
    for path in sorted(directory.glob('chapter-*.tex'), key=natural_key):
        text = path.read_text()
        text = comment_line.sub('', text)
        for pattern, repl in command_replacements:
            text = pattern.sub(repl, text)
        for needle, replacement in simple_replacements.items():
            text = text.replace(needle, replacement)
        text = brace_cleanup.sub('', text)
        text = extra_command.sub('', text)
        text = re.sub(r"\s+\n", '\n', text)
        text = whitespace_cleanup.sub('\n\n', text)
        text = text.strip()
        texts.append(text)

output = '\n\n'.join(texts) + '\n'
Path('audits/ai-osi-stack-v5-plaintext.txt').write_text(output)
