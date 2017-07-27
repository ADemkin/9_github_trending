import requests
import datetime
import json

def get_date_week_ago():
    today = datetime.datetime.now()
    week = datetime.timedelta(days=7)
    week_ago = today - week
    return(week_ago.date())
    
def get_trending_repositories(top_size):
    # search for github repositories using github api
    # keys: created less than week ago, sorted by number of stars
    request =  requests.get('https://api.github.com/search/repositories?q=created:>'
                     + str(get_date_week_ago())
                     + '&sort=stars&order=desc')
    json_data = json.loads(request.content)
    json_most_common = json_data["items"][:top_size]
    return json_most_common

def get_open_issues_amount(repo):
    print(repo["open_issues"])


def print_repo_info(repo):
    repo_name = repo["name"]
    repo_open_issues = repo["open_issues"]
    repo_url = repo["html_url"]
    print("Name: %s, open issues: %s \n%s" % (repo_name, repo_open_issues, repo_url))

if __name__ == '__main__':
    try:
        top_repos = get_trending_repositories(20)
    except requests.exceptions.ConnectionError as error:
        print("Connection error: %s" % error)
    else:
        for repo in top_repos:
            print_repo_info(repo)
