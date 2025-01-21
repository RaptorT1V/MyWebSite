from django.shortcuts import render
from .models import GameScore
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required
def index(request):
    leaderboard = GameScore.objects.all().order_by('-ninja_score', '-snake_score', '-typing_score')[:10]

    context = {
        'leaderboard': leaderboard,
    }

    return render(request, 'game/index.html', context)


@login_required
def save_score(request):
    if request.method == 'POST':
        game_name = request.POST.get('game')
        score = float(request.POST.get('score'))
        score = round(score)

        user = request.user
        try:
            game_score = GameScore.objects.get(user=user)
        except GameScore.DoesNotExist:
            game_score = GameScore(user=user)

        if game_name == 'ninja':
            if score > game_score.ninja_score:
                game_score.ninja_score = score
        elif game_name == 'snake':
            if score > game_score.snake_score:
                game_score.snake_score = score
        elif game_name == 'typing':
            if score > game_score.typing_score:
                game_score.typing_score = score

        game_score.save()

        return JsonResponse({'status': 'success', 'message': 'Score saved successfully'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)


def ninja(request):
    return render(request, 'game/ninja.html')


def typing(request):
    return render(request, 'game/typing.html')


def snake(request):
    return render(request, 'game/snake.html')