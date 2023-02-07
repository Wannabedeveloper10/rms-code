from tkinter import *

root = Tk()
root.geometry('1300x690+0+0')

#root.resizable(0,0)


root.title('Restaurant management system')
root.configure(bg='light blue')

topFrame = Frame(root, bd=10, relief=RIDGE, bg='light blue')
topFrame.pack(side=TOP)

labelTitle = Label(topFrame, text='Restaraunt management system', font=('arial', 30, 'bold'), width=53, bd=11, bg='light blue')
labelTitle.grid(row=0, column=0)

#frames

menuFrame = LabelFrame(root, text='Menu', font=('arial', 15, 'bold'), bd=15, relief=RIDGE, bg='lightblue')
menuFrame.pack(side=LEFT)

costFrame = Frame(menuFrame, bd=10, relief=RIDGE, bg='lightblue')
costFrame.pack(side=BOTTOM)

drinksFrame = LabelFrame(menuFrame, text='Drink', font=('arial', 15, 'bold'), bd=10, relief=RIDGE, bg='lightblue')
drinksFrame.pack(side=LEFT)

saladFrame = LabelFrame(menuFrame,text='Salad', font=('arial',15,'bold'),bd=10,relief=RIDGE,bg='lightblue')
saladFrame.pack(side=LEFT)

StartersFrame = LabelFrame(menuFrame, text='Starters', font=('arial', 15, 'bold'), bd=10, relief=RIDGE,  bg='lightblue')
StartersFrame.pack(side=LEFT)

main_courseFrame = LabelFrame(menuFrame, text='Main Course', font=('arial', 15, 'bold'), bd=10, relief=RIDGE, bg='lightblue')
main_courseFrame.pack(side=LEFT)

desertFrame = LabelFrame(menuFrame, text='Desert', font=('arial', 15, 'bold'), bd=10, relief=RIDGE, bg='lightblue')
desertFrame.pack(side=LEFT)

rightFrame = Frame(root, bd=15, relief=RIDGE)
rightFrame.pack(side=RIGHT)

calculatorFrame = Frame(rightFrame, bd=10, relief=RIDGE)
calculatorFrame.pack()

receiptFrame = Frame(rightFrame, bd=10, relief=RIDGE)
receiptFrame.pack()

buttonFrame = Frame(rightFrame, bd=10, relief=RIDGE)
buttonFrame.pack()

#varialbles
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()

e_Tomato_soup = StringVar()
e_Chicken_soup = StringVar()
e_Crispy_soup = StringVar()
e_guacamole_salad = StringVar()
e_chicken_salad = StringVar()
e_grilled_fish_and_potatoes = StringVar()
e_chicken_and_rice = StringVar()
e_shepards_pie = StringVar()
e_cheese_pasta = StringVar()
e_chocolate_icecream = StringVar()
e_doughnuts = StringVar()
e_Tiramisu = StringVar()
e_cheese_cake = StringVar()
e_kulfi = StringVar()
e_mineral_water = StringVar()
e_tea = StringVar()
e_fruit_juice = StringVar()
e_coffee = StringVar()
e_Wines = StringVar()

CostofStartersvar=StringVar()
Costofmaincoursevar=StringVar()
Costofdesertsvar=StringVar()
Costofdrinksvar=StringVar()
costofStartersvar=StringVar()
Subtotalvar=StringVar()
ServiceTaxvar=StringVar()
Totalvar=StringVar()

e_Tomato_soup.set('0')
e_Chicken_soup.set('0')
e_Crispy_soup.set('0')
e_guacamole_salad.set('0')
e_chicken_salad.set('0')
e_grilled_fish_and_potatoes.set('0')
e_chicken_and_rice.set('0')
e_shepards_pie.set('0')
e_cheese_pasta.set('0')
e_chocolate_icecream.set('0')
e_doughnuts.set('0')
e_Tiramisu.set('0')
e_cheese_cake.set('0')
e_kulfi.set('0')
e_mineral_water.set('0')
e_tea.set('0')
e_fruit_juice.set('0')
e_coffee.set('0')
e_Wines.set('0')

#food

