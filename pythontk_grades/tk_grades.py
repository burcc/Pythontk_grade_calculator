import tkinter as tk

def hesapla():

    if vize.get().isdigit() and final.get().isdigit:
        s1= float(vize.get())
        s2 = float(final.get())
        hesap = round((s1 * 0.4 + s2 * 0.6), 2)
        result.configure(text=str(hesap))

        if int(((hesap) >= 80)):
            #print(f"Not harfi 'A'. Geçtiniz.")
            bilgi = tk.Label(screen, text = (f"Not harfi 'A'. Geçtiniz.\n Not ortalaması : {hesap}"), font = "Courier 16 bold", width = 50, justify= "center")
            bilgi.place(x=0,y=80)
        
        elif int((hesap) <= 79 and (hesap) >=70):
            bilgi = tk.Label(screen, text = (f"Not harfi 'B'. Geçtiniz. \n Not ortalaması : {hesap}"), font = "Courier 16 bold", width = 50, justify= "center")
            bilgi.place(x=0,y=80)
        
        elif int((hesap) <= 69 and (hesap) >=60):
            bilgi = tk.Label(screen, text = (f"Not harfi 'C'. Geçtiniz. \n Not ortalaması : {hesap}"), font = "Courier 16 bold", width = 50, justify= "center")
            bilgi.place(x=0,y=80)
        
        elif int ((hesap) <= 59 and (hesap) >=50):
            bilgi = tk.Label(screen, text = (f"Not harfi 'D'. Geçtiniz. \n Not ortalaması : {hesap}"), font = "Courier 16 bold", width = 50, justify= "center")
            bilgi.place(x=0,y=80)
        
        elif int((hesap) <= 49):
            bilgi = tk.Label(screen, text = (f"Not harfi 'F'. Kaldınız. \n Not ortalaması : {hesap}"), font = "Courier 16 bold", width = 50, justify= "center")
            bilgi.place(x=0,y=80)
    

screen = tk.Tk()
screen.title("Calculation of Student Grades")
screen.geometry("600x600")
screen.config(bg = "black")

result = tk.Label(screen, text="Vize ve Final Notunu Girin: ", font= "Courier 16 bold", width= 30, justify = "center")
result.place(x=120,y=80)

vize = tk.Entry(screen, font = "Courier 16 bold", width = 30, justify = "center")
vize.place(x= 120, y = 160)

final = tk.Entry(screen, font = "Courier 16 bold", width = 30, justify = "center")
final.place(x= 120, y = 200)

tus1 = tk.Button(screen, text = "Hesapla", font = "Courier 14 bold", width= 10,command = hesapla)

tus1.place(x=250, y=300)

vize.focus()

screen.mainloop()