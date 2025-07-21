import easyocr
reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory



result = reader.readtext('screenshot.jpg')
# print(result)
for _ in range(len(result)):
    for x in result[_]:
        # print(x)
        # print(type(x))
        if type(x) == str:
            print(x)
    # print(result[_])
    # print(type(result[_])) #tuple

    #NOTE!!!!!!
    #when installing packages with pip
    #instead of git bash
    #use command prompt 
    # bottom right of vscode, the downward arrow next to +
    # type:
    #.venv/Scipts/activate
    #then it should come up with prefix (.venv)
