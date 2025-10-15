from django.shortcuts import render, redirect, get_object_or_404
from .models import Memo
from .forms import MemoForm

# 一覧画面
def memo_list(request):
    memos = Memo.objects.all().order_by('-created_at')
    return render(request, 'work08/memo_list.html', {'memos': memos})

# 新規作成
def memo_create(request):
    memo = Memo.objects.create(title="no title", content="")
    return redirect('work08:memo_edit', memo_id=memo.id)

# 編集画面
def memo_edit(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    if request.method == 'POST':
        # フォームを使って画像も保存
        form = MemoForm(request.POST, request.FILES, instance=memo)
        if form.is_valid():
            form.save()
            return redirect('work08:memo_list')
    else:
        form = MemoForm(instance=memo)
    return render(request, 'work08/memo_edit.html', {'form': form, 'memo': memo})

# 削除
def memo_delete(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    memo.delete()
    return redirect('work08:memo_list')
