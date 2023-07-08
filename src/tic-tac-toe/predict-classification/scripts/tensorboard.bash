#!/usr/bin/env bash

tensorboard --port 6006 --load_fast false --logdir 'keras-tuner-trials/logs-search'
tensorboard --port 6007 --load_fast false --logdir 'keras-tuner-trials/logs-fit'
tensorboard --port 6008 --load_fast false --logdir 'keras-tuner-trials/logs-evaluate-production'

# tail -n +1 tic-tac-toe-records-02.csv > tic-tac-toe-records-production-all.csv
# tail -n +2 tic-tac-toe-records-03.csv >> tic-tac-toe-records-production-all.csv

# ./venv/bin/tensorboard --port 6006 --load_fast false --logdir 'keras-tuner-trials/logs-search'
# ./venv/bin/tensorboard --port 6007 --load_fast false --logdir 'keras-tuner-trials/logs-fit'
# ./venv/bin/tensorboard --port 6008 --load_fast false --logdir 'keras-tuner-trials/logs-best-model'
