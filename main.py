from procesador_dicom import ProcesadorDICOM
#carpeta donde están los archivos DICOM
carpeta ="data/dicom"
#crear objeto
procesador = ProcesadorDICOM(carpeta)
#cargar archivos DICOM
procesador.cargar_archivos()
#Extraer metadata
procesador.extraer_metadata()
#Crear DataFrame
df = procesador.crear_dataframe()
#calcular intendidad promedio 
df = procesador.calcular_intesidad_promedio(df)
#mostrar DataFrame
print(df)
#procesar imagenes
procesador.procesar_imagenes()
#guardar CSV
df.to_csv("metadata.csv", index=False)
print("Archivo CSV guardado correctamente")
