

def change_case(func):
    def inner(name):
        return "Hi"+name.upper()
    return inner

@change_case
def display(name):
    print(name)


display("Rahul")
print("*****")

display("Sonia")
