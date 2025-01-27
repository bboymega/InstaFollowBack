# FollowBack
Checking Accounts that are not following back on Instagram with account dumped file HTML

It use local HTML file dumped from Instagram "Request Download" instead of direct loggin the account to avoid getting banned.

# To use this script a local copy of Instagram account data is required. 

Here's the step of dumping your account data in HTML format.

1) Log in your Instagram account with browser
2) Go to Settings > Privacy and Security > Data Download > Request Download

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
# Disclaimer 
FollowBack runs completely offline and does not collect, store, or share personal information from Instagram users without their consent. Any use of Instagram’s content (such as images, text, or other media) is subject to Instagram’s Terms of Service and Community Guidelines. Users are responsible for ensuring their use of the platform complies with these terms.

FollowBack is not affiliated with, endorsed by, or in any way officially connected to Instagram, Inc., or any of its subsidiaries or affiliates. Instagram®, INSTA® and GRAM® are registered trademarks of Meta Platforms, Inc. All trademarks, service marks, and trade names are the property of their respective owners.

FollowBack is intended solely for educational, informational, or entertainment purposes. It is not intended for commercial use unless explicitly stated otherwise. Any commercial use is at your own risk and should comply with Instagram’s terms and applicable laws.
