from django.db import models


 

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.created_at} - {self.updated_at}"



class Profile(BaseModel):
    full_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="profile/")
    bio = models.TextField()


    def __str__(self):
        return self.full_name
    

class Skill(BaseModel):
    title = models.CharField(max_length=50)
    percentage = models.IntegerField(default=0)
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.title
    


class About(BaseModel):
    experience = models.TextField()
    total_projects = models.IntegerField(default=0)
    total_users = models.IntegerField(default=0)
    salary = models.IntegerField()


    def __str__(self):
        return self.id
    


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Portfolio(BaseModel):
    autor = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="portfolio/")
    link = models.URLField()
    used_tools = models.ManyToManyField(Skill)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    completed_at = models.DateField()
    desc = models.TextField()


    def __str__(self):
        return self.title
    

class Post(BaseModel):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to="post/", default=1)
    desc = models.TextField()
    count_views = models.PositiveIntegerField(default=1)


    def __str__(self) -> str:
        return f"{self.title} - {self.author}"
    

class Service(BaseModel):
    title = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    desc = models.TextField()


    def __str__(self):
        return self.title
    
