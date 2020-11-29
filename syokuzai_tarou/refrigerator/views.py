from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def top(request):
    params = {
        'title': '食材残さないよ太郎',
        'setsumei':'レシピ表示をする時は使いたい食材にチェックをいれてレシピ表示ボタンを押してください',
        'goto' : 'food_register'
    }
    return render(request, 'refrigerator/top.html', params)
def food_register(request):
    params = {
        'title' : '食材残さないよ太郎',
        'setsumei' : '食材を登録できます',
        'goto' : 'top'
    }
    return render(request, 'refrigerator/food_register.html', params)
