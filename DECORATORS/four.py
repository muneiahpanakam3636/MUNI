
def login_req(func):
    def inner(name,islogin):
        if islogin ==False:
            print('Login required')

        else :
            return func(name,islogin)    
    return inner

@login_req
def home_page(name,islogin):
    print("Home page")
home_page("Rahul",False)    

@login_req
def About_page(name,islogin):
    print("about page")
About_page("Rahul",True)    


@login_req
def order_page(name,islogin):
    print("order page")
order_page("Rahul",False)    

# Login required
# about page
# Login require