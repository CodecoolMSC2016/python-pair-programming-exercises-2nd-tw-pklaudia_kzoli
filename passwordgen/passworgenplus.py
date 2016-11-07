import string
import random
def passwordgenS(chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    print(''.join(random.choice(chars) for _ in range(random.randint(12,20))))
def passwordgenM(chars=string.ascii_lowercase + string.digits):
    print(''.join(random.choice(chars) for _ in range(random.randint(8,16))))
def passwordgenW(chars=string.ascii_uppercase):
    print(''.join(random.choice(chars) for _ in range(random.randint(4,8))))    
def options():
    print("\ns : Strong\nm : Medium\nw : Weak\n")
while True:
    action =(input("How strong you want your password to be? (o:options) : "))
    if action == "o":
        options()
    if action == "s":
        passwordgenS()
    if action == "m":
        passwordgenM()
    if action == "w":
        passwordgenW()