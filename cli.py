import os
import typer
from datetime import datetime
from composer import generate_prompt
import re

app = typer.Typer()
def slugify(text:str) ->str:
    """Converts text to a safe filename: lowercase, hyphens, no symbols."""
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


@app.command()
def compose(
    summary: str,
    output_dir: str = typer.Option("outputs","--output-dir", "-d", help="Output directory")
):
    typer.echo(f"SUMMARY: {summary}")
    # typer.echo(f"OUTPUT: {output}")

    os.makedirs(output_dir,exist_ok=True)

    prompt_yaml = generate_prompt(summary)
    timestamp = datetime.now().strftime("%Y%m%dT%H%M%S")
    scene_slug = slugify(summary)[:40]
    filename = f"{timestamp}_{scene_slug}.yaml"
    output_path = os.path.join(output_dir,filename) 

    with open(output_path, "w") as f:
        f.write(prompt_yaml)
    typer.echo(f"Scene saved: {output_path}")

# if __name__ == "__main__":
    app()
    #ERROR I HAVE FACED
'''💡 If you’re using @app.command() and have only one command(in this case 'compose'), do NOT include the function name(compose) when running it.
This can cause argument error:╭─ Error ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Got unexpected extra argument ('some name')     
only if we have more than one commands,then name it '''