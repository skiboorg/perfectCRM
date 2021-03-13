from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from pytils.translit import slugify


class Settings(models.Model):
    feedback_icon = models.FileField('Иконка блока отзывы ', blank=False, null=True, upload_to='logo/')
    feedback_title = models.CharField('Заголовок блока отзывы', max_length=255, blank=False, null=True)
    feedback_subtitle = models.CharField('Подзаголовок блока отзывы', max_length=255, blank=False, null=True)
    logo_footer = models.FileField('Логотип футер ', blank=False, null=True, upload_to='logo/')
    footer_text = models.CharField('Текст под лого в футере', max_length=255, blank=False, null=True)
    footer_company = models.CharField('Название организации',max_length=255, blank=False, null=True)
    footer_contacts = RichTextUploadingField('Реквизиты в футере', blank=False, null=True)
    footer_soc1_icon = models.FileField('Иконка соц сети 1', blank=False, null=True, upload_to='icon/')
    footer_soc1_link = models.CharField('Ссылка соц сети 1', max_length=255, blank=False, null=True)
    footer_soc2_icon = models.FileField('Иконка соц сети 2', blank=False, null=True, upload_to='icon/')
    footer_soc2_link = models.CharField('Ссылка соц сети 2', max_length=255, blank=False, null=True)
    footer_soc3_icon = models.FileField('Иконка соц сети 3', blank=False, null=True, upload_to='icon/')
    footer_soc3_link = models.CharField('Ссылка соц сети 3', max_length=255, blank=False, null=True)
    footer_copyright = models.CharField('Текст копирайт', max_length=255, blank=False, null=True)
    footer_link1_text = models.CharField('Текст ссылки', max_length=255, blank=False, null=True)
    footer_link1_link = models.CharField('URL ссылки', max_length=255, blank=False, null=True)
    footer_link2_text = models.CharField('Текст ссылки', max_length=255, blank=False, null=True)
    footer_link2_link = models.CharField('URL ссылки', max_length=255, blank=False, null=True)

    def __str__(self):
        return f'Настройка общих блоков'

    class Meta:
        verbose_name = "Общие блоки"
        verbose_name_plural = "Общие блоки"



class Header(models.Model):
    logo = models.FileField('Логотип хедер ', blank=False, null=True, upload_to='logo/')
    supportBtnText = models.CharField('Текст на ссылке', max_length=255, blank=False, null=True)
    supportBtnLink = models.CharField('Ссылка', max_length=255, blank=False, null=True)
    innerBtn1Text = models.CharField('Текст на кнопке 1 меню', max_length=255, blank=True, null=True)
    innerBtn1Link = models.CharField('Ссылка с  кнопки 1 меню', max_length=255, blank=True, null=True)
    innerBtn2Text = models.CharField('Текст на кнопке 2 меню', max_length=255, blank=True, null=True)
    innerBtn2Link = models.CharField('Ссылка с  кнопки 2 меню', max_length=255, blank=True, null=True)
    innerBtn3Text = models.CharField('Текст на кнопке 3 меню', max_length=255, blank=True, null=True)
    innerBtn3Link = models.CharField('Ссылка с  кнопки 3 меню', max_length=255, blank=True, null=True)


    def __str__(self):
        return f'Настройка блока'

    class Meta:
        verbose_name = "1. Хедер"
        verbose_name_plural = "1. Хедер"

class HeaderService(models.Model):
    header = models.ForeignKey(Header, on_delete=models.CASCADE, null=True, blank=True, related_name='services')
    name = models.CharField('Название услуги', max_length=255, blank=False, null=True)
    image = models.FileField('Картинка на кнопке', max_length=255, blank=False, null=True)
    text = models.CharField('Текст на кнопке', max_length=255, blank=False, null=True)
    link = models.CharField('Ссылка', max_length=255, blank=False, null=True)

    def __str__(self):
        return f'Настройка блока'

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

class Block1(models.Model):
    phone = models.CharField('Номер телефона', max_length=255, blank=False, null=True)
    video = models.FileField('Видео', blank=False, null=True, upload_to='video/')
    text = models.TextField('Текст', blank=False, null=True)

    def __str__(self):
        return f'Настройка блока'

    class Meta:
        verbose_name = "2. Оффер"
        verbose_name_plural = "2. Оффер"


class Block2(models.Model):
    blockIcon = models.FileField('Иконка блока ', blank=False, null=True, upload_to='icons/')
    title = models.CharField('Заголовок блока', max_length=255, blank=False, null=True)
    subtitle = models.CharField('Подзаголовок блока', max_length=255, blank=False, null=True)
    blockImage = models.FileField('Картинка в блоке ', blank=False, null=True, upload_to='images/')

    def __str__(self):
        return f'Настройка блока'

    class Meta:
        verbose_name = "3. Управление"
        verbose_name_plural = "3. Управление"


