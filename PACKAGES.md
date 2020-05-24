# Creating s3pkg packages

An s3pkg package file consists of two parts: a manifest and a .tar.gz containing files to be installed.

## Manifests
Manifests consist of three sections: package information, package-specific directories/permissions and package-specific files/permissions.

## Example manifest
  name: my-great-package
  version: 0.1
  description: provides disruptive tools to collaboratively iterate cost effective methods of empowerment
  [dir] /usr/local/my-great-tool 0755
  [dir] /usr/local/my-great-tool/config 0755
  [dir] /usr/local/my-great-tool/secure 0644
  my-great-package /usr/local/bin/my-great-tool 0755
  my-great-config /usr/local/my-great-tool/config 0755
  credentials /usr/local/my-great-tool/secure 0600

## Details
The first three lines detail the package information.

After that, list the directories that need to be created specifically for this package. The first field must be [dir]. The second field is the directory name (no trailing slash). The third field is the permissions that should be applied to the new directory. The directories should be listed in order of nesting depth (start with the highest-leve directories and work your way down).

Finally, list the files that will be installed. The first field is the name of the file (which should match the filename in the .tar.gz containing the package files). The second field is the destination directory (no trailing slash). Finally, the third field contains the permissions that should be applied to the new directory.

## Notes
* Filenames and directory names must not contain ':'. 
* Filenames must not equal '[dir]'.
* The name of the .tar.gz file should be a concatenation of 'name', '-', 'version' and '.tar.gz' (e.g. my-great-package-0.1.tar.gz).
