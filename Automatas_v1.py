# Simulación de autómatas finitos en Python

# --- AFD1 ---

def afd1(cadena):
    estado = 'p'
    for simbolo in cadena:
        if estado == 'p':
            estado = 'q' if simbolo == 'a' else 'r'
        elif estado == 'q':
            estado = 'q' if simbolo == 'a' else 'r'
        elif estado == 'r':
            estado = 'r'
    return estado == 'q'

# Casos de uso
casos_afd1 = ['a', 'b', 'aa', 'bb', 'abab', 'baba']
print("AFD1:")
for caso in casos_afd1:
    print(f"Cadena: {caso}, Aceptada: {afd1(caso)}")

# --- AFD2 con estado trampa ---

def afd2(cadena):
    estado = 's0'
    for simbolo in cadena:
        if estado == 's0':
            estado = 's1' if simbolo == '0' else 'sT'
        elif estado == 's1':
            estado = 's1' if simbolo == '0' else 's2'
        elif estado == 's2':
            estado = 's3' if simbolo == '0' else 's1'
        elif estado == 's3':
            estado = 's3'
        elif estado == 'sT':
            estado = 'sT'
    return estado == 's3'

# Casos de uso
casos_afd2 = ['000', '110', '1001', '0110', '111']
print("\nAFD2:")
for caso in casos_afd2:
    print(f"Cadena: {caso}, Aceptada: {afd2(caso)}")

# --- AFN ---

def afn(cadena):
    estados = {'t0'}
    for simbolo in cadena:
        nuevos_estados = set()
        for estado in estados:
            if estado == 't0' and simbolo == 'a':
                nuevos_estados.update(['t0', 't1'])
            elif estado == 't1' and simbolo == 'b':
                nuevos_estados.update(['t2', 't3'])
            elif estado == 't2' and simbolo == 'a':
                nuevos_estados.add('t3')
        estados = nuevos_estados
    return 't2' in estados or 't3' in estados

# Casos de uso
casos_afn = ['a', 'b', 'ab', 'ba', 'aab', 'abb']
print("\nAFN:")
for caso in casos_afn:
    print(f"Cadena: {caso}, Aceptada: {afn(caso)}")

# --- AFN con ε-transiciones ---
def afn_epsilon(cadena):
    estado = 'p'
    for simbolo in cadena:
        if estado == 'p':
            estado = 'r' if simbolo == 'ε' else 'q'
        elif estado == 'q':
            estado = 'q' if simbolo == '0' else 'r'
        elif estado == 'r':
            estado = 'r' if simbolo == '1' else estado
    return estado == 'r'

# Casos de uso
casos_afn_epsilon = ['ε', '0', '00', '01', '10', '0001']
print("\nAFN con ε-transiciones:")
for caso in casos_afn_epsilon:
    print(f"Cadena: {caso}, Aceptada: {afn_epsilon(caso)}")
