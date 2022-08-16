import logging
import imp
from functools import wraps

def decorator_fun(orignal_function):
    def wrapper_fun(*args , **kwargs):
        print('Wrapper Function Ran')
        orignal_function(*args , **kwargs)
    return wrapper_fun

class decorator_cls(object):

    def __init__(self,orignal_fun):
        self.orignal_fun = orignal_fun
    
    def __call__(self, *args, **kwargs):
        print('Call Method Ran')
        self.orignal_fun(*args , **kwargs)



@decorator_fun
def display():
    print('Display Function Ran')

# @decorator_fun
# def display_info(name, age):
#     print(f'Information Below')
#     print(f'Name : {name}')
#     print(f'Age : {age}')



def my_logger(orignal_function):
    logging.basicConfig(filename='output.log',level=logging.INFO)
    @wraps(orignal_function)
    def wrapper_fun(*args , **kwargs):
        logging.info(f'Ran with args {args} and kwargs {kwargs}')
        orignal_function(*args , **kwargs)
    
    return wrapper_fun
    

# display()
# display_info('Talha' , 22)

# @my_logger
# def display_info(name, age):
#     print(f'Information Below')
#     print(f'Name : {name}')
#     print(f'Age : {age}')

# display_info('Ali' , 22)

@my_logger
@imp.timer_func
def display_info(name, age , Industry):
    print(f'{name} is {age} years old and he works at {Industry}')

display_info('Talha' , 22, 'SOCO Engineers')