import collections
import random

import simpy

RANDOM_SEED = 42
TICKETS = 50
SIM_TIME = 120


def moviegoer(env, movie, num_tickets, theater):
    pass


def customer_arrivals(env, theater):
    pass


Theater = collections.namedtuple('Theater', 'counter, movies, available, sold_out, when_sold_out, num_renegers')


print('Movie renege')
random.seed(RANDOM_SEED)
env = simpy.Environment()

# Create movie theater
counter = simpy.Resource(env, capacity=1)
movies = ['Python Unchained', 'Kill Process', 'Pulp Implementation']
available = {movie: TICKETS for movie in movies}
sold_out = {movie: env.event() for movie in movies}
when_sold_out = None
