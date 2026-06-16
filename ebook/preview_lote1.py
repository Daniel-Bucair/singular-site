# -*- coding: utf-8 -*-
"""
preview_lote1.py — Gera PDF de previa do Lote 1 para revisao.
Uso: python ebook/preview_lote1.py
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout.reconfigure(encoding="utf-8")

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from ebook.questions.lote1 import QUESTOES as QUESTOES_L1
from ebook.questions.lote2 import QUESTOES as QUESTOES_L2
from ebook.questions.lote3 import QUESTOES as QUESTOES_L3

QUESTOES = QUESTOES_L1 + QUESTOES_L2 + QUESTOES_L3
LOTES_INFO = "Lotes 1, 2 e 3 (120 questões)"
SUBTITULO = "Porcentagem · Razão/Proporção · Funções · Geometria Plana"

OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output", "previa_lotes1a3.pdf")
os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)

# ── Estilos ────────────────────────────────────────────────────────────────

AZUL       = colors.HexColor("#3B5BDB")
CINZA_CLARO = colors.HexColor("#F1F3F5")
CINZA_TEXTO = colors.HexColor("#495057")
PRETO      = colors.HexColor("#212529")
VERDE      = colors.HexColor("#2F9E44")

def estilos():
    base = getSampleStyleSheet()

    capa_titulo = ParagraphStyle(
        "CapaTitulo",
        fontName="Helvetica-Bold",
        fontSize=26,
        leading=32,
        textColor=AZUL,
        alignment=TA_CENTER,
        spaceAfter=10,
    )
    capa_sub = ParagraphStyle(
        "CapaSub",
        fontName="Helvetica",
        fontSize=13,
        leading=18,
        textColor=CINZA_TEXTO,
        alignment=TA_CENTER,
        spaceAfter=6,
    )
    num_questao = ParagraphStyle(
        "NumQuestao",
        fontName="Helvetica-Bold",
        fontSize=10,
        leading=13,
        textColor=colors.white,
        alignment=TA_LEFT,
    )
    enunciado = ParagraphStyle(
        "Enunciado",
        fontName="Helvetica",
        fontSize=10.5,
        leading=15,
        textColor=PRETO,
        alignment=TA_JUSTIFY,
        spaceAfter=6,
    )
    pergunta = ParagraphStyle(
        "Pergunta",
        fontName="Helvetica-Bold",
        fontSize=10.5,
        leading=14,
        textColor=PRETO,
        alignment=TA_LEFT,
        spaceAfter=8,
    )
    alternativa = ParagraphStyle(
        "Alternativa",
        fontName="Helvetica",
        fontSize=10.5,
        leading=14,
        textColor=PRETO,
        leftIndent=10,
        spaceAfter=2,
    )
    gabarito_label = ParagraphStyle(
        "GabaritoLabel",
        fontName="Helvetica-Bold",
        fontSize=14,
        leading=18,
        textColor=AZUL,
        alignment=TA_CENTER,
        spaceBefore=20,
        spaceAfter=10,
    )
    gab_item = ParagraphStyle(
        "GabItem",
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=PRETO,
    )
    rodape = ParagraphStyle(
        "Rodape",
        fontName="Helvetica",
        fontSize=8,
        leading=10,
        textColor=CINZA_TEXTO,
        alignment=TA_CENTER,
    )
    topico_tag = ParagraphStyle(
        "TopicoTag",
        fontName="Helvetica-Bold",
        fontSize=8,
        leading=10,
        textColor=AZUL,
        spaceAfter=4,
    )
    return dict(
        capa_titulo=capa_titulo,
        capa_sub=capa_sub,
        enunciado=enunciado,
        pergunta=pergunta,
        alternativa=alternativa,
        gabarito_label=gabarito_label,
        gab_item=gab_item,
        rodape=rodape,
        topico_tag=topico_tag,
    )


# ── Capa ───────────────────────────────────────────────────────────────────

def pagina_capa(st):
    s = []
    s.append(Spacer(1, 3*cm))
    s.append(Paragraph("SINGULAR MENTORIA", st["capa_sub"]))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph("200 Questões de Matemática", st["capa_titulo"]))
    s.append(Paragraph("para a Reta Final do ENEM", st["capa_titulo"]))
    s.append(Spacer(1, 0.6*cm))
    s.append(HRFlowable(width="60%", thickness=2, color=AZUL, hAlign="CENTER"))
    s.append(Spacer(1, 0.6*cm))
    s.append(Paragraph(f"Prévia — {LOTES_INFO}", st["capa_sub"]))
    s.append(Paragraph(SUBTITULO, st["capa_sub"]))
    s.append(Spacer(1, 2*cm))
    s.append(Paragraph(
        "Questões no estilo ENEM: contexto real, enunciado narrativo,<br/>"
        "5 alternativas (A–E) em ordem crescente.",
        st["capa_sub"]
    ))
    return s


# ── Marcador de dificuldade ────────────────────────────────────────────────

DIFIC_LABEL = {"facil": "● Fácil", "media": "●● Médio", "dificil": "●●● Difícil"}
DIFIC_COR   = {"facil": VERDE, "media": AZUL, "dificil": colors.HexColor("#C92A2A")}

def tag_dificuldade(dificuldade):
    label = DIFIC_LABEL.get(dificuldade, dificuldade)
    cor_hex = DIFIC_COR.get(dificuldade, CINZA_TEXTO)
    st = ParagraphStyle(
        "TagDif",
        fontName="Helvetica-Bold",
        fontSize=8,
        textColor=cor_hex,
        spaceAfter=3,
    )
    return Paragraph(label, st)


# ── Bloco de cada questão ──────────────────────────────────────────────────

def bloco_questao(num, q, st):
    elementos = []

    topico_fmt = q.get("topico", "").replace("_", " ").title()
    dif = q.get("dificuldade", "")

    cabecalho = ParagraphStyle(
        "Cab",
        fontName="Helvetica-Bold",
        fontSize=9,
        textColor=AZUL,
        spaceBefore=14,
        spaceAfter=4,
    )
    elementos.append(Paragraph(
        f"QUESTÃO {num}  <font color='#868E96'>|  {topico_fmt}</font>",
        cabecalho
    ))
    elementos.append(tag_dificuldade(dif))
    elementos.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#DEE2E6")))
    elementos.append(Spacer(1, 5))

    # Enunciado — quebra \n\n em parágrafos separados
    for parte in q["enunciado"].split("\n\n"):
        parte = parte.strip()
        if parte:
            elementos.append(Paragraph(parte, st["enunciado"]))

    elementos.append(Paragraph(q["pergunta"], st["pergunta"]))

    for letra in "ABCDE":
        texto_alt = q["alternativas"][letra]
        gab = q["gabarito"]
        if letra == gab:
            alt_st = ParagraphStyle(
                "AltCerta",
                parent=st["alternativa"],
                textColor=VERDE,
                fontName="Helvetica-Bold",
            )
            elementos.append(Paragraph(f"({letra})  {texto_alt}  ✓", alt_st))
        else:
            elementos.append(Paragraph(f"({letra})  {texto_alt}", st["alternativa"]))

    return KeepTogether(elementos)


# ── Gabarito final ─────────────────────────────────────────────────────────

def pagina_gabarito(questoes, st):
    s = []
    s.append(Spacer(1, 0.5*cm))
    s.append(HRFlowable(width="100%", thickness=1.5, color=AZUL))
    s.append(Spacer(1, 0.3*cm))
    s.append(Paragraph(f"GABARITO — {LOTES_INFO.upper()}", st["gabarito_label"]))

    linhas = []
    for i, q in enumerate(questoes, start=1):
        linhas.append(f"Q{i:>3}: {q['gabarito']}")
        if i % 10 == 0:
            s.append(Paragraph("    ".join(linhas), st["gab_item"]))
            s.append(Spacer(1, 4))
            linhas = []
    if linhas:
        s.append(Paragraph("    ".join(linhas), st["gab_item"]))

    return s


# ── Montagem ───────────────────────────────────────────────────────────────

def gerar():
    st = estilos()
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=2.2*cm,
        rightMargin=2.2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm,
        title="200 Questões ENEM — Singular Mentoria",
        author="Singular Mentoria",
    )

    conteudo = []
    conteudo += pagina_capa(st)

    from reportlab.platypus import PageBreak
    conteudo.append(PageBreak())

    for i, q in enumerate(QUESTOES, start=1):
        conteudo.append(bloco_questao(i, q, st))
        conteudo.append(Spacer(1, 0.3*cm))

    conteudo.append(PageBreak())
    conteudo += pagina_gabarito(QUESTOES, st)

    doc.build(conteudo)
    print(f"\nPDF gerado: {OUTPUT}\n")


if __name__ == "__main__":
    gerar()
