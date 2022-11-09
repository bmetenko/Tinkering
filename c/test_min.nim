proc intAdd*(a: int, b: int): int {.discardable.} =
    return a + b

# run with `num js -r test-min.nim`
# Lots of shims included for safety and memory 
# allocation in resulting js