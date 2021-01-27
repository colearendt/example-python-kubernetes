import eks_token

cluster_name = 'my-eks-cluster'
my_token = eks_token.get_token(cluster_name)
