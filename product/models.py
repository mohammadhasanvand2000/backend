
from django.db import models
from colorfield.fields import ColorField
from django_jalali.db import models as jmodels
from accounts.models import User





class KingCategory(models.Model):
    title= models.CharField(max_length=200,null=True,blank=True)





    def __str__(self):
        return '{}'.format (self.title )
    






class Categorytwo(models.Model):
    grouping2= models.ForeignKey(KingCategory,on_delete=models.CASCADE,related_name="catg",verbose_name=("دسته بندی 2"))
    title= models.CharField(max_length=200,null=True,blank=True)




    def __str__(self):
        return '{}'.format (self.title )







class Categorythree(models.Model):
    grouping3                   = models.ForeignKey(Categorytwo,on_delete=models.CASCADE,related_name="cat3",verbose_name=("grouping2"))
    title                      = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self): 
        return '{}'.format (self.title )










class Product (models.Model):
    
    kingcategory               = models.ForeignKey(KingCategory,on_delete=models.CASCADE,related_name="kingcategory",verbose_name=("دسته بندی اصلی "))
    category2                  = models.ForeignKey(Categorytwo ,on_delete=models.CASCADE,related_name="category2",verbose_name=("دسته بندی 2"))
    category3                  = models.ForeignKey(Categorythree ,on_delete=models.CASCADE,related_name="category3",verbose_name=("دسته بندی 3")) 
    title                      = models.CharField(max_length=200,null=True,blank=True , help_text="نام محصول:")
    #discount_percentage       = models.FloatField(default='0',null=True,blank=True,verbose_name=("درصد تخفیف"))
    price                      = models.IntegerField(default='1000',null=True,blank=True,help_text="قیمت محصول: ")
    discount_price             = models.IntegerField(null=True,blank=True,verbose_name=("قیمت جدید (همراه با تخفیف )"))
    unit_of_measurement        = models.CharField(max_length=200,null=True,blank=True,help_text="  واحد محاصبه:")
    Lowest_wholesale_amount    = models.CharField(max_length=200,null=True,blank=True,help_text="پایین ترین مقدار برای خرید:") 
    discribtion                = models.CharField(max_length=1000,null=True,blank=True,help_text="توضیحات محصول:")
    introduction               = models.CharField(max_length=2000,null=True,blank=True,help_text="معرفی بیشتر محصول:")
    Alloy                      = models.CharField(max_length=200,null=True,blank=True,help_text="آلیاژ یا جنس محصول:")
    warranty                   = models.IntegerField(null=True,blank=True,help_text="گارانتی محصول:")
    made_in                    = models.CharField(max_length=50,null=True,blank=True,help_text="کشور سازنده محصول:")
    dimensions                 = models.FloatField(null=True,blank=True,help_text="مقدار اولیه ابعاد :")
    in_dimensions              = models.FloatField(null=True,blank=True,help_text="مقدار دوم ابعاد")
    Weight                     = models.IntegerField(null=True,blank=True,help_text="وزن محصول:")
    stock_quantity             = models.PositiveIntegerField(default=0,verbose_name=("مقدار موجودی "))
    slug                       = models.SlugField(unique=True, max_length=255,null=True,blank=True,help_text="شماره جهت فیلتر (کد محصول ):") 
    image1                     = models.ImageField(upload_to="assets\img\poducts",null=True,blank=True)
    image2                     = models.ImageField(upload_to="assets\img\poducts",null=True,blank=True)
    image3                     = models.ImageField(upload_to="assets\img\poducts",null=True,blank=True)
    image4                     = models.ImageField(upload_to="assets\img\poducts",null=True,blank=True)
    image5                     = models.ImageField(upload_to="assets\img\poducts",null=True,blank=True)
    image6                     = models.ImageField(upload_to="assets\img\poducts",null=True,blank=True)
    image7                     = models.ImageField(upload_to="assets\img\poducts",null=True,blank=True)
    image8                     = models.ImageField(upload_to="assets\img\poducts",null=True,blank=True)
    image9                     = models.ImageField(upload_to="assets\img\poducts",null=True,blank=True)
    image10                    = models.ImageField(upload_to="assets\img\poducts",null=True,blank=True)
    color1                     = ColorField(default='#FF0000',null=True,blank=True)
    color2                     = ColorField(default='#FF0000',null=True,blank=True)
    color3                     = ColorField(default='#FF0000',null=True,blank=True)
    color4                     = ColorField(default='#FF0000',null=True,blank=True)
    color5                     = ColorField(default='#FF0000',null=True,blank=True)
    color6                     = ColorField(default='#FF0000',null=True,blank=True)
    color7                     = ColorField(default='#FF0000',null=True,blank=True)
    color8                     = ColorField(default='#FF0000',null=True,blank=True)
    color9                     = ColorField(default='#FF0000',null=True,blank=True)
    color10                    = ColorField(default='#FF0000',null=True,blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.check_stock()

    def check_stock(self):
        if self.stock_quantity <= 0:
            self.is_available = False
            self.save()

    @property
    def is_available(self):
        return self.stock_quantity > 0




    def set_discount_percentage(self, discount_percentage):
        if discount_percentage is not None and 0 <= discount_percentage <= 100:
            discount_amount = (discount_percentage / 100) * self.price
            self.discount_price = self.price - discount_amount
        else:
            self.discount_price = None

    @property
    def discount_percentage(self):
        if self.discount_price is not None and self.discount_price < self.price:
            discount = self.price - self.discount_price
            discount_percentage = (discount / self.price) * 100
            return discount_percentage
        return None

    def save(self, *args, **kwargs):
        if self.discount_percentage is not None:
            self.set_discount_percentage(self.discount_percentage)
        super().save(*args, **kwargs)









    def __str__(self):
        return "{}".format(self.title)





class Order(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at              = models.DateTimeField(auto_now_add=True)
    is_completed            = models.BooleanField(default=False)
    order_items             = models.ManyToManyField(Product, through='OrderItem')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        for order_item in self.order_items.all():
            product = order_item.product
            quantity = order_item.quantity
            if product.stock_quantity >= quantity:
                product.stock_quantity -= quantity
                product.save()





class OrderItem(models.Model):
    order                   = models.ForeignKey(Order, on_delete=models.CASCADE)
    product                 = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity                = models.PositiveIntegerField(default=1)





class Additional_field (models.Model):

    product                   = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="field",verbose_name=("field"))
    title                     = models.CharField(max_length=2000,null=True,blank=True,help_text="عنوان فیلد")
    content                   = models.CharField(max_length=2000,null=True,blank=True,help_text="محتوا ی فیلد")







    def __str__(self):
        return "{}".format(self.title)






class Bestselling (models.Model):

    product                   = models.OneToOneField(Product,on_delete=models.CASCADE,related_name="bestselling",verbose_name= ('محصول پرفروش '))
    from_date                 = jmodels.jDateField(verbose_name="از تاریخ", null=True, blank=True)
    up_to_date                = jmodels.jDateField(verbose_name="تا تاریخ", null=True, blank=True)




    

    def __str__(self):
        return f"{self.product} - از تاریخ: {self.from_date} - تا تاریخ: {self.up_to_date}"






class Customer_comment (models.Model):

    user                      = models.ForeignKey(User, on_delete=models.CASCADE)
    product                   = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="comment",verbose_name=("محصول مربوطه"))
    title                     = models.CharField(max_length=2000,null=True,blank=True,help_text="عنوان نظر")
    score                     = models.FloatField(default=100,null=True,blank=True)
    positive_points           = models.CharField(max_length=2000,null=True,blank=True,help_text="نکات مثبت")
    cons                      = models.CharField(max_length=2000,null=True,blank=True,help_text="نکات منفی ")
    comment                   = models.TextField(help_text=" متن نظر")
    like                      = models.BooleanField(default=True)
    created_at                = models.DateTimeField(auto_now_add=True)                  



    def __str__(self):
        return "{}".format(self.title)



