#include <windows.h>
#include <stdio.h>
//#include <unistd.h>

void f(int n)
{
  printf ("Number: %d\n", n);
}

int main(int argc, char * argv[])
{
  int i = 0;
  printf ("f() is at %p\n", f);
  while (1)
  {
    f (i++);
    //睡眠2秒再输出
    Sleep (2000);
  }
}
