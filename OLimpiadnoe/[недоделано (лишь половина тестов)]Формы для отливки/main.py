#тестовая система
from ff15 import xd
for i in range(1,14):
  put1 = f"f15/input{i}.txt"
  put2 = f"f15/output{i}.txt"
  
  output_file = open(put2, "r")
  answer = output_file.read()
  answer = set(answer.split("\n"))
  try:
    result = set(xd(put1))
  except Exception as e:
    print(f"{i}: Произошла ошибка: {e}")
    print()
    continue
  b = result == answer

  lenn = 39
  print(f"{i}: {b}   result: {str(result)[:lenn] + '...' if len(str(result)) > lenn else result}  answer: {str(answer)[:lenn] + '...' if len(str(answer)) > lenn else answer}")
  print()
