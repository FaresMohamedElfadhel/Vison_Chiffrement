from django.shortcuts import render
from . import forms,models
from django.http import JsonResponse
import json
from django.core import serializers
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

# Create your views here.
def Home(request):
    form=forms.ChiffrementForm(request.POST or None, request.FILES or None)
    context={'Chiffrement_form':form}

    data=serializers.serialize('json',[form.save(commit=False)])

    if is_ajax(request=request):
        methode = request.POST.get('methode')
        print(methode)
        if(methode=='dechiffrer'):
            pic_id=json.loads(request.POST.get('id'))
            pic_id2=json.loads(request.POST.get('id2'))
            obj=models.Chiffrement.objects.get(chiffrement_id=pic_id)
            models.Dechiffrement.objects.filter(dechiffrement_id=pic_id2).update(image_txt_dechiffrement=obj.image_txt)
            obj2=models.Dechiffrement.objects.get(dechiffrement_id=pic_id2)
            # obj2.save(all_save='dechiffrer')
            data=serializers.serialize('json',[obj])
            data2=serializers.serialize('json',[obj2])
            return JsonResponse({'data':data,'data2':data2})
        if(methode=='envoyer'):
            pic_id=json.loads(request.POST.get('id'))
            pic_id2=json.loads(request.POST.get('id2'))
            if pic_id2 is None:
                if form.is_valid():
                    obj=models.Chiffrement.objects.get(chiffrement_id=pic_id)
                    obj2=models.Dechiffrement(ref_chiffrement=obj,image_chiffree=obj.image_chiffree)
            else:
                obj=models.Chiffrement.objects.get(chiffrement_id=pic_id)
                obj2=models.Dechiffrement.objects.get(dechiffrement_id=pic_id2)
                obj2.image_chiffree=obj.image_chiffree
            obj2.save()
            data=serializers.serialize('json',[obj])
            data2=serializers.serialize('json',[obj2])
            return JsonResponse({'data':data,'data2':data2})
        if(methode=='generer'):
            pic_id=json.loads(request.POST.get('id'))
            if form.is_valid():
                # print('height_txt= ',request.POST.get('height_txt'),'width_source= ',request.POST.get('width_txt'),' img_sour =',request.FILES.get('image_source'))
                obj=models.Chiffrement.objects.filter(chiffrement_id=pic_id).update(txt=request.POST.get('txt'),height_txt=request.POST.get('height_txt'),width_txt=request.POST.get('width_txt'),image_txt=request.FILES.get('image_source'))
                obj=models.Chiffrement.objects.get(chiffrement_id=pic_id)
                obj.txt=request.POST.get('txt')
                obj.height_txt=request.POST.get('height_txt')
                obj.width_source=request.POST.get('width_source')
                obj.save(all_save='generer')
            data=serializers.serialize('json',[obj])
            return JsonResponse({'data':data})
        if(methode=='resize'):
            pic_id=json.loads(request.POST.get('id'))
            print(pic_id)
            if form.is_valid():
                obj=models.Chiffrement.objects.get(chiffrement_id=pic_id)
                obj.height_source=request.POST.get('height_source')
                obj.width_source=request.POST.get('width_source')
                obj.save(all_save='resize')
            # obj.update(height_source=request.POST.get('height_source'),width_source=request.POST.get('width_source'))
            data=serializers.serialize('json',[obj])
            return JsonResponse({'data':data})

        if(methode=='taille_source'):
            pic_id=json.loads(request.POST.get('id'))
            if pic_id is None:
                if form.is_valid():
                    obj=form.save(commit=False)
                    obj.save(all_save='taille_source')
            else:
                print(pic_id)
                obj=models.Chiffrement.objects.get(chiffrement_id=pic_id)
                obj.height_source=request.POST.get('height_source')
                obj.width_source=request.POST.get('width_source')
                print('sizeee = ',request.POST.get('height_source'),request.POST.get('width_source'))
                obj.save()
            data=serializers.serialize('json',[obj])
            return JsonResponse({'data':data})


            pass
        if(methode=='chiffrer'):
            pic_id=json.loads(request.POST.get('id'))
            
            print('b')
            obj=models.Chiffrement.objects.get(chiffrement_id=pic_id)
            obj.save(all_save='chiffrer')
            data=serializers.serialize('json',[obj])
            return JsonResponse({'data':data})
        return JsonResponse({'data':data})
    return render(request,'imagery/home.html',context)