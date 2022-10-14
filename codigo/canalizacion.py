#Carga del archivo
import pandas as pnd
mensajesTwitter = pnd.read_csv("datas/calentamientoClimatico.csv", delimiter=";")



#------ Uso de SVM ------#

def canalizacion():
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


    #Definición de la canalización
    from sklearn.pipeline import Pipeline
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.feature_extraction.text import TfidfTransformer
    from sklearn import svm
    etapas_aprendizaje = Pipeline([('frequencia', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('algoritmo', svm.SVC(kernel='linear', C=2))])


    #Aprendizaje
    modelo = etapas_aprendizaje.fit(X_train,y_train)
    from sklearn.metrics import classification_report
    print(classification_report(y_test, modelo.predict(X_test), digits=4))

    #Búsqueda del mejor parámetro C
    from sklearn.model_selection import GridSearchCV
    parametrosC = {'algoritmo__C':(1,2,4,5,6,7,8,9,10,11,12)}

    busquedaCOptimo = GridSearchCV(etapas_aprendizaje, parametrosC,cv=2)
    busquedaCOptimo.fit(X_train,y_train)
    print(busquedaCOptimo.best_params_)


    #Parámetro nuevo C=1
    etapas_aprendizaje = Pipeline([('frequencia', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('algoritmo', svm.SVC(kernel='linear', C=1))])

    modelo = etapas_aprendizaje.fit(X_train,y_train)
    from sklearn.metrics import classification_report
    print(classification_report(y_test, modelo.predict(X_test), digits=4))