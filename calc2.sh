#! /bin/bash
while true
do

  echo  "Enter first number: "
  read a
  echo "Enter second number: "
  read b

  echo "Input operation:"
  echo "1. +"
  echo "2. -"
  echo "3. * "
  echo "4. /"
  echo "5. Exit:)"
  echo "6. Read file from inputed path"
  echo "7. CURLing request"

  read operation

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
    5) exit 0
    ;;
    6)echo "Input path to file: "
      read path
      cd $path
      echo "Input file for reading: "
      read file_name
      cat $file_name
    ;;
    7) echo "Input your link: "
       read link
       curl $link >> result.txt
  esac


  echo "Result: $res"
done
