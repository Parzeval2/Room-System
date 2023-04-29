

from website import create_app

# setup for flask app
# ROOMS = {
#     "111": Room("111"),
#     "125": Room("125"),
#     "131": Room("131"),
#     "211": Room("211"),
#     "225": Room("225"),
#     "231": Room("231"),
#     "311": Room("311"),
#     "325": Room("325"),
#     "331": Room("331"),
# }

app = create_app()

if __name__ == "__main__":
    app.run()
