import csv

with open("messages.csv", "r", encoding="utf-8") as mensagem:
    arquivo_msg_csv = csv.reader(mensagem, delimiter=';')

    cabecalho_msg = next(arquivo_msg_csv)
    instruction = next(arquivo_msg_csv)
    question_a = next(arquivo_msg_csv)
    question_b = next(arquivo_msg_csv)
    question_c = next(arquivo_msg_csv)
    question_d = next(arquivo_msg_csv)

with open("results.csv", "r", encoding="utf-8") as resposta:
    arquivo_rspt_csv = csv.reader(resposta, delimiter=";")

    cabecalho_results = next(arquivo_rspt_csv)
    ISTJ = next(arquivo_rspt_csv)
    ISFJ = next(arquivo_rspt_csv)
    INFJ = next(arquivo_rspt_csv)
    INTJ = next(arquivo_rspt_csv)
    ISTP = next(arquivo_rspt_csv)
    ISFP = next(arquivo_rspt_csv)
    INFP = next(arquivo_rspt_csv)
    INTP = next(arquivo_rspt_csv)
    ESTP = next(arquivo_rspt_csv)
    ESFP = next(arquivo_rspt_csv)
    ENFP = next(arquivo_rspt_csv)
    ENTP = next(arquivo_rspt_csv)
    ESTJ = next(arquivo_rspt_csv)
    ESFJ = next(arquivo_rspt_csv)
    ENFJ = next(arquivo_rspt_csv)
    ENTJ = next(arquivo_rspt_csv)
