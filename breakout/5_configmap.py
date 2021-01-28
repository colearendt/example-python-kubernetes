my_configmap = kubernetes.client.V1ConfigMap(
    api_version='v1',
    metadata={'name': 'my-configmap'},
    kind='ConfigMap',
    data={'my_file.txt': 'mycontent'}
)

api_client.create_namespaced_config_map(namespace='default', body=my_configmap)

# NOTE: to update a configmap, you need to
# use k8s_client.replace_namespaced_config_map
#
# If it already exists, create will give a 409 conflict
