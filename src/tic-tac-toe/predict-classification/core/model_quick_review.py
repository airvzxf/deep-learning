#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Execute a quick deep learning model to review the tendencies.
"""
from numpy import ndarray
from pandas import DataFrame
from tensorflow.python.keras.activations import softmax
from tensorflow.python.keras.backend import relu
from tensorflow.python.keras.callbacks import History
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.losses import categorical_crossentropy
from tensorflow.python.keras.metrics import Precision, accuracy
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.optimizer_v2.adam import Adam

from core.graphic_information import GraphicInformation
from core.split_data import SplitData


class ModelQuickReview:
    """
    Execute a quick deep learning model.
    """
    __data: DataFrame
    __output_feature: str
    __train_set_x: DataFrame
    __train_set_y: ndarray
    __validation_set_x: DataFrame
    __validation_set_y: ndarray
    __test_set_x: DataFrame
    __test_set_y: ndarray
    __history: History
    __model: Sequential

    def __init__(self, data: DataFrame, output_feature: str, train_size: float = 0.98) -> None:
        """
        Construction method.

        :rtype: None
        """
        self.__data = data
        self.__output_feature = output_feature
        self.__train_size = train_size

    def split_data(self,
                   show_text_information: bool = False,
                   show_graph_information: bool = False) -> None:
        """
        Split the data for the training, validation and test.

        :type show_text_information: bool
        :param show_text_information: Display information in the console.

        :type show_graph_information: bool
        :param show_graph_information: Display the plot with the graphic representation.

        :rtype: None
        """
        split_data: SplitData = SplitData(self.__data, train_size=self.__train_size,
                                          output_feature=self.__output_feature,
                                          convert_output_to_category=True)
        self.__train_set_x, self.__train_set_y, \
            self.__validation_set_x, self.__validation_set_y, \
            self.__test_set_x, self.__test_set_y = split_data.get_data_split()
        if show_text_information:
            split_data.display_information_text()
        if show_graph_information:
            split_data.display_information_graphic(columns=[self.__output_feature])

    def fit(self) -> None:
        """
        Fit the deep learning model with the training data and the validation set.

        :rtype: None
        """
        self.__model = Sequential()
        self.__model.add(Dense(512, activation=relu, input_shape=self.__train_set_x.shape[1:]))
        self.__model.add(Dense(512, activation=relu))
        self.__model.add(Dense(self.__train_set_y.shape[1], activation=softmax))
        self.__model.compile(
            optimizer=Adam(),
            loss=categorical_crossentropy,
            metrics=[accuracy, Precision()]
        )
        print(self.__model.summary())

        self.__history = self.__model.fit(
            self.__train_set_x,
            self.__train_set_y,
            epochs=3,
            batch_size=512,
            validation_data=(self.__validation_set_x, self.__validation_set_y)
        )

    def show_graphic_information(self) -> None:
        """
        Display plots with graphical information for the history record of the model.

        :rtype: None
        """
        graphic_for_quick_model = GraphicInformation(self.__data, is_show_activated=False)
        graphic_for_quick_model.get_history_model(self.__history, filters=['loss', 'val_loss'],
                                                  x_label='Epochs', y_label='Loss')
        graphic_for_quick_model.get_history_model(self.__history, filters=['accuracy', 'val_accuracy'],
                                                  x_label='Epochs', y_label='Accuracy')
        precision = [i for i in self.__history.history.keys() if i.startswith("precision")][0]
        graphic_for_quick_model.get_history_model(self.__history, filters=[precision, f'val_{precision}'],
                                                  x_label='Epochs', y_label='Precision')
        graphic_for_quick_model.show()

    def evaluate(self) -> None:
        """
        Evaluate the deep learning model with the test data.

        :rtype: None
        """
        error_evaluation, accuracy_evaluation, \
            precision_evaluation = self.__model.evaluate(self.__test_set_x, self.__test_set_y)
        print()
        print('Evaluate the model with the test data.')
        print(f'Error Raw: {error_evaluation:,.2g}')
        print(f'Accuracy: {accuracy_evaluation:,.2g}')
        print(f'Precision: {precision_evaluation:,.2g}')
