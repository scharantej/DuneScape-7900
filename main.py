
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Sample data
game_features = [
    "Explore the vast and dangerous planet of Arrakis",
    "Compete for control of the precious spice, melange",
    "Build your army and wage war against your opponents",
    "Establish alliances and betray your allies",
    "Become the ultimate ruler of Arrakis"
]

game_components = [
    {
        "name": "Cards",
        "image": "cards.jpg",
        "description": "The game includes over 300 cards, featuring characters, locations, and events from the Dune universe."
    },
    {
        "name": "Tiles",
        "image": "tiles.jpg",
        "description": "The game board is made up of tiles that represent the different regions of Arrakis."
    },
    {
        "name": "Miniatures",
        "image": "miniatures.jpg",
        "description": "The game includes detailed miniatures of the game's characters and units."
    }
]

game_artwork = [
    {
        "image": "dune_imperium_1.jpg",
        "description": "The game's artwork is inspired by the classic Dune novels and films."
    },
    {
        "image": "dune_imperium_2.jpg",
        "description": "The game's cards feature stunning illustrations by some of the world's top fantasy artists."
    },
    {
        "image": "dune_imperium_3.jpg",
        "description": "The game's board and tiles are beautifully designed and evoke the atmosphere of the Dune universe."
    }
]

@app.route('/')
def index():
    return render_template('index.html', features=game_features)

@app.route('/components')
def components():
    return render_template('components.html', components=game_components)

@app.route('/artwork')
def artwork():
    return render_template('artwork.html', artwork=game_artwork)

@app.route('/purchase')
def purchase():
    return redirect('https://www.amazon.com/Dune-Imperium-Board-Game/dp/B08873D57X')

if __name__ == '__main__':
    app.run()
