#!/usr/bin/env bash

# for f in *.zip
# do
#     dirname=$(basename $f)
#     dname=`echo $dirname | cut -d '.' -f 1`-`echo $dirname | cut -d '.' -f 2`
#     unzip -t $f answers.c &> /dev/null
#     if [ $? -ne 0 ]
#     then
# 	unzip -t $f tp-entrenaiment/answers.c &> /dev/null
# 	if [ $? -ne 0 ]
# 	then
# 	    echo "Could not find answers.c in $f"
# 	else
# 	    mkdir -p $dname
# 	    unzip -p $f tp-entrenaiment/answers.c > $dname/answers.c
# 	    rm $f
# 	fi
#     else
# 	    mkdir -p $dname
# 	    unzip -p $f answers.c > $dname/answers.c
# 	    rm $f
#     fi
# done

for f in *.tar.gz
do
    dirname=$(basename $f)
    dname=`echo $dirname | cut -d '.' -f 1`-`echo $dirname | cut -d '.' -f 2`
    tar -xf $f answers.c &> /dev/null
    if [ $? -ne 0 ]
    then
	echo "Could not find answers.c in $f"
    else
	mkdir -p $dname
	tar xf $f answers.c &> /dev/null
	mv answers.c $dname
	rm $f
    fi
done
