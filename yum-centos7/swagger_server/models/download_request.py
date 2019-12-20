# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util
from .download_spec import DownloadSpec

class DownloadRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id=None, spec=None, status=None, is_consumable=None):  # noqa: E501
        """DownloadRequest - a model defined in Swagger

        :param id: The id of this DownloadRequest.  # noqa: E501
        :type id: int
        :param spec: The spec of this DownloadRequest.  # noqa: E501
        :type spec: DownloadSpec
        :param status: The status of this DownloadRequest.  # noqa: E501
        :type status: str
        :param is_consumable: The is_consumable of this DownloadRequest.  # noqa: E501
        :type is_consumable: bool
        """
        self.swagger_types = {
            'id': int,
            'spec': DownloadSpec,
            'status': str,
            'is_consumable': bool
        }

        self.attribute_map = {
            'id': 'id',
            'spec': 'spec',
            'status': 'status',
            'is_consumable': 'isConsumable'
        }

        self._id = id
        self._spec = spec
        self._status = status
        self._is_consumable = is_consumable

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DownloadRequest of this DownloadRequest.  # noqa: E501
        :rtype: DownloadRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this DownloadRequest.


        :return: The id of this DownloadRequest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DownloadRequest.


        :param id: The id of this DownloadRequest.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def spec(self):
        """Gets the spec of this DownloadRequest.


        :return: The spec of this DownloadRequest.
        :rtype: DownloadSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this DownloadRequest.


        :param spec: The spec of this DownloadRequest.
        :type spec: DownloadSpec
        """
        if spec is None:
            raise ValueError("Invalid value for `spec`, must not be `None`")  # noqa: E501

        self._spec = spec

    @property
    def status(self):
        """Gets the status of this DownloadRequest.

        Request status to display for the user. CAUTION: Do not rely on this for any computation!   # noqa: E501

        :return: The status of this DownloadRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DownloadRequest.

        Request status to display for the user. CAUTION: Do not rely on this for any computation!   # noqa: E501

        :param status: The status of this DownloadRequest.
        :type status: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def is_consumable(self):
        """Gets the is_consumable of this DownloadRequest.

        Whether the requested files are ready for download or not  # noqa: E501

        :return: The is_consumable of this DownloadRequest.
        :rtype: bool
        """
        return self._is_consumable

    @is_consumable.setter
    def is_consumable(self, is_consumable):
        """Sets the is_consumable of this DownloadRequest.

        Whether the requested files are ready for download or not  # noqa: E501

        :param is_consumable: The is_consumable of this DownloadRequest.
        :type is_consumable: bool
        """
        if is_consumable is None:
            raise ValueError("Invalid value for `is_consumable`, must not be `None`")  # noqa: E501

        self._is_consumable = is_consumable
