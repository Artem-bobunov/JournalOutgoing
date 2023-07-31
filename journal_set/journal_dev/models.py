from django.db import models

# Create your models here.
class journal(models.Model):
    choices_otdel = (
        ('01','01'),
        ('02','02'),
        ('03','03'),
        ('04','04'),
        ('05','05'),
        ('06','06'),
        ('07','07'),
        ('08','08'),
        ('09','09'),
        ('10','10'),
        ('11','11'),
        ('12','12'),
        ('14','14'),
    )
    dateReg = models.DateField('Дата регисрации',null=True,blank=True)
    res_ni = models.CharField('Номера отделов', null=True, blank=True, max_length=4000,choices=choices_otdel)
    numberInput = models.IntegerField('Номер исходящий',null=True,blank=True)
    res_nm = models.CharField('Номер исходящий и дата',null=True,blank=True,max_length=4000)
    adresat = models.CharField('Адресат (кому направлен)',null=True,blank=True,max_length=4000)
    content = models.CharField('Краткое содержание',null=True,blank=True,max_length=4000)
    executor = models.CharField('исполнитель',null=True,blank=True,max_length=4000)
    note = models.CharField('Примечание',null=True,blank=True,max_length=4000)
