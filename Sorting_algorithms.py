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
def merge_sort(unsorted_list):
    if len(unsorted_list) <=1:
        return unsorted_list
    left_list = unsorted_list[:len(unsorted_list)//2]
    right_list = unsorted_list[len(unsorted_list)//2:]
 
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list,right_list))

def merge(left_half,right_half):
    res = []
    while len(left_half) != 0 and len(right_half) !=0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    
    if len(left_half) ==0:
        res = res +right_half
    else:
        res = res + left_half
    return res 

unsorted_list = [1,3,5,7,9,2,4,6,8,0]
print(merge_sort(unsorted_list))