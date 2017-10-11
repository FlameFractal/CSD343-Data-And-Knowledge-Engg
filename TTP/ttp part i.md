# Travelling Thief Problem (TTP) Report

### Problem Statement:

There is a thief who has to visit the given `n` cities in a rental car and pick up from total unique items  `m`, these are available in all the cities. The distance between each city is given in distance matrix `d`. The items have an associated profit of `p_k` and each item has weight `w_k`. Time taken to pick up an item depends on its weight. The rent `r` that the thief has to pay at the end of his heist for the car is proportional to the time taken. The maximum carrying capacity of the car is `W`. The car burns gasoline at a cost of `g`  per unit of distance travelled. Thief cannot visit a city more than once and cannot remain in a city for more than time `t_n` dependent on the probability of robbery conviction rates of that city `r_n`. Find out the path that the thief should take in order to maximise his profit and minimise the time taken to reach back to the original city.

 

### Assumptions:

- Each city has all the items
- He can pick same item from multiple cities
- Cannot visit a city more than once
- If knapsack is full, may come back to origin city




pi returns if he visited that edge

theta is quantity of items (multiple copies of same item can be picked from multiple cities)



### **Variables to optimise:**

- Total distance 
  $$
  D = \sum _{i=0,j=0}^{n,n} \pi(i,j) * d_{i,j}
  $$

- Total Profit
  $$
  P = \sum _{i=0}^{n} \theta(i) * d_{i} - R - G
  $$

- Total Time  

  i = `city travelling from `

  j =`city travelling to`
  $$
  T = \pi(i,j) * ( \sum_{i=0,j=0}^{n,n} d(i,j)/v(j) + \sum \theta(k)*t(k) )
  $$

  $$
  tmax(k,j) =  \sum \theta(k)*y(w_k) < prob(j)*n
  $$

  ​
  $$
  v(j) = v_{max} - ((v_{max}-v_{min})/W)*w(j)
  $$

- Car Rent
  $$
  R = T * r
  $$
  ​

- Gasoline = distance\*(constant\*weight)*time
  $$
  G = D*constant
  $$
  ​

- Weight 

  ​
  $$
  \sum w_k <= W 
  $$





### **Variables to input and their source:**

- distance matrix `D(i,j)` - randomly generated
- probability of getting caught by police per city `prob(j)` - randomly generated
- list of items and their profit (`p_k`), weight (`w_k`)
- car capacity - `W` 
- `vmin` `vmax` 



### Extra points discussed

- dynamic police risk
- road conditions (obstructions)
- multiple thieves (swarming)
- gasoline dependent on weight (mileage)
- different items in different cities








Group = Samarjoy, Saksham, Saurabh, Vishal
