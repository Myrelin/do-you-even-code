import os
arr = os.listdir("/home/myrelin/codecool/pet_projects/do-you-even-code/modules")

try:
    from modules import process_checker
    HAS_PROCESS_CHECKER = True
except ImportError:
    HAS_PROCESS_CHECKER = False


def main():
    while True:
        test = process_checker.ProcessChecker()
        test.start()


if __name__ == '__main__':
    main()
