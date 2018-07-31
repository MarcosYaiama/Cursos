from dic_1 import displayInventory
dragon_loot=['gold coin',
             'dagger',
             'gold coin',
             'gold coin',
             'ruby']

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

inv = {'gold coin':42, 'rope':1}
print(inv)
inv = addToInventory(inv, dragon_loot)
displayInventory(inv)


