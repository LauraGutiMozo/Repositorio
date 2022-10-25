import math
def numero_primo (numero:int)-> bool:
    assert isinstance (numero, int) and (numero >=0), "el número debe ser positivo"

    if 1 < numero < 4: