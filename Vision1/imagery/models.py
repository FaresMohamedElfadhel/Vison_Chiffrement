from django.db import models
from .utils import cacher_image,dechiffrer_image
from PIL import Image
import numpy as np
import io
from io import BytesIO
from django.core.files.base import ContentFile
import cv2

# Create your models here.
class Chiffrement(models.Model):
    chiffrement_id = models.AutoField(primary_key=True)
    image_source=models.ImageField(upload_to='', null=True,blank=True)
    height_source=models.DecimalField(max_digits=5,decimal_places=0,null=True,blank=True)
    width_source=models.DecimalField(max_digits=5,decimal_places=0,null=True,blank=True)
    txt=models.CharField(max_length=20,null=True,blank=True)
    height_txt=models.DecimalField(max_digits=5,decimal_places=0,null=True,blank=True)
    width_txt=models.DecimalField(max_digits=5,decimal_places=0,null=True,blank=True)
    image_txt=models.ImageField(upload_to='', null=True,blank=True)
    image_chiffree=models.ImageField(upload_to='', null=True,blank=True)
    add_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'image '+str(self.chiffrement_id)
    # def update(self, *args, **kwargs): 
    #     pil_img_s = Image.open(self.image_source)
    #     cv_img_s = np.array(pil_img_s)
    #     print('resized with ',int(kwargs.get('height_source')),int(kwargs.get('width_source')))
    #     cv_img_s=cv2.resize(cv_img_s,(int(kwargs.get('height_source')),int(kwargs.get('width_source'))))
    #     buffer = BytesIO()
    #     is_success, buffer=cv2.imencode(".png",cv_img_s)
    #     buffer=io.BytesIO(buffer)
    #     image_png = buffer.getvalue()
    #     self.image_source.save(str(self.image_source), ContentFile(image_png), save=False)
    #     super().update(*args, **kwargs)

    def save(self, *args, **kwargs):
        if(kwargs.get('all_save')=='taille_source'):
            pil_img_s = Image.open(self.image_source)
            cv_img_s = np.array(pil_img_s)
            print('shape==',cv_img_s.shape)
            self.height_source,self.width_source=cv_img_s.shape[:2]
            super().save(*args, kwargs)
        elif(kwargs.get('all_save')=='chiffrer'):
        
            # open image
            pil_img_s = Image.open(self.image_source)
            pil_img_txt=Image.open(self.image_txt)
            self.image_chiffree=self.image_source

            # convert the image to array and do some processing
            cv_img_s = np.array(pil_img_s)
            cv_img_txt=np.array(pil_img_txt)
            print('saved succesfully0')
            img = cacher_image(cv_img_txt,cv_img_s)
            print('saved succesfully1')

            # convert back to pil image
            # im_pil = Image.fromarray((img/255).astype(np.uint8))
            # img_dec=dechiffrer_image(img)


            # save
            buffer = BytesIO()
            is_success, buffer=cv2.imencode(".png",img)
            buffer=io.BytesIO(buffer)
            # im_pil.save(buffer, format='png')
            image_png = buffer.getvalue()
            self.image_chiffree.save(str(self.image_chiffree), ContentFile(image_png), save=True)
            print('saved succesfully2')
        elif(kwargs.get('all_save')=='resize'):
            pil_img_s = Image.open(self.image_source)
            cv_img_s = np.array(pil_img_s)
            cv_img_s=cv2.resize(cv_img_s,(int(self.width_source),int(self.height_source)))
            buffer = BytesIO()
            im_pil = Image.fromarray(cv_img_s)
            im_pil.save(buffer, format='png')
            image_png = buffer.getvalue()
            self.image_source.save(str(self.image_source), ContentFile(image_png), save=True)
            # super().save(*args, kwargs)
        elif(kwargs.get('all_save')=='generer'):
            iamgeTxt = np.zeros((int(self.width_txt),int(self.height_txt)), np.uint8)
            font = cv2.FONT_HERSHEY_SIMPLEX
            j = 40
            i = 10
            cv2.putText(iamgeTxt, str(self.txt), (i, j), font,
                        1, 255, 1, 2)
            im_pil = Image.fromarray(iamgeTxt)
            buffer = BytesIO()
            im_pil.save(buffer, format='png')
            image_png = buffer.getvalue()
            self.image_txt.save(str(self.image_txt), ContentFile(image_png), save=True)
        else:
            super().save(*args, **kwargs)

class Dechiffrement(models.Model):
    ref_chiffrement=models.OneToOneField(Chiffrement, on_delete=models.CASCADE)
    dechiffrement_id = models.AutoField(primary_key=True)
    image_chiffree=models.ImageField(upload_to='', null=True,blank=True)
    image_txt_dechiffrement=models.ImageField(upload_to='', null=True,blank=True)
    add_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'image '+str(self.dechiffrement_id)
    def save(self, *args, **kwargs):
        if(kwargs.get('all_save')=='dechiffrer'):
            pil_img_s = Image.open(self.image_chiffree)

            # convert the image to array and do some processing
            cv_img_s = np.array(pil_img_s)
            img = dechiffrer_image(cv_img_s)

            # convert back to pil image
            # im_pil = Image.fromarray((img/255).astype(np.uint8))
            # img_dec=dechiffrer_image(img)


            # save
            buffer = BytesIO()
            is_success, buffer=cv2.imencode(".png",img)
            buffer=io.BytesIO(buffer)
            # im_pil.save(buffer, format='png')
            image_png = buffer.getvalue()
            self.image_txt_dechiffrement.save(str(self.image_chiffree), ContentFile(image_png), save=True)
        else:
            super().save(*args, **kwargs)

