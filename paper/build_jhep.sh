#!/usr/bin/env bash
# Build the JHEP-class PDF (jheppub) for Paper VI from mu_transmutation_glueball.md.
#   makedoc (title/abstract/keywords -> YAML, fold figures, number sections)
#   -> pandoc --natbib (emits \citep) with template_jhep.tex -> xelatex + bibtex.
set -e
cd "$(dirname "$0")"
mkdir -p tex
BASE=mu_transmutation_glueball

python3 tools/makedoc.py $BASE.md .build.md
trap 'rm -f .build.md' EXIT
# (a) drop the citeproc "## References / ::: {#refs}" placeholder if present — natbib handles refs
# (b) protect native inline $...$ math as raw-LaTeX spans `\(...\)`{=latex}: pandoc otherwise
#     refuses to parse $x$N when the closing $ is followed by a digit (its "$5" heuristic),
#     which this paper's notation ($\sim$30, $3\to2$, …) hits constantly.
python3 - <<'PY'
import re
t=open('.build.md',encoding='utf-8').read()
t=re.sub(r'\n##\s+References\s*\n+:::\s*\{#refs\}\s*\n:::\s*\n','\n',t)
t=re.sub(r'(?<!\\)(?<!\$)\$(?!\$)((?:\\.|[^$\\\n]|\\\n)+?)\$(?!\$)',
         lambda m: '`\\('+m.group(1)+'\\)`{=latex}', t)
open('.build.md','w',encoding='utf-8').write(t)
PY

pandoc -f markdown-superscript-subscript .build.md -o tex/$BASE.tex \
  --standalone --shift-heading-level-by=-1 --natbib \
  --template=tools/template_jhep.tex

# numeric journal (JHEP): no author-prominent form — normalise \citet -> \citep
perl -0pi -e 's#\\citet\{#\\citep{#g' tex/$BASE.tex
# number display equations: pandoc emits \[ ... \]; convert to a numbered equation environment
perl -0pi -e 's/\\\[/\\begin{equation}/g; s/\\\]/\\end{equation}/g' tex/$BASE.tex

( cd tex && \
  xelatex -interaction=nonstopmode $BASE.tex >$BASE.build.log 2>&1 ; \
  BIBINPUTS="..:$BIBINPUTS" bibtex $BASE      >>$BASE.build.log 2>&1 ; \
  xelatex -interaction=nonstopmode $BASE.tex >>$BASE.build.log 2>&1 ; \
  xelatex -interaction=nonstopmode $BASE.tex >>$BASE.build.log 2>&1 ) || true

if [ -f tex/$BASE.pdf ]; then
  cp tex/$BASE.pdf $BASE.pdf
  echo "built paper/$BASE.pdf"
  grep -c "^!" tex/$BASE.build.log | awk '{print $1" LaTeX errors (see tex/'$BASE'.build.log)"}'
  grep -c "Warning--" tex/$BASE.build.log 2>/dev/null | awk '{print $1" bibtex warnings"}'
  grep -c "Citation.*undefined" tex/$BASE.build.log 2>/dev/null | awk '{print $1" undefined citations"}'
else
  echo "BUILD FAILED — see tex/$BASE.build.log"; grep -A2 '^!' tex/$BASE.build.log | head -20
fi
