# age_gender_project

학습 모델
Resnet18
![image](https://user-images.githubusercontent.com/76443227/180386580-6c929a46-ff1e-490a-a988-7fb0b3e08a26.png)

 
train결과 
gen_acc = 74%
age_acc = 57%
 ![image](https://user-images.githubusercontent.com/76443227/180386626-cfc978a2-2ad8-4385-acc2-1cce86c352ea.png)

Test 결과
gen_acc = 74%
age_acc = 57%



학습 모델2
Resnet32
 ![image](https://user-images.githubusercontent.com/76443227/180386668-67906988-6b6e-41c3-a8c7-9c1a061c82d4.png)

Train 결과
gen_acc = 71%
age_acc = 59%

![image](https://user-images.githubusercontent.com/76443227/180386708-5cf195bc-ccff-4d5c-b4f5-9bfb5bdac355.png)

Test 결과
gen_acc = 71%
age_acc = 59%

gender accuracy가 생각보다 낮게 출력되어 성별의 구분이 힘든 유아와 아동들을 제외하고 다시 test를 했습니다.
![image](https://user-images.githubusercontent.com/76443227/180386743-3581d1c8-e4d8-4676-b96b-835947a1503c.png)

![image](https://user-images.githubusercontent.com/76443227/180386763-e4d04ae4-1a2e-40ec-bf85-4a066793a82f.png)

 
Test 결과
gen_acc = 79%
age_acc = 54%

연령대 별 age와 gender accuracy의 이상치가 있는거 같아 연령대별로 나누어 accuracy를 보도록 하였습니다.
2 classification = 8 ~14
3 classification = 15 ~ 24
4 classification = 25 ~ 37
5 classification = 38 ~ 47
6 classification = 48 ~ 59
7 classification = 60세 이상
![image](https://user-images.githubusercontent.com/76443227/180386806-bfb3d2c1-b7fd-4b1b-b962-60b4529d43d3.png)

 
결과
2 Classification = gender_acc: 57%, age_acc : 62% 
3 classification = gender_acc : 80%, age_acc : 48%
4 classification = gender_acc : 81%, age_acc : 64%
5 classification = gender_acc : 97%, age_acc : 7%
6 classification = gender_acc : 84%, age_acc : 48%
7 classification = gender_acc : 80%, age_acc : 80%


영상 결과
![zzz](https://user-images.githubusercontent.com/76443227/184066863-e30389db-172c-4cbf-ae89-ffc2a2bd9b99.PNG)
![as](https://user-images.githubusercontent.com/76443227/184066868-12531252-bcb8-4b1b-aacf-129cd9112a50.PNG)

weigh 파일 가중치 업데이트 중요!!

