# Generated by Django 3.2.15 on 2022-09-22 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=30, verbose_name='Key')),
                ('value', models.CharField(max_length=200, verbose_name='Value')),
                ('autoload', models.BooleanField(default=False, verbose_name='Autoload')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'db_table': 'app_option',
            },
        ),
        migrations.CreateModel(
            name='ResetRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(db_index=True, max_length=60, verbose_name='Email')),
                ('token', models.CharField(db_index=True, max_length=200, verbose_name='Token')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('expire_at', models.DateTimeField(verbose_name='Expire at')),
                ('messages_count', models.PositiveSmallIntegerField(verbose_name='Messages Count')),
            ],
            options={
                'db_table': 'app_reset_request',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('uuid', models.CharField(db_index=True, max_length=60, verbose_name='uuid')),
                ('hostname', models.CharField(max_length=100, verbose_name='Hostname')),
                ('ipaddress', models.CharField(max_length=100, verbose_name='IP Address')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'db_table': 'app_server',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(db_index=True, max_length=60, verbose_name='UUID')),
                ('status', models.CharField(choices=[
                    ('pending', 'pending'),
                    ('failed', 'failed'),
                    ('succeeded', 'succeeded')
                ], default='pending', max_length=20, verbose_name='Status')),
                ('payload', models.TextField(verbose_name='payload')),
                ('result', models.TextField(verbose_name='Result')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'db_table': 'app_task',
            },
        ),
        migrations.CreateModel(
            name='UserMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=60, verbose_name='Meta key')),
                ('value', models.TextField(verbose_name='Meta Value')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Related User')),
            ],
            options={
                'db_table': 'app_user_meta',
            },
        ),
        migrations.CreateModel(
            name='ServerMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=60, verbose_name='Meta key')),
                ('value', models.TextField(verbose_name='Meta Value')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.server', verbose_name='Related Server')),
            ],
            options={
                'db_table': 'app_server_meta',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(default='', max_length=100, verbose_name='Job Title')),
                ('company', models.CharField(default='', max_length=60, verbose_name='Company')),
                ('personal_url', models.CharField(default='', max_length=100, verbose_name='Personal URL')),
                ('api_key', models.CharField(default='', max_length=100, verbose_name='API Key')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Related user')),
            ],
            options={
                'db_table': 'app_profile',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highlight', models.CharField(max_length=200, verbose_name='Highlight')),
                ('notification', models.CharField(max_length=200, verbose_name='Notification')),
                ('url', models.CharField(max_length=200, verbose_name='URL')),
                ('type', models.CharField(choices=[
                    ('pending', 'PENDING'),
                    ('failed', 'FAILED'),
                    ('passed', 'PASSED'),
                    ('error', 'ERROR'),
                    ('message', 'MESSAGE')
                ], default='message', max_length=20, verbose_name='Type')),
                ('delivered', models.BooleanField(default=False, verbose_name='Delivered')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.task', verbose_name='Related Task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Related user')),
            ],
            options={
                'db_table': 'app_notification',
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.TextField(verbose_name='Activity')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Related User')),
            ],
            options={
                'db_table': 'app_activity',
            },
        ),
    ]
