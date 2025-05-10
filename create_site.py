from pathlib import Path
from jinja2 import FileSystemLoader, Environment
import os
import miniflux

body = "This is where the articles go"

# Pull data from Miniflux
minifluxKey = os.environ['MINIFLUX_API_KEY'])
minifluxClient = miniflux.Client("https://reader.miniflux.app", api_key=minifluxKey)
feeds = minifluxClient.get_feeds()

body+=str(feeds)

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
