import os
import glob
from PIL import Image
#from numpy import sort
from random import randint,sample
import shutil



os.chdir("shelf")
label_names = [ p.replace('/', '') for p in sorted(glob.glob('*/')) ]

#label_names_1=sorted(label_names)
print "labels: "
print '\n'.join([ str(labels) for labels in label_names ])
print "\n"
with open('labels_names.txt','w') as in_files:
	for i in range(len(label_names)):
		in_files.write(label_names[i]+' '+str(i)+'\n')


if os.path.exists("/home/ubuntu/ARC/py-faster-rcnn/caffe-fast-rcnn/data/mini_dataset/train"):
	shutil.rmtree("/home/ubuntu/ARC/py-faster-rcnn/caffe-fast-rcnn/data/mini_dataset/train")
	print "deleting old train folder"
if os.path.exists("/home/ubuntu/ARC/py-faster-rcnn/caffe-fast-rcnn/data/mini_dataset/test"):
	shutil.rmtree("/home/ubuntu/ARC/py-faster-rcnn/caffe-fast-rcnn/data/mini_dataset/test")
	print "deleting old val folder"

os.mkdir("/home/ubuntu/ARC/py-faster-rcnn/caffe-fast-rcnn/data/mini_dataset/train")
os.mkdir("/home/ubuntu/ARC/py-faster-rcnn/caffe-fast-rcnn/data/mini_dataset/test")

train_list_file=open('/home/ubuntu/ARC/py-faster-rcnn/caffe-fast-rcnn/data/mini_dataset/train.txt', 'w')
test_list_file=open('/home/ubuntu/ARC/py-faster-rcnn/caffe-fast-rcnn/data/mini_dataset/test.txt', 'w')

#print "entering subfolders"
# under each subdir:
for i in range(len(label_names)):
	images_list = sorted(glob.glob(label_names[i]+"/"+"*"+"/*color*.png")) # subfolder:scene-0000
	testdata_not_traindata=sample(range(0,len(images_list)-1), len(images_list)/5)
	print "val files for ",label_names[i]," : ", testdata_not_traindata
#	print images_list
	for j in range(0,len(images_list)):
		images=images_list[j]
#       		print images
       		im=Image.open(images)
		im.resize([256,256])
		name_jpg="label_"+str(i)+"_"+images.split('/')[2].split('.')[0]+'.jpg'

#		print name_jpg
       		#if randint(0,14) <= 7:
		if j in testdata_not_traindata: 
			im.save("/home/ubuntu/ARC/py-faster-rcnn/caffe-fast-rcnn/data/mini_dataset/test/"+name_jpg)
			test_list_file.write(name_jpg+" "+str(i)+'\n')			
#			test_list_file.write("/test/"+name_jpg+" "+str(i)+'\n')			
		else:
			im.save("/home/ubuntu/ARC/py-faster-rcnn/caffe-fast-rcnn/data/mini_dataset/train/"+name_jpg)
			train_list_file.write(name_jpg+" "+str(i)+'\n')
#			train_list_file.write("/train/"+name_jpg+" "+str(i)+'\n')




