# RepoPeek - Take a Sneak Peek at Repositories.

RepoPeek is a python script to get details about a repository just from your terminal before cloning it. All the information are retrieved using the [GitHub API](http://developer.github.com/v3/repos/). 

Please Note: In this script API requests aren't using basic authentication or OAuth. Therefore the rate limit allows for up to 60 requests per hour. Unauthenticated requests are associated with the originating IP address, and not the user making requests. (You can use a VPN to overcome this situation.)

![iaa1](https://user-images.githubusercontent.com/55880211/80363200-7d35a000-88a1-11ea-8afe-0e3f688eb180.gif)

## Features
1. Basic information about the repository.
   - Repository Name
   - Default Branch
   - Repository Size
   - Repository License
   - Repository Description

2. Languages used in the repository.

3. Repository Statistics.
   - Forks
   - Watchers
   - Open Issues
   - Total Stars
   
4. URL's of the repository.
   - GIT URL
   - SSH URL
   - SVN URL
   - Clone URL
   
5. Cloning repositories.

### Git Installation
```
# clone the repo
$ git clone https://github.com/sameera-madushan/RepoPeek.git

# change the working directory to RepoPeek
$ cd RepoPeek

# install the requirements
$ pip3 install -r requirements.txt
```

## Usage

```
python repopeek.py
```

### Support & Contributions
- Please ⭐️ this repository if this project helped you!
- Contributions of any kind welcome!

## License
MIT ©[sameera-madushan](https://github.com/sameera-madushan)
