import sys
sys.path.append(r"C:\Users\BIGKIMO\Documents\GitHub\GitDoc")
import gitdoc

FILENAME = "tk2"
FOLDERPATH = r"C:\Users\BIGKIMO\Dropbox\Work\Research\Software\Various Python Libraries\Tk2"
OUTPATH = r"C:\Users\BIGKIMO\Dropbox\Work\Research\Software\Various Python Libraries\Tk2"
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
