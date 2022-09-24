import sys
from commands.aggregator import aggregator

args = sys.argv
command = args[1]

if command == "aggregator":
    aggregator()
