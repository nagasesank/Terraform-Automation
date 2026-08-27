# Security Policy

Do not commit credentials, private keys, local environment files, Terraform state, Terraform plans, or real infrastructure endpoints to this repository.

Report suspected secret exposure privately to the repository owner. If a credential is committed, revoke or rotate it first, then remove it from the current tree and Git history.

Automated secret scanning runs on pushes and pull requests.
