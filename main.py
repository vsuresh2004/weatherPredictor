from tkinter import *
from tkcalendar import Calendar
from datetime import date

root = Tk()

root.geometry("400x400")

cal = Calendar(root, selectmode = 'day',
			year = 2021, month = 7,
			day = 11)
variable1 = StringVar(root)
variable2 = StringVar(root)
T = Text(root, height=5, width=52)
l = Label(root, text="Which measurement would you like to project for?")
l.config(font=("Times New Roman", 12))
variable1.set("Max Temperature") # default value
variable2.set("Tallahassee")
l.pack()
w = OptionMenu(root, variable1, "Max Temperature", "Min Temperature", "Precipitation", "Mean Temperature")
w.pack()
q = Label(root, text="Which measurement would you like to project for?")
q.pack()
cities = ["Apalachicola", "Arcadia", "Archbold", "Avon Park", "Bartow", "Belle Glade", "Bradenton", "Brooksville", "Bushnell", "Canal Point", "Chipley", "Clermont", "Crescent City", "Crestview", "Cross City", "Daytona Beach", "De Funiak Springs", "Deland", " Desoto City", "Devil's Garden", "Everglades", "Federal Point", "Fernandina Beach", "Flamingo", "Ft. Drum", "Ft. Green", "Ft. Lauderdale", "Ft. Myers", "Ft. Pierce", "Gainesville", "Glen", "Hastings", "Hialeah", "High Springs", "Hillsborough", "Immokalee", "Inverness", "Jacksonville", "Jasper", "Key West", "Kissimmee", "La Belle", "Lake City", "Lisbon", "Live Oak", "Madison", "Mayo", "Melbourne", "Miami", "Monticello", "Moore Haven", "Mountain Lake", "Myakka", "Naples", "Niceville", "Oasis", "Ocala", "Okeechobee", "Orlando", "Panama City", "Parrish", "Pensacola", "Perrine", "Perry", "Plant City", "Punta Gorda", "Quincy", "Royal Palm", "St. Augustine", "St. Leo", "St. Petersburg", "Sanford", "Stuart", "Tallahassee", "Tampa", "Tarpon Springs", "Titusville", "Usher", "Venice", "Vero Beach", "Wauchala", "Weeki Wachee", "West Palm Beach", "Wewahitchka"]

k = OptionMenu(root, variable2, *cities)
k.pack()
cal.pack(pady = 20)
def find_date():
	date.config(text = "Selected Date is: " + cal.get_date())

Button(root, text = "Get Prediction",command=lambda:[(run_program(str(variable1.get()), str(variable2.get()), str(cal.get_date())))]).pack(pady = 20)

dat = Label(root, text = "")
dat.pack(pady = 20)
predictDate = cal.get_date
root.mainloop()
print(variable1.get())
print(variable2.get())
print(cal.get_date())