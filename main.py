import math, queue
from collections import Counter
from tabulate import tabulate

####### Problem 1 #######

class TreeNode(object):
    # we assume data is a tuple (frequency, character)
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
    def __lt__(self, other):
        return(self.data < other.data)
    def children(self):
        return((self.left, self.right))
    
def get_frequencies(fname):
    f=open(fname, 'r')
    C = Counter()
    for l in f.readlines():
        C.update(Counter(l))
    return(dict(C.most_common()))

# given a dictionary f mapping characters to frequencies, 
# create a prefix code tree using Huffman's algorithm
def make_huffman_tree(f):
    p = queue.PriorityQueue()
    # construct heap from frequencies, the initial items should be
    # the leaves of the final tree
    for c in f.keys():
        p.put(TreeNode(None,None,(f[c], c)))

    # greedily remove the two nodes x and y with lowest frequency,
    # create a new node z with x and y as children,
    # insert z into the priority queue (using an empty character "")
    while (p.qsize() > 1):
        #greedily remove x and y with lowest frequency

        #greedily remove x and y with lowest frequency
        x = p.get()
        y = p.get()

        #create a new node z with x and y as children
        z = TreeNode(left=x, right=y, data=(int(x.data[0] + y.data[0]), ""))

        #insert z into the priority queue (using an empty character "")
        p.put(z)

        
    # return root of the tree
    return p.get()

# perform a traversal on the prefix code tree to collect all encodings
def get_code(node, prefix="", code={}):
    #perform a tree traversal and collect encodings for leaves in code
    if node.left == None and node.right == None:
        char = node.data[1]
        code[char] = prefix

    #recursively visit the left and right subtrees, 
    #appending a 0 or 1 to the encoding in each direction asappropriate.
    else:
        if node.left:
           get_code(node.left, prefix + "0", code)

        if node.right:
            get_code(node.right, prefix + "1", code)

    return code

# given an alphabet and frequencies, compute the cost of a fixed length encoding
def fixed_length_cost(f):
    cost = 0.0

    for val in f.values():
        cost += float(val * math.ceil(math.log2(len(f))))

    return cost

# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):
    cost = 0.0

    for ch in f:
        cost += float(f[ch] * len(C[ch]))
    
    return cost

#f = get_frequencies('f1.txt')
#print("Fixed-length cost:  %d" % fixed_length_cost(f))
#T = make_huffman_tree(f)
#C = get_code(T)
#print("Huffman cost:  %d" % huffman_cost(C, f))

#custom built comparison - reused from HW2
def print_results(results):
    print("\n")
    print(tabulate(results,
            headers=['file', 'fixed cost', 'huffman cost', 'ratio'],
            floatfmt=".3f",
            tablefmt="github"))
    print("\n")

#call the preprovided driving code for a given file
def result_Generator(file):
    f = get_frequencies(str(file))
    T = make_huffman_tree(f)
    C = get_code(T)

    return fixed_length_cost(f), huffman_cost(C, f)

results = []
files = ['f1.txt', 'asyoulik.txt', 'alice29.txt', 'fields.c', 'grammar.lsp']

for file in files:
    fixed, huffman = result_Generator(file)
    ratio = huffman/fixed
    results.append((file, fixed, huffman, ratio))

print_results(results)


identicalResults = []
identicalFiles = ['identicalTest1.txt', 'identicalTest2.txt', 'identicalTest3.txt']

for file in identicalFiles:
    fixed, huffman = result_Generator(file)
    ratio = huffman/fixed
    identicalResults.append((file, fixed, huffman, ratio))

print_results(identicalResults)