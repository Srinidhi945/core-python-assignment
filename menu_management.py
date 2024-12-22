def adding_item(menu, item):
    if item not in menu:
        menu.append(item)

def removing_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} does not exist in the menu.")

def checking_item(menu, item):
    return f"{item} is available" if item in menu else f"{item} is not available"

menu = ["Pizza", "Burger", "Pasta", "Salad"]
adding_item(menu, "Tacos")
removing_item(menu, "Salad")
print("Updated menu:", menu)
print(checking_item(menu, "Pizza"))
