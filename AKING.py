import platform

arch = platform.uname().machine
if 'aarch' in arch:
	import akin
	akin.main()
else:
	exit(' only 64bit supported!')
