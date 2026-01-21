from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm, StockForm, StockOutForm
from django.db.models import Q
from .models import Item, StockHistory


# 一覧表示
def item_list(request):
    query = request.GET.get('q')  # URLの?q=xxx から取得
    if query:
        items = Item.objects.filter(Q(name__icontains=query))
    else:
        items = Item.objects.all()
    return render(request, 'zaiko/item_list.html', {'items': items, 'query': query})

# 商品登録
def item_create(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('item_list')
    return render(request, 'zaiko/item_form.html', {'form': form})


# --- 入庫処理 ---
def stock_in(request, pk):
    item = get_object_or_404(Item, pk=pk)
    form = StockForm(request.POST or None)
    if form.is_valid():
        qty = form.cleaned_data['quantity']
        item.stock += qty
        item.save()
        # 履歴作成
        StockHistory.objects.create(item=item, action=StockHistory.IN, quantity=qty)
        return redirect('item_list')
    return render(request, 'zaiko/stock_form.html', {'item': item, 'form': form})

# --- 出庫処理 ---
def stock_out(request, pk):
    item = get_object_or_404(Item, pk=pk)
    form = StockForm(request.POST or None)
    if form.is_valid():
        qty = form.cleaned_data['quantity']
        item.stock -= qty
        if item.stock < 0:
            item.stock = 0
        item.save()
        # 履歴作成
        StockHistory.objects.create(item=item, action=StockHistory.OUT, quantity=qty)
        return redirect('item_list')
    return render(request, 'zaiko/stock_out_form.html', {'item': item, 'form': form})

# --- 履歴一覧 ---
def history_list(request):
    histories = StockHistory.objects.select_related('item').order_by('-created_at')
    return render(request, 'zaiko/history_list.html', {'histories': histories})
