import sys


def get_firefox_profile_dir():
    if sys.platform in ['linux', 'linux2']:
        import subprocess
        cmd = "ls -d /home/$USER/.mozilla/firefox/*.default/"
        p = subprocess.Popen([cmd], shell=True, stdout=subprocess.PIPE)
        FF_PRF_DIR = p.communicate()[0][0:-2]
        FF_PRF_DIR_DEFAULT = str(FF_PRF_DIR, 'utf-8')
    elif sys.platform == 'win32':
        import os
        import glob
        APPDATA = os.getenv('APPDATA')
        FF_PRF_DIR = "%s\\Mozilla\\Firefox\\Profiles\\" % APPDATA
        PATTERN = FF_PRF_DIR + "*default*"
        FF_PRF_DIR_DEFAULT = glob.glob(PATTERN)[0].replace("\\", "/") + "/"
    else:
        raise ValueError("This platform is not supported")

    return FF_PRF_DIR_DEFAULT


def get_chrome_user_dir():
    if sys.platform == 'win32':
        import os
        import glob
        APPDATA = os.getenv('APPDATA').replace("\\Roaming", "")
        USER_DATA_DIR = "{}\\Local\\Google\\Chrome\\User Data\\".format(APPDATA).replace("\\", "/")

        return USER_DATA_DIR
    else:
        raise ValueError("This platform is not supported")
