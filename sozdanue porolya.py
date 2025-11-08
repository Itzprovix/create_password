from tkinter import*
import random



window = Tk()
window.geometry("400x400")
window.title("Генератор паролей")

lowercase = BooleanVar()
lowercase2 = BooleanVar()
lowercase3 = BooleanVar()
lowercase4 = BooleanVar()

frame1 = LabelFrame(text="Символы", width=300, height=300)

frame1.pack(expand=True)

check_lowercase = Checkbutton(frame1, text="abcdefghijklmnopqrstuvwxyz", width=40, command=Text, variable=lowercase, onvalue=True, offvalue=False)
check_numbers = Checkbutton(frame1, text="0123456789", width=20, command=Text, variable=lowercase2, onvalue=True, offvalue=False)
check_uppercase = Checkbutton(frame1, text="ABCDEFGHIJKLMNOPQRSTUVWXYZ", width=43, command=Text, variable=lowercase3, onvalue=True, offvalue=False)
check_symbols = Checkbutton(frame1, text="!@#$%^&*()", width= 20, command=Text, variable=lowercase4, onvalue=True, offvalue=False)
porol = Entry(frame1, width=30)
alarmbox = Listbox(width=30, height=10, justify=CENTER)

def generate():
    check_lowercase = lowercase.get()
    check_numbers = lowercase2.get()
    check_uppercase = lowercase3.get()
    check_symbols = lowercase4.get()
    pwd = generate_password(check_lowercase, check_numbers, check_uppercase, check_symbols)
    porol.delete(0, END)
    porol.insert(0, pwd)
    alarmbox.insert(END, generate_password(check_lowercase, check_numbers, check_uppercase, check_symbols))
    alarmbox.insert(END, generate_password(check_lowercase, check_numbers, check_uppercase, check_symbols))
    alarmbox.insert(END, generate_password(check_lowercase, check_numbers, check_uppercase, check_symbols))
    alarmbox.insert(END, generate_password(check_lowercase, check_numbers, check_uppercase, check_symbols))
    alarmbox.insert(END, generate_password(check_lowercase, check_numbers, check_uppercase, check_symbols))
knopka = Button(frame1, width=20, text="Сгенерировать пароль", command=generate)

def generate_password(lowercase, numbers, uppercase, symbols):
    password = ''
    for i in range(10):
        if lowercase == True:
            password += random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

        if numbers == True:
            password += str(random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

        if uppercase == True:
            password += str(random.choice(["A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))

        if symbols == True:
            password += str(random.choice(["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]))
    return password





check_lowercase.pack()
check_numbers.pack()
check_uppercase.pack()
check_symbols.pack()
alarmbox.pack()
porol.pack()
knopka.pack()


window.mainloop()
