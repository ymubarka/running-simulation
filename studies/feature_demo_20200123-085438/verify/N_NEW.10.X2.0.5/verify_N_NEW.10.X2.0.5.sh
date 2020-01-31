#!/bin/bash

if [[ -f /Users/mubarka1/march-tutorial/studies/feature_demo_20200123-085438/learn/X2.0.5/random_forest_reg.pkl && -f /Users/mubarka1/march-tutorial/studies/feature_demo_20200123-085438/predict/N_NEW.10.X2.0.5/prediction_10.npy ]]
then
    touch FINISHED
    exit 0
else
    exit 101
fi

