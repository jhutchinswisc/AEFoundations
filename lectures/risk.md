### Risk

Human beings have provided some form of insurance to one another for at least
as long as recorded time (e.g., @bogucki_wealth_2011, @clare_pastoral_2010,
@trenerry_origin_1926), and the modern world is full of institutional
arrangements that protect individuals against risk. One way way to derive
demand for these institutions from an economic model is to assume that
individuals are inherently *risk averse* in the sense that they are willing to
pay something now in return for a more certain outcome in the future. The
*expected utility* model is a simple representation for this sort of
preference. In it, we assume that individuals can rank choices that influence
the probability distribution over uncertain future payoffs $\pi$ by comparing
the expected value of an increasing state-independent concave utility function
$u(\pi)$ across choices.

Let's think about this with a few examples. To keep things simple, let's assume
initially that a farmer's preferences can be represented by a linear function
of the mean and variance of $\pi$. In particular, for $\alpha>0$ and $\beta>0$, let

$$\mathbb{E}u(\pi)= \alpha\mathbb{E}\pi - \beta\text{var}(\pi).$$

Further, suppose that $\pi = \overline{\pi}$ or $\pi = 0$ with probabilities
$p$ and $1-p$.

#### Exercises 

(@ex1) Demonstrate that a farmer with this utility function is willing to purchase
actuarially fair insurance (premium = expected indemnity).

(@ex2) Suppose there are two farmers, $A$ and $B$, with $\beta_A > \beta_B$.
Characterize optimal risk sharing between these two farmers.

Here's another exercise that relates to a pair of papers
 (@chibwana_cropland_2012 and @dercon_risk_1996) that you will read next week.

(@ex3) A farmer has $L$ total acres of land, and must choose the acreage $l_i$
to plant this year to each crop. Suppose that there is no risk in the first
crop; it has a certain return $\pi_1$. Crop 2 returns $\pi_2>\pi_1$ with
probability $p$ and zero otherwise. How much acreage should the farmer plant to
each crop?

(@ex4) Write a Python class called LandAllocation() that has "attributes" for
model parameters and "methods" for a) farmer utility (for now you can stick
with mean-variance preferences), b) the probability distribution of each crop
(you may assume there are just two crops as in the previous exercise.), c) the
farmers optimal acreage allocation, and e) a plot that summarizes some
comparative static that you find interesting. Ideally your methods will
accommodate many probability distributions.

(@ex5) Suppose the farmer is offered insurance that costs $P$ up front (the
premium) and reimburses up to 75% of the expected output for each crop (assume
that the farmer and the insurance company agree on the relevant distribution
for computing this expectation, and that it's the one from your model).
Exercise: What is the farmer's willingness to pay for this insurance? What is
the welfare gain from insurance? Is there a profit maximizing premium and
reimbursement rate for the insurance company?
