import subprocess


class Process(object):

    def __init__(self, command):
        self.command = command
        self.process = self.run()
        self.output = self.output()
        self.error = self.error()

    def run(self):
        process = subprocess.Popen(self.command, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        return process

    def output(self):
        line = self.process.stdout.readline().lstrip()
        return line

    def error(self):
        error = self.process.stderr.readline().lstrip()
        return error

    def write_line(self, line):
        self.process.stdin.writeline(line)
