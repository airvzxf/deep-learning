#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Scalable hyperparameter optimization to search the best parameters for the model.
"""
from os.path import isdir
from shutil import rmtree

from keras import Sequential, callbacks
from keras import activations
from keras import losses
from keras import metrics
from keras import layers
from keras import optimizers
from keras_tuner import HyperModel, Hyperband, Objective, HyperParameters, HyperParameter
from numpy import ndarray
from pandas import DataFrame

from core.split_data import SplitData


class GeneralHyperModel(HyperModel):
    __output_layer_units: int

    def __init__(self, output_layer_units: int):
        super().__init__()
        self.__output_layer_units = output_layer_units

    def build(self, hp: HyperParameters) -> Sequential:
        # Total of combinations = 3*3*2*2 = 36
        hp.Choice('batch_size', values=[64, 128, 512])
        hp_units: int = hp.Choice('units', values=[256, 512, 1024])
        hp_layers: int = hp.Choice('layers', values=[4, 16])
        learning_rate = [1e-03, 1e-04]
        hp_learning_rate: float = hp.Choice('learning_rate', values=learning_rate)
        # hp_amsgrad: bool = hp.Boolean('amsgrad')

        # Total of combinations = 1*1*1*3*2 = 6
        # hp.Choice('batch_size', values=[256])
        # hp_units: int = hp.Choice('units', values=[64])
        # hp_layers: int = hp.Choice('layers', values=[4])
        # learning_rate = [1e-02, 1e-03, 1e-04]
        # hp_learning_rate: float = hp.Choice('learning_rate', values=learning_rate)
        # hp_amsgrad: bool = hp.Boolean('amsgrad')

        model: Sequential = Sequential()
        # Input layer and Hidden layers
        for _ in range(hp_layers):
            model.add(layers.Dense(units=hp_units, activation=activations.relu))
        # Output layer
        model.add(layers.Dense(self.__output_layer_units, activation=activations.softmax))

        model.compile(
            optimizer=optimizers.Adam(
                learning_rate=hp_learning_rate,
                # amsgrad=hp_amsgrad,
            ),
            loss=losses.CategoricalCrossentropy(),
            metrics=[
                metrics.Accuracy(),
                metrics.CategoricalAccuracy(),
                # metrics.TopKCategoricalAccuracy(),
                metrics.CategoricalCrossentropy(),
                # metrics.KLDivergence(),
                # metrics.Poisson(),
                # metrics.MeanSquaredError(),
                # metrics.RootMeanSquaredError(),
                # metrics.MeanAbsoluteError(),
                # metrics.MeanAbsolutePercentageError(),
                # metrics.MeanSquaredLogarithmicError(),
                # metrics.CosineSimilarity(),
                # metrics.LogCoshError(),
                metrics.Precision(),
                # metrics.AUC(),
                # metrics.Recall(),
                # metrics.TruePositives(),
                # metrics.TrueNegatives(),
                # metrics.FalsePositives(),
                # metrics.FalseNegatives(),
                # metrics.PrecisionAtRecall(recall=0.8),
                # metrics.SensitivityAtSpecificity(0.8),
                # metrics.SpecificityAtSensitivity(0.8),
                # metrics.Hinge(),
                # metrics.SquaredHinge(),
                # metrics.CategoricalHinge(),
            ],
        )

        return model

    def fit(self, hp: HyperParameters, model: Sequential, *args, **kwargs):
        batch_size = hp.get('batch_size')
        return model.fit(
            *args,
            batch_size=batch_size,
            **kwargs,
        )


class KerasTunerHyper:
    """
    Search the best parameters for the model.
    """
    __tuner: Hyperband
    __data: DataFrame
    __train_set_x: DataFrame
    __train_set_y: ndarray
    __validation_set_x: DataFrame
    __validation_set_y: ndarray
    __test_set_x: DataFrame
    __test_set_y: ndarray
    __train_size: float
    __max_epochs: int
    __output_feature: str
    tuner_directory: str
    tuner_best_model_result_directory: str

    def __init__(self, data: DataFrame, output_feature: str, fit_epochs: int = 40,
                 train_size: float = 0.98, tuner_directory: str = 'keras-tuner-trials') -> None:
        """
        Construction method.
        """
        self.__data = data
        self.__train_size = train_size
        self.__output_feature = output_feature
        self.__max_epochs = fit_epochs

        self.__split_data()

        self.tuner_directory = tuner_directory
        if isdir(self.tuner_directory):
            rmtree(self.tuner_directory)

    def __split_data(self) -> None:
        """
        Split the data for the training, validation and test.

        :rtype: None
        """
        split_data: SplitData = SplitData(self.__data, train_size=self.__train_size,
                                          output_feature=self.__output_feature,
                                          convert_output_to_category=True)
        self.__train_set_x, self.__train_set_y, \
            self.__validation_set_x, self.__validation_set_y, \
            self.__test_set_x, self.__test_set_y = split_data.get_data_split()

    def search(self):
        tuner_logs_search_directory: str = f'{self.tuner_directory}/logs-search'
        # max_collisions: int = self.__max_epochs * 10

        self.__tuner = Hyperband(
            GeneralHyperModel(
                output_layer_units=self.__train_set_y.shape[1]
            ),
            objective=[
                Objective('val_categorical_crossentropy', direction='min'),
                Objective('val_categorical_accuracy', direction='max'),
                # Objective('val_categorical_hinge', direction='min'),
                # Objective('val_top_k_categorical_accuracy', direction='max'),
                # Objective('val_precision', direction='max'),
            ],
            seed=42,
            overwrite=True,
            directory=self.tuner_directory,
            project_name='PredictClassification',
        )
        print(f'tuner.tuner_id: {self.__tuner.tuner_id}')

        self.__tuner.search(
            self.__train_set_x,
            self.__train_set_y,
            validation_data=(self.__validation_set_x, self.__validation_set_y),
            callbacks=[callbacks.TensorBoard(tuner_logs_search_directory,
                                             histogram_freq=1, write_images=True,
                                             embeddings_freq=1)],
        )

        print('--- --- --- --- --- --- --- --- --- --- --- --- --- --- ---')
        print('# Get the best results')
        bests_hp: list = self.__tuner.get_best_hyperparameters(num_trials=100000000)
        best_hp: HyperParameter
        for index, best_hp in enumerate(bests_hp):
            print(f'best_hp #{index}: {best_hp.values}')
        print('--- --- --- --- --- --- --- --- --- --- --- --- --- --- ---')
        self.__tuner.search_space_summary()
        print('--- --- --- --- --- --- --- --- --- --- --- --- --- --- ---')
        self.__tuner.results_summary()
        print('--- --- --- --- --- --- --- --- --- --- --- --- --- --- ---')
        print(f'tuner_id: {self.__tuner.tuner_id}')
        print(f'bests_hp: {len(bests_hp)}')
        print('--- --- --- --- --- --- --- --- --- --- --- --- --- --- ---')
