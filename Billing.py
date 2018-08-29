#-----------------------------------Packages-------------------------------------------------

from tkinter import *
import random
import time
import datetime

#-----------------------------------Frames-------------------------------------------------


root = Tk()
root.geometry("1350x650+0+0")
root.title("Billing Systems")

Top = Frame(root, width=1350, height = 100, bd= 8, relief="raise")
Top.pack(side=TOP)



F1 = Frame(root, width=880, height = 650, bd= 8, relief="raise")
F1.pack(side=LEFT)
F2 = Frame(root, width=440, height = 650, bd= 8, relief="raise")
F2.pack(side=RIGHT)

F1a = Frame(F1, width=880, height = 330, bd= 8, relief="raise")
F1a.pack(side=TOP)
F1b = Frame(F1, width=880, height = 320, bd= 8, relief="raise")
F1b.pack(side=BOTTOM)

F1a1 = Frame(F1a, width=400, height = 430, bd= 8, relief="raise")
F1a1.pack(side=LEFT)
F1a2 = Frame(F1a, width=400, height = 430, bd= 8, relief="raise")
F1a2.pack(side=BOTTOM)

F1b1 = Frame(F1b, width=400, height = 300, bd= 8, relief="raise")
F1b1.pack(side=LEFT)
F1b2 = Frame(F1b, width=400, height = 300, bd= 8, relief="raise")
F1b2.pack(side=RIGHT)

labelTop = Label(Top, width=1330,bd = 10, font=("Times", 48,"bold"), text="ALFERDIZE Billing", relief="raise")
labelTop.pack()

#-----------------------------------Variables-------------------------------------------------

equa = ""
PaymentRef = StringVar()
Carpets = StringVar()
Fabric = StringVar()
Blinds = StringVar()
DateofOrder = StringVar()
HomeDelivery = StringVar()
CostofCarpets = StringVar()
CostofFabric = StringVar()
CostofBlinds = StringVar()
CostofHomeDelivery = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
equation = StringVar()

#-----------------------------------Function-------------------------------------------------


def iExit():
    Exit = messageboxaskyesno("Billing System","Do you want to exit the system")
    if Exit > 0:
        root.destroy()
        return

    
def Reset():
    PaymentRef.set("")
    Carpets.set("")
    Fabric.set("")
    Blinds.set("")
    HomeDelivery.set("")
    DateofOrder.set("")
    CostofCarpets.set("")
    CostofFabric.set("")
    CostofBlinds.set("")
    CostofHomeDelivery.set("")
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")

    

def btnPress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)

def ans():
    global equa
    equation.set(eval(equa))
    equa = str(eval(equa))

def clear():
    global equa
    equation.set("0")
    equa = ""
    




#-----------------------------------Calculator-------------------------------------------------

calculation = Entry(F2,font=('arial', 20, 'bold'),
                    textvariable = equation,insertwidth=420,justify='right',bd = 10)

equation.set("0")
calculation.grid(columnspan = 3)
buttonclear = Button(F2, text="Clear",font=('arial', 20, 'bold'),
                     bd = 10,relief = 'raise', command=clear,height=2,width=4)
button1 = Button(F2, text="1",font=('arial', 20, 'bold'),
                 bd = 10,relief = 'raise', command=lambda:btnPress(1),height=2,width=4)
button2 = Button(F2, text="2",font=('arial', 20, 'bold'),
                 bd = 10,relief = 'raise', command=lambda:btnPress(2),height=2,width=4)
button3 = Button(F2, text="3",font=('arial', 20, 'bold'),
                 bd = 10,relief = 'raise', command=lambda:btnPress(3),height=2,width=4)
button4 = Button(F2, text="4",font=('arial', 20, 'bold'),
                 bd = 10,relief = 'raise', command=lambda:btnPress(4),height=2,width=4)
button5 = Button(F2, text="5",font=('arial', 20, 'bold'),
                 bd = 10,relief = 'raise', command=lambda:btnPress(5),height=2,width=4)
button6 = Button(F2, text="6",font=('arial', 20, 'bold'),
                 bd = 10,relief = 'raise', command=lambda:btnPress(6),height=2,width=4)
button7 = Button(F2, text="7",font=('arial', 20, 'bold'),
                 bd = 10,relief = 'raise', command=lambda:btnPress(7),height=2,width=4)
