import random

# Opciones posibles
opciones = ["piedra", "papel", "tijera"]

# Función para determinar el ganador de una ronda
def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "empate"
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        return "jugador"
    else:
        return "computadora"

# Función principal del juego
def jugar():
    rondas = int(input("¿Cuántas rondas quieres jugar? "))
    puntaje_jugador = 0
    puntaje_computadora = 0

    for ronda in range(0, rondas):
        print(f"\n🎲 Ronda {ronda + 1}")
        jugador = input("Elige piedra, papel o tijera: ").lower()
        if jugador not in opciones:
            print("❌ Opción inválida. Pierdes esta ronda.")
            puntaje_computadora += 1
            continue

        computadora = random.choice(opciones)
        print(f"🖥️ La computadora eligió: {computadora}")

        resultado = determinar_ganador(jugador, computadora)

        if resultado == "jugador":
            print("✅ ¡Ganaste esta ronda!")
            puntaje_jugador += 1
        elif resultado == "computadora":
            print("❌ La computadora ganó esta ronda.")
            puntaje_computadora += 1
        else:
            print("🤝 Empate.")

        print(f"📊 Puntaje actual — Tú: {puntaje_jugador} | Computadora: {puntaje_computadora}")

    print("\n🏁 Juego terminado.")
    if puntaje_jugador > puntaje_computadora:
        print("🎉 ¡Ganaste el juego!")
    elif puntaje_jugador < puntaje_computadora:
        print("😢 La computadora ganó el juego.")
    else:
        print("🤝 Empate total.")

# Ejecutar el juego solo si se corre directamente
jugar()