"""
Here This is a mini project where i create a AUTOMATIC PASSWORD GENERATOR.........
That is really too strong and that is too tough to crack..............
So, Lets start this project...........

"""

import string
import random

if __name__ == "__main__":
    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.punctuation)

    # print(help(string))

    s = []

    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)

    # print(len(s))

    # random.shuffle(s)

    # print("".join(s[:10]))

    passlen = int(input("Enter the length of your password (>=8) : "))

    if passlen < 8:
        print('''\tYour password length is too small.
        Its easy to crack by any Cracker..
        So, I will create a 8 letters password for you
        I hope you dont gonna crazy on me''')
        print("".join(random.sample(s, 8)))
    elif passlen > 94:
        print(f"Where to use {passlen} letters password LOL")
        print(f"If you really want to create a password of {passlen} letters then Enter")
        typed_string = input("")
        x = passlen // 94
        y = passlen % 94
        print(("".join(random.sample(s, 94))) * x + ("".join(random.sample(s, y))))
    else:
        print("Yup! Good choice..!!")
        print("".join(random.sample(s, passlen)))

# "".join(random.sample(s,94))

