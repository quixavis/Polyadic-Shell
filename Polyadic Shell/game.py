from logic import update_game
import pygame
from ui import create_ui, update_ui, event_handler

def main():
    pygame.init()
    pygame.display.set_caption('Polyadic Shell')
    window_surface = pygame.display.set_mode((800, 600))
    background = pygame.Surface((800, 600))
    background.fill(pygame.Color("#000000"))

    ui = create_ui()
    clock = pygame.time.Clock()

    running = True

    while running:

        dt = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            ui["manager"].process_events(event)
            event_handler(event, ui)

        ui["manager"].update(dt)

        update_game()
        update_ui(ui, window_surface)

        window_surface.blit(background, (0, 0))
        ui["manager"].draw_ui(window_surface)

        pygame.display.update()

main()