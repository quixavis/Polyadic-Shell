from game.state import game_state
from game.data import DATA
from game.logic import regolith_clicker, mdrone_purchase, fabricator_purchase, synthsteel_convert, foundry_purchase
import pygame
import pygame_gui
from pygame_gui.elements import UIButton, UILabel, UITextBox
import os

def create_screen():
    pygame.display.set_caption('Polyadic Shell')
    window_surface = pygame.display.set_mode((800, 600), pygame.RESIZABLE | pygame.SCALED)

    return window_surface

def create_ui():
    ui = {}

    theme_path = os.path.join(os.path.dirname(__file__), "theme.json")
    ui["manager"] = pygame_gui.UIManager((800, 600), theme_path)

    ui["intro_text"] = UITextBox(
        html_text='',
        relative_rect=pygame.Rect(0, 0, 800, 600),
        manager=ui["manager"],
        object_id="#terminal_text"
    )

    ui["outro_text"] = UITextBox(
        html_text='',
        relative_rect=pygame.Rect(0, 0, 800, 600),
        manager=ui["manager"],
        object_id="#terminal_text"
    )

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
    text='regolith: 0',
    manager=ui["manager"]
    )

    ui["synthsteel_label"] = UILabel(
    relative_rect=pygame.Rect(50, 250, 200, 50),
    text='synthsteel: 0',
    manager=ui["manager"]
    )

    ui["synthsteel_cost_label"] = UILabel(
    relative_rect=pygame.Rect(50, 270, 200, 50),
    text='synthsteel cost: 0',
    manager=ui["manager"],
    object_id="#sub_label"
    )


    ui["mdrone_label"] = UILabel(
    relative_rect=pygame.Rect(300, 50, 200, 50),
    text='mdrones: 0',
    manager=ui["manager"]
    )

    ui["mdrone_cost_label"] = UILabel(
    relative_rect=pygame.Rect(300, 70, 200, 50),
    text='mdrones cost: 0',
    manager=ui["manager"],
    object_id="#sub_label"
    )

    ui["fabricator_label"] = UILabel(
    relative_rect=pygame.Rect(550, 50, 200, 50),
    text='fabricators: 0',
    manager=ui["manager"]
    )

    ui["fabricator_cost_label"] = UILabel(
    relative_rect=pygame.Rect(550, 70, 200, 50),
    text='fabricators cost: 0',
    manager=ui["manager"],
    object_id="#sub_label"
    )

    ui["foundry_label"] = UILabel(
    relative_rect=pygame.Rect(300, 250, 200, 50),
    text='foundries: 0',
    manager=ui["manager"]
    )

    ui["foundry_cost_label"] = UILabel(
    relative_rect=pygame.Rect(300, 270, 200, 50),
    text='foundries cost: 0',
    manager=ui["manager"],
    object_id="#sub_label"
    )

    ui["end_label"] = UILabel(
    relative_rect=pygame.Rect(550, 270, 200, 50),
    text='Cost: 10,000 synthsteel',
    manager=ui["manager"],
    object_id="#sub_label"
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

    ui["synthsteel_button"] = UIButton(
    relative_rect=pygame.Rect(50, 350, 200, 50),
    text='Forge synthsteel',
    manager=ui["manager"]
    )

    ui["mdrone_button"] = UIButton(
    relative_rect=pygame.Rect(300, 150, 200, 50),
    text='Build mining drone',
    manager=ui["manager"]
    )

    ui["fabricator_button"] = UIButton(
    relative_rect=pygame.Rect(550, 150, 200, 50),
    text='Build fabricator',
    manager=ui["manager"]
    )

    ui["foundry_button"] = UIButton(
    relative_rect=pygame.Rect(300, 350, 200, 50),
    text='Build foundry',
    manager=ui["manager"]
    )

    ui["quit_button"] = UIButton(
    relative_rect=pygame.Rect(350, 500, 100, 50),
    text='Quit',
    manager=ui["manager"]
    )

    ui["debug_add_synthsteel"] = UIButton(
    relative_rect=pygame.Rect(650, 500, 120, 50),
    text='Add synthsteel',
    manager=ui["manager"]
    )

    ui["end_button"] = UIButton(
    relative_rect=pygame.Rect(550, 350, 200, 50),
    text='Build orbital ring',
    manager=ui["manager"]
    )

    ui["debug_add_synthsteel"].hide()

    ui["status_label_mask"] = pygame.Surface((200, 30), pygame.SRCALPHA)
    ui["status_label_mask"].fill((0, 0, 0, 255))

    animations = {
        "fade_in_out": {
            "active": False,
            "duration": 0.75,
            "elapsed": 0,
            "version": 1,
            "surface": None
        },

        "intro_text": {
            "active": False,
            "elapsed": 0,
            "version": 1,
            "letter_index": 0,
            "current_text": ""
        },

        "outro_text": {
            "active": False,
            "elapsed": 0,
            "version": 1,
            "letter_index": 0,
            "current_text": ""
        }
    }

    ui["regolith_label"].hide()
    ui["mdrone_label"].hide()
    ui["fabricator_label"].hide()
    ui["regolith_button"].hide()
    ui["mdrone_button"].hide()
    ui["fabricator_button"].hide()
    ui["debug_button"].hide()
    ui["quit_button"].hide()
    ui["status_label"].hide()
    ui["intro_text"].hide()
    ui["outro_text"].hide()
    ui["synthsteel_label"].hide()
    ui["synthsteel_button"].hide()
    ui["foundry_label"].hide()
    ui["foundry_button"].hide()
    ui["synthsteel_cost_label"].hide()
    ui["mdrone_cost_label"].hide()
    ui["foundry_cost_label"].hide()
    ui["fabricator_cost_label"].hide()
    ui["end_label"].hide()
    ui["end_button"].hide()

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

def intro_text_tick(animations, ui, dt):
    if animations["intro_text"]["active"] == True:
        letter_index = animations["intro_text"]["letter_index"]

        if animations["intro_text"]["version"] == 1:
            if letter_index >= len(DATA["intro_text"]):
                animations["intro_text"]["version"] = 0
                animations["intro_text"]["elapsed"] = 0
                return

            if animations["intro_text"]["elapsed"] >= 0.05:
                if DATA["intro_text"][letter_index] == "§":
                    animations["intro_text"]["current_text"] += "<br>"
                elif DATA["intro_text"][letter_index] == "α":
                    animations["intro_text"]["current_text"] += "<font face='space_mono'>"
                elif DATA["intro_text"][letter_index] == "ω":
                    animations["intro_text"]["current_text"] += "</font>"
                else:
                    animations["intro_text"]["current_text"] += DATA["intro_text"][letter_index]

                ui["intro_text"].set_text(animations["intro_text"]["current_text"] + "_")
                if ui["intro_text"].scroll_bar is not None:
                    ui["intro_text"].scroll_bar.set_scroll_from_start_percentage(1.0)
                    ui["intro_text"].update(dt)
                animations["intro_text"]["elapsed"] -= 0.05
                animations["intro_text"]["letter_index"] += 1
        elif animations["intro_text"]["elapsed"] >= 5:
            animations["intro_text"]["active"] = False
            return


        animations["intro_text"]["elapsed"] += dt

def outro_text_tick(animations, ui, dt):
    if animations["outro_text"]["active"] == True:
        letter_index = animations["outro_text"]["letter_index"]

        if animations["outro_text"]["version"] == 1:
            if letter_index >= len(DATA["outro_text"]):
                animations["outro_text"]["version"] = 0
                animations["outro_text"]["elapsed"] = 0
                return

            if animations["outro_text"]["elapsed"] >= 0.09:
                if DATA["outro_text"][letter_index] == "§":
                    animations["outro_text"]["current_text"] += "<br>"
                elif DATA["outro_text"][letter_index] == "α":
                    animations["outro_text"]["current_text"] += "<font face='space_mono'>"
                elif DATA["outro_text"][letter_index] == "ω":
                    animations["outro_text"]["current_text"] += "</font>"
                else:
                    animations["outro_text"]["current_text"] += DATA["outro_text"][letter_index]

                ui["outro_text"].set_text(animations["outro_text"]["current_text"] + "_")
                if ui["outro_text"].scroll_bar is not None:
                    ui["outro_text"].scroll_bar.set_scroll_from_start_percentage(1.0)
                    ui["outro_text"].update(dt)
                animations["outro_text"]["elapsed"] -= 0.09
                animations["outro_text"]["letter_index"] += 1
        elif animations["outro_text"]["elapsed"] >= 5:
            animations["outro_text"]["active"] = False
            return


        animations["outro_text"]["elapsed"] += dt

def change_mode(ui, animations, new_mode):
    game_state["mode"] = new_mode
    if new_mode == "menu":
        ui["intro_text"].hide()
        ui["outro_text"].hide()
        ui["title_label"].show()
        ui["subtitle_label"].show()
        ui["start_button"].show()
        ui["regolith_label"].hide()
        ui["mdrone_label"].hide()
        ui["fabricator_label"].hide()
        ui["regolith_button"].hide()
        ui["mdrone_button"].hide()
        ui["fabricator_button"].hide()
        ui["debug_button"].hide()
        ui["quit_button"].hide()
        ui["status_label"].hide()
        ui["synthsteel_label"].hide()
        ui["synthsteel_button"].hide()
        ui["foundry_label"].hide()
        ui["foundry_button"].hide()
        ui["synthsteel_cost_label"].hide()
        ui["mdrone_cost_label"].hide()
        ui["foundry_cost_label"].hide()
        ui["fabricator_cost_label"].hide()
        ui["end_label"].hide()
        ui["end_button"].hide()
    elif new_mode == "intro":
        animations["intro_text"]["active"] = True
        ui["intro_text"].show()
        ui["outro_text"].hide()
        ui["title_label"].hide()
        ui["subtitle_label"].hide()
        ui["start_button"].hide()
        ui["regolith_label"].hide()
        ui["mdrone_label"].hide()
        ui["fabricator_label"].hide()
        ui["regolith_button"].hide()
        ui["mdrone_button"].hide()
        ui["fabricator_button"].hide()
        ui["debug_button"].hide()
        ui["quit_button"].hide()
        ui["status_label"].hide()
        ui["synthsteel_label"].hide()
        ui["synthsteel_button"].hide()
        ui["foundry_label"].hide()
        ui["foundry_button"].hide()
        ui["synthsteel_cost_label"].hide()
        ui["mdrone_cost_label"].hide()
        ui["foundry_cost_label"].hide()
        ui["fabricator_cost_label"].hide()
        ui["end_label"].hide()
        ui["end_button"].hide()
    elif new_mode == "game":
        ui["intro_text"].hide()
        ui["outro_text"].hide()
        ui["title_label"].hide()
        ui["subtitle_label"].hide()
        ui["start_button"].hide()
        ui["regolith_label"].show()
        ui["mdrone_label"].show()
        ui["fabricator_label"].show()
        ui["regolith_button"].show()
        ui["mdrone_button"].show()
        ui["fabricator_button"].show()
        ui["debug_button"].show()
        ui["quit_button"].show()
        ui["status_label"].show()
        ui["synthsteel_label"].show()
        ui["synthsteel_button"].show()
        ui["foundry_label"].show()
        ui["foundry_button"].show()
        ui["synthsteel_cost_label"].show()
        ui["mdrone_cost_label"].show()
        ui["foundry_cost_label"].show()
        ui["fabricator_cost_label"].show()
        ui["end_label"].show()
        ui["end_button"].show()
    elif new_mode == "outro":
        animations["outro_text"]["active"] = True
        ui["outro_text"].show()
        ui["intro_text"].hide()
        ui["title_label"].hide()
        ui["subtitle_label"].hide()
        ui["start_button"].hide()
        ui["regolith_label"].hide()
        ui["mdrone_label"].hide()
        ui["fabricator_label"].hide()
        ui["regolith_button"].hide()
        ui["mdrone_button"].hide()
        ui["fabricator_button"].hide()
        ui["debug_button"].hide()
        ui["quit_button"].hide()
        ui["status_label"].hide()
        ui["synthsteel_label"].hide()
        ui["synthsteel_button"].hide()
        ui["foundry_label"].hide()
        ui["foundry_button"].hide()
        ui["synthsteel_cost_label"].hide()
        ui["mdrone_cost_label"].hide()
        ui["foundry_cost_label"].hide()
        ui["fabricator_cost_label"].hide()
        ui["end_label"].hide()
        ui["end_button"].hide()

def event_handler(event, ui, animations):
    if event.type == pygame_gui.UI_BUTTON_PRESSED:
        if event.ui_element == ui["regolith_button"]:
            regolith_clicker()
        elif event.ui_element == ui["mdrone_button"]:
            if mdrone_purchase() == False:
                ui["status_label"].set_text("Not enough synthsteel")
                start_fade(animations, ui["status_label_mask"])
        elif event.ui_element == ui["fabricator_button"]:
            if fabricator_purchase() == False:
                ui["status_label"].set_text("Not enough synthsteel")
                start_fade(animations, ui["status_label_mask"])
        elif event.ui_element == ui["quit_button"]:
            game_state["running"] = False
        elif event.ui_element == ui["debug_button"]:
            ui["status_label"].set_text("Debug Mode Toggled")
            start_fade(animations, ui["status_label_mask"])
            game_state["debug"] = not game_state["debug"]
            if game_state["debug"] == True:
                ui["debug_add_synthsteel"].show()
            else:
                ui["debug_add_synthsteel"].hide()
        elif event.ui_element == ui["debug_add_synthsteel"]:
            game_state["synthsteel"] += 1000
        elif event.ui_element == ui["start_button"]:
            change_mode(ui, animations, "intro")
        elif event.ui_element == ui["synthsteel_button"]:
            if synthsteel_convert() == False:
                ui["status_label"].set_text("Not enough regolith")
                start_fade(animations, ui["status_label_mask"])
        elif event.ui_element == ui["foundry_button"]:
            if foundry_purchase() == False:
                ui["status_label"].set_text("Not enough synthsteel")
                start_fade(animations, ui["status_label_mask"])
        elif event.ui_element == ui["end_button"]:
            change_mode(ui, animations, "outro")
    elif event.type == pygame.QUIT:
        game_state["running"] = False

def update_ui(ui, animations, dt, window_surface):
    background = pygame.Surface((800, 600))
    background.fill(pygame.Color("#000000"))

    if game_state["mode"] == "menu":
        pass
    if game_state["mode"] == "intro":
        intro_text_tick(animations, ui, dt)
        if animations["intro_text"]["active"] == False:
            change_mode(ui, animations, "game")
    elif game_state["mode"] == "game":
        ui["regolith_label"].set_text(f'Regolith: {int(game_state["regolith"])}')
        ui["mdrone_label"].set_text(f'Mining Drones: {int(game_state["mdrones"])}')
        ui["fabricator_label"].set_text(f'Fabricators: {int(game_state["fabricators"])}')
        ui["synthsteel_label"].set_text(f'Synthsteel: {int(game_state["synthsteel"])}')
        ui["foundry_label"].set_text(f'Foundries: {int(game_state["foundries"])}')
        ui["mdrone_cost_label"].set_text(f'Cost: {int(game_state["mdro_cost"])} synthsteel')
        ui["fabricator_cost_label"].set_text(f'Cost: {int(game_state["fab_cost"])} synthsteel')
        ui["synthsteel_cost_label"].set_text(f'Cost: {int(DATA["synthsteel"]["conversion_cost"])} regolith')
        ui["foundry_cost_label"].set_text(f'Cost: {int(game_state["foundry_cost"])} synthsteel')
    elif game_state["mode"] == "outro":
        outro_text_tick(animations, ui, dt)
        if animations["outro_text"]["active"] == False:
            game_state["running"] = False
    
    ui["manager"].draw_ui(background)

    if game_state["mode"] == "game":
        fade_in_out_tick(animations, dt)
        background.blit(ui["status_label_mask"], (300, 230))

    window_surface.blit(background, (0, 0))

    pygame.display.update()