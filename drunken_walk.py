from utils import walk, plot_walks

p = 2 / 3
recurrent_states = {0, 300}  # the home is at state 300, the lake at step 0
start_state = 100
n_steps = 3000

n_walks = 100
drunken_walks = [walk(n_steps, start_state, p, recurrent_states)
                 for _ in range(n_walks)]


title = f"drunken walks (p = {p:.3f})"
plot_walks(drunken_walks, title)
