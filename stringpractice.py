# str1="saiteja"
# l=len(str1)
# mi=l//2  #3
# res=str1[mi-1:mi+2]
# print(res)




list1=[33,45,99,99,99,5,2,1,1,1,99,2]
random=0
list2=[]
for ele in list1:
    if random==ele:
        list2.append(ele)
    random=ele
print(list2)