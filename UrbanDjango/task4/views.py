from django.shortcuts import render


# Create your views here.
def task3_platform(request):
   namepage = 'Главная страница'
   context = {
      'namepage': namepage,
   }

   return render(request, 'fourth_task/platform.html', context)


def task3_games(request):
   namepage = 'Игры'
   games = ['Antjmic Heart',
            'Cyberpunk 2077',
            'PayDay 2']
   button_text = 'Купить'
   context = {
      'namepage': namepage,
      'games': games,
      'button_text': button_text
              }
   return render(request, 'fourth_task/games.html', context)

def task3_cart(request):
   namepage = 'Корзина'
   text = 'Извините, Ваша корзина пуста'
   context = {
      'namepage': namepage,
      'text': text,
               }
   return render(request, 'fourth_task/cart.html', context)


def base(request):
   return render(request, 'fourth_task/menu.html')
