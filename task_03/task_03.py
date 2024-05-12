import timeit



# Реалізація алгоритму Бойера-Мура
def boyer_moore(text, pattern):
    def bad_character_table(pattern):
        table = {}
        for i in range(len(pattern) - 1):
            table[pattern[i]] = len(pattern) - 1 - i
        return table

    def good_suffix_table(pattern):
        table = [0] * len(pattern)
        last_prefix_position = len(pattern)
        for i in range(len(pattern) - 1, -1, -1):
            if is_prefix(pattern, i + 1):
                last_prefix_position = i + 1
            table[len(pattern) - 1 - i] = last_prefix_position - i + len(pattern) - 1
        for i in range(len(pattern) - 1):
            suffix_len = suffix_length(pattern, i)
            if pattern[i - suffix_len] != pattern[len(pattern) - 1 - suffix_len]:
                table[suffix_len] = len(pattern) - 1 - i + suffix_len
        return table

    def is_prefix(pattern, p):
        j = 0
        for i in range(p, len(pattern)):
            if pattern[i] != pattern[j]:
                return False
            j += 1
        return True

    def suffix_length(pattern, p):
        length = 0
        i = p
        j = len(pattern) - 1
        while i >= 0 and pattern[i] == pattern[j]:
            length += 1
            i -= 1
            j -= 1
        return length

    if len(pattern) == 0:
        return 0

    bc_table = bad_character_table(pattern)
    gs_table = good_suffix_table(pattern)
    i = 0

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            return i
        else:
            bad_character_skip = bc_table.get(text[i + j], len(pattern))
            good_suffix_skip = gs_table[len(pattern) - 1 - j]
            i += max(bad_character_skip, good_suffix_skip)

    return -1  # Підрядок не знайдено




# Алгоритм Кнута-Морріса-Пратта
def kmp(text, pattern):
    def compute_prefix_function(pattern):
        m = len(pattern)
        pi = [0] * m
        k = 0
        for q in range(1, m):
            while k > 0 and pattern[k] != pattern[q]:
                k = pi[k - 1]
            if pattern[k] == pattern[q]:
                k += 1
            pi[q] = k
        return pi

    n = len(text)
    m = len(pattern)
    pi = compute_prefix_function(pattern)
    q = 0
    indices = []
    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]
        if pattern[q] == text[i]:
            q += 1
        if q == m:
            indices.append(i - m + 1)
            q = pi[q - 1]
    return indices


# Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern):
    def rabin_hash(s):
        h = 0
        for char in s:
            h = (h * 256 + ord(char)) % 101
        return h

    n = len(text)
    m = len(pattern)
    pattern_hash = rabin_hash(pattern)
    text_hash = rabin_hash(text[:m])
    indices = []
    for i in range(n - m + 1):
        if text_hash == pattern_hash and text[i:i + m] == pattern:
            indices.append(i)
        if i < n - m:
            text_hash = (256 * (text_hash - ord(text[i]) * (256 ** (m - 1))) + ord(text[i + m])) % 101
    return indices

# Вибір відомих та вигаданих підрядків
real_pattern1 = "Двійковий або логарифмічний пошук"    # існуючий підрядок
fake_pattern1 = "qwerty"
real_pattern2 = "Бінарні діаграми рішень"
fake_pattern2 = "Qwetry123"

# неіснуючий підрядок

# Зчитування текстових файлів
with open("text_01.txt", "r", encoding="utf-8") as file:
    article1_text = file.read()

    


with open("text_01.txt", "r", encoding="utf-8") as file:
    article2_text = file.read()


# Вимірювання часу виконання для кожного алгоритму з реальним підрядком
print("TEXT 1")
print("Реальний підрядок")
print("Час виконання алгоритму Бойера-Мура для статті 1:", timeit.timeit(lambda: boyer_moore(article1_text, real_pattern1), number=1000))
print("Час виконання алгоритму Кнута-Морріса-Пратта для статті 1:", timeit.timeit(lambda: kmp(article1_text, real_pattern1), number=1000))
print("Час виконання алгоритму Рабіна-Карпа для статті 1:", timeit.timeit(lambda: rabin_karp(article1_text, real_pattern1), number=1000))

