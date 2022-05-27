import joblib
from django.shortcuts import render
import ai.tag_predict
from ML.models import Tag


# from ai.mlPredict import pred_tag

def start(req):
    return render(req, 'ML/index.html')

def index(req):
    return render(req, 'ML/index.html')

#값 입력 받는 부분
def insert(req):
    return render(req, 'ML/insert.html')

#입력받은 값을 db에 저장하는 부분
def insert2(req):
    # 1. 입력한 정보를 post로 받아오자.
    data = req.POST
    print('입력한 정보 >> ', data)
    # 2. 입력한 값을 db에 저장하기위해 one변수에 넣어보자.
    # 브라우저에서 입력한 값 one에 넣기.Tag는 db컬럼 클래스.(models.py에 있다.)
    one = Tag(week1=data['week1'], week2=data['week2'], hour=data['hour'],
              gender=data['gender'], age=data['age'], size=data['size'],
              tag_click=data['tag_click'])
    # 3. 받은 데이터를 db에 저장하자.
    one.save()

    # 4. context를 이용하여 post로 받은 값을 담은 변수 one을 return해주자.
    #   insert2.html에서 one을 받아 id를 출력해주자.({{ one.id }})사용.
    context = {'one': one}
    return render(req, 'ML/insert2.html', context)

# 검색할 아이디 입력 받는 부분
def one(req):
    return render(req, 'ML/one.html')


# 검색한 입력값의 id를 가져와 검색 처리리
def one2(req):
    data = req.POST  # req파라메터에 POST로 넘어온 것 전부다 data로 받음
    print('서버에서 받은 데이터(views.py)>> ', data)
    print('id:', data['id'])
    # 2.db에서 값을 가져와보자.
    # get을 쓰면 검색 결과가 많아도 값 하나만  가져옴
    idValue = data['id']
    one = Tag.objects.get(id=idValue)
    print('db검색한 결과', one)
    context = {'one': one}
    print('insert2 db검색결과(one).>> ', one)
    # print('insert2 one을 찍어보자.>> ', list)
    # result_tag = pred_tag('받은 데이터의 리스트')
    return render(req, 'ML/one2.html', context)

#ML
# python을 거처 카테고리 분류한 값이 넘어와서 템플릿으로 출력해주는 함수
def output(req, id):
    # 1. one변수를 이용하여 입력받은 id에따른 db의 값을 가져오자.
    # 리스트에 db의 값들을 넣고 ai폴더의 함수를 이용하여 정확도 예측을 해보자.
    one = Tag.objects.get(id=id)
    input_tag = [one.week1, one.week2, one.hour, one.gender,
                 one.age, one.size, one.tag_click]
    print('output전달받은 예측할 id는 ', id)
    print('output리스트에 넣은 예측값은 ', input_tag)

    # ML프로젝트 함수를 읽어와 input_tag를 넣어보자.
    tag_pred = ai.tag_predict.load_pkl(input_tag)
    result = {'tag': tag_pred}
    return render(req, 'ML/output.html', context=result)

#시각화처리
#월 평균 구매빈도-3회 이상 (%)의 그래프
def chart(req):
    #20대~60대까지의 수치를 data에 담음.
    data = [47.475000,48.463462,44.905769,39.793303,39.933024]
    context = {
        'data' : data
    }
    return render(req, 'ML/chart.html', context)

#각 앙상블로 측정한 정확도 예측 % 비교 그래프
def chart2(req):
    #lr_acc,dt_acc,hard_acc,soft_acc,rf_acc 순서대로 카테고리 정확도 예측 값을 data에 담음.
    data = [0.6297657326596233,0.816260909508498,0.6196600826825908,
            0.8171796049609554,0.6669728984841525]
    context = {
        'data' : data
    }
    return render(req, 'ML/chart2.html', context)