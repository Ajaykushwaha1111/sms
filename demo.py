
# def generate_password_randam():
#     import random
#     import string
#     password =''.join(random.choices(string.ascii_uppercase+ string.ascii_lowercase+string.digits, k =8))
#     return password
#
# p=generate_password_randam()


# import random
#
# otp = random.randrange(111111,999999)
# print(otp)

# def myadd(*a,**kwargs):
#     print(a,kwargs)
#
# myadd()




# from datetime import datetime, timedelta
# # import time
# # now = datetime.now()
# # other_time = now + timedelta(seconds=60)
# #
# # other_time =other_time.strftime('%M:%S')
# # while True:
# #     time.sleep(1)
# #     ctime =datetime.now().strftime('%M:%S')
# #     print(ctime)
# #     if ctime==other_time:
# #         break










data={'attempt': 0, 'correct': 0, 'wrong': 0, 'missed': 15}
print(data['correct'])




# total =15
# attempt =8
# correct =int(input('correct='))
# wrong =4
#

myresult =dict()
myresult['percentage']=result
if result<=33:
    myresult['status']='Fail'
if result>=33 and result<50:
    myresult['status']='Third'
if result>=50 and result<60:
    myresult['status']='Second'
if result>=60 and result<70:
    myresult['status']='First'
if result>=80 and result<90:
    myresult['status']='Great'
if result>=90 and result<=100:
    myresult['status']='Exellent'
print(myresult)
