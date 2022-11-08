from Test.main import *
from tkinter import *
#iniciar janela
window = Tk()

#titulo da janela
window.title("Teste Rápido MBTI")

#tamanho da janela
window.geometry("400x400")

#label: pedaço de texto a ser apresentado (entre parenteses selecione a janela base do label)
text_instructions = Label(window, text ="Instruções")

#posição do texto (tipo excel)
text_instructions.grid(column=0, row=0, padx=10, pady=10)

#botão
button = Button(window, text = "Clique aqui", command = results)
button.grid(column=0, row=1, padx=10, pady=10)

#texto vazio / posição
text_questions = Label(window, text = " ")
text_questions.grid(column=0, row=2, padx=10, pady=10)
#texto dinamico: colocar dentro do código sendo a variavel texto aquela que deve ser printada - text_questions["text"] = texto

#manter janela
window.mainloop()
