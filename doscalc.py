from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button

def calc():
	#Delete any existing values
	dr.delete(0,'end')
	qm.delete(0,'end')

	#Calculation of Dosing rate
	Qp,X = float(qp.get()),float(x.get())
	dr_calc = Qp*X
	dr.insert(0, dr_calc)

	#Calculation of Quantity
	Qd,Vt,conc = float(qd.get()),float(vt.get()),float(con.get())
	d = dr_calc*(100/conc)
	u = ((Vt*d)/Qd)/1000
	qm.insert(0, round(u,1))


#Creating the window
root = Tk()
root.title('DosCalc')
root.geometry("325x300")
root.resizable(width=False,height=False)



#------------------------Definition of components-------------------------

#Entry field for Feed pump flow rate
qplabel= Label(root, text="Feed pump flowrate")
qpunitlabel = Label(root, text="m3/h") #Displays units
qp = Entry(root, width=20,borderwidth=1) #Entry box for feed pump flowrate

#Entry Field for desired dosage
xlabel= Label(root, text="Dosage quantity")
xunitlabel = Label(root, text="ppm") #Displays units
x = Entry(root, width=20,borderwidth=1) #Entry box for dosage

#Concentration of Solution
conlabel= Label(root, text="Concentration")
conunitlabel= Label(root, text="%") #Display units
con = Entry(root, width = 20, borderwidth=1)
con.insert(0, '100') #Default value assumed to be 100% concentration

#Dosing Pump Flowrate
qdlabel= Label(root, text="Dosing Pump Flowrate")
qdunitlabel = Label(root, text="lph") #Displays units
qd = Entry(root, width=20,borderwidth=1) #Entry box for flowrate

#Tank Capacity
vtlabel= Label(root, text="Dosing Tank Volume")
vtunitlabel = Label(root, text="Litre")
vt = Entry(root, width=20,borderwidth=1)

#Calculate Button
calc = Button(root, text="Calculate!",padx=10,pady=8, command=calc)

#Rate of Dosing
drlabel= Label(root, text="Dosing rate @")
drunitlabel = Label(root, text="g/h") 
dr = Entry(root, width=20,borderwidth=1,bg="Yellow",fg="Red")

#Quantity for Mixing
qmlabel= Label(root, text="Quantity of chemical")
qmunitlable = Label(root,text="Kg")
qm = Entry(root, width=20,borderwidth=1,bg="Yellow",fg="Red")

#-------------------------Component Placement-----------------------------

#Pump flowrate section
qplabel.grid(row=0,column=0, padx = 5)
qp.grid(row=0,column=1,pady = 5)
qpunitlabel.grid(row=0,column=2,pady =2)

#Dosage section
xlabel.grid(row=1,column=0, padx = 5)
x.grid(row=1,column=1,pady = 5)
xunitlabel.grid(row=1,column=2,pady =2)

#Concentration Section
conlabel.grid(row=2, column=0, padx=5)
con.grid(row=2,column=1,pady = 5)
conunitlabel.grid(row=2,column=2,pady =2)

#Dosing Pump flowrate section
qdlabel.grid(row=3,column=0, padx = 5)
qd.grid(row=3,column=1,pady = 5)
qdunitlabel.grid(row=3,column=2,pady =2)

#Tank Capacity section
vtlabel.grid(row=4,column=0, padx = 5)
vt.grid(row=4,column=1,pady = 5)
vtunitlabel.grid(row=4,column=2,pady =2)

#Calculate button
calc.grid(row=5,column=1,pady=10)

#Rate of Dosing
drlabel.grid(row=6,column=0, padx=5)
dr.grid(row=6,column=1,pady =2)
drunitlabel.grid(row=6,column=2,pady=2)

#Quantinty for Mixing
qmlabel.grid(row=7,column=0,padx=5)
qm.grid(row=7,column=1,pady=2)
qmunitlable.grid(row=7,column=2,pady=2)

root.mainloop() #Event loop
