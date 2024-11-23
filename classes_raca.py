import random
global atrib
atrib = {'Vigor': 0,
         'Força': 0,
         'Destreza': 0,
         'Inteligência': 0,
         'Fé': 0,
         'Carisma': 0}

def selecClasse():
    classe = random.randint(1,8)
    global nomeclasse

    match classe:
        case 1:
            #print("Classe: Guerreiro")
            nomeclasse = "Guerreiro"
            atrib['Vigor'] = 13
            atrib['Força'] = 14
            atrib['Destreza'] = 12
            atrib['Inteligência'] = 6
            atrib['Fé'] = 7
            atrib['Carisma'] = 8
            #print(f'Ficha: {atrib}')
        case 2:
            #print("Classe: Mago")
            nomeclasse = "Mago"
            atrib['Vigor'] = 10
            atrib['Força'] = 6
            atrib['Destreza'] = 7
            atrib['Inteligência'] = 16
            atrib['Fé'] = 13
            atrib['Carisma'] = 8
            #print(f'Ficha: {atrib}')
        case 3:
            #print('Classe: Barbaro')
            nomeclasse = "Barbaro"
            atrib['Vigor'] = 15
            atrib['Força'] = 17
            atrib['Destreza'] = 13
            atrib['Inteligência'] = 3
            atrib['Fé'] = 5
            atrib['Carisma'] = 7
            #print(f'Ficha: {atrib}')
        case 4:
            #print('Classe: Monge')
            nomeclasse = "Monge"
            atrib['Vigor'] = 10
            atrib['Força'] = 8
            atrib['Destreza'] = 13
            atrib['Inteligência'] = 11
            atrib['Fé'] = 13
            atrib['Carisma'] = 5
            #print(f'Ficha: {atrib}')
        case 5:
            #print('Classe: Ladino')
            nomeclasse = "Ladino"
            atrib['Vigor'] = 7
            atrib['Força'] = 11
            atrib['Destreza'] = 17
            atrib['Inteligência'] = 9
            atrib['Fé'] = 3
            atrib['Carisma'] = 13
            #print(f'Ficha: {atrib}')
        case 6:
            #print('Classe: Clérigo')
            nomeclasse = "Clérigo"
            atrib['Vigor'] = 7
            atrib['Força'] = 6
            atrib['Destreza'] = 4
            atrib['Inteligência'] = 12
            atrib['Fé'] = 18
            atrib['Carisma'] = 13
            #print(f'Ficha: {atrib}')
        case 7:
            #print('Classe: Paladino')
            nomeclasse = "Paladino"
            atrib['Vigor'] = 14
            atrib['Força'] = 14
            atrib['Destreza'] = 5
            atrib['Inteligência'] = 8
            atrib['Fé'] = 17
            atrib['Carisma'] = 7
            #print(f'Ficha: {atrib}')
        case 8:
            #print('Classe: Bardo')
            nomeclasse = "Bardo"
            atrib['Vigor'] = 6
            atrib['Força'] = 3
            atrib['Destreza'] = 7
            atrib['Inteligência'] = 13
            atrib['Fé'] = 12
            atrib['Carisma'] = 19
            #print(f'Ficha: {atrib}')

def selecRaca():
    raca = random.randint(1,6)
    global nomeraca
    match raca:
        case 1:
           # print("Raça: Humano")
            nomeraca = "Humano"
        case 2:
           # print("Raça: Elfo")
            nomeraca = "Elfo"
        case 3:
           # print('Raça: Anão')
            nomeraca = "Anão"
        case 4:
           # print('Raça: Meio Elfo')
            nomeraca = "Meio Elfo"
        case 5:
           # print('Raça: Draconato')
            nomeraca = "Draconato"
        case 6:
           # print('Raça: Bestial')
            nomeraca = "Bestial"

def refazerClasse():
    selecClasse()


def refazerRaca():
    selecRaca()

def refClasseRaca():
    selecClasse()
    selecRaca()

selecClasse()
selecRaca()
refazerClasse()
#print(nomeclasse)
#print(nomeraca)