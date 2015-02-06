from django.db import models


# Create your models here.
class Post(models.Model):
    header = models.CharField(max_length=255)
    text = models.TextField()
    when = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=True)

    def __unicode__(self):
        return u'{} at {}'.format(self.header, self.when)


class Comment(models.Model):
    post = models.ForeignKey('Post')
    text = models.TextField(u'Comment text')
    when = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'Comment to "{}"'.format(self.post.header)