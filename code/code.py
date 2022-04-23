import os
import time

print("hello python")

username = os.environ.get("clhub_username")
password = os.environ.get("clhub_password")
url = os.environ.get("clhub_url")
print(f"username: {username}")
print(f"password: {password}")
print(f"url: {url}")

time.sleep(15)
raise Exception("error!")
