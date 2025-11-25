from state import game_state
from data import DATA
import time

game_state["gen_cost"] = int(DATA["generators"]["base_cost"] * (1 + DATA["generators"]["scaling"] * game_state["generators"]))
game_state["pres_cost"] = int(DATA["prestiges"]["base_cost"] * (1 + DATA["prestiges"]["scaling"] * game_state["prestiges"]))
game_state["production_rate"] = int(game_state["generators"] * DATA["generators"]["generator_rate"] * (1 + DATA["prestiges"]["prestige_boost"] * game_state["prestiges"]))

def coin_clicker():
    game_state["coins"] += DATA["coins"]["coins_per_click"]

def generator_purchase():
    if game_state["coins"] >= game_state["gen_cost"]:
        game_state["coins"] -= game_state["gen_cost"]
    else:
        return False
    game_state["generators"] += 1
    game_state["gen_cost"] = int(DATA["generators"]["base_cost"] * (1 + DATA["generators"]["scaling"] * game_state["generators"]))

def prestige():
    if game_state["coins"] >= game_state["pres_cost"]:
        game_state["coins"] = 0
        game_state["generators"] = 0
        game_state["prestiges"] += 1
        game_state["pres_cost"] = int(DATA["prestiges"]["base_cost"] * (1 + DATA["prestiges"]["scaling"] * game_state["prestiges"] ))
        game_state["gen_cost"] = int(DATA["generators"]["base_cost"] * (1 + DATA["generators"]["scaling"] * game_state["generators"]))
    else:
        return False

def update_game():
    now = time.time()
    delta = round(now - game_state["last_time"], 4)
    print(delta)
    game_state["last_time"] = now
    game_state["gen_cost"] = DATA["generators"]["base_cost"] * (1 + DATA["generators"]["scaling"] * game_state["generators"])
    game_state["pres_cost"] = DATA["prestiges"]["base_cost"] * (1 + DATA["prestiges"]["scaling"] * game_state["prestiges"])
    game_state["production_rate"] = game_state["generators"] * DATA["generators"]["generator_rate"] * (1 + DATA["prestiges"]["prestige_boost"] * game_state["prestiges"])
    game_state["coins"] += game_state["production_rate"] * delta
    print("coin_rate =", game_state["production_rate"])

