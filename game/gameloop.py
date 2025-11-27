from game.state import game_state
from game.logic import update_game
import pygame
from game.ui import create_screen, create_ui, update_ui, event_handler

def run_gameloop():
    window_surface = create_screen()
    ui, animations = create_ui()
    clock = pygame.time.Clock()
    running = True
    debug_iter = 100

    while running:
        if game_state["debug"] == True:
            if debug_iter % 100 == 0:
                print(game_state)
            if debug_iter >= 1000:
                debug_iter = 0
            debug_iter += 1

        dt = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            ui["manager"].process_events(event)
            event_handler(event, ui, animations)
        ui["manager"].update(dt)

        update_game(dt)
        update_ui(ui, animations, dt, window_surface)

run_gameloop()