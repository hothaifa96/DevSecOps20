
resource "aws_iam_role" "eks-fargate-profile-role" {
  name = "eks-fargate-profile-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "eks-fargate-pods.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}


resource "aws_iam_role_policy_attachment" "fargate_execution_policy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSFargatePodExecutionRolePolicy"
  role = aws_iam_role.eks-fargate-profile-role.name
}

resource "aws_eks_fargate_profile" "eks-fg-profile" {
  cluster_name = aws_eks_cluster.eks-cluster-tf.name
  fargate_profile_name = "eks-fg-profile"
  pod_execution_role_arn = aws_iam_role.eks-fargate-profile-role.arn
  subnet_ids= [
    aws_subnet.private-subnet-1.id,
    aws_subnet.private-subnet-2.id
  ]
    selector {
      namespace = "application"
    }
    depends_on = [ aws_iam_role_policy_attachment.fargate_execution_policy ]
}