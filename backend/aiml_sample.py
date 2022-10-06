from proc import *

def main():

    kernel = aiml.Kernel()
    kernel.learn("std-startup.xml")
    kernel.respond("load aiml b")

    input_memory = []

    ans = ''
    user_input = 'START'

    while(1):

        user_input = process_test(ans, user_input)     #обработка вопросов 1-3 из теста
        ans = kernel.respond(user_input)

        # --- обработка неправильного ввода --- #

        if ans == ERR_MSG:

            print(ERR_MSG)

            for x in input_memory:
                ans = kernel.respond(x)

        else:
            input_memory.append(user_input)


        print(ans)
        user_input = process_input(input())           #обработка пользовательского ввода



if __name__ == '__main__':
    main()

