# Facial-Recognition-Independent-study

## Overview
[Facial Recognition](https://aws.amazon.com/rekognition/) with Amazon Web Services.

## Getting Started
[IDE For Development Here](<linkToDownloadIDE>)

### Local Configuration and Setup

## S3 Bucket Pricing
https://aws.amazon.com/s3/pricing/

## Bounding Box
Documentation on bounding box: https://docs.aws.amazon.com/rekognition/latest/dg/API_BoundingBox.html

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

