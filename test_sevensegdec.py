"""
Pruebas unitarias para el decodificador de 7 segmentos usando Pytest.
"""
import pytest
from myhdl import Signal, intbv, Simulation, delay, instance
from sevensegdec import cargar_tabla, decodificador_7seg

TABLA_VERDAD = cargar_tabla("tabla.txt")

@pytest.mark.parametrize("valor_entrada", range(16))
def test_precision_decodificador(valor_entrada):
    """Verifica que la salida combinacional coincida con la tabla de diseño."""
    entrada = Signal(intbv(0)[4:])
    salida = Signal(intbv(0)[7:])
    
    dut = decodificador_7seg(entrada, salida, TABLA_VERDAD)
    
    @instance
    def verificador():
        entrada.next = valor_entrada
        yield delay(5)
        
        valor_esperado = int(TABLA_VERDAD[valor_entrada])
        resultado_actual = int(salida)
        
        # Validación estricta
        assert resultado_actual == valor_esperado, (
            f"Fallo en entrada {valor_entrada}: "
            f"Esperado {bin(valor_esperado)}, Obtenido {bin(resultado_actual)}"
        )
        
    sim = Simulation(dut, verificador)
    sim.run(10)