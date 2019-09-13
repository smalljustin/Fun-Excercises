# Riddler Classic

Recent Riddlers have tackled Scrabble Superstrings and road trips through 48 states. For this week’s Riddler Classic, Max Maguire combines these two puzzles into one:

The challenge is to find the longest string of letters in which (1) every pair of consecutive letters is a two-letter state or territory abbreviation, and (2) no state abbreviation occurs more than once. For example, Guam, Utah and Texas can be combined into the valid four-letter string GUTX. Another valid string is ALAK (Alabama, Louisiana and Alaska), while ALAL (Alabama, Louisiana and Alabama) is invalid because it includes the same state, Alabama, twice.

For reference, the full list of abbreviations is available here, courtesy of the United States Postal Service.

# Solution:

The solution uses graph theory, and then an implementation of BFS to solve the final problem.

1. Initialize all abbreviations as a directed graph.
2. Implement BFS on this graph, solving
