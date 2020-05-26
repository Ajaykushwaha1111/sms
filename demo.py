
def generate_password_randam():
    import random
    import string
    password =''.join(random.choices(string.ascii_uppercase+ string.ascii_lowercase+string.digits, k =8))
    return password

p=generate_password_randam()


# import random
#
# otp = random.randrange(111111,999999)
# print(otp)

def myadd(*a,**kwargs):
    print(a,kwargs)

myadd()