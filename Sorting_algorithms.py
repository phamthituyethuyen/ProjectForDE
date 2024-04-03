####BUBBLE SORT#####
def bubble_sort(list):
    for i in range(len(list)):
        for j in range(0,len(list) - i -1):
            if list[j] >list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]

    return list
list_to_sort = [45,32,7,6,98,100,3,42,56,23]
print(bubble_sort(list_to_sort))

#########MERGE SORT##########
def merge_sort