from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/home.html')
def redirect_home():
    return redirect(url_for('index'))

@app.route('/')
def index():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
      <title>My Website</title>
    </head>
    <body>
      <header>
        <h1>Welcome to My Website</h1>
        <nav>
          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about.html">About</a></li>
            <li><a href="/contact.html">Contact</a></li>
          </ul>
        </nav>
      </header>

      <main>
        <section>
          <h2>About</h2>
          <p>This is a sample website created using HTML.</p>
        </section>

        <section>
          <h2>Contact</h2>
          <p>You can reach us at example@example.com</p>
        </section>
      </main>

      <footer>
        <p>&copy; 2023 My Website. All rights reserved.</p>
      </footer>
    </body>
    </html>
    '''
    return html

if __name__ == '__main__':
    app.run()
