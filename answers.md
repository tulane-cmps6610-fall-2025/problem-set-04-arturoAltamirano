# CMPS 6610 Problem Set 04
## Answers

**Name:** Arturo Altamirano


Place all written answers from `problemset-04.md` here for easier grading.




- **1d.**

File | Fixed-Length Coding | Huffman Coding | Huffman vs. Fixed-Length
----------------------------------------------------------------------
f1.txt    |                     |                |
alice29.txt    |                     |                |
asyoulik.txt    |                     |                |
grammar.lsp    |                     |                |
fields.c    |                     |                |




- **1d.**





- **2a.**

Using the provided hint, I will consider the following array of almost properly ordered elements A from 1 to 18.

Consider the following incomplete arrangement: 

1 ---> root node 

10 | 2 ---> second level 

14, 11 | 6, 3 ---> third level

15, 16, 12, 17 | 7, 8, 5, 4 ---> fourth level 

So our array of elements looks like this: [1, 10, 2, 14, 11, 6, 3, 15, 16, 12, 17, 7, 8, 5, 4]

Instead of digging through the class slides to find the textbook solution, I am willing to lose points on this question to experiment a datastructure idea I have:

Why don't we treat our whole tree as a list of listed lists? Our entire tree is one massive list, and each layer is represented by a list, and all of the child clusters of the prior layers nodes is their own list within this second list. 

I figure if we want linear runtime, why not structure this as a linear problem.

[] ---> our whole tree (first layer of encapsulation)

[[]] ---> our layer (second layer of encapsulation)

[[[]]] ---> our cluster(s) (third layer of encapsulation)

So our above diagram can be represented with: 

[[1], [[[10], [2]]], [[[14, 11], [6, 3]]], 

[[[15, 16], [12, 17], [7, 8], [5, 4]]]]

or, more intuitively: 

[
    [1], ----> root node
    
    [
        [

        [10], [2], ----> first layer

        ]
        
            [
                [14, 11], [6, 3] ----> second layer
            
            ], 

                [

                [15, 16], [12, 17], [7, 8], [5, 4] ----> third layer

                ]
    ]
]

For this example, we are looking to complete this structure with 



- **2b.**




- **3a.**

The currency is setup in this way because you can always scale to a smaller/larger denomination and perfectly fill the entirety of your 'knapsack' with 'interfacing' even values.

This enables a greedy algorithm to take the biggest denomination until it is no longer possible, then take the next biggest, and then the next biggest after that, until eventually the remaining void is filled perfectly or 'geometrically'. 

For every N dollars we want to fill this 'knapsack' type capacity with coins. Our first coin should be the largest possbile denomination they have, with the condition of being below N.

The following specification outlines this process:

    #at every recursion we want to check if we've filled the N value

    fun evaluator(0, []) = false
        evaluator (capacity, coin::rest) =
        | (coin = capacity) orelse evaluator (capacity - coin, rest);
    
    #this will determine if the next k value is in excess of our limit N 
    #will be driven from main to determine the max value to greedily select

    fun maximalEvaluator (coin, capacity) = (coin > capacity);

    fun coinSplit (N, k, []) = N, []
        let 
            fun insert (x, []) = [x]
               insert (x, y::ys) = 
               if x > y 
                    then x::y 
               else 
                    y :: insert (x, ys)
            
            fun sort [] = []
                sort(x::xs) = insert (x, sort)

        in 
            splitHelper(N, sortedCoins, [])

        end;

Basic outline assuming sample value of N = 100

1. Subproblem 1: N = 100 | 2<sup>6</sup> ---> 64

    For our first iteration we increment up from 2<sup>0</sup> until we reach a value that is in excess of our limit. This would be 2<sup>7</sup> so we decrement the exponent by 1 and take that value. 

    We evaluate if our value has been filled, and continue iterating since it is not.

2. Subroblem 2: N = 36 | 2<sup>5</sup> ---> 32

    At the next iteration we try to take our current denomination again, but we determine 2<sup>6</sup> is too large, so we evaluate and subsequently take 2<sup>5</sup>

    We evaluate if our value has been filled, and continue iterating since it is not.

3. Subproblem 3: N = 4 | 2<sup>2</sup> ---> 4

    Finally we try to take 2<sup>5</sup> again but determine it is too large, so we iteratively decrement and evaluate until we find 2<sup>2</sup> to perfectly fill our remaining space.

    We evaluate if our value has been filled, and stop our process since it has been.

- **3b.**
Greedy Property: Since these values all 'interface' perfectly with each other, there is only one ideal choice at a given state, and this will remain the ideal choice for all subsequent timesteps that derive from it.

For every possible member in the set of [2<sup>0</sup> ... 2<sup>k</sup>] we must have a largest and smaller value to choose from. This is because 2<sup>k</sup> must always be greater than 2<sup>k - 1</sup> and less than 2<sup>k + 1</sup>

In our base case of 0 or 1 for k, we are either given 1 or 2 itself, respectively. 

So, for our base case, the values of 1 or 2 will pass since they are valid positive integers. For our hypothesis we can state that for every value of k, there is a maximal value to be chosen, or a smaller value to choose if the maximal is not legal.

