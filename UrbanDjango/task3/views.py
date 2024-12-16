from django.shortcuts import render


# Create your views here.
def task3_platform(request):
   return render(request, 'third_task/platform.html')


def task3_games(request):
   title = 'games'
   text = 'Игры'
   text_1 = 'Antjmic Heart'
   text_2 = 'Cyberpunk 2077'
   text_3 = 'PayDay 2'
   text_4 = 'Вернуться обратно'
   button_text = 'Купить'
   context = {
      'title': title,
      'text': text,
      'text_1': text_1,
      'text_2': text_2,
      'text_3': text_3,
      'text_4': text_4,
      'button_text': button_text
              }
   return render(request, 'third_task/games.html', context)

def task3_cart(request):
   title = 'cart'
   text = 'Извините, Ваша корзина пуста'
   text_1 = 'Вернуться обратно'
   context = {
      'title': title,
      'text': text,
      'text_1': text_1
              }
   return render(request, 'third_task/cart.html', context)