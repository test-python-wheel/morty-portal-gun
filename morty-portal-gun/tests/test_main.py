from morty_portal_gun.main import app
from typer.testing import CliRunner
import json 
from datetime import datetime

runner = CliRunner()

def seconds_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d %H:%M:%S")
    d2 = datetime.strptime(d2, "%Y-%m-%d %H:%M:%S")
    return abs((d2 - d1).seconds)

def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def test_add():
    result = runner.invoke(app, ["add", "test"])
    assert result.exit_code == 0
    assert "Your item added successfully." in result.stdout
    
    with open("db.json" , "r") as f:
        file = json.load(f)
        
    time = file['_default']['1']['time']
    del file['_default']['1']['time']
    
    assert seconds_between(time, now()) < 1000
    assert file == {'_default': {'1': {'item': 'test'}}}

def test_show():
    result = runner.invoke(app, ["show"])
    assert result.exit_code == 0
    
    with open("db.json" , "r") as f:
        file = json.load(f)        
    item = file['_default']['1']['item']
    time = file['_default']['1']['time']

    assert item,time in result.stdout

def test_reset():
    result = runner.invoke(app, ["reset"])
    assert result.exit_code == 0
    assert "Database Reset Successfully" in result.stdout

    with open("db.json" , "r") as f:
        file = json.load(f)
    
    assert file == {'_default': {}}

print(test_add())