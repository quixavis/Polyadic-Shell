from state import game_state
from logic import coin_clicker, generator_purchase, prestige
import pygame
import pygame_gui
from pygame_gui.elements import UIButton, UILabel

def create_ui():
    ui = {}
    ui["manager"] = pygame_gui.UIManager((800, 600))

    ui["coin_label"] = UILabel(
    relative_rect=pygame.Rect(50, 50, 200, 50),
    text='Coins: 0',
    manager=ui["manager"]
    )

    ui["generator_label"] = UILabel(
    relative_rect=pygame.Rect(300, 50, 200, 50),
    text='Generators: 0',
    manager=ui["manager"]
    )

    ui["prestige_label"] = UILabel(
    relative_rect=pygame.Rect(550, 50, 200, 50),
    text='Prestiges: 0',
    manager=ui["manager"]
    )

    ui["coin_button"] = UIButton(
    relative_rect=pygame.Rect(50, 150, 200, 50),
    text='Click for Coins',
    manager=ui["manager"]
    )

    ui["generator_button"] = UIButton(
    relative_rect=pygame.Rect(300, 150, 200, 50),
    text='Buy Generator',
    manager=ui["manager"]
    )

    ui["prestige_button"] = UIButton(
    relative_rect=pygame.Rect(550, 150, 200, 50),
    text='Prestige',
    manager=ui["manager"]
    )

    ui["quit_button"] = UIButton(
    relative_rect=pygame.Rect(350, 500, 100, 50),
    text='Quit',
    manager=ui["manager"]
    )

    return ui

def event_handler(event, ui):
    if event.type == pygame_gui.UI_BUTTON_PRESSED:
        if event.ui_element == ui["coin_button"]:
            coin_clicker()
        elif event.ui_element == ui["generator_button"]:
            generator_purchase()
        elif event.ui_element == ui["prestige_button"]:
            prestige()
        elif event.ui_element == ui["quit_button"]:
            pygame.quit()
            exit()

def update_ui(ui, window_surface):
    ui["coin_label"].set_text(f'Coins: {int(game_state["coins"])}')
    ui["generator_label"].set_text(f'Generators: {int(game_state["generators"])}')
    ui["prestige_label"].set_text(f'Prestiges: {int(game_state["prestiges"])}')
    ui["generator_button"].set_text(f'Buy Generator (Cost: {int(game_state["gen_cost"])})')
    ui["prestige_button"].set_text(f'Prestige (Cost: {int(game_state["pres_cost"])})')
    ui["manager"].draw_ui(window_surface)