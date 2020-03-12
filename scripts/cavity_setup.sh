#!/bin/bash

MERLIN_INFO=$1
HEIGHT=$2
WIDTH=$3
RESOLUTION=$4

docker create -ti --name temp-container cfdengine/openfoam bash
docker cp temp-container:/opt/openfoam6/tutorials/incompressible/icoFoam/cavity/cavity $MERLIN_INFO/
docker rm -f temp-container

cd $MERLIN_INFO/cavity

echo "***** Setting Up Mesh *****"
python $MERLIN_INFO/scripts/mesh_param_script.py -scripts_dir $MERLIN_INFO/scripts/ -y $HEIGHT -x $WIDTH -r $RESOLUTION
mv blockMeshDict.txt system/blockMeshDict

echo "***** Setting Control Dictionary *****"
sed -i '' "30s/.*/writeControl    runTime;/" system/controlDict
sed -i '' "26s/.*/endTime         10;/" system/controlDict
sed -i '' "32s/.*/writeInterval   1;/" system/controlDict
