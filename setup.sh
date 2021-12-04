for i in {1..25}
do
    mkdir "$i"
    mkdir "$i/1"
    mkdir "$i/2"
    touch "$i/1/main.py"
    touch "$i/2/main.py"
    touch "$i/inp"
done