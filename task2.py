amount_days= 7

temperatures = []
celsius = 0
maxtemp = -999999
mintemp = 9999999
midtemp = 0
for temp in range(amount_days):
    farenheit = int(input("please enter temperature"))
    celsius = (farenheit - 32) * 5 / 9
    temperatures.append(celsius)
    print(celsius)
    if celsius < 10:
        print("Холодно")
    elif celsius > 10 and celsius <= 28 :
        print("Тепло")
    elif  celsius > 28 and celsius < 36:
        print("Спекотно")
    elif celsius > 36:
        print("Дуже спекотно")

total =sum(temperatures)
average = sum(temperatures)/7
print("average temperature: ", f" average {average}")
for x in temperatures:
    if x > maxtemp:
        maxtemp = x
    if x < mintemp:
        mintemp = x
print("max temp = ", str(maxtemp))
print("min temp = ", str(mintemp))




