from tqdm import tqdm
import requests
import datetime

time_ref = datetime.datetime.now()

# get file name from time_ref

suffixes = ['f006', 'f012', 'f018', 'f024', 'f030', 'f036']

test_file_name = 'p06m_2019102400f006.grb'

def get_grib(file_name):
    url = 'https://ftp.wpc.ncep.noaa.gov/2p5km_qpf/{f}'.format(f=file_name)

    response = requests.get(url, stream=True)

    with open(file_name, "wb") as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)

get_grib(test_file_name)

# read grib2 file

# convert grib2 file to shape file

# write shape file to db