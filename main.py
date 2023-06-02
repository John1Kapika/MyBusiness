import this
from tkinter import*

a1 = 0
a2 = 1
a3 = 2
c = 0
arenda = 0
technic = 0
resurs = 0
other = 0
worker = 0
workerZp: int = 0
Kapital1Time = 0
kapital1 = 0
amorTime = 0
reinvestment = 0
pillow = 0
revenue = 0
profit1: float = 0
profit2: float = 0
btn4: Button

def clicked1():
    def clicked2():
        def clicked6():
            def clicked7():
                global amorTime
                global reinvestment
                global pillow
                global revenue
                amorTime = txtAmorTime.get()
                reinvestment = txtReinvestment.get()
                pillow = txtPillow.get()
                revenue = txtRevenue.get()

                n = j - 7
                lblAmorTime1.destroy()
                lblAmorTime2.destroy()
                lblAmorTime3 = Label(window, text="Амортизация: ")
                lblAmorTime3.grid(column=a1, row=n)
                lblAmorTime4 = Label(window, text="месяцев")
                lblAmorTime4.grid(column=a3, row=n)
                lblAmorTime = Label(window, text=txtAmorTime.get())
                lblAmorTime.grid(column=a2, row=n)
                txtAmorTime.destroy()

                n = n + 1
                lblReinvestment1.destroy()
                lblReinvestment2.destroy()
                lblReinvestment3 = Label(window, text="Ежемесячное реинвестирование: ")
                lblReinvestment3.grid(column=a1, row=n)
                lblReinvestment4 = Label(window, text="%")
                lblReinvestment4.grid(column=a3, row=n)
                lblReinvestment = Label(window, text=txtReinvestment.get())
                lblReinvestment.grid(column=a2, row=n)
                txtReinvestment.destroy()

                n = n + 1
                lblPillow1.destroy()
                lblPillow2.destroy()
                lblPillow3 = Label(window, text="Ежемесячный вклад в фин. подушку: ")
                lblPillow3.grid(column=a1, row=n)
                lblPillow4 = Label(window, text="%")
                lblPillow4.grid(column=a3, row=n)
                lblPillow = Label(window, text=txtPillow.get())
                lblPillow.grid(column=a2, row=n)
                txtPillow.destroy()

                n = n + 1
                lblRevenue1.destroy()
                lblRevenue2.destroy()
                lblRevenue3 = Label(window, text="Желаемая ЧИСТЕЙШАЯ прибыль: ")
                lblRevenue3.grid(column=a1, row=n)
                lblRevenue4 = Label(window, text="руб.")
                lblRevenue4.grid(column=a3, row=n)
                lblRevenue = Label(window, text=txtRevenue.get())
                lblRevenue.grid(column=a2, row=n)
                txtRevenue.destroy()
                btn6.destroy()

                global profit1
                global profit2
                revenue = int(revenue)/(1-0.01*(int(reinvestment)+int(pillow)))
                profit1 =  round(float((int(arenda) + int(workerZp) + int(resurs) + int(kapital1)/int(amorTime) +
                                  int(revenue))*12/365), 2)
                profit2 = round(float((int(arenda) + int(workerZp) + int(resurs) + int(revenue))*12/365), 2)

                n = n + 2
                lblProfit = Label(text="При заданных условиях Ваша среднесуточная прибыль должна составлять - " +
                                       str(profit1) + " рублей за " + str(amorTime) + " месяцев амортизации."
                                       " И в последующем - " + str(profit2)+" рублей.")
                lblProfit.grid(column=3, row=n)

            j = n + 2
            lblAmorTime1 = Label(window, text="\nУкажите в какой срок Вы\nхотели бы закончить процесс\n"
                                             "амортизации, начиная с "+str(int(Kapital1Time)+1)+" месяца: ")
            lblAmorTime1.grid(column=a1, row=j)
            txtAmorTime = Entry(window, width=10)
            txtAmorTime.grid(column=a2, row=j)
            lblAmorTime2 = Label(window, text="месяцев")
            lblAmorTime2.grid(column=a3, row=j)

            j = j + 3
            lblReinvestment1 = Label(window, text="Укажите процент от чистой\nприбыли, который Вы хотели бы"
                                                  "\nреинвестировать в предприятие: ")
            lblReinvestment1.grid(column=a1, row=j)
            txtReinvestment = Entry(window, width=10)
            txtReinvestment.grid(column=a2, row=j)
            lblReinvestment2 = Label(window, text="%")
            lblReinvestment2.grid(column=a3, row=j)

            j = j + 3
            lblPillow1 = Label(window, text="Укажите процент от чистой\nприбыли, который Вы хотели бы\nоткладывать в "
                                            "финансовую подушку: ")
            lblPillow1.grid(column=a1, row=j)
            txtPillow = Entry(window, width=10)
            txtPillow.grid(column=a2, row=j)
            lblPillow2 = Label(window, text="%")
            lblPillow2.grid(column=a3, row=j)

            j = j + 1
            lblRevenue1 = Label(window, text="Укажите итоговую желаемую\nсреднемесячную ЧИСТЕЙШУЮ\nприбыль, начиная с"
                                              " "+str(int(Kapital1Time)+1)+" месяца: ")
            lblRevenue1.grid(column=a1, row=j)
            txtRevenue = Entry(window, width=10)
            txtRevenue.grid(column=a2, row=j)
            lblRevenue2 = Label(window, text="руб.")
            lblRevenue2.grid(column=a3, row=j)

            btn6 = Button(window, text="Ввести данные", command=clicked7)
            btn6.grid(column=5, row=j)

        def clicked5():
            lblKapital1Time1.destroy()
            radKapital1Time1.destroy()
            radKapital1Time2.destroy()
            global Kapital1Time
            global kapital1
            kapital1 = int(technic) + (int(resurs) + int(arenda)) * (1 + int(Kapital1Time)) + workerZp * \
                       int(Kapital1Time) + int(other)
            lblKapital = Label(text="Ваш стартовый капитал должен составлять - " + str(kapital1) + " рублей.")
            lblKapital.grid(column=3, row=n)

            clicked6()

        def clicked3():
            def clicked4():
                lblKapital1Time1.configure(text="Предприятие будет\nсуществовать без реинвестрования ")
                lblKapital1Time = Label(window, text=txtKapital1Time.get())
                lblKapital1Time.grid(column=a2, row=j)
                global Kapital1Time
                global kapital1
                Kapital1Time = txtKapital1Time.get()
                txtKapital1Time.destroy()
                btn3.destroy()
                n = j + 1
                kapital1 = int(technic) + (int(resurs) + int(arenda))*(1+int(Kapital1Time)) + workerZp*\
                           int(Kapital1Time) + int(other)
                lblKapital = Label(text="Ваш стартовый капитал должен составлять - "+str(kapital1)+" рублей.")
                lblKapital.grid(column=3, row=n)

                clicked6()

            lblKapital1Time1.configure(text="Укажите время,\nна которое необходимо,\nрасчитать стартовый капитал: ")
            txtKapital1Time = Entry(window, width=10)
            txtKapital1Time.grid(column=a2, row=n)
            lblKapital1Time2 = Label(window, text="месяцев")
            lblKapital1Time2.grid(column=a3, row=n)
            radKapital1Time1.destroy()
            radKapital1Time2.destroy()

            btn3 = Button(window, text="Ввести данные", command=clicked4)
            btn3.grid(column=5, row=n)

        n: int = 5
        global workerZp
        if int(worker) > 1:
            lblWorkerZpArray = [i for i in range(int(worker))]
            for i in range(len(lblWorkerZp1Array)):
                n=n+1
                lblWorkerZp1Array[i].configure(text="Зарплата " + str(i + 1) + " сотрудника: ")
                lblWorkerZpArray[i] = Label(window, text=txtWorkerZpArray[i].get())
                lblWorkerZpArray[i].grid(column=a2, row=n)
                workerZpGap = txtWorkerZpArray[i].get()
                workerZp = workerZp + int(workerZpGap)
                txtWorkerZpArray[i].destroy()
        else:
            n = n + 1
            lblWorkerZp1.configure(text="Зарплата сотрудника: ")
            lblWorkerZp = Label(window, text=txtWorkerZp.get())
            lblWorkerZp.grid(column=a2, row=n)
            workerZpGap = txtWorkerZp.get()
            workerZp = int(workerZpGap)
            txtWorkerZp.destroy()
        n = n + 1
        lblOther1.configure(text="Иные расходы: ")
        lblOther = Label(window, text=txtOther.get())
        lblOther.grid(column=a2, row=n)
        other = txtOther.get()
        txtOther.destroy()

        n = n + 1
        lblKapital1Time1 = Label(window,
                                 text="Расчитывать стартовый капитал на\n несколько месяцев работы предприятия: ")
        lblKapital1Time1.grid(column=a1, row=n)
        radKapital1Time1 = Radiobutton(window, text='Да', value=1, command=clicked3)
        radKapital1Time2 = Radiobutton(window, text='Нет', value=2, command=clicked5)
        radKapital1Time1.grid(column=a2, row=n)
        radKapital1Time2.grid(column=a3, row=n)
        btn2.destroy()

    global arenda
    global resurs
    arenda = txtArenda.get()
    technic = txtTechnic.get()
    resurs = txtResurs.get()
    worker = txtWorker.get()
    lblArenda1.configure(text="Аренда: ")
    lblArenda = Label(window, text=txtArenda.get())
    lblArenda.grid(column=a2, row=1)
    txtArenda.destroy()
    lblTechnic1.configure(text="Расходы на оборудование: ")
    lblTechnic = Label(window, text=txtTechnic.get())
    lblTechnic.grid(column=a2, row=2)
    txtTechnic.destroy()
    lblResurs1.configure(text="Траты на расходники: ")
    lblResurs = Label(window, text=txtResurs.get())
    lblResurs.grid(column=a2, row=3)
    txtResurs.destroy()
    lblWorker1.configure(text="Количество сотрудников: ")
    lblWorker = Label(window, text=txtWorker.get())
    lblWorker.grid(column=a2, row=4)
    txtWorker.destroy()
    btn1.destroy()

    if int(worker) > 0:
        j = 5
        if int(worker) == 1:
            j = j + 1
            lblWorkerZp1 = Label(window, text="Укажите зарплату сотрудника: ")
            lblWorkerZp1.grid(column=a1, row=j)
            txtWorkerZp = Entry(window, width=10)
            txtWorkerZp.grid(column=a2, row=j)
            lblWorkerZp2 = Label(window, text="руб.")
            lblWorkerZp2.grid(column=a3, row=j)
        else:
            lblWorkerZp1Array = [i for i in range(int(worker))]
            txtWorkerZpArray = [i for i in range(int(worker))]
            lblWorkerZp2Array = [i for i in range(int(worker))]
            for i in range(len(lblWorkerZp1Array)):
                lblWorkerZp1Array[i] = Label(window, text="Укажите зарплату " + str(i + 1) + " сотрудника: ")
                j=j+1
                lblWorkerZp1Array[i].grid(column=a1, row=j)
                txtWorkerZpArray[i] = Entry(window, width=10)
                txtWorkerZpArray[i].grid(column=a2, row=j)
                lblWorkerZp2Array[i] = Label(window, text="руб.")
                lblWorkerZp2Array[i].grid(column=a3, row=j)
    j=j+1
    lblOther1 = Label(window, text="Укажите иные расходы: ")
    lblOther1.grid(column=a1, row=j)
    txtOther = Entry(window, width=10)
    txtOther.grid(column=a2, row=j)
    lblOther2 = Label(window, text="руб.")
    lblOther2.grid(column=a3, row=j)

    j = j + 1
    btn2 = Button(window, text="Ввести данные", command=clicked2)
    btn2.grid(column=5, row=j)


