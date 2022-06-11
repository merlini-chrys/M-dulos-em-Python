#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

# Use a Biblioteca PYGAME, usada para jogos.
# Ele carrega: imagens, videos, músicas
# Abra o Terminal e instale

import pygame 
pygame.init() #iniciar
pygame.mixer.music.load('C:/Users/cliente/Desktop/PYTHON/EXERCÍCIOS/4 UTILIZANDO MÓDULOS/music.mp3')
pygame.mixer.music.play () #tocar
pygame.event.wait ()
input()
