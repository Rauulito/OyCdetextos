#Carga del archivo
import pandas as pnd
mensajesTwitter = pnd.read_csv("datas/calentamientoClimatico.csv", delimiter=";")

#Aplicación de stemming
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer('english')
mensajesTwitter['TWEET'] = mensajesTwitter['TWEET'].apply(lambda mensaje: ' '.join([stemmer.stem(palabra) for palabra in mensaje.split(' ')]))
print(mensajesTwitter.head(10))


#Conjunto de aprendizaje y de prueba:
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(mensajesTwitter['TWEET'].values,  mensajesTwitter['CREENCIA'].values,test_size=0.2)


#Creación de la canalización de aprendizaje
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

etapas_aprendizaje = Pipeline([('frequencia', CountVectorizer()),
('tfidf', TfidfTransformer()),
('algoritmo', MultinomialNB())])


#Aprendizaje
modelo = etapas_aprendizaje.fit(X_train,y_train)

from sklearn.metrics import classification_report
print(classification_report(y_test, modelo.predict(X_test), digits=4))

#Frase nueva:
frase = "Why should trust scientists with global warming if they didnt know Pluto wasnt a planet"
print(frase)

#Aplicación de stemming
frase =  ' '.join([stemmer.stem(palabra) for palabra in frase.split(' ')])