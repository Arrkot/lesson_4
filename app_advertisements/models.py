from django.db import models
from django.contrib import admin
# Create your models here.

class Advertisements(models.Model):

    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг", help_text="Отметьте если торг уместен")
    create_at = models.DateTimeField( auto_now_add=True) #"Датта создания",
    update_at = models.DateTimeField(auto_now=True) #"Датта обновления",
    # uuu = models.CharField('uuu', max_length=22, default='')

    def __str__(self):
        return(f' Advertisement(id={self.id}, title = {self.title}, price = {self.price})') #<Advertisement: Advertisement(id=1, title=Заголовок №1, price=100.00)>

    class Meta:
        db_table = "Advertisements"

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.create_at.date() == timezone.now().date():
            created_time = self.create_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold">'
                'Сегодня в {}</span>', created_time
            )
        return self.create_at.strftime('%d.%m.%Y в %H:%M:%S')


    @admin.display(description='Дата обновления')
    def updated_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        print(self.update_at)
        if self.update_at.date() == timezone.now().date():
            updated_time = self.update_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: blue; font-weight: bold">'
                'Сегодня в {}</span>', updated_time
            )
        return self.update_at.strftime('%d.%m.%Y в %H:%M:%S')


