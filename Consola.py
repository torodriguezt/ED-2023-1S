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

  if control!=0:
    print(f"Turno del jugador {control+1}")
  else:
    print(f"Turno de {nombre}")

  jugar = separado[control]
  ficha_a_poner = -1
  print(f"Las fichas del jugador son {jugar}")
  
  #Juega el jugador humano
  if control == 0:
    if domino[-1][1]!=domino[0][0] and (domino[-1][1],domino[-1][1]) in paresJugador and (domino[0][0],domino[0][0]) in paresJugador:
      print("Puedes jugador dobles, deseas hacerlo?")
      respuesta=input("Ingresa y para si, en caso contrario, cualquier otra cosa")
      if respuesta=="y":
        print("El jugador juega dobles\n")
        actualizacionFichasJugador(domino[-1][1],domino[-1][1])
        actualizacionDomino(domino[-1][1],domino[-1][1])
        actualizacionFichasJugador(domino[0][0],domino[0][0])
        actualizacionDomino(domino[0][0],domino[0][0])
        actualizacionParesJugador(domino[0][0],domino[0][0])
        actualizacionParesJugador(domino[-1][1],domino[-1][1])
        continue   
    print("\nEscoge la ficha con la que deseas jugar: ")
    print("Escribe sus números separados por un espacio")
    print("En caso de no tener opciones o no querer jugar el turno, marca 0\n")
    j = entrada()
    while True:
      if len(j) != 2 and j[0] != 0 or type(j[0])!=int:
        print("Porfavor ingresa una ficha valida: ")
        j = entrada()
      elif len(j) == 1 and j[0] == 0:
        break
      elif j not in jugar and j[::-1] not in jugar:
        print("No tienes esa ficha")
        print("Porfavor ingresa una ficha valida: ")
        j = entrada()
      elif j in jugar or j[::-1] in jugar:
        arriba, abajo = j
        if arriba == domino[-1][1] or abajo == domino[0][0] or arriba == domino[0][0] or abajo == domino[-1][1]:
          a = arriba
          b = abajo
          ficha_a_poner = sum(j)
          if a==b:
            actualizacionParesJugador(a,b)
          break
        else:
          print("Porfavor ingresa una ficha valida: ")
          j = entrada()
  #Juegan los bots
  else:
    r=random.random()
    #Probabilidad de que el bot pase turno 0.2
    if r>0.2:
      pp=[]
      for j in jugar:
        arriba, abajo = j
        if j in pares:
          pp.append(j)
        if arriba == domino[-1][1] or abajo == domino[0][0] or arriba == domino[
            0][0] or abajo == domino[-1][1]:
          cantidad = sum(j)
          if cantidad > ficha_a_poner:
            ficha_a_poner = cantidad
            a = arriba
            b = abajo
      #Poner pares
      i1, i2=-1, -1
      if len(pp)>1 and domino[-1][1]!=domino[0][0]:
        for i in range(len(pp)):
          if domino[-1][1]==pp[i][0] or domino[0][0]==pp[i][0]:
            if i1!=-1:
              i2=i
              d1, d2=pp[i]
            else:
              i1=i
              u1, u2=pp[i]
    
      if i1!=-1 and i2!=-1:
        print("El jugador juega dobles\n")
        actualizacionFichasJugador(d1, d2)
        actualizacionDomino(d1, d2)
        actualizacionFichasJugador(u1, u2)
        actualizacionDomino(u1, u2)
        continue
      
  #Pasa turno, cierra juego, etc.
  if ficha_a_poner == -1:
    contador += 1
    print("Pasa turno")
    print("\nEl domino sigue así")
    print(f"{domino}\n")
    if contador == 8:
      print("Se cerro el juego, sin embargo, por suma de puntos:\n")
      sumar_tuplas = lambda separado: sum(sum(t) for t in separado)
      ganador = min(range(len(separado)),
                    key=lambda i: sumar_tuplas(separado[i]))
      control = ganador
      break
    continue

  #se actualiza el juego
  actualizacionFichasJugador(a,b)
  actualizacionDomino(a,b)

#finaliza juego, imprime mensajes de terminación
if control==0:
  print("Ganaste el juego en horabuena!!\n")
else:
  print(f"Gano el jugador {control + 1}\n")

print("Fichas de cada jugador al final")
fichasJugadores(fichas_1, fichas_2, fichas_3, fichas_4)