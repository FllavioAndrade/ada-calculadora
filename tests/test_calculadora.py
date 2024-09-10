import pytest
from calculadora import soma, subtracao, multiplicacao, divisao

def test_soma():
    assert soma(3, 2) == 5

def test_subtracao():
    assert subtracao(5, 2) == 3

def test_multiplicacao():
    assert multiplicacao(3, 2) == 6

def test_divisao():
    assert divisao(6, 2) == 3
    assert divisao(5, 0) == "Erro: Divisão por zero!"
