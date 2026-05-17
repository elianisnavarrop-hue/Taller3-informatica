# Taller 3 - Introducciíon a la informática médica
**Universidad de Antioquia – Facultad de Ingeniería**  
**Asignatura:** Informática 2  
**Monitor:** Juan Esteban Pineda Lopera
---
## Realizado por
Elianis Milena Navarro Peralta 
1063275944
---

## Descripción del proyecto

Este proyecto consiste en el desarrollo de una aplicación en Python para el procesamiento básico de imágenes médicas en formato DICOM utilizando herramientas de software libre.

La aplicación permite:

- Cargar archivos DICOM desde un directorio.
- Extraer metadata médica relevante.
- Organizar la información en un DataFrame de Pandas.
- Calcular la intensidad promedio de las imágenes usando NumPy.
- Aplicar procesamiento digital de imágenes con OpenCV.
- Exportar resultados a archivos CSV e imágenes PNG.

El proyecto utiliza Programación Orientada a Objetos (POO) mediante una clase llamada `ProcesadorDICOM`, encargada de encapsular toda la lógica del sistema.

---

## Tecnologías y librerías utilizadas

- Python
- pydicom
- NumPy
- Pandas
- OpenCV

Instalación de dependencias:

```bash
pip install pydicom numpy pandas opencv-python
```

---

## Estructura del proyecto

```text
taller3_DICOM/
│
├── data/
│   └── dicom/
│
├── output/
│   ├── edges/
│   └── equalized/
│
├── main.py
├── procesador_dicom.py
├── metadata.csv
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Funcionalidades implementadas

### 1. Carga de archivos DICOM

Se implementó una función capaz de recorrer automáticamente un directorio y cargar archivos DICOM utilizando `pydicom.dcmread()`.

Además, se manejan errores mediante bloques `try/except` para evitar fallos cuando un archivo no es válido.

---

### 2. Extracción de metadata

El programa extrae los siguientes tags DICOM:

- PatientID
- PatientName
- StudyInstanceUID
- StudyDescription
- StudyDate
- Modality
- Rows
- Columns

En algunos archivos DICOM ciertos tags pueden no estar disponibles debido a procesos de anonimización. Para manejar estos casos se utilizó `getattr()` con valores por defecto.

---

### 3. Creación de DataFrame

Toda la metadata se organiza utilizando Pandas en un DataFrame, donde cada fila representa un archivo DICOM y cada columna corresponde a un atributo extraído.

---

### 4. Análisis con NumPy

Se calculó la intensidad promedio de los píxeles de cada imagen utilizando:

```python
np.mean()
```

Este valor se agregó como una nueva columna llamada `IntensidadPromedio`.

---

### 5. Procesamiento de imágenes con OpenCV

El procesamiento incluyó:

#### Normalización

Las imágenes DICOM fueron convertidas al rango de 0 a 255 utilizando OpenCV para facilitar su visualización y procesamiento.

#### Ecualización de histograma

Se utilizó `cv2.equalizeHist()` para mejorar el contraste de las imágenes médicas.

#### Detección de bordes

Se aplicó el algoritmo de Canny mediante `cv2.Canny()` para resaltar contornos y estructuras anatómicas.

#### Exportación de resultados

Las imágenes procesadas fueron guardadas en formato PNG dentro de la carpeta `output`.

---

# DICOM y HL7 a

## Importancia de DICOM

DICOM es un estándar utilizado para almacenar, transmitir y visualizar imágenes médicas como radiografías, tomografías y resonancias magnéticas.

Permite que diferentes equipos médicos y sistemas PACS puedan intercambiar imágenes de forma estandarizada.

## Importancia de HL7

HL7 es un estándar enfocado en el intercambio de información clínica y administrativa, como historias clínicas, resultados de laboratorio y datos de pacientes.

## Diferencias conceptuales

- DICOM se centra principalmente en imágenes médicas y metadata asociada.
- HL7 se enfoca en información textual y comunicación entre sistemas hospitalarios.

Ambos estándares son fundamentales para garantizar interoperabilidad en salud.

---

# Ventajas y limitaciones del procesamiento aplicado

## Ventajas de la ecualización de histograma

- Mejora el contraste de imágenes médicas.
- Facilita la visualización de estructuras anatómicas.
- Puede ayudar a identificar detalles difíciles de observar.

## Limitaciones de la ecualización

- Puede amplificar ruido presente en la imagen.
- Algunas regiones pueden perder naturalidad visual.
- No siempre mejora el diagnóstico clínico.

## Ventajas del detector de bordes Canny

- Resalta contornos anatómicos importantes.
- Facilita tareas de segmentación.
- Puede utilizarse como preprocesamiento para análisis computacional.

## Limitaciones del detector de Canny

- Puede detectar ruido como bordes falsos.
- La selección de umbrales afecta mucho el resultado.
- No reemplaza interpretación médica profesional.

## Escenarios clínicos útiles

- Preprocesamiento de tomografías.
- Segmentación anatómica.
- Mejora visual en radiografías.
- Sistemas de apoyo computacional.

## Escenarios donde puede ser perjudicial

- Imágenes con mucho ruido.
- Casos donde se altere información diagnóstica original.
- Procesamientos excesivos que oculten detalles clínicos importantes.

---

# Dificultades encontradas

Durante el desarrollo se encontraron varias dificultades:

- Manejo de imágenes DICOM comprimidas.
- Compatibilidad de librerías para JPEG2000 y JPEG-LS.
- Diferencias entre imágenes grayscale y RGB.
- Manejo de tags faltantes en metadata.
- Configuración inicial de Git y GitHub.

Estas dificultades permitieron comprender mejor el funcionamiento interno del estándar DICOM y el procesamiento de imágenes médicas.

---

# Importancia de Python en análisis de datos médicos

Python es ampliamente utilizado en bioingeniería e informática médica debido a:

- Gran disponibilidad de librerías científicas.
- Facilidad para análisis de imágenes médicas.
- Integración con inteligencia artificial y machine learning.
- Automatización de procesamiento clínico.
- Manipulación eficiente de datos biomédicos.

Herramientas como NumPy, Pandas, OpenCV y pydicom facilitan el desarrollo rápido de soluciones para investigación y aplicaciones médicas.

---

# Ejecución del proyecto

Ejecutar:

```bash
py main.py
```

---

# Resultados obtenidos

El programa genera:

- Un archivo `metadata.csv` con la metadata extraída.
- Imágenes ecualizadas.
- Imágenes con detección de bordes.
- Organización automática de resultados.



