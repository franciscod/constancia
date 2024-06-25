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
    d = {}
    for k, v in datos.__dict__.items():
        if k != k.upper():
            continue

        if k.startswith("MM"):
            v = MESES[int(v) - 1]

        d[k] = v
    return d


lines = []
with open("template.xopp") as f:
    lines = f.readlines()

remove_everything_else = False
dkv = get_datos_kv()
for i, line in enumerate(lines):
    remove = False
    if dkv.get("SOLO_PRIMERA_MITAD") and "-- hr --" in line:
        remove_everything_else = True

    if not (line.startswith("<text") or ("-- final --" in line) or ("-- parcial --" in line)):
        continue

    if ("-- final --" in line) and dkv.get("ES_PARCIAL"):
        remove = True

    if ("-- parcial --" in line) and dkv.get("ES_FINAL"):
        remove = True

    if remove_everything_else:
        remove = True

    if remove:
        line = ""

    for k, v in dkv.items():
        line = line.replace("K_" + k, f"{v}")


    lines[i] = line

with open(TMPXOPP, "w") as f:
    f.writelines(lines)

print(f"generando {OUTFILE}", file=sys.stderr)
os.system(f"xournalpp {TMPXOPP} -p {OUTFILE}")
os.system(f"rm {TMPXOPP}")
