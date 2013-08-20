from django.db import models, connections


class SampleDO(models.Model):
    """Details of the SaaS User
    """
    id = models.AutoField(primary_key=True)
    uuid = models.CharField(max_length='40')
