from settings import IS_DEVELOPEMENT_MODE
def c_print(*args):
    if IS_DEVELOPEMENT_MODE:
        for matter in args:
            print(matter, end=" ")
        print()
    