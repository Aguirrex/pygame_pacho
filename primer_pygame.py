import pygame
import time

def main():
    pygame.init()
    ventana = pygame.display.set_mode((800, 600))
    rojo = (255, 0, 0)
    azul = (0, 0, 255)
    amarillo = (255, 255, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.set_caption("3d cube")
            pygame.draw.line(ventana,rojo,(100,100),(200,100),2)
            pygame.draw.line(ventana,rojo,(200,100),(200,200),2)
            pygame.draw.line(ventana,rojo,(200,200),(100,200),2)
            pygame.draw.line(ventana,rojo,(100,200),(100,100),2)
            pygame.draw.line(ventana,rojo,(150,50),(250,50),2)
            pygame.draw.line(ventana,rojo,(250,50),(250,150),2)
            pygame.draw.line(ventana,rojo,(250,150),(150,150),2)
            pygame.draw.line(ventana,rojo,(150,150),(150,50),2)
            pygame.draw.line(ventana,rojo,(100,100),(150,50),2)
            pygame.draw.line(ventana,rojo,(200,100),(250,50),2)
            pygame.draw.line(ventana,rojo,(200,200),(250,150),2)
            pygame.draw.line(ventana,rojo,(100,200),(150,150),2)

# scribd figuras geometricas para recortar y pegar en el cuaderno
            
            pygame.display.update()
main()
#show a house

"""
nombre procedimiento: cubo3d
entrada: ventana, x, y, width, height, color
salida: dibuja un cubo 3d
proceso: dibuja un cubo 3d


"""