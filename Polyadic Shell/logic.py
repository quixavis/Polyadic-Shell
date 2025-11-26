from state import game_state
from data import DATA

game_state["mdro_cost"] = int(DATA["mdrones"]["base_cost"] * (1 + DATA["mdrones"]["scaling"] * game_state["mdrones"]))
game_state["cnsd_cost"] = int(DATA["consolidations"]["base_cost"] * (1 + DATA["consolidations"]["scaling"] * game_state["consolidations"]))
game_state["production_rate"] = int(game_state["mdrones"] * DATA["mdrones"]["mdrone_rate"] * (1 + DATA["consolidations"]["consolidation_boost"] * game_state["consolidations"]))

def regolith_clicker():
    game_state["regolith"] += DATA["regolith"]["regolith_per_click"]

def mdrone_purchase():
    if game_state["regolith"] >= game_state["mdro_cost"]:
        game_state["regolith"] -= game_state["mdro_cost"]
        game_state["mdrones"] += 1
        game_state["mdro_cost"] = int(DATA["mdrones"]["base_cost"] * (1 + DATA["mdrones"]["scaling"] * game_state["mdrones"]))
        return True
    else:
        return False

def consolidate():
    if game_state["regolith"] >= game_state["cnsd_cost"]:
        game_state["regolith"] = 0
        game_state["mdrones"] = 0
        game_state["consolidations"] += 1
        game_state["cnsd_cost"] = int(DATA["consolidations"]["base_cost"] * (1 + DATA["consolidations"]["scaling"] * game_state["consolidations"] ))
        game_state["mdro_cost"] = int(DATA["mdrones"]["base_cost"] * (1 + DATA["mdrones"]["scaling"] * game_state["mdrones"]))
        return True
    else:
        return False

def update_game(dt):
    game_state["mdro_cost"] = DATA["mdrones"]["base_cost"] * (1 + DATA["mdrones"]["scaling"] * game_state["mdrones"])
    game_state["cnsd_cost"] = DATA["consolidations"]["base_cost"] * (1 + DATA["consolidations"]["scaling"] * game_state["consolidations"])
    game_state["production_rate"] = game_state["mdrones"] * DATA["mdrones"]["mdrone_rate"] * (1 + DATA["consolidations"]["consolidation_boost"] * game_state["consolidations"])
    game_state["regolith"] += game_state["production_rate"] * dt




