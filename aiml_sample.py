import aiml

ERR_MSG = "Извините, я не понимаю ваш ответ. Можете повторить?"
allowed = ["РФ", "РОССИЯ", "РОССИЙСКАЯ ФЕДЕРАЦИЯ", "АРМЕНИЯ", "БЕЛАРУСЬ", "КАЗАХСТАН", "КЫРГЫЗСТАН", 
           "УКРАИНА", "ДНР", "ДОНЕЦКАЯ НАРОДНАЯ РЕСПУБЛИКА", "ЛНР", "ЛУГАНСКАЯ НАРОДНАЯ РЕСПУБЛИКА"]

#print(kernel.respond("start"))

def detect_country(str):
    """
    Это нужно для обработки вопроса 2 (громоздко делается в aiml)
    """
    if str in allowed:
        return 'TRUE'
    return 'FALSE'


def main():

    kernel = aiml.Kernel()
    kernel.learn("std-startup.xml")
    kernel.respond("load aiml b")

    input_memory = []

    ans = ''
    user_input = 'START'

    while(1):

        if "2. Гражданином какой страны вы являетесь?" in ans:
            user_input = detect_country(user_input)
        
        ans = kernel.respond(user_input)

        # --- обработка неправильного ввода --- #

        if ans == ERR_MSG:

            print(ERR_MSG)

            for x in input_memory:
                ans = kernel.respond(x)

        else:
            input_memory.append(user_input)

        print(ans)
        user_input = input().upper()



if __name__ == '__main__':
    main()
