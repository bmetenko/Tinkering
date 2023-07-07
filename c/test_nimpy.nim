# test_nimpy.nim - file name should match the module name you're going to import from python
import nimpy

proc greet(name: string): string {.exportpy.} =
  return "Hello, " & name & "!"

#[
    nimble install nimpy
    nim c --app:lib --out:test_nimpy.so --threads:on test_nimpy
]#
