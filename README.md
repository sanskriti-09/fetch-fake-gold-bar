**Fake Gold Bar Detection
**

This project implements an algorithm to detect a fake gold bar among a set of identical-looking gold bars using a balance scale. It also includes a test automation script to perform the 
detection process on a website simulator.

The algorithm utilizes a binary search strategy to minimize the number of weighings required to identify the fake gold bar. It divides the gold bars into two groups and compares their 
weights on the balance scale, eliminating one group based on the result. This process is repeated recursively until the fake gold bar is found.

The test automation script is written in Python using the Selenium library. It interacts with a website simulator where users can place gold bars on the scale and receive weighing results. 
The script performs the detection process described in the algorithm and outputs the results.


