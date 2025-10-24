def add_item(item, lst=[]):
    lst.append(item)
    return lst

def add_item2(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2]  ❌ common gotcha

print(add_item(3))
print(add_item(4))

print(add_item2(2))
print(add_item2(1))