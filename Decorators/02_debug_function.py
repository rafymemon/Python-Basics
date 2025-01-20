

def debug(func) :
    def wrapper(*args, **kwargs) :
        args_value = ', '.join(str(args) for args in args)
        kwargs_value = ', '.join(f"{k} = {v}" for k, v in kwargs.items())
        print(f"calling : {func.__name__} with args = {args_value} and kwargs = {kwargs_value}")
        return func(*args, **kwargs)    
    return wrapper



@debug
def greet(name, greeting) :
    print(f"{greeting}, {name}")
#@debug
#def hello() :
#   print("hello")
    
    
#hello()
greet("Rafy", "hello")