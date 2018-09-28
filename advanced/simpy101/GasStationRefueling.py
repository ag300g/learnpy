import itertools
import random

import simpy

RANDOM_SEED = 42
GAS_STATION_SIZE = 200
THRESHOLD = 10
FUEL_TANK_SIZE = 50
FUEL_TANK_LEVEL = [5, 25]
REFUELING_SPEED = 2
TANK_TRUCK_TIME = 300
T_INTER = [30, 300]
SIM_TIME = 1000


def car(name, env, gas_station, fuel_pump):

    fuel_tank_level = random.randint(*FUEL_TANK_LEVEL)
    print('%s arriving at gas station at %.1f' % (name, env.now))
    with gas_station.request() as req:
        start = env.now
        # Request one of the gas pumps
        yield req

        liters_required = FUEL_TANK_SIZE - fuel_tank_level
        yield fuel_pump.get(liters_required)

        yield env.timeout(liters_required / REFUELING_SPEED)

        print('%s finished refueling in %.1f seconds' % (name, env.now - start))


def gas_station_control(env, fuel_pump):
    while True:
        if fuel_pump.level / fuel_pump.capacity * 100 < THRESHOLD:
            print('Calling tank truck at %d' % env.now)
            yield env.process(tank_truck(env, fuel_pump))

        yield env.timeout(10)


def tank_truck(env, fuel_pump):
    yield env.timeout(TANK_TRUCK_TIME)
    print('Tank truck arriving at time %d' % env.now)
    ammount = fuel_pump.capacity - fuel_pump.level
    print('Tank truck refuelling %.1f liters.' % ammount)
    yield fuel_pump.put(ammount)


def car_generator(env, gas_station, fuel_pump):
    for i in itertools.count():
        yield env.timeout(random.randint(*T_INTER))
        env.process(car('Car %d' % i, env, gas_station, fuel_pump))


print('Gas Station refulling')
random.seed(RANDOM_SEED)

env = simpy.Environment()
gas_station = simpy.Resource(env, 2)
fuel_pump = simpy.Container(env, GAS_STATION_SIZE, init=GAS_STATION_SIZE)
env.process(gas_station_control(env, fuel_pump))
env.process(car_generator(env, gas_station, fuel_pump))

env.run(until=SIM_TIME)
