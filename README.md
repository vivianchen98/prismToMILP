# ambiguousPref

1. Edit PRISM file "simple_map.prism" and export model files (tra, sta, lab, rew) using the command:  
`prism simple_map.prism -exportmodel .tra,sta,lab -exporttransrewards .rew`  
(You need to rename the rewards files to make sure it is in the format of simple_mapi.rew where i is the reward index)
---
2. Parse the model files into data structures  
`python parse.py simple_map THRESHOLD_LOWER THRESHOLD_UPPER`  
where the last to parameters are the lower threshold and upper threshold
---
3. Compute bfs costs pre and post decision points  
`python bfs_decision.py`  
(it should generate two property files and one model file for each decision point)
---
4. Check the cost of pre and post decision point in properties  
`prism simple_map.prism pre-decision.props -exportresults pre-decisionLog.txt`  
`prism simple_map$i$.prism post-decision.props -exportresults post-decisionLog$i$.txt` (general case where i is the decision point number)
---
5. Generate lp formulation by  
`python generate-lp.py`
---
6. Go to https://online-optimizer.appspot.com/?model=builtin:empty.mod and copy the content in lp-output.txt  
Solve the model and view the result in variables section
