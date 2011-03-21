#!/bin/bash
# argouml2xmi.sh
# Creates a .xmi file from an ArgoUML-generated .uml file.
# Usage: ./argouml2xmi.sh filename.uml
# A file called filename.xmi will be created.

if [ ! -n "$1" ]
then
  echo "Usage: `basename $0` input_file"
  exit
fi

XMI_FILE=`echo $1 | sed 's/\.uml/\.xmi/'`
echo '<?xml version = "1.0" encoding = "UTF-8" ?>' > $XMI_FILE
sed -n '/<XMI*/,/<\/XMI>/p' $1 >> $XMI_FILE
