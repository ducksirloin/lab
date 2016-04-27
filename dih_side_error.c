#include<stdio.h>
#include<math.h>

double error(double *x){
	double sum,a,n,dif;
	int i;
	sum = 0.0;
	for(i = 0;i < 20;i++){
		sum += x[i];
	}
	a = sum / 20.0;

	n = 0.0;
	for(i = 0;i < 20;i++){
		n += pow(x[i] - a,2);
	}

	dif = n / 19.0;
	return sqrt(dif);
}

main(){
	FILE *fp;
	char *fname = "dih_side.txt";
	double n[10000],s[10000];
	double sum_syn,sum_anti;
	double sam_syn,sam_anti;
	double ave_syn,ave_anti;
	double x[50],y[50];
	int i,j,p;

	fp = fopen(fname,"r");
	if(fp == NULL){
		printf("%sファイルが開けません。\n",fname);
		return -1;
	}

	i = 0;
	while((fscanf(fp,"%lf %lf",&n[i],&s[i])) != EOF){
		i++;
	}
	fclose(fp);

	sum_syn = 0;
	sum_anti = 0;
	j = 0;
	p = 0;
	for(i = 0;i < 20;i++){
		sam_syn = 0;
		sam_anti = 0;
		for(;j < p + 500;j++){
			if(-90.00 < s[j] && s[j] < 90.00){
				sam_syn++;
			}else{
				sam_anti++;
			}
		}
		sum_syn += sam_syn;
		sum_anti += sam_anti;
		x[i] = sam_syn / 500.0;
		y[i] = sam_anti / 500.0;
		printf("x[%d] = %lf y[%d] = %lf\n",i,x[i],i,y[i]);
		p = j;
	}

	ave_syn = sum_syn / 10000.0;
	ave_anti = sum_anti / 10000.0;

	printf("ave_syn = %lf +-%lf\nave_anti= %lf +-%lf\n",ave_syn,error(x),ave_anti,error(y));

	return 0;
}
