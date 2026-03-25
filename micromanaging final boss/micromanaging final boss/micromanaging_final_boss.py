inventory = {}
choice = "silly goose, five banana"
while choice != "4":
    print("")
    print("---Personal Inventory Manager---")
    print("")
    print("Options: [1] Add    [2] Remove    [3] List    [4]Exit")
    choice = input("Select an option(1-4): ")
    if choice == "1":
        name = input("Enter item name: ").strip().capitalize()
        qty = int(input("How many " + name + "s?: "))
        inventory[name] = qty
        print("Added", str(qty), name + "s.")
    elif choice == "2":
        name = input("Enter item name: ").strip().capitalize()
        del inventory[name]
        print("Removed", name + ".")
    elif choice == "3":
        for item in inventory:
            print(str(inventory[item]), str(item))
    elif choice == "4":
        break
    else:
        print("Please choose something from the avalible options.")
print("Exiting Personal Inventory Manager. Goodbye!")