
# Apprendre Django

### Installation
+ installer python http://www.python.org/download/
+ installer pip ( package manager) http://pypi.python.org/pypi/pip
+ installer django https://www.djangoproject.com/

+ créer un project
  + <code>django-admin.py startproject [nomduprojet]</code>
+ démarrer le serveur
  + dans le dossier du project
    + <code>python manage.py runserver</code>

### Nomenclature
  Un ***projet*** Django est crée pas la commande startproject et contient de multiple applications (exemple : un blog, un shop, )

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

<pre>
  <code>
    from django.contrib import admin
    admin.autodiscover()
    # (...)
    url(r'^admin/', include(admin.site.urls)),
  </code>
</pre>

+ créer les tables associées à l'admin :

<code>
  python manager.py syncdb
</code>

+ Entrer ses informations de login/password pour l'administrateur
+ On doit maintenant pouvoir se logger dans l'admin à l'adresse suivante : 
 <b>http://localhost:8000/admin</b>

+ Si le serveur n'est pas lancé le lancer aver <code>python manager.py runserver</code>

#### Créer une application

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

On peut maintenant créer et éditer des posts dans l'administration

##### référencer l'application main dans settings.py

<pre>
<code>
  INSTALLED_APPS = (
        [...]
        'taggit',
        'main'
      )
</code>
</pre>

##### configurer les routes :
+ Créer un fichiers main/urls.py avec le code suivant :

<pre>
<code>

  from django.conf.urls.defaults import patterns, include, url
  from django.views.generic import ListView, DetailView
  from django.contrib.syndication.views import Feed
  from main.models import Post


  class BlogFeed(Feed):
      title = "MySite"
      description = "Some feeds about cloud technologies"
      link = "/blog/feed"

      def items(self):
          return Post.objects.all().order_by("-created")[:4]

      def item_title(self, item):
          return item.title

      def item_description(self, item):
          return item.body

      def item_link(self, item):
          return u"/blog/%d" % item.id


  urlpatterns = patterns('',
    url(r'^feed$', BlogFeed()),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(
      model=Post,
      template_name="post.html")),
    url(r'^tag/(?P<tag>\w+)$', 'main.views.tagpage'),
    url(r'^archives$', ListView.as_view(
      queryset=Post.objects.all().order_by("-created"),
      template_name="archive.html")),
    url(r'^', ListView.as_view(
      queryset=Post.objects.all().order_by("-created")[:2],
      template_name="blog.html")),
    )
</code>
</pre>

+ chaque route est une expression régulière à laquelle est associée une expression
  + Exemple : afficher la liste de articles : 
  <pre><code>
      urlpatterns = patterns('',
      url(r'^', ListView.as_view(
        queryset=Post.objects.all().order_by("-created")[:2],
        template_name="blog.html")),
      )
  </code></pre>
  est une route qui est ensuite rendue via un template nommé blog.html dans le dossier templates

#### Templates 
+ les templates sont définies dans le dossier "templates" d'une application
  + https://docs.djangoproject.com/en/1.4/topics/templates/


### Déployer son application Django sur Heroku
+ sources  : https://devcenter.heroku.com/articles/django

#### Créer une liste des dépendances du projet
<code> pip freeze > requirements.txt</code>

## Autres frameworks python
+ [Flash](http://flask.pocoo.org/)
