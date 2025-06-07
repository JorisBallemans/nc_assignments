# Natural Computing 24/25
This repository contains all code made for the assignments and project of the course Natural Computing at Radboud University.

# Project: Reciprocity in Cooperation
Cooperation is an important concept for many aspects of life that has been studied extensively before. Think about cooperation between humans for interactions between individuals and group work, interactions between animals or interactions between companies. Direct reciprocity is based on the idea that individuals are more likely to cooperate if they can expect their beneficiaries to remember and to return their cooperative acts in future. With indirect reciprocity, you can build a reputation as a helpful individual, which can then lead to receiving more help from others.

The folder *project* in this repository contains code to simulate a population of agents, competing for food every generation. The files labeled '1_base_scenario.py' '2_direct_reciprocity.py' and '3_indirect_reciprocity.py' in this folder are the three main sections of this project, the other files are supporting code. 
Base_scenario simulates a baseline of cooperation that does not involve reciprocity. The other two files both simulate a form of reciprocity on top of the baseline.

## How to run
Each of the three files mentioned above can be run directly with any current python version (3.13 for example) and uses the following packages:
Pandas
Matplotlib
Scipy

The files can be run with the following parameters:
```
"-f",   "--food",   type=int, help = "Defines the count of food", default=100)
"-g",   "--greedy", type=int, help = "Defines the count of greedy agents", default=50)
"-c",   "--coop",   type=int, help = "Defines the count of cooperative agents", default=50)
"-ge",  "--gen",    type=int, help = "Defines the count of generations", default=200)
"-r",   "--runs",   type=int, help = "Defines the count of runs", default=0)
```

To run a baseline experiment with:
<ul>
  <li>10 food</li>
  <li>5 greedy starting agents</li>
  <li>5 cooperative starting agents</li>
  <li>50 averaged runs</li>
  <li>200 generations</li>
</ul> 
You can use the following command: <code>python3 1_base_scenario.py -f 10 -g 5 -c 5 -r 50 -ge 200</code>
