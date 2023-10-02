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

int round(const std::string& line){
    char leftPart = line[0];
    char rightPart = line[2];
    if(leftPart == 'A'){
        if(rightPart == 'X'){
            return 4;
        }
        else if(rightPart == 'Y'){
            return 8;
        }
        else if(rightPart == 'Z'){
            return 3;
        }
    }
    if(leftPart == 'B'){
        if(rightPart == 'X'){
            return 1;
        }
        else if(rightPart == 'Y'){
            return 5;
        }
        else if(rightPart == 'Z'){
            return 9;
        }
    }
    if(leftPart == 'C'){
        if(rightPart == 'X'){
            return 7;
        }
        else if(rightPart == 'Y'){
            return 2;
        }
        else if(rightPart == 'Z'){
            return 6;
        }
    }
    return 0;
}

int roundPart2(const std::string& line){
    char leftPart = line[0];
    char rightPart = line[2];
    if(leftPart == 'A'){
        if(rightPart == 'X'){
            return 3;
        }
        else if(rightPart == 'Y'){
            return 4;
        }
        else if(rightPart == 'Z'){
            return 8;
        }
    }
    if(leftPart == 'B'){
        if(rightPart == 'X'){
            return 1;
        }
        else if(rightPart == 'Y'){
            return 5;
        }
        else if(rightPart == 'Z'){
            return 9;
        }
    }
    if(leftPart == 'C'){
        if(rightPart == 'X'){
            return 2;
        }
        else if(rightPart == 'Y'){
            return 6;
        }
        else if(rightPart == 'Z'){
            return 7;
        }
    }
    return 0;
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

    {
        int score = 0;
        for (const std::string& line: lines){
            score += round(line);
        }
        std::cout<<score<<std::endl;
    }
    //part2
    {
        int score = 0;
        for (const std::string& line: lines){
            score += roundPart2(line);
        }
        std::cout<<score<<std::endl;
    }
    

    return EXIT_SUCCESS;
}