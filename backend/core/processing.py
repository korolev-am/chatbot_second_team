import core.constants as const
from core.aiml_sample import aiml_processing

def processing(data: str, kernel, input_memory, is_empty: bool, ans: str='') -> dict:

    if not is_empty:
        id_current, is_user_msg, answer = data.split(sep=';', maxsplit=2)
        id_current = int(id_current)
        is_user_msg = int(is_user_msg)
        if not is_user_msg:
            print(id_current, int(answer))
            number = const.MESSAGES[id_current]['buttons'][int(answer)-1]['text']
            ans, input_memory = aiml_processing(kernel, input_memory,
                                                number, ans=ans)
            id_next = const.TRANSITION_MAP[id_current][int(answer)]
            return ans, input_memory, const.MESSAGES[id_next]
        else:
            ans, input_memory  = aiml_processing(kernel, input_memory, answer, ans)
            id_message = int(ans.split(';')[0])

            return ans, input_memory, const.MESSAGES[id_message]
    else:
        id_current = int(data)
        id_next = const.TRANSITION_MAP[id_current][1]
        return ans, input_memory, const.MESSAGES[id_next]
