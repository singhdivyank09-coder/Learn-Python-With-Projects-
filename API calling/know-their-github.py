import requests #this module helps to access urls
def main():
    check_github(input('github username : ').strip()) 
    

def check_github(user):  #creating function accessing basic information of user using GitHub API 
    response= requests.get(f'https://api.github.com/users/{user}') 
    data=response.json() 
    print('PUBLIC REPOS:',data['public_repos'])
    print('FOLLOWERS:',data['followers'])
    print('PROFILE LINK:',data['html_url'])



if __name__=='__main__':
    main()