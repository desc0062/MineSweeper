# Model/Cellule.py
#

from Model.Constantes import *
#
# Modélisation d'une cellule de la grille d'un démineur
#

def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)

def isContenuCorrect (n:int)->bool:
    """
    Vérifie que le contenu d'une cellule est correct
    :param n: contenu d'une cellule
    :return: True (si contenu correct) or False (si contenu incorrect)
    """
    tf = False
    if type(n) == int:
        if n>=0 and n<=8 or n == const.ID_MINE:
            tf = True
    return tf

def construireCellule (contenu:int = 0,visible:bool = False)->dict:
    """
    Construit une cellule
    :param contenu: contenu d'une cellule
    :param visible: True (si cellule visible) or False (si cellule non visible)
    :return: dictionnaire de la cellule
    """
    if isContenuCorrect(contenu) is not True:
        raise ValueError(f"construireCellule : le contenu {contenu} n’est pas correct ")

    if type(visible) != bool:
        raise TypeError(f"construireCellule : le second paramètre {type(visible)} n’est pas un booléen »")

    cellule = {
        const.CONTENU : contenu,
        const.VISIBLE : visible,
        const.ANNOTATION: None
    }
    return cellule

def getContenuCellule(cellule:dict)->int:
    """
    Cherche le contenu d'une cellule
    :param cellule: dictionnaire de la cellule
    :return: contenu de la cellule
    """
    if type_cellule(cellule) is not True:
        raise TypeError("getContenuCellule : Le paramètre n’est pas une cellule.")

    return cellule[const.CONTENU]


def isVisibleCellule(cellule: dict) -> bool:
    """
    Cherche si la cellule est visible ou non
    :param cellule: dictionnaire de la cellule
    :return: True (si cellule visible) or False (si cellule non visible)
    """
    if type_cellule(cellule) is not True:
        raise TypeError("isVisibleCellule : Le paramètre n’est pas une cellule.")

    return cellule[const.VISIBLE]


def setContenuCellule(cellule:dict, contenu:int) -> None:
    """
    Change le contenu d'une cellule
    :param cellule: dictionnaire d'une cellule
    :param contenu: contenu de la cellule
    :return: nouveau contenu de la cellule
    """
    if type_cellule(cellule) is not True:
        raise TypeError("setContenuCellule : Le premier paramètre n'est pas une cellule.")
    if type(contenu) != int:
        raise TypeError("setContenuCellule : Le second paramètre n'est pas un entier.")
    if isContenuCorrect(contenu) is not True:
        raise ValueError(f"setContenuCellule : la valeur du contenu {contenu} n’est pas correcte.")

    if contenu == -1:
        contenu = const.ID_MINE

    cellule[const.CONTENU] = contenu
    return None

def setVisibleCellule(cellule:dict,tf:bool)->None:
    """
    Change la visibilité de la cellule
    :param cellule: dictionnaire d'une cellule
    :param tf: cellule visible ou non
    :return: dépendant de la visibilité de la cellule, la rend visible ou non
    """
    if type_cellule(cellule) is not True:
        raise TypeError("setVisibleCellule : Le premier paramètre n'est pas une cellule.")
    if type(tf) != bool:
        raise TypeError("setVisibleCellule : Le second paramètre n'est pas un booléen.")

    if cellule[const.VISIBLE] != tf:
        cellule[const.VISIBLE] = tf
    return None

def contientMineCellule(cellule:dict)->bool:
    """
    Vérifie si une cellule contient une mine
    :param cellule: dictionnaire d'une cellule
    :return: True (si mine) or False
    """
    if type_cellule(cellule) is not True:
        raise TypeError("contientMineCellule : Le premier paramètre n'est pas une cellule.")

    tf = False
    if cellule[const.CONTENU] == const.ID_MINE:
        tf = True
    return tf

def isAnnotationCorrecte(annotation:str)->bool:
    """
    Vérifie l'annotation d'une cellule
    :param annotation: annotation
    :return: True (si annotation correcte) or False (si erreur)
    """
    tf = False
    if annotation == None or annotation == const.DOUTE or annotation == const.FLAG:
        tf = True
    return tf

def getAnnotationCellule(cellule:dict)->str:
    """
    Cherche l'nanotation d'une cellule
    :param cellule: dictionnaire d'une cellule
    :return: annotation de la cellule
    """
    if type_cellule(cellule) is not True:
        raise TypeError("getAnnotationCellule : le paramètre valeur_du paramètre n’est pas une cellule.")
    if const.ANNOTATION not in cellule:
        return None

    return cellule[const.ANNOTATION]

def changeAnnotationCellule(cellule: dict) -> None:
    """
    Change l'annotation d'une cellule
    :param cellule: dictionnaire d'une cellule
    :return: None
    """
    if type_cellule(cellule) is not True:
        raise TypeError("changeAnnotationCellule : le paramètre n’est pas une cellule.")

    if cellule[const.ANNOTATION] == None:
        cellule[const.ANNOTATION] = const.FLAG
    elif cellule[const.ANNOTATION] == const.FLAG:
        cellule[const.ANNOTATION] = const.DOUTE
    else:
        cellule[const.ANNOTATION] = None
    return None

def reinitialiserCellule(cellule:dict)->None:
    """
    Réinitialise la cellule
    :param cellule: dictionnaire d'une cellule
    :return: None
    """
    setContenuCellule(cellule,0)
    setVisibleCellule(cellule,False)
    return None