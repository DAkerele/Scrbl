
import os
from PIL import Image
import img2pdf
import handTrackBenchMarkB as ht
from config import *
from google.oauth2 import service_account
import sys
import importlib
#importlib.reload(sys)
#sys.setdefaultencoding('utf8')
from google.cloud import vision
from google.cloud import storage
from google.protobuf import json_format
from doc_txt_detect import detect_hand_writtent_text
credentials = service_account.Credentials.from_service_account_file("new_auth.json")
#os.system("python handTrackBenchMarkB.py")
ht.start()

input_dir=os.path.dirname(os.path.abspath(__file__))

if os.path.isdir(input_dir):
    print("Input directory path is valid")
else:
    print("\n Entered path is not valid please check the format and enter again ")
    os._exit(1)

data_dir=os.path.dirname(os.path.abspath(__file__))
"""
if not os.path.isdir(os.path.abspath(data_dir)+"/001"):
    print("Could not find the input directory (001) in entered path. Please check the input path")
    os._exit(2)
"""
if not os.path.exists(os.path.abspath(data_dir)+"/output/"):
        os.makedirs(os.path.abspath(data_dir)+"/output/")

#for input_file in os.listdir(data_dir+"/001"):
input_file = "Roboto.pdf"
storage_client = storage.Client(credentials=credentials)
bucket = storage_client.get_bucket(BUCKET_NAME)
blob = bucket.blob("input/"+input_file)
blob.upload_from_filename(os.path.dirname(os.path.abspath(__file__))+"\\"+input_file)
gcs_source_uri = "gs://" + BUCKET_NAME + INPUT_BUCKET_PATH+input_file
gcs_destination_uri= "gs://" + BUCKET_NAME + OUTPUT_BUCKET_DIR
detect_hand_writtent_text(gcs_source_uri, gcs_destination_uri, input_file)
#detect_hand_writtent_text(gcs_source_uri,gcs_destination_uri , os.path.abspath(data_dir)+"/output/"+input_file)
print("All files are processed. Please find the output in data/output directory..")

#gcs_destination_uri="gs://mldata101/"
#gcs_source_uri="gs://mldata101/FORM-FREETEXTINOUTBOXES_4.pdf"
#async_detect_document(gcs_source_uri,gcs_destination_uri,"result.txt"