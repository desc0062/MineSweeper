# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse

# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                                         and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True


def construireGrilleDemineur(nb_lignes: int, nb_colonnes: int) -> list:
    """
    Construction d'une grille de démineur
    :param nb_lignes: nombre de lignes
    :param nb_colonnes: nombre de colonnes
    :return: grille
    """
    if type(nb_lignes) != int or type(nb_colonnes) != int:
        raise TypeError(f"construireGrilleDemineur : Le nombre de lignes {type(nb_lignes)} ou de colonnes {type(nb_colonnes)} n’est pas un entier.")

    if nb_lignes <= 0 or nb_colonnes <= 0:
        raise ValueError(f"« construireGrilleDemineur : Le nombre de lignes {nb_lignes} ou de colonnes {nb_colonnes} est négatif ou nul.")
    grille = []
    for i in range(nb_lignes):
        ligne = []
        for j in range(nb_colonnes):
            ligne += [construireCellule()]
        grille += [ligne]
    return grille


def getNbLignesGrilleDemineur(grille: list) -> int:
    """
    Chercher le nombre de lignes dans une grille
    :param grille: grille de démineur
    :return: nombre de lignes
    """
    if type_grille_demineur(grille) is not True:
        raise TypeError("getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")

    return len(grille)


def getNbColonnesGrilleDemineur(grille: list) -> int:
    """
    Chercher le nombre de colonnes
    :param grille: grille de démineur
    :return: nombre de colonnes
    """
    if type_grille_demineur(grille) is not True:
        raise TypeError("getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")

    return len(grille[0])


def isCoordonneeCorrecte(grille: list, coordonnees: tuple) -> bool:
    """
    Vérifie que la cellule se trouve dans la grille
    :param grille: grille de démineur
    :param coordonnees: coordonnées de la cellule
    :return: True (dans la grille) ou False (hors de la grille)
    """
    if type_grille_demineur(grille) is not True or type(coordonnees) != tuple:
        raise TypeError("isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")

    tf = False
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            # Vérifier si la coordonnée est placée dans la grille
            if coordonnees == (i, j):
                tf = True
    return tf


def getCelluleGrilleDemineur(grille: list, coordonnees: tuple) -> dict:
    """
    Cherche le dictionnaire d'une case de démineur
    :param grille: grille de démineur
    :param coordonnees: coordonnées de la cellule
    :return: dictionnaire de la cellule
    """
    if type_grille_demineur(grille) is not True or type(coordonnees) != tuple or type_coordonnee(
            coordonnees) is not True:
        raise TypeError("getCelluleGrilleDemineur : un des paramètres n’est pas du bon type.")
    if isCoordonneeCorrecte(grille, coordonnees) is not True:
        raise IndexError("getCelluleGrilleDemineur : coordonnée non contenue dans la grille.")

    return grille[coordonnees[0]][coordonnees[1]]


def getContenuGrilleDemineur(grille: list, coordonnees: tuple) -> int:
    return getContenuCellule(grille[coordonnees[0]][coordonnees[1]])


def setContenuGrilleDemineur(grille: list, coordonnees: tuple, contenu: int) -> int:
    return setContenuCellule(grille[coordonnees[0]][coordonnees[1]], contenu)


def isVisibleGrilleDemineur(grille: list, coordonnees: tuple) -> bool:
    return isVisibleCellule(grille[coordonnees[0]][coordonnees[1]])


def setVisibleGrilleDemineur(grille: list, coordonnees: tuple, tf: bool) -> bool:
    return setVisibleCellule(grille[coordonnees[0]][coordonnees[1]], tf)


def contientMineGrilleDemineur(grille: list, coordonnees: tuple) -> bool:
    return contientMineCellule(grille[coordonnees[0]][coordonnees[1]])


def getCoordonneeVoisinsGrilleDemineur(grille: list, coordonnees: tuple) -> list:
    """
    Faire une liste des voisins d'une cellule
    :param grille: grille de démineur
    :param coordonnees: coordonnées de la cellule
    :return: liste des voisins de la cellule
    """
    if type_grille_demineur(grille) is not True or type(coordonnees) != tuple:
        raise TypeError("getCoordonneeVoisinsGrilleDemineur : un des paramètres n’est pas du bon type.")
    if isCoordonneeCorrecte(grille, coordonnees) is not True:
        raise IndexError("getCoordonneeVoisinsGrilleDemineur : la coordonnée n’est pas dans la grille.")

    voisins = []

    # Sélection des cases voisines
    for i in range(coordonnees[0] - 1, coordonnees[0] + 2):
        for j in range(coordonnees[1] - 1, coordonnees[1] + 2):
            # Vérifier que les cases voisines existent dans la grille
            if isCoordonneeCorrecte(grille, (i, j)):
                voisins.append((i, j))
    # Retirer la case du milieu de la liste des cases voisines
    voisins.remove((coordonnees[0], coordonnees[1]))
    return voisins


