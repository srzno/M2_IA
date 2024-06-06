# Módulo 2: Inteligencia Artificial

El objetivo de este repositorio es crear un reconocedor de imagenes que sea capaz de distinguir entre un Hotdog y algun otro objeto que no sea un hotdog, esto con fines unicamente educativos, haciendo referencia a la serie de Silicon Valley.

### Referencia al dataset:
https://www.kaggle.com/datasets/thedatasith/hotdog-nothotdog/data

## Dataset: 
https://drive.google.com/drive/folders/1y81hudQd1ExQyfYo0CJX8BE1wbcRrjsH?usp=sharing

### 🌭 Hotdog | Not Hotdog Dataset

Aquí encontrarás las imágenes de prueba y entrenamiento del Hotdog | Not Hotdog. El objetivo es tener un conjunto divertido de imágenes para usar en la clasificación binaria. Consulte la sección de códigos para ver ejemplos de modelos que funcionan bien para este propósito.

#### Archivos

Contenido del dataset:

- **Training** imágenes que se utilizarán para desarrollar un modelo de clasificación binaria.
     - Imágenes `2021` de hot dogs e imágenes `2021` de otros artículos.
- **Validation** Imágenes que se utilizarán después de entrenar un modelo de clasificación binaria pero antes de probarlo.
     - `100` imágenes de hot dogs y `100` imágenes de otros artículos
- **Test** Imágenes que se utilizarán después de entrenar un modelo de clasificación binaria.
     - `200` imágenes de hot dogs y `200` imágenes de otros artículos

El número total de imágenes es de `4642` archivos.

La división 85% train - 10% test - 5% validation es ideal para este modelo simple de hot dogs. El 90% de entrenamiento garantiza un aprendizaje profundo, mientras que el 10% de prueba permite una evaluación precisa. Si es necesario, se puede usar el aumento de datos para ampliar el conjunto de entrenamiento.

Cabe destacar que en el dataset original no se cuenta con la parte de **validation** la cual fue insertada manualmente creando una carpeta extra y moviendo las imagenes que se quieren a esta.
    
    .
    ├── hotdog-nothotdog 
        ├── test
            ├── hotdog
            ├── nothotdog   
        ├── validation
            ├── hotdog
            ├── nothotdog
        ├── train
            ├── hotdog
            ├── nothotdog

## Preprocesado de los datos

Utilice imageGenerator para ampliar y enriquecer el conjunto de datos de entrenamiento ("train") del modelo de aprendizaje automático mediante la modificación creativa de las imágenes existentes. De esta manera, generará un conjunto de datos más robusto que permitirá un entrenamiento más efectivo de su modelo, lo que se traduce en un mejor rendimiento y resultados más precisos.

Se utilizaron las siguientes condiciones para crear mas imagenes para el dataset

```
train_datagen = ImageDataGenerator(
					rescale = 1./255,
					rotation_range = 150,
					width_shift_range = 0.1,
					height_shift_range = 0.1,
					shear_range = 0.2,
					horizontal_flip = True)
```
- Normalización de la escala de los píxeles (rescale):
Aplicamos un factor de escala de 1./255 para normalizar los valores de los píxeles al rango [0, 1], lo que facilita la convergencia durante el entrenamiento del modelo.

- Rotación (rotation_range):
Configuramos un rango de rotación de hasta 150 grados para aumentar la robustez del modelo ante variaciones en la orientación de los objetos.

- Desplazamiento horizontal y vertical (width_shift_range y height_shift_range):
Implementamos desplazamientos horizontales y verticales de 10% del ancho y altura de las imágenes para mejorar la capacidad del modelo de generalizar y reconocer objetos en diferentes posiciones.

- Corte (shear_range):
Utilizamos un rango de corte de 0.2 para aplicar transformaciones que inclinan los objetos, ayudando al modelo a aprender representaciones invariantes a distorsiones geométricas.

