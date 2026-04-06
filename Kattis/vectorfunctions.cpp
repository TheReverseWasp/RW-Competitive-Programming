#include "vectorfunctions.h"

void backwards(std::vector<int>& vec){
    std::vector<int> ans;
    for(int i = vec.size()-1; i >= 0; i--){
        ans.push_back(vec[i]);
    }
    vec = ans;
}

std::vector<int> everyOther(const std::vector<int>& vec){
    std::vector<int> ans;
    for(int i = 0; i < vec.size(); i+=2){
        ans.push_back(vec[i]);
    }
    return ans;
}

int smallest(const std::vector<int>& vec){
    int smallest = vec[0];
    for(int i = 1; i < vec.size(); i++){
        if(vec[i] < smallest){
            smallest = vec[i];
        }
    }
    return smallest;
}

int sum(const std::vector<int>& vec){
    int sum = vec[0];
    for (int i = 1; i < vec.size(); i++)
    {
        sum += vec[i];
    }
    return sum;
    
}

int veryOdd(const std::vector<int>& suchVector){
    int numodds = 0;
    for(int i = 0; i<suchVector.size(); i++){
        if(suchVector[i] % 2 == 1 and i % 2 == 1){
            numodds++;
        }
    }
    return numodds;
}