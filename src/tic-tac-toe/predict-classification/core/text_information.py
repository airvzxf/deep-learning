#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Display information about the data frame of Pandas.
"""
from pandas import DataFrame


class TextInformation:
    """
    This class get information about the data frame of Pandas.
    """
    __data_frame: DataFrame

    def __init__(self, data_frame: DataFrame) -> None:
        """
        Construction method.

        :type data_frame: DataFrame
        :param data_frame: Data frame object to execute Pandas methods.

        :rtype: None
        """
        self.__data_frame = data_frame

    def display_information(self) -> None:
        """
        Display the information of the data frame.

        :rtype: None
        """
        print('┏━━━━━━━━━━━━┓')
        print('┃ Data frame ┃')
        print('┗━━━━━━━━━━━━┛')
        print(self.__data_frame)
        print('┏━━━━━━━━━━━━━┓')
        print('┃ Information ┃')
        print('┗━━━━━━━━━━━━━┛')
        print(self.__data_frame.info())
        print('┏━━━━━━━━━━┓')
        print('┃ Describe ┃')
        print('┗━━━━━━━━━━┛')
        print(self.__data_frame.describe())
        print('┏━━━━━━━━━━━━━━━━━━━┓')
        print('┃ NDim, Shape, Size ┃')
        print('┗━━━━━━━━━━━━━━━━━━━┛')
        print(self.__data_frame.ndim)
        print(self.__data_frame.shape)
        print(self.__data_frame.size)
        print('┏━━━━━━━━━┓')
        print('┃ Columns ┃')
        print('┗━━━━━━━━━┛')
        print(self.__data_frame.columns)
        print('┏━━━━━━━━━━━━━━┓')
        print('┃ Empty values ┃')
        print('┗━━━━━━━━━━━━━━┛')
        print(self.__data_frame.empty)
        print('┏━━━━━━━━━━━━━━┓')
        print('┃ Value counts ┃')
        print('┗━━━━━━━━━━━━━━┛')
        for column in self.__data_frame.columns:
            print(self.__data_frame[column].value_counts())
            print('───────────────')
