# running-simulation
Pre-reqs:
1. Docker
  a. openfoam
  b. redis
2. Merlin

Steps:
1. Set up a redis server using docker
2. Activate virtual environment with merlin in it
3. clone this repo
4. merlin run openfoam-study.yaml
5. merlin run-workers openfoam-study.yaml
