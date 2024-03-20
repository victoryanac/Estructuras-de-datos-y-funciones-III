
def choose_level(n_pregunta, p_level):
    # Convertimos los argumentos a enteros para evitar problemas con el tipo de datos
    n_pregunta = int(n_pregunta)
    p_level = int(p_level)
    
    # Calculamos el nivel basado en el rango en el que cae la pregunta.
    if n_pregunta <= p_level:
        nivel = 'basicas'
    elif n_pregunta <= 2 * p_level:
        nivel = 'intermedias'
    else:
        nivel = 'avanzadas'
    
    return nivel

