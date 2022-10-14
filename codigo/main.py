#lanzador
import sys
sys.path.insert(0, "/Users/Lorenzo/Documents/programacion/5.archivos_utiles/OyCdetextos/codigo")
from InformacionTransformacion import Info_original
from normalizacion import normalizacion2
from Stopwords import Stop_words
from stemming import stemming
from lematizacion import lematizacion
from canalizacion import canalizacion



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
    canalizacion()


if __name__ == "__main__":
    pruebas()
