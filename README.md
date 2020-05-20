# s3pkg
### a package manager using s3 buckets for remote repos

## what?
s3pkg is intended for use as a secondary simple package manager that uses an AWS S3 bucket for remote storage.
Its goal is to provide an easy way to maintain a custom repository of scripts/utilities/anything else to be installed on hosts without having to generate more-complicated .rpm/.deb files. 
It's currently written in POSIX sh because I'm a sadist.

## why?
I don't feel like creating .rpm packages for 30-line shell scripts, and I'm sick of manually running 'aws s3' and 'chmod +x' whenever I need to pull a script from an S3 bucket. It's also going to be nice not to have to call scripts with paths, since they'll just get installed to /usr/bin.

## caveats
Don't name your scripts anything that might already exist in your /usr/bin.
In fact, don't name your scripts anything that might already exist in any repos you might use with your system's package manager.
Yes, I could just learn how to build RPMs.