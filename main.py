import click

@click.command(help="This is just a hello app.")
@click.option("--name", prompt="Name", help="Need name")
@click.option("--color", prompt="Color", help="This is your color")
def main(name, color):
    if name == "Selman":
        click.echo("Selman, you are always green.")
        click.echo(click.style(f"Hello {name}!", fg="green"))
    else:
        click.echo(f"Your color is {color}!")
        click.echo(click.style(f"Hello {name}!", fg=color))

if __name__ == "__main__":
    main()