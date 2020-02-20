/*
 * indi.h
 *   created on: April 24, 2013
 * last updated: June 13, 2013
 *       author: liushujia
 */

#ifndef __INDI__
#define __INDI__

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

class TIndi{
public:
	TIndi();
	~TIndi();
	void define( int N );
	TIndi& operator = ( const TIndi& src );
	bool operator == (  const TIndi& indi2 );	// �ж���·���Ƿ���ͬ 

	int fN;						// ������Ŀ
	int** fLink;				// fLink[i][]��ʾ·����i���������ڵĳ���
	int fEvaluationValue;		// TSP·������
};

#endif
