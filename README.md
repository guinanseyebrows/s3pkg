# s3pkg
### A package manager using s3 buckets as remote repos

## What?
s3pkg is intended for use as a secondary simple package manager that uses an AWS S3 bucket for remote storage.

Its goal is to provide an easy way to maintain a custom repository of scripts/utilities/anything else to be installed on hosts without having to generate more-complicated .rpm/.deb files. 

It's currently written in POSIX sh because I'm a sadist.

**Features**
* install a package: `s3pkg install <pkg_name>`
* remove a package: `s3pkg remove <pkg_name>`

## But *why*?
![Yeah, why?](https://i.imgur.com/dfaI4bI.png)
I don't feel like maintaining an RPM repo or creating .rpm packages for 30-line shell scripts, and I'm sick of manually running 'aws s3 cp' and 'chmod +x' whenever I need to pull a script from an S3 bucket. 

It's also going to be nice not to have to call scripts with paths, since they'll just get installed to /usr/bin/ or whatever.

## Caveats
* Don't name your scripts anything that might already exist in your /usr/bin.
* In fact, don't name your scripts anything that might already exist in any repos you might use with your system's package manager.

## TODO
* cleanup removed packages
* dependency resolution (kill me)
* pre/post script support
* separate bootstrap into new script
* package generation framework/script (oof)
