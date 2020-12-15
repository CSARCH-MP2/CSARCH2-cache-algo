# CSARCH2-cache-algo
This is a mini-library whose purpose is to automate and display the results of different cache algorithms.

## The following algorithms have been implemented to date:
1. LRU (Least Recently Used)
2. MRU (Most Recently Used)
3. Direct Mapping

## Usage:
1. cd cache_alg
2. python3 main.py < [input_file].txt
3. Optional: To see the output at each step, set debug=True


The input format for LRU, MRU, and DM is as follows:
[number of blocks]
[list of data]

ex: <br>
4 <br>
1 2 3 4 3 2 1 <br>

The output is a table showing the final cache snapshot.
