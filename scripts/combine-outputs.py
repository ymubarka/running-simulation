import numpy as np
import glob
import Ofpp
import argparse

descript = """Using parameters to edit OpenFOAM parameters"""
parser = argparse.ArgumentParser(description=descript)

parser.add_argument('-data', '--data_dir', help='The home directory of the data directories')

args = parser.parse_args()

DATA_DIR = args.data_dir

dirs_array = open("out","r")
x = dirs_array.read()
x = x.split(' ')
x[-1] = x[-1][:-1]

dir_names = [DATA_DIR + '/' + xi + '/cavity' for xi in x]

num_of_timesteps = 10
vorticity = []
physical_times = []
U = []
enstrophy = []

for i, dir_name in enumerate(dir_names):
    for name in glob.glob(dir_name + '/[0-9]*/vorticity'):
        if name[-12:]== '/0/vorticity':
            continue
        physical_times.append(round(float(name.split('/')[-2]), 2))
        vorticity.append(Ofpp.parse_internal_field(name))


    for name in glob.glob(dir_name + '/[0-9]*/U'):
        if name[-4:]== '/0/U':
            continue
        U.append(Ofpp.parse_internal_field(name))

    for name in glob.glob(dir_name + '/[0-9]*/enstrophy'):
        if name[-12:]== '/0/enstrophy':
            continue
        enstrophy.append(Ofpp.parse_internal_field(name))

resolution = np.array(enstrophy).shape[-1]
U = np.array(U).reshape(len(dir_names), num_of_timesteps, resolution, 3)
vorticity = np.array(vorticity).reshape(len(dir_names), num_of_timesteps, resolution, 3)
enstrophy = np.array(enstrophy).reshape(len(dir_names), num_of_timesteps, resolution)/float(resolution)

np.savez('data.npz', U, vorticity, enstrophy)
