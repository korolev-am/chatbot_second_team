from core.proc import aiml


def loading() -> aiml.Kernel:
    kernel = aiml.Kernel()
    kernel.learn('std-startup.xml')
    kernel.respond('LOAD AIML B')
    return kernel