- Inversión horizontal (horizontal_flip):
Habilitamos la inversión horizontal para reflejar las imágenes aleatoriamente, duplicando el número de muestras de entrenamiento y mejorando la capacidad del modelo para reconocer objetos en distintas orientaciones.

## Implementación del modelo (Inicial)

El objetivo de este proyecto es desarrollar un modelo de clasificación de imágenes capaz de distinguir entre hotdogs y no hotdogs. Inicialmente, seleccioné MoBiNet [2], un modelo prometedor por su eficiencia en términos de uso de memoria y costo computacional. Sin embargo, al implementarlo, no obtuve la precisión esperada y decidí explorar alternativas basadas en investigaciones y conocimientos adquiridos en clase.

Para encontrar una mejor solución, revisé varias arquitecturas de redes neuronales convolucionales (CNN). Me inspiré particularmente en el paper "Deep Residual Learning for Image Recognition" [1], que introduce la arquitectura ResNet. ResNet utiliza conexiones residuales para facilitar el entrenamiento de redes profundas, mejorando significativamente la precisión en tareas de reconocimiento de imágenes.

Basándome en los principios de ResNet y en conocimientos adquiridos en clase, diseñé una arquitectura CNN más simple y robusta. Este nuevo modelo incluyó varias capas de convolución y max pooling, seguidas de capas densas para la clasificación final.

Elegí utilizar TensorFlow y Keras por su simplicidad, flexibilidad y amplio soporte comunitario. Estas herramientas permiten construir, entrenar y desplegar modelos de manera eficiente. Seleccioné las métricas *loss* y *accuracy* porque son intuitivas y reflejan directamente la proporción de predicciones correctas realizadas por el modelo. Dado que mi conjunto de datos está balanceado, la accuracy es una métrica adecuada para evaluar la eficacia del clasificador.

El proceso de selección y ajuste del modelo es crucial en cualquier proyecto de aprendizaje automático. Aunque MoBiNet [2] ofrecía ventajas teóricas, la implementación práctica reveló limitaciones en mi caso específico. Inspirado por los principios de redes residuales y utilizando conocimientos adquiridos en clase, logré diseñar una CNN más efectiva. La elección del framework TensorFlow/Keras y la métrica de accuracy facilitó la construcción y evaluación del modelo, permitiéndome mejorar el rendimiento en la tarea de clasificación de imágenes de hotdogs vs. no hotdogs.

## Evaluación inicial del modelo

