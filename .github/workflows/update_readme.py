import json

# Read dev.to articles
with open("devto.json", "r") as f:
    articles = json.load(f)

# Open README.md and find where to insert posts
with open("README.md", "r") as f:
    readme_content = f.readlines()

# Find the line where you want to insert the posts (e.g., after a specific marker)
start_line = readme_content.index("<!-- BLOG-POST-LIST:START -->\n")
end_line = readme_content.index("<!-- BLOG-POST-LIST:END -->\n")

# Prepare the blog posts
new_content = []
for article in articles[:5]:  # Show top 5 recent articles
    new_content.append(f"- [{article['title']}]({article['url']})\n")

# Insert the new posts
readme_content[start_line+1:end_line] = new_content

# Write the updated README back
with open("README.md", "w") as f:
    f.writelines(readme_content)
