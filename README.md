# Proyecto: Simulador de Máquina de Turing - Sucesión de Fibonacci

## 1. Descripción de las Convenciones Elegidas
## Complejidad
- Temporal: O(n · F(n)²)
- Espacial: O(F(n))
- F(n) ≈ φⁿ/√5 (exponencial)

### Notación Unaria
Para facilitar la implementación y los cálculos, utilizaremos **notación unaria** para representar números enteros no negativos en la cinta.

#### Representación de Números:
- **0** se representa como: `B` (cinta en blanco o símbolo especial)
- **n** (donde n > 0) se representa como: `1^n` (n símbolos consecutivos de '1')
  - Ejemplo: 1 = `1`, 2 = `11`, 3 = `111`, 5 = `11111`

#### Formato de Entrada:
- **Entrada**: Un número n en notación unaria que indica qué término de Fibonacci calcular
- **Formato**: `1^n` seguido de blancos
- **Ejemplos**:
  - Para calcular F(3): entrada = `111`
  - Para calcular F(5): entrada = `11111`
  - Para calcular F(0): entrada = `B` (blanco)

#### Formato de Salida:
- **Salida**: El resultado F(n) en notación unaria
- **Formato**: La cinta contendrá `1^F(n)` 
- **Ejemplos**:
  - F(3) = 2, salida: `11`
  - F(5) = 5, salida: `11111`
  - F(6) = 8, salida: `11111111`

#### Símbolos de la Cinta:
- `1`: Representa una unidad (usado para notación unaria)
- `B`: Blanco (representa espacio vacío o inicio/fin de datos)
- `X`: Símbolo auxiliar para marcaje durante el cálculo
- `Y`: Símbolo auxiliar para marcaje durante el cálculo
- `Z`: Símbolo auxiliar para separación de secciones

### Convención de Estados:
- `q0`: Estado inicial
- `q_accept`: Estado de aceptación (final)
- `q_halt`: Estado de parada
- Estados intermedios: `q1, q2, q3, ...` según sea necesario

### Secuencia de Fibonacci:
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) para n ≥ 2

## 2. Descripción del Algoritmo de la Máquina de Turing

La máquina de Turing implementada usa una **estrategia optimizada con marcadores**:

### Ventajas de esta implementación:
- **Solo 18 estados** (vs 45+ en versiones tradicionales)
- **Estado genérico de navegación** (q_ir_inicio) que reemplaza múltiples estados
- **Marcadores A** en vez de mover bloques completos
- **Suma "in-situ"**: marca con A, escribe al final, restaura

### Estrategia:

1. **Casos base integrados**: 
   - F(0), F(1), F(2) se manejan naturalmente en el flujo

2. **Estructura de cinta para n ≥ 3**: 
   ```
   [Contador: X^(n-2)] # [F(i-1)] # [F(i-2)]
   ```

3. **Bucle principal**: 
   - Marca cada `1` en F(i-1) como `A`, escribe `1` al final
   - Lo mismo con F(i-2)
   - Restaura todos los `A` de vuelta a `1`
   - Limpia valores anteriores
   - Usa **un solo estado** (q_ir_inicio) para volver al principio

4. **Resultado**: Copia el número final al inicio y limpia

## 3. Estructura del Proyecto

```
Algoritmos/
├── README.md                    # Este archivo (documentación)
├── maquina_fibonacci.json       # Definición de la MT
├── simulador_turing.py          # Simulador de MT
├── analisis_empirico.py         # Análisis de rendimiento
└── diagrama_mt_fibonacci.txt    # Diagrama visual de la MT
```

## 4. Uso del Simulador

### Ejecutar la simulación:
```bash
python simulador_turing.py
```

El programa:
1. Carga la definición de la máquina desde `maquina_fibonacci.json`
2. Solicita la entrada en notación unaria
3. Ejecuta la simulación paso a paso
4. Muestra todas las configuraciones (estado, posición, cinta)
5. Muestra el resultado final

### Ejemplo de ejecución:
```
Ingrese la entrada (notación unaria, ej: 111 para n=3): 11111
```

## 5. Análisis Empírico

Para ejecutar el análisis empírico:
```bash
python analisis_empirico.py
```

Esto generará:
- Mediciones de tiempo para diferentes tamaños de entrada
- Diagrama de dispersión (guardado como imagen)
- Regresión polinomial ajustada a los datos
- Análisis de complejidad temporal
