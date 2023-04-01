from utils import walk, plot_walks

p = 1 / 2
recurrent_states = {0}  # only recurrent state => the gambler looses everything
start_state = 10  # starts with 10€
n_steps = 3000

n_walks = 100
gambles = [walk(n_steps, start_state, p, recurrent_states)
           for _ in range(n_walks)]

title = f"gambler's ruin (p = {p:.3f})"
plot_walks(gambles, title)
