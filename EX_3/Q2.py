import doctest

last_name_func = {}

def lastcall(func):
    """
    This is Kastan of function
    I take the key is it name of argument and the value of argument
    check if is in global dict if no i save the argument and the result and the name of the function
    if not in dict we check if the argument send before if yes we retrun the result
    else we did the function
    :param func:
    :return:
    >>> func_add(2)
    4
    >>> func_sub(2)
    0
    >>> func_div(4)
    2.0
    >>> func_pow(4)
    16
    >>> func_add(2)
    'i already told you that the answer is 4'
    >>> func_div(4)
    'i already told you that the answer is 2.0'
    """

    def wrapper(*args, **kwargs):
        global last_name_func
        if kwargs:
            x = list(kwargs.keys())
            y = list(kwargs.values())
            key = x[0]
            value = y[0]
        elif args is not None:
              key = args[0]
              value = args[0]
        f_name = func.__name__
        if f_name not in last_name_func:
            return_val = func(*args, **kwargs)
            last_name_func[f_name]={key:{value:return_val}}
            return return_val
        elif last_name_func[f_name][key][value]:
            return f"i already told you that the answer is {last_name_func[f_name][key][value]}"
        else:
            return
    return wrapper


@lastcall
def func_add(x: int):
    return x + x


@lastcall
def func_sub(x: int):
    return x - 2


@lastcall
def func_pow(x: int):
    return x ** 2


@lastcall
def func_div(x: int):
    return x / 2


@lastcall
def func_name(x: str):
   return "Hello " + x


if __name__ == '__main__':
    doctest.testmod()
    last_name_func={}

    print("----------------workflow -----------------")
    print("1) func_add(2) result is 4 ----> ",func_add(2))
    print("2) func_sub(2) result is 0 ----> ", func_sub(2))
    print("3) func_duv(4) result is 2 ----> ", func_div(4))
    print("4) func_pow(4) result is 16 ----> ", func_pow(4))
    print("5) func_name(2) result is 'hello daniel' ----> ", func_name("daniel"))
    print("1) func_add(2) result is i already told you that the answer is 4 ----> ", func_add(2))
    print("2) func_sub(2) result is i already told you that the answer is 0 ----> ", func_sub(2))
    print("3) func_duv(4) result is i already told you that the answer is 2 ----> ", func_div(4))
    print("4) func_pow(4) result is i already told you that the answer is 16----> ", func_pow(4))
    print("5) func_name(2) result is i already told you that the answer is 'hello daniel'----> ", func_name("daniel"))