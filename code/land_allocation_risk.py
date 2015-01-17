# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import sympy as sp
import numpy as np

# make things look pretty in the notebook
from sympy.interactive import printing
printing.init_printing()

import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

# <codecell>

symbol_str = 'alpha delta q rho L R_1 R_2 R_H R_L c'
a, d, q, r, L, R1, R2, RH, RL, c = sp.symbols(symbol_str)

# <codecell>

# I'm defining risk aversion as 1-rho, with rho < 1.
# This simplifies the algebra.
u = lambda x: x**r

ex_post_return = a*L*R1 + (1-a)*L*R2

# Utility conditional on allocation decision x
u_a = lambda a: u(ex_post_return)


# Note that I'm manually factoring L and then implicitly
# setting the equation to zero and removing L (by setting it to 1).
# Solving this equation is a little tricky.

marginal_utility_L = u_a(a).diff(a).factor(L).subs(R2, RL)
marginal_utility_H = u_a(a).diff(a).factor(L).subs(R2, RH)
expected_marginal_util = (q * marginal_utility_L +
                          (1 - q)*marginal_utility_H).subs(L, 1)

# Interior solution assuming RL < R1 < RH
D = ((1 - q) * (RH - R1)/(q * (R1 - RL)))**(1 / (1 - r))
solution = (RH - D * RL)/(D * (R1 - RL) + (RH - R1))

# <codecell>

parameters = {'$q=.3, R_1=1, R_L=0, R_H=2$': {q: .3, R1: 1, RL: 0, RH: 2},
              '$q=.25$': {q: .25, R1: 1, RL: 0, RH: 2},
              '$q=.35$': {q: .35, R1: 1, RL: 0, RH: 2},
              '$R_1=.9$': {q: .3, R1: .9, RL: 0, RH: 2},
              '$R_1=1.1$': {q: .3, R1: 1.1, RL: 0, RH: 2}}


fig, ax = plt.subplots(figsize=(9, 6))
rho = np.linspace(0.05, .95, 100)

solution_scenario = {}
for scenario, parms in parameters.items():
    try:
        assert parms[R1] < parms[q] * parms[RL] + (1 - parms[q]) * parms[RH]
    except AssertionError:
        print(scenario)
    f = sp.lambdify(r, solution.subs(parameters[scenario]), "numpy")
    ax.plot(rho, f(rho), label=scenario)

ax.set_xlim(rho[0], rho[-1])
ax.set_xlabel(r'$\rho$', fontsize=16)
ax.set_ylabel('Percent planted to safe crop', fontsize=14)
ax.legend()
ax.set_title("Solution to static model in Dercon '96 EDCC",fontsize=14)

# Recall that low rho represents high risk aversion.

# Uncomment for sympy plotting. It's useful in pinch for quick graph,
# but not very pretty!

# p = sp.plot(solution_scenario['base'],
#             solution_scenario['low_q'],
#             solution_scenario['high_q'],
#             solution_scenario['low_R1'],
#             solution_scenario['high_R1'],
#             (r, .1, .9),xlabel=r'$\rho$',ylabel=r'$\alpha$',
#             xlim=(.1,.9),ylim=(0,1),axis_center=(0.1,0),
#             show=False,legend=False)

# p[0].line_color = 'b'
# p[1].line_color = 'g'
# p[2].line_color = 'r'
# p[3].line_color = 'm'
# p[4].line_color = 'c'
# p.show()


# <codecell>


