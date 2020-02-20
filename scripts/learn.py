from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
from joblib import dump, load
import argparse

descript = """Using parameters to edit OpenFOAM parameters"""
parser = argparse.ArgumentParser(description=descript)

parser.add_argument('-specroot', help='The DAG spec root')

args = parser.parse_args()

training_percent = 0.5
timestep = -1

SPECROOT = args.specroot
inputs_dir = SPECROOT + '/merlin_info'
outputs_dir = SPECROOT + '/combine-outputs'

outputs = np.load(outputs_dir + '/data.npz')
U = outputs['arr_0']
vorticity = outputs['arr_1']
enstrophy = outputs['arr_2']

energy_byhand = np.sum(np.sum(U**2, axis=3), axis=2)/ U.shape[2] /2
enstrophy_all = np.sum(enstrophy, axis=2)

X = np.load(inputs_dir + '/samples.npy')
y = np.concatenate((enstrophy_all[:, timestep].reshape(-1,1), energy_byhand[:, timestep].reshape(-1,1)), axis=1)
X[:,1] = np.log10(X[:,0]/X[:,1]) #np.log10(X)
y = np.log10(y)

training_size = int(training_percent * len(X))

X_train = X[:training_size]
y_train = y[:training_size]
X_test = X[training_size:]
y_test = y[training_size:]

regr = RandomForestRegressor(max_depth=10, random_state=0, n_estimators=7)

regr.fit(X_train, y_train)
print('training score:', regr.score(X_train, y_train))
print('testing score: ', regr.score(X_test, y_test))
print(mean_squared_error(y_test, regr.predict(X_test)))

dump(regr, 'trained-model.joblib')
