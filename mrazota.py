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
        hp -= 5
        print("осталось хп", hp)
        sleep(1)
    elif ce == yetti:
        print("вы столкнулись с МОХНАТАЯ ШНЯГА")
        hp -= 5
        print("осталось хп", hp)
        sleep(1)
    elif ce == tree:
        print("вы столкнулись с АААААААААА ПРИРОДА")
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