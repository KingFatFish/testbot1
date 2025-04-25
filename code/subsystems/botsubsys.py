import wpilib
import phoenix6
import commands2
from constants import ELEC

class TestBotSubsystemClass(commands2.Subsystem):
    def __init__(self) -> None:
        self.testmotor = phoenix6.hardware.TalonFX(ELEC.test_motor_CAN_ID)
        
    def motorrun(self):
        self.testmotor.set(ELEC.motor_speed)

    def motorstop(self):
        self.testmotor.set(0)