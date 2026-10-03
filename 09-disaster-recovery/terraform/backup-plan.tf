resource "aws_backup_vault" "portfolio" {
  name = "vijay-portfolio-backup-vault"
}

resource "aws_backup_plan" "portfolio" {
  name = "vijay-portfolio-backup-plan"

  rule {
    rule_name         = "daily"
    target_vault_name = aws_backup_vault.portfolio.name
    schedule          = "cron(0 5 * * ? *)"
  }
}
