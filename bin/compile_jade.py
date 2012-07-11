cd templates
for filz in $(ls *.jade)                                                                                   
do
base=$(echo $filz | sed 's/\.[^.]*$//')
pyjade -c jinja $filz $base.html
done

