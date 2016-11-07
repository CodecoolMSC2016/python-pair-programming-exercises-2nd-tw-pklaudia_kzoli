import string
import random

def passwordgen(chars=string.ascii_uppercase + "!" + "@" + "#" + "$" + "%" + "^" + "&" + "*" + "(" + ")" + "?" + string.ascii_lowercase + string.digits):
    passw =''.join(random.choice(chars) for _ in range(random.randint(8,16)))
    print(passw)
    return passw


def main():
    passwordgen()
    return


if __name__ == '__main__':
    main()
