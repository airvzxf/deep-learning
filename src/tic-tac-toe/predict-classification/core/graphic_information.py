#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Graphic information with MatPlotLib.
"""
from matplotlib import pyplot as plt
from pandas import DataFrame
from pandas.plotting import scatter_matrix
from tensorflow.python.keras.callbacks import History


class GraphicInformation:
    """
    Represents the information with graphics, using the MatPlotLib.
    """
    __data_frame: DataFrame
    __data_frame_source: DataFrame
    __fig_size: tuple
    __is_show_activated: bool

    def __init__(self, data_frame: DataFrame,
                 fig_size: tuple = (20, 11),
                 is_show_activated: bool = True) -> None:
        """
        Construction method.

        :type data_frame: DataFrame
        :param data_frame: Data frame object to execute Pandas methods.

        :type fig_size: tuple[float:float]
        :param fig_size: Size of the figure in the plot.

        :rtype: None
        """
        self.__data_frame = data_frame
        self.__data_frame_source = data_frame
        self.__fig_size = fig_size
        self.__is_show_activated = is_show_activated

    @staticmethod
    def show() -> None:
        """
        Execute the show method for the plot which display all the windows for each plot.

        :rtype: None
        """
        plt.show()

    def set_columns(self, attributes: list) -> None:
        """
        Set the columns of the Data Frame, it will affect all  the operations.
        To reset the Data Frame to the original use `reset_columns()`.

        :type attributes: list[str]
        :param attributes: List with the columns.

        :rtype: None
        """
        self.__data_frame = self.__data_frame_source[attributes]

    def reset_columns(self) -> None:
        """
        Reset the Data Frame to the original.

        :rtype: None
        """
        self.__data_frame = self.__data_frame_source

    def get_distribution_columns(self) -> None:
        """
        Graph the distribution of columns.

        :rtype: None
        """
        self.__data_frame.hist(bins=50, figsize=self.__fig_size)
        plt.suptitle('Distribution of the columns', fontsize=16)
        if self.__is_show_activated:
            plt.show()

    def get_correlation_matrix(self) -> None:
        """
        Graph the correlation matrix of columns.

        :rtype: None
        """
        corr = self.__data_frame.corr()
        fig, ax = plt.subplots(figsize=self.__fig_size)
        ax.matshow(corr)
        plt.title('Correlation matrix of columns', fontsize=16)
        plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
        plt.yticks(range(len(corr.columns)), corr.columns)
        if self.__is_show_activated:
            plt.show()

    def get_matrix_scatter_plots(self) -> None:
        """
        Graph the matrix of scatter plots.

        :rtype: None
        """
        scatter_matrix(self.__data_frame, figsize=self.__fig_size, grid=True)
        plt.suptitle('Matrix of scatter plots', fontsize=16)
        if self.__is_show_activated:
            plt.show()

    def get_scatter_plots(self, x: str, y: str) -> None:
        """
        Graph the scatter plots.

        :type x: str
        :param x: Column Name from the Data Frame where the data will take.

        :type y: str
        :param y: Column Name from the Data Frame where the data will take.

        :rtype: None
        """
        self.__data_frame.plot.scatter(x, y, figsize=self.__fig_size)
        plt.title('Scatter plots', fontsize=16)
        plt.grid(True)
        if self.__is_show_activated:
            plt.show()

    def get_3d_scatter_plots(self, columns: list,
                             x_label: str = None,
                             y_label: str = None,
                             z_label: str = None) -> None:
        """
        Graph the 3D scatter plots.

        :type columns: list[tuple[str, str, str]]
        :param columns: The tree Columns Names from the Data Frame where the data will take.

        :type x_label: str
        :param x_label: The label for the X axis in the plot.

        :type y_label: str
        :param y_label: The label for the Y axis in the plot.

        :type z_label: str
        :param z_label: The label for the Z axis in the plot.

        :rtype: None
        """
        plt.figure(figsize=self.__fig_size)
        ax = plt.axes(projection="3d")
        column: tuple[str, str, str]
        for column in columns:
            ax.scatter3D(self.__data_frame[column[0]],
                         self.__data_frame[column[1]],
                         self.__data_frame[column[2]], )
        if x_label:
            ax.set_xlabel(x_label)
        if y_label:
            ax.set_ylabel(y_label)
        if z_label:
            ax.set_zlabel(z_label)
        plt.title('3D scatter plots', fontsize=16)
        if self.__is_show_activated:
            plt.show()

    def get_density(self, x_label: str = None) -> None:
        """
        Graph the scatter plots.

        :type x_label: str
        :param x_label: The label for the X axis in the plot.

        :rtype: None
        """
        self.__data_frame.plot(kind='density', figsize=self.__fig_size)
        plt.title('Density of the values', fontsize=16)
        if x_label:
            plt.xlabel(x_label)
        plt.legend(loc='upper right')
        plt.grid(True)
        if self.__is_show_activated:
            plt.show()

    def get_history_model(self, history: History, filters: list,
                          x_label: str = None, y_label: str = None) -> None:
        """
        Graph the history of the deep learning model training and validation.

        :type history: History
        :param history: History of the model iteration.

        :type filters: list[str, str]
        :param filters: The metrics or loss data usually, the training and the validation.

        :type x_label: str
        :param x_label: Label for the X axis.

        :type y_label: str
        :param y_label: Label for the Y axis.

        :rtype: None
        """
        DataFrame(history.history)[filters].plot(figsize=self.__fig_size)
        plt.grid(True)
        plt.title('History of the deep learning model', fontsize=16)
        if x_label:
            plt.xlabel(x_label)
        if y_label:
            plt.ylabel(y_label)
        if self.__is_show_activated:
            plt.show()
