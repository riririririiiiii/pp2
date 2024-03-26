import pygame
import os                                                            
pygame.init()
WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Cool music player ;)')
MUSIC_DIRECTION = "music"
playlist = os.listdir(MUSIC_DIRECTION)
current_track_index = 0



current_track = os.path.join(MUSIC_DIRECTION, playlist[current_track_index])
pygame.mixer.music.load(current_track)
background_image = pygame.image.load("sound.jpeg").convert()
def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def play_next_track():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(playlist)
    next_track = os.path.join(MUSIC_DIRECTION, playlist[current_track_index])
    pygame.mixer.music.load(next_track)
    play_music()

def play_previous_track():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(playlist)
    previous_track = os.path.join(MUSIC_DIRECTION, playlist[current_track_index])
    pygame.mixer.music.load(previous_track)
    play_music()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  #SPACE- play
                play_music()
            elif event.key == pygame.K_s:    #S-stop
                stop_music()
            elif event.key == pygame.K_p:    #P-pass
                play_next_track()
            elif event.key == pygame.K_b:    #B-back
                play_previous_track()
    screen.blit(background_image, (0, 0))
    pygame.display.flip()
pygame.quit()
