/*
 * evaluator.h
 *   created on: April 24, 2013
 * last updated: June 13, 2013
 *       author: liushujia
 */

#ifndef __EVALUATOR__
#define __EVALUATOR__

#ifndef __INDI__
#include "indi.h"
#endif

#include <string.h>
#include <assert.h>

class TEvaluator{
public:
	TEvaluator();
	~TEvaluator();
	void setInstance( char filename[] );		// ���ñ���
	void doIt( TIndi& indi );					// ����indi.fEvaluationValue
	void writeTo( FILE* fp, TIndi& indi );		// ���TSP·��
	bool checkValid( int* array, int value );	// ���TSP·���Ϸ��� 

	int fNearNumMax;	// ���ڵ���Ŀ�����ֵ
	int **fNearCity;	// NearCity[i][k]��ʾ����i����ĵ�k������
	int **fEdgeDis;		// EdgeDis[i][j]��ʾ����i��j�ľ���
	int Ncity;			// ������Ŀ
	double *x;			// x[i]��ʾ��i�����е�x����
	double *y;			// y[i]��ʾ��i�����е�y����
	int *Array;			// ���Ž�Ľڵ���
};

#endif
