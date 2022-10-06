folder=$1
if [[ -e $folder ]]
then
>result.txt
  for file in $(find $folder -name "*txt"); do grep -i -l  "«In vino veritas!»" $file>> result.txt && echo -en '\n'>>result.txt 
done 
else
  echo "Даной папки не существует"
fi

