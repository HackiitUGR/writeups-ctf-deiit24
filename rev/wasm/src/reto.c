#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const char *FAKE_PASSWORD = "SuperSecurePassword\n";

int check_password(char *input) {
  int password_size = strlen(FAKE_PASSWORD);
  for (int i = 0; i < password_size - 1; i++) {
    input[i] -= 1;
  }
  //contraseña="TvqfsTfdvsfQbttxpse";
  return strncmp(input, FAKE_PASSWORD, password_size) == 0;
}

void print_flag() {
  char *a = "DSRHHS^BSE";
  char *b = "wasi";
  char *c = "1s";
  char *d = "fun";
  int len_a = strlen(a);
  for (int i = 0; i < len_a; i++) {
    a[i] += 1;
  }
  printf("%s{%s_%s_%s}\n", a, b, c, d);
}

int main() {
  char input[30] = {0};
  puts("Introduce la contraseña:");
  fgets(input, 30, stdin);
  if (check_password(input)) {
    print_flag();
  } else {
    puts("Contraseña incorrecta");
  }
}