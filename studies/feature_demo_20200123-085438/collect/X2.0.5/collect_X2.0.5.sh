#!/bin/bash

echo */*/
echo /Users/mubarka1/march-tutorial/studies/feature_demo_20200123-085438/hello
ls /Users/mubarka1/march-tutorial/studies/feature_demo_20200123-085438/hello/X2.0.5/*/*//hello_world_output_*.json > files_to_collect.txt
python /Users/mubarka1/march-tutorial/feature_demo/scripts/collector.py -outfile results.json -instring "$(cat files_to_collect.txt)"

