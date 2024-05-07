# -*- coding: utf-8 -*-

from time import sleep

from multiprocessing import Process

from config import API_HOST, API_PORT
from api import app
import _thread


class Scheduler:
    """调度器，程序运行逻辑实现"""

    def schedule_api(self):
        print("Start api server")
        app.run(API_HOST, API_PORT)

    def run(self):
        print('Start main function')

        api_process = Process(target=self.schedule_api)
        api_process.start()


if __name__ == '__main__':
    scheduler = Scheduler()
    scheduler.run()
