from flask import Flask, url_for

i = 0
app = Flask(__name__)


@app.route('/')
def page():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    promotion_list = ["Человечество вырастает из детства.",
                      "Человечеству мала одна планета.",
                      "Мы сделаем обитаемыми безжизненные пока планеты.",
                      "И начнем с Марса!",
                      "Присоединяйся!"]

    return '</br>'.join(promotion_list)


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>жди нас Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.png')}" alt="здесь должна была быть картинка, но не нашлась">
                      </body>
                    </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
                         rel="stylesheet"
                         integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>жди нас Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.png')}" alt="здесь должна была быть картинка, но не нашлась">
                        <div class="text-bg-dark p-3">Человечество вырастает из детства.</div>
                        <div class="text-bg-success p-3">Человечеству мала одна планета.</div>
                        <div class="text-bg-dark p-3">Мы сделаем обитаемые безжизненные пока планеты.</div>
                        <div class="text-bg-warning p-3">И начнем с Марса!</div>
                        <div class="text-bg-danger p-3">Присоединяйся!</div>
                      </body>
                    </html>"""


@app.route('/i')
def show_i():
    global i
    i += 1
    return str(i)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
