import logging


import logging
import requests
import util
import os
import cgit
class Github:
  def __init__(self, username, token):
    self.username = username
    self.token = token
  @staticmethod
  def check(*args, **kwargs):
    return util.try_run('git', *args, **kwargs)
  def getRepos(self):
    URL = "https://api.github.com/user/repos"
    HEADERS = {
      "Content-Type": "application/json",
      "Authorization": "Bearer {githubAccessToken}".format(githubAccessToken=self.token)
    }
    r = requests.get(url = URL, headers=HEADERS)
    data = r.json()
    return data
  def mirrorRepo(self, repo):
    repo_location = "./srv/git/{name}".format(name=repo['name'])
    self.check('clone', '--mirror', '--quiet', "git@github.com:{loc}".format(loc=repo['full_name']), repo_location )
    logging.info('Successfully cloned ' + repo['full_name'] + ' to ' + repo_location)
    cgit.CGit.write(cgit.CGit, repo_location, repo)
    logging.info('Wrote cgit info for ' + repo['full_name'])

    
