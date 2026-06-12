import json
import requests
import os

USERNAME = "sarangp-c"

TOKEN = os.getenv("GITHUB_TOKEN_CUSTOM")

headers = {}

if TOKEN:
    headers["Authorization"] = f"token {TOKEN}"

url = f"https://api.github.com/users/{USERNAME}/repos"

response = requests.get(url, headers=headers)

repos = response.json()

projects = []

for repo in repos:

    if repo["fork"]:
        continue

    projects.append({
        "name": repo["name"],
        "description": repo["description"],
        "url": repo["html_url"],
        "stars": repo["stargazers_count"],
        "language": repo["language"]
    })

os.makedirs("data", exist_ok=True)

with open("data/projects.json", "w", encoding="utf-8") as file:
    json.dump(projects, file, indent=4)

print("Projects JSON generated.")import json
import requests
import os

USERNAME = "sarangp-c"

TOKEN = os.getenv("GITHUB_TOKEN_CUSTOM")

headers = {}

if TOKEN:
    headers["Authorization"] = f"token {TOKEN}"

url = f"https://api.github.com/users/{USERNAME}/repos"

response = requests.get(url, headers=headers)

repos = response.json()

projects = []

for repo in repos:

    if repo["fork"]:
        continue

    projects.append({
        "name": repo["name"],
        "description": repo["description"],
        "url": repo["html_url"],
        "stars": repo["stargazers_count"],
        "language": repo["language"]
    })

os.makedirs("data", exist_ok=True)

with open("data/projects.json", "w", encoding="utf-8") as f:
    json.dump(projects, f, indent=4)

print("Projects JSON generated.")