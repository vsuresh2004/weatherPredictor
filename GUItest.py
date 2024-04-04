# Import Required Library
from tkinter import *
from tkcalendar import Calendar
import pandas as pd
from sklearn.model_selection import train_test_split
from datetime import date
from sklearn.ensemble import RandomForestRegressor
#run command "pip install tkcalendar in terminal before running
def run_program(measure, city, selectdate):
    data = pd.read_csv('weatherData\weatherData' + city +'.csv')
    if measure == "Precipitation":
        measindex = 4
    elif measure == "Max Temperature":
        measindex = 5
    elif measure == "Min Temperature":
        measindex = 6
    else:
        measindex = 7
    badIndeces = []
    for i in range(len(data)):
        if data.iloc[i][measindex] < -98:
            badIndeces.append(i)
    for i in badIndeces:
        data = data.drop(i)
    dateparts = selectdate.split("/",2)
    daysOfYear = []
    for i in range(len(data)):
        d0 = date(int(data.iloc[i][1]), int(data.iloc[i][2]), int(data.iloc[i][3]))
        d1 = date(int(data.iloc[i][1]), 1, 1)
        dateBetween = (d0 - d1).days + 1
        daysOfYear.append(dateBetween)
    data.insert(len(data.columns), "DAYSOFYEAR", daysOfYear)
    data.insert(len(data.columns), "YEARSFROMSTART", data[' YEAR'] - data.iloc[0][1])

    x = data[['DAYSOFYEAR', 'YEARSFROMSTART']]
    y = data[[' MAX TEMP']]
    for i in range(len(x)):
        x.iloc[i][0] = float(x.iloc[i][0])
        x.iloc[i][1] = float(x.iloc[i][1])
        y.iloc[i][0] = float(y.iloc[i][0])

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 43)

    maxDays = max(x['DAYSOFYEAR'])
    maxYears = max(x['YEARSFROMSTART'])
    scaledDays = x['DAYSOFYEAR'] / maxDays
    scaledYears = x['YEARSFROMSTART'] / maxYears
    x.insert(len(x.columns), "scaledDays", scaledDays)
    x.insert(len(x.columns), "scaledYears", scaledYears)

    scaledTrain = x[['scaledDays', 'scaledYears']]
    model = RandomForestRegressor()
    model.fit(scaledTrain, y)


    predictDate = date(2000 + int(dateparts[2]), int(dateparts[0]), int(dateparts[1]))
    startDate = date(predictDate.year, 1, 1)
    countDays = (predictDate - startDate).days + 1

    predictDays = countDays / maxDays
    predictYears = (predictDate.year - data.iloc[0][1]) / maxYears
    return "Predicted "+ measure + " for " + selectdate + " is " + str(model.predict([[predictDays, predictYears]]))

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
#cities = ['Ft.Lauderdale', 'Gainesville', 'Hialeah', 'Jacksonville', 'Miami', 'Orlando', 'PuntaGorda', 'St.Petersburg', 'Tallahassee', 'Tampa']
#cities = ['Ft.Lauderdale', 'Gainesville', 'Hialeah', 'Jacksonville', 'Miami', 'Orlando', 'PuntaGorda', 'St.Petersburg', 'Tallahassee', 'Tampa']
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
#This GUI will be a part of Vishal and I's final project. It allows a user to input a future date, measurement type, and city to predict for. However, the
#program only prints the three inputs when the GUI is closed after teh Get Date button is clicked. In the final project, these inputs will be used in the projection methods
