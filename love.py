#
# Take a weighted graph representing a social network where the weight
# between two nodes is the "love" between them.  In this "feel the
# love of a path" problem, we want to find the best path from node `i`
# and node `j` where the score for a path is the maximum love of an
# edge on this path. If there is no path from `i` to `j` return
# `None`.  The returned path doesn't need to be simple, ie it can
# contain cycles or repeated vertices.
#
# Devise and implement an algorithm for this problem.
#
import operator
def feel_the_love(G, i, j):
    for node,neighbors in G.iteritems():
        #neighbors = values.values()
        #print max(stats.iterkeys(), key=(lamda key: stats[key]))
        try:
            print max(neighbors.iteritems(), key=operator.itemgetter(1))
        except:
            pass

        #for n in neighbors

G = {'a':{'c':1},
     'b':{'c':1},
     'c':{'a':1, 'b':1, 'e':1, 'd':1},
     'e':{'c':1, 'd':2},
     'd':{'e':2, 'c':1},
     'f':{}}
feel_the_love(G, 'a','b')

'''def score_of_path(G, path):
    max_love = -float('inf')
    for n1, n2 in zip(path[:-1], path[1:]):
        love = G[n1][n2]
        if love > max_love:
            max_love = love
    return max_love


G = {'a':{'c':1},
     'b':{'c':1},
     'c':{'a':1, 'b':1, 'e':1, 'd':1},
     'e':{'c':1, 'd':2},
     'd':{'e':2, 'c':1},
     'f':{}}
path = feel_the_love(G, 'a', 'b')
assert score_of_path(G, path) == 2

path = feel_the_love(G, 'a', 'f')
assert path == None'''