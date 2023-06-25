import os
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
    echo "Usage: myprogram <arg1> <arg2>"
    quit(1)
  
  # Accessing individual arguments
  let arg1 = args[0]
  let arg2 = args[1]
  
  # Process the arguments
  echo "Argument 1: ", arg1
  echo "Argument 2: ", arg2

main()
