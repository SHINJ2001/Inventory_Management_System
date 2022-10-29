# Generated by Django 4.1.2 on 2022-10-28 17:29

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('1', 'manager'), ('2', 'staff')], default='1', max_length=10)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='completed_processes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_produced', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Managers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='manufacturers',
            fields=[
                ('lead', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('lead_contact', models.IntegerField(null=True)),
                ('lead_email', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Operations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_name', models.CharField(choices=[('1', 'Procuring Raw Material'), ('2', 'Cleaning'), ('3', 'Heating'), ('4', 'Shaping'), ('5', 'Cooling'), ('6', 'Cutting'), ('7', 'Resting'), ('8', 'Polishing'), ('9', 'Packing')], default='1', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='parts',
            fields=[
                ('part_name', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='rejections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rejection_date', models.DateField()),
                ('rejection_amount', models.IntegerField()),
                ('operation_status', models.CharField(default='0', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='requirement',
            fields=[
                ('order_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('order_date', models.DateField()),
                ('date_of_transport', models.DateField()),
                ('acceptance_status', models.CharField(max_length=1)),
                ('deadline', models.DateField()),
                ('customer_email', models.CharField(max_length=100)),
                ('customer_phone1', models.CharField(max_length=10)),
                ('customer_phone2', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='targets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production', models.IntegerField()),
                ('current_average', models.FloatField()),
                ('date_of_production', models.DateField()),
                ('expected_average', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='tools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tool_name', models.CharField(max_length=40)),
                ('tool_life', models.IntegerField()),
                ('bought_on', models.DateField(default=datetime.datetime(2022, 10, 28, 17, 29, 34, 448628))),
                ('parts_manufactured', models.IntegerField(null=True)),
                ('num_polished', models.IntegerField(null=True)),
                ('last_polished_on', models.DateField(null=True)),
                ('price', models.CharField(max_length=8)),
            ],
        ),
        migrations.AddConstraint(
            model_name='tools',
            constraint=models.UniqueConstraint(fields=('bought_on', 'tool_name'), name='prim_key_for_tools'),
        ),
        migrations.AddField(
            model_name='targets',
            name='operation_lead',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.manufacturers'),
        ),
        migrations.AddField(
            model_name='targets',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.requirement'),
        ),
        migrations.AddField(
            model_name='staff',
            name='admin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='requirement',
            name='part_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.parts'),
        ),
        migrations.AddField(
            model_name='rejections',
            name='operations_required',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.operations'),
        ),
        migrations.AddField(
            model_name='rejections',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.requirement'),
        ),
        migrations.AddField(
            model_name='operations',
            name='tool_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.tools'),
        ),
        migrations.AddField(
            model_name='managers',
            name='admin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='completed_processes',
            name='operation_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.operations'),
        ),
        migrations.AddField(
            model_name='completed_processes',
            name='order_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.requirement'),
        ),
        migrations.AddField(
            model_name='completed_processes',
            name='part_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.parts'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