class Block2Features(models.Model):
    block = models.ForeignKey(Block2,on_delete=models.CASCADE, null=True, blank=True,related_name='features')
    title = models.CharField('Заголовок элемента списка', max_length=255, blank=False, null=True)
    text = RichTextUploadingField('Текст элемента', blank=False, null=True)
    blockImage = models.FileField('Картинка в блоке ', blank=False, null=True, upload_to='images/')

    class Meta:
        verbose_name = "Блок"
        verbose_name_plural = "Блок"

class Block3(models.Model):
    blockIcon = models.FileField('Иконка блока ', blank=False, null=True, upload_to='icons/')
    title = models.CharField('Заголовок блока', max_length=255, blank=False, null=True)
    subtitle = models.CharField('Подзаголовок блока', max_length=255, blank=False, null=True)
    leftPercent = models.CharField('Проценты левый блок', max_length=255, blank=False, null=True)
    leftText = models.CharField('Текст левый блок', max_length=255, blank=False, null=True)
    centerPercent = models.CharField('Проценты центральный блок', max_length=255, blank=False, null=True)
    centerText = models.CharField('Текст центральный блок', max_length=255, blank=False, null=True)
    rightPercent = models.CharField('Проценты правый блок', max_length=255, blank=False, null=True)
    rightText = models.CharField('Текст правый блок', max_length=255, blank=False, null=True)


    def __str__(self):
        return f'Настройка блока'

    class Meta:
        verbose_name = "4. Рост"
        verbose_name_plural = "4. Рост"

class Block4(models.Model):
    blockIcon = models.FileField('Иконка блока ', blank=False, null=True, upload_to='icons/')
    title = models.CharField('Заголовок блока', max_length=255, blank=False, null=True)
    subtitle = models.CharField('Подзаголовок блока', max_length=255, blank=False, null=True)

    def __str__(self):
        return f'Настройка блока'

    class Meta:
        verbose_name = "5. Фунциональность"
        verbose_name_plural = "5. Фунциональность"

class Block4Features(models.Model):
    block = models.ForeignKey(Block4,on_delete=models.CASCADE, null=True, blank=True,related_name='features')
    title = models.CharField('Заголовок элемента списка', max_length=255, blank=False, null=True)
    text = RichTextUploadingField('Текст элемента', blank=False, null=True)
    image = models.FileField('Картинка', blank=True, null=True, upload_to='images/')
    video = models.FileField('Видео', blank=True, null=True, upload_to='video/')

    class Meta:
        verbose_name = "Блок"
        verbose_name_plural = "Блок"

class Block5(models.Model):
    blockIcon = models.FileField('Иконка блока ', blank=False, null=True, upload_to='icons/')
    title = models.CharField('Заголовок блока', max_length=255, blank=False, null=True)
    subtitle = models.CharField('Подзаголовок блока', max_length=255, blank=False, null=True)
    subsubtitle = models.CharField('Подподзаголовок блока', max_length=255, blank=False, null=True)
    text = models.TextField('Текст блока', max_length=255, blank=False, null=True)
    image = models.FileField('Картинка', blank=True, null=True, upload_to='images/')

    def __str__(self):
        return f'Настройка блока'

    class Meta:
        verbose_name = "6. Личный кабинет"
        verbose_name_plural = "6. Личный кабинет"

class Block6(models.Model):
    blockIcon = models.FileField('Иконка блока ', blank=False, null=True, upload_to='icons/')
    title = models.CharField('Заголовок блока', max_length=255, blank=False, null=True)
    subtitle = models.CharField('Подзаголовок блока', max_length=255, blank=False, null=True)
    subsubtitle = models.CharField('Подподзаголовок блока', max_length=255, blank=False, null=True)
    text = RichTextUploadingField('Текст блока', blank=False, null=True)
    image = models.FileField('Картинка', blank=True, null=True, upload_to='images/')

    def __str__(self):
        return f'Настройка блока'

    class Meta:
        verbose_name = "7. Возможности платформы"
        verbose_name_plural = "7. Возможности платформы"

