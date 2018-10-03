
# Facial-Recognition-Independent-study

## Overview
[Facial Recognition](https://aws.amazon.com/rekognition/) with Amazon Web Services.

## Getting Started
[IDE For Development Here](<linkToDownloadIDE>)

### Local Configuration and Setup

## S3 Bucket Pricing

#### Description of the different storage classes:
https://aws.amazon.com/s3/storage-classes/

Pricing - https://aws.amazon.com/s3/pricing/

S3 Standard Storage
* First 50 TB / Month	$0.023 per GB
* Next 450 TB / Month	$0.022 per GB
* Over 500 TB / Month	$0.021 per GB



## Bounding Box
Documentation on bounding box: https://docs.aws.amazon.com/rekognition/latest/dg/API_BoundingBox.html

Identifies the bounding box around the face or text. The left (x-coordinate) and top (y-coordinate) are coordinates representing the top and left sides of the bounding box. **Note that the upper-left corner of the image is the origin (0,0).**
The top and left values returned are ratios of the overall image size. For example, if the input image is 700x200 pixels, and the top-left coordinate of the bounding box is 350x50 pixels, the API returns a left value of 0.5 (350/700) and a top value of 0.25 (50/200).

The width and height values represent the dimensions of the bounding box as a ratio of the overall image dimension. For example, if the input image is 700x200 pixels, and the bounding box width is 70 pixels, the width returned is 0.1.

#### Note
The bounding box coordinates can have negative values. For example, if Amazon Rekognition is able to detect a face that is at the image edge and is only partially visible, the service can return coordinates that are outside the image bounds and, depending on the image edge, you might get negative values or values greater than 1 for the left or top values.

## API Request and Response Syntax
1. [Amazon Rekognition Video StartFaceDetection](https://docs.aws.amazon.com/rekognition/latest/dg/API_StartFaceDetection.html)
```
{
   "ClientRequestToken": "string",
   "FaceAttributes": "string",
   "JobTag": "string",
   "NotificationChannel": { 
      "RoleArn": "string",
      "SNSTopicArn": "string"
   },
   "Video": { 
      "S3Object": { 
         "Bucket": "string",
         "Name": "string",
         "Version": "string"
      }
   }
}
```

2. [Amazon Rekognition Video GetFaceDetection](https://docs.aws.amazon.com/rekognition/latest/dg/API_GetFaceDetection.html)
```
{
   "JobId": "string",
   "MaxResults": number,
   "NextToken": "string"
}
```


## Data explanation
- Roll, Pitch, Yaw - https://www.youtube.com/watch?v=pQ24NtnaLl8
- Landmarks - https://docs.aws.amazon.com/rekognition/latest/dg/API_Landmark.html

## Python Tutorials
##### Introduction to Python 
   - https://www.codecademy.com/learn/learn-python
   - https://www.w3schools.com/python/
   - https://www.tutorialspoint.com/python/
   - https://www.reddit.com/r/learnpython/
##### Facial Recognition tutorials and Intermediate Python
   - [Getting Started with Face Recognition in Python](https://www.youtube.com/watch?v=IWoigw6-crg)
   - [Amazon Rekognition Code Samples](https://gist.github.com/alexcasalboni/0f21a1889f09760f8981b643326730ff)
   - [AWS Tutorial Series YouTube](https://www.youtube.com/channel/UClLLJjpSWRRa1BosQrNVDjA)
   - [AWS Tutorial Series Website](https://awstutorialseries.com)
