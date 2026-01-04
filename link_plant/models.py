from django.db import models

# Each class is a table in our database
# Profiles -> Link
class Profile(models.Model):
    BG_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('yellow', 'Yellow')
    ]
    # name, slug , bg_color
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100)
    bg_color = models.CharField(max_length=50, choices=BG_CHOICES)
    #link_set by default
    #profile.links

    def __str__(self):
        return self.name
    
class Link(models.Model):
    # text, url, profile
    text = models.CharField(max_length=255)
    url = models.URLField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='links')

# What does related_name do? So, basically, the profile field(parent class) lives on the Link table.So if we wanted to access a certain profile that's associated with a Link
# We could just look up a specific link and then look up that profile through 

# manytomany = many profiles can be associated with many link and vice versa
# one to one = each profile could have one link and one link would be associated with one profile
# one to many