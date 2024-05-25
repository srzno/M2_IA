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

## Implementación y Evaluación inicial del modelo

El objetivo de este proyecto es desarrollar un modelo de clasificación de imágenes capaz de distinguir entre hotdogs y no hotdogs. Inicialmente, seleccioné MoBiNet, un modelo prometedor por su eficiencia en términos de uso de memoria y costo computacional. Sin embargo, al implementarlo, no obtuve la precisión esperada y decidí explorar alternativas basadas en investigaciones y conocimientos adquiridos en clase.

Para encontrar una mejor solución, revisé varias arquitecturas de redes neuronales convolucionales (CNN). Me inspiré particularmente en el paper "Deep Residual Learning for Image Recognition" de Kaiming He, Xiangyu Zhang, Shaoqing Ren y Jian Sun, que introduce la arquitectura ResNet. ResNet utiliza conexiones residuales para facilitar el entrenamiento de redes profundas, mejorando significativamente la precisión en tareas de reconocimiento de imágenes.

Basándome en los principios de ResNet y en conocimientos adquiridos en clase, diseñé una arquitectura CNN más simple y robusta. Este nuevo modelo incluyó varias capas de convolución y max pooling, seguidas de capas densas para la clasificación final.

Elegí utilizar TensorFlow y Keras por su simplicidad, flexibilidad y amplio soporte comunitario. Estas herramientas permiten construir, entrenar y desplegar modelos de manera eficiente. Seleccioné la métrica de **accuracy* porque es intuitiva y refleja directamente la proporción de predicciones correctas realizadas por el modelo. Dado que mi conjunto de datos está balanceado, la accuracy es una métrica adecuada para evaluar la eficacia del clasificador.

El proceso de selección y ajuste del modelo es crucial en cualquier proyecto de aprendizaje automático. Aunque MoBiNet ofrecía ventajas teóricas, la implementación práctica reveló limitaciones en mi caso específico. Inspirado por los principios de redes residuales y utilizando conocimientos adquiridos en clase, logré diseñar una CNN más efectiva. La elección del framework TensorFlow/Keras y la métrica de accuracy facilitó la construcción y evaluación del modelo, permitiéndome mejorar el rendimiento en la tarea de clasificación de imágenes de hotdogs vs. no hotdogs.

### Referencias
He, K., Zhang, X., Ren, S., & Sun, J. (2016). "Deep Residual Learning for Image Recognition." Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, 770-778. https://arxiv.org/abs/1512.03385 

Yan, S., Yao, G., & Liu, X. (2019). "MoBiNet: A Mobile Binary Network for Image Classification." arXiv preprint. https://arxiv.org/abs/1907.12629 
