from django.http import HttpResponse

import uuid
from models import SampleDO

def index(request):
    uuid1 = uuid.uuid1().hex
    response = "Generated UUID: <b>" + uuid1 + "</b><BR><BR>"
    sampleDO = SampleDO(uuid=uuid1)
    sampleDO.save()
    hexString = "List of all UUIDs from database: <BR> <table border=\"1\"><tr><td>UUID</td></tr>"
    for sampleDO in SampleDO.objects.all():
        hexString = hexString + "<tr><td>" + sampleDO.uuid + "</td></tr>"
    hexString = hexString + "</table><BR>"
    return HttpResponse("CumuLogic Sample DB Application: <a href=\"#\" onclick=\"window.location.reload(true);\">Generate UUID</a> <BR><BR>" + response + hexString)
