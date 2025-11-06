from settings import GERNAL_SETTINGS


def c_print(*args):
    if GERNAL_SETTINGS.get('IS_DEVELOPEMENT'):
        for matter in args:
            print(matter, end=" ")
        print()
