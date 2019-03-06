from django.shortcuts import render
import random

def index(request):
    cafeteria = ["하루돈가스", "신촌 황소곱창", "진원조 닭한마리", "설레임", "삼호복집", "애슐리W", "더 맵군", "신촌 형제갈비", "고바우", "에머이", "구복", "죽이야기"]
    xCafeteria = ["37.5582143", "37.5584257", "37.5573685", "37.5571547", "37.5564816", "37.5562575", "37.5570126", "37.5577357", "37.5582872", "37.5574399", "37.5573808", "37.5558409"]
    yCafeteria = ["126.935851", "126.9350512", "126.9357239", "126.9348882", "126.934986", "126.9345501", "126.9341126", "126.9372059", "126.9373125", "126.9375047", "126.938277", "126.9377515"]
    select_cafeteria = random.choice(cafeteria)
    index_num = cafeteria.index(select_cafeteria)
    x = xCafeteria[index_num]
    y = yCafeteria[index_num]
    
    recommend_sentence = [1, 2, 3, 4 ,5]
    select_recommend_sentence = random.choice(recommend_sentence)
    complete_sentence = recommend(select_recommend_sentence, select_cafeteria)
    return render(request, 'index.html', {'cafeteria' : complete_sentence, 'x' : x, 'y' : y})

def recommend(sentence_num, cafeteria):
    sentence_list = {
        1 : "오늘은 <" + cafeteria + "> 어떠신가요?",
        2 : "<" + cafeteria + ">" + " 여기 JMT 더라구요!",
        3 : "배고플 땐 <" + cafeteria + "> (으)로!",
        4 : "저의 강력추천 맛집은 <" + cafeteria + "> 이에요!",
        5 : "<" + cafeteria + ">" +" 여기 맛집이라던데요?"
    }
    return sentence_list.get(sentence_num, "에러 발생")