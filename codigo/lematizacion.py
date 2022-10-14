#Carga del archivo
import pandas as pnd
mensajesTwitter = pnd.read_csv("/Users/Lorenzo/Documents/programacion/2.Desarrollo_OO/OyC-de-textos/codigo/datas/calentamientoClimatico.csv", delimiter=";")

#Añadimos el modulo nltk con la version necesaria
import nltk
nltk.download('omw-1.4')
def lematizacion():
    #Lematización
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    mensajesTwitter['TWEET'] = mensajesTwitter['TWEET'].apply(lambda mensaje: ' '.join([lemmatizer.lemmatize(palabra) for palabra in mensaje.split(' ')]))
    print(mensajesTwitter.head(10))

    print("¡Fin de la preparación!")

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

    #Lematización
    frase = ' '.join([lemmatizer.lemmatize(palabra) for palabra in frase.split(' ')])
    print (frase)