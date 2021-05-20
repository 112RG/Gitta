import logging
import util
import sys
from git import Github
def main():
  util.setup_logging()
  logging.info('Starting Gitta')
  github = Github('test', sys.argv[1])

  for repo in github.getRepos():
    github.mirrorRepo(repo)

if __name__ == '__main__':
    main()