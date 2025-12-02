resource "aws_instance" "devops" {
  ami = data.aws_ami.ubuntu-ec2-ami.id
  # ami = "ami-0fa3fe0fa7920f68e" # amazon linux x86
  # instance_type = "t2.micro"
  instance_type =  var.instance_type
  region = var.main_region
  tags = {
    Name = "was_devops"
    Env = "dev"
  }
}


output "instance_ip" {
  value = aws_instance.devops.public_ip
}
