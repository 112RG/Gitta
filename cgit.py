class CGit:
    def write(self, repo_dir, repo):
      with open(repo_dir + 'cgitrc', 'w') as fd:
          self._write_field(fd, 'clone-url', repo['clone_url'])
          self._write_field(fd, 'owner', repo['owner']['login'])
          self._write_field(fd, 'desc', repo['description'])
          self._write_field(fd, 'homepage', repo['html_url'])

    @staticmethod
    def _write_field(fd, field, value):
        if value is None:
            return
        fd.write(f'{field}={value}\n')