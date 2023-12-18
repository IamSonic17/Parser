import schedule
import time
from main import launch_parser


def launch_sheduler():
    schedule.every().hour.do(launch_parser)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    launch_sheduler()
