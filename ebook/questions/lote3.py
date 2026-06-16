# lote3.py — Lote 3 · 40 questões
# Tópicos: Triângulos (16), Quadriláteros/Polígonos (12), Círculo e Setores (12)
# Gabarito: A×8  B×8  C×8  D×8  E×8
# Dificuldade: 6 fácil · 10 médio · 24 difícil

QUESTOES = [

    # ─────────────────────────────────────────────
    # TRIÂNGULOS — 16 questões (Q1 a Q16)
    # ─────────────────────────────────────────────

    {   # Q1 · Triângulos · Fácil · Gabarito A
        "enunciado": (
            "Um terreno retangular tem 6 m de largura e 8 m de comprimento. O proprietário "
            "pretende instalar um muro ao longo da diagonal do terreno para dividi-lo em "
            "dois triângulos retângulos iguais."
        ),
        "pergunta": "Qual é o comprimento do muro diagonal?",
        "alternativas": {
            "A": "10 m",
            "B": "11 m",
            "C": "12 m",
            "D": "13 m",
            "E": "14 m",
        },
        "gabarito": "A",
        "check": lambda: 6 ** 2 + 8 ** 2 == 10 ** 2,
        "figura": None,
        "dificuldade": "facil",
        "topico": "triangulos",
    },

    {   # Q2 · Triângulos · Fácil · Gabarito B
        "enunciado": (
            "Um lote triangular tem base medindo 20 m e altura de 15 m em relação a essa "
            "base. O proprietário deseja calcular a área do lote para contratar o serviço "
            "de terraplanagem, que é cobrado por metro quadrado."
        ),
        "pergunta": "Qual é a área do lote triangular?",
        "alternativas": {
            "A": "120 m²",
            "B": "150 m²",
            "C": "180 m²",
            "D": "200 m²",
            "E": "225 m²",
        },
        "gabarito": "B",
        "check": lambda: (20 * 15) / 2 == 150,
        "figura": None,
        "dificuldade": "facil",
        "topico": "triangulos",
    },

    {   # Q3 · Triângulos · Médio · Gabarito C
        "enunciado": (
            "Dois triângulos são semelhantes. Os lados do triângulo menor medem "
            "6 cm, 8 cm e 10 cm, e seu perímetro é de 24 cm. A razão de semelhança "
            "entre o triângulo maior e o menor é de 5 para 2."
        ),
        "pergunta": "Qual é o perímetro do triângulo maior?",
        "alternativas": {
            "A": "48 cm",
            "B": "54 cm",
            "C": "60 cm",
            "D": "66 cm",
            "E": "72 cm",
        },
        "gabarito": "C",
        "check": lambda: 24 * 5 / 2 == 60,
        "figura": None,
        "dificuldade": "media",
        "topico": "triangulos",
    },

    {   # Q4 · Triângulos · Médio · Gabarito D
        "enunciado": (
            "Uma escada de 13 m de comprimento está encostada em uma parede vertical. "
            "A base da escada foi afastada 5 m do pé da parede, por questões de segurança. "
            "O chão é plano e forma ângulo reto com a parede."
        ),
        "pergunta": "A que altura da parede o topo da escada se encontra?",
        "alternativas": {
            "A": "8 m",
            "B": "10 m",
            "C": "11 m",
            "D": "12 m",
            "E": "13 m",
        },
        "gabarito": "D",
        "check": lambda: 13 ** 2 - 5 ** 2 == 12 ** 2,
        "figura": None,
        "dificuldade": "media",
        "topico": "triangulos",
    },

    {   # Q5 · Triângulos · Médio · Gabarito E
        "enunciado": (
            "Um parque municipal tem formato de triângulo equilátero com lado medindo "
            "12 m. A prefeitura quer calcular a área total do parque para planejar o "
            "paisagismo. Dado: √3 ≈ 1,73."
        ),
        "pergunta": "Qual é a área do parque triangular?",
        "alternativas": {
            "A": "54,72 m²",
            "B": "58,14 m²",
            "C": "60,48 m²",
            "D": "61,56 m²",
            "E": "62,28 m²",
        },
        "gabarito": "E",
        "check": lambda: abs(1.73 / 4 * 12 ** 2 - 62.28) < 0.01,
        "figura": None,
        "dificuldade": "media",
        "topico": "triangulos",
    },

    {   # Q6 · Triângulos · Difícil · Gabarito A
        "enunciado": (
            "Em um dia ensolarado, uma árvore projeta uma sombra de 8 m sobre o solo "
            "plano. No mesmo instante, uma estaca vertical de 1,5 m de altura projeta "
            "uma sombra de 2 m. Usando semelhança de triângulos formados pelos raios "
            "solares, pela estaca e pela árvore com suas sombras,"
        ),
        "pergunta": "qual é a altura da árvore?",
        "alternativas": {
            "A": "6 m",
            "B": "7 m",
            "C": "8 m",
            "D": "9 m",
            "E": "10 m",
        },
        "gabarito": "A",
        "check": lambda: 8 * 1.5 / 2 == 6,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "triangulos",
    },

    {   # Q7 · Triângulos · Difícil · Gabarito B
        "enunciado": (
            "Uma torre de transmissão vertical mede 24 m de altura. Dois cabos de aço "
            "partem do seu topo: o primeiro é fixado no chão a 7 m da base da torre, e "
            "o segundo é fixado no chão a 10 m da base, do lado oposto. Os cabos formam "
            "triângulos retângulos com a torre e o solo."
        ),
        "pergunta": "Qual é o comprimento total dos dois cabos?",
        "alternativas": {
            "A": "47 m",
            "B": "51 m",
            "C": "54 m",
            "D": "57 m",
            "E": "60 m",
        },
        "gabarito": "B",
        "check": lambda: (24 ** 2 + 7 ** 2) ** 0.5 + (24 ** 2 + 10 ** 2) ** 0.5 == 51,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "triangulos",
    },

    {   # Q8 · Triângulos · Difícil · Gabarito C
        "enunciado": (
            "Uma estrada de montanha parte do ponto A, sobe 30 m verticalmente e percorre "
            "40 m horizontalmente até o ponto B, no cume de uma colina. A partir de B, "
            "a estrada desce 24 m verticalmente e avança 32 m horizontalmente até o "
            "ponto C no vale. Os dois trechos formam triângulos retângulos."
        ),
        "pergunta": "Qual é o comprimento total do trajeto de A até C, ao longo da estrada?",
        "alternativas": {
            "A": "80 m",
            "B": "85 m",
            "C": "90 m",
            "D": "95 m",
            "E": "100 m",
        },
        "gabarito": "C",
        "check": lambda: (30 ** 2 + 40 ** 2) ** 0.5 + (24 ** 2 + 32 ** 2) ** 0.5 == 90,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "triangulos",
    },

    {   # Q9 · Triângulos · Difícil · Gabarito D
        "enunciado": (
            "Um terreno triangular tem os três lados medindo 10 m, 24 m e 26 m. "
            "Um topógrafo suspeita que o terreno forma um triângulo retângulo e quer "
            "confirmar isso antes de calcular a área pelo método simplificado "
            "(base × altura / 2)."
        ),
        "pergunta": "Supondo que o triângulo seja realmente retângulo, qual é a área do terreno?",
        "alternativas": {
            "A": "100 m²",
            "B": "108 m²",
            "C": "112 m²",
            "D": "120 m²",
            "E": "130 m²",
        },
        "gabarito": "D",
        "check": lambda: 10 ** 2 + 24 ** 2 == 26 ** 2 and (10 * 24) / 2 == 120,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "triangulos",
    },

    {   # Q10 · Triângulos · Difícil · Gabarito E
        "enunciado": (
            "No triângulo ABC, traçou-se uma reta paralela ao lado BC passando por um "
            "ponto D do lado AB, determinando o ponto E no lado AC. Sabe-se que "
            "AD = 6 cm, DB = 4 cm e BC = 15 cm. Pelo Teorema de Tales, a reta DE "
            "divide os lados proporcionalmente."
        ),
        "pergunta": "Qual é o comprimento de DE?",
        "alternativas": {
            "A": "5 cm",
            "B": "6 cm",
            "C": "7 cm",
            "D": "8 cm",
            "E": "9 cm",
        },
        "gabarito": "E",
        "check": lambda: 15 * 6 / (6 + 4) == 9,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "triangulos",
    },

    {   # Q11 · Triângulos · Difícil · Gabarito A
        "enunciado": (
            "Um galpão tem telhado com formato de triângulo isósceles. A base do triângulo "
            "mede 16 m e os dois lados iguais medem 10 m cada. Para calcular a quantidade "
            "de telhas, o engenheiro precisa da área da superfície do telhado."
        ),
        "pergunta": "Qual é a área do triângulo que forma o telhado?",
        "alternativas": {
            "A": "48 m²",
            "B": "52 m²",
            "C": "56 m²",
            "D": "60 m²",
            "E": "64 m²",
        },
        "gabarito": "A",
        "check": lambda: (16 * (10 ** 2 - 8 ** 2) ** 0.5) / 2 == 48,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "triangulos",
    },

    {   # Q12 · Triângulos · Difícil · Gabarito B
        "enunciado": (
            "Um triângulo retângulo tem hipotenusa de 25 cm e um dos catetos medindo "
            "7 cm. A partir do vértice do ângulo reto, traça-se a altura h relativa "
            "à hipotenusa, que é usada em projetos de engenharia para determinar "
            "subdivisões internas da peça."
        ),
        "pergunta": "Qual é o comprimento dessa altura h?",
        "alternativas": {
            "A": "5,60 cm",
            "B": "6,72 cm",
            "C": "7,14 cm",
            "D": "7,68 cm",
            "E": "8,00 cm",
        },
        "gabarito": "B",
        "check": lambda: abs(7 * (25 ** 2 - 7 ** 2) ** 0.5 / 25 - 6.72) < 0.01,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "triangulos",
    },

    {   # Q13 · Triângulos · Difícil · Gabarito C
        "enunciado": (
            "Os pontos médios dos lados de um retângulo de 12 cm × 9 cm foram "
            "unidos, formando um losango interno. Essa construção é usada em design "
            "gráfico para criar padrões geométricos."
        ),
        "pergunta": "Qual é a área do losango formado?",
        "alternativas": {
            "A": "42 cm²",
            "B": "48 cm²",
            "C": "54 cm²",
            "D": "60 cm²",
            "E": "66 cm²",
        },
        "gabarito": "C",
        "check": lambda: (12 * 9) / 2 == 54,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "triangulos",
    },

    {   # Q14 · Triângulos · Difícil · Gabarito D
        "enunciado": (
            "Uma equipe de orientação esportiva parte do ponto A, caminha 9 km "
            "exatamente para o norte e depois caminha 12 km exatamente para o leste, "
            "chegando ao ponto B. O trajeto formou um ângulo reto no ponto intermediário."
        ),
        "pergunta": "Qual é a distância em linha reta entre os pontos A e B?",
        "alternativas": {
            "A": "12 km",
            "B": "13 km",
            "C": "14 km",
            "D": "15 km",
            "E": "16 km",
        },
        "gabarito": "D",
        "check": lambda: (9 ** 2 + 12 ** 2) ** 0.5 == 15,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "triangulos",
    },

    {   # Q15 · Triângulos · Difícil · Gabarito E
        "enunciado": (
            "Uma placa de sinalização tem formato de triângulo equilátero com lado "
            "de 60 cm. A fábrica precisa calcular a área de cada placa para determinar "
            "o consumo de tinta por unidade produzida. Dado: √3 ≈ 1,73."
        ),
        "pergunta": "Qual é a área da placa triangular?",
        "alternativas": {
            "A": "1.368,00 cm²",
            "B": "1.440,00 cm²",
            "C": "1.492,00 cm²",
            "D": "1.530,00 cm²",
            "E": "1.557,00 cm²",
        },
        "gabarito": "E",
        "check": lambda: abs(1.73 / 4 * 60 ** 2 - 1557) < 0.5,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "triangulos",
    },

    {   # Q16 · Triângulos · Difícil · Gabarito A
        "enunciado": (
            "Um terreno triangular tem os três lados medindo 13 m, 14 m e 15 m. "
            "Para calcular a área, o engenheiro utiliza a Fórmula de Heron: "
            "A = √(s·(s−a)·(s−b)·(s−c)), onde s é o semiperímetro "
            "s = (a+b+c)/2."
        ),
        "pergunta": "Qual é a área do terreno?",
        "alternativas": {
            "A": "84 m²",
            "B": "88 m²",
            "C": "92 m²",
            "D": "96 m²",
            "E": "100 m²",
        },
        "gabarito": "A",
        "check": lambda: (21 * 8 * 7 * 6) ** 0.5 == 84,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "triangulos",
    },

    # ─────────────────────────────────────────────
    # QUADRILÁTEROS E POLÍGONOS — 12 questões (Q17 a Q28)
    # ─────────────────────────────────────────────

    {   # Q17 · Quadriláteros · Fácil · Gabarito B
        "enunciado": (
            "Uma sala retangular mede 8 m de comprimento e 5 m de largura. O proprietário "
            "contratou um serviço de instalação de piso cerâmico, que cobra R$ 45,00 "
            "por metro quadrado. Para fechar o orçamento, ele precisa da área total do piso."
        ),
        "pergunta": "Qual é a área do piso da sala?",
        "alternativas": {
            "A": "32 m²",
            "B": "40 m²",
            "C": "48 m²",
            "D": "52 m²",
            "E": "56 m²",
        },
        "gabarito": "B",
        "check": lambda: 8 * 5 == 40,
        "figura": None,
        "dificuldade": "facil",
        "topico": "quadrilateros",
    },

    {   # Q18 · Quadriláteros · Fácil · Gabarito C
        "enunciado": (
            "Uma praça pública tem formato de quadrado com 50 m de lado. A prefeitura "
            "municipal quer plantar grama em toda a área da praça. A empresa de "
            "jardinagem cobra por metro quadrado de área plantada."
        ),
        "pergunta": "Qual é a área total da praça?",
        "alternativas": {
            "A": "2.000 m²",
            "B": "2.250 m²",
            "C": "2.500 m²",
            "D": "2.750 m²",
            "E": "3.000 m²",
        },
        "gabarito": "C",
        "check": lambda: 50 ** 2 == 2500,
        "figura": None,
        "dificuldade": "facil",
        "topico": "quadrilateros",
    },

    {   # Q19 · Quadriláteros · Médio · Gabarito D
        "enunciado": (
            "Um terreno tem formato de trapézio com as duas bases paralelas medindo "
            "18 m e 24 m. A distância perpendicular entre as bases (altura do trapézio) "
            "é de 10 m. O dono quer calcular a área para pagar o IPTU."
        ),
        "pergunta": "Qual é a área do terreno trapezoidal?",
        "alternativas": {
            "A": "180 m²",
            "B": "190 m²",
            "C": "200 m²",
            "D": "210 m²",
            "E": "220 m²",
        },
        "gabarito": "D",
        "check": lambda: (18 + 24) / 2 * 10 == 210,
        "figura": None,
        "dificuldade": "media",
        "topico": "quadrilateros",
    },

    {   # Q20 · Quadriláteros · Médio · Gabarito E
        "enunciado": (
            "Uma rampa de acesso para cadeirantes tem formato de paralelogramo com "
            "base de 15 m e altura perpendicular de 8 m. A construtora precisa da área "
            "para calcular a quantidade de concreto a ser aplicada no revestimento."
        ),
        "pergunta": "Qual é a área da superfície da rampa?",
        "alternativas": {
            "A": "90 m²",
            "B": "100 m²",
            "C": "108 m²",
            "D": "114 m²",
            "E": "120 m²",
        },
        "gabarito": "E",
        "check": lambda: 15 * 8 == 120,
        "figura": None,
        "dificuldade": "media",
        "topico": "quadrilateros",
    },

    {   # Q21 · Quadriláteros · Médio · Gabarito A
        "enunciado": (
            "Uma peça metálica em formato de losango tem diagonais medindo 10 cm e "
            "24 cm. Para fabricar a moldura que envolve a peça, o técnico precisa "
            "conhecer o perímetro do losango, dado por quatro vezes o lado."
        ),
        "pergunta": "Qual é o perímetro do losango?",
        "alternativas": {
            "A": "52 cm",
            "B": "56 cm",
            "C": "60 cm",
            "D": "64 cm",
            "E": "68 cm",
        },
        "gabarito": "A",
        "check": lambda: 4 * (5 ** 2 + 12 ** 2) ** 0.5 == 52,
        "figura": None,
        "dificuldade": "media",
        "topico": "quadrilateros",
    },

    {   # Q22 · Quadriláteros · Difícil · Gabarito B
        "enunciado": (
            "Um terreno tem formato de trapézio retângulo, com as bases paralelas "
            "medindo 4 m e 16 m, e a altura (lado perpendicular) de 9 m. O proprietário "
            "quer construir um muro ao longo de todos os lados do terreno, inclusive "
            "pelo lado oblíquo."
        ),
        "pergunta": "Qual é o perímetro total do terreno?",
        "alternativas": {
            "A": "38 m",
            "B": "44 m",
            "C": "48 m",
            "D": "52 m",
            "E": "56 m",
        },
        "gabarito": "B",
        "check": lambda: 4 + 16 + 9 + (12 ** 2 + 9 ** 2) ** 0.5 == 44,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "quadrilateros",
    },

    {   # Q23 · Quadriláteros · Difícil · Gabarito C
        "enunciado": (
            "Um azulejo decorativo tem formato de hexágono regular com lado de 6 cm. "
            "O hexágono regular pode ser dividido em 6 triângulos equiláteros iguais. "
            "A fábrica de azulejos precisa calcular a área de cada peça. Dado: √3 ≈ 1,73."
        ),
        "pergunta": "Qual é a área do azulejo hexagonal?",
        "alternativas": {
            "A": "85,32 cm²",
            "B": "89,46 cm²",
            "C": "93,42 cm²",
            "D": "97,38 cm²",
            "E": "101,52 cm²",
        },
        "gabarito": "C",
        "check": lambda: abs(6 * (1.73 / 4 * 6 ** 2) - 93.42) < 0.01,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "quadrilateros",
    },

    {   # Q24 · Quadriláteros · Difícil · Gabarito D
        "enunciado": (
            "Um azulejo quadrado de 20 cm de lado teve os quatro cantos cortados em "
            "forma de triângulo isósceles retângulo, com catetos de 5 cm cada, resultando "
            "em um octógono. Esse formato é comum em pisos de estilo clássico."
        ),
        "pergunta": "Qual é a área do octógono resultante?",
        "alternativas": {
            "A": "310 cm²",
            "B": "320 cm²",
            "C": "330 cm²",
            "D": "350 cm²",
            "E": "370 cm²",
        },
        "gabarito": "D",
        "check": lambda: 20 ** 2 - 4 * (5 * 5 / 2) == 350,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "quadrilateros",
    },

    {   # Q25 · Quadriláteros · Difícil · Gabarito E
        "enunciado": (
            "Um retângulo de 24 cm × 10 cm tem um círculo inscrito, tangente aos dois "
            "lados menores. O raio do círculo é igual à metade da largura do retângulo. "
            "Um designer quer calcular a área do retângulo não coberta pelo círculo. "
            "Dado: π ≈ 3,14."
        ),
        "pergunta": "Qual é essa área restante?",
        "alternativas": {
            "A": "148,5 cm²",
            "B": "152,5 cm²",
            "C": "155,0 cm²",
            "D": "158,5 cm²",
            "E": "161,5 cm²",
        },
        "gabarito": "E",
        "check": lambda: abs(24 * 10 - 3.14 * 5 ** 2 - 161.5) < 0.01,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "quadrilateros",
    },

    {   # Q26 · Quadriláteros · Difícil · Gabarito A
        "enunciado": (
            "Um paisagista precisa cercar um jardim retangular de 100 m² usando o "
            "menor comprimento possível de cerca. Sabe-se que, para área fixa, o "
            "retângulo de menor perímetro é o quadrado."
        ),
        "pergunta": "Qual é o comprimento mínimo de cerca necessário para cercar o jardim?",
        "alternativas": {
            "A": "40 m",
            "B": "44 m",
            "C": "48 m",
            "D": "52 m",
            "E": "56 m",
        },
        "gabarito": "A",
        "check": lambda: 4 * 100 ** 0.5 == 40,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "quadrilateros",
    },

    {   # Q27 · Quadriláteros · Difícil · Gabarito B
        "enunciado": (
            "Uma pista de atletismo tem formato retangular com semicírculos nas duas "
            "extremidades, formando um estádio oval. A parte reta central mede 100 m "
            "de comprimento e a largura total da pista (incluindo os semicírculos) "
            "é de 70 m. Dado: π ≈ 3,14."
        ),
        "pergunta": "Qual é o comprimento total de uma volta na pista?",
        "alternativas": {
            "A": "408,4 m",
            "B": "419,8 m",
            "C": "428,6 m",
            "D": "437,2 m",
            "E": "448,0 m",
        },
        "gabarito": "B",
        "check": lambda: abs(2 * 100 + 2 * 3.14 * 35 - 419.8) < 0.01,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "quadrilateros",
    },

    {   # Q28 · Quadriláteros · Difícil · Gabarito C
        "enunciado": (
            "Uma peça de madeira tem formato de octógono regular com lado de 5 cm. "
            "A área de um octógono regular de lado L é dada por "
            "A = 2(1 + √2) × L². O carpinteiro precisa da área para orçar a laca "
            "de acabamento. Dado: √2 ≈ 1,41."
        ),
        "pergunta": "Qual é a área da peça octogonal?",
        "alternativas": {
            "A": "108,5 cm²",
            "B": "114,0 cm²",
            "C": "120,5 cm²",
            "D": "127,0 cm²",
            "E": "133,5 cm²",
        },
        "gabarito": "C",
        "check": lambda: abs(2 * (1 + 1.41) * 5 ** 2 - 120.5) < 0.01,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "quadrilateros",
    },

    # ─────────────────────────────────────────────
    # CÍRCULO E SETORES — 12 questões (Q29 a Q40)
    # ─────────────────────────────────────────────

    {   # Q29 · Círculo · Fácil · Gabarito D
        "enunciado": (
            "Uma pizzaria serve pizzas redondas com raio de 20 cm. O gerente quer "
            "calcular a área de cada pizza para comparar o custo por centímetro "
            "quadrado com a concorrência. Dado: π ≈ 3,14."
        ),
        "pergunta": "Qual é a área de uma pizza inteira?",
        "alternativas": {
            "A": "1.024 cm²",
            "B": "1.100 cm²",
            "C": "1.200 cm²",
            "D": "1.256 cm²",
            "E": "1.440 cm²",
        },
        "gabarito": "D",
        "check": lambda: abs(3.14 * 20 ** 2 - 1256) < 0.01,
        "figura": None,
        "dificuldade": "facil",
        "topico": "circulo_setores",
    },

    {   # Q30 · Círculo · Fácil · Gabarito E
        "enunciado": (
            "Uma roda de bicicleta tem diâmetro de 70 cm. Cada vez que a roda dá uma "
            "volta completa, a bicicleta avança uma distância igual ao comprimento da "
            "circunferência. Dado: π ≈ 3,14."
        ),
        "pergunta": "Qual é a distância percorrida pela bicicleta em uma volta completa da roda?",
        "alternativas": {
            "A": "185,0 cm",
            "B": "196,0 cm",
            "C": "204,0 cm",
            "D": "212,0 cm",
            "E": "219,8 cm",
        },
        "gabarito": "E",
        "check": lambda: abs(3.14 * 70 - 219.8) < 0.01,
        "figura": None,
        "dificuldade": "facil",
        "topico": "circulo_setores",
    },

    {   # Q31 · Círculo · Médio · Gabarito A
        "enunciado": (
            "Uma fatia de pizza equivale a um setor circular com ângulo central de "
            "60° (ou seja, a pizza foi cortada em 6 fatias iguais). O raio da pizza "
            "é de 15 cm. Dado: π ≈ 3,14."
        ),
        "pergunta": "Qual é a área de uma fatia?",
        "alternativas": {
            "A": "117,75 cm²",
            "B": "120,50 cm²",
            "C": "124,25 cm²",
            "D": "128,00 cm²",
            "E": "132,75 cm²",
        },
        "gabarito": "A",
        "check": lambda: abs(60 / 360 * 3.14 * 15 ** 2 - 117.75) < 0.01,
        "figura": None,
        "dificuldade": "media",
        "topico": "circulo_setores",
    },

    {   # Q32 · Círculo · Médio · Gabarito B
        "enunciado": (
            "Uma pista circular de corrida tem raio externo de 50 m e raio interno "
            "de 40 m. A área da pista corresponde à região entre as duas circunferências "
            "(coroa circular), que será asfaltada. Dado: π ≈ 3,14."
        ),
        "pergunta": "Qual é a área da pista que será asfaltada?",
        "alternativas": {
            "A": "2.512 m²",
            "B": "2.826 m²",
            "C": "3.140 m²",
            "D": "3.454 m²",
            "E": "3.768 m²",
        },
        "gabarito": "B",
        "check": lambda: abs(3.14 * (50 ** 2 - 40 ** 2) - 2826) < 0.01,
        "figura": None,
        "dificuldade": "media",
        "topico": "circulo_setores",
    },

    {   # Q33 · Círculo · Médio · Gabarito C
        "enunciado": (
            "O ponteiro das horas de um relógio analógico mede 10 cm de comprimento. "
            "Em 2 horas, esse ponteiro percorre um ângulo central de 60°. O comprimento "
            "do arco percorrido é dado por (θ/360) × 2πr. Dado: π ≈ 3,14."
        ),
        "pergunta": "Qual é o comprimento do arco percorrido pela ponta do ponteiro das horas em 2 horas?",
        "alternativas": {
            "A": "8,37 cm",
            "B": "9,42 cm",
            "C": "10,47 cm",
            "D": "11,52 cm",
            "E": "12,57 cm",
        },
        "gabarito": "C",
        "check": lambda: abs(60 / 360 * 2 * 3.14 * 10 - 10.47) < 0.01,
        "figura": None,
        "dificuldade": "media",
        "topico": "circulo_setores",
    },

    {   # Q34 · Círculo · Médio · Gabarito D
        "enunciado": (
            "Um setor circular tem raio de 6 cm e ângulo central de 90°. Dentro desse "
            "setor, traça-se um triângulo retângulo isósceles cujos catetos coincidem "
            "com os dois raios do setor. A região sombreada é a parte do setor não "
            "ocupada pelo triângulo (a 'casca' entre o arco e a hipotenusa). Dado: π ≈ 3,14."
        ),
        "pergunta": "Qual é a área da região sombreada?",
        "alternativas": {
            "A": "8,14 cm²",
            "B": "9,42 cm²",
            "C": "10,14 cm²",
            "D": "10,26 cm²",
            "E": "11,14 cm²",
        },
        "gabarito": "D",
        "check": lambda: abs(90 / 360 * 3.14 * 6 ** 2 - 6 ** 2 / 2 - 10.26) < 0.01,
        "figura": None,
        "dificuldade": "media",
        "topico": "circulo_setores",
    },

    {   # Q35 · Círculo · Difícil · Gabarito E
        "enunciado": (
            "Uma arruela metálica tem formato de coroa circular com raio externo de "
            "10 cm e raio interno de 6 cm. Na fabricação, remove-se um setor de 90° "
            "da coroa para abrir uma fenda de encaixe. Dado: π ≈ 3,14."
        ),
        "pergunta": "Qual é a área da arruela após a remoção do setor de 90°?",
        "alternativas": {
            "A": "138,16 cm²",
            "B": "142,44 cm²",
            "C": "145,20 cm²",
            "D": "148,56 cm²",
            "E": "150,72 cm²",
        },
        "gabarito": "E",
        "check": lambda: abs(270 / 360 * 3.14 * (10 ** 2 - 6 ** 2) - 150.72) < 0.01,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "circulo_setores",
    },

    {   # Q36 · Círculo · Difícil · Gabarito A
        "enunciado": (
            "Um círculo está inscrito em um quadrado de lado 20 cm, tangenciando os "
            "quatro lados. Um artesão quer recortar o círculo do quadrado e reaproveitar "
            "os 4 cantos restantes para outra peça. Dado: π ≈ 3,14."
        ),
        "pergunta": "Qual é a área total dos 4 cantos que sobram após o recorte do círculo?",
        "alternativas": {
            "A": "86 cm²",
            "B": "92 cm²",
            "C": "98 cm²",
            "D": "104 cm²",
            "E": "110 cm²",
        },
        "gabarito": "A",
        "check": lambda: abs(20 ** 2 - 3.14 * 10 ** 2 - 86) < 0.01,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "circulo_setores",
    },

    {   # Q37 · Círculo · Difícil · Gabarito B
        "enunciado": (
            "Sobre os quatro lados de um quadrado de 10 cm de lado, constroem-se "
            "externamente quatro semicírculos, um em cada lado. A figura resultante "
            "é usada em design de logotipos. Dado: π ≈ 3,14."
        ),
        "pergunta": "Qual é a área total da figura formada pelo quadrado e os quatro semicírculos?",
        "alternativas": {
            "A": "228,5 cm²",
            "B": "257,0 cm²",
            "C": "285,5 cm²",
            "D": "314,0 cm²",
            "E": "342,5 cm²",
        },
        "gabarito": "B",
        "check": lambda: abs(10 ** 2 + 4 * (3.14 * 5 ** 2 / 2) - 257) < 0.01,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "circulo_setores",
    },

    {   # Q38 · Círculo · Difícil · Gabarito C
        "enunciado": (
            "Um ventilador de teto possui 3 pás idênticas. Cada pá tem formato de "
            "setor circular com raio de 50 cm e ângulo central de 60°. A empresa "
            "fabricante quer calcular a área total de tinta necessária para pintar "
            "as 3 pás. Dado: π ≈ 3,14."
        ),
        "pergunta": "Qual é a área total das 3 pás do ventilador?",
        "alternativas": {
            "A": "3.300 cm²",
            "B": "3.610 cm²",
            "C": "3.925 cm²",
            "D": "4.240 cm²",
            "E": "4.555 cm²",
        },
        "gabarito": "C",
        "check": lambda: abs(3 * (60 / 360 * 3.14 * 50 ** 2) - 3925) < 0.01,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "circulo_setores",
    },

    {   # Q39 · Círculo · Difícil · Gabarito D
        "enunciado": (
            "Um estádio de atletismo tem formato oval: uma parte central retangular de "
            "90 m × 50 m e duas extremidades semicirculares com diâmetro de 50 m. "
            "A administração quer calcular a área total do campo para instalar "
            "iluminação proporcional. Dado: π ≈ 3,14."
        ),
        "pergunta": "Qual é a área total do estádio?",
        "alternativas": {
            "A": "5.890,0 m²",
            "B": "6.050,5 m²",
            "C": "6.215,0 m²",
            "D": "6.462,5 m²",
            "E": "6.710,0 m²",
        },
        "gabarito": "D",
        "check": lambda: abs(90 * 50 + 3.14 * 25 ** 2 - 6462.5) < 0.01,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "circulo_setores",
    },

    {   # Q40 · Círculo · Difícil · Gabarito E
        "enunciado": (
            "A tela de um smartphone tem formato retangular de 15 cm × 7 cm, com os "
            "quatro cantos arredondados. Cada canto é um quarto de círculo com raio "
            "de 1 cm. Ao arredondar, cada quarto de círculo substitui um quadradinho "
            "de 1 cm × 1 cm do canto. Dado: π ≈ 3,14."
        ),
        "pergunta": "Qual é a área efetiva da tela com os cantos arredondados?",
        "alternativas": {
            "A": "102,28 cm²",
            "B": "103,14 cm²",
            "C": "103,56 cm²",
            "D": "103,86 cm²",
            "E": "104,14 cm²",
        },
        "gabarito": "E",
        "check": lambda: abs(15 * 7 - 4 * 1 * 1 + 3.14 * 1 ** 2 - 104.14) < 0.01,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "circulo_setores",
    },

]
