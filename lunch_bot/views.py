from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
import json
import random
# from django.views.decorators import csrf
# from rest_framework.decorators import api_view

# 한식 리스트
korean_rice = ['김밥','비빔밥','볶음밥','덮밥','죽']
korean_noodle = ['비빔국수','잔치국수','칼국수','물냉면','비빔냉면']
korean_soup = ['국밥','설렁탕','김치찌개','순두부찌개','부대찌개']
korean_meat = ['불고기','삼겹살','제육볶음','수육','닭갈비']
korean_snack = ['떡볶이','순대','라면','쫄면','튀김']
korean_foods = korean_rice + korean_noodle + korean_soup + korean_meat + korean_snack

# 중식 리스트
chinese_noodle = ['짜장면','간짜장','짬뽕','볶음짬뽕','기스면']
chinese_rice = ['짜장밥','짬뽕밥','볶음밥','마파두부밥','잡채밥']
chinese_stir_fry = ['잡채','고추잡채','팔보채','양장피','유산슬']
chinese_meat = ['탕수육','깐풍기','유린기','라조기','깐쇼새우']
chinese_dumpling = ['꽃빵','군만두','멘보샤']
chinese_foods = chinese_noodle + chinese_rice + chinese_stir_fry + chinese_meat + chinese_dumpling

# 일식 리스트
japanese_rice = ['초밥','오니기리','가츠동','규동','텐동']
japanese_noodle = ['우동','소바']
japanese_grill = ['타코야끼','오코노미야끼']
japanese_fry = ['덴푸라','가라아게','돈까스']
japanese_hot_pot = ['오뎅나베','샤브샤브','스키야키','부타나베']
japanese_foods = japanese_rice + japanese_noodle + japanese_grill + japanese_fry + japanese_hot_pot

# 양식 리스트
western_pasta = ['토마토 파스타','크림 파스타','로제 파스타','알리오 에 올리오','봉골레 파스타']
western_pizza = ['하와이안 피자','쉬림프 피자','고구마 피자','포테이토 피자','시카고 피자']
western_hamburger = ['맥도날드','버거킹','롯데리아','맘스터치','쉑쉑버거']
western_chicken = ['후라이드 치킨','양념 치킨','간장 치킨','파닭','닭강정']
western_foods = western_pasta + western_pizza + western_hamburger + western_chicken

# 모든 음식 리스트
all_foods = korean_foods + chinese_foods + japanese_foods + western_foods


# 음식 딕셔너리
foods_dict = {
    "korean_rice" : korean_rice,
    "korean_noodle" : korean_noodle,
    "korean_soup" : korean_soup,
    "korean_meat" : korean_meat,
    "korean_snack" : korean_snack,
    "korean_foods" : korean_foods,
    
    "chinese_noodle" : chinese_noodle,
    "chinese_rice" : chinese_rice,
    "chinese_stir_fry" : chinese_stir_fry,
    "chinese_meat" : chinese_meat,
    "chinese_dumpling" : chinese_dumpling,
    "chinese_foods" : chinese_foods,

    "japanese_rice" : japanese_rice,
    "japanese_noodle" : japanese_noodle,
    "japanese_grill" : japanese_grill,
    "japanese_fry" : japanese_fry,
    "japanese_hot_pot" : japanese_hot_pot,
    "japanese_foods" : japanese_foods,

    "western_pasta" : western_pasta,
    "western_pizza" : western_pizza,
    "western_hamburger" : western_hamburger,
    "western_chicken" : western_chicken,
    "western_foods" : western_foods,

    "all_foods": all_foods
}

