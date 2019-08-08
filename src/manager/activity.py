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

    def cmd_start_bot(self, account, ip):
        self.logger.warning("run start.sh on IP %s" % ip)
        return subprocess.Popen(["./start.sh_vm", ip])