button8 = Button(F2, text="8",font=('arial', 20, 'bold'),
                 bd = 10,relief = 'raise', command=lambda:btnPress(8),height=2,width=4)
button9 = Button(F2, text="9",font=('arial', 20, 'bold'),
                 bd = 10,relief = 'raise', command=lambda:btnPress(9),height=2,width=4)
button0 = Button(F2, text="0",font=('arial', 20, 'bold'),
                 bd = 10,relief = 'raise', command=lambda:btnPress(0),height=2,width=4)
button_eq = Button(F2, text="=",height=2,width=4,command=ans,bd = 10,relief = 'raise',font=('arial', 20, 'bold'))
button_plus = Button(F2, text="+",height=2,width=4,
                     font=('arial', 20, 'bold'),bd = 10,relief = 'raise',
                     command=lambda:btnPress("+"))
button_sub = Button(F2, text="-",height=2,width=4,
                    font=('arial', 20, 'bold'),bd = 10,relief = 'raise',
                    command=lambda:btnPress("-"))
button_mul = Button(F2, text="*",height=2,width=4,
                    font=('arial', 20, 'bold'),bd = 10,relief = 'raise',
                    command=lambda:btnPress("*"))
button_div = Button(F2, text="/",height=2,width=4,
                    font=('arial', 20, 'bold'),bd = 10,relief = 'raise',
                    command=lambda:btnPress("/"))
button_dot = Button(F2, text=".",height=2,width=4,
                    font=('arial', 20, 'bold'),bd = 10,relief = 'raise',
                    command=lambda:btnPress("."))

buttonclear.grid(row = 0, column = 3)
button7.grid(row = 1,column = 0)
button8.grid(row = 1,column = 1)
button9.grid(row = 1,column = 2)
button_plus.grid(row = 1,column = 3)
button4.grid(row = 2,column = 0)
button5.grid(row = 2,column = 1)
button6.grid(row = 2,column = 2)
button_sub.grid(row = 2,column = 3)
button1.grid(row = 3,column = 0)
button2.grid(row = 3,column = 1)
button3.grid(row = 3,column = 2)
button_mul.grid(row = 3,column = 3)
button_dot.grid(row = 4,column = 0)
button0.grid(row = 4,column = 1)
button_eq.grid(row = 4,column = 2)
button_div.grid(row = 4,column = 3)

#-----------------------------------Order Information F1a1-------------------------------------------------

labelRef = Label(F1a1,font=('arial', 20, 'bold'),
                    text = 'Sales Referencs',bd = 16,justify='right',width=12)
labelRef.grid(row=0,column=0)
textRef = Entry(F1a1,font=('arial', 20, 'bold'),
                    textvariable = PaymentRef,bd = 10,justify='left',width=12)
textRef.grid(row=0,column=1)
lblCarpet = Label(F1a1,font=('arial', 20, 'bold'),
                    text = 'Carpets',bd = 16,justify='right',width=12)
lblCarpet.grid(row=1,column=0)
textCarpet = Entry(F1a1,font=('arial', 20, 'bold'),
                    textvariable = Carpets,bd = 10,justify='left',width=12)
textCarpet.grid(row=1,column=1)

labelFabric = Label(F1a1,font=('arial', 20, 'bold'),
                    text = 'Fabric',bd = 16,justify='right',width=12)
labelFabric.grid(row=2,column=0)
textFabric = Entry(F1a1,font=('arial', 20, 'bold'),
                    textvariable = Fabric,bd = 10,justify='left',width=12)
textFabric.grid(row=2,column=1)
labelBlinds = Label(F1a1,font=('arial', 20, 'bold'),
                    text = 'Blinds',bd = 16,justify='right',width=12)
labelBlinds.grid(row=3,column=0)
textBlinds = Entry(F1a1,font=('arial', 20, 'bold'),
                    textvariable = Blinds,bd = 10,justify='left',width=12)
textBlinds.grid(row=3,column=1)
labelHomeDelivery = Label(F1a1,font=('arial', 20, 'bold'),
                    text = 'Home Delivery',bd = 16,justify='right',width=12)
labelHomeDelivery.grid(row=4,column=0)
textHomeDelivery = Entry(F1a1,font=('arial', 20, 'bold'),
                    textvariable = HomeDelivery,bd = 10,justify='left',width=12)
textHomeDelivery.grid(row=4,column=1)

#-----------------------------------Order Information F1a2-------------------------------------------------


