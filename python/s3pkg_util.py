# s3pkg_util - various utility functions used by s3pkg

import boto3
from os import path

'''
get_matching generators sourced from 
https://alexwlchan.net/2019/07/listing-s3-keys/
'''

def get_matching_s3_objects(bucket, prefix="", suffix=""):
    s3 = boto3.client("s3")
    paginator = s3.get_paginator("list_objects_v2")
    kwargs = {'Bucket': bucket}

    if isinstance(prefix, str):
        prefixes = (prefix, )
    else:
        prefixes = prefix

    for key_prefix in prefixes:
        kwargs["Prefix"] = key_prefix

        for page in paginator.paginate(**kwargs):
            try:
                contents = page["Contents"]
            except KeyError:
                break

            for obj in contents:
                key = obj["Key"]
                if key.endswith(suffix):
                    yield obj

def get_matching_s3_keys(bucket, prefix="", suffix=""):
    for obj in get_matching_s3_objects(bucket, prefix, suffix):
        yield obj["Key"]

def get_package_data(bucket, prefix, suffix):
    '''
    retreives either package .tar.gz or manifest file names
    '''
    filename = []
    files = get_matching_s3_keys(bucket, prefix, suffix)
    for i in files:
        filename += [i]
    
    if len(filename) > 1:
        raise Exception("Package name too ambiguous or suffix not specified")
    
    return str(filename[0])

def retrieve_manifest(package_name, destination):
    '''
    retrieves manifest file from remote repository.
    by default, download to cache_dir/package_name.
    '''
    remote_manifest = prefix + '/' + package_name + '.manifest'
    s3 = boto3.client('s3')
    s3.download_file(bucket, remote_manifest, destination)

def retrieve_package(package_name, destination):
    '''
    retrieves package .tar.gz from remote repository.
    by default, download to cache_dir/package_name.
    '''
    remote_package = get_package_data(bucket, prefix, 'tar.gz')
    s3 = boto3.client('s3')
    s3.download_file(bucket, remote_package, destination)


def parse_manifest(packagename):
    '''
    parse manifest into dict to create folders and install paths
    '''
    # assign manifest_file to path of manifest file
    # if file does not exist, raise exception
    manifest
    
    # read manifest into new data structure
    ''' 
    info_regex finds info lines such as:
        name: package_name
        version: 2.3
        description: this is a package i like
    and splits them into [0]: [1] tuples.
    '''
    info_regex = re.compile(r'^(.*): (.*)$')

    '''
    file_regex finds file/directory lines such as:
        <dir> /path/to/dir 0775
        filename /path/to/dir 0755
    and splits them into [0] [1] [2] tuples:
    [0] is either a filename or an indication that 
    this line should be a directory.
    [1] is the path to the file, and
    [2] is the permissions (3 or 4 digits) that should
    should be applied to the directory or file upon install.
    '''
    file_regex = re.compile(r'^(.*) (.*) (\d{3,4})')


def install_package(package_name):
    '''
    install_package installs a package.
    first checks to see if the most recent version exists
    in the cachedir. if so, install from local. if not, retrieve
    package and continue with installation.
    '''

