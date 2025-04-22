from pathlib import Path
from jinja2 import FileSystemLoader, Environment

body = "This is where the articles go"

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
