import logging
from manager.AWS import AWS


class Activity:
    def __init__(self, logger=logging):
        self.logger = logger
        self.aws = AWS(logger)

    def start_vm(self):
        self.logger.warning("Start VM")
        return self.aws.start()
