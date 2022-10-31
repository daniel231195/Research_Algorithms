import doctest

"""
    Question number 1

"""

def f(x: int, y: float, z):
    return x + y + z


def safe_call(f, **kwargs):
    """
     First, we will check and save what type of arguments are in the function,
    then we will go through each argument we received and check if they match,
     if not we will check that they are not in the function to which we sent
     the arguments if so we will throw an error because the type does not match
    :param f: function
    :param kwargs: argument with name
    :return: the ans from f
    """
    """
        >>> safe_call(f, x=5, y=7.0, z=3)
        15.0
        >>> safe_call(f, x=5.0, y=7.0, z=3)
        Traceback (most recent call last):
            ...
        Exception: raises an exception
        >>> safe_call(f, x="a", y=7.0, z=3)
        Traceback (most recent call last):
            ...
        Exception: raises an exception
        >>> safe_call(f, x=5, y=7.0, z=3.0)
        15.0
    """
    try:
        annotations = f.__annotations__
        for key in kwargs:
            if key in annotations and type(kwargs[key]) is annotations[key]:
                1
            elif key in annotations:
                raise Exception("raises an exception")
        return f(**kwargs)
    except:
        raise Exception("raises an exception")



if __name__ == '__main__':
    doctest.testmod()
    print("\n------------Q 1 ----------------- \n")
    print("1) run f, x=5, y=7.0, z=3 need 15.0 ")
    print("asn 1 is : ",safe_call(f, x=5, y=7.0, z=3),"\n")

    print("2) run f, x=1, y=0.5, z=0.5 need 2.0 ")
    print("asn 1 is : ", safe_call(f, x=1, y=0.5, z=0.5), "\n")

    # print("3) run f, x=2.0, y=0.5, z=0.5 need error ")
    # print("asn 3 is :  Exception", safe_call(f, x=2.0, y=0.5, z=0.5), "\n")

    print("4) run f, x=2, y='a', z=0.5 need error ")
    print("asn 4 is :  Exception", safe_call(f, x=2.0, y=0.5, z=0.5), "\n")