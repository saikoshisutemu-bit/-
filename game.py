# 🎮 SAIKO NO BRAIN — GAME SYSTEM

MAX_PV = 100
DEGATS_BALLON = 10


def creer_joueur():
    return {
        "pv": MAX_PV,
        "blessure": 0,
        "vivant": True,
        "esquive": False
    }


def afficher_pv(joueur):
    pv = joueur["pv"]

    pleines = pv // 10
    vides = 10 - pleines

    return "█" * pleines + "▒" * vides + f" {pv}%"


def subir_degats(joueur, degats):
    joueur["pv"] -= degats

    if joueur["pv"] <= 0:
        joueur["pv"] = 0
        joueur["vivant"] = False

    joueur["blessure"] += degats


def esquiver(joueur):
    joueur["esquive"] = True


def reinitialiser_esquive(joueur):
    joueur["esquive"] = False


def soigner(joueur, soin):
    joueur["pv"] += soin

    if joueur["pv"] > MAX_PV:
        joueur["pv"] = MAX_PV


def doubler_blessure(joueur):
    joueur["blessure"] *= 2
