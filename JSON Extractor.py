import sys, os, json, re

inputFile = open(sys.argv[1])
pattern = re.compile(r'\{[^}]+\}')
gCounter = 0
path = os.path.join(os.getcwd(),'JSON Extractor')
os.mkdir(path)

def fn1(inputFile):
  obj = ''
  flag = False
  counter = 0
  global gCounter
  
  for l in inputFile:
    for c in l:
      if c == "{": 
        counter += 1
        flag = True
      elif c == "}": counter -= 1
      if flag: obj += c
      if counter == 0 and flag:
        flag = False
        ft = obj.replace("'", "\"").replace(",}", "}")
        obj = ''
        if len(ft) == 2: continue
        try:
          jsonproof = json.dumps(json.loads(ft), indent=2)
          gCounter += 1
          outputFile = open(os.path.join(path, 'object_' + str(gCounter)) + '.json', 'w')
          outputFile.write(str(jsonproof))
          outputFile.close()
        except Exception as e:
          # print(e)
          # print(ft)
          if len(pattern.findall(ft)) > 1:
            fn1(ft[1:len(ft)-1])

fn1(inputFile)
inputFile.close()
print(str(gCounter) + " JSON object found!")

