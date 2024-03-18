# Coordonnee.py

import const
import unittest

# Définition des coordonnées (ligne, colonne)

def type_coordonnee(coord: tuple) -> bool:
    """
    Détermine si le paramètre correspond ou non à une coordonnée.

    Cette fonction teste notamment si les lignes et colonnes sont bien positives. Dans le cas contraire, la fonction
    retourne `False`.

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: `True` si le paramètre correspond à une coordonnée, `False` sinon.
    """
    return type(coord) == tuple and len(coord) == 2 and type(coord[0]) == int and type(coord[1]) == int \
        and coord[0] >= 0 and coord[1] >= 0

def construireCoordonnee(num_ligne:int,num_colonne:int)->tuple:
    """
    Crée une coordonnée de cellule
    :param num_ligne: numéro de ligne
    :param num_colonne: numéro de colonne
    :return: coordonnée
    """
    if type(num_ligne)!=int or type(num_colonne)!=int:
        raise TypeError(f"construireCoordonnee : construireCoordonnee : Le numéro de ligne {type(num_ligne)} ou le numéro de colonne {type(num_colonne)} ne sont pas des entiers")
    return (num_ligne,num_colonne)

def getLigneCoordonnee(coordonnee:tuple)->int:
    """
    Cherche la ligne d'une coordonnée
    :param coordonnee: coordonnée d'une cellule
    :return: numéro de ligne de la cellule
    """
    if type(coordonnee)!=tuple:
        raise TypeError("getLigneCoordonnee : Le paramètre n’est pas une coordonnée")
    return coordonnee[0]

def getColonneCoordonnee(coordonnee:tuple)->int:
    """
    Cherche le numéro de colonne de la cellule
    :param coordonnee: coordonnée d'une cellule
    :return: numéro de colonne de la cellule
    """
    if type(coordonnee)!=tuple:
        raise TypeError(" getColonneCoordonnee : Le paramètre n’est pas une coordonnée")
    return coordonnee[1]