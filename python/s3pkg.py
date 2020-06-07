#!/usr/bin/env python3

import boto3

# bootstrap function
# create cache directory, manifest directory and empty package list

'''
need to define vars if not bootstrapping:
        reconfig_dir:
        bucket_name
        prefix
        cache_dir
        local_pkglist


# get_package_data function
# return remote package name (which includes the version number)
# from the bucket. this function uses list-objects-v2 to find the 
# package that starts with the package name and has a '-' immediately 
# following, eg: mypackage = mypackage-0.1.tar.gz.  if not found, 
# return an error and exit.
# 

# get_remote_manifest function
# return the contents of the remote manifest that matches the pattern
# 'packagename'.manifest. if not found, return error and exit.

# search subcommand function
# calls get_remote_manifest and selects just the lines containing 
# details. right now, the dash version returns lines containing ':'
# which indicate details (name, version, description). this is clever
# but not entirely clear unless the user implicitly understands 
# the manifest syntax.

# install subcommand function
# first, use get_remote_package to set a remote package variable. 
# determine if the package is installed. if so, and the installed 
# version is less than the remote version, return a message that the
# user should run the update subcommand instead. if the local package
# is the same version and the --force option is not specified, return 
# a message that the package is already installed and then exit.
# otherwise, print a message that the installation is proceeding.
# retrieve the manifest and store it in the manifest directory. based on
# the version number in the manifest, either retrieve the remote package 
# and store it in the package cache directory, or use the local .tar.gz
# if the versions match.
# create a new directory in the package cache using the name of the package
# without the version number, then decompress/untar the package contents
# into that directory. 
# next, load the directory and file portions of the manifest into a dict.
# for all directory entries in the dict, create the directory and apply the
# permissions associated with the directory entry. this should be done in
# order of depth starting with the shallowest and moving toward the deepest. 
# for each directory created, save the directory name into a package install
# file under manifest_dir/pkg_name.install. this is based on using mkdir -p 
# in the dash version, so i need to figure this one out for python.
# for all file entries, move the filename that matches the entry from the
# package cache folder into the specified directory, then apply the correct
# permissions. finally, add the package name/version to the local package
# list and return a message stating that the package is installed and exit.

# remove subcommand function
# check the local packagelist to determine whether the package is installed.
# if not, return an error stating so and exit.
# otherwise, read the file entries from the manifest into an array. for 
# each array item, remove the file. next, read the install file to recursively 
# remove any directories created by the package, but remove each one 
# at a time starting from deepest and moving to shallowest.
# it may be nice at some point to retain directories and files files not 
# installed by the package manager but for now we will assume fairly 
# blunt force operation.
# finally, clean up (remove the package name from the package list and remove
# local install and manifest files, and then the package directory. finally,
# print a message that the package has been removed and exit.

# update subcommand function
# accepts one argument (a single package). if no arguments are passed,
# read the contents of the package list into a dict/array.
# using the contents of the single argument or the data structure,
# run the install command for each package specified using the 
# --force option.
