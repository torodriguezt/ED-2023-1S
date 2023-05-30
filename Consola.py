import random
from collections import deque

def entrada():
  while True: #o(k) siendo k el número de veces que el usuario ingrese cosas que no sean números
    try:
      j = tuple(map(int, input("Elige la ficha: ").split())) #Depende del tamaño del input pero no debe pasar de dos, o(1)
      break #0(1)
    except ValueError: 
      print("Solo se permiten números enteros. Inténtalo de nuevo.") #o(1)
  return j

def actualizacionDomino(a,b):
  global contador #o(1)
  global domino #o(1)
  if a == domino[0][0]: #o(1)
    domino.appendleft((b, a)) #o(1)
  elif a == domino[-1][1]: #o(1)
    domino.append((a, b)) #o(1)
  elif b == domino[0][0]: #o(1)
    domino.appendleft((a, b)) #o(1)
  else:
    domino.append((b, a)) #o(1)
  contador = 0 #Sirve para revisar que no se cierre el juego
  print("\nEl domino sigue así") #o(1)
  print(f"{domino}\n") #o(1)
  return 

def actualizacionFichasJugador(a,b):
  global jugar 
  try:
    print(f"La ficha seleccionada fue ({a},{b})")
    jugar.remove((a, b)) #O(N) siendo N el tamaño de la lista jugar
  except ValueError:
    print(f"La ficha seleccionada fue ({b},{a})")
    jugar.remove((b, a)) #O(N) siendo N el tamaño de la lista jugar
  return

def actualizacionParesJugador(a,b):
  global paresJugador
  paresJugador.remove((a, b)) #o(N) siendo N el tamaño de la lista paresJugador
  return 
  
def fichasJugadores(fichas_1, fichas_2, fichas_3, fichas_4):
  print(f"\nLas fichas del primer jugador son {fichas_1}") #o(1)
  print(f"Las fichas del segundo jugador son {fichas_2}") #o(1)
  print(f"Las fichas del tercer jugador son {fichas_3}") #o(1)
  print(f"Las fichas del cuarto jugador son {fichas_4}") #o(1)
  return 


fichas = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (1, 1),
          (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 2), (2, 3), (2, 4),
          (2, 5), (2, 6), (3, 3), (3, 4), (3, 5), (3, 6), (4, 4), (4, 5),
          (4, 6), (5, 5), (5, 6), (6, 6)] #O(1)

domino = deque() #O(1)

pares=[(0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6)] #O(1)

fichas_1 = random.sample(fichas, 7) #O(1) en el caso del 7, pero si lo consideramos con un número K es O(K)
fichas_2 = random.sample(list(set(fichas) - set(fichas_1)), 7) 
#No se pueden restar listas, por eso las convertimos a set (conjuntos) que si permiten esta operación
#O(tamaño(fichas)) el tamaño de la lista define la eficiencia, si es N o(N).   
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
#o(1) el texto
print(texto) #o(1)
nombre=input("\nEn breve comenzamos, por favor ingrese su nombre ") #o(1)
print(f"\nBienvenid@ {nombre}")  #o(1)

fichasJugadores(fichas_1, fichas_2, fichas_3, fichas_4) #O(1)

separado = list((fichas_1, fichas_2, fichas_3, fichas_4)) #O(1)
paresJugador=[i for i in fichas_1 if i in pares] #Si el jugador tiene N fichas, O(N). En este caso tiene 7, sería o(1)

for i in range(len(separado)): #Como siempre van a ser 4 jugadores el len(separado)==4, por lo tanto o(1)
  if (6, 6) in separado[i]: #O(N), siendo N el tamaño de la lista separado[i], en este caso es 7, O(1)
    domino.append((6, 6)) #O(1)
    control = i #o(1)
    jugar = separado[control] #o(1)
    actualizacionFichasJugador(6,6) #o(n) siendo n el numero de fichas del jugador
    if control!=0: #o(1)
      print(f"\nEl jugador que tenía la marrana es el {i+1}") #o(1)
    else: #o(1)
      actualizacionParesJugador(6,6) #o(k) siendo k el número de fichas pares del jugador
      print("Felicidades! comenzaste tú") #o(1)
    break

print("\nEl domino empieza así") #o(1)
print(f"{domino}\n") #o(1)

completo = True #o(1)
contador = 0 #o(1)

