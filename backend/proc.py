import aiml
import pymorphy2

ERR_MSG = "Извините, я не понимаю ваш ответ. Можете повторить?"
RUS = ["РФ", "РОССИЯ", "РОССИЙСКИЙ ФЕДЕРАЦИЯ"]
ALLOWED = RUS + ["АРМЕНИЯ", "БЕЛАРУСЬ", "КАЗАХСТАН", "КЫРГЫЗСТАН", 
           "УКРАИНА", "ДНР", "ДОНЕЦКИЙ НАРОДНЫЙ РЕСПУБЛИКА", "ЛНР", "ЛУГАНСКИЙ НАРОДНЫЙ РЕСПУБЛИКА"]
TEST_QUESTIONS = ["1. Сколько вам лет?", "2. Гражданином какой страны вы являетесь?", 
                  "3. На какой территории вы планируете осуществлять деятельность?"]

morph = pymorphy2.MorphAnalyzer()

def detect_country(str):
    
    if str in ALLOWED:
        return 'TRUE'
    return 'FALSE'

def detect_age(str):

    age = int(str)

    if age >= 18:
        return process_input("мне 18 лет или больше")
    elif age < 18 and age >= 14:
        return process_input("мне от 14 до 18 лет")
    else:
        return process_input("мне меньше 14 лет")

def detect_territory(str):

    if str in RUS:
        return "РФ"
    else:
        return "ЗАГРАНИЦЕЙ"

def process_input(str):
    """
    приведение слов пользователя в начальную форму
    """

    res = ''
    tmp = str.split()

    for x in tmp:
        res += (morph.parse(x)[0].normal_form).upper() + ' '

    return res.strip()

def process_test(ans, user_input):
    """
    вопросы из теста про самозанятость требуют обработки (возраст и страны)
    """

    if TEST_QUESTIONS[0] in ans:
        user_input = detect_age(user_input)
    elif TEST_QUESTIONS[1] in ans:
        user_input = detect_country(user_input)
    elif TEST_QUESTIONS[2] in ans:
        user_input = detect_territory(user_input)

    return user_input