Tomato_soup=Checkbutton(StartersFrame, text='Tomato soup', font=('arial', 10, 'bold'), onvalue=1, offvalue=0, variable=var1, bg='lightblue')
Tomato_soup.grid(row=0, column=0, sticky=W)

Chicken_soup=Checkbutton(StartersFrame, text='Chicken soup', font=('arial', 10, 'bold'), onvalue=1, offvalue=0, variable=var2, bg='lightblue')
Chicken_soup.grid(row=1, column=0, sticky=W)

Crispy_corn=Checkbutton(StartersFrame, text='Crispy corn', font=('arial', 10, 'bold'), onvalue=1, offvalue=0, variable=var3, bg='lightblue')
Crispy_corn.grid(row=2, column=0, sticky=W)

guacamole_salad=Checkbutton(StartersFrame,text='Guacamole salad',font=('arial',10,'bold'),onvalue=1,offvalue=0,variable=var4,bg='lightblue')
guacamole_salad.grid(row=3, column=0, sticky=W)

chicken_salad=Checkbutton(StartersFrame,text='Chicken salad',font=('arial',10,'bold'),onvalue=1,offvalue=0,variable=var5,bg='lightblue')
chicken_salad.grid(row=4, column=0, sticky=W)

grilled_fish_and_potatoes=Checkbutton(main_courseFrame,text='Grilled fish and potatoes',font=('arial',10,'bold'),onvalue=1,offvalue=0,variable=var6,bg='lightblue')
grilled_fish_and_potatoes.grid(row=0, column=0, sticky=W)

chicken_and_rice=Checkbutton(main_courseFrame,text='Chicken and Rice',font=('arial',10,'bold'),onvalue=1,offvalue=0,variable=var7,bg='lightblue')
chicken_and_rice.grid(row=1, column=0, sticky=W)

shepards_pie=Checkbutton(main_courseFrame,text='Shepards pie',font=('arial',10,'bold'),onvalue=1,offvalue=0,variable=var8,bg='lightblue')
shepards_pie.grid(row=2, column=0, sticky=W)

cheese_pasta=Checkbutton(main_courseFrame,text='Cheese pasta',font=('arial',10,'bold'),onvalue=1,offvalue=0,variable=var9,bg='lightblue')
cheese_pasta.grid(row=3, column=0, sticky=W)

chocolate_icecream=Checkbutton(desertFrame,text='Chocolate ice cream',font=('arial',10,'bold'),onvalue=1,offvalue=0,variable=var10,bg='lightblue')
chocolate_icecream.grid(row=0, column=0, sticky=W)

doughnuts=Checkbutton(desertFrame,text='Doughnuts',font=('arial',10,'bold'),onvalue=1,offvalue=0,variable=var11,bg='lightblue')
doughnuts.grid(row=1,column=0,sticky=W)

Tiramisu=Checkbutton(desertFrame,text='Tiramisu',font=('arial',10,'bold'),onvalue=1,offvalue=0,variable=var12,bg='lightblue')
Tiramisu.grid(row=2,column=0,sticky=W)

cheese_cake=Checkbutton(desertFrame,text='Cheese cake',font=('arial',10,'bold'),onvalue=1,offvalue=0,variable=var13,bg='lightblue')
cheese_cake.grid(row=3,column=0,sticky=W)

kulfi=Checkbutton(desertFrame,text='Kulfi',font=('arial',10,'bold'),onvalue=1,offvalue=0,variable=var14,bg='lightblue')
kulfi.grid(row=4,column=0,sticky=W)

mineral_water=Checkbutton(drinksFrame,text='Mineral water',font=('arial',10,'bold'),onvalue=1,offvalue=0,variable=var15,bg='lightblue')
mineral_water.grid(row=0,column=0,sticky=W)

tea=Checkbutton(drinksFrame,text='Chai',font=('arial',10,'bold'),onvalue=1,offvalue=0,variable=var16,bg='lightblue')
tea.grid(row=1,column=0,sticky=W)

fruit_juice=Checkbutton(drinksFrame,text='Fruit Juice',font=('arial',10,'bold'),onvalue=1,offvalue=0,variable=var17,bg='lightblue')
fruit_juice.grid(row=2,column=0,sticky=W)

