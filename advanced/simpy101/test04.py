from random import seed, randint
import simpy

seed(23)


class EV:
    def __init__(self, env):
        self.env = env
        self.drive_proc = env.process(self.drive(env))
        self.bat_ctrl_proc = env.process(self.bat_ctrl(env))
        self.bat_ctrl_reactivate = env.event()

    def drive(self, env):
        while True:
            yield env.timeout(randint(20, 40))

            print('Start parking at', env.now)
            self.bat_ctrl_reactivate.succeed()
            self.bat_ctrl_reactivate = env.event()
            yield env.timeout(randint(60, 360))
            print('Stop parking at', env.now)

    def bat_ctrl(self, env):
        while True:
            print('Bat. ctrl. passivating at', env.now)
            yield self.bat_ctrl_reactivate
            print('Bat. ctrl. reactivated at', env.now)

            yield env.timeout(randint(30, 90))


env = simpy.Environment()
ev = EV(env)
env.run(until=150)
