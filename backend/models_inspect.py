# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserCustomuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Option(models.Model):
    option_id = models.AutoField(primary_key=True)
    option_text = models.CharField(max_length=200, blank=True, null=True)
    is_correct = models.BooleanField(blank=True, null=True)
    question = models.ForeignKey('Question', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'option'


class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=400, blank=True, null=True)
    session = models.ForeignKey('Session', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'question'


class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    session_name = models.CharField(max_length=300, blank=True, null=True)
    session_date_start = models.TimeField(blank=True, null=True)
    session_date_end = models.TimeField(blank=True, null=True)
    session_description = models.CharField(max_length=300, blank=True, null=True)
    teacher = models.ForeignKey('Teacher', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session'


class SessionSesion(models.Model):
    sesion_id = models.IntegerField(primary_key=True)
    sesion_name = models.CharField(max_length=100)
    description = models.TextField()
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_sesion'


class Student(models.Model):
    est_id = models.AutoField(primary_key=True)
    est_full_name = models.CharField(max_length=60)
    est_email = models.CharField(unique=True, max_length=100)
    est_phone = models.CharField(max_length=10, blank=True, null=True)
    est_pass = models.CharField(max_length=30, blank=True, null=True)
    est_tab = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class Studentsession(models.Model):
    est = models.OneToOneField(Student, models.DO_NOTHING, primary_key=True)  # The composite primary key (est_id, session_id) found, that is not supported. The first column is selected.
    session = models.ForeignKey(Session, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'studentsession'
        unique_together = (('est', 'session'),)


class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    teacher_document = models.IntegerField(unique=True)
    teacher_full_name = models.CharField(max_length=60)
    teacher_email = models.CharField(unique=True, max_length=100)
    teacher_address = models.CharField(max_length=300, blank=True, null=True)
    teacher_picture = models.CharField(max_length=200, blank=True, null=True)
    teacher_pass = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teacher'


class TeacherTeacher(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    documento = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    validar = models.BooleanField()
    foto = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'teacher_teacher'


class TeacherTeacherGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    teacher = models.ForeignKey(TeacherTeacher, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'teacher_teacher_groups'
        unique_together = (('teacher', 'group'),)


class TeacherTeacherUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    teacher = models.ForeignKey(TeacherTeacher, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'teacher_teacher_user_permissions'
        unique_together = (('teacher', 'permission'),)


class UserCustomuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    full_name = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'user_customuser'


class UserCustomuserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(UserCustomuser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_customuser_groups'
        unique_together = (('customuser', 'group'),)


class UserCustomuserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(UserCustomuser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_customuser_user_permissions'
        unique_together = (('customuser', 'permission'),)
