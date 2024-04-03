from click.testing import CliRunner
from main import main

def test_main():
    runner = CliRunner()
    result = runner.invoke(main, ["--name", "Selman", "--color", "green"])
    assert "Selman" in result.output