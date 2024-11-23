from pathlib import Path
from tkinter import Tk, Canvas, Text, Button, Radiobutton, StringVar
from PIL import Image, ImageTk
import gerador_nomes as tn
import classes_raca as cr
import gerador_historiasIA as gia
import historias as gh

#Variaveis Globais
nomegb = ""
historiagb = ""
genero_var = ""

# Caminho para o diretório de imagens
OUTPUT_PATH = Path(__file__).parent
IMG_PATH = OUTPUT_PATH / "img"

# Função para carregar e redimensionar imagens
def load_and_resize_image(filename, width, height):
    img = Image.open(IMG_PATH / filename)
    return ImageTk.PhotoImage(img.resize((width, height), Image.Resampling.LANCZOS))

# Inicialização da janela
window = Tk()
window.geometry("1200x700")
window.configure(bg="#FFFFFF")
window.title("RPGenerator")

# Canvas principal
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=700,
    width=1200,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Imagem de fundo redimensionada
background_image = load_and_resize_image("castbg.png", 1200, 700)
canvas.create_image(0, 0, anchor="nw", image=background_image)

# Área do Logo
logo_image = load_and_resize_image("logoS.png", 601, 221)  # Tamanho do campo do logo
canvas.create_image(300.0, 14.0, anchor="nw", image=logo_image)

# Área da Imagem de Perfil
#profile_image = load_and_resize_image("guerr.png", 200, 200)
#profile_image1 = load_and_resize_image("iconm.png", 200, 200)
#profile_image2 = load_and_resize_image("iconf.png", 200, 200)  # Tamanho do campo de perfil
#canvas.create_image(980.0, 128.0, anchor="nw", image=profile_image)

#reload Imagem
re_image = load_and_resize_image("reroll.png", 27, 27)

# Campos de entrada de texto para Nome, Classe, Raça, Atributos e História
nome_field = Text(window, height=1, width=30, font=("MarcellusSC Regular", 14))
nome_field.place(x=126, y=239)

classe_field = Text(window, height=1, width=30, font=("MarcellusSC Regular", 14))
classe_field.place(x=126, y=287)

raca_field = Text(window, height=1, width=30, font=("MarcellusSC Regular", 14))
raca_field.place(x=126, y=335)

atributos_field = Text(window, height=4, width=30, font=("MarcellusSC Regular", 14))
atributos_field.place(x=621, y=232)

historia_field = Text(window, height=6, width=35, wrap="word", font=("MarcellusSC Regular", 14))
historia_field.place(x=621, y=335)

# Labels para cada campo
canvas.create_text(51.0, 239.0, anchor="nw", text="Nome:", fill="#FFFFFF", font=("MarcellusSC Regular", 24 * -1))
canvas.create_text(42.0, 287.0, anchor="nw", text="Classe:", fill="#FFFFFF", font=("MarcellusSC Regular", 24 * -1))
canvas.create_text(60.0, 334.0, anchor="nw", text="Raça:", fill="#FFFFFF", font=("MarcellusSC Regular", 24 * -1))
canvas.create_text(512.0, 249.0, anchor="nw", text="Atributos:", fill="#FFFFFF", font=("MarcellusSC Regular", 24 * -1))
canvas.create_text(527.0, 350.0, anchor="nw", text="História:", fill="#FFFFFF", font=("MarcellusSC Regular", 24 * -1))
canvas.create_text(35, 385, anchor="nw", text="Gênero:", fill="#FFFFFF", font=("MarcellusSC Regular", 24 * -1))

# Variável para armazenar o gênero selecionado
genero_var = StringVar(value="Masculino")
# Radiobuttons de Gênero
radio_masculino = Radiobutton(
    window,
    text="Masculino",
    variable=genero_var,
    value="Masculino",
    font=("MarcellusSC Regular", 14),
)
radio_masculino.place(x=126, y=385)

radio_feminino = Radiobutton(
    window,
    text="Feminino",
    variable=genero_var,
    value="Feminino",
    font=("MarcellusSC Regular", 14),
)
radio_feminino.place(x=250, y=385)

# Funções para mostrar dados nos campos de texto
def mostrar_nome(nome):
    nome_field.configure(state="normal")
    nome_field.delete("1.0", "end")
    nome_field.insert("1.0", nome)
    nome_field.configure(state="disabled")

def mostrar_personagem(nome, classe, raca, atributos, historia):
    mostrar_nome(nome)
    classe_field.configure(state="normal")
    classe_field.delete("1.0", "end")
    classe_field.insert("1.0", classe)
    classe_field.configure(state="disabled")

    raca_field.configure(state="normal")
    raca_field.delete("1.0", "end")
    raca_field.insert("1.0", raca)
    raca_field.configure(state="disabled")

    atributos_field.configure(state="normal")
    atributos_field.delete("1.0", "end")
    atributos_field.insert("1.0", atributos)
    atributos_field.configure(state="disabled")

    historia_field.configure(state="normal")
    historia_field.delete("1.0", "end")
    historia_field.insert("1.0", historia)
    historia_field.configure(state="disabled")

