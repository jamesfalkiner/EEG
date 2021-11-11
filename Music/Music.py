import pygame
from Menu.SettingSaves import GetAud


def MainMenuMusic():
    pygame.mixer.init()
    pygame.mixer.music.load("Music/SICKOMODE.mp3")
    pygame.mixer.music.set_volume(float(GetAud()[1]))
    pygame.mixer.music.play()


def StopMusic():
    pygame.mixer.music.stop()

def ChangeSoundLevel(new_volume):
    #pygame.mixer.sound.set_volume(new_volume)
    pass

def ChangeMusicLevel(new_volume):
    print(new_volume)
    pygame.mixer_music.pause()
    pygame.mixer.music.set_volume(new_volume)
    pygame.mixer.music.unpause()

def ChangeMasterLevel(new_volume, old_music_volume, old_sound_volume):
    new_music_volume = new_volume*old_music_volume
    new_sound_volume = new_volume*old_sound_volume
    pygame.mixer_music.pause()
    pygame.mixer.music.set_volume(new_music_volume)
    pygame.mixer.music.unpause()
    #pygame.mixer.sound.set_volume(new_sound_volume)