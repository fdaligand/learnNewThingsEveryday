##Filesystems

Linux supports a number of native filesystem types, expressly created by Linux developers, such as:
 * ext3
 * ext4
 * squashfs
 * btrfs. 

It also offers implementations of filesystems used on other alien operating systems, such as those from:
 * Windows (ntfs, vfat)
 * SGI (xfs)
 * IBM (jfs)
 * MacOS (hfs, hfs+).
j
Many older, legacy filesystems, such as FAT, are also supported.

![mount point](img/mount_point.jpg)


If you want it to be automatically available every time the system starts up, you need to edit `/etc/fstab` accordingly (the name is short for filesystem table). Looking at this file will show you the configuration of all pre-configured filesystems. `man fstab` will display how this file is used and how to configure it.