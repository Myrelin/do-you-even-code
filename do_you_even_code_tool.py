import logging

logger = logging.getLogger('doyouevencode')

try:
    from modules import process_checker
    HAS_PROCESS_CHECKER = True
except ImportError:
    HAS_PROCESS_CHECKER = False

try:
    from modules import runtime_tracker
    HAS_RUNTIME_TRACKER = True
except ImportError:
    HAS_RUNTIME_TRACKER = False


def main():
    while True:
        if not HAS_PROCESS_CHECKER:
            logger.warning('Please make sure the process_checker is in the modules directory!')
        if not HAS_RUNTIME_TRACKER:
            logger.warning('Please make sure the runtime tracker is in the modules directory!')
        else:
            process_check = process_checker.ProcessChecker()
            process_check.start()
            print(process_check.running_processes)


if __name__ == '__main__':
    main()
