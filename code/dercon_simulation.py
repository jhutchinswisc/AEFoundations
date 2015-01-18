"""Start with static Dercon '96 model and replicate outcomes.

   Create $n$ farmers with heterogeneous preferences and production
   parameters. Then simulate land allocations and outcomes associated with the
   empirical technology. Initially, let the technology and beliefs coincide.
   Outcomes from this simulation will generate data $(l_1,l_2,q_1,q_2,x)_i$.

   Technologies are production functions (I could introduce scale
   diseconomies) for each crop that relate the land allocation, $l_{ik}$,
   farmer characteristics, $x_i$, and the realization of uncertainty to a
   production outcome for each farmer.

   Assignment:

   1. Estimate a production function conditional on $x_i$ and $l_{ik}$.
   2. Estimate land-allocation decisions conditional on $x_i$ and $L_i$ using
      a behavioral model that assumes risk aversion. Students will probably
      estimate a linear relationship, but in principle they could use the
      moment condition from farmers' first-order condition to estimate $\rho$,
      and realized output to estimate dependence of $q_i$ on $x_i$ and $L_i$.
   3. Do you think you might be able to fit the data better with a more
      general model? Discuss.
   4. Assume that a benefactor from outside the economy offers each farmer an
      insurance contract with premium $p$ that covers all losses up to 75% of
      the realized mean yield across all farmers. 
   5. Can you predict the number of farmers who will buy this insurance? What
      degree of confidence can you put on your estimate? Assuming your
      predictions are acccurate, what kind of welfare gains will this program
      generate, and with what degree of confidence?
   6. Finally, what could go wrong with this program? Is it possible that,
      even with substantial uptake by farmers, that the program generates
      welfare losses.
      - Farmers have different beliefs. Education is a better intervention
        than insurance.
      - Farmers self-insure with neighbors and insurance crowds out this
        sharing.
	  - Adverse selection: insurance will select bad risks and be a lot more
        costly than we expected
	  - Moral hazard: insurance will change the distribution of returns!
	  - General equilibrium: insurance could move everyone into producing
        rice.
"""

class Farmer(land_endowment,preference_parm,productivity_parm):
	"""An individual who is risk averse and who chooses an allocation of his
	land across two possible crops. 

	Farmers are potentially heterogenous in their attitudes toward risk, and
	with respect to a single parameter that affects their productivity."""

	def utility():
		"""Bernoulli utility function"""
		pass

	def beliefs():
		"""Beliefs on the distribution of output."""
		pass

class DerconEconomy(Farmer):
	"""An economy represented by preferences, beliefs, and constraints for
	farmers who choose how much of their land to plant into safe and risky
	(but high-return) crops.

	Each farmer $i$ has a Bernoulli utility function $u_i(c)$ defined over
	consumption $c$, and chooses the fraction $\alpha$ of his total land $L$
	to allocate to crop $k$. Farmers have subjective beliefs, represented by
	the distribution function $F_{ik}(q)$, regarding returns on their land for
	each crop.
	""" 

	def technology():
		"""Actual empirical distribution over output for each farmer."""
		pass
	
	def land_allocation():
		"""Farmers optimize based on their beliefs."""
		pass

	def outcome():
		"""Outcome depends on empirical distribution and a farmer's action."""
		pass
