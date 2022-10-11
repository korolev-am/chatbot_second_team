from core.proc import aiml


def loading() -> aiml.Kernel:
    kernel = aiml.Kernel()
    kernel.learn(r'C:\Users\Артём\Documents\Python Projects\chatbot_second_team\backend\core\basic_chat_developed.aiml')
    return kernel
