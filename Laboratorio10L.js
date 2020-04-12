int Main()
{
    int numero =0;
    int contador =0;

printf("ungrse un numero\n");
scanf("%d" ,&numero);

for(int i=1;i<numero;i++)
{

if( numero % 1 == 0 )

contador = contador + i;
}

if(contador == numero)
printf("si es perfecto");
else
printf("no es perfecto");

return 0;
}