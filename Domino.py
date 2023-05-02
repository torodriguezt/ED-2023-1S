import pygame
import random
import sys
import os

# Definir dimensiones de la ventana
WIDTH, HEIGHT = 450,450
WINDOW_SIZE = (WIDTH, HEIGHT)

# Inicializar Pygame y crear la ventana
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)

class Button:
    def __init__(self, x, y, width=None, height=None, text=None, text_color=None, color=None, action=None, data=None, value=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_color = text_color
        self.color = color
        self.action = action

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        font = pygame.font.SysFont(None, 30)
        text = font.render(self.text, True, self.text_color)
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)
    
    def draw1(self, surface):
        surface.blit(self.image, (self.x, self.y))
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()

def eliminar_ficha_interfaz(i, j):
    global eliminada
    global screen2
    if i==0:
        screen2.blit(eliminada, ((50*(j+1)), 400))
    elif i==1:
        screen2.blit(eliminada, (0, 50*(j+1)))
    elif i==2:
        screen2.blit(eliminada, (50*(j+1),0))
    else:
        screen2.blit(eliminada, (400, 50*(j+1)))
    pygame.display.update()
    return 

def actualizacionFichasJugador(a,b,jugar,i):
    global fichas_12
    global fichas_22
    global fichas_32
    global fichas_42
    for j in range(len(jugar)):
        if jugar[j]==(a, b):
            print(f"La ficha seleccionada fue ({a},{b})")
            jugar.remove((a, b))
            if i==0:
                p=fichas_12.index((a, b))
            elif i==1:
                p=fichas_22.index((a, b))   
            elif i==2:
                p=fichas_32.index((a, b))  
            else:
                p=fichas_42.index((a, b))  
            eliminar_ficha_interfaz(i, p)
            break
        elif jugar[j]==(b, a):
            print(f"La ficha seleccionada fue ({b},{a})")
            jugar.remove((b, a))
            if i==0:
                p=fichas_12.index((b, a))
            elif i==1:
                p=fichas_22.index((b, a))   
            elif i==2:
                p=fichas_32.index((b, a))  
            else:
                p=fichas_42.index((b, a))  
            eliminar_ficha_interfaz(i, p)
            break
    return

def actualizacionParesJugador(a,b,paresJugador):
    paresJugador.remove((a, b))
    return 

def actualizacionDomino(a,b,domino): 
    global contador
    global screen2
    global fichas_images
    global fichas
    if a == domino[0][0]:
        domino.insert(0, (b, a))
        x = 175
        y= 200
        if (a, b) in fichas:
            rotated_image = pygame.transform.rotate(fichas_images[(a, b)], -90)
        else:
            rotated_image = pygame.transform.rotate(fichas_images[(b, a)], -90)
        screen2.blit(rotated_image, (x, y))
    elif a == domino[-1][1]:
        domino.append((a, b))
        x = 225
        y= 200
        if (a, b) in fichas:
            rotated_image = pygame.transform.rotate(fichas_images[(a, b)], +90)
        else:
            rotated_image = pygame.transform.rotate(fichas_images[(b, a)], +90)
        screen2.blit(rotated_image, (x, y))
    elif b == domino[0][0]:
        domino.insert(0, (a, b))
        x = 175
        y= 200
        if (a, b) in fichas:
            rotated_image = pygame.transform.rotate(fichas_images[(a, b)], +90)
        else:
            rotated_image = pygame.transform.rotate(fichas_images[(b, a)], +90)
        screen2.blit(rotated_image, (x, y))
    else:
        domino.append((b, a))
        x = 225
        y= 200
        if (a, b) in fichas:
            rotated_image = pygame.transform.rotate(fichas_images[(a, b)], -90)
        else:
            rotated_image = pygame.transform.rotate(fichas_images[(b, a)], -90)
        screen2.blit(rotated_image, (x, y))
    print(domino)
    contador = 0
    pygame.display.update()
    return

def entrada1(j):
    while True:
        if j is None or not isinstance(j, str):
            print("Entrada inválida. Inténtalo de nuevo.")
        else:
            try:
                j = tuple(map(int, j.split()))
                break
            except ValueError:
                print("Solo se permiten números enteros. Inténtalo de nuevo.")
                break
    return j


def caja_texto(duracion):
    font = pygame.font.SysFont('Arial', 24)
    text_surface = font.render('Escribe aquí', True, (255, 255, 255))
    input_rect = pygame.Rect(125, 300, 200, 30)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = True    
    text=""
    start_time = pygame.time.get_ticks()

    # Dibujar la caja de texto
    pygame.draw.rect(screen, color, input_rect, 2)
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    pygame.display.flip()

    while active:
        pygame.draw.rect(screen, (0,0,0), input_rect)
        #clock = pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si el usuario hace clic en la caja de texto
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                    # Cambiar el color de fondo de la caja de texto
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                        pygame.display.update()  # Actualizar la pantalla después de eliminar el último carácter
                    else:
                        text += event.unicode
        pygame.draw.rect(screen, color, input_rect, 2)
        text_surface = font.render(text, True, (255, 255, 255))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        pygame.display.update()

        elapsed_time = pygame.time.get_ticks() - start_time
        if elapsed_time >= duracion:
            active = False
            return text

