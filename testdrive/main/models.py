from django.db import models


class Status(models.Model):
    title = models.CharField(verbose_name='Название', max_length=60)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Orders(models.Model):
    created = models.DateTimeField()
    owner = models.ForeignKey('auth.User', verbose_name='Автор', related_name='orders_user', on_delete=models.CASCADE)
    status = models.ForeignKey('Status', verbose_name='Статуст', related_name='orders_status', on_delete=models.CASCADE)
    car = models.ForeignKey('Cars', verbose_name='Автомобиль', related_name='orders_car', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.created

    class Meta:
        ordering = ['created']
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Fuel(models.Model):
    title = models.CharField(verbose_name='Название', max_length=60)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Тип топлива'
        verbose_name_plural = 'Тип топлива'


class DriveType(models.Model):
    title = models.CharField(verbose_name='Название', max_length=60)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Тип привода'
        verbose_name_plural = 'Тип привода'


class Cars(models.Model):
    stamp = models.ForeignKey('auth.User', verbose_name='На дату', related_name='orders_user', on_delete=models.CASCADE)
    model = models.CharField(verbose_name='Модель', max_length=50)
    engine_capacity = models.FloatField(verbose_name='Объём двигателя')
    engine_power = models.IntegerField(verbose_name='Мощность двигателя')
    fuel = models.ForeignKey('Fuel', verbose_name='Тип топлива', related_name='cars_fuel', on_delete=models.CASCADE)
    drive_type = models.ForeignKey('DriveType', verbose_name='Тип привода', related_name='cars_drivetype',
                                   on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f'{self.stamp} {self.model}'

    class Meta:
        ordering = ['stamp']
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
