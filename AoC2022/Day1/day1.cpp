#include <iostream>
#include <fstream>
#include <string>
#include <vector>

bool readFile(const std::string& fileName, std::vector<std::string>& lines){
    std::ifstream myfile (fileName);
    std::string line;
    if (myfile.is_open()){
        while (getline(myfile,line)){
            lines.push_back(line);
        }
        myfile.close();
        return true;
    }
    else{
        std::cout << "error while opening";
        return false;
    }
}

int main(int argc, char* argv[]) {
    std::vector<std::string> lines{};
    if (argc == 2){
        if (!readFile(argv[1], lines)){
            return EXIT_FAILURE;
        }
    }
    else {
        std::cout << "Wrong numbers of arguments\n";
        return EXIT_FAILURE;
    }
    lines.push_back(std::string());
    //part 1
    {
        int max = 0;
        int sum = 0;
        for (const std::string& line: lines){
            if (line.empty()) {
                if (sum > max) {
                    max = sum;
                }
                sum = 0;
            } else {
                sum += std::stoi(line);
            }
        }

        std::cout<<max<<"\n";
    }    
    //part 2
    {
        int max1 = 0;
        int max2 = 0;
        int max3 = 0;
        int sum = 0;
        for (const std::string& line: lines){
             if (line.empty()) {
                if (sum > max1) {
                    max3 = max2;
                    max2 = max1;
                    max1 = sum;
                } else if (sum > max2){
                    max3 = max2;
                    max2 = sum;
                } else if (sum > max3){
                    max3 = sum;
                }
                sum = 0;
             } else {
                sum += std::stoi(line);
            }
        }
        std::cout<<max1+max2+max3<<"\n";
    }

    return EXIT_SUCCESS;
}