from django.db import models

# OnlineCourses
# add course
class add_courses(models.Model):
    Course_name=models.CharField(max_length=50,unique='true')
    Details=models.CharField(max_length=100)
    Fees=models.IntegerField()
    Duration=models.CharField(max_length=50)
    Image=models.CharField(max_length=50)
    Mode=models.CharField(max_length=10)

    
class add_enquiry(models.Model):
    e_name=models.CharField(max_length=50)
    e_email=models.CharField(max_length=50)
    e_subject=models.CharField(max_length=100)
    e_message=models.CharField(max_length=50)
