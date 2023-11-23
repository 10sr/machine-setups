terraform {
  backend "s3" {
    region = "ap-northeast-1"
    profile = "8-admin"

    bucket = "10sr-tfstate-bucket"
    key    = "tfstates/scrapbook.tfstate"

    dynamodb_table = "tfstate_lock"
  }
}
