import doctest


class List(list):
    """
        This class is like 2D arr and get to item
    """
    def __init__(self, *args):
        self.lst = []
        if not args:
            return
        else:
            for i in args:
                if not isinstance(i,list):
                    raise Exception("need insert type list ")
                else:
                    self.lst.append(i)

    def append(self , *args):
        """
            This function implement append of List
        :param args:
        :return:
        """
        if not args:
            return
        else:
            for i in args:
                if not isinstance(i,list):
                    raise Exception("need insert type list ")
                else:
                    self.lst.append(i)


    def __append__(self,*args):
        if not args:
            return
        else:
            for i in args:
                if not isinstance(i,list):
                    raise Exception("need insert type list ")
                else:
                    self.lst.append(i)

    def __getitem__(self, *args):
        """
            This function gets a specific item in our data structure
        :param args: the loction of item
        :return:
        """
        if not args:
            return
        else:
            if not isinstance(args[0] , int) :
                x = list(args[0])
            else:
                return self.lst[args[0]]
            res = self.lst[x[0]]
            for i in x[1:]:
                res = res[i]
            return res


    def __str__(self):
        return str(self.lst)



if __name__ == '__main__':

    print("\n--------------TEST---------------\n")
    mylist = List(
        [[1, 2, 3, 33], [4, 5, 6, 66]],
        [[7, 8, 9, 99], [10, 11, 12, 122]],
        [[13, 14, 15, 155], [16, 17, 18, 188]],
    )
    mylist.append([1, 2, 3])
    print("1) the result of append  [[[1, 2, 3, 33], [4, 5, 6, 66]], [[7, 8, 9, 99], [10, 11, 12, 122]], [[13, 14, 15, 155], [16, 17, 18, 188]], [1, 2, 3]] -----> ",mylist)
    print("2) the result is 66 ----->  ",mylist[0,1,3])
    print("3) the result is 99 ----->  ",mylist[1,0,3])
    print("4) the result is 188 ----->  ", mylist[2, 1, 3])
    print("5) the result is 1 ----->  ", mylist[3, 1])
    print("6) the result is [[1, 2, 3, 33], [4, 5, 6, 66]] ----->  ", mylist[0])
    print("7) the result is [1, 2, 3] ----->  ", mylist[3])