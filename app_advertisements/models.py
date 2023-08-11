from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.html import mark_safe
from django.utils.html import format_html
# Create your models here.


User = get_user_model()
class Advertisements(models.Model):

    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг", help_text="Отметьте если торг уместен")
    create_at = models.DateTimeField(auto_now_add=True) #"Датта создания",
    update_at = models.DateTimeField(auto_now=True) #"Датта обновления",
    image = models.ImageField('Изображение', upload_to='advertisements/',)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
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

    @admin.display(description='маленькая картинка(вар 1)')
    def picture(self):
        from django.utils.html import mark_safe
        if self.image:
            return mark_safe(f'<img src = "/media/{self.image.name}" width = "100" height = "100"/>')
        else:
            return ""

    @admin.display(description='Изображение(вар 2)')
    def image_display(self):
        media_str = '/media/'
        if self.image:
            return format_html(
                '<img src="{}" style="max-width:100px; max-height:100px"/>'.format(media_str + self.image.name))
            # return mark_safe(f'<img src = "/media/{self.image.name}" width = "200"/>')
        else:
            return ''


