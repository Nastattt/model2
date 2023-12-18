from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    category = models.CharField(max_length=20, choices=[(1, 'Cпорт'), (2, 'Красота')])

    def __str__(self):
        return self.title

