Resultados primer entrenamiento (1000):

2025-07-26 13:54:07.248178: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
2025-07-26 13:54:08.326368: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
C:\Users\Zamch\Desktop\qqq\coding\ai_machine_learning\Venv\Lib\site-packages\keras\src\layers\core\dense.py:93: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
2025-07-26 13:54:10.469822: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX512F AVX512_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
Comenzamos el entrenamiento...
Modelo entrenado
predicción 1
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 41ms/step
El resultado es [[211.74376]]fahrenheit

---
Gráfica de la función de pérdida.

<img width="717" height="482" alt="image" src="https://github.com/user-attachments/assets/1dd9b87d-b74f-4902-8d21-10907a291a63" />
