# test_nimpy.nim - file name should match the module name you're going to import from python
import nimpy
import json

proc greet(name: string): string {.exportpy.} =
  return "Hello, " & name & "!"

#[
    nimble install nimpy
    nim c --app:lib --out:test_nimpy.so --threads:on test_nimpy
]#


proc check_py_call(): string {.exportpy.} =
  let os = pyImport("os")
  echo "Current dir is: ", os.getcwd().to(string)

# sum(range(1, 5))
  let py = pyBuiltinsModule()
  let s = py.sum(py.range(0, 5)).to(int)
  assert s == 10

  return $(s)


proc tupleDiff(a, b: tuple[x, y: int]): tuple[x, y: int] {.exportpy: "tuple_diff".} =
  result = (a.x - b.x, a.y - b.y)


proc nimOutConfig(): JsonNode {.exportpy: "nim_json".} =
  result = %* { "init" : 1.0,
                "final" : 5,
                "nested" : [1, 2, 3.5, {"InArray" : 5}],
                "dictLike" : { "Nested" : "Value" }
              }

iterator testIterator(s: string): int {.exportpy: "iter_from_nim".} =
  for i in 0 ..< s.len:
    yield i


type
  Obj = ref object of PyNimObjectExperimental
    a, b: int
    c: string

  MyRefObj = ref Obj

proc validateMyObj(o: MyRefObj): bool {.exportpy: "validate_obj".} =
  o.a == 5 and o.b == 3 and o.c == "hello"