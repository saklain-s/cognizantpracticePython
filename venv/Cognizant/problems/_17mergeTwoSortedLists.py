"""
Example
Input
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
Output
[1, 2, 3, 4, 5, 6, 7, 8]
"""

def merge_sorted(list1, list2):
    i = 0
    j = 0
    newList=[]

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            newList.append(list1[i])
            i+=1
        else:
            newList.append(list2[j])
            j+=1
    while i < len(list1):
        newList.append(list1[i])
        i+=1
    while j < len(list2):
        newList.append(list2[j])
        j+=1
    # newList.extend(list1[i:])
    # newList.extend(list2[j:])
    return newList

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8,10]
print(merge_sorted(list1,list2))