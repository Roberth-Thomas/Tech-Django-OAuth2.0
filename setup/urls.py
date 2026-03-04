from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tech.urls')), # -> '' = rotas principais do app 'tech'
                #   ('tech.urls') lista de de urls que vem da pasta tech / ele controla e gerencia a aplicação.
     # E isso se repete para o allauth: indicamos uma lista de urls lá da pasta venv/Lib/allath
     # Ela é basicamente o arquivo urls que criamos na pasta tech, mas só que demos um pip install django-allauth e 
     #                                                                  pip install "django-allauth[socialaccount]"
     # E isso é aproveitar algo que veio de outras pessoas que criaram.
    path('accounts/', include('allauth.urls')),
    #    'acconts/' = rota e recebo um inclusão(include) lá do app 'allauth.urls'
]
