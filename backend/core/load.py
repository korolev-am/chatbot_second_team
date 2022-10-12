from core.proc import aiml


def loading() -> aiml.Kernel:
    kernel = aiml.Kernel()
    kernel.learn(r'.\core\basic_chat_developed.aiml')
    return kernel
