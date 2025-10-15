from django.shortcuts import render
import random

def top(request):
    return render(request, "work07/top.html")

def omikuji(request):
    results = ['大吉', '中吉', '小吉', '吉', '末吉', '凶']
    result = random.choice(results)
    return render(request, "work07/omikuji.html", {"result": result})

def janken(request):
    hands = ['グー', 'チョキ', 'パー']
    user_hand = request.GET.get('hand')  # ← 修正済み
    cpu_hand = random.choice(hands)
    outcome = None

    if user_hand in hands:
        if user_hand == cpu_hand:
            outcome = 'あいこ'
        elif (user_hand == 'グー' and cpu_hand == 'チョキ') or \
             (user_hand == 'チョキ' and cpu_hand == 'パー') or \
             (user_hand == 'パー' and cpu_hand == 'グー'):
            outcome = '勝ち'
        else:
            outcome = '負け'

    return render(request, "work07/janken.html", {
        "user_hand": user_hand,
        "cpu_hand": cpu_hand,
        "outcome": outcome
    })

def hi_low(request):
    cpu_number = random.randint(1, 10)
    guess = request.GET.get('guess')  # 'high' または 'low'
    result = None
    if guess:
        if (guess == 'high' and cpu_number > 5) or (guess == 'low' and cpu_number <= 5):
            result = '正解！'
        else:
            result = '不正解！'
    return render(request, 'work07/hi_low.html', {
        'cpu_number': cpu_number,
        'guess': guess,
        'result': result
    })
