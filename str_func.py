new_word = input("Введите слово: ")


def word(new_word):
    """Принимает строку и возвращает ее 
    со всеми заглавными буквами"""
    new_word = new_word.upper()
    return new_word


print(word(new_word))
