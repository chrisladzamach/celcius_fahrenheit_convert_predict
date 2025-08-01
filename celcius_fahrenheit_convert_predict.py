import tensorflow as tf # librería para inteligencia artificial hecha por google
import numpy as np # para trabajar fácilmente con arreglos numéricos
import matplotlib.pyplot as plt

celcius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float) # arreglo de números que contiene las 7 entradas de grados celcuis
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float) # resultados en grados fahrenheit

'''
# uso el framework keras para hacer las redes neuronales de manera simple.
# las capas de tipo densa son las que tienen relaciones de la capa principal hacia todas las neuronas de la siguiente capa
'''
capa = tf.keras.layers.Dense(units=1, input_shape=[1]) # se indican las unidades o neuronas de la capa, también se le especifica que tenemos una entrada con una neurona.
modelo = tf.keras.Sequential([capa]) # se usa un modelo de keras para darle las capas y poder trabajar con él

# ahora, se procede a compilar el modelo para indicarle cómo quiero que se procecen los calculos para poder aprender mejor.
modelo.compile(
  # para este ejemplo solo indicaremos dos propiedades, el optimizador y la función de perdida.
  optimizer=tf.keras.optimizers.Adam(0.1), # El optimizador Adam, permite que la red sepa cómo ajustar los pesos y sesgos de forma eficiente para que apdenda y no desaprenda. lo que va en parentesis es la taza de aprendizaje
  loss='mean_squared_error' # para la función de perdida usamos 'error cuadratico medio', básicamente, esta función considera que una poca cantidad de errores grandes, es peor que una gran cantidad de errores pequeños
)

print("Comenzamos el entrenamiento...")
'''
Para entrenar al modelo, usamos la función fit, a la cuál se le indican los datos de entrada y resultados esperados.
además, se le indica cuántas veces quiero que lo intente o cuantas vueltas debe hacer.

De momento, tenemos 7 datos, y cada vuelta revisa los 7 datos una sola vez.
Tenemos que darle muchas vueltas para darle tiempo a que realmente se optimice lo más posible.

Además, se le pasa verbose=False para que no retorne tanta información al estar entrenando
'''
historial = modelo.fit(celcius, fahrenheit, epochs=1000, verbose=False)
print("Modelo entrenado")

'''
Antes de intentar predecir algo, se van a visualizar los datos de la función de perdida
'''

plt.xlabel("# Epoca")
plt.ylabel("Magnitud de perdida")
plt.plot(historial.history["loss"])

# predicción:
print("predicción 1")
resultado = modelo.predict(np.array([[100.0]]))
print('El resultado es ' + str(resultado) + 'fahrenheit')

