from .constants import MESSAGES, TRANSITION_MAP


class Messages:

    history_id = []  # храним только id сообщений
    history_messages = []  # храним сообщения

    def __init__(self):
        self.history_id.append(1)
        self.history_messages.append(MESSAGES[1])

    def next_message(self, id_current: int, answer: int):
        id_next = TRANSITION_MAP[id_current][answer]
        self.history_id.append(id_next)
        self.history_messages.append(MESSAGES[id_next])
        if len(MESSAGES[id_next]['buttons']) == 0:
            if id_next == 100:  # НЕ ПОНИМАЮ ОТВЕТА
                pass
            else:
                id_current = id_next
                id_next = TRANSITION_MAP[id_current][1]  # 1 так как раньше была 1 кнопка с id=1 "ДАЛЬШЕ" - в карте переходов
                self.history_id.append(id_next)
                self.history_messages.append(MESSAGES[id_next])

    def next_message_using_id_next(self, id_next: int):
        self.history_id.append(id_next)
        self.history_messages.append(MESSAGES[id_next])
        if len(MESSAGES[id_next]['buttons']) == 0:
            if id_next == 100:  # НЕ ПОНИМАЮ ОТВЕТА
                pass
            else:
                id_current = id_next
                id_next = TRANSITION_MAP[id_current][1]  # 1 так как раньше была 1 кнопка с id=1 "ДАЛЬШЕ" - в карте переходов
                self.history_id.append(id_next)
                self.history_messages.append(MESSAGES[id_next])
