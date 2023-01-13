# Rocket Elevators Django API

Welcome to Rocket Elevators Facial Recognition API


* First Endpoint : http://127.0.0.1:8000/employees/ - to get a list of every entry in the employee database.

* Second Endpoint : http://127.0.0.1:8000/register/ - to add a new employee with a photo, the photo will then be encoded and stored in the keypoints column.

* Third Endpoint : http://127.0.0.1:8000/facialrecognition/ - to take the image file you attached, encodes it then finds a match to the encoded information in the keypoints column of the database and returns the employee information.


### Postman Collection:
https://api.postman.com/collections/24446774-c86eff5a-20ab-414f-b8a6-3dc685060d0e?access_key=PMAT-01GPNZC4N0HHG0ZPBTD5G4GKQ8