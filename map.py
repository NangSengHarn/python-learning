from ast import comprehension


nums=[2,5,6,7,8,9,10]

def mapfunction(num):
    return num*2

nums=list(map(mapfunction,nums))
print(nums);

# comprehension way
# nums=[num*2 for num in nums]
# print(nums);

#lambda function
#nums=list(map(lambda num:num*2,nums))