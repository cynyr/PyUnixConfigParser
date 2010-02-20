#!/usr/bin/env python
from __future__ import print_function
from __future__ import with_statement

import re

def parse_file(file, dict={}):
    """parse_file(file, dict={})

    parse_file() takes a file to parse and a seed dictionary. If the dict is 
    present it will add the options found in file to dict. This allows simple
    merging of files. The intent is that this is then used with
    optparse.Values(dict) to handle merging config files with command line
    options.

    """
    try:
        f = open(file)
    except IOError:
        return dict
    else:
        lines = f.readlines()
        vlines =[]
        for line in lines:
            if not re.match(r"^\s*$",line) and not re.match(r"^#.*$",line):
                vlines.append(line.strip('\n'))
        lines = []
        while len(vlines) >0:
            i = vlines.pop(0)
            i =re.sub(r"\s*#.*$","",i)
            while i.endswith('\\'):
                try:
                    o = vlines.pop(0)
                except IndexError:
                    o = ""
                i = i.rstrip('\\') + o.strip()
            lines.append(i)

        for opt in lines:
            [name,val] = opt.split("=",1)
            dict[name] = val.strip('"')
    
    return dict

    #for file in file_list:
    #    default_dict=_parse_file(file,default_dict)
    #parser = OptionParser(option_list=option_list)
    #parser.set_defaults(default_dict)
    #(options,args) = parser.parse_args(args)
    #return options


if __name__ =="__main__":
    import sys
    print(parse_file(sys.argv[1]))
