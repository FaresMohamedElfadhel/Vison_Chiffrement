const alertBox = document.getElementById('alert-box')
const imgBox = document.getElementById('img-box')
const imgbox2 = document.getElementById('img-box2')
const imgbox3 = document.getElementById('img-box3')
const imgbox4 = document.getElementById('img-box4')
const imgbox5 = document.getElementById('img-box5')
const sourceSizeBox=document.getElementById('source-size-box')
const form = document.getElementById('p-form')

const image_source = document.getElementById('id_image_source')
const height_source= document.getElementById('id_height_source')
const width_source = document.getElementById('id_width_source')
const txt=document.getElementById('id_txt')
const width_txt=document.getElementById('id_width_txt')
const height_txt =document.getElementById('id_height_txt')
const image_txt = document.getElementById('id_image_txt')
const image_chiffree = document.getElementById('id_image_chiffree')
const btnBox=document.getElementById('btn-box')
const btnBox2=document.getElementById('btn-box-2')
const btnBox3=document.getElementById('btn-box-3')
const btnBox4=document.getElementById('btn-box-4')
const btnBox5=document.getElementById('btn-box-5')
const btnBox6=document.getElementById('btn-box-6')






const mediaURL=window.location.href + 'media/'
console.log(mediaURL)

const btns=[...btnBox.children]
const btns2=[...btnBox2.children]
const btns3=[...btnBox3.children]
const btns4=[...btnBox4.children]
const btns5=[...btnBox5.children]
const btns6=[...btnBox6.children]





const csrf = document.getElementsByName('csrfmiddlewaretoken')
console.log(csrf)

const url = ""
const url2= ""
const url3=""

const handleAlerts = (type, text) =>{
    alertBox.innerHTML = `<div class="alert alert-${type}" role="alert">
                            ${text}
                        </div>`
}

image_source.addEventListener('change', ()=>{
    const img_data = image_source.files[0]
    const url = URL.createObjectURL(img_data)
    console.log(url)
    imgBox.innerHTML = `<img src="${url}" width="50%">`
})
image_txt.addEventListener('change', ()=>{
    const img_data2= image_txt.files[0]
    const url2 = URL.createObjectURL(img_data2)
    console.log(url2)
    imgbox2.innerHTML = `<img src="${url2}" width="50%">`
})
let id = null
let id2= null
let methode=null
btns.forEach(btn => btn.addEventListener('click', ()=>{
    methode=btn.getAttribute('data-filter')
    console.log('thiiiis method',methode)
}))
btns2.forEach(btn2 => btn2.addEventListener('click', ()=>{
    methode=btn2.getAttribute('data-filter')
    console.log('thiiiis method',methode)
}))
btns3.forEach(btn3 => btn3.addEventListener('click', ()=>{
    methode=btn3.getAttribute('data-filter')
    console.log('thiiiis method',methode)
    console.log('btnBox4.classList',btnBox4.classList)
    btnBox4.classList.remove('not-visible')
}))
btns4.forEach(btn4 => btn4.addEventListener('click', ()=>{
    methode=btn4.getAttribute('data-filter')
    console.log('thiiiis method',methode)
    btnBox5.classList.remove('not-visible-envoyer')
}))
btns5.forEach(btn5 => btn5.addEventListener('click', ()=>{
    methode=btn5.getAttribute('data-filter')
    console.log('thiiiis method',methode)
    btnBox6.classList.remove('not-visible-envoyer')
}))
btns6.forEach(btn6 => btn6.addEventListener('click', ()=>{
    methode=btn6.getAttribute('data-filter')
    console.log('thiiiis method',methode)
}))

console.log('thiiiisss method',methode)

