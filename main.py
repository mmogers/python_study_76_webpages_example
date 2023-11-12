from flask import Flask

app = Flask(__name__)


@app.route('/portfolio')
def portfolio():
  page = f"""
  
  <html>
    <head>
      <title>Marina's Portfolio</title>
      <link rel="stylesheet" type="text/css" href="/static/portfolio_style.css">
    </head>  
    <body>
      <h1>Marina's Learning Python Porfolio</h1>
      <!--Day1-->
        <h2>Day 39 - Hangman Game</h2>
      <!--paragraph-->
          <p>Hangman is a classic word-guessing game where players try to discover a hidden word by suggesting letters. With each incorrect guess, a part of a stick-figure is drawn, and the challenge is to guess the word before the figure is completed.</p>
      <!--image-->
          <a href="https://replit.com/@mmogers/Day39-100Days?v=1"><img src = "/static/images/hangman.png" width = "20%"> </a>
      <!--Day2-->
      <h2>Day 45 - Todo List Manager</h2>
      <!--paragraph-->
          <p>
            A todo list manager is a handy tool for organizing tasks, allowing users to create, prioritize, and track their daily or long-term activities. It helps streamline productivity by providing a clear overview of pending tasks and completed achievements.
          </p>
            <!--image-->
      <a href="https://replit.com/@mmogers/Day45-100Days?v=1"><img src = "/static/images/todo.png" width = "20%"> </a>
        <!--Day3-->
      <h2>Day 50 - Idea Generator</h2>
          <!--paragraph-->
      <p>An idea generator is a creative tool that sparks innovation by randomly generating concepts, prompts, or combinations to inspire fresh and unique ideas. It serves as a catalyst for brainstorming sessions, helping individuals overcome creative blocks and explore new avenues of thought.</p>
          <!--image-->
      <a href="https://replit.com/@mmogers/Day50-100Days?v=1"><img src = "/static/images/ideas.png" width = "20%"> </a>
        <!--Day4-->
      <h2>Day 62 - Secret Diary</h2>
          <!--paragraph-->
      <p>A secret diary is a personal sanctuary for recording thoughts, emotions, and experiences in a private space, offering a therapeutic outlet for self-reflection. It provides a confidential haven where one can express innermost feelings without fear of judgment, fostering a sense of introspective catharsis.</p>
          <!--image-->
       <a href="https://replit.com/@mmogers/Day62-100Days?v=1"><img src = "/static/images/diary.png" width = "20%"> </a>
        <!--Day5-->
      <h2>Day 29 - Customized Printing Subroutine</h2>
          <!--paragraph-->
      <p>A customized printing subroutine is a tailored function within a program designed to produce personalized or specific print outputs, allowing users to format and present information according to their preferences. It enhances flexibility in document creation, enabling the adaptation of print layouts, styles, and content for individualized and professional results.</p>
          <!--image-->
        <a href="https://github.com/mmogers/python_study_29"><img src = "/static/images/print.png" width = "20%"> </a>

    </body>



  </html>
  
  
  """
  return page

@app.route('/linktree')
def linktree():
  page = f"""
  
  <!DOCTYPE html>
  <html lang="en">

  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Marina's Link Tree</title>
    <link href="/static/linktree_style.css" rel="stylesheet" type="text/css" />
  </head>

  <body>
    <div class="container">
      <h1>Marina Mogers</h1>
      <p>Java Backend Developer</p>
      <div class="profile">
        <img src="/static/images/me.jpeg" alt="marina mogers">
      </div>
      <h2>Socials</h2>
      <div class="links">
        <a href="https://www.linkedin.com/public-profile/settings?trk=d_flagship3_profile_self_view_public_profile"
          target="_blank">LinkedIn</a>
        <a href="https://www.facebook.com/marina.moger" target="_blank">Facebook</a>
        <a href="https://github.com/mmogers" target="_blank">GitHub</a>
      </div>
    </div>
    <!-- This script places a badge on your repl's full-browser view back to your repl's cover page. -->
    <script src="https://replit.com/public/js/replit-badge.js" theme="blue" defer></script>
  </body>

  </html>
  
  """
  return page
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)