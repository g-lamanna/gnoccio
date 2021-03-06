from django.db import models

class Dinner_Post(models.Model):
  title = models.CharField(max_length=100)
  image = models.ImageField(default='default.JPG', upload_to='image_posts')
  button_id= models.CharField(max_length=100,default='')
  recipe_id= models.CharField(max_length=100,default='')
  serving = models.CharField(max_length=100,default='')
  fryer = models.CharField(max_length=100,default='')
  stars = models.IntegerField(default='')
  star_id= models.CharField(max_length=100,default='')
  instructions_1 = models.TextField(max_length=500,default='.')
  instructions_2 = models.TextField(max_length=500,default='.')
  instructions_3 = models.TextField(max_length=500,default='.')
  instructions_4 = models.TextField(max_length=500,default='.')
  instructions_5 = models.TextField(max_length=500,default='.')
  instructions_6 = models.TextField(max_length=500,default='.')
  instructions_7 = models.TextField(max_length=500,default='.')
  instructions_8 = models.TextField(max_length=500,default='.')
  instructions_9 = models.TextField(max_length=500,default='.')
  instructions_10 = models.TextField(max_length=500,default='.')
  ingredients_1 = models.TextField(max_length=500,default='.')
  ingredients_2 = models.TextField(max_length=500,default='.')
  ingredients_3 = models.TextField(max_length=500,default='.')
  ingredients_4 = models.TextField(max_length=500,default='.')
  ingredients_5 = models.TextField(max_length=500,default='.')
  ingredients_6 = models.TextField(max_length=500,default='.')
  ingredients_7 = models.TextField(max_length=500,default='.')
  ingredients_8 = models.TextField(max_length=500,default='.')
  ingredients_9 = models.TextField(max_length=500,default='.')
  ingredients_10 = models.TextField(max_length=500,default='.')
  cook_time_lower = models.IntegerField(default=1)
  cook_time_upper = models.IntegerField(default=1)
  prep_time_lower = models.IntegerField(default=1)
  prep_time_upper = models.IntegerField(default=1)

  def __str__(self):
    return self.title

class Snack_Post(models.Model):
  title = models.CharField(max_length=100)
  image = models.ImageField(default='default.JPG', upload_to='image_posts')
  button_id = models.CharField(max_length=100,default='')
  recipe_id= models.CharField(max_length=100,default='')
  serving = models.CharField(max_length=100,default='')
  fryer = models.CharField(max_length=100,default='')
  stars = models.IntegerField(default='')
  star_id= models.CharField(max_length=100,default='')
  instructions_1 = models.TextField(max_length=500,default='.')
  instructions_2 = models.TextField(max_length=500,default='.')
  instructions_3 = models.TextField(max_length=500,default='.')
  instructions_4 = models.TextField(max_length=500,default='.')
  instructions_5 = models.TextField(max_length=500,default='.')
  instructions_6 = models.TextField(max_length=500,default='.')
  instructions_7 = models.TextField(max_length=500,default='.')
  instructions_8 = models.TextField(max_length=500,default='.')
  instructions_9 = models.TextField(max_length=500,default='.')
  instructions_10 = models.TextField(max_length=500,default='.')
  ingredients_1 = models.TextField(max_length=500,default='.')
  ingredients_2 = models.TextField(max_length=500,default='.')
  ingredients_3 = models.TextField(max_length=500,default='.')
  ingredients_4 = models.TextField(max_length=500,default='.')
  ingredients_5 = models.TextField(max_length=500,default='.')
  ingredients_6 = models.TextField(max_length=500,default='.')
  ingredients_7 = models.TextField(max_length=500,default='.')
  ingredients_8 = models.TextField(max_length=500,default='.')
  ingredients_9 = models.TextField(max_length=500,default='.')
  ingredients_10 = models.TextField(max_length=500,default='.')
  cook_time_lower = models.IntegerField(default=1)
  cook_time_upper = models.IntegerField(default=1)
  prep_time_lower = models.IntegerField(default=1)
  prep_time_upper = models.IntegerField(default=1)

  def __str__(self):
    return self.title

class Dessert_Post(models.Model):
  title = models.CharField(max_length=100)
  image = models.ImageField(default='default.JPG', upload_to='image_posts')
  button_id = models.CharField(max_length=500,default='')
  recipe_id= models.CharField(max_length=100,default='')
  serving = models.CharField(max_length=100,default='')
  fryer = models.CharField(max_length=100,default='')
  stars = models.IntegerField(default='')
  star_id= models.CharField(max_length=100,default='')
  instructions_1 = models.TextField(max_length=500,default='.')
  instructions_2 = models.TextField(max_length=500,default='.')
  instructions_3 = models.TextField(max_length=500,default='.')
  instructions_4 = models.TextField(max_length=500,default='.')
  instructions_5 = models.TextField(max_length=500,default='.')
  instructions_6 = models.TextField(max_length=500,default='.')
  instructions_7 = models.TextField(max_length=500,default='.')
  instructions_8 = models.TextField(max_length=500,default='.')
  instructions_9 = models.TextField(max_length=500,default='.')
  instructions_10 = models.TextField(max_length=500,default='.')
  ingredients_1 = models.TextField(max_length=500,default='.')
  ingredients_2 = models.TextField(max_length=500,default='.')
  ingredients_3 = models.TextField(max_length=500,default='.')
  ingredients_4 = models.TextField(max_length=500,default='.')
  ingredients_5 = models.TextField(max_length=500,default='.')
  ingredients_6 = models.TextField(max_length=500,default='.')
  ingredients_7 = models.TextField(max_length=500,default='.')
  ingredients_8 = models.TextField(max_length=500,default='.')
  ingredients_9 = models.TextField(max_length=500,default='.')
  ingredients_10 = models.TextField(max_length=500,default='.')
  cook_time_lower = models.IntegerField(default=1)
  cook_time_upper = models.IntegerField(default=1)
  prep_time_lower = models.IntegerField(default=1)
  prep_time_upper = models.IntegerField(default=1)

  def __str__(self):
    return self.title

class Wine_Post(models.Model):
  title = models.CharField(max_length=100)
  image = models.ImageField(default='default.JPG', upload_to='image_posts')
  description = models.TextField(max_length=500,default='.')
  #article_id = models.CharField(max_length=500,default='')

  def __str__(self):
    return self.title

class Tips_Post(models.Model):
  title = models.CharField(max_length=100)
  image = models.ImageField(default='default.JPG', upload_to='image_posts')
  description = models.TextField(max_length=500,default='.')
  #article_id = models.CharField(max_length=500,default='')

  def __str__(self):
    return self.title

class Wine_Generator(models.Model):
  name = models.CharField(max_length=20)
  overview = models.TextField(max_length=100,default='.')
  blend = models.TextField(max_length=20,default='.')


  def __str__(self):
    return self.title


