from bs4 import BeautifulSoup
import requests
import time

url_saves = 'http://www.tripadvisor.com/Saves#37685322'
url = 'https://cn.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html'
urls = [
    'https://cn.tripadvisor.com/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST'.format(
        str(i)) for i in range(30, 930, 30)]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36',
    'Cookie': 'TAUnique=%1%enc%3A44eMu7dZO5DDnsukDr9A%2F0JhuPze5TI3ulV0WaoXvVHiMVPFs%2B5nZg%3D%3D; ServerPool=C; PMC=V2*MS.61*MD.20170917*LD.20170917; TAPD=cn.tripadvisor.com; TASSK=enc%3AAO7APoVA6TGIGTxYUT8TPs52aaHxU2EWBMH0hUz90JNdTH3QdfwzUsflujUzhPGm0HuwNoBnA8A35XDHYjhTXkeytVDTMUEKOfBaNIsmavVuxlZ%2BkvOghRTtunZCajcY0w%3D%3D; PAC=AOibpjcA7L-AgYqNNUi90YKRyPydXCFG5Br6JZ9THCUWjSNZtTJc3zgljtGQqJY6z2I4apsr5wKOXmQAirAOw4sC1xWTpyraZKCjjMJw-zKBJxYu4o1tVDOvW9Zh5P5v5tDe0sLdKpkT_I3GraGgaWURItklFEwWfS5vbYPsH2cEUt8YeW3-nLJHmE3UJXaRA33koIlZJvcpCRXg1JDgCPw%3D; TART=%1%enc%3AgwxEHxXXKx5BYnaIIFeRj27aiHhNb%2Fv9BPJdjeXryr%2F2cHoqKbY7jG%2BUzv2ZUbfeW1JxtpsONWQ%3D; ki_t=1505649736279%3B1505649736279%3B1505649736279%3B1%3B1; ki_r=; ki_u=5511491f-a3fa-4370-a6b6-6a50; ki_s=175381%3A1.0.0.0.2; TAReturnTo=%1%%2FAttractions-g60763-Activities-New_York_City_New_York.html; SecureLogin2=3.4%3AABCk52Bwl6rwcmNfsPSZ5YL2sVgBeJgwKwwRJNvnXIHYosJ2Si0jE0klKcxCoaa13qnRmtCx68gvKhtL2yvjbF0GkmA1Wq5A2YlxrZvCJtXcxua2byUlKV0MxuYfFlOQhwNq8bSswWPSRbR4b3efwckNU0MXag9Cdqzt6Q3nCI0s9h3ozLaEOTzeHB1Xq1PYSRIpVKOhSiC1yQpLvb%2F5c4w%3D; TAAuth3=3%3A59fdaf0d81b51499674b9caf7d3e93b0%3AANOlyOLxAH%2F3Sg%2Be1zULTofDeLnA%2FLR2758jcodTK26EADRrKp%2BbyDu8HxslVNPcLv8dZ28WMUvk5EHWb%2BgXiSRLzNiepkq9C6aelI3lveMtsb2jwXazMezRdM%2Bbni56RzhU79kJbmPdqQMHy3qyKfona5qfY92IrSFDNZb%2BzKVTejijo%2BDLz3%2BX%2BZXhxs53WQ%3D%3D; __gads=ID=e92a37ba1848214c:T=1505650171:S=ALNI_Mb6zWPBa8IQKj-A7nyitnNA8mIujg; interstitialCounter=4; MobileLastViewedList=%1%%2FAttractions-g60763-Activities-New_York_City_New_York.html; taMobileRV=%1%%7B%2210028%22%3A%5B60763%5D%7D; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RVL.60763_260*DSM.1505649767917; CM=%1%pu_vr2%2C%2C-1%7CHanaPersist%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7Cpv%2C3%2C-1%7Cpu_vr1%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C2%2C-1%7CPremiumSURPers%2C%2C-1%7Ctvsess%2C-1%2C-1%7CPremiumMCSess%2C%2C-1%7Ccatchsess%2C5%2C-1%7Cbrandsess%2C%2C-1%7CCpmPopunder_1%2C%2C-1%7CCCSess%2C%2C-1%7CCpmPopunder_2%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7Cmds%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CHomeAPers%2C%2C-1%7C+r_lf_1%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7C+r_lf_2%2C%2C-1%7Ccatchpers%2C3%2C1506254508%7CLaFourchette+MC+Banners%2C%2C-1%7Cvr_npu2%2C%2C-1%7CLastPopunderId%2C104-771-null%2C-1%7Csh%2CRuleBasedPopup%2C1505736163%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7Cvr_npu1%2C%2C-1%7CCCPers%2C%2C-1%7Ctvpers%2C1%2C1506254563%7Cbrandpers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CWarPopunder_Session%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CWarPopunder_Persist%2C%2C-1%7CTheForkORPers%2C%2C-1%7Cr_ta_2%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7Cr_ta_1%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CCPNC%2C1%2C1568721709%7CMetaFtrPers%2C%2C-1%7C; roybatty=TNI1625!AC3arv7V%2Bzbqz%2BGv2lR0iHuhVMk6ASpAe5zydMdv%2FJqBFJ1B01E5iJ0OPxKuW8MC7pirq239d1tTy6k%2FtF7n4FSU3q5noGjFWZ8lNjJ5JbiiYbY%2B6fzyG6Mb35l6u4%2B32hHjw9VMzTWiCQbszKAsM2p52NYdR4CYviWI1uwHYJrx%2C1; TASession=%1%V2ID.0E201C5A2FD1A7E7BEA639E5E0B4DFA3*SQ.49*PR.427%7C*LS.PageMoniker*GR.61*TCPAR.8*TBR.38*EXEX.20*ABTR.59*PHTB.36*FS.74*CPU.30*HS.recommended*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.457194720C3F658872FF0124054450D6*FA.1*DF.0*IR.1*OD.null*FLO.60763*TRA.true*LD.60763; TAUD=LA-1505649692446-1*RDD-1-2017_09_17*LG-582664-2.0.F.*LD-582665-.....'
}


def get_attractions(url, data=None):
    wb_data = requests.get(url)
    time.sleep(4)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select('div.property_title > a[target="_blank"]')
    imgs = soup.select('img[width="160"]')
    cates = soup.select('div.p13n_reasoning_v2')
    if data == None:
        for title, img, cate in zip(titles, imgs, cates):
            data = {
                'title': title.get_text(),
                'img': img.get('src'),
                'cate': list(cate.stripped_strings),
            }
        print(data)


def get_favs(url, data=None):
    wb_data = requests.get(url, headers=headers)
    print(wb_data)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select("div.title.titleLLR > div")
    imgs = soup.find_all("div", "missing lazyMiss")
    metas = soup.select('div.attraction_types > span')

    if data == None:
        for title, img, meta in zip(titles, imgs, metas):
            data = {
                'title': title.get_text().strip(),
                'img': img.get('data-thumburl'),
                'meta': meta.get_text()
            }
            print(data)


for single_url in urls:
    get_attractions(single_url)
