import random
from time import sleep

# сделать, чтобы игрок мог выбирать сторону, куда повернуть с помощью инпут

hp = 100
speed = 0 
distance = 400

yetti = 1
tree = 2
rock = 3

while True:

    ce = random.randint(0, 6)
    if ce == rock:
        print("вы столкнулись с ТЯЖЁЛЫМ РОКОМ")
        stor = random.randint(0, 3)
        print("попробуй увернуться! вправо - 1, влево - 2, прыжок - 3")
        stro = int(input())
        if stro == stor:
            print("у тебя получилось! едем дальше")
            sleep(1)
        elif stro>3 or 0>=stro:
            print("так нельзя! ты врезался")
            hp -= 5
            print("осталось хп", hp)
            sleep(1)
        elif stro != stor:
            print("не вышло! лох")
            hp -= 5
            print("осталось хп", hp)
            sleep(1)
    
    elif ce == yetti:
        print("вы столкнулись с МОХНАТАЯ ШНЯГА")
        stor = random.randint(0, 3)
        print("попробуй увернуться! вправо - 1, влево - 2, прыжок - 3")
        stro = int(input())
        if stro == stor:
            print("у тебя получилось! едем дальше")
            sleep(1)
        elif stro>3 or 0>=stro:
            print("так нельзя! ты врезался")
            hp -= 5
            print("осталось хп", hp)
            sleep(1)
        elif stro != stor:
            print("не вышло! лох")
            hp -= 5
            print("осталось хп", hp)
            sleep(1)
        
    elif ce == tree:
        print("вы столкнулись с АААААААААА ПРИРОДА")
        stor = random.randint(0, 3)
        print("попробуй увернуться! вправо - 1, влево - 2, прыжок - 3")
        stro = int(input())
        if stro == stor:
            print("у тебя получилось! едем дальше")
            sleep(1)
        elif stro>3 or 0>=stro:
            print("так нельзя! ты врезался")
            hp -= 5
            print("осталось хп", hp)
            sleep(1)
        elif stro != stor:
            print("не вышло! лох")
            hp -= 5
            print("осталось хп", hp)
            sleep(1)
        
        
    speed += 1
    distance -= speed
    print(f"\nвы едете со скоростью", speed,"м/с\nпроехать осталось", distance, "м")

    if hp<=0:
        print("ты сдох бро")
        break
    if (distance <= 0):
        print("УРА БРО КРАСАВА ДОЕХАЛ")
        break

    sleep(0.6)