def mostrar_nome(nome):
    nome_field.configure(state="normal")
    nome_field.delete("1.0", "end")
    nome_field.insert("1.0", nome)
    nome_field.configure(state="disabled")

def mostrar_classe(classe):
    classe_field.configure(state="normal")
    classe_field.delete("1.0", "end")
    classe_field.insert("1.0", classe)
    classe_field.configure(state="disabled")

def mostrar_raca(raca):
    raca_field.configure(state="normal")
    raca_field.delete("1.0", "end")
    raca_field.insert("1.0", raca)
    raca_field.configure(state="disabled")

def mostrar_atributos(atributos):
    atributos_field.configure(state="normal")
    atributos_field.delete("1.0", "end")
    atributos_field.insert("1.0", atributos)
    atributos_field.configure(state="disabled")

def mostrar_historia(historia):
    historia_field.configure(state="normal")
    historia_field.delete("1.0", "end")
    historia_field.insert("1.0", historia)
    historia_field.configure(state="disabled" )

# Função para criar novo personagem
def criar_personagem():
    genero = genero_var.get()  # Verifica o gênero selecionado
    if genero == "Masculino":
        tn.global_model_path = tn.model_masculino
    else:
        tn.global_model_path = tn.model_feminino

    global nomegb
    global historiagb
    nome = tn.gerar_e_retornar_nome(genero='genero_var')
    nomegb = nome
    classe = cr.nomeclasse
    raca = cr.nomeraca
    atributos = cr.atrib
    historia = gh.generate_background()
    historiagb = historia
    mostrar_personagem(nome, classe, raca, atributos, f"{nome} {historia}")


#Função para o botão "Refazer Classes e Atributos"
def refazerClasseAtrib():
    cr.refClasseRaca()
    classe = cr.nomeclasse
    raca = cr.nomeraca
    atributos = cr.atrib
    
    mostrar_classe(classe)
    mostrar_raca(raca)
    mostrar_atributos(atributos)

#Função para o botão de "Criar Nova História IA"
def criar_historiaIA():
    historia = gia.gerar_e_retornar_historia()
    global historiagb
    historiagb = historia 

    mostrar_historia(f"{nomegb}, {historia}")

#Função para o botão de "Criar Nova História IA"
def criar_historia():
    historia = gh.generate_background()
    global historiagb
    historiagb = historia

    mostrar_historia(f"{nomegb}, {historia}")

#Função para o botão de recriar nome
def recriar_nome():
    global genero_var
    nome = tn.gerar_e_retornar_nome(genero='genero_var')
    global nomegb
    global historiagb
    nomegb = nome

    mostrar_nome(nome)
    mostrar_historia(f"{nomegb}, {historiagb}")

#Função para o botão de recriar classe
def recriar_classe():
    cr.refazerClasse()
    classe = cr.nomeclasse
    atributos = cr.atrib

    mostrar_classe(classe)
    mostrar_atributos(atributos)

#Função para o botão de recriar raça
def recriar_raca():
    cr.refazerRaca()
    raca = cr.nomeraca

    mostrar_raca(raca)

# Botão Criar Personagem
botao_criar_personagem = Button(
    window,
    text="Criar Novo Personagem",
    command=criar_personagem,
    bg="#000000",
    fg="#FFFFFF",
    font=("MarcellusSC Regular", 18),
    borderwidth=0,
)
botao_criar_personagem.place(x=128, y=498, width=302, height=50)

# Botão Refazer Classes e Atributos 
botao_refazer_classes = Button(
    window,
    text="Refazer Classes e Raça",
    command=refazerClasseAtrib,
    bg="#000000",
    fg="#FFFFFF",
    font=("MarcellusSC Regular", 18),
    borderwidth=0,
)
botao_refazer_classes.place(x=110, y=579, width=331, height=50)

# Botão Criar nova História 
botao_criar_historia = Button(
    window,
    text="Criar Nova História",
    command=criar_historia,
    bg="#000000",
    fg="#FFFFFF",
    font=("MarcellusSC Regular", 18),
    borderwidth=0,
)
botao_criar_historia.place(x=622, y=498, width=331, height=50)

# Botão Criar Nova História IA (Beta) 
botao_criar_historia_ia = Button(
    window,
    text="Criar Nova História IA (Beta)",
    command=criar_historiaIA,
    bg="#000000",
    fg="#FFFFFF",
    font=("MarcellusSC Regular", 18),
    borderwidth=0,
)
botao_criar_historia_ia.place(x=605, y=579, width=361, height=50)

#Botão para Recriar Nome
botao_recriar_nome = Button(
    image=re_image,
    bg="#808080",
    command=recriar_nome
)
botao_recriar_nome.place(x=463,y=239, width=27, height=27)

#Botão para Recriar Classe
botao_recriar_classe = Button(
    image=re_image,
    bg="#808080",
    command=recriar_classe
)
botao_recriar_classe.place(x=463,y=287, width=27, height=27)

#Botão para Recriar Raça
botao_recriar_raca = Button(
    image=re_image,
    bg="#808080",
    command=recriar_raca
)
botao_recriar_raca.place(x=463,y=335, width=27, height=27)

# Configurações finais da janela
window.resizable(False, False)
window.mainloop()
