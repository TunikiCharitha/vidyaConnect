import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'vidyaConnect.settings'
import django
django.setup()
from users.models import CustomUser
username='Chuck Bass'
email='iamchuckbass@gmail.com'
userLL = CustomUser.objects.get(username=username)
print(userLL)
last_login = userLL.last_login
print(last_login)