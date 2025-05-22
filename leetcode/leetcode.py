firstList = [[14,16]]
secondList = [[7,13],[16,20]]

# exp o/p: [[1,2],[3,5],[6,7],[9,10],[11,12],[13,14]]

'''
[0,2] | [3,7] | [8,12] | [13,14]
[1,5] | [6,7] | [9,10] | [11,12] | [13,15]



cur_value       next_value  prev_value  res_arr
---------       ----------  ----------  -------
[0,2] [i]       [1,5] [i]   []          [1,2]   i = 0
[2,5] [i+=1]    [3,7]       [6,7]       [3,5]   i = 1
[5,7]           [6,7]                   [6,7]
i += 1--------------------------------------- 
[8,12] [i]      [9,10] [i]              [9,10]  i = 2
[10,12] [i+=1]  [11,12]     [13,14]     [11,12] i = 3
i += 1---------------------------------------
[13,15]         [13,14]                 [13,14] i = 4

'''

i: int = 0
if len(firstList) == 0 or len(secondList) == 0: print([])
cur_value: list = firstList[i]
next_value: list = secondList[i]
prev_value: list = []
res_arr: list = []

while i < max(len(firstList), len(secondList)):
    if cur_value and next_value:
    
        if max(cur_value[0], next_value[0]) <= min(cur_value[1], next_value[1]):
        
            res_arr.append([max(cur_value[0], next_value[0]), min(cur_value[1], next_value[1])])

            if min(cur_value[1], next_value[1]) != max(cur_value[1], next_value[1]):
                cur_value = [min(cur_value[1], next_value[1]), max(cur_value[1], next_value[1])]
                if not prev_value:
                    i += 1
                    if i < min(len(firstList), len(secondList)):
                        next_value = firstList[i] if firstList[i][0] <= secondList[i][0] else secondList[i]
                        prev_value = secondList[i] if next_value == firstList[i] else firstList[i]
                else:
                    next_value = prev_value
                    prev_value = []
            else:
                i += 1
                if i < len(firstList) or i < len(secondList):
                    cur_value = firstList[i] if i < len(firstList) else secondList[i]
                    if i < len(secondList):
                        next_value = secondList[i]
                    else:
                        if not prev_value: break
                        else:
                            next_value = prev_value
                            prev_value = []
                else:
                    break
        else:
            cur_value = next_value
            next_value = prev_value
            prev_value = []
    else:
        break
            
print(res_arr)
