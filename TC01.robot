
*** Settings ***
Library  SeleniumLibrary
Library  Boto3_s3_configuration.py

*** Test Cases ***
TestCreateBucket
    ${bucketName}   create_bucket   firstpythonbucket   s3_resource
    log   ${bucketName}


TestUploadFiles
    upload_files   Hello.txt   firstpythonbucket3ddbd7da-1521-460f-b9ae-17061054463d


TestDownloadFiles
    ${is_downloaded}   download_files
    log   ${is_downloaded}


TestCheckFilePresent
    ${is_uploaded}   check_file_uploaded
    log   ${is_uploaded}