class Block7(models.Model):
    blockIcon = models.FileField('Иконка блока ', blank=False, null=True, upload_to='icons/')
    title = models.CharField('Заголовок блока', max_length=255, blank=False, null=True)
    subtitle = models.CharField('Подзаголовок блока', max_length=255, blank=False, null=True)

    block1_title = models.CharField('Заголовок блока1', max_length=255, blank=False, null=True)
    block1_subtitle = models.CharField('Подзаголовок блока1', max_length=255, blank=False, null=True)
    block1_check = models.BooleanField('Показывать чекбокс в блоке1', blank=True)
    block1_costSubFix = models.CharField('costSubFix', max_length=255, blank=False, null=True)
    block1_costSubUser = models.CharField('costSubUser', max_length=255, blank=False, null=True)
    block1_costSubPCC = models.CharField('costSubPCC', max_length=255, blank=False, null=True)

    block2_title = models.CharField('Заголовок блока2', max_length=255, blank=False, null=True)
    block2_subtitle = models.CharField('Подзаголовок блока2', max_length=255, blank=False, null=True)
    block2_check = models.BooleanField('Показывать чекбокс в блоке2', blank=True)
    block2_costEntFix = models.CharField('costEntFix', max_length=255, blank=False, null=True)
    block2_costEntUser = models.CharField('costEntUser', max_length=255, blank=False, null=True)
    block2_costEntPCC = models.CharField('costEntPCC', max_length=255, blank=False, null=True)

    block3_title = models.CharField('Заголовок блока3', max_length=255, blank=False, null=True)
    block3_info = RichTextUploadingField('Инфо в блоке', blank=False, null=True)

    def __str__(self):
        return f'Настройка блока'

    class Meta:
        verbose_name = "8. Стоимость"
        verbose_name_plural = "8. Стоимость"

class Feedback(models.Model):
    avatar = models.FileField('Аватар', blank=False, null=True, upload_to='icons/')
    link = models.CharField('Ссылка', max_length=255, blank=False, null=True)
    name = models.CharField('ФИО', max_length=255, blank=False, null=True)
    work = models.CharField('Должность', max_length=255, blank=False, null=True)
    text = RichTextUploadingField('Текст отзыва',blank=False, null=True)

    def __str__(self):
        return f'Отзыв от {self.name}'

    class Meta:
        verbose_name = "Отзывы"
        verbose_name_plural = "Отзывы"


class Page(models.Model):
    name = models.CharField('Название страницы', max_length=255, blank=False, null=True)
    name_slug = models.CharField('Название решения', max_length=255, blank=True, null=True , editable=False)
    header_btn_img = models.FileField('Картинка на кнопке в меню', max_length=255, blank=False, null=True)
    header_btn_text = models.CharField('Текст на кнопке в меню', max_length=255, blank=False, null=True)
    title = models.CharField('Заголовок страницы', max_length=255, blank=False, null=True)
    subtitle = models.CharField('Подзаголовок страницы', max_length=255, blank=False, null=True)
    video = models.FileField('Видео под заголовком', blank=False, null=True, upload_to='page/')
    subsubtitle = models.CharField('Текст под видео', max_length=255, blank=False, null=True)

    is_visible = models.BooleanField('Отображать видео блок', default=False)
    video_block_title = models.CharField('Заголовок видео блока', max_length=255, blank=True, null=True)
    video_block_text = models.CharField('Текст видео блока', max_length=255, blank=True, null=True)
    video_block_video = models.FileField('Видео в видео блоке', blank=True, null=True, upload_to='page/')
    video_block_image = models.FileField('Картинка в видео блоке (если видео файл выбран, картинка игнорируется)', blank=True, null=True, upload_to='page/')
    is_active = models.BooleanField('Показывать страницу', default=True)

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(Page, self).save(*args, **kwargs)

    def __str__(self):
        return f'Страница отраслевого решения - {self.name}'

    class Meta:
        verbose_name = "Страница отраслевого решения"
        verbose_name_plural = "Страницы отраслевых решений"


class PageFeatures(models.Model):
    block = models.ForeignKey(Page,on_delete=models.CASCADE, null=True, blank=True,related_name='features')
    icon = models.FileField('Иконка', blank=False, null=True, upload_to='images/')
    title = models.CharField('Заголовок', max_length=255, blank=False, null=True)
    text = RichTextUploadingField('Текст', blank=False, null=True)

    class Meta:
        verbose_name = "Приемущество"
        verbose_name_plural = "Приемущества"

class PageBlocks(models.Model):
    block = models.ForeignKey(Page,on_delete=models.CASCADE, null=True, blank=True,related_name='blocks')
    image = models.FileField('Картинка в блоке', blank=False, null=True, upload_to='images/')
    title = models.CharField('Заголовок', max_length=255, blank=False, null=True)
    text = RichTextUploadingField('Текст', blank=False, null=True)


    class Meta:
        verbose_name = "Блок с картинкой"
        verbose_name_plural = "Блоки с картинками"