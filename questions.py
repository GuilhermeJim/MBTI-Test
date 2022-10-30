#Instruções
def instructions():
    inst = "Esta versão simplificada do teste de personalidade Myers-Briggs pode dizer muito sobre você com apenas quatro perguntas fáceis. O teste de personalidade Myers-Briggs normal pode incluir até 93 perguntas para encontrar seu tipo de personalidade. Este teste demorado pode ser extremamente útil para pessoas que estão tentando aprender mais sobre seu tipo de personalidade. No entanto, criamos uma forma mais simples do Indicador de Tipo Myers-Briggs (MBTI), que você pode preencher em apenas quatro perguntas. Cada pergunta tem uma letra correspondente com a qual você usará posteriormente para identificar seu tipo específico de personalidade. Depois de terminar todas as quatro perguntas, você terá um conjunto de quatro letras que indicarão seu tipo de personalidade entre as dezesseis possibilidades abaixo. As descrições abaixo vêm diretamente da Fundação Myers & Briggs ."
    print(inst)

#Questões
def question_a():
    a = "\nPergunta 1: Depois de uma semana extremamente difícil e longa de trabalho, o fim de semana finalmente chegou, como você vai aproveitar o seu fim de semana?\nTecle E para: Extroversão - Você decide que quer ir ao clube, a uma festa ou a qualquer outro lugar que outras pessoas estejam. Pode ser para os cinemas ou uma noite na cidade de qualquer maneira que você esteja saindo. \nTecle I para: Introversão - Você leva o fato de ser uma pessoa caseira a um nível totalmente novo. Você provavelmente se esconde e assiste Netflix, lê seu livro favorito ou faz qualquer outra coisa que o ajude a se recuperar para a próxima semana na solidão."
    print(a)
    answer_a = input().upper()
    if answer_a != "E" and answer_a != "I":
        while answer_a != "E" and answer_a != "I":
            del answer_a
            answer_a = input("Por gentileza, use somente as teclas E e I para responder o questionário").upper()
    return answer_a

def question_b():
    b = "\nPergunta 2: Qual dos dois melhor descreve você?\nTecle S para: Sensing -  Apenas coisas que são materiais tangíveis. Se você não pode pegá-lo e segurá-lo, ele não vale muito. Você nunca toma uma decisão sem evidências concretas.\nTecle N para: Intuição - As coisas tangíveis são as menos valiosas para você. Sua própria intuição é mais confiável do que aquilo que seus sentidos poderiam lhe dizer. Você tende a seguir seus instintos."
    print(b)
    answer_b = input().upper()
    if answer_b != "S" and answer_b != "N":
        while answer_b != "S" and answer_b != "N":
            del answer_b
            answer_b = input("Por gentileza, use somente as teclas S e N para responder o questionário").upper()
    return answer_b

def question_c():
    c = "\nPergunta 3: Você recebe uma oferta para o emprego dos seus sonhos. O salário é bem maior e o gerente de lá faz muitas promessas com relação à sua mobilidade ascendente. No entanto, seu trabalho atual se encaixa perfeitamente e compartilha de seus ideais. Também houve sugestões para uma promoção futura. O que você faz?\nTecle T para: Pensando - Sempre existe a chance de que isso seja bom demais para ser verdade. Você toma seu tempo para pesar cuidadosamente suas opções, considerando o que poderia acontecer se as coisas prometidas a você não fossem verdadeiras. Você leva o máximo de tempo para considerar a opção o mais humanamente possível – considerando todos os resultados potenciais.\nTecle F para: Feeling - Você aceitou o emprego no minuto em que ele foi oferecido a você. Quando uma oportunidade como essa surge, você confia no seu instinto e vai atrás dela."
    print(c)
    answer_c = input().upper()
    if answer_c != "T" and answer_c != "F":
        while answer_c != "T" and answer_c != "F":
            del answer_c
            answer_c = input("Por gentileza, use somente as teclas T e F para responder o questionário").upper()
    return answer_c

