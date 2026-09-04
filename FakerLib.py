# Импортируем класс Faker из библиотеки
from faker import Faker

# Инициализируем генератор.
# Аргумент 'ru_RU' указывает, что данные должны быть на русском языке.
fake = Faker('ru_RU')

# Генерируем случайное имя и адрес
random_name = fake.name()
random_address = fake.address()

# Выводим результат в консоль
print("Генерация случайных данных:")
print(f"Имя:   {random_name}")
print(f"Адрес: {random_address}")