import os
import std/parseopt
import md5



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
            of "string", "s":
                echo key, " ", value
                echo getMD5(value)
                if value == "abc":
                    assert $toMD5("abc") == "900150983cd24fb0d6963f7d28e17f72"
            else:
                echo "Unknown option: ", key

        of cmdEnd:
            discard

main()