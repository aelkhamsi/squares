# Problem
Given a set S of n points in the plane, how many subsets of four points that form the vertices of a square does it contain ? Both the axis-parallel case and the arbitrarily oriented case are studied.
For example: 
* [-1,-1][2,1][4,-2][1,-4] is a valid square.
* [0, 0][0, 2][2, 0][2, 2] is a valid square.

# Solution
The following algorithm propose a solution to this problem. We will proceed as follow:
1.  Create a Hash Table and insert all the points in it.
2.  For every pair of points a & b, search in the Hash Table whether the other points forming the vertices of any of the two squares defined by the vertice (a,b) are existing.  
