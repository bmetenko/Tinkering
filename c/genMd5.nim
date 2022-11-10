import os
import std/parseopt



proc main = 
    echo "Name: ", getAppFilename().extractFilename()
    echo "Params: ", paramCount()

    for paramVal in 1..paramCount():
        echo "param ", paramVal, ": ", paramStr(paramVal)

    echo ""

    var argIdx : int

    for kind, key, value in getOpt():
        case kind
        of cmdArgument:
            echo "Arg", argIdx, ": \"", key, "\""

        of cmdLongOption, cmdShortOption:
            case key
            of "v", "n", "z", "w":
                echo "Got a \"", key, "\" option with value: \"", value, "\""
            else:
                echo "Unknown option: ", key

        of cmdEnd:
            discard

main()