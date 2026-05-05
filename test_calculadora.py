from calculadora import Calculadora


def test_soma():
    #arrange
    calc = Calculadora()
    a = 2
    b = 3

    #act
    #chamada da função a ser testada
    #Inteiros positivos
    assert calc.soma(2, 3) == 5

    #Inteiros negativos
    assert calc.soma(-7, 4) == -3

    #ponto flutuante
    assert calc.soma(2.5, 3.1) == 5.6

def test_subtracao():
    calc = Calculadora()

    #Inteiros positivos
    assert calc.subtracao(5 , 2) == 3

    #Inteiros negativos 
    assert calc.subtracao(-7, -4) == -3

    #ponto flutuante
    assert calc.subtracao(5.5, 2.2) == 3.3

def test_multiplicacao():
    calc = Calculadora()

    #Inteiros positivos
    assert calc.multiplicacao(4, 3) == 12

    #Inteiros negativos
    assert calc.multiplicacao(-5, 6) == -30

    #ponto flutuante
    assert calc.multiplicacao(2.5, 4.0) == 10.0

def test_divisao():
    calc = Calculadora()

    #Inteiros positivos
    assert calc.divisao(10, 2) == 5

    #Inteiros negativos
    assert calc.divisao(-15, 3) == -5

    #ponto flutuante
    assert calc.divisao(7.5, 2.5) == 3.0
