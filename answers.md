# CMPS 6610 Problem Set 04
## Answers

**Name:** Arturo Altamirano

Place all written answers from `problemset-04.md` here for easier grading.

- **1d.**

see main.py for the code to generate this:

| file         |   fixed cost |   huffman cost |   ratio |
|--------------|--------------|----------------|---------|
| f1.txt       |     1340.000 |        826.000 |   0.616 |
| asyoulik.txt |   876253.000 |     606448.000 |   0.692 |
| alice29.txt  |  1039367.000 |     676374.000 |   0.651 |
| fields.c     |    78050.000 |      56206.000 |   0.720 |
| grammar.lsp  |    26047.000 |      17356.000 |   0.666 |

Seems Huffman Coding incurs only 60-70% of the cost compared to fixed encoding.

- **1d.**

My presumption would be that Huffman does not improve the performance for this, since there are no frequencies to push to the top. There is simply nothing for the algorithm to do and as such we can expect it to be the same as fixed cost.

I created a few of my own files to test this, and it upheld this presumption. These files are located in the repository if you wish to view them.

see main.py for the code to generate this:

| file               |   fixed cost |   huffman cost |   ratio |
|--------------------|--------------|----------------|---------|
| identicalTest1.txt |      216.000 |        216.000 |   1.000 |
| identicalTest2.txt |     2216.000 |       2216.000 |   1.000 |
| identicalTest3.txt |      160.000 |        160.000 |   1.000 |

- **2a.**

Using the provided hint, I will consider the following array of almost properly ordered elements A from 1 to 11.

Useful to document that the heap property states that the children of any given parent node (and it's children's children) must be smaller (or in this case larger) than their parent. This naturally places the biggest (in this case smallest) node at the root.

Consider the following arrangement: 

1 ---> root node 

2 | 5 ---> second level 

3, 11 | 9, 12 ---> third level

So our array of elements looks like this: 
    [1, 2, 5, 3, 11, 9, 12] 

and we want to add the following 8 values to flush out another level: 
    [8, 99, 101, 32, 6, 10, 13, 14]

When we have an element we need to insert to the heap we must traverse the tree (represented as a list here) to find a slot to insert our value. 

In graph form:
 1) We would need to traverse likely using BFS, find which value in our first breadth sweep is a valid parent (must be smaller than current value)
 
 2) Then move down that vertex(continuing BFS) to the bottom, appending the candidate to the end.

 3) Continue this process, leveraging the fact that a node's child does not need to be strictly minimal in relation to their value distance. That is to say, that given a node with value 1, a node with value 47 is just as valid as node with value 9 as a child.

Note, if graph balance is desired, you could implement a type of cache to track the depth of your vertices, updating this with the amount of values you append to a given vertex so as to balance the distribution. 


- **2b.**

Span for BFS would be the width of the tree, for DFS it would be the height. You could say that depending on the approach you choose (both are valid) that you would want to carefully consider the amount of children each node has. 

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

**Explain**

span = O(n)

**Explain**


- **4a.**

This can be expressed as a maximization/minimization problem. Since the currency is no longer flexible in it's divisibility. 

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

We want to memoize all previously seen calculations and results, and want to build from the bottom up since each timestep represents an individual subproblem that we want to continously build upon.

We may do repeat calculations for this in the form of the sequences of values leading to a given timestep, and would benefit from saving them. 

I like Standard ML because the documentation from CMU on it is very extensive, but the syntax is very difficult, I have specified something using bottom up memoization:

fun coinCount (selectedCoins : int list, amount : int, cached : int) =
    let
        val memo = Array.array (amount + 1)

        fun opt amt =
            #if our index is not 0, then we need to check our memoization cache
            if amt != 0 then 

                #we want to access our table and see if this problem is in there
                let
                    cached = Array.sub(memo, amt) |

                in
                    #if our current cache index is found, return result member
                    if cached = cached.result

                    #if not cached, we can cache it for later
                    else 
                        let
                            #(amt - coin value)
                            fun try_each [] = len[]
                              | try_each (c::cs) =
                                    if c > a then try_each cs
                                    else Int.min(1 + opt(a - c), try_each cs)

                            val result = try_each coins
                            val arr = Array.update(memo, a, result)

                        in
                            result

                        end

            #if we're at 0, just return nothing, since no value has been incurred
            else
                0
    in
        val answer = coinCount(v, p);

    end

**Explanation 1,2,3...**

**Work and Span**


- **5a.**

Yes, because at each time step there is a solution which is optimal. By viewing the start times as our timesteps, we can form the following recurrence: 

OPT(i) = max(v(i) + OPT(p(i)),  OPT(i−1))

 1) OPT in this case indicated the maximum value that we can select for in the first i tasks. 

 2) max() is used to denote our desire to select the optimal solution at the given timestep, note that this is technically greedy, but our expression within the parenthesis will account for future opportunity.

 3) v(i) represents the value of the current candidate task 

 4) OPT(p(i)) represents the opportunity cost of all other candidates not being selected.

 5) OPT(i−1) is used to indicate the current total rewards acquired.

We can say that for any given series of events, there is potential for overlap that will interfere with us selecting a subsequent ideal value. Therefor if we remove any given selection from our hypothetical ideal series of selections and replaced it with a sub-optimal selection, it would destroy the rest of the sequence. 

Essentially, by defining the problem in this recurrence, we assert that any given task is not only optimal in the local sense when compared to it's other candidates, but on a global level for the whole sequence, since they are all dependent on one another. 

This condition acts as proof for the optimal substrucutre property. Since for any given solution, or even timestep within an incomplete solution, it cannot be optimal without all other prior selections being optimal. 

My reasoning for this was based on the recurrence for the knapsack problem, pertaining to capacity: 

v(OPT(n, Value)) = max{v(task) + v(OPT([n - 1], W - w(n))), v(OPT(n - 1), W)}

Only for this application, there is no more capacity metric, only the time element and the opportunity cost of potentially being stalled on a task.

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

Similair to before, but this time I do not feel memoization is neccesary, since the only thing you could potentially reuse is the runtime to value ratio. Which is a trivial calculation at worst, and adds too much complexity to the solution for what it gains in performance.

Also since each timestep has a different set of candidates, it is not feasible to reuse these calculations.

fun weighted_opt (v : int list, p : int list) =
    let
        val n = len(v)

        fun opt i =
            #if our index is not 0, then we need to check our memoization cache
            if i != 0 then 
                    else 
                        let
                            #OPT(i) = max
                            val vi = List.nth(v, i-1)
                            val pi = List.nth(p, i-1)

                            #(v(i) - OPT(p(i)))
                            val include = vi + opt(pi)

                            #OPT(i−1)
                            val exclude = opt(i-1)

                            val result = Int.max(include, exclude)
                            Array.update(memo, i, result)

                        in
                            result

                        end

            #if we're at 0, just return nothing, since no value has been incurred
            else
                0
    in
        val answer = weighted_opt(v, p);

    end

**Explanation 1,2,3...**

**Work and Span**