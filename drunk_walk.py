from utils import walk, plot_walks

p = 1 / 3
recurrent_states = {0, 300}  # the home is at state 300, the lake at step 0
start_state = 100
n_steps = 3000

n_walks = 100
drunk_walks = [walk(n_steps, start_state, p, recurrent_states)
               for _ in range(n_walks)]

plot_walks(drunk_walks, p)
