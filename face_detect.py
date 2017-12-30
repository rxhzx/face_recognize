
#-*-coding:utf-8-*-
import os
import cv2
import dlib
#创建脸部集文件目录
outfile_dir='./myface'
if not os.path.exists(outfile_dir):
	os.makedirs(outfile_dir)
#人脸检测
detector = dlib.get_frontal_face_detector()
#获取摄像头
capture = cv2.VideoCapture(0)
while(1):
	#读取一张照片
	#frame = cv2.imread('/home/ren/下载/1001.png')
	#从摄像头中获取照片
	ret,frame=capture.read()
	#将当前图片转换为灰度图像
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
	faces = detector(frame, 1)
	#确定标识人脸的矩形框的颜色
	color = (0, 255, 0)
	#frame图像，起点坐标，终点坐标（在这里是x+w,y+h,因为w,h分别是人脸的长宽）颜色，线宽）
	for face in faces:
		x = face.left()
		y = face.top() #could be face.bottom() - not sure
		w = face.right() - face.left()
		h = face.bottom() - face.top()
		#参数：原始图，标识人脸矩形块的左上，右下坐标，矩形颜色，线宽
		cv2.rectangle(frame,(x,y),(x+w+1,y+h+1),color,2)
	#显示人脸检测结果
	cv2.imshow("capture", frame)
	#按q退出
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break
#释放摄像头，关闭窗口
capture.release()  
cv2.destroyAllWindows()  


