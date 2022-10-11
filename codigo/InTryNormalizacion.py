
#Carga del archivo
import pandas as pnd
mensajesTwitter = pnd.read_csv("datas/calentamientoClimatico.csv", delimiter=";")

#Información sobre la cantidad de observaciones y su contenido
print(mensajesTwitter.shape)
print(mensajesTwitter.head(2))

#Transformación de la característica Creencia
mensajesTwitter['CREENCIA'] = (mensajesTwitter['CREENCIA']=='Yes').astype(int)
print(mensajesTwitter.head(100))

#Función de normalización
import re
def normalizacion(mensaje):
    mensaje = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL', mensaje)
    mensaje = re.sub('@[^\s]+','USER', mensaje)
    mensaje = mensaje.lower().replace("ё", "е")
    mensaje = re.sub('[^a-zA-Zа-яА-Я1-9]+', ' ', mensaje)
    mensaje = re.sub(' +',' ', mensaje)
    return mensaje.strip()


#Normalización
mensajesTwitter["TWEET"] = mensajesTwitter["TWEET"].apply(normalizacion)
print(mensajesTwitter.head(10))