import luigi

class Crawler(luigi.Task):
    crawler_path = luigi.Parameter(default='/tmp/')

    def requires(self):
        return []

    def output(self):
        return luigi.LocalTarget(crawler_path)

    def run(self):
        print >> "hello world"