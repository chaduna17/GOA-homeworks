#3.დაწერეთ პროგრამა, რათა შეამოწმოთ იყოფა თუ არა რიცხვი სხვა რიცხვზე.
number1=int(input("შეიყვანე პირველი რიცხვი"))
number2=int(input("შეიყვანე მეორე რიცხვი"))

if number1 / number2 == int(number1 / number2):
    print("იყოფა")
else:
    print("არ იყოფა")