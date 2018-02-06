#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

EXAMPLE=/home/ubuntu/ARC/py-faster-rcnn/caffe-fast-rcnn/data/mini_dataset/
DATA=/home/ubuntu/ARC/py-faster-rcnn/caffe-fast-rcnn/data/mini_dataset/
TOOLS=/home/ubuntu/ARC/py-faster-rcnn/caffe-fast-rcnn/build/tools

$TOOLS/compute_image_mean $EXAMPLE/mit_train_lmdb \
  $DATA/mit_mean.binaryproto

echo "Done."
