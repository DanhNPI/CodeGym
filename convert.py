from tkinter import *

def Convert():
    '''Convert Kg to gram, pounds and ounce'''
    kg = float(a.get())
    gram = kg * 1000
    pounds = kg * 2.20462
    ounce = kg * 35.274

    result_gram['text'] = str(gram)
    result_pound['text'] = str(pounds)
    result_ounce['text'] = str(ounce)

root = Tk()

a = StringVar()
root.title("Convert")

lbl1 = Label(root, text="Enter the weight in Kg", font=('Calibri', 12, 'bold'))
lbl1.grid(column=0, row=0, padx=20, pady=20, sticky="w")

entry_lbl = Entry(root, width=50, borderwidth=3, highlightthickness=3, textvariable=a, font=('Calibri', 12, 'bold'), justify='left')
entry_lbl.grid(column=1, row=0, padx=20, sticky="w")

btn_convert = Button(root, text="Convert", relief=RAISED, bg='grey', font=('Calibri', 12, 'bold'), command=Convert)
btn_convert.grid(column=2, row=0, padx=10)

lbl_gram = Label(root, text="Gram", font=('Calibri', 12, 'bold'))
lbl_gram.grid(column=0, row=1, padx=20, pady=20, sticky="n")

lbl_pounds = Label(root, text="Pounds", font=('Calibri', 12, 'bold'))
lbl_pounds.grid(column=1, row=1, padx=20, pady=20, sticky="n")

lbl_ounce = Label(root, text="Ounce", font=('Calibri', 12, 'bold'))
lbl_ounce.grid(column=2, row=1, padx=20, pady=20, sticky="n")

result_gram = Label(root, text="", font=('Calibri', 12, 'bold'))
result_gram.grid(column=0, row=2, padx=20, sticky='n')

result_pound = Label(root, text="", font=('Calibri', 12, 'bold'))
result_pound.grid(column=1, row=2, padx=20, sticky='n')

result_ounce = Label(root, text="", font=('Calibri', 12, 'bold'))
result_ounce.grid(column=2, row=2, padx=20, sticky='n')

root.mainloop()