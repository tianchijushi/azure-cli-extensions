# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from .providers.ExtensionProvider import ExtensionProvider
from .providers.FluxConfigurationProvider import FluxConfigurationProvider
from . import consts

def flux_config_show(cmd, client, resource_group_name, cluster_name, cluster_type, name):
    """Get an existing Kubernetes Source Control Configuration.

    """
    provider = FluxConfigurationProvider(cmd, client, resource_group_name, cluster_name, cluster_type, name)
    return provider.show()


# pylint: disable=too-many-locals
def flux_config_create(cmd, client, resource_group_name, cluster_name, name, cluster_type, url=None,
                       scope='cluster', namespace='default', kind=consts.GIT, timeout=None, sync_interval=None,
                       branch=None, tag=None, semver=None, commit=None, auth_ref_override=None, ssh_private_key=None,
                       ssh_private_key_file=None, https_user=None, https_key=None, known_hosts=None,
                       known_hosts_file=None, kustomization=None):

    provider = FluxConfigurationProvider(cmd, client, resource_group_name, cluster_name, name, cluster_type)
    return provider.create(url, scope, namespace, kind, timeout, sync_interval,
                           branch, tag, semver, commit, auth_ref_override, ssh_private_key,
                           ssh_private_key_file, https_user, https_key, known_hosts,
                           known_hosts_file, kustomization)


def flux_config_delete(cmd, client, resource_group_name, cluster_name, cluster_type, name):
    provider = FluxConfigurationProvider(cmd, client, resource_group_name, cluster_name, cluster_type, name)
    return provider.delete()


# def flux_create_source(cmd, client, resource_group_name, cluster_name, name, cluster_type, url,
#     scope='cluster', namespace='default', kind='git', timeout=None, sync_interval=None, branch=None, tag=None, semver=None, commit=None, 
#     auth_ref_override=None, ssh_private_key=None, ssh_private_key_file=None, https_user=None, https_key=None,
#     ssh_known_hosts=None, ssh_known_hosts_file=None):

#     # Determine ClusterRP
#     cluster_rp = get_cluster_type(cluster_type)

#     repository_ref = RepositoryRefDefinition(
#         branch=branch,
#         tag=tag,
#         semver=semver,
#         commit=commit
#     )

#     git_repository = GitRepositoryDefinition(
#         url=url,
#         timeout=timeout,
#         sync_interval=sync_interval,
#         repository_ref=repository_ref,
#         ssh_known_hosts=ssh_known_hosts,
#         https_user=https_user,
#         auth_ref_override=auth_ref_override
#     ) 
    
#     flux_configuration = FluxConfiguration(
#         scope=scope,
#         namespace=namespace,
#         source_kind=kind,
#         timeout=timeout,
#         sync_interval=sync_interval,
#         git_repository=git_repository,
#         kustomizations=[]
#     )
#     # cache the payload if --defer used or send to Azure
#     return cached_put(cmd, client.begin_create_or_update, flux_configuration, resource_group_name, name, cluster_rp, cluster_type, cluster_name)

# def flux_create_kustomization(cmd, client, resource_group_name, cluster_name, config_name, name, cluster_type,
#     dependencies, timeout, sync_interval, retry_interval, path='', prune=False, validation='none', force=False):
    
#     # Determine ClusterRP
#     cluster_rp = get_cluster_type(cluster_type)

#     flux_configuration = cached_get(cmd, client.get, resource_group_name, cluster_rp, cluster_type, cluster_name, config_name)

#     kustomization = KustomizationDefinition(
#         name=name,
#         path=path,
#         dependencies=dependencies,
#         timeout=timeout,
#         sync_interval=sync_interval,
#         retry_interval=retry_interval,
#         prune=prune,
#         validation=validation,
#         force=force
#     )

#     upsert_to_collection(flux_configuration, 'kustomizations', kustomization, 'name')
#     flux_configuration = cached_put(cmd, client.begin_create_or_update, flux_configuration, resource_group_name, name).result()
#     return get_property(flux_configuration.kustomizations, name)
