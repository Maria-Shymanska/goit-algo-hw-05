import timeit


# Реалізація алгоритму Бойера-Мура
def boyer_moore(text, pattern):
    pass  

def kmp(text, pattern):
    pass  # Реалізація алгоритму Кнута-Морріса-Пратта

def rabin_karp(text, pattern):
    pass  # Реалізація алгоритму Рабіна-Карпа

# Вибір відомих та вигаданих підрядків
real_pattern = ""
fake_pattern = "qwerty"

# Зчитування текстових файлів
with open('/task_03/text_01.txt', 'r', encoding='latin-1') as file:
    article1_text = file.read()

with open('/task_03/text_01.txt', 'r', encoding='latin-1') as file:
    article2_text = file.read()

# Вимірювання часу виконання для кожного алгоритму з реальним підрядком
print("Час виконання алгоритму Бойера-Мура для статті 1:", timeit.timeit(lambda: boyer_moore(article1_text, real_pattern), number=1000))
print("Час виконання алгоритму Кнута-Морріса-Пратта для статті 1:", timeit.timeit(lambda: kmp(article1_text, real_pattern), number=1000))
print("Час виконання алгоритму Рабіна-Карпа для статті 1:", timeit.timeit(lambda: rabin_karp(article1_text, real_pattern), number=1000))

print("Час виконання алгоритму Бойера-Мура для статті 2:", timeit.timeit(lambda: boyer_moore(article2_text, real_pattern), number=1000))
print("Час виконання алгоритму Кнута-Морріса-Пратта для статті 2:", timeit.timeit(lambda: kmp(article2_text, real_pattern), number=1000))
print("Час виконання алгоритму Рабіна-Карпа для статті 2:", timeit.timeit(lambda: rabin_karp(article2_text, real_pattern), number=1000))

# Вимірювання часу виконання для кожного алгоритму з вигаданим підрядком
print("Час виконання алгоритму Бойера-Мура для статті 1 з вигаданим підрядком:", timeit.timeit(lambda: boyer_moore(article1_text, fake_pattern), number=1000))
print("Час виконання алгоритму Кнута-Морріса-Пратта для статті 1 з вигаданим підрядком:", timeit.timeit(lambda: kmp(article1_text, fake_pattern), number=1000))
print("Час виконання алгоритму Рабіна-Карпа для статті 1 з вигаданим підрядком:", timeit.timeit(lambda: rabin_karp(article1_text, fake_pattern), number=1000))

print("Час виконання алгоритму Бойера-Мура для статті 2 з вигаданим підрядком:", timeit.timeit(lambda: boyer_moore(article2_text, fake_pattern), number=1000))
print("Час виконання алгоритму Кнута-Морріса-Пратта для статті 2 з вигаданим підрядком:", timeit.timeit(lambda: kmp(article2_text, fake_pattern), number=1000))
print("Час виконання алгоритму Рабіна-Карпа для статті 2 з вигаданим підрядком:", timeit.timeit(lambda: rabin_karp(article2_text, fake_pattern), number=1000))







with open('/task_03/text_01.txt', 'r', encoding='latin-1') as f:
    text1 = f.read()