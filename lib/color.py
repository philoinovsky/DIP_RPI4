class Base:
    # Foreground:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    # Formatting
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'    
    # End colored text
    END = '\033[0m'
    NC ='\x1b[0m' # No Color

type2color = dict({
    "info": Base.OKGREEN + "[+]" + Base.END,
    "warning": Base.WARNING + "[!]" + Base.END,
    "fail": Base.FAIL + "[x]" + Base.END
})

def console(outtype,values):
    if type2color.get(outtype):
        print(type2color[outtype],values)
    else:
        raise("console output error: no such outtype")