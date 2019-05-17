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


class ConnectionTypeCreateOrUpdateParameters(Model):
    """The parameters supplied to the create or update connection type operation.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Gets or sets the name of the connection type.
    :type name: str
    :param is_global: Gets or sets a Boolean value to indicate if the
     connection type is global.
    :type is_global: bool
    :param field_definitions: Required. Gets or sets the field definitions of
     the connection type.
    :type field_definitions: dict[str,
     ~azure.mgmt.automation.models.FieldDefinition]
    """

    _validation = {
        'name': {'required': True},
        'field_definitions': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'is_global': {'key': 'properties.isGlobal', 'type': 'bool'},
        'field_definitions': {'key': 'properties.fieldDefinitions', 'type': '{FieldDefinition}'},
    }

    def __init__(self, **kwargs):
        super(ConnectionTypeCreateOrUpdateParameters, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.is_global = kwargs.get('is_global', None)
        self.field_definitions = kwargs.get('field_definitions', None)