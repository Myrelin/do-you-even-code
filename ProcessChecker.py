import psutil


def check_if_process_running(process_name):
    for proc in psutil.process_iter():
        try:
            if process_name.lower() in proc.name().lower():
                print("Process is running")
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    print("Process is not running")
    return False


# if check_if_process_running("idea.sh"):
#     print("Yes, intellij is running")
# else:
#     print("No, intellij is not running")
#
#
# if check_if_process_running("pycharm.sh"):
#     print("Yes, pycharm is running")
# else:
#     print("No, pycharm is not running")
#


