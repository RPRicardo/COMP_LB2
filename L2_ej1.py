class AFD:
    def __init__(self, estado_inicial='q1', estados_finales={'q4'}):
        # Definición del AFD 
        self.estados = {'q1', 'q2', 'q3', 'q4'}
        self.alfabeto = {'a', 'b'}
        self.estado_inicial = estado_inicial
        self.estados_finales = estados_finales
        
        #función de transición
        self.transiciones = {
            'q1': {'a': 'q2', 'b': 'q1'},
            'q2': {'a': 'q3', 'b': 'q4'},
            'q3': {'a': 'q4', 'b': 'q2'},
            'q4': {'a': 'q1', 'b': 'q3'}
        }
    
    def procesar_cadena(self, cadena):
        """Procesa una cadena y determina si es aceptada por el AFD."""
        estado_actual = self.estado_inicial
        
        # Registra el camino de estados
        camino = [estado_actual]
        
        # Procesa cada símbolo de la cadena
        for simbolo in cadena:
            if simbolo not in self.alfabeto:
                return False, camino, f"Símbolo '{simbolo}' no está en el alfabeto"
            
            # Aplica la transición
            estado_actual = self.transiciones[estado_actual][simbolo]
            camino.append(estado_actual)
        
        # Verifica si terminamos en un estado final
        aceptada = estado_actual in self.estados_finales
        
        return aceptada, camino, "Cadena aceptada" if aceptada else "Cadena rechazada"
    
    def mostrar_detalle_procesamiento(self, cadena):
        """Muestra el detalle del procesamiento de una cadena."""
        aceptada, camino, mensaje = self.procesar_cadena(cadena)
        
        print(f"Procesando cadena: '{cadena}'")
        
        # Muestra el camino de transiciones
        print("Camino de estados:")
        for i, estado in enumerate(camino):
            if i < len(cadena):
                print(f"{estado} --({cadena[i]})--> ", end="")
            else:
                print(estado)
        
        # Resultado final
        print(f"Resultado: {mensaje}")
        print(f"¿Cadena aceptada? {'Sí' if aceptada else 'No'}")
        print("-" * 50)
        
        return aceptada

# Ejemplo de uso
if __name__ == "__main__":
    automata = AFD()
    
    # Prueba con algunas cadenas
    pruebas = ["ab", "aaa", "abba", "bab", "aaaaba", "ababab", ""]
    
    print("SIMULACIÓN DE AUTÓMATA FINITO DETERMINISTA")
    print("=" * 50)
    print("Alfabeto: {a, b}")
    print("Estados: {q1, q2, q3, q4}")
    print("Estado inicial: q1")
    print("Estados finales: {q4}")
    print("Función de transición:")
    print("  | a  | b ")
    print("--+----+----")
    print("q1| q2 | q1")
    print("q2| q3 | q4")
    print("q3| q4 | q2")
    print("q4| q1 | q3")
    print("=" * 50)
    
    for cadena in pruebas:
        automata.mostrar_detalle_procesamiento(cadena)
    
    
    print("\nIngrese una cadena para procesar (o 'salir' para terminar)")
    while True:
        entrada = input("\nCadena a procesar: ")
        if entrada.lower() == "salir":
            break
        automata.mostrar_detalle_procesamiento(entrada)