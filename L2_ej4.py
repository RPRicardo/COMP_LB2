class AFD:
    def __init__(self):
        
        
        # Mapeo de nombres de estados del AFD (para facilitar la lectura)
        # A = {p, q, r}
        # B = {q, r}
        # C = {r}
        # D = ∅ (estado sumidero)
        
        self.estados = {'A', 'B', 'C', 'D'}
        self.alfabeto = {'0', '1'}
        self.estado_inicial = 'A'  # Clausura-ε(p) = {p, q, r}
        self.estados_finales = {'A', 'B', 'C'}  # Todos los conjuntos que contienen r
        
        # Función de transición del AFD resultante
        self.transiciones = {
            'A': {'0': 'B', '1': 'C'},  # δ(clausura-ε(p), 0) y δ(clausura-ε(p), 1)
            'B': {'0': 'B', '1': 'D'},  # δ(clausura-ε(q,r), 0) y δ(clausura-ε(q,r), 1)
            'C': {'0': 'D', '1': 'D'},  # δ(clausura-ε(r), 0) y δ(clausura-ε(r), 1)
            'D': {'0': 'D', '1': 'D'}   # Estado sumidero
        }
        
        # Mapeo para mostrar qué estados del AFN corresponden a cada estado del AFD
        self.mapeo_estados = {
            'A': '{p, q, r}',
            'B': '{q, r}',
            'C': '{r}',
            'D': '∅'
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
        
        # Muestra el camino de transiciones con los estados correspondientes del AFN
        print("Camino de estados:")
        for i, estado in enumerate(camino):
            if i < len(cadena):
                simbolo = cadena[i]
                print(f"{estado} {self.mapeo_estados[estado]} --({simbolo})--> ", end="")
            else:
                print(f"{estado} {self.mapeo_estados[estado]}")
        
        # Resultado final
        print(f"Resultado: {mensaje}")
        print(f"¿Cadena aceptada? {'Sí' if aceptada else 'No'}")
        print("-" * 50)
        
        return aceptada

# Ejemplo de uso
if __name__ == "__main__":
    automata = AFD()
    
    # Prueba con las cadenas solicitadas
    pruebas = ["", "0", "1", "00", "10", "100"]
    
    print("SIMULACIÓN DEL AFD RESULTANTE DE LA CONVERSIÓN")
    print("=" * 60)
    print("Alfabeto: {0, 1}")
    print("Estados del AFD y su correspondencia con el AFN original:")
    for estado, conjuntos in automata.mapeo_estados.items():
        print(f"  {estado}: {conjuntos}")
    print(f"Estado inicial: {automata.estado_inicial} {automata.mapeo_estados[automata.estado_inicial]}")
    print(f"Estados finales: {automata.estados_finales}")
    print("Función de transición del AFD resultante:")
    print("  | 0 | 1 ")
    print("--+---+---")
    for estado in ['A', 'B', 'C', 'D']:
        print(f"{estado} | {automata.transiciones[estado]['0']} | {automata.transiciones[estado]['1']}")
    print("=" * 60)
    
    for cadena in pruebas:
        automata.mostrar_detalle_procesamiento(cadena)
    
    
    print("\n Ingrese una cadena para procesar (o 'salir' para terminar)")
    while True:
        entrada = input("\nCadena a procesar: ")
        if entrada.lower() == "salir":
            break
        automata.mostrar_detalle_procesamiento(entrada)