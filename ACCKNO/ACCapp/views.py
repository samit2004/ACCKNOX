from django.http import HttpResponse
from django.contrib.auth.models import User
import ACCapp.signals as s
import threading 
import time
from django.db import transaction





def test_signal(request):
    s.log.clear()
    s.log.append(f"caller thread: {threading.current_thread().name}")
    s.log.append("before send")
    User.objects.create_user(f"testuser{int(time.time())}", password="pass")
    s.log.append("after send")
    
    
    with transaction.atomic():                                         
        s.log.append(f"transaction is open in caller: {not transaction.get_autocommit()}")
        User.objects.create_user(f"testuser{int(time.time())}", password="pass")
        s.log.append("after send")

    return HttpResponse("<br><br>".join(s.log))