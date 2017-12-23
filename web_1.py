from flask import Flask, render_template

my_flask_app = Flask(__name__)

@my_flask_app.route('/')
def index():
    return render_template('index_diplom.html', title="Сетевой эмулятор")

@my_flask_app.route('/map/')
def maps_network():
    return render_template('map_diplom.html', title="Схема сети")


@my_flask_app.route('/input/')
def input():
    return render_template('input_1.html', title="Ввод данных")

@my_flask_app.route('/authors/')
def authors():
    return render_template('authors.html', title="Ввод данных")

if __name__=="__main__":
    my_flask_app.run(port=5010, debug=True) # debug=True - рестартует сайт при изменении файла .рy