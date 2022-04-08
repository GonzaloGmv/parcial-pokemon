from clases.pokemon import *
from clases.fichero import *


def crear_pokemon(columna, fila, archivo):
  atributo = leer(archivo)
  atributo.lista[columna][fila]


def main():
    print("Welcome to the Game.")
    print("Let's start to set the configuration of each game user. \n")
    print("Jugador 1: \n")
    while True:
      fichero1 = input("Elija el fichero en el que esta el pokemon con el que quiere jugar (1/2)")
      if fichero1 == 1:
        fichero1 = 'coach_1_pokemons.csv'
        break
      
      elif fichero1 == 2:
        fichero1 = 'coach_2_pokemons.csv'
        break

    while True:
      n1 = input("Elija el pokemon con el que quiere jugar (0/1/2)")
      try:
          n1 == 0 or n1 == 1 or n1 ==2
      except:
          pass
      else:
          break
      
    id1 = crear_pokemon(n1, 0, fichero1)
    name1 = crear_pokemon(n1, 1, fichero1)
    weapon1 = crear_pokemon(n1, 2, fichero1)
    hp1 = crear_pokemon(n1, 3, fichero1)
    attack1 = crear_pokemon(n1, 4, fichero1)
    defense1 = crear_pokemon(n1, 5, fichero1)
    pokemon1 = Pokemon(id1, name1, weapon1, hp1, attack1, defense1)
    
    print("Jugador 2: \n")
    while True:
      fichero2 = input("Elija el fichero en el que esta el pokemon con el que quiere jugar (1/2)")
      if fichero2 == 1:
        fichero2 = 'coach_1_pokemons.csv'
        break
      
      elif fichero2 == 2:
        fichero2 = 'coach_2_pokemons.csv'
        break

    while True:
      n2 = input("Elija el pokemon con el que quiere jugar (0/1/2)")
      try:
          n2 == 0 or n2 == 1 or n2 ==2
      except:
          pass
      else:
          break
      
    id2 = crear_pokemon(n2, 0, fichero2)
    name2 = crear_pokemon(n2, 1, fichero2)
    weapon2 = crear_pokemon(n2, 2, fichero2)
    hp2 = crear_pokemon(n2, 3, fichero2)
    attack2 = crear_pokemon(n2, 4, fichero2)
    defense2 = crear_pokemon(n2, 5, fichero2)
    pokemon2 = Pokemon(id2, name2, weapon2, hp2, attack2, defense2)

    print("------------------------------------------------------------------")
    print("The Game starts...")
    print("------------------------------------------------------------------")


    print("------------------------------------------------------------------")
    print("The Game has end...")
    print("------------------------------------------------------------------")


    print("------------------------------------------------------------------")
    print("Statistics")
    print("------------------------------------------------------------------")
    print("Game User 1:")


    print("Game User 2:")


if __name__ == "__main__":
    main()