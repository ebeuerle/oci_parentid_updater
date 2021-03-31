#Prisma Cloud OCI CSV Parent ID

Version: *1.0*
Author: *Eddie Beuerlein*

### Summary
This script will ingest an OCI only alert ```.csv``` file and for each alert, it will pull the parent name and add a column with that data.  

### Requirements and Dependencies

1. Python 3.7 or newer

2. OpenSSL 1.0.2 or newer

(if using on Mac OS, additional items may be nessessary.)

3. Pip

```sudo easy_install pip```

4. Requests (Python library)

```sudo pip install requests```

5. YAML (Python library)

```sudo pip install pyyaml```


### Configuration

1. In alert overview, make sure to filter on OCI cloud type and then download the CSV.

2. Place the CSV file to be checked in the ```/main``` directory of this repository after pulling down from GitHub.

3. Navigate to ```config/configs.yml```

4. Fill out your Prisma Cloud access key/secret, stack info, and CSV filename to be scanned.  
   *To determine stack, look at your browser when access console (appX.prismacloud.io, where X is the stack number.  
   Change this to apiX.prismacloud.io and populate it in the configs.yml.  
    Or go here for more information:* https://api.docs.prismacloud.io/

### Run

```
python main.py
```
