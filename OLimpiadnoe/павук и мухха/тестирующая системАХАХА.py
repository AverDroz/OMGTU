#тестовая система
from павук_и_мухахахах import xd
for i in range(1, 21):
    if i < 10:
        ii = "0" + str(i)
    else:
        ii = str(i)
    put1 = f"Паук и муха\input_s1_{ii}.txt"
    put2 = f"Паук и муха\output_s1_{ii}.txt"
    

    
    #код
    result = xd(put1)
    result = f"{result:.3f}"
    #тестовая система
    output_file = open(put2, "r")
    ans = output_file.read()
    b = str(result) == ans
    print(str(ii) + ":", b, "   ", "result:", result, " ", "answer:", ans)