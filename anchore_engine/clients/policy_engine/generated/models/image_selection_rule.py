# coding: utf-8

"""
    anchore_engine.services.policy_engine

    This is a policy evaluation service. It receives push-events from external systems for data updates and provides an api for requesting image policy checks  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: zach@anchore.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from anchore_engine.clients.policy_engine.generated.models.image_ref import ImageRef  # noqa: F401,E501


class ImageSelectionRule(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'registry': 'str',
        'repository': 'str',
        'image': 'ImageRef'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'registry': 'registry',
        'repository': 'repository',
        'image': 'image'
    }

    def __init__(self, id=None, name=None, registry=None, repository=None, image=None):  # noqa: E501
        """ImageSelectionRule - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._registry = None
        self._repository = None
        self._image = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.registry = registry
        self.repository = repository
        self.image = image

    @property
    def id(self):
        """Gets the id of this ImageSelectionRule.  # noqa: E501


        :return: The id of this ImageSelectionRule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImageSelectionRule.


        :param id: The id of this ImageSelectionRule.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ImageSelectionRule.  # noqa: E501


        :return: The name of this ImageSelectionRule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImageSelectionRule.


        :param name: The name of this ImageSelectionRule.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def registry(self):
        """Gets the registry of this ImageSelectionRule.  # noqa: E501


        :return: The registry of this ImageSelectionRule.  # noqa: E501
        :rtype: str
        """
        return self._registry

    @registry.setter
    def registry(self, registry):
        """Sets the registry of this ImageSelectionRule.


        :param registry: The registry of this ImageSelectionRule.  # noqa: E501
        :type: str
        """
        if registry is None:
            raise ValueError("Invalid value for `registry`, must not be `None`")  # noqa: E501

        self._registry = registry

    @property
    def repository(self):
        """Gets the repository of this ImageSelectionRule.  # noqa: E501


        :return: The repository of this ImageSelectionRule.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this ImageSelectionRule.


        :param repository: The repository of this ImageSelectionRule.  # noqa: E501
        :type: str
        """
        if repository is None:
            raise ValueError("Invalid value for `repository`, must not be `None`")  # noqa: E501

        self._repository = repository

    @property
    def image(self):
        """Gets the image of this ImageSelectionRule.  # noqa: E501


        :return: The image of this ImageSelectionRule.  # noqa: E501
        :rtype: ImageRef
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ImageSelectionRule.


        :param image: The image of this ImageSelectionRule.  # noqa: E501
        :type: ImageRef
        """
        if image is None:
            raise ValueError("Invalid value for `image`, must not be `None`")  # noqa: E501

        self._image = image

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list([x.to_dict() if hasattr(x, "to_dict") else x for x in value])
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict([(item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item for item in list(value.items())])
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImageSelectionRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
