import sys
import yaml
import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))


if __name__ == '__main__':
    with open('.github/workflows/tmp.txt') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        print(data)
    magnet = sys.argv[1]
    content = {
  'name': get_random_string(18),
  'on': {
    'push': {
      'branches': ['master']
    }
  },
  'jobs': {
    'build': {
      'runs-on': 'windows-latest',
      'strategy': {
        'matrix': {
          'node-version': ['16.x']
        }
      },
      'steps': [{
        'uses': 'actions/checkout@v3'
      }, {
        'name': 'Use Node.js',
        'uses': 'actions/setup-node@v3',
        'with': {
          'node-version': '16.x'
        }
      }, {
        'name': 'Set up Python 3.10',
        'uses': 'actions/setup-python@v3',
        'with': {
          'python-version': '3.10'
        }
      }, {
        'name': 'Install dependencies',
        'run': 'python -m pip install --upgrade pip\npip install wheel\npip install -r requirements.txt\n'
      }, {
        'name': 'ins',
        'run': 'npm install git+https://github.com/Persie0/webtorrent-cli-timelimit -g'
      }, {
        'name': 'download',
        'run': 'webtorrent '+magnet,
      }, {
        'name': 'Upload',
        'uses': 'Difegue/action-megacmd@master',
        'with': {
          'args': 'put . .'
        },
        'env': {
          'USERNAME': '${{ secrets.USERNAME }}',
          'PASSWORD': '${{ secrets.PASSWORD }}'
        }
      }, {
        'name': 'Commit files',
        'run': 'git config --local user.email "41898282+github-actions[bot]@users.noreply.github.com"\ngit config --local user.name "github-actions[bot]"\ngit commit -m "Downloading" -a\ngit pull -r\n'
      }, {
        'name': 'Push changes',
        'uses': 'ad-m/github-push-action@master',
        'with': {
          'github_token': '${{ secrets.ADD_NEW }}',
          'branch': '${{ github.ref }}'
        }
      }]
    }
  }
}

    f=open('.github/workflows/slow_magnet_progress.yml', 'w')
    yaml.dump(content, f)
    f.close()
