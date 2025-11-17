from django.db import models


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=100)
    task_description = models.TextField()
    status = models.CharField(max_length=12)
    due_date = models.DateField(blank=True,null=True)

    class Meta:
        db_table = 'task'
