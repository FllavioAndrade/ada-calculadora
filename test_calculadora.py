# tests/test_calculadora.py

import pytest
from calculadora import soma  # Importe a função que você deseja testar

def test_soma():
    assert soma(1, 2) == 3
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0
    assert soma(-1, -1) == -2

if __name__ == "__main__":
    pytest.main()
