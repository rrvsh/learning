print("Hello, world!")

local num = 38
local s = "not other"
while num < 50 do
  num = num + 1
  if num > 40 then
    print("over 40")
  elseif s ~= "other" then
    print("not over 40")
    -- s = "other"
  else
    local line = io.read()
    print("hello " .. line)
  end
end

print("")

local function fib(n)
  if n < 2 then return 1 end
  return fib(n-1) + fib(n-2)
end

print("Fibonacci Sequence 0 <= n <= 10")
local n = 0
while n <= 10 do
  print(fib(n))
  n = n + 1
end

print("")


print("Closures:")
local function adder(x)
  return function(y) return x + y end
end
local a = adder(10) -- a becomes a function
print(a(5))
local b = a
print(b(10))
