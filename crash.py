# TODO: Добавить проверку на пустой ввод
def hello_func(user_score, y):

    print("Привет, мир!")
    if user_score > y:
        return user_score
    else:
        return y


print(hello_func(5, 10))