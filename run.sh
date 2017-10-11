echo
echo -e "\e[32mpython $1.py:\e[39m"
[ -f "$1.py" ] && python $1.py || echo "The file does not exist"
echo

echo
echo -e "\e[35mjulia $1.jl\e[39m"
[ -f "$1.jl" ] && julia $1.jl || echo "The file does not exist"

echo

echo
echo -e "\e[34mgo build $1.go\e[39m"
go clean
[ -f "$1.go" ] && go build $1.go || echo "The file does not exist"
[ -f "./$1" ] && ./$1 || echo "No compiled file"
echo

echo
echo -e "\e[33mg++ $1.cpp\e[39m"
[ -f "$1.cpp" ] && g++ $1.cpp || echo "The file does not exist"
[ -f "./a.out" ] && ./a.out || echo "No compiled file"
echo


