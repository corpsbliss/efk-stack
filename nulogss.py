from logparser.NuLog import NuLogParser

# Initialize the parser
parser = NuLogParser(log_format='<Date> <Time> <Level> <Component>: <Content>',
                     indir='path/to/log/dir',
                     outdir='path/to/output/dir')

# Parse the logs
parser.parse('your_log_file.log')