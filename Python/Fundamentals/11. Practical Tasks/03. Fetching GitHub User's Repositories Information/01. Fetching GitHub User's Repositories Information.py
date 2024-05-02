import requests

def fetch_user(username):
    url = f"http://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        repositories = response.json()
        return repositories
    else:
        print("Error!")
        return None


def display_repo(repositories):
    if repositories:
        print("\nUser's Repositories: ")
        print(repositories)
        for repo in repositories:
            print("\nRepository Name:", repo["name"])
            print("Description:", repo["description"])
            print("Language", repo["language"])
            print("ID:", repo["id"])
            print("HTML", repo["html_url"])



def main():
    username = input("Enter username: ")
    repositories = fetch_user(username)
    if repositories:
        display_repo(repositories)


if __name__ == "__main__":
    main()
