from django.shortcuts import render
from .backend_aiml.aiml_sample import aiml_processing, aiml
from .load import loading
from .messages import Messages


messages = Messages()
flag = True
kernel = aiml.Kernel()

input_memory = []
answer = ''


def _button_pressed(messages, number):
    print("MESSAGE FROM BUTTON: ", messages.history_messages[-1]['buttons'][number - 1]['text'])
    print("id_current=", messages.history_id[-1], "answer=", number)
    global answer
    answer = aiml_processing(kernel, input_memory, messages.history_messages[-1]['buttons'][number - 1]['text'], ans=answer)
    messages.next_message(id_current=messages.history_id[-1], answer=number)


def frontpage(request):

    global flag
    global kernel
    if flag:
        kernel = loading(kernel)
        flag = False
    if request.method == 'POST':
        if '1' in request.POST:
            _button_pressed(messages, 1)
        elif '2' in request.POST:
            _button_pressed(messages, 2)
        elif '3' in request.POST:
            _button_pressed(messages, 3)
        elif '4' in request.POST:
            _button_pressed(messages, 4)
        elif '5' in request.POST:
            _button_pressed(messages, 5)
        elif '6' in request.POST:
            _button_pressed(messages, 6)
        elif 'content' in request.POST:
            text = request.POST['content']
            global answer
            answer = aiml_processing(kernel, input_memory, text, answer)
            id_message = int(answer.split(';')[0])
            messages.next_message_using_id_next(id_message)

    is_buttons = messages.history_messages[-1]["is_buttons"]
    is_field = int(messages.history_messages[-1]["is_field"])

    return render(request, "../templates/frontpage.html", {'messages': messages.history_messages,
                                                           'is_field': is_field,
                                                           'is_buttons': is_buttons,
                                                           'buttons': messages.history_messages[-1]["buttons"]})