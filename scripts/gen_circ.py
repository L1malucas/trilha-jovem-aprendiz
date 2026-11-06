#!/usr/bin/env python3
"""Gera arquivos .circ (formato Logisim 2.7.2, usado pelo logisim.app) do módulo 04.

Saídas:
  static/logisim/04/starters/*.circ  esqueletos (pins nomeados + instruções) para os alunos
  static/logisim/04/examples/*.circ  demos da teoria (circuitos prontos)
  gabaritos/04/*.circ                modelos de referência (NÃO publicados no site)

Geometria assumida (portas de 2 entradas, atributo size=30): saída em (x,y),
entradas em (x-30, y-10) e (x-30, y+10). Pin de entrada: conexão em loc (desenhado à
esquerda). Pin de saída (facing west): conexão em loc (desenhado à direita).
"""
from pathlib import Path
from xml.sax.saxutils import quoteattr

ROOT = Path(__file__).resolve().parent.parent

HEADER = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<project source="2.7.2" version="1.0">
This file is intended to be loaded by Logisim (http://www.cburch.com/logisim/).
<lib desc="#Wiring" name="0"/>
<lib desc="#Gates" name="1"/>
<lib desc="#Plexers" name="2"/>
<lib desc="#Arithmetic" name="3"/>
<lib desc="#Memory" name="4"/>
<lib desc="#I/O" name="5"/>
<lib desc="#Base" name="6"/>
<main name="main"/>
<options>
  <a name="gateUndefined" val="ignore"/>
  <a name="simlimit" val="1000"/>
  <a name="simrand" val="0"/>
</options>
"""


class Circuit:
    def __init__(self):
        self.items = []

    def pin(self, x, y, label, output=False, width=1):
        a = f'    <a name="label" val={quoteattr(label)}/>\n'
        if output:
            a += '    <a name="facing" val="west"/>\n    <a name="output" val="true"/>\n'
        if width > 1:
            a += f'    <a name="width" val="{width}"/>\n'
        self.items.append(f'  <comp lib="0" loc="({x},{y})" name="Pin">\n{a}  </comp>')

    def gate(self, kind, x, y):
        names = {"AND": "AND Gate", "OR": "OR Gate", "XOR": "XOR Gate",
                 "NAND": "NAND Gate", "NOR": "NOR Gate", "XNOR": "XNOR Gate"}
        self.items.append(
            f'  <comp lib="1" loc="({x},{y})" name="{names[kind]}">\n'
            f'    <a name="size" val="30"/>\n  </comp>')

    def wire(self, x1, y1, x2, y2):
        if (x1, y1) != (x2, y2):
            self.items.append(f'  <wire from="({x1},{y1})" to="({x2},{y2})"/>')

    def net(self, src, trunk_x, taps):
        """Fio da fonte `src` até cada tap, com tronco vertical em trunk_x."""
        sx, sy = src
        ys = sorted({sy, *[t[1] for t in taps]})
        self.wire(sx, sy, trunk_x, sy)
        for a, b in zip(ys, ys[1:]):
            self.wire(trunk_x, a, trunk_x, b)
        for tx, ty in taps:
            self.wire(trunk_x, ty, tx, ty)

    def text(self, x, y, txt):
        self.items.append(
            f'  <comp lib="6" loc="({x},{y})" name="Text">\n'
            f'    <a name="text" val={quoteattr(txt)}/>\n  </comp>')

    def render(self):
        body = '<circuit name="main">\n  <a name="circuit" val="main"/>\n' + "\n".join(self.items) + "\n</circuit>\n"
        return HEADER + body + "</project>\n"


def save(path, circ):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(circ.render(), encoding="utf-8")


# ---------- circuitos prontos ----------

def portas_basicas():
    c = Circuit()
    c.text(200, 20, "Portas basicas: clique nos pins de entrada (A e B) com a Poke Tool")
    for i, kind in enumerate(["AND", "OR", "XOR", "NAND", "NOR", "XNOR"]):
        y = 80 + i * 60
        c.pin(60, y - 10, f"A_{kind}")
        c.pin(60, y + 10, f"B_{kind}")
        c.gate(kind, 150, y)
        c.wire(60, y - 10, 120, y - 10)
        c.wire(60, y + 10, 120, y + 10)
        c.wire(150, y, 220, y)
        c.pin(220, y, kind, output=True)
    return c


def meio_somador():
    c = Circuit()
    c.text(180, 20, "Meio somador: SOMA = A XOR B, CARRY = A AND B")
    c.pin(30, 50, "A")
    c.pin(30, 70, "B")
    c.gate("XOR", 150, 60)   # entradas (120,50) (120,70)
    c.gate("AND", 150, 140)  # entradas (120,130) (120,150)
    c.net((30, 50), 50, [(120, 50), (120, 130)])
    c.net((30, 70), 60, [(120, 70), (120, 150)])
    c.wire(150, 60, 220, 60)
    c.pin(220, 60, "SOMA", output=True)
    c.wire(150, 140, 220, 140)
    c.pin(220, 140, "CARRY", output=True)
    return c


def somador_completo():
    c = Circuit()
    c.text(260, 20, "Somador completo: SOMA = A^B^CIN, COUT = A.B + (A^B).CIN")
    c.pin(30, 50, "A")
    c.pin(30, 70, "B")
    c.pin(30, 90, "CIN")
    c.gate("XOR", 200, 60)   # in (170,50) (170,70)
    c.gate("AND", 200, 140)  # in (170,130) (170,150)
    c.gate("XOR", 330, 80)   # in (300,70) (300,90)
    c.gate("AND", 330, 160)  # in (300,150) (300,170)
    c.gate("OR", 450, 150)   # in (420,140) (420,160)
    c.net((30, 50), 50, [(170, 50), (170, 130)])
    c.net((30, 70), 60, [(170, 70), (170, 150)])
    c.net((30, 90), 70, [(300, 90), (300, 170)])
    c.net((200, 60), 250, [(300, 70), (300, 150)])
    c.wire(200, 140, 420, 140)
    c.wire(330, 160, 420, 160)
    c.wire(330, 80, 500, 80)
    c.pin(500, 80, "SOMA", output=True)
    c.wire(450, 150, 520, 150)
    c.pin(520, 150, "COUT", output=True)
    return c


# ---------- esqueletos (apenas pins nomeados + instrução) ----------

def starter(instrucao, entradas, saidas):
    """entradas/saidas: lista de (nome, largura)."""
    c = Circuit()
    c.text(220, 20, instrucao)
    for i, (n, w) in enumerate(entradas):
        c.pin(60, 70 + i * 40, n, width=w)
    for i, (n, w) in enumerate(saidas):
        c.pin(360, 70 + i * 40, n, output=True, width=w)
    return c


def bits(prefixo, n):
    return [(f"{prefixo}{i}", 1) for i in range(n - 1, -1, -1)]


STARTERS = {
    "ex01_tabelas": ("Ex 1: monte AND, OR, XOR e NOT ligando A e B as saidas", [("A", 1), ("B", 1)], [("AND", 1), ("OR", 1), ("XOR", 1), ("NOT_A", 1)]),
    "ex02_a_and_b_or_c": ("Ex 2: F = A AND (B OR C)", [("A", 1), ("B", 1), ("C", 1)], [("F", 1)]),
    "ex03_xor_sem_xor": ("Ex 3: monte XOR so com AND/OR/NOT e compare com a porta XOR nativa", [("A", 1), ("B", 1)], [("XOR_NATIVO", 1), ("XOR_MONTADO", 1)]),
    "ex05_meio_somador": ("Ex 5: meio somador (A, B -> SOMA, CARRY)", [("A", 1), ("B", 1)], [("SOMA", 1), ("CARRY", 1)]),
    "ex06_flipflop_d": ("Ex 6: flip-flop D (use o componente D Flip-Flop e observe Q so mudar na borda do clock)", [("D", 1), ("CLK", 1)], [("Q", 1)]),
    "ex07_trava_senha": ("Ex 7: trava com senha 8-1-5-3. DIGITO (4 bits) a cada pulso de CLK; ABRE=1 so se a sequencia estiver certa", [("DIGITO", 4), ("CLK", 1), ("RESET", 1)], [("ABRE", 1)]),
    "lab37_portas": ("Lab 37: De Morgan - monte NOT(A AND B) e a forma simplificada (so OR e NOT); as saidas devem ser iguais", [("A", 1), ("B", 1)], [("ORIGINAL", 1), ("SIMPLIFICADA", 1)]),
    "lab38_tabelas_verdade": ("Lab 38: F = (A XOR B) OR (A AND C); confira com Window > Combinational Analysis", [("A", 1), ("B", 1), ("C", 1)], [("F", 1)]),
    "lab39_multiplexador": ("Lab 39: MUX 2x1 com portas: Y = (NOT S AND D0) OR (S AND D1)", [("D0", 1), ("D1", 1), ("S", 1)], [("Y", 1)]),
    "lab40_meio_somador": ("Lab 40: meio somador", [("A", 1), ("B", 1)], [("SOMA", 1), ("CARRY", 1)]),
    "lab41_somador_completo": ("Lab 41: somador completo (A, B, CIN -> SOMA, COUT)", [("A", 1), ("B", 1), ("CIN", 1)], [("SOMA", 1), ("COUT", 1)]),
    "lab41_somador_4bits": ("Lab 41: somador de 4 bits encadeando 4 somadores completos", bits("A", 4) + bits("B", 4) + [("CIN", 1)], bits("S", 4) + [("COUT", 1)]),
    "lab42_registrador": ("Lab 42: registrador de 4 bits com LOAD (carrega D na borda do clock quando LOAD=1)", bits("D", 4) + [("LOAD", 1), ("CLK", 1)], bits("Q", 4)),
    "lab43_contador": ("Lab 43: contador binario de 3 bits (000 a 111) com RESET", [("CLK", 1), ("RESET", 1)], bits("Q", 3)),
    "lab44_maquina_estados": ("Lab 44: maquina de estados (defina estados, transicoes e a saida Z)", [("X", 1), ("CLK", 1), ("RESET", 1)], [("Z", 1)]),
}


def main():
    static = ROOT / "static" / "logisim" / "04"
    for nome, (instr, ins, outs) in STARTERS.items():
        save(static / "starters" / f"{nome}.circ", starter(instr, ins, outs))
    save(static / "examples" / "portas_basicas.circ", portas_basicas())
    save(static / "examples" / "meio_somador.circ", meio_somador())
    save(static / "examples" / "somador_completo.circ", somador_completo())
    # gabaritos (fora de static/, nao publicados)
    save(ROOT / "gabaritos" / "04" / "ex05_meio_somador.circ", meio_somador())
    save(ROOT / "gabaritos" / "04" / "lab41_somador_completo.circ", somador_completo())
    print("circ gerados")


if __name__ == "__main__":
    main()
