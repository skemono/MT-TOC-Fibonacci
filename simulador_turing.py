import json
import sys

class MaquinaTuring:
    def __init__(self, archivo):
        with open(archivo, 'r') as f: config = json.load(f)
        self.transiciones = {(t['estado_actual'], t['simbolo_leido']): 
                           (t['estado_siguiente'], t['simbolo_escrito'], t['movimiento']) 
                           for t in config['transiciones']}
        self.inicial = config['estado_inicial']
        self.aceptacion = config['estados_aceptacion']
        self.blanco = config['simbolo_blanco']
        self.cinta = []
        self.cabezal = 0
        self.estado = ""

    def ejecutar(self, entrada, mostrar_configs=False):
        self.cinta = list(entrada) if entrada else [self.blanco]
        self.cabezal = 0
        self.estado = self.inicial
        pasos = 0
        
        while self.estado not in self.aceptacion:
            # Expandir cinta dinámicamente
            if self.cabezal < 0: 
                self.cinta.insert(0, self.blanco)
                self.cabezal = 0
            if self.cabezal >= len(self.cinta): 
                self.cinta.append(self.blanco)
            
            simbolo = self.cinta[self.cabezal]
            
            if mostrar_configs:
                # Mostrar configuración actual
                cinta_str = "".join(self.cinta).rstrip(self.blanco) or self.blanco
                print(f"Paso {pasos}: Estado={self.estado}, Cabezal={self.cabezal}, Cinta={cinta_str}")
            
            if (self.estado, simbolo) not in self.transiciones:
                break
            
            nuevo_estado, nuevo_simbolo, mov = self.transiciones[(self.estado, simbolo)]
            self.cinta[self.cabezal] = nuevo_simbolo
            self.cabezal += 1 if mov == 'R' else -1
            self.estado = nuevo_estado
            pasos += 1
            
            if pasos > 500000: # Safety limit
                print("Límite de pasos excedido")
                break

        # Interpretación del resultado:
        # Convención: La cinta contiene la secuencia de Fibonacci separada por '#'.
        # El resultado final es el bloque más grande de unos (convención robusta).
        resultado_raw = "".join(self.cinta)
        bloques = resultado_raw.replace('B', '#').split('#')
        unos = 0
        if bloques:
             unos = max(b.count('1') for b in bloques)
        
        return unos, pasos

if __name__ == "__main__":
    import os
    
    archivo_mt = "maquina_fibonacci.json"
    
    # Permitir pasar el archivo JSON como primer argumento
    if len(sys.argv) > 1 and sys.argv[1].endswith('.json'):
        archivo_mt = sys.argv[1]
        # Eliminamos el argumento para no confundir con la entrada si se pasa después
        sys.argv.pop(1)
    elif len(sys.argv) == 1:
         # Si no hay argumentos, preguntar al usuario (o usar default si enter)
        entrada_usuario = input(f"Ingrese archivo de configuración [{archivo_mt}]: ").strip()
        if entrada_usuario:
            archivo_mt = entrada_usuario

    if not os.path.exists(archivo_mt):
        print(f"Error: El archivo '{archivo_mt}' no existe.")
        sys.exit(1)

    mt = MaquinaTuring(archivo_mt)
    print(f"Cargada máquina: {archivo_mt}")

    if len(sys.argv) > 1:
        # Modo archivo (argumento restante es la entrada)
        res, pasos = mt.ejecutar(sys.argv[1], mostrar_configs=True)
        print(f"Entrada: {len(sys.argv[1])}, Salida: {res} (Pasos: {pasos})")
    else:
        # Modo interactivo
        print("Simulador MT")
        entrada = input("Ingrese entrada en unario (ej. 111): ")
        print("\nConfiguraciones:")
        res, pasos = mt.ejecutar(entrada, mostrar_configs=True)
        print(f"\nResultado (bloque más grande de 1s) = {res}")
        print(f"Pasos totales: {pasos}")
