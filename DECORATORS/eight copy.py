
def change_case(func):
    def inner(name):
    #     if not name:
    #          result =" "
    #     else:
    #         result = "Hi"  +name.upper() 
    #     return func(result)    
    # return inner
           return func("Hi"+name.upper())
    return inner

@change_case
def display(name):
    print(name)
display("rahul")
display("sonia")
display("priya")


# HiRAHUL
# HiSONIA
# HiPRIYA
    
    