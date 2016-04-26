#include<stdio.h>

main(){
	FILE *fp;
	char *fname = "dih_side.txt";
	double n[10000],s[10000];
	double sum_syn,sum_anti;
	double ave_syn,ave_anti;
	int i;

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

	for(i = 0;i < 10000;i++){
		if(-90.00 < s[i] && s[i] < 90.00){
			sum_syn++;
		}else if(-180.00 < s[i] && s[i] < -90.00){
			sum_anti++;
		}else if(90.00 < s[i] && s[i] < 180.00){
			sum_anti++;
		}
	}

	ave_syn = sum_syn / 10000.00;
	ave_anti = sum_anti / 10000.00;

	printf("ave_syn = %lf\nave_anti = %lf\n",ave_syn,ave_anti);

	return 0;
}
