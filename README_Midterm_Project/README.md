# Mid Term Project - 3D Object Detection
Author : Shreyansh Shethia 

In this project, the LiDAR measurements are transformed into range and height images with a birds-eye-view angle. Then an off-the-shelf CNN model is used to classify the objects in those images into car, pedestrians, and cyclists. The real-world data from the Waymo Open Dataset is used.

### ID S1 EX1

![ids1ex1_0](results/s1ex1/IDS1EX1_0.jpg)
*Upper Image is the range and lower image shows intensity*

### ID S1 EX2

In this exrcise, the lidar point cloud datapoint are visualized.
The closer points are blue in color and farther points are red in color.

![ids1ex2_t1](results/s1ex2/t1.png)

Following  video shows the point clouds being captured at different time stamps.

![ids1ex2_t2345](results/s1ex2/t2345.png)

In the images, the flow of cars and their respective shadows show that the ego vehicle is moving from left to right in the bev.

Below shows the vehicles at different locations and their visibility.

![ids1ex2_v1](results/s1ex2/deg_visibility_v1.png)
* Clear visibility of vehicle moving in opposite direction. Vehicles farther from our sensor have low number of datapoints and less obvious features. apart from front bonnet, side doors are also obsevred. 

![ids1ex2_v2](results/s1ex2/deg_visibility_v2_REAR_CARS.png)
* Rear vehicles trailing behind the ego vehile shows only the windsield and bonnet.

![ids1ex2_v3](results/s1ex2/deg_visibility_v2_REAR_RIGHT_DISTANT_CARS.png)
* Some vehicles are visbile to be at a perpendicular direction as compared to our vehicle

![ids1ex2_v4](results/s1ex2/deg_visibility_v4_occlusion_due_to_vehicleoutoffov.png)
* When any other vehicle gets too close, it gets out of FOV

![ids1ex2_v5](results/s1ex2/deg_visibility_v5_vehicle_behind_vehicle.png)
* This shows a vehicle being occluded by other vehicle

![ids1ex2_v6](results/s1ex2/deg_visibility_v3_TRUCK_TRAILER.png)
* Looks like a pick-up Truck and a Trailer

 - Below shows a few identifiable feature of a car in the images 

![ids1ex2_v6](results/s1ex2/t12_better_view_2.png)
* Side mirrors and Front Windshield 

![ids1ex2_v7](results/s1ex2/some_feature_v1.png)
* Side doors and windows, rear bumper, tires, front bonnet is visible  


### ID S2 EX1 
![ids2ex1_v1](results/s2ex1/pcl_f2.png)

### ID S2 EX2 
![ids2ex2_v1](results/s2ex2/all_compare.png)
* BEV Image shows different normalization of Range values based upon different %ile and max-min

![ids2ex2_v2](results/s2ex2/955_982_closeup.png)
* BEV Image shows a close look at normlization comparison between 95-5 % ile and 98-2 % ile. 98-2 %ile shows no clippings or close to clipping and hence is chosen as the base.

### ID S2 EX3 

![ids2ex3_v1](results/s2ex3/height_img.png)
* BEV Image with Height  

![ids2ex3_v2](results/s2ex3/height_img_values.png)
* BEV Image with Height (closer looks)

### ID S3 EX1-5 

![ids3ex15_v1](results/s2ex3/detections.png)
* Detection Variable

### ID S3 EX2 

![ids3ex2_v1](results/s3ex2/detect_images_51.png)
* Detection results with bounding box on BEV Lidar and Camera  

![ids3ex2_v2](results/s3ex2/v2.png)
* Detection output (red) is overlayed with ground truth (green)  

### ID S4 EX2 

![ids3ex2_v1](results/s4ex2/s4ex3.png)
* Precision nad recall: when the detection algorithm is run over 100 images. 

![ids3ex2_v2](results/s4ex2/S4EX3_truedetection.png)
* Precision and recall: when ground truths are used, to check the code calculating the values correctly.