labelDateofOrder = Label(F1a2,font=('arial', 20, 'bold'),
                    text = 'Date of Order',bd = 16,justify='right',width=17)
labelDateofOrder.grid(row=0,column=0)
textDateofOrder = Entry(F1a2,font=('arial', 20, 'bold'),
                    textvariable = DateofOrder,bd = 10,justify='left',width=17)
textDateofOrder.grid(row=0,column=1)
lblCostofCarpet = Label(F1a2,font=('arial', 20, 'bold'),
                    text = 'Cost of Carpets',bd = 16,justify='right',width=17)
lblCostofCarpet.grid(row=1,column=0)
textCostofCarpet = Entry(F1a2,font=('arial', 20, 'bold'),
                    textvariable = CostofCarpets,bd = 10,justify='left',width=17)
textCostofCarpet.grid(row=1,column=1)

labelCostofFabric = Label(F1a2,font=('arial', 20, 'bold'),
                    text = 'Cost of Fabric',bd = 16,justify='right',width=17)
labelCostofFabric.grid(row=2,column=0)
textCostofFabric = Entry(F1a2,font=('arial', 20, 'bold'),
                    textvariable = CostofFabric,bd = 10,justify='left',width=17)
textCostofFabric.grid(row=2,column=1)
labelCostofBlinds = Label(F1a2,font=('arial', 20, 'bold'),
                    text = 'Cost of Blinds',bd = 16,justify='right',width=17)
labelCostofBlinds.grid(row=3,column=0)
textCostofBlinds = Entry(F1a2,font=('arial', 20, 'bold'),
                    textvariable = CostofBlinds,bd = 10,justify='left',width=17)
textCostofBlinds.grid(row=3,column=1)
labelCostofHomeDelivery = Label(F1a2,font=('arial', 20, 'bold'),
                    text = 'Cost of Home Delivery',bd = 16,justify='right',width=17)
labelCostofHomeDelivery.grid(row=4,column=0)
textCostofHomeDelivery = Entry(F1a2,font=('arial', 20, 'bold'),
                    textvariable = CostofHomeDelivery,bd = 10,justify='left',width=17)
textCostofHomeDelivery.grid(row=4,column=1)

#-----------------------------------Order Information F1b1-------------------------------------------------
labelPaidTax = Label(F1b1,font=('arial', 20, 'bold'),
                    text = 'Paid Tax',bd = 16,justify='right',width=12)
labelPaidTax.grid(row=0,column=0)
textPaidTax = Entry(F1b1,font=('arial', 20, 'bold'),
                    textvariable = PaidTax,bd = 10,justify='left',width=12)
textPaidTax.grid(row=0,column=1)
lblSubTotal = Label(F1b1,font=('arial', 20, 'bold'),
                    text = 'Sub Total',bd = 16,justify='right',width=12)
lblSubTotal.grid(row=1,column=0)
textSubTotal = Entry(F1b1,font=('arial', 20, 'bold'),
                    textvariable = SubTotal,bd = 10,justify='left',width=12)
textSubTotal.grid(row=1,column=1)

labelTotalCost = Label(F1b1,font=('arial', 20, 'bold'),
                    text = 'Total Cost',bd = 16,justify='right',width=12)
labelTotalCost.grid(row=2,column=0)
textTotalCost = Entry(F1b1,font=('arial', 20, 'bold'),
                    textvariable = TotalCost,bd = 10,justify='left',width=12)
textTotalCost.grid(row=2,column=1)

#-----------------------------------Order Information F1b2-------------------------------------------------


btnTotal= Button(F1b2, text="Total Cost",font=('arial', 20, 'bold'),
                 bd = 10,relief = 'raise',width=12,command=ans)
btnTotal.grid(row=0,column=0)
btnRefer= Button(F1b2, text="Sales Reference",font=('arial', 20, 'bold'),
                 bd = 10,relief = 'raise',width=12,command=ans)
btnRefer.grid(row=0,column=1)
btnReset= Button(F1b2, text="Reset",font=('arial', 20, 'bold'),
                 bd = 10,relief = 'raise',width=12,command=Reset)
btnReset.grid(row=1,column=0)
btnExit= Button(F1b2, text="Exit",font=('arial', 20, 'bold'),
                 bd = 10,relief = 'raise',width=12,command=iExit)
btnExit.grid(row=1,column=1)

#--------------------------------------------------------------------------------------------------------------------

root.mainloop()
