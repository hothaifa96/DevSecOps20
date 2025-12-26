
resource "aws_iam_role" "eks-ng-role" {
  name = "eks-ng-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "eks-ng-AmazonEKSWorkerNodePolicy" {
  role       = aws_iam_role.eks-ng-role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
}

resource "aws_iam_role_policy_attachment" "eks-ng-AmazonEKS_CNI_Policy" {
  role       = aws_iam_role.eks-ng-role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy"
}

resource "aws_iam_role_policy_attachment" "eks-ng-AmazonEC2ContainerRegistryReadOnly" {
  role       = aws_iam_role.eks-ng-role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
}
# arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy
# arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy
# arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly


resource "aws_eks_node_group" "eks-node-group" {
  cluster_name    = aws_eks_cluster.eks-cluster-tf.name
  node_group_name = "eks-node-group"
  node_role_arn   = aws_iam_role.eks-ng-role.arn
  subnet_ids = [
    aws_subnet.private-subnet-1.id,
    aws_subnet.private-subnet-2.id
  ]
  scaling_config {
    desired_size = 2
    max_size     = 3
    min_size     = 1
  }
  update_config {
    max_unavailable = 1
  }
  depends_on = [
    aws_iam_role_policy_attachment.eks-ng-AmazonEC2ContainerRegistryReadOnly,
    aws_iam_role_policy_attachment.eks-ng-AmazonEKS_CNI_Policy,
    aws_iam_role_policy_attachment.eks-ng-AmazonEKSWorkerNodePolicy
  ]
}
