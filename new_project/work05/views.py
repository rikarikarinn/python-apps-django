from django.shortcuts import render

# トップページ
def top(request):
    return render(request, "work05/index.html")

# index ページ（トップと同じ内容でもOK）
def index(request):
    return render(request, "work05/index.html")

# list ページ（必要に応じて list.html を作る）
def list_view(request):
    return render(request, "work05/list.html")
