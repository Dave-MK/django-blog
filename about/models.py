from django.db import models

# Create your models here.
class About(models.Model):
    """
    Model to store information about the blog.
    
    **Fields**
    
    - `title`: Title of the blog.
    - `content`: Content of the blog.
    - `updated_on`: Date and time when the blog was created.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title