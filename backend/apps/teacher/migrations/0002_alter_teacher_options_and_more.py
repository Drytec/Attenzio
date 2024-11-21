# Generated by Django 5.1.2 on 2024-11-19 19:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={},
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='documento',
            new_name='teacher_document',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='apellidos',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='email',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='foto',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='id',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='password',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='telefono',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='username',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='validar',
        ),
        migrations.AddField(
            model_name='teacher',
            name='customuser_ptr',
            field=models.OneToOneField(auto_created=True, default=12, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher_address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher_picture',
            field=models.ImageField(blank=True, null=True, upload_to='teacher_pictures/'),
        ),
        migrations.AlterModelTable(
            name='teacher',
            table='teacher',
        ),
    ]
