from flask import Flask, render_template, url_for

app = Flask(__name__) # создаем объект на основе класса фласк в основе которого этот файл

@app.route('/') #это декоратор, в фун-ии раут отслеживается страница / - главная страница, /smth - отслеживание другой страницы
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/constraction')
def constr_choose():
    return render_template("constr.html")

@app.route('/technology')
def tech():
    return render_template("tech.html")


if __name__ == "__main__":
    app.run(debug=True)




