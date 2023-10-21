
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# mid = (a + b + c + d)/4
# print(round(mid, 2))
a = int(input("введи числа, и программа выведет среднее значение. когда закончишь, введи 0\n"))
if a == 0:
    print("oshibka")
sum = 0
colvo = 0
while a != 0:
    sum = sum + a
    colvo = colvo + 1
    print("da")
    a = int(input())
    if a == 0:
        print(sum / colvo)