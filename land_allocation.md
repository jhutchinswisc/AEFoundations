# Motivating question

Present development policy scenario (see De Falco paper). Let's think about what kinds of policy we might use in this setting, and what kind of analysis we could do to assess policy design.

# Uncertainty in economic analysis

- Discuss risk and uncertainty and how it complicates decision making.
- Discuss objective function, VN utility functions, and stochastic dominance.
- Discuss subtly in moving from VN utility to expected utility.
- Let's assume the farmer has VN utility $u$ and wants to maximize expected
  utility.

A farmer has $A$ units of land to allocate across $n$ crops. Net returns for each crop are uncertain and characterized by cummulative distribution functions, $F_i(y)$, for each crop. What's the first step to thinking about how the farmer *should* allocate her acres acros crops?

### Exercises

1. Characterize profit maximizing allocation analytically.
1. Characterize expected-utility maximizing allocation
1. Examine numerically FOSD and SOSD of distrubtions
1. Use distributions and utility function to compute range of profit maximizing
   and expected utility maximizing allocations
1. Exercise: What is the farmer's willingness to pay for insurance?

- Write code that is general and use test for simple analytic expressions to verify

### Simulation and estimation exercise

Generate allocation choices for sample of heterogenous farmers based on individual-specific beliefs and low-level risk-aversion. Generate outcome from policy experiment that offers insurance. Let students measure "impact" from insurance program. How much did it change land allocation? What is the welfare gain from insurance? How much should we spend to subsidize program, and how much are farmers willing to pay for insurance? We have no idea because we don't the utility functions or the distributions. Can we estimate these things? How does this differ relative to *predicting* allocations based on farmer characteristics. Let's give each farmer a characteristic. This will allow us to use fixed effect plus common regressor for prediction.

Economics gives us a model and lets us look at counterfactuals and welfare, but our model could be totally wrong and as a consequence give us bad advice. *But*, if we have a sensible model that makes good predictions, if someone thinks the model is wrong, the onus is on them to come up with a different model that explains the data better.

Two examples:

- Farmers have different beliefs. Education is a better intervention than
  insurance.
- Farmers self-insure with neighbors and insurance crowds out this sharing.
- Adverse selection: insurance will select bad risks and be a lot more costly
  than we expected
- Moral hazard: insurance will change the distribution of returns!

### Model

1. Farmer $i\in\{1,\ldots,n\}$ produces two crops, $k\in\{\text{corn,potatoes}\}$, each with a distribution function $F_{ki}(y|x_i)$, where $y$ is yield per acre, and $x_i$ are characteristics of the grower and his land.
2. Farmers have $L_i$ total acres of land that allocate to each of the crops.
3. Can we help the farmer make a choice about how many acres to plant to each crop.
4. Can we say antyhing about the choice without knowing the utility function of the farmer?
    - Answer: if we know that the farmer is risk averse, then FOSD or SOSD maybe enough, but those are very restrictive conditions. We're unlikely to find such an easy decision in the real world.
    - Here's the definition of FOSD. Let's draw a picture to see what these conditions mean. 
    
Draw FOSD and SOSD for couple specific distribution functions. You can see why
we don't need to know much about the utility function in this case (I think we
just need that it's increasing and concave).