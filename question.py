import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

def choose_q(dificultad):
    global opciones
    preguntas = opciones[dificultad]    
    n_elegido = random.choice(preguntas)
    preguntas.remove(n_elegido)  # Correctamente elimina la pregunta seleccionada
        
        # Accediendo y mezclando alternativas
    pregunta = p.pool_preguntas[dificultad]['pregunta_' + str(n_elegido)]
    alternativas = shuffle_alt(pregunta['alternativas'].copy())
        
    opciones[dificultad] = preguntas  # Asegura que la lista actualizada se guarde globalmente
    return pregunta['enunciado'][0], alternativas


if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')