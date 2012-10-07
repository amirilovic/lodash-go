
# Apprendre Django

### Installation
+ installer python
+ installer pip ( package manager)
+ installer django

+ créer un project
  + <code>django-admin.py startproject [nomduprojet]</code>
+ démarrer le serveur
  + dans le dossier du project
    + <code>python manage.py runserver</code>

#### Configurer le project
  + modifier le fichier settings.py

###### Utiliser sqlite3 comme RDBMS:

<pre>
<code>
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  
        'NAME': 'mysite.db'
    }
}
</code>
</pre>

###### Activer l'admin : 

+ décommenter la ligne 119 du fichier settings.py
  + <code>'django.contrib.admin',</code>
+ dans le fichier urls.py
  + décommenter les lignes suvantes
<pre><code>
from django.contrib import admin
admin.autodiscover()
# (...)
url(r'^admin/', include(admin.site.urls)),
</code></pre>
+ créer les tables associées à l'admin :
<code>
  python manager.py syncdb
</code>

#### Créer une application
+ le nom de l'application est main

<code>
  python manager.py startapp main
</code>

##### Créer un modèle 

+ exemple main\models.py ( installer django-taggit avec pip si absent '<code>pip install django-taggit</code>')

<pre><code>
  from django.db import models
  from taggit.managers import TaggableManager

  # Create your models here.


  class Post(models.Model):

    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField()
    tags = TaggableManager()

    def __unicode__(self):
        return self.title
</code></pre>

+ synchroniser la base de donnée
  <code>python manager.py syncdb</code>

##### Créer une page admin pour le modèle

+ créer un fichier admin.py dans le dossier de l'application ( ex : main )
+ ajouter le code suivant

<pre><code>
  from django.contrib import admin
  from main.models import Post
  admin.site.register(Post)
</code></pre>

##### référencer l'application main dans settings.py

<pre><code>
  INSTALLED_APPS = (
        [...]
        'taggit',
        'main'
      )
</code></pre>