
def main():
    print(f"Welcome to our resturant .")
    menu={
        "Coffee":50,
        "Pasta":100,
        "Pizza":100,
        "Water":50,
        "Green Tea":70,
        "Milk tea":60
    }
    print(f"Here is our menu:")
    for key in menu:
        print(f"{key} : {menu[key]} taka ")

    total_order =0
    
    order = input(f"Which item would you like to order : ")
    for key in menu :
        if key==order :
            total_order+= menu[key]

    print(f"Your total bill is : {total_order}")

    while True:
        order_other = input("Would you like to order anything else (Yes/No):")

        if order_other =="Yes":
            order = input("Which item you want to order : ")
            for key in menu :
                if key==order:
                    total_order+=menu[key]

            print(f"Your total bill is : {total_order}")
        else :
            break


if __name__=='__main__':
    main()