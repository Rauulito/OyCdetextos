#Carga del archivo
import pandas as pnd
mensajesTwitter = pnd.read_csv("datas/calentamientoClimatico.csv", delimiter=";")

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
def normalizacion2():
    mensajesTwitter["TWEET"] = mensajesTwitter["TWEET"].apply(normalizacion)
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

    #Normalización
    frase = normalizacion(frase)
