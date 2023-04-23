from django.contrib.auth.models import User
from django.db import models
# https://django-mptt.readthedocs.io/en/latest/tutorial.html
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(MPTTModel):
    """ Рекурсивная. Для представления подкатегорий """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    parent = TreeForeignKey(
        'self',
        related_name='children',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_list', kwargs={'slug': self.slug})


class Tag(models.Model):
    """ Для добавленяи тэгов к рецепту """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_list_use_tag', kwargs={'tag_slug': self.slug})


class Post(models.Model):
    """ Статья. На неё вещаются рецепты.  """
    author = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, default='')
    image = models.ImageField(upload_to='articles/')
    text = models.TextField()
    category = models.ForeignKey(
        Category,
        related_name='post',
        on_delete=models.SET_NULL,
        null=True
    )
    read_time = models.CharField(max_length=35, blank=False, null=True)
    tags = models.ManyToManyField(Tag, related_name='post')
    create_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'post_detail',
            kwargs={'category_slug': self.category.slug,
                    'post_slug': self.slug}
        )


class Recipe(models.Model):
    """ Рецепт блюда """
    name = models.CharField(max_length=100, unique=True)
    serves = models.CharField(max_length=50)
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    Ingredients = RichTextField() # Класс из библиотеки ckeditor
    directions = RichTextField()
    post = models.ForeignKey(
        Post,
        related_name='recipe',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.name


class Comment(models.Model):
    """ Комментарий к посту """
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.CharField(max_length=150)
    message = models.TextField(max_length=500)
    #create_at = models.DateTimeField(auto_now_add=True, default=None)
    post = models.ForeignKey(
        Post,
        related_name='comment',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
