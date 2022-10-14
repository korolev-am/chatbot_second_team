from core.proc import *
import time

time.clock = time.time


def aiml_processing(kernel, inp_memory, inp: str=None, ans: str=''):

    user_input = process_input(inp)
    user_input = process_test(ans, user_input)     #обработка вопросов 1-3 из теста
    print("ANSWER BEFORE:", ans)
    print("USER INPUT:", user_input)

    ans = kernel.respond(user_input)
    print("ANSWER AFTER:", ans)

    # --- обработка неправильного ввода --- #

    if ans == ERR_MSG:

        for x in inp_memory:
            ans = kernel.respond(x)

        return '100;' + ERR_MSG + ans, inp_memory

    else:
        inp_memory.append(user_input)
        return ans, inp_memory
    
