from gtts import gTTS
import pygame
import os


pygame.mixer.init()
pygame.mixer.music.set_volume(0.6)

def play_tts(text):
    tts = gTTS(text)
    tts.save("test.mp3")

    pygame.mixer.music.load("scrungle_sounds/scrungle.ogg")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(0)

    pygame.mixer.music.load("test.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(0)

    pygame.mixer.music.unload()
    os.remove("test.mp3")