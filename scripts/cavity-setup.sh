docker create -ti --name temp-container cfdengine/openfoam bash
docker cp temp-container:/opt/openfoam6/tutorials/incompressible/icoFoam/cavity/cavity .
docker rm -f temp-container

cd cavity

echo "***** Setting Up Mesh *****"
$1/python $2/scripts/mesh-param-script.py -scripts_dir $2/scripts/
mv blockMeshDict.txt system/blockMeshDict
sed -i '' "30s/.*/writeControl    runTime;/" system/controlDict
sed -i '' "26s/.*/endTime         10;/" system/controlDict
sed -i '' "32s/.*/writeInterval   1;/" system/controlDict
