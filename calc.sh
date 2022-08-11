#! /bin/bash

# taking user input
echo  "Enter first number: "
read a

# input desired operation
echo "Input operation:"
echo "1. +"
echo "2. -"
echo "3. * "
echo "4. /"
read operation

echo "Enter second number:"
read b

# our calculator
case $operation in
    1) res=$((`echo $a + $b`))
    ;;
    2) res=$((`echo $a - $b`))
    ;;
    3) res=$((`echo $a \* $b`))
    ;;
    4) res=$((`echo $a / $b`))
    ;;
esac
echo "Result: $res"
