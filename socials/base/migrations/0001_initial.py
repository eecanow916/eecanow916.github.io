from django.conf import settings
from django.db import migrations, models
from django.db.models.deletion import CASCADE
import ckeditor.fields

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', settings.AUTH_USER_MODEL),  # Example dependency, update according to your app structure
    ]

    operations = [
        migrations.CreateModel(
            name='FollowersCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(on_delete=CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LikePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('fname', models.CharField(max_length=100, blank=True)),
                ('lname', models.CharField(max_length=100, blank=True)),
                ('username', models.CharField(max_length=100, blank=True)),
                ('profileimg', models.ImageField(default='profile_images/blank-profile-picture.png', upload_to='profile_images')),
                ('user', models.OneToOneField(null=True, on_delete=CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('title_tag', models.CharField(default='', max_length=255)),
                ('caption', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('post_date', models.DateField(auto_now_add=True)),
                ('location', models.CharField(default='', max_length=255)),
                ('no_of_likes', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=CASCADE, to=settings.AUTH_USER_MODEL)),  # Or use settings.AUTH_USER_MODEL directly
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=CASCADE, related_name='comments', to='base.post')),
            ],
        ),
    ]
