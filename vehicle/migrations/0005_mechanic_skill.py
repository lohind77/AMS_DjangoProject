

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0004_auto_20200926_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='mechanic',
            name='skill',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
