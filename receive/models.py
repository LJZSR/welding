from django.db import models

# Create your models here.

class UpdataTime(models.Model):
    time = models.CharField(max_length=128)
    def __str__(self):
        return self.time

class SoundOrigin(models.Model):
    time = models.ForeignKey(UpdataTime)
    sound = models.FloatField()
    class Meta:
        managed = True

class ImageOrigin(models.Model):
    time = models.ForeignKey(UpdataTime)
    image = models.CharField(max_length=1024)
    class Meta:
        managed = True

class CurrentOrigin(models.Model):
    time = models.ForeignKey(UpdataTime)
    current = models.FloatField()
    class Meta:
        managed = True

class VoltageOrigin(models.Model):
    time = models.ForeignKey(UpdataTime)
    voltage = models.FloatField()
    class Meta:
        managed = True

class RobotOrigin(models.Model):
    time = models.ForeignKey(UpdataTime)
    robot = models.CharField(max_length=1024)
    class Meta:
        managed = True
