import pygame
import sys

# Inicializando o Pygame
pygame.init()

# Definindo as dimensões da te4la
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Capibariver")

#Definindo cores
WHITE = (255, 255, 255) #Branco
BLACK = (0, 0, 0)       #Preto

#Função principal
def main():
    clock = pygame.time.Clock() #Relógio para controlar a taxa de atualização da tela
    running = True #Flag para o loop principal
    
    while running:
        for event in pygame.event.get(): #Checa por eventos (ex: fechar a janela)
            if event.type == pygame.QUIT: 
                running = False
           
        #Preenchendo a tela com a cor branca
        screen.fill(WHITE)
        
        #Atualizando a tela
        pygame.display.flip()
        
        #Definindo a taxa de atualização (FPS)
        clock.tick(60)
        
    pygame.quit()
    sys.exit()
    
if __name__ == "__main__":
    main() 