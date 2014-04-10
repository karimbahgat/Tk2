import sys
sys.path.append(r"C:\Users\BIGKIMO\Documents\GitHub\GitDoc")
import gitdoc

FILENAME = "tk2"
FOLDERPATH = r"C:\Users\BIGKIMO\Documents\GitHub\Tk2"
OUTPATH = r"C:\Users\BIGKIMO\Documents\GitHub\Tk2"
OUTNAME = "README"
EXCLUDETYPES = ["variable","module"]
EXCLUDENAMES = "izip,listzip".split(",")
gitdoc.DocumentModule(FOLDERPATH,
                  filename=FILENAME,
                  outputfolder=OUTPATH,
                  outputname=OUTNAME,
                  excludetypes=EXCLUDETYPES,
                  excludenames=EXCLUDENAMES
                  )
