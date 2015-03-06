from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    header = models.CharField(max_length=255)
    text = models.TextField()
    when = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=True)

    def __unicode__(self):
        return u'{} at {}'.format(self.header, self.when)

    def short_text(self):
        if len(self.text) <= 250:
            return self.text
        else:
            return self.text[:200] + '<a href="/posts/{}/"> <i>(Read more...)</i></a>'.format(self.id)


class Comment(models.Model):
    post = models.ForeignKey(Post)
    text = models.TextField(max_length=3000)
    when = models.DateTimeField(auto_now=True)
    header = models.CharField(max_length=255, default='')
    who = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return u'Comment at {}'.format(self.when)