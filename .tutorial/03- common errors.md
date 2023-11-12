# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## Copy, Paste and EDIT

👉 What's the problem here?


```python
from flask import Flask
import datetime

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index(): 
  page = f"""<html><body>
  <p><a href = "/home">Go home</a></p>
  </body>
  </html>"""
  return page

@app.route('/home') 
def index(): 
  page = """html
  
  <html>
    
  <head>
    <title>David's World Of Baldies</title>
  </head>


  <body>
  <h1>Dave's World of Baldies</h1> 
  <h2>Welcome to our website!</h2>

  <p>We all know that throughout history some of the greatest have been Baldies, let's see the epicness of their heads bereft of hair.</p>

  <h2>Gallery of Baldies</h2>
  <p>Here are some of the legends of the bald world.</p>

  <img src="images/picard.jpg" width = 30%> 
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
  
  return page


app.run(host='0.0.0.0', port=81)
```

<details> <summary> 👀 Answer </summary>

I've copied the code from `@app.route('/')` to create `@app.route('/home')`, but I now have **two subroutines called index**. This is what is creating the error. We can't have two subroutines with the same name.

```python
@app.route('/')
def index(): 
  page = f"""<html><body>
  <p><a href = "/home">Go home</a></p>
  </body>
  </html>"""
  return page

@app.route('/home') 
def home(): 
```

</details>

## Directionless

👉 What's the problem here?


```python
from flask import Flask
import datetime # import the datetime library

app = Flask(__name__)


```

<details> <summary> 👀 Answer </summary>

I've missed the path to the static folder, so none of my images/videos, etc. will load.

```python
from flask import Flask
import datetime

app = Flask(__name__, static_url_path="/static") 
```

</details>
