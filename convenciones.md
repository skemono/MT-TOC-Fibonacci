# Convenciones de la Máquina de Turing - Fibonacci

## 1. Representación de Enteros (Entrada)
Utilizamos notación unaria para representar números enteros no negativos.
- El número `N` se representa como una secuencia de `N` unos (`1`).
- Ejemplos:
  - `0`: (Cadena vacía o `B`)
  - `1`: `1`
  - `2`: `11`
  - `3`: `111`
- La entrada debe estar colocada al inicio de la cinta.

## 2. Interpretación de la Respuesta (Salida)
Dado que la máquina utiliza la cinta para cálculos intermedios y almacena la secuencia de números de Fibonacci generados:
- La cinta contendrá bloques de unos separados por símbolos especiales (`#`, `B` u otros marcadores).
- **Convención de Salida:** El resultado `F(N)` se define como el **bloque con mayor cantidad de unos consecutivos** presente en la cinta al finalizar la ejecución.
- Esta convención es robusta frente a residuos de cálculo o estados intermedios de la cinta.

## 3. Componentes de la Máquina
La máquina se define en el archivo `maquina_fibonacci.json` e incluye:
- Alfabeto de entrada: `{1, B}`
- Alfabeto de cinta: `{1, B, X, A, #, S, 2}`
- Estado inicial: `q0`
- Estados de aceptación: `{q_accept}`
