let name = readLine(stdin)
if name == "":
  echo "Poor soul, you lost your name?"
elif name == "name":
  echo "Very funny, your name is name."
else:
  echo "Hi, ", name, "!"

# run using nim c -r test_stdin.nim
# `nim js -r test_stdin.nim` fails :: JS crosspile attempt does not have 'stdin'