import kubernetes


def k8s_api_client(endpoint: str, token: str, cafile: str) -> kubernetes.client.CoreV1Api:
    kconfig = kubernetes.config.kube_config.Configuration(
        host=endpoint,
        api_key={'authorization': 'Bearer ' + token}
    )
    kconfig.ssl_ca_cert = cafile
    kclient = kubernetes.client.ApiClient(configuration=kconfig)
    return kubernetes.client.CoreV1Api(api_client=kclient)
