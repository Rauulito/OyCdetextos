#Carga del archivo
import pandas as pnd
mensajesTwitter = pnd.read_csv("datas/calentamientoClimatico.csv", delimiter=";")

import nltk
nltk.download('stopwords')
nltk.download('wordnet')


#Aplicación de stemming
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer('english')
mensajesTwitter['TWEET'] = mensajesTwitter['TWEET'].apply(lambda mensaje: ' '.join([stemmer.stem(palabra) for palabra in mensaje.split(' ')]))
print(mensajesTwitter.head(10))

#Lematización
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
mensajesTwitter['TWEET'] = mensajesTwitter['TWEET'].apply(lambda mensaje: ' '.join([lemmatizer.lemmatize(palabra) for palabra in mensaje.split(' ')]))
print(mensajesTwitter.head(10))

print("¡Fin de la preparación!")