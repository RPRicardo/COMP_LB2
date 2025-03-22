class AFD2:
    def __init__(self):
        # Estados: q0=0, q1=1, q2=2, q3=3, qT=4 (trampa)
        # Tabla de transición
        self.transitions = {
            0: {'0': 1, '1': 4},  # q0
            1: {'0': 1, '1': 2},  # q1
            2: {'0': 3, '1': 1},  # q2
            3: {'0': 4, '1': 3},  # q3
            4: {'0': 4, '1': 4}   # qT (trampa)
        }
        self.initial_state = 0    # q0
        self.final_states = {3}   # q3

    def simulate(self, input_string):
        """Simula el autómata para la cadena de entrada dada."""
        current_state = self.initial_state
        path = [current_state]
        
        print(f"Procesando cadena: '{input_string}'")
        print(f"Estado inicial: q{current_state}")
        
        for idx, symbol in enumerate(input_string):
            if symbol not in '01':
                print(f"Símbolo no válido: '{symbol}'")
                return False
            
            current_state = self.transitions[current_state][symbol]
            path.append(current_state)
            
            state_name = f"q{current_state}" if current_state != 4 else "qT"
            print(f"  Paso {idx+1}: Leyendo '{symbol}', transición a estado {state_name}")
            
            if current_state == 4:  # Estado trampa
                print("  ¡Llegamos al estado trampa! La cadena será rechazada.")
        
        is_accepted = current_state in self.final_states
        state_name = f"q{current_state}" if current_state != 4 else "qT"
        print(f"Estado final: {state_name}")
        print(f"La cadena '{input_string}' es {'aceptada' if is_accepted else 'rechazada'}.")
        
        path_str = []
        for s in path:
            path_str.append(f"q{s}" if s != 4 else "qT")
        print(f"Recorrido: {' -> '.join(path_str)}")
        
        return is_accepted

# Casos de prueba
if __name__ == "__main__":
    afd = AFD2()
    
    print("=== AUTÓMATA FINITO DETERMINISTA CON ESTADO TRAMPA (EJERCICIO 2) ===")
    print("Tabla de transición:")
    print("   | 0  | 1  |")
    print("---+----+----+")
    print("q0 | q1 | qT |")
    print("q1 | q1 | q2 |")
    print("q2 | q3 | q1 |")
    print("q3 | qT | q3 |")
    print("qT | qT | qT |")
    print("\nEstado inicial: q0")
    print("Estado final: q3")
    print("\nExpresión regular equivalente: 0(0)*10(1)*")
    print("Descripción del lenguaje: Cadenas que empiezan con al menos un 0, seguido por un 1, luego un 0, y finalmente cualquier número de 1's.")
    
    print("\n--- Cadenas aceptadas ---")
    accepted_strings = ["010", "0010", "00010", "0101", "01011", "010111"]
    for s in accepted_strings:
        afd.simulate(s)
        print()
    
    print("\n--- Cadenas rechazadas ---")
    rejected_strings = ["", "0", "1", "00", "11", "01", "100", "001", "0100"]
    for s in rejected_strings:
        afd.simulate(s)
        print()