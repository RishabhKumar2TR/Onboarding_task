
*** Settings ***
Library  SeleniumLibrary
Library  Boto3_s3_configuration.py

*** Variables ***
${file_name}  Hello.txt
${bucket}  firstpythonbucket3ddbd7da-1521-460f-b9ae-17061054463d
${Bucket_name_prefix}  firstpythonbucket

*** Test Cases ***
TestBucketname
    ${bucket_name}=   Get name of S3 bucket created   ${Bucket_name_prefix}   s3_resource
    log   ${bucket_name}

TestDownloadFiles
    ${is_downloaded}   Download Files
    Should be true   ${is_downloaded}

TestCheckFilePresent
    Upload file to S3   ${file_name}   ${bucket}
    ${is_uploaded}   Check File Uploaded
    Should be true   ${is_uploaded}

*** Keywords ***
Upload file to S3
   [Arguments]   ${file_name}   ${bucket}
   Upload Files   ${file_name}   ${bucket}

Get name of S3 bucket created
   [Arguments]   ${bucket_prefix}   ${connection}
   ${bucket_name}=   Create Bucket   ${bucket_prefix}   ${connection}
   RETURN   ${bucket_name}










