1. Edit PRISM file and export model files (tra, sta, lab, rew) using the command:  
```prism simple_map_prob_new.prism -exportmodel .tra,sta,lab -exporttransrewards .rew```  
(You need to rename the rewards files to make sure it is in the format of simple_mapi.rew where i is the reward index)

2. Parse the model files into data structures  
```python parse.py simple_map_prob_new (ObjNum) {(lower threshold) (upper threshold) for each obj}```  
- ```python parse.py simple_map_prob_new 1 6 9``` (for single objective)   
- ```python parse.py simple_map_prob_new 2 6 9 0 6``` (for 2-objective)  
(please make sure the number of objectives correspond to the reward files from prism)

3. Generate lp formulation by  
```python generate-lp-new.py```

4. Go to https://online-optimizer.appspot.com/?model=builtin:empty.mod and copy the content in lp-output.txt
Solve the model and view the result in variables section
