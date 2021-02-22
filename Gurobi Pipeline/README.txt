1. Download and place all files in the bin folder of your Prism files. This
should be the same folder with the prism executable file.

2. Open the evaluationBatch.txt files and input wanted model parameters as indicated
in the file for your batch.

3. Navigate to the correct folder using the terminal and execute the following
command: python3 scaleMap.py

4. The following files will be created:
      scaled_file.prism: The prism file of the map scaled to N rows and N columns
      scaled_file.lab/.sta/.tra/.rew: The exported model files
      resultsLog.txt: The results of the executed prism properties
      out_combined.lp: Holds the generated MILP file
      out_combined.sol: Hold the generated MILP solution
      output_file.txt: Holds the collected statistics for each model

5. Open output_file.txt to collect needed data.
