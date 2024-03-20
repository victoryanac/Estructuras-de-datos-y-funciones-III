# Definición de las preguntas básicas
preguntas_basicas = {
    'pregunta_1': {'enunciado': ['¿Cuál es la capital de Francia?'],
                   'alternativas': [['Londres', 0],
                                    ['París', 1],
                                    ['Berlín', 0],
                                    ['Madrid', 0]]},
    'pregunta_2': {'enunciado': ['¿Quién pintó la Mona Lisa?'],
                   'alternativas': [['Vincent Van Gogh', 0],
                                    ['Leonardo da Vinci', 1],
                                    ['Pablo Picasso', 0],
                                    ['Claude Monet', 0]]},
    'pregunta_3': {'enunciado': ['¿Cuál es el río más largo del mundo?'],
                'alternativas': [['Nilo', 0],
                                    ['Amazonas', 1],
                                    ['Yangtsé', 0],
                                    ['Misisipi', 0]]}
}

# Definición de las preguntas intermedias
preguntas_intermedias = {
    'pregunta_1': {'enunciado': ['¿En qué año llegó el hombre a la Luna?'],
                'alternativas': [['1969', 1],
                                    ['1972', 0],
                                    ['1965', 0],
                                    ['1980', 0]]},
    'pregunta_2': {'enunciado': ['¿Cuál es el elemento químico más abundante en la atmósfera terrestre?'],
                'alternativas': [['Oxígeno', 0],
                                    ['Hidrógeno', 0],
                                    ['Nitrógeno', 1],
                                    ['Carbono', 0]]},
    'pregunta_3': {'enunciado': ['¿Quién escribió "Cien años de soledad"?'],
                'alternativas': [['Gabriel García Márquez', 1],
                                    ['Mario Vargas Llosa', 0],
                                    ['Julio Cortázar', 0],
                                    ['Jorge Luis Borges', 0]]}
}

# Definición de las preguntas avanzadas
preguntas_avanzadas = {
    'pregunta_1': {'enunciado': ['¿Cuál es la fórmula química del agua?'],
                'alternativas': [['CO2', 0],
                                    ['H2O', 1],
                                    ['NaCl', 0],
                                    ['O2', 0]]},
    'pregunta_2': {'enunciado': ['¿Qué filósofo dijo "Solo sé que no sé nada"?'],
                'alternativas': [['Platón', 0],
                                    ['Sócrates', 1],
                                    ['Aristóteles', 0],
                                    ['Descartes', 0]]},
    'pregunta_3': {'enunciado': ['¿Cuál es el país más grande del mundo?'],
                'alternativas': [['China', 0],
                                    ['Estados Unidos', 0],
                                    ['Canadá', 0],
                                    ['Rusia', 1]]}
}

# Agrupar todas las preguntas en un solo diccionario
pool_preguntas = {'basicas': preguntas_basicas,
                'intermedias': preguntas_intermedias,
                'avanzadas': preguntas_avanzadas}
