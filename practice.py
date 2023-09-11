# def hello(func):
#     def inside(x):
#         print(x)
#         print("inside")
#         relu = func(x)
#     return inside


# @hello
# def sqr(n):
#     return n*n
# sqr(2)

# def make_pretty(func):

#     # def inner():
#         print("I got decorated")
#         func()
#     # return inner

# @make_pretty
# def ordinary():
#     print("I am ordinary")

# ordinary()

# def make_pretty(func):
#     # define the inner function 
#     def inner():
#         # add some additional behavior to decorated function
#         print("I got decorated")

#         # call original function
#         func()
        
#     # return the inner function
    
#     return inner

# # define ordinary function
# def ordinary():
#     print("I am ordinary")
    
# # decorate the ordinary function
# # decorated_func = make_pretty(ordinary)
# # call the decorated function
# # decorated_func()
# (make_pretty(ordinary)())



arr = [1,2]
try:
    print(arr[2])
except IndexError:
     arr.append(0)
     print(arr[2])