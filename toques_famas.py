import matplotlib.pyplot as plt
import pandas as pd
import random

# Esta función recibe el número secreto y un intento realizado por el usuario como cadenas de texto. Cuenta los toques (cifras en el lugar correcto) y famas (cifras en el número secreto pero en lugar incorrecto) del intento en comparación con el número secreto.
# La función recorre los dígitos del intento y compara cada dígito con el número secreto para determinar si hay toques o famas. Un acierto ocurre cuando un dígito está en el mismo lugar en el intento y en el número secreto. Una coincidencia ocurre cuando un dígito está presente en el número secreto, pero en una posición diferente al intento.
def contar_toques_y_famas(numero_secreto, intento):
    # Inicializa contadores para toques (cifras en el lugar correcto) y famas (cifras en el número secreto pero en lugar incorrecto).
    toques = 0
    famas = 0

    # Compara cada dígito del intento con el número secreto y cuenta los toques y famas.
    for i in range(4):
        if intento[i] == numero_secreto[i]:
            # Si el dígito del intento está en el mismo lugar que el número secreto, aumenta las famas.
            famas += 1
        elif intento[i] in numero_secreto:
            # Si el dígito del intento está en el número secreto pero en un lugar diferente, aumenta los toques.
            toques += 1

    return toques, famas

# Esta función inicia el juego del "Número Fama". Llama a generar_numero_aleatorio_unico para obtener el número secreto y luego permite que el usuario realice intentos para adivinar el número secreto.
def iniciar_juego():
    # Define un número aleatorio.
    numero_secreto = generar_numero_aleatorio_unico()
    
    #print("Este sería el número secreto: ", numero_secreto)
    
    intentos = 0
    
    # Se utiliza un ciclo while True para mantener el juego en ejecución hasta que el usuario adivine el número secreto. En cada iteración del ciclo, recopila el intento del usuario, verifica si es válido, llama a contar_toques_y_famas para obtener los toques y famas del intento y proporciona retroalimentación al usuario. Si el usuario adivina el número, se muestra un mensaje de felicitación y se registra el número de intentos realizados.
    while True:
        intento_usuario = input(f"\nIngresa un número de 4 cifras: ")

        # Verifica que el intento sea válido (4 dígitos no repetidos).
        if not intento_usuario.isdigit() or len(intento_usuario) != 4 or len(set(intento_usuario)) != 4:
            print("¡Código de 4 cifras no repetidas!")
            continue
        
        intentos += 1
        
        # Llama a la función contar_toques_y_famas para determinar los toques y famas del intento.
        toques, famas = contar_toques_y_famas(str(numero_secreto), intento_usuario)
        print(f"toques: {toques} - famas: {famas}")
        
        # Si el usuario adivina el número secreto, muestra un mensaje de felicitación y finaliza el juego.
        if famas == 4:
            print(f"¡Buen trabajo! Número adivinado en {intentos} intentos.")
            #ranking.append(intentos)
            break
        
    return intentos

# Esta función genera un número aleatorio de 4 dígitos únicos entre 0 y 9. Los dígitos no se repiten en el número generado.
def generar_numero_aleatorio_unico():
    # Genera una lista de 4 dígitos únicos entre 0 y 9 para formar el número secreto.
    numero_secreto = random.sample(range(1, 9), 4)
    
    # Convierte la lista de dígitos en un número entero.
    numero_secreto = int(''.join(map(str, numero_secreto)))
    
    # Devuelve el número secreto generado.
    return numero_secreto

#Esta función genera el gráfico de barras a partir de los valores x = Juego, y = Cantidad de intentos.
def generaGrafico(x, y):
    plt.bar(x, y, width=0.4)
    plt.ylabel('Cantidad de intentos')
    plt.title('Ranking de los últimos 10 juegos')
    plt.show()

juegos_jugados = 0  # Inicializa el contador de juegos.
lista_juegos = [] # Inicializa una lista para almacenar el número de cada juego
ranking_total = []  # Inicializa una lista para almacenar los intentos de todos los juegos.
    
while True:  # Ciclo para permitir jugar varias veces.
    print("¡Bienvenido al juego!")
    juegos_jugados += 1  # Incrementa el contador de juegos.
    print(f"\nJuego número: ", juegos_jugados)
    
    # Se inicia el juego y se actualizan los contadores.
    lista_juegos.append('Juego ' + str(juegos_jugados))
    ranking_total.append(iniciar_juego())

    volver_a_jugar = input(f"\n¿Repetir juego? (si/no): ")
    if volver_a_jugar.lower() != 'si':        

        # Se crea un Dataframe para almacenar cada juego con su cantidad de intentos
        df = pd.DataFrame()
        df['Juego_NRO'] = lista_juegos
        df['Intentos'] = ranking_total
        # Se obtienen los últimos 10 registros del Dataframe
        ultimos10 = df.tail(10)
        # Se ordenan los últimos 10 registros de mayor a menor, según cantidad de intentos
        ultimos10 = ultimos10.sort_values('Intentos', ascending=False)

        print("¡Nos vemos!")

        # Llama a la función que genera el gráfico de barras, a partir del Dataframe "ultimos10"
        generaGrafico(ultimos10['Juego_NRO'], ultimos10['Intentos'])

        break