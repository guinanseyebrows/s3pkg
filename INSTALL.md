# Installation
1. Clone or download the s3pkg repo to the target system.
1. Create a directory to install s3pkg to (default `/usr/local/s3pkg/`)
1. Edit s3pkg/doc/config to point at the s3 bucket/prefix you want to use for your repo
1. Move s3pkg/doc/config to the s3pkg directory you created earlier
1. Run `s3pkg bootstrap <path_to_s3pkg_dir>`

