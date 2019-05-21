import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'vidyaConnect.settings'
import django
django.setup()
from users.models import CustomUser,Profile
username='Harvey Specter'
#email='iamchuckbass@gmail.com'
userLL = CustomUser.objects.get(username=username)
#userLL=CustomUser.objects.get(username=self.request.user.username)
print(userLL)
userprof=Profile.objects.get(user=userLL)
print(userprof)
cat = userprof.category
print(cat)