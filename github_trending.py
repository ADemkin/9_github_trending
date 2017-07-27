import requests
import datetime


def get_date_weekstart():
    today = datetime.datetime.now()
    week = today.replace(day = (today.day - today.weekday()))
    return week.date()


def get_trending_repositories(top_size):
    # make a request using github api
    # keys: created since monday, sorted by number of stars
    payload = {'q':'created:>' + str(get_date_weekstart()), 'sort':'stars', 'order':'desc'}
    request = requests.get('https://api.github.com/search/repositories', params=payload)
    return request.json()['items'][:top_size]


def print_repo_info(repo):
    print("Name: %s, open issues: %s \n%s" % ((repo["name"]), (repo["open_issues"]), (repo["html_url"])))

def main():
    try:
        top_size = 20
        top_repos = get_trending_repositories(top_size)
    except requests.exceptions.ConnectionError as error:
        print("Connection error: %s" % error)
    else:
        for repo in top_repos:
            print_repo_info(repo)


if __name__ == '__main__':
    main()