# Generated by Django 3.2.5 on 2021-07-19 12:50

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
            name='Customer',
            fields=[
                ('Id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50, verbose_name='Name')),
                ('Locality', models.CharField(max_length=200, verbose_name='Locality')),
                ('City', models.CharField(max_length=200, verbose_name='City')),
                ('ZipCode', models.IntegerField(verbose_name='ZipCode')),
                ('State', models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Goa', 'Goa'), ('Haryana', 'Haryana'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Tamil Nadu', 'Tamil Nadu')], max_length=50)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=200, verbose_name='Title')),
                ('Selling_price', models.FloatField(verbose_name='Selling Price')),
                ('Discounted_Price', models.FloatField()),
                ('Descriptio', models.TextField(verbose_name='Description')),
                ('Brand', models.CharField(max_length=50, verbose_name='Brand')),
                ('Category', models.CharField(choices=[('MT', 'Men Top Wear'), ('MB', 'Men Bottom Wear'), ('WEC', 'Women Ethnic Churidar '), ('WES', 'Women Ethnic Saree '), ('WWT', 'Women Western Top'), ('WWB', 'Women Western Bottom'), ('WW', 'Women Western Wear'), ('MO', 'Mobile'), ('LA', 'Laptop')], max_length=5)),
                ('Product_image', models.ImageField(upload_to='product_img')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('Id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Quantity', models.PositiveIntegerField(default=1)),
                ('Ordered_date', models.DateTimeField(auto_now_add=True)),
                ('Status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Packed', 'Packed'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='Pending', max_length=50)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('Id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Quantity', models.PositiveIntegerField(default=1)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]