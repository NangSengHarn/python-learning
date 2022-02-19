# with open('./about.txt','w') as file:
#     file.write('I am Nang Seng Harn')

# #other work

# #with open('./about.txt','w') as file:#overwrite
# with open('./about.txt','a') as file:#ammand 
#     file.write('\nI am 20 years old')

lists=['I am Nang Seng Harn','\nI am 20 years old']
with open('./about.txt','a')as file:
    file.writelines(lists)