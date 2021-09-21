#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number *= -1

    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    liste = []
    for pre in prefixes:
        liste.append(pre + suffixe)
    return liste


def prime_integer_summation() -> int:
    prime_list = [2]
    for i in range(101):
        for diviseur in range(i - 2):
            if i % (diviseur + 2) == 0:
                break
            elif (diviseur + 2) == (i - 1):
                prime_list.append(i)
    somme = 0
    for prime in prime_list:
        somme += prime
    return somme


def factorial(number: int) -> int:
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


def use_continue() -> None:
    for i in range(11):
        if i == 5:
            continue
        else:
            print(i)
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    acceptance = []
    someoneIs50 = False
    someoneIs70 = False
    allAccepted = True
    for group in groups:
        if len(group) > 10 or len(group) <= 3:
            acceptance.append(False)
            continue
        for people in group:
            if people == 25:
                acceptance.append(False)
                allAccepted = False
                break
            if people < 18:
                acceptance.append(False)
                allAccepted = False
                break
            if (people > 70 or people == 50) and (someoneIs50 or someoneIs70):
                acceptance.append(False)
                allAccepted = False
                break
            if people == 50:
                someoneIs50 = True
            elif people > 70:
                someoneIs70 = True
        if allAccepted:
            acceptance.append(True)
        allAccepted = True
        someoneIs50 = False
        someoneIs70 = False
    return acceptance


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
