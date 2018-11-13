# CHAPTER 3 Linux Basics and System startup 

## Startup process
### BIOS
> Basic Input/Output system 
Initialize the hardware (screen, keyboard) and test the main memory.  
Also called POST (Power On Slef Test)
BIOS software is stored on ROM in MotherBoard.

### Master Boot Record (MBR) and Boot Loader
Stored in one of the hard disk of teh machine (boot sector/ EFI partition).
Take the system control. Search for bootloader and load it in RAM
When booting Linux, bootloader is responsible for loading the kernel ant the initial RAM disk or filesystem 

#### Boot loader in action 
for BIOS/MBR, the bootloader reside on the first sector of the hard disk (also know as Master Boot Record).
Bootloader search for a bootable partition and then load GRUB into RAM.
For UEFI, it read the Boot Manager data and the firmware launches the UEFI application (GRUB).
Second stage bootloader always reside in `/boot`.
After choosing OS, the boot loader load the kernel and pass control to it.

### Initial RAM Disk

`initramfs` filesystem image contains programs and binary files that perform all actions needed to mount the proper root filesystem.  
If this is successful, the initramfs is cleared from RAM and the init program on the root filesystem `/sbin/init` is executed.

### Text-Mode Login 
init starts text-mode login to enable user to login.

## Linux Kernel
> The boot loader loads both the kernel and an initial RAM–based file system (initramfs) into memory.

When the kernel is loaded in RAM, it immediately initializes and configures the computer’s memory and also configures all the hardware attached to the system. This includes all processors, I/O subsystems, storage devices, etc. The kernel also loads some necessary user space applications.

### `/sbin/init`

 initial process, which then starts other processes to get the system running.  
 init is responsible for keeping the system running and for shutting it down cleanly.  

### systemd features 

systemd = parallelization
systemd use simple configuration file to startup, stop, restart services
Now, `/sbin/init` point to `/lib/systemd/systemd`. 
`systemd` command is `systemctl`
Starting, stopping, restarting a service (using nfs as an example) on a currently running system: 
`$ sudo systemctl start|stop|restart nfs.service`
Enabling or disabling a system service from starting up at system boot:
`$ sudo systemctl enable|disable nfs.service`

**`.service` can be omitted**


## Linux Filesystems 

Different types of filesystems supported by Linux:

 * Conventional disk filesystems: ext2, ext3, ext4, XFS, Btrfs, JFS, NTFS, etc.
 * Flash storage filesystems: ubifs, JFFS2, YAFFS, etc.
 * Database filesystems
 * Special purpose filesystems: procfs, sysfs, tmpfs, squashfs, debugfs, etc.

### Partitions an dfilesystems
A partition is a physically contiguous section of a disk, or what appears to be so in some advanced setups.

A filesystem is a method of storing/finding files on a hard disk (usually in a partition). 

## Gloasry

MBR : Master Boot Record
(U)EFI : (Unified) Extensible Firmware Interface 
GRUB : GRand Unified Boot loader
