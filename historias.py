import random

# Funções auxiliares para gerar partes da história
def generate_event():
    events = [
        "perdeu sua família em uma batalha sangrenta",
        "foi exilado de sua terra natal",
        "descobriu um poder oculto que mudaria sua vida",
        "foi traído por seu melhor amigo",
        "foi convocado para uma missão secreta pelo rei",
        "sobreviveu a uma emboscada inesperada",
        "encontrou um artefato mágico de imenso poder",
        "se apaixonou por uma figura misteriosa e proibida"
    ]
    return random.choice(events)

def generate_motivation():
    motivations = [
        "procurar vingança",
        "provar seu valor",
        "restaurar a honra de sua família",
        "descobrir a verdade por trás de um grande mistério",
        "encontrar seu verdadeiro propósito",
        "proteger os mais fracos",
        "encontrar redenção por erros passados",
        "dominar o poder oculto dentro de si"
    ]
    return random.choice(motivations)

def generate_ending():
    endings = [
        "agora está em uma jornada para mudar o destino do mundo.",
        "se tornou um herói lendário em sua terra.",
        "vive escondido, mas sempre pronto para um novo desafio.",
        "segue em busca de respostas que podem abalar o reino.",
        "se uniu a um grupo de aventureiros em busca de grandes feitos.",
        "é agora um mercenário que luta pelo que acredita."
    ]
    return random.choice(endings)

# Função para gerar uma história de background
def generate_background():
    event = generate_event()
    motivation = generate_motivation()
    ending = generate_ending()
    
    # Construir a história
    background = f"{event}. Agora, motivado(a) por {motivation}, {ending}"
    return background


historia = generate_background()

