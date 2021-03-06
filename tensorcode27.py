# Redes Neurais - Multilayer Perceptron 

# Imports
import numpy as np
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Gerando dados sintéticos

# Hiperparâmetros
size = 200000
num_epochs = 10
learning_rate = 0.001

# Gerando dados para x
# https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.random.randint.html
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.dstack.html
x1 = np.random.randint(0, 100, size)
x2 = np.random.randint(0, 100, size)
x_treino = np.dstack((x1, x2))[0]

# Gerando dados para y
y_treino = 3*(x1**(1/2)) + 2*(x2**2)

# Print
print("\nValores e shape de x:")
print(x_treino)
print(x_treino.shape)
print("\nValores e shape de y:")
print(y_treino)
print(y_treino.shape)

# Método 2 para construir modelos MPL com TF2

# tf.keras.Model
class Modelo(tf.keras.Model):
    def __init__(self):
        super(Modelo, self).__init__()
        self.entrada = tf.keras.layers.Dense(64, input_shape = (2,), activation = 'sigmoid')
        self.oculta1 = tf.keras.layers.Dense(128, activation = 'relu')
        self.saida = tf.keras.layers.Dense(2)
        self.compile(optimizer = tf.keras.optimizers.RMSprop(learning_rate), loss = tf.keras.losses.MSE)

# https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/RMSprop

    def call(self, inputs):
        x = self.entrada(inputs)
        x = self.oculta1(x)
        x = self.saida(x)
        return x

# Cria o modelo
modelo_v2 = Modelo()

# Treina o modelo
modelo_v2.fit(x = x_treino, y = y_treino, epochs = num_epochs)

# Sumário do modelo
print("\nSumário do modelo:")
modelo_v2.summary()

# Avaliando a performance em treino
scores_treino = modelo_v2.evaluate(x_treino, y_treino, verbose = 0)
print("\nErro Final em Treino: {:.0f}".format(scores_treino))


# Testando o modelo

# Gerando novos dados para x
x1 = np.array([100, 9, 62, 79, 94, 91, 71, 41])
x2 = np.array([65, 39, 40, 44, 77, 42, 36, 74])
x_teste = np.dstack((x1, x2))[0]

# Gerando novos dados para y
y_teste = 3*(x1**(1/2)) + 2*(x2**2)

# Fazendo previsões
print("\nTestando o Modelo...")
y_pred = modelo_v2.predict(x_teste)

# Avaliando a performance em teste
scores_teste = modelo_v2.evaluate(x_teste, y_teste, verbose = 0)
print("\nErro Final em Teste: {:.0f}".format(scores_teste))

print("\n")
for i in range(5):
	print ('''Entrada(x): ({}, {}), Saida(y): ({:.0f}), Previsão do Modelo(y_pred): ({:.0f})'''.format(x1[i], x2[i], y_teste[i], y_pred[i][0]))

print("\n")
