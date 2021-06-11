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

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from msrest import Deserializer, Serializer

from ._configuration import SourceControlConfigurationClientConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential
    from azure.core.pipeline.transport import HttpRequest, HttpResponse

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class SourceControlConfigurationClient(MultiApiClientMixin, _SDKClient):
    """KubernetesConfiguration Client.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API version to use if no profile is provided, or if missing in profile.
    :type api_version: str
    :param base_url: Service URL
    :type base_url: str
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    DEFAULT_API_VERSION = '2021-03-01'
    _PROFILE_TAG = "azure.mgmt.kubernetesconfiguration.SourceControlConfigurationClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        api_version=None, # type: Optional[str]
        base_url=None,  # type: Optional[str]
        profile=KnownProfiles.default, # type: KnownProfiles
        **kwargs  # type: Any
    ):
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = SourceControlConfigurationClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(SourceControlConfigurationClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2020-07-01-preview: :mod:`v2020_07_01_preview.models<azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models>`
           * 2020-10-01-preview: :mod:`v2020_10_01_preview.models<azure.mgmt.kubernetesconfiguration.v2020_10_01_preview.models>`
           * 2021-03-01: :mod:`v2021_03_01.models<azure.mgmt.kubernetesconfiguration.v2021_03_01.models>`
           * 2021-05-01-preview: :mod:`v2021_05_01_preview.models<azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.models>`
           * 2021-06-01-preview: :mod:`v2021_06_01_preview.models<azure.mgmt.kubernetesconfiguration.v2021_06_01_preview.models>`
        """
        if api_version == '2020-07-01-preview':
            from .v2020_07_01_preview import models
            return models
        elif api_version == '2020-10-01-preview':
            from .v2020_10_01_preview import models
            return models
        elif api_version == '2021-03-01':
            from .v2021_03_01 import models
            return models
        elif api_version == '2021-05-01-preview':
            from .v2021_05_01_preview import models
            return models
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def cluster_extension_type(self):
        """Instance depends on the API version:

           * 2021-05-01-preview: :class:`ClusterExtensionTypeOperations<azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.operations.ClusterExtensionTypeOperations>`
        """
        api_version = self._get_api_version('cluster_extension_type')
        if api_version == '2021-05-01-preview':
            from .v2021_05_01_preview.operations import ClusterExtensionTypeOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'cluster_extension_type'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def cluster_extension_types(self):
        """Instance depends on the API version:

           * 2021-05-01-preview: :class:`ClusterExtensionTypesOperations<azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.operations.ClusterExtensionTypesOperations>`
        """
        api_version = self._get_api_version('cluster_extension_types')
        if api_version == '2021-05-01-preview':
            from .v2021_05_01_preview.operations import ClusterExtensionTypesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'cluster_extension_types'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def extension_type_versions(self):
        """Instance depends on the API version:

           * 2021-05-01-preview: :class:`ExtensionTypeVersionsOperations<azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.operations.ExtensionTypeVersionsOperations>`
        """
        api_version = self._get_api_version('extension_type_versions')
        if api_version == '2021-05-01-preview':
            from .v2021_05_01_preview.operations import ExtensionTypeVersionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'extension_type_versions'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def extensions(self):
        """Instance depends on the API version:

           * 2020-07-01-preview: :class:`ExtensionsOperations<azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.operations.ExtensionsOperations>`
           * 2021-05-01-preview: :class:`ExtensionsOperations<azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.operations.ExtensionsOperations>`
        """
        api_version = self._get_api_version('extensions')
        if api_version == '2020-07-01-preview':
            from .v2020_07_01_preview.operations import ExtensionsOperations as OperationClass
        elif api_version == '2021-05-01-preview':
            from .v2021_05_01_preview.operations import ExtensionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'extensions'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def flux_config_operation_status(self):
        """Instance depends on the API version:

           * 2021-06-01-preview: :class:`FluxConfigOperationStatusOperations<azure.mgmt.kubernetesconfiguration.v2021_06_01_preview.operations.FluxConfigOperationStatusOperations>`
        """
        api_version = self._get_api_version('flux_config_operation_status')
        if api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import FluxConfigOperationStatusOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'flux_config_operation_status'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def flux_configurations(self):
        """Instance depends on the API version:

           * 2021-06-01-preview: :class:`FluxConfigurationsOperations<azure.mgmt.kubernetesconfiguration.v2021_06_01_preview.operations.FluxConfigurationsOperations>`
        """
        api_version = self._get_api_version('flux_configurations')
        if api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import FluxConfigurationsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'flux_configurations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def location_extension_types(self):
        """Instance depends on the API version:

           * 2021-05-01-preview: :class:`LocationExtensionTypesOperations<azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.operations.LocationExtensionTypesOperations>`
        """
        api_version = self._get_api_version('location_extension_types')
        if api_version == '2021-05-01-preview':
            from .v2021_05_01_preview.operations import LocationExtensionTypesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'location_extension_types'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operation_status(self):
        """Instance depends on the API version:

           * 2021-05-01-preview: :class:`OperationStatusOperations<azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.operations.OperationStatusOperations>`
           * 2021-06-01-preview: :class:`OperationStatusOperations<azure.mgmt.kubernetesconfiguration.v2021_06_01_preview.operations.OperationStatusOperations>`
        """
        api_version = self._get_api_version('operation_status')
        if api_version == '2021-05-01-preview':
            from .v2021_05_01_preview.operations import OperationStatusOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import OperationStatusOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'operation_status'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2020-07-01-preview: :class:`Operations<azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.operations.Operations>`
           * 2020-10-01-preview: :class:`Operations<azure.mgmt.kubernetesconfiguration.v2020_10_01_preview.operations.Operations>`
           * 2021-03-01: :class:`Operations<azure.mgmt.kubernetesconfiguration.v2021_03_01.operations.Operations>`
           * 2021-05-01-preview: :class:`Operations<azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.operations.Operations>`
           * 2021-06-01-preview: :class:`Operations<azure.mgmt.kubernetesconfiguration.v2021_06_01_preview.operations.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2020-07-01-preview':
            from .v2020_07_01_preview.operations import Operations as OperationClass
        elif api_version == '2020-10-01-preview':
            from .v2020_10_01_preview.operations import Operations as OperationClass
        elif api_version == '2021-03-01':
            from .v2021_03_01.operations import Operations as OperationClass
        elif api_version == '2021-05-01-preview':
            from .v2021_05_01_preview.operations import Operations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import Operations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'operations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def source_control_configurations(self):
        """Instance depends on the API version:

           * 2020-07-01-preview: :class:`SourceControlConfigurationsOperations<azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.operations.SourceControlConfigurationsOperations>`
           * 2020-10-01-preview: :class:`SourceControlConfigurationsOperations<azure.mgmt.kubernetesconfiguration.v2020_10_01_preview.operations.SourceControlConfigurationsOperations>`
           * 2021-03-01: :class:`SourceControlConfigurationsOperations<azure.mgmt.kubernetesconfiguration.v2021_03_01.operations.SourceControlConfigurationsOperations>`
           * 2021-05-01-preview: :class:`SourceControlConfigurationsOperations<azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.operations.SourceControlConfigurationsOperations>`
        """
        api_version = self._get_api_version('source_control_configurations')
        if api_version == '2020-07-01-preview':
            from .v2020_07_01_preview.operations import SourceControlConfigurationsOperations as OperationClass
        elif api_version == '2020-10-01-preview':
            from .v2020_10_01_preview.operations import SourceControlConfigurationsOperations as OperationClass
        elif api_version == '2021-03-01':
            from .v2021_03_01.operations import SourceControlConfigurationsOperations as OperationClass
        elif api_version == '2021-05-01-preview':
            from .v2021_05_01_preview.operations import SourceControlConfigurationsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'source_control_configurations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    def close(self):
        self._client.close()
    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)