def question_d():
    d = "\nPergunta 4: Sua melhor amiga vai ter um bebê e você vai dar um chá de bebê para ela em uma semana. Que tipo de arranjos você fez? \nTecle J para: Julgamento - Você está planejando este chá de bebê desde que soube que ela estava grávida. Você escolheu os melhores presentes e enviou convites para todos os amigos dela e até mesmo para alguns de seus colegas de trabalho. Você está dando uma grande festa para seu amigo e passou muito tempo se preparando.\nTecle P para: Percepção - Você sabe que seu amigo não quer nada muito louco. As melhores ocasiões são pequenas, com apenas alguns amigos íntimos. Você vai improvisar quase tudo e isso normalmente funciona muito bem para você. Você provavelmente vai sair para comprar um presente para ela na noite anterior."
    print(d)
    answer_d = input().upper()
    if answer_d != "J" and answer_d != "P":
        while answer_d != "J" and answer_d != "P":
            del answer_d
            answer_d = input("Por gentileza, use somente as teclas J e P para responder o questionário").upper()
    return answer_d

#Processamento e Resultado
def results():
    #Formulando MBTI
    ans_a = question_a()
    ans_b = question_b()
    ans_c = question_c()
    ans_d = question_d()
    ans = ans_a + ans_b + ans_c + ans_d
    print("Seu tipo de personalidade é:" + " " + ans)

    #Criando a Tupla para relacionar 2 listas
    final_ans =[]

    #Criando listas descritivas
    personalities = ["ISTJ","ISFJ","INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP", "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ","ESFJ", "ENFJ", "ENTJ"]
    description = ["Calmo, sério, obtenha sucesso com meticulosidade e confiabilidade. Prático, prático, realista e responsável. Decida logicamente o que deve ser feito e trabalhe para isso de forma constante, independentemente das distrações. Tenha prazer em fazer tudo em ordem e organizado – seu trabalho, sua casa, sua vida. Valorize as tradições e a lealdade.", "Calmo, amigável, responsável e consciencioso. Comprometidos e firmes no cumprimento de suas obrigações. Completo, meticuloso e preciso. Leal, atencioso, observe e lembre-se de detalhes sobre pessoas que são importantes para eles, preocupando-se em como os outros se sentem. Esforce-se para criar um ambiente ordenado e harmonioso no trabalho e em casa.", "Procure significado e conexão em idéias, relacionamentos e posses materiais. Quer entender o que motiva as pessoas e é perspicaz sobre os outros. Consciente e comprometido com os valores da empresa. Desenvolva uma visão clara sobre a melhor forma de servir ao bem comum. Organizado e decisivo na implementação de sua visão.", "Procure significado e conexão em idéias, relacionamentos e posses materiais. Quer entender o que motiva as pessoas e é perspicaz sobre os outros. Consciente e comprometido com os valores da empresa. Desenvolva uma visão clara sobre a melhor forma de servir ao bem comum. Organizado e decisivo na implementação de sua visão.", "Observadores tolerantes e flexíveis, silenciosos até que apareça um problema, então ajam rapidamente para encontrar soluções viáveis. Analise o que faz as coisas funcionarem e obtenha prontamente grandes quantidades de dados para isolar o núcleo dos problemas práticos. Interessado em causa e efeito, organize os fatos usando princípios lógicos, valorize a eficiência.", "Calmo, amigável, sensível e gentil. Aproveite o momento presente, o que está acontecendo ao seu redor. Gostam de ter seu próprio espaço e de trabalhar dentro do seu tempo. Leal e comprometido com seus valores e com as pessoas que são importantes para eles. Não gosto de desentendimentos e conflitos, não force suas opiniões ou valores sobre os outros.", "Idealista, fiel aos seus valores e às pessoas que são importantes para ele. Quer uma vida externa que seja congruente com seus valores. Curioso, rápido para ver as possibilidades, pode ser um catalisador para a implementação de ideias. Procure compreender as pessoas e ajudá-las a realizar seu potencial. Adaptável, flexível e de aceitação, a menos que um valor seja ameaçado.", "Procure desenvolver explicações lógicas para tudo o que lhes interessa. Teórico e abstrato, interessado mais em ideias do que em interação social. Silencioso, contido, flexível e adaptável. Possui habilidade incomum de se concentrar em profundidade para resolver problemas em sua área de interesse. Cético, às vezes crítico, sempre analítico.", "Flexíveis e tolerantes, eles têm uma abordagem pragmática focada em resultados imediatos. Teorias e explicações conceituais os aborrecem – eles querem agir energicamente para resolver o problema. Concentre-se no aqui-e-agora, espontâneo, aproveite cada momento em que eles podem ser ativos com os outros. Desfrute de conforto e estilo materiais. Aprenda melhor fazendo.", "Extrovertido, amigável e receptivo. Amantes exuberantes da vida, das pessoas e dos confortos materiais. Gosto de trabalhar com outras pessoas para fazer as coisas acontecerem. Traga bom senso e uma abordagem realista para o trabalho e torne o trabalho divertido. Flexível e espontâneo, adapta-se prontamente a novas pessoas e ambientes. Aprenda melhor experimentando uma nova habilidade com outras pessoas.", "Calorosamente entusiasmado e imaginativo. Veja a vida cheia de possibilidades. Faça conexões entre eventos e informações muito rapidamente e prossiga com confiança com base nos padrões que eles veem. Deseje muitas afirmações de outras pessoas e dê prontamente apreço e apoio. Espontâneo e flexível, muitas vezes contam com sua habilidade de improvisar e sua fluência verbal.", "Rápido, engenhoso, estimulante, alerta e franco. Engenhoso na resolução de problemas novos e desafiadores. Hábil em gerar possibilidades conceituais e então analisá-las estrategicamente. Bom para ler outras pessoas. Entediado com a rotina, raramente fará a mesma coisa da mesma maneira, apto a se voltar para um novo interesse após o outro.", "Prático, realista, prático. Decisivo, mova-se rapidamente para implementar decisões. Organize projetos e pessoas para fazer as coisas, concentre-se em obter resultados da maneira mais eficiente possível. Cuide dos detalhes da rotina. Tenha um conjunto claro de padrões lógicos, siga-os sistematicamente e queira que outros também o façam. Forte na implementação de seus planos.", "Caloroso, consciencioso e cooperativo. Queira harmonia em seu ambiente, trabalhe com determinação para estabelecê-la. Gosta de trabalhar com outras pessoas para concluir as tarefas com precisão e no prazo. Leal, siga em frente mesmo em questões pequenas. Observe o que os outros precisam em seu dia-a-dia e tente prover. Quer ser apreciado por quem são e pelo que contribuem.", "Caloroso, empático, responsivo e responsável. Altamente sintonizado com as emoções, necessidades e motivações dos outros. Encontre o potencial em todos, queira ajudar os outros a realizarem seu potencial. Podem atuar como catalisadores para o crescimento individual e de grupo. Leal, receptivo a elogios e críticas. Sociável, facilita outros em um grupo e fornece liderança inspiradora.", "Frank, decidido, assume prontamente a liderança. Veja rapidamente procedimentos e políticas ilógicas e ineficientes, desenvolva e implemente sistemas abrangentes para resolver problemas organizacionais. Desfrute de planejamento de longo prazo e definição de metas. Normalmente bem informado, bem lido, gosta de expandir seus conhecimentos e transmiti-los a outras pessoas. Forte na apresentação de suas idéias."]

    #Buscando a personalidade e printando na tela
    for i in range(len(personalities)):
        if ans == personalities[i]:
            tuple = (personalities[i], description[i])
            final_ans.append(tuple)
            print(final_ans)




