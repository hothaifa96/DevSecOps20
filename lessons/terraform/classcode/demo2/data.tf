
data "aws_ami" "ubuntu-ec2-ami" {
  most_recent = true
  owners = [ "099720109477" ]

  filter {
    name   = "name"
    values = ["*ubuntu*"]
  }
}
