from tkinter import *
import math

def leftClickButton(event):
    result = float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2)
    labelResult.configure(text="Your BMI is  %.1F"%result)
    if result >= 30:
        resultExplain.configure(text="อ้วนมาก")
    elif 25 <= result <= 29.9:
        resultExplain.configure(text="อ้วน")
    elif 23 <= result <= 24.9:
        resultExplain.configure(text="น้ำหนักเกิน")
    elif 18.6 <= result <= 22.9:
        resultExplain.configure(text="น้ำหนักปกติ เหมาะสม")
    elif result <= 18.5:
        resultExplain.configure(text="ผอมเกินไป")

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.grid(row=2)
calculateButton.bind('<Button-1>', leftClickButton)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)
resultExplain = Label(MainWindow)
resultExplain.grid(row=3, column=1)

MainWindow.mainloop()