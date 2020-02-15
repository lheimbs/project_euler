#include<iostream>
#include<vector>
#include<cmath>


bool is_prime(int x) {
    if (x <= 1)
        return false;
    else if (x <= 3)
        return true;
    else if (x % 2 == 0 || x % 3 == 0)
        return false;
    else {
        for (int i = 5; i < (int)sqrt(x); i+=6) {
            if ((x % i == 0) || (x % i + 2 == 0))
                return false;
        }
        /*int i = 5;
        while (i  * i < x) {
            if (x % i == 0 || x % i + 2 == 0)
                return false;
            i = i + 6;
        }*/
    }
    return true;
}


std::vector<int> prime_factors(int x) {
    std::vector<int> res;
    while ( x % 2 == 0) {
        res.push_back(2);
        x /= 2;
    }
    
    for (int i = 3; i <= sqrt(x); i += 2) {
        while (x % i == 0) {
            res.push_back(i);
            x /= i;
        }
    }

    /*for (int i = 1; i < x / 2; i++) {
        if (x % i == 0 && is_prime(i)) 
            res.push_back(i);
    }*/
    return res;
}

int main() {
    std::vector<int> res = prime_factors(13195); //600851475143
    int max = 0, current = 0;
    for (auto i = res.begin();i != res.end(); ++i) {
        std::cout << *i << " ";
    }
}
