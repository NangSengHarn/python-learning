# file=open('./text.txt')

# # for line in file:
# #     print(line)

# # file.seek(0); #move cursor to the beginning

# # lineLists=file.readlines()
# # print(lineLists);

# file.seek(50)
# paragraph=file.read(100)
# #read from words50 to words100

# file.close()

with open('./text.txt') as file: #no need to close file
    for line in file:
        print(line);

