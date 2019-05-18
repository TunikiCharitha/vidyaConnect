from django.test import TestCase
from models import CustomUser
# Create your tests here.
username='Jason Dilaurentis'
userLL = CustomUser.objects.get(username=username)
print(userLL)
last_login = userLL.last_login
print(last_login)