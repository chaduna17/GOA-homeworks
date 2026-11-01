#3) შექმენი ცვლადი:

#password = "python123"

#მომხმარებელს შეაყვანინე პაროლი.

#თუ სწორია, დაბეჭდე "წარმატებით შეხვედი".
#წინააღმდეგ შემთხვევაში "არასწორი პაროლი".



password = "python123"
entered_password = input("შეიყვანე პაროლი")
if entered_password == password:
    print("წარმატებით შეხვედი")
else:
    print("არასწორი პაროლი")