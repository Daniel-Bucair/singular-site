# lote2.py — Lote 2 · 40 questões
# Tópicos: Função Afim (14), Função Quadrática (14), Função Exponencial (12)
# Gabarito: A×8  B×8  C×8  D×8  E×8

QUESTOES = [

    # ─────────────────────────────────────────────
    # FUNÇÃO AFIM — 14 questões (Q1 a Q14)
    # ─────────────────────────────────────────────

    {   # Q1 · Função Afim · Fácil · Gabarito A
        "enunciado": (
            "Um motorista de aplicativo cobra uma taxa fixa de entrada de R$ 5,00 "
            "acrescida de R$ 3,00 por quilômetro rodado. Nenhuma outra taxa é cobrada "
            "durante a corrida."
        ),
        "pergunta": "Qual será o valor total de uma corrida de 12 km?",
        "alternativas": {
            "A": "R$ 41,00",
            "B": "R$ 44,00",
            "C": "R$ 47,00",
            "D": "R$ 50,00",
            "E": "R$ 53,00",
        },
        "gabarito": "A",
        "check": lambda: 3 * 12 + 5 == 41,
        "figura": None,
        "dificuldade": "facil",
        "topico": "funcao_afim",
    },

    {   # Q2 · Função Afim · Fácil · Gabarito B
        "enunciado": (
            "Uma academia cobra mensalidade fixa de R$ 80,00 e R$ 15,00 por cada "
            "aula avulsa adicional contratada fora da franquia mensal. Em determinado "
            "mês, um aluno frequentou 6 aulas avulsas além da franquia."
        ),
        "pergunta": "Qual foi o valor total pago pelo aluno nesse mês?",
        "alternativas": {
            "A": "R$ 155,00",
            "B": "R$ 170,00",
            "C": "R$ 185,00",
            "D": "R$ 200,00",
            "E": "R$ 215,00",
        },
        "gabarito": "B",
        "check": lambda: 80 + 6 * 15 == 170,
        "figura": None,
        "dificuldade": "facil",
        "topico": "funcao_afim",
    },

    {   # Q3 · Função Afim · Fácil · Gabarito C
        "enunciado": (
            "Um marceneiro autônomo gasta R$ 12,00 em material por prateleira produzida "
            "e paga R$ 150,00 mensais de aluguel de seu ateliê. Em um determinado mês, "
            "ele produziu exatamente 25 prateleiras."
        ),
        "pergunta": "Qual foi o custo total do marceneiro nesse mês?",
        "alternativas": {
            "A": "R$ 390,00",
            "B": "R$ 420,00",
            "C": "R$ 450,00",
            "D": "R$ 480,00",
            "E": "R$ 510,00",
        },
        "gabarito": "C",
        "check": lambda: 12 * 25 + 150 == 450,
        "figura": None,
        "dificuldade": "facil",
        "topico": "funcao_afim",
    },

    {   # Q4 · Função Afim · Fácil · Gabarito D
        "enunciado": (
            "Uma usina solar opera com geração constante de energia. Às 7h — após "
            "1 hora de funcionamento — o medidor marcava 4 kWh acumulados. Às 11h "
            "— após 5 horas de funcionamento — o medidor marcava 20 kWh acumulados. "
            "A relação é linear."
        ),
        "pergunta": "Qual é a taxa de geração de energia da usina, em kWh por hora?",
        "alternativas": {
            "A": "2 kWh/h",
            "B": "3 kWh/h",
            "C": "3,5 kWh/h",
            "D": "4 kWh/h",
            "E": "5 kWh/h",
        },
        "gabarito": "D",
        "check": lambda: (20 - 4) / (5 - 1) == 4,
        "figura": None,
        "dificuldade": "facil",
        "topico": "funcao_afim",
    },

    {   # Q5 · Função Afim · Fácil · Gabarito E
        "enunciado": (
            "Um serviço de streaming cobra R$ 25,00 de assinatura mensal e R$ 4,00 "
            "por cada filme alugado na plataforma acima do limite incluso no plano. "
            "Em determinado mês, um usuário alugou 7 filmes extras."
        ),
        "pergunta": "Qual foi o valor cobrado desse usuário no mês?",
        "alternativas": {
            "A": "R$ 39,00",
            "B": "R$ 43,00",
            "C": "R$ 47,00",
            "D": "R$ 51,00",
            "E": "R$ 53,00",
        },
        "gabarito": "E",
        "check": lambda: 4 * 7 + 25 == 53,
        "figura": None,
        "dificuldade": "facil",
        "topico": "funcao_afim",
    },

    {   # Q6 · Função Afim · Médio · Gabarito A
        "enunciado": (
            "O valor cobrado por um táxi em uma cidade segue uma função afim do tipo "
            "C(d) = ad + b, onde d é a distância percorrida em quilômetros. Sabe-se "
            "que uma corrida de 6 km custou R$ 17,00 e uma corrida de 12 km custou "
            "R$ 29,00."
        ),
        "pergunta": "Qual seria o custo de uma corrida de 9 km com esse táxi?",
        "alternativas": {
            "A": "R$ 23,00",
            "B": "R$ 25,00",
            "C": "R$ 27,00",
            "D": "R$ 29,00",
            "E": "R$ 31,00",
        },
        "gabarito": "A",
        "check": lambda: (29 - 17) / (12 - 6) * 9 + (17 - (29 - 17) / (12 - 6) * 6) == 23,
        "figura": None,
        "dificuldade": "media",
        "topico": "funcao_afim",
    },

    {   # Q7 · Função Afim · Médio · Gabarito B
        "enunciado": (
            "Uma empresa de vendas paga a seus representantes um salário fixo de "
            "R$ 1.800,00 mensais, acrescido de 6% de comissão sobre o total de vendas "
            "realizadas no mês. Uma representante quer calcular o valor mínimo de vendas "
            "necessário para que sua remuneração total alcance R$ 3.000,00 no mês."
        ),
        "pergunta": "Qual é o valor mínimo de vendas que ela deve atingir?",
        "alternativas": {
            "A": "R$ 18.000,00",
            "B": "R$ 20.000,00",
            "C": "R$ 22.000,00",
            "D": "R$ 24.000,00",
            "E": "R$ 26.000,00",
        },
        "gabarito": "B",
        "check": lambda: 1800 + 0.06 * 20000 == 3000,
        "figura": None,
        "dificuldade": "media",
        "topico": "funcao_afim",
    },

    {   # Q8 · Função Afim · Médio · Gabarito C
        "enunciado": (
            "A temperatura T (em °C) em uma cidade litorânea varia linearmente ao longo "
            "de um dia de verão. Às 6h, a temperatura era de 18 °C, e às 14h atingiu "
            "34 °C. Admitindo variação estritamente linear durante todo esse período,"
        ),
        "pergunta": "qual era a temperatura às 11h?",
        "alternativas": {
            "A": "24 °C",
            "B": "26 °C",
            "C": "28 °C",
            "D": "30 °C",
            "E": "32 °C",
        },
        "gabarito": "C",
        "check": lambda: 18 + (34 - 18) / (14 - 6) * (11 - 6) == 28,
        "figura": None,
        "dificuldade": "media",
        "topico": "funcao_afim",
    },

    {   # Q9 · Função Afim · Médio · Gabarito D
        "enunciado": (
            "Um caminhão inicia uma viagem com 150 litros de combustível no tanque. "
            "O motor consome combustível a uma taxa constante de 8 litros por hora "
            "de deslocamento. O motorista planeja parar para abastecer quando restar "
            "exatamente 54 litros no tanque."
        ),
        "pergunta": "Após quantas horas de viagem o motorista deverá parar?",
        "alternativas": {
            "A": "9 horas",
            "B": "10 horas",
            "C": "11 horas",
            "D": "12 horas",
            "E": "13 horas",
        },
        "gabarito": "D",
        "check": lambda: (150 - 54) / 8 == 12,
        "figura": None,
        "dificuldade": "media",
        "topico": "funcao_afim",
    },

    {   # Q10 · Função Afim · Médio · Gabarito E
        "enunciado": (
            "Uma empresa de locação de patinetes elétricos cobra R$ 6,00 de taxa de "
            "desbloqueio e R$ 2,50 por cada 10 minutos de uso. Uma cliente utilizou "
            "o patinete por 1 hora e 40 minutos."
        ),
        "pergunta": "Qual foi o valor cobrado dessa cliente?",
        "alternativas": {
            "A": "R$ 25,00",
            "B": "R$ 27,00",
            "C": "R$ 29,00",
            "D": "R$ 30,00",
            "E": "R$ 31,00",
        },
        "gabarito": "E",
        "check": lambda: 2.50 * 10 + 6 == 31,
        "figura": None,
        "dificuldade": "media",
        "topico": "funcao_afim",
    },

    {   # Q11 · Função Afim · Difícil · Gabarito A
        "enunciado": (
            "Em uma rodovia, o piloto A partiu de um posto de combustível às 8h, "
            "viajando a velocidade constante de 120 km/h. O piloto B saiu do mesmo "
            "ponto 30 minutos depois, na mesma direção, a velocidade constante de "
            "150 km/h. Ambos mantiveram suas velocidades durante toda a viagem."
        ),
        "pergunta": "Após quantos minutos, contados a partir da saída do piloto B, ele alcançará o piloto A?",
        "alternativas": {
            "A": "120 minutos",
            "B": "130 minutos",
            "C": "140 minutos",
            "D": "150 minutos",
            "E": "160 minutos",
        },
        "gabarito": "A",
        "check": lambda: 150 * 2 == 120 * (2 + 0.5),
        "figura": None,
        "dificuldade": "dificil",
        "topico": "funcao_afim",
    },

    {   # Q12 · Função Afim · Difícil · Gabarito B
        "enunciado": (
            "Duas locadoras de andaimes praticam os seguintes preços: a empresa Alfa "
            "cobra R$ 200,00 de taxa de instalação e R$ 35,00 por dia de uso; a empresa "
            "Beta cobra R$ 50,00 de instalação e R$ 65,00 por dia. Para obras de "
            "curta duração, a Beta é mais barata; para obras longas, a Alfa passa a "
            "ser mais econômica."
        ),
        "pergunta": "A partir de qual dia de uso a empresa Alfa passa a ser mais econômica que a Beta?",
        "alternativas": {
            "A": "a partir do 4º dia",
            "B": "a partir do 6º dia",
            "C": "a partir do 8º dia",
            "D": "a partir do 10º dia",
            "E": "a partir do 12º dia",
        },
        "gabarito": "B",
        "check": lambda: (200 - 50) / (65 - 35) + 1 == 6,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "funcao_afim",
    },

    {   # Q13 · Função Afim · Difícil · Gabarito C
        "enunciado": (
            "Um agricultor possui um reservatório com 12.000 litros de água. Para "
            "irrigar a plantação, ele liga uma bomba que retira 180 litros por minuto. "
            "Ao mesmo tempo, uma nascente abastece o reservatório com 60 litros por "
            "minuto. O agricultor liga a bomba e não a desliga mais."
        ),
        "pergunta": "Quantos minutos levará para que o reservatório fique completamente vazio?",
        "alternativas": {
            "A": "80 minutos",
            "B": "90 minutos",
            "C": "100 minutos",
            "D": "110 minutos",
            "E": "120 minutos",
        },
        "gabarito": "C",
        "check": lambda: 12000 / (180 - 60) == 100,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "funcao_afim",
    },

    {   # Q14 · Função Afim · Difícil · Gabarito D
        "enunciado": (
            "Uma indústria farmacêutica produz dois medicamentos. O custo de produção "
            "do medicamento X é dado por Cx(q) = 120q + 4.800 reais e o do medicamento "
            "Y por Cy(q) = 180q + 1.200 reais, onde q é o número de frascos produzidos. "
            "Para baixas quantidades, Y é mais barato; à medida que q cresce, X torna-se "
            "mais econômico."
        ),
        "pergunta": "A partir de quantos frascos o custo de produção do medicamento X passa a ser inferior ao de Y?",
        "alternativas": {
            "A": "a partir de 48 frascos",
            "B": "a partir de 52 frascos",
            "C": "a partir de 56 frascos",
            "D": "a partir de 61 frascos",
            "E": "a partir de 66 frascos",
        },
        "gabarito": "D",
        "check": lambda: (4800 - 1200) / (180 - 120) + 1 == 61,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "funcao_afim",
    },

    # ─────────────────────────────────────────────
    # FUNÇÃO QUADRÁTICA — 14 questões (Q15 a Q28)
    # ─────────────────────────────────────────────

    {   # Q15 · Quadrática · Fácil · Gabarito E
        "enunciado": (
            "Uma bola é lançada verticalmente para cima a partir do solo. Sua altura "
            "h (em metros) em função do tempo t (em segundos) é dada por "
            "h(t) = 20t − 5t². A bola sobe, atinge a altura máxima e retorna ao solo."
        ),
        "pergunta": "Após quantos segundos a bola retorna ao solo?",
        "alternativas": {
            "A": "1 segundo",
            "B": "2 segundos",
            "C": "3 segundos",
            "D": "3,5 segundos",
            "E": "4 segundos",
        },
        "gabarito": "E",
        "check": lambda: 20 * 4 - 5 * 4 ** 2 == 0,
        "figura": None,
        "dificuldade": "facil",
        "topico": "funcao_quadratica",
    },

    {   # Q16 · Quadrática · Fácil · Gabarito A
        "enunciado": (
            "O lucro L (em reais) de uma pequena empresa em função do número de "
            "unidades vendidas x é modelado por L(x) = −x² + 10x. A função tem "
            "um ponto de máximo que indica a quantidade ótima de vendas."
        ),
        "pergunta": "Quantas unidades devem ser vendidas para que o lucro seja máximo?",
        "alternativas": {
            "A": "5 unidades",
            "B": "6 unidades",
            "C": "7 unidades",
            "D": "8 unidades",
            "E": "10 unidades",
        },
        "gabarito": "A",
        "check": lambda: -10 / (2 * (-1)) == 5,
        "figura": None,
        "dificuldade": "facil",
        "topico": "funcao_quadratica",
    },

    {   # Q17 · Quadrática · Fácil · Gabarito B
        "enunciado": (
            "A área A (em m²) de um terreno retangular cercado é dada por "
            "A(x) = x(20 − x), onde x é a largura em metros. Um proprietário "
            "quer cercar uma área de exatamente 75 m²."
        ),
        "pergunta": "Qual é o menor valor da largura x (em metros) que satisfaz essa condição?",
        "alternativas": {
            "A": "3 m",
            "B": "5 m",
            "C": "7 m",
            "D": "10 m",
            "E": "15 m",
        },
        "gabarito": "B",
        "check": lambda: 5 * (20 - 5) == 75,
        "figura": None,
        "dificuldade": "facil",
        "topico": "funcao_quadratica",
    },

    {   # Q18 · Quadrática · Fácil · Gabarito C
        "enunciado": (
            "Uma pedra é solta do topo de uma falésia e sua altura h (em metros) "
            "acima do solo em função do tempo t (em segundos) é dada por "
            "h(t) = 80 − 5t². A pedra cai em queda livre até atingir o solo."
        ),
        "pergunta": "Em quantos segundos a pedra atinge o solo?",
        "alternativas": {
            "A": "2 segundos",
            "B": "3 segundos",
            "C": "4 segundos",
            "D": "5 segundos",
            "E": "6 segundos",
        },
        "gabarito": "C",
        "check": lambda: 80 - 5 * 4 ** 2 == 0,
        "figura": None,
        "dificuldade": "facil",
        "topico": "funcao_quadratica",
    },

    {   # Q19 · Quadrática · Médio · Gabarito D
        "enunciado": (
            "A receita total R (em reais) de uma confeitaria que vende bolos a um "
            "preço p (em reais) é modelada por R(p) = −2p² + 80p. A confeiteira "
            "quer definir o preço que maximiza a receita total."
        ),
        "pergunta": "Qual deve ser o preço unitário para maximizar a receita da confeitaria?",
        "alternativas": {
            "A": "R$ 12,00",
            "B": "R$ 15,00",
            "C": "R$ 18,00",
            "D": "R$ 20,00",
            "E": "R$ 24,00",
        },
        "gabarito": "D",
        "check": lambda: -80 / (2 * (-2)) == 20,
        "figura": None,
        "dificuldade": "media",
        "topico": "funcao_quadratica",
    },

    {   # Q20 · Quadrática · Médio · Gabarito E
        "enunciado": (
            "Um projétil é lançado e sua altura em metros em função do tempo em "
            "segundos é dada por h(t) = −5t² + 30t + 10. O projétil parte do solo "
            "com uma altura inicial de 10 metros (lançado de uma plataforma elevada)."
        ),
        "pergunta": "Qual é a altura máxima atingida pelo projétil?",
        "alternativas": {
            "A": "40 m",
            "B": "45 m",
            "C": "50 m",
            "D": "52 m",
            "E": "55 m",
        },
        "gabarito": "E",
        "check": lambda: -5 * 3 ** 2 + 30 * 3 + 10 == 55,
        "figura": None,
        "dificuldade": "media",
        "topico": "funcao_quadratica",
    },

    {   # Q21 · Quadrática · Médio · Gabarito A
        "enunciado": (
            "Um produtor rural observou que a produção P (em toneladas) de soja "
            "em função da quantidade de fertilizante aplicado x (em sacas por hectare) "
            "segue o modelo P(x) = −x² + 12x + 20, válido para 0 ≤ x ≤ 12. "
            "Aplicar fertilizante em excesso reduz a produção."
        ),
        "pergunta": "Qual quantidade de fertilizante por hectare maximiza a produção de soja?",
        "alternativas": {
            "A": "6 sacas/ha",
            "B": "7 sacas/ha",
            "C": "8 sacas/ha",
            "D": "9 sacas/ha",
            "E": "10 sacas/ha",
        },
        "gabarito": "A",
        "check": lambda: -12 / (2 * (-1)) == 6,
        "figura": None,
        "dificuldade": "media",
        "topico": "funcao_quadratica",
    },

    {   # Q22 · Quadrática · Médio · Gabarito B
        "enunciado": (
            "A função custo de produção de um item é C(x) = 2x² − 40x + 500 reais, "
            "onde x é o número de unidades produzidas. Um gerente de produção quer "
            "determinar a quantidade que minimiza o custo total."
        ),
        "pergunta": "Qual é o custo mínimo de produção (em reais)?",
        "alternativas": {
            "A": "R$ 250,00",
            "B": "R$ 300,00",
            "C": "R$ 350,00",
            "D": "R$ 400,00",
            "E": "R$ 450,00",
        },
        "gabarito": "B",
        "check": lambda: 2 * 10 ** 2 - 40 * 10 + 500 == 300,
        "figura": None,
        "dificuldade": "media",
        "topico": "funcao_quadratica",
    },

    {   # Q23 · Quadrática · Médio · Gabarito C
        "enunciado": (
            "Um arquiteto projetou um arco parabólico para a entrada de um parque. "
            "A equação que descreve o arco é y = −x² + 6x, onde x e y estão em metros "
            "e o eixo x representa o nível do chão. A largura do arco corresponde à "
            "distância entre os dois pontos onde ele toca o solo."
        ),
        "pergunta": "Qual é a largura do arco ao nível do solo?",
        "alternativas": {
            "A": "4 m",
            "B": "5 m",
            "C": "6 m",
            "D": "7 m",
            "E": "8 m",
        },
        "gabarito": "C",
        "check": lambda: -(6 ** 2) + 6 * 6 == 0,
        "figura": None,
        "dificuldade": "media",
        "topico": "funcao_quadratica",
    },

    {   # Q24 · Quadrática · Médio · Gabarito D
        "enunciado": (
            "Em uma cidade, o número semanal de casos de uma doença respiratória "
            "durante o inverno é modelado por N(t) = −3t² + 42t + 15, onde t é o "
            "número de semanas após o início do período de frio, com 0 ≤ t ≤ 14. "
            "Após o pico, os casos diminuem gradualmente."
        ),
        "pergunta": "Em qual semana o número de casos atinge o valor máximo?",
        "alternativas": {
            "A": "4ª semana",
            "B": "5ª semana",
            "C": "6ª semana",
            "D": "7ª semana",
            "E": "8ª semana",
        },
        "gabarito": "D",
        "check": lambda: -42 / (2 * (-3)) == 7,
        "figura": None,
        "dificuldade": "media",
        "topico": "funcao_quadratica",
    },

    {   # Q25 · Quadrática · Difícil · Gabarito E
        "enunciado": (
            "Um fazendeiro dispõe de 120 metros de arame para cercar um pasto "
            "retangular encostado em uma parede reta. A parede serve como um dos "
            "lados maiores, portanto apenas três lados precisam ser cercados com arame. "
            "Seja x a medida de cada um dos dois lados perpendiculares à parede."
        ),
        "pergunta": "Qual é a área máxima possível do pasto?",
        "alternativas": {
            "A": "1.500 m²",
            "B": "1.600 m²",
            "C": "1.700 m²",
            "D": "1.750 m²",
            "E": "1.800 m²",
        },
        "gabarito": "E",
        "check": lambda: 30 * (120 - 2 * 30) == 1800,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "funcao_quadratica",
    },

    {   # Q26 · Quadrática · Difícil · Gabarito A
        "enunciado": (
            "Um departamento de engenharia modela o custo de produção de um "
            "componente eletrônico por C(x) = x² − 24x + 200 reais, onde x é a "
            "quantidade produzida. O custo é mínimo para uma quantidade específica q "
            "de unidades."
        ),
        "pergunta": "Quais são a quantidade q e o custo mínimo correspondente?",
        "alternativas": {
            "A": "q = 12 unidades e custo mínimo de R$ 56,00",
            "B": "q = 13 unidades e custo mínimo de R$ 64,00",
            "C": "q = 14 unidades e custo mínimo de R$ 72,00",
            "D": "q = 15 unidades e custo mínimo de R$ 80,00",
            "E": "q = 16 unidades e custo mínimo de R$ 88,00",
        },
        "gabarito": "A",
        "check": lambda: 12 ** 2 - 24 * 12 + 200 == 56,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "funcao_quadratica",
    },

    {   # Q27 · Quadrática · Difícil · Gabarito B
        "enunciado": (
            "Um objeto é lançado do alto de uma plataforma. Sua posição vertical "
            "s (em metros acima do solo) em função do tempo t (em segundos) é dada "
            "por s(t) = −5t² + 20t + 60. O objeto sobe brevemente antes de cair."
        ),
        "pergunta": "Em que instante o objeto atinge o solo?",
        "alternativas": {
            "A": "5 segundos",
            "B": "6 segundos",
            "C": "7 segundos",
            "D": "8 segundos",
            "E": "9 segundos",
        },
        "gabarito": "B",
        "check": lambda: -5 * 6 ** 2 + 20 * 6 + 60 == 0,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "funcao_quadratica",
    },

    {   # Q28 · Quadrática · Difícil · Gabarito C
        "enunciado": (
            "Uma agência de publicidade percebeu que o número de visualizações V "
            "(em milhares) de um anúncio em função do investimento x (em milhares "
            "de reais) segue V(x) = −2x² + 24x − 40. O anúncio só é exibido quando "
            "V(x) > 0, ou seja, quando o investimento está dentro de um intervalo "
            "específico."
        ),
        "pergunta": "Qual é o investimento mínimo (em R$ mil) para que o anúncio comece a ser exibido?",
        "alternativas": {
            "A": "R$ 1.000,00",
            "B": "R$ 1.500,00",
            "C": "R$ 2.000,00",
            "D": "R$ 2.500,00",
            "E": "R$ 3.000,00",
        },
        "gabarito": "C",
        "check": lambda: -2 * 2 ** 2 + 24 * 2 - 40 == 0,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "funcao_quadratica",
    },

    # ─────────────────────────────────────────────
    # FUNÇÃO EXPONENCIAL — 12 questões (Q29 a Q40)
    # ─────────────────────────────────────────────

    {   # Q29 · Exponencial · Fácil · Gabarito D
        "enunciado": (
            "Uma colônia de bactérias dobra de tamanho a cada hora. No início do "
            "experimento havia 500 bactérias na amostra. O crescimento segue um "
            "modelo exponencial de base 2."
        ),
        "pergunta": "Quantas bactérias haverá na amostra após 3 horas?",
        "alternativas": {
            "A": "2.000",
            "B": "2.500",
            "C": "3.000",
            "D": "4.000",
            "E": "5.000",
        },
        "gabarito": "D",
        "check": lambda: 500 * 2 ** 3 == 4000,
        "figura": None,
        "dificuldade": "facil",
        "topico": "funcao_exponencial",
    },

    {   # Q30 · Exponencial · Fácil · Gabarito E
        "enunciado": (
            "Um smartphone perde 20% da carga da bateria a cada hora de uso contínuo "
            "sem recarga. Ao iniciar o uso, a bateria estava com 100% de carga. O "
            "processo de descarga segue um modelo exponencial de fator 0,80 por hora."
        ),
        "pergunta": "Qual é o percentual de carga restante após 3 horas de uso?",
        "alternativas": {
            "A": "40,0%",
            "B": "44,0%",
            "C": "48,0%",
            "D": "50,0%",
            "E": "51,2%",
        },
        "gabarito": "E",
        "check": lambda: abs(100 * 0.8 ** 3 - 51.2) < 0.01,
        "figura": None,
        "dificuldade": "facil",
        "topico": "funcao_exponencial",
    },

    {   # Q31 · Exponencial · Fácil · Gabarito A
        "enunciado": (
            "Um capital de R$ 1.000,00 é aplicado em uma poupança com juros compostos "
            "de 10% ao mês. Nenhuma retirada é feita durante o período de aplicação."
        ),
        "pergunta": "Qual será o montante ao final de 2 meses?",
        "alternativas": {
            "A": "R$ 1.210,00",
            "B": "R$ 1.220,00",
            "C": "R$ 1.230,00",
            "D": "R$ 1.240,00",
            "E": "R$ 1.250,00",
        },
        "gabarito": "A",
        "check": lambda: abs(1000 * 1.10 ** 2 - 1210) < 0.01,
        "figura": None,
        "dificuldade": "facil",
        "topico": "funcao_exponencial",
    },

    {   # Q32 · Exponencial · Fácil · Gabarito B
        "enunciado": (
            "O número de usuários de uma rede social cresce a uma taxa de 50% ao ano. "
            "Em 2022, a plataforma registrava 400 mil usuários ativos. Assumindo "
            "crescimento exponencial constante,"
        ),
        "pergunta": "qual é a projeção do número de usuários (em milhares) para 2024?",
        "alternativas": {
            "A": "800 mil",
            "B": "900 mil",
            "C": "1.000 mil",
            "D": "1.100 mil",
            "E": "1.200 mil",
        },
        "gabarito": "B",
        "check": lambda: abs(400 * 1.5 ** 2 - 900) < 0.01,
        "figura": None,
        "dificuldade": "facil",
        "topico": "funcao_exponencial",
    },

    {   # Q33 · Exponencial · Médio · Gabarito C
        "enunciado": (
            "Um elemento radioativo possui meia-vida de 30 anos, ou seja, perde metade "
            "de sua massa a cada 30 anos. Uma amostra inicial contém 640 gramas desse "
            "elemento. Após 90 anos, o material terá passado por três meias-vidas."
        ),
        "pergunta": "Qual será a massa da amostra após 90 anos?",
        "alternativas": {
            "A": "40 g",
            "B": "60 g",
            "C": "80 g",
            "D": "100 g",
            "E": "120 g",
        },
        "gabarito": "C",
        "check": lambda: 640 * (0.5) ** 3 == 80,
        "figura": None,
        "dificuldade": "media",
        "topico": "funcao_exponencial",
    },

    {   # Q34 · Exponencial · Médio · Gabarito D
        "enunciado": (
            "Um capital de R$ 2.000,00 é aplicado a juros compostos de 20% ao ano. "
            "Um investidor quer saber em quantos anos o montante superará R$ 3.000,00. "
            "Dados fornecidos: 1,20² = 1,44; 1,20³ = 1,728."
        ),
        "pergunta": "A partir de quantos anos completos o montante supera R$ 3.000,00?",
        "alternativas": {
            "A": "1 ano",
            "B": "2 anos",
            "C": "2,5 anos",
            "D": "3 anos",
            "E": "4 anos",
        },
        "gabarito": "D",
        "check": lambda: 2000 * 1.20 ** 2 < 3000 and 2000 * 1.20 ** 3 > 3000,
        "figura": None,
        "dificuldade": "media",
        "topico": "funcao_exponencial",
    },

    {   # Q35 · Exponencial · Médio · Gabarito E
        "enunciado": (
            "Uma epidemia de gripe em uma escola se espalhou de modo que o número "
            "de alunos infectados triplicava a cada dia. Na segunda-feira (dia 1), "
            "2 alunos estavam infectados. O crescimento seguiu essa taxa até o fim "
            "da semana."
        ),
        "pergunta": "Quantos alunos estarão infectados na sexta-feira (dia 5)?",
        "alternativas": {
            "A": "54",
            "B": "81",
            "C": "108",
            "D": "126",
            "E": "162",
        },
        "gabarito": "E",
        "check": lambda: 2 * 3 ** 4 == 162,
        "figura": None,
        "dificuldade": "media",
        "topico": "funcao_exponencial",
    },

    {   # Q36 · Exponencial · Médio · Gabarito A
        "enunciado": (
            "Um banco oferece aplicação de renda fixa com rentabilidade de 2% ao mês "
            "em regime de juros compostos. Ana investiu R$ 3.000,00 e quer calcular o "
            "rendimento líquido obtido ao final de 2 meses. Dado: 1,02² = 1,0404."
        ),
        "pergunta": "Qual é o rendimento líquido (montante menos capital) obtido por Ana ao final de 2 meses?",
        "alternativas": {
            "A": "R$ 121,20",
            "B": "R$ 123,00",
            "C": "R$ 124,80",
            "D": "R$ 126,00",
            "E": "R$ 128,40",
        },
        "gabarito": "A",
        "check": lambda: abs(3000 * 1.0404 - 3000 - 121.20) < 0.01,
        "figura": None,
        "dificuldade": "media",
        "topico": "funcao_exponencial",
    },

    {   # Q37 · Exponencial · Difícil · Gabarito B
        "enunciado": (
            "Um automóvel adquirido por R$ 80.000,00 deprecia a uma taxa de 15% ao "
            "ano sobre o valor do ano anterior. O proprietário quer saber após quantos "
            "anos o valor do veículo ficará abaixo de R$ 48.620,00. "
            "Dados: 0,85³ ≈ 0,6141; 0,85⁴ ≈ 0,5220."
        ),
        "pergunta": "Após quantos anos o valor do veículo será inferior a R$ 48.620,00?",
        "alternativas": {
            "A": "após 2 anos",
            "B": "após 4 anos",
            "C": "após 5 anos",
            "D": "após 6 anos",
            "E": "após 7 anos",
        },
        "gabarito": "B",
        "check": lambda: 80000 * 0.85 ** 3 > 48620 and 80000 * 0.85 ** 4 < 48620,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "funcao_exponencial",
    },

    {   # Q38 · Exponencial · Difícil · Gabarito C
        "enunciado": (
            "Duas cidades vizinhas têm as seguintes características populacionais: "
            "a Cidade A possui 200.000 habitantes e cresce a 10% ao ano; a Cidade B "
            "possui 250.000 habitantes e cresce a 4% ao ano. "
            "Dados: 1,10³ ≈ 1,331; 1,04³ ≈ 1,1249; 1,10⁴ ≈ 1,4641; 1,04⁴ ≈ 1,1699."
        ),
        "pergunta": "Após quantos anos a população da Cidade A ultrapassará a da Cidade B?",
        "alternativas": {
            "A": "após 2 anos",
            "B": "após 3 anos",
            "C": "após 4 anos",
            "D": "após 5 anos",
            "E": "após 6 anos",
        },
        "gabarito": "C",
        "check": lambda: (
            200000 * 1.10 ** 3 < 250000 * 1.04 ** 3
            and 200000 * 1.10 ** 4 > 250000 * 1.04 ** 4
        ),
        "figura": None,
        "dificuldade": "dificil",
        "topico": "funcao_exponencial",
    },

    {   # Q39 · Exponencial · Difícil · Gabarito D
        "enunciado": (
            "Um banco oferece duas modalidades de investimento com montantes dados por "
            "M_A(t) = 5.000 × 1,15^t e M_B(t) = 6.000 × 1,10^t, onde t é o tempo em "
            "anos. Inicialmente M_B > M_A, mas a taxa maior de A fará com que ele "
            "supere B em algum momento. "
            "Dados: 1,15⁴ ≈ 1,749; 1,10⁴ ≈ 1,464; 1,15⁵ ≈ 2,011; 1,10⁵ ≈ 1,611."
        ),
        "pergunta": "A partir de qual ano o montante da modalidade A supera o da modalidade B?",
        "alternativas": {
            "A": "a partir do 2º ano",
            "B": "a partir do 3º ano",
            "C": "a partir do 4º ano",
            "D": "a partir do 5º ano",
            "E": "a partir do 6º ano",
        },
        "gabarito": "D",
        "check": lambda: (
            5000 * 1.15 ** 4 < 6000 * 1.10 ** 4
            and 5000 * 1.15 ** 5 > 6000 * 1.10 ** 5
        ),
        "figura": None,
        "dificuldade": "dificil",
        "topico": "funcao_exponencial",
    },

    {   # Q40 · Exponencial · Difícil · Gabarito E
        "enunciado": (
            "Um estudo climático registrou que a concentração de um gás estufa na "
            "atmosfera era de 370 ppm (partes por milhão) no ano 2000 e crescia à "
            "taxa exponencial de 0,5% ao ano. Um cientista utilizou o modelo "
            "C(t) = 370 × (1,005)^t para projetar concentrações futuras. "
            "Dado: (1,005)²⁰ ≈ 1,105."
        ),
        "pergunta": "Qual é a concentração projetada para o ano 2020, em ppm?",
        "alternativas": {
            "A": "388,5 ppm",
            "B": "393,2 ppm",
            "C": "399,6 ppm",
            "D": "404,1 ppm",
            "E": "408,9 ppm",
        },
        "gabarito": "E",
        "check": lambda: abs(370 * 1.105 - 408.85) < 0.1,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "funcao_exponencial",
    },

]
