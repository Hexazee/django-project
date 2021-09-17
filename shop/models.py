from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
from django.utils.text import slugify

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=70, help_text='Nama Lengkap')
    email = models.EmailField(
        max_length=50,
        help_text='Masukan Email dengan benar!')

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField()
    slug = models.SlugField(editable=False)

    def save(self):
        self.slug = slugify(self.name)
        super(Product, self).save()

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.id}"


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=150)
    provinsi = models.CharField(max_length=50)
    kota = models.CharField(max_length=50)
    kode_pos = models.CharField(max_length=10)
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer


class SpecProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    microcontroller = models.CharField(max_length=20, verbose_name="Microcontroller")
    operating_voltage = models.CharField(max_length=10, verbose_name="Operating Voltage")
    input_voltage_recomended = models.CharField(max_length=10, verbose_name="Input Voltage Recomended")
    input_voltage_limit = models.CharField(max_length=10, verbose_name="Input Voltage Limit")
    IO_pins = models.IntegerField(verbose_name="I/O Pins")
    analog_pins = models.IntegerField(verbose_name="Analog Pins")
    pwm_IO_pins = models.IntegerField(verbose_name="PWM I/O Pins")
    dc_current_per_IO_pin = models.IntegerField(verbose_name="DC Current Per I/O Pin")
    dc_current_for_3_3v_pin = models.IntegerField(verbose_name="DC Current for 3.3V Pin")
    flash_memory = models.CharField(max_length=100, verbose_name="Flash Memory")
    sram = models.CharField(max_length=20, verbose_name="SRAM")
    eeprom = models.CharField(max_length=20, verbose_name="EEPROM")
    clock_speed = models.IntegerField(verbose_name="Clock Speed")
    led_builtin = models.IntegerField(verbose_name="LED BuiltIn")
    length = models.FloatField(verbose_name="Length")
    width = models.FloatField(verbose_name="Width")
    weight = models.IntegerField(verbose_name="Weight")

    def __str__(self):
        return f'{self.product}'
