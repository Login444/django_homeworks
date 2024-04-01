from django.db import models

# Create your models here.
class CoinThrows(models.Model):
    throw_result = models.CharField(max_length=5)
    throw_date_time = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def stat_coin(count: int):
        last_count_games = CoinThrows.objects.all().order_by('-id')[:count]
        result = {'Орёл': 0, 'Решка': 0}
        for game in last_count_games:
            result[game.throw_result] +=1
        return result


class Author(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField(max_length=1500)
    birthday = models.DateField(blank=False)

    def fullname(self):
        return f'{self.name} {self.lastname}'