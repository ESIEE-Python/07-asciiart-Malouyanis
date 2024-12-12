"""
Ce module contient des fonctions pour encoder une chaîne de caractères
sous forme de tuples indiquant chaque caractère et son nombre d'occurrences consécutives.
"""

import sys

# Augmenter la limite de récursion si nécessaire
sys.setrecursionlimit(3000)

def artcode_i(s):
    """
    Encode une chaîne de caractères en une liste de tuples, avec un algorithme itératif.

    Args:
        s (str): la chaîne de caractères à encoder.

    Returns:
        list: une liste de tuples (caractère, nombre d'occurrences).
    """
    if not s:  # Si la chaîne est vide, retourner une liste vide
        return []
    result = []
    current_char = s[0]  # Initialiser avec le premier caractère
    count = 0  # Compteur d'occurrences

    for char in s:
        if char == current_char:  # Si le caractère est le même que le précédent
            count += 1
        else:  # Si un nouveau caractère est rencontré
            result.append((current_char, count))  # Ajouter le tuple au résultat
            current_char = char  # Mettre à jour le caractère courant
            count = 1  # Réinitialiser le compteur

    # Ajouter le dernier groupe de caractères
    result.append((current_char, count))
    return result


def artcode_r(s):
    """
    Encode une chaîne de caractères en une liste de tuples, avec un algorithme récursif.

    Args:
        s (str): la chaîne de caractères à encoder.

    Returns:
        list: une liste de tuples (caractère, nombre d'occurrences).
    """
    if not s:  # Si la chaîne est vide, retourner une liste vide
        return []
    def helper(substring):
        """
        Fonction auxiliaire pour traiter récursivement la chaîne.
        """
        if not substring:  # Cas de base : chaîne vide
            return []
        # Compter les occurrences consécutives du premier caractère
        first_char = substring[0]
        count = 1
        while count < len(substring) and substring[count] == first_char:
            count += 1
        # Retourner le tuple du caractère courant et continuer avec le reste de la chaîne
        return [(first_char, count)] + helper(substring[count:])
    return helper(s)


def main():
    """
    Fonction principale pour tester les fonctions `artcode_i` et `artcode_r`.
    """
    test_string = 'MMMMaaacXolloMM'
    print("Codage itératif :", artcode_i(test_string))
    print("Codage récursif :", artcode_r(test_string))


if __name__ == "__main__":
    main()
