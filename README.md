# Tesina Final de Grado - Volman, Mariel

Este repositorio contiene el código desarrollado para la Tesina Final de Grado **"Análisis e Implementación de Herramientas Inteligentes para la Detección de Cáncer en Imágenes Médicas"**, para la obtención del grado de Licenciada en Ciencias de la Computación en la Facultad de Ingeniería, Universidad Nacional de Cuyo.

## Descripción de archivos

- *gen_bboxes.py*: este script contiene el código correspondiente al **preprocesamiento de las imágenes** de los conjuntos de datos utilizados para las tareas de detección. En particular, se encarga de la **generación de cuadros delimitadores (*bounding boxes*)**. Lo que hace es, a partir de las imágenes y sus respectivas máscaras, extraer los contornos para generar el bounding box, convertirlo al formato YOLO (*x_center y_center width height*), normalizarlo y guardarlo en un archivo de texto (*.txt*).

- *train_yolo.py*: este script se utiliza para automatizar el proceso de **entrenamiento y validación de la red neuronal** y guardar los resultados que produce. Para ello, primero carga el modelo seleccionado (*yolov8n*) y el conjunto de datos a utilizar. Luego define la configuración de hiperparámetros. Y finalmente, entrena el modelo con las distintas configuraciones guardando los resultados de las métricas a evaluar.

- *cancer_detection_app*: en esta carpeta se encuentra el código correspondiente a la **herramienta de visualización**.

## Herramienta de visualización

En este trabajo se llevó a cabo la implementación de un prototipo inicial de una herramienta que sirve como un sistema de ayuda al diagnóstico para visualizar la detección producida por la red neuronal. La estructura del proyecto se encuentra organizada de la siguiente manera:

- *images*: esta carpeta sirve para organizar las **imágenes** que serán evaluadas por el sistema. No obstante, la herramienta permite seleccionar una imagen desde cualquier directorio de la computadora.

- *neural network model*: esta carpeta contiene los **pesos del modelo** entrenado de la red neuronal que se utilizarán para la tarea de detección.
- *processed_images*: en esta carpeta se guardan las **imágenes** producidas como **resultado** de la detección.
- *python_scripts*: acá se encuentra el código escrito en Python que realiza el **proceso de detección**: obtiene la imagen de entrada, carga el modelo de la red neuronal, realiza la detección y guarda la imagen resultante. 
- *index.php*: este es el código correspondiente a la **página de inicio** de la aplicación. Contiene un botón para seleccionar la imagen y otro para procesarla.
- *upload.php*: este código corresponde a la **página de resultado**, que muestra la imagen obtenida al realizar la detección.
