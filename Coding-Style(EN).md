#Coding rules and notes related to Real-Time. 

##INDEX

###ROS specific coding Notes
1.  Not to “publish” in random period.
2.  Node combining two or more topics, to publish at the stage of uniform two topics. 
3.  Always put a header in the topic and time stamp to inherit the value of previous topic. 
4.  Do not use of the service. 
5.　Not to topic large data. If unavoidable, use the “nodelet”. 
6.  Interdict the use of “MultiThreadSpin”.
7.  Interdict the usage for launch file output=”screen” 
8.  Avoid using “tf” as much as possible.

###Notes for the general embedded and real-time systems.
1.  Do not use wide variety of the library such as the chrono.
2.  For a functional argument, deploy the pointer and const reference pointer as much as possible. 
3.  Use the reference argument as a result of the function.
4.  Avoid dynamic partitioning, such as malloc and new. 
5.  If the size of vector is roughly estimable, use reserve. 
6.  Avoid monster function that spans more than 50 lines. 
7.  Make effective use of inline.
8.  Naming functions, such as get and set, shall not have processing code described.

###Fine coding conventions
※Appreciate if any collaborator can add, as needed.

Must read (at least once) http://qiita.com/shirakawa4756/items/55b509fb56cb1bb0c9a4
If time allows, strongly advised http://www.textdrop.net/google-styleguide-ja/cppguide.xml

Other recommendations for reading 
* Effective C++ (recommend)
* ReadableCode (recommend)
* CODE COMPLETE
* C++ Coding Standards
 
##ROS specific coding Notes

-  Not to “publish” in random period.
-  Basicaly, the topic must publish once updated, In other words, there is a need to publics hin the callback.
Following is bad example of coding.
```
while(ros::ok()) {
    publisher.publish(hogehoge);
    loop.sleep();
}
```
- Node combining two or more topics, to publish at the stage of uniform two topics.
For example, if you subscribe to A,B topic, do not publish in the call back function of A, which is updated only A topic.  Both A,B topic being updated and pair must be made in order to perform publish.   

###SAMPLE CODE### 
```
A_callback(A_msg) {
    if (is_b_callback == true){ // When A topic has been updated already 
        publish(hogehoge); // publish the data
        is_a_callback = false;
        is_b_callback = false;
        return;
    }
    is_a_callback = true;
}
B_callback(B_msg) {
    if (is_a_callback == true){
        publish(hogehoge);
        is_a_callback = false;
        is_b_callback = false;
        return;
    }
    is_b_callback = true;
}
```

- Always put a header in the topic and time stamp to inherit the value of previous topic.  Update must not be performed without inheritance of the header’s time stamp. Yet, when combining 2 topic together, either topic’s header time stamp can be inherited. 
*Time stamp of two topics header will be the same by synchronization.
 
-  Do not use of the service.  When the service and topic are mixed, real-time estimate becomes difficult.  Basically, it should be carried out in a topic-based.  In non-real-time portion not involved in the recognition, judgment and control of the automated driving operation may utilise the service. 

- Not to topic large data. If unavoidable, use the “nodelet”.  Big data requires few msec to serialize-deserialize, for that reason, large data, such as graphics should utilise the nodelet and invalidate serialize-deserialize. 

- Interdict the use of “MultiThreadSpin”.  When MultiThreadSpin is used, from the point of view of real-time scheduling, it is not preferable because it will become rapidly more complex. You shall not use the MultiThreadSpin in the processing that requires real-time process.

- Interdict the usage for launch file output=”screen”  It is OK for debugging use, however, output=”screen” described file should NEVER be pushed to Git. Other person’s terminal information will be leaked. Basically, do not check rgt, but check  ROS_INFO and ROS_DEBUG from node. 

- Avoid using “tf” as much as possible. For getting location information by using current_pose.  tf library and ROS are separated (not exactly devided, however), it is difficult to secure real-time.  To unify as much as possible to the topic-base, avoid using tf. In addition, tf is very effective when there’s many joints such as arm robot, but not very effective if determined statically coordinate relationship such as automatic driving operation.  

##Notes for the general embedded and real-time systems.
-  Do not use wide variety of the library such as the chrono. It will greatly reduces the portability of the RTOS. Do not use them, such as chrono, but utilise ros::WallTime.

-  For a functional argument, deploy the pointer and const reference pointer as much as possible.  int or double is not necessary to use a const call by reference, but the vector or array should use a const call by reference. It reduces the memory consumption and at the same time, it will reduce overhead of the function call.

-  Use the reference argument as a result of the function.  Pass by return value, the speed is significantly slower.  Therefore, including call by reference and pointer, these return value for passing the result to argument should be used.  Pointer, careful attention has to be paid to the scope of the contents of the data.  Basically, return value may use for the error, such as success or failure.
http://nonbiri-tereka.hatenablog.com/entry/2014/02/18/091945

-  Avoid dynamic partitioning, such as malloc and new. malloc and new will cause memory leak to happen.  In addition, It should be avoided as much as possible in order to prevent it difficult to estimate the use size of the resource.

-  If the size of vector is roughly estimable, use reserve. Capacity shortage in the vector, allocate twice the area.  From the experiences, when shortage occur on a large vector, it requires large amount of time to secure, therefore, it is recommended to use the reserve to allocate area in advance.
http://qiita.com/amayaw9/items/6e55b91c28cdc8d32cf2

-  Avoid monster function that spans more than 50 lines. Basically, any function should be kept around 20-30 lines. In addition, bear in mind the particle size of the processing in the function to align.
*I remember reading in “Effective C++”, sophisticated code method is average of 14 lines.
 
-  Make effective use of inline. Few lines of function maybe expanded to inline.  However, it may lead to the increase of the footprint. Caution!

###Bad Example###
```
callback() {
    start_time = clock_get_time(); // Particle size and degree of abstraction is small 
    compute_xxxx(); // Particle size and degree of abstraction is large
}
```
-  Naming functions, such as get and set, shall not have processing code described.
Programmer shall not describe time consuming processs to get or set.  Only the acquisition and storage of value should be performed by get and set. Another idea is to be able to provide hint/estimate for processing time by the name and heavy function should use computeXXXX. 
