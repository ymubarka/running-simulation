import argparse
import sys
import numpy as np

def Round_n_sig_dig(x, n):
    xr = (np.floor(np.log10(np.abs(x)))).astype(int)
    xr = 10. ** xr * np.around(x / 10. ** xr, n - 1)
    return xr

def loguniform(low=-1, high=3, size=None, base=10):
    return np.power(base, np.random.uniform(low, high, size))

parser = argparse.ArgumentParser("Generate some samples!")
parser.add_argument("-n", help="number of samples", default=100, type=int)
parser.add_argument("-re", help="Reynold's number range (e.g. 1 1000)", nargs='+', type=int)
parser.add_argument("-U", help="Lidspeed range (e.g. 0.1 100)", nargs='+', type=float)
parser.add_argument(
    "-sample_type",
    help="type of sampling. options: random, grid. If grid, will try to get close to the correct number of samples",
    default="log_random")
parser.add_argument("-b", help="the base for log random sampling", default=10, type=int)
parser.add_argument("-outfile", help="name of output .npy file", default="samples")

args = parser.parse_args()

N_SAMPLES = args.n
SAMPLE_TYPE = args.sample_type
REYNOLD_RANGE = args.re
LIDSPEED_RANGE = args.U
BASE = args.b

if SAMPLE_TYPE == "log_random":
    x = np.empty((N_SAMPLES, 2))
    x[:,0] = loguniform(low = np.log10(LIDSPEED_RANGE[0]), high = np.log10(LIDSPEED_RANGE[1]), size = N_SAMPLES, base=BASE)
    vi_low = np.log10(x[:,0]/REYNOLD_RANGE[0])
    vi_high = np.log10(x[:,0]/REYNOLD_RANGE[1])
    x[:,1] = [loguniform(low = vi_low[i], high = vi_high[i], base=BASE) for i in range(N_SAMPLES)]

elif SAMPLE_TYPE == "random":
    x = np.empty((N_SAMPLES, 2))
    x[:,0] = np.random.uniform(LIDSPEED_RANGE[0], LIDSPEED_RANGE[1], size = N_SAMPLES)
    vi_low = np.log10(x[:,0]/REYNOLD_RANGE[1])
    vi_high = np.log10(x[:,0]/REYNOLD_RANGE[0])
    x[:,1] = [loguniform(low = vi_low[i], high = vi_high[i], base=BASE) for i in range(N_SAMPLES)]

elif SAMPLE_TYPE == "fixed":
    num_samples = 3
    viscosity = [0.002, 0.001, 0.0005]

    width = [10.0]
    lid_speed = [100]
    xp = [0.5]
    yp = [0.5]

    x = np.empty((num_samples, 5))
    x[:,0] = width * num_samples
    x[:,1] = xp * num_samples
    x[:,2] = yp * num_samples
    x[:,3] = lid_speed * num_samples
    x[:,4] = viscosity

np.save(args.outfile, x)
