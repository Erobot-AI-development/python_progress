def example(str1):
    s = 0
    list1 = [] 
    for i in str1:
        if i.isdigit():
            s = s + int(i)
        else:
            list1.append(i)
    list1.append(str(s))
    list2 = "".join(list1)
    return list2
   
example('apple555banana333')