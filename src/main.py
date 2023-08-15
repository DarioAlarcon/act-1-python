import random

options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0

rounds = 1

while True:

    print('*' * 10)
    print('Ronda', rounds)
    print('*' * 10)

    print('puntos de la maquina', computer_wins)
    print('puntos del usuario', user_wins)

    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()

    rounds += 1

    if not user_option in options:
      print('esa opcion no es valida')
      continue

    computer_option = random.choice(options)

    print('opcion del usuario =>', user_option)
    print('opcion de la maquina =>', computer_option)

    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('gano el usuario!')
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print('gano la maquina!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('gano el usuario')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('gano la maquina!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('gano el usuario')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('gano la maquina!')
            computer_wins += 1

    if computer_wins == 2:
      print('El ganador es la computadora')
      break

    if user_wins == 2:
      print('El ganador es el usuario')
      break

    