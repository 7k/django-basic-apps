from django.db import models
from django.conf import settings
from basic.people.models import Person
from django.urls import reverse


class Genre(models.Model):
    """Genre model"""
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        db_table = 'music_genres'
        ordering = ('title',)

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('music_genre_detail', kwargs={ 'slug': self.slug })


class Label(models.Model):
    """Label model"""
    title = models.CharField(max_length=100)
    prefix = models.CharField(max_length=20, blank=True)
    slug = models.SlugField(unique=True)
    website = models.URLField(blank=True)

    class Meta:
        db_table = 'music_labels'
        ordering = ('title',)

    def __unicode__(self):
        return '%s' % self.full_title

    @property
    def full_title(self):
        return '%s %s' % (self.prefix, self.title)

    def get_absolute_url(self):
        return reverse('music_label_detail', kwargs={ 'slug': self.slug })


class Band(models.Model):
    """Band model"""
    title = models.CharField(max_length=100)
    prefix = models.CharField(max_length=20, blank=True)
    slug = models.SlugField(unique=True)
    musicians = models.ManyToManyField(Person, blank=True, limit_choices_to={'person_types__slug__exact': 'musician'})
    website = models.URLField(blank=True)

    class Meta:
        db_table = 'music_bands'
        ordering = ('slug', 'title',)

    def __unicode__(self):
        return '%s' % self.full_title

    @property
    def full_title(self):
        return '%s %s' % (self.prefix, self.title)

    def get_absolute_url(self):
        return reverse('music_band_detail', kwargs={ 'slug': self.slug })


class Album(models.Model):
    """Album model"""
    title = models.CharField(max_length=255)
    prefix = models.CharField(max_length=20, blank=True)
    subtitle = models.CharField(blank=True, max_length=255)
    slug = models.SlugField()
    band = models.ForeignKey(Band, blank=True, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, blank=True, null=True, on_delete=models.CASCADE)
    asin = models.CharField(max_length=14, blank=True)
    release_date = models.DateField(blank=True, null=True)
    cover = models.FileField(upload_to='albums', blank=True)
    review = models.TextField(blank=True)
    genre = models.ManyToManyField(Genre, blank=True)
    is_ep = models.BooleanField(default=False)
    is_compilation = models.BooleanField(default=False)

    class Meta:
        db_table = 'music_albums'
        ordering = ('title',)

    def __unicode__(self):
        return '%s' % self.full_title

    def get_absolute_url(self):
        return reverse('music_album_detail', kwargs={ 'slug': self.slug })

    @property
    def full_title(self):
        return '%s %s' % (self.prefix, self.title)

    @property
    def cover_url(self):
        return '%s%s' % (settings.MEDIA_URL, self.cover)

    @property
    def amazon_url(self):
        try:
            return 'http://www.amazon.com/dp/%s/?%s' % (self.asin, settings.AMAZON_AFFILIATE_EXTENTION)
        except:
            return 'http://www.amazon.com/dp/%s/' % self.asin


class Track(models.Model):
    """Tracks model"""
    album = models.ForeignKey(Album, blank=True, null=True, related_name='tracks', on_delete=models.CASCADE)
    band = models.ForeignKey(Band, blank=True, null=True, related_name='tracks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    mp3 = models.FilePathField(path=settings.MEDIA_ROOT+'tracks', match='.*\.mp3$')
    number = models.IntegerField(default=0)

    class Meta:
        db_table = 'music_tracks'
        ordering = ('album', 'number', 'title', 'mp3')

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('music_track_detail', kwargs={ 'slug': self.slug })

    @property
    def mp3_url(self):
        return self.mp3.replace(settings.MEDIA_ROOT, settings.MEDIA_URL)