while separado[control] != []: #o(j) siendo j el número de jugadas que se hagan para terminar el juego, en este caso, serían 28 +- x jugadas. Lo que sería o(1). Si fueran n fichas, lo necesario serían n+-x fichas. es decir o(n).
  
  #Cambia turno
  if control < 3: #o(1)
    control += 1 #o(1)
    print(f"Turno del jugador {control+1}") #o(1)
  else: #o(1)
    control = 0 #o(1)
    print(f"Turno de {nombre}") #o(1)

  jugar = separado[control] #o(1)
  ficha_a_poner = -1 #o(1)
  print(f"Las fichas del jugador son {jugar}") #o(1)
  
  #Juega el jugador humano
  if control == 0: #o(1)
    if domino[-1][1]!=domino[0][0] and (domino[-1][1],domino[-1][1]) in paresJugador and (domino[0][0],domino[0][0]) in paresJugador: #o(N) siendo N el tamaño de paresJugador, en este caso el peor escenario es que tenga los 7 pares, O(1)
      #Revisa si los extremos son distintos y si el jugador tiene ese par de dobles
      print("Puedes jugador dobles, deseas hacerlo?") #o(1)
      respuesta=input("Ingresa y para si, en caso contrario, cualquier otra cosa") #o(1)
      if respuesta=="y": #o(1)
        print("El jugador juega dobles\n") #o(1)
        actualizacionFichasJugador(domino[-1][1],domino[-1][1]) 
        actualizacionDomino(domino[-1][1],domino[-1][1]) 
        actualizacionFichasJugador(domino[0][0],domino[0][0]) 
        actualizacionDomino(domino[0][0],domino[0][0]) 
        actualizacionParesJugador(domino[0][0],domino[0][0]) 
        actualizacionParesJugador(domino[-1][1],domino[-1][1]) 
        continue   
    print("\nEscoge la ficha con la que deseas jugar: ") #o(1)
    print("Escribe sus números separados por un espacio") #o(1)
    print("En caso de no tener opciones o no querer jugar el turno, marca 0\n") #o(1)
    j = entrada() #o(k) siendo k el número de veces que el usuario ingrese algo que no sean números
    while True: #o(K) siendo K el número de veces que el usuario ingrese algo mal o erroneo
      if len(j) != 2 and j[0] != 0: #o(1)
        print("Porfavor ingresa una ficha valida: ") #o(1)
        j = entrada() 
      elif len(j) == 1 and j[0] == 0: #o(1)
        break #o(1)
      elif j not in jugar and j[::-1] not in jugar: #o(N) siendo N el tamaño de jugar, en este caso el peor caso es 7, o(1)
        print("No tienes esa ficha") #o(1)
        print("Porfavor ingresa una ficha valida: ") #o(1)
        j = entrada() #o(1)
      else:
        arriba, abajo = j #o(1)
        if arriba == domino[-1][1] or abajo == domino[0][0] or arriba == domino[0][0] or abajo == domino[-1][1]: #o(1)
          a = arriba #o(1)
          b = abajo #o(1)
          ficha_a_poner = sum(j) #o(1)
          if a==b: #o(1)
            actualizacionParesJugador(a,b) #o(k) siendo k el número de pares del jugador
          break #o(1)
        else: #o(1)
          print("Porfavor ingresa una ficha valida: ") #o(1)
          j = entrada() 
  #Juegan los bots
  else:
    r=random.random() #o(1)
    #Probabilidad de que el bot pase turno 0.2
    if r>0.2: #o(1)
      pp=[] #o(1)
      for j in jugar: #o(n) siendo n el tamaño de jugar
        arriba, abajo = j #o(1)
        if j in pares: #o(k) siendo k el tamaño de pares
          pp.append(j) #o(1) por amortiguado
        if arriba == domino[-1][1] or abajo == domino[0][0] or arriba == domino[0][0] or abajo == domino[-1][1]: #o(1)
          cantidad = sum(j) #o(1)
          if cantidad > ficha_a_poner: #o(1)
            ficha_a_poner = cantidad #o(1)
            a = arriba #o(1)
            b = abajo #o(1)
      #Poner pares
      i1, i2=-1, -1 #o(1)
      if len(pp)>1 and domino[-1][1]!=domino[0][0]: #o(1) revisa si los extremos son distintos y si tiene más de un par en sus fichas
        for i in range(len(pp)): #en el peor caso, sería 7, o(1). A menos que hayan k pares y todos los tenga un bot, O(k) 
          if domino[-1][1]==pp[i][0] or domino[0][0]==pp[i][0]: #o(1) revisa si el par coincide con uno de los extremos o(1)
            if i1!=-1: #o(1)
              i2=i #o(1)
              d1, d2=pp[i] #o(1)
            else: #o(1)
              i1=i #o(1)
              u1, u2=pp[i] #o(1)
              
      #si tenemos los dos pares i1 y i2 van a ser distintos de -1
      if i1!=-1 and i2!=-1: #o(1)
        print("El jugador juega dobles\n") 
        actualizacionFichasJugador(d1, d2) 
        actualizacionDomino(d1, d2) 
        actualizacionFichasJugador(u1, u2) 
        actualizacionDomino(u1, u2)
        continue
      
  #Pasa turno, cierra juego, etc.
  if ficha_a_poner == -1: #o(1)
    contador += 1 #o(1)
    print("Pasa turno") #o(1)
    print("\nEl domino sigue así") #o(1)
    print(f"{domino}\n") #o(n) siendo n el tamaño del deque 
    if contador == 16: #revisamos que no se cierre el juego o(1)
      print("Se cerro el juego, sin embargo, por suma de puntos:\n") #o(1)
      sumar_tuplas = lambda separado: sum(sum(t) for t in separado) #o(n) siendo n el tamaño de separado, en este caso, el peor escenario sería 7 o(1).
      ganador = min(range(len(separado)),key=lambda i: sumar_tuplas(separado[i])) #o(n) por la llamada a sumar_tuplas, si el número de jugadores fuera k sería o(k*n), pero en este caso son 4 es decir o(1). 
      control = ganador #o(1)
      break #o(1)
    continue #o(1)

  #se actualiza el juego
  actualizacionFichasJugador(a,b) 
  actualizacionDomino(a,b) 

#finaliza juego, imprime mensajes de terminación
if control==0: #o(1)
  print("Ganaste el juego en horabuena!!\n") #o(1)
else: #o(1)
  print(f"Gano el jugador {control + 1}\n") #o(1)

print("Fichas de cada jugador al final") #o(1)
fichasJugadores(fichas_1, fichas_2, fichas_3, fichas_4) #o(1)
