api_client = k8s_api_client(
    endpoint=cluster_data['endpoint'],
    token=my_token['data'],
    cafile=my_cafile
)

api_client.list_namespace()
