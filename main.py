from testing import*
#Funtions go here...
def pie_burger(question):
    vaild = False
    while not vaild:
        response = input(question).lower()

        if response == "pie" or response == "Pie":
            print(" we currently only have pies and burgers in store")
            print("burgers are $7.89 and pies are $4.50")

        if response == "no" or response == "n":
            print(" thank you for buying at fraser high school canteen")


#Main Routine goes here...
name = str(input("whats your name"))
print("kia ora", name)
answer = input(" would you like to see our menu? ").lower()
if answer == "yes" "Yes":
  print ("program continues")
elif answer == "No" "no":
  print ("program stops")
else:
  print(" please respond with a yes or a no")









 