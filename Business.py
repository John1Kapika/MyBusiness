arenda: int
technic: int
resurs: int
other: int
worker: int
workerZp: int = 0
kapital1Time: int
kapital1: int
amorTime: int
revenue: int
profit1: float
profit2: float

print("Добро пожаловать в программу для расчёта бюджета для Вашего предприятия!")
arenda = int(input("Укажите стоимость аренды помещения (в месяц): "))
technic = int(input("Укажите траты на оборудование: "))
resurs = int(input("Укажите траты на расходники: "))
worker = int(input("Укажите количество сотрудников: "))
if worker > 0:
    if worker == 1:
        workerZp = int(input("Укажите зарплату сотрудника: "))
    else:
        workerArray = [i for i in range(worker)]
        for i in range(len(workerArray)):
            workerArray[i] = int(input("Укажите зарплату "+ str(i+1) + " сотрудника: "))
            workerZp = workerZp + workerArray[i]
other = int(input("Укажите иные расходы: "))
kapital1Time = int(input("Укажите время (в месяцах), на которое необходимо, расчитать стартовый капитал, без вложения выручки: "))
kapital1 = technic + (arenda + resurs)*(1+kapital1Time) + workerZp*kapital1Time + other
print("Ваш стартовый капитал должен составлять - "+str(kapital1)+" рублей.")
amorTime = int(input("\nУкажите в какой срок (в месяцах) Вы хотели бы закончить процесс амортизации, начиная с"
                     " "+str(kapital1Time+1)+" месяца: "))
profit1 = 0.01*(int(input("Укажите процент от чистой прибыли, который Вы хотели бы реинвестировать в предприятие: ")))
profit1 = profit1 + 0.01*(int(input("Укажите процент от чистой прибыли, который Вы хотели бы вкладывать в"
                                    " финансовую подушку: ")))
revenue = (int(input("Укажите итоговую желаемую среднемесячную чистейшую прибыль, начиная с "+str(kapital1Time+1)+""
                                    " месяца: ")))/(1-profit1)
profit1 = arenda + workerZp + resurs + kapital1/amorTime + revenue
profit2 = arenda + workerZp + resurs + revenue
print("При заданных условиях Ваша среднесуточная прибыль должна составлять - " + str((profit1*12)/365) + " рублей в " +
      str(amorTime) + " месяцев амортизации. И в последующем - " + str((profit2*12)/365)+" рублей.")