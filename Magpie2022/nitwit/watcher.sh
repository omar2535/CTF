inotifywait -m /tmp -e create -e moved_to |
    while read dir action file; do
        # echo "The file '$file' appeared in directory '$dir' via '$action'"
        cp -r $file/ .
        # do something with the file
    done