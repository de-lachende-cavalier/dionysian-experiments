import matplotlib.pyplot as plt


from chain import MarkovChain1D


def walk(n_steps, start_state, p, recurrent_states):
    mc = MarkovChain1D(
        n_steps, start_state, p, recurrent_states=recurrent_states)
    return mc.walk()


def plot_walks(walks, p):
    """Plots the various walks

    Args:
        walks (list): The matrix containing all the walks (together with booleans representing whether they ended in a recurrent state or not)
    """

    row_data = [walk[0] for walk in walks]

    # Set the plot title and axis labels
    plt.xlabel("time")
    plt.ylabel("states")
    plt.title(f"drunken walk (p = {p:.2f})")

    # Plot the rows using multi-colored lines
    for i, row in enumerate(row_data):
        color = plt.cm.jet(i / len(row_data) + 0.1)
        plt.plot(row, color=color)

    plt.show()
