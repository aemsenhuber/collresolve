/**
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * MATLAB Coder version            : 3.4
 * C/C++ source code generated on  : 25-Apr-2019 09:54:28
 *
 * @file
 */

#ifndef COLLISION_CLASSIFIER_H
#define COLLISION_CLASSIFIER_H

/* Include Files */
#include <math.h>
#include <stddef.h>
#include <stdlib.h>
#include <string.h>
#include "rt_nonfinite.h"
#include "rtwtypes.h"
#include "collision_classifier_types.h"

/* Function Declarations */
extern void collision_classifier(const double X[4], int* label, double score[3]);

#endif