def testcase(func):
    def inner(a,b):
        if b==0:
            print("buddy -- can't divide by zero")
        else:
            return func(a,b)    
        
    return inner

@testcase
def calC(a,b):
    print(a/b)
calC (10,2)
calC(10,0) 
# 5.0
# buddy -- can't divide by zero