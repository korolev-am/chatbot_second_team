from core.proc import aiml
import platform

def loading() -> aiml.Kernel:
    kernel = aiml.Kernel()
    if platform.system() == 'Linux':
        kernel.learn('./core/basic_chat_developed.aiml')
    elif platform.system() == 'Windows':
        kernel.learn(r'.\core\basic_chat_developed.aiml')
    return kernel
