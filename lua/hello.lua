print("Hello, world!")

local num = 38
local s = "not other"
while num < 50 do
  num = num + 1
  if num > 40 then
    print("over 40")
  elseif s ~= "other" then
    print("not over 40")
    s = "other"
  else
    local line = io.read()
    print("hello " .. line)
  end
end
