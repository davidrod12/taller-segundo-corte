# taller-segundo-corte


**Autor:** Oscar Rodriguez 
**Programa:** Tecnología en Desarrollo de Software | Universidad de San Buenaventura  

## 1. Diseño de Patrones (Tabla de Decodificación)
El diseño cumple con los requisitos del taller, estableciendo decisiones explícitas para los caracteres ambiguos y diseñando símbolos personalizados para los valores hexadecimales superiores (evitando las letras A-F).

* **0-9:** Patrones estándar. El **1** se dibuja a la derecha, el **6** cerrado (segmento A encendido) y el **9** cerrado (segmento D encendido).
* **10 (Signo Menos `-`):** Útil para indicar números negativos en calculadoras.
* **11 (Líneas Paralelas `||`):** Indicador de estado de "pausa" en un sistema.
* **12 (Cuadro Superior):** Indicador visual de carga alta.
* **13 (Cuadro Inferior):** Indicador visual de carga baja.
* **14 (Tres Rayas `_ - ¯`):** Símbolo de "procesando" o "cargando".
* **15 (Letra `u` minúscula):** Símbolo genérico para interfaces de usuario.

## 2. Ejecución y Comandos
* **Generar VHDL y simulación (.vcd):** `python sevensegdec.py`
* **Ejecutar marco de pruebas unitarias:** `pytest test_sevensegdec.py -v`

## 3. Análisis de Resultados
* **Validación del Testbench:** El entorno de simulación (o testbench) automatiza la inyección de los 16 estados posibles en el puerto de entrada del decodificador. Tras un breve retardo de propagación, captura la salida del módulo y la contrasta contra una lectura de la tabla original.
* **Ausencia de Errores:** Las aserciones pasan exitosamente y de forma silenciosa porque la fuente de verdad (la tabla `.txt`) se utiliza tanto para sintetizar la lógica combinacional del módulo como para realizar la validación en la prueba.
* **Señal `sseg` (7 bits):** Representa un bus de datos paralelo donde cada bit controla el flujo de corriente hacia uno de los siete LEDs del display físico, siguiendo la convención industrial `a,b,c,d,e,f,g`.
* **Síntesis HDL:** El script `sevensegdec.py` transforma la tabla de búsqueda (Look-Up Table) en una estructura combinacional (un bloque `with/select` en VHDL), logrando que el mapeo entre la entrada y la salida sea instantáneo y sin depender de un reloj.

