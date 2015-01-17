# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import sympy as sp

# make things look pretty in the notebook
from sympy.interactive import printing
printing.init_printing()

%matplotlib inline

# <codecell>

a, d, q, r, L, pi1, pi2, piH, piL,c = sp.symbols('alpha delta q rho L pi_1 pi_2 pi_H pi_L c')

# <codecell>

# I'm defining risk aversion is 1-rho, with rho < 1.
# This simplifies the algebra.

u = lambda x: x**r

# <codecell>

u_a = lambda x: u(x*L*pi1 + (1-x)*L*pi2)


# Note that I'm manually factoring L and then implicitly
# setting the equation to zero and removing L (by setting it to 1).
# Solving this equation is a little tricky.

marginal_utility_L = u_a(a).diff(a).factor(L).subs(pi2,piL)
marginal_utility_H = u_a(a).diff(a).factor(L).subs(pi2,piH)
expected_marginal_util = (q*marginal_utility_L + (1-q)*marginal_utility_H).subs(L,1)

D = ((1 - q) * (piH - pi1)/(q * (pi1 - piL)))**(1 / (1 - r))
solution = (piH - D * piL)/(D * (pi1 - piL) + (piH - pi1))

# <codecell>

parameters = {q:.3, pi1:1, piL:0, piH:2}

# Recall that low rho represents high risk aversion.
sp.plot(solution.subs(parameters), (r, .01, .99))

# <codecell>


