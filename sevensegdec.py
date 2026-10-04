"""
Decodificador de 7 Segmentos
Generador de HDL (VHDL) y simulador usando MyHDL.
"""
from myhdl import block, always_comb, instance, delay, Signal, intbv

def cargar_tabla(ruta_archivo: str) -> tuple:
    """Lee la tabla de verdad y la convierte en una tupla inmutable."""
    with open(ruta_archivo, 'r') as archivo:
        lineas = archivo.read().splitlines()
    # Retorna tupla para garantizar que MyHDL la sintetice como ROM/LUT
    return tuple(int(linea.strip(), 2) for linea in lineas if linea.strip())

@block
def decodificador_7seg(entrada, salida_segmentos, tabla_referencia):
    """Módulo combinacional del decodificador."""
    @always_comb
    def logica_combinacional():
        salida_segmentos.next = tabla_referencia[int(entrada)]
    return logica_combinacional

@block
def entorno_simulacion():
    """Testbench moderno para generar las formas de onda."""
    tabla = cargar_tabla("tabla.txt")
    entrada_test = Signal(intbv(0)[4:])
    salida_test = Signal(intbv(0)[7:])
    
    # Instancia del módulo a probar (DUT)
    dut = decodificador_7seg(entrada_test, salida_test, tabla)
    
    @instance
    def estimulos():
        for valor in range(16):
            entrada_test.next = valor
            yield delay(10)
            
    return dut, estimulos

if __name__ == '__main__':
    # 1. Ejecutar simulación y exportar archivo VCD
    simulacion = entorno_simulacion()
    simulacion.config_sim(trace=True)
    simulacion.run_sim()
    print("-> Simulación exitosa: 'entorno_simulacion.vcd' generado.")
    
    # 2. Generar el código fuente en VHDL
    tabla_vhd = cargar_tabla("tabla.txt")
    din = Signal(intbv(0)[4:])
    sseg = Signal(intbv(0)[7:])
    decodificador = decodificador_7seg(din, sseg, tabla_vhd)
    decodificador.convert(hdl='VHDL')
    print("-> Síntesis exitosa: Archivo VHDL generado.")