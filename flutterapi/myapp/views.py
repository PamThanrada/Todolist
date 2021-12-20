from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TodolistSerializer
from .models import Todolist
from myapp import serializers

#Get Data
@api_view(['GET'])
def all_todolist(request):
    alltodolist = Todolist.objects.all() #ดึงข้อมูลจากmodels Todolist
    serializer = TodolistSerializer(alltodolist, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#Post Data (sava data to database)
@api_view(['POST'])
def post_todolist(request):
    if request.method == 'POST':
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_todolist(request, TID):
    #localhost:8000/api/update-todolist/TID
    todo = Todolist.objects.get(id=TID)

    if request.method == 'PUT':
        data = {}
        serializer = TodolistSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status'] = 'updated'
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_todolist(request, TID):
    todo = Todolist.objects.get(id=TID)
    
    if request.method == 'DELETE':
        delete = todo.delete()
        data = {}
        if delete:
            data['status'] = 'deleted'
            statuscode = status.HTTP_200_OK
        else:
            data['status'] = 'failed'
            statuscode = status.HTTP_400_BAD_REQUEST
        return Response(data=data, status=statuscode)




data = [
    {
        "title": "ทุเรีย",
        "subtitle": "ทุเรียนคือ.....",
        "image_url": "https://raw.githubusercontent.com/PamThanrada/BasicAPI/main/durian.jpg",
        "detail": "ทุเรียน เป็นไม้ผลในวงศ์ฝ้าย (Malvaceae) ในสกุลทุเรียน (Durio) (ถึงแม้ว่านักอนุกรมวิธานบางคนจัดให้อยู่ในวงศ์ทุเรียน (Bombacaceae)ก็ตาม เป็นผลไม้ซึ่งได้ชื่อว่าเป็นราชาของผลไม้ ผลทุเรียนมีขนาดใหญ่และมีหนามแข็งปกคลุมทั่วเปลือก อาจมีขนาดยาวถึง 30 ซม. และอาจมีเส้นผ่าศูนย์กลางยาวถึง 15 ซม. โดยทั่วไปมีน้ำหนัก 1-3 กิโลกรัม"
    },
    
    {
        "title": "สัปปะรด",
        "subtitle": "สัปปะรดคือ.....",
        "image_url": "https://raw.githubusercontent.com/PamThanrada/BasicAPI/main/pineapple.jpg",
        "detail": "สับปะรดเป็นผลไม้เขตร้อนที่อุดมไปด้วยวิตามิน แร่ธาตุ ใยอาหาร และมีเอนไซม์บรอมมีเลน (bromelain) ซึ่งเป็นสารสำคัญที่มีฤทธิ์ทางเภสัชวิทยาที่น่าสนใจหลายอย่าง ปัจจุบันนอกจากการนำสับปะรดมาบริโภคในรูปแบบของผลไม้สดและใช้เป็นส่วนประกอบในอาหารและขนมต่างๆ แล้ว ยังมีการนำสับปะรดมาแปรรูปเป็นผลิตภัณฑ์ต่างๆ ได้หลายชนิด เช่น สับปะรดกระป๋อง สับปะรดอบแห้ง สับปะรดแช่แข็ง น้ำผลไม้ น้ำส้มสายชู ไวน์สับปะรด อุตสาห์กรรมเบียร์ อุตสาหกรรมอาหาร อุตสาหกรรมอาหารสัตว์ และการใช้ในผลิตภัณฑ์เครื่องสำอาง ซึ่งช่วยเพิ่มมูลค่าทางการตลาดให้กับสับปะรดได้เป็นอย่างดี"
    },
    {
        "title": "ฝรั่ง",
        "subtitle": "ฝรั่งคือ.....",
        "image_url": "https://raw.githubusercontent.com/PamThanrada/BasicAPI/main/guava.jpg",
        "detail": "ฝรั่งเป็นผลไม้ที่มีถิ่นกำเนิดในแถบอเมริกากลางและในหมู่เกาะอินดีสตะวันตก และคาดว่ามีการนำเข้ามาในประเทศไทยในช่วงสมัยของสมเด็จพระนารายณ์มหาราช โดยสายพันธุ์ในบ้านเราที่นิยมนำมารับประทานสด ๆ ก็ได้แก่ฝรั่งกิมจู ฝรั่งเวียดนาม ฝรั่งแป้นสีทอง ฝรั่งไร้เมล็ด ฝรั่งกลมสาลี่ เป็นต้น ฝรั่งเป็นผลไม้ที่อุดมไปด้วยวิตามินและแร่ธาตุหลายชนิด โดยจัดเป็นผลไม้ที่มีวิตามินซีสูงที่สุดในบรรดาผลไม้ทุกชนิด ในฝรั่งน้ำหนัก 165 กรัม จะให้วิตามินสูงถึง 377 มิลลิกรัม ! มีวิตามินซีสูงกว่าส้มถึง 5 เท่า !"
    }


]

def Home(request):
    return JsonResponse(data=data,safe=False,json_dumps_params={'ensure_ascii': False})



