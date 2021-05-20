import logging
import sys
import subprocess
def setup_logging(verbose=False):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S',
        format='%(asctime)s | %(levelname)s | %(message)s',
        # Log to stdout, because that's where subprocess's output goes (so that
        # the don't get interleaved).
        stream=sys.stdout)
def run(*args, capture_output=False, **kwargs):
    stdout = None
    stderr = None
    if capture_output:
        stdout = subprocess.PIPE
        stderr = subprocess.STDOUT

    logging.debug('%s', args)
    result = subprocess.run(args, check=True, stdout=stdout, stderr=stderr,
                            encoding='utf-8', **kwargs)

    if result.stdout is not None:
        logging.debug('\n%s', result.stdout)
    return result.stdout
def try_run(*args, **kwargs):
    try:
        run(*args, **kwargs)
        return True
    except subprocess.CalledProcessError as e:
        return e.returncode == 0