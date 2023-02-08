import utils.bcolors as BC


def printerr(message):
    print(BC.BColors.WARNING.value + str(message) + BC.BColors.ENDC.value)

def printsucces(message):
    print(BC.BColors.OKGREEN.value + str(message) + BC.BColors.ENDC.value)

def printinfo(message):
    print(BC.BColors.OKBLUE.value + str(message) + BC.BColors.ENDC.value)

def printcriterr(message):
    print(BC.BColors.FAIL.value + str(message) + BC.BColors.ENDC.value)

def printbold(message):
    print(BC.BColors.BOLD.value + str(message) + BC.BColors.ENDC.value)

def printunder(message):
    print(BC.BColors.UNDERLINE.value + str(message) + BC.BColors.ENDC.value)