username <- Sys.getenv("clhub_username")
password <- Sys.getenv("clhub_password")
app_token <- Sys.getenv("app_token")

credentials <- hubr::get_credentials("https://clhub.clessn.cloud/", username, password)
print(username)
