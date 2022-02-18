prices = [2000,1000,3000,5000]

# double_prices=[]

# for price in prices:
#     double_prices.append(price*2)

# print(double_prices);

double_prices=[price*2 for price in prices]

print(double_prices);

nums=[1,2,3,4,5,6,7,8,9,10]

# double_evenNums=[]
# for num in nums :
#      if (num%2)==0 :
#          double_evenNums.append(num*2)

# print(double_evenNums);

double_evenNums=[num*2 for num in nums if (num%2)==0]
print(double_evenNums);