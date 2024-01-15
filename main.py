import pygame
import math

#Carlos Esteban Rivera Perez 8B 213530

# Inicializa Pygame
pygame.init()

# Configura el tamaño de la ventana
ancho_pantalla = 800
alto_pantalla = 600
ventana = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

# Configura los colores
color_pantalla = (255, 255, 255) # blanco
color_dibujo = (0, 0, 0) # negro

# Configura la línea y el círculo
linea = []
circulo_pos = None
circulo_radio = None
velocidad = .3 # Ajusta la velocidad del círculo aquí
dibujando = False
indice = 0
tamaño_circulo = True

# Bucle principal
corriendo = True
while corriendo:
    # Limpia la pantalla
    ventana.fill(color_pantalla)

    # Maneja los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            linea.append(evento.pos)
            dibujando = True
            if circulo_pos is None:
                circulo_pos = evento.pos
        elif evento.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]: # Si el botón izquierdo del ratón está presionado
                if tamaño_circulo:
                    circulo_radio = int(math.hypot(evento.pos[0] - circulo_pos[0], evento.pos[1] - circulo_pos[1]))
                else:
                    linea.append(evento.pos)
        elif evento.type == pygame.MOUSEBUTTONUP:
            dibujando = False
            tamaño_circulo = False

    # Dibuja la línea
    if len(linea) > 1:
        pygame.draw.lines(ventana, color_dibujo, False, linea, 3)

    # Dibuja el círculo en su posición actual
    if circulo_pos is not None and circulo_radio is not None:
        pygame.draw.circle(ventana, color_dibujo, circulo_pos, circulo_radio)

    # Mueve el círculo a lo largo de la línea
    if linea and not dibujando:
        dx = linea[indice][0] - circulo_pos[0]
        dy = linea[indice][1] - circulo_pos[1]
        distancia = math.sqrt(dx**2 + dy**2)
        if distancia > velocidad:
            dx /= distancia
            dy /= distancia
            circulo_pos = (circulo_pos[0] + dx * velocidad, circulo_pos[1] + dy * velocidad)
        else:
            circulo_pos = linea[indice]
            indice += 1
            if indice >= len(linea):
                linea = []
                indice = 0

    # Actualiza la pantalla
    pygame.display.flip()

# Finaliza Pygame
pygame.quit()



