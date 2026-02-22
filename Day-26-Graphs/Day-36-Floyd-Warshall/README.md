# Day 36 - Floyd Warshall Algorithm

## Problem
Find shortest distance between all pairs of vertices.

## Algorithm
Floyd-Warshall (Dynamic Programming)

## Time Complexity
O(V^3)

## Space Complexity
O(V^2)

## Key Concept
Try every node as intermediate and update distance matrix.

## Negative Cycle Detection
If dist[i][i] < 0 → negative cycle exists