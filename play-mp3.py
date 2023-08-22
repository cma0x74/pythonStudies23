# reproduz mp3

import pygame

pygame.init()
pygame.mixer.init()

musga = "/home/papiro/Área de Trabalho/estudos-python/exercises-media/ringside.mp3"

pygame.mixer_music.load(musga)
pygame.mixer_music.play()

while pygame.mixer_music.get_busy():
    continue

# o script não funciona sem as duas últimas linhas