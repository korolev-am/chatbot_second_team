import core.constansts as const
from aiml_sample import aiml_processing

def processing(data: str, kernel, inp_memory, ans: str='', is_empty: bool) -> dict:

    if not is_empty:
        id_current, is_user_msg, answer = data.split(sep=';', maxsplit=2)
        if not is_user_msg:
            ans, input_memory = aiml_processing(kernel, input_memory,
                                                answer, ans=ans)
            id_next = const.TRANSITION_MAP[id_current][answer]
        # self.history_id.append(id_next)
        # self.history_messages.append(MESSAGES[id_next])
        '''if len(MESSAGES[id_next]['buttons']) == 0:
            if id_next == 100:  # НЕ ПОНИМАЮ ОТВЕТА
                pass
            else:
                id_current = id_next
                id_next = TRANSITION_MAP[id_current][1]  # 1 так как раньше была 1 кнопка с id=1 "ДАЛЬШЕ" - в карте переходов
                self.history_id.append(id_next)
                self.history_messages.append(MESSAGES[id_next])'''
            return ans, input_memory, const.MESSAGES[id_next]
        else:
            ans, input_memory  = aiml_processing(kernel, input_memory, answer, ans)
            id_message = int(ans.split(';')[0])
        # self.history_id.append(id_next)
        # self.history_messages.append(MESSAGES[id_next])
        '''if len(MESSAGES[id_next]['buttons']) == 0:
            if id_next == 100:  # НЕ ПОНИМАЮ ОТВЕТА
                pass
            else:
                id_current = id_next
                id_next = TRANSITION_MAP[id_current][1]  # 1 так как раньше была 1 кнопка с id=1 "ДАЛЬШЕ" - в карте переходов
                self.history_id.append(id_next)
                self.history_messages.append(MESSAGES[id_next])'''
            return ans, input_memory, const.MESSAGES[id_message]
    else:
        id_current = data
        id_next = TRANSITION_MAP[id_current][1]
        return ans, input_memory, const.MESSAGES[id_next]

    
