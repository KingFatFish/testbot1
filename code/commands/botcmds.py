import wpilib
import commands2
from subsystems.botsubsys import TestBotSubsystemClass
import logging
logger = logging.getLogger("testmotorsubsyslogger")
from wpilib import XboxController
import phoenix6

class testmotorstuff(commands2.Command):
    def __init__(self, botsubsys: TestBotSubsystemClass) -> None:
        self.addRequirements(botsubsys)
        self.motorsub = botsubsys
        self.controller = XboxController(1)

    def initialize(self):
        logger.info(" test motor run command initialized")

    def execute(self):
        if self.controller.getAButton():
            self.motorsub.motorrun()
        else:
            self.motorsub.motorstop()
        logger.info("yes")

    def isFinished(self):
        return False
    
    def end(self, interrupted):
        self.motorsub.motorstop()

class MotorStop(commands2.Command):
    def __init__(self, botsubsys: TestBotSubsystemClass) -> None:
        self.motorsub = botsubsys

    def initialize(self):
        logger.info("motor stop initialized")

    def execute(self):
        self.motorsub.motorstop()
        logger.info("stoppppping")

    def isFinished(self):
        return False
    
    def end(self, interrupted):
        self.motorsub.motorstop()
        