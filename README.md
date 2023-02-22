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


### 

