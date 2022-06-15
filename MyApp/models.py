from django.db import models

# Create your models here.
class Contact(models.Model):
    name  = models.CharField(max_length=60)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=12)
    desc  = models.TextField()
    date  = models.DateField()

    def __str__(self):
        return self.name

class Course(models.Model):
    course_id    = models.AutoField
    name         = models.CharField(max_length=50)
    desc         = models.CharField(max_length=500)
    publish_date = models.DateField()
    section_1    = models.CharField(max_length=50, default="")
    sec_1_link_1 = models.CharField(max_length=100, default="")
    sec1_lnk1_name = models.CharField(max_length=50, default="")
    sec_1_link_2 = models.CharField(max_length=100, default="")
    sec1_lnk2_name = models.CharField(max_length=50, default="")
    sec_1_link_3 = models.CharField(max_length=100, default="")
    sec1_lnk3_name = models.CharField(max_length=50, default="")
    sec_1_link_4 = models.CharField(max_length=100, default="")
    sec1_lnk4_name = models.CharField(max_length=50, default="")
    section_2    = models.CharField(max_length=50, default="")
    sec_2_link_1 = models.CharField(max_length=100, default="")
    sec2_lnk1_name = models.CharField(max_length=50, default="")
    sec_2_link_2 = models.CharField(max_length=100, default="")
    sec2_lnk2_name = models.CharField(max_length=50, default="")
    sec_2_link_3 = models.CharField(max_length=100, default="")
    sec2_lnk3_name = models.CharField(max_length=50, default="")
    sec_2_link_4 = models.CharField(max_length=100, default="")
    sec2_lnk4_name = models.CharField(max_length=50, default="")
    section_3    = models.CharField(max_length=50, default="")
    sec_3_link_1 = models.CharField(max_length=100, default="")
    sec3_lnk1_name = models.CharField(max_length=50, default="")
    sec_3_link_2 = models.CharField(max_length=100, default="")
    sec3_lnk2_name = models.CharField(max_length=50, default="")
    sec_3_link_3 = models.CharField(max_length=100, default="")
    sec3_lnk3_name = models.CharField(max_length=50, default="")
    sec_3_link_4 = models.CharField(max_length=100, default="")
    sec3_lnk4_name = models.CharField(max_length=50, default="")
    section_4    = models.CharField(max_length=50, default="")
    sec_4_link_1 = models.CharField(max_length=100, default="")
    sec4_lnk1_name = models.CharField(max_length=50, default="")
    sec_4_link_2 = models.CharField(max_length=100, default="")
    sec4_lnk2_name = models.CharField(max_length=50, default="")
    sec_4_link_3 = models.CharField(max_length=100, default="")
    sec4_lnk3_name = models.CharField(max_length=50, default="")
    sec_4_link_4 = models.CharField(max_length=100, default="")
    sec4_lnk4_name = models.CharField(max_length=50, default="")
    section_5    = models.CharField(max_length=50, default="")
    sec_5_link_1 = models.CharField(max_length=100, default="")
    sec5_lnk1_name = models.CharField(max_length=50, default="")
    sec_5_link_2 = models.CharField(max_length=100, default="")
    sec5_lnk2_name = models.CharField(max_length=50, default="")
    sec_5_link_3 = models.CharField(max_length=100, default="")
    sec5_lnk3_name = models.CharField(max_length=50, default="")
    sec_5_link_4 = models.CharField(max_length=100, default="")
    sec5_lnk4_name = models.CharField(max_length=50, default="")
    quiz         = models.CharField(max_length=50)
    image        = models.ImageField(upload_to="static/img")

    def __str__(self):
        return self.name

class Quizze(models.Model):
    name    = models.CharField(max_length=20)
    link    = models.CharField(max_length=50)

    def __str__(self):
        return self.name