form.addEventListener('submit', e=>{
    e.preventDefault()
    console.log('thiiiisssss method',methode)

    const fd = new FormData()
    if(methode=='dechiffrer'){
        fd.append('csrfmiddlewaretoken', csrf[0].value)
        fd.append('methode',methode)
        fd.append('id',id)
        fd.append('id2',id2)
    }
    if(methode=='envoyer'){
        fd.append('csrfmiddlewaretoken', csrf[0].value)
        fd.append('methode',methode)
        fd.append('id',id)
        fd.append('id2',id2)
        console.log(fd)

    }
    if(methode=='chiffrer'){
        fd.append('csrfmiddlewaretoken', csrf[0].value)
        fd.append('image_source', image_source.files[0])
        fd.append('image_txt', image_txt.files[0])
         // fd.append('image_chiffree', image_chiffree.files[0])
        fd.append('methode',methode)
        fd.append('id',id)
        console.log(fd)

    }
    if(methode=='generer'){
        fd.append('csrfmiddlewaretoken', csrf[0].value)
        console.log('ffffffffffffffffffff=',txt.value)
        fd.append('image_source', image_source.files[0])
        fd.append('txt', txt.value)
        fd.append('height_txt', height_txt.value)
        fd.append('width_txt', width_txt.value)
        fd.append('methode',methode)
        fd.append('id',id)

    }

    if(methode=='resize'){
        fd.append('csrfmiddlewaretoken', csrf[0].value)
        fd.append('image_source', image_source.files[0])
        fd.append('height_source', height_source.value)
        fd.append('width_source', width_source.value)
        fd.append('methode',methode)
        fd.append('id',id)

    }
    if(methode=='taille_source'){
        fd.append('csrfmiddlewaretoken', csrf[0].value)
        fd.append('image_source', image_source.files[0])
        fd.append('height_source', height_source.value)
        fd.append('width_source', width_source.value)
        fd.append('methode',methode)
        fd.append('id',id)
        console.log('id0 =============',id)

    }
    

    $.ajax({
        type: 'POST',
        url: url,
        enctype: 'multipart/form-data',
        data: fd,
        success: function(response){
            let data2=null
            if(methode=='dechiffrer'){
                data2=JSON.parse(response.data2)
                console.log('data 2 ',data2)
                id2=data2[0].pk
                console.log('id2 ===== ',id2)
            }
            if(methode=='envoyer'){
                data2=JSON.parse(response.data2)
                console.log('data 2 ',data2)
                id2=data2[0].pk
                console.log('id2 ===== ',id2)
            }
            const data=JSON.parse(response.data)
            console.log('data ',data)
            console.log(methode)
            id=data[0].pk
            console.log('id ===== ',id)
            console.log('alooooo ',mediaURL+data[0].fields.image_txt)
            if(methode=='dechiffrer'){
                imgbox5.innerHTML = `<div class="row text-center m-3 p-1" style="border: 0.5px #F0f0ff solid; background-image: linear-gradient(to right,#380036,#0CBABA); border-radius: 5px;
                color: #fff;"><h5>Image Dechiffrée</h5></div><img src="${mediaURL+data2[0].fields.image_txt_dechiffrement}" width="50%">`
            }
            if(methode=='envoyer'){
                /***********   ici   ********* */
                imgbox4.innerHTML = `<div class="row text-center m-3 p-1" style="border: 0.5px #F0f0ff solid; background-image: linear-gradient(to right,#380036,#0CBABA); border-radius: 5px;
                color: #fff;"><h5>Image Chiffrée Reçu</h5></div><img src="${mediaURL+data2[0].fields.image_chiffree}" width="50%">`
            }
            if(methode=='generer'){
                imgbox2.innerHTML = `<img src="${mediaURL+data[0].fields.image_txt}" width="50%">`
            }
            if(methode=='resize'){
                imgBox.innerHTML = `<img src="${mediaURL+data[0].fields.image_source}" width="50%">`
            }
            if(methode=='taille_source'){
                fd.append('id',id)
                height_source.value=data[0].fields.height_source
                width_source.value=data[0].fields.width_source
                sourceSizeBox.classList.remove('invisible-taille-source')
        
            }
            if(methode=='chiffrer'){
                imgbox3.innerHTML = `<div class="row text-center m-3 p-1" style="border: 0.5px #F0f0ff solid; background-image: linear-gradient(to right,#380036,#0CBABA); border-radius: 5px;
                color: #fff;"><h5>Image Chiffrée</h5></div><img src="${mediaURL+data[0].fields.image_chiffree}" width="50%">`
                const sText = `successfully saved ${mediaURL+data[0].fields.image_chiffree}`
                handleAlerts('success', sText)
                
            }
            setTimeout(()=>{
                alertBox.innerHTML = ""
            }, 4000)
            },
            error: function(error){
                console.log(error)
                handleAlerts('danger', 'ups..something went wrong')
            },
            
        cache: false,
        contentType: false,
        processData: false,
    })
    // const img_data3= image_chiffree.files[0]
    // const url3 = URL.createObjectURL(img_data3)
    // console.log(url3)
    // imgbox3.innerHTML = `<img src="${url3}" width="50%">`
})

console.log(form)