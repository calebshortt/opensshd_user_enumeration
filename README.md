# OpenSSHD User Enumeration
A simple script that takes advantage of OpenSSHD 7.2p2 - User Enumeration: CVE 2016-6210.

Can take a list of usernames and try them against a server -- looks to find users in the system.
Built from the sample code specified at https://www.exploit-db.com/exploits/40113/

# Usage

> python opensshd.py [-h] [-u --userlist USERLIST_FILE] target_ip

# Results

[attempted username]    [rejection speed]   [* if flagged or of interest]

Ex:
> testuser      0.0356

> root          0.5625      *

Note: The * is a flag that marks usernames of interest and that might be in the target system.


