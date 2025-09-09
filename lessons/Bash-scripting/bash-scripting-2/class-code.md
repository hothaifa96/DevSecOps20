=== ./if.sh ===
#!/bin/bash
=== ./if3.sh ===
#!/bin/bash

i=1

while [[ $i -le 10 ]];do
	if [ $(( i%2 )) -eq 1 ];then
		echo odd
	fi
	if [ $i -eq 5 ];then
		 exit 99
	 fi
	echo "this is the end ::: $i"
	(( i+=1 ))

done
=== ./demos/demo1.sh ===
#!/bin/bash

echo "hello $USER"
echo 'this pc path is $PATH'

name=haim
job="DevOps Eng"

echo "hey : $name "


=== ./demos/demo2.sh ===
#!/bin/bash

echo "you asksed to run $0"

echo -e "please enter the file that you want to create:"
read filename

./create_script.sh "$filename.sh"
=== ./demos/demo3.sh ===
#!/bin/bash

# create a bash script that asks the user to enter
# path for  dirc and you must show the content of it

echo -e "etnetr the path that you wnat to explore :"
read path_to_explore

ls -al $path_to_explore
=== ./create_script.sh ===
#!/bin/bash

# how to use ./create_bash.sh {{file name}}
# output > file {{filename}} created

shbang="#!/bin/bash"

echo "welcom to Or script generator"

echo "you asked to create $1"

touch $1

echo "$shbang" > $1

chmod u+x $1

figlet $1 created
=== ./if2.sh ===
#!/bin/bash

## ask the user to give you a filename with extention
# print if the file exists or not

echo -e "enter the file name"
read file

if [ -e $file ]; then
	echo "exists already "
else
	./create_script.sh $file
fi


=== ./if.sh ===
#!/bin/bash

=== ./if3.sh ===
#!/bin/bash

i=1

while [[ $i -le 10 ]];do
	if [ $(( i%2 )) -eq 1 ];then
		echo odd
	fi
	if [ $i -eq 5 ];then
		 exit 99
	 fi
	echo "this is the end ::: $i"
	(( i+=1 ))

done

=== ./demos/demo1.sh ===
#!/bin/bash

echo "hello $USER"
echo 'this pc path is $PATH'

name=haim
job="DevOps Eng"

echo "hey : $name "



=== ./demos/demo2.sh ===
#!/bin/bash

echo "you asksed to run $0"

echo -e "please enter the file that you want to create:"
read filename

./create_script.sh "$filename.sh"

=== ./demos/demo3.sh ===
#!/bin/bash

# create a bash script that asks the user to enter
# path for  dirc and you must show the content of it

echo -e "etnetr the path that you wnat to explore :"
read path_to_explore

ls -al $path_to_explore

=== ./create_script.sh ===
#!/bin/bash

# how to use ./create_bash.sh {{file name}}
# output > file {{filename}} created

shbang="#!/bin/bash"

echo "welcom to Or script generator"

echo "you asked to create $1"

touch $1

echo "$shbang" > $1

chmod u+x $1

figlet $1 created
