# Необходимо реализовать свой проект на каком-то другом языке программирования( + прикрепить исходник на Java)
# Ссылка на 2 е домашнее задание  https://github.com/Garik073/OOPJavaHome2/tree/master/src


import Calc      

def main_menu():
        
        my_cl = Calc.iCalculator() 
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        
        play = True
        while play:

            answer = input("Select operation:\n"
                           "+. Сложение \n"
                           "-. Вычитание \n"
                           "*. Умножение \n"
                           "/. Деление \n"
                           "5. Exit\n")
            match answer:
                case "+":
                    print(a, "+",b, "=", my_cl.add(a,b))
                case "-":
                    print(a, "-",b, "=", my_cl.subtract(a,b))
                case "*":
                    print(a, "*",b, "=", my_cl.multiply(a,b))
                case "/":
                    print(a, "/",b, "=", my_cl.div(a,b))
                case "5":
                    play = False
                case _:
                    print("Try again!\n")


main_menu()
