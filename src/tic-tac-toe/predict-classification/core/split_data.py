#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Split the data for the deep learning in three slices: training, validation and test.
"""
from numpy import ndarray
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from tensorflow.python.keras.utils.np_utils import to_categorical

from core.graphic_information import GraphicInformation


class SplitData:
    """
    Split data in three slices: training, validation and test.
    """
    __data: DataFrame
    __output_feature: str
    __convert_output_to_category: bool
    __train_set: DataFrame
    __train_set_x: DataFrame
    __train_set_y: ndarray
    __validation_set: DataFrame
    __validation_set_x: DataFrame
    __validation_set_y: ndarray
    __test_set: DataFrame
    __test_set_x: DataFrame
    __test_set_y: ndarray
    __train_size: float
    __random_state: int

    def __init__(self, data: DataFrame, output_feature: str, convert_output_to_category=False,
                 train_size: float = 0.98, random_state: int = 42) -> None:
        """
        Construction method.

        :type data: DataFrame
        :param data: Data frame with the data which will split.

        :type output_feature: str
        :param output_feature: The Column Name for the output feature.

        :type convert_output_to_category: bool
        :param convert_output_to_category: If true, it converts the output feature to category.

        :type train_size: float
        :param train_size: The size of the records for the train size.
        The remaining ones will be divided in two at 50%, some for validation and others for tests.

        :type random_state: int
        :param random_state: Generate the same results always. It keeps the same split in every iteration.
        If random is desired, set to `None` this parameter.

        :rtype: None
        """
        self.__data = data
        self.__output_feature = output_feature
        self.__train_size = train_size
        self.__random_state = random_state
        self.__convert_output_to_category = convert_output_to_category

    def get_data_split(self) -> tuple:
        """
        Return the split data for training, validation and test.

        :rtype: tuple[DataFrame, ndarray, DataFrame, ndarray, DataFrame, ndarray]
        :return: The data set for training for x and y, validation for x and y and test for x and y.
        """
        self.__train_set, remaining_set = train_test_split(self.__data,
                                                           train_size=self.__train_size,
                                                           random_state=self.__random_state)
        self.__validation_set, self.__test_set = train_test_split(remaining_set,
                                                                  test_size=0.5,
                                                                  random_state=self.__random_state)

        self.__train_set_y = self.__train_set[self.__output_feature].copy().to_numpy()
        self.__validation_set_y = self.__validation_set[self.__output_feature].copy().to_numpy()
        self.__test_set_y = self.__test_set[self.__output_feature].copy().to_numpy()

        if self.__convert_output_to_category:
            self.__train_set_y = to_categorical(self.__train_set_y)
            self.__validation_set_y = to_categorical(self.__validation_set_y)
            self.__test_set_y = to_categorical(self.__test_set_y)

        self.__train_set_x = self.__train_set.drop(columns=[self.__output_feature])
        self.__validation_set_x = self.__validation_set.drop(columns=[self.__output_feature])
        self.__test_set_x = self.__test_set.drop(columns=[self.__output_feature])

        return self.__train_set_x, self.__train_set_y, \
            self.__validation_set_x, self.__validation_set_y, \
            self.__test_set_x, self.__test_set_y

    def display_information_text(self) -> None:
        """
        Display or print in the console the information in text mode.

        :rtype: None
        """
        print('--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---')
        print(f'Null values for all the data:\n{self.__data.isna().any()}')
        print('--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---')
        print(f'Data set length:       {len(self.__data)}')
        print(f'Training set length:   {len(self.__train_set_x)}')
        print(f'Validation set length: {len(self.__validation_set_x)}')
        print(f'Test set length:       {len(self.__test_set_x)}')
        print('--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---')

    def display_information_graphic(self, columns: list) -> None:
        """
        Display the graphics in the plot for the selected columns.

        :type columns: list[str]
        :param columns: The Columns Names which will represent the information.

        :rtype: None
        """
        graphic_train_set = GraphicInformation(self.__train_set)
        graphic_train_set.set_columns(columns)
        graphic_train_set.get_distribution_columns()

        graphic_validation_set = GraphicInformation(self.__validation_set)
        graphic_validation_set.set_columns(columns)
        graphic_validation_set.get_distribution_columns()

        graphic_test_set = GraphicInformation(self.__test_set)
        graphic_test_set.set_columns(columns)
        graphic_test_set.get_distribution_columns()
