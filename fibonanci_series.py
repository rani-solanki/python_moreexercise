# def fib(n):    # write Fibonacci series up to n
#      """Print a Fibonacci series up to n."""
#      a, b = 0, 1
#      while a < n:
#          print(a, end=' ')
#          a, b = b, a+b
#      print()
# Now call the function we just defined:
# fib(20)
def function(n):
    a,b=0,1
    while(a<20):
        print(a)
        a,b = b,a+b
    print( )
user=int(input("enter the number:"))
function ( user )