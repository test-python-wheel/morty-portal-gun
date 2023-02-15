import typer

import database

app = typer.Typer()

@app.command(help="add new item")
def add(item: str = typer.Argument(...)):
    # try:
        database.insert(item)
        print("Your item added successfully.")
    # except:
        # print("Something went wrong.")

@app.command(help="list your items")
def show():
    all = database.all()
    for i in all:
        print(i['item'], i['time'])

@app.command(help="reset all data")
def reset():
    database.reset()
    
if __name__ == "__main__":
    app()