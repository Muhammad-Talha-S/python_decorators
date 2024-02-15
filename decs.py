'''
Muhammad Talha Saleem
Python Decorators
'''
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

def my_logger(orignal_function):
    logging.basicConfig(filename='output.log',level=logging.INFO)
    @wraps(orignal_function)
    def wrapper_fun(*args , **kwargs):
        logging.info(f'Ran with args {args} and kwargs {kwargs}')
        orignal_function(*args , **kwargs)
    
    return wrapper_fun
    
@my_logger
@imp.timer_func
def display_info(name, age , Industry):
    print(f'{name} is {age} years old and he works at {Industry}')

display_info('Talha' , 22, 'SOCO Engineers')

@decorator_cls
@imp.timer_func
@my_logger
def display_info_using_class_as_decorator(name, age , Industry):
    print(f'{name} is {age} years old and he works at {Industry}')

display_info_using_class_as_decorator('Arslan',23,'SOCO Engineers')