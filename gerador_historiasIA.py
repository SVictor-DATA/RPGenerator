import numpy as np
import pandas as pd
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense, Embedding, Dropout
from tensorflow.keras.callbacks import ModelCheckpoint
import random
import os

# Função para carregar e preparar os dados de história
def load_stories(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        stories = f.read().splitlines()

    stories = [story.lower() for story in stories]

    # Mapeamento de caracteres
    chars = sorted(list(set(''.join(stories))))
    char_to_int = {char: i for i, char in enumerate(chars)}
    int_to_char = {i: char for i, char in enumerate(chars)}

    seq_length = 5  # Tamanho da sequência de entrada
    dataX, dataY = [], []

    for story in stories:
        for i in range(len(story) - seq_length):
            seq_in = story[i:i + seq_length]
            seq_out = story[i + seq_length]
            dataX.append([char_to_int[char] for char in seq_in])
            dataY.append(char_to_int[seq_out])

    X = np.array(dataX)
    y = to_categorical(dataY, num_classes=len(chars))

    X = pad_sequences(X, maxlen=seq_length, padding='pre')
    return X, y, char_to_int, int_to_char, chars, stories

# Função para construir o modelo LSTM
def build_model(chars, seq_length):
    model = Sequential()
    model.add(Embedding(len(chars), 50, input_length=seq_length))
    model.add(LSTM(100, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(len(chars), activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# Função para amostrar próxima letra com temperatura
def sample(preds, temperature=0.6):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds + 1e-7) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

# Função para gerar histórias com ajuste automático de comprimento narrativo
def generate_story(model, start_seq, char_to_int, int_to_char, seq_length, min_length=100, max_length=300, temperature=0.6):
    story = start_seq
    sentence_end = False
    attempts = 0  # Contador de tentativas
    unique_chars = set()  # Conjunto para monitorar caracteres únicos

    while len(story) < max_length:
        input_seq = [char_to_int.get(char, 0) for char in story][-seq_length:]
        input_seq = pad_sequences([input_seq], maxlen=seq_length, padding='pre')
        pred = model.predict(input_seq, verbose=0)
        next_char = int_to_char[sample(pred[0], temperature)]
        
        # Verificar repetição para evitar sequência de uma só palavra
        if next_char == ' ' and story[-1] == ' ':
            continue
        if next_char not in unique_chars or len(unique_chars) > 3:  # Evita repetição excessiva
            story += next_char
            unique_chars.add(next_char)

        # Checar final de sentença para garantir frases completas e coesas
        if next_char in '.!?':
            sentence_end = True

        # Incrementar tentativas e checar critério de finalização
        attempts += 1
        if sentence_end and len(story) >= min_length and attempts >= 20:
            break
        elif attempts > 300:  # Limite máximo para evitar loops longos demais
            break

    return story.capitalize()

# Função para gerar uma nova história com possibilidade de múltiplas tentativas
def generate_another_story(model, start_seq, char_to_int, int_to_char, seq_length=5, min_length=50, max_length=200, temperature=0.6):
    while True:
        # Gera a história
        nova_historia = generate_story(model, start_seq, char_to_int, int_to_char, seq_length, min_length, max_length, temperature)
        print(f"História do Personagem: {nova_historia}")
        
        # Pergunta ao usuário se deseja uma nova história
        resposta = input("Deseja gerar outra história? (s/n): ").strip().lower()
        
        if resposta != 's':
            break
        else:
            # Opcional: Alterar os parâmetros para diversidade nas novas histórias geradas
            start_seq = random.choice(stories)[:seq_length]  # Escolhe uma nova sequência inicial
            min_length = random.randint(50, 150)  # Ajuste aleatório do comprimento mínimo
            max_length = random.randint(150, 300)  # Ajuste aleatório do comprimento máximo
            temperature = round(random.uniform(0.5, 0.8), 2)  # Ajuste aleatório da temperatura para variar a criatividade

    print("Geração de histórias concluída.")

import random
import numpy as np

def gerar_e_retornar_historia():
    # Seleciona uma sequência inicial aleatória de uma história de treinamento para iniciar
    start_seq = random.choice([story for story in stories if len(story) >= 5])[:5]
    
    # Gera a história usando a função generate_story
    nova_historia = generate_story(
        model, 
        start_seq, 
        char_to_int, 
        int_to_char, 
        seq_length=5, 
        min_length=50, 
        max_length=100, 
        temperature=1
    )
    
    # Salva o modelo atualizado
    model.save(model_filename)
    
    # Retorna a nova história gerada
    return nova_historia



# Carregar o dataset de histórias
file_path = 'historias_treinamento.txt'
X, y, char_to_int, int_to_char, chars, stories = load_stories(file_path)

# Verificar se o modelo existe para carregar ou treinar
model_filename = 'modelo_historias.keras'
if os.path.exists(model_filename):
    print(f"Carregando o modelo salvo de {model_filename}...")
    model = load_model(model_filename)
else:
    print("Treinando um novo modelo...")
    model = build_model(chars, seq_length=5)
    
    checkpoint = ModelCheckpoint(model_filename, monitor='loss', verbose=1, save_best_only=True, mode='min')
    model.fit(X, y, epochs=150, batch_size=64, callbacks=[checkpoint])

# Selecionar sequência inicial
start_seq = random.choice(stories)[:5]

# Iniciar o processo de geração de histórias com possibilidade de múltiplas tentativas
gerar_e_retornar_historia()