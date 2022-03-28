while read string
do
    echo $string | head -c 3 | tail -c 1
    echo
done