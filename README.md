# Program to solve the problem of Non-Intersecting Billboard Selection

## Problem:
In a new tunnel, various products want to put up billboards to promote their products. You must give the appropriate permissions to place these fences and you do not want any of these to intersect with another (however, two fences can be next to each other, that is, share an end). Advertising proposals include the point where the fence will start (in meters, counting from the beginning of the tunnel) and its size (also in meters). None of these conditions are negotiable. The advertising departments of each of the interested products have come to the conclusion that they want the billboard at that exact point, with those exact dimensions or they prefer not to place any advertising. All
Fences will be placed flat on a single wall of the tunnel.<br>
Given n advertising requests, where the ith request has pi (the starting point of the fence) and ti (the size of the fence), design an efficient algorithm that allows choosing a maximal set of requests such that no fence intersects with other.
For example, consider that n = 3 and the requests are:<br>
- p1 = 1 and t1 = 4
- p2 = 2 and t2 = 1
- p3 = 3 and t3 = 3
  
<br>A maximal set would be {2, 3}, covering the ranges [2..3] and [3..6].<br>
Your algorithm must use O(n log n) time and O(n) extra memory.

## Requirements:
To run this program, you must have the following installed:
- Python

## How to install the project
Follow these steps to install the project:
1. **Clone the repository**: Clone the repository using the following git command:<br>
   ```git clone https://github.com/PanquecaFuriosa/Non-Intersecting_Billboard_Selection```

## How to run the project
Follow these steps to run the project:
1. **Run the following bash command**:<br>
   ```python main.py```
