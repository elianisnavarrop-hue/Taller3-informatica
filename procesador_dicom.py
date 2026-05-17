import os 
import pydicom
import numpy as np
import pandas as pd
import cv2


class ProcesadorDICOM: 
    def __init__(self, carpeta_dicom): 
        self.carpeta_dicom = carpeta_dicom
        self.archivos = []
        self.metadata = []
    def cargar_archivos(self):
        for archivo in os.listdir(self.carpeta_dicom):
            ruta_completa = os.path.join(self.carpeta_dicom, archivo)
            try: 
                dicom = pydicom.dcmread(ruta_completa)
                self.archivos.append(dicom)
                print(f" Archivo cargado: {archivo}")
            except Exception as e:
                print(f"Error al cargar {archivo}: {e}")

    def extraer_metadata(self):
        for dicom in self.archivos:
           datos = {
               "PatientID": getattr(dicom, "PatientID", "No disponible"),

               "PatientName": str(getattr(dicom, "PatientName", "No disponible")),
               
               "StudyInstanceUID": getattr(dicom, "StudyInstanceUID", "No disponible"),

               "StudyDescription": getattr(dicom, "StudyDescription", "No disponible"),

               "StudyDate": getattr(dicom, "StudyDate", "No disponible"),

                "Modality": getattr(dicom, "Modality", "No disponible"),

                "Rows": getattr(dicom, "Rows", 0),
                "Columns": getattr(dicom, "Columns", 0)

           }
           self.metadata.append(datos)
    def crear_dataframe(self):
        df = pd.DataFrame(self.metadata)
        return df
    
    def calcular_intesidad_promedio(self, df): 
        intensidades = []
        for dicom in self.archivos:
            try: 
                imagen= dicom.pixel_array
                promedio = np.mean(imagen)
                intensidades.append(promedio)
            except: 
                intensidades.append(None)

        df["IntensidadPromedio"] = intensidades
        return df
    
    def procesar_imagenes(self): 

        os.makedirs("output/equalized", exist_ok=True)
        os.makedirs("output/edges", exist_ok=True)

        for i, dicom in enumerate(self.archivos):
            try: 
                imagen = dicom.pixel_array
                if len(imagen.shape) ==3:
                    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
                imagen_normalizada = cv2.normalize(imagen, None, 0, 255, cv2.NORM_MINMAX)
                imagen_normalizada = np.uint8(imagen_normalizada)
                imagen_equalizada = cv2.equalizeHist(imagen_normalizada)
                bordes = cv2.Canny(imagen_equalizada, 100, 200)
                cv2.imwrite(f"output/equalized/imagen_{i}.png", imagen_equalizada)
                cv2.imwrite(f"output/edges/bordes_{i}.png", bordes)
                print(f"Imagen procesada {i}")

            except Exception as e:
                print(f"Error al procesar la imagen {i}: {e}")


      