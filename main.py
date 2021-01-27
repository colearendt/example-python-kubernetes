import kubernetes
import tempfile
import boto3
import base64
import eks_token


def k8s_api_client(endpoint: str, token: str, cafile: str) -> kubernetes.client.CoreV1Api:
    kconfig = kubernetes.config.kube_config.Configuration(
      host=endpoint,
      api_key={'authorization': 'Bearer ' + token}
    )
    kconfig.ssl_ca_cert = cafile
    kclient = kubernetes.client.ApiClient(configuration=kconfig)
    return kubernetes.client.CoreV1Api(api_client=kclient)


cluster_name = 'my-eks-cluster'
my_token = eks_token.get_token(cluster_name)


def _write_cafile(data: str) -> tempfile.NamedTemporaryFile:
    # protect yourself from automatic deletion
    cafile = tempfile.NamedTemporaryFile(delete=False)

    cadata_b64 = data
    cadata = base64.b64decode(cadata_b64)
    cafile.write(cadata)
    cafile.flush()

    return cafile


bclient = boto3.client('eks')
cluster_data = bclient.describe_cluster(name=cluster_name)
my_cafile = _write_cafile(cluster_data['certificateAuthority']['data'])


api_client = k8s_api_client(
  endpoint=cluster_data['endpoint'],
  token=my_token['data'],
  cafile=my_cafile
)

api_client.list_namespace()

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
# If it already exists, you get a 409 conflict
