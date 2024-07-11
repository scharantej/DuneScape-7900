## Flask Application Design

### HTML Files

**index.html:**
- The main landing page for the Dune: Imperium board game.
- Features high-quality images, engaging animations, and concise, captivating text.
- Uses a color scheme inspired by the Dune universe, with deep blues, rich oranges, and sandy neutrals.
- Includes a brief overview of the game's features, gameplay, and themes.
- Contains a call-to-action button that takes users to a purchase or learn more page.

**components.html:**
- A partial HTML file used to display individual components of the game, such as cards, tiles, or miniatures.
- Includes images and brief descriptions of each component.
- Can be dynamically populated with data from a database or API.

**artwork.html:**
- A partial HTML file used to showcase the stunning artwork from the game.
- Includes high-quality images of the game's cards, board, and other elements.
- Provides a deeper dive into the game's thematic and visual appeal.

### Routes

**@app.route('/')**
- The main route that renders the `index.html` template.
- Handles the initial request for the landing page.

**@app.route('/components')**
- A route that renders the `components.html` template.
- Provides a detailed overview of the game's components.

**@app.route('/artwork')**
- A route that renders the `artwork.html` template.
- Showcases the beautiful artwork from the game.

**@app.route('/purchase')**
- A route that redirects users to a purchase page or provides more information on how to acquire the game.
- Handles the call-to-action from the landing page.