# 이미지 URL dictionary
food_URL_dict = {
    # 한식 이미지
    "김밥" : "https://d1blyo8czty997.cloudfront.net/tour-course/12433/600x600/2922004803.jpg",
    "비빔밥" : "https://i.pinimg.com/originals/1e/a6/3f/1ea63f2165c67d13452ff8a131787cc7.jpg",
    "볶음밥" : "https://mblogthumb-phinf.pstatic.net/MjAyMDA1MjlfMTA4/MDAxNTkwNzAyMzA4OTQ3.9hcGQv_iZlbCfNXM1PFYdizB_SXKgeyZz8ST16i5F-Ag.YPTqtZCVfmiEiTEuNN6GUOuFsfRLuE2drqMa6_krf_Ig.JPEG.blogdanielland/A32.jpg?type=w800",
    "덮밥" : "https://t1.daumcdn.net/cfile/tistory/9958383B5C939D8D22",
    "죽" : "https://lh3.googleusercontent.com/proxy/JwwNU3X1FL1DRoU95mOKe1iQZSu7Eo72u21N0eQWlIZqHg1TCYI-qTkH3wC8EE5eSxYy5XQyy_aScST4IwgNCU1AIMdhsbFcONsnBE_kW0D2m5Ar_DjXTKKTC9cg76s3CWjOReBV_gD-xr9GldU",

    '비빔국수' : "https://lh3.googleusercontent.com/proxy/xA7dXxRTswWZBoNs7rv5U0G26T0Rv_H7EW2hL07KZlnKigMzMhYTDKdxI9FSzXaM8o-z_MvI6OMePaGENXi2w8mOk2GAOH4H_ehDMPHq7bkB58ogQkigUjU19aEagRNeRAU1ZSRBAXQJe5qXx3AP4JyrtEc_Bblvb28C4oHl",
    '잔치국수' : "https://img.mimint.co.kr/food/bbs/2019/3/18/20190318164604_ketozyvi.jpg",
    '칼국수' : "https://i.pinimg.com/originals/81/f8/7c/81f87c024512f7acbc932333bcc3e02b.jpg",
    '물냉면' : "https://shopping-phinf.pstatic.net/main_8290432/82904329411.jpg",
    '비빔냉면' : "https://upload3.inven.co.kr/upload/2021/10/07/bbs/i16137460551.jpg",

    '국밥' : "https://image.fmkorea.com/files/attach/new2/20210301/1135415169/2841875140/3423424636/8d9267368f3829a401e5ffa28e7229db.jpg",
    '설렁탕' : "https://item-shopping.c.yimg.jp/i/n/assign-1_20211106000305-02259_1",
    '김치찌개' : "https://img1.daumcdn.net/thumb/S1200x630/?fname=https://t1.daumcdn.net/news/201403/07/korea_herald/20140307194107826.jpg",
    '순두부찌개' : "https://qph.fs.quoracdn.net/main-qimg-4aadd8420bc177ed47ab06feecfc8a54",
    '부대찌개' : "https://obs.line-scdn.net/0hJY7LVS-QFXYKNT2KbyxqITBjFhk5WQZ1bgNEdVZbS0JzDQEnP1YOQyZhS0IvBVIoY1JeGS01Dkd0UFQpYVEO/w644",

    '불고기' : "https://asiangenoma.com/wp-content/uploads/2020/03/BULGOGUI.jpg",
    '삼겹살' : "https://img1.daumcdn.net/thumb/S1200x630/?fname=https://t1.daumcdn.net/news/202106/14/KorMedi/20210614193110171hlwb.jpg",
    '제육볶음' : "https://mblogthumb-phinf.pstatic.net/MjAxOTEwMTBfMTY4/MDAxNTcwNjY4NDMyMDI2.iJp8FqIL-gtpCxbniD3VluS-3tnE5KA6rhIni04c6bIg.zjcYtdYyGimlZhLUiq6cFxaxy3MLTDGMdVs_S4gAYg0g.JPEG.ho1772/%EA%BE%B8%EB%AF%B8%EA%B8%B0%EA%BE%B8%EB%AF%B8%EA%B8%B0Screenshot_20191008-232406_Video_Player.jpg?type=w800",
    '수육' : "https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F995280375BEFC11931",
    '닭갈비' : "https://post-phinf.pstatic.net/MjAyMTA4MjdfMjUg/MDAxNjMwMDM3MzIyNTU5.A15h_pq2DrXWcoCkslrnc6fYVeNnm9dgx2xVRZhT7Zcg.rA8flqJ2LBBxAlfy6Lx6CoqefkDixlsM8O46I4FFJ8wg.JPEG/1.jpg?type=w1200",

    '떡볶이' : "https://shopping-phinf.pstatic.net/main_2795605/27956051357.20210803155027.jpg",
    '순대' : "https://post-phinf.pstatic.net/MjAxOTExMDZfODQg/MDAxNTczMDIwMTQ2NTQx.LoPDJ6xvEeYMikhaOjREUxV1nA_ahS0h6LY198UjzhQg.rMFTtCNReQ-EmBLQIADX5pVNhk2KotE9FE0X2posesMg.JPEG/7-1.jpg?type=w1200",
    '라면' : "https://image.fmkorea.com/files/attach/new2/20210903/486616/3213524086/3886041701/4e4cc04199d7a9a0006585975a9dabdf.jpeg",
    '쫄면' : "https://th-test-11.slatic.net/p/0efa1976d73754544d4476c56b433241.jpg",
    '튀김' : "https://cdn.crowdpic.net/list-thumb/thumb_l_C7F4D561E1FD8C87862220ABC1838884.jpg",

    # 중식 이미지
    '짜장면' : "http://file3.instiz.net/data/file3/2021/07/08/8/d/4/8d4b94e2a14eeb0140b5f4eb461fb64b.jpg",
    '간짜장' : "https://post-phinf.pstatic.net/MjAxNzExMjFfMTEg/MDAxNTExMjI4NjkzMDY2.z9bUkvFDY0nnhqErnAEPk53jnzutqwjYRiNgl5uDmGAg.kzSYoFDZwYPp21zjQKMC92H2BojSO3tiFLoSjPTlZVwg.JPEG/GettyImages-jv10998496.jpg?type=w1200",
    '짬뽕' : "https://img-cf.kurly.com/shop/data/goodsview/20210531/gv10000188583_1.jpg",
    '볶음짬뽕' : "https://post-phinf.pstatic.net/MjAxNzA5MThfMTE0/MDAxNTA1Njk4NDQyOTg3.zRMBiXmuTl_oQBXUQt6y5WO7RrQeku5rKTeDbVtXRcIg.EIH4nuk9714ySXJX_A5DBoP2RukwYGV9Ug8xPttjztwg.JPEG/1.jpg?type=w1200",
    '기스면' : "https://blog.kakaocdn.net/dn/868cw/btqEpZI9BUc/NcuDRLXlReB9OGztRwRqbK/img.jpg",

    '짜장밥' : "https://themoonworld.com/wp-content/uploads/2020/11/DSC06550-1024x1024.jpg",
    '짬뽕밥' : "https://post-phinf.pstatic.net/MjAyMDA1MDhfMjg4/MDAxNTg4OTEzOTQ0ODEw.MlKOS-d0T-lX69FdD-brsFU-GmHF6rhGvRWeweCVANMg.TWeaKUNZU35kW6iQgznXnkKZFlxUAWW6FFd8DpRsEYwg.JPEG/4q44rrk5l89i838j64ju.jpg?type=w1200",
    '볶음밥' : "https://mblogthumb-phinf.pstatic.net/20151026_77/akwldrkr8158_1445840780134DIOXw_JPEG/2015-10-26_15%3B24%3B55.jpg?type=w2",
    '마파두부밥' : "https://recipe1.ezmember.co.kr/cache/recipe/2015/06/18/8561efecd85e95dcd1f887e5c1ede50f.jpg",
    '잡채밥' : "https://image.bada.io/files//crawling/2021/03/06/bhu/51192264_166fe19a68188e1a.jpg",

    '잡채' : "https://homecuisine.co.kr/files/attach/images/142/158/100/9e4b37e66d5fe27ba7c39af668b10d78.JPG",
    '고추잡채' : "https://recipe1.ezmember.co.kr/cache/recipe/2020/04/23/99c43fc85dc67aff919587f4d9a1f2f81.jpg",
    '팔보채' : "https://mblogthumb-phinf.pstatic.net/MjAxODEwMDVfMTM1/MDAxNTM4NzM2MDk2Mzg0.z9JZ64HhfYZdCbY1YOI7LeCWvLG3PdzplP-8xtl-YV0g.Sy58bnE3PsyyXMM28_bhEDpXK2ydQRUojW2UywNHwv4g.JPEG.annasuism/IMG_2350.jpg?type=w800",
    '양장피' : "https://recipe1.ezmember.co.kr/cache/recipe/2016/04/22/8e8d26b8f9a2fef59896ba3e9fc22c0c1.jpg",
    '유산슬' : "https://homecuisine.co.kr/files/attach/images/142/821/001/31c249d8f3fe7ff55a910c988e21faf8.JPG",

    '탕수육' : "https://lh3.googleusercontent.com/proxy/9sSXqCc-2WsulkOAE2V7aoLJDmxsJr7lagG3JmElCo6A7MzH64_wK7KfGcXNjaRvzwVlwcF6FLCAXAdQqTYbB3D7OWOgTjUnKdgDdPyL1SQydeoTaPBQUivaOLV93QO4O8ayrdf1shCugIbgeCfH6F3g8Uky95OGqqYF3iUM2hoz_ijDW2wSxAdn_o8KQTZ5T4u2sl2fH3hs66GygKfjKugv8OCvgJdVl26XwZ6aETtt1r1lpRgx9YzcTfdIQyIX9dwzuSnR",
    '깐풍기' : "http://food.chosun.com/site/data/img_dir/2012/05/21/2012052101195_0.jpg",
    '유린기' : "https://i.pinimg.com/originals/fe/9b/b2/fe9bb208ce80fbf23321aa19d72a3b96.jpg",
    '라조기' : "https://upload.wikimedia.org/wikipedia/commons/c/c9/Rajogi.jpg",
    '깐쇼새우' : "https://blog.kakaocdn.net/dn/Zx9Yx/btqCO1aA9Hv/8l7nfkfrP3E69iNiLuQG8k/img.png",

    '꽃빵' : "https://upload.wikimedia.org/wikipedia/commons/c/cb/Hu%C4%81ju%C7%8En.jpg",
    '군만두' : "https://i1.ruliweb.com/img/20/06/21/172d607e11351e670.jpeg",
    '멘보샤' : "http://i30.tcafe2a.com/2009/20200910121202_83e5e943dd4f3bb685ab04b7fe6334a9_ntga.jpg",

    # 일식 이미지
    '초밥' : "https://cdn.hinative.com/attached_images/696135/b0b3a09c81ef53e2ab9cb8a56586229ac63838d6/large.jpg?1607229073",
    '오니기리' : "https://recipe1.ezmember.co.kr/cache/recipe/2015/04/14/4dcf7f2d9618f3c8a9da9fb82756d0071.JPG",
    '가츠동' : "https://ww.namu.la/s/d57991f21eba6b35e07f05f112fde972cdd5b4950dd6ed829644e0f92e06ee3ca12fb6e78d73df8d2b27b38dd01ef822ceb692f380b73ee6b91849e06456688e3550e5dbf9ad649bc5d393d2ab03ab8e",
    '규동' : "https://cdn-mart.baemin.com/sellergoods/main/0b878d17-2e3d-49d2-9a33-51e787619f01.jpg",
    '텐동' : "https://article-image-ix.nikkei.com/https%3A%2F%2Fimgix-proxy.n8s.jp%2FDSXMZO5899290012052020000001-1.jpg?ixlib=js-2.3.2&w=696&h=696&auto=format%2Ccompress&ch=Width%2CDPR&q=75&fit=crop&bg=FFFFFF&s=a50438923a2ce8882be9a2d1634fa140",

    '우동' : "https://udon0410.com/wp-content/themes/udon0410/assets/images/history01_01.png",
    '소바' : "https://i.ytimg.com/vi/xMM7etFZteA/maxresdefault.jpg",

    '타코야끼' : "https://1.gall-img.com/tdgall/files/attach/images/82/180/314/161/d2f75093fdc08688ccb84af2afe6ec54.jpg",
    '오코노미야끼' : "https://pbs.twimg.com/media/E64w9UCUcAIi9ea.jpg",
    
    '덴푸라' : "https://rimage.gnst.jp/livejapan.com/public/article/detail/a/00/00/a0000341/img/ja/a0000341_parts_5850d472d0cdc.jpg?20200706163250&q=80&rw=686&rh=490",
    '가라아게' : "https://image.wingeat.com/item/images/28d9990d-d2ea-4496-a5c5-2038e3d84824-w600.jpg",
    '돈까스' : "https://meeco.kr/files/attach/images/134/564/100/030/b6b7b90620afe1504a6aefd7427de9c2.jpeg",

    '오뎅나베' : "https://i.ytimg.com/vi/QP9LXNhwukY/maxresdefault.jpg",
    '샤브샤브' : "https://www.chungjungone.com/knowhow/images/blog/ezr/ker8/1.jpg",
    '스키야키' : "https://pbs.twimg.com/media/EwTQiJ9UYAIWR15.jpg",
    '부타나베' : "https://mblogthumb-phinf.pstatic.net/MjAxNzAyMDhfMTQw/MDAxNDg2NTMxNzc2NDU3.86qSFgfEWuya5PNy7N5bebHLoc7o5A6JA49C_-jrMiwg._xWxAVOPRx-D7nakK3xMUDz71Ep9XBGL0pllPw44Jlog.JPEG.roqkf0202/A73E8CED-38FD-42C0-B6E6-A8114C4AD8C6.JPG?type=w800",

    # 양식 이미지
    '토마토 파스타' : "https://sjnfzdfjrjgl1655541.cdn.ntruss.com/goods/7/2021/06/828_tmp_a243214ae2736918e91d0a6047178fb35360view.jpg",
    '크림 파스타' : "https://post-phinf.pstatic.net/MjAyMDEyMTRfMjQ2/MDAxNjA3OTMyMDExNzQx.GyHdnqKUOBeqSN5gYorGtf3bwfbeAX41ByPQ5n2BOgkg.MItqemxae4or50BtO-6cwYj8-ae7PzMkj6A5yszuvY8g.JPEG/4.jpg?type=w1200",
    '로제 파스타' : "https://sjnfzdfjrjgl1655541.cdn.ntruss.com/goods/2/2021/06/821_tmp_559f54016fcb596e0f449438b8bfe6d79520view.jpg",
    '알리오 에 올리오' : "https://i3.ruliweb.com/img/20/12/24/17694c5e1fc18beeb.jpg",
    '봉골레 파스타' : "http://storage.enuri.info/pic_upload/knowbox2/202107/11051795320210715bc57163d-bec6-4af0-aabd-8f4fa0d0908b.jpg",

    '하와이안 피자' : "https://joinsmedia.sfo2.digitaloceanspaces.com/news/1200-1934279980_tJUSodex_63e2898b98f6d8914be50797f5c94014f44f8e1c.jpg",
    '쉬림프 피자' : "https://dasima.xyz/wp-content/uploads/2021/01/mrpizza-shirimp-1.png",
    '고구마 피자' : "https://www.7thpizza.com/files/MENU/4AE67EEDFE5F421A8DA3C502FD6F8F18.jpg",
    '포테이토 피자' : "https://m.dibidibi.com:444/Data/GP/hg5n4uek98/DETAIL/c966776f-22ec-4dc0-8067-014c9cfd6502.jpg",
    '시카고 피자' : "https://image.fmkorea.com/files/attach/new/20200718/486616/2861024907/2995422168/e8ddff4876cb84b65085b81845f87481.jpg",

    '맥도날드' : "https://i2.wp.com/mediapanasonline.com/wp-content/uploads/2021/05/mcdonalds-exterior.jpg?fit=1024%2C750&ssl=1",
    '버거킹' : "https://lh3.googleusercontent.com/proxy/YMgSEKdubTXdCLvKsB8jKmYX5N_7YDbAr7WxHdQyklca0dAR2t45qJhmUOdQBhXL6Qi8gFNzio9uCq9yGnJvAC1AeHJyMFfJZwX_Sz1TNNQbOLItK1lBmA",
    '롯데리아' : "https://community.bitoc.co.kr/data/editor/2005/thumb-e0828900d623f993e514d6fbbda6a767_1589047899_4998_835x817.jpg",
    '맘스터치' : "https://www.kakazo.com/main/data/shop/sh_img_10_68197.jpg",
    '쉑쉑버거' : "https://img.insight.co.kr/static/2019/04/14/700/va4w57113mb91salj0cz.jpg",

    '후라이드 치킨' : "https://bbqchickenca.com/wp-content/uploads/2020/09/%ED%81%AC%EB%A6%AC%EC%8A%A4%ED%94%BC_TOP_%EB%88%84%EB%81%BC.png",
    '양념 치킨' : "https://blog.kakaocdn.net/dn/ob36q/btqugDbd3BW/8KNs8EscA7gf2ey8k2DqNK/img.jpg",
    '간장 치킨' : "https://file.namu.moe/file/8bc9e381797334eb33da66e3ba501be1461a607ecbec0886cc846e2afd9aaf592e236fac6ce44794218b9236b266202e058f51d3cddb464151ed255134391c3e",
    '파닭' : "http://file3.instiz.net/data/file3/2021/11/13/d/a/d/dad8a5e423663a9c3032a3007e0b2667.jpg",
    '닭강정' : "https://lh3.googleusercontent.com/proxy/LicCaN99DGSqbVIn_pnaX35woZIXL9BuLx4PyHzWgCFxGL0K3MrGF4H7WCyRccliUzjnnydd9hG474qkyoPcGQCJ-OZPfPe1v3EiHH_RX_VtVY-eJ1LkjsW9",
}

