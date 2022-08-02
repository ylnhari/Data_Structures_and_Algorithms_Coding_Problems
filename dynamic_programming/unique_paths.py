"""Question : https://leetcode.com/problems/unique-paths
Final Approach : Recursively search through cells by going to down and right at each cell untill you reach edge of the destination cell, while remembering 
number of new paths possible at a particular cell so that it can be used multiple times at many places during recursive search (As many paths have same sub path) 
Thought Process/progression of the Approach
1) proceed towards right and down at each cell recursively, starting from the start  (every right, down direction taken is considered to be an entirely
new path), when a path reaches edge cell of the bottom side or right side of the grid add 1 (found new path) to a counter.
2) but this takes lot of recusions (since we at every cell we recursing to go towards doen, right -> we will have a binary tree of recusive functions with max depth
(length + breadth), we exceeded time limit
3) What if we memorize no of paths possible from a cell -> so we use dynamic programming techniques to memorize no of paths possible from a cell location
   -> From cells located on edges(bottom, right edge) no new paths are possible so their count is 1 by default
   -> now we start counting cells from which are adjacent to these cells and recursively get counts of cells adjacent to newly calculated cells 
   (Here counts are nothing byt no of more possible paths can be taken from a cell)
Approaches: partition at mid point and checking for peak --> partitions untill both start and end index meet
Time taken: time exceeded                                --> 47 ms
Memoryused: time exceeded                                --> 13.9 mb
"""
def uniquePaths_using_memoization(m, n):
    def find_paths_by_caching(x, y, cache_var):
        if cache_var[x][y] > 0:
            return cache_var[x][y]
        else: 
            cache_var[x][y] = find_paths_by_caching(x, y + 1, cache_var) + \
                              find_paths_by_caching(x + 1, y, cache_var)
            return cache_var[x][y]

    cache_var = [[0 for i in range(0,(n-1))] + [1] for j in range(0, m)] 
    cache_var[m-1] = [1 for i in range(0, n)]
    return find_paths_by_caching(0, 0, cache_var)
  
def uniquePaths_brute_force(m, n):
  def find_new_path_brute_force(x, y, m, n, counts):
    if x == n:
        counts[0] +=1
    elif y == m:
        counts[1] +=1
    else:
        if (x < n):
            find_new_path_brute_force(x + 1, y, m, n, counts)

        if (y < m):
            find_new_path_brute_force(x, y + 1, m, n, counts)


  counts = [0, 0]

  find_new_path_brute_force(1, 1, m, n, counts)

  return sum(counts)
