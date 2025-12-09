from game.state import game_state
from game.data import DATA

game_state["mdro_cost"] = int(DATA["mdrones"]["base_cost"] * (1 + DATA["mdrones"]["scaling"] * game_state["mdrones"]))
game_state["fab_cost"] = int(DATA["fabricators"]["base_cost"] * (1 + DATA["fabricators"]["scaling"] * game_state["fabricators"]))
game_state["foundry_cost"] = int(DATA["foundries"]["base_cost"] * (1 + DATA["foundries"]["scaling"] * game_state["foundries"]))
game_state["regolith_production"] = int(game_state["mdrones"] * DATA["mdrones"]["mdrone_rate"])
game_state["synthsteel_production"] = int(game_state["foundries"] * DATA["foundries"]["foundry_rate"])
game_state["mdrone_production"] = int(game_state["fabricators"] * DATA["fabricators"]["fabricator_rate"])

def regolith_clicker():
    game_state["regolith"] += DATA["regolith"]["regolith_per_click"]

def synthsteel_convert():
    if game_state["regolith"] >= DATA["synthsteel"]["conversion_cost"]:
        game_state["regolith"] -= DATA["synthsteel"]["conversion_cost"]
        game_state["synthsteel"] += 1
        return True
    else:
        return False

def mdrone_purchase():
    if game_state["synthsteel"] >= game_state["mdro_cost"]:
        game_state["synthsteel"] -= game_state["mdro_cost"]
        game_state["mdrones"] += 1
        game_state["mdro_cost"] = int(DATA["mdrones"]["base_cost"] * (1 + DATA["mdrones"]["scaling"] * game_state["mdrones"]))
        return True
    else:
        return False

def fabricator_purchase():
    if game_state["synthsteel"] >= game_state["fab_cost"]:
        game_state["synthsteel"] -= game_state["fab_cost"]
        game_state["fabricators"] += 1
        game_state["fab_cost"] = int(DATA["fabricators"]["base_cost"] * (1 + DATA["fabricators"]["scaling"] * game_state["fabricators"]))
        return True
    else:
        return False

def foundry_purchase():
    if game_state["synthsteel"] >= game_state["foundry_cost"]:
        game_state["synthsteel"] -= game_state["foundry_cost"]
        game_state["foundries"] += 1
        game_state["foundry_cost"] = int(DATA["foundries"]["base_cost"] * (1 + DATA["foundries"]["scaling"] * game_state["foundries"]))
        return True
    else:
        return False

def update_game(dt):
    game_state["mdro_cost"] = DATA["mdrones"]["base_cost"] * (1 + DATA["mdrones"]["scaling"] * game_state["mdrones"])
    game_state["fab_cost"] = DATA["fabricators"]["base_cost"] * (1 + DATA["fabricators"]["scaling"] * game_state["fabricators"])
    game_state["regolith_production"] = game_state["mdrones"] * DATA["mdrones"]["mdrone_rate"]
    game_state["synthsteel_production"] = game_state["foundries"] * DATA["foundries"]["foundry_rate"]
    game_state["mdrone_production"] = game_state["fabricators"] * DATA["fabricators"]["fabricator_rate"]
    game_state["regolith"] += game_state["regolith_production"] * dt
    game_state["mdrones"] += game_state["mdrone_production"] * dt
    if game_state["foundries"] >= 1 and game_state["regolith"] >= DATA["synthsteel"]["conversion_cost"]:
        game_state["regolith"] -= DATA["synthsteel"]["conversion_cost"] * dt
        game_state["synthsteel"] += game_state["synthsteel_production"] * dt