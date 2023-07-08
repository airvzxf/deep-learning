#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Handle files in the Operating System.
"""
from os import remove, path


class File:
    """
    This class handle the files in the operating system.
    """
    __filename: str
    __was_deleted: bool

    def __init__(self, filename: str) -> None:
        """
        Construction method.

        :type filename: str
        :param filename: File information with the path and name.

        :rtype: None
        """
        self.__filename = filename
        self.__was_deleted = False

    def delete(self, delete_one_time: bool = False) -> None:
        """
        Delete file in the operating system.

        :type delete_one_time: bool
        :param delete_one_time: If true, it deletes the file always. False, it deletes only one time.

        :rtype: None
        """
        if path.exists(self.__filename) and (not delete_one_time or not self.__was_deleted):
            remove(self.__filename)

        self.__was_deleted = True

    def create(self) -> None:
        """
        Create new file if it doesn't exist.

        :rtype: None
        """
        if not path.exists(self.__filename):
            with open(self.__filename, 'w'):
                pass

    @property
    def filename(self) -> str:
        """
        Return the filename.

        :rtype: str
        :return: The filename.
        """
        return self.__filename

    def append(self, information: str) -> None:
        """
        Add information to the end of the file.

        :type information: str
        :param information: Text which will be added in the file.

        :rtype: None
        """
        if path.exists(self.__filename):
            with open(self.__filename, 'a') as file_reference:
                file_reference.write(information)
