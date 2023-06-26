import os
import strutils
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
    echo "Usage: test_args -start=06Jun2023 -end=07Jun2023"
    quit(1)
  
  let arg1 = args[0]
  let arg2 = args[1]

  var start = "0"
  var arg_end = "0"

  for arg in args:
    var arg_val: string = ""
    echo arg

    if arg.contains("="):
      arg_val = arg1.split("=")[1]
      echo arg_val

    if arg.contains("-start"):
      echo "argument start is ", arg_val
      start = arg_val

    if arg.contains("-end"):
      echo "argument end is ", arg_val
      arg_end = arg_val

  
  # Process the arguments
  echo "Argument 1: ", arg1
  echo "Argument 2: ", arg2

  echo "\n"
  echo "starting with: ", start
  echo "ending with: ", arg_end

main()
