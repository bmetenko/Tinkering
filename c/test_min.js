/* Generated by the Nim Compiler v1.6.8 */
var framePtr = null;
var excHandler = 0;
var lastJSError = null;
if (!Math.trunc) {
  Math.trunc = function(v) {
    v = +v;
    if (!isFinite(v)) return v;
    return (v - v % 1) || (v < 0 ? -0 : v === 0 ? v : 0);
  };
}

var F = {procname: "module test_min", prev: framePtr, filename: "/Users/bohdanmetenko/Code/Tinkering/c/test_min.nim", line: 0};
framePtr = F;
framePtr = F.prev;
var F = {procname: "module test_min", prev: framePtr, filename: "/Users/bohdanmetenko/Code/Tinkering/c/test_min.nim", line: 0};
framePtr = F;
framePtr = F.prev;
