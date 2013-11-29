satellite-api-scripts
=====================

A few handy RHN Satellite API scripts.

common.py:
	Handles login information. Edit accordingly.

clone_epel_6.py:
	Clone EPEL6 into your satellite.
	SAMPLE USAGE:	$ ./clone_epel_6.py

channel2repo.py: 
	Downloads channel content, creates local yum repo. Takes multiple -c arguments.
	SAMPLE USAGE:	$ ./channel2repo.py --createrepo -c jbappplatform-6-x86_64-server-6-rpm
			$ ./channel2repo.py --createrepo -c jbappplatform-6-x86_64-server-6-rpm -c rhel-x86_64-server-6
