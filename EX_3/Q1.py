import re

# The regex take for internet
regex = r'([A-Za-z0-9]+[--_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'


def check_email(email):
    """
    This function takes the address email and checks with regex if the email is valid
    :param email: address mail
    :return: if the address is valid or invalid
                True for valid
                False for invalid
    """
    if re.match(regex, email):
        return True
    else:
        return False


def make_list(name_file):
    """
    This function takes the name of a file and opens it.
    After that, we pass on all emails in the file and check if they valid.
    :param name_file:
    :return:
    """
    list_valid = []
    list_invalid = []
    with open(name_file, "r") as file:
        list_email = list(file.read().split("\n"))
        for i in list_email:
            list_valid.append(i) if check_email(i) else list_invalid.append(i)
    print("emails valid :")
    print(list_valid)
    print("emails invalid :")
    print(list_invalid)


if __name__ == '__main__':
    make_list("list_email")
