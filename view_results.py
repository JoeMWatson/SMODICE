import pickle
import matplotlib.pyplot as plt

envs = ["halfcheetah"]

n_demos = [10]

n_seeds = 1

for env in envs:
    for nd in n_demos:
        for s in range(n_seeds):
            with open(f'{env}_{nd}_{s}.pkl', 'rb') as f:
                res = pickle.load(f)
            evals = [l['log']['eval'] for l in res]
            iter = [l['log']['iteration'] for l in res]
            print(res)
            fig, ax = plt.subplots()
            ax.plot(iter, evals)

plt.show()
