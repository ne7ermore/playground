states = ('Healthy', 'Fever')

observations = ('normal', 'cold', 'dizzy')

start_probability = {'Healthy': 0.6, 'Fever': 0.4}

transition_probability = {
    'Healthy': {'Healthy': 0.7, 'Fever': 0.3},
    'Fever': {'Healthy': 0.4, 'Fever': 0.6},
}

emission_probability = {
    'Healthy': {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
    'Fever': {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6},
}


def viterbi(obser):
    last_state = {state: emission_probability[state][obser[0]] *
                  start_probability[state] for state, pro in start_probability.items()}
    dp = [[None] * (len(obser)-1) for _ in range(2)]

    for day, ob in enumerate(obser[1:]):
        c_state = {}
        for index, cs in enumerate(states):
            res = []
            for ls in states:
                score = last_state[ls]*transition_probability[ls][cs] * \
                    emission_probability[cs][ob]
                res.append((ls, score))
            res.sort(key=lambda x: x[1])
            dp[day][index] = res[-1]
            c_state[cs] = res[-1][1]
        last_state = c_state


if __name__ == "__main__":
    print(viterbi(observations))
