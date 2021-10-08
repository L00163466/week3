"""
#
# File        : q1
# Created     : 08/10/21 9:45 AM
# Author      : R. Aravind
# Version     : v1.0.0
# Licencing   : (C) 2021 Aravind Rajesh Kanna, LYIT
                Available under GNU Public License (GPL)
# Credits    :
# Maintainer  :
# Description : Printing Modules and Grades
#
"""


if __name__ == '__main__':
    '''

       Main method of application 

       Printing Modules and Grades

       Parameters:

        none

       Returns:

        none

    '''

    LNumbers = ("L12345", "L54321")
    Modules = ["Java_ooprogramming", "Python_Scripting"]
    Grades = {"Java_ooprogramming": {"L12345": 40, "L54321": 70}, "Python_Scripting": {"L12345": 69, "L54321": 58}}

    selectedLNumber = input()

    for i in Modules:
        print("{0}:{1}".format(i, Grades[i][selectedLNumber]))
