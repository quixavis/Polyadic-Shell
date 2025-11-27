from game.state import game_state
from game.logic import regolith_clicker, mdrone_purchase, consolidate
import pygame
import pygame_gui
from pygame_gui.elements import UIButton, UILabel
import os

def create_screen():
    pygame.init()
    pygame.display.set_caption('Polyadic Shell')
    window_surface = pygame.display.set_mode((800, 600))

    return window_surface

def create_ui():
    ui = {}

    theme_path = os.path.join(os.path.dirname(__file__), "theme.json")
    ui["manager"] = pygame_gui.UIManager((800, 600), theme_path)

    ui["title_label"] = UILabel(
    relative_rect=pygame.Rect(250, 70, 300, 100),
    text='Polyadic Shell',
    manager=ui["manager"],
    object_id="#title_label"
    )

    ui["subtitle_label"] = UILabel(
    relative_rect=pygame.Rect(100, 170, 600, 100),
    text='An incremental game about an ancient colonial supply chain',
    manager=ui["manager"],
    )

    ui["start_button"] = UIButton(
    relative_rect=pygame.Rect(350, 300, 100, 50),
    text='Start',
    manager=ui["manager"],
    object_id="regular_button"
    )

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

    animations = {
        "fade_in_out": {
            "active": False,
            "duration": 0.75,
            "elapsed": 0,
            "version": 1,
            "surface": None
        }
    }

    ui["regolith_label"].hide()
    ui["mdrone_label"].hide()
    ui["consolidate_label"].hide()
    ui["regolith_button"].hide()
    ui["mdrone_button"].hide()
    ui["consolidate_button"].hide()
    ui["debug_button"].hide()
    ui["quit_button"].hide()
    ui["status_label"].hide()

    return ui, animations

def fade_in_out_tick(animations, dt):
    if animations["fade_in_out"]["active"] == True and animations["fade_in_out"]["surface"] != None:
        progress = animations["fade_in_out"]["elapsed"] / animations["fade_in_out"]["duration"]
        if animations["fade_in_out"]["version"] == 1:
            animations["fade_in_out"]["surface"].set_alpha(255 - (progress * 255))
            if animations["fade_in_out"]["elapsed"] >= animations["fade_in_out"]["duration"]:
                animations["fade_in_out"]["version"] = 0
                animations["fade_in_out"]["elapsed"] = 0

        elif animations["fade_in_out"]["version"] == 0:
            animations["fade_in_out"]["surface"].set_alpha(0)
            if animations["fade_in_out"]["elapsed"] >= animations["fade_in_out"]["duration"]:
                animations["fade_in_out"]["version"] = -1
                animations["fade_in_out"]["elapsed"] = 0

        elif animations["fade_in_out"]["version"] == -1:
            animations["fade_in_out"]["surface"].set_alpha(progress * 255)
            if animations["fade_in_out"]["elapsed"] >= animations["fade_in_out"]["duration"]:
                animations["fade_in_out"]["active"] = False
                animations["fade_in_out"]["version"] = 1
                animations["fade_in_out"]["elapsed"] = 0
        
        animations["fade_in_out"]["elapsed"] += dt

def start_fade(animations, surface):
    animations["fade_in_out"]["active"] = True
    animations["fade_in_out"]["elapsed"] = 0
    animations["fade_in_out"]["version"] = 1
    animations["fade_in_out"]["surface"] = surface

def change_mode(ui, new_mode):
    game_state["mode"] = new_mode
    if new_mode == "menu":
        ui["title_label"].show()
        ui["subtitle_label"].show()
        ui["start_button"].show()
        ui["regolith_label"].hide()
        ui["mdrone_label"].hide()
        ui["consolidate_label"].hide()
        ui["regolith_button"].hide()
        ui["mdrone_button"].hide()
        ui["consolidate_button"].hide()
        ui["debug_button"].hide()
        ui["quit_button"].hide()
        ui["status_label"].hide()
    elif new_mode == "game":
        ui["title_label"].hide()
        ui["subtitle_label"].hide()
        ui["start_button"].hide()
        ui["regolith_label"].show()
        ui["mdrone_label"].show()
        ui["consolidate_label"].show()
        ui["regolith_button"].show()
        ui["mdrone_button"].show()
        ui["consolidate_button"].show()
        ui["debug_button"].show()
        ui["quit_button"].show()
        ui["status_label"].show()

def event_handler(event, ui, animations):
    if event.type == pygame_gui.UI_BUTTON_PRESSED:
        if event.ui_element == ui["regolith_button"]:
            regolith_clicker()
        elif event.ui_element == ui["mdrone_button"]:
            if mdrone_purchase() == False:
                ui["status_label"].set_text("Not enough regolith")
                start_fade(animations, ui["status_label_mask"])
        elif event.ui_element == ui["consolidate_button"]:
            if consolidate() == False:
                ui["status_label"].set_text("Not enough regolith")
                start_fade(animations, ui["status_label_mask"])
            else:
                print("Consolidated")
                ui["status_label"].set_text("Consolidated")
                start_fade(animations, ui["status_label_mask"])
        elif event.ui_element == ui["quit_button"]:
            pygame.quit()
            exit()
        elif event.ui_element == ui["debug_button"]:
            ui["status_label"].set_text("Debug Mode Toggled")
            start_fade(animations, ui["status_label_mask"])
            game_state["debug"] = not game_state["debug"]
            if game_state["debug"] == True:
                ui["debug_add_regolith"].show()
            else:
                ui["debug_add_regolith"].hide()
        elif event.ui_element == ui["debug_add_regolith"]:
            game_state["regolith"] += 1000
        elif event.ui_element == ui["start_button"]:
            change_mode(ui, "game")

def update_ui(ui, animations, dt, window_surface):
    background = pygame.Surface((800, 600))
    background.fill(pygame.Color("#000000"))

    if game_state["mode"] == "menu":
        pass
    elif game_state["mode"] == "game":
        ui["regolith_label"].set_text(f'Regolith: {int(game_state["regolith"])}')
        ui["mdrone_label"].set_text(f'Mining Drones: {int(game_state["mdrones"])}')
        ui["consolidate_label"].set_text(f'Consolidations: {int(game_state["consolidations"])}')
        ui["mdrone_button"].set_text(f'Buy Mining Drone (Cost: {int(game_state["mdro_cost"])})')
        ui["consolidate_button"].set_text(f'Consolidate (Cost: {int(game_state["cnsd_cost"])})')
    
    ui["manager"].draw_ui(background)

    fade_in_out_tick(animations, dt)
    if game_state["mode"] == "game":
        background.blit(ui["status_label_mask"], (300, 230))

    window_surface.blit(background, (0, 0))

    pygame.display.update()