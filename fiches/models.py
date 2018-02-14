from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Format(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Fiche(models.Model):
    project_title = models.CharField(max_length=300)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    format = models.ForeignKey(Format, on_delete=models.CASCADE,null=True,blank=True)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.client,self.project_title)


