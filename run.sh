echo
echo -e "\033[32mpython $1.py:\033[39m"
[ -f "$1.py" ] && python $1.py || echo "The file does not exist"
echo

echo
echo -e "\033[35mjulia $1.jl\033[39m"
[ -f "$1.jl" ] && julia $1.jl || echo "The file does not exist"

echo

echo
echo -e "\033[34mgo build $1.go\033[39m"
go clean
[ -f "$1.go" ] && go run $1.go || echo "The file does not exist"
## [ -f "$1.go" ] && go build $1.go || echo "The file does not exist"
## [ -f "./$1" ] && ./$1 || echo "No compiled file"
echo

echo
echo -e "\033[33mclang++ $1.cpp\033[39m"
/bin/rm a.out 2> /dev/null 
##[ -f "$1.cpp" ] && xcrun clang++ -std=c++11 -stdlib=libc++ -Weverything $1.cpp || echo "The file does not exist"
[ -f "$1.cpp" ] && xcrun clang++ -std=c++11 -stdlib=libc++ $1.cpp $2 || echo "The file does not exist"
[ -f "./a.out" ] && ./a.out || echo "No compiled file"
echo



