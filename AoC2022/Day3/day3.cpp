#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

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

int priority(char item){
    if( item >= 'a'){
        return item - 'a' + 1;
    }
    else{
        return item - 'A' + 27;
    }
}

int line_priority(std::string& line){
    auto half_size = line.size()/2;
    auto item = std::find_first_of(line.cbegin(),line.cbegin()+half_size,line.cbegin()+half_size,line.cend());
    if( item != line.cbegin() + half_size){
        return priority(*item);
    }
    return 0;
}

int line_priority3(std::string& line1, std::string& line2, std::string& line3){
    for(auto letter :line1){
        if(line2.find(letter) != std::string::npos && line3.find(letter) != std::string::npos){
            return priority(letter);
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
        for (std::string& line: lines){
            score += line_priority(line);
        }
        std::cout<<score<<std::endl;
    }
    //part2
    {
        int score = 0;
        for (int i = 0; i < lines.size()-2; i+=3){
            score += line_priority3(lines[i],lines[i+1],lines[i+2]);
        }
        std::cout<<score<<std::endl;
    }
    

    return EXIT_SUCCESS;
}