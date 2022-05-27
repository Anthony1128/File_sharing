# File storage with access by http protocol

## App run

To start the app do the following:
- from the root folder of the app run next commands:
 1. `export FLASK_APP=app`
 2. `flask run`
- follow the provided link from command line

To run the app with gunicorn run next command:
- `gunicorn 'app:create_app()'`

## Implementation

The App has three main functionalities:
1. Upload
  User uploads a file of any format into the form and gets the hash of a file as a response. The file itself is uploaded to the server store/ab/abcdef12345..., where "abcdef12345..." - name of a file (its hash). /ab/  - subfolder which is the first two letters from hash.
2. Download
  User enters file name (its hash) into the form. In case the system finds the file with such name user gets this file downloaded. Otherwise, the app returns 404.
3. Delete
  User enters file name (its hash) into the form. In case the system finds the file with such name files is deleted from server. Otherwise, the app returns 404.

## Tools

[flask](https://flask.palletsprojects.com/en/1.1.x/) is used for implementation.
hashlib lib is used for getting hash by md5 algorithm.
