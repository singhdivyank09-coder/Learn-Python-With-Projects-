import requests #this module helps to access urls
def main():
    user = input('github username : ').strip()
    if not user:
        print("Username cannot be empty.")
        return

    if check_github(user):
        # Ask if they want to look up a specific repository
        repo_name = input('\nenter repository name to get its link (or press enter to skip): ').strip()
        if repo_name:
            check_repo(user, repo_name)
    

def check_github(user):  #creating function accessing basic information of user using GitHub API 
    response = requests.get(f'https://api.github.com/users/{user}') 
    
    # Handle user not found or other API issues
    if response.status_code == 404:
        print(f"Error: GitHub username '{user}' not found.")
        return False
    elif response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return False

    data = response.json() 
    print('PUBLIC REPOS:', data.get('public_repos', 0))
    print('FOLLOWERS:', data.get('followers', 0))
    print('PROFILE LINK:', data.get('html_url'))
    return True

def check_repo(user, repo_name):  #creating function accessing specific repository using GitHub API
    response = requests.get(f'https://api.github.com/repos/{user}/{repo_name}')
    
    # Handle repo not found or other API issues
    if response.status_code == 404:
        print(f"Error: Repository '{repo_name}' not found for user '{user}'.")
    elif response.status_code == 200:
        data = response.json()
        print(f"\nREPO '{repo_name.upper()}' LINK: {data.get('html_url')}")
    else:
        print(f"Error: Received status code {response.status_code}")


if __name__=='__main__':
    main()

