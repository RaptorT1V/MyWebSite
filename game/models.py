from django.db import models
from django.conf import settings


class GameScore(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ninja_score = models.IntegerField(default=0)
    snake_score = models.IntegerField(default=0)
    typing_score = models.IntegerField(default=0)

    class Meta:
        ordering = ['-ninja_score', '-snake_score', '-typing_score']

    def __str__(self):
        return f"{self.user.username}'s scores"

    def update_score(self, game_type, new_score):
        if game_type == 'ninja':
            if self.ninja_score is None or new_score > self.ninja_score:
                self.ninja_score = new_score
                self.save()
        elif game_type == 'snake':
            if self.snake_score is None or new_score > self.snake_score:
                self.snake_score = new_score
                self.save()
        elif game_type == 'typing':
            if self.typing_score is None or new_score > self.typing_score:
                self.typing_score = new_score
                self.save()
        else:
            raise ValueError("Invalid game type")