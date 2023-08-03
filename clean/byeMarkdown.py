############byeMarkdown.py##################
# got frustrated because I couldn't find clean uncommented versions of kaggle notebooks
# so here's quick and simple function to take out all cells with markdown in it
# works because every cell with markdown has "cell_type": "markdown", 
# and seperator between cells is the same "},\n  {".
########       usage        ##############
# put the function in the same folder where yourFile.ipynb is
# just type >byeMarkdown("yourFile.ipynb")
# and you'll get new file clean_yourFile.ipynb with no markdown!

def byeMarkdown(filename="file.ipynb"):
    with open(filename, "r") as file
        tekstas = file.read()
    splyte = tekstas.split("},\n  {")
    BigDaddy = splyte[0]
    for n in splyte[1:]:
        if n.find("markdown") == -1:
            BigDaddy += "},\n  {"+n
    with open("clean_"+filename, "w") as nfile
        nfile.write(BigDaddy)
    print("done... :)")
