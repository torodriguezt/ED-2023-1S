import pygame
import random
import sys

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
    for j in range(len(jugar)):
        if jugar[j]==(a, b):
            print(f"La ficha seleccionada fue ({a},{b})")
            jugar.remove((a, b))
            eliminar_ficha_interfaz(i, j)
            break
        elif jugar[j]==(b, a):
            print(f"La ficha seleccionada fue ({b},{a})")
            jugar.remove((b, a))
            eliminar_ficha_interfaz(i, j)
            break
    return

def actualizacionParesJugador(a,b,paresJugador):
    paresJugador.remove((a, b))
    return 

def actualizacionDomino(a,b,domino): 
    global contador
    global screen2
    global fichas_images
    if a == domino[0][0]:
        domino.insert(0, (b, a))
        x = 175
        y= 200
        rotated_image = pygame.transform.rotate(fichas_images[(a, b)], -90)
        screen2.blit(rotated_image, (x, y))
    elif a == domino[-1][1]:
        domino.append((a, b))
        x = 225
        y= 200
        rotated_image = pygame.transform.rotate(fichas_images[(a, b)], +90)
        screen2.blit(rotated_image, (x, y))
    elif b == domino[0][0]:
        domino.insert(0, (a, b))
        x = 175
        y= 200
        rotated_image = pygame.transform.rotate(fichas_images[(a, b)], +90)
        screen2.blit(rotated_image, (x, y))
    else:
        domino.append((b, a))
        x = 225
        y= 200
        rotated_image = pygame.transform.rotate(fichas_images[(a, b)], -90)
        screen2.blit(rotated_image, (x, y))
    print(domino)
    contador = 0
    pygame.display.update()
    return

def entrada1():
    while True:
        try:
            j = tuple(map(int, input("Elige la ficha: ").split()))
            break
        except ValueError:
            print("Solo se permiten números enteros. Inténtalo de nuevo.")
    return j

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
            print(f"Turno del jugador")

        jugar = separado[control]
        ficha_a_poner = -1
        
        #Juegan los bots
        if control>4:   
            if domino[-1][1]!=domino[0][0] and (domino[-1][1],domino[-1][1]) in paresJugador and (domino[0][0],domino[0][0]) in paresJugador:
                print("Puedes jugador dobles, deseas hacerlo?")
                respuesta=input("Ingresa y para si, en caso contrario, cualquier otra cosa")
                if respuesta=="y":
                    print("El jugador juega dobles\n")
                    actualizacionFichasJugador(domino[-1][1],domino[-1][1],jugar,control)
                    actualizacionDomino(domino[-1][1],domino[-1][1],domino)
                    actualizacionFichasJugador(domino[0][0],domino[0][0],jugar,control)
                    actualizacionDomino(domino[0][0],domino[0][0],domino)
                    actualizacionParesJugador(domino[0][0],domino[0][0],paresJugador)
                    actualizacionParesJugador(domino[-1][1],domino[-1][1],paresJugador)
                    continue
            j = entrada1()
            while True:
                if len(j) != 2 and j[0] != 0 or type(j[0])!=int:
                    print("Porfavor ingresa una ficha valida: ")
                    j = entrada1()
                elif len(j) == 1 and j[0] == 0:
                    break
