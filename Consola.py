import random

def entrada():
  while True:
    try:
      j = tuple(map(int, input("Elige la ficha: ").split()))
      break
    except ValueError:
      print("Solo se permiten números enteros. Inténtalo de nuevo.")
  return j

def actualizacionDomino(a,b):
  global contador
  global domino 
  if a == domino[0][0]:
    domino.insert(0, (b, a))
  elif a == domino[-1][1]:
    domino.append((a, b))
  elif b == domino[0][0]:
    domino.insert(0, (a, b))
  else:
    domino.append((b, a))
  contador = 0

  print("\nEl domino sigue así")
  print(f"{domino}\n")
  return 

def actualizacionFichasJugador(a,b):
  global jugar
  if (a, b) in jugar:
    print(f"La ficha seleccionada fue ({a},{b})")
    jugar.remove((a, b))
  else:
    print(f"La ficha seleccionada fue ({b},{a})")
    jugar.remove((b, a)) 
  return

def actualizacionParesJugador(a,b):
  global paresJugador
  paresJugador.remove((a, b))
  return 
  
def fichasJugadores(fichas_1, fichas_2, fichas_3, fichas_4):
  print(f"\nLas fichas del primer jugador son {fichas_1}")
  print(f"Las fichas del segundo jugador son {fichas_2}")
  print(f"Las fichas del tercer jugador son {fichas_3}")
  print(f"Las fichas del cuarto jugador son {fichas_4}")
  return 


fichas = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (1, 1),
          (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 2), (2, 3), (2, 4),
          (2, 5), (2, 6), (3, 3), (3, 4), (3, 5), (3, 6), (4, 4), (4, 5),
          (4, 6), (5, 5), (5, 6), (6, 6)]

domino = []

pares=[(0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6)]

fichas_1 = random.sample(fichas, 7)
fichas_2 = random.sample(list(set(fichas) - set(fichas_1)), 7)
fichas_3 = random.sample(list(set(fichas) - set(fichas_1) - set(fichas_2)), 7)
fichas_4 = list(set(fichas) - set(fichas_1) - set(fichas_2) - set(fichas_3))

texto = (" .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------. \n"
         "| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |\n"
         "| |  ________    | || |     ____     | || | ____    ____ | || |     _____    | || | ____  _____  | || |     ____     | |\n"
         "| | |_   ___ `.  | || |   .'    `.   | || ||_   \  /   _|| || |    |_   _|   | || ||_   \|_   _| | || |   .'    `.   | |\n"
         "| |   | |   `. \ | || |  /  .--.  \  | || |  |   \/   |  | || |      | |     | || |  |   \ | |   | || |  /  .--.  \  | |\n"
         "| |   | |    | | | || |  | |    | |  | || |  | |\  /| |  | || |      | |     | || |  | |\ \| |   | || |  | |    | |  | |\n"
         "| |  _| |___.' / | || |  \  `--'  /  | || | _| |_\/_| |_ | || |     _| |_    | || | _| |_\   |_  | || |  \  `--'  /  | |\n"
         "| | |________.'  | || |   `.____.'   | || ||_____||_____|| || |    |_____|   | || ||_____|\____| | || |   `.____.'   | |\n"
         "| |              | || |              | || |              | || |              | || |              | || |              | |\n"
         "| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |\n"
         " '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' ")

print(texto)
nombre=input("\nEn breve comenzamos, por favor ingrese su nombre ")
print(f"\nBienvenid@ {nombre}")

fichasJugadores(fichas_1, fichas_2, fichas_3, fichas_4)

separado = list((fichas_1, fichas_2, fichas_3, fichas_4))
paresJugador=[i for i in fichas_1 if i in pares]

for i in range(len(separado)):
  if (6, 6) in separado[i]:
    domino.append((6, 6))
    control = i
    jugar = separado[control]
    actualizacionFichasJugador(6,6)
    if control!=0:
      print(f"\nEl jugador que tenía la marrana es el {i+1}")
    else:
      actualizacionParesJugador(6,6)
      print("Felicidades! comenzaste tú")
    break

print("\nEl domino empieza así")
print(f"{domino}\n")

completo = True
contador = 0

while separado[control] != []:
  #Cambia turno
  if control < 3:
    control += 1
  else:
    control = 0