def imprime_mensaje(m):
    global screen2
    font = pygame.font.SysFont(None,25)
    mensaje = font.render(m, True, "white")
    screen2.blit(mensaje, (100,300))
    pygame.display.update()

def imprime_text(m):
    global screen2
    inputr = pygame.Rect(50, 90,350, 30)
    pygame.draw.rect(screen2, (0,0,0), inputr)
    font = pygame.font.SysFont(None,20)
    mensaje = font.render(m, True, "white")
    screen2.blit(mensaje, (125,90))
    pygame.display.update()
    
def game():
    global fichas_1
    global fichas_2
    global fichas_3
    global fichas_4
    global fichas_images
    global screen2 
    global separado 
    global control 

    domino=[]
    separado = list((fichas_1, fichas_2, fichas_3, fichas_4))
    pares=[(0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6)]
    paresJugador=[i for i in fichas_1 if i in pares]

    for i in range(len(separado)):
        if (6, 6) in separado[i]:
            domino.append((6, 6))
            control = i
            jugar = separado[control]
            actualizacionFichasJugador(6, 6,jugar,control)
            x = 200
            y= 200
            rotated_image = pygame.transform.rotate(fichas_images[(6, 6)], -90)
            screen.blit(rotated_image, (x, y))
            if control==0:
                actualizacionParesJugador(6, 6,paresJugador)
            break
    pygame.display.update()
    contador = 0

    while separado[control] != []:
    #Cambia turno
        if control < 3:
            control += 1
        else:
            control = 0

        if control!=0:
            print(f"Turno del bot {control}")
        else:
            imprime_text("Turno del jugador")

        jugar = separado[control]
        ficha_a_poner = -1
        
        #Juegan los bots
        if control==0:   
            if domino[-1][1]!=domino[0][0] and (domino[-1][1],domino[-1][1]) in paresJugador and (domino[0][0],domino[0][0]) in paresJugador:
                imprime_text("Puedes jugador dobles, presiona y")
                respuesta=caja_texto(30000)
                if respuesta=="y":
                    print("El jugador juega dobles\n")
                    actualizacionFichasJugador(domino[-1][1],domino[-1][1],jugar,control)
                    actualizacionDomino(domino[-1][1],domino[-1][1],domino)
                    pygame.display.update()
                    actualizacionFichasJugador(domino[0][0],domino[0][0],jugar,control)
                    actualizacionDomino(domino[0][0],domino[0][0],domino)
                    pygame.display.update()
                    actualizacionParesJugador(domino[0][0],domino[0][0],paresJugador)
                    actualizacionParesJugador(domino[-1][1],domino[-1][1],paresJugador)
                    continue
            j = entrada1(caja_texto(30000))
            while True:
                if j==():
                    print("Se acabo tu tiempo para jugar")
                    break
                if len(j) != 2 and j[0] != 0 or type(j[0])!=int:
                    print("Porfavor ingresa una ficha valida: ")
                    j = entrada1(caja_texto(30000))
                elif len(j) == 1 and j[0] == 0:
                    break
                elif j not in jugar and j[::-1] not in jugar:
                    print("No tienes esa ficha")
                    print("Porfavor ingresa una ficha valida: ")
                    j = entrada1(caja_texto(30000))
                elif j in jugar or j[::-1] in jugar:
                    arriba, abajo = j
                    if arriba == domino[-1][1] or abajo == domino[0][0] or arriba == domino[0][0] or abajo == domino[-1][1]:
                        a = arriba
                        b = abajo
                        ficha_a_poner = sum(j)
                        if a==b:
                            actualizacionParesJugador(a,b,paresJugador)
                        break
                    else:
                        print("Porfavor ingresa una ficha valida: ")
                        j = entrada1(caja_texto(30000))
        else:
            r=random.random()
            #Probabilidad de que el bot pase turno 0.2
            if r>0.2:
                pp=[]
                for j in jugar:
                    arriba, abajo = j
                    if j in pares:
                        pp.append(j)
                    if arriba == domino[-1][1] or abajo == domino[0][0] or arriba == domino[0][0] or abajo == domino[-1][1]:
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
                    actualizacionFichasJugador(d1, d2, jugar, control)
                    actualizacionDomino(d1, d2, domino)
                    actualizacionFichasJugador(u1, u2,jugar, control)
                    actualizacionDomino(u1, u2,domino)
                    continue

        #Pasa turno, cierra juego, etc.
        if ficha_a_poner == -1:
            contador += 1
            print("Pasa turno")
            if contador == 20:
                print("Se cerro el juego, sin embargo, por suma de puntos:\n")
                sumar_tuplas = lambda separado: sum(sum(t) for t in separado)
                ganador = min(range(len(separado)),key=lambda i: sumar_tuplas(separado[i]))
                control = ganador
                break
            continue
        #se actualiza el juego
        actualizacionFichasJugador(a,b,jugar,control)
        actualizacionDomino(a,b,domino)
        pygame.display.update()
    
    if control==0:
      imprime_mensaje("Ganaste el juego en horabuena!!")
    else:
        imprime_mensaje(f"Gano el jugador {control + 1}")

    print("Fichas de cada jugador al final")
    print(f"\nLas fichas del primer jugador son {fichas_1}")
    print(f"Las fichas del segundo jugador son {fichas_2}")
    print(f"Las fichas del tercer jugador son {fichas_3}")
    print(f"Las fichas del cuarto jugador son {fichas_4}")

