# lote1.py — Lote 1 · 40 questões
# Tópicos: Porcentagem (18), Razão/Proporção (14), Regra de Três (8)
# Gabarito: A×8  B×8  C×8  D×8  E×8

QUESTOES = [

    # ─────────────────────────────────────────────
    # PORCENTAGEM — 18 questões (Q1 a Q18)
    # ─────────────────────────────────────────────

    {   # Q1 · Porcentagem · Fácil · Gabarito A
        "enunciado": (
            "Uma loja de eletrodomésticos anuncia uma promoção com 25% de desconto "
            "em todos os produtos da linha branca. Joana deseja comprar um micro-ondas "
            "que, antes da promoção, estava etiquetado a R$ 480,00."
        ),
        "pergunta": "Qual é o valor que Joana pagará pelo micro-ondas durante a promoção?",
        "alternativas": {
            "A": "R$ 360,00",
            "B": "R$ 380,00",
            "C": "R$ 400,00",
            "D": "R$ 420,00",
            "E": "R$ 440,00",
        },
        "gabarito": "A",
        "check": lambda: 480 * 0.75 == 360,
        "figura": None,
        "dificuldade": "facil",
        "topico": "porcentagem",
    },

    {   # Q2 · Porcentagem · Fácil · Gabarito B
        "enunciado": (
            "Em uma eleição para o grêmio estudantil de uma escola pública, foram "
            "registrados 520 votos válidos. A candidata Mariana obteve 156 desses votos, "
            "enquanto os demais foram distribuídos entre os outros candidatos."
        ),
        "pergunta": "Qual foi o percentual de votos recebidos por Mariana?",
        "alternativas": {
            "A": "25%",
            "B": "30%",
            "C": "35%",
            "D": "40%",
            "E": "45%",
        },
        "gabarito": "B",
        "check": lambda: (156 / 520) * 100 == 30,
        "figura": None,
        "dificuldade": "facil",
        "topico": "porcentagem",
    },

    {   # Q3 · Porcentagem · Fácil · Gabarito C
        "enunciado": (
            "Uma empresa de logística contratou 80 candidatos para participar de um "
            "treinamento obrigatório de segurança no trabalho. Ao final do curso, todos "
            "realizaram uma avaliação prática e teórica. Dos 80 participantes, 68 foram "
            "aprovados e receberam a certificação."
        ),
        "pergunta": "Qual é o percentual de aprovação no treinamento?",
        "alternativas": {
            "A": "78%",
            "B": "80%",
            "C": "85%",
            "D": "88%",
            "E": "90%",
        },
        "gabarito": "C",
        "check": lambda: (68 / 80) * 100 == 85,
        "figura": None,
        "dificuldade": "facil",
        "topico": "porcentagem",
    },

    {   # Q4 · Porcentagem · Médio · Gabarito D
        "enunciado": (
            "Uma concessionária oferece 10% de desconto sobre o preço de tabela para "
            "pagamento à vista e, adicionalmente, mais 5% de desconto sobre o valor já "
            "reduzido para clientes com cadastro ativo no programa de fidelidade. Lucas "
            "possui cadastro ativo e pretende pagar à vista por um veículo cujo preço de "
            "tabela é R$ 62.000,00."
        ),
        "pergunta": "Qual é o preço final que Lucas pagará pelo veículo?",
        "alternativas": {
            "A": "R$ 51.460,00",
            "B": "R$ 52.700,00",
            "C": "R$ 52.890,00",
            "D": "R$ 53.010,00",
            "E": "R$ 53.200,00",
        },
        "gabarito": "D",
        "check": lambda: abs(62000 * 0.90 * 0.95 - 53010) < 0.01,
        "figura": None,
        "dificuldade": "media",
        "topico": "porcentagem",
    },

    {   # Q5 · Porcentagem · Médio · Gabarito E
        "enunciado": (
            "Um servidor público recebeu um reajuste salarial de 12% em janeiro. Em "
            "outubro do mesmo ano, em razão de um corte orçamentário, seu salário foi "
            "reduzido em 8% sobre o valor então vigente. O salário inicial, antes de "
            "qualquer alteração, era de R$ 3.500,00."
        ),
        "pergunta": "Qual é o salário do servidor após as duas alterações?",
        "alternativas": {
            "A": "R$ 3.500,00",
            "B": "R$ 3.528,00",
            "C": "R$ 3.556,00",
            "D": "R$ 3.578,40",
            "E": "R$ 3.606,40",
        },
        "gabarito": "E",
        "check": lambda: abs(3500 * 1.12 * 0.92 - 3606.40) < 0.01,
        "figura": None,
        "dificuldade": "media",
        "topico": "porcentagem",
    },

    {   # Q6 · Porcentagem · Médio · Gabarito A
        "enunciado": (
            "Durante uma liquidação de fim de ano, uma loja de eletrônicos colocou "
            "uma televisão em promoção com 30% de desconto. O preço promocional exibido "
            "na etiqueta era de R$ 1.169,00. Um cliente, interessado em saber o histórico "
            "de preço, deseja descobrir quanto custava a televisão antes do desconto."
        ),
        "pergunta": "Qual era o preço original da televisão antes do desconto?",
        "alternativas": {
            "A": "R$ 1.670,00",
            "B": "R$ 1.690,00",
            "C": "R$ 1.710,00",
            "D": "R$ 1.730,00",
            "E": "R$ 1.750,00",
        },
        "gabarito": "A",
        "check": lambda: abs(1169 / 0.70 - 1670) < 0.01,
        "figura": None,
        "dificuldade": "media",
        "topico": "porcentagem",
    },

    {   # Q7 · Porcentagem · Médio · Gabarito B
        "enunciado": (
            "De acordo com dados do Censo Demográfico 2022 publicados pelo IBGE, um "
            "município do interior registrou 45.000 domicílios, dos quais 12,4% não "
            "tinham acesso à rede geral de abastecimento de água e dependiam de poços, "
            "cisternas ou outras fontes alternativas."
        ),
        "pergunta": "Quantos domicílios do município não tinham acesso à rede de abastecimento de água?",
        "alternativas": {
            "A": "5.400",
            "B": "5.580",
            "C": "5.760",
            "D": "5.940",
            "E": "6.120",
        },
        "gabarito": "B",
        "check": lambda: abs(45000 * 0.124 - 5580) < 0.01,
        "figura": None,
        "dificuldade": "media",
        "topico": "porcentagem",
    },

    {   # Q8 · Porcentagem · Médio · Gabarito C
        "enunciado": (
            "Um produto importado custa US$ 350,00 no exterior. Ao ser importado para "
            "o Brasil, incidem tributos aduaneiros que totalizam 60% sobre o valor de "
            "compra em dólares. Na data da importação, a cotação oficial do dólar era "
            "de R$ 5,20."
        ),
        "pergunta": "Qual é o preço final do produto no Brasil, em reais, após a incidência dos tributos?",
        "alternativas": {
            "A": "R$ 2.548,00",
            "B": "R$ 2.730,00",
            "C": "R$ 2.912,00",
            "D": "R$ 3.094,00",
            "E": "R$ 3.276,00",
        },
        "gabarito": "C",
        "check": lambda: abs(350 * 5.20 * 1.60 - 2912) < 0.01,
        "figura": None,
        "dificuldade": "media",
        "topico": "porcentagem",
    },

    {   # Q9 · Porcentagem · Médio · Gabarito D
        "enunciado": (
            "Duas empresas do setor varejista divulgaram seus resultados anuais. A "
            "empresa Alpha faturou R$ 2.400.000,00 em 2022 e registrou crescimento de "
            "15% em 2023. A empresa Beta faturou R$ 3.200.000,00 em 2022 e registrou "
            "crescimento de 10% em 2023."
        ),
        "pergunta": "Qual é a diferença, em reais, entre o faturamento de 2023 das duas empresas?",
        "alternativas": {
            "A": "R$ 560.000,00",
            "B": "R$ 620.000,00",
            "C": "R$ 700.000,00",
            "D": "R$ 760.000,00",
            "E": "R$ 820.000,00",
        },
        "gabarito": "D",
        "check": lambda: abs(3200000 * 1.10 - 2400000 * 1.15 - 760000) < 0.01,
        "figura": None,
        "dificuldade": "media",
        "topico": "porcentagem",
    },

    {   # Q10 · Porcentagem · Médio · Gabarito E
        "enunciado": (
            "Em uma turma de 60 alunos do ensino médio, 40% são meninas. A professora "
            "de educação física informou que, das meninas da turma, 75% participam da "
            "equipe de vôlei da escola e representam o colégio em competições municipais."
        ),
        "pergunta": "Quantas meninas da turma participam da equipe de vôlei da escola?",
        "alternativas": {
            "A": "12",
            "B": "14",
            "C": "15",
            "D": "16",
            "E": "18",
        },
        "gabarito": "E",
        "check": lambda: 60 * 0.40 * 0.75 == 18,
        "figura": None,
        "dificuldade": "media",
        "topico": "porcentagem",
    },

    {   # Q11 · Porcentagem · Difícil · Gabarito A
        "enunciado": (
            "Uma rede varejista de eletrônicos adota a seguinte política de "
            "precificação: sobre o preço de custo de cada produto, aplica-se um "
            "acréscimo de 40% para cobrir despesas operacionais (frete, armazenagem e "
            "administração); sobre o valor obtido, aplica-se uma margem de lucro "
            "líquido de 25%. Esse é o preço de venda padrão ao consumidor.\n\n"
            "Em campanhas promocionais sazonais, a rede concede um desconto adicional "
            "de 15% sobre o preço de venda padrão para clientes que pagarem à vista. "
            "Carlos identificou um notebook cujo preço de custo para a loja é de "
            "R$ 2.800,00 e aproveitará a campanha, pagando à vista."
        ),
        "pergunta": "Qual é o valor que Carlos pagará pelo notebook durante a promoção?",
        "alternativas": {
            "A": "R$ 4.165,00",
            "B": "R$ 4.235,00",
            "C": "R$ 4.305,00",
            "D": "R$ 4.375,00",
            "E": "R$ 4.445,00",
        },
        "gabarito": "A",
        "check": lambda: abs(2800 * 1.40 * 1.25 * 0.85 - 4165) < 0.01,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "porcentagem",
    },

    {   # Q12 · Porcentagem · Difícil · Gabarito B
        "enunciado": (
            "Dois investidores aplicaram capital em fundos distintos de uma corretora "
            "durante o mesmo período de 2 anos. O investidor Alberto aplicou "
            "R$ 15.000,00 em um fundo de renda variável que rendeu 18% ao final do "
            "1º ano e sofreu uma desvalorização de 8% ao longo do 2º ano. A investidora "
            "Beatriz aplicou R$ 12.000,00 em um fundo de renda fixa que rendeu 12% ao "
            "final do 1º ano e mais 10% ao final do 2º ano, sobre os valores acumulados "
            "em cada período."
        ),
        "pergunta": "Qual é a diferença, em reais, entre os saldos finais de Alberto e Beatriz ao fim dos 2 anos?",
        "alternativas": {
            "A": "R$ 1.200,00",
            "B": "R$ 1.500,00",
            "C": "R$ 1.800,00",
            "D": "R$ 2.100,00",
            "E": "R$ 2.400,00",
        },
        "gabarito": "B",
        "check": lambda: abs(
            15000 * 1.18 * 0.92 - 12000 * 1.12 * 1.10 - 1500
        ) < 0.01,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "porcentagem",
    },

    {   # Q13 · Porcentagem · Difícil · Gabarito C
        "enunciado": (
            "Duas lojas de materiais esportivos vendem o mesmo modelo de bicicleta, "
            "que tem preço de tabela de R$ 2.000,00 nas duas lojas. A Loja A anuncia "
            "\"desconto de 10% + mais 10%\", ou seja, aplica 10% de desconto e, sobre "
            "o preço já reduzido, aplica novamente 10%. A Loja B anuncia \"20% de "
            "desconto direto\" sobre o preço de tabela.\n\n"
            "Um consumidor desconfiado resolveu calcular os preços finais de cada loja "
            "antes de decidir onde comprar."
        ),
        "pergunta": "Qual é a diferença, em reais, entre os preços finais das duas lojas?",
        "alternativas": {
            "A": "R$ 0,00",
            "B": "R$ 10,00",
            "C": "R$ 20,00",
            "D": "R$ 40,00",
            "E": "R$ 80,00",
        },
        "gabarito": "C",
        "check": lambda: abs(
            2000 * 0.90 * 0.90 - 2000 * 0.80 - 20
        ) < 0.01,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "porcentagem",
    },

    {   # Q14 · Porcentagem · Difícil · Gabarito D
        "enunciado": (
            "Uma empresa de tecnologia concedeu reajustes anuais consecutivos a seus "
            "funcionários ao longo de três anos: 10% no 1º ano, 8% no 2º ano e 5% no "
            "3º ano. Cada reajuste foi calculado sobre o salário vigente no momento de "
            "sua aplicação. A analista Fernanda ingressou na empresa recebendo "
            "R$ 5.000,00 mensais e permaneceu na empresa durante todo esse período sem "
            "mudança de cargo."
        ),
        "pergunta": "Qual é o salário atual de Fernanda após os três reajustes consecutivos?",
        "alternativas": {
            "A": "R$ 6.047,00",
            "B": "R$ 6.137,00",
            "C": "R$ 6.187,00",
            "D": "R$ 6.237,00",
            "E": "R$ 6.287,00",
        },
        "gabarito": "D",
        "check": lambda: abs(5000 * 1.10 * 1.08 * 1.05 - 6237) < 0.01,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "porcentagem",
    },

    {   # Q15 · Porcentagem · Difícil · Gabarito E
        "enunciado": (
            "De acordo com censos demográficos, a população de um município do "
            "interior paulista passou por crescimento percentual em três períodos "
            "sucessivos: cresceu 12% entre os anos de 2000 e 2010, cresceu 8% entre "
            "2010 e 2020 e, segundo projeção do IBGE, deverá crescer mais 5% entre "
            "2020 e 2030. O último censo realizado em 2000 registrou 250.000 habitantes "
            "nesse município."
        ),
        "pergunta": "Qual é a projeção de habitantes para esse município no ano de 2030?",
        "alternativas": {
            "A": "311.760",
            "B": "313.600",
            "C": "315.200",
            "D": "316.800",
            "E": "317.520",
        },
        "gabarito": "E",
        "check": lambda: abs(250000 * 1.12 * 1.08 * 1.05 - 317520) < 0.01,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "porcentagem",
    },

    {   # Q16 · Porcentagem · Difícil · Gabarito A
        "enunciado": (
            "Uma cooperativa agrícola do Mato Grosso produziu, em 2023, 15.000 "
            "toneladas de soja. A destinação da produção foi a seguinte: 35% foram "
            "exportadas, 28% foram vendidas à indústria alimentícia nacional, 22% foram "
            "destinadas à produção de rações animais e o restante foi mantido como "
            "reserva estratégica da própria cooperativa, sem gerar receita de venda.\n\n"
            "Os preços médios praticados foram: R$ 185,00 por tonelada para a "
            "exportação, R$ 170,00 por tonelada para a indústria alimentícia e "
            "R$ 155,00 por tonelada para as rações animais."
        ),
        "pergunta": "Qual foi a receita total obtida pela cooperativa com a venda da soja em 2023?",
        "alternativas": {
            "A": "R$ 2.196.750,00",
            "B": "R$ 2.254.500,00",
            "C": "R$ 2.312.250,00",
            "D": "R$ 2.370.000,00",
            "E": "R$ 2.550.000,00",
        },
        "gabarito": "A",
        "check": lambda: abs(
            15000 * 0.35 * 185 +
            15000 * 0.28 * 170 +
            15000 * 0.22 * 155
            - 2196750
        ) < 0.01,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "porcentagem",
    },

    {   # Q17 · Porcentagem · Difícil · Gabarito B
        "enunciado": (
            "Uma pesquisa de eficiência energética realizada em um shopping center de "
            "grande porte identificou a seguinte distribuição do consumo mensal de "
            "energia elétrica: iluminação 38%, ar-condicionado 31%, elevadores e "
            "escadas rolantes 14%, lojas e estabelecimentos 12% e outros 5%. O consumo "
            "total mensal do shopping é de 420.000 kWh, e a tarifa de energia cobrada "
            "pela concessionária é de R$ 0,75 por kWh consumido."
        ),
        "pergunta": "Qual é o custo mensal com ar-condicionado nesse shopping center?",
        "alternativas": {
            "A": "R$ 94.500,00",
            "B": "R$ 97.650,00",
            "C": "R$ 100.800,00",
            "D": "R$ 103.950,00",
            "E": "R$ 107.100,00",
        },
        "gabarito": "B",
        "check": lambda: abs(420000 * 0.31 * 0.75 - 97650) < 0.01,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "porcentagem",
    },

    {   # Q18 · Porcentagem · Difícil · Gabarito C
        "enunciado": (
            "Um varejista de vestuário precisa calcular o preço de etiqueta de uma "
            "peça cujo preço de custo é R$ 120,00. Para isso, aplica, sobre o custo, "
            "três acréscimos sequenciais: 18% referentes a impostos sobre venda, "
            "12% para despesas fixas (aluguel, salários e utilidades) e 8% de margem "
            "de lucro líquido.\n\n"
            "Além disso, o varejista sabe que, durante promoções, concederá 10% de "
            "desconto ao cliente. Para não comprometer a margem de lucro, ele adiciona "
            "previamente um \"buffer\" de 10% sobre o preço já formado, de modo que, "
            "mesmo com o desconto, a margem seja preservada."
        ),
        "pergunta": "Qual será o preço de etiqueta da peça, antes de qualquer desconto ao cliente?",
        "alternativas": {
            "A": "R$ 178,90",
            "B": "R$ 180,00",
            "C": "R$ 182,16",
            "D": "R$ 184,32",
            "E": "R$ 186,48",
        },
        "gabarito": "C",
        "check": lambda: abs(120 * 1.38 * 1.10 - 182.16) < 0.01,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "porcentagem",
    },

    # ─────────────────────────────────────────────
    # RAZÃO E PROPORÇÃO — 14 questões (Q19 a Q32)
    # ─────────────────────────────────────────────

    {   # Q19 · Razão/Proporção · Fácil · Gabarito D
        "enunciado": (
            "Uma escola municipal adota a relação de um professor para cada 25 alunos "
            "como critério mínimo de atendimento pedagógico. A escola possui 875 alunos "
            "matriculados no ensino fundamental e está adequada exatamente a esse critério."
        ),
        "pergunta": "Quantos professores essa escola possui?",
        "alternativas": {
            "A": "30",
            "B": "32",
            "C": "33",
            "D": "35",
            "E": "38",
        },
        "gabarito": "D",
        "check": lambda: 875 / 25 == 35,
        "figura": None,
        "dificuldade": "facil",
        "topico": "razao_proporcao",
    },

    {   # Q20 · Razão/Proporção · Fácil · Gabarito E
        "enunciado": (
            "Uma receita de bolo de cenoura foi elaborada para servir 12 pessoas e "
            "utiliza 480 g de farinha de trigo. Cleide quer preparar o mesmo bolo para "
            "uma confraternização com 20 convidados, mantendo as mesmas proporções da "
            "receita original."
        ),
        "pergunta": "Quantos gramas de farinha de trigo Cleide precisará usar?",
        "alternativas": {
            "A": "660 g",
            "B": "700 g",
            "C": "740 g",
            "D": "760 g",
            "E": "800 g",
        },
        "gabarito": "E",
        "check": lambda: (480 / 12) * 20 == 800,
        "figura": None,
        "dificuldade": "facil",
        "topico": "razao_proporcao",
    },

    {   # Q21 · Razão/Proporção · Fácil · Gabarito A
        "enunciado": (
            "Um automóvel flex percorre 360 km com 30 litros de combustível, "
            "mantendo uma média constante de consumo em rodovia. O proprietário "
            "planeja fazer uma viagem de 480 km pelo mesmo tipo de estrada e com "
            "o mesmo padrão de condução."
        ),
        "pergunta": "Quantos litros de combustível serão necessários para realizar essa viagem?",
        "alternativas": {
            "A": "40 litros",
            "B": "42 litros",
            "C": "44 litros",
            "D": "46 litros",
            "E": "48 litros",
        },
        "gabarito": "A",
        "check": lambda: (30 / 360) * 480 == 40,
        "figura": None,
        "dificuldade": "facil",
        "topico": "razao_proporcao",
    },

    {   # Q22 · Razão/Proporção · Médio · Gabarito B
        "enunciado": (
            "Uma fundição especializada produz componentes a partir de uma liga "
            "metálica composta exclusivamente por cobre e zinco na proporção de 3:2 "
            "em massa. O gerente de produção recebeu um pedido para fabricar 850 kg "
            "dessa liga para um cliente da indústria automotiva."
        ),
        "pergunta": "Quantos quilogramas de cobre serão necessários para atender ao pedido?",
        "alternativas": {
            "A": "500 kg",
            "B": "510 kg",
            "C": "520 kg",
            "D": "530 kg",
            "E": "540 kg",
        },
        "gabarito": "B",
        "check": lambda: 850 * 3 / 5 == 510,
        "figura": None,
        "dificuldade": "media",
        "topico": "razao_proporcao",
    },

    {   # Q23 · Razão/Proporção · Médio · Gabarito C
        "enunciado": (
            "O mapa digital de uma cidade foi impresso em papel na escala 1:25.000 "
            "para distribuição em postos de informação turística. No mapa impresso, "
            "a distância medida com régua entre a prefeitura municipal e o hospital "
            "regional é de 6,4 cm."
        ),
        "pergunta": "Qual é a distância real, em quilômetros, entre a prefeitura e o hospital?",
        "alternativas": {
            "A": "1,2 km",
            "B": "1,4 km",
            "C": "1,6 km",
            "D": "1,8 km",
            "E": "2,0 km",
        },
        "gabarito": "C",
        "check": lambda: 6.4 * 25000 / 100000 == 1.6,
        "figura": None,
        "dificuldade": "media",
        "topico": "razao_proporcao",
    },

    {   # Q24 · Razão/Proporção · Médio · Gabarito D
        "enunciado": (
            "Uma fábrica de parafusos opera com 4 máquinas idênticas em plena "
            "capacidade, produzindo juntas 1.200 parafusos por hora. Após uma revisão "
            "preventiva programada, apenas 3 máquinas estarão disponíveis para operar "
            "durante um período. O supervisor precisa saber em quanto tempo produzirá "
            "um lote de 2.700 parafusos com esse contingente reduzido."
        ),
        "pergunta": "Quantas horas serão necessárias para produzir 2.700 parafusos com 3 máquinas?",
        "alternativas": {
            "A": "2,0 horas",
            "B": "2,5 horas",
            "C": "2,75 horas",
            "D": "3,0 horas",
            "E": "3,5 horas",
        },
        "gabarito": "D",
        "check": lambda: 2700 / (1200 / 4 * 3) == 3,
        "figura": None,
        "dificuldade": "media",
        "topico": "razao_proporcao",
    },

    {   # Q25 · Razão/Proporção · Médio · Gabarito E
        "enunciado": (
            "Em uma escola técnica estadual, a proporção entre o número de alunos do "
            "turno matutino e o do vespertino é de 5:3. No vespertino, estão "
            "matriculados 216 alunos. A diretora precisa informar ao sistema estadual "
            "o total de alunos da escola."
        ),
        "pergunta": "Qual é o total de alunos matriculados na escola?",
        "alternativas": {
            "A": "516",
            "B": "536",
            "C": "546",
            "D": "556",
            "E": "576",
        },
        "gabarito": "E",
        "check": lambda: 216 * 5 / 3 + 216 == 576,
        "figura": None,
        "dificuldade": "media",
        "topico": "razao_proporcao",
    },

    {   # Q26 · Razão/Proporção · Médio · Gabarito A
        "enunciado": (
            "Uma pesquisa realizada em um bairro da periferia de uma capital revelou "
            "que, a cada 7 domicílios, 4 têm acesso à internet de banda larga por "
            "fibra óptica ou cabo, enquanto 3 não têm esse acesso. O bairro possui "
            "2.058 domicílios cadastrados no registro municipal."
        ),
        "pergunta": "Quantos domicílios do bairro não têm acesso à internet de banda larga?",
        "alternativas": {
            "A": "882",
            "B": "896",
            "C": "910",
            "D": "924",
            "E": "938",
        },
        "gabarito": "A",
        "check": lambda: 2058 * 3 / 7 == 882,
        "figura": None,
        "dificuldade": "media",
        "topico": "razao_proporcao",
    },

    {   # Q27 · Razão/Proporção · Médio · Gabarito B
        "enunciado": (
            "Para preparar uma solução desinfetante hospitalar de uso seguro, o "
            "protocolo técnico determina que se misture água destilada e um concentrado "
            "bactericida na proporção volumétrica de 9:1. Um técnico de enfermagem "
            "precisa preparar 5 litros dessa solução para abastecer os dispensadores "
            "de um corredor cirúrgico."
        ),
        "pergunta": "Quantos mililitros do concentrado bactericida serão necessários para preparar os 5 litros de solução?",
        "alternativas": {
            "A": "450 mL",
            "B": "500 mL",
            "C": "550 mL",
            "D": "600 mL",
            "E": "650 mL",
        },
        "gabarito": "B",
        "check": lambda: 5000 * 1 / 10 == 500,
        "figura": None,
        "dificuldade": "media",
        "topico": "razao_proporcao",
    },

    {   # Q28 · Razão/Proporção · Médio · Gabarito C
        "enunciado": (
            "Um canteiro de obras de pavimentação emprega 18 pedreiros que trabalham "
            "8 horas por dia e concluem uma determinada etapa da obra em 12 dias. O "
            "engenheiro responsável recebeu ordem do cliente para antecipar a entrega "
            "dessa etapa, que deverá ser concluída em apenas 8 dias, mantendo a mesma "
            "jornada de 8 horas diárias."
        ),
        "pergunta": "Quantos pedreiros serão necessários para cumprir o novo prazo?",
        "alternativas": {
            "A": "24",
            "B": "25",
            "C": "27",
            "D": "29",
            "E": "30",
        },
        "gabarito": "C",
        "check": lambda: 18 * 12 / 8 == 27,
        "figura": None,
        "dificuldade": "media",
        "topico": "razao_proporcao",
    },

    {   # Q29 · Razão/Proporção · Difícil · Gabarito D
        "enunciado": (
            "Um empresário deixou em testamento um patrimônio total avaliado em "
            "R$ 840.000,00 para ser dividido entre seus três filhos — Ana, Bruno e "
            "Carlos — em proporção direta ao número de anos que cada um contribuiu "
            "ativamente para os negócios da família. Segundo registros contábeis "
            "reconhecidos em cartório, Ana trabalhou na empresa por 7 anos, Bruno por "
            "5 anos e Carlos por 3 anos. O inventário seguirá exatamente essa "
            "proporcionalidade."
        ),
        "pergunta": "Qual é a diferença, em reais, entre a herança de Ana e a herança de Carlos?",
        "alternativas": {
            "A": "R$ 168.000,00",
            "B": "R$ 196.000,00",
            "C": "R$ 210.000,00",
            "D": "R$ 224.000,00",
            "E": "R$ 238.000,00",
        },
        "gabarito": "D",
        "check": lambda: abs(
            840000 * 7 / 15 - 840000 * 3 / 15 - 224000
        ) < 0.01,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "razao_proporcao",
    },

    {   # Q30 · Razão/Proporção · Difícil · Gabarito E
        "enunciado": (
            "Um motorista de aplicativo de transporte registra, em média, 280 km "
            "percorridos por semana. Desse total, 35% ocorrem no período noturno "
            "(entre 22h e 6h) e o restante no período diurno. A plataforma pratica "
            "tarifa de R$ 2,40 por km nas corridas diurnas e R$ 3,20 por km nas "
            "corridas noturnas, conforme regulamentação municipal vigente."
        ),
        "pergunta": "Qual é o faturamento semanal bruto desse motorista?",
        "alternativas": {
            "A": "R$ 693,60",
            "B": "R$ 712,80",
            "C": "R$ 729,60",
            "D": "R$ 741,20",
            "E": "R$ 750,40",
        },
        "gabarito": "E",
        "check": lambda: abs(
            280 * 0.65 * 2.40 + 280 * 0.35 * 3.20 - 750.40
        ) < 0.01,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "razao_proporcao",
    },

    {   # Q31 · Razão/Proporção · Difícil · Gabarito A
        "enunciado": (
            "Um tanque de armazenamento de combustível de um posto contém 3.000 litros "
            "de uma mistura de gasolina e etanol na proporção de 3:1 em volume (ou seja, "
            "para cada 3 litros de gasolina há 1 litro de etanol). O proprietário do "
            "posto recebeu orientação da distribuidora para ajustar a mistura e atingir "
            "a nova proporção de 2:1 (gasolina:etanol), adicionando apenas etanol puro "
            "ao tanque — sem remover nenhum volume já existente."
        ),
        "pergunta": "Quantos litros de etanol puro devem ser adicionados ao tanque para obter a nova proporção?",
        "alternativas": {
            "A": "375 litros",
            "B": "400 litros",
            "C": "425 litros",
            "D": "450 litros",
            "E": "475 litros",
        },
        "gabarito": "A",
        "check": lambda: abs(
            3000 * 3 / 4 / 2 - 3000 * 1 / 4 - 375
        ) < 0.01,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "razao_proporcao",
    },

    {   # Q32 · Razão/Proporção · Difícil · Gabarito B
        "enunciado": (
            "Três sócios fundaram uma empresa e definiram, em contrato social, que os "
            "lucros seriam distribuídos trimestralmente de acordo com o capital "
            "investido por cada um. No 1º semestre, os lucros foram de R$ 480.000,00 "
            "e a proporção de distribuição era de 3:2:1 (Sócio A : Sócio B : Sócio C).\n\n"
            "No 2º semestre, os lucros cresceram 25% em relação ao 1º semestre e os "
            "sócios aprovaram em assembleia uma nova distribuição igualitária (1:1:1), "
            "pois o Sócio B e o Sócio C haviam aportado capital adicional equivalente "
            "ao do Sócio A."
        ),
        "pergunta": "Qual é a diferença, em reais, entre o que o Sócio A recebeu no 1º e no 2º semestre?",
        "alternativas": {
            "A": "R$ 30.000,00",
            "B": "R$ 40.000,00",
            "C": "R$ 50.000,00",
            "D": "R$ 60.000,00",
            "E": "R$ 70.000,00",
        },
        "gabarito": "B",
        "check": lambda: abs(
            480000 * 3 / 6 - 480000 * 1.25 / 3 - 40000
        ) < 0.01,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "razao_proporcao",
    },

    # ─────────────────────────────────────────────
    # REGRA DE TRÊS — 8 questões (Q33 a Q40)
    # ─────────────────────────────────────────────

    {   # Q33 · Regra de Três · Fácil · Gabarito C
        "enunciado": (
            "Em uma padaria do interior de Minas Gerais, o pão de queijo é vendido "
            "em embalagens individuais a R$ 1,50 cada. Uma cliente deseja comprar "
            "12 unidades para servir em um café da manhã em família no fim de semana."
        ),
        "pergunta": "Qual é o valor total que a cliente pagará pelos 12 pães de queijo?",
        "alternativas": {
            "A": "R$ 15,50",
            "B": "R$ 16,50",
            "C": "R$ 18,00",
            "D": "R$ 19,50",
            "E": "R$ 21,00",
        },
        "gabarito": "C",
        "check": lambda: 1.50 * 12 == 18.00,
        "figura": None,
        "dificuldade": "facil",
        "topico": "regra_de_tres",
    },

    {   # Q34 · Regra de Três · Fácil · Gabarito D
        "enunciado": (
            "Em uma fábrica de componentes plásticos, 3 operários montam, juntos, "
            "18 peças por turno de 6 horas, mantendo produtividade constante e "
            "uniforme entre eles. O gerente de produção deseja saber qual seria a "
            "produção do mesmo turno se escalasse 5 operários com a mesma "
            "produtividade individual."
        ),
        "pergunta": "Quantas peças 5 operários montarão no mesmo turno de 6 horas?",
        "alternativas": {
            "A": "24",
            "B": "26",
            "C": "28",
            "D": "30",
            "E": "32",
        },
        "gabarito": "D",
        "check": lambda: 18 / 3 * 5 == 30,
        "figura": None,
        "dificuldade": "facil",
        "topico": "regra_de_tres",
    },

    {   # Q35 · Regra de Três · Médio · Gabarito E
        "enunciado": (
            "Um aquário retangular de grande porte tem capacidade total de 180 litros. "
            "Sua torneira de abastecimento enche-o a uma taxa constante de 12 litros "
            "por minuto. O proprietário iniciou o enchimento, mas precisou interromper "
            "o processo por razões técnicas. Quando retomou, o aquário já continha "
            "45 litros."
        ),
        "pergunta": "Quantos minutos serão necessários para concluir o enchimento do aquário?",
        "alternativas": {
            "A": "10,25 min",
            "B": "10,50 min",
            "C": "10,75 min",
            "D": "11,00 min",
            "E": "11,25 min",
        },
        "gabarito": "E",
        "check": lambda: (180 - 45) / 12 == 11.25,
        "figura": None,
        "dificuldade": "media",
        "topico": "regra_de_tres",
    },

    {   # Q36 · Regra de Três · Médio · Gabarito A
        "enunciado": (
            "Um caminhão de carga percorre, em média, 240 km a cada 48 litros de "
            "diesel consumido, mantendo velocidade constante em rodovia. O motorista "
            "recebeu uma ordem de serviço para fazer uma entrega em uma cidade cuja "
            "distância pelo trajeto de rodovia é de 310 km a partir do depósito."
        ),
        "pergunta": "Quantos litros de diesel serão necessários para percorrer os 310 km até a cidade de destino?",
        "alternativas": {
            "A": "62 litros",
            "B": "64 litros",
            "C": "66 litros",
            "D": "68 litros",
            "E": "70 litros",
        },
        "gabarito": "A",
        "check": lambda: 48 / 240 * 310 == 62,
        "figura": None,
        "dificuldade": "media",
        "topico": "regra_de_tres",
    },

    {   # Q37 · Regra de Três · Médio · Gabarito B
        "enunciado": (
            "Uma gráfica industrial possui uma impressora de alta capacidade que "
            "imprime 240 páginas por minuto de forma contínua. Uma editora contratou "
            "a gráfica para imprimir o relatório de sustentabilidade de uma empresa, "
            "que totaliza 8.400 páginas distribuídas em vários volumes."
        ),
        "pergunta": "Em quantos minutos a impressora concluirá a impressão completa do relatório?",
        "alternativas": {
            "A": "30 minutos",
            "B": "35 minutos",
            "C": "40 minutos",
            "D": "42 minutos",
            "E": "45 minutos",
        },
        "gabarito": "B",
        "check": lambda: 8400 / 240 == 35,
        "figura": None,
        "dificuldade": "media",
        "topico": "regra_de_tres",
    },

    {   # Q38 · Regra de Três · Difícil · Gabarito C
        "enunciado": (
            "Uma construtora empregou 24 pedreiros que trabalhavam 8 horas por dia "
            "para construir um muro de contenção. Com essa equipe, o muro foi concluído "
            "em 15 dias. A construtora recebeu uma nova encomenda para construir um "
            "muro com exatamente o dobro do volume de material do primeiro, mas o "
            "cliente exige entrega em apenas 10 dias úteis. A jornada diária será "
            "mantida em 8 horas.\n\n"
            "Considerando que a produtividade por pedreiro é constante e que o volume "
            "de trabalho é diretamente proporcional ao número de pedreiros, ao número "
            "de dias e à jornada diária,"
        ),
        "pergunta": "Quantos pedreiros serão necessários para concluir o novo muro no prazo estabelecido?",
        "alternativas": {
            "A": "56",
            "B": "64",
            "C": "72",
            "D": "80",
            "E": "88",
        },
        "gabarito": "C",
        "check": lambda: 24 * 15 * 8 * 2 / (10 * 8) == 72,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "regra_de_tres",
    },

    {   # Q39 · Regra de Três · Difícil · Gabarito D
        "enunciado": (
            "Uma usina de tratamento de água opera normalmente com 6 bombas de "
            "recalque idênticas, que juntas tratam 1.800.000 litros por dia em uma "
            "jornada de 20 horas diárias. Em razão de uma manutenção preventiva "
            "emergencial, 2 bombas ficaram inativas durante 3 dias consecutivos. "
            "Nesse período, as 4 bombas restantes operaram apenas 15 horas por dia "
            "em vez das 20 horas habituais, por determinação do operador.\n\n"
            "A prefeitura precisa informar à população o volume total de déficit "
            "acumulado nesse período de manutenção em relação à capacidade de "
            "tratamento normal."
        ),
        "pergunta": "Qual foi o déficit total de tratamento de água durante os 3 dias de manutenção, em litros?",
        "alternativas": {
            "A": "1.800.000 litros",
            "B": "2.160.000 litros",
            "C": "2.520.000 litros",
            "D": "2.700.000 litros",
            "E": "2.880.000 litros",
        },
        "gabarito": "D",
        "check": lambda: abs(
            3 * 1800000 - (1800000 / (6 * 20)) * 4 * 15 * 3 - 2700000
        ) < 0.01,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "regra_de_tres",
    },

    {   # Q40 · Regra de Três · Difícil · Gabarito E
        "enunciado": (
            "A Prefeitura de uma cidade contratou uma empresa de engenharia elétrica "
            "para instalar a iluminação pública de uma avenida. O projeto original "
            "previa 8 equipes de trabalho — cada uma composta por 5 eletricistas — "
            "trabalhando 9 horas por dia, com prazo de 12 dias para iluminar 4 km "
            "da avenida.\n\n"
            "Após uma revisão técnica municipal, a obra foi ampliada: a avenida a "
            "ser iluminada passou de 4 km para 6 km, e o prazo foi reduzido de 12 "
            "para 9 dias para não conflitar com o cronograma de outras obras. A "
            "jornada diária de 9 horas foi mantida. O empreiteiro precisa calcular "
            "quantas equipes de 5 eletricistas deverá mobilizar para cumprir o novo "
            "cronograma, sabendo que a produtividade por equipe é constante."
        ),
        "pergunta": "Quantas equipes de 5 eletricistas serão necessárias para cumprir o novo cronograma?",
        "alternativas": {
            "A": "10 equipes",
            "B": "12 equipes",
            "C": "13 equipes",
            "D": "14 equipes",
            "E": "16 equipes",
        },
        "gabarito": "E",
        "check": lambda: (8 * 12 * 9 / 4) * 6 / (9 * 9) == 16,
        "figura": None,
        "dificuldade": "dificil",
        "topico": "regra_de_tres",
    },

]
