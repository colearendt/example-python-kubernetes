import boto3
import tempfile
import base64


def _write_cafile(data: str) -> tempfile.NamedTemporaryFile:
    # protect yourself from automatic deletion
    cafile = tempfile.NamedTemporaryFile(delete=False)
    cadata_b64 = data
    cadata = base64.b64decode(cadata_b64)
    cafile.write(cadata)
    cafile.flush()
    return cafile


bclient = boto3.client('eks')
cluster_data = bclient.describe_cluster(name=cluster_name)['cluster']
my_cafile = _write_cafile(cluster_data['certificateAuthority']['data'])
