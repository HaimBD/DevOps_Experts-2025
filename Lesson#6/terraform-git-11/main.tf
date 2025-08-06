terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

provider "github" {
  token = "<Token>"
}

# Add a user to the organization
resource "github_repository" "DevOps_Experts-2026" {
  name = "terraform-example"
  description = "cloud repo"
  visibility = "public"
}