from state import game_state
from logic import regolith_clicker, mdrone_purchase, consolidate
import pygame
import pygame_gui
from pygame_gui.elements import UIButton, UILabel

def create_screen():
    pygame.init()
    pygame.display.set_caption('Polyadic Shell')
    window_surface = pygame.display.set_mode((800, 600))
    background = pygame.Surface((800, 600))
    background.fill(pygame.Color("#000000"))

    return window_surface, background

def create_ui():
    ui = {}

    ui["manager"] = pygame_gui.UIManager((800, 600))

    ui["status_label"] = UILabel(
    relative_rect=pygame.Rect(300, 230, 200, 30),
    text='Polyadic Shell',
    manager=ui["manager"]
    )

    ui["regolith_label"] = UILabel(
    relative_rect=pygame.Rect(50, 50, 200, 50),
    text='regoliths: 0',
    manager=ui["manager"]
    )

    ui["mdrone_label"] = UILabel(
    relative_rect=pygame.Rect(300, 50, 200, 50),
    text='mdrones: 0',
    manager=ui["manager"]
    )

    ui["consolidate_label"] = UILabel(
    relative_rect=pygame.Rect(550, 50, 200, 50),
    text='consolidates: 0',
    manager=ui["manager"]
    )

    ui["debug_button"] = UIButton(
    relative_rect=pygame.Rect(700, 10, 80, 30),
    text='Debug',
    manager=ui["manager"]
    )

    ui["regolith_button"] = UIButton(
    relative_rect=pygame.Rect(50, 150, 200, 50),
    text='Mine regolith',
    manager=ui["manager"]
    )

    ui["mdrone_button"] = UIButton(
    relative_rect=pygame.Rect(300, 150, 200, 50),
    text='Buy mdrone',
    manager=ui["manager"]
    )

    ui["consolidate_button"] = UIButton(
    relative_rect=pygame.Rect(550, 150, 200, 50),
    text='consolidate',
    manager=ui["manager"]
    )

    ui["quit_button"] = UIButton(
    relative_rect=pygame.Rect(350, 500, 100, 50),
    text='Quit',
    manager=ui["manager"]
    )

    ui["debug_add_regolith"] = UIButton(
    relative_rect=pygame.Rect(650, 500, 120, 50),
    text='Add 1000 regoliths',
    manager=ui["manager"]
    )

    ui["debug_add_regolith"].hide()

    ui["status_label_mask"] = pygame.Surface((200, 30), pygame.SRCALPHA)
    ui["status_label_mask"].fill((0, 0, 0, 255))

    # ui["debug_button"].hide()

    # create animation elements

    animations = {
        "status_fade": {
            "active": False,
            "duration": 0.75,
            "elapsed": 0,
            "version": 1,
            "surface": ui["status_label_mask"]
        }
    }

    return ui, animations

def status_fade_tick(animations, dt):
    if animations["status_fade"]["active"]:
        progress = animations["status_fade"]["elapsed"] / animations["status_fade"]["duration"]
        if animations["status_fade"]["version"] == 1:
            animations["status_fade"]["surface"].set_alpha(255 - (progress * 255))
            if animations["status_fade"]["elapsed"] >= animations["status_fade"]["duration"]:
                animations["status_fade"]["version"] = 0
                animations["status_fade"]["elapsed"] = 0

        elif animations["status_fade"]["version"] == 0:
            animations["status_fade"]["surface"].set_alpha(0)
            if animations["status_fade"]["elapsed"] >= animations["status_fade"]["duration"]:
                animations["status_fade"]["version"] = -1
                animations["status_fade"]["elapsed"] = 0

        elif animations["status_fade"]["version"] == -1:
            animations["status_fade"]["surface"].set_alpha(progress * 255)
            if animations["status_fade"]["elapsed"] >= animations["status_fade"]["duration"]:
                animations["status_fade"]["active"] = False
                animations["status_fade"]["version"] = 1
                animations["status_fade"]["elapsed"] = 0
        
        animations["status_fade"]["elapsed"] += dt

def start_fade(animations):
    animations["status_fade"]["active"] = True
    animations["status_fade"]["elapsed"] = 0
    animations["status_fade"]["version"] = 1

def event_handler(event, ui, animations):
    if event.type == pygame_gui.UI_BUTTON_PRESSED:
        if event.ui_element == ui["regolith_button"]:
            regolith_clicker()
        elif event.ui_element == ui["mdrone_button"]:
            if mdrone_purchase() == False:
                ui["status_label"].set_text("Not enough regolith")
                start_fade(animations)
        elif event.ui_element == ui["consolidate_button"]:
            if consolidate() == False:
                ui["status_label"].set_text("Not enough regolith")
                start_fade(animations)
            else:
                print("Consolidated")
                ui["status_label"].set_text("Consolidated")
                start_fade(animations)
        elif event.ui_element == ui["quit_button"]:
            pygame.quit()
            exit()
        elif event.ui_element == ui["debug_button"]:
            ui["status_label"].set_text("Debug Mode Toggled")
            start_fade(animations)
            game_state["debug"] = not game_state["debug"]
            if game_state["debug"] == True:
                ui["debug_add_regolith"].show()
            else:
                ui["debug_add_regolith"].hide()
        elif event.ui_element == ui["debug_add_regolith"]:
            game_state["regolith"] += 1000

def update_ui(ui, animations, dt, window_surface, background):
    ui["regolith_label"].set_text(f'Regolith: {int(game_state["regolith"])}')
    ui["mdrone_label"].set_text(f'Mining Drones: {int(game_state["mdrones"])}')
    ui["consolidate_label"].set_text(f'Consolidations: {int(game_state["consolidations"])}')
    ui["mdrone_button"].set_text(f'Buy Mining Drone (Cost: {int(game_state["mdro_cost"])})')
    ui["consolidate_button"].set_text(f'Consolidate (Cost: {int(game_state["cnsd_cost"])})')
    ui["manager"].draw_ui(window_surface)

    status_fade_tick(animations, dt)

    window_surface.blit(background, (0, 0))
    ui["manager"].draw_ui(window_surface)
    window_surface.blit(animations["status_fade"]["surface"], (300, 230))

    pygame.display.update()