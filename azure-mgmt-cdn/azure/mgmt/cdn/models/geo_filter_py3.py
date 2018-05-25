# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GeoFilter(Model):
    """Rules defining user's geo access within a CDN endpoint.

    All required parameters must be populated in order to send to Azure.

    :param relative_path: Required. Relative path applicable to geo filter.
     (e.g. '/mypictures', '/mypicture/kitty.jpg', and etc.)
    :type relative_path: str
    :param action: Required. Action of the geo filter, i.e. allow or block
     access. Possible values include: 'Block', 'Allow'
    :type action: str or ~azure.mgmt.cdn.models.GeoFilterActions
    :param country_codes: Required. Two letter country codes defining user
     country access in a geo filter, e.g. AU, MX, US.
    :type country_codes: list[str]
    """

    _validation = {
        'relative_path': {'required': True},
        'action': {'required': True},
        'country_codes': {'required': True},
    }

    _attribute_map = {
        'relative_path': {'key': 'relativePath', 'type': 'str'},
        'action': {'key': 'action', 'type': 'GeoFilterActions'},
        'country_codes': {'key': 'countryCodes', 'type': '[str]'},
    }

    def __init__(self, *, relative_path: str, action, country_codes, **kwargs) -> None:
        super(GeoFilter, self).__init__(**kwargs)
        self.relative_path = relative_path
        self.action = action
        self.country_codes = country_codes