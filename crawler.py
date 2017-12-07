import luigi
from utils import mkdir 

class Crawler(luigi.Task):
    directory = luigi.Parameter(default='/tmp/downloads')

    def requires(self):
        return []

    def output(self):
        return luigi.LocalTarget(self.directory)

    def run(self):
    	mkdir(self.directory)

        print("hello world")