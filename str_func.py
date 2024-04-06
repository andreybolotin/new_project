new_word = input("Введите слово: ")


def word(new_word):
    """Принимает строку и возвращает его
    со всеми заглавными буквами"""
    new_word = new_word.upper()
    return new_word


print(word(new_word))

new_words = input("Введите слово: ")


def words(new_words):
    """Принимает строку и возвращает
    с первыми заглавными буквами"""
    new_words = new_words.capitalize()
    return new_words


print(words(new_words))
