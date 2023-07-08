# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Generate a CSV file with the information about the trials.
"""
from json import load
from os import listdir
from os.path import isdir


class CsvTrials:
    """
    Generate a CSV with the trials' information.
    """
    __tuner_path: str
    __trials_path: str
    __csv_path: str

    def __init__(self, tuner_path: str = 'keras-tuner-trials',
                 trials_path: str = 'keras-tuner-trials/PredictClassification/',
                 csv_path: str = 'keras-tuner-trials/trials-analysis.csv'):
        self.__tuner_path = tuner_path
        self.__trials_path = trials_path
        self.__csv_path = csv_path

    def generate(self):
        csv_headers = 'trial_id,batch_size,units,layers,learning_rate,amsgrad,best_epoch,score,' \
                      'accuracy,accuracy_epoch,' \
                      'crossentropy,crossentropy_epoch,' \
                      'accuracy_val,accuracy_val_epoch,' \
                      'crossentropy_val,crossentropy_val_epoch,' \
                      'epochs,initial_epoch,bracket,round,best_step,status\n'
        with open(self.__csv_path, 'w') as csv_file:
            csv_file.write(csv_headers)
            filenames = listdir(self.__trials_path)
            for filename in filenames:
                filename_path = self.__trials_path + filename
                if not isdir(filename_path):
                    continue

                if not filename.startswith('trial_'):
                    continue

                json_path = f'{filename_path}/trial.json'
                with open(json_path, 'rb') as file_handler:
                    json_data = load(file_handler)
                    trial_id = json_data.get('trial_id')
                    hyperparameter = json_data.get('hyperparameters')
                    values = hyperparameter.get('values')
                    batch_size = values.get('batch_size')
                    units = values.get('units')
                    layers = values.get('layers')
                    learning_rate = values.get('learning_rate')
                    ams_grad = values.get('amsgrad')
                    tuner_epochs = values.get('tuner/epochs')
                    tuner_initial_epoch = values.get('tuner/initial_epoch')
                    tuner_bracket = values.get('tuner/bracket')
                    tuner_round = values.get('tuner/round')
                    score = json_data.get('score')
                    metrics = json_data.get('metrics').get('metrics')
                    cat_accuracy = metrics.get('categorical_accuracy')
                    cat_accuracy_value = cat_accuracy.get('observations')[0].get('value')[0]
                    cat_accuracy_epoch = cat_accuracy.get('observations')[0].get('step') + 1
                    cat_cross_entropy = metrics.get('categorical_crossentropy')
                    cat_cross_entropy_value = cat_cross_entropy.get('observations')[0].get('value')[0]
                    cat_cross_entropy_epoch = cat_cross_entropy.get('observations')[0].get('step') + 1
                    cat_accuracy_val = metrics.get('val_categorical_accuracy')
                    cat_accuracy_val_value = cat_accuracy_val.get('observations')[0].get('value')[0]
                    cat_accuracy_val_epoch = cat_accuracy_val.get('observations')[0].get('step') + 1
                    cat_cross_entropy_val = metrics.get('val_categorical_crossentropy')
                    cat_cross_entropy_val_value = cat_cross_entropy_val.get('observations')[0].get('value')[0]
                    cat_cross_entropy_val_epoch = cat_cross_entropy_val.get('observations')[0].get('step') + 1
                    best_step = json_data.get('best_step')
                    status = json_data.get('status')

                    best_epoch = -1
                    if status != 'FAILED':
                        best_epoch = tuner_initial_epoch + best_step + 1

                    row = f'{trial_id},{batch_size},{units},{layers},{learning_rate},{ams_grad},' \
                          f'{best_epoch},{score},{cat_accuracy_value},{cat_accuracy_epoch},' \
                          f'{cat_cross_entropy_value},{cat_cross_entropy_epoch},' \
                          f'{cat_accuracy_val_value},{cat_accuracy_val_epoch},' \
                          f'{cat_cross_entropy_val_value},{cat_cross_entropy_val_epoch},' \
                          f'{tuner_epochs},{tuner_initial_epoch},{tuner_bracket},{tuner_round},' \
                          f'{best_step},{status}\n'
                    csv_file.write(row)
