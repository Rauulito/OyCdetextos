#Carga del archivo
import pandas as pnd
mensajesTwitter = pnd.read_csv("datas/calentamientoClimatico.csv", delimiter=";")

import nltk
nltk.download('stopwords')
nltk.download('wordnet')

#Carga de StopWords
from nltk.corpus import stopwords
stopWords = stopwords.words('english')

#Eliminación de las Stops Words en las distintas frases
mensajesTwitter['TWEET'] = mensajesTwitter['TWEET'].apply(lambda mensaje: ' '.join([palabra for palabra in mensaje.split() if palabra not in (stopWords)]))
print(mensajesTwitter.head(10))