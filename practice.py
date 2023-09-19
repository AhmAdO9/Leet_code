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



# file = list(open('topics.csv','r', encoding='utf-8'))
# file.pop(0)    
# file.pop(1)    
# file.pop(2)
# print(file[0])    


# d = {
#     '(a,b)':'b'
# }

# d['(a,b)']


def canCompleteCircuit(gas, cost):
    n = len(gas)
    
    total_gas = 0  # Total gas in the tank
    current_gas = 0  # Gas at the current station
    start_index = 0  # Index of the starting station
    
    for i in range(n):
        total_gas += gas[i] - cost[i]
        current_gas += gas[i] - cost[i]
        
        # If the current gas becomes negative, reset the starting station
        if current_gas < 0:
            current_gas = 0
            start_index = i + 1
    
    # If the total gas is negative, it means there is no solution
    if total_gas < 0:
        return -1
    
    return start_index

# Example usage:
gas = [2,3,4]
cost = [3,4,3]
result = canCompleteCircuit(gas, cost)
print(result) 
