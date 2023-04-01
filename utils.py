from chain import MarkovChain1D
import matplotlib.pyplot as plt
plt.style.use("dark_background")


def walk(n_steps, start_state, p, recurrent_states):
    """Generates the walk along the Markov Chain.

    Args:
        n_steps (int): The number of steps to walk for (which, in our case, also corresponds to the number of states)
        start_state (int): Which state to start from
        p (float32): The probability of moving to the right (that of moving to the left is thus 1 - p)
        recurrent_states (set): The recurrent states

    Returns:
        tuple: A single walk and a boolean, representing whether we ended up in a recurrent state or not
    """
    mc = MarkovChain1D(
        n_steps, start_state, p, recurrent_states=recurrent_states)
    return mc.walk()


def plot_walks(walks, title):
    """Plots the various walks

    Args:
        walks (list): The matrix containing all the walks (together with booleans representing whether they ended in a recurrent state or not)
    """

    row_data = [walk[0] for walk in walks]

    # Set the plot title and axis labels
    plt.xlabel("time")
    plt.ylabel("states")
    plt.title(title)

    # Plot the rows using multi-colored lines
    for i, row in enumerate(row_data):
        color = plt.cm.jet(i / len(row_data) + 0.05)
        plt.plot(row, color=color, linewidth=0.5)

    plt.show()