# Función para mostrar la pantalla de "Juego"
def show_game_screen():
    global fichas
    global fichas_1
    global fichas_2
    global fichas_3
    global fichas_4
    global fichas_12
    global fichas_22
    global fichas_32
    global fichas_42
    global fichas_images
    global screen2
    WIDTH, HEIGHT = 450,450
    WINDOW_SIZE = (WIDTH, HEIGHT)

    # Inicializar Pygame y crear la ventana
    pygame.init()
    screen2 = pygame.display.set_mode(WINDOW_SIZE)
    # Cargar las imágenes de las fichas del domino
    fichas = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 1),
              (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 2), (2, 3), (2, 4),
              (2, 5), (2, 6), (3, 3), (3, 4), (3, 5), (3, 6), (4, 4), (4, 5),
              (4, 6), (5, 5), (5, 6), (6, 6)]

    fichas_images = {}
    for ficha in fichas:
        image = pygame.image.load(f'imagenes/{ficha}.png')
        fichas_images[ficha] = pygame.transform.scale(image, (50, 50))
    pares=[(0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6)]
    fichas_1 = random.sample(fichas, 7)
    fichas_2 = random.sample(list(set(fichas) - set(fichas_1)), 7)
    fichas_3 = random.sample(list(set(fichas) - set(fichas_1) - set(fichas_2)), 7)
    fichas_4 = list(set(fichas) - set(fichas_1) - set(fichas_2) - set(fichas_3))

    fichas_12=fichas_1.copy()
    fichas_22=fichas_2.copy()
    fichas_32=fichas_3.copy()
    fichas_42=fichas_4.copy()

    # Mostrar las imágenes de las fichas del jugador 2 (rotadas 90 grados a la derecha)
    x = 0
    y = 50
    for ficha in fichas_2:
        rotated_image = pygame.transform.rotate(fichas_images[ficha], -90)
        screen2.blit(rotated_image, (x, y))
        y += 50

    # Mostrar las imágenes de las fichas del jugador3
    x = 50
    y = 0
    for ficha in fichas_3:
        screen2.blit(fichas_images[ficha], (x, y))
        x += 50

    # Mostrar las imágenes de las fichas del jugador 4 (rotadas 90 grados a la izquierda)
    x = 400
    y = 50
    for ficha in fichas_4:
        rotated_image = pygame.transform.rotate(fichas_images[ficha], +90)
        screen2.blit(rotated_image, (x, y))
        y += 50

    # Mostrar las imágenes de las fichas del jugador
    x = 50
    y = 400
    for ficha in fichas_1:
        screen2.blit(fichas_images[ficha], (x, y))
        x += 50

    empezar_button = Button(WIDTH/2-25, HEIGHT/2-25, 50, 50, "Play", (255, 255, 255), (0, 128, 0), game)

    # Mostrar el botón en la ventana
    empezar_button.draw(screen2)

    pygame.display.update()
    # Esperar a que el usuario cierre la ventana o haga clic en
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            empezar_button.handle_event(event)
        pygame.display.update()

fichas=[]
fichas_1=[]
fichas_2=[]
fichas_3=[]
fichas_4=[]
fichas_12=[]
fichas_22=[]
fichas_32=[]
fichas_42=[]
fichas_images={}
screen2=None
separado=[]
control=-1
ruta_imagen = os.path.join("imagenes", "eliminada.png")
image = pygame.image.load(ruta_imagen)
eliminada = pygame.transform.scale(image, (50, 50))
# Crear un botón para iniciar el juego
play_button = Button(WIDTH/2-50, HEIGHT/2-25, 100, 50, "Jugar", (255, 255, 255), (0, 128, 0), show_game_screen)

# Mostrar el botón en la ventana
play_button.draw(screen)
# Actualizar la ventana
pygame.display.update()

# Esperar a que el usuario cierre la ventana o haga clic en
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        play_button.handle_event(event)
    pygame.display.update()