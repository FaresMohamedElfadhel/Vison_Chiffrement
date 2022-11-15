import cv2
import numpy as np
def cacher_taille(image_txt, image_source):
    image_source_YCrCb = image_source
    # /--------------la taille de l'image source-------------/
    h, w, c = image_source_YCrCb.shape
    # /--------------construction de la liste contient les pixels de l'image texte-------------/
    list_img_txt = list(image_txt.flatten())
    # /--------------la taille de l'image texte-------------/
    ht, wt = image_txt.shape
    # /--------------convertion de la taille de l'image texte en string binaire de 16 bit-------------/
    h_b, w_b = '{0:016b}'.format(ht), '{0:016b}'.format(wt)
    # /--------------travailler sur h_b (pour codifier h_b dan Cr il nous faut 8 pixels de l'image source)-------------/
    # /-----------------eclater h_b en 8 listes binaires de 16 bit h_b_p-----------/
    h_b = [int(i) for i in list(h_b)]
    i = len(h_b)-1
    h_b_p = list()
    while(i > 0):
        h_b_p.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     h_b[i-1], h_b[i], 0, 1, 1, 1])
        i -= 2
    # /--------------creation d'un mask pour forcer les 6 premiers bits de Cr être à 1 -------------/
    mask = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    # /**************forcer les 6 premiers bits de Cr être à 1*************/
    y = 1
    w_Cr_p = list()
    for i in range(8):
        w_Cr_bin = [int(f) for f in list('{0:016b}'.format(image_source_YCrCb[h-y, w -
                                                                              1][1]))]
        w_Cr_p.append([w_Cr_bin[i] | mask[i] for i in range(len(w_Cr_bin))])
        y += 1
    # /****************Appliquer un et logique sur w_Cr_p et h_b_p pour avoir un 7 dans les 4 premiers bits de Cr et une partie de h_b dans le 6ème et le 5ème bit*********************/
    w_Cr_partie = list()
    for i in range(8):
        w_Cr_partie.append([w_Cr_p[i][j] & h_b_p[i][j]
                            for j in range(len(h_b_p[0]))])

     # /--------------travailler sur w_b (pour codifier w_b dan Cb il nous faut 8 pixels de l'image source)-------------/
    # /-----------------eclater w_b en 8 listes binaires de 16 bit w_b_p-----------/
    w_b = [int(i) for i in list(w_b)]
    i = len(w_b)-1
    w_b_p = list()
    while(i > 0):
        w_b_p.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     w_b[i-1], w_b[i], 0, 1, 1, 1])
        i -= 2
    # /--------------creation d'un mask pour forcer les 6 premiers bits de Cr être à 1 -------------/
    mask = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    # /**************forcer les 6 premiers bits de Cr être à 1*************/
    y = 1
    w_Cb_p = list()
    for i in range(8):
        w_Cb_bin = [int(f) for f in list('{0:016b}'.format(image_source_YCrCb[h-y, w -
                                                                              1][2]))]
        w_Cb_p.append([w_Cb_bin[i] | mask[i] for i in range(len(w_Cb_bin))])
        y += 1
    # /****************Appliquer un et logique sur w_Cr_p et h_b_p pour avoir un 7 dans les 4 premiers bits de Cr et une partie de h_b dans le 6ème et le 5ème bit*********************/
    w_Cb_partie = list()
    for i in range(8):
        w_Cb_partie.append([w_Cb_p[i][j] & w_b_p[i][j]
                            for j in range(len(w_b_p[0]))])
    # for i in range(8):
    #     print(w_Cb_p[i], '\nand\n', w_b_p[i],
    #           '\n=\n', w_Cb_partie[i], '\n-------')
    y = 1
    for i in range(8):
        image_source_YCrCb[h-y, w -
                           1][1] = int(''.join(str(x) for x in w_Cr_partie[i]), 2)
        image_source_YCrCb[h-y, w -
                           1][2] = int(''.join(str(x) for x in w_Cb_partie[i]), 2)
        # print(int(''.join(str(x) for x in w_Cr_partie[i]), 2), int(
        #     ''.join(str(x) for x in w_Cb_partie[i]), 2))
        y += 1
    return image_source_YCrCb


def extraire_taille_txt(img):
    # # /--------------convertir l'image source en YCrCb-------------/
    image_source_YCrCb = img
    # /--------------la taille de l'image source-------------/
    h, w, c = image_source_YCrCb.shape
    # /-------------------------------------------- width---------------------/
    y = 1
    w_Cb_partie = list()
    for i in range(8):
        w_Cb_bin = [int(f) for f in list('{0:016b}'.format(image_source_YCrCb[h-y, w -
                                                                              1][2]))]
        w_Cb_partie.append(w_Cb_bin)
        y += 1
    w_b = [0]*16
    n = 15
    for i in w_Cb_partie:
        w_b[n] = i[-5]
        w_b[n-1] = i[-6]
        n -= 2
    # /-------------------------------------------- height---------------------/
    y = 1
    h_Cr_partie = list()
    for i in range(8):
        h_Cr_bin = [int(f) for f in list('{0:016b}'.format(image_source_YCrCb[h-y, w -
                                                                              1][1]))]
        h_Cr_partie.append(h_Cr_bin)
        y += 1
    h_b = [0]*16
    n = 15
    for i in h_Cr_partie:
        h_b[n] = i[-5]
        h_b[n-1] = i[-6]
        n -= 2
    h, w = int(''.join(str(s) for s in h_b), 2), int(
        ''.join(str(s) for s in w_b), 2)
    return h, w

