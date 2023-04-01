import numpy as np
import matplotlib.pyplot as plt
from functools import partial


class MarkovChain1D:
    def __init__(self, num_steps, start_state, p, recurrent_states=None):
        # assumes these are actual probabilities (checking done elsewhere)
        self.p = p
        self.num_steps = num_steps
        self.start_state = start_state
        self.recurrent_states = recurrent_states

    def walk(self):
        bernoulli = partial(np.random.binomial, 1, self.p)

        from_state = 0
        if self.start_state:
            from_state = self.start_state

        walk = [0 for _ in range(self.num_steps)]
        walk[0] = from_state
        for n in range(1, self.num_steps):
            x = bernoulli()
            walk[n] = (walk[n - 1] + 1) if x else (walk[n - 1] - 1)

            if self.recurrent_states is not None:
                if walk[n] in self.recurrent_states:
                    # we're in a recurrent state => we can't leave
                    return (np.trim_zeros(walk), True)

        return (walk, False)
