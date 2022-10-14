#Carga del archivo
import pandas as pnd
mensajesTwitter = pnd.read_csv("datas/calentamientoClimatico.csv", delimiter=";")

import nltk
nltk.download('stopwords')
nltk.download('wordnet')



def Info_original():
    #Información sobre la cantidad de observaciones y su contenido
    print(mensajesTwitter.shape)
    print(mensajesTwitter.head(2))

    #Transformación de la característica Creencia
    mensajesTwitter['CREENCIA'] = (mensajesTwitter['CREENCIA']=='Yes').astype(int)
    print(mensajesTwitter.head(100))

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

    prediccion = modelo.predict([frase])
    print(prediccion)
    if(prediccion[0]==0):
        print(">> No cree en el calentamiento climático...")
    else:
        print(">> Cree en el calentamiento climático...")