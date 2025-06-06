def sub_decorator(func):
    def wrapper(num1,num2):
        if num1 < num2:
            num1,num2 = num2,num1
            return func(num1,num2)
        else:
            return func(num1,num2)
    return wrapper
