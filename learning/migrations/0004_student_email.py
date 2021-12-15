# Generated on 2021-12-15 21:14 to add email field which will be used by boto3 down the line for SNS

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0003_alter_module_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='nakultyagi27@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]
