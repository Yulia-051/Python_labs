money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while 1:
    if count != 0: spend *= (1 + increase)
    money_capital -=spend - salary
    count+=1
    if money_capital<=0:
        count-=1
        break
print("Количество месяцев, которое можно протянуть без долгов:", count)
