# Cache Simulator 
* This is a simulator for the Replacement Algorithm for cache memory using the Least Recently Used Replacement Algorithm with Block Set Associative mapping.
  * This simulator can support sequential iterations but it cannot support sequentials with inner loops.
  * The Cache Snapshot presented in the WebApp is only the last iteration of the process. 
    *The previous iterations can be found on a downloadable text file that will be available after calculation.

## CSARCH S11 GROUP 8 Members:
* Ang, Gwyneth
* Badulis, Keith
* Joya, Patrick Jaspher
* Lua, Matthew Walden

## Application Deployment
* http://csarch2cachesimulator.herokuapp.com/

## Input
* Cache Access Time (in nanoseconds)
* Memory Access Time (in nanoseconds)
* Set Size
* Blocks per set
* Block Sequence
* Number of Sequence Iterations

## Output
* Load Through Time (in nanoseconds)
* Non-Load Through Time (in nanoseconds)
* Average Time (in nanoseconds)
* Hits
* Misses
* Hit Rate
* Miss Penalty
* Cache Snapshot
