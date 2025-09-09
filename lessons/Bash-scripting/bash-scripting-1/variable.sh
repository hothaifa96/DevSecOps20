#!/bin/bash

source ./config.env

name="hodi"
age=88
fav_food='pizza'
echo hello im $name 
echo "and my age is $age"
echo 'i love $fav_food' 

# ENV_VAR
export CAR="audi"
echo "the user on this pc is : $USER "
echo "new car alert : $CAR"

echo connecting to db : postgresql://$IP:$PORT/$db


# ----------------- exiting env

# $? - exit code
echo $?
# $0 - filename of the current script
echo $0

# $#  the number of arguments provided to the script
echo $# 

# $1,2,3,4,5,67,8 gives the argument by it order
echo $1

# $$ proccess id of the script
echo $$

# $@ list of all arguments
echo $@
