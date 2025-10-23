resource "aws_dynamodb_table" "receivables" {
  name = "${var.project_name}-receivables"
  billing_mode = "PAY_PER_REQUEST"
  hash_key = "proposal_id"

  attribute {
    name = "proposal_id"
    type = "S"
  }
}

output "dynamodb_table" {
  value = aws_dynamodb_table.receivables.name
}
