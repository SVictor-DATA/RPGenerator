import numpy as np
import os
import random
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense, Embedding, Dropout
from tensorflow.keras.callbacks import ModelCheckpoint

# Variáveis globais
model_masculino = 'nome_modelo_masculino.keras'
model_feminino = 'nome_modelo_feminino.keras'

# Função para carregar e preparar os dados
def load_names(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        names = f.read().splitlines()
    names = [name.lower() for name in names]

    chars = sorted(list(set(''.join(names))))
    char_to_int = {char: i for i, char in enumerate(chars)}
    int_to_char = {i: char for i, char in enumerate(chars)}

    seq_length = 5  # Tamanho da sequência de entrada
    dataX, dataY = [], []
    for name in names:
        for i in range(0, len(name) - seq_length):
            seq_in = name[i:i + seq_length]
            seq_out = name[i + seq_length]
            dataX.append([char_to_int[char] for char in seq_in])
            dataY.append(char_to_int[seq_out])

    X = pad_sequences(np.array(dataX), maxlen=seq_length, padding='pre')
    y = to_categorical(dataY, num_classes=len(chars))
    return X, y, char_to_int, int_to_char, chars, names

# Função para construir o modelo LSTM
def build_model(chars, seq_length):
    model = Sequential([
        Embedding(len(chars), 50, input_length=seq_length),
        LSTM(100, return_sequences=False),
        Dropout(0.2),
        Dense(len(chars), activation='softmax')
    ])
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# Função para amostrar próxima letra baseado na "temperatura"
def sample(preds, temperature=1.0):
    preds = np.log(np.asarray(preds).astype('float64') + 1e-7) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    return np.argmax(np.random.multinomial(1, preds, 1))

# Função para gerar nomes com comprimento variável
def generate_name(model, start_seq, char_to_int, int_to_char, seq_length, min_length=5, max_length=6, temperature=1):
    name = start_seq
    name_length = random.randint(min_length, max_length)
    for _ in range(name_length):
        input_seq = pad_sequences([[char_to_int[char] for char in name][-seq_length:]], maxlen=seq_length, padding='pre')
        pred = model.predict(input_seq, verbose=0)
        next_char = int_to_char[sample(pred[0], temperature)]
        name += next_char
    return name.capitalize()

# Função para treinar o modelo incrementalmente com novos exemplos
def incremental_training(model, generated_names, char_to_int, seq_length=5, batch_size=64, epochs=1):
    dataX, dataY = [], []
    for name in generated_names:
        for i in range(0, len(name) - seq_length):
            seq_in = name[i:i + seq_length]
            seq_out = name[i + seq_length]
            dataX.append([char_to_int.get(char, 0) for char in seq_in])
            dataY.append(char_to_int.get(seq_out, 0))

    X = pad_sequences(dataX, maxlen=seq_length, padding='pre')
    y = to_categorical(dataY, num_classes=len(char_to_int))
    model.fit(X, y, epochs=epochs, batch_size=batch_size)

# Função para carregar ou treinar o modelo
def carregar_ou_treinar_modelo(file_path, model_path):
    X, y, char_to_int, int_to_char, chars, names = load_names(file_path)

    if os.path.exists(model_path):
        model = load_model(model_path)
    else:
        model = build_model(chars, seq_length=5)
        checkpoint = ModelCheckpoint(model_path, monitor='loss', verbose=1, save_best_only=True, mode='min')
        model.fit(X, y, epochs=500, batch_size=64, callbacks=[checkpoint])
    return model, char_to_int, int_to_char, chars, names

# Função para carregar o modelo com base no gênero
def carregar_modelo_por_genero(genero):
    if genero == "Masculino":
        file_path = 'nomes_masculinos.txt'
        model_path = model_masculino
    else:
        file_path = 'nomes_femininos.txt'
        model_path = model_feminino

    return carregar_ou_treinar_modelo(file_path, model_path)

# Função para gerar um novo nome e retornar (aceita gênero como argumento)
def gerar_e_retornar_nome(genero="Masculino", min_length=5, max_length=6, temperatura=1):
    model, char_to_int, int_to_char, chars, names = carregar_modelo_por_genero(genero)
    start_seq = random.choice([name for name in names if len(name) >= 5])[:5]
    novo_nome = generate_name(model, start_seq, char_to_int, int_to_char, seq_length=5, min_length=min_length, max_length=max_length, temperature=temperatura)
    incremental_training(model, [novo_nome], char_to_int)
    model.save(model_masculino if genero == "Masculino" else model_feminino)
    return novo_nome

# Exemplo de uso
if __name__ == "__main__":
    genero = input("Escolha o gênero (Masculino/Feminino): ").capitalize()
#    print(f"Gênero escolhido: {genero}")  # Adiciona um print para exibir o gênero escolhido
    print("Nome gerado:", gerar_e_retornar_nome(genero))