coffee=Checkbutton(drinksFrame,text='Coffee',font=('arial',10,'bold'),onvalue=1,offvalue=0,variable=var18,bg='lightblue')
coffee.grid(row=3,column=0,sticky=W)

Wines=Checkbutton(drinksFrame,text='Wine',font=('arial',10,'bold'),onvalue=1,offvalue=0,variable=var19,bg='lightblue')
Wines.grid(row=4,column=0,sticky=W)

#Entry fields
textTomato_soup=Entry(StartersFrame,font=('arial',10,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Tomato_soup)
textTomato_soup.grid(row=0,column=1)

textChicken_soup=Entry(StartersFrame,font=('arial',10,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Chicken_soup)
textChicken_soup.grid(row=1,column=1)

textCrispy_corn=Entry(StartersFrame,font=('arial',10,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Crispy_soup)
textCrispy_corn.grid(row=2,column=1)

textguacamole_salad=Entry(StartersFrame,font=('arial',10,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_guacamole_salad)
textguacamole_salad.grid(row=3,column=1)

textchicken_salad=Entry(StartersFrame,font=('arial',10,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chicken_salad)
textchicken_salad.grid(row=4,column=1)

textgrilled_fish_and_potatoes=Entry(main_courseFrame,font=('arial',10,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_grilled_fish_and_potatoes)
textgrilled_fish_and_potatoes.grid(row=0,column=1)

textchicken_and_rice=Entry(main_courseFrame,font=('arial',10,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chicken_and_rice)
textchicken_and_rice.grid(row=1,column=1)

textshepards_pie=Entry(main_courseFrame,font=('arial',10,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_shepards_pie)
textshepards_pie.grid(row=2,column=1)

textcheese_pasta=Entry(main_courseFrame,font=('arial',10,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_cheese_pasta)
textcheese_pasta.grid(row=3,column=1)

textchocolate_icecream=Entry(desertFrame,font=('arial',10,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chocolate_icecream)
textchocolate_icecream.grid(row=0,column=1)

textdoughnuts=Entry(desertFrame,font=('arial',10,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_doughnuts)
textdoughnuts.grid(row=1,column=1)

textTiramisu=Entry(desertFrame,font=('arial',10,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Tiramisu)
textTiramisu.grid(row=2,column=1)

textcheese_cake=Entry(desertFrame,font=('arial',10,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_cheese_cake)
textcheese_cake.grid(row=3,column=1)

textkulfi=Entry(desertFrame,font=('arial',10,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_kulfi)
textkulfi.grid(row=4,column=1)

textmineral_water=Entry(drinksFrame,font=('arial',10,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_mineral_water)
textmineral_water.grid(row=0,column=1)

texttea=Entry(drinksFrame,font=('arial',10,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_tea)
texttea.grid(row=1,column=1)

textfruit_juice=Entry(drinksFrame,font=('arial',10,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_fruit_juice)
textfruit_juice.grid(row=2,column=1)

textcoffee=Entry(drinksFrame,font=('arial',10,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_coffee)
textcoffee.grid(row=3,column=1)

textWines=Entry(drinksFrame,font=('arial',10,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Wines)
textWines.grid(row=4,column=1)

#cost

labelCostofStarters=Label(costFrame,text='Cost of Starters',font=('arial',10,'bold'),bg='light blue')
labelCostofStarters.grid(row=0,column=0)

textCostofStarters=Entry(costFrame,font=('arial',10,'bold'),state='readonly',textvariable=CostofStartersvar)
textCostofStarters.grid(row=0,column=1,padx=41)

labelCostofmaincourse=Label(costFrame,text='Cost of Main Course',font=('arial',10,'bold'),bg='light blue')
labelCostofmaincourse.grid(row=1,column=0)

textCostofmaincourse=Entry(costFrame,font=('arial',10,'bold'),state='readonly',textvariable=Costofmaincoursevar)
textCostofmaincourse.grid(row=1,column=1,padx=41)

labelCostofdeserts=Label(costFrame,text='Cost of Deserts',font=('arial',10,'bold'),bg='light blue')
labelCostofdeserts.grid(row=2,column=0)

textCostofdeserts=Entry(costFrame,font=('arial',10,'bold'),state='readonly',textvariable=Costofdesertsvar)
textCostofdeserts.grid(row=2,column=1,padx=41)

labelCostofdrinks=Label(costFrame,text='Cost of Main Course',font=('arial',10,'bold'),bg='light blue')
labelCostofdrinks.grid(row=3,column=0)

textCostofdrinks=Entry(costFrame,font=('arial',10,'bold'),state='readonly',textvariable=Costofdrinksvar)
textCostofdrinks.grid(row=3,column=1,padx=41)

labelSubtotal=Label(costFrame,text='Sub total',font=('arial',10,'bold'),bg='light blue')
labelSubtotal.grid(row=0,column=2)

textSubtotal=Entry(costFrame,font=('arial',10,'bold'),state='readonly',textvariable=Subtotalvar)
textSubtotal.grid(row=0,column=3,padx=41)

labelServiceTax=Label(costFrame,text='Service tax',font=('arial',10,'bold'),bg='light blue')
labelServiceTax.grid(row=1,column=2)

textServiceTax=Entry(costFrame,font=('arial',10,'bold'),state='readonly',textvariable=ServiceTaxvar)
textServiceTax.grid(row=1,column=3,padx=41)

labelTotal=Label(costFrame,text='Total',font=('arial',10,'bold'),bg='light blue')
labelTotal.grid(row=2,column=2)

textTotal=Entry(costFrame,font=('arial',10,'bold'),state='readonly',textvariable=Totalvar)
textTotal.grid(row=2,column=3,padx=41)

#Buttons

buttonTotal=Button(buttonFrame,text='Total',font=('arial',10,'bold'),bg='light blue',padx=15)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',10,'bold'),bg='light blue',padx=15)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('arial',10,'bold'),bg='light blue',padx=15)
buttonSave.grid(row=0,column=2)

buttonSend=Button(buttonFrame,text='Send',font=('arial',10,'bold'),bg='light blue',padx=15)
buttonSend.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='Reset',font=('arial',10,'bold'),bg='light blue',padx=15)
buttonReset.grid(row=0,column=2)

#textarea for receipts

textReceipt=Text(receiptFrame,font=('arial',10,'bold'),width=45,height=12)
textReceipt.grid(row=0,column=0)

#calculator
operator=''
def buttonClick(numbers):
    global operator
    operator = operator+numbers
    calculatorField.delete(0, END)
    calculatorField.insert(END, operator)

def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def calculate():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''

calculatorField=Entry(calculatorFrame,font=('arial',10,'bold'),width=45,bd=5,)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('arial',10,'bold'),width=8,
               command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('arial',10,'bold'),width=8,
               command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('arial',10,'bold'),width=8,
               command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(calculatorFrame,text='+',font=('arial',10,'bold'),width=8,
               command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('arial',10,'bold'),width=8,
               command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('arial',10,'bold'),width=8,
               command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('arial',10,'bold'),width=8,
               command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorFrame,text='-',font=('arial',10,'bold'),width=8,
               command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font=('arial',10,'bold'),width=8,
               command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font=('arial',10,'bold'),width=8,
               command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font=('arial',10,'bold'),width=8,
               command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMultiply=Button(calculatorFrame,text='*',font=('arial',10,'bold'),width=8,
               command=lambda:buttonClick('*'))
buttonMultiply.grid(row=3,column=3)

buttonCalculate=Button(calculatorFrame,text='Calculate',font=('arial',10,'bold'),width=8
                       ,command=calculate)
buttonCalculate.grid(row=4,column=0)

buttonClear=Button(calculatorFrame,text='Clear',font=('arial',10,'bold'),width=8,
                   command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font=('arial',10,'bold'),width=8,
               command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDivide=Button(calculatorFrame,text='/',font=('arial',10,'bold'),width=8,
               command=lambda:buttonClick('/'))
buttonDivide.grid(row=4,column=3)

root.mainloop()
