resource "aws_s3_bucket" "artifacts" {
  bucket = "${var.project_name}-artifacts"
}

output "s3_bucket_name" {
  value = aws_s3_bucket.artifacts.bucket
}
