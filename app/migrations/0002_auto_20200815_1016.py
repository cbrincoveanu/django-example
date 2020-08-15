# Generated by Django 3.1 on 2020-08-15 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='userasset',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.profile'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='userasset',
            unique_together={('profile', 'currency')},
        ),
        migrations.RemoveField(
            model_name='userasset',
            name='user_profile',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
