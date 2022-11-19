# InstaFollowBack
Checking Accounts that are not following back on Instagram with account dumped file HTML

It use local HTML file dumped from Instagram "Request Download" instead of direct loggin the account to avoid getting banned.

# To use this script a local copy of Instagram account data is required.

1) Log in your Instagram account with browser
2) Go to Settings > Privacy and Security > Data Download > Request Download

<img src="a0.png" alt="a0" width="200"/>
<img src="a1.png" alt="a1" width="200"/>

3) Unzip the dumped File and navigate to followers_and_following.
```
followers.html
following.html
```

This script compares the difference between followers.html and following.html for checking accounts that are not following back.

<img src="a2.png" alt="a2" width="200"/>
<img src="a3.png" alt="a3" width="200"/>

# Example
```
instafollowback.py -i /path/to/following.html -e /path/to/followers.html
```
The script will print the account names that are not following back.

# Output
![image](output.png)

# Help

```
usage: instafollowback.py [-h] [-i FOLLOWING_FILE] [-e FOLLOWER_FILE]
optional arguments:
  -h, --help            show this help message and exit
  -i FOLLOWING_FILE, --following FOLLOWING_FILE
                        Following List Html Dump
  -e FOLLOWER_FILE, --follower FOLLOWER_FILE
                        Followers List Html Dump
```
# Front-end
Front-end webpage of this project is available at <a href="https://github.com/bboymega/InstaFollowingBack-Web">InstaFollowingBack-Web</a>
