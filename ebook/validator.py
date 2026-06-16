# -*- coding: utf-8 -*-
"""
validator.py — Valida matematicamente todas as questoes de todos os lotes.
Uso: python ebook/validator.py
"""

import importlib
import sys
import os

sys.stdout.reconfigure(encoding="utf-8")

LOTES = ["lote1", "lote2", "lote3"]  # adicionar "lote4"... conforme forem criados

CORES = {
    "ok":    "\033[92m",
    "erro":  "\033[91m",
    "info":  "\033[94m",
    "reset": "\033[0m",
}

def cor(texto, tipo):
    return f"{CORES[tipo]}{texto}{CORES['reset']}"


def validar_lote(nome_lote):
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    modulo = importlib.import_module(f"ebook.questions.{nome_lote}")
    questoes = modulo.QUESTOES

    erros = []
    gabarito_count = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
    dific_count = {"facil": 0, "media": 0, "dificil": 0}

    sep = "-" * 60
    print(cor(f"\n{sep}", "info"))
    print(cor(f"  Validando {nome_lote.upper()} -- {len(questoes)} questoes", "info"))
    print(cor(sep, "info"))

    for i, q in enumerate(questoes, start=1):
        for campo in ("enunciado", "pergunta", "alternativas", "gabarito", "check"):
            if campo not in q:
                erros.append(f"Q{i}: campo '{campo}' ausente")

        gab = q.get("gabarito", "")
        if gab not in "ABCDE" or len(gab) != 1:
            erros.append(f"Q{i}: gabarito invalido -> '{gab}'")
        else:
            gabarito_count[gab] += 1

        alts = q.get("alternativas", {})
        for letra in "ABCDE":
            if letra not in alts:
                erros.append(f"Q{i}: alternativa '{letra}' ausente")

        try:
            resultado = q["check"]()
            if not resultado:
                erros.append(
                    f"Q{i} [{q.get('topico','')}]: check() retornou False -- "
                    f"gabarito {gab} = {alts.get(gab, '?')}"
                )
            else:
                print(f"  Q{i:>3}  OK  {q.get('topico',''):<22}  "
                      f"{q.get('dificuldade',''):<8}  gab={gab}")
        except Exception as e:
            erros.append(f"Q{i}: check() lancou excecao -> {e}")

        dif = q.get("dificuldade", "")
        if dif in dific_count:
            dific_count[dif] += 1
        else:
            erros.append(f"Q{i}: dificuldade invalida -> '{dif}'")

    print(cor(f"\n{sep}", "info"))
    print("  Distribuicao de gabarito:")
    for letra, cnt in gabarito_count.items():
        barra = "#" * cnt
        print(f"    {letra}: {barra} ({cnt})")

    print("\n  Distribuicao de dificuldade:")
    total = len(questoes)
    for dif, cnt in dific_count.items():
        pct = cnt / total * 100 if total else 0
        print(f"    {dif:<10}: {cnt:>3} ({pct:.0f}%)")

    if erros:
        print(cor(f"\n  FALHOU -- {len(erros)} erro(s):", "erro"))
        for e in erros:
            print(cor(f"    - {e}", "erro"))
    else:
        print(cor(f"\n  APROVADO -- {len(questoes)} questoes sem erros.", "ok"))

    return len(erros) == 0


def main():
    todos_ok = True
    for lote in LOTES:
        ok = validar_lote(lote)
        if not ok:
            todos_ok = False

    sep = "=" * 60
    print(cor(f"\n{sep}", "info"))
    if todos_ok:
        print(cor("  VALIDACAO GERAL: APROVADA", "ok"))
    else:
        print(cor("  VALIDACAO GERAL: REPROVADA -- corrija os erros acima.", "erro"))
    print(cor(f"{sep}\n", "info"))
    sys.exit(0 if todos_ok else 1)


if __name__ == "__main__":
    main()
