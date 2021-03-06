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


class QueryTimePeriod(Model):
    """The start and end date for pulling data for the query.

    All required parameters must be populated in order to send to Azure.

    :param from_property: Required. The start date to pull data from.
    :type from_property: datetime
    :param to: Required. The end date to pull data to.
    :type to: datetime
    """

    _validation = {
        'from_property': {'required': True},
        'to': {'required': True},
    }

    _attribute_map = {
        'from_property': {'key': 'from', 'type': 'iso-8601'},
        'to': {'key': 'to', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(QueryTimePeriod, self).__init__(**kwargs)
        self.from_property = kwargs.get('from_property', None)
        self.to = kwargs.get('to', None)
