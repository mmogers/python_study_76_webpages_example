# fStrings With Flask

One of the cool things we can do is use fStrings to format some content inside our webpages.

👉 Let's say I want to insert today's date on the homepage.  I will:
1. Write the code to get the date inside the `home` subroutine and assign to a variable.
2. Format the HTML as an fString.
3. Use curly braces to drop the date variable into the HTML.


Here's the code with comments to show the changes.
```python
from flask import Flask
import datetime # import the datetime library

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/home') 
def home():
  today = datetime.date.today() # Get today's date
  page = f"""html 
  # Format the html as an fString
  <html>
    
  <head>
    <title>David's World Of Baldies</title>
  </head>


  <body>
  <h1>Dave's World of Baldies</h1> 
  <h2>Welcome to our website!</h2>
  <h2>{today}</h2> #Drop the date variable inside curly braces.

  <p>We all know that throughout history some of the greatest have been Baldies, let's see the epicness of their heads bereft of hair.</p>

  <h2>Gallery of Baldies</h2>
  <p>Here are some of the legends of the bald world.</p>

  <img src="static/images/picard.jpg" width = 30%> 
  <p><a href = "https://memory-alpha.fandom.com/wiki/Star_Trek:_Picard">Captain Jean Luc Picard: Baldest Star Trek captain, and legend.</a></p>

  <ul>
    <li>Beautiful bald man</li>
    <li>Calm and cool under pressure</li>
    <li>All the Picard memes</li>
  </ul>

  <p><a href = "page2.html">Go to page 2</a></p>
  
</body>
  
</html>
  
  """
```

## Linking With Flask

👉 Let's  add a link from our index to our home page.  I'm just going to show the `index` part of the code to add some quick content with a link.

```python
from flask import Flask
import datetime # import the datetime library

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index():
  page = f"""<html><body>
  <p><a href = "/home">Go home</a></p>
  </body>
  </html>"""
  
  return page
```

### Try it out!