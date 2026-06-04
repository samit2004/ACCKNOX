from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db import transaction
import threading 
import time

log = []

def slow_receiver(sender, **kwargs):
    log.append(f"receiver thread: {threading.current_thread().name}")
    log.append("receiver: START")
    time.sleep(2)
    log.append("receiver: END")

post_save.connect(slow_receiver, sender=User)



def transaction_receiver(sender, instance, **kwargs):
   
    log.append(f"transaction is open in receiver: {not transaction.get_autocommit()}")

post_save.connect(transaction_receiver, sender=User)