### Accuracy y Loss (Inicial)
![Gráfica acc y loss_v1](https://github.com/srzno/M2_IA/blob/main/plt_v1.png)

Después de analizar los resultados de precisión y pérdida de mi modelo, observo que la precisión alcanzó un valor de alrededor del 63.75% en el conjunto de prueba, lo que indica que mi modelo puede predecir correctamente la clase de una imagen (ya sea "hotdog" o "not hotdog") aproximadamente dos tercios del tiempo. Si bien esta precisión no es excepcionalmente alta, es un punto de partida decente para mi modelo.

En cuanto a la pérdida, parece que ha disminuido gradualmente durante las primeras épocas del entrenamiento, lo que sugiere que mi modelo estaba mejorando y ajustándose a los datos de entrenamiento. Sin embargo, la pérdida en el conjunto de validación comenzó a aumentar después de algunas épocas, lo que indica un posible sobreajuste. Esto significa que mi modelo podría estar memorizando los datos de entrenamiento en lugar de aprender patrones generales que se apliquen a nuevos datos.

Basándome en estos resultados, creo que mi modelo tiene un buen potencial para clasificar imágenes de "hotdog" y "not hotdog", pero necesita cierto ajuste para mejorar su generalización a nuevos datos. Para abordar esto, podría considerar técnicas como la regularización, la optimización de hiperparámetros o la recolección de más datos para aumentar la diversidad de mi conjunto de entrenamiento. En conclusión, el objetivo es mejorar tanto la precisión como la pérdida en el conjunto de validación para lograr un rendimiento más robusto y generalizable de mi modelo.


### Matriz de Confusión (Inicial):

![Matriz de Confusión v1](https://github.com/srzno/M2_IA/blob/readme-img/confusion_matrix.png)

- **Precisión y Recall:**
Muy baja precisión y recall para los hotdogs (Hotdog), con solo 1 verdadero positivo y una cantidad extremadamente alta de falsos negativos (199).
Aunque tiene muchos verdaderos negativos (198), casi no puede identificar correctamente los hotdogs.

- **Errores:**
Solo 2 falsos positivos, pero esto se debe a que casi siempre predice que la imagen no es un hotdog.
Este modelo es significativamente peor porque falla en detectar correctamente los hotdogs.

## Evaluación de modelo mejorado

### Implementaación de modelo (Mejorado)

- Utilizamos el modelo ResNet50 preentrenado en la base de datos ImageNet, lo que permite aprovechar las características aprendidas en un gran conjunto de datos. Esto mejora significativamente la capacidad del modelo para generalizar en la tarea de clasificación.
- Las imágenes de entrada se ajustaron al tamaño que ResNet50 espera, es decir, (224, 224, 3). Esto asegura que las dimensiones de las imágenes sean compatibles con la arquitectura de ResNet50.
- Se usó ResNet50 como base del modelo con la configuración include_top=False, lo que excluye las capas de clasificación superiores para permitir la personalización. Se añadieron capas adicionales específicas para nuestro problema:
- GlobalAveragePooling2D: Reduce las dimensiones de los mapas de características.
	- Dense (128 unidades, activación relu): Añade una capa densa para aprendizaje de características específicas.
	- Dropout (50%): Evita el sobreajuste.
	- Dense (1 unidad, activación sigmoid): Capa de salida para clasificación binaria.
- El modelo se compiló usando binary_crossentropy como la función de pérdida, el optimizador RMSprop con una tasa de aprendizaje de 1e-4, y la métrica de accuracy.
- Se entrenó el modelo usando los conjuntos de datos de entrenamiento y validación con un número específico de épocas.

### Accuracy y Loss (Mejorado)
![Gráfica acc y loss_v3](https://github.com/srzno/M2_IA/blob/main/plt_v3.png)
- **Accuracy:**
La accuracy de entrenamiento aumenta de manera constante y llega a más del 92%.
La accuracy de validación es relativamente alta y estable alrededor del 85%, lo cual muestra un buen rendimiento general sin señales significativas de sobreajuste.

- **Loss:**
La pérdida de entrenamiento disminuye constantemente, indicando que el modelo está aprendiendo bien.
La pérdida de validación también disminuye inicialmente y se estabiliza, mostrando que el modelo no está sobreajustando significativamente.

### Matriz de Confusión (Mejorado):
![Matriz de Confusión v3](https://github.com/srzno/M2_IA/blob/readme-img/confusion_matrix3.png)
- **Precisión y Recall:**
Alta precisión y recall para los hotdogs (Hotdog), con un buen equilibrio entre falsos positivos y falsos negativos.
Tiene una cantidad significativa de verdaderos positivos (163) y verdaderos negativos (183), mostrando una buena capacidad de identificación correcta para ambas clases.

- **Errores:**
37 falsos negativos y 17 falsos positivos indican que hay algunos errores, pero no son significativos en comparación con las predicciones correctas.

### Referencias
[1] He, K., Zhang, X., Ren, S., & Sun, J. (2016). "Deep Residual Learning for Image Recognition." Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, 770-778. https://arxiv.org/abs/1512.03385 

[2] Yan, S., Yao, G., & Liu, X. (2019). "MoBiNet: A Mobile Binary Network for Image Classification." arXiv preprint. https://arxiv.org/abs/1907.12629 
