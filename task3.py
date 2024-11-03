# TODO  Напишите функцию count_letters
def count_letters(text):
    dictionary_letters = dict()
    for sym in text:
        if sym.isalpha():
            sym = sym.lower()

            if sym in dictionary_letters:
                dictionary_letters[sym] += 1
            else:
                dictionary_letters[sym] = 1

    return dictionary_letters


# TODO Напишите функцию calculate_frequency
def calculate_frequency(dictionary, all_count):
    dictionary_frequency = {}
    for letter_dict in dictionary:
        count = dictionary.get(letter_dict)
        dictionary_frequency[letter_dict] = count / all_count
    return dictionary_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
dict_cnt_letters = count_letters(main_str)
count_all_letters = sum(dict_cnt_letters.values())

dict_result = calculate_frequency(dict_cnt_letters, count_all_letters)
for letter, frequency in dict_result.items():
    print(f"{letter}:{frequency: .2f}")