def cacher_image(image_txt, image_source):
    # /--------------convertir l'image source en YCrCb sur 16bit-------------/
    image_source_uint16 = np.uint16(image_source)
    image_source_uint16 *= 255
    image_source_YCrCb = cv2.cvtColor(
        image_source_uint16, cv2.COLOR_BGR2YCR_CB)
    # /--------------convertir l'image text en niveau de grie-------------/
    if len(image_txt.shape) == 3:
        image_txt = cv2.cvtColor(image_txt, cv2.COLOR_BGR2GRAY)
    image_txt=cv2.resize(image_txt,(100,100))
    # /--------------cacher la taille de l'image txt dans l'image source-------------/
    image_source_YCrCb = cacher_taille(image_txt, image_source_YCrCb)
    # /--------------la taille de l'image source-------------/
    h, w, c = image_source_YCrCb.shape
    # /--------------construction de la liste contient les pixels de l'image texte-------------/
    list_img_txt = list(image_txt.flatten())
    # /--------------la taille de l'image texte-------------/
    ht, wt = image_txt.shape
    n, m = 0, 0
    mask = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    print('hhhh', ht, wt)
    for y in range(ht):
        for x in range(wt):
            pixel_text_binaire = [int(p) for p in list(
                '{0:08b}'.format(image_txt[y, x]))]
            [1, 0, 1, 1, 0, 1, 0, 0]
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1]
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1]
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1]
            i = len(pixel_text_binaire)-1
            pixel_text_binaire_partie = list()
            while(i > 0):
                pixel_text_binaire_partie.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                                  pixel_text_binaire[i-1], pixel_text_binaire[i], 0, 1, 1, 1])
                i -= 2
            if(n < h):
                if(m < w):  # 184168  185380 184782
                    u = 0
                    # print(n, m)
                    for q in range(2):
                        Cr_bin = [int(f) for f in list(
                            '{0:016b}'.format(image_source_YCrCb[n, m+q, 1]))]
                        Cb_bin = [int(f) for f in list(
                            '{0:016b}'.format(image_source_YCrCb[n, m+q, 2]))]
                        Cr_bin_i = [Cr_bin[i] | mask[i]
                                    for i in range(len(Cr_bin))]
                        Cb_bin_i = [Cb_bin[i] | mask[i]
                                    for i in range(len(Cb_bin))]
                        Cr_bin_f = [pixel_text_binaire_partie[u][s]
                                    & Cr_bin_i[s] for s in range(len(Cr_bin_i))]
                        Cb_bin_f = [pixel_text_binaire_partie[u+1][s]
                                    & Cb_bin_i[s] for s in range(len(Cb_bin_i))]
                        image_source_YCrCb[n, m+q,
                                           1] = int(''.join(str(r) for r in Cr_bin_f), 2)
                        image_source_YCrCb[n, m+q,
                                           2] = int(''.join(str(r) for r in Cb_bin_f), 2)
                        u += 2
                    m += 2
                else:
                    m = 0
                    n += 1
            else:
                break
    final_image=cv2.cvtColor(image_source_YCrCb, cv2.COLOR_YCR_CB2RGB)
    return final_image
def dechiffrer_image(image_source):
    # /--------------convertir l'image source en YCrCb sur 16bit-------------/
    image_source_YCrCb = cv2.cvtColor(image_source, cv2.COLOR_RGB2YCR_CB)
    # /--------------la taille de l'image source-------------/
    h, w, c = image_source_YCrCb.shape
    ht, wt = extraire_taille_txt(image_source_YCrCb)
    print(ht, wt)
    iamgeTxt = np.zeros((ht, wt), np.uint8)
    n, m, x = 0, 0, 0

    for y in range(ht):
        for x in range(wt):
            if(n < h):
                if(m < w):  # 184168  185380 184782
                    txt_pixel_bin = [0]*8
                    Cr_bin1 = [int(f) for f in list(
                        '{0:016b}'.format(image_source_YCrCb[n, m, 1]))]
                    Cb_bin1 = [int(f) for f in list(
                        '{0:016b}'.format(image_source_YCrCb[n, m, 2]))]
                    Cr_bin2 = [int(f) for f in list(
                        '{0:016b}'.format(image_source_YCrCb[n, m+1, 1]))]
                    Cb_bin2 = [int(f) for f in list(
                        '{0:016b}'.format(image_source_YCrCb[n, m+1, 2]))]
                    # print(Cr_bin1, Cb_bin1)
                    txt_pixel_bin[7] = Cr_bin1[-5]
                    txt_pixel_bin[6] = Cr_bin1[-6]
                    txt_pixel_bin[5] = Cb_bin1[-5]
                    txt_pixel_bin[4] = Cb_bin1[-6]
                    txt_pixel_bin[3] = Cr_bin2[-5]
                    txt_pixel_bin[2] = Cr_bin2[-6]
                    txt_pixel_bin[1] = Cb_bin2[-5]
                    txt_pixel_bin[0] = Cb_bin2[-6]
                    txt_pixel = int(''.join(str(r) for r in txt_pixel_bin), 2)
                    m += 2
                else:
                    m = 0
                    n += 1
            else:
                break
            iamgeTxt[y, x] = txt_pixel
            # print(n, m)
    return iamgeTxt