my_list = [2, 3, 4, 5, 6]
res = []
for i in range((len(my_list)+1)//2):
    res.append(my_list[i]*my_list[len(my_list)-1-i])
print(res)
