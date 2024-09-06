import json
import requests

# Define your dev.to username
devto_username = "anikakash"

# Fetch the latest dev.to posts using the API
response = requests.get(f"https://dev.to/api/articles?username={devto_username}")
devto_posts = response.json()

# Generate the markdown for the latest 5 blog posts
latest_posts_md = "\n".join([
    f"- [{post['title']}]({post['url']})" for post in devto_posts[:5]
])

# Read the README.md file
with open("README.md", "r") as f:
    readme_content = f.read()

# Replace the section with the latest dev.to posts
new_readme_content = readme_content.split("## Latest dev.to posts")[0] + f"## Latest dev.to posts\n\n{latest_posts_md}\n"

# Write the updated content back to the README.md file
with open("README.md", "w") as f:
    f.write(new_readme_content)