# @api_view(['GET', 'POST'])
def index(request):
    request_json = json.loads(request.body)
    print(request_json)

    # 해당 파라미터에 맞는 리스트에서 랜덤으로 하나 추출
    selected_food = random.choice(foods_dict[request_json['action']['params']['food_kinds']])
    print(selected_food)

    # 해당 음식에 맞는 이미지 URL 매핑
    if selected_food in food_URL_dict:
        food_URL = food_URL_dict[selected_food]
    else:
        food_URL = "https://lh3.googleusercontent.com/proxy/tKM9_Ws8Ib7MxNlcote2f0EyrK4xpbmBBzRHwaQ4IBZlysVglksraB1iMyGOCZ1rOwm3r5k7VFZ6hlNBDvZ2SXVlUXOed_Ixy2KAn7i9JzC1jDUcI1i2uyIrlZPSWzXBd8u0mzzN4O1u34t2bTRA7DvZzytlDMtOLDPqyA3tjkQ0_J2F"
   
    response_string = {
        "version": "2.0",
        "template": {
            "outputs": [
            {
                "basicCard": {
                "title": selected_food,
                "description": "라고 챗봇이 말했습니다.",
                "thumbnail": {
                    "imageUrl": food_URL
                },
                "profile": {
                },
                "social": {
                },
                "buttons": [
                ]
                }
            }
            ]
        }
    }
    response_json = json.dumps(response_string)
    return HttpResponse(response_json)


def health_check(request):
    response_string = "ok"
    response_json = json.dumps(response_string)
    return HttpResponse(response_json)