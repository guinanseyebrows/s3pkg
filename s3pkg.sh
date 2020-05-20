#!/bin/sh

# writing a package manager in sh because i am an idiot

# dependency check
command -v aws >/dev/null 2>&1 || { printf >&2 "ERROR: AWS CLI utilities are not installed.\n" ; exit 1; } 
command -v jq >/dev/null 2>&1 || { printf >&2 "ERROR: jq is not installed.\n" ; exit 1; } 

option=$1
packagename=$2
bucketname="bt-pkg"
repo="packages"
local_dir="/usr/local/s3pkg"
cache_dir="${local_dir}/.cache"
local_pkglist="${local_dir}/pkglist"

prefix="${repo}/${packagename}"

if [ ! "$option" ] ; then printf "USAGE: $0 <install/remove/update/search> <package-name>\n" ; exit ;fi

bootstrap () {
mkdir -p "${local_dir}/{bin,.cache}"
touch "${local_pkglist}"
}

get_remote_pkg () {
    if [ ! "${packagename}" ] ; then printf "USAGE: $0 "${option}"  package-name\n" ; exit ;fi

    remote_pkg=$(aws s3api list-objects-v2 \
        --bucket "$bucketname" \
        --query "Contents[?contains(Key, '${prefix}/${packagename}-')].Key" \
        --output text  )

    if [ ! "${remote_pkg}" ] ; then 
        printf "${packagename} not found.\n"
        exit 1
fi
}
search () {
    get_remote_pkg
    printf "${remote_pkg}\n" | sed 's:.*/::'
}

install () {
    get_remote_pkg
    if [ $(grep ${packagename} ${local_pkglist}) ] ; then
        echo "$packagename already installed."
        exit
        else
            aws s3 cp s3://${bucketname}/${remote_pkg} "${cache_dir}" 
            # untar into cachedir
            # while read manifest
                # ignore lines that start with #
                # chmod file using 3rd field in manifest
                # move file into destination directory described in 2nd field in manifest
                
           printf "${remote_pkg}\n" | sed 's:.*/::' >> "${local_pkglist}" 
    fi
}

"${option}" 
