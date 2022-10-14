from bs4 import BeautifulSoup
from lxml import html
import argparse,sys
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--following", default='./',dest="following_file", help="Following List Html Dump", action="store")
parser.add_argument("-e", "--follower", default='./',dest="follower_file", help="Followers List Html Dump", action="store")
args=parser.parse_args()
if len(sys.argv) < 2:
    parser.print_usage()
    sys.exit("Error: Missing Parameters")

following = html.parse(args.following_file)
follower = html.parse(args.follower_file)
following_list_stored=[]
follower_list_stored=[]
following_page = html.tostring(following)
follower_page = html.tostring(follower)
following_soup = BeautifulSoup(following_page,features="html.parser")
follower_soup = BeautifulSoup(follower_page,features="html.parser")
following_list = following_soup.find_all("a", {"target": "_blank"})
follower_list = follower_soup.find_all("a", {"target": "_blank"})

for following_account_raw in following_list:
    for following_account in following_account_raw:
        following_list_stored.append(following_account)

for follower_account_raw in follower_list:
    for follower_account in follower_account_raw:
        follower_list_stored.append(follower_account)

print("------ACCOUNTS NOT FOLLOWING BACK (USERNAME)------\n")
for account_check in following_list_stored:
    if account_check not in follower_list_stored:
        print(account_check)