print("Неіснуючий підрядок")
print("Час виконання алгоритму Бойера-Мура для статті 1 з вигаданим підрядком:", timeit.timeit(lambda: boyer_moore(article1_text, fake_pattern1), number=1000))
print("Час виконання алгоритму Кнута-Морріса-Пратта для статті 1 з вигаданим підрядком:", timeit.timeit(lambda: kmp(article1_text, fake_pattern1), number=1000))
print("Час виконання алгоритму Рабіна-Карпа для статті 1 з вигаданим підрядком:", timeit.timeit(lambda: rabin_karp(article1_text, fake_pattern1), number=1000))

print("TEXT 2")
print("Реальний підрядок")
print("Час виконання алгоритму Бойера-Мура для статті 2:", timeit.timeit(lambda: boyer_moore(article2_text, real_pattern2), number=1000))
print("Час виконання алгоритму Кнута-Морріса-Пратта для статті 2:", timeit.timeit(lambda: kmp(article2_text, real_pattern2), number=1000))
print("Час виконання алгоритму Рабіна-Карпа для статті 2:", timeit.timeit(lambda: rabin_karp(article2_text, real_pattern2), number=1000))

print("Неіснуючий підрядок")
print("Час виконання алгоритму Бойера-Мура для статті 2 з вигаданим підрядком:", timeit.timeit(lambda: boyer_moore(article2_text, fake_pattern2), number=1000))
print("Час виконання алгоритму Кнута-Морріса-Пратта для статті 2 з вигаданим підрядком:", timeit.timeit(lambda: kmp(article2_text, fake_pattern2), number=1000))
print("Час виконання алгоритму Рабіна-Карпа для статті 2 з вигаданим підрядком:", timeit.timeit(lambda: rabin_karp(article2_text, fake_pattern2), number=1000))



print("Порівняння: ")

if timeit.timeit(lambda: boyer_moore(article1_text, real_pattern1), number=1000) < timeit.timeit(lambda: kmp(article1_text, real_pattern1), number=1000):
    print('Boyer-Moore швидший в пошуку реального підрядка у першій статті')
elif timeit.timeit(lambda: rabin_karp(article1_text, real_pattern1), number=1000) < timeit.timeit(lambda: kmp(article1_text, real_pattern1), number=1000):
    print('RabinKarp швидший в пошуку реального підрядка у першій статті')
else:
    print('KMP швидший в пошуку реального підрядка у першій статті')


if timeit.timeit(lambda: boyer_moore(article1_text, fake_pattern1), number=1000) < timeit.timeit(lambda: kmp(article1_text, fake_pattern1), number=1000):
    print('Boyer-Moore швидший в пошуку неіснуючого підрядка у першій статті')
elif timeit.timeit(lambda: rabin_karp(article1_text, fake_pattern1), number=1000) < timeit.timeit(lambda: kmp(article1_text, fake_pattern1), number=1000):
    print('Rabin-Karp швидший в пошуку неіснуючого підрядка у першій статті')
else:
    print('KMP швидший в пошуку неіснуючого підрядка у першій статті')


if timeit.timeit(lambda: boyer_moore(article2_text, real_pattern2), number=1000) < timeit.timeit(lambda: rabin_karp(article2_text, real_pattern2), number=1000):
    print('Boyer-Moore швидший в пошуку реального підрядка у другій статті')
elif timeit.timeit(lambda: rabin_karp(article2_text, real_pattern2), number=1000) < timeit.timeit(lambda: kmp(article2_text, real_pattern2), number=1000):
    print('RabinKarp швидший в пошуку реального підрядка у другій статті')
else:
    print('KMP швидший в пошуку реального підрядка у другій статті')


if timeit.timeit(lambda: boyer_moore(article2_text, fake_pattern2), number=1000) < timeit.timeit(lambda: kmp(article2_text, fake_pattern2), number=1000):
    print('Boyer-Moore швидший в пошуку неіснуючого підрядка у другій статті')
elif timeit.timeit(lambda: rabin_karp(article2_text, fake_pattern2), number=1000) < timeit.timeit(lambda: kmp(article2_text, fake_pattern2), number=1000):
    print('Rabin-Karp швидший в пошуку неіснуючого підрядка у другій статті')
else:
    print('KMP швидший в пошуку неіснуючого підрядка у другій статті')







