1. Download and place all files in the bin folder of your Prism files. This
should be the same folder with the prism executable file.

2. Open the uav.prism file and place prism file inside. Open the uavproperties.pctl file to place wanted properties inside. The current files I was using are already set up inside.

3. The pipeline will call Prism from inside it. You can change the command it sends to prism by editing line 598 in scaleMapBenchmark.py. It is currently set up to run the file using the mac os commands. Also, I set the constraints inside of the prism file, but the could also be set here.

4. To change the number of objectives, the preferences (alphas), uncertainty (betas), or the c value, you can edit Lines 581 to 584 in scaleMapBenchmark.py. This is right under the start of the main function.

5. To change the destination states for the model and MILP, you can change the values under the function findDestState in
scaleMapBenchmark.py at line 530. The terminal states for the model need to be in the list destState. You can do this by changing the values in the for loops present or setting them manually. The current values are set up for my understanding of the terminal states for the uav files.

6. Navigate to the correct folder using the terminal and execute the following
command: python3 scaleMapBenchmark.py

7. The following files should be created if there is a solution present:
      uav.lab/.sta/.tra/.rew: The exported model files
      resultsLog.txt: The results of the executed prism properties
      out_combined.lp: Holds the generated MILP file
      out_combined.sol: Hold the generated MILP solution
      output_file.txt: Holds the collected statistics for each model

8. Open output_file.txt to collect needed data.
