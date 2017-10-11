echo "python $1.py:"
[ -f "$1.py" ] && python $1.py || echo "The file does not exist"
echo

echo
echo "julia $1.jl"
[ -f "$1.jl" ] && julia $1.jl || echo "The file does not exist"

echo

echo
echo "go build $1.go"
[ -f "$1.go" ] && go build $1.go || echo "The file does not exist"
[ -f "./$1" ] && ./$1 || echo "No compiled file"
echo

echo
echo "g++ $1.cpp"
[ -f "$1.cpp" ] && g++ $1.cpp || echo "The file does not exist"
[ -f "./a.out" ] && ./a.out || echo "No compiled file"
echo


