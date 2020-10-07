def xyz(*args,**kwargs):
    print(kwargs)
    print(args)
    
b= ["a","b","c","d"]
a = {"sachin":"teacher","raman":"hero","shub":"netaji"}

xyz(*b,**a)