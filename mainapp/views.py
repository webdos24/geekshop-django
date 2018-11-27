from django.shortcuts import render

# Create your views here.
base_menu = [
{'href':'main', 'name':'домой'},
{'href':'products', 'name':'продукты'},
{'href':'contact', 'name':'контакты'},
]

def main(request):
	clDiv = 'slider'
	basket = False
	return render(request, 'mainapp/index.html', {'clDiv':clDiv, 'basket':basket,
	'base_menu':base_menu,
	})

def products(request):
	clDiv = 'hero-white'
	basket = True

	links_menu = [
	{'href': 'products_all', 'name': 'все'},
	{'href': 'product_home', 'name': 'дом'},
	{'href': 'product_office', 'name': 'офис'},
	{'href': 'product_modern', 'name': 'модерн'},
	{'href': 'product_classic', 'name': 'классика'},
	]

	# block спецпредложение
	slider_main = {'main':'/static/img/slider1.jpg'}
	slider_control = [
	{'control':'/static/img/controll.jpg'},
	{'control':'/static/img/controll1.jpg'},
	{'control':'/static/img/controll2.jpg'},
	]

	details_description = [
	{'big_bold':'Отличный стул'},
	{'red':'горячее предложение'},
	{'price':'2585.9', 'valuta':'руб'},
	]

	details_desc_text = ['Расположитесь комфортно.',
	'Отличное качество материалов позволит вам это.',
	'Различные цвета',
	'высочайший уровень эргономики и прочность.',
	]

	# endblock

	related_products = ['/static/img/product-11.jpg',
	'/static/img/product-21.jpg',
	'/static/img/product-31.jpg',
	]
	return render(request, 'mainapp/products.html',
	{'clDiv':clDiv, 'basket':basket, 'links_menu':links_menu,
	'base_menu':base_menu,
	'slider_main':slider_main,
	'slider_control':slider_control,
	'details_description':details_description,
	'details_desc_text':details_desc_text,
	'related_products':related_products,
	})

def contact(request):
	clDiv = 'hero'
	basket = True
	locCity = ['Moscow', 'Moscow', 'Moscow',]

	clContacts = [
	{'h5':'Телефон', 'p':'+7-888-888-8888'},
	{'h5':'Email', 'p':'info@geekshop.ru'},
	{'h5':'Адрес', 'p':'В пределах МКАД'},
	]

	return render(request, 'mainapp/contact.html', {'clDiv':clDiv,
	'basket':basket,
	'base_menu':base_menu,
	'clContacts':clContacts,
	'locCity':locCity,
	})
