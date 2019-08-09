import logging
import subprocess
from time import sleep

from manager.AWS import AWS


class Activity:
    def __init__(self, logger=logging):
        self.logger = logger
        self.aws = AWS(logger)

    def start_vm(self):
        self.logger.warning("Start VM")
        ip = self.aws.start()

        sleep(120)
        self.cmd_start_bot(ip)

        return ip

    def cmd_start_bot(self, ip):
        self.logger.warning("run start.sh on IP %s" % ip)
        return subprocess.Popen(["./start_vm.sh", ip])

    def get_running_ip_list(self):
        return list(map(lambda i: i.public_ip_address, self.aws.get_running_list()))
