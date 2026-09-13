# ⌬⌥ 𝚂𝙰𝙸𝙺𝙾✦𝚂𝚈𝚂𝚃𝙴𝙼𝙴⬢
# SAIKO NO BRAIN — SYSTÈME DE COMBAT

joueurs = {}


def creer_joueur(pseudo):
    if pseudo not in joueurs:
        joueurs[pseudo] = {
            "pv": 100,
            "blessure": 0,
            "vivant": True
        }


def afficher_pv(pseudo):
    pv = joueurs[pseudo]["pv"]

    barres = pv // 10
    vide = 10 - barres

    return "█" * barres + "▒" * vide + f" {pv}%"


def attaquer(attaquant, cible, ballon):
    creer_joueur(attaquant)
    creer_joueur(cible)

    if not joueurs[cible]["vivant"]:
        return f"☠ {cible} est déjà éliminé."

    print("⌬⌥ 𝚂𝙰𝙸𝙺𝙾✦𝚂𝚈𝚂𝚃𝙴𝙼𝙴⬢")
    print()
    print("⚠ ATTAQUE DÉTECTÉE")
    print(f"🎯 Cible : {cible}")
    print(f"⚽ Ballon : {ballon}")
    print()
    print(f"{cible} doit utiliser !esquiv")
    print("⏱ Temps limite : 5 secondes")


def esquiver(pseudo):
    creer_joueur(pseudo)

    print("⌬⌥ SYSTÈME")
    print()
    print(f"✓ {pseudo} réussit son esquive !")
    print("Aucun dégât.")


def afficher_stats(pseudo):
    creer_joueur(pseudo)

    print("⌬⌥ 𝚂𝙰𝙸𝙺𝙾✦𝚂𝚈𝚂𝚃𝙴𝙼𝙴⬢")
    print()
    print(f"👤 Joueur : {pseudo}")
    print(f"❤️ PV : {afficher_pv(pseudo)}")
    print(f"🩸 Blessure : {joueurs[pseudo]['blessure']}")
    print(f"☠ Statut : {'VIVANT' if joueurs[pseudo]['vivant'] else 'ÉLIMINÉ'}")


# TEST DU SYSTÈME
print("⌬⌥ 𝚂𝙰𝙸𝙺𝙾✦𝚂𝚈𝚂𝚃𝙴𝙼𝙴⬢")
print("✓ Système démarré.")
print("✓ Incarnation : HIGH-RISE INVASION")
