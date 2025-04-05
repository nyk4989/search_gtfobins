import requests
import sys

args = sys.argv
with open(sys.argv[1]) as f:
    extracted_strings = []
    #for line in f.split('\n'):
    for line in f:
        elements = line.split()
        if len(elements) >= 9:
            extracted_string = ' '.join(elements[8:9])  # 8番目のスペースから9番目のスペースの直前までを抽出
            extracted_strings.append(extracted_string)

result = '\n'.join(extracted_strings)
result2 = '\n'.join(line.split('/')[-1] for line in result.split('\n') if line.strip())
print("===成形したリスト===\n")
print(f"{result2}\n===")

for command in result2.split('\n'):
    command = command.replace("\n", "")
    gtfobins = r"https://gtfobins.github.io/gtfobins/"+ command + '/'
    print(f"{gtfobins}")
    rq = requests.get(gtfobins)
    print(f"{rq.status_code}\n===")
