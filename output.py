class colors:
    INFO = '\33[36M'
    OK = '\033[92m'
    FOUND = '\033[32m'
    NOTFOUND = '\033[31m'
    ERROR = '\033[91m'
    END = '\033[0m'


def status(str, element, status):
    text = f"{str} : {element}"
    match status.replace(" ", "").split():
        case 'info':
            print(colors.INFO + text + colors.END)
        case 'ok':
            print(colors.OK + text + colors.END)
        case 'found':
            print(colors.FOUND + text + colors.END)
        case 'notfound':
            print(colors.NOTFOUND + text + colors.END)
        case 'error':
            print(colors.ERROR + text + colors.END)

        case _:
            print(text)
