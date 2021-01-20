from django.db import models

# Create your models here.
class ToDoList(models.Model):
    no = models.AutoField(db_column='NO',primary_key= True)
    pcode = models.CharField(db_column='PCODE', max_length=4)
    user_id = models.CharField(db_column='USER_ID', max_length=50, blank = True, null = True)
    title = models.CharField(db_column='TITLE', max_length=200, blank = True, null = True)
    content = models.CharField(db_column='CONTENT', max_length=1000, blank = True, null = True)
    is_complete = models.IntegerField(db_column='IS_COMPLETE', blank = True, null = True)
    priority = models.IntegerField(db_column='PRIORITY', blank = True, null = True)
    end_date = models.DateField(db_column='END_DATE', blank = True, null = True)


class Apidata(models.Model):
     no = models.AutoField(db_column='NO',primary_key= True)
     pcode = models.CharField(db_column='PCODE', max_length=4)
     contents = models.CharField(db_column='contents', max_length=1000, blank = True, null = True)
     datetime = models.CharField(db_column='datetime', max_length=1000, blank = True, null = True)
     title = models.CharField(db_column='title', max_length=1000, blank = True, null = True)
     url = models.CharField(db_column='url', max_length=1000, blank = True, null = True)
