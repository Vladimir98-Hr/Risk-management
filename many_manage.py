from tkinter import *

import tkinter.messagebox as box


window = Tk()
window.title('Entry Example')


frame = Frame(window)
entry = Entry(window)
entry2 = Entry(window)
entry3 = Entry(window)
entry4 = Entry(window)

book = StringVar()
book2 = StringVar()

def dialog():
    capital = float(entry.get())

    if capital < 2500:
        capital_prosent = float(5/100)
        capital_prosent2 = 5
    elif 2500 < capital < 25000:
        capital_prosent = float(2/100)
        capital_prosent2 = 2
    elif capital > 25000:
        capital_prosent = float(1/100)
        capital_prosent2 = 1

    manera_torgovli = float(book.get())
    catigori_cdelci= float(book2.get())
    sum_vhoda = f'{float(entry2.get())}'

    sum_next = f'{float(entry3.get())}'
    #box.showinfo('Сумма', float(manera_torgovli)  + float(catigori_cdelci))
    riscki = float(manera_torgovli) * float(capital_prosent2) * float(catigori_cdelci)
    dollar_riski = f'{capital * (riscki/100)}'
    # dollar_riski = float(riscki)
    poteri_s_coin = float(sum_next) - float(sum_vhoda)
    total = '%.20f' % poteri_s_coin
    session = float(riscki * 3)

    labels1.configure(text=f'Риск на сделку: {riscki}')
    labels2.configure(text=f'Риск в долларах: {dollar_riski}')
    labels3.configure(text=f'Потеря с монеты: {total}')
    labels4.configure(text=f'Обём сделки: {float(dollar_riski)/float(poteri_s_coin)}')
    labels5.configure(text=f'Процент риска на сессию: {session}')
    labels6.configure(text=f'Лимит потерь: {capital * (float(session)/100)}')

label1 = Label(window, text=" Введите ваш капитал:")
label2 = Label(window, text=" Сумма входа в сделку:")
label3 = Label(window, text=" Сумма выхода из сделки:")
label4 = Label(window, text=" Определите вашу манеру торговли и категорию сделки:")


radio_1 = Radiobutton(frame, text='Консервативный инвестор', variable=book, value='0.5')
radio_2 = Radiobutton(frame, text='Сбалансированный инвестор', variable=book, value='1')
radio_3 = Radiobutton(frame, text='Агрессивный инвестор', variable=book, value='2')
radio_4 = Radiobutton(frame, text='Кратко-срокосрочная ', variable=book2, value='0.3')
radio_5 = Radiobutton(frame, text='Средне-срокосрочная', variable=book2, value='1')
radio_6 = Radiobutton(frame, text='Долго-срокосрочная', variable=book2, value='1.5')

radio_1.select()
radio_4.select()

bth = Button(frame, text='test', command=dialog)
#bth2 = Button(frame, text='test', command=dialog)

label1.pack(padx=100,pady=5)
entry.pack(padx=100,pady=5)
label2.pack(padx=100,pady=5)
entry2.pack(padx=100,pady=5)
label3.pack(padx=100,pady=5)
entry3.pack(padx=100,pady=5)
label4.pack(padx=100,pady=5)

frame.pack()
radio_1.grid(row=1, column=1,pady=5)
radio_2.grid(row=1, column=2,pady=5)
radio_3.grid(row=1, column=3,pady=5)
radio_4.grid(row=2, column=1,pady=5)
radio_5.grid(row=2, column=2,pady=5)
radio_6.grid(row=2, column=3,pady=5)


labels1 = Label(window, relief='groove', width=50)
labels2 = Label(window, relief='groove', width=50)
labels3 = Label(window, relief='groove', width=50)
labels4 = Label(window, relief='groove', width=50)
labels5 = Label(window, relief='groove', width=50)
labels6 = Label(window, relief='groove', width=50)


labels1.pack(padx=200,pady=5)
labels2.pack(padx=210,pady=5)
labels3.pack(padx=220,pady=5)
labels4.pack(padx=230,pady=5)
labels5.pack(padx=240,pady=5)
labels6.pack(padx=250,pady=5)

bth.grid(row=3, column=2,pady=5)



# window = Tk()
#
# frame = Frame(window)
# entry = Entry(frame)
#
#
# entry.grid(p)
#
#
# label1 = Label(window, relief='groove', width=2)
# label2 = Label(window, relief='groove', width=2)
# label3 = Label(window, relief='groove', width=2)
# label4 = Label(window, relief='groove', width=2)
#
# label1.grid(row=1, column=1,pady=5)
# label2.grid(row=2, column=1,pady=5)
# label3.grid(row=3, column=1,pady=5)
# label4.grid(row=4, column=1,pady=5)



window.mainloop()