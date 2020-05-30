# RepoPeek - Take a Sneak Peek at Repositories

RepoPeek is a Python script to get details about a repository without cloning
it. All the information are retrieved using the
[GitHub API](http://developer.github.com/v3/repos/).

Please Note: API requests made by this module aren't using basic authentication or
OAuth. Therefore the rate limit allows for up to 60 requests per hour.
Unauthenticated requests are associated with the originating IP address.

![iaa1](https://user-images.githubusercontent.com/55880211/80460274-3bfcc900-8951-11ea-9814-66779d8f8f4f.gif)

## Information Provided

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
   
5. Commit details of the repository
   - Last Commit Date
   - Last Commit Message

## Installation

To install this script so that it is accessible via Python from anywhere, copy
the script into a directory of your choice, and then add that directory to your
`PYTHONPATH`

## Usage

```
python -m repopeek
```

## Support & Contributions

- Please ⭐️ this repository if this project helped you!
- Contributions of any kind welcome!

## License

RepoPeek is made with ♥ by [@_\_sa_miya__](https://twitter.com/__sa_miya__) and it is released under the MIT license.

## Contributors

Thanks goes to this wonderful person. :heart:

<table>
  <tr>
    <td align="center"><a href="https://github.com/WillDaSilva"><img src="https://avatars3.githubusercontent.com/u/11428666?s=400&u=b704bfcf6ce6f94f55fdf0b8a973389417b0243e&v=4" width="100px;" alt=""/><br /><sub><b>William Da Silva</b></sub></a></td>

</table>
