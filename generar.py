import os
import sys

import datos

TMPXOPP = "constancia.xopp"
OUTFILE = "constancia.pdf"

MESES = [
    "enero",
    "febrero",
    "marzo",
    "abril",
    "mayo",
    "junio",
    "julio",
    "agosto",
    "septiembre",
    "octubre",
    "noviembre",
    "diciembre",
]


def get_datos_kv():
    for k, v in datos.__dict__.items():
        if k != k.upper():
            continue

        if k.startswith("MM"):
            v = MESES[int(v) - 1]

        yield k, v


lines = []
with open("template.xopp") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if not line.startswith("<text"):
        continue

    for k, v in get_datos_kv():
        line = line.replace("K_" + k, f"{v}")

    lines[i] = line

with open(TMPXOPP, "w") as f:
    f.writelines(lines)

print(f"generando {OUTFILE}", file=sys.stderr)
os.system(f"xournalpp {TMPXOPP} -p {OUTFILE}")
os.system(f"rm {TMPXOPP}")
