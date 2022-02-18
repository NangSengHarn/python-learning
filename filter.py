from ast import comprehension


nums=[1,2,3,4,5,6,7,8,9,10]

def even(num) :
    return (num%2)==0

evenNums=list(filter(even,nums))
print(evenNums)

# comprehension way
# evenNums=[num for num in nums if (num%2)==0]
# print(evenNums);

# lambda function
#evenNums=list(filter(lambda num:(num%2)==0,nums))