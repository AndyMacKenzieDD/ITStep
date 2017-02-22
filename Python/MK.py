# Игра Mortal Kombat 12 

import random 
#Выбор класса игрока
print("Выберите класс своего персонажа") 
chr = int(input("1 - Силовик. 2 - Ловкач. 3 - Кувалдин\n")) 
if(chr == 1): 
    hp = 1500 
    damage = 50 
elif(chr == 2): 
    hp = 750 
    damage = 85 
else: 
    print("Вы победили!") 
    exit() 
#Выбор класса противника
print("Выберите класс персонажа противника") 
chrenemy = int(input("1 - Силовик. 2 - Ловкач. 3 - Кувалдин \n")) 
if(chrenemy == 1): 
    hc = 1500 
    damage = 200 
elif(chrenemy == 2): 
    hc = 750 
    damage = 50 
elif(chrenemy == 3): 
    print("Вы проиграли!") 
    exit() 

#Let's the combat begin 
while(hp > 0 and hc > 0): 
    print("У вас ", hp, " очков здоровья")
    print("У противника ", hc, " очков здоровья") 
#Вариант атаки 
    print("Выберите вариант атаки") 
    ap = int(input("1 - Верхняя. 2 - Нижняя ")) 
#Вариант блока 
    print("Выберите вариант блока") 
    bp = int(input("1 - Верхний. 2 - Нижний ")) 
#рандом для компа 
    ac = random.randint(1,2) 
    bc = random.randint(1,2) 
    print("\nВы наносите удар") 
#условия урона от выбора персоажа 
    if(chr == 1): 
        r = random.randint(-50, 100) 
    else: 
        r = random.randint(1, 100) 
    if(r < 0): 
        print("Вы промахнулись =(") 
    else: 
#Условия блокирования и направления ударов 
        if(ap != bc): 
#расчёт урона при пробитии в зависимости от персонажа
            if(chr == 1): 
                print("Ваш нанесённый урон = ", damage + r) 
                hc = hc - (damage + r) 
            else: 
                print("Ваш нанесённый урон = ", damage + r, " + ", damage + r) 
                hc = hc - ((damage + r) * 2) 
        else: 
            print("Вы попали в блок =(") 
#условия на нулевое значение жизненных поинтов 
    if(hc < 0): 
        print("Вы победили!") 
        break 
    print("Противник наносит удар") 
#Вариант урона от выбора персонажа противника 
    if (chrenemy == 1): 
        r = random.randint(-100, 200) 
    else: 
        r = random.randint(1, 100) 
#Условия на промах 
    if(r < 0): 
        print("Противник промахнулся =)") 
    else: 
#Условия на блок и направление удара 
        if(ac != bp): 
#условия на урон от персонажа 
            if(chrenemy == 1): 
                print("Нанесённый урон противника = ", damage + r) 
                hp = hp - (damage + r) 
            else: 
                print("Нанесённый урон противника = ", damage + r, " + ", damage + r) 
                hp = hp - ((damage + r) * 2) 
        else: 
            print("Противник попал в блок =)") 
#Условия на отсутсвие ХП 
        if (hp < 0): 
            print("Вы проиграли") 
            break 
    input("Что бы нанести следующий удар, нажми Enter") 
    print("\n") 
input("Press Enter to continue..")