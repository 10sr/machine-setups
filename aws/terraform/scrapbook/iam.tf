resource "aws_iam_role" "r" {
  name = "ScrapbookEcrPush"

  # TODO: ひとまず全権限を与えているが、細かく制御したい
  managed_policy_arns = ["arn:aws:iam::aws:policy/AdministratorAccess"]

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = "sts:AssumeRole"
        Principal = {
          # TODO: 一旦 SSO ユーザからログインする形にしているが、別の IAM ユーザを用意したほうがいい？
          AWS = "arn:aws:iam::645223824092:role/aws-reserved/sso.amazonaws.com/ap-northeast-1/AWSReservedSSO_permset-AdministratorAccess_e2a193310af6f660"
        }
      },
    ]
  })
}
