#-*-coding:utf-8-*-
#---------------------------
#GUESS NUMBER GAME
#Author:  Liu Siyuan
#Date:    2018/01/23
#--------------------------
import random

def generate_num_rand():
    num_rand = random.randint(1,100)
    return num_rand

def scanf_num_gamer():
    for i in range(5):
        num_input = input("Please input a number(-1 means exit game):")
        if num_input.isdigit():
            break
    if num_input.isdigit() != True:
        return -1
    return int(num_input)

def cmp_num(num1, num2):
    if num1 > num2:
        return 1
    elif num1 < num2:
        return 2
    else:
        return 0
    
def result_display(cmp_result):
    if cmp_result == 1:
        print("Guess Smaller!")
    elif cmp_result == 2:
        print("Guess Bigger!")
    else:
        print("---Congratulations!---")
        print("-------You Win!-------")

def select_menu():
    print("Do you want to play again?(y/n)")
    option_gamer = str(input())
    if option_gamer == 'y':
        return 0
    elif option_gamer == 'n':
        return 1
    else:
        return 2

def guess_num_game():
    while True:
        num_static = generate_num_rand()
        while True:
            num_gamer = scanf_num_gamer()
            if num_gamer == -1:
                break 
            cmp_result = cmp_num(num_static, num_gamer)
            result_display(cmp_result)
            if cmp_result == 0:
                break
            
        while True:
            gamer_option = select_menu()
            if gamer_option == 0 or gamer_option == 1:
                break
            else:
                print("Unknow Option!")

        if gamer_option == 0:
            continue
        else:
            break;
        
    return 0

def main():
    guess_num_game()

main()
