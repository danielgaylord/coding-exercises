while read string
do
    echo "$string" | cut -d " " -f 1-3
done