python crop_rotate_v3.py --weights /Users/Projects/cvision/ID/yolov5/weights/best.pt --conf 0.25 --source /Users/Projects/cvision/ID/yolov5/test

- labeling images
- 



python3 detect-xs.py --weights /Users/nguyentruongthuc/Projects/cvision/ID/yolov5/weights/best.pt --source /Users/nguyentruongthuc/Projects/LTN/cv-xsangiang/data/test

python3 train.py --batch 8 --epochs 50 --data custom_data.yaml --weights /Users/nguyentruongthuc/Projects/cvision/ID/yolov5/weights/best.pt

python3 -m torch.distributed.run --nproc_per_node 2 train.py --batch 8 --epochs 50 --data custom_data.yaml --weights /Users/Projects/cvision/ID/yolov5/weights/best.pt --device 0,1 --master_addr="127.0.0.1" --master_port=$RANDOM

python3 train.py  --batch 8 --epochs 50 --data custom_data.yaml --weights /Users/Projects/cvision/ID/yolov5/weights/best.pt --device 0,1