Optimal Substructure: At every given timestep, the optimal solution can be considered the solution which fill the largest amount of N without being illegal, since our requirement is to fullfill this requirement with the least amount of coins, we are essentially optimizing a series of subproblems until we find all of our coins.

Essentially, every given greedy choice fullfils the optimal substructure by maximizing the value of the selected coin with respect to N.

Also, according to the Bellman optimality, the value chosen at all subsequent time states is taken from the prior decisions in older time steps. That is, that given our N value (t) we solve our current state's problem (s) to eventually be left with our coins (T)

This is frequently used to uphold the presence of optimal substrucutre for a given problem, to my understanding.

Bellman optimality is a central theme in Reinforcement Learning, a class I am enrolled in this semester.

- **3c.**

work = O(log n)
span = O(n)



- **4a.**

This can be expressed as the 0-1 Knapsack problem. Since the currency is no longer flexible in it's divisibility. 

With the greedy algorithm, we blindly select the maximal value with no attention paid to future consequences. But now there is potential for the maximal choice to end up hurting us by nullifying a potentially better long term choice. 

    Say the denominations for a bank's coins are given by D = [95, 90, 10, 1] and we are trying to make change for N = 100 dollars.

Our greedy algorithm will take 95 off the bat as it is the maximal choice, but now it is left with only 1 as the remaining valid choice. 

    It will then be forced into picking 6 total coins: (95, 1, 1, 1, 1, 1)

    However, we can see intuitively that the optimal combination is 2 coins consisting of: (90 and 10)

- **4b.**

This problem does not have greedy property because simply choosing the maximal value is not guranteed to render the ideal solution, as exampled above. 

The fact that the values are no longer guaranteed to interface perfectly, means there may be suboptimal combinations that involve choices that are maximal at their respective selection timestep, but suboptimal over the whole episode. 

However, this problem still has optimal substructure property because at every given selection timestep, their has to be a value that we can select that is definitively ideal, we just have to employ a more nuanced approach to determine it.

Take our above example, and assume we are at timestep 1 ---> t<sub>1</sub>. We currently have a 90 cent coin in our pocket, and need to fill the remaining 10 cents of value. 

We determine we can either take the 10 cent coin, or the 1 cent coin. We do not care about any of the previous time steps, though our current state is a result of them. At this point, the 10 cent coin is clearly optimal according to our criterion of selecting the least amount of coins, but the 1 cent selection is still a valid choice that we can make, it is simply not optimal.

Essentially, at every timestep (t<sub>k</sub>) there is a value which is optimal with respect to our criterion, and our overall solution is nothing but a collection of timesteps and their respective valid solution sets, and the choices we make within them. 


- **4c.**

We want to memoize all previously seen values, and want to build from the bottom up since each timestep represents an individual subproblem that we want to continously build upon.

**SPECIFICATION NEEDED**


- **5a.**

Yes, because at each time step there is a solution which is optimal. By viewing the start times as our timesteps, we can 


- **5b.**

No it does not satisfy the greedy property.

Like minimizing the amount of coins I make change with, or maximizing the value of items I am stealing and putting in my sack, I viewed this as a knapsack style problem. Our goal is to maximize the amount of value we harvest, given a fixed amount of time and problems. If we did not assume our time to be limited, we could say that our time is unlimited, and simply do all problems sequentially to harvest all reward.

We can frame this as filling fixed amount of time, lets say N = 10 seconds and N - 1 = 9 tasks

There is also the issue of what are greedy criterion is, is it total time taken? Is it reward? I will assume this problem is called 'weighted selection' because we are supposed to use a weighting of time to reward as the criterion. 

We will use reward divided by total time as our criterion!

Counterexample 1: 
    
    Tasks = (0, 10, 15), (0, 1, 1), (1, 5, 12) ...

Right away we can see that at timestep 0, the greedy criterion will select the task which runs for the entire 10 second period (0, 10, 15) because it has the best per second weighted reward. Assuming that once we schedule a task we are locked into it and cannot interrupt the process, we will be stuck processing while a better task was never even evaluated.

Counterexample 2: 

We will take a different set of tasks:

            Chosen                             Chosen
    Tasks = (0, 1, 15), (0, 1, 1), (1, 5, 12), (1, 2, 9), (1, 9, 1), 
            
            Chosen    <------------> Chosen                 Missed!
            (2, 8, 7)   Processing   (8, 10, 7), (8, 9, 1), (9, 10, 50)

Only this time, we can see that the very last task (with massive reward of 50) in the sequence is missed because the prior chosen task runs to the end. Essentially blocking out the remaining potential for greater benefit.

Totally unrelated note: It would be interesting to make this a reinforcement learning problem, with value being reward, and overlapping start times incurring a penalty to encourage our agent to find it's own maximal way of scheduling.

- **5c.**

Similair to before, we want to memoize the currently running tasks, and want to build from the bottom up since each timestep represents an individual subproblem that we want to continously build upon.

**SPECIFICATION NEEDED**