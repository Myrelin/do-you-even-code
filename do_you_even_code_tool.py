import logging
import time

logger = logging.getLogger('doyouevencode')
process_names = ["pycharm.sh", "idea.sh"]

try:
    from modules import process_checker
    HAS_PROCESS_CHECKER = True
except ImportError:
    HAS_PROCESS_CHECKER = False


def main():
    while True:
        if not HAS_PROCESS_CHECKER:
            logger.warning('Please make sure the process_checker is in the modules directory!')
        else:
            process_check = process_checker.ProcessChecker(process_names)
            process_check.update_sessions()
            process_check.close_sessions()
            time.sleep(5)


if __name__ == '__main__':
    main()
