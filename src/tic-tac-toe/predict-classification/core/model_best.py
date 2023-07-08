#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Load the model with the best training.
"""
from keras import models, Sequential, callbacks, layers, activations, optimizers, losses, metrics
from keras.utils import to_categorical
from numpy import ndarray
from pandas import DataFrame


class ModelBest:
    """
    Load the best model and evaluate it.
    """
    __data: DataFrame
    __data_set_x: DataFrame
    __data_set_y: ndarray
    __epochs: int
    __logs_path: str
    __model_path: str
    __best_model: Sequential
    __batch_size: int
    __units: int
    __layers: int
    __learning_rate: float
    __ams_grad: bool
    tuner_directory: str
    tuner_best_model_result_directory: str

    def __init__(self, data: DataFrame, model_path: str, output_feature: str, epochs: int,
                 batch_size: int, units: int, layers_model: int, learning_rate: float, ams_grad: bool,
                 tuner_directory: str = 'keras-tuner-trials',
                 ):
        """
        Construction method.
        """
        self.__data = data
        self.__logs_path = f'{tuner_directory}/logs-best-model'
        self.__model_path = model_path
        self.tuner_directory = tuner_directory
        self.tuner_best_model_result_directory = model_path
        self.__output_feature = output_feature
        self.__epochs = epochs
        self.__batch_size = batch_size
        self.__units = units
        self.__layers = layers_model
        self.__learning_rate = learning_rate
        self.__ams_grad = ams_grad

        self.__split_data()
        self.__generate_model()

    def __split_data(self) -> None:
        """
        Split the data for input and output features.

        :rtype: None
        """
        self.__data_set_x = self.__data.drop(columns=[self.__output_feature])
        print('self.__data_set_x:')
        print(self.__data_set_x)
        self.__data_set_y = self.__data[self.__output_feature].copy().to_numpy()
        print('self.__data_set_y:')
        print(self.__data_set_y)
        self.__data_set_y = to_categorical(self.__data_set_y)
        print('self.__data_set_y:')
        print(self.__data_set_y)

    def __generate_model(self):
        self.__best_model: Sequential = models.Sequential()

        # Input layer
        self.__best_model.add(layers.Dense(input_shape=self.__data_set_x.shape[1:],
                                           units=self.__units, activation=activations.relu))
        # Hidden layers
        for _ in range(self.__layers - 1):
            self.__best_model.add(layers.Dense(units=self.__units, activation=activations.relu))

        # Output layer
        self.__best_model.add(layers.Dense(self.__data_set_y.shape[1], activation=activations.softmax))

        self.__best_model.compile(
            optimizer=optimizers.Adam(
                learning_rate=self.__learning_rate,
                amsgrad=self.__ams_grad,
            ),
            loss=losses.CategoricalCrossentropy(),
            metrics=[
                metrics.Accuracy(),
                metrics.CategoricalAccuracy(),
                metrics.TopKCategoricalAccuracy(),
                metrics.CategoricalCrossentropy(),
                metrics.Precision(),
                metrics.CategoricalHinge(),
            ],
        )

        self.__best_model.summary()

    def fit(self):
        self.__best_model.fit(
            self.__data_set_x,
            self.__data_set_y,
            batch_size=self.__batch_size,
            epochs=self.__epochs,
            callbacks=[callbacks.TensorBoard(self.__logs_path,
                                             histogram_freq=1, write_images=True,
                                             embeddings_freq=1)],
        )

    def evaluate(self):
        evaluation = self.__best_model.evaluate(
            self.__data_set_x,
            self.__data_set_y,
            batch_size=self.__batch_size,
            verbose=2,
        )
        index: int
        metric_name: str
        for index, metric_name in enumerate(self.__best_model.metrics_names):
            print(f'{metric_name.replace("_", " ").capitalize()}: {evaluation[index]}')

    def save(self):
        print('=== Save ===')
        self.__best_model.save(self.__model_path)
