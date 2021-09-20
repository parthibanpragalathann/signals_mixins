import datetime
from django.db import models
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from django.template.defaultfilters import slugify
import json

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=200, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class TaskDate(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)

class History(models.Model):
    history = models.TextField(default='{}')

class HistoryDate(models.Model):
    historydate = models.TextField(default='{}')


#way 1
# def task_handler(sender, instance, **kwargs):
#     print("Pre save")
#     print(instance.name)
#     print(instance.description)
#
# pre_save.connect(task_handler, sender=Task)

#Way 2
@receiver(pre_save, sender=Task)
def task_handler(sender, instance, **kwargs):
    print("Pre save")
    print(instance.name)
    print(instance.description)
    print(task_handler)
    print(slugify(instance.name))
    instance.slug = (slugify(instance.name))

@receiver(post_save, sender=Task)
def task_handler_post(sender, instance, **kwargs):
    print("Post save")
    TaskDate.objects.create(task=instance, date = datetime.datetime.now())

@receiver(pre_delete, sender=Task)
def task_handler_pre_delete(sender, instance, **kwargs):
    print("Pre Delete")
    data = {'task name' : instance.name, 'desc': instance.description, 'slug': instance.slug}
    History.objects.create(history=json.dumps(data))

@receiver(post_delete, sender=History)
def task_handler_post_delete(sender, instance, **kwargs):
    print("Post Delete")
    print(instance.history)
    dataa = {'task history' : instance.history}
    HistoryDate.objects.create(historydate=json.dumps(dataa))
