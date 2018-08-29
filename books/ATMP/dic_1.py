stuff ={'arrow':12,'gold coin':42,'rope':1,'torch':6,'dagger':1}

def displayInventory(inventario):
    n = 0
    print('Inventory:')
    for k,v in inventario.items():
        print('{} {}'.format(v,k))
        n += v
    print('Total number of items: {}'.format(n))

#displayInventory(stuff)
