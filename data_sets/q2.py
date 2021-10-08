"""
#
# File        : q2
# Created     : 08/10/21 11:00 AM
# Author      : R. Aravind
# Version     : v1.0.0
# Licencing   : (C) 2021 Aravind Rajesh Kanna, LYIT
                Available under GNU Public License (GPL)
# Credits    :
# Maintainer  :
# Description : Lotto players
#
"""


import random

if __name__ == '__main__':
    '''

           Main method of application 

           Lotto players

           Parameters:

            none

           Returns:

            none

    '''

    week1 = ["Joe", "John", "Jane", "Mick", "Mary", "Ann", "Rick", "Johnne", "Aine", "Brenda"]
    random_num_1 = [random.randrange(1, 10) for i in range(0, 10)]
    week1_lotto = {}
    for i in range(10):
        week1_lotto[week1[i]] = random_num_1[i]
    print(week1_lotto)

    week2 = ["Jack", "Mary", "Phil", "John", "Pat", "Joe", "Luke", "Bill", "Ben", "Nathan"]
    random_num_2 = [random.randrange(1, 10) for i in range(0, 10)]
    week2_lotto = {}
    for i in range(10):
        week2_lotto[week2[i]] = random_num_2[i]
    print(week2_lotto)
