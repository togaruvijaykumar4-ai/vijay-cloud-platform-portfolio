variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "gcp_project" {
  type        = string
  description = "Your GCP project ID."
}

variable "gcp_region" {
  type    = string
  default = "us-central1"
}
