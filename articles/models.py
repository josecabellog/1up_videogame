
from django.db import models
from django.contrib.auth.models import User  # Django's built-in user model

class Article(models.Model):
    # Basic fields
    title = models.CharField(max_length=200)
    content = models.TextField()
    game_reviewed = models.CharField(max_length=100)
    
    # Rating (1-10 scale)
    rating = models.IntegerField(
        choices=[(i, i) for i in range(1, 11)],  # Creates choices 1-10
        blank=True,  # Not required if it's just an article, not a review
        null=True
    )
    
    # Relationships
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Links to Django's user
    
    # Dates
    date_published = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title  # Makes admin interface more readable

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # Links to Article
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Links to User
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.author.username} on {self.article.title}"
