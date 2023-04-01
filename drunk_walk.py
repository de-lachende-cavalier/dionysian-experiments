from chain import MarkovChain1D
from utils import plot_walks


def drunk_walk(n_steps, start_state, p, recurrent_states):
    mc = MarkovChain1D(n_steps, start_state, p, recurrent_states=recurrent_states)
    return mc.walk()


p = 1 / 3
recurrent_states = {0, 300}  # the home is at state 300, the lake at step 0
start_state = 100
n_steps = 3000

walks = [drunk_walk(n_steps, start_state, p, recurrent_states) for _ in range(100)]

plot_walks(walks, p)
