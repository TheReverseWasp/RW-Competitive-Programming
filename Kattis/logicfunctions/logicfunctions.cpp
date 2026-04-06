#include "logicfunctions.h"

// Compute xor
void exclusive(bool x, bool y, bool& ans){
  ans = (x^y);
}

// Compute implication
void implies(bool x, bool y, bool& ans){
  ans = (!x||y);
}

// Compute equivalence
void equivalence(bool x, bool y, bool& ans){
  bool temp_1, temp_2;
  implies(x, y, temp_1);
  implies(y, x, temp_2);
  ans = temp_1 & temp_2;
}
