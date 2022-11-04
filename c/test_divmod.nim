proc divmod(a, b: int; res, remainder: var int) =
  res = a div b        # integer division
  remainder = a mod b  # integer modulo operation

var
  x, y: int
divmod(8, 5, x, y) # modifies x and y
echo x
echo y

# run with `num js -r test-divmod.nim`
# Lots of shims included for safety and memory 
# allocation in resulting js
# echo procedures seem to be only executed at compile time.