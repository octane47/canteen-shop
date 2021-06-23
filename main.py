#Funtions go here...

def yes_no(question):
    vaild = False
    while not vaild:
        response = input("would you like to see the canteen menu").lower()

        if response == "yes" or response == "y":
            response = "yes "
            return response
            print(" we currently only have pies and burgers in store")
            print("burgers are $7.89 and pies are $4.50")

        if response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please answer yes / no")

# Main Routine goes here...
name = str(input("whats your name"))
print("kia ora", name)



 