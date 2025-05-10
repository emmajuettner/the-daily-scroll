from pathlib import Path
from jinja2 import FileSystemLoader, Environment
import os
import miniflux

body = "This is where the articles go"

# Utility methods
def getObjectByAttribute(arr, attributeName, attributeValue):
    for obj in arr:
        if obj[attributeName] == attributeValue:
            return obj

def convertEntryToNewsArticle(entry):
	print(entry)
    newsArticle = "<h2>"+entry.get("title")+" by "+entry.get("author")+"</h2>"

# Set up Miniflux connection
minifluxKey = os.environ['MINIFLUX_API_KEY']
minifluxClient = miniflux.Client("https://reader.miniflux.app", api_key=minifluxKey)

# Pull list of categories
categories = minifluxClient.get_categories()
news_category_id = getObjectByAttribute(categories, "title", "News")["id"]

# Pull list of news items
newsEntries = minifluxClient.get_category_entries(news_category_id)
for entry in newsEntries:
	body += convertEntryToNewsArticle(entry)

# Build the html file
loader = FileSystemLoader(".")
env = Environment(
    loader=loader, extensions=["jinja2_humanize_extension.HumanizeExtension"]
)
template = env.get_template("index.jinja")
Path("index.html").write_text(
    template.render(
        {
            "body" : body
        }
    )
)
print("Generated index.html")
