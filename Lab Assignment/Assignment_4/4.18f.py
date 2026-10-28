x = 50
def fun():
    x = 20
    def inner():
        nonlocal x
        x=10
        print("Inside inner,x=",x)
    inner()
    print("Inside fun, x=",x)
fun()
print("Global,x=",x)