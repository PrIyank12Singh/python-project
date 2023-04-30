import string
import random
print("welcome to the otp generator")
c = string.digits
d = string.ascii_letters
c = c+d
c = list(c)
random.shuffle(c)
e = random.randint(6,8)
l = random.choices(c,k = e)
l = ''.join(l)
print(f"Your one time passowrd is {l}")
