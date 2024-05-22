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

`train_datagen = ImageDataGenerator(
							rescale = 1./255,
							rotation_range = 150,
							width_shift_range = 0.1,
							height_shift_range = 0.1,
							shear_range = 0.2,
							horizontal_flip = True)`
