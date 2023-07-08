#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Load the model and evaluate it.
"""
from keras import models, Sequential, callbacks, layers, activations, optimizers, losses, metrics
from keras.utils import to_categorical
from numpy import ndarray
from pandas import DataFrame


class ModelBestEvaluation:
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
    __output_categories: int
    tuner_directory: str
    tuner_best_model_result_directory: str

    def __init__(self, data: DataFrame, output_feature: str, model_path: str, output_categories: int):
        """
        Construction method.
        """
        self.__data = data
        self.__output_feature = output_feature
        self.__model_path = model_path
        self.__output_categories = output_categories

        self.__split_data()
        self.__best_model = models.load_model(self.__model_path)

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
        self.__data_set_y = to_categorical(self.__data_set_y, num_classes=self.__output_categories)
        print('self.__data_set_y:')
        print(self.__data_set_y)

    def evaluate(self):
        evaluation = self.__best_model.evaluate(
            self.__data_set_x,
            self.__data_set_y,
            verbose=2,
        )
        index: int
        metric_name: str
        for index, metric_name in enumerate(self.__best_model.metrics_names):
            print(f'{metric_name.replace("_", " ").capitalize()}: {evaluation[index]}')
