import boto3
import uuid

s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')


def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(uuid.uuid4())])


def create_bucket(bucket_prefix, s3_connection):
    bucket_name = create_bucket_name(bucket_prefix)
    print(bucket_name)
    return bucket_name


'''-----------------To create a bucket----------------------'''


# first_bucket_name, first_response = create_bucket(
#    bucket_prefix='firstpythonbucket', s3_connection=s3_resource)


def upload_files(file_name, bucket_name, object=None, args=None):
    if object is None:
        object = file_name
    response = s3_client.upload_file(file_name, bucket_name, object, ExtraArgs=args)
    print(response)


'''-----------------To upload files in bucket----------------------'''


# upload_files('Hello.txt', 'firstpythonbucket3ddbd7da-1521-460f-b9ae-17061054463d')


def download_files():
    names_of_file = []
    bucket = s3_resource.Bucket('firstpythonbucket3ddbd7da-1521-460f-b9ae-17061054463d')
    files = list(bucket.objects.all())
    print("Start downloding")
    for file in files:
        s3_client.download_file('firstpythonbucket3ddbd7da-1521-460f-b9ae-17061054463d', file.key, file.key)
        names_of_file.append(file.key)
    print(names_of_file)
    return 'pictures\\OIP.jfif' in names_of_file


'''-----------------To download and check file downloaded in bucket----------------------'''


# is_downloaded = download_files()
# print(is_downloaded)


def check_file_uploaded():
    FilesInBucket = []
    ListOfItems = s3_client.list_objects_v2(Bucket='firstpythonbucket3ddbd7da-1521-460f-b9ae-17061054463d')
    for obj in ListOfItems['Contents']:
        FilesInBucket.append(obj['Key'])
    print(FilesInBucket)
    return 'Hello.txt' in FilesInBucket


'''-----------------To download and check file downloaded in bucket----------------------'''
# is_uploaded = check_file_uploaded()
# print(is_uploaded)
