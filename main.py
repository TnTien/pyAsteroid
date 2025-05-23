import pygame

from constants import *
from player import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	Clock = pygame.time.Clock()
	dt = 0
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		player.draw(screen)
		pygame.display.flip()
		dt += Clock.tick(60)/1000
	start_text()
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

def start_text():
	print("Starting Asteroids!")

if __name__ == "__main__":
	main()
