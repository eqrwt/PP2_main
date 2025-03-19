import pygame
import os
import time

pygame.init()

screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Music Player")
font = pygame.font.Font(None, 22)

MUSIC_FOLDER = "Lab7/music"
songs = [os.path.join(MUSIC_FOLDER, song) for song in os.listdir(MUSIC_FOLDER) if song.endswith((".mp3", ".wav"))]
current_song = 0

pygame.mixer.init()

def play_song(index):
    pygame.mixer.music.load(songs[index])
    pygame.mixer.music.play()
    print(f"Playing: {os.path.basename(songs[index])}")

if songs:
    play_song(current_song)


def draw_text(text, x, y):
    screen.fill((0, 0, 0))
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (x, y))
    pygame.display.flip()

running = True
while running:
    draw_text(f'Playing: {os.path.basename(songs[current_song])}', 50, 130)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_p]:
        pygame.mixer.music.play()
        time.sleep(0.5)
    elif key[pygame.K_SPACE]:
        pygame.mixer.music.stop()
        time.sleep(0.5)
    elif key[pygame.K_RIGHT]:
        current_song = (current_song + 1) % len(songs)
        play_song(current_song)
        time.sleep(0.5)
    elif key[pygame.K_LEFT]: 
        current_song = (current_song - 1) % len(songs)
        play_song(current_song)
        time.sleep(0.5)


pygame.quit()
