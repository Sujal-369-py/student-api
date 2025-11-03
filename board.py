# board = [['.'for _ in range(4)]for _ in range(4)] 

# for i in board: 
#     print(i)


nums = [2,5,7,8,9,2,3,4]
k = 3
l = 0 
mark1 = mark2 = 0 
for i in range(1,len(nums)): 
    print(l)
    if nums[i-1] >= nums[i]: 
        l = i
    if i-l+1 == k:
        mark2 = mark1 
        mark1 = i-l+1 
    if mark1 - mark2 == k: 
        print("yes") 

