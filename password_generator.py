import random
def password_generator(length):
    data = "qwertyuiopasdfgjklzxcvbnm1234567890[];',./!@#$%^&*()_+:<>?"
    password = "".join(random.sample(data, length))
    return 'your password: ', password



print(password_generator(7))
