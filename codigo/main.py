#lanzador
# import normalizacion, InformacionTransformacion, lematizacion , canalizacion ,Stopwords, stemming
import sys
sys.path.insert(0, "/Users/Lorenzo/Documents/programacion/2.Desarrollo_OO/OyC-de-textos/codigo")
from InformacionTransformacion import Info_original
from normalizacion import normalizacion2
from Stopwords import Stop_words
from stemming import stemming
from lematizacion import lematizacion



def pruebas():
    Info_original()
    print("FASE 1: Normalización")
    normalizacion2()
    print("FASE 2: Stopwords")
    Stop_words()
    print("FASE 3: Stemming")
    stemming()
    print("FASE 4: Lematización")
    lematizacion()
    print("FASE 5: Canalización")


if __name__ == "__main__":
    pruebas()
    # print(normalizacion.normalizacion2())
