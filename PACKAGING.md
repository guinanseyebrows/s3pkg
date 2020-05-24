# Creating s3pkg packages
An s3pkg package file consists of two parts: a manifest and a .tar.gz package archive containing files to be installed.
## Manifests
Manifests consist of three sections: package information, package-specific directories/permissions and package-specific files/permissions.

#### Details
The first three lines detail the package information.

After that, list the directories that need to be created specifically for this package. The first field must be [dir]. The second field is the directory name (no trailing slash). The third field is the permissions that should be applied to the new directory. The directories should be listed in order of nesting depth (start with the highest-leve directories and work your way down).

Finally, list the files that will be installed. The first field is the name of the file (which should match the filename in the .tar.gz containing the package files). The second field is the destination directory (no trailing slash). Finally, the third field contains the permissions that should be applied to the new directory.

#### Example manifest
```name: my-great-package
version: 0.1
description: provides disruptive tools to collaboratively iterate cost effective methods of empowerment
[dir] /usr/local/my-great-tool/config 0755
[dir] /usr/local/my-great-tool/secure 0644
my-great-package /usr/local/bin/my-great-tool 0755
my-great-config /usr/local/my-great-tool/config 0755
credentials /usr/local/my-great-tool/secure 0600```

#### Notes
* Filenames and directory names must not contain ':'. 
* Filenames must not equal '[dir]'.
* The name of the .tar.gz file should be a concatenation of 'name', '-', 'version' and '.tar.gz' (e.g. my-great-package-0.1.tar.gz).

## Package archive
The package archive is just a .tar.gz containing all the files to be installed as detailed in the manifest. Do not nest the files in subdirectories - those will get created via the manifest.

One shortcoming of s3pkg is that it's relatively inconvenient to create packages that require many nested files, but that falls outside of the intended use case. s3pkg should be used as a secondary package manager and may not be appropriate for complex packages that are better suited to your OS's package management system.
