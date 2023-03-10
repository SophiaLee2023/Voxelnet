import os

os.chdir("./crop_data/")

lines_train = [line.rstrip('\n') for line in open('train.txt')]
lines_val = [line.rstrip('\n') for line in open('val.txt')]

for i in lines_train:
  os.remove('training/calib/'+i+'.txt')
  os.remove('training/image_2/'+i+'.png')
  os.remove('training/label_2/'+i+'.txt')
  os.remove('training/velodyne/'+i+'.bin')

for i in lines_val:
  os.remove('validation/calib/'+i+'.txt')
  os.remove('validation/image_2/'+i+'.png')
  os.remove('validation/label_2/'+i+'.txt')
  os.remove('validation/velodyne/'+i+'.bin')