window = Tk()
#root = window

#root.iconbitmap('C:\Users\John Kapika\MB\icona.ico')
window.geometry('1620x600')
window.title("MyBusiness")
lbl = Label(window, text="Добро пожаловать в программу для расчёта бюджета Вашего бизнеса!\nЗдесь Вы сможете "
                         "узнать необходимый для создания предприятия стартовый капитал и когда сможете получать"
                         " желаемую чистую прибыль.\n")
lbl.grid(column=3, row=0)

lblArenda1 = Label(window, text="Укажите стоимость аренды помещения: ")
lblArenda1.grid(column=a1, row=1)
txtArenda = Entry(window, width=10)
txtArenda.grid(column=a2, row=1)
lblArenda2 = Label(window, text="руб./месяц")
lblArenda2.grid(column=a3, row=1)

lblTechnic1 = Label(window, text="Укажите траты на оборудование: ")
lblTechnic1.grid(column=a1, row=2)
txtTechnic = Entry(window, width=10)
txtTechnic.grid(column=a2, row=2)
lblTechnic2 = Label(window, text="руб.")
lblTechnic2.grid(column=a3, row=2)

lblResurs1 = Label(window, text="Укажите траты на расходники: ")
lblResurs1.grid(column=a1, row=3)
txtResurs = Entry(window, width=10)
txtResurs.grid(column=a2, row=3)
lblResurs2 = Label(window, text="руб.")
lblResurs2.grid(column=a3, row=3)

lblWorker1 = Label(window, text="Укажите количество сотрудников: ")
lblWorker1.grid(column=a1, row=4)
txtWorker = Entry(window, width=10)
txtWorker.grid(column=a2, row=4)
lblWorker2 = Label(window, text="чел.")
lblWorker2.grid(column=a3, row=4)

btn1 = Button(window, text="Ввести данные", command=clicked1)
btn1.grid(column=5, row=5)
#root.mainloop()
window.mainloop()
