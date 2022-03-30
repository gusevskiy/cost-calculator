from tkinter import *

window = Tk()

window.title('Калькулятор плотности и цены')
window.geometry('270x170+100+100')

#заголовки колонок
lbl = Label(window, text = 'обьем')
lbl.grid(column = 2, row = 0)
lbl = Label(window, text = 'плотность')
lbl.grid(column = 3, row = 0)
lbl = Label(window, text = 'стоимость')
lbl.grid(column = 4, row = 0)
lbl = Label(window, text = 'общ. обьем')
lbl.grid(column = 2, row = 6)
lbl = Label(window, text = 'общ. плотность')
lbl.grid(column = 3, row = 6)
lbl = Label(window, text = 'общ. стоимость')
lbl.grid(column = 4, row = 6)

#номера рядов
lbl = Label(window, text = '1')
lbl.grid(column = 1, row = 1)
lbl = Label(window, text = '2')
lbl.grid(column = 1, row = 2)
lbl = Label(window, text = '3')
lbl.grid(column = 1, row = 3)
lbl = Label(window, text = '4')
lbl.grid(column = 1, row = 4)

#окна ввода обьема
volume1 = Entry(window, width = 10)
volume1.grid(column = 2, row = 1)
volume1.insert(0, '0')
volume2 = Entry(window, width = 10)
volume2.grid(column = 2, row = 2)
volume2.insert(0, '0')
volume3 = Entry(window, width = 10)
volume3.grid(column = 2, row = 3)
volume3.insert(0, '0')
volume4 = Entry(window, width = 10)
volume4.grid(column = 2, row = 4)
volume4.insert(0, '0')

# общ. обьем
def v():
    v1 = int(volume1.get())
    v2 = int(volume2.get())
    v3 = int(volume3.get())
    v4 = int(volume4.get())
    sum = v1 + v2 + v3 + v4
    vv.config(text = (sum))

vv = Label(window, text = 0, font = ('Arial' ,9, 'bold'))
vv.grid(column = 2, row = 7)

#окна ввода плотности
density1 = Entry(window, width = 10)
density1.grid(column = 3, row = 1)
density1.insert(0, '0')
density2 = Entry(window, width = 10)
density2.grid(column = 3, row = 2)
density2.insert(0, '0')
density3 = Entry(window, width = 10)
density3.grid(column = 3, row = 3)
density3.insert(0, '0')
density4 = Entry(window, width = 10)
density4.grid(column = 3, row = 4)
density4.insert(0, '0')

#общ. плотность
def d():
    v1 = int(volume1.get())
    v2 = int(volume2.get())
    v3 = int(volume3.get())
    v4 = int(volume4.get())
    d1 = float(density1.get())
    d2 = float(density2.get())
    d3 = float(density3.get())
    d4 = float(density4.get())
    d0 = round((v1 * d1 + v2 * d2 + v3 * d3 + v4 * d4) / (v1 + v2 + v3 + v4), 3)
    dd.config(text = (d0))

dd = Label(window, text = 0, font = ('Arial' ,9, 'bold'))
dd.grid(column = 3, row = 7)

#окна ввода стоимости
cost1 = Entry(window, width = 10)
cost1.grid(column = 4, row = 1)
cost1.insert(0, '0')
cost2 = Entry(window, width = 10)
cost2.grid(column = 4, row = 2)
cost2.insert(0, '0')
cost3 = Entry(window, width = 10)
cost3.grid(column = 4, row = 3)
cost3.insert(0, '0')
cost4 = Entry(window, width = 10)
cost4.grid(column = 4, row = 4)
cost4.insert(0, '0')

#общ стоимость
def c():
    v1 = int(volume1.get())
    v2 = int(volume2.get())
    v3 = int(volume3.get())
    v4 = int(volume4.get())
    c1 = float(cost1.get())
    c2 = float(cost2.get())
    c3 = float(cost3.get())
    c4 = float(cost4.get())
    c0 = round((v1 * c1 + v2 * c2 + v3 * c3 + v4 * c4) / (v1 + v2 + v3 + v4), 2)
    cc.config(text = (c0))

cc = Label(window, text = 0, font = ('Arial' ,9, 'bold'))
cc.grid(column = 4, row = 7)

#кнопка вычислить
button = Button(text='вычислить', command = lambda:[v(), c(), d()])
button.grid(column = 4, row = 8)

# кнопка очистить
def delet():
    volume1.delete(0, END)
    volume1.insert(0, '0')
    volume2.delete(0, END)
    volume2.insert(0, '0')
    volume3.delete(0, END)
    volume3.insert(0, '0')
    volume4.delete(0, END)
    volume4.insert(0, '0')
    density1.delete(0, END)
    density1.insert(0, '0')
    density2.delete(0, END)
    density2.insert(0, '0')
    density3.delete(0, END)
    density3.insert(0, '0')
    density4.delete(0, END)
    density4.insert(0, '0')
    cost1.delete(0, END)
    cost1.insert(0, '0')
    cost2.delete(0, END)
    cost2.insert(0, '0')
    cost3.delete(0, END)
    cost3.insert(0, '0')
    cost4.delete(0, END)
    cost4.insert(0, '0')
    vv.config(text = 0)
    cc.config(text = 0)
    dd.config(text = 0)


button = Button(text='очистить', command = lambda: [delet()])
button.grid(column = 2, row = 8)


window.mainloop()
