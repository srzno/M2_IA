# Módulo 2: Inteligencia Artificial

El objetivo de este repositorio es crear un reconocedor de imagenes que sea capaz de distinguir entre un Hotdog y algun otro objeto que no sea un hotdog, haciendo referencia a la serie de Silicon Valley.

### Referencia de el dataset:
https://www.kaggle.com/datasets/thedatasith/hotdog-nothotdog/data

## Dataset: 
https://drive.google.com/drive/folders/1y81hudQd1ExQyfYo0CJX8BE1wbcRrjsH?usp=sharing

### 🌭 Hotdog | Not Hotdog Dataset

Aquí encontrarás las imágenes de prueba y entrenamiento del Hotdog | No es un conjunto de datos de Hotdog. El objetivo es tener un conjunto divertido de imágenes para usar en la clasificación binaria. Consulte la sección de códigos para ver ejemplos de modelos que funcionan bien para este propósito.

#### Archivos

Contenido del dataset:

- **Training** imágenes que se utilizarán para desarrollar un modelo de clasificación binaria.
     - Imágenes `2121` de perritos calientes e imágenes `2121` de otros artículos.
- **Test** Imágenes que se utilizarán después de entrenar un modelo de clasificación binaria.
     - `200` imágenes de hot dogs y `200` imágenes de otros artículos

El número total de imágenes es, por supuesto, `2x2121` para entrenamiento y `2x200` para pruebas, con un total de `4642` archivos.
    
    .
    ├── hotdog-nothotdog 
        ├── test
            ├── hotdog
            ├── nothotdog   
        ├── train
            ├── hotdog
            ├── nothotdog
