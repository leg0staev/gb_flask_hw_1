from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def main():
    title = 'Главная'
    _categories = [
        {
            'name': 'Одежда',
            'description': 'В разделе "Одежда" вы найдете стильные и модные наряды для любого случая: от повседневных '
                           'образов до элегантных вечерних нарядов. Широкий ассортимент размеров и цветов, '
                           'качественные ткани и выгодные цены.',
            'link_to_page': '/shoes/',
            'link_to_img': '../static/img/clothes.jpeg',
        },
        {
            'name': 'Обувь',
            'description': 'В разделе "Обувь" представлены удобные и модные модели для всех случаев жизни. От '
                           'стильных кроссовок до элегантных туфель - у нас вы найдете идеальную пару для любого '
                           'наряда. Качество, комфорт и стиль по доступным ценам.',
            'link_to_page': '/shoes/',
            'link_to_img': '../static/img/shoes.jpg',
        },
    ]
    return render_template('main.html', title=title, categories=_categories)


@app.route('/product_page/')
def product():
    title = 'Продукт'
    _specifications = {
        'name': 'модель 1',
        'size': '38',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor '
                       'incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud '
                       'exercitation ullamco ',
        'link_to_img': '../static/img/shoe_1.jpg',
    }
    return render_template('product.html', title=title, specifications=_specifications)


@app.route('/shoes/')
def shoes():
    title = 'Обувь'
    _shoes = [
        {
            'name': 'модель 1',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor '
                           'incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud '
                           'exercitation ullamco ',
            'link_to_page': '/product_page/',
            'link_to_img': '../static/img/shoe_1.jpg',
        },
        {
            'name': 'модель 2',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor '
                           'incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud '
                           'exercitation ullamco ',
            'link_to_page': '/product_page/',
            'link_to_img': '../static/img/shoe_2.jpg',
        },
        {
            'name': 'модель 3',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor '
                           'incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud '
                           'exercitation ullamco ',
            'link_to_page': '/product_page/',
            'link_to_img': '../static/img/shoe_3.jpg',
        },
        {
            'name': 'модель 4',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor '
                           'incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud '
                           'exercitation ullamco ',
            'link_to_page': '/product_page/',
            'link_to_img': '../static/img/shoe_4.jpg',
        }, {
            'name': 'модель 5',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor '
                           'incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud '
                           'exercitation ullamco ',
            'link_to_page': '/product_page/',
            'link_to_img': '../static/img/shoe_5.jpg',
        },
        {
            'name': 'модель 6',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor '
                           'incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud '
                           'exercitation ullamco ',
            'link_to_page': '/product_page/',
            'link_to_img': '../static/img/shoe_6.jpg',
        },
        {
            'name': 'модель 7',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor '
                           'incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud '
                           'exercitation ullamco ',
            'link_to_page': '/product_page/',
            'link_to_img': '../static/img/shoe_7.jpg',
        },
        {
            'name': 'модель 8',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor '
                           'incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud '
                           'exercitation ullamco ',
            'link_to_page': '/product_page/',
            'link_to_img': '../static/img/shoe_8.jpg',
        },
    ]
    return render_template('shoes.html', title=title, shoes=_shoes)


if __name__ == '__main__':
    app.run()
