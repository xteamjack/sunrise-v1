import typer

app = typer.Typer(name="sunrise")


@app.command()
def ask(question: str) -> None:
    print("I cannot answer yet: the knowledge and agent layers are not built. (bootstrap)")


@app.command()
def search(query: str) -> None:
    print("Search is not wired yet. (bootstrap)")


@app.command()
def ingest() -> None:
    print("Ingest is not wired yet. (bootstrap)")


if __name__ == "__main__":
    app()