def placerMinesGrilleDemineur(grille: list, nb: int, coordNoMine: tuple) -> None:
    """
    Placer un certain nombre de mines dans une grille
    :param grille: grille de démineur
    :param nb: nombre de mines à placer
    :param coordNoMine: première case rendue visible qui ne doit pas avoir de mine
    :return: None
    """
    if nb < 0 or nb > (getNbColonnesGrilleDemineur(grille)) * (getNbLignesGrilleDemineur(grille)) - 1:
        raise ValueError("placerMinesGrilleDemineur : Nombre de bombes à placer incorrect.")
    if not isCoordonneeCorrecte(grille, coordNoMine):
        raise IndexError("placerMinesGrilleDemineur : la coordonnée n'est pas dans la grille.")

    i = 0

    # Tant qu'il n'y a pas le nombre de mines voulues
    while i < nb:
        coord_mine = construireCoordonnee(randint(0, len(grille)), randint(0, len(grille[0])))
        # Vérifier que la case où est placée la mine n'est pas sur la première case cliquée
        if (coord_mine != coordNoMine) and isCoordonneeCorrecte(grille, coord_mine) \
        and getContenuGrilleDemineur(grille,coord_mine) != const.ID_MINE:
            setContenuGrilleDemineur(grille, coord_mine, const.ID_MINE)
            i += 1
    compterMinesVoisinesGrilleDemineur(grille)
    return None


def compterMinesVoisinesGrilleDemineur(grille: list) -> None:
    """
    Compte le nombre de mines autour d'une cellule
    :param grille: grille de démineur
    :return: None
    """
    voisin = []
    count = 0

    for i in range(len(grille)):
        for j in range(len(grille[0])):
            # Si le contenu de la case n'est pas une mine
            if grille[i][j][const.CONTENU] != const.ID_MINE:
                voisin = getCoordonneeVoisinsGrilleDemineur(grille, (i, j))
                for k in range(len(voisin)):
                    # Si les voisins sont des mines
                    if getContenuGrilleDemineur(grille, voisin[k]) == const.ID_MINE:
                        # Augmenter son contenu
                        count += 1
                    setContenuGrilleDemineur(grille, (i, j), count)
            voisin.clear()
            count = 0
    return None


def getNbMinesGrilleDemineur(grille: list) -> int:
    """
    Compte le nombre de mines dans une grille
    :param grille: grille de démineur
    :return: nombre de mines dans la grille
    """
    if type_grille_demineur(grille) is not True:
        raise ValueError("getNbMinesGrilleDemineur : le paramètre n’est pas une grille.")

    # Compter le nombre de mines en parcourant chaque case
    mine = 0
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j][const.CONTENU] == const.ID_MINE:
                mine += 1
    return mine


def getAnnotationGrilleDemineur(grille: list, coordonnees: tuple) -> str:
    return getAnnotationCellule(grille[coordonnees[0]][coordonnees[1]])


def getMinesRestantesGrilleDemineur(grille: list) -> int:
    """
    Cherche le nombre de mines restantes dans une grille
    :param grille: grille
    :return: Soustraction du nombre de mines totale par le nombre de drapeaux placés
    """

    nb = 0
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j][const.ANNOTATION] == const.FLAG:
                nb += 1
    return getNbMinesGrilleDemineur(grille) - nb


def gagneGrilleDemineur(grille: list) -> bool:
    """
    Vérifie que la grille est finie
    :param grille: grille
    :return: True (si partie gagnée) or False (si erreur)
    """
    tf = True
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if (contientMineGrilleDemineur(grille, (i, j))) and (isVisibleGrilleDemineur(grille, (i, j))) \
            or (contientMineGrilleDemineur(grille, (i, j))) and (getAnnotationCellule(getCelluleGrilleDemineur(grille, (i,j))) != const.FLAG) \
            or (contientMineGrilleDemineur(grille, (i, j)) is not True) and (isVisibleGrilleDemineur(grille, (i, j)) is not True):
                tf = False
    return tf


def perduGrilleDemineur(grille: list) -> bool:
    """
    Vérifie si la partie est perdue
    :param grille: grille de démineur
    :return: True (si partie perdue) or False (si pas d'erreur)
    """
    tf = False
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if contientMineGrilleDemineur(grille, (i, j)) and isVisibleGrilleDemineur(grille, (i, j)):
                tf = True
    return tf


def reinitialiserGrilleDemineur(grille: list) -> None:
    """
    Réinitialise la grille en cours
    :param grille: grille de démineur
    :return: None
    """
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            reinitialiserCellule(grille[i][j])
    return None


def decouvrirGrilleDemineur(grille: list, coordonnees: tuple) -> set:
    """
    Découvre les cellules autour d'une cellule vide
    :param grille: grille de démineur
    :param coordonnees: coordonnées d'une cellule
    :return: ensemble de cellules découvertes
    """
    cellules_decouvertes = set()
    cellules_a_decouvrir = [coordonnees]
    # Tant qu'il reste des cases à découvrir
    while len(cellules_a_decouvrir) > 0:
        coord_actu = cellules_a_decouvrir.pop()
        # Si la cellule n'est pas déjà révélée
        if coord_actu not in cellules_decouvertes:
            setVisibleGrilleDemineur(grille, coord_actu, True)
            cellules_decouvertes.add(coord_actu)
            # Si la case révélée est vide, rajouter ses voisines dans la liste des cases à découvrir
            if getContenuGrilleDemineur(grille, coord_actu) == 0:
                voisines = getCoordonneeVoisinsGrilleDemineur(grille, coord_actu)
                cellules_a_decouvrir.extend(voisines)
    return cellules_decouvertes


def simplifierGrilleDemineur(grille: list, coordonnees: tuple) -> set:
    """
    Simplifie la grille en découvrant toutes les cellules où il n'y a pas de drapeaux autour d'une cellule
    :param grille: grille de démineur
    :param coordonnees: coordonnées d'une cellule
    :return: ensemble des cellules découvertes
    """
    ensemble = set()
    count = 0
    voisins = getCoordonneeVoisinsGrilleDemineur(grille, coordonnees)

    # Vérifier que la case est déjà révélée
    if isVisibleGrilleDemineur(grille, coordonnees) is not True:
        return set()
    else:
        # Compte le nb de drapeux au voisinnage
        for i in range(len(voisins)):
            if (grille[getLigneCoordonnee(voisins[i])][getColonneCoordonnee(voisins[i])])\
            [const.ANNOTATION] == const.FLAG:
                count += 1
        # Vérifier que le nombre de drapeaux est égal au nombre de mines
        if getContenuGrilleDemineur(grille, coordonnees) == count:
            for j in range(len(voisins)):
                # Si c'est le cas, révéler toutes les cases non-annotées
                if isVisibleGrilleDemineur(grille, voisins[j]) is not True \
                and getAnnotationGrilleDemineur(grille,voisins[j]) == None:
                    setVisibleGrilleDemineur(grille, voisins[j], True)
                    ensemble.add(voisins[j])
    return ensemble


def ajouterFlagsGrilleDemineur(grille: list, coordonnees: tuple) -> set:
    """
    Ajoute des drapeaux quand il reste un nombre de cases non visible égal au contenu de la cellule
    :param grille: grille de démineur
    :param coordonnees: coordonnées d'une cellule
    :return: ensemble des
    """
    ensemble = set()
    count = 0
    voisins = getCoordonneeVoisinsGrilleDemineur(grille, coordonnees)

    # Vérifier si la case visible n'est pas une bombe ou un zéro
    if (isVisibleGrilleDemineur(grille, coordonnees) and getContenuGrilleDemineur(grille, coordonnees) == 0) \
    or (isVisibleGrilleDemineur(grille, coordonnees) and getContenuGrilleDemineur(grille,coordonnees) == const.ID_MINE):
        return set()
    else:
        # Compter le nombre de cases non découvertes
        for i in range(len(voisins)):
            if isVisibleGrilleDemineur(grille, voisins[i]) is not True:
                count += 1
        # Vérifier que le nombre de cases non découvertes est égal au contenu de la case
        if getContenuGrilleDemineur(grille, coordonnees) == count:
            for j in range(len(voisins)):
                # Si c'est le cas, changer leur annotation en drapeau
                if isVisibleGrilleDemineur(grille, voisins[j]) is not True:
                    if getAnnotationGrilleDemineur(grille, voisins[j]) == None:
                        (grille[getLigneCoordonnee(voisins[j])][getColonneCoordonnee(voisins[j])])[const.ANNOTATION] = const.FLAG
                        ensemble.add(voisins[j])
    return ensemble

def simplifierToutGrilleDemineur(grille: list) -> tuple:
    """
    Simplie toute la grille en appliquant les dexu fonctions précédentes
    :param grille: grille de démineur
    :return: un tuple contenant l'ensemble des cellules découvertes et l'ensemble des cellules où un drapeau a été placé
    """
    visible, drapeau = set(), set()
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            coord = (i, j)
            visible.update(simplifierGrilleDemineur(grille, coord))
            drapeau.update(ajouterFlagsGrilleDemineur(grille, coord))
    return (visible, drapeau)
