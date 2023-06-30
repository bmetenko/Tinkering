import os
import strutils
import std/times
# import argparse

# let p = newParser("example"):
#   help("A demonstration of this library in a program named {prog}")

#   option("-c", "--config", help="Configuration file")

#[
    Simpler Approach first
    #[
        Nested Comments are interesting.

        #[
            How far can this go?
        ]#
    ]#
]#

proc main() =
  let args = commandLineParams()
  
  # Check the number of arguments
  if args.len < 2:
    echo "Usage: test_args -start=06Jun2023 -end=07Jun2023 -format=ddMMMyyyy"
    quit(1)
  
  let arg1 = args[0]
  let arg2 = args[1]

  var start = "0"
  var arg_end = "0"
  var date_format = "ddMMMyyyy"

  var arg_val: string = ""

  for arg in args:
    echo arg

    if arg.contains("="):
      arg_val = arg.split("=")[1]
      echo arg_val

      if arg.contains("-start"):
        echo "argument start is ", arg_val
        start = arg_val

      if arg.contains("-end"):
        echo "argument end is ", arg_val
        arg_end = arg_val

      if arg.contains("-format"):
        echo "argument format is ", arg_val
        date_format = arg_val

    arg_val = ""

  let day_start = parse(start, date_format)
  let day_end = parse(arg_end, date_format)

  echo day_start.format("yyyy-MM-dd")
  echo day_end.format("yyyy-MM-dd")

  
  # Process the arguments
  echo "Argument 1: ", arg1
  echo "Argument 2: ", arg2

  echo "\n"
  echo "starting with: ", start, ", ", day_start.weekday
  echo "ending with: ", arg_end, ", ", day_end.weekday

  let between_dates = (day_end - day_start)

  type 
    DateRange = object
      rangeStart: DateTime
      rangeEnd: DateTime

  # List-like iterator
  iterator items(range: DateRange): DateTime =
    var i = range.rangeStart
    while i <= range.rangeEnd:
      yield i
      i = i + initDuration(days = 1)

  # Enumerate-Like iterator
  # Uses values from items function as enumerated indeces though,
  # simplifying this to integer values might be better... 
  iterator pairs(range: DateRange): tuple[a: DateTime, b: string] =
    for i in range:  # uses CustomRange.items
      yield (i, i.format("yyyy-MM-dd"))

  # Example: enumarate-like
  for i, c in DateRange(rangeStart: day_start, rangeEnd: day_end):
    echo i, " - ", c

  # Example: list-like
  for j in DateRange(rangeStart: day_start, rangeEnd: day_end):
    echo " - ", j
  
  echo "between these is: ", between_dates.inDays, " days"
  echo "which is also: ", between_dates.inHours, " hours"

main()
