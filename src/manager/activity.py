import logging
import subprocess
from time import sleep

from manager.AWS import AWS


class Activity:
    def __init__(self, logger=logging):
        self.logger = logger
        self.aws = AWS(logger)

    def start_vm(self, width=1920, height=1080):
        self.logger.warning("Start VM")
        ip = self.aws.start()

        sleep(120)
        self.cmd_start_bot(ip, width, height)

        return ip

    def cmd_start_bot(self, ip, width=1920, height=1080):
        self.logger.warning("run start_vm.sh on IP %s" % ip, width, height)
        return subprocess.Popen(["./start_vm.sh", ip, width, height])

    def get_running_ip_list(self):
        return list(map(lambda i: i.public_ip_address, self.aws.get_running_list()))
