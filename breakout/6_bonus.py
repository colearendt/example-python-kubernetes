def create_update_configmap(
        k8s_client: kubernetes.client.CoreV1Api,
        namespace: str,
        configmap: kubernetes.client.V1ConfigMap
) -> kubernetes.client.V1ConfigMap:
    """
    Try to create a new namespaced configmap, and fall back to replacing
    a namespaced configmap if the create fails with a 409 (conflict)

    :rtype: client.V1ConfigMap
    :param k8s_client: The kubernetes.ApiClient object to use
    :param namespace: The namespace to update a configmap within
    :param configmap: The kubernetes.ConfigMap to apply
    :return: The kubernetes.ConfigMap API response
    """
    try:
        res = k8s_client.create_namespaced_config_map(namespace, configmap)
    except kubernetes.client.exceptions.ApiException as e:
        if e.status == 409:
            # 409 conflict = it exists... try to replace instead
            res = k8s_client.replace_namespaced_config_map('aws-auth', namespace, configmap)
        else:
            raise e
    return res


create_update_configmap(api_client, namespace=default, body=my_configmap)

api_client.delete_namespaced_config_map(namespace='default', name='my-configmap')
