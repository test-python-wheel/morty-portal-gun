from morty_portal_gun.main import app
from typer.testing import CliRunner
import json

runner = CliRunner()


def test_add():
    result = runner.invoke(app, ["add", "test"])
    assert result.exit_code == 0
    assert "Your item added successfully." in result.stdout

def test_show():
    result = runner.invoke(app, ["show"])
    assert result.exit_code == 0
    assert "Hello Camila" in result.stdout

def test_reset():
    result = runner.invoke(app, ["reset"])
    assert result.exit_code == 0

    with open("db.json" , "r") as f:
        file = json.load(f)
    assert file == {'_default': {}}