#!/bin/bash

MERLIN_PATH=$1
SPECROOT=$2

docker create -ti --name temp-container cfdengine/openfoam bash
docker cp temp-container:/opt/openfoam6/tutorials/incompressible/icoFoam/cavity/cavity .
docker rm -f temp-container

cd cavity

echo "***** Setting Up Mesh *****"
$MERLIN_PATH/python $SPECROOT/scripts/mesh-param-script.py -scripts_dir $SPECROOT/scripts/
mv blockMeshDict.txt system/blockMeshDict
sed -i '' "30s/.*/writeControl    runTime;/" system/controlDict
sed -i '' "26s/.*/endTime         10;/" system/controlDict
sed -i '' "32s/.*/writeInterval   1;/" system/controlDict
