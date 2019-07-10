from django.db import models

# Create your models here.

class Version(models.Model):
    ios_available_version = models.CharField(max_length=20)
    ios_current_version = models.CharField(max_length=20)
    ios_updateinfo = models.TextField()
    ios_force_updateinfo = models.TextField(default="sorry, your app version is too low, please update, thx")
    ios_url = models.CharField(max_length=200)

    def to_dict(self):
        dict = {}
        dict["IOSAvailableVersion"] = self.ios_available_version
        dict["IOSCurrentVersion"] = self.ios_current_version
        dict["IOSUpdateInfo"] = self.ios_updateinfo
        dict["IOSForceUpdateInfo"] = self.ios_force_updateinfo
        dict["IOSUrl"] = self.ios_url
        